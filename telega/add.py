from design.design import *
# from settings.meta_engine import get_engine
from settings.data import coms, dat, coms_list

import os
import sys
import json

from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    oldPos: object

    def __init__(self):
        super(MyWidget, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        # self.engine = get_engine()
        # self.conn = self.engine.connect()
        self.start()

    def start(self):
        self.ui.list_widget.addItems(list(coms_list.keys()))
        self.ui.change.setCheckable(True)
        self.ui.change_2.setCheckable(True)
        self.ui.change.setChecked(True)
        self.ui.change_2.setChecked(True)
        self.ui.off.hide()

        self.ui.start.clicked.connect(lambda: self.str())

        self.ui.close.clicked.connect(lambda: self.close())
        self.ui.change.clicked.connect(lambda: self.change(1))
        self.ui.change_2.clicked.connect(lambda: self.change(2))

        self.ui.save.clicked.connect(lambda: self.save())

        self.ui.link_0.clicked.connect(lambda: self.links(0))
        # self.ui.link_1.clicked.connect(lambda: self.links(1))
        # self.ui.link_2.clicked.connect(lambda: self.links(2))
        # self.ui.link_3.clicked.connect(lambda: self.links(3))

        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)

        self.ui.ed.setText(str(dat["API"]))
        self.ui.ed_2.setText(str(dat["ID"]))

        # self.ui.com_0.setText(str(list(coms[0].keys())[0]))
        # self.ui.link_ed_0.setText(str(coms[0][list(coms[0].keys())[0]]))
        #
        # self.ui.com_1.setText(str(list(coms[1].keys())[0]))
        # self.ui.link_ed_1.setText(str(coms[1][list(coms[1].keys())[0]]))
        # self.ui.com_2.setText(str(list(coms[2].keys())[0]))
        # self.ui.link_ed_2.setText(str(coms[2][list(coms[2].keys())[0]]))

        self.ui.list_widget.itemDoubleClicked.connect(self.set_edit_text)
        #self.ui.delete_item.clicked.connect(self.remove_item)
        self.ui.add_item.clicked.connect(self.add_item_in)

        self.show()

    def add_item_in(self):
        keys = []
        for d in coms:
            if d != {'': ''}:
                keys.append(list(d.keys())[0])

        items = self.ui.list_widget.findItems("*", Qt.MatchWildcard)
        key = f"{self.ui.com_0.text()}:{self.ui.link_ed_0.text().split('/')[-1]}"

        if self.ui.com_0.text() == "" or self.ui.link_ed_0.text() == "" or self.ui.com_0.text() in keys:
            return
        else:
            for item in items:
                if item.text() == key:
                    return

        coms_list[key] = {self.ui.com_0.text(): self.ui.link_ed_0.text()}
        coms.append({self.ui.com_0.text(): self.ui.link_ed_0.text()})
        self.ui.list_widget.addItem(key)

    def set_edit_text(self, item):
        # Получаем текст выделенного элемента и устанавливаем его в QLineEdit
        text = item.text()
        command = list(coms_list[text].keys())[0]
        link = coms_list[text][command]
        # print(command)
        # print(link)
        self.ui.com_0.setText(command)
        self.ui.link_ed_0.setText(link)

        #item = self.ui.list_widget.currentItem()

        #print(item.text())
        #print(coms_list[item.text()])
        coms.remove(coms_list[item.text()])
        coms_list.pop(item.text())
        #print(coms_list)
        #print(coms)

        self.ui.list_widget.takeItem(self.ui.list_widget.row(item))
        #print(text)

    def save(self):
        dat = {'API': self.ui.ed.text(), 'ID': self.ui.ed_2.text()}
        open("settings/data.txt", "w").write(json.dumps(dat))
        open("settings/coms.txt", "w").write(json.dumps(coms))
        open("settings/coms_list.txt", "w").write(json.dumps(coms_list))


    def remove_item(self):
        # Получаем выбранный элемент и удаляем его из QListWidget
        item = self.ui.list_widget.currentItem()

        coms.remove(coms_list[item.text()])
        coms_list.pop(item.text())

        self.ui.list_widget.takeItem(self.ui.list_widget.row(item))

    def change(self, key=int):
        if key == 1:
            if self.ui.change.isChecked():
                self.ui.lab.show()
            else:
                self.ui.lab.hide()
        if key == 2:
            if self.ui.change_2.isChecked():
                self.ui.lab_2.show()
            else:
                self.ui.lab_2.hide()

    def str(self):
        os.startfile('bot.py')
        QApplication.quit()

    def links(self, but):
        try:
            buts = {0: self.ui.link_ed_0}
            wb_patch = QtWidgets.QFileDialog.getOpenFileName()[0]
            if wb_patch != "":
                buts[but].setText(wb_patch)
            else:
                pass
        except:
            pass

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
