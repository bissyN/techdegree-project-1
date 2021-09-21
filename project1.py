import random

def start_game():
    player_attempts = 0
#Store a random number as the answer/solution#
    random_num = random.randrange(0,11)
    player_guess = 0
#Continuously prompt the player for a guess.#
    while player_guess != random_num:
        try:
            player_guess = int(input("Guess a number between 0-10 "))
            if player_guess < 1 or player_guess > 10:
                print("Your guess is not in range. Please try again")   
        except ValueError:
            print("Please can you insert a valid value")
# If the guess greater than the solution, display to the player "It's lower".#
        else: 
            if player_guess < random_num:
                player_attempts +=1
                print("Your guess is too low!")
#If the guess is less than the solution, display to the player "It's higher".#
            if player_guess > random_num:
                print("Your guess is too high!")
                player_attempts +=1
                
#Once the guess is correct, stop looping, inform the user they "Got it" and show how many attempts it took them to get the correct number.#  
    else: 
        print("Well done! You managed to guess the number in {} attempts! You gain the satisfaction of knowing that you won a computer game!".format(player_attempts))
                
#Display an intro/welcome message to the player#
player_name = input("Welcome Player! Please enter your name: ")
print("{} are you ready to play the Ultimate Number Guessing Game?".format(player_name))

start_game()
        
#Let the player know the game is ending, or something that indicates the game is over.#
print("Thanks for playing!")
        

    