from boto.s3.key import Key
from datetime import datetime
from dateutil.relativedelta import relativedelta
from weasyprint import HTML, CSS

from django.template.loader import render_to_string
from management.dbapi import restore_auction_to_nextmonth, \
    get_chitbatch_by_id

from chits.settings import bucket

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

def generate_report_to_s3(chit_id):
    """
    To generate_report and save it in Amazon S3
    """
    k = Key(bucket)
    chit = get_chitbatch_by_id(chit_id)
    k.key = str(chit.id)+'.pdf'
    html = render_to_string('report.html', {'chit':chit})
    report = HTML(string=html).write_pdf()
    k.set_contents_from_string(report)

def generate_report_locally(chit_id):
    """
    To generate report and save it locally
    """
    html = render_to_string('report.html', {'chit':chit})
    report = HTML(string=html).write_pdf('static/media/report')