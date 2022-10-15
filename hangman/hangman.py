print(str.upper("hangman"))
print("Welcome to the game.\nGuess the word to survive")
my_list = ["python", "java", "javascript", "kotlin"]
import random
randon_word = (random.choice(my_list))
k = input("This word is: " + randon_word[:3] + "-".join(['' for _ in range(len(randon_word)-2)]) + ">")
if k == randon_word:
    print("You survived!")
else:
    print("You lost!")
