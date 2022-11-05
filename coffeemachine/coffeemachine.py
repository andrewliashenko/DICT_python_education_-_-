water = 400
milk = 540
coffee = 120
number_of_cups = 9
money = 550


def recipe(a, b, c, cup, m):
    k = [water//200, milk//50, coffee//15]
    n = min(k) - number_of_cups
    print(f"The coffee machine has:"
          f"\n{water - a} of water"
          f"\n{milk - b} of milk"
          f"\n{coffee - c} of coffee beans"
          f"\n{number_of_cups - cup} of disposable cups"
          f"\n{money + m} of money")


print(f"The coffee machine has:"
      f"\n{water} of water"
      f"\n{milk} of milk"
      f"\n{coffee} of coffee beans"
      f"\n{number_of_cups} of disposable cups"
      f"\n{money} of money")

action = input("Write action (buy, fill, take):\n>")
if action == "buy":
    buy = int(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:\n>"))
    if buy == 1:
        recipe(250, 0, 16, 1, 4)
    elif buy == 2:
        recipe(350, 75, 20, 1, 7)
    elif buy == 3:
        recipe(200, 100, 12, 1, 6)
elif action == "fill":
    a = int(input("Write how many ml of water you want to add:\n>"))
    b = int(input("Write how many ml of milk you want to add:\n>"))
    c = int(input("Write how many grams of coffee beans you want to add:\n>"))
    cup = int(input("Write how many disposable coffee cups you want to add:\n>"))
    recipe(-a, -b, -c, -cup, 0)
elif action == "take":
    print(f"I gave you {money}")
    recipe(0, 0, 0, 0, -money)
