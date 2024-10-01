import json
#sp23-bai-054
# Define the castle map
castle_map = {
    'Entrance': {
        'description': "The castle's main entrance, a grand hallway leading into the heart of the castle.",
        'exits': {'north': 'Great Hall', 'west': 'Stables', 'east': 'Library'},
        'items': ['castle map', 'torch'],
        'locked': False
    },
    'Great Hall': {
        'description': "A grand hall for receptions and feasts, with doors leading to various parts of the castle.",
        'exits': {'south': 'Entrance', 'west': 'Pantry and Kitchen', 'east': 'Private Quarters'},
        'items': ['chandelier', 'painting of the king', 'dining table'],
        'locked': False
    },
    'Pantry and Kitchen': {
        'description': "A large kitchen for food preparation, with a connected pantry for food storage.",
        'exits': {'east': 'Great Hall', 'west': 'Defensive Areas and Armory'},
        'items': ['shelves', 'cupboards', 'pan', 'knife', 'glasses', 'jug of water', 'light pan', 'heavy pan'],
        'pantry_locked': True  # Pantry is initially locked
    },
    'Defensive Areas and Armory': {
        'description': "A room for weapon storage, connected to the defensive sections of the castle.",
        'exits': {'north': 'Pantry and Kitchen', 'east': 'Secret Chamber', 'south': 'Stables'},
        'items': ['sword', 'shield', 'armor', 'helmet'],
        'locked': False
    },
    'Stables': {
        'description': "The stables house the horses and are located towards the south of the castle.",
        'exits': {'north': 'Defensive Areas and Armory', 'east': 'Entrance'},
        'items': ['horse', 'saddle', 'bucket of water', 'haystack'],
        'locked': False
    },
    'Library': {
        'description': "A quiet space filled with books for study and knowledge.",
        'exits': {'north': 'Secret Chamber', 'west': 'Entrance'},
        'items': ['bookshelf', 'book of spells', 'ancient scroll', 'ink and quill'],
        'locked': False
    },
    'Secret Chamber': {
        'description': "A hidden room filled with treasures and ancient artifacts, accessed from the library or private quarters.",
        'exits': {'south': 'Library', 'west': 'Defensive Areas and Armory', 'north': 'Private Quarters'},
        'items': ['key', 'golden crown', 'ancient artifact', 'jewel chest'],
        'locked': True  # Initially locked
    },
    'Private Quarters': {
        'description': "The lavish quarters for the king, queen, princes, and guests.",
        'exits': {'west': 'Great Hall', 'south': 'Secret Chamber'},
        'items': ['crown', 'royal bed', 'silk curtains', 'diary of the queen'],
        'locked': False
    }
}

# Player's current status
player_inventory = []
print("START pantry and secret chamber is locked you have to unlock both to win the game")
current_room = 'Entrance'

# To track unlocking triggers
secret_chamber_unlocked = False

#sp23-bai-044
def display_room_details(room):
    """Displays the description, exits, and items in the current room."""
    print(f"\nYou are in the {room}.")
    print(castle_map[room]['description'])
    print("\nExits:", ', '.join(castle_map[room]['exits'].keys()))
    if castle_map[room]['items']:
        print("Items in this room:", ', '.join(castle_map[room]['items']))
    else:
        print("No items to see here.")
        
#sp23-bai-054
def move_to_room(direction):
    """Moves the player to a new room, if possible."""
    global current_room
    if direction in castle_map[current_room]['exits']:
        next_room = castle_map[current_room]['exits'][direction]
        
        # Unlock Secret Chamber from Private Quarters by having the diary
        if current_room == 'Private Quarters' and next_room == 'Secret Chamber':
            if 'diary of the queen' in player_inventory:
                print("The secret chamber unlocks as you move through a hidden door.")
                castle_map['Secret Chamber']['locked'] = False
            else:
                print("The Secret Chamber is locked.")
                return

        # Unlock Secret Chamber from Library by pushing the bookshelf
        if current_room == 'Library' and next_room == 'Secret Chamber':
            if 'bookshelf' in player_inventory:
                print("You push the bookshelf and reveal a hidden passage!")
                castle_map['Secret Chamber']['locked'] = False
            else:
                print("The Secret Chamber is locked.")
                return

        if castle_map[next_room].get('locked', False):
            print(f"The {next_room} is locked.")
        else:
            current_room = next_room
            display_room_details(current_room)
    else:
        print("You can't go that way.")
        
#sp23-bai-044
def look():
    print ("room:",[current_room])
    if player_inventory:
        print("inventory:",player_inventory)
        
#sp23-bai-054
def pick_up_item(item):
    """Allows the player to pick up items in the room."""
    if item in castle_map[current_room]['items']:
        player_inventory.append(item)
        castle_map[current_room]['items']
        print(f"You picked up: {item}")
        if item == 'heavy pan':
            print("You found a key hidden under the heavy pan!")
            castle_map[current_room]['items'].append('key')  # Key is now available in the room
    else:
        print(f"{item} is not here.")

#sp23-bai-044
def examine_items(item):
    """Examine a specific item in the room for clues or hidden objects."""
    if item in castle_map[current_room]['items']:
        if current_room == 'Pantry and Kitchen' and item == 'heavy pan':
            print("You examine the heavy pan and find a hidden key underneath ...pantry unlocked!")
            player_inventory.append('key')
            castle_map[current_room]['items'].remove('heavy pan')  # Remove the pan after the key is found
        
        elif current_room == 'Library' and item == 'bookshelf':
            if 'bookshelf' in player_inventory:
                print("You examine the bookshelf. It seems unusual... you push it and discover a hidden passage towards secret chamber!")
                player_inventory.append('bookshelf')
                # Unlock Secret Chamber
                castle_map['Secret Chamber']['locked'] = False
            else:
                print("The bookshelf has already been pushed aside. Nothing else here.")

 

        else:
            print(f"You examine the {item}, but nothing special is found.")

    else:
        print(f"{item} is not a key to unlock")


#sp23-bai-054
def save_game():
    """Saves the current game state to a file."""
    game_state = {
        'current_room': current_room,
        'inventory': player_inventory,
        'secret_chamber_unlocked': secret_chamber_unlocked
    }
    with open('save_game.json', 'w') as file:
        json.dump(game_state, file)
    print("Game saved!")

#sp23-bai-044
# Main game loop
def game_loop():
    display_room_details(current_room)
    while True:
        command = input("\nWhat would you like to do? ").lower().split()
        if len(command) == 0:
            continue

        if command[0] == 'go':
            if len(command) > 1:
                move_to_room(command[1])
            else:
                print("Go where?")
        elif command[0] == 'take':
            if len(command) > 1:
                pick_up_item(' '.join(command[1:]))
            else:
                print("Take what?")
        elif command[0] == 'examine' and len(command)>1:
            examine_items(command[1])
        elif command[0] == 'inventory':
            print("You have:", ', '.join(player_inventory) if player_inventory else "No items.")
        elif command[0] == 'look':
            look()   
        elif command[0] == 'save':
            save_game()
        elif command[0] == 'exit':
            print("Exiting the game.")
            break
        else:
            print("Unknown command.")

# Start the game
game_loop()
