#
#IT-140

#Show instructions to user
def show_instructions():
    print('--------------')
    print("Shipwrecked!")
    print("You are shipwrecked on a deserted island, but you have found a hidden door, leading to a hidden stronghold. Collect all of the items from the dungeon, but be wary, you are not alone...")
    print("You may move North, East, West and South with 'go -direction-.' Use 'get: item name' to collect an item!")
    print("Good luck, and watch out for the Sleepless Captain...")
    print('--------------')

#Define rooms and movement
rooms = {
    'The Dark Room': {
        'name': 'The Dark Room',
        'commands': {
            'go North': 'Midday Room',
            'go East': 'Sunrise Room',
            'go South': 'Midnight Room',
            'go West': 'Sunset Room',
        },
        'item': 'Torch',
        },
    'Midday Room': {
        'name': 'Midday Room',
        'commands': {
            'go North': 'Aviary',
            'go South': 'The Dark Room',
        },
        'item': 'Incredibly Fancy Hat',
    },
    'Sunrise Room': {
        'name': 'Sunrise Room',
        'commands': {
            'go West': 'The Dark Room',
        },
        'item': 'Flintlock',
    },
    'Midnight Room': {
        'name': 'Midnight Room',
        'commands': {
            'go North': 'The Dark Room',
            'go West': 'The Crypt',
        },
        'item': 'Mediocre Hat',
    },
    'Sunset Room': {
        'name': 'Sunset Room',
        'commands': {
            'go East': 'The Dark Room',
        },
        'item': 'Cutlass',
    },
    'The Crypt': {
        'name': 'The Crypt',
        'commands': {
            'go East': 'Midnight Room'
        },
        'item': 'The Unsleeping Captain',
    },
    'Aviary': {
        'name': 'Aviary',
        'commands': {
            'go South': 'Midday Room',
            'go East': 'Watchtower',
        },
        'item': 'nothing',
    },
    'Watchtower': {
        'name': 'Watchtower',
        'commands': {
            'go West': 'Aviary',
        },
        'item': 'Grog Bottle',
    },
}

inventory_items = []

current_room_name = rooms

# Make the available directions
directions = ['go North',
              'go South',
              'go East',
              'go West']

# Start game here!
current_room_name = 'The Dark Room'

show_instructions()

#Show user their status
def user_status():
    print('You are in {}'.format(current_room_name)),
    print('In this room there is a {}'.format(rooms[current_room_name]['item']))
#    print(rooms['text']),
    print('Inventory:'), inventory_items
def get_item(rooms):
    inventory_items = {
        'The Dark Room': 'Torch',
        'Midday Room': 'Incredibly Fancy Hat',
        'Sunrise Rooom': 'Flintlock',
        'Midnight Room': 'Mediocre Hat',
        'Sunset Room': 'Cutlass',
        'Aviary': 'none',
        'Watchtower': 'Grog Bottle',
    }
    return inventory_items[rooms]

# Gameplay Loop
while True:
    user_status()
    current_room_info = rooms[current_room_name]

    if current_room_name == 'Watchtower':
        print('You have made it to the Watchtower!')
        break
    if current_room_name == 'The Crypt':
        print('The Sleepless Captain claims another victim. Try again!')
        break

    # Get user input
    command = input('\nWhat direction will you proceed?')

    # Movement
    if command in directions:
        if command in current_room_info['commands']:
            current_room_name = current_room_info['commands'][command]
        else:
            # Invalid move
            print('You cannot go that way.')
    #Acquiring items was something I could absolutely not figure out.

    # Exiting game
    elif command == 'Quit':
        print('Thanks for playing!')
        break
    # Invalid command
    else:
        print('Invalid input, please try again.')