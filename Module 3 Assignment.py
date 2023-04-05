#Welcome user
print('Welcome to Moving Between Rooms!')
print('You may use "go North, go South, go East, go West" as commands')

rooms = {
        'Great Hall': {'South': 'Bedroom'},
        'Bedroom': {'North': 'Great Hall', 'East': 'Cellar'},
        'Cellar': {'West': 'Bedroom'}
    }

current_room = 'Great Hall'
direction = 'go North', 'go South', 'go East', 'go West'

while True:
    if current_room == 'Cellar':
        print('Congratulations! You have reached the cellar and defeated the Dragon!')
        break
    # Display location
    print('You are in {}.'.format(current_room))
   
    # Get user input
    command = input('\nWhat do you do?')
    # Moving
    if command in direction:
        if command in current_room:
            current_room = rooms[current_room[command]]
        else:
            # Invalid movement
            print('You cannot go that way.')
    # Quit game
    elif command == 'quit':
        print('Thanks for playing!')
        break
    # Invalid input
    else:
        print('Invalid input')