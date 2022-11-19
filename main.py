# This file will constitute our runtime enviroment. All of our variable and program structure will be put together and then run through this file. 
# import random
from monster import pokemon_list
from move import moves_list



# Here is an experimental for loop which tests the output of all our currently instantiated moves which have been updated to our 'moves_list'
for self in moves_list:
  print(vars(self))
# print(vars(pikachu))


# Here is another experimental for loop which formats and returns all the properties and info of each item in our currently most updated 'pokemon_list'
for i in pokemon_list:
  print((f'My name is {i.name}. Here are my stats!\nHP: {i.HP}\nATK: {i.ATK}\nDEF: {i.DEF}\nSPD: {i.SPD}\nKnocked?: {i.is_ko}')) # <-- Just like this homie :)

