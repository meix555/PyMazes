import sys

from PyQt5 import QtWidgets

from src.start.mazes_dialog import PyMazesDialog


app = QtWidgets.QApplication(sys.argv)
dialog = PyMazesDialog()
dialog.show()
sys.exit(app.exec_())