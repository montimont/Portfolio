from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWebEngineWidgets import *

class WebBrowser(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(WebBrowser, self).__init__(*args, **kwargs)

        self.window = QWidget()
        self.window.setWindowTitle('Simple Web Browser')

        self.layout = QVBoxLayout()
        self.horizontal = QHBoxLayout()

        self.url_bar = QTextEdit()
        self.url_bar.setMaximumHeight(30)

        self.go_btn = QPushButton('Go')
        self.go_btn.setMinimumHeight(30)
        self.go_btn.setStyleSheet("background-color: green;")

        self.cancel_btn = QPushButton('Cancel')
        self.cancel_btn.setMinimumHeight(30)
        self.cancel_btn.setStyleSheet("background-color: red;")

        self.back_btn = QPushButton('<')
        self.back_btn.setMinimumHeight(30)
        self.back_btn.setStyleSheet("background-color: yellow;")

        self.forward_btn = QPushButton('>')
        self.forward_btn.setMinimumHeight(30)
        self.forward_btn.setStyleSheet("background-color: yellow;")


        self.horizontal.addWidget(self.url_bar)
        self.horizontal.addWidget(self.go_btn)
        self.horizontal.addWidget(self.cancel_btn)
        self.horizontal.addWidget(self.back_btn)
        self.horizontal.addWidget(self.forward_btn)

        self.browser = QWebEngineView()

        self.go_btn.clicked.connect(lambda:self.navigate(self.url_bar.toPlainText()))
        self.cancel_btn.clicked.connect(self.browser.stop)
        self.back_btn.clicked.connect(self.browser.back)
        self.forward_btn.clicked.connect(self.browser.forward)

        self.layout.addLayout(self.horizontal)
        self.layout.addWidget(self.browser)

        self.browser.setUrl(QUrl("http://google.com"))

        self.window.setLayout(self.layout)
        self.window.show()

    def navigate(self, url):
        if not url.startswith('http'):
            url = 'http://' + url
            self.url_bar.setText(url)
        if url:
            self.browser.setUrl(QUrl(url))

app = QApplication([])
window = WebBrowser()
app.exec()
