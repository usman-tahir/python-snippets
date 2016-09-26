import requests
from bs4 import BeautifulSoup

def get_article_portions(soup):
  heading = soup.find("div", {"class": "dek"})
  if heading:
    yield heading.text
  
  for p in soup.find_all("p", {"class": ""}):
    yield p.text

def read_page(address):
  page = requests.get(address)
  soup = BeautifulSoup(page.text, "html.parser")

  for s in get_article_portions(soup):
    print "\n%s" % s.encode("utf-8")
    raw_input("\nPress enter to continue")
  print("End of article")

if __name__ == "__main__":
  read_page("http://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture")