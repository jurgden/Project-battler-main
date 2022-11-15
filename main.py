import logging as logg
import sys 
import random as rnd

logger = logg.getLogger(__name__)
formatter = logg.Formatter('[%(asctime)s] {%(levelname)s} %(name)s: #%(lineno)d - %(message)s')
stream_handler = logg.StreamHandler(sys.stdout)
file_handler = logg.FileHandler('monster.log')
logger.addHandler(stream_handler)
logger.addHandler(file_handler)
stream_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)
logger.setLevel(10)

def equation(a, b, c):
  obj = (a * a) + (b * b) / c
  return logger.info(obj)

  



equation(1, 3, 2)