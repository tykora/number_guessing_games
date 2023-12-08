num1 = 0
guesses = []
while num1 != 10:
    print("type guesses to look t your history")
    num1 = input("guess a number from 1 to 100: ")
    #
    guesses.append(num1)
   
    if num1.isdigit():
        num1 = int(num1)
        if num1 != 10:
            if num1 < 10 and num1 >= 1:
                print("too small try again.")
            if num1 > 10 and num1 <= 100:
                print("too big try again.")
            if num1 > 100 or num1 < 1:
                print("Thats out of bounds! try again.")
        elif num1 == 10:
            print("you found me ah haha!")
            break
    elif num1 == "guesses":
        print(guesses)
