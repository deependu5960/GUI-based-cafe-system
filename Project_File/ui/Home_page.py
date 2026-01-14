from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QStackedWidget, QPushButton,QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap, QFont

from Models.cart_algo import cart_detail


class HomePage(QWidget):
    
    def __init__(self,stack):
        super().__init__()
        self.stack = stack
        self.home_ui()

    def home_ui(self):
        # layout of home page
        self.layout = QVBoxLayout(self)
        # self.layout.setAlignment(Qt.AlignCenter)

        # CREATE NAV BAR layout
        self.nav_layout = QHBoxLayout()
        self.nav = QWidget()
        self.nav.setObjectName("nav")
        self.nav.setLayout(self.nav_layout)
        self.nav.setFixedHeight(100)

        # creating contents in NAV BAR
        self.nav_logo = QPixmap(r"C:\Users\ASUS\OneDrive\Desktop\Project_File\images\logo.png").scaled(100,100)
        self.nav_logo_label = QLabel()
        self.nav_logo_label.setPixmap(self.nav_logo)

            # cart
        self.cart = QPushButton("CART")
        self.cart.setObjectName("logout")
        self.cart.setFont(QFont("Arial", 12))

        self.cart.clicked.connect(self.cart_click)

            #logout
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




        # create main page layout
        self.main_layout = QHBoxLayout()
        self.main_layout.setAlignment(Qt.AlignCenter)
        # self.main_page = QWidget()
        # self.main_page.setFixedHeight(700)
        # self.main_layout.setLayout(self.main_layout)

        self.container1 = QVBoxLayout()
        self.container1.setAlignment(Qt.AlignCenter)

        self.container2 = QVBoxLayout()
        self.container2.setAlignment(Qt.AlignCenter)

        self.container3 = QVBoxLayout()
        self.container3.setAlignment(Qt.AlignCenter)


        self.box1_img = QPixmap(r"C:\Users\ASUS\OneDrive\Desktop\Project_File\images\beverages.png").scaled(400,400)
        self.box1 = QLabel("")
        self.box1.setPixmap(self.box1_img)

        self.b_btn = QPushButton("Explore Beverages")
        self.b_btn.setFont(QFont("Georgia", 20))
        self.b_btn.setObjectName("explore")
        self.b_btn.clicked.connect(self.bev_page)

        self.container1.addWidget(self.box1)
        self.container1.addSpacing(20)
        self.container1.addWidget(self.b_btn)

        self.box2_img = QPixmap(r"C:\Users\ASUS\OneDrive\Desktop\Project_File\images\Desserts.png").scaled(400,400)
        self.box2 = QLabel("")
        self.box2.setPixmap(self.box2_img)

        self.d_btn = QPushButton("Explore Desserts")
        self.d_btn.setFont(QFont("Georgia", 20))
        self.d_btn.setObjectName("explore")
        self.d_btn.clicked.connect(self.des_page)

        self.container2.addWidget(self.box2)
        self.container2.addSpacing(20)
        self.container2.addWidget(self.d_btn)

        self.box3_img = QPixmap(r"C:\Users\ASUS\OneDrive\Desktop\Project_File\images\Snacks.png").scaled(400,400)
        self.box3 = QLabel("")
        self.box3.setPixmap(self.box3_img)

        self.s_btn = QPushButton("Explore Snacks")
        self.s_btn.setFont(QFont("Georgia", 20))
        self.s_btn.setObjectName("explore")
        self.s_btn.clicked.connect(self.snac_page)

        # self.setStyleSheet("""
        #     QPushButton#explore:hover {
        #         background: qlineargradient(
        #             x1: 0, y1: 0,
        #             x2: 1, y2: 0,
        #             stop: 0 #2BBCA1,
        #             stop: 1 #7FD26F
        #         );
        #     }
        # """)

        self.container3.addWidget(self.box3)
        self.container3.addSpacing(20)
        self.container3.addWidget(self.s_btn)


        for i in self.box1,self.box2,self.box3:
            i.setAlignment(Qt.AlignCenter)
            i.setStyleSheet("""
                QLabel {
                    background-color: black;
                    min-width: 400px;
                    max-width: 400px;
                    min-height: 400px;
                    max-height: 400px;
                    border-radius: 15px;
                    border: 10px solid qlineargradient(
                    x1: 0, y1: 0,
                    x2: 1, y2: 0,
                    stop: 0 #2BBCA1,
                    stop: 1 #7FD26F );
                }
            """)


        # adding content to main page layout
        self.main_layout.addLayout(self.container1)
        self.main_layout.addSpacing(10)
        self.main_layout.addLayout(self.container2)
        self.main_layout.addSpacing(10)
        self.main_layout.addLayout(self.container3)
        # self.main_layout.addWidget(self.box4)





        # adding layouts in home layout
        # self.layout.addStretch(5)
        self.layout.addWidget(self.nav)
        self.layout.addLayout(self.main_layout)



    def logout_click(self):
        self.stack.setCurrentIndex(0)

    def bev_page(self):
        self.stack.setCurrentIndex(3)

    def des_page(self):
        self.stack.setCurrentIndex(4)

    def snac_page(self):
        self.stack.setCurrentIndex(5)

    def cart_click(self):
        if len(cart_detail)==0:
            self.stack.setCurrentIndex(2)
        else:
            self.stack.setCurrentIndex(6)
            self.window().close()