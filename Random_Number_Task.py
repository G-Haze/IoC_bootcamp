import random

random_number = random.randint(1,10)
guess_counter = 0

while guess_counter < 5:
    user_guess = int(input("Enter your guess (1-10):"))
    if  user_guess == random_number:
        print("You have guessed the number!")
        break
    if  user_guess < random_number:
        guess_counter = (guess_counter+1)
        print("Too low, guess again:") 
    if user_guess > random_number: 
        guess_counter = (guess_counter+1) 
        print("Too high, guess again")
if guess_counter == 5:
        print("You have run out of tries")



