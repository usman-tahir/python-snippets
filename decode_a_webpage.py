import requests
from bs4 import BeautifulSoup

url = "http://www.nytimes.com"
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")

headlines = []
for headline in soup.find_all(class_="story-heading"):
  if headline.a:
    # print(headline.a.text.replace("\n", " ").strip())
    headlines.append(headline.a.text.replace("\n", " ").strip())
  else:
    # print(headline.contents[0].strip())
    headlines.append(headline.contents[0].strip())
  
# print(str(headlines))
print("There are %s headlines. " % (str(len(headlines))))