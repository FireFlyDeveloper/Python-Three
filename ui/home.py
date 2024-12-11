from PyQt5 import QtCore, QtGui, QtWidgets

from helper.CRUD import CRUD
from models.SQLquery import SQLquery

class Home(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.crud = CRUD()
        self.crud.setup()
        self.users = self.crud.read()

        self.setWindowTitle("Home")
        self.setFixedSize(1300, 800)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.center_window()

        # Background Image
        self.background_label = QtWidgets.QLabel(self)
        self.background_pixmap = QtGui.QPixmap("res/bubble.png")
        self.background_pixmap = self.background_pixmap.scaled(
            1300, 800, QtCore.Qt.KeepAspectRatioByExpanding, QtCore.Qt.SmoothTransformation
        )
        self.background_label.setPixmap(self.background_pixmap)

        self.panel = QtWidgets.QWidget(self)
        self.panel.setGeometry(0, 0, 1300, 110)  # Position and size of the panel
        self.panel.setStyleSheet("""
            background-color: rgba(0, 0, 0, 0.1);  /* White with transparency */
        """)

        # Apply Blur Effect
        blur_effect = QtWidgets.QGraphicsBlurEffect(self)
        blur_effect.setBlurRadius(50)
        self.panel.setGraphicsEffect(blur_effect)

        # Logo
        self.logo_label = QtWidgets.QLabel(self)
        self.logo_pixmap = QtGui.QPixmap("res/logo.png").scaled(70, 70, QtCore.Qt.KeepAspectRatio)  # Path to the logo image
        self.logo_label.setPixmap(self.logo_pixmap)
        self.logo_label.setGeometry(25, 25, 70, 70)

        # Title
        self.title_label = QtWidgets.QLabel("Washing Well", self)
        self.title_label.setFont(QtGui.QFont("Blank's Script Personal Use", 40))
        self.title_label.setStyleSheet("color: white;")
        self.title_label.setGeometry(125, 15, 300, 80)

        # Apply Blur Effect
        blur_effect = QtWidgets.QGraphicsBlurEffect(self)
        blur_effect.setBlurRadius(10)
        self.background_label.setGraphicsEffect(blur_effect)

        # Panel 1
        self.panel1 = QtWidgets.QWidget(self)
        self.panel1.setGeometry(460, 10, 400, 110)  # Position and size of the panel
        self.panel1.setStyleSheet("""
            background-color: rgba(255, 255, 255, 0.9);  /* White with transparency */
            border: 2px solid #000;                      /* Black border */
            border-radius: 15px;                         /* Rounded corners */
        """)

        # Panel 2
        self.panel2 = QtWidgets.QWidget(self)
        self.panel2.setGeometry(880, 10, 400, 110)  # Position and size of the panel
        self.panel2.setStyleSheet("""
            background-color: rgba(255, 255, 255, 0.9);  /* White with transparency */
            border: 2px solid #000;                      /* Black border */
            border-radius: 15px;                         /* Rounded corners */
        """)

        ###################################################################

        # Scrollable Table Widget
        self.table = QtWidgets.QTableWidget(self)
        self.table.setGeometry(20, 180, 615, 600)  # Position and size
        self.table.setColumnCount(6)  # Set number of columns

        # Set column headers
        self.table.setHorizontalHeaderLabels(["ID", "Name", "Number", "Email", "Price", "Date"])
        self.table.setColumnHidden(0, True)

        self.table.setFont(QtGui.QFont("Poppins", 12))
        self.table.horizontalHeader().setStyleSheet("font: 12pt 'Poppins';")

        # Set appearance
        self.table.setAlternatingRowColors(True)
        self.table.setStyleSheet("alternate-background-color: #f2f2f2; background-color: #ffffff;")
        self.table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)  # Stretch columns to fit

        ###################################################################

        # Scrollable Table Widget
        self.table2 = QtWidgets.QTableWidget(self)
        self.table2.setGeometry(660, 180, 615, 600)  # Position and size
        self.table2.setColumnCount(6)  # Set number of columns

        # Set column headers
        self.table2.setHorizontalHeaderLabels(["ID", "Name", "Number", "Email", "Price", "Date"])
        self.table2.setColumnHidden(0, True)

        self.table2.setFont(QtGui.QFont("Poppins", 12))
        self.table2.horizontalHeader().setStyleSheet("font: 12pt 'Poppins';")

        # Set appearance
        self.table2.setAlternatingRowColors(True)
        self.table2.setStyleSheet("alternate-background-color: #f2f2f2; background-color: #ffffff;")
        self.table2.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)  # Stretch columns to fit

        # new_user = SQLquery(None, "Jane Doe", "0987654321", "jane.doe@example.com", 25.99, "2024-12-11", True)
        # self.crud.create(new_user)

        self.updateTable(self.users)


    def center_window(self):
        # Get screen geometry
        screen = QtWidgets.QApplication.primaryScreen().geometry()

        # Calculate x, y for centering
        x = (screen.width() - self.width()) // 2
        y = (screen.height() - self.height()) // 2

        # Move the window to the center
        self.move(x, y)

    def updateTable(self, data1):
        # Reset the table rows
        self.table.setRowCount(0)
        self.table2.setRowCount(0)

        count1 = 0  # Start count from 0
        count2 = 0  # Start count from 0
        
        # Populate the tables with data
        for user in data1:
            if not user.done:  # User is not done, add to table1
                self.table.insertRow(count1)
                self.table.setItem(count1, 0, QtWidgets.QTableWidgetItem(str(user.id)))  # ID
                self.table.setItem(count1, 1, QtWidgets.QTableWidgetItem(user.name))       # Name
                self.table.setItem(count1, 2, QtWidgets.QTableWidgetItem(user.number))     # Number
                self.table.setItem(count1, 3, QtWidgets.QTableWidgetItem(user.email))      # Email
                self.table.setItem(count1, 4, QtWidgets.QTableWidgetItem(str(user.price))) # Price
                self.table.setItem(count1, 5, QtWidgets.QTableWidgetItem(user.date))       # Date
                
                # Make the row non-editable
                for col_idx in range(6):
                    item = self.table.item(count1, col_idx)
                    item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)  # Make non-editable

                count1 += 1  # Increment count for table1
                
            else:  # User is done, add to table2
                self.table2.insertRow(count2)
                self.table2.setItem(count2, 0, QtWidgets.QTableWidgetItem(str(user.id)))  # ID
                self.table2.setItem(count2, 1, QtWidgets.QTableWidgetItem(user.name))       # Name
                self.table2.setItem(count2, 2, QtWidgets.QTableWidgetItem(user.number))     # Number
                self.table2.setItem(count2, 3, QtWidgets.QTableWidgetItem(user.email))      # Email
                self.table2.setItem(count2, 4, QtWidgets.QTableWidgetItem(str(user.price))) # Price
                self.table2.setItem(count2, 5, QtWidgets.QTableWidgetItem(user.date))       # Date

                # Make the row non-editable
                for col_idx in range(6):
                    item = self.table2.item(count2, col_idx)
                    item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)  # Make non-editable

                count2 += 1  # Increment count for table2

        # Set background color for the first row in table1
        if count1 > 0:  # Ensure there is at least one row in table1
            for col_idx in range(6):  # Loop through all columns for the first row
                item = self.table.item(0, col_idx)
                item.setBackground(QtGui.QColor(255, 255, 0))