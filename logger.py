import logging as logg


# Below is our logger
logger = logg.getLogger(__name__)
formatter_file = logg.Formatter('[%(asctime)s] {%(levelname)s} %(name)s: #%(lineno)d - %(message)s')
formatter_stream = logg.Formatter('{%(levelname)s} - %(message)s')
file_handler = logg.FileHandler('monster.log')
logger.addHandler(file_handler)
file_handler.setFormatter(formatter_file)
logger.setLevel(10)
