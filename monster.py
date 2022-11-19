# This File will contain all Monster Class methods, information and properties. 

class Monster():
  def __init__(self, name, HP, ATK, DEF, SPD, is_ko=False):
    self.name = name
    self.HP = HP
    self.ATK = ATK
    self.DEF = DEF
    self.SPD = SPD
    self.is_ko = is_ko

# Lets keep our instantiated monsters together in this file so that it will be simply accessible and more easily imported to our other files.
pikachu = Monster('pika', 30, 50, 200, 1000) 
togepi = Monster('dildo', 20, 100, 200, 1000)
diglet = Monster('plug', 10, 200, 200, 1000)

# THIS IS AN ACCESSIBLE LIST OF ALL OUR CURRENTLY INSTANTIATED MONSTERS.
pokemon_list = [pikachu, togepi, diglet]