import sys
import re

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

    # 2. Rewrite \passthrough
    content = replace_passthrough(content)

    file.seek(0)
    file.write(content)
    file.truncate()
    file.close()


def replace_passthrough(string):
    string = re.sub(r'\\passthrough\{', "", string)
    string = re.sub(r'!\}', "!", string)
    return string


def test_replace_passthrough():
    TESTS = [
        "  \passthrough{\lstinline!<didname>!} to \passthrough{\lstinline!<did>!}",
        "  Show the did of a single \passthrough{\lstinline!<didname>!}.",
        "\passthrough{\lstinline!did!} in the command-line. The user has to make",
        "looks after running \passthrough{\lstinline!did init!} :"
    ]

    for test in TESTS:
        print(replace_passthrough(test))


if __name__ == "__main__":
    main()
