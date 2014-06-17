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

import re
import urllib2

import requests


API_URL = "http://www.videoweed.es/api/player.api.php?cid2=undefined&key={key}&numOfErrors=0&cid3=watchseries%2Elt&user=undefined&cid=1&file={file_id}&pass=undefined"


class Videoweed(object):
    def __init__(self, file_url):
        self.url = file_url
        self.cookies = None
        self.headers = {
        'User-Agent': "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36"}

    def __parse_api(self, file_id, file_key):
        url = API_URL.format(key=urllib2.quote(file_key), file_id=file_id)

        r = requests.get(url, cookies=self.cookies, headers=self.headers)

        if r.status_code == 200:
            resp = r.text
            resp = resp.replace("url=", '')
            return resp.split("&title")[0]
        else:
            return None

    def get_direct_link(self):
        r = requests.get(self.url)
        self.cookies = r.cookies
        page = r.text
        file_id = re.findall(r'file="(.+?)\"', page)[0]
        file_key = re.findall(r'filekey="(.+?)\"', page)[0]

        return self.__parse_api(file_id, file_key)


if __name__ == "__main__":
    v = Videoweed("http://www.videoweed.es/file/96b9fa261962d")
    v.get_direct_link()
