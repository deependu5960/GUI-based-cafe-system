from PyQt5.QtWidgets import QWidget,QVBoxLayout,QHBoxLayout,QPushButton,QLabel,QPushButton
from PyQt5.QtGui import QPixmap,QFont



class empty_cart(QWidget):
    def __init__(self,stack):
        super().__init__()
        self.stack = stack
        self.empty_cart_ui()

    def empty_cart_ui(self):
        # layout of cart page
        self.layout = QVBoxLayout(self)

        # CREATE NAV BAR layout
        self.nav_layout = QHBoxLayout()
        self.nav = QWidget()
        self.nav.setObjectName("nav")
        self.nav.setLayout(self.nav_layout)
        self.nav.setFixedHeight(100)

        # creating contents in NAV BAR
        self.nav_logo = QPixmap(r"C:\Users\ASUS\OneDrive\Desktop\Project_File\images\logo.png").scaled(100, 100)
        self.nav_logo_label = QLabel()
        self.nav_logo_label.setPixmap(self.nav_logo)

        # cart
        self.cart = QPushButton("CART")
        self.cart.setObjectName("logout")
        self.cart.setFont(QFont("Arial", 12))

        # logout
        self.logout = QPushButton("Logout")
        self.logout.setObjectName("logout")
        self.logout.setFont(QFont("Arial", 12))
        # logout.setFixedWidth(200)
        self.logout.clicked.connect(self.logout_click)

        # adding content in nav bar
        self.nav_layout.addWidget(self.nav_logo_label)
        self.nav_layout.addWidget(self.cart)
        self.nav_layout.addSpacing(10)
        self.nav_layout.addWidget(self.logout)

        # creating cart page
        self.cart_page = QVBoxLayout()

        self.msg = QLabel("Cart is empty")
        self.msg.setFont(QFont("Arial", 40))
        self.msg.setStyleSheet("QLabel{color:red;}")
        self.msg2 = QLabel("Please Order something")
        self.msg2.setFont(QFont("Arial", 40))
        self.msg2.setStyleSheet("QLabel{color:red;}")

        self.back_btn = QPushButton("Back")
        self.back_btn.setObjectName("back")
        self.back_btn.clicked.connect(self.back_click)

        self.cart_page.addWidget(self.msg)
        self.cart_page.addWidget(self.msg2)
        self.cart_page.addWidget(self.back_btn)

        #
        self.layout.addWidget(self.nav)
        self.layout.addStretch(1)
        self.layout.addLayout(self.cart_page)
        self.layout.addStretch(1)

    def logout_click(self):
        self.stack.setCurrentIndex(0)

    def back_click(self):
        self.stack.setCurrentIndex(1)