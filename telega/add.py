from design.add_design import *
from settings.meta_engine import get_engine

import sys

from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    oldPos: object

    def __init__(self):
        super(MyWidget, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.engine = get_engine()
        self.conn = self.engine.connect()
        self.start()

    def start(self):
        self.ui.change.setCheckable(True)
        self.ui.change_2.setCheckable(True)
        self.ui.change.setChecked(True)
        self.ui.change_2.setChecked(True)

        self.ui.close.clicked.connect(lambda: self.close())
        self.ui.change.clicked.connect(lambda: self.change(1))
        self.ui.change_2.clicked.connect(lambda: self.change(2))

        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.show()

    def change(self, key=int):
        if key == 1:
            if self.ui.change.isChecked():
                self.ui.lab.show()
                if self.ui.ed.text() != '':
                    exz = f"""UPDATE data set token='{self.ui.ed.text()}' WHERE id=1"""
                    self.conn.execute(exz)
            else:
                self.ui.lab.hide()
        if key == 2:
            if self.ui.change_2.isChecked():
                if self.ui.ed_2.text() != '':
                    exz = f"""UPDATE data set user_id='{self.ui.ed_2.text()}' WHERE id=1"""
                    self.conn.execute(exz)
                self.ui.lab_2.show()
            else:
                self.ui.lab_2.hide()

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):

        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()


def main():
    sapp = QApplication(sys.argv)
    ex = MyWidget()
    sys.exit(sapp.exec_())


if __name__ == '__main__':
    main()
