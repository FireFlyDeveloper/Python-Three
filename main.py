import sys
from PyQt5.QtWidgets import QApplication
from ui.login import Login

if __name__ == "__main__":
    app = QApplication(sys.argv)  # Create a Qt application
    window = Login()  # Instantiate the Login window
    window.show()  # Show the window
    sys.exit(app.exec_())