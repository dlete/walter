import logging

#logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)
## https://docs.python.org/3/howto/logging-cookbook.html
#logger.setLevel(logging.DEBUG)
#logger.setLevel(logging.INFO)

logger.debug('DEBUB Got a request for host2ticket with GET')
logger.info('INFO Got a request for host2ticket with GET')
logger.warning('WARNING Got a request for host2ticket with GET')
