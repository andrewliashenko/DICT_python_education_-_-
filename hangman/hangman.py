print(str.upper("hangman"))
print("Welcome to the game.\nGuess the word to survive")
my_list = ["python", "java", "javascript", "php"]
k = str(input(">"))
if k == my_list[0]:
    print("You survived!")
else:
    print("You lost!")


