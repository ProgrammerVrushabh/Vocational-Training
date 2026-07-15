from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 600)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(parent=self.centralwidget)
        self.line.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        self.line.setGeometry(QtCore.QRect(10, 70, 781, 21))
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(parent=self.centralwidget)
        self.line_2.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        self.line_2.setGeometry(QtCore.QRect(10, 0, 781, 21))
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.line_2.setLineWidth(3)
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setObjectName("line_2")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 20, 511, 51))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 150, 101, 201))
        self.label_2.setFrameShape(QtWidgets.QFrame.Shape.WinPanel)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 350, 41, 181))
        self.label_3.setFrameShape(QtWidgets.QFrame.Shape.WinPanel)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(90, 170, 41, 31))
        self.label_4.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(90, 230, 41, 31))
        self.label_5.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(90, 290, 41, 31))
        self.label_6.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(650, 340, 41, 181))
        self.label_7.setFrameShape(QtWidgets.QFrame.Shape.WinPanel)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(620, 140, 101, 201))
        self.label_8.setFrameShape(QtWidgets.QFrame.Shape.WinPanel)
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(650, 160, 41, 31))
        self.label_9.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(650, 280, 41, 31))
        self.label_10.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(650, 220, 41, 31))
        self.label_11.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(40, 100, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(600, 90, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_13.setObjectName("label_13")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Traffic Light"))
        self.label_12.setText(_translate("MainWindow", "Poll A"))
        self.label_13.setText(_translate("MainWindow", "Poll B"))

    def update_logic(self):
        # State transition logic (Red -> Green -> Yellow -> Red)
        # Red: 1, Yellow: 0, Green: 2
        for i in range(2):
            if self.A[i] == 1: self.A[i] = 2   # Red to Green
            elif self.A[i] == 2: self.A[i] = 0 # Green to Yellow
            else: self.A[i] = 1           # Yellow to Red
        
        self.update_ui_colors()

    def update_ui_colors(self):
        # Poll A
        if self.A[0] == 1: # Red
            self.label_4.setStyleSheet("background-color: red;")
            self.label_5.setStyleSheet("background-color: gray;")
            self.label_6.setStyleSheet("background-color: gray;")
        elif self.A[0] == 0: # Yellow
            self.label_4.setStyleSheet("background-color: gray;")
            self.label_5.setStyleSheet("background-color: yellow;")
            self.label_6.setStyleSheet("background-color: gray;")
        else: # Green
            self.label_4.setStyleSheet("background-color: gray;")
            self.label_5.setStyleSheet("background-color: gray;")
            self.label_6.setStyleSheet("background-color: green;")

        # Poll B
        if self.A[1] == 1: # Red
            self.label_9.setStyleSheet("background-color: red;")
            self.label_11.setStyleSheet("background-color: gray;")
            self.label_10.setStyleSheet("background-color: gray;")
        elif self.A[1] == 0: # Yellow
            self.label_9.setStyleSheet("background-color: gray;")
            self.label_11.setStyleSheet("background-color: yellow;")
            self.label_10.setStyleSheet("background-color: gray;")
        else: # Green
            self.label_9.setStyleSheet("background-color: gray;")
            self.label_11.setStyleSheet("background-color: gray;")
            self.label_10.setStyleSheet("background-color: green;")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    
    # Initialize states
    ui.A = [1, 2] # Poll A: Red, Poll B: Green
    ui.update_ui_colors()

    # Setup Timer
    timer = QtCore.QTimer()
    timer.timeout.connect(ui.update_logic)
    timer.start(5000) # 5 seconds

    MainWindow.show()
    sys.exit(app.exec())
