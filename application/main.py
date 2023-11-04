import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

def get_previous_number():
    previous_number = 0  # Default value
    if os.path.exists("disk.txt"):
        with open("disk.txt", "r") as file:
            previous_number = int(file.read())
    return previous_number

def save_total_number(total_number):
    with open("disk.txt", "w") as file:
        file.write(str(total_number))

class TotalNumberApp(QWidget):
    def __init__(self):
        super().__init__()

        self.previous_number = get_previous_number()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Format of the application
        self.label = QLabel(f"Previous total number: {self.previous_number}")
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Enter a number")
        self.calculate_button = QPushButton("Calculate total")

        layout.addWidget(self.label)
        layout.addWidget(self.input_field)
        layout.addWidget(self.calculate_button)

        # Call function when button is pressed
        self.calculate_button.clicked.connect(self.calculate_total)

        self.setLayout(layout)
        self.setWindowTitle("Total number calculator")
        self.show()

    def calculate_total(self):
        entered_number = self.input_field.text()
        # Preforming a check to see if the entered number is an integer
        try:
            entered_number = int(entered_number)
            total_number = self.previous_number + entered_number
            if total_number > 152:
                total_number -= 152

            self.label.setText(f"Total number: {total_number}")
            save_total_number(total_number)
            self.previous_number = total_number
        except ValueError:
            self.label.setText("Please enter an integer")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TotalNumberApp()
    sys.exit(app.exec_())
