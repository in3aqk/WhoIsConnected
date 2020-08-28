import logging
import logging.handlers
from datetime import datetime

from libs.utility import readIni
conf = readIni()

logging.getLogger(conf.get('logger','loggerName'))
cur_date = datetime.now().strftime("%Y%m%d")
logging.basicConfig(
    filename='logs/{}.log'.format(cur_date),
    level=logging.DEBUG,
    format='%(asctime)s-%(levelname)s-%(message)s')