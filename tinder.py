import pymongo
from PyQt5.QtWidgets import *

my_client = pymongo.MongoClient("mongodb://localhost:27017")
my_db = my_client["Logika_15"]
my_col = my_db["Test"]

app = QApplication([])

window = QWidget()
window.setWindowTitle("Criminal Tinder")
window.setFixedSize(400, 400)

label = QLabel("Photo", window)
label.setFixedSize(70, 20)
label.move(160, 160)

but0 = QPushButton("<", window)
but1 = QPushButton(">", window)

but0.move(115, 200)
but1.move(195, 200)

num = 0

def incr(): 
    global num   
    slovar = my_col.find_one({"app":"criminal"})
    spisok = slovar["photos"]
    try:        
        label.setText(spisok[num])
    except:
        num = 0
        label.setText(spisok[num])
    num += 1

but1.clicked.connect(incr)

window.show()

app.exec()