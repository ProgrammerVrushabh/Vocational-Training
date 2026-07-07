from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 606)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonIconOnly)
        MainWindow.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Output = QtWidgets.QLabel(parent=self.centralwidget)
        self.Output.setEnabled(True)
        self.Output.setGeometry(QtCore.QRect(4, 15, 392, 111))
        font = QtGui.QFont()
        font.setFamily("Malgun Gothic")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.Output.setFont(font)
        self.Output.setFrameShape(QtWidgets.QFrame.Shape.WinPanel)
        self.Output.setLineWidth(19)
        self.Output.setMidLineWidth(19)
        self.Output.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.Output.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.Output.setIndent(-1)
        self.Output.setObjectName("Output")
        self.percentButton = QtWidgets.QPushButton(parent=self.centralwidget, clicked=lambda: self.percent_it())
        self.percentButton.setGeometry(QtCore.QRect(10, 130, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.percentButton.setFont(font)
        self.percentButton.setIconSize(QtCore.QSize(20, 20))
        self.percentButton.setObjectName("percentButton")
        self.CE = QtWidgets.QPushButton(parent=self.centralwidget, clicked= lambda:self.press_it("CE") )
        self.CE.setGeometry(QtCore.QRect(110, 130, 81, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.CE.setFont(font)
        self.CE.setObjectName("CE")
        self.CButton = QtWidgets.QPushButton(parent=self.centralwidget, clicked= lambda:self.press_it("C") )
        self.CButton.setGeometry(QtCore.QRect(200, 130, 93, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.CButton.setFont(font)
        self.CButton.setObjectName("CButton")
        self.BackButton = QtWidgets.QPushButton(parent=self.centralwidget, clicked= lambda:self.remove_it() )
        self.BackButton.setGeometry(QtCore.QRect(300, 130, 93, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.BackButton.setFont(font)
        self.BackButton.setObjectName("BackButton")
        self.divisionbyx = QtWidgets.QPushButton(parent=self.centralwidget, clicked=lambda: self.inverse_it())
        self.divisionbyx.setGeometry(QtCore.QRect(10, 200, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.divisionbyx.setFont(font)
        self.divisionbyx.setObjectName("divisionbyx")
        self.power2 = QtWidgets.QPushButton(parent=self.centralwidget, clicked=lambda: self.square_it())
        self.power2.setGeometry(QtCore.QRect(110, 200, 81, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.power2.setFont(font)
        self.power2.setObjectName("power2")
        self.rootx = QtWidgets.QPushButton(parent=self.centralwidget, clicked=lambda: self.sqrt_it())
        self.rootx.setGeometry(QtCore.QRect(200, 200, 93, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.rootx.setFont(font)
        self.rootx.setObjectName("rootx")
        self.devide = QtWidgets.QPushButton(parent=self.centralwidget, clicked= lambda:self.press_it("/"))
        self.devide.setGeometry(QtCore.QRect(300, 200, 93, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.devide.setFont(font)
        self.devide.setObjectName("devide")
        self.button7 = QtWidgets.QPushButton(parent=self.centralwidget, clicked= lambda:self.press_it("7"))
        self.button7.setGeometry(QtCore.QRect(10, 270, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.button7.setFont(font)
        self.button7.setObjectName("button7")
        self.buttonmultiply = QtWidgets.QPushButton(parent=self.centralwidget, clicked= lambda:self.press_it("*"))
        self.buttonmultiply.setGeometry(QtCore.QRect(300, 270, 93, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.buttonmultiply.setFont(font)
        self.buttonmultiply.setObjectName("buttonmultiply")
        self.buttonminus = QtWidgets.QPushButton(parent=self.centralwidget, clicked= lambda:self.press_it("-"))
        self.buttonminus.setGeometry(QtCore.QRect(300, 340, 93, 61))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.buttonminus.setFont(font)
        self.buttonminus.setObjectName("buttonminus")
        self.Button9 = QtWidgets.QPushButton(parent=self.centralwidget, clicked= lambda:self.press_it("9"))
        self.Button9.setGeometry(QtCore.QRect(200, 270, 93, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.Button9.setFont(font)
        self.Button9.setObjectName("Button9")
        self.button5 = QtWidgets.QPushButton(parent=self.centralwidget, clicked= lambda:self.press_it("5"))
        self.button5.setGeometry(QtCore.QRect(110, 340, 81, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.button5.setFont(font)
        self.button5.setObjectName("button5")
        self.decimabutton = QtWidgets.QPushButton(parent=self.centralwidget, clicked= lambda:self.dot_it())
        self.decimabutton.setGeometry(QtCore.QRect(200, 480, 93, 61))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.decimabutton.setFont(font)
        self.decimabutton.setObjectName("decimabutton")
        self.button4 = QtWidgets.QPushButton(parent=self.centralwidget, clicked= lambda:self.press_it("4"))
        self.button4.setGeometry(QtCore.QRect(10, 340, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.button4.setFont(font)
        self.button4.setObjectName("button4")
        self.button6 = QtWidgets.QPushButton(parent=self.centralwidget, clicked= lambda:self.press_it("6"))
        self.button6.setGeometry(QtCore.QRect(200, 340, 93, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.button6.setFont(font)
        self.button6.setObjectName("button6")
        self.Button8 = QtWidgets.QPushButton(parent=self.centralwidget, clicked= lambda:self.press_it("8"))
        self.Button8.setGeometry(QtCore.QRect(110, 270, 81, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.Button8.setFont(font)
        self.Button8.setObjectName("Button8")
        self.equalsbutton = QtWidgets.QPushButton(parent=self.centralwidget, clicked= lambda:self.math_it("="))
        self.equalsbutton.setGeometry(QtCore.QRect(300, 480, 93, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.equalsbutton.setFont(font)
        self.equalsbutton.setObjectName("equalsbutton")
        self.plusminus = QtWidgets.QPushButton(parent=self.centralwidget, clicked= lambda:self.plus_minus_it())
        self.plusminus.setGeometry(QtCore.QRect(10, 480, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.plusminus.setFont(font)
        self.plusminus.setObjectName("plusminus")
        self.button2 = QtWidgets.QPushButton(parent=self.centralwidget, clicked= lambda:self.press_it("2"))
        self.button2.setGeometry(QtCore.QRect(110, 410, 81, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.button2.setFont(font)
        self.button2.setObjectName("button2")
        self.Buttonplus = QtWidgets.QPushButton(parent=self.centralwidget, clicked= lambda:self.press_it("+"))
        self.Buttonplus.setGeometry(QtCore.QRect(300, 410, 93, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.Buttonplus.setFont(font)
        self.Buttonplus.setObjectName("Buttonplus")
        self.button3 = QtWidgets.QPushButton(parent=self.centralwidget, clicked= lambda:self.press_it("3"))
        self.button3.setGeometry(QtCore.QRect(200, 410, 93, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.button3.setFont(font)
        self.button3.setObjectName("button3")
        self.zerbutton = QtWidgets.QPushButton(parent=self.centralwidget, clicked= lambda:self.press_it("0"))
        self.zerbutton.setGeometry(QtCore.QRect(110, 480, 81, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.zerbutton.setFont(font)
        self.zerbutton.setObjectName("zerbutton")
        self.button1 = QtWidgets.QPushButton(parent=self.centralwidget, clicked= lambda:self.press_it("1"))
        self.button1.setGeometry(QtCore.QRect(10, 410, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.button1.setFont(font)
        self.button1.setObjectName("button1")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    
    # backspace in calculator
    def remove_it(self):
        #get the screen
        screen = self.Output.text()
        #remove the last character from the screen
        screen=screen[:-1]
        #update the screen
        self.Output.setText(screen)
    
    # math operations in calculator
    def math_it(self, pressed):
        #get the screen
        screen = self.Output.text()
        try:
            answer=eval(screen)
            self.Output.setText(str(answer))
        except:
            self.Output.setText("Error")
    # prevent multiple decimal points in calculator
    def dot_it(self):
        #get the screen
        screen = self.Output.text()
        #check if the last character is a decimal point
        if screen[-1] == ".":
            pass
        else:
            #add a decimal point to the screen
            self.Output.setText(f'{screen}.')
    # percent operation in calculator
    def percent_it(self):
        screen = self.Output.text().strip()
        if screen in {"", "Error"}:
            self.Output.setText("0")
            return
        try:
            value = float(screen)
            self.Output.setText(str(value / 100))
        except ValueError:
            self.Output.setText("Error")

    def inverse_it(self):
        screen = self.Output.text().strip()
        if screen in {"", "Error", "0"}:
            self.Output.setText("Error")
            return
        try:
            value = float(screen)
            self.Output.setText(str(1 / value))
        except ValueError:
            self.Output.setText("Error")

    def square_it(self):
        screen = self.Output.text().strip()
        if screen in {"", "Error"}:
            self.Output.setText("0")
            return
        try:
            value = float(screen)
            self.Output.setText(str(value * value))
        except ValueError:
            self.Output.setText("Error")

    def sqrt_it(self):
        screen = self.Output.text().strip()
        if screen in {"", "Error"}:
            self.Output.setText("0")
            return
        try:
            value = float(screen)
            if value < 0:
                self.Output.setText("Error")
            else:
                self.Output.setText(str(value ** 0.5))
        except ValueError:
            self.Output.setText("Error")
    
    #Change the sign of the number in calculator
    def plus_minus_it(self):
        screen = self.Output.text().strip()
        if screen in {"", "Error", "0"}:
            return
        try:
            value = float(screen)
            if value == 0:
                self.Output.setText("0")
            else:
                self.Output.setText(str(-value))
        except ValueError:
            self.Output.setText("Error")
        
    # decimal system in calculator
    def dot_it(self):
        #get the screen
        screen = self.Output.text()
        #check if the last character is a decimal point
        if screen[-1] == ".":
            pass
        else:
            #add a decimal point to the screen
            self.Output.setText(f'{screen}.')
    # number input in calculator
    def press_it(self, pressed):
        if pressed == "CE" or pressed == "C":
            self.Output.setText("0")
        else:
            # remove the leading zero when a number is pressed
            if self.Output.text()=="0":
                self.Output.setText("")

            self.Output.setText(f'{self.Output.text()}{pressed}')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.Output.setText(_translate("MainWindow", "0"))
        self.percentButton.setText(_translate("MainWindow", "%"))
        self.CE.setText(_translate("MainWindow", "CE"))
        self.CButton.setText(_translate("MainWindow", "C"))
        self.BackButton.setText(_translate("MainWindow", "⌫"))
        self.divisionbyx.setText(_translate("MainWindow", "1/x"))
        self.power2.setText(_translate("MainWindow", "x²"))
        self.rootx.setText(_translate("MainWindow", "√x"))
        self.devide.setText(_translate("MainWindow", "÷"))
        self.button7.setText(_translate("MainWindow", "7"))
        self.buttonmultiply.setText(_translate("MainWindow", "X"))
        self.buttonminus.setText(_translate("MainWindow", "-"))
        self.Button9.setText(_translate("MainWindow", "9"))
        self.button5.setText(_translate("MainWindow", "5"))
        self.decimabutton.setText(_translate("MainWindow", "."))
        self.button4.setText(_translate("MainWindow", "4"))
        self.button6.setText(_translate("MainWindow", "6"))
        self.Button8.setText(_translate("MainWindow", "8"))
        self.equalsbutton.setText(_translate("MainWindow", "="))
        self.plusminus.setText(_translate("MainWindow", "+/-"))
        self.button2.setText(_translate("MainWindow", "2"))
        self.Buttonplus.setText(_translate("MainWindow", "+"))
        self.button3.setText(_translate("MainWindow", "3"))
        self.zerbutton.setText(_translate("MainWindow", "0"))
        self.button1.setText(_translate("MainWindow", "1"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
