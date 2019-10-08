# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import QDir
from PyQt5.QtGui import QPixmap, QIcon
import md4, md5
import mw

class MD45(QtWidgets.QMainWindow, mw.Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)  # Для инициализации дизайна
		self.setWindowTitle("Вычисление hash-суммы MD4/MD5")

		# вставляем изображение
		pixmap = QPixmap("img.bmp")
		self.label_for_image.setPixmap(pixmap)
		self.setWindowIcon(QIcon('icon.ico')) 

		# connect
		self.pbOpenFile.clicked.connect(self.openFile) # open file to hash
		self.pbHashFile.clicked.connect(self.hashFile) # hash file
		self.pbHashString.clicked.connect(self.hashString) # hash string

	# открытие файла
	def openFile(self):
		self.file_path = QFileDialog.getOpenFileName(self, 'Open file', QDir.currentPath())
		self.label_CheckFile.setText("файл открыт")

	# хэш файла
	def hashFile(self):
		with open(self.file_path[0], "rb") as f:
			file = f.read()

		md4_res = md4.md4_hash(file).hex()
		md5_res = md5.md5_hash(file).hex()

		self.leMD4.setText(md4_res)
		self.leMD5.setText(md5_res)

	# хэш строки
	def hashString(self):
		hash_string = self.leString.text().encode()

		md4_res = md4.md4_hash(hash_string).hex()
		md5_res = md5.md5_hash(hash_string).hex()

		self.leMD4.setText(md4_res)
		self.leMD5.setText(md5_res)

def main():
	app = QtWidgets.QApplication(sys.argv) # Новый экземпляр QApplication
	window = MD45() # Создаем объект класса ExampleApp
	window.show() # Показать окно
	app.exec() # Запускаем приложение

if __name__ == '__main__': # Если мы запусаем файл напрямую, а не импортируем
	main()