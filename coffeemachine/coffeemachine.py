ingredients = {'water': 400, 'milk': 540,  'coffee': 120, 'number_of_cups': 9, 'money': 550}


def recipe(a, b, c, cup, m):
    ingredients['water'] = ingredients['water'] - a
    ingredients['milk'] = ingredients['milk'] - b + 1
    ingredients['coffee'] = ingredients['coffee'] - c
    ingredients['number_of_cups'] = ingredients['number_of_cups'] - cup
    ingredients['money'] = ingredients['money'] - m


def remain():
    print(f"The coffee machine has:"
          f"\n{ingredients['water']}ml of water"
          f"\n{ingredients['milk']}ml of milk"
          f"\n{ingredients['coffee']}g of coffee beans"
          f"\n{ingredients['number_of_cups']} of disposable cups"
          f"\n{ingredients['money']} of money")


def ingredient(a, b, c, cup, m):
    k = [ingredients['water'] // a, ingredients['milk'] // b, ingredients['coffee'] // c]
    n = min(k)
    if n >= 1:
        print("I have enough resources, making you a coffee!")
        recipe(a, b, c, cup, m)
    elif n < 1:
        print("not enough ingredients")
    elif ingredients['number_of_cups'] == 0:
        print("not enough cups")


while True:
    action = input("Write action (buy, fill, take, remaining, exit):\n>")
    if action == "buy":
        buy = int(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:\n>"))
        if buy == 1:
            ingredient(250, 1, 16, 1, -4)
        elif buy == 2:
            ingredient(350, 75, 20, 1, -7)
        elif buy == 3:
            ingredient(200, 100, 12, 1, -6)
    elif action == "fill":
        a = int(input("Write how many ml of water you want to add:\n>"))
        b = int(input("Write how many ml of milk you want to add:\n>"))
        c = int(input("Write how many grams of coffee beans you want to add:\n>"))
        cup = int(input("Write how many disposable coffee cups you want to add:\n>"))
        recipe(-a, -b, -c, -cup, 0)
    elif action == "take":
        print(f"I gave you {ingredients['money']}")
        recipe(0, 0, 0, 0, ingredients['money'])
        remain()
    elif action == "remaining":
        remain()
    elif action == "exit":
        break
