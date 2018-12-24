import sys
import logging
import random
from PyQt5.QtWidgets import *
from PyQt.FlipCoin.Flips import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt.FlipCoin.MatplotlibWidget import *
import matplotlib
import numpy as np

class FlipCoin(QMainWindow, Ui_MainWindow):

    def __init__(self, parent = None):
        super(FlipCoin, self).__init__(parent)
        self.setupUi(self)
        self.coin_number_le.setValidator(QIntValidator(self))
        self.p_up_le.setReadOnly(True)
        self.p_down_le.setReadOnly(True)
        self.coin_number_up_le.setReadOnly(True)
        self.coin_number_down_le.setReadOnly(True)

        self.flipcoin.clicked.connect(self.flipCoin)
        self.flip_fcoins.clicked.connect(lambda: self.flipcoins(self.flip_fcoins))
        self.flip_tcoins.clicked.connect(lambda: self.flipcoins(self.flip_tcoins))
        self.exit_button.clicked.connect(self.exitEvent)
        # self.xValue = np.array([])
        # self.yValue = np.array([])
        self.xValue = []
        self.yValue = []

    @pyqtSlot()
    def flipCoin(self):
        self.xValue.clear()
        self.yValue.clear()
        cnumber = (int)(self.coin_number_le.text())
        head = 0
        tail = 0
        allcount = 0
        for i in range(1, cnumber + 1):
            hort = random.randint(0, 1)
            if hort == 0:
                head = head + 1
            else:
                tail = tail + 1
            self.xValue.append(i)
            self.yValue.append(head / i)
            # np.append(self.xValue, cnumber)
            # np.append(self.yValue, head/cnumber)
        print(self.yValue)
        self.drawPlot(self.xValue, self.yValue)
        self.coin_number_up_le.setText(str(head))
        self.coin_number_down_le.setText(str(tail))
        self.p_up_le.setText(str(head/cnumber))
        self.p_down_le.setText(str(tail/cnumber))


    @pyqtSlot()
    def flipcoins(self, btn):
        if btn.text() == '10 coins':
            tmp_num = 10
        elif btn.text() == '50 coins':
            tmp_num = 50
        cnumber = (int)(self.coin_number_le.text())
        head = (int)(self.coin_number_up_le.text())
        tail = (int)(self.coin_number_down_le.text())


        for i in range(1, tmp_num + 1):
            hort = random.randint(0,1)
            if hort == 0:
                head = head + 1
            else:
                tail = tail + 1
            self.xValue.append(cnumber + i)
            #print(head, cnumber+i)
            self.yValue.append(head / (cnumber + i))
        #print(self.yValue)
        cnumber = cnumber + tmp_num
        self.coin_number_le.setText(str(cnumber))
        self.coin_number_up_le.setText(str(head))
        self.coin_number_down_le.setText(str(tail))
        self.p_up_le.setText(str(head/cnumber))
        self.p_down_le.setText(str(tail/cnumber))
        self.drawPlot(self.xValue, self.yValue)

    @pyqtSlot()
    def exitEvent(self):
        qApp = QApplication.instance()
        qApp.quit()

    def drawPlot(self, xValue, yValue):
        # logging.info('show probility image')
        cur_plot = self.matplotwidget
        cur_plot.fig.clear()
        subplot = cur_plot.getFigure().add_subplot(111)
        subplot.plot(xValue, yValue)
        cur_plot.draw()







if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = FlipCoin()
    win.show()
    sys.exit(app.exec_())