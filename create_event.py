import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit, QTextEdit, QFormLayout, QSpinBox, QDoubleSpinBox, QComboBox, QDialog

class EventCreatorApp(QDialog):
    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)

        # Create a list to store event information
        self.event_list = []

        self.init_ui()

    def init_ui(self):
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

        # Set the layout for the main window
        self.setLayout(layout)

        # Set window properties
        self.setWindowTitle('Event Creator')
        self.setGeometry(550, 300, 400, 300)

        # Show the window
        #self.show()

    def create_event_clicked(self):
        # Retrieve input values from the input fields
        event_name = self.event_name_input.text()
        location = self.location_input.text()
        size = self.size_input.value()
        age_requirement = self.age_input.value()
        cost = self.cost_input.value()
        sport = self.sport_input.currentText()
        description = self.description_input.toPlainText()

        # Create a dictionary to store event information
        event_info = {
            'Event Name': event_name,
            'Location': location,
            'Size of Party': size,
            'Age Requirement': age_requirement,
            'Cost': cost,
            'Sport': sport,
            'Description': description
        }

        # Append/addthe dictionary to the event list
        self.event_list.append(event_info)

        # Optional, print the event list to verify the stored information
        print("Event List:")
        for event in self.event_list:
            print(event)

if __name__ == '__main__':
    #run the PyQt application
    app = QApplication(sys.argv)
    ex = EventCreatorApp()
    ex.show()
    sys.exit(app.exec_())
