"""Repeating a beat in a loop."""

__author__ = "730397999"


# Begin your solution here...

ZERO: int = 0
beat: str = str(input("What beat do you want to repeat? "))
times_repeated: int = int(input("How many times do you want to repeat it? "))
repitition_multiplier: int = (int(times_repeated) - 1)
if times_repeated <= ZERO:
    print("No beat...")
else:
    while ZERO < times_repeated:
        ZERO = ZERO + times_repeated
        beat_repeater: str = (str(beat) + str(" ")) * int(repitition_multiplier) + str(beat)
        print(beat_repeater)
