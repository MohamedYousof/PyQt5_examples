import sys
from PyQt5.QtWidgets import QPushButton, QLabel, QWidget, QApplication, QVBoxLayout
from PyQt5.QtCore import QThread, pyqtSignal


class Main(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.label = QLabel("0")
        self.button = QPushButton('Start')
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        self.setLayout(layout)
        self.counter_thread = CounterThread()
        self.button.clicked.connect(self.start_thread)

    def counter(self, num):
        self.label.setText(str(num))

    def start_thread(self):
        self.counter_thread.counter.connect(self.counter)
        self.counter_thread.start()


class CounterThread(QThread):

    counter = pyqtSignal(int)

    def __init__(self):
        QThread.__init__(self)

    def run(self):
        for i in range(100):
            self.counter.emit(i)
            self.sleep(1)  # sleep one second after each iteration so you can see the progress


app = QApplication(sys.argv)
win = Main()
win.show()
sys.exit(app.exec_())
