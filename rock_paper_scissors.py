"""
Project:  Rock paper scissors
Author: Siham Elmali
Date: 1/4/2021
"""
import random
import itertools
import collections

# Constants
PLAYER = "Player"
COMPUTER = "Computer"


def get_images():
	rock = '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    '''

	paper = '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    '''

	scissors = '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    '''
	selection = [rock, paper, scissors]
	return selection


def get_user_choice():
	user = int(input("What is your choice? type 0 for Rock, 1 for Paper or 2 for Scissors: "))
	return user


def get_computer_choice():
	computer = random.randint(0, 2)
	return computer


def evaluate_round(user_input, computer_choice):
	score_ = {}
	selection = get_images()
	if user_input >= 3 or user_input < 0:
		print("You entered an invalid choice. Try again")  # FIXME
	else:
		print(f"You chose: {selection[user_input]}")
		print(f"Computer chose: {selection[computer_choice]}")

		if user_input == 0 and computer_choice == 2:
			print("You win the round")
			score_[PLAYER] = 1
		elif computer_choice == 2 and user_input == 1:
			print("You lose the round !!")
			score_[COMPUTER] = 1
		elif computer_choice > user_input:
			print("You lose the round!!")
			score_[COMPUTER] = 1
		elif user_input > computer_choice:
			print("You win the round !!")
			score_[PLAYER] = 1
		elif computer_choice == user_input:
			print("It's a draw!!")
	return score_


def add_score(score_, round_score):
	cdict = collections.defaultdict(int)
	for key, value in itertools.chain(score_.items(), round_score.items()):
		cdict[key] += value

	return cdict


def check_game_over(score_, win_threshold_):
	return any([value >= win_threshold_ for value in score_.values()])


def print_game_over(score_):
	underscores = "--------------------------------------------"
	print(underscores)
	print("FINAL SCORE")
	for key, value in score_.items():
		print("{}: {}".format(key, value))
	print(underscores)


if __name__ == '__main__':

	print("Welcome to Rock Paper Scissors.\nYour objective is to win against the computer")
	score = {PLAYER: 0, COMPUTER: 0}
	win_threshold = 2

	while True:
		user_choice = get_user_choice()
		comp_choice = get_computer_choice()
		round_result = evaluate_round(user_choice, comp_choice)
		score = add_score(score, round_result)

		if check_game_over(score, win_threshold):
			break

	print_game_over(score)
