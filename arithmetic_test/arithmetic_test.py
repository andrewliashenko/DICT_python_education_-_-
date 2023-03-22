import random
mark = 0
while True:
    print("Which level do you want? Enter a number:"
          "\n1 - simple operations with numbers 2-9"
          "\n2 - integral squares of 11-29")
    level = int(input(">"))
    if level == 1:
        for _ in range(5):
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
                mark += 1
            else:
                print("Wrong!")
        print(f"Your mark is {mark}/5.")
    if level == 2:
        for i in range(5):
            a = random.choice(range(11, 29))
            print(f"{a}**2=")
            answer = int(input(">"))
            if answer == a**2:
                print("Right!")
                mark += 1
            else:
                print("Wrong!")
        print(f"Your mark is {mark}/5.")
    print("Would you like to save your result to the file?\nEnter yes or no.")
    save = str(input(">"))
    if save in ["yes", "y", "Yes", "YES"]:
        name = input("Enter your name:>")
        result = f"{name}: {mark}/5 in level {level}"
        print(result)
        f = open("marks.md", mode="w")
        f.write(result)
        break
    elif save in ["no", "No", "NO", "n"]:
        break
