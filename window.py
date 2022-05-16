from PyQt6.QtWidgets import QWidget, QGridLayout, QListWidget


class Window(QWidget):
    def __init__(self, fach):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)
        self.listwidget = QListWidget()
        for el in fach.grades:
            self.listwidget.insertI(0, el)

        self.listwidget.clicked.connect(self.clicked)
        layout.addWidget(self.listwidget)

    def clicked(self, qmodelindex):
        item = self.listwidget.currentItem()
        print(item.text())