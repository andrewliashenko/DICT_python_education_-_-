water = int(input("Write how many ml of water the coffee machine has:\n>"))
milk = int(input("Write how many ml of milk the coffee machine has:\n>"))
coffee = int(input("Write how many grams of coffee beans the coffee machine has:\n>"))
number_of_cups = int(input("Write how many cups of coffee you will need:\n>"))


def recipe():
    a = 200 * number_of_cups
    b = 50 * number_of_cups
    c = 15 * number_of_cups
    k = [water//200, milk//50, coffee//15]
    n = min(k) - number_of_cups
    if water >= a and milk >= b and coffee >= c and n == 1:
        print("Yes, I can make that amount of coffee")
    elif water >= a and milk >= b and coffee >= c and n >= 2:
        print(f"Yes, I can make that amount of coffee and even {n} more than that")
    elif water <= a or milk <= b or coffee <= c:
        print(f"No, I can make only {-n} cups of coffee")


recipe()

