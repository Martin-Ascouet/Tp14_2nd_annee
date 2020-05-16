from PySide2.QtWidgets import QWidget, QTextEdit, QGridLayout, QVBoxLayout, QLabel, QPushButton, QProgressBar, QApplication
from PySide2.QtGui import QIcon, Qt
from PySide2 import QtCore
class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle('Ma fenetre')

        self.layout = QGridLayout()

        self.label = QLabel('Laisse un commentaire')
        self.text = QTextEdit()
        self.button1 = QPushButton('Succes')
        self.button2 = QPushButton('Cancel')
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button1)#, alignment=QtCore.Qt.AlignLeft)
        self.layout.addWidget(self.button2)

        self.setLayout(self.layout)



if __name__ == "__main__":
   app = QApplication([])
   win = Window()
   win.show()
   app.exec_()
