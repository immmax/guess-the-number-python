import sys
from PyQt6.QtWidgets import QApplication
from controllers.launch_controller import LaunchScreen

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LaunchScreen()
    sys.exit(app.exec())
