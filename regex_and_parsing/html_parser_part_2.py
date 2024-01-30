"""algo aqui"""
import re
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    """ssss"""

    def handle_comment(self, data):
        if bool(re.search("\n", data)):
            print(">>> Multi-line Comment")
        else:
            print(">>> Single-line Comment")
        print(data)

    def handle_data(self, data):
        if data != "\n":
            print(">>> Data")
            print(data)


if __name__ == "__main__":
    parser = MyHTMLParser()
    for _ in range(int(input())):
        parser.feed(input() + "\n")
    parser.close()
