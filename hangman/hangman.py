print(str.upper("hangman"))
print("Welcome to the game.\nGuess the word to survive")
import random
my_list = ["python", "java", "javascript", "php"]
k = str(input(">"))
if k == random.choice(my_list):
    print("You survived!")
else:
    print("You lost!")
