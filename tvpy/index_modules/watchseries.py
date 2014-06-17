#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2014 Nikola Kovacevic <nikolak@outlook.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import urllib2
import re

from bs4 import BeautifulSoup
import requests


SEARCH_URL = "http://watchseries.lt/search/{query}"
BASE_URL = "http://watchseries.lt"


class WatchSeries(object):
    def __init__(self):
        pass

    def __parse_search(self, search_page):
        search_soup = BeautifulSoup(search_page)
        results = search_soup.find_all(href=re.compile("/serie/"))
        result_dict = {}
        for show in results:
            if len(show.attrs) != 2:
                continue
            if show.text == "\n ":
                continue
            result_dict[show.text] = "{}{}".format(BASE_URL, show['href'])
        if result_dict:
            return result_dict
        else:
            return None

    def parse_show(self, show_url):
        r = requests.get(show_url)
        if not r.status_code == 200:
            return None

        s = BeautifulSoup(r.text)

        seasons = s.find_all('ul', class_='listings episodeListings')

        episode_dictionary = {}
        for season in seasons:
            episodes = season.find_all('a')
            for episode in episodes:
                title = "".join(episode['title'].split('-')[1:])
                episode_dictionary[title] = "{}{}".format(BASE_URL,
                                                          episode['href'])

        if episode_dictionary:
            return episode_dictionary
        else:
            return None


    def search(self, search_query):
        if not search_query:
            return None

        r = requests.get(SEARCH_URL.format(query=urllib2.quote(search_query)))
        if r.status_code == 200:
            return self.__parse_search(r.text)
        else:
            return None

    def get_hoster_link(self, episode_url):
        r = requests.get(episode_url)
        if not r.status_code == 200:
            return None

        s = BeautifulSoup(r.text)

        eng_links = s.find('div', id='lang_1')

        redirect_link = None
        for link in eng_links.find_all('a', title='videoweed'):
            redirect_link = "{}{}".format(BASE_URL, link['href'])
            break

        redirect_page = requests.get(redirect_link)

        rsoup = BeautifulSoup(redirect_page.text)

        hoster_link = rsoup.find('a', class_='myButton')['href']

        return hoster_link if hoster_link != "" else None


if __name__ == "__main__":
    i = WatchSeries()
    i.get_hoster_link("http://watchseries.lt/episode/rookie_blue_s1_e1.html")