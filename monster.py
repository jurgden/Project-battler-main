# This File will contain all Monster Class methods, information and properties. 

class Monster():
  def __init__(self, name, id_num, HP, ATK, DEF, SPD, is_ko=False):
    self.name = name
    self.id_num = id_num
    self.HP = HP
    self.ATK = ATK
    self.DEF = DEF
    self.SPD = SPD
    self.is_ko = is_ko

# Lets keep our instantiated monsters together in this file so that it will be simply accessible and more easily imported to our other files.
bulbasaur = Monster('bulbasaur','#001', 45, 49, 49, 45) 
charmander = Monster('charmander', '#004', 39, 52, 43, 65)
squirtle = Monster('squirtle', '#007', 44, 48, 65, 43)


# THIS IS AN ACCESSIBLE LIST OF ALL OUR CURRENT MONSTER NAMES.
pokemon_names_list = [bulbasaur.name, charmander.name, squirtle.name]

# This is an accessible list of all of our instantiated classes. 
instantiated_mons_list = [bulbasaur, charmander, squirtle]