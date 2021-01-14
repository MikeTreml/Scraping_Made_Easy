from bs4 import BeautifulSoup
import requests

#url
url = "https://www.audible.com/search?keywords=eric+ungland"

#requests grabs the web ages information and save it as a class
page_source = requests.get(url)

#pass the the through beautifulsoup. this is an easy way to parse through the data
soup = BeautifulSoup(page_source.text, 'lxml')

print(soup.prettify())

#find_all is a good way to get multiple items from a page. replace li with any html tag. replace class with any attribute inside the tag
books = soup.find_all('li', attrs={"class": "bc-list-item productListItem"})

#for book in books:
    #print(book)