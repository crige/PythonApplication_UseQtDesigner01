#方法1：定制一个模板来引用UI文件，实现UI与主体PY程序分离
#http://pythonforengineers.com/your-first-gui-app-with-python-and-pyqt/ 中的评论部分有PyQt5的版本

import sys
#from PyQt4 import QtCore, QtGui, uic
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5 import uic

qtCreatorFile = "C:\\Users\\crige\\source\\repos\\Learn_Pyqt5\\PythonApplication_UseQtDesigner01\\PythonApplication_UseQtDesigner01\\PythonApplication_UseQtDesigner01_form.ui"# Enter file here
#注意路径直接写成：qtCreatorFile = 'PythonApplication_UseQtDesigner01_form.ui' 也是可以的。但是用Pyinstaller生成EXE文件时会提示找不到UI文件，
#这个提示只有在命令行下才能看到此提示，在Windows下则一闪而过。经测试，此种方法还是有缺陷，如果将UI文件改名，EXE文件仍不能运行。
#解决办法，还是要将UI文件拷贝到EXE文件下。
Ui_MainWindow,QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QMainWindow):#PyQt4 is:class MyApp(QtGui.QMainWindow,Ui_MainWindow):
    def __init__(self):
        '''Use PyQt4:
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        '''
        super(MyApp,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Calc_Tax_Button.clicked.connect(self.CalculateTax)
    def CalculateTax(self):
        price = int(self.ui.price_box.toPlainText())
        tax = (self.ui.tax_rate.value())
        total_price = price + ((tax/100)*price)
        total_price_string = "The total price with tax is: "+str(total_price)
        self.ui.results_window.setText(total_price_string)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())