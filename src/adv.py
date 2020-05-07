import textwrap
from room import Room
from player import Player
from item import Item
from utility import clear_terminal

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons."),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),

    'kitchen': Room("Kitchen", """You've walked into a kitchen! You are hungry, 
but the disarming stench of rotting flesh indicates that you would not find 
anything fit for eating in this room.  Shadows scurry back and forth beneath 
sagging shelves and from inside broken cabinets.  You hope these are only 
rats, but you have a feeling the room may house more than simple pests.""")
}

# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

room['kitchen'].e_to = room['foyer']
room['foyer'].w_to = room['kitchen']

# create player
player = Player('Guile', room['outside'], 'badass knife')

# add items to rooms
# room['outside'].items = ['rocks', 'bushes']
# room['foyer'].items = ['brass knuckles', 'torch']

# clear terminal as game starts
clear_terminal()

done = False

# helper function to skip input that we don't understand or cannot act upon
def skip_input():
    print('Invalid command, please try again.\n')

def help_text():
    print("""
    Valid commands:
        -[n]: move north
        -[s]: move south
        -[e]: move east
        -[w]: move west
        -[q]: quit
        -[help]: help text
        """)

# welcome message
def get_welcome_message():
    welcome_message = (f'  Guile\'s Adventure of Punching and Patriotism  \nWelcome to the game, {player.name}! You currently have a {player.inventory} to help you along the way!  Your location is: {player.room}.  {player.room.description}')
    print(welcome_message)

get_welcome_message()

# Main
#

while not done:
    # for line in textwrap.wrap(player.room.print_description()):
    #     print(line)
    #     print('\n')

    command = input('What would you like to do?')

    if len(command) > 2 or len(command) < 1:
        skip_input()
        continue

    if command in ['n', 's', 'e', 'w']:
        player.room = player.move_to(command, player.room)
        print(f'You move to: {player.room}')
        continue

    if command in ['q', 'quit', 'exit']:
        done = True

    if command in ['?', 'help']:
        help_text()
        continue
    
    else:
        skip_input()
        continue

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

# Day 1 MVP: 
# Allow player to move room to room in the 4 cardinal directions
# Create player and room classes in their respective files

# Day 2 MVP: 
# Add ability for rooms to hold multiple items
# Add ability for player to hold multiple items
# Add items to the game that the player can carry around and use
# Add get [ITEM_NAME] and drop [ITEM_NAME] commands to the parser, which will allow the player to get and drop items.  Upon dropping, we should update location information for the item in case the player wants to return and pick it up again.

# Add functionality for other 2-word commands, such as 'take coins' or 'drop sword'.