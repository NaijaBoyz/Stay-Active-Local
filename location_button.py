import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QGraphicsView, QGraphicsScene, QGraphicsProxyWidget, QLineEdit
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage
from PyQt5.QtCore import QUrl

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Create a layout
        layout = QVBoxLayout()

        # Create a line edit for user input
        self.location_input = QLineEdit(self)
        self.location_input.setPlaceholderText("Enter location")
        layout.addWidget(self.location_input)

        # Create a button for searching
        search_button = QPushButton('Search', self)
        layout.addWidget(search_button)

        # Create two buttons
        button2 = QPushButton('Button 2', self)

        # Add buttons to the layout
        layout.addWidget(button2)

        # Set the layout for the main window
        self.setLayout(layout)

        # Create a member variable to store the reference to map_view
        self.map_view = None

        # Set up connections
        search_button.clicked.connect(self.search_location)
        button2.clicked.connect(self.button2_clicked)

    def search_location(self):
        # Get user input from the line edit
        location = self.location_input.text()

        # Create an instance of MapView
        self.map_view = MapView(location)

        # Show the map view
        self.map_view.show()

    def button2_clicked(self):
        print('Button 2 Clicked')

class MapView(QWidget):
    def __init__(self, location):
        super().__init__()

        # Create a layout for the map view
        layout = QVBoxLayout()

        # Create a QGraphicsView to embed the map
        map_view = QGraphicsView(self)
        scene = QGraphicsScene(self)

        # Create a QGraphicsProxyWidget to embed the QWebEngineView
        proxy_widget = QGraphicsProxyWidget()
        web_engine_view = QWebEngineView()

        # Construct the OpenStreetMap URL
        url = QUrl.fromUserInput(f'https://www.openstreetmap.org/?query={location}')

        # Load the URL in the QWebEngineView
        web_engine_view.setUrl(url)

        # Add the proxy widget to the scene
        proxy_widget.setWidget(web_engine_view)
        scene.addItem(proxy_widget)

        # Set the scene for the QGraphicsView
        map_view.setScene(scene)

        # Add the map view to the layout
        layout.addWidget(map_view)

        # Set the layout for the map view window
        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()

    sys.exit(app.exec_())
