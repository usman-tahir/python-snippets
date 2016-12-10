from bs4 import BeautifulSoup
import re

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, "html.parser")
# print(soup.prettify())
# print(len(soup.find_all("a")))

# Print all the links
for link in soup.find_all("a"):
  print(link.get("href"))

for _class in soup.find_all("p"):
  print(_class.get("class"))

'''
a = [1, 2, 3]
b = [5, 10, 15]

# Compiles a list by multiplying the list elements and returning those that are odd
c = [x * y for x in a for y in b if x * y % 2 != 0]
print(str(c))

# Compiles all the products regardless of parity
d = [x * y for x in a for y in b]
print(str(d))
'''

sample_filenames = ["www/root/filesystem", "www/root/software/licenses", "www/root/engineers", "www/html/main"]
for filename in sample_filenames:
	print(filename[filename.index("/"):filename.index("/") + 1])