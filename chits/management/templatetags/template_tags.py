from django import template

from management.dbapi import get_bid_record_by_id_and_bid_date

"""
To create template tags
"""

register = template.Library()

@register.filter(name='get_commission')
def get_commmission(chit):
	"""
	To return chit commission
	"""
	return chit.get_commission()


@register.filter(name='get_auction_amt')
def get_auction_amt(chit):
	"""
	to return the amount left for auction
	"""
	return chit.get_auction_amt()