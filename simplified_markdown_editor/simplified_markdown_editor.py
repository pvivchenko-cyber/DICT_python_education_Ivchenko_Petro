FORMATTERS = (
    "plain",
    "bold",
    "italic",
    "header",
    "link",
    "inline-code",
    "ordered-list",
    "unordered-list",
    "new-line",
)


def print_help():
    print(f"Available formatters: {' '.join(FORMATTERS)}")
    print("Special commands: !help !done")


def format_header():
    while True:
        level = int(input("Level: "))
        if 1 <= level <= 6:
            break
        print("The level should be within the range of 1 to 6")
    text = input("Text: ")
    return f"{'#' * level} {text}\n"


def format_link():
    label = input("Label: ")
    url = input("URL: ")
    return f"[{label}]({url})"


def format_list(ordered=True):
    while True:
        rows = int(input("Number of rows: "))
        if rows > 0:
            break
        print("The number of rows should be greater than zero")

    result = ""
    for i in range(1, rows + 1):
        row_text = input(f"Row #{i}: ")
        prefix = f"{i}." if ordered else "*"
        result += f"{prefix} {row_text}\n"
    return result


def save_to_file(content, filename="output.md"):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)


def main():
    markdown_text = ""

    while True:
        choice = input("Choose a formatter: ")
        if choice == "!done":
            save_to_file(markdown_text)
            break
        elif choice == "!help":
            print_help()
            continue
        elif choice not in FORMATTERS:
            print("Unknown formatting type or command")
            continue

        if choice == "plain":
            markdown_text += input("Text: ")
        elif choice == "bold":
            markdown_text += f"**{input('Text: ')}**"
        elif choice == "italic":
            markdown_text += f"*{input('Text: ')}*"
        elif choice == "inline-code":
            markdown_text += f"`{input('Text: ')}`"
        elif choice == "new-line":
            markdown_text += "\n"
        elif choice == "header":
            markdown_text += format_header()
        elif choice == "link":
            markdown_text += format_link()
        elif choice == "ordered-list":
            markdown_text += format_list(ordered=True)
        elif choice == "unordered-list":
            markdown_text += format_list(ordered=False)

        print(markdown_text)


if __name__ == "__main__":
    main()