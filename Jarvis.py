# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Jarvis.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_JarvisUi(object):
    def setupUi(self, JarvisUi):
        JarvisUi.setObjectName("JarvisUi")
        JarvisUi.resize(1367, 676)
        self.centralwidget = QtWidgets.QWidget(JarvisUi)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, -80, 1421, 871))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("GUI/4.gif"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1060, 620, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1190, 620, 71, 23))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 411, 131))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("GUI/init sys.gif"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(920, 400, 471, 201))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("GUI/border.jpg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(80, 430, 371, 211))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("GUI/j.gif"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(960, 20, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser_3.setFont(font)
        self.textBrowser_3.setStyleSheet("background-color:transparent;\n"
"border-radius:none;\n"
"color :white;\n"
"font-size:20px")
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_4.setGeometry(QtCore.QRect(1100, 20, 141, 41))
        self.textBrowser_4.setStyleSheet("background-color:transparent;\n"
"border-radius:none;\n"
"color :white;\n"
"font-size:20px")
        self.textBrowser_4.setObjectName("textBrowser_4")
        JarvisUi.setCentralWidget(self.centralwidget)

        self.retranslateUi(JarvisUi)
        QtCore.QMetaObject.connectSlotsByName(JarvisUi)

    def retranslateUi(self, JarvisUi):
        _translate = QtCore.QCoreApplication.translate
        JarvisUi.setWindowTitle(_translate("JarvisUi", "MainWindow"))
        self.pushButton.setText(_translate("JarvisUi", "RUN"))
        self.pushButton_2.setText(_translate("JarvisUi", "STOP"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    JarvisUi = QtWidgets.QMainWindow()
    ui = Ui_JarvisUi()
    ui.setupUi(JarvisUi)
    JarvisUi.show()
    sys.exit(app.exec_())
