import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Thomas_Edison"

# Fetch the page content
r = requests.get(url)
print(r)  # This ensures whether the page can be accessed or not

# Parse the page content
soup = BeautifulSoup(r.text, "html.parser")

# Print the title of the page
title = soup.find("span", {"class": "mw-page-title-main"})
print(title.string)

# Printing the first meaningful paragraph
paragraphs = soup.find_all('p')
print(paragraphs[1].text)

# Extract external links
external_links = []
for link in soup.find_all('a', href=True):
    href = link['href']
    if href.startswith('http') and not href.startswith('https://en.wikipedia.org'):
        external_links.append(href)

# Print external links
for link in external_links:
    print(link)

# Printing image links defined under <a> tag and href attribute
for link in soup.find_all('a', href=True, class_="mw-file-description"):
    print(link['href'])

# Print the information under the main image
rows = soup.find_all('tr')
for row in rows[:13]:
    print(row.get_text(separator=' ', strip=True))

# Printing captions under images defined under <figcaption> tag
figcaptions = soup.find_all('figcaption')
for caption in figcaptions:
    print(caption.get_text())

























