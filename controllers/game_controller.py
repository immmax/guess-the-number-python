from random import randint
from PyQt6.QtWidgets import QMainWindow, QMessageBox
from ui.py.game_screen_ui import Ui_GameScreen
from lexicon.lexicon import WarningMessage, HigherNumber, LowerNumber,\
                            WinMessage, LoseMessage, InitMessage

class GameScreen(QMainWindow, Ui_GameScreen):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.setupUi(self)
        self.init_state()
        self.pushButton_guess.clicked.connect(self.guess)
        self.show()

    def guess(self):
        result = None
        self.attempts -= 1
        try:
            user_number = int(self.lineEdit_user_input.text())
        except Exception as e:
            QMessageBox.information(self,
                                    WarningMessage.header,
                                    WarningMessage.body,
                                    QMessageBox.StandardButton.Ok)
            print(e)
            return
        if user_number == self.number:
            winMessage = WinMessage(number=self.number)
            result = QMessageBox.information(self,
                                             winMessage.header,
                                             winMessage.body,
                                             QMessageBox.StandardButton.Yes,
                                             QMessageBox.StandardButton.No)
        elif user_number > self.number:
            self.label_robot_answer.setText(LowerNumber(self.attempts).text)
        else:
            self.label_robot_answer.setText(HigherNumber(self.attempts).text)

        if self.attempts == 0:
            loseMessage = LoseMessage(number=self.number)
            result = QMessageBox.information(self,
                                             loseMessage.header,
                                             loseMessage.body,
                                             QMessageBox.StandardButton.Yes,
                                             QMessageBox.StandardButton.No)

            if result == QMessageBox.StandardButton.Yes:
                self.init_state()
            elif result == QMessageBox.StandardButton.No:
                self.parent.show()
                self.close()
                return

    def init_state(self):
        self.attempts = 7
        self.number = randint(0, 100)
        print(self.number)
        self.label_robot_answer.setText(InitMessage(attempts=self.attempts).text)
