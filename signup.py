import sys
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QFormLayout, QLabel, QLineEdit, QComboBox, QDialogButtonBox, QGroupBox
from PyQt5.QtCore import Qt
from backendfunctions import sign_up_user







class Form2(QDialog):
    def __init__(self, parent=None):
        super(Form2, self).__init__(parent)

        # Set window dimensions
        self.windowWidth = 400
        self.windowHeight = 380
        self.setGeometry(100, 100, self.windowWidth, self.windowHeight)
        self.formGroupBox = QGroupBox("Signup")

        # Widget dimensions
        textBoxWidth = 80
        textBoxHeight = 30

        # Name field
        self.nameBox = QLineEdit()
        self.nameBox.setPlaceholderText("Name")
        self.nameBox.setMinimumSize(textBoxWidth, textBoxHeight)
        self.nameBox.setMaxLength(20)

        # Email field
        self.emailBox = QLineEdit()
        self.emailBox.setPlaceholderText("Email")
        self.emailBox.setMinimumSize(textBoxWidth, textBoxHeight)
        self.emailBox.setMaxLength(30)

        # Password field
        self.passwordBox = QLineEdit()
        self.passwordBox.setPlaceholderText("Password")
        self.passwordBox.setEchoMode(QLineEdit.Password)  # Echo mode set for password input
        self.passwordBox.setMinimumSize(textBoxWidth, textBoxHeight)

        # Preferred Sport field
        self.preferredSport = QComboBox()
        self.preferredSport.setMinimumSize(textBoxWidth, textBoxHeight)
        self.__loadSports()

        # Age field
        self.age = QLineEdit() 
        self.age.setPlaceholderText("Age")
        self.age.setMinimumSize(textBoxWidth, textBoxHeight)
        self.age.setMaxLength(3)

        # Warning text
        self.warningText = QLabel()
        self.warningText.setObjectName("warning")

        # Form layout setup
        self.__createFormFormat()

        # Buttons
        self.button = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.button.centerButtons()
        self.button.accepted.connect(self.__getInfo)
        self.button.rejected.connect(self.reject)

        # Main layout
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addWidget(self.button)
        self.setLayout(mainLayout)

    def __createFormFormat(self):
        formLayout = QFormLayout()
        formLayout.setSpacing(12)

        formLayout.addRow("Name", self.nameBox)
        formLayout.addRow("Email", self.emailBox)
        formLayout.addRow("Password", self.passwordBox)
        formLayout.addRow("Preferred Sport", self.preferredSport)
        formLayout.addRow("Age", self.age)
        formLayout.addRow(self.warningText)

        self.formGroupBox.setLayout(formLayout)

    def __loadSports(self):
        try:
            with open("sports.txt") as file:
                for line in file:
                    sport = line.strip()
                    if sport:
                        self.preferredSport.addItem(sport)
        except Exception as e:
            print("Error reading sports file:", e)

    
    def __getInfo(self):
        enteredName = self.nameBox.text()
        enteredEmail = self.emailBox.text()
        enteredPassword = self.passwordBox.text()
        enteredPreferredSport = self.preferredSport.currentText()
        try:
            enteredAge = int(self.age.text())
            if not all([enteredName, enteredEmail, enteredPassword, enteredPreferredSport, enteredAge >= 0]):
                self.warningText.setText("One or more fields is empty or invalid")
            else:
                success, message = sign_up_user(enteredEmail, enteredPassword, enteredName, enteredPreferredSport, enteredAge)
                self.warningText.setText(message)
        except ValueError:
            self.warningText.setText("Invalid Age")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Form2()
    form.show()
    sys.exit(app.exec())


  