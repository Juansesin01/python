#Pre start
import re
import cmd
import textwrap
import sys
import time
import os
import random


#Define things

screen_width = 100


#Define PLayer

class player:
    def __init__ (self):
        self.name = ''
        self.hp = 0
        self.xp = 0
        self.status = []
        self.location = 'a1'

player1 = player()

#Title Screen setup

def pre_start():
   os.system('clear')
   print("################################")
   print("#########   -WELCOME-   ########")
   print("##-To this rpg text adventure-##")
   print("################################")
   print("################################")
   print("##########   -PLAY-   ##########")
   print("########## -OPTIONS-  ##########")
   print("##########   -QUIT-   ##########")
   print("################################")

   title_screen_select()

#Title Screen interactivity

def title_screen_select():
    option = input("> ")
    if option.lower() == ("play"):
        start()
    elif option.lower() == ("options"):
        help_screen()
    elif option.lower() == ("quit"):
        sys.exit
    while option.lower() not in ["play", "help", "quit"]:
      print("Enter a valid command")
      option = input("> ")
      if option.lower() == ("play"):
        start()
      elif option.lower() == ("options"):
        help_screen()
      elif option.lower() == ("quit"):
        sys.exit
        exit
        



#help Screen

   
def help_screen():
   os.system('clear')
   print("################################")
   print("#########   -OPTIONS-   ########")
   print("###-TYPE THE OPTION DESIRED- ###")
   print("################################")
   print("################################")
   print("#########  -CONTROLS- ##########")
   print("############  -MAP- #############")
   print("##########   -MENU-   ##########")
   print("################################")
   help_screen_select()
   
#help interactivity

def help_screen_select():
    option = input("> ")
    if option.lower() == ("controls"):
        controls_help_screen()
    elif option.lower() == ("map"):
        maping()
    elif option.lower() == ("menu"):
          start()
          
    while option.lower() not in ["controls", "map", "a2"]:
      print("Enter a valid command")
      option = input("> ")
      if option.lower() == ("controls"):
        controls_help_screen()
      elif option.lower() == ("map"):
        maping()
      elif option.lower() == ("menu"):
          start()

#control Screen

def controls_help_screen():
   os.system('clear')
   print("################################")
   print("#########  -CONTROLS-   ########")
   print("################################")
   print("################################")
   print("################################")
   print("##            -MAP-           ##")
   print("##     -UNDER DEVELOPMENT-    ##")
   print("##########   -MENU-   ##########")
   print("################################")
   controls_screen_select()       

#control Screen interactivity

def controls_screen_select():
    option = input("> ")
    if option.lower() == ("controls"):
        controls_help_screen()
    elif option.lower() == ("map"):
        maping()
    elif option.lower() == ("menu"):
          start()
          
    while option.lower() not in ["controls", "map", "a2"]:
      print("Enter a valid command")
      option = input("> ")
      if option.lower() == ("controls"):
        controls_help_screen()
      elif option.lower() == ("map"):
          maping()
      elif option.lower() == ("menu"):
          start()



def start():
  pre_start()

  #map

NAME = ""
DESCRIPTION = 'description'
ABOUT =  'about'
SOLVED = 'solved'

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

places = {
   'a1': False, 'a2': False, 'a3': False, 'a4': False, 
   'b1': False, 'b2': False, 'b3': False, 'b4': False, 
   'c1': False, 'c2': False, 'c3': False, 'c4': False, 
   'd1': False, 'd2': False, 'd3': False, 'd4': False, 
                  }


zones = {
  'a1': {
      NAME: 'Home',
      DESCRIPTION: 'Is Your House',
      ABOUT:  'Your parents raised you here',
      SOLVED: False,
      
      UP: 'The edge of the World',
      DOWN:'b1',
      LEFT: 'The edge of the World',
      RIGHT:'a2',
   },
          
  'a2': {
      NAME: 'Horsefield',
      DESCRIPTION: 'A field with white horses',
      ABOUT:  'It appears some time ago, many strong and brave warriors dominated this land,\n and after war decided to rely on their 4 Legged fellas, providing shelter and resources for them,\n then the warriors died of a cruel flu and the horses survived, a fine lineage of 2 meter horses lays around here all day\n don´t mess with them or they´ll charge at you',
      SOLVED: False,
      
      UP: 'The edge of the World',
      DOWN:'b2',
      LEFT: 'a1',
      RIGHT:'a3',
   },
  'a3': {
      NAME: 'the ladder to abyss',
      DESCRIPTION: 'A giant abyss with an alleged ladder',
      ABOUT:  'The abyss is scary, not many desire to approach\n this abyss has been object to many myths, the most famous one is about a ladder carrying bottom,\n many say it guides straight to hell, some others suggest said ladder ends fairly quick and you can´t go back, \n I prefer not to believe anything in particular',
      SOLVED: False,
      
      UP: 'The edge of the World',
      DOWN:'b3',
      LEFT: 'a2',
      RIGHT:'a4',
   },
  'a4': {
      NAME: 'pond under the tree',
      DESCRIPTION: 'a regular pond under a giant tree',
      ABOUT:  'The tree is estimated to have at least 400 years, but no one cares much',
      SOLVED: False,
      
      UP: 'The edge of the World',
      DOWN:'b3',
      LEFT: 'a2',
      RIGHT:'The edge of the World',
   },
  'b1': {
      NAME: '',
      DESCRIPTION: 'description',
      ABOUT:  'about',
      SOLVED: False,
      
      UP: 'a1',
      DOWN:'c1',
      LEFT: 'The edge of the World',
      RIGHT:'b2',
   },
  'b2': {
      NAME: '',
      DESCRIPTION: 'description',
      ABOUT:  'about',
      SOLVED: False,
      
      UP: 'a2',
      DOWN:'c2',
      LEFT: 'b1',
      RIGHT:'b3',
   },
  'b3': {
      NAME: '',
      DESCRIPTION: 'description',
      ABOUT:  'about',
      SOLVED: False,
      
      UP: 'a3',
      DOWN:'c3',
      LEFT: 'b2',
      RIGHT:'b4',
   },
  'b4': {
      NAME: '',
      DESCRIPTION: 'description',
      ABOUT:  'about',
      SOLVED: False,
      
      UP: 'a4',
      DOWN:'c4',
      LEFT: 'b3',
      RIGHT:'The edge of the World',
   },
  'c1': {
      NAME: '',
      DESCRIPTION: 'description',
      ABOUT:  'about',
      SOLVED: False,
      
      UP: 'b1',
      DOWN:'d1',
      LEFT: 'The edge of the World',
      RIGHT:'c2',
   },

  'c2': {
      NAME: '',
      DESCRIPTION: 'description',
      ABOUT:  'about',
      SOLVED: False,
      
      UP: 'b2',
      DOWN:'d2',
      LEFT: 'c1',
      RIGHT:'c3',
   },        
  'c3': {
      NAME: '',
      DESCRIPTION: 'description',
      ABOUT:  'about',
      SOLVED: False,
      
      UP: 'b3',
      DOWN:'d3',
      LEFT: 'c2',
      RIGHT:'c4',
   },
  'c4': {
      NAME: '',
      DESCRIPTION: 'description',
      ABOUT:  'about',
      SOLVED: False,
      
      UP: 'b4',
      DOWN:'d4',
      LEFT: 'c3',
      RIGHT:'The edge of the World',
   },
  'd1': {
      NAME: '',
      DESCRIPTION: 'description',
      ABOUT:  'about',
      SOLVED: False,
      
      UP: 'c1',
      DOWN:'The edge of the World',
      LEFT: 'The edge of the World',
      RIGHT:'d2',
   },

  'd2': {
      NAME: '',
      DESCRIPTION: 'description',
      ABOUT:  'about',
      SOLVED: False,
      
      UP: 'c2',
      DOWN:'The edge of the World',
      LEFT: 'd1',
      RIGHT:'d3',
   },        
  'd3': {
      NAME: '',
      DESCRIPTION: 'description',
      ABOUT:  'about',
      SOLVED: False,
      
      UP: 'c3',
      DOWN:'The edge of the World',
      LEFT: 'd2',
      RIGHT:'d4',
   },
  'd4': {
      NAME: '',
      DESCRIPTION: 'description',
      ABOUT:  'about',
      SOLVED: False,
      
      UP: 'c4',
      DOWN:'The edge of the World',
      LEFT: 'd3',
      RIGHT:'The edge of the World',
   }
}



  
def maping():
    print("___________________________________________________ ")
    print("|",zones['a1'][NAME].center(10),"|""|""|""|")
    print("|""|""|""|""|")
    print("|__________|""__________|""__________|""___________|")
    print("|""|""|""|""|")
    print("|""|""|""|""|")
    print("|__________|""__________|""__________|""___________|")
    print("|""|""|""|""|")
    print("|""|""|""|""|")
    print("|__________|""__________|""__________|""___________|")
    print("|""|""|""|""|")
    print("|""|""|""|""|")
    print("|__________|""__________|""__________|""___________|")
    print('                        THE WORLD')
    print('                     You are in ' + zones[player1.location][NAME].upper())

maping()

start()
        
        
