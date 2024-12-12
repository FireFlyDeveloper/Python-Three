from PyQt5 import QtCore, QtGui, QtWidgets

from helper.CRUD import CRUD
from models.SQLquery import SQLquery
from ui.new import NewCustomerDialog

class Home(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.crud = CRUD()
        self.crud.setup()

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

        # Dashboard Label 1
        self.Dashboard_label = QtWidgets.QLabel("Current :", self)
        self.Dashboard_label.setFont(QtGui.QFont("Blank's Script Personal Use", 20))
        self.Dashboard_label.setStyleSheet("color: black;")
        self.Dashboard_label.setGeometry(480, 5, 300, 50)

        self.Dashboard_label_text = QtWidgets.QLabel("N/A", self)
        self.Dashboard_label_text.setFont(QtGui.QFont("Poppins", 15))
        self.Dashboard_label_text.setStyleSheet("color: black;")
        self.Dashboard_label_text.setGeometry(480, 40, 225, 50)

        self.Dashboard_label_text2 = QtWidgets.QLabel("N/A", self)
        self.Dashboard_label_text2.setFont(QtGui.QFont("Poppins", 15))
        self.Dashboard_label_text2.setStyleSheet("color: black;")
        self.Dashboard_label_text2.setGeometry(480, 70, 225, 50)

        self.Dashboard_label2 = QtWidgets.QLabel("Total :", self)
        self.Dashboard_label2.setFont(QtGui.QFont("Blank's Script Personal Use", 20))
        self.Dashboard_label2.setStyleSheet("color: black;")
        self.Dashboard_label2.setGeometry(750, 5, 300, 50)

        self.Dashboard_label2_text = QtWidgets.QLabel("0", self)
        self.Dashboard_label2_text.setFont(QtGui.QFont("Poppins", 40))
        self.Dashboard_label2_text.setStyleSheet("color: black;")
        self.Dashboard_label2_text.setGeometry(750, 50, 300, 70)

        # Panel 2
        self.panel2 = QtWidgets.QWidget(self)
        self.panel2.setGeometry(880, 10, 400, 110)  # Position and size of the panel
        self.panel2.setStyleSheet("""
            background-color: rgba(255, 255, 255, 0.9);  /* White with transparency */
            border: 2px solid #000;                      /* Black border */
            border-radius: 15px;                         /* Rounded corners */
        """)

        # Dashboard 2
        self.Dashboard2_label = QtWidgets.QLabel("Recent :", self)
        self.Dashboard2_label.setFont(QtGui.QFont("Blank's Script Personal Use", 20))
        self.Dashboard2_label.setStyleSheet("color: black;")
        self.Dashboard2_label.setGeometry(900, 5, 300, 50)

        self.Dashboard2_label_text = QtWidgets.QLabel("N/A", self)
        self.Dashboard2_label_text.setFont(QtGui.QFont("Poppins", 15))
        self.Dashboard2_label_text.setStyleSheet("color: black;")
        self.Dashboard2_label_text.setGeometry(900, 40, 225, 50)

        self.Dashboard2_label_text2 = QtWidgets.QLabel("N/A", self)
        self.Dashboard2_label_text2.setFont(QtGui.QFont("Poppins", 15))
        self.Dashboard2_label_text2.setStyleSheet("color: black;")
        self.Dashboard2_label_text2.setGeometry(900, 70, 225, 50)

        self.Dashboard2_label2 = QtWidgets.QLabel("Total :", self)
        self.Dashboard2_label2.setFont(QtGui.QFont("Blank's Script Personal Use", 20))
        self.Dashboard2_label2.setStyleSheet("color: black;")
        self.Dashboard2_label2.setGeometry(1170, 5, 300, 50)

        self.Dashboard2_label2_text = QtWidgets.QLabel("0", self)
        self.Dashboard2_label2_text.setFont(QtGui.QFont("Poppins", 40))
        self.Dashboard2_label2_text.setStyleSheet("color: black;")
        self.Dashboard2_label2_text.setGeometry(1170, 50, 300, 70)

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

        self.updateTable()

        self.done_button = QtWidgets.QPushButton("Done", self)
        self.done_button.setGeometry(500, 140, 100, 30)
        self.done_button.setFont(QtGui.QFont("Poppins", 12))
        self.done_button.clicked.connect(self.remove_first_row_from_queue)

        self.new_button = QtWidgets.QPushButton("New", self)
        self.new_button.setGeometry(400, 140, 100, 30)
        self.new_button.setFont(QtGui.QFont("Poppins", 12))
        self.new_button.clicked.connect(self.open_new_customer_dialog)

    def center_window(self):
        # Get screen geometry
        screen = QtWidgets.QApplication.primaryScreen().geometry()

        # Calculate x, y for centering
        x = (screen.width() - self.width()) // 2
        y = (screen.height() - self.height()) // 2

        # Move the window to the center
        self.move(x, y)

    def updateTable(self):
        data1 = self.crud.read()

        # Reset the table rows
        self.table.setRowCount(0)
        self.table2.setRowCount(0)

        # Separate rows into priority and regular queues
        priority_data = [user for user in data1 if user.queue_type == 'priority']
        regular_data = [user for user in data1 if user.queue_type == 'regular']

        priority_data.reverse()

        count1 = 0  # Start count from 0
        count2 = 0  # Start count from 0

        done = []

        # Populate the tables with sorted data
        for user in priority_data:
            if not user.done:  # User is not done, add to table
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

                count1 += 1  # Increment count for table

            else:
                done.append(user)

        # Populate the regular queue
        for user in regular_data:
            if not user.done:  # User is not done, add to table
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

                count1 += 1  # Increment count for table

            else:
                done.append(user)

        done.reverse()

        for user in done:
            self.table2.insertRow(count2)
            self.table2.setItem(count2, 0, QtWidgets.QTableWidgetItem(str(user.id)))  # ID
            self.table2.setItem(count2, 1, QtWidgets.QTableWidgetItem(user.name))       # Name
            self.table2.setItem(count2, 2, QtWidgets.QTableWidgetItem(user.number))     # Number
            self.table2.setItem(count2, 3, QtWidgets.QTableWidgetItem(user.email))      # Email
            self.table2.setItem(count2, 4, QtWidgets.QTableWidgetItem(str(user.price))) # Price
            self.table2.setItem(count2, 5, QtWidgets.QTableWidgetItem(user.date))       # Date

            for col_idx in range(6):
                item = self.table2.item(count2, col_idx)
                item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)  # Make non-editable

            count2 += 1

        self.Dashboard_label_text.setText("N/A")
        self.Dashboard_label_text2.setText("N/A")
        self.Dashboard_label2_text.setText(f"{count1}")

        self.Dashboard2_label_text.setText("N/A")
        self.Dashboard2_label_text2.setText("N/A")
        self.Dashboard2_label2_text.setText(f"{count2}")

        if self.table.rowCount() > 0:
            self.Dashboard_label_text.setText(self.table.item(0, 1).text())
            self.Dashboard_label_text2.setText(self.table.item(0, 2).text())
            for col_idx in range(6):  # Loop through all columns for the first row
                item = self.table.item(0, col_idx)
                item.setBackground(QtGui.QColor(255, 255, 0))

        if self.table2.rowCount() > 0:
            self.Dashboard2_label_text.setText(self.table2.item(0, 1).text())
            self.Dashboard2_label_text2.setText(self.table2.item(0, 2).text())


    def add_row_to_queue(self, customer):
        # Get the last inserted ID from the database and increment by 1
        new_id = self.crud.get_last_inserted_id() + 1 if self.crud.get_last_inserted_id() else 1
        
        # Create the new customer object with done = False (indicating it's in the regular queue)
        sql = SQLquery(new_id, customer.name, customer.number, customer.email, customer.price, customer.date, False, 'regular')
        
        # Insert into the database with regular queue flag
        if self.crud.create(sql):
            # Row inserted successfully, reload data and update the table
            self.updateTable()  # Update the table with the latest data
            print("Row successfully added to the regular queue.")
        else:
            print("Failed to add row to the database.")

    def add_row_to_priority_queue(self, customer):
        # Get the last inserted ID from the database and increment by 1
        new_id = self.crud.get_last_inserted_id() + 1 if self.crud.get_last_inserted_id() else 1
        
        # Create the new customer object with done = False (indicating it's in the priority queue)
        sql = SQLquery(new_id, customer.name, customer.number, customer.email, customer.price, customer.date, False, 'priority')
        
        # Insert into the database with priority queue flag
        if self.crud.create(sql):
            print("Row successfully added to the priority queue.")
            
            # Reload the data and update the table
            self.updateTable()  # Update the table with the latest data
        else:
            print("Failed to add row to the database.")

    def remove_first_row_from_queue(self):
        if self.table.rowCount() > 0:
            # Remove the first row from the table
            row_data = [
                self.table.item(0, col_idx).text() for col_idx in range(self.table.columnCount())
            ]

            # Update the database to mark the record as completed
            sql = SQLquery(
                int(row_data[0]), row_data[1], row_data[2], row_data[3], float(row_data[4]), row_data[5], True, 'regular'
            )

            if self.crud.update(sql):
                # Move the row to the second table
                self.updateTable()
                print("First row successfully moved to completed queue.")
            else:
                print("Failed to update row in the database.")

    def open_new_customer_dialog(self):
        dialog = NewCustomerDialog(self)
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            self.updateTable()
