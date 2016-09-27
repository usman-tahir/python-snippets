import builtwith

def built_with(url):
	result = builtwith.parse(url)
	return(result)

print(built_with("http://www.google.com"))
print(built_with("http://example.webscraping.com"))