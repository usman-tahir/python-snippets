import urllib2

def download(url, user_agent = "wswp", num_retries = 2):
	print("Downloading: ", url)
	headers = {
		"User-agent": user_agent
	}
	try:
		html = urllib2.urlopen(url).read()
	except urllib2.URLError as e:
		print("Download error: ", e.reason)
		html = None
		if num_retries > 0:
			if hasattr(e, 'code') and 500 <= e.code < 600:
				# Recursively retry 5xx HTTP errors
				return download(url, num_retries - 1)
	finally:
		return html

# print(download("http://www.github.com/usman-tahir"))
print(download("http://httpstat.us/500"))
print(download("http://httpstat.us/404"))