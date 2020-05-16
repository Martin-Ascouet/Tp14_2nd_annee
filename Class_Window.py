from PySide2.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QProgressBar, QApplication

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.layout = QVBoxLayout()

        self.label = QLabel('SALUT')
        self.button = QPushButton('Bouton')
        self.barre = QProgressBar()

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.barre)

        self.setLayout(self.layout)


if __name__ == "__main__":
   app = QApplication([])
   win = Window()
   win.show()
   app.exec_()
