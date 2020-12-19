def show_instructions():
    # Intro Statement
    print('------------------------')
    print('Wheel of Time Text Adventure Game\n'
          'Collect your 7 friends before running into the Dark One to win the game.\n'
          'Travel commands: go North, go South, go East, go West\n'
          'To gather friends: get "friend name"')
    print('------------------------')


# assign inventory to empty list and current room to Emond's Field
inventory = []
current_room = 'Emond\'s Field'
current_friend = ''


def show_status():
    # print the player's current status
    print('You are in', current_room)
    # print current inventory(gathered friends)
    print('Gathered Friends:', inventory)
    print('------------------------')


def show_travel(room):
    # print where the player traveled to and status
    print('You\'ve traveled to', room)
    print('Gathered Friends:', inventory)
    print('------------------------')


def main():
    # dictionary linking rooms
    rooms = {

        'Emond\'s Field': {'North': 'Saldaea', 'South': 'Caemlyn', 'East': 'Tar Valon', 'West': 'Seanchan Empire'},
        'Seanchan Empire': {'East': 'Emond\'s Field', 'friend': 'Mat'},
        'Caemlyn': {'North': 'Emond\'s Field', 'East': 'Cairhien', 'West': 'Tower of Ghenjei', 'friend': 'Elayne'},
        'Tower of Ghenjei': {'East': 'Caemlyn', 'friend': 'Moiraine'},
        'Cairhien': {'West': 'Caemlyn', 'friend': 'Thom'},
        'Tar Valon': {'North': 'Aiel Waste', 'West': 'Emond\'s Field', 'friend': 'Egwene'},
        'Aiel Waste': {'South': 'Tar Valon', 'friend': 'Aviendha'},
        'Saldaea': {'South': 'Emond\'s Field', 'East': 'Shayol Ghul', 'friend': 'Perrin'},
        'Shayol Ghul': {'West': 'Saldaea'},

    }

    # show the player the game instructions
    show_instructions()

    # show the player status
    show_status()

    # loop forever
    while True:

        # get move from player
        player_move = input('Enter a move:').split()
        print('------------------------')

        room = current_room

        # statement to allow player to exit at anytime
        if player_move[0] == 'exit':
            exit()

        # while statement if go is true
        if player_move[0] == 'go':
            # assign direction to second half of move
            direction = (player_move[1]).capitalize()

            # if statement to determine if direction is in room dictionary
            if direction in rooms[room]:
                # assign new room to value in dictionary
                room = rooms[room][(player_move[1]).capitalize()]

                # show current room & friend
                show_travel(room)
                if 'friend' in rooms[room]:
                    # print friend if not collected yet
                    inventory.append(rooms[room]['friend'])
                    print('You see', rooms[room]['friend'])
                    
                    print('------------------------')

                if room == 'Shayol Ghul':
                    # winning statement
                    if len(inventory) == 7:
                        print('You defeated the Dark One with the help of your friends!')
                        exit()

                    # losing statement
                    elif len(inventory) != 7:
                        print('You have not gathered enough friends!\n'
                              'The Dark One defeated you. Humanity is DOOMED')
                        exit()

                player_move = input('Enter a move:').split()
                print('------------------------')

            else:
                print('You cannot travel this way!')
                print('------------------------')
                player_move = input('Enter a move:').split()
                print('------------------------')

        elif player_move[0] == 'get':
            # assign item name to second half of move
            item_name = (player_move[1]).capitalize()

            # if statement to determine if item name is in room dictionary
            if item_name in rooms[room]['friend']:
                # add item name to inventory
                inventory.append(item_name)
                del rooms[room]['friend']
                print('Great! you gathered', item_name)
                print('------------------------')
                player_move = input('Enter a move:').split()
                print('------------------------')
            else:
                print('Please enter a valid command.')
                player_move = input('Enter a move:').split()
                print('------------------------')
        else:
            print('Please enter a valid command.')
            player_move = input('Enter a move:').split()
            print('------------------------')


main()
