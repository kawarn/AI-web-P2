# ------ imports ---------------------------------------------------
import requests
from bs4 import BeautifulSoup
from urllib.parse import urldefrag, urljoin
from whoosh import index
from whoosh.index import create_in
from whoosh.fields import *
from whoosh.qparser import QueryParser
import os

# ------ variables -------------------------------------------------
in_word = "affen und ufos"
search_words = []
search_words_clean = []
special_chars = '\.,-"\'!?'
lists = []
wordsandlists = []

# ------ crawler skeleton ------------------------------------------

# where to start crawling
root = "https://info.cern.ch/hypertext/WWW/"

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

# ------ index --------------------------------------------------

schema = Schema(url=ID(stored=True), title=TEXT(stored=True), content=TEXT)

# create Index-Ordner, if not existed
if not os.path.exists("indexdir"):
    os.mkdir("indexdir")

# Create an index in the directory indexdr (the directory must already exist!)
ix = create_in("indexdir", schema)
writer = ix.writer()

# word input & processing
search_words = in_word.split()
for word in search_words:
    search_words_clean.append(word.strip(special_chars))
    
with ix.searcher() as searcher:
    for clean in search_words_clean:
        # find entries with the input words 
        query = QueryParser("content", ix.schema).parse(clean)
        results = searcher.search(query)

        # if there is no website
        if len(results) == 0:
            print("Keine Ergebnisse gefunden.")

        # Empty lists
        lists.clear()

        # print all results
        for r in results:
            lists.append(r)

        wordsandlists.append(clean[lists])




