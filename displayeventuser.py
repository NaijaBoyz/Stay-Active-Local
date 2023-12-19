from PyQt5.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QLabel,
                             QPushButton, QLineEdit, QWidget, QTextEdit)
from PyQt5.QtCore import Qt
import sys
# displayeventuser.py
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QLabel, QPushButton, QTextEdit, QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

# Define the PyQt window class
class EventWindow(QMainWindow):
    def __init__(self, event_data, parent=None):
        super(EventWindow, self).__init__(parent)
        self.event_data = event_data
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Event Details")
        self.setGeometry(100, 100, 600, 400)  # Adjust size as needed

        # Create the layout
        layout = QVBoxLayout()

        # Event Name Header
        event_name = self.event_data.get("Event Name", "Unknown Event")
        self.event_header_label = QLabel(event_name, self)
        self.event_header_label.setAlignment(Qt.AlignCenter)
        self.event_header_label.setStyleSheet("font-size: 24px; font-weight: bold; margin-bottom: 20px;")
        layout.addWidget(self.event_header_label)

        # Map Display
        self.map_view = QWebEngineView(self)
        map_url = "http://maps.google.com/?q={}".format(self.event_data.get("Location", ""))
        self.map_view.load(QUrl(map_url))
        self.map_view.setFixedHeight(200)  # Set the map height
        layout.addWidget(self.map_view)

        # Event Information Text Box
        description = self.event_data.get("Description", "No description provided.")
        self.event_info_text_box = QTextEdit(description, self)
        self.event_info_text_box.setReadOnly(True)
        layout.addWidget(self.event_info_text_box)

        # Join Event Button
        self.join_event_button = QPushButton("Join Event", self)
        self.join_event_button.setStyleSheet("font-size: 18px; font-weight: bold; padding: 10px; margin-top: 20px;")
        layout.addWidget(self.join_event_button)

        # Set the layout for the central widget
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)


