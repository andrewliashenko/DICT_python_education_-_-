def navigation():
    print("Available formatters: plain bold italic header\n" \
           "link ordered-list unordered-list new-line space \n" \
           "Special commands: !help !done")


def output(a):
    text.append(a)
    print("".join(text))


formatter = ["space", "plain", "bold", "italic", "header", "link", "ordered-list", "unordered-list", "new-line", "!help", "!done"]
text = []
while True:
    enter = str(input("Choose a formatter:"))
    if enter in formatter:
        if enter == "plain":
            plain_txt = input("Text:>")
            output(plain_txt)
        elif enter == "bold":
            bold_txt = input("Text:>")
            result = "".join(["**", bold_txt, "**"])
            output(result)
        elif enter == "italic":
            italic_txt = input("Text:>")
            result = "".join(["*", italic_txt, "*"])
            output(result)
        elif enter == "header":
            level = int(input("Level:>"))
            header_txt = input("Text:>")
            header = ""

            for i in range(level):
                header += "#"
            result = "".join([header, header_txt])
            output(result)
        elif enter == "link":
            label = input("Label:>")
            link = input("Link:>")
            result = "".join(["[", label, "]","(", link, ")"])
            output(result)
        elif enter == "ordered-list":
            n = 0
            number = int(input("Number of rows: >"))
            or_list = []
            for i in range(number):
                n += 1
                element = input(f"Row #{n}:>")
                result = f"{n}.{element}\n"
                text.append(result)
            print("".join(text))
        elif enter == "unordered-list":
            number = int(input("Number of rows:>"))
            or_list = []
            n = 0
            for i in range(number):
                n += 1
                element = input(f"Row #{n}:>")
                result = f"*{element}\n"
                text.append(result)
            print("".join(text))
        elif enter == "new-line":
            text.append("\n")
        elif enter == "space":
            text.append(" ")
        elif enter == "!help":
            navigation()
        elif enter == "!done":
            f = open("output.md", mode="w")
            f.write("".join(text))
            break
    else:
        print("Unknown formatting type or command")
