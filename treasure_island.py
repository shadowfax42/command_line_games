"""
Treasure island
"""
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input("Would you like to turn 'left' or 'right'?").lower()
if choice1 == 'left':
	choice2 = input("You've come to a lake. There is an island in the middle of the late. Type 'wait' to wait for a"
					"boat. Type 'swim' to swim across ").lower()
	if choice2 == 'wait':
		choice3 = input("You've arrived at the island unharmed. There is a house with 3 doors. One red, one yellow and"
						"one blue. Which color do you choose ").lower()
		if choice3 == 'yellow':
			print("You found the treasure. You Win!")
		elif choice3 == 'blue':
			print("Oops, you've been eaten by a giant beast. Game Over")
		elif choice3 == 'red':
			print("You've been burned by fire. Game Over")
		else:
			print("Game Over")

	else:
		print("You've been attacked by an angry trout. Game Over")

else:
	print("Oops!! you fell into a hole. Game Over")


