"""
:Required packages
    gsutil
"""

import os, sys
import datetime
from utilities import settings
import logging

_init = settings.__init__()

def get_tif(year):
    _location = 'gs://%s/%s/%d'%(_init.EXPORT_BUCKET, _init.EXPORT_BUCKET_PATH, year)
    _tif = 'gsutil ls -d %s/*/alert%s_*' % (_location, str(year)[-2:])
    return os.popen(_tif).read().split()

def get_date(year):
    _location = 'gs://%s/%s/%d'%(_init.EXPORT_BUCKET, _init.EXPORT_BUCKET_PATH, year)
    _date = 'gsutil ls %s' % (_location)
    logging.info('number of dates: ', len(os.popen(_date).read().split()))


def download2dir(path):
    logging.info("===== Getting available datasets for the year =====")
    year = _init.YEARS[1]

    files = get_tif(int(year))
    now = datetime.datetime.now()
    if not year: year = str(now.year)
    if not os.path.isdir('./data/'): os.mkdir('./data/')

