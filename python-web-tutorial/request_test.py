import requests

# r = requests.get("https://api.github.com/events")
r = requests.post("http://httpbin.org/post", data = {"key" : "value"})
print(r.status_code)
print(r.url)
print(r.content)

profile = requests.get("http://gihub.com/usman-tahir")
profile_html = profile.text
print(profile_html)