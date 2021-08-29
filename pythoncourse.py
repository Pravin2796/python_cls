print("GO CORONA GO")

i= 0 
cases=list()
while(i < 5):
    num = input("enter the total cases")
    i = i + 1
    cases.append(float(num))
    #sum = sum + float(num)
avg = sum(cases) / len(cases) 
print("avg", avg)   