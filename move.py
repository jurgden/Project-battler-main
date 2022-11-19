# This File will contain all Move Class related methods, information and properties.


class Move():
  def __init__(self, name, POW,type):
    self.name = name
    self.POW = POW
    self.type = type 

  
# This is where we will instantiate our moves and then below we will keep all of our updated and most relevant moves in an accessible list. 
slap = Move('Slap', 5, 'Normal')
shock = Move('Shock', 10, 2)
# Here is our accessible list that is storing all of our instantiated moves!
moves_list = [slap, shock]