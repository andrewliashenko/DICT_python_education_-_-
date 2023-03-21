import random
a = random.choice(range(2, 9))
b = random.choice(range(2, 9))
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
else:
    print("Wrong!")
