import time
import random

def print_pause(pause):
    print(pause)
    time.sleep(0)

def intro():
    print_pause("Welcome to Direction Adventure Game!")
    print_pause("You are currently on the surface of panet earth right \n"  
    "on the Equator in central African Continent.")

def press_One(items):
    print_pause("You chose to go East")
    print_pause("You chose wisely")
    #if input("1") in input:
        #print_pause("You are one step closer to your home")
        #print_pause("You need to choose one more correct direction to reach your home")
        #directions()

def press_Two(items):
    print_pause("You chose to go South")
    print_pause("You chose wisely")

def press_Three(items):
    print_pause("You chose to go West")
    print_pause("You chose wisely")

def press_Four(items):
    print_pause("You chose to go North")
    print_pause("You chose wisely")

def directions(items):
    print_pause("There are four directions you can take to reach your home\n")
    print_pause("Press 1 for East\n"
        "Press 2 for South\n"
        "Press 3 for West \n"
        "Press 4 for North")
    chosen_Direction = input("Choose your direction:\n")
    if chosen_Direction == '1':
        press_One(items)
    elif chosen_Direction == '2':
        press_Two(items)
    elif chosen_Direction == '3':
        press_Three(items)
    elif chosen_Direction == '4':
        press_Four(items)
    else:
        print_pause("This is an invalid input.")
    directions(items)



def play_Direction_Game():
    items = []
    intro()
    directions(items)

play_Direction_Game()