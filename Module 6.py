#Set up environment / rooms
rooms = {'Great Hall': {'name': 'Great Hall', 'go South': 'Bedroom',
        'text': 'You are in the Great Hall.'},
        
    'Bedroom': {'name': 'the bedroom', 'go East': 'Cellar', 'go North': 'Great Hall',
        'text': 'You are in the Bedroom.'},  
    'Cellar': {'name': 'the Cellar', 'go West': 'Bedroom',
        'text': 'You are in the Cellar.'}
    }
#Set up user input
directions = ['go North', 'go South', 'go East', 'go West']
current_room = rooms['Great Hall']
 
# game loop
while True:
    if current_room['name'] == 'the Cellar':
        print('Congratulations! You have reached the cellar and defeated the Dragon!')
        break
    # display current location
    print('You are in {}.'.format(current_room['name']))
   
    # get user input
    command = input('\nWhat do you do?')
    # movement
    if command in directions:
        if command in current_room:
            current_room = rooms[current_room[command]]
        else:
            # bad movement
            print('You cannot go that way.')
    # quit game
    elif command == 'quit':
        print('Thanks for playing!')
        break
    # bad command
    else:
        print('Invalid input')