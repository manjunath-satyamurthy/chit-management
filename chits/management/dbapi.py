from management.models import Member, ChitBatch, PaymentRecord, \
    BidRecord


def get_members_by_user(user):
    """
    To return all members realated to a particular
    user
    """
    return user.members.all()


def get_live_chit_batches(user):
    """
    To return all the chit batches created by a 
    particular user
    """
    return user.chit_batches.filter(state=True).all()


def get_payment_records_by_chitbatch_id(id):
    """
    To return payment records of a particular chit batch
    """
    return PaymentRecord.objects.filter(chitbatch_id=id).all()


def get_chits_by_user(user):
    """
    To return all chit batches created by a particular 
    user
    """
    return user.chit_batches.all()


def get_members_by_ids(mids):
    """
    get members by a list of ids
    """
    return Member.objects.filter(mid__in=mids).all()


def get_chitbatch_by_id(id):
    """
    To return ChitBatch by id
    """
    return ChitBatch.objects.get(pk=id)


def is_chit_name_existing(name):
    chit = ChitBatch.objects.filter(name=name).count()
    if not chit:
        return False
    return True


def create_member(user, firstname, lastname, address, phone_number,
    photo=None):

    username = firstname+'_'+lastname
    member = Member(user=user, firstname=firstname, lastname=lastname,
            username=username, address=address,phone_number=phone_number,
            photo=photo)
    member.save()
    return member


def create_chit_batch(user, name, principal, period, no_of_members,
    start_date, start_time, members):
    emi = principal/period
    chitbatch = ChitBatch(user=user, name=name, principal=principal, period=period,
        no_of_members=no_of_members, start_date=start_date, emi=emi, dues=period,
        start_time=start_time, next_auction=start_date)
    chitbatch.save()

    for member in members:
        chitbatch.members.add(member)
        
    chitbatch.update_payment_record()

    return chitbatch