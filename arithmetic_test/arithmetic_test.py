import random


def mathem(n, k):
    mark = 0
    for _ in range(5):
        a = random.choice(range(n, k))
        b = random.choice(range(n, k))
        action = random.choice([a+b, a-b, a*b])
        if action == a+b:
            print(f"{a}+{b}=")
        elif action == a-b:
            print(f"{a}-{b}=")
        elif action == a*b:
            print(f"{a}*{b}=")
        answer = int(input(">"))
        if answer == action:
            print("Right!")
            mark += 1
        else:
            print("Wrong!")
    print(f"Your mark is {mark}/5.")


mathem(2, 9)
