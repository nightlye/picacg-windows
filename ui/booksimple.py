# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'booksimple.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BookSimple(object):
    def setupUi(self, BookSimple):
        BookSimple.setObjectName("BookSimple")
        BookSimple.resize(725, 500)
        BookSimple.setMinimumSize(QtCore.QSize(0, 0))
        BookSimple.setStyleSheet("background:transparent;border:2px solid red;")
        self.horizontalLayout = QtWidgets.QHBoxLayout(BookSimple)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.title = QtWidgets.QLabel(BookSimple)
        self.title.setObjectName("title")
        self.verticalLayout.addWidget(self.title)
        self.autor = QtWidgets.QLabel(BookSimple)
        self.autor.setObjectName("autor")
        self.verticalLayout.addWidget(self.autor)
        self.category = QtWidgets.QLabel(BookSimple)
        self.category.setObjectName("category")
        self.verticalLayout.addWidget(self.category)
        self.pushButton = QtWidgets.QPushButton(BookSimple)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.gridLayout.addLayout(self.verticalLayout, 1, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 1, 1, 1)
        self.picture = QtWidgets.QLabel(BookSimple)
        self.picture.setMinimumSize(QtCore.QSize(240, 480))
        self.picture.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.picture.setObjectName("picture")
        self.gridLayout.addWidget(self.picture, 1, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)

        self.retranslateUi(BookSimple)
        self.pushButton.clicked.connect(BookSimple.OpenBookInfo)
        QtCore.QMetaObject.connectSlotsByName(BookSimple)

    def retranslateUi(self, BookSimple):
        _translate = QtCore.QCoreApplication.translate
        BookSimple.setWindowTitle(_translate("BookSimple", "Form"))
        self.title.setText(_translate("BookSimple", "TextLabel"))
        self.autor.setText(_translate("BookSimple", "TextLabel"))
        self.category.setText(_translate("BookSimple", "TextLabel"))
        self.pushButton.setText(_translate("BookSimple", "打开"))
        self.picture.setText(_translate("BookSimple", "TextLabel"))
