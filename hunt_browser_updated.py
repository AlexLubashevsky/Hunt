
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QVBoxLayout, QWidget, QHBoxLayout, QToolBar, QAction, QListWidget, QDockWidget, QLabel
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl, Qt

class HuntBrowser(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the title of the browser
        self.setWindowTitle("The Hunt Browser")

        # Set the default size of the window
        self.setGeometry(50, 50, 1400, 900)

        # Create a web engine view
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://www.google.com"))

        # Create the search bar
        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText("Search or enter URL")
        self.search_bar.returnPressed.connect(self.navigate_to_url)

        # Create a home button
        home_button = QPushButton("Home")
        home_button.clicked.connect(self.navigate_home)

        # Create a back button
        back_button = QPushButton("Back")
        back_button.clicked.connect(self.browser.back)

        # Create a forward button
        forward_button = QPushButton("Forward")
        forward_button.clicked.connect(self.browser.forward)

        # Create a button for navigating
        self.go_button = QPushButton("Go")
        self.go_button.clicked.connect(self.navigate_to_url)

        # Create a bookmarks panel
        self.bookmarks_panel = QListWidget()
        self.bookmarks_panel.itemDoubleClicked.connect(self.load_bookmarked_site)

        # Create a button to bookmark the current page
        bookmark_button = QPushButton("Bookmark")
        bookmark_button.clicked.connect(self.add_bookmark)

        # Set up side panel for bookmarks
        bookmarks_dock = QDockWidget("Bookmarks", self)
        bookmarks_dock.setWidget(self.bookmarks_panel)
        bookmarks_dock.setFloating(False)
        self.addDockWidget(Qt.LeftDockWidgetArea, bookmarks_dock)

        # Watermark at the bottom
        watermark = QLabel("By Alex", self)
        watermark.setStyleSheet("color: gray; font-size: 12px;")
        watermark.setAlignment(Qt.AlignCenter)

        # Set the colors and styles
        self.setStyleSheet("""
            QMainWindow {
                background-color: black;
            }
            QLineEdit {
                background-color: white;
                color: black;
                border-radius: 10px;
                padding: 10px;
                font-size: 16px;
            }
            QPushButton {
                background-color: red;
                color: white;
                border-radius: 10px;
                padding: 5px 15px;
                font-size: 14px;
            }
            QListWidget {
                background-color: white;
                color: black;
                border: none;
                font-size: 14px;
            }
            QLabel {
                margin-bottom: 10px;
            }
        """)

        # Create the top navigation layout
        nav_layout = QHBoxLayout()
        nav_layout.addWidget(back_button)
        nav_layout.addWidget(forward_button)
        nav_layout.addWidget(home_button)
        nav_layout.addWidget(self.search_bar)
        nav_layout.addWidget(self.go_button)
        nav_layout.addWidget(bookmark_button)

        # Add the layout to a central widget
        central_widget = QWidget()
        layout = QVBoxLayout()
        layout.addLayout(nav_layout)
        layout.addWidget(self.browser)
        layout.addWidget(watermark)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def navigate_to_url(self):
        url = self.search_bar.text()
        if "http" not in url:
            url = "https://www.google.com/search?q=" + url
        self.browser.setUrl(QUrl(url))

    def navigate_home(self):
        self.browser.setUrl(QUrl("https://www.google.com"))

    def add_bookmark(self):
        current_url = self.browser.url().toString()
        self.bookmarks_panel.addItem(current_url)

    def load_bookmarked_site(self, item):
        bookmarked_url = item.text()
        self.browser.setUrl(QUrl(bookmarked_url))

# Run the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HuntBrowser()
    window.show()
    sys.exit(app.exec_())
