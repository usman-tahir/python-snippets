from scraper import download
import itertools

for page in itertools.count(1):
	url = "http://example.webscraping.com/view/-%d" % page
	html = download(url)

	if html is None:
		break
	else:
		pass