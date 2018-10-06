import sys
from PyQt5.QtWidgets import (QInputDialog,QMainWindow,QApplication)
from PythonApplication_UseQtDesigner02_form_QInputDialog import Ui_MainWindow

class MyApp(QMainWindow):
    def __init__(self):
        super(MyApp,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.showDialog)
        self.setWindowTitle('Input dialog')
    def showDialog(self):
        text,ok = QInputDialog.getText(self,'Input Dialog','Enter your name:')

        if ok:
            self.ui.lineEdit.setText(str(text))
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())