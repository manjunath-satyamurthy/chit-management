from django import template

from management.dbapi import get_bid_record_by_id_and_bid_date, \
	get_latest_bid, get_first_bid_from_bidrecord

"""
To create template tags
"""

register = template.Library()

@register.filter(name='get_commission')
def get_commission(chit):
	"""
	To return chit commission
	"""
	return chit.get_commission()


@register.filter(name='get_auction_amt')
def get_auction_amt(chit):
	"""
	to return the amount left for auction
	"""
	return chit.get_auction_amt


@register.filter(name='get_bidderprice')
def get_bidderprice(chit):
	"""
	TO return the money bidder gets after auction
	"""
	latest_bid = get_latest_bid(chit)
	return chit.principal - latest_bid.bid_amount


@register.filter(name='get_bidder')
def get_bidder(chit):
	"""
	To return the latest bidder
	"""
	return get_latest_bid(chit).bidder.username


@register.filter(name='get_max_shortage')
def get_max_shortage(chit):
	"""
	To return max possible get_max_shortage
	"""
	latest_bid = get_latest_bid(chit)
	return chit.get_max_shortage(latest_bid.bid_amount)


@register.filter(name='get_min_bid')
def get_min_bid(chit):
	"""
	To return the minimum amount to bid 
	"""
	return get_first_bid_from_bidrecord(chit).bid_amount

@register.filter(name='get_min_bid_for_multiple_auction')
def get_min_bid_for_multiple_auction(chit):
	"""
	To return the minimum amount tp bid in 
	a multiple auction
	"""
	return get_latest_bid(chit).bid_amount