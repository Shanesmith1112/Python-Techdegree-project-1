import random

print("-----------------------------------\n Welcome to the Number Guessing Game! \n-----------------------------------")

name = input("\nWhat is your name?  ")

highscore = []

def start_game():
    def play_again():
        answer = input("Would you like to play again? (Yes / No) ")
        answer.lower()
        if answer == "yes" or answer == "y":
            print("\nYour current high score is {}!".format(min(highscore)))
            start_game()
            answer
        else:
            print("\nYour best score was {}! Try to beat it next time!".format(min(highscore)))
            exit()

    attempts = 1
    
	num = random.randint(1, 10)

    print("\nGood luck, {}!".format(name))

    while True:
        try:
            guess = int(input("\nI'm thinking of a number between 1 and 10. Can you guess it? "))
        except ValueError:
            print("\nERROR!\nPlease enter a number! ")
        else:
            while guess != num:               
                if guess < num:
                    guess = int(input("\nTry Again!\nThe number is going to be higher! "))
                    attempts += 1
				elif guess > num:
                    guess = int(input("\nTry Again!\nThe number is going to be lower! "))
                    attempts += 1
            	elif guess < 1 or guess > 10:
                    guess = int(input("\nERROR!\nThe number is between 1 and 10!\nThe number you guessed was not a valid number! "))
			if attempts > 1:
                print("Well Done!!\nIt only took you {} attempts to guess correctly!".format(attempts))
            else:
                print("\nYou got LUCKY, you guessed it on the first try!")
            highscore.append(attempts)
            play_again()

start_game()