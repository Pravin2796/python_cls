n=18
no_of_guess = 1
print("no_of_guess is 9 \n")
while(no_of_guess<=9):
    guess_no= int(input("guesstheno\n"))
    if guess_no < 18:
        print("you have entered less no\n")
    elif guess_no > 18:
        print("you enter big no\n")
    else 
        print("you won\n")
        print(no_of_guess,"no of guess he took to finish")
        break
    print(9-no_of_guess,"no of guess left") 
    no_of_guess = no_of_guess + 1

    if(no_of_guess>9):
        print("game over\n")       