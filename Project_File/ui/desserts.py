from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QStackedWidget, QPushButton, QLabel, \
    QGridLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap, QFont
from Models.cart_algo import add_to_cart,cart_detail

class Desserts(QWidget):
    def __init__(self,stack):
        super().__init__()
        self.stack = stack
        self.Des_ui()

    def Des_ui(self):
        # layout of bev page
        self.layout = QVBoxLayout(self)

        # CREATE NAV BAR layout
        self.nav_layout = QHBoxLayout()
        self.nav = QWidget()
        self.nav.setObjectName("nav")
        self.nav.setLayout(self.nav_layout)
        self.nav.setFixedHeight(100)

        # creating contents in NAV BAR
        self.nav_logo = QPixmap(r"images\logo.png").scaled(100, 100)
        self.nav_logo_label = QLabel()
        self.nav_logo_label.setPixmap(self.nav_logo)

        # cart
        self.cart = QPushButton("CART")
        self.cart.setObjectName("logout")
        self.cart.setFont(QFont("Arial", 12))

        self.cart.clicked.connect(self.cart_click)

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

        # menu page
        self.menu_page = QGridLayout()

        self.menu1 = QWidget()
        self.menu2 = QWidget()
        self.menu3 = QWidget()
        self.menu4 = QWidget()
        self.menu5 = QWidget()
        self.menu6 = QWidget()

        for menu in self.menu1,self.menu2,self.menu3,self.menu4,self.menu5,self.menu6:
            menu.setFixedSize(500,200)
            menu.setObjectName("menu")

        # adding menu in menu page layout
        self.menu_page.addWidget(self.menu1,0,0)
        self.menu_page.addWidget(self.menu2,0,1)
        self.menu_page.addWidget(self.menu3,0,2)
        self.menu_page.addWidget(self.menu4,1,0)
        self.menu_page.addWidget(self.menu5,1,1)
        self.menu_page.addWidget(self.menu6,1,2)


        # buttons
        self.btn_layer = QHBoxLayout()
        self.btn_layer.setAlignment(Qt.AlignCenter)

            # Back button
        self.back = QPushButton("BACK")
        self.back.setObjectName("back")
        self.back.setFont(QFont("Arial", 20))

        self.back.clicked.connect(self.back_click)

        #     # Cart button
        # self.cart = QPushButton("🛒")

        # adding content to button layout
        self.btn_layer.addWidget(self.back)

        # adding msg
        self.msg_layer = QHBoxLayout()
        self.msg_layer.setAlignment(Qt.AlignCenter)
        self.msg = QLabel("")
        self.msg.setFont(QFont("Arial", 20))
        self.msg.setStyleSheet("color : white")
        self.msg_layer.addWidget(self.msg)



        # creating all menu box using loop
        self.menus = [self.menu1,self.menu2,self.menu3,self.menu4,self.menu5,self.menu6]

        for i,menu in enumerate(self.menus,start=1):
            box_layout = QHBoxLayout(menu)  #creating layout

            img = QPixmap(fr"images\desserts\menu{i}.png").scaled(200, 200)
            img_label = QLabel()
            img_label.setPixmap(img)

            box_rightlayout = QVBoxLayout()

            name = QLabel("")
            name.setObjectName("menu_name")
            menu.name = name

            price = QLabel("")
            price.setObjectName("menu_price")
            menu.price = price
            #

            Add_cart_btn = QPushButton("+ ADD")
            Add_cart_btn.setFont(QFont("Arial", 10))
            Add_cart_btn.setObjectName("menu_cart_btn")


            box_rightlayout.addWidget(name)
            box_rightlayout.addWidget(price)
            box_rightlayout.addWidget(Add_cart_btn)
            #
            #     # adding widget in layout
            box_layout.addWidget(img_label)
            box_layout.addStretch(1)
            box_layout.addLayout(box_rightlayout)


        self.menus_name = ["Chocolate Brownie","Blueberry Muffin","Cheesecake","Croissant","Donut","Ice Cream Scoop"]
        self.menus_price = [160,110,180,90,60,70]

        for i, menu in enumerate(self.menus):
            menu.name.setText(self.menus_name[i])
            menu.price.setText(f"Rs. {self.menus_price[i]}")

            btn = menu.findChild(QPushButton)
            btn.setProperty( "name", self.menus_name[i])
            btn.setProperty("price", self.menus_price[i])
            btn.setProperty("image", fr"images\desserts\menu{i+1}.png")
            btn.clicked.connect(self.add_btn)


        # C:\Users\ASUS\OneDrive\Desktop\Project_File\images\desserts\menu1.png


        self.layout.addWidget(self.nav)
        self.layout.addStretch(1)
        self.layout.addLayout(self.menu_page)
        self.layout.addSpacing(20)
        self.layout.addLayout(self.btn_layer)
        self.layout.addSpacing(50)
        self.layout.addLayout(self.msg_layer)
        self.layout.addStretch(1)


    def logout_click(self):
        self.stack.setCurrentIndex(0)
        cart_detail.clear()

    def back_click(self):
        self.stack.setCurrentIndex(1)
        self.msg.setText("")

    def cart_click(self):
        if len(cart_detail) == 0:
            self.stack.setCurrentIndex(2)
        else:
            self.stack.setCurrentIndex(6)
            self.window().close()

    def add_btn(self):
        btn = self.sender()
        name = btn.property("name")
        price = btn.property("price")
        image = btn.property("image")
        add_to_cart(name,price,image)
        self.msg.setText(f"'{name}' Added to Cart")