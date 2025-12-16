from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel,QLineEdit, QPushButton,QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class LoginDialogueBox(QDialog):

    def __init__(self):
        super().__init__()
        self.init_ui() #initialize UI components

    def init_ui(self):
        self.setWindowTitle("Sign In - JeSuite Hotel")
        self.setFixedSize(400, 350)
        self.setStyleSheet("background-color:#f5f5f5;")
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.Dialog)
        self.setModal(True)

        layout = QVBoxLayout()
        layout.setSpacing(15)
        layout.setContentsMargins(40, 40, 40, 40)

        #TITLE
        title = QLabel("Sign In")
        title.setAlignment(Qt.AlignCenter)
        title.setFont(QFont("Arial", 20, QFont.Bold))
        title.setStyleSheet("color: #2c3e50; margin-bottom: 20px;")
        layout.addWidget(title)

        #EMAIL PROMPT:
        email_label = QLabel("Email:")
        email_label.setFont(QFont("Arial", 12))
        email_label.setStyleSheet("color: #2c3e50;")
        layout.addWidget(email_label)

        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Enter your email")
        self.email_input.setStyleSheet("""QLineEdit{
        padding: 10px; 
        border: 2px solid #bdc3c7;
        border-radius: 5px;
        font-size: 14px;
        background-color: white;
        color: #2c3e50;
        }
        QLineEdit:focus{
            border: 2px solid #3498db;
      }
        """)
        layout.addWidget(self.email_input)

        #PASSWORD PROMPT:
        password_label = QLabel("Password:")
        password_label.setFont(QFont("Arial", 12))
        password_label.setStyleSheet("color: #2c3e50;") 
        layout.addWidget(password_label)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Enter your password")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setStyleSheet("""
            QLineEdit{
                padding: 10px; 
                border: 2px solid #bdc3c7;
                border-radius: 5px;
                font-size: 12px;
                background-color: white;
                color: #2c3e50; 
            }
            QLineEdit:focus{
                border: 2px solid #3498db;
            }
        """)
        self.password_input.returnPressed.connect(self.handle_login)  # Enter key triggers login
        layout.addWidget(self.password_input)

        #login button
        login_button = QPushButton("Sign In")
        login_button.setFont(QFont("Arial", 12,QFont.Bold))
        login_button.setStyleSheet("""
        QPushButton{
            background-color: #8c6d3d; #main color 
            color: white;
            padding: 12px;
            border: none;
            border-radius: 5px;
            margin-top: 10px;
        }
        QPushButton:hover{
            background-color: #6d5730;
        }
        QPushButton:pressed{
            background-color: #5a4826;
        }
        """)
        login_button.clicked.connect(self.handle_login)
        layout.addWidget(login_button)

        layout.addStretch()
        self.setLayout(layout) 

        #handle login
    def handle_login(self):   
        email = self.email_input.text().strip()
        password = self.password_input.text()

        if email == "admin@jesuite.com" and password == "admin123":
            print("Login successful!") #dbug-remove later
            try: #dbug-remove later
                self.open_admin_dashboard()
            except Exception as e:
                print(f"Error opening admin dashboard: {e}")
                QMessageBox.critical(self, "Error", f"Failed to open admin dashboard: {e}")
        else:
            QMessageBox.warning(self, "Login Failed", "Invalid email or password.")
            self.password_input.clear()

    #open admin dashboard
    def open_admin_dashboard(self):
        try: #dbug-remove later
            from admin_dashboard import AdminDashboard
            self.admin_dashboard = AdminDashboard()
            self.admin_dashboard.show()
            prinbt("admin dashboard opened") #dbug-remove later
            self.close()
            print("login dialog closed") #dbug-remove later
        except Exception as e:
            print(f"Error opening admin dashboard: {e}")
        import traceback
        traceback.print_exc()
        raise