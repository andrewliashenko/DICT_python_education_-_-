number_of_cups = int(input("Write how many cups of coffee you will need:\n>"))


def recipe():
    a = 200
    b = 50
    c = 15
    print(f"For {number_of_cups} cups of coffee you will need:"
          f"\n{a*number_of_cups}ml of water"
          f"\n{b*number_of_cups}ml of milk"
          f"\n{c*number_of_cups}g of coffee beans")


recipe()

