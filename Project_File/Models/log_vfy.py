def verify(username,password):
    if username == "user":
        if password == "1234":
            return True
        else:
            return "Incorrect Password"
    else:
        return "Invalid Credentials"

def logout_click(self):
    self.stack.setCurrentIndex(0)
