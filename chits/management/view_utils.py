from datetime import datetime
from dateutil.relativedelta import relativedelta

from management.dbapi import restore_auction_to_nextmonth


"""
Utils for views.py
"""


def group_auctions_by_current_complete_remaining(chit_batches):
	"""
	To group auctions by today's auctions, the rest of the
	months and the completed auction of the respective month
	"""

	today = datetime.now().date()

	auctions = {}
	auctions['today'] = []
	auctions['multiple_auction'] = []
	auctions['remaining'] = []
	auctions['completed'] = []

	for cb in chit_batches:
		if cb.next_auction == today and not cb.is_multiple_auction:
			auctions['today'].append(cb)
		elif cb.is_multiple_auction:
			if cb.next_auction == today:
				auctions['multiple_auction'].append(cb)
				auctions['completed'].append(cb)
			else:
				restore_auction_to_nextmonth(cb)
		elif cb.get_last_auction_date() == today:
			auctions['completed'].append(cb)
		else:
			auctions['remaining'].append(cb)
	print auctions
	return auctions
