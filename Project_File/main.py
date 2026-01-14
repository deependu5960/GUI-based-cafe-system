import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QStackedWidget, QLabel, QPushButton,QLineEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from ui.Home_page import HomePage
from ui.Log_page import LoginPage
from ui.beverages import Beverages
from ui.desserts import Desserts
from ui.empty_cart import empty_cart
from Models.cart_algo import cart_detail,total_price
from ui.snacks import Snacks
from ui.bill import Last_page


# from ui.cart_window import cart_win_ui



class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CAFE")
        self.setGeometry(200, 100, 1500, 800)

        # creating container(stack) which will contain all pages
        self.stack = QStackedWidget()

        # creating login page
        self.login = LoginPage(self.stack)

        # creating home page
        self.home = HomePage(self.stack)

        # creating empty page
        self.empty_cart = empty_cart(self.stack)

        # creating Beverages page
        self.beverages = Beverages(self.stack)

        # creating Desserts page
        self.desserts = Desserts(self.stack)

        # creating Snacks page
        self.snacks = Snacks(self.stack)

        #  creating last page
        self.last = Last_page(self.stack)

        # add to stack
        self.stack.addWidget(self.login)      #index 0
        self.stack.addWidget(self.home)       #index 1
        self.stack.addWidget(self.empty_cart) #index 2
        self.stack.addWidget(self.beverages)  #index 3
        self.stack.addWidget(self.desserts)   #index 4
        self.stack.addWidget(self.snacks)     #index 5
        self.stack.addWidget(self.last)       #index 6


        layout = QVBoxLayout(self)
        layout.addWidget(self.stack)
        self.setLayout(layout)


class Cart_Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CART")
        self.setGeometry(200, 100, 1500, 800)
        # self.cart_win_ui()
        self.cart_win_ui()


    def cart_win_ui(self):
        self.page_layout = QVBoxLayout()

        self.tittle = QLabel("Your Cart")
        self.tittle.setObjectName("tittle")
        self.tittle.setFont(QFont("Arial", 40))
        self.tittle.setFixedHeight(70)
        self.tittle.setAlignment(Qt.AlignCenter)

        # cart page
        self.cart_pannel = QVBoxLayout()
        for item_name, item_data in cart_detail.items():
            menu_box = QWidget()
            menu_layer = QHBoxLayout(menu_box)
            # menu_layer.addWidget(QLabel(item_name))
            prod_name = QLabel(item_name)
            prod_name.setObjectName("prod_name")
            prod_name.setFont(QFont("Arial", 15))
            # menu_layer.addWidget(QLabel(str(item_data["price"])))
            prod_price = QLabel(str(item_data["price"]))
            prod_price.setObjectName("prod_price")
            prod_price.setFont(QFont("Arial", 20))

            menu_layer.addWidget(prod_name)
            menu_layer.addWidget(prod_price)
            self.cart_pannel.addWidget(menu_box)


        self.bottom_page = QWidget()
        self.bottom_layout = QHBoxLayout(self.bottom_page)

        self.total_str = QLabel("Total :")
        self.total_str.setObjectName("Total")
        self.total_str.setFont(QFont("Arial", 30))
        self.bottom_layout.addWidget(self.total_str)

        self.total_price = QLabel(f" ₹{total_price()}")
        self.total_price.setObjectName("Total")
        self.total_price.setFont(QFont("Arial", 30))

        self.order_btn = QPushButton("Order Now")
        self.order_btn.setObjectName("back")
        self.order_btn.setFont(QFont("Georgia", 20))
        self.order_btn.clicked.connect(self.order_btn_click)


        self.bottom_layout.addStretch(1)
        self.bottom_layout.addWidget(self.total_str)
        self.bottom_layout.addWidget(self.total_price)
        self.bottom_layout.addSpacing(100)
        self.bottom_layout.addWidget(self.order_btn)
        self.bottom_layout.addStretch(1)


        self.page_layout.addWidget(self.tittle)
        self.page_layout.addSpacing(50)
        self.page_layout.addLayout(self.cart_pannel)
        self.page_layout.stretch(1)
        self.page_layout.addWidget(self.bottom_page)


        self.setLayout(self.page_layout)


    def order_btn_click(self):
        # self.stack.setCurrentIndex(0)
        # self.page_layout.hide()
        # self.tittle.setText("Get Your Bill")
        # self.mail_bar = QLineEdit()
        #
        # # self.menubox.hide()
        display.close()
        window.show()
        # self.stack.setCurrentIndex(0)
        app.exec()


if __name__=="__main__":
    # app = QApplication(sys.argv)
    #
    # with open (r"styles/main.qss") as f:
    #     app.setStyleSheet(f.read())
    #
    # window = MainWindow()
    # window.show()
    # sys.exit(app.exec_())

    app = QApplication(sys.argv)

    with open (r"styles/main.qss") as f:
        app.setStyleSheet(f.read())

    window = MainWindow()
    window.show()
    app.exec()


    if len(cart_detail) > 0:
        # Pass the dictionary into the new window
        display = Cart_Window()
        display.show()
        sys.exit(app.exec())
        # app.exec_()
    else:
        print("Dictionary is still empty. Closing application.")


    # if
    last_page = Last_page()
    last_page.show()
    sys.exit(app.exec_())
