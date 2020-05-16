from PySide2.QtWidgets import QWidget, QLineEdit,  QGridLayout, QLabel, QPushButton, QProgressBar, QApplication
from PySide2.QtGui import QIcon, Qt

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setFixedSize(400, 300)
        self.setWindowTitle('Ma fenetre')
        self.setWindowIcon(QIcon('fr-flag.png'))

        self.layout = QGridLayout()

        self.label = QLabel('LABEL')
        self.label.setAlignment(Qt.AlignCenter)

        self.barre = QProgressBar()
        self.barre.setValue(95)

        self.lineEdit = QLineEdit()
        self.button = QPushButton('Entree')
        self.button.setToolTip('salut thomas')

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.barre)
        self.layout.addWidget(self.lineEdit)
        self.layout.addWidget(self.button)

        self.setLayout(self.layout)



if __name__ == "__main__":
   app = QApplication([])
   win = Window()
   win.show()
   app.exec_()
