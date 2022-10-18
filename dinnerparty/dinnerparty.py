number_of_people = int(input("Enter the number of friends joining (including you):\n>"))
payments = {}
if number_of_people > 0:
    print("Enter the name of every friend (including you), each on a new line:")
    for i in range(int(number_of_people)):
        names = input(">")
        payments[names] = 0
    total = int(input("Enter the total amount:\n>"))
    a = int(total // number_of_people)
    for names in payments:
        payments[names] = a
    print(payments)
else:
    print("No one is joining for the party")
