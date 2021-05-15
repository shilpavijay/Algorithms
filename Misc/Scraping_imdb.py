#scrap data from IMDb top 250 movies page. It should only have fields movie name, year, and rating.
#url: 'http://www.imdb.com/chart/top'

from bs4 import BeautifulSoup
import requests

url = 'https://www.imdb.com/chart/top'
response = requests.get(url)
soup = BeautifulSoup(response.text,"html.parser")

tr = soup.findChildren('tr')
tr = iter(tr)
next(tr)

for eachitem in tr:
    title = eachitem.find('td', { 'class':'titleColumn' }).find('a').contents[0]
    year = eachitem.find('td', { 'class':'titleColumn' }).find('span', {'class':'secondaryInfo'}).contents[0]
    rating = eachitem.find('td', {'class': 'ratingColumn imdbRating'} ).find('strong').contents[0]
    movie = 'TITLE: ' + title + year + '   RATING: ' + rating
    print(movie)