import sys
from PyQt5.QtWidgets import QApplication, QWidget, QCalendarWidget, QPushButton, \
							QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QTextCharFormat, QIcon
import pandas as pd

class Calenderio(QCalendarWidget):
	def __init__(self):
		super().__init__()
		self.from_date = None
		self.to_date = None

		self.highlighter_format = QTextCharFormat()
		# get the calendar default highlight setting
		self.highlighter_format.setBackground(self.palette().brush(QPalette.Highlight))
		self.highlighter_format.setForeground(self.palette().color(QPalette.HighlightedText))


		# this will pass selected date value as a QDate object
		self.clicked.connect(self.select_range)

		super().dateTextFormat()

	def highlight_range(self, format):
		if self.from_date and self.to_date:
			d1 = min(self.from_date, self.to_date)
			d2 = max(self.from_date, self.to_date)
			while d1 <= d2:
				self.setDateTextFormat(d1, format)
				d1 = d1.addDays(1)

	def select_range(self, date_value):
		self.highlight_range(QTextCharFormat())

		# check if a keyboard modifer is pressed
		if QApplication.instance().keyboardModifiers() & Qt.ShiftModifier and self.from_date:
			self.to_date = date_value
			# print(self.from_date, self.to_date)
			self.highlight_range(self.highlighter_format)
		else:
			# required
			self.from_date = date_value
			self.to_date = None
			# print(self.from_date, self.to_date, 'x')


## FINE APP




#if __name__ == '__main__':
	# don't auto scale when drag app to a different monitor.
	# QApplication.setAttribute(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)

	#app = QApplication(sys.argv)

	#myApp = MyApp()
	#myApp.show()


