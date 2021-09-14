"""Drawing forests in a loop."""

__author__ = "730397999"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'

depth: int = int(input("Depth: "))
ZERO: int = 0
multiplier: int = 1
if depth <= ZERO:
    print("")
else:
    while depth > ZERO:
        print('\U0001F332' * multiplier)
        multiplier = multiplier + 1
        depth = depth - 1