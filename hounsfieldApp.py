from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QIcon
from gui import MainWindow

import qtmodern.styles
import qtmodern.windows


app = QApplication([])
app.setWindowIcon(QIcon('icon\\instrument.png'))
#qtmodern.styles.dark(app)
#window = qtmodern.windows.ModernWindow(MainWindow())
window =MainWindow()
window.show()
app.exec_()
