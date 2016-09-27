from scraper import download
import urlparse
import re

def link_crawler(seed_url, link_regex):
	"""Crawl from the given seed URL following links matched by link_regex
	"""
	crawl_queue = [seed_url]
	while crawl_queue:
		url = crawl_queue.pop()
		html = download(url)

		# Filter for links that match the regex
		for link in get_links(html):
			if re.match(link_regex, link):
				link = urlparse.urljoin(seed_url, link)
				crawl_queue.append(link)

def get_links(html):
	"""Return a list of link from the html passed in
	"""
	# A regular expression to extract all links from the webpage
	webpage_regex = re.compile("<a[^>]+href=[\"\'](.*?)[\"\']", re.IGNORECASE)
	return webpage_regex.findall(html)

link_crawler("http://example.webscraping.com", "example.webscraping.com/(index|view)/")