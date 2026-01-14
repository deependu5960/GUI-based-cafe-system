from PyQt5.QtWidgets import QApplication,QWidget,QVBoxLayout,QHBoxLayout,QStackedWidget,QLabel,QLineEdit,QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap,QFont
from Models.log_vfy import verify

class LoginPage(QWidget):

    def __init__(self,stack):
        super().__init__()
        self.stack = stack
        self.login_ui()

    def login_ui(self):
        # creating layout inside which all ui 
        self.layout = QHBoxLayout(self)
        
        # dividing layout in left side and right side


        # left side- 
        self.left_layout = QVBoxLayout()
        self.left_layout.setObjectName("left_panel")
        self.left_layout.setAlignment(Qt.AlignCenter)

            # adding logo
        self.logo = QPixmap(r"C:\Users\ASUS\OneDrive\Desktop\Project_File\images\logo.png").scaled(600, 600)
        self.logo_label = QLabel()
        self.logo_label.setObjectName("logo")
        self.logo_label.setPixmap(self.logo)
        self.logo_label.setAlignment(Qt.AlignCenter)

            # adding logo to left layout
        self.left_layout.addWidget(self.logo_label)



        # right side -
        self.right_layout = QVBoxLayout()
        self.right_layout.setAlignment(Qt.AlignCenter)


            # create a box inside which all show
        self.right_box = QWidget()
        self.right_box.setObjectName("right_box")
        self.right_box.setLayout(self.right_layout)
        self.right_box.setFixedHeight(600)
        self.right_box.setFixedWidth(700)

            # create brand name show 
        self.name = QLabel("COFFEE HOUSE")
        self.name.setObjectName("name")
        self.name.setFont(QFont("Algerian", 40))

            # create username input
        self.username = QLineEdit()
        self.username.setPlaceholderText("Enter your username")

             # create password input
        self.password = QLineEdit()
        self.password.setPlaceholderText("Enter your password")
        self.password.setEchoMode(QLineEdit.Password)


             # create submit button
        self.btn = QPushButton("Login")
        self.btn.setObjectName("login_btn")
        self.btn.clicked.connect(self.login)


             #create authentication msg
        self.msg=QLabel("")
        self.msg.setAlignment(Qt.AlignCenter)
        self.msg.setFont(QFont("Arial", 15))


        # adding content in right layout
        self.right_layout.addWidget(self.name)
        self.right_layout.addWidget(self.username)
        self.right_layout.addWidget(self.password)
        self.right_layout.addSpacing(20)
        self.right_layout.addWidget(self.btn)
        self.right_layout.addSpacing(20)
        self.right_layout.addWidget(self.msg)

        # adding left and right side in main layout
        self.layout.addStretch(1)
        self.layout.addLayout(self.left_layout)
        self.layout.addSpacing(50)
        self.layout.addWidget(self.right_box)
        self.layout.addStretch(1)

        
    def login(self):
        if verify(self.username.text(),self.password.text())==True:
            self.stack.setCurrentIndex(1)


        else:
            self.msg.setText(verify(self.username.text(),self.password.text()))
            self.msg.setStyleSheet("color: red;")
            self.right_box.setStyleSheet("""
            #right_box {
               border: 10px solid red;
            }
            """)
