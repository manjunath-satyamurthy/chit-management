from datetime import datetime
from dateutil.relativedelta import relativedelta

from django.db.models import CharField, IntegerField, Model, \
    DateTimeField, ImageField, ForeignKey, TimeField, SmallIntegerField, \
    BooleanField, ManyToManyField, DateField

from base.models import ChitUser


class PaymentRecordEnum(object):
    """
    Enum for PaymentRecord Model
    """
    UNKNOWN = -1
    UN_PAID = 0
    PAID = 1
    CHIT_BENIFIT = 2

    CHOICES = (
        (UNKNOWN, 'UNKNOWN'),
        (PAID, 'PAID'),
        (UN_PAID, 'UN_PAID'),
        (CHIT_BENIFIT, 'CHIT_BENIFIT')
    )


class Member(Model):
    """
    Members of Chits
    """
    user = ForeignKey(ChitUser, related_name='members')
    mid = IntegerField(primary_key=True)
    username = CharField(max_length=50, unique=True, blank=False)
    firstname = CharField(max_length=25)
    lastname = CharField(max_length=25)
    address = CharField(max_length=25)
    phone_number = CharField(max_length=20, unique=True)
    photo = ImageField(blank=True)
    created_on = DateTimeField(auto_now_add=True)

    def add_photo(self, photo):
        """
        To add a member's photo individually
        """
        self.photo = photo
        self.save()
        return self


class ChitBatch(Model):
    """
    Description of all the chit batches
    """
    user = ForeignKey(ChitUser, related_name='chit_batches')
    name = CharField(max_length=25, unique=True, blank=False)
    members = ManyToManyField(Member)
    no_of_members = SmallIntegerField(blank=False, default=0)
    principal = IntegerField(blank=False)
    commission_percent = IntegerField(default=3, blank=False)
    balance = IntegerField(blank=False, default=0)
    shortage = IntegerField(blank=False, default=0)
    emi = IntegerField(blank=False)
    period = SmallIntegerField(blank=False)
    dues = SmallIntegerField(blank=False)
    start_date = DateField(blank=False)
    start_time = TimeField(blank=False)
    next_auction = DateField(blank=False, null=True)
    is_multiple_auction = BooleanField(default=False)
    state = BooleanField(default=True)
    end_date = TimeField(blank=True, null=True)
    created_on = DateTimeField(auto_now_add=True)


    def get_commission(self):
        return (self.principal * self.commission_percent)/100

    def get_auction_amt(self):
        return (self.principal - self.get_commission()) + self.balance

    def get_last_auction_date(self):
        if self.next_auction != self.start_date:
            return self.next_auction-relativedelta(months=+1)

    def get_max_shortage(self, bid_amount):
        possible_balance = self.balance + bid_amount - self.get_commission()
        print possible_balance, bid_amount
        return (self.principal - bid_amount) - (possible_balance)

    def update_balance(self, bid_amt):
        self.balance = self.balance + bid_amt - self.get_commission()

    def update_payment_record(self):
        if self.next_auction:
            if not self.is_multiple_auction:
                paid = PaymentRecordEnum.UN_PAID
            else:
                paid = PaymentRecordEnum.CHIT_BENIFIT
            prs = []
            for member in self.members.all():
                prs.append(PaymentRecord(
                    chitbatch=self, member=member,
                    bid_date=self.next_auction,
                    paid=paid,
                ))
            PaymentRecord.objects.bulk_create(prs)

    def is_another_auction_possible(self, bid_amount):
        """
        To check if another auction is possible in the same month
        """
        latest_balance = self.balance + (bid_amount - self.get_commission())
        if (latest_balance - bid_amount) > (0.06*self.principal):
            return True
        return False


class PaymentRecord(Model):
    """
    To keep track of all the member's payments
    """
    chitbatch = ForeignKey(ChitBatch, related_name='payments')
    member = ForeignKey(Member, related_name='payments')
    paid = IntegerField(blank=True, null=True,
        default=PaymentRecordEnum.PAID, choices=PaymentRecordEnum.CHOICES)
    bid_date = DateField(blank=False)


class BidRecord(Model):
    """
    Monthly details of all Chit batch's bid's
    """
    chitbatch = ForeignKey(ChitBatch, related_name='records')
    bidder = ForeignKey(Member, related_name='bids')
    bid_date = DateField(blank=False)
    bid_amount = IntegerField(blank=False)
    balance = IntegerField(blank=False)
    bid_count = SmallIntegerField(default=1)
    payment_record = ManyToManyField(PaymentRecord)
    shortage = IntegerField(default=0)

    class Meta:
        get_latest_by = "bid_date"


