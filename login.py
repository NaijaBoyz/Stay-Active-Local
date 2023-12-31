import sys
from pathlib import Path
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from signup import Form2  # Import the Form2 class from signup.py
from backendfunctions import login_user
from homepage import Ui_MainWindow as Homepage

class Login(QDialog):

    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        
        self.setObjectName("login")

       # Create a QLabel for displaying warnings or error messages
        self.warningText = QLabel("")
        self.warningText.setObjectName("warning")
        ###### stylesheets
        self.setStyleSheet(Path('signup.qss').read_text())

        self.windowWidth = 400
        self.windowHeight = 300

        textBoxWidth = 80
        textBoxHeight = 30

        sg = QDesktopWidget().availableGeometry()
        initx = int((sg.width() - self.windowWidth) / 2)
        inity = int((sg.height() - self.windowHeight) / 2)

        self.setGeometry(initx,inity,self.windowWidth,self.windowHeight)
        self.formGroupBox = QGroupBox("Login") 

        ##### login label
        self.loginLabel = QLabel("Login")
        self.loginLabel.setGeometry(100,100,100,100)
        self.loginLabel.setAlignment(Qt.AlignCenter)
        self.loginLabel.setObjectName('loginLabel')

        ##### login subheading
        self.loginSubheading = QLabel("Please login with your account",
                                      alignment=Qt.AlignCenter)
        
        ###### username
        self.usernameBox = QLineEdit()
        self.usernameBox.setPlaceholderText("Username")
        self.usernameBox.setMinimumSize(textBoxWidth,textBoxHeight)
        self.usernameBox.setMaxLength(20)

        ##### password
        self.passwordBox = QLineEdit()
        self.passwordBox.setPlaceholderText("Password")
        self.passwordBox.setEchoMode(QLineEdit.EchoMode.Password)
        self.passwordBox.setMaxLength(20)
        self.passwordBox.setObjectName("password")

        ##### login button
        self.button = QPushButton("Login")
        self.button.setFixedSize(130,45)
        self.button.setObjectName("login")
        self.button.clicked.connect(self.__getInfo)
       

        ##### signup button
        self.signupButton = QPushButton("Signup")
        self.signupButton.setFixedSize(100,35)
        self.signupButton.setObjectName('signup')
        self.signupButton.clicked.connect(self.openSignupForm)  # Connecting the button here


        ###### create the format
        self.__createFormFormat()

        ##### main layout
        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.formGroupBox)
        self.mainLayout.addWidget(self.button, alignment=Qt.AlignCenter | Qt.AlignBottom)
        self.mainLayout.addWidget(self.signupButton, alignment=Qt.AlignCenter | Qt.AlignBottom)
        self.mainLayout.addWidget(self.warningText, alignment=Qt.AlignCenter)
        
        ##### main layout of the window/widget
        self.setLayout(self.mainLayout)

        # Connect the signup button to the new function
        self.signupButton.clicked.connect(self.openSignupForm)


    """
    Creates the form layout
    """
    def __createFormFormat(self):

        # init layout
        self.formLayout = QFormLayout()
        self.formLayout.setSpacing(20)

        # create separate vbox for login labels
        self.loginVBox = QVBoxLayout()
        self.loginVBox.addWidget(self.loginLabel)
        self.loginVBox.addWidget(self.loginSubheading)
        self.loginVBox.setSpacing(1)
        self.loginVBox.setObjectName('loginVbox')

        self.formLayout.addRow(self.loginVBox)
        self.formLayout.addRow(self.usernameBox)
        self.formLayout.addRow(self.passwordBox)

        self.formGroupBox.setLayout(self.formLayout)



    """
    Gets the string inside the edit text when button is pressed.
    """
    def __getInfo(self):
        enteredEmail = self.usernameBox.text()
        enteredPassword = self.passwordBox.text()

        # Call the login function
        success, response = login_user(enteredEmail, enteredPassword)

        if success:
            # Extract the user's Firebase ID
            user_id = response.split("uid: ")[-1]

            # Instantiate the Homepage class with the user ID
            homepage = Homepage(self, user_id=user_id)
            homepage.show()
            homepageGeometry = homepage.geometry()
            homepage.move(homepageGeometry.x(), homepageGeometry.y()+70)
            self.hide()
        else:
            # Show error message on failure
            self.warningText.setText(response)



    def openSignupForm(self):
        # This function opens the signup form
        self.signupForm = Form2(self)
        self.signupForm.show()