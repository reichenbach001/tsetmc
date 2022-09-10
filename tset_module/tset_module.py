import requests
import re
from config2 import constant_vars
class TsetCrawler():

    def fetch_urls(self, url, selecting_length=30):
        self.uurl = url
        self.selecting_length = selecting_length
        fetched_data = requests.get(self.uurl)
        urls_check_set = set()

        for id_selector in re.finditer(r';', fetched_data.text):

            selected_id = id_selector.string[
                          id_selector.start() + 1:id_selector.start() + self.selecting_length]

            refined_id = selected_id.split(',')
            if refined_id[0] not in urls_check_set:
                urls_check_set.add(refined_id[0])

        return list(urls_check_set)

    def fetch_data(self, url):
        self.uurl = constant_vars['crawling_url_1'] + url + constant_vars['crawling_url_2']

        fetched = requests.get(self.uurl)
        return fetched.text

