# print a if choice < 25
# print b if choice >= 25 and <50 
# print c if choice > 75
# print d if choice >= 50 and <= 75

choice: int = int(input("Enter a number: "))

if choice < 25:
    print("A")
else:
    if choice < 50:
        print("B")
    else:
        if choice <= 75:
            print("D")
        else:
            print("C")