# This File holds all of our logger formatting and then our logger object itself and output handlers.
import logging as logg
import sys 

 
logger = logg.getLogger(__name__)
formatter_file = logg.Formatter('[%(asctime)s] {%(levelname)s} %(name)s: #%(lineno)d - \n%(message)s')
formatter_stream = logg.Formatter('{%(levelname)s} - %(message)s')
file_handler = logg.FileHandler('monster.log')
stream_handler = logg.StreamHandler(sys.stdout)
logger.addHandler(file_handler)
logger.addHandler(stream_handler)
file_handler.setFormatter(formatter_file)
stream_handler.setFormatter(formatter_stream)
logger.setLevel(10)
