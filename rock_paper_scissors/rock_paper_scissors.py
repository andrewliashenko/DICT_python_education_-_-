import random


def result():
    win = f"Well done. The computer chose {option_computer} and failed"
    lose = f"Sorry, but the computer chose {option_computer}"
    draw = f"There is a draw ({option_computer})"
    n = -1
    for i in range(3):
        n += 1
        if n == -2:
            n = 2
        elif n == 2:
            n = -1
        elif n == 1:
            n = -2
        if option_player == option[n]:
            if option_computer == option[n]:
                print(draw)
                rating[name] += 50
            elif option_computer == option[n+1]:
                print(lose)
            elif option_computer == option[n+2]:
                print(win)
                rating[name] += 100
    if option_player not in option and option_player != "!exit" and option_player != "!rating":
        print("Invalid input!")


name = input("Enter your name: >")
print(f"Hello, {name}")
rating = {name: 0}
while True:
    option_player = input(">")
    option = ["rock", "paper", "scissors"]
    option_computer = random.choice(option)
    result()
    if option_player == "!rating":
        print(f"{name}: {rating.values()}")
    if option_player == "!exit":
        print("Bue!")
        break


