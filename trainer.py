# This File will contain all Trainer class methods , information and properties.
from logger import logger

 

class Trainer():
  def __init__(self, name, *mons):
    self.name = name
    self.mons = mons


  def battle(self, enemy):
    logger.info(f'{self.name} is in battle against {enemy.name}!')
    mon_selec = input(f'Which on would you like to use? {self.mons}')
    logger.info(f"You chose {mon_selec}!")
    logger.info(f'Your {mon_selec} has a HP of ')







# Instansiating or Trainer Class
trainerX = Trainer('James', 'pikachu', 'machamp')
trainerY = Trainer('Carluna', 'wigglytuff', 'charmander')
trainerX.battle(trainerY)