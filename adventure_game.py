import time
import random
import sys


def print_pause(pause):
    print(pause)
    time.sleep(1.5)
 

def intro():
    print_pause("Welcome to Direction Adventure Game!")
    print_pause("You are currently on the surface of panet earth right \n"
                "on the Equator in central African Continent.")


def random_destination():
    return random.choice([' home', ' work', ' vacation home'])


def press_One(items):
    print_pause("You chose to go East")
    print_pause("You chose wisely")
    print_pause(f"You are one step closer to {random_destination()}")
    if '1' in items:
        print_pause("You already selected East, choose a different direction")
        if '3' in items:
            print_pause("I am sorry, you're lost in the wilderness. :(")
            play_again(items)
    else:
        print_pause(f"Choose this next direction wisely to reach {random_destination()}")
        items.append('1')
    directions(items)


def press_Two(items):
    print_pause("You chose to go South")
    print_pause("You chose wisely")
    print_pause(f"You are one step closer to your {random_destination()}")
    if '2' in items:
        print_pause("You already selected South, choose a different direction")
        if '4' in items:
            print_pause(f"Congradulations! You have reached your                {random_destination()} safely")
            play_again(items)
    else:
        print_pause(f"Choose this next direction wisely to reach {random_destination()}")
        items.append('2')
    directions(items)


def press_Three(items):
    print_pause("You chose to go West")
    print_pause("You chose wisely")
    print_pause(f"You are one step closer to your {random_destination()}")
    if '3' in items:
        print_pause("You already selected West, choose a different direction")
        if '1' in items:
            print_pause("I am sorry, you're lost in the wilderness. :(")
            play_again(items)
    else:
        print_pause(f"Choose this next direction wisely to reach {random_destination()}")
        items.append('3')
    directions(items)


def press_Four(items):
    print_pause("You chose to go North")
    print_pause("You chose wisely")
    print_pause(f"You are one step closer to your {random_destination()}")
    if '4' in items:
        print_pause("You already selected North, choose a different direction")
        if '2' in items:
            print_pause(f"Congradulations! You have reached your                {random_destination()} safely")
            play_again(items)
    else:
        print_pause(f"Choose this next direction wisely to reach{random_destination()}")
        items.append('4')
    directions(items)


def directions(items):
    print_pause(f"There are four directions you can take to reach your{random_destination()}\n")
    print_pause("Press 1 for East\n"
                "Press 2 for South\n" "Press 3 for West \n"
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


def play_again(items):
    chosen_Option = input("Do you want to play again (y/n)?\n")
    if 'y' in chosen_Option:
        play_Direction_Game()
    elif 'n' in chosen_Option:
        print_pause("Thank you for playing! Bye")
        sys.exit()
    else:
        print_pause("This is an invalid input.")
        play_again(items)


def play_Direction_Game():
    items = []
    intro()
    directions(items)


play_Direction_Game()
