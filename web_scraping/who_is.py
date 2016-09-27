import whois

def who_is(url):
	return(whois.whois(url))

# print(who_is("http://www.google.com"))
# print(who_is("http://www.facebook.com"))
print(who_is("http://github.com/usman-tahir"))
print(who_is("mason.gmu.edu/~utahir/IT415/"))