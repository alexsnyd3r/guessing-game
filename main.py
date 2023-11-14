import random

name = input("What is your name? ")
print("Welcome " + name + "! I'm thinking of \
a number between 1 and 100.")

my_number = random.randint(1, 100)
guesses = []
for guess_number in range(1, 11):
    valid_guess = False
  
    while not valid_guess:
        try:
            user_guess = int(input("Take a guess...\n"))
            valid_guess = True
        except ValueError:
            print("Please provide a valid number.")

    difference = abs(my_number - user_guess)
    guesses.append(user_guess)
    
    if user_guess < my_number and difference > 10:
      print("Your guess is very low.Try again")
    elif user_guess > my_number and difference < 10:
      print("Your guess is a little low.Try again")
      
    elif user_guess > my_number and difference > 10:
      print("Your guess is very high. Try again.")
      
    elif user_guess > my_number and difference < 10:
      print("Your guess is a little high. Try again.")
    else:
      break
      
if user_guess == my_number:
    print("You won " + name + "! You guessed my number in " + str(guess_number) + " guesses.")
    print("Here are your previous guesses: " + str(guesses))
else:
    print("Sorry. You didnt guess my number I was thinking of was " + str(my_number))
#testcommit