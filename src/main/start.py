import sys

from src.main.mazes_dialog import *

app = QtWidgets.QApplication(sys.argv)
dialog = PyMazesDialog()
dialog.show()
sys.exit(app.exec_())
