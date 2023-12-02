import sys
from login import Login
from pathlib import Path
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from signup import Form2

# window dimensions
maxWidth = 500; maxHeight = 500

class Form2(QDialog):

    def __init__(self, parent=None):
        super(Form2, self).__init__(parent)

        ##### stylesheets
        self.setStyleSheet(Path('signup.qss').read_text())
        
        self.windowWidth = 400
        self.windowHeight = 380

        textBoxWidth = 80
        textBoxHeight = 30

        ### buffer for user info

        self.setGeometry(100,100,self.windowWidth,self.windowHeight)
        self.formGroupBox = QGroupBox("Signup")


        ########### add widgets
        ##### username
        self.usernameLabel = QLabel("Username")
        self.usernameLabel.setFrameStyle(QFrame.Sunken)
        self.usernameLabel.setAlignment(Qt.AlignBottom | Qt.AlignLeft)
        self.usernameLabel.setObjectName("formLabel")

        self.usernameLine = QLineEdit()
        self.usernameLine.setMinimumSize(textBoxWidth,textBoxHeight)
        self.usernameLine.setMaxLength(20)

        ##### password
        self.passwordLabel = QLabel("Password")
        self.passwordLabel.setObjectName("formLabel")
        self.passwordLine = QLineEdit()
        self.passwordLine.setEchoMode(QLineEdit.EchoMode.Password)
        self.passwordLine.setMinimumSize(textBoxWidth,textBoxHeight)
        self.passwordLine.setMaxLength(20)

        ##### first name
        self.nameBox = QLineEdit()
        self.nameBox.setPlaceholderText("First Name")
        self.nameBox.setMinimumSize(textBoxWidth,textBoxHeight)
        self.nameBox.setMaxLength(20)

        ##### last name
        self.lastNameBox = QLineEdit()
        self.lastNameBox.setPlaceholderText("Last Name")
        self.lastNameBox.setMinimumSize(textBoxWidth,textBoxHeight)
        self.lastNameBox.setMaxLength(20)

        ##### email
        self.emailBox = QLineEdit()
        self.emailBox.setPlaceholderText("Email")
        self.emailBox.setMinimumSize(textBoxWidth,textBoxHeight)
        self.emailBox.setMaxLength(30)

        ##### preferred sport
        self.preferredSport = QComboBox()
        self.preferredSport.setPlaceholderText("Preferred Sport")
        self.preferredSport.setMinimumSize(textBoxWidth,textBoxHeight)

        ##### age
        self.age = QLineEdit() 
        self.age.setMinimumSize(textBoxWidth,textBoxHeight)
        self.age.setPlaceholderText("Age")
        self.age.setMaxLength(3)

        ### warning text
        self.warningText = QLabel()
        self.warningText.setObjectName("warning")

        # creating the form layout
        self.__createFormFormat()
        
        ### button
        self.button = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.button.centerButtons()

        # when OK is clicked, execute selfInfo func
        self.button.accepted.connect(self.__getInfo)

        # when Cancel is clicked
        self.button.rejected.connect(self.reject)
        self.button.move(300,300)

        # main layout
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addWidget(self.button)

        self.setLayout(mainLayout)


    ### creates the form format
    def __createFormFormat(self):
        formLayout = QFormLayout()
        formLayout.setSpacing(12)

        # separate hbox for the name
        nameHBox = QHBoxLayout()
        nameHBox.addWidget(self.nameBox)
        nameHBox.addWidget(self.lastNameBox)

        formLayout.addRow(self.usernameLabel, self.usernameLine)
        formLayout.addRow(self.passwordLabel, self.passwordLine)
        formLayout.addRow(nameHBox)
        formLayout.addRow(self.emailBox)
        formLayout.addRow(self.age)
        formLayout.addRow(self.preferredSport)
        formLayout.addRow(self.warningText)

        self.__extractSportList()

        self.formGroupBox.setLayout(formLayout)

    ### get the string from line edits
    def __getInfo(self):
        enteredUsername = self.usernameLine.text()
        enteredPassword = self.passwordLine.text()
        enteredName = self.nameBox.text()
        enteredLast = self.lastNameBox.text()
        enteredPreferredSport = self.preferredSport.currentText()

        ##### value error handling
        try:
            enteredAge = int(self.age.text())

            ##### checking
            # if any field is empty
            if self.__isEmpty(enteredUsername) or self.__isEmpty(enteredPassword) or self.__isEmpty(enteredName) \
                or self.__isEmpty(enteredLast) or self.__isEmpty(enteredPreferredSport):
                self.warningText.setText("One or more fields is empty")


            if enteredAge < 18:
                self.warningText.setText("Age Warning: Below 18")
        
            print(f"{enteredUsername}\n{enteredPassword}\n{enteredName}\n" \
                + f"{enteredLast}\n{enteredPreferredSport}\n{enteredAge}")
            
        except ValueError as vE:
            self.warningText.setText("Invalid Age")

    ### extracts sport from the txt file
    def __extractSportList(self):
        print("stuff")
        file = open("sports.txt", "r")
        while True:
            sport = file.readline()
            if not sport:
                break
            ### action
            # trim the string first, remove the \n
            sport = sport.rstrip("\n")
            self.preferredSport.addItem(sport)
        file.close()

    ### defines if a variable has empty string
    def __isEmpty(self, var):
        return var == ""




if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Create and show the login form
    loginForm = Login()
    loginForm.show()

    # Run the main Qt loop
    sys.exit(app.exec())