"""Choose your own Adventure Program: Calculating Professional Sports Odds."""

__author__ = "730397999"

from random import randint
player: str
points: int
CAT_EMOJI: str = "\U0001F639"


def main() -> None:
    """The entrypoint of the program."""
    global points
    points = randint(50, 55)
    greet()
    times_played: int = 1
    while times_played < 3:
        print(f"Currently, we predict that you have a {initial_odds(points)}% of making it professionally.")
        three_choices: str = input("Type '1' if you want to do baseball, '2' if you want to do football, and '3' if you wish to quit! ")
        if three_choices == "1":
            baseball()
        else:
            if three_choices == "2":
                football()
            else: 
                quit()
        times_played = times_played + 1
    quit()


def initial_odds(points: int) -> int:
    """Randomly calculates the initial odds of the user playing professional sports."""
    times_evaluated: int = 1
    while times_evaluated == 1:
        points = points - 1
        enthusiasm: str = input(f"{player}, do you know what baseball and football are?! (yes/no) ")
        if enthusiasm == "yes":
            points = points + 5
            print("Nice.")
        else:
            points = points - 5
            print("Google them, then play.")
        return(points)
    return(points)


def greet() -> None:
    """Greets the player and introduces the game."""
    global player
    player = str(input("Hi! Before we start, what is your name? "))
    print(f"In this game, {player}, you can see your odds of playing professional sports! {CAT_EMOJI}")
    print("You will play this game twice, once for each league. After, your overall probability of making it professionally will be displayed! ")


def baseball() -> None:
    """Baseball questions if user selects option 1."""
    print("Questionable choice!")
    global points
    global player
    print(f"Based on your last answer, we now predict that you have a {(points)}% chance of making it professionally.")
    first_baseball_question: str = input("Can you throw a ball 90mph? (yes/no) ")
    if first_baseball_question == "yes":
        print("Absolute cannon.")
        points = points + 20
    else:
        print("Noodle arm.")
        points = points - 20
    second_baseball_question: str = input("Can you hit a baseball 400 feet? (yes/no) ")
    if second_baseball_question == "yes":
        print("That's huge.")
        points = points + 20
    else:
        print("Might want to hit the weight room.")
        points = points - 10
    final_baseball_question: str = input("Lastly, can you rock a baseball hat with ease? (yes/no) ")
    if final_baseball_question == "yes":
        print("Mr. Stylish")
        points = points + 5
    else:
        print("That's gonna hurt your chances big time. ")
        points = points - 20
    print(f"Based on our algorthim, you have a {points}% chance of making it to the MLB.")
    if points < 50:
        print("Maybe start crocheting.")
    else:
        print(f"See you on draft night, {player}!")
    

def football() -> None:
    """Football option if user selects option 2."""
    global points
    global player
    print("Questionable choice!")
    print(f"Based on your last answer, we now predict that you have a {points}% chance of making it professionally.")
    first_football_question: str = input("Can you bench 225 pounds? (yes/no) ")
    if first_football_question == "yes":
        print("Someone's been eating their green beans.")
        points = points + 20
    else:
        print("Maybe one day.")
        points = points - 20
    second_football_question: str = input("Have you ever watched 'The Longest Yard' (yes/no) ")
    if second_football_question == "yes":
        print("Great movie.")
        points = points + 20
    else:
        print("Neither have I.")
        points = points - 10
    final_football_question: str = input("Lastly, have you ever held a football? (yes/no) ")
    if final_football_question == "yes":
        print("Good, just had to make sure.")
        points = points + 5
    else:
        print("I think we both know where this one's going. ")
        points = points - 20
    print(f"Based on our algorthim, you have a {points}% chance of making it to the NFL.")
    if points < 50:
        print("Watch some film or something, then try again.")
    else:
        print(f"See you on draft night, {player}!")


def quit() -> None:
    """Allows the user to exit the program."""
    global points
    """Allows user to quit and see their chances of making it professionally. """
    print(f"Thanks for playing! {CAT_EMOJI}")
    print(f"Based on our calculations, you have an {points}% chance of playing professional sports! ")
    play_again: str = input("Do you want to play again? (yes/no) ")
    if play_again == "yes":
        main()
    else:
        print("Goodbye!")


if __name__ == "__main__":
    main()