from PyQt5.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QLabel,
                             QPushButton, QLineEdit, QWidget, QTextEdit, QHBoxLayout)
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

        # Main layout
        main_layout = QVBoxLayout()

          # Event Name Header
        self.event_header_label = QLabel("Event Name", self)
        self.event_header_label.setAlignment(Qt.AlignCenter)
        self.event_header_label.setStyleSheet(
            "font-size: 24px; font-weight: bold; margin-bottom: 20px;")
        main_layout.addWidget(self.event_header_label)

        # Viewing as Host Label
        self.viewing_as_host_label = QLabel("Viewing as Host", self)
        self.viewing_as_host_label.setAlignment(Qt.AlignRight)
        self.viewing_as_host_label.setStyleSheet("margin-right: 10px; margin-top: -20px; margin-bottom: 20px;")
        main_layout.addWidget(self.viewing_as_host_label)

        # Placeholder for Map
        self.map_placeholder_label = QLabel("Location of event map(Xavier)", self)
        self.map_placeholder_label.setAlignment(Qt.AlignCenter)
        self.map_placeholder_label.setStyleSheet(
            "background-color: #e0e0e0; padding: 50px; margin-bottom: 20px;")
        main_layout.addWidget(self.map_placeholder_label)

        # Event Information Text Box
        self.event_info_text_box = QTextEdit(self)
        self.event_info_text_box.setPlaceholderText("Display Info about Event")
        self.event_info_text_box.setReadOnly(True)
        main_layout.addWidget(self.event_info_text_box)

        # Join Event Button
        self.join_event_button = QPushButton("Join Event", self)
        main_layout.addWidget(self.join_event_button)

        # Horizontal layout for Edit and Cancel buttons
        button_layout = QHBoxLayout()
        self.edit_event_button = QPushButton("Edit Event", self)
        self.cancel_event_button = QPushButton("Cancel Event", self)
        button_layout.addWidget(self.edit_event_button)
        button_layout.addWidget(self.cancel_event_button)
        
        # Add the button layout to the main layout
        main_layout.addLayout(button_layout)

        # Set the layout for the central widget
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

# Run the application
def main():
    app = QApplication(sys.argv)
    window = EventWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
