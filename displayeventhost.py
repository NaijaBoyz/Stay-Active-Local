from PyQt5.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QLabel, QPushButton, QWidget, QTextEdit, QHBoxLayout)
from PyQt5.QtCore import Qt
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
import sys
from backendfunctions import add_attendee_to_event, cancel_event
from PyQt5.QtWidgets import QMessageBox 

class EventWindow(QMainWindow):
    def __init__(self, event_data, user_id, parent=None):
        super(EventWindow, self).__init__(parent)
        self.event_data = event_data
        self.user_id = user_id 
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Event Details")
        self.setGeometry(100, 100, 600, 800)  # Adjust size as needed

        # Main layout
        main_layout = QVBoxLayout()

        # Event Name Header
        event_name = self.event_data.get("Event Name", "Unknown Event")
        self.event_header_label = QLabel(event_name, self)
        self.event_header_label.setAlignment(Qt.AlignCenter)
        self.event_header_label.setStyleSheet("font-size: 24px; font-weight: bold; margin-bottom: 20px;")
        main_layout.addWidget(self.event_header_label)

        # Viewing as Host Label
        self.viewing_as_host_label = QLabel("Viewing as Host", self)
        self.viewing_as_host_label.setAlignment(Qt.AlignRight)
        self.viewing_as_host_label.setStyleSheet("margin-right: 10px; margin-top: -20px; margin-bottom: 20px;")
        main_layout.addWidget(self.viewing_as_host_label)

        # Map Display
        self.map_view = QWebEngineView(self)
        map_url = "http://maps.google.com/?q={}".format(self.event_data.get("Location", ""))
        self.map_view.load(QUrl(map_url))
        self.map_view.setFixedHeight(200)  # Set the map height
        main_layout.addWidget(self.map_view)

        # Event Information Text Box
        description = self.event_data.get("Description", "No description provided.")
        self.event_info_text_box = QTextEdit(description, self)
        self.event_info_text_box.setReadOnly(True)
        main_layout.addWidget(self.event_info_text_box)

        # Join Event Button
        self.join_event_button = QPushButton("Join Event", self)
   
        self.join_event_button.clicked.connect(self.joinEvent)

        main_layout.addWidget(self.join_event_button)

        # Horizontal layout for Edit and Cancel buttons
        button_layout = QHBoxLayout()
        self.edit_event_button = QPushButton("Edit Event", self)
        self.cancel_event_button = QPushButton("Cancel Event", self)
        button_layout.addWidget(self.edit_event_button)
        button_layout.addWidget(self.cancel_event_button)
        self.cancel_event_button.clicked.connect(self.cancelEvent)
        
        # Add the button layout to the main layout
        main_layout.addLayout(button_layout)

        # Set the layout for the central widget
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def joinEvent(self):
            # Call the backend function to add the attendee
            event_id = self.event_data.get("id")  # Get event ID from event_data
            add_attendee_to_event(event_id, self.user_id)
            print("Joined the event:", event_id)
            QMessageBox.information(self, "Event Joined", "You have successfully joined the event!")

    def cancelEvent(self):
        event_id = self.event_data.get("id")  # Get event ID from event_data
        success, message = cancel_event(event_id)
        if success:
            QMessageBox.information(self, "Event Cancelled", message)
            # You might want to close the window or update the UI here
        else:
            QMessageBox.warning(self, "Cancellation Failed", message)


# Run the application
def main():
    app = QApplication(sys.argv)
    # Example event data, replace with actual data
    event_data = {
        "Event Name": "Community Soccer Game",
        "Location": "Central Park, New York",
        "Description": "Join us for a friendly soccer match at Central Park."
    }
    user_id=1
    window = EventWindow(event_data, user_id)
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
