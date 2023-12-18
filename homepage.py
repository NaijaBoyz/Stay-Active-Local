# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'homepage2.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from pathlib import Path
import sys
from create_event import EventCreatorApp
from displayeventuser import EventWindow as EventWindowUser
from displayeventhost import EventWindow as EventWindowHost

class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(QtWidgets.QMainWindow, self).__init__(parent)

        self.setObjectName("MainWindow")
        self.resize(984, 828)

        self.setStyleSheet(Path('signup.qss').read_text())

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")


        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 20, 921, 761))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 50, 831, 50))
        self.layoutWidget.setObjectName("layoutWidget")

        self.searchHBox = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.searchHBox.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.searchHBox.setContentsMargins(20, 10, 10, 10)
        self.searchHBox.setSpacing(15)
        self.searchHBox.setObjectName("searchHBox")

        ##### search line
        self.searchLine = QtWidgets.QPlainTextEdit(self.layoutWidget)
        self.searchLine.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchLine.sizePolicy().hasHeightForWidth())
        self.searchLine.setSizePolicy(sizePolicy)
        self.searchLine.setMaximumSize(QtCore.QSize(770, 30))
        self.searchLine.setObjectName("searchLine")
        self.searchHBox.addWidget(self.searchLine)

        ##### search button
        self.searchButton = QtWidgets.QPushButton(self.layoutWidget)
        self.searchButton.setFixedSize(QtCore.QSize(90, 32))
        self.searchButton.setObjectName("searchButton")
        self.searchHBox.addWidget(self.searchButton)

        self.searchButton.clicked.connect(self.__getText)

        ##### create event button
        self.createEventButton = QtWidgets.QPushButton(self.frame)
        self.createEventButton.setGeometry(QtCore.QRect(340, 680, 221, 51))
        self.createEventButton.setObjectName("createEventButton")
        
        self.createEventButton.clicked.connect(self.__createEvent)

        ##### makes the events VBox scrollable
        self.scrollArea = QtWidgets.QScrollArea(self.frame)
        self.scrollArea.setGeometry(QtCore.QRect(50, 150, 831, 231))
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setFixedSize(831, 231)
        self.scrollArea.setObjectName("scrollArea")

        ##### to be attached to the scroll area. Attach the widget that needs to 
        ##### scroll here.
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 812, 229))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        """
        self.verticalLayoutWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 831, 231))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        """
        ##### events Vbox
        self.events = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.events.setContentsMargins(15, 15, 25, 15)
        self.events.setObjectName("events")
        
        ##### events box
        ##### creates the events and the detail

        self.eventsList = []


        self.eventBox1 = EventBox(False)
       # self.events.addWidget(self.eventBox1)
        self.eventsList.append(self.eventBox1)

        self.eventBox2 = EventBox(False)
        #self.events.addWidget(self.eventBox2)
        self.eventsList.append(self.eventBox2)

        self.eventBox3 = EventBox(False)
        #self.events.addWidget(self.eventBox3)
        self.eventsList.append(self.eventBox3)

        ##### event boxes to the events widget
        for event in self.eventsList:
            self.events.addWidget(event)

        ##### add the widget attached to the vbox to the scroll area.
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.scrollArea_2 = QtWidgets.QScrollArea(self.frame)
        self.scrollArea_2.setGeometry(QtCore.QRect(50, 420, 831, 231))
        self.scrollArea_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")

        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 812, 229))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")

        """
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(-1, -1, 831, 231))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        """

        
        self.myEvents = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.myEvents.setContentsMargins(15, 15, 25, 15)
        self.myEvents.setSpacing(8)
        self.myEvents.setObjectName("myEvents")

        self.myEventsList = []

        self.myEvent1 = EventBox(True)
        self.myEventsList.append(self.myEvent1)

        # my cycling event example
        self.myEvent2 = self.addEvent(EventBox(True))
        self.myEventsList.append(self.myEvent2)

        for event in self.myEventsList:
            self.myEvents.addWidget(event)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        ##### events label
        self.eventsLabel = QtWidgets.QLabel(self.frame)
        self.eventsLabel.setGeometry(QtCore.QRect(50, 35, 100, 200))
        self.eventsLabel.setObjectName("eventsLabel")

        ##### my events label
        self.myEventsLabel = QtWidgets.QLabel(self.frame)
        self.myEventsLabel.setGeometry(QtCore.QRect(50, 305, 100, 200))
        self.myEventsLabel.setObjectName("eventsLabel")
         
        self.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 984, 21))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.searchLine.setPlaceholderText(_translate("MainWindow", "Search event..."))
        self.searchButton.setText(_translate("MainWindow", "Search"))
        self.createEventButton.setText(_translate("MainWindow", "CreateEvent"))
        self.myEventsLabel.setText(_translate("MainWindow", "My Events"))
        self.eventsLabel.setText(_translate("MainWindow", "Events"))
        #self.eventBox.setTitle(_translate("MainWindow", "Event"))
        #self.label_3.setText(_translate("MainWindow", "TextLabel"))
        #self.label.setText(_translate("MainWindow", "TextLabel"))
        #self.label_4.setText(_translate("MainWindow", "TextLabel"))
        #self.label_5.setText(_translate("MainWindow", "TextLabel"))
        #self.eventBox_2.setTitle(_translate("MainWindow", "Event"))
        #self.label_11.setText(_translate("MainWindow", "TextLabel"))
        #self.label_2.setText(_translate("MainWindow", "TextLabel"))
        #self.label_12.setText(_translate("MainWindow", "TextLabel"))
        #self.label_13.setText(_translate("MainWindow", "TextLabel"))

    def __getText(self):
        text = self.searchLine.toPlainText()

        ### for developers
        print(text)
    
    #
    # adds the details of the events to the event box
    #  filled with test items for now.
    #
    def addEvent(self, eventBox:QtWidgets.QGroupBox):
        eventTitle = "Cycle Bowie"
        eventDateTime = "some date and time format"
        eventSport = "Cycling"
        eventLocation = "Bowie, MD"
        eventHost = "James Jaluag"
        eventDescription = "Fun cycling exercise around Bowie!"

        eventBox.eventTitle.setText(eventTitle)
        eventBox.dateTime.setText(eventDateTime)
        eventBox.sport.setText(eventSport)
        eventBox.location.setText(eventLocation)
        eventBox.host.setText(eventHost)
        eventBox.description.setText(eventDescription)

        return eventBox

        
    def __createEvent(self):

        event = EventCreatorApp(self)
        event.show()






############### EVENT BOX ###############
# creates event box with the event      #
#   details                             #
#                                       #
#                                       #
# NOTE: will add a class with all the   #
#         details                       #
#                                       #
#########################################

class EventBox(QtWidgets.QGroupBox):

    def __init__(self, owner, parent=None):
        super(EventBox, self).__init__(parent)

        # signifies if the user is the owner of the event.
        # bool
        self.owner = owner

        self.setFixedSize(QtCore.QSize(770, 125))
        self.setObjectName("eventBox")
       

        self.gridLayoutWidget = QtWidgets.QWidget(self)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 19, 771, 111))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayoutWidget.setContentsMargins(10,0,20,0)
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 15)
        self.gridLayout.setSpacing(15)
        self.gridLayout.setObjectName("gridLayout")

        self.dateTime = QtWidgets.QLabel(self.gridLayoutWidget)
        self.dateTime.setMaximumSize(QtCore.QSize(300, 30))
        self.dateTime.setObjectName("dateTime")
        self.gridLayout.addWidget(self.dateTime, 0, 2, 1, 1)
        
        self.eventTitle = QtWidgets.QLabel(self.gridLayoutWidget)
        self.eventTitle.setMaximumSize(QtCore.QSize(300, 30))
        self.eventTitle.setObjectName("eventTitle")
        self.gridLayout.addWidget(self.eventTitle, 0, 0, 1, 1)

        self.sport = QtWidgets.QLabel(self.gridLayoutWidget)
        self.sport.setMaximumSize(QtCore.QSize(300, 30))
        self.sport.setObjectName("sport")
        self.gridLayout.addWidget(self.sport, 0, 1, 1, 1)

        self.location = QtWidgets.QLabel(self.gridLayoutWidget)
        self.location.setMaximumSize(QtCore.QSize(300, 30))
        self.location.setObjectName("location")
        self.gridLayout.addWidget(self.location, 2, 1, 1, 1)

        self.host = QtWidgets.QLabel(self.gridLayoutWidget)
        self.host.setMaximumSize(QtCore.QSize(300, 30))
        self.host.setObjectName("host")
        self.gridLayout.addWidget(self.host, 2, 2, 1, 1)

        self.description = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.description.setMaximumSize(QtCore.QSize(300, 40))
        self.description.setReadOnly(True)
        self.description.setText("Add description here..")
        self.description.setObjectName("description")
        self.gridLayout.addWidget(self.description, 2, 0, 1, 1)

        self.detailsButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.detailsButton.setFixedSize(QtCore.QSize(120,30))
        self.detailsButton.setContentsMargins(0,10,150,10)
        self.detailsButton.clicked.connect(self.__detailsButton)
        self.gridLayout.addWidget(self.detailsButton, 0, 3, 1, 1)


        # translation for whatever idk what for
        # I think the setText or smthg
        _translate = QtCore.QCoreApplication.translate
        self.setTitle(_translate("MainWindow", "Event"))
        self.dateTime.setText(_translate("MainWindow", "Date and Time"))
        self.eventTitle.setText(_translate("MainWindow", "Event name"))
        self.location.setText(_translate("MainWindow", "Location"))
        self.host.setText(_translate("MainWindow", "Host"))
        self.sport.setText(_translate("MainWindow", "Sport"))
        self.detailsButton.setText(_translate("MainWindow", "Details"))

    ##
    # opens up the details of the 
    # event based on the user's ownership
    ##
    def __detailsButton(self):
        # if owner
        if self.owner:
            print("Im owner")
            event = EventWindowHost()
            event.show()

        else:
            print("just a user")
            event = EventWindowUser()
            event.show()
        




########## Runs the window above #############
# NOTE: Do not forget to remove this when    #
#       integrating to the main proj         #
#                                            #
##############################################

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui_MainWindow()
    window.setWindowTitle("Stay Active Local")
    window.show()
    sys.exit(app.exec())
