# This File will contain all Move methods, information and properties. 

class Monster():
  def __init__(self, name, HP, ATK, DEF, SPD, is_ko=False):
    self.name = name
    self.HP = HP
    self.ATK = ATK
    self.DEF = DEF
    self.SPD = SPD
    self.is_ko = is_ko
