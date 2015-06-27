from django.db.models import CharField, IntegerField, Model, \
    DateTimeField, ImageField, ForeignKey

from base.models import ChitUser

class Member(Model):
    """
    Members of Chits
    """
    uid = ForeignKey(ChitUser, related_name='members')
    mid = IntegerField(primary_key=True)
    username = CharField(max_length=50, unique=True, blank=False)
    first_name = CharField(max_length=25)
    last_name = CharField(max_length=25)
    address = CharField(max_length=25)
    phone_number = CharField(max_length=20, unique=True)
    photo = ImageField(blank=True)
    created_on = DateTimeField(auto_now_add=True)