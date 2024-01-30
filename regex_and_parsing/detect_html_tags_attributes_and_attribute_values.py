"""algo aqui"""
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    """ssss"""

    def handle_starttag(self, tag, attrs):
        print(tag)
        for i in attrs:
            print("->", i[0], ">", i[1])

    # def handle_endtag(self, tag):
    #     print("End   :", tag)

    def handle_startendtag(self, tag, attrs):
        print(tag)
        for i in attrs:
            print("->", i[0], ">", i[1])


if __name__ == "__main__":
    HTML = ""
    parser = MyHTMLParser()
    for _ in range(int(input())):
        HTML += input()

    parser.feed(HTML)
    parser.close()
