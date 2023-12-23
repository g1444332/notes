from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog, QWidget
from ui import *
import json


app = QApplication([])
class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
note_names = []
with open("note.json",'r',encoding='utf-8') as file:
    notes = json.load(file)
    for n in notes:
        note_names.append(n)
ex = Widget()
ex.ui.listWidget.addItems(note_names)
print(ex.ui.listWidget)
def show_note():
    name = ex.ui.listWidget.selectedItems()[0].text()
    ex.ui.textEdit.setText(notes[name]["текст"])
    ex.ui.listWidget_2.clear()
    ex.ui.listWidget_2.addItems(notes[name]["теги"])
def add_note():
    notes_win = QWidget()
    note_name, result = QInputDialog.getText(
        notes_win, "Додати замітку", "Назва замітки:")
    notes[note_name]
def delete_note():
    pass

ex.ui.listWidget.itemClicked.connect(show_note)
ex.ui.pushButton.clicked.connect(add_note)

ex.show()
app.exec_()