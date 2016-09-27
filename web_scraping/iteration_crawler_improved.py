from scraper import download
import itertools

# Maximum number of download errors
maximum_errors = 5

# Current number of download errors
number_of_errors = 0

for page in itertools.count(1):
	url = "http://example.webscraping.com/view/-%d" % page
	html = download(url)

	if html is None:
		# Error upon trying to download the webpage
		number_of_errors += 1
		if number_of_errors == maximum_errors:
			break
	else:
		# Result scraping
		number_of_errors = 0