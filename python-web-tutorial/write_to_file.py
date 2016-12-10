import requests
from bs4 import BeautifulSoup

def get_article_portions(soup):
  # Find the heading with the specific class
  heading = soup.find("div", {"class": "dek"})
  if heading:
    yield heading.text
  
  # Locate all the paragraphs from the webpage
  for p in soup.find_all("p", {"class": ""}):
    yield p.text

def read_page(address):
  page = requests.get(address) # Open the webpage
  soup = BeautifulSoup(page.text, "html.parser")

  open_file = open("news_article_contents.txt", "w+")

  # Get each paragraph, and allow the user to continue by hitting 'enter'
  for s in get_article_portions(soup):
    # print "\n%s" % s.encode("utf-8")
    open_file.write("\n%s" % (s.encode("utf-8")))
    # raw_input("\nPress enter to continue")
  # Once the article ends
  # print("End of article")
  open_file.close()

if __name__ == "__main__":
  url = "http://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture"
  read_page(url)