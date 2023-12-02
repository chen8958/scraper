import requests
# from html.parser import HTMLParser
from helper import Parser

URL = "http://market.dcview.com/brand/%E5%85%B6%E4%BB%96%E5%BB%A0%E7%89%8C?categories=3"
response = requests.get(url = URL)
htmlparser = Parser()
htmlparser.feed(response.text)


print(response)
