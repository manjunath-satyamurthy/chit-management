from django.db.models import CharField, IntegerField, Model, \
    DateTimeField, ImageField, ForeignKey, TimeField, SmallIntegerField, \
    BooleanField, ManyToManyField, DateField

from base.models import ChitUser


class PaymentRecordEnum(object):
    """
    Enum for PaymentRecord Model
    """
    UNKNOWN = -1
    PAID = 1
    UN_PAID = 0

    CHOICES = (
        (UNKNOWN, 'UNKNOWN'),
        (PAID, 'PAID'),
        (UN_PAID, 'UN_PAID'),
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
    emi = IntegerField(blank=False)
    period = SmallIntegerField(blank=False)
    dues = SmallIntegerField(blank=False)
    start_date = DateField(blank=False)
    start_time = TimeField(blank=False)
    next_auction = DateField(blank=False, null=True)
    state = BooleanField(default=True)
    end_date = TimeField(blank=True, null=True)
    created_on = DateTimeField(auto_now_add=True)

    def update_payment_record(self):
        if self.next_auction:
            prs = []
            for member in self.members.all():
                prs.append(PaymentRecord(
                    chitbatch=self, member=member,
                    paid=PaymentRecordEnum.UN_PAID,
                    bid_date=self.next_auction
                ))
            PaymentRecord.objects.bulk_create(prs)


class PaymentRecord(Model):
    """
    To keep track of all the member's payments
    """
    chitbatch = ForeignKey(ChitBatch, related_name='payments')
    member = ForeignKey(Member, related_name='payments')
    paid = IntegerField(blank=True, null=True,
        default=PaymentRecordEnum.PAID, choices=PaymentRecordEnum.CHOICES)
    bid_date = DateTimeField(blank=False)


class BidRecord(Model):
    """
    Monthly details of all Chit batch's bid's
    """
    chitbatch = ForeignKey(ChitBatch, related_name='records')
    bidder = ForeignKey(Member, related_name='bidders')
    bid_date = DateTimeField(blank=False)
    bid_amount = IntegerField(blank=False)
    balance = IntegerField(blank=False)
    payment_record = ManyToManyField(PaymentRecord)
