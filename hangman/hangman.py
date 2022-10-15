print(str.upper("hangman"))
print("Welcome to the game.\nGuess the word to survive")
my_list = ["python", "java", "javascript", "kotlin"]
import random
randon_word = (random.choice(my_list))
attempts = 8
letters = []
all_letters = list(set(randon_word))
word = "".join([i if i in range(len(randon_word)+1)]) + "\nInput a letter: >"
k = input()

if k == randon_word:
    print("You survived!")
else:
    print("You lost!")
