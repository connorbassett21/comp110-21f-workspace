"""An exercise in remainders and boolean logic."""

__author__ = "730397999"


# Begin your solution here...

integer: int = int(input("Enter an int: "))
zero: int = 0 
two: int = 2
seven: int = 7

if (integer % two) == 0 and (integer % seven) == 0:
    print("TAR HEELS")
else:
    if (integer % two) == zero:
        print("TAR")
    else:
        if (integer % seven) == zero:
            print("HEELS")
        else:
            print("CAROLINA")