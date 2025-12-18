from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QTableWidget, 
                             QTableWidgetItem, QTabWidget,QPushButton,QHeaderView,QFrame)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from admin_Backend import AdminBackend

class AdminDashboard(QMainWindow):

    def __init__(self):
        super().__init__()
        self.backend = AdminBackend()
        self.init_ui()
        
    def init_ui(self):
        self.setWindowTitle("Admin Dashboard - JeSuite Hotel")
        self.setGeometry(100, 100, 12000, 700)

        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        main_widget = QWidget()
        main_layout = QVBoxLayout()

        header = QLabel("Admin Dashboard")
        header.setFont(QFont("Arial", 20, QFont.Bold))
        header.setStyleSheet("color: #2c3e50; margin: 20px;")
        main_layout.addWidget(header)

        stats_frame = self.create_stats_panel()
        main_layout.addWidget(stats_frame)

        self.tabs = QTabWidget()
        self.tabs.setStyleSheet("""
            QTabWidget::pane { 
                border: 1px solid #bdc3c7; 
                background-color: #ecf0f1;
            }
            QTabBar::tab {
                background: #bdc3c7; 
                padding: 10px; 
                font-size: 14px;
                margin-right: 2px;
                font-size:12px;
            }
            QTabBar::tab::selected {
                background: #8c6d3d; 
                color: white;
            }""")
        
        self.tabs.addTab(self.create_customers_tab(), "Customer data")
        self.tabs.addTab(self.create_bookings_tab(), "Booking data")

        main_layout.addWidget(self.tabs)

        refresh_button = QPushButton("Refresh Data")
        refresh_button.setStyleSheet("""
            QPushButton {
                background-color: #27ae60;
                color: white;
                padding: 10px;
                border-radius: 5px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #229954;
            }""")
        refresh_button.clicked.connect(self.refresh_data)
        main_layout.addWidget(refresh_button)      

        central_widget.setLayout(main_layout)
        self.refresh_data()

    def create_stats_panel(self):
        frame = QFrame()
        frame.setStyleSheet("""
            QFrame{
            background-color: #f5f6fa;
            border: 1px solid #bdc3c7;
        }
        """)
        
        layout = QHBoxLayout()

        self.total_customers_box = self.create_stat_box("Total Customers", "0","#3498db")
        self.total_bookings_box = self.create_stat_box("Total Bookings", "0","#27ae60")
        self.active_bookings_box = self.create_stat_box("Active Bookings", "0","#f39c12")
        self.canceled_bookings_box = self.create_stat_box("Canceled Bookings", "0", "#e74c3c")
        self.revenue_box = self.create_stat_box("Total Revenue", "$0.00", "#9b59b6")

        layout.addWidget(self.total_customers_box)
        layout.addWidget(self.total_bookings_box)
        layout.addWidget(self.active_bookings_box)
        layout.addWidget(self.canceled_bookings_box)
        layout.addWidget(self.revenue_box)  

        frame.setLayout(layout)
        return frame
    
    def create_stat_box(self, title, value,color):
        container = QFrame()
        container.setStyleSheet(f"""
            QFrame{{
                background-color: white; 
                border-left: 5px solid {color}; 
                border-radius: 5px; 
                padding: 10px;
            }}
        """)

        layout = QVBoxLayout()
        title_label = QLabel(title)
        title_label.setFont(QFont("Arial", 12))
        title_label.setStyleSheet("color: #7f8c8d;")

        value_label = QLabel(value)
        value_label.setFont(QFont("Arial", 16, QFont.Bold))
        value_label.setStyleSheet(f"color: {color};")
        value_label.setObjectName("value")

        layout.addWidget(title_label)
        layout.addWidget(value_label)
        layout.addStretch()

        container.setLayout(layout)
        return container
    
    def create_customers_tab(self):
        widget = QWidget()
        layout = QVBoxLayout()

        self.customers_table = QTableWidget()
        self.customers_table.setStyleSheet("""
            QTableWidget {
                gridline-color: #bdc3c7;
                background-color: white;
            }
            QHeaderView::section {
                background-color: #bdc3c7;
                color: white;
                padding: 5px;
                font-size: 14px;
            }
        """)
        self.customers_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        
        layout.addWidget(self.customers_table)
        widget.setLayout(layout)
        return widget
    
    def create_bookings_tab(self):
        widget = QWidget()
        layout = QVBoxLayout()

        self.bookings_table = QTableWidget()
        self.bookings_table.setStyleSheet("""
            QTableWidget {
                gridline-color: #bdc3c7;
                background-color: white;
            }
            QHeaderView::section {
                background-color: #34495e;
                color: white;
                padding: 8px;
                font-weight: bold;
            }
        """)
        layout.addWidget(self.bookings_table)
        widget.setLayout(layout)
        return widget
    
    def refresh_data(self):
        stats = self.backend.get_stats()
        self.total_customers_box.findChild(QLabel, "value").setText(str(stats['total_customers'])) # update total customers
        self.total_bookings_box.findChild(QLabel, "value").setText(str(stats['total_bookings']))    # update total bookings
        self.active_bookings_box.findChild(QLabel, "value").setText(str(stats['active_bookings'])) # update active bookings
        self.canceled_bookings_box.findChild(QLabel, "value").setText(str(stats['canceled_bookings'])) # update canceled bookings
        self.revenue_box.findChild(QLabel, "value").setText(f"${stats['total_revenue']:.2f}")   # update revenue

        customers = self.backend.get_all_customers() # fetch the customer data
        self.populate_table(self.customers_table, customers) # populate customer table

        bookings = self.backend.get_all_bookings() # fetch the booking data
        self.populate_table(self.bookings_table, bookings) # populate booking table

    #
    def populate_table(self, table, data):
        if not data:
            table.setRowCount(0)
            table.setColumnCount(0)
            return
        
        headers = list(data[0].keys())
        table.setColumnCount(len(headers))
        table.setHorizontalHeaderLabels(headers)
        table.setRowCount(len(data))

        for row_idx, row_data in enumerate(data):
            for col_idx, header in enumerate(headers): #populate char by char 
                item = QTableWidgetItem(str(row_data[header])) # convert to string
                table.setItem(row_idx, col_idx, item) # set item in table

        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)