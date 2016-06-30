import sys

from PyQt5 import QtWidgets

from src.start.start import PyMazesDialog


app = QtWidgets.QApplication(sys.argv)
dialog = PyMazesDialog()
dialog.show()
sys.exit(app.exec_())