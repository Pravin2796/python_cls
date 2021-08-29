


sum = 0
while(True):
    UserInput= int("enter the price of product :")
    if (UserInput !='q'):
         sum = sum + int(UserInput)
    print(f"your total is",{sum})
    else :
         print(f"your total bill ammount is : ",{sum})
    break

