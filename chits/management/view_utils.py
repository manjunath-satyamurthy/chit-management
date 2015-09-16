from datetime import datetime

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
	auctions['remaining'] = []
	auctions['completed'] = []

	for cb in chit_batches:

		if cb.next_auction == today:
			auctions['today'].append(cb)
		elif cb.next_auction > today:
			auctions['remaining'].append(cb)
		else:
			auctions['completed'].append(cb)

	return auctions
