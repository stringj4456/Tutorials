import requests
from bs4 import BeautifulSoup

req = requests.get('https://en.wikipedia.org/wiki/Python_(programming_language)')
soup = BeautifulSoup(req.text, "lxml")  # BeautifulSoup Object

print(soup.title)               # Tag object
print(soup.title.name)          # Tag name
print(soup.title.string)        # Navigable string
print()

print(soup.h1)                  # Tag object
print(soup.h1.string)           # Navigable string
print(soup.h1["class"])         # The HTML 'class' attribute for the h1 tag
print(soup.h1["id"])            # The HTML 'id' attribute for the h1 tag
print(soup.h1.attrs)            # All attribute names and values for the tag
print()

soup.h1["class"] = "firstHeading, mainHeading"
soup.h1.string.replace_with("Python - Programming Language")
del soup.h1["lang"]
del soup.h1["id"]
print(soup.h1)
