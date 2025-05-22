from PyQt5.QtWidgets import (
   QApplication, QWidget,
   QFileDialog, # Diálogo para abrir archivos (y carpetas)
   QLabel, QPushButton, QListWidget,
   QHBoxLayout, QVBoxLayout
)
 
app = QApplication([])
win = QWidget()       
win.resize(700, 500) 
win.setWindowTitle('Editor simple')
lb_image = QLabel("Imagen")
btn_dir = QPushButton("Carpeta")
lw_files = QListWidget()
 
btn_left = QPushButton("Izquierda")
btn_right = QPushButton("Derecha")
btn_flip = QPushButton("Reflejo")
btn_sharp = QPushButton("Nitidez")
btn_bw = QPushButton("B/N")
 
row = QHBoxLayout()          # Línea principal
col1 = QVBoxLayout()         # dividida en dos columnas
col2 = QVBoxLayout()
col1.addWidget(btn_dir)      # en la primera – botón de selección de directorio
col1.addWidget(lw_files)     # y lista de archivos
col2.addWidget(lb_image, 95) # en la segunda – imagen
row_tools = QHBoxLayout()    # y el botón
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
app.exec()
