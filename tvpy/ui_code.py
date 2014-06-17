# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design/main.ui'
#
# Created: Tue Jun 17 22:12:20 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(426, 493)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.search_layout = QtGui.QHBoxLayout()
        self.search_layout.setObjectName("search_layout")
        self.lne_search = QtGui.QLineEdit(Dialog)
        self.lne_search.setObjectName("lne_search")
        self.search_layout.addWidget(self.lne_search)
        self.btn_search = QtGui.QPushButton(Dialog)
        self.btn_search.setObjectName("btn_search")
        self.search_layout.addWidget(self.btn_search)
        self.verticalLayout.addLayout(self.search_layout)
        self.info_label = QtGui.QLabel(Dialog)
        self.info_label.setTextFormat(QtCore.Qt.PlainText)
        self.info_label.setObjectName("info_label")
        self.verticalLayout.addWidget(self.info_label)
        self.lst_results = QtGui.QListWidget(Dialog)
        self.lst_results.setObjectName("lst_results")
        self.verticalLayout.addWidget(self.lst_results)
        self.nex_prev_ep_layout = QtGui.QHBoxLayout()
        self.nex_prev_ep_layout.setObjectName("nex_prev_ep_layout")
        self.verticalLayout.addLayout(self.nex_prev_ep_layout)
        self.line_watch = QtGui.QFrame(Dialog)
        self.line_watch.setFrameShape(QtGui.QFrame.HLine)
        self.line_watch.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_watch.setObjectName("line_watch")
        self.verticalLayout.addWidget(self.line_watch)
        self.btn_select = QtGui.QPushButton(Dialog)
        self.btn_select.setEnabled(True)
        self.btn_select.setObjectName("btn_select")
        self.verticalLayout.addWidget(self.btn_select)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.lne_search, self.btn_search)
        Dialog.setTabOrder(self.btn_search, self.lst_results)
        Dialog.setTabOrder(self.lst_results, self.btn_select)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(
            QtGui.QApplication.translate("Dialog", "TVPY", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.btn_search.setText(
            QtGui.QApplication.translate("Dialog", "Search", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.info_label.setText(
            QtGui.QApplication.translate("Dialog", "TextLabel", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.btn_select.setText(
            QtGui.QApplication.translate("Dialog", "Select", None,
                                         QtGui.QApplication.UnicodeUTF8))

