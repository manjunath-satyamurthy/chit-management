from management.models import Member, ChitBatch, PaymentRecord, \
    BidRecord


def create_member(user, firstname, lastname, address, phone_number,
    photo=None):

    username = firstname+'_'+lastname
    member = Member(user=user, firstname=firstname, lastname=lastname,
            username=username, address=address,phone_number=phone_number,
            photo=photo)
    member.save()
    return member


def get_members_by_user(user):
    """
    To return all members realated to a particular
    user
    """
    return user.members.all()


def get_chits_by_user(user):
    """
    To return all chit batches created by a particular 
    user
    """
    return user.chit_batches.all()
