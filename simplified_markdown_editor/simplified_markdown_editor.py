def navigation():
    print("Available formatters: plain bold italic header\n" \
           "link ordered-list unordered-list new-line \n" \
           "Special commands: !help !done")


def output(a):
    text.append(a)
    print(" ".join(text))


plain = ""
bold = "**"
italic = "*"
header = {"H1": "#", "H2": "##", "H3": "###", "H4": "####"}
link = ["[", "]", "(", ")"]
ordered_list = "n"
unordered_list = "*"
new_line = "\n"
formatter = ["plain", "bold", "italic", "header", "link", "ordered-list", "new-line", "!help", "!done"]
text = []

while True:
    enter = str(input("Choose a formatter:"))
    if enter in formatter:
        if enter == "plain":
            plain_txt = input("Text:>")
            output(plain_txt)
        elif enter == "bold":
            bold_txt = input("Text:>")
            result = "".join([bold, bold_txt, bold])
            output(result)

        elif enter == "italic":
            print("italic")
        else:
            print("!")
    else:
        print("Unknown formatting type or command")
