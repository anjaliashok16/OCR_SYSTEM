import base64
import sys
#import numpy as np
import pymysql
from PyQt5 import QtCore
from PyQt5.QtCore  import pyqtSlot
from PyQt5.QtGui import QImage , QPixmap
from PyQt5.QtWidgets import QDialog , QApplication
from PyQt5.uic import loadUi
from tkinter import messagebox
from subprocess import call


import datetime
import cv2
import pytesseract
from gtts import gTTS
import os
class tehseencode(QDialog):
	def __init__(self):
		super(tehseencode,self).__init__()
		#loadUi("student3.ui",self)
		loadUi("UI_Design.ui",self)
		
		self.logic = 0
		self.value = 0
		self.SHOW.clicked.connect(self.onClicked)
		self.TEXT.setText("Kindly Press 'Show' to connect with webcam.")
		self.CAPTURE.clicked.connect(self.CaptureClicked)
		self.STOP.clicked.connect(self.Stopme)

	@pyqtSlot()
	def onClicked(self):
		self.TEXT.setText('Kindly Press "Capture Image " to Capture image')
		cap =cv2.VideoCapture(0)
		#while (True):
		#print(cap.read())
		while(cap.isOpened()):
			ret, frame=cap.read()

			if ret==True:
				self.displayImage(frame,1)
				cv2.waitKey()
				if (self.logic==2):
					ct = datetime.datetime.now()
					self.ID = ct.strftime("%Y%m%d_%H%M%S")
					print(ct)
					print(self.ID)
					cv2.imwrite('D:/OCR_MAIN_PROJECT/Scanned_Storage/%s.png'%(self.ID),frame)
					self.logic= 1
					self.TEXT.setText('Your Image have been Saved at -D:/OCR_MAIN_PROJECT/Scanned_Storage/%s.png'%(self.value))
					print('CP# -01')
					self.Src_File = "D:/OCR_MAIN_PROJECT/Scanned_Storage/%s"%(self.ID)
					print("selfFile:------------")
					print(self.Src_File)
					pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
					print('CP# -0102')
					img = cv2.imread(self.Src_File + '.PNG')
					print('CP# -0103')
					img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
					print('CP# -02')
					ocr_text = pytesseract.image_to_string(img).replace("", " ")
					self.ocr_text=ocr_text
					print('CP# 01')
					print(ocr_text)
					print('CP# 02')
					hImg, wImg, _ = img.shape
					boxes = pytesseract.image_to_boxes(img)
					print('CP# 03')
					for b in boxes.splitlines():
						# print(b)
						b = b.split(' ')
						# print(b)
						x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
						cv2.rectangle(img, (x, hImg - y), (w, hImg - h), (0, 0, 225), 1)
						cv2.putText(img, b[0], (x, hImg - y + 25), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 1)

					#cv2.imshow('Result', img)
					self.Tgt_File = self.Src_File + '_OCR' + '.PNG'
					#self.ocr_filename = ocr_filename
					print('Here is the OCR_Converted Image Location' + self.Tgt_File)
					cv2.imwrite(self.Tgt_File, img)
					# Appending to an output file
					with open("output.txt", 'w') as file1:
						file1.write(ocr_text)
						file1.close()
					fh = open("output.txt", "r")
					mytext = fh.read().replace("\n", ". ",)#.replace(" ","")
					print("Pit Point- Check")
					print(mytext)
					fh.close()
					try:
						def read_file(filename):
							with open(filename, 'rb') as f:
								photo = f.read()
							return photo

						def write_blob(author_id, filename):
							data = read_file(filename)
							args = (author_id, data)
						Filename_captured = self.Src_File + '.PNG'
						with open(Filename_captured, 'rb') as f:
							photo_captured = f.read()
						self.encodestring_captured = base64.b64encode(photo_captured)
						print(self.encodestring_captured)
						Filename_ocr = self.Tgt_File
						with open(Filename_ocr, 'rb') as f:
							photo_ocr = f.read()
						self.encodestring_ocr = base64.b64encode(photo_ocr)
						print(self.encodestring_ocr)
					except Exception as e:
						print(e)

					try:
						con = pymysql.connect(host="localhost", user="root", password="administrator",	database="db_project_01")
						cur = con.cursor()
						sql = "insert into db_project_01.text(ID,IMG_CAPTURED_PATH,IMG_CAPTURED,IMG_OCR_PATH,IMG_OCR,EXTRACTED_TEXT) values (%s, %s, %s, %s, %s, %s)"
						val = (self.ID, self.Src_File + '.PNG', self.encodestring_captured, self.Tgt_File, self.encodestring_ocr, mytext)
						cur.execute(sql, val)
						con.commit()

						print (len(mytext))

						print("The zero length string without spaces is empty ? : ", end="")
						if (len(mytext.strip()) == 0):
							print("OCR has not detected any text within the given image.")
						else:
							print("Detected text,proceeding with Google TTS functionality")
							language = "en"
							output = gTTS(text=mytext, lang=language, slow=False)
							output.save("output_audio.mp3")
							os.system("start output_audio.mp3")
							print("cp#1")
							print(os.getpid())
							print("cp#2")
							cv2.waitKey(0)

					except Exception as e:
						print(e)
							#os.system("start output_audio.mp3")
					finally:
						cur.close()
						con.close()
			else:
				print('not found')
		cap.release()
		cv2.destroyAllWindows()
	def CaptureClicked(self):
		self.logic=2
	def Stopme(self):
		sys.exit(app.exec_())
	def displayImage(self,img,window=1):
		qformat=QImage.Format_Indexed8
		if len(img.shape)==3:
			if(img.shape[2])==4:
				qformat=QImage.Format_RGBA888
			else:
				qformat=QImage.Format_RGB888
		img = QImage(img,img.shape[1],img.shape[0],qformat)
		img = img.rgbSwapped()
		self.imgLabel.setPixmap(QPixmap.fromImage(img))
		self.imgLabel.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
app =  QApplication(sys.argv)
window=tehseencode()
window.show()
try:
	sys.exit(app.exec_())
except:
	print('excitng')
