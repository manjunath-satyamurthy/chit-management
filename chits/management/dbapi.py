import time, datetime
from dateutil.relativedelta import *
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


def get_payment_records_by_chitbatch_id_date(id, bid_date):
    """
    To return payment records of a particular chit batch
    """
    return PaymentRecord.objects.filter(chitbatch_id=id, bid_date=bid_date).all()


def get_chitbatch_distinct_bit_dates(chits):
    """
    To return a dict of chit to its bid_dates
    """
    chit_bid_dates = {}
    for chit in chits:
        distinct_bids = chit.payments.all().values('bid_date').distinct()
        bid_dates = [bd['bid_date'].strftime('%Y-%m-%d') for bd in distinct_bids]
        chit_bid_dates[chit.id] = bid_dates

    return chit_bid_dates


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


def update_payment(ids):
    """
    To update payment info by PaymentRecord list of ids
    """
    prs = PaymentRecord.objects.filter(pk__in=ids)
    for pr in prs:
        pr.paid = 1
        pr.save()
    

def get_recent_auctions():
    """
    To return ChitBatches which are +/- one current month
    """
    today = datetime.date.today()
    next_month = today+relativedelta(months=+1)
    last_month = today-relativedelta(months=+1)
    return ChitBatch.objects.filter(
        next_auction__lte=next_month, next_auction__gte=last_month).all()



def get_bid_record_by_id_and_bid_date(chit_id, bid_date):
    """
    To return BidRecord if exists
    """
    return BidRecord.objects.filter(
        chitbatch=chit_id,
        bid_date=bid_date
    )


def get_latest_bid(chit):
    """
    To return the latest BidRecord
    """
    try:
        return chit.records.latest()
    except:
        return None


def get_first_bid_from_bidrecord(chit):
    print BidRecord.objects.filter(
        chitbatch=chit.id,
        bid_date=chit.start_date
    )
    
    return BidRecord.objects.filter(
        chitbatch=chit.id,
        bid_date=chit.start_date
    )


def restore_auction_to_nextmonth(chit):
    chit.next_auction += relativedelta(months=+1)
    chit.is_multiple_auction = False
    chit.save()


def update_chit_batch(chit, bid_amt, cancel_auction=False):
    """
    To update ChitBatch after every auction
    """

    if chit.is_another_auction_possible and not cancel_auction:
        chit.is_multiple_auction = True
    else:
        next_auction = chit.next_auction+relativedelta(months=+1)
        chit.is_multiple_auction = False
        chit.next_auction = next_auction

    chit.dues = chit.dues - 1
    chit.update_balance(bid_amt)
    
    chit.save()
    chit.update_payment_record()


def update_bid_record(chit, member_id, bid_amt):
    """
    To update BidRecord after every auction
    """

    last_bid = get_latest_bid(chit)

    if chit.is_multiple_auction and last_bid:
        bid_count = last_bid.bid_count+1
    else:
        bid_count = 1
    balance = bid_amt - chit.get_commission()
    member = get_members_by_ids([member_id])[0]
    bid_record = BidRecord(chitbatch=chit, bidder=member,
        bid_date=chit.next_auction, bid_amount=bid_amt,
        balance=balance, bid_count=bid_count
    )
    bid_record.save()


    for payment in chit.payments.all():
        bid_record.payment_record.add(payment)

    return bid_record