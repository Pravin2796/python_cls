list = ["hi", "bu","sjd","ksd","skd",1 ,5,6,5,3,12,12,36]

for item in list :
    if str(item).isnumeric() and item>=6:
        print(item)