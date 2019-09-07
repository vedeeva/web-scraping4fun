import requests
from bs4 import BeautifulSoup

url = 'https://www.billboard.com/festivals'
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
news_containers = soup.find_all('div', class_ = 'channel-article')

number_of_articles = 10
dash = '-' * 70

for i in range (number_of_articles):

    title = news_containers[i].get_text()
    link = news_containers[i].find('a')['href']

    print(dash)
    print("Category: " + title.lstrip())
    print("Link: "+ link)
