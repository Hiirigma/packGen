from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import PaGeMain
from scapy.all import *

class ExampleApp(QtWidgets.QMainWindow, PaGeMain.Ui_Dialog):
    dbg = 1

    def log_write(self,sMsg):
        if self.dbg == 1:
            print (sMsg)


    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.cancelButton.clicked.connect(self.ex_prog)
        self.sendButton.clicked.connect(self.send_packet)

    def ex_prog(self):
        print ('Close app')
        exit(0)

    def send_packet(self):
        sTarget = ""
        dCurIdx = self.PacketTabWidget.currentIndex()
        if (dCurIdx == 0):
            sTarget = "TCP"
        if (dCurIdx == 1):
            sTarget = "UDP"
        if (dCurIdx == 2):
            sTarget = "ICMP"

        self.log_write("Log: Target: " + sTarget)

        sIPSrc = self.IPSrcEdit.toPlainText()
        sIPDst = self.IPDstEdit.toPlainText()
        dIPVer = int(self.VersionEdit.toPlainText())
        dIPIhl = int(self.IHLEdit.toPlainText())
        dIPID = int(self.IDEdit.toPlainText())
        dTTL = int(self.TTLEdit.toPlainText())
        dProto = int(self.ProtocolEdit.toPlainText())
        dChkSum = int(self.ChsumEdit.toPlainText())
        dFrag = int(self.FragEdit.toPlainText())

        
        self.log_write("Log: Target: " + sIPSrc)
        self.log_write("Log: Target: " + sIPDst)

        print ('Packet send')        

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()