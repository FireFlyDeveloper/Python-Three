from PyQt5 import QtWidgets, QtGui

from models.SQLquery import SQLquery

class NewCustomerDialog(QtWidgets.QDialog):
    def __init__(self, home, parent=None):
        super().__init__(parent)
        self.home = home
        self.setWindowTitle("Add New Customer")

        # Create the layout
        layout = QtWidgets.QVBoxLayout()

        # Title Label
        self.title_label = QtWidgets.QLabel("Add new customer")
        self.title_label.setFont(QtGui.QFont("Segoe UI", 12, QtGui.QFont.Bold))
        layout.addWidget(self.title_label)

        # Create form fields
        self.name_input = QtWidgets.QLineEdit()
        self.name_input.setPlaceholderText("Name")
        self.number_input = QtWidgets.QLineEdit()
        self.number_input.setPlaceholderText("No.")
        self.email_input = QtWidgets.QLineEdit()
        self.email_input.setPlaceholderText("Email")
        self.year_input = QtWidgets.QLineEdit()
        self.year_input.setPlaceholderText("Year")
        self.month_input = QtWidgets.QLineEdit()
        self.month_input.setPlaceholderText("Month")
        self.day_input = QtWidgets.QLineEdit()
        self.day_input.setPlaceholderText("Day")
        self.price_input = QtWidgets.QLineEdit()
        self.price_input.setPlaceholderText("Price")

        # Add inputs to layout
        layout.addWidget(self.name_input)
        layout.addWidget(self.number_input)
        layout.addWidget(self.email_input)
        layout.addWidget(self.year_input)
        layout.addWidget(self.month_input)
        layout.addWidget(self.day_input)
        layout.addWidget(self.price_input)

        # Priority Checkbox
        self.priority_checkbox = QtWidgets.QCheckBox("Priority")
        layout.addWidget(self.priority_checkbox)

        # Done Button
        self.done_button = QtWidgets.QPushButton("Done")
        self.done_button.clicked.connect(self.on_done_button_click)
        layout.addWidget(self.done_button)

        self.setLayout(layout)
        self.setModal(True)
        self.setFixedSize(300, 350)

    def on_done_button_click(self):
        # Validate input fields
        name = self.name_input.text().strip()
        number = self.number_input.text().strip()
        email = self.email_input.text().strip()
        year = self.year_input.text().strip()
        month = self.month_input.text().strip()
        day = self.day_input.text().strip()
        price = self.price_input.text().strip()

        if not all([name, number, email, year, month, day, price]):
            QtWidgets.QMessageBox.warning(self, "Input Required", "Please complete all the fields.")
            return

        # Capitalize name
        name = self.capitalize_first(name)

        # Validate the date
        try:
            year, month, day = int(year), int(month), int(day)

            if month < 1 or month > 12:
                raise ValueError("Month must be between 1 and 12.")

            if day < 1 or day > 31:
                raise ValueError("Day must be between 1 and 31.")

            if month in [4, 6, 9, 11] and day > 30:
                raise ValueError("This month has only 30 days.")

            if month == 2:
                if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                    if day > 29:
                        raise ValueError("February in a leap year has only 29 days.")
                else:
                    if day > 28:
                        raise ValueError("February has only 28 days.")

        except ValueError as e:
            QtWidgets.QMessageBox.warning(self, "Invalid Date", str(e))
            return

        # Validate the price
        try:
            price = float(price)
            if price <= 0:
                raise ValueError("Price must be greater than 0.")
        except ValueError:
            QtWidgets.QMessageBox.warning(self, "Invalid Price", "Please enter a valid price.")
            return

        date = f"{year:04d}-{month:02d}-{day:02d}"

        customer = SQLquery(None, name, number, email, price, date, False)

        # Add to home queue (this part depends on your Home class logic)
        if self.priority_checkbox.isChecked():
            self.home.add_row_to_priority_queue(customer)
        else:
            self.home.add_row_to_queue(customer)

        self.accept()

    def capitalize_first(self, text):
        return text.title()