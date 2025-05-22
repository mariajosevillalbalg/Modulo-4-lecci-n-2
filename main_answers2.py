import os
from PyQt5.QtWidgets import (
   QApplication, QWidget, QFileDialog,
   QLabel, QPushButton, QListWidget,
   QHBoxLayout, QVBoxLayout
)
from PyQt5.QtGui import QPixmap

app = QApplication([])
win = QWidget()
win.resize(700, 500)
win.setWindowTitle('Editor simple')
lb_image = QLabel("Imagen")
lb_image.setStyleSheet("background-color: #eee; border: 1px solid #ccc")
lb_image.setScaledContents(True)

btn_dir = QPushButton("Carpeta")
lw_files = QListWidget()

btn_left = QPushButton("Izquierda")
btn_right = QPushButton("Derecha")
btn_flip = QPushButton("Reflejo")
btn_sharp = QPushButton("Nitidez")
btn_bw = QPushButton("B/N")

row = QHBoxLayout()
col1 = QVBoxLayout()
col2 = QVBoxLayout()
col1.addWidget(btn_dir)
col1.addWidget(lw_files)
col2.addWidget(lb_image, 95)
row_tools = QHBoxLayout()
row_tools.addWidget(btn_left)
row_tools.addWidget(btn_right)
row_tools.addWidget(btn_flip)
row_tools.addWidget(btn_sharp)
row_tools.addWidget(btn_bw)
col2.addLayout(row_tools)

row.addLayout(col1, 20)
row.addLayout(col2, 80)
win.setLayout(row)

win.show()

workdir = ''

def filter(files, extensions):
   result = []
   for filename in files:
       for ext in extensions:
           if filename.lower().endswith(ext):
               result.append(filename)
   return result

def chooseWorkdir():
   global workdir
   workdir = QFileDialog.getExistingDirectory()

def showFilenamesList():
   extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
   chooseWorkdir()
   filenames = filter(os.listdir(workdir), extensions)
   lw_files.clear()
   for filename in filenames:
       lw_files.addItem(filename)

def showChosenImage():
    if lw_files.currentRow() >= 0:
        filename = lw_files.currentItem().text()
        full_path = os.path.join(workdir, filename)
        pixmap = QPixmap(full_path)
        if not pixmap.isNull():
            lb_image.setPixmap(pixmap.scaled(
                lb_image.width(), lb_image.height(), aspectRatioMode=1
            ))
        else:
            lb_image.setText("No se pudo cargar la imagen")

btn_dir.clicked.connect(showFilenamesList)
lw_files.currentRowChanged.connect(showChosenImage)

app.exec()

