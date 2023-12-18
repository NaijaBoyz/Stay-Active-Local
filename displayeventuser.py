from PyQt5.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QLabel,
                             QPushButton, QLineEdit, QWidget, QTextEdit)
from PyQt5.QtCore import Qt
import sys

# Define the PyQt window class
class EventWindow(QMainWindow):
    def __init__(self, parent=None):
        super(EventWindow, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Event Details")
        self.setGeometry(100, 100, 600, 800)  # Adjust size as needed

        # Create the layout
        layout = QVBoxLayout()

        # Event Name Header
        self.event_header_label = QLabel("Event Name", self)
        self.event_header_label.setAlignment(Qt.AlignCenter)
        self.event_header_label.setStyleSheet(
            "font-size: 24px; font-weight: bold; margin-bottom: 20px;")
        layout.addWidget(self.event_header_label)

        # Placeholder for Map
        self.map_placeholder_label = QLabel("Map will be displayed here.", self)
        self.map_placeholder_label.setAlignment(Qt.AlignCenter)
        self.map_placeholder_label.setStyleSheet(
            "background-color: #e0e0e0; padding: 100px; margin-bottom: 20px;")
        layout.addWidget(self.map_placeholder_label)

        # Event Information Text Box
        self.event_info_text_box = QTextEdit(self)
        self.event_info_text_box.setPlaceholderText("Information about the event will be displayed here.")
        self.event_info_text_box.setReadOnly(True)
        layout.addWidget(self.event_info_text_box)

        # Join Event Button
        self.join_event_button = QPushButton("Join Event", self)
        self.join_event_button.setStyleSheet(
            "font-size: 18px; font-weight: bold; padding: 10px; margin-top: 20px;")
        layout.addWidget(self.join_event_button)

        # Set the layout for the central widget
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

# Run the application
def main():
    app = QApplication(sys.argv)
    window = EventWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
