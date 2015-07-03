from django.db.models import CharField, IntegerField, Model, \
    DateTimeField, ImageField, ForeignKey, TimeField, SmallIntegerField, \
    BooleanField, ManyToManyField

from base.models import ChitUser

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

def create_member(user, firstname, lastname, address, phone_number,
    photo=None):

    username = firstname+'_'+lastname
    member = Member(user=user, firstname=firstname, lastname=lastname,
            username=username, address=address,phone_number=phone_number,
            photo=photo)
    member.save()
    return member


class ChitBatch(Model):
    """
    Description of all the chit batches
    """
    user = ForeignKey(ChitUser, related_name='chit_batches')
    name = CharField(max_length=25, unique=True, blank=False)
    members = ManyToManyField(Member)
    principal = IntegerField(blank=False)
    emi = IntegerField(blank=False)
    period = SmallIntegerField(blank=False)
    dues = SmallIntegerField(blank=False)
    start_date = DateTimeField(blank=False)
    start_time = TimeField(blank=False)
    state = BooleanField(default=True)
    end_date = TimeField(blank=True, null=True)
    created_on = DateTimeField(auto_now_add=True)


class BidRecord(Model):
    """
    Monthly details of all Chit batch's bid's
    """
    chitbatch = ForeignKey(ChitBatch, related_name='records')
    bidder = ForeignKey(Member, related_name='bidders')
    bid_date = DateTimeField(blank=False)
    bid_amount = IntegerField(blank=False)
    balance = IntegerField(blank=False)
