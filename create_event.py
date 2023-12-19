import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit, QTextEdit, QFormLayout, QSpinBox, QDoubleSpinBox, QComboBox, QDialog, QMessageBox
from backendfunctions import create_event  # Make sure this import is correct based on your project structure
from PyQt5.QtWidgets import QDateTimeEdit 
from PyQt5 import QtCore

class EventCreatorApp(QDialog):
    def __init__(self, user_id, parent=None):
        super(EventCreatorApp, self).__init__(parent)
        self.user_id = user_id  # Store the logged-in user's ID
        self.init_ui()

    def init_ui(self):
        self.setStyleSheet("""
            QDialog {
                background-color: #add8e6;
            }
            QLabel {
                font: bold 14px;
            }
            QLineEdit, QTextEdit, QSpinBox, QDoubleSpinBox, QComboBox, QPushButton {
                font: 14px;
                border: 1px solid #000;
                padding: 5px;
                background-color: #fff;
                margin-bottom: 10px;
            }
            QPushButton {
                background-color: #6495ed;
                color: #fff;
            }
            QPushButton:hover {
                background-color: #4169e1;
            }
        """)

        # Create labels and input fields for event information
        event_name_label = QLabel('Event Name:')
        self.event_name_input = QLineEdit()

        location_label = QLabel('Location:')
        self.location_input = QLineEdit()

        size_label = QLabel('Size of Party:')
        self.size_input = QSpinBox()

        age_label = QLabel('Age Requirement:')
        self.age_input = QSpinBox()

        cost_label = QLabel('Cost:')
        self.cost_input = QDoubleSpinBox()

        sport_label = QLabel('Sport:')
        self.sport_input = QComboBox()
        self.sport_input.addItems(['Football', 'Basketball', 'Soccer', 'Other'])

        description_label = QLabel('Description:')
        self.description_input = QTextEdit()

        date_time_label = QLabel('Date & Time:')
        self.date_time_input = QDateTimeEdit(self)
        self.date_time_input.setCalendarPopup(True)
        self.date_time_input.setDateTime(QtCore.QDateTime.currentDateTime())  # Set the current date and time as default


        # Create a button to create an event
        create_event_button = QPushButton('Create An Event', self)
        create_event_button.clicked.connect(self.create_event_clicked)

        # Set up the layout using QFormLayout
        layout = QFormLayout()
        layout.addRow(event_name_label, self.event_name_input)
        layout.addRow(location_label, self.location_input)
        layout.addRow(size_label, self.size_input)
        layout.addRow(age_label, self.age_input)
        layout.addRow(cost_label, self.cost_input)
        layout.addRow(sport_label, self.sport_input)
        layout.addRow(description_label, self.description_input)
        layout.addRow(create_event_button)
        layout.addRow(date_time_label, self.date_time_input)

        # Set the layout for the main window
        self.setLayout(layout)

        # Set window properties
        self.setWindowTitle('Event Creator')
        self.setGeometry(550, 300, 400, 300)

    def create_event_clicked(self):
    # Retrieve input values from the input fields
        event_name = self.event_name_input.text()
        location = self.location_input.text()
        size = self.size_input.value()
        age_requirement = self.age_input.value()
        cost = self.cost_input.value()
        sport = self.sport_input.currentText()
        description = self.description_input.toPlainText()
        date_time = self.date_time_input.dateTime().toString(QtCore.Qt.ISODate) # Example date, you might want to add a field for this

    # Call the backend function to create the event
        event_id = create_event(
            self.user_id, event_name, location, size, date_time, cost, sport, description, age_requirement
        )

        # Show a confirmation message or handle errors accordingly
        QMessageBox.information(self, 'Event Created', f'Your event has been created successfully! Event ID: {event_id}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # You need to pass the user ID when creating the EventCreatorApp
    # For demonstration, I'm passing a placeholder string
    ex = EventCreatorApp(user_id='your_user_id_here')
    ex.show()
    sys.exit(app.exec_())
