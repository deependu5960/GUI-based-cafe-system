from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtCore import Qt
import smtplib
from Models.cart_algo import total_price
from email.message import EmailMessage

from Models.cart_algo import cart_detail


class Last_page(QWidget):
    def __init__(self,stack):
        super().__init__()
        self.setWindowTitle("Get Your Bill")
        self.stack = stack
        self.last_page_ui()

    def last_page_ui(self):
        self.page_layout = QHBoxLayout()
        self.page_layout.setAlignment(Qt.AlignCenter)

        self.greet = QLabel("Order Completed✅\n\n    Thank You \n for visiting here")
        self.greet.setObjectName("greet")
        self.greet.setFont(QFont("Arial", 30))

        self.right_layout = QVBoxLayout()
        self.right_layout.setAlignment(Qt.AlignCenter)

        self.mail_bar = QLineEdit()
        self.mail_bar.setFixedSize(500,100)
        self.mail_bar.setPlaceholderText("Enter your email here")

        self.get_btn = QPushButton("Get Your Bill")
        self.get_btn.setFont(QFont("Arial", 20))
        self.get_btn.setObjectName("back")
        self.get_btn.setStyleSheet("margin-left:100px; margin-top: 40px; color:white;")
        self.get_btn.clicked.connect(self.mail)

        self.indicator = QLabel("Email automation is disabled\nfor public reposatorydue to security reason\nYou can check detail in bill.txt file")
        self.indicator.setFont(QFont("Arial", 12))
        self.indicator.setStyleSheet("color:white;")


        self.right_layout.addSpacing(50)
        self.right_layout.addWidget(self.mail_bar)
        self.right_layout.addWidget(self.get_btn)
        self.right_layout.addSpacing(50)
        self.right_layout.addWidget(self.indicator)

        self.page_layout.addStretch(1)
        self.page_layout.addWidget(self.greet)
        self.page_layout.addSpacing(200)
        self.page_layout.addLayout(self.right_layout)
        self.page_layout.addStretch(1)

        self.setLayout(self.page_layout)

    def mail(self):

        with open(r"bill.txt","w") as f:
            for i_name,i_data in cart_detail.items():
                f.write(f"{i_name} : {i_data['price']}\n")
            f.write(f"Your Total Bill : {total_price()}")

        # try:

        #     # Email details
        #     sender_email = "Enter Your email id"
        #     receiver_email = self.mail_bar.text()
        #     app_password = "Enter your App Password of your Google"

        #     msg = EmailMessage()
        #     msg["Subject"] = "Your Bill from Café House "
        #     msg["From"] = sender_email
        #     msg["To"] = receiver_email
        #     msg.set_content("""Hello,

        #     Thank you for visiting café House! ☕
        #     We’re happy to share your bill for your recent order. Please find the attached invoice for your reference.

        #     Your payment has been received successfully.
        #     We truly appreciate your visit and hope you enjoyed your time with us.

        #     We’d love to welcome you back again soon for another great cup and a warm experience.

        #     Thank you for choosing us.

        #     Warm regards,
        #     Café House Team
        #     """)

        #     with open(r"bill.txt","r") as f:
        #         bill_data = f.read()

        #     msg.add_attachment(bill_data,"bill.txt")
        #     # Send email
        #     with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        #         server.login(sender_email, app_password)
        #         server.send_message(msg)

        #     self.indicator.setText("Your Bill has been sent successfully")
        #     self.indicator.setStyleSheet("color:white;")
        #     self.mail_bar.setStyleSheet("border : 0px;")

        # except:
        #     self.indicator.setText("Please Enter Valid Email-id")
        #     self.indicator.setStyleSheet("color:red;")
        #     self.mail_bar.setStyleSheet("border : 5px solid red;")