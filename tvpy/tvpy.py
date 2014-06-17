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

import sys
import os

from PySide.QtCore import *
from PySide.QtGui import *

import ui_code
from index_modules import WatchSeries
from hoster_modules import Videoweed


class TVPY(QDialog, ui_code.Ui_Dialog):
    def __init__(self, parent=None):
        super(TVPY, self).__init__(parent)
        self.setupUi(self)

        self.results = {}
        self.mode = None
        self.watch_series = WatchSeries()

        self.lst_results.itemDoubleClicked.connect(self.on_btn_select_clicked)

    @Slot()
    def on_btn_search_clicked(self):
        query = self.lne_search.text()

        if query:
            self.results = self.watch_series.search(query)

        self.update_results_list()
        self.mode = 'show'
        self.info_label.setText('Search results for:{}'.format(query))
        self.btn_select.setText('Select')

    @Slot()
    def on_btn_select_clicked(self):
        if self.mode == 'show':
            selected_show = self.lst_results.selectedItems()[0]
            if not selected_show:
                return

            selected = self.results.get(selected_show.text())
            if not selected:
                return
            else:
                self.results = self.watch_series.parse_show(selected)
                self.update_results_list()

        if self.mode == 'episode':
            selected_episode = self.lst_results.selectedItems()[0]
            if not selected_episode:
                return

            selected = self.results.get(selected_episode.text())
            if not selected:
                return
            else:
                host_url = self.watch_series.get_hoster_link(selected)
                self.get_start_stream(host_url)

    def get_start_stream(self, host_url):
        hoster = Videoweed(host_url)
        file_location = hoster.get_direct_link()
        if file_location:
            os.system("parole {}".format(file_location))

    def update_results_list(self):
        self.lst_results.clear()
        if self.results is None:
            self.lst_results.addItem("Nothing found")
            return

        if self.mode == 'show':
            self.mode = 'episode'
        else:
            self.mode = 'show'
        for item in sorted(self.results.keys()):
            self.lst_results.addItem(item)


def main():
    app = QApplication(sys.argv)
    form = TVPY()
    form.show()
    app.exec_()


if __name__ == "__main__":
    main()