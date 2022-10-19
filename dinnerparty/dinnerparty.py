import random

number_of_people = int(input("Enter the number of friends joining (including you):\n>"))
payments = {}
if number_of_people > 0:
    print("Enter the name of every friend (including you), each on a new line:")
    for i in range(int(number_of_people)):
        names = input(">")
        payments[names] = 0
    total = int(input("Enter the total amount:\n>"))
    a = round(total / number_of_people, 2)
    print('Do you want to use the "Who is lucky?" feature? Write yes/no:')
    lucky = str(input(">"))
    lucky_name = random.choice(list(payments.keys()))
    if lucky == "yes":
        print(lucky_name, "is the lucky one!")
    elif lucky == "no":
        print("No one is going to be lucky")
        for names in payments:
            payments[names] = a
        print(payments)
else:
    print("No one is joining for the party")
