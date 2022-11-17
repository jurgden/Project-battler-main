import logger

class Trainer():
  def __init__(self, name, *mons):
    self.name = name
    self.mons = mons


  def battle(self, enemy):
    mon_selec = input(f'Which on would you like to use? {self.mons}')
    return logger.info(mon_selec)







# Instansiating or Trainer Class
trainerX = Trainer('James', 'Pikachu', 'Machamp')
trainerX.battle('JJ')