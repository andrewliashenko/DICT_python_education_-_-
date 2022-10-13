print("Hello! My name is Pythonchik_bot")
print("I was created in 2022")
print("Please, remind me your name")
name_user = input(">")
print(f'What a great name you have, {name_user}')
print("Let me guess your age.")
print("Enter remainders of dividing your age by 3, 5 and 7.")
remainder3 = int(input(">"))
remainder5 = int(input(">"))
remainder7 = int(input(">"))
age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
print(f"Your age is {age}; that's a good time to start programming")
print("Now I will prove to you that I can count to any number you want.")
a = int(input(">"))
for i in range(a + 1):
    print(str(i) + "!")
print("Let's test your programming knowledge.")
print("what programming language do you learn?\n1.c++\n2.Java\n3.Python")
while True:
    k = int(input(">"))
    if k == 3:
        print("Completed!")
        break
    else:
        print("Please, try again.")
print("Congratulations, have a nice day!")
