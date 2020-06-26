""" import logging

# Create a custom logger
logger = logging.getLogger(__name__)

# Create handlers
c_handler = logging.StreamHandler()
f_handler = logging.FileHandler('file.log')
c_handler.setLevel(logging.WARNING)
f_handler.setLevel(logging.ERROR)

# Create formatters and add it to handlers
c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
formatter = logging.Formatter('[%(asctime)s] p%(process)s {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s','%m-%d %H:%M:%S')

c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

# Add handlers to the logger
logger.addHandler(c_handler)
logger.addHandler(f_handler)

logger.warning('This is a warning')
logger.error('This is an error')
logger.info('This is an error') """

import logging
import logstash
import sys
import os
from logging.handlers import RotatingFileHandler

class OneLineExceptionFormatter(logging.Formatter):
    def formatException(self, exc_info):
        result = super().formatException(exc_info)
        return repr(result)
 
    def format(self, record):
        result = super().format(record)
        result = result.replace("\n", "\\n")
        # if record.exc_text:
        #     result = result.replace("\n", "")
        return result


logger = logging.getLogger('app')
logger.setLevel(logging.DEBUG)
handler = RotatingFileHandler('app.log', maxBytes=512*1024*1024, backupCount=2)
# formatter = logging.Formatter('[%(asctime)s] [p%(process)s] [%(funcName)s] [%(pathname)s:%(lineno)d] [%(levelname)s] - %(message)s','%m-%d %H:%M:%S')
formatter = OneLineExceptionFormatter('[%(asctime)s] [p%(process)s] [%(funcName)s] [%(pathname)s:%(lineno)d] [%(levelname)s] - %(message)s','%m-%d %H:%M:%S')

handler.setFormatter(formatter)
logger.addHandler(handler)
# logger.warning('This is a warning')
# logger.error('This is an error')
logger.info('This is an info\n\n aaaaaaaaaaaa')
def trace_log():
    import traceback
    just_the_string = traceback.format_exc().replace('\n','!!').replace('\r', '!!!')
    logger.error(just_the_string)
def test():
    # logger.info('This is an info test')
    a = 5
    b = 0
    try:
        c = a / b
    except Exception as e:
        # logging.exception("Exception occurred")
        logger.exception(e)
        # logger.exception(str(e))
        # logger.critical(e, exc_info=True)
        # import traceback
        trace_log()

test()