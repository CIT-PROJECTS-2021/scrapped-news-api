import requests
from bs4 import BeautifulSoup



def scrape_rss(url):
    """Scrape the RSS feed and return a list of news"""
    response = requests.get(url)
    soup = BeautifulSoup(response.text, features="xml")
    return soup.find_all('item')


def scrape_un_news():
    url = 'https://news.un.org/en/rss-feeds'
    response = requests.get(url).text
    soup = BeautifulSoup(response, features="html.parser")
    container = soup.find('div', {'class': 'panel-body'})
    rss_links = container.find_all('p')
    rss_links = [link.find('a').get('href') for link in rss_links]
    news = []
    for link in rss_links:
        # check if the link is rss feed
        if '.xml' in link:
            news.extend(scrape_rss(link))
        else:
            # if not, skip it
            continue

    return news


def parse_un_rss_data(data):
    """Extract required data from the RSS feed"""
    soup = BeautifulSoup(str(data), features="html.parser")
    urls = soup.find_all('source')
    urls = [url.get('url') for url in urls]
    clean_urls = []
    for url in urls:
        if url not in clean_urls:
            clean_urls.append(url)
        else:
            continue

    return clean_urls


def scrape_nytimes():
    url = 'https://www.nytimes.com/rss'
    response = requests.get(url).text
    soup = BeautifulSoup(response, features="html.parser")
    containers = soup.find_all('div', {'class': 'css-1qj0uia'})
    rss_links = []
    for container in containers:
        rss_links.extend(container.find_all('a'))

    rss_links = [link.get('href') for link in rss_links]

    return rss_links


def scrape_sky_news():
    """Scrape the RSS feed and return a list of news feed urls from sky news"""
    url = 'https://news.sky.com/info/rss'
    response = requests.get(url).text
    soup = BeautifulSoup(response, features="html.parser")
    rss_links = soup.find_all('ul')[2].find_all('a')
    rss_links = [link.get('href') for link in rss_links]
    return rss_links


def scrape_cnn_news():
    """Scrape the RSS feed and return a list of news feed urls from cnn news"""
    url = 'https://edition.cnn.com/services/rss/'
    response = requests.get(url).text
    soup = BeautifulSoup(response, features="html.parser")
    table_data = soup.find('table').find_all('td', {'class': 'cnnRSS'})
    rss_links = []
    for data in table_data:
        rss_links.extend(data.find_all('a'))

    rss_links = [link.get('href') for link in rss_links]
    
    return rss_links
