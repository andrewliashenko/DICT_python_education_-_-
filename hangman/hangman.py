print("HANGMAN")
print("The game will be available soon.")
my_list = ["python", "java", "kotlin", "javascript"]
import random
randon_word = random.choice(my_list)
remember_letters = []
all_letters = list(set(randon_word))
words = ''.join([i if i in remember_letters else "-" for i in randon_word])
print(words)
life = 8
while life > 0:
    letter = input("input a letter:")
    if letter in randon_word and letter not in remember_letters:
        remember_letters.append(letter)
        all_letters.remove(letter)
    else:
        life -= 1
        print("That letter doesn't appear in the word")
    words = ''.join([i if i in remember_letters else "-" for i in randon_word])
    print(words)
    if len(all_letters) == 0:
        break
print("thanks for playing\nWe'll see how well you did in the next stage")
