from PySide2.QtWidgets import QLabel, QWidget, QPushButton, QApplication, QVBoxLayout, QProgressBar
app = QApplication([])

mainWidget = QWidget()

layout = QVBoxLayout()

label = QLabel('SALUT')
button = QPushButton('Bouton')
barre = QProgressBar()


layout.addWidget(label)
layout.addWidget(button)
layout.addWidget(barre)

mainWidget.setLayout(layout)

mainWidget.show()
app.exec_()
