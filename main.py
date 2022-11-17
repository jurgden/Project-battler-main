import random



moves_list = ['quick attack', 'thunderbolt', 'headbut', 'harder']
def moves(): 
  move_one = moves_list[random.randint(0, 3)]
  moves_list.pop(move_one)
  move_two = moves_list[random.randint(0, 2)]  

class Move():
  def __init__(self, name, POW,type):
    self.name = name
    self.POW = POW
    self.type = type 

class Monster():
  def __init__(self, name, HP, ATK, DEF, SPD, is_ko=False):
    self.name = name
    self.HP = HP
    self.ATK = ATK
    self.DEF = DEF
    self.SPD = SPD
    self.is_ko = is_ko

  def __iter__(self):
    return self

  def __next__(self):
    pass

  def move_slot_one(self):
    return 




Slap = Move('Slap', 5, 'Normal')
Shock = Move('Shock', 10, 2)
moves_lists = [Slap, Shock]
for self in moves_lists:
  
  print(vars(self))


pikachu = Monster('pika', 30, 50, 200, 1000) 
togepi = Monster('dildo', 20, 100, 200, 1000)
diglet = Monster('plug', 10, 200, 200, 1000)
# print(vars(pikachu))

pokemon = [pikachu, togepi, diglet]
for i in pokemon:
  print((f'My name is {i.name}. Here are my stats!\nHP: {i.HP}\nATK: {i.ATK}\nDEF: {i.DEF}\nSPD: {i.SPD}\nKnocked?: {i.is_ko}')) # <-- Just like this homie :)
    #pokemon are listed and can be called // how do we call the properties?
list(pokemon[0])

def test(x, y):
 
  if pokemon(x(2)) != pokemon(y(2)):
    print("The first one's bigger.")
  else: 
    print("The second one's bigger.")
