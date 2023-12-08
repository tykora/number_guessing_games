# guess the number game
import random
num1 = random.randrange(1, 100)
history = []
guess = 1

while guess != num1:
    guess = input("guess a number 1 to 100: ")
  
    history.append(guess)
    if guess.isdigit():
        guess = int(guess)
        if guess > num1:
            print("to big! try again.")
        if guess < num1:
            print("to small! try again.")
        if guess == num1:
            print("you found me! ah ha ha!")
            break
        elif guess < 1 or guess > 100:
            print("out of bounds! try again.")
    if guess == "exit":
        break
    elif guess == "history":
        history.remove("history")
        print(history)