from datetime import datetime

"""
Utils for views.py
"""

def group_auctions_by_current_complete_remaining(chit_batches):
	"""
	To group auctions by today's auctions, the rest of the
	months and the completed auction of the respective month
	"""
	today = datetime.now()
	today_date = today.date()
	time_now = today.time()

	auctions = {}
	auctions['today'] = []
	auctions['remaining'] = []
	auctions['completed'] = []

	for cb in chit_batches:

		if cb.next_auction == today_date and cb.start_time > time_now:
			auctions['today'].append(cb)
		elif cb.next_auction > today_date:
			auctions['remaining'].append(cb)
		else:
			auctions['completed'].append(cb)

	return auctions