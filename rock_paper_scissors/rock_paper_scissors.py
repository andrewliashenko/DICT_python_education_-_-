import random


def result():
    win = f"Well done. The computer chose {option_computer} and failed"
    lose = f"Sorry, but the computer chose {option_computer}"
    draw = f"There is a draw ({option_computer})"
    n = 0
    for i in range(3):
        n += 1
        if n == 3:
            n = 0
        if option_player == option[n]:
            if option_computer == option[n]:
                print(draw)
            elif option_computer == option[n+1]:
                print(lose)
            elif option_computer == option[n+2]:
                print(win)


option_player = input(">")
option = ["rock", "paper", "scissors"]
option_computer = random.choice(option)
result()


