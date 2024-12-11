import sys
from PyQt5.QtWidgets import QApplication
from ui.home import Home

if __name__ == "__main__":
    app = QApplication(sys.argv)  # Create a Qt application
    window = Home()  # Instantiate the Login window
    window.show()  # Show the window
    sys.exit(app.exec_())