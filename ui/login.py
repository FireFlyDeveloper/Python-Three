from PyQt5 import QtCore, QtGui, QtWidgets

from ui.home import Home

class Login(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login")
        self.setFixedSize(400, 500)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.center_window()

        # Background Image
        self.background_label = QtWidgets.QLabel(self)
        self.background_pixmap = QtGui.QPixmap("res/bubble.png")  # Path to the background image
        self.background_label.setPixmap(self.background_pixmap)
        self.background_label.setGeometry(0, 0, 400, 500)

        # Logo
        self.logo_label = QtWidgets.QLabel(self)
        self.logo_pixmap = QtGui.QPixmap("res/logo.png").scaled(70, 70, QtCore.Qt.KeepAspectRatio)  # Path to the logo image
        self.logo_label.setPixmap(self.logo_pixmap)
        self.logo_label.setGeometry(21, 20, 70, 70)

        # Username Field with Placeholder Text
        self.username_input = QtWidgets.QLineEdit(self)
        self.username_input.setPlaceholderText("User Name")
        self.username_input.setGeometry(94, 150, 200, 30)
        self.username_input.setFont(QtGui.QFont("Poppins", 12))
        self.username_input.setStyleSheet("background-color: white; color: black;")
        self.username_input.setAlignment(QtCore.Qt.AlignCenter)

        # Password Field with Placeholder Text
        self.password_input = QtWidgets.QLineEdit(self)
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_input.setPlaceholderText("Password")
        self.password_input.setGeometry(94, 200, 200, 30)
        self.password_input.setFont(QtGui.QFont("Poppins", 12))
        self.password_input.setStyleSheet("background-color: white; color: black;")
        self.password_input.setAlignment(QtCore.Qt.AlignCenter)

        # Login Button
        self.login_button = QtWidgets.QPushButton("Login", self)
        self.login_button.setGeometry(94, 250, 200, 30)
        self.login_button.setFont(QtGui.QFont("Poppins", 12))
        self.login_button.clicked.connect(self.login)

        # Exit Button
        self.exit_button = QtWidgets.QPushButton("Exit", self)
        self.exit_button.setGeometry(94, 400, 200, 30)
        self.exit_button.setFont(QtGui.QFont("Poppins", 12))
        self.exit_button.clicked.connect(self.exit_application)

        # Error Label
        self.error_label = QtWidgets.QLabel("", self)
        self.error_label.setFont(QtGui.QFont("Poppins", 12))
        self.error_label.setStyleSheet("color: red;")
        self.error_label.setGeometry(94, 300, 200, 30)

        # Title
        self.title_label = QtWidgets.QLabel("Washing Well", self)
        self.title_label.setFont(QtGui.QFont("Blank's Script Personal Use", 40))
        self.title_label.setStyleSheet("color: white;")
        self.title_label.setGeometry(100, 15, 300, 80)

    def login(self):
        username = self.username_input.text().strip()
        password = self.password_input.text()

        if username == "" or password == "":
            self.error_label.setText("Please fill both fields!")
        else:
            self.login_button.setText("Loading...")
            self.login_button.setEnabled(False)
            if username == "admin" and password == "password":
                self.open_home_screen()
            else:
                self.error_label.setText("Wrong username or password!")
                self.login_button.setText("Login")
                self.login_button.setEnabled(True)

    def open_home_screen(self):
        # Create and show the Home screen
        self.home_window = Home()  # Instantiate the Home window
        self.home_window.show()  # Show the Home window

        # Close the Login screen
        self.close()

    def exit_application(self):
        QtWidgets.QApplication.quit()

    def center_window(self):
        # Get screen geometry
        screen = QtWidgets.QApplication.primaryScreen().geometry()

        # Calculate x, y for centering
        x = (screen.width() - self.width()) // 2
        y = (screen.height() - self.height()) // 2

        # Move the window to the center
        self.move(x, y)
