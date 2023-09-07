from random import randint
from PyQt6.QtWidgets import QMainWindow, QMessageBox
from ui.py.game_screen_ui import Ui_GameScreen


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
        user_number = int(self.lineEdit_user_input.text())
        if user_number == self.number:
            result = QMessageBox.information(self, "Победа!",
                                             f"Вы угадали!\n\nБыло загадано\
                                              число {self.number}\
                                              \n\nХотите сыграть ещё?",
                                             QMessageBox.StandardButton.Yes,
                                             QMessageBox.StandardButton.No)
        elif user_number > self.number:
            self.label_robot_answer.setText(f"Загаданное число меньше!\
                \n\nОсталось {self.attempts} попыток.")
        else:
            self.label_robot_answer.setText(f"Загаданное число больше!\
                \n\nОсталось {self.attempts} попыток.")

        if self.attempts == 0:
            result = QMessageBox.information(self, "Поражение!",
                                             f"Жаль, но Вы не угадали!\n\n\
                                             Было загадано число {self.number}\
                                             \n\nХотите сыграть ещё?",
                                             QMessageBox.StandardButton.Yes,
                                             QMessageBox.StandardButton.No)

            if result == QMessageBox.StandardButton.Yes:
                self.init_state()
            else:
                self.parent.show()
                self.close()

    def init_state(self):
        self.attempts = 7
        self.number = randint(0, 100)
        self.label_robot_answer.setText(f"Я загадал число от 1 до 100.\n\n\
                                        У тебя {self.attempts} попыток.")
