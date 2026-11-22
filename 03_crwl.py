import requests
from bs4 import BeautifulSoup
from urllib.parse import urldefrag, urljoin

# where to start crawling
root = "https://www.uni-osnabrueck.de/fb8/en/ikw"

agenda = [root] # what to crawl next

while agenda:
    url = agenda.pop()

    # Get the page
    r = requests.get(
        url,
        headers={"User-Agent": "AIWebPageCheck/1.0"},
        timeout=15,
    )

    # Check the status code and skip if not 200 OK
    print("Get", r.status_code, r.url)
    if r.status_code != 200:
        continue

    # Parse the page and find all links
    soup = BeautifulSoup(r.content, "html.parser")
    for link in soup.select("a[href]"):

        # Get the absolute URL of the link, and remove any fragment (the part after #)
        target, _ = urldefrag(urljoin(r.url, link["href"]))
        if (target == root or target.startswith(root + "/")):
            print("Found ", target)

