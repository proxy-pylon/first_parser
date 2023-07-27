import requests
from bs4 import BeautifulSoup
from time import sleep


headers = {"User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36"}


def download(url):
    resp = requests.get(url, stream=True)
    r = open("D:\\Python projects\\parser\\images\\" + url.split("/")[-1], "wb")
    for value in resp.iter_content(1024*1024):
        r.write(value)
    r.close()

def get_url():
    for page in range(1, 8):
        url = f'https://scrapingclub.com/exercise/list_basic/?page={page}'

        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')

        data = soup.find_all("div", class_='col-lg-4 col-md-6 mb-4')

        for i in data:
            card_url = "https://scrapingclub.com" + i.find("a").get("href")
            yield card_url


def array():
    for card_url in get_url():
        response = requests.get(card_url, headers=headers)
        sleep(1)
        soup = BeautifulSoup(response.text, 'lxml')

        data = soup.find("div", class_='card mt-4 my-4')
        name = data.find("h3", class_='card-title').text
        price = data.find("h4").text
        description = data.find("p", class_="card-text").text
        image_url = "https://scrapingclub.com" + data.find("img", class_="card-img-top img-fluid").get("src")
        download(image_url)
        yield name, price, description, image_url

