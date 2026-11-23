import requests

r = requests.get(
    'https://ikw.uni-osnabrueck.de',
    headers={"User-Agent": "AIWebPageCheck/1.0"},
    timeout=15,)
                 
print(r.status_code)
print(r.headers)

# r.text is the content of the page, but it can be very long
# print(r.text)

# r.url is the final URL after any redirects, and r.history is a list of Response objects that were created in order to complete the request.
# print(r.url)
# print(r.history)