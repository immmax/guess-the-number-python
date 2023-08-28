from PyQt6.QtWidgets import QMainWindow
from ui.py.launch_screen_ui import Ui_LaunchScreen
from controllers.game_controller import GameScreen


class LaunchScreen(QMainWindow, Ui_LaunchScreen):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_new_game.clicked.connect(self.start_game)
        self.pushButton_exit.clicked.connect(self.close)
        self.show()

    def start_game(self):
        self.game_screen = GameScreen(parent=self)
        self.game_screen.show()
        self.close()
