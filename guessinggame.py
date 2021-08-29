import random as r

num = r.randrange (100)
guess = 5

while guess >= 0:
    your_guess = int(input("enter your guess :"))


    def chek(x):
        if your_guess== x :
            print("you win")
        elif your_guess > x:
            print("you are close keep trying lower")
        else :
            print("you are close keep trying higher")

if guess > 1:
    chek(num)
elif guess == 1:
    chek(num)
    print("this is your last chance")
else:
     print("you lost")
     guess = guess - 1

