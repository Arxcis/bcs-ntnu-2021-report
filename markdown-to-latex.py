import sys

CHAPTERS = ["1-introduction",
            "2-development-process",
            "3-functional-requirements",
            "4-user-interface",
            "5-architecture",
            "6-results",
            "7-discussion",
            "8-conclusion"]


def main():
    file = open(sys.argv[1], "r+")

    content = file.read()

    # 1. Replace first occurance of section with chapter
    content = content.replace("section", "chapter", 1)

    # 2. Rewrite "".svg" -> ""
    content = content.replace(".svg", "")

    file.seek(0)
    file.write(content)
    file.truncate()
    file.close()


if __name__ == "__main__":
    main()
