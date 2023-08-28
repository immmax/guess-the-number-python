# Form implementation generated from reading ui file 'ui/qt/game_screen.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_GameScreen(object):
    def setupUi(self, GameScreen):
        GameScreen.setObjectName("GameScreen")
        GameScreen.resize(450, 300)
        GameScreen.setMinimumSize(QtCore.QSize(450, 300))
        GameScreen.setMaximumSize(QtCore.QSize(450, 300))
        GameScreen.setStyleSheet("QWidget{\n"
"    background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(0, 102, 153, 69), stop:0.375 rgba(0, 102, 153, 69), stop:0.423533 rgba(0, 102, 153, 145), stop:0.45 rgba(0, 102, 153, 208), stop:0.477581 rgba(0, 102, 153, 130), stop:0.518717 rgba(0, 102, 153, 130), stop:0.55 rgba(0, 102, 153, 255), stop:0.57754 rgba(0, 102, 153, 130), stop:0.625 rgba(0, 102, 153, 69), stop:1 rgba(0, 102, 153, 69));\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton{\n"
"    padding: 10px;\n"
"    border-radius: 15px;\n"
"    background-color: rgb(255, 159, 10);\n"
"    color: black;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"    background-color: rgba(255, 159, 10, 0.8);\n"
"}\n"
"\n"
"QGroupBox{\n"
"    background: transparent;\n"
"    border: 1px solid white;\n"
"    border-radius: 15px;\n"
"    text-align: center;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(parent=GameScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(429, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 2, 1, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_user_input = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_user_input.setObjectName("lineEdit_user_input")
        self.gridLayout.addWidget(self.lineEdit_user_input, 0, 1, 1, 1)
        self.pushButton_guess = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_guess.setMinimumSize(QtCore.QSize(100, 0))
        self.pushButton_guess.setObjectName("pushButton_guess")
        self.gridLayout.addWidget(self.pushButton_guess, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setStyleSheet("background-color: transparent;")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 3, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(429, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 1, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_robot_answer = QtWidgets.QLabel(parent=self.groupBox)
        self.label_robot_answer.setStyleSheet("background-color: transparent;")
        self.label_robot_answer.setObjectName("label_robot_answer")
        self.gridLayout_3.addWidget(self.label_robot_answer, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 1, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(429, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 4, 1, 1, 1)
        GameScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(GameScreen)
        QtCore.QMetaObject.connectSlotsByName(GameScreen)

    def retranslateUi(self, GameScreen):
        _translate = QtCore.QCoreApplication.translate
        GameScreen.setWindowTitle(_translate("GameScreen", "Числовая угадайка"))
        self.pushButton_guess.setText(_translate("GameScreen", "Угадать"))
        self.label_2.setText(_translate("GameScreen", "Ваше число:"))
        self.groupBox.setTitle(_translate("GameScreen", "Робот"))
        self.label_robot_answer.setText(_translate("GameScreen", "TextLabel"))
