# This file will constitute our runtime enviroment. All of our variable and program structure will be put together and then run through this file. 
# import random
# from monster import pokemon_list
# from move import moves_list
from logger import logger
from trainer import Trainer 
from monster import pokemon_names_list

program_running = True
def main():
  while program_running == True:
    # Here is an experimental for loop which tests the output of all our currently instantiated moves which have been updated to our 'moves_list'
    # for self in moves_list:
    #   print(f'{vars(self)}\n')
  
    # Here is another experimental for loop which formats and returns all the properties and info of each item in our currently most updated 'pokemon_list'
    # for i in pokemon_list:
    #   logger.info((f'My name is {i.name}.\nMy dex number is {i.id_num}\nHere are my stats!\nHP: {i.HP}\nATK: {i.ATK}\nDEF: {i.DEF}\nSPD: {i.SPD}\nKnocked?: {i.is_ko}\n'))
    print('Welcome to the wide world of Monster Battler!')
    playerX_name = input('Please enter your name: ')
    if len(playerX_name) < 1:
      print('Please enter a valid name!')
      main()
      break
    playerX_mon_one = input(f'Please select your first pokemon {pokemon_names_list}: ')
    # pokemon_names_list.pop(playerX_mon_one)
    if playerX_mon_one not in pokemon_names_list:
      print('That is not a valid monster!')
      main()
      break
    playerX_mon_two = input(f'Please select your second pokemon {pokemon_names_list}: ')
    # pokemon_names_list.pop(playerX_mon_two)
    if playerX_mon_one == playerX_mon_two: 
      print("You can't have more than 2 of the same pokemon on your team!\nTry Again..")
      main()
      break
    if playerX_mon_two not in pokemon_names_list:
      print('Please enter a valid pokemon!')
      main()
      break
    trainerX = Trainer(playerX_name, playerX_mon_one, playerX_mon_two)
    logger.info(f'Hello {trainerX.name}!\nYou have selected {trainerX.mons[0]} and {trainerX.mons[1]} as your starting monsters! ')
    # call the main menu or something to that effect


main()

    
  