# This file is used to test the newsapp\scrapper\scrape.py file

import unittest
from newsapp.scrapper.scrape import scrape_un_news, parse_un_rss_data, scrape_nytimes, scrape_cnn_news, scrape_sky_news

class TestScrape(unittest.TestCase):
    def test_scrape_un_news(self):
        news = scrape_un_news()
        self.assertTrue(len(news) > 0)

    def test_parse_un_rss_data(self):
        news = scrape_un_news()
        urls = parse_un_rss_data(news)
        self.assertTrue(len(urls) > 0)

    def test_scrape_nytimes(self):
        urls = scrape_nytimes()
        self.assertTrue(len(urls) > 0)

    def test_scrape_cnn_news(self):
        urls = scrape_cnn_news()
        self.assertTrue(len(urls) > 0)

    def test_scrape_sky_news(self):
        urls = scrape_sky_news()
        self.assertTrue(len(urls) > 0)

if __name__ == '__main__':
    unittest.main()


