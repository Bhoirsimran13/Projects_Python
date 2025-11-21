import random

def number_guess():
    ran_num = random.randint(1, 10)
    attempts = 0
    max_attempts = 3

    print("***** Number Guessing Game *****")    
    print("-------------------------------")
    print(f"You have {max_attempts} attempts to guess it!\n")

    while attempts < max_attempts:
        try:
            guess_num = int(input("Enter a number (1 to 10): "))
            attempts += 1
            
            if guess_num == ran_num:
                print("🎉 You have won the game..!!!") 
                break 
            elif guess_num > ran_num:
                print("Too high! Try again.")
            elif guess_num < ran_num:
                print("Too low! Try again.")
        
        except ValueError:
            print("Enter a valid Integer")

    else:
        print(f"Sorry! You've used all {max_attempts} attempts. The number was {ran_num}.")

number_guess()
