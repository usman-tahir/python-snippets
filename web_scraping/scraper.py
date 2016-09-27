import urllib2

def download(url, user_agent = "wswp", num_retries = 2):
	print("Downloading: ", url)
	# Header information
	headers = {
		"User-agent": user_agent
	}

	try:
		html = urllib2.urlopen(url).read()
	except urllib2.URLError as e:
		# In the event of an error, show its reason
		print("Download error: ", e.reason)
		html = None
		if num_retries > 0:
			# If the exception has a code between 500 and 600
			if hasattr(e, 'code') and 500 <= e.code < 600:
				# Recursively retry 5xx HTTP errors
				return download(url, num_retries - 1)
	finally:
		return html

# print(download("http://www.github.com/usman-tahir"))
print(download("http://httpstat.us/500"))
print(download("http://httpstat.us/404"))