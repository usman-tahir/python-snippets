from scraper import download
import re

def crawl_sitemap(url):
	# Download the sitemap file
	sitemap = download(url)

	# Extract the sitemap links
	links = re.findall("<loc>(.*?)</loc>", sitemap)

	# Download each link
	for link in links:
		html = download(link)

crawl_sitemap("http://example.webscraping.com/sitemap.xml")
