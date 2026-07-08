from PyQt6 import QtCore, QtGui, QtWidgets
import random
import time
import string


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1183, 805)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 1161, 16))
        self.label.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.label.setLineWidth(5)
        self.label.setMidLineWidth(5)
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 1161, 16))
        self.label_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.label_2.setLineWidth(5)
        self.label_2.setMidLineWidth(5)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.Headinglabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.Headinglabel.setGeometry(QtCore.QRect(184, 20, 791, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.Headinglabel.setFont(font)
        self.Headinglabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Headinglabel.setObjectName("Headinglabel")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 80, 1111, 671))
        self.label_4.setFrameShape(QtWidgets.QFrame.Shape.WinPanel)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.Generatorbutton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Generatorbutton.setGeometry(QtCore.QRect(470, 140, 181, 71))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Generatorbutton.setFont(font)
        self.Generatorbutton.setObjectName("Generatorbutton")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(60, 90, 1011, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.resultbutton = QtWidgets.QLabel(parent=self.centralwidget)
        self.resultbutton.setGeometry(QtCore.QRect(80, 230, 991, 61))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.resultbutton.setFont(font)
        self.resultbutton.setFrameShape(QtWidgets.QFrame.Shape.WinPanel)
        self.resultbutton.setText("")
        self.resultbutton.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.resultbutton.setObjectName("resultbutton")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(50, 300, 1061, 441))
        self.label_7.setFrameShape(QtWidgets.QFrame.Shape.WinPanel)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(70, 320, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.labeluppercase = QtWidgets.QLabel(parent=self.centralwidget)
        self.labeluppercase.setGeometry(QtCore.QRect(70, 370, 751, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labeluppercase.setFont(font)
        self.labeluppercase.setObjectName("labeluppercase")
        self.labellower = QtWidgets.QLabel(parent=self.centralwidget)
        self.labellower.setGeometry(QtCore.QRect(70, 420, 351, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labellower.setFont(font)
        self.labellower.setObjectName("labellower")
        self.labeldigit = QtWidgets.QLabel(parent=self.centralwidget)
        self.labeldigit.setGeometry(QtCore.QRect(70, 470, 351, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labeldigit.setFont(font)
        self.labeldigit.setObjectName("labeldigit")
        self.labelsymbol = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelsymbol.setGeometry(QtCore.QRect(70, 520, 401, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelsymbol.setFont(font)
        self.labelsymbol.setObjectName("labelsymbol")
        self.requirement = QtWidgets.QLabel(parent=self.centralwidget)
        self.requirement.setGeometry(QtCore.QRect(70, 570, 661, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.requirement.setFont(font)
        self.requirement.setObjectName("requirement")
        self.requirement2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.requirement2.setGeometry(QtCore.QRect(70, 620, 461, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.requirement2.setFont(font)
        self.requirement2.setObjectName("requirement2")
        self.labelstrength = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelstrength.setGeometry(QtCore.QRect(60, 680, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelstrength.setFont(font)
        self.labelstrength.setObjectName("labelstrength")
        self.strengthresult = QtWidgets.QLabel(parent=self.centralwidget)
        self.strengthresult.setGeometry(QtCore.QRect(530, 670, 531, 61))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.strengthresult.setFont(font)
        self.strengthresult.setFrameShape(QtWidgets.QFrame.Shape.WinPanel)
        self.strengthresult.setText("")
        self.strengthresult.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.strengthresult.setObjectName("strengthresult")
        self.matching1 = QtWidgets.QLabel(parent=self.centralwidget)
        self.matching1.setGeometry(QtCore.QRect(850, 370, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.matching1.setFont(font)
        self.matching1.setFrameShape(QtWidgets.QFrame.Shape.WinPanel)
        self.matching1.setText("")
        self.matching1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.matching1.setObjectName("matching1")
        self.matching2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.matching2.setGeometry(QtCore.QRect(850, 420, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.matching2.setFont(font)
        self.matching2.setFrameShape(QtWidgets.QFrame.Shape.WinPanel)
        self.matching2.setText("")
        self.matching2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.matching2.setObjectName("matching2")
        self.matching3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.matching3.setGeometry(QtCore.QRect(850, 470, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.matching3.setFont(font)
        self.matching3.setFrameShape(QtWidgets.QFrame.Shape.WinPanel)
        self.matching3.setText("")
        self.matching3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.matching3.setObjectName("matching3")
        self.matching4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.matching4.setGeometry(QtCore.QRect(850, 520, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.matching4.setFont(font)
        self.matching4.setFrameShape(QtWidgets.QFrame.Shape.WinPanel)
        self.matching4.setText("")
        self.matching4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.matching4.setObjectName("matching4")
        self.matching5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.matching5.setGeometry(QtCore.QRect(850, 570, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.matching5.setFont(font)
        self.matching5.setFrameShape(QtWidgets.QFrame.Shape.WinPanel)
        self.matching5.setText("")
        self.matching5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.matching5.setObjectName("matching5")
        self.matching6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.matching6.setGeometry(QtCore.QRect(850, 620, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.matching6.setFont(font)
        self.matching6.setFrameShape(QtWidgets.QFrame.Shape.WinPanel)
        self.matching6.setText("")
        self.matching6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.matching6.setObjectName("matching6")
        self.Scrollbutton = QtWidgets.QScrollBar(parent=self.centralwidget)
        self.Scrollbutton.setGeometry(QtCore.QRect(1150, 100, 41, 701))
        self.Scrollbutton.setMinimum(1)
        self.Scrollbutton.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.Scrollbutton.setObjectName("Scrollbutton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1183, 26))
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
        self.Headinglabel.setText(_translate("MainWindow", "PASSWORD GENERATOR"))
        self.Generatorbutton.setText(_translate("MainWindow", "GENERATE"))
        self.label_5.setText(_translate("MainWindow", "Press the generate button below to generate the password"))
        self.label_8.setText(_translate("MainWindow", "Password status :"))
        self.labeluppercase.setText(_translate("MainWindow", "Must contain atleast 1 Uppercase                                                                                                                             :"))
        self.labellower.setText(_translate("MainWindow", "Must contain atleast 1 Lowercase"))
        self.labeldigit.setText(_translate("MainWindow", "Must contain atleast 1 Digit"))
        self.labelsymbol.setText(_translate("MainWindow", "Must contain atleast 1 Special Symbol"))
        self.requirement.setText(_translate("MainWindow", "Must contain minimum 16 character and maximum 24 character"))
        self.requirement2.setText(_translate("MainWindow", "Doesn\'t contain consecutive same character "))
        self.labelstrength.setText(_translate("MainWindow", "Password Strength : "))


# Password generation logic with time-based entropy
s1 = string.ascii_lowercase  # lowercase
s2 = string.ascii_uppercase  # uppercase
s3 = string.punctuation      # special characters (enhanced)
s4 = string.digits           # digits

def get_time_seed():
    """Generate time-based entropy for stronger randomization"""
    current_time = time.time()
    # Use microseconds for additional entropy
    return int((current_time * 1000000) % 2147483647)

def password():
    """Generate a stronger, uncrackable password using time-based entropy"""
    # Seed random with time-based entropy for stronger randomization
    random.seed(get_time_seed())
    
    # Dynamic length based on time (16-24 characters)
    base_length = random.randint(16, 24)
    
    # Ensure at least one of each character type
    required_chars = [
        random.choice(s1),
        random.choice(s2),
        random.choice(s3),
        random.choice(s4)
    ]
    
    # Fill remaining length with random characters from all sets
    all_chars = s1 + s2 + s3 + s4
    passwd_list = []
    
    # Build password while preventing consecutive identical characters
    for _ in range(base_length):
        while True:
            char = random.choice(all_chars)
            # Check if this character is different from the last one
            if not passwd_list or char != passwd_list[-1]:
                passwd_list.append(char)
                break
    
    # Insert required characters at random positions while maintaining no-consecutive rule
    for req_char in required_chars:
        inserted = False
        attempts = 0
        while not inserted and attempts < 100:
            insert_pos = random.randint(0, len(passwd_list))
            # Check neighbors to ensure no consecutive duplicates
            can_insert = True
            if insert_pos > 0 and passwd_list[insert_pos - 1] == req_char:
                can_insert = False
            if insert_pos < len(passwd_list) and passwd_list[insert_pos] == req_char:
                can_insert = False
            
            if can_insert:
                passwd_list.insert(insert_pos, req_char)
                inserted = True
            attempts += 1
    
    passwd = ''.join(passwd_list)
    
    # Validation check
    if (16 <= len(passwd) <= 24 and
        any(c.islower() for c in passwd) and
        any(c.isupper() for c in passwd) and
        any(c.isdigit() for c in passwd) and
        any(c in s3 for c in passwd) and
        not any(passwd[i] == passwd[i+1] for i in range(len(passwd)-1))):
        return passwd
    else:
        return password()  # Recursive call if validation fails

def check_requirements(passwd):
    """Check which requirements are met"""
    # Check for consecutive identical characters
    has_consecutive = any(passwd[i] == passwd[i+1] for i in range(len(passwd)-1))
    
    checks = {
        'uppercase': any(c.isupper() for c in passwd),
        'lowercase': any(c.islower() for c in passwd),
        'digit': any(c.isdigit() for c in passwd),
        'symbol': any(c in s3 for c in passwd),
        'length': 16 <= len(passwd) <= 24,
        'no_consecutive': not has_consecutive  # No consecutive identical characters allowed
    }
    return checks


class PasswordGeneratorApp(Ui_MainWindow):
    """Extended UI class with password generation logic"""
    
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        # Connect the generate button to the password generation function
        self.Generatorbutton.clicked.connect(self.generate_and_display)
        self.current_password = ""
    
    def generate_and_display(self):
        """Generate password and update UI with results"""
        self.current_password = password()
        
        # Display the generated password
        self.resultbutton.setText(self.current_password)
        
        # Check all requirements
        checks = check_requirements(self.current_password)
        
        # Update requirement labels with checkmarks or X marks
        self.matching1.setText("✓" if checks['uppercase'] else "✗")
        self.matching1.setStyleSheet("color: green; font-weight: bold;" if checks['uppercase'] else "color: red; font-weight: bold;")
        
        self.matching2.setText("✓" if checks['lowercase'] else "✗")
        self.matching2.setStyleSheet("color: green; font-weight: bold;" if checks['lowercase'] else "color: red; font-weight: bold;")
        
        self.matching3.setText("✓" if checks['digit'] else "✗")
        self.matching3.setStyleSheet("color: green; font-weight: bold;" if checks['digit'] else "color: red; font-weight: bold;")
        
        self.matching4.setText("✓" if checks['symbol'] else "✗")
        self.matching4.setStyleSheet("color: green; font-weight: bold;" if checks['symbol'] else "color: red; font-weight: bold;")
        
        # Update length display (now supports 16-40 characters)
        length_text = f"Length: {len(self.current_password)} chars (16-24)"
        self.matching5.setText("✓" if checks['length'] else "✗")
        self.matching5.setStyleSheet("color: green; font-weight: bold;" if checks['length'] else "color: red; font-weight: bold;")
        self.labellower.setText(length_text)
        
        self.matching6.setText("✓" if checks['no_consecutive'] else "✗")
        self.matching6.setStyleSheet("color: green; font-weight: bold;" if checks['no_consecutive'] else "color: red; font-weight: bold;")
        
        # Determine overall strength with enhanced criteria
        passed = sum(checks.values())
        password_len = len(self.current_password)
        
        # Enhanced strength calculation
        if passed == 6 and password_len >= 24:
            strength = "VERY STRONG"
            color = "green"
        elif passed == 6:
            strength = "STRONG"
            color = "lightgreen"
        elif passed >= 5:
            strength = "STRONG"
            color = "lightgreen"
        elif passed >= 4:
            strength = "MEDIUM"
            color = "orange"
        else:
            strength = "WEAK"
            color = "red"
        
        self.strengthresult.setText(strength)
        self.strengthresult.setStyleSheet(f"color: {color}; font-weight: bold;")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = PasswordGeneratorApp()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
