Castle Game Documentation
Overview
This is a text-based adventure game set in a medieval castle where players can explore rooms, solve puzzles, and collect items. The player navigates the castle using simple text commands, manages an inventory, and interacts with objects to progress through the game.
Game Structure
The game is set in the following rooms:
1.	Entrance – The main entry point of the castle.
2.	Great Hall – A grand space for feasts and receptions.
3.	Pantry and Kitchen – For food preparation and storage.
4.	Defensive Areas and Armory – Stores weapons and armor.
5.	Stables – For keeping horses.
6.	Library – A quiet place filled with books.
7.	Secret Chamber – A hidden room accessible only through solving puzzles.
8.	Private Quarters – The living space for the royal family.
Players move between rooms using directional commands and interact with items through various commands, such as take, examine, and inventory.
Locked Areas:
•	Pantry
•	Secret chamber
Commands
1.	go [direction]: Moves the player to a different room.
o	Example: go north
2.	take [item]: Picks up an item from the current room.
o	Example: take torch
3.	examine [item]: Examines an object in the room for hidden items or clues.
o	Example: examine pan
4.	inventory: Displays the items the player is carrying.
o	Example: inventory
5.	look: Shows the player’s current room and what’s in the inventory.
o	Example: look
6.	save: Saves the current game state to a json file.
o	Example: save
7.	exit: Exits the game.
o	Example: exit
Puzzles
Puzzle 1: Unlock the Pantry
•	Scenario: The pantry is locked, and the key is hidden inside one of items in the kitchen.
•	Solution: The player must examine the heavy pan in the kitchen to find the key.
1.	Use “take heavy pan”.
2.	Use “examine heavy pan” to reveal the key.
Puzzle 2: Unlock the Secret Chamber
•	Scenario: The Secret Chamber is locked, and the player must either find a diary in the Private Quarters or push the bookshelf in the Library to gain access.
1.	In the Private Quarters, use “take diary of the queen” then use “examine diary of the queen” to unlock secret chamber.
2.	In the Library, use “take bookshelf” then use “examine bookshelf” to reveal the passage.
3.	After obtaining the correct item, the player can enter the Secret Chamber.
Inventory System
Players can collect items from rooms to help them solve puzzles and progress through the game. Items can be examined and stored in the player's inventory, which can be viewed using the inventory command.
Game State Management
The game includes a save and load feature, allowing players to store their progress:
•	Save: Type save to store the current room and inventory in a file.
User Interface
The game provides feedback for all actions, error handling for invalid commands, and clear descriptions of the player’s surroundings and items. All interactions are done through text commands, providing a straightforward experience.
________________________________________
Sample Gameplay
Scenario: The player starts at the entrance and explores the castle, solves puzzles, and unlocks the pantry and Secret Chamber.
Step 1: Exploring the Castle
•	Command: go north
•	Description: You enter the Great Hall.
•	Command: go west
•	Description: You enter the Pantry and Kitchen.
Step 2: Solving the Pantry Puzzle
•	Command: take heavy pan
•	Description: You found a key hidden under the heavy pan!
Step 3: Moving to the Secret Chamber
•	Command: go east
•	Description: You enter the Great Hall.
•	Command: go east
•	Description: You enter the Private Quarters.
•	Command: take diary of the queen
•	Description: You picked up: diary of the queen.
•	Description: The secret chamber unlocks as you move through a hidden door
                        You are in the Secret Chamber..

