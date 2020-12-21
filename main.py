from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import PaGeMain
import random
from scapy.all import *

class ExampleApp(QtWidgets.QMainWindow, PaGeMain.Ui_Dialog):
    dbg = 1
    dIPFlag = 0

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
    #     self.ResRadioBtn.clicked.connect(self.block_DF_MF)
    #     self.DFRadioBtn.clicked.connect(self.block_RES_MF)
    #     self.MFRadioBtn.clicked.connect(self.block_RES_DF)

    # def block_DF_MF(self):
    #     self.dIPFlag = 0
    #     self.log_write("Log: DF_MF btn disabled")

    # def block_RES_MF(self):
    #     self.dIPFlag = 1
    #     self.ResRadioBtn.setDisabled()
    #     self.MFRadioBtn.setDisabled()
    #     self.log_write("Log: Res_MF btn disabled")

    # def block_RES_DF(self):
        # self.dIPFlag = 2
        # self.DFRadioBtn.setDisabled()
        # self.MFRadioBtn.setDisabled()
        # self.log_write("Log: Res_DF btn disabled")

    def genRandMAC(self):
        return "02:00:00:%02x:%02x:%02x" % (random.randint(0, 255),
                             random.randint(0, 255),
                             random.randint(0, 255))

    def ex_prog(self):
        print ('Close app')
        exit(0)

    def send_packet(self):
        sTarget = ""
        dCurIdx = self.PacketTabWidget.currentIndex()
        self.log_write("Log: Target: " + sTarget)

        sIPSrc = self.IPSrcEdit.toPlainText()
        sIPDst = self.IPDstEdit.toPlainText()
        dIPVer = int(self.VersionEdit.toPlainText())
        dIPIhl = int(self.IHLEdit.toPlainText())
        dIPID = int(self.IDEdit.toPlainText())
        dTTL = int(self.TTLEdit.toPlainText())
        dProto = int(self.ProtocolEdit.toPlainText())
        if (self.ChsumCheck.isEnabled()):
            dChkSum = random.randint()
        else:
            dChkSum = int(self.ChsumEdit.toPlainText())
        dType = int(self.TypeEdit.toPlainText())
        dFrag = int(self.FragEdit.toPlainText())
        if (self.ResRadioBtn.isEnabled()):
            dIPFlag = 0
        if (self.DFRadioBtn.isEnabled()):
            dIPFlag = 1
        if (self.MFRadioBtn.isEnabled()):
            dIPFlag = 2

        dTOS = 0
        
        if (self.PrecCheckBox0.isEnabled()):
            dTOS |= 0x0000001
        if (self.PrecCheckBox1.isEnabled()):
            dTOS |= 0x0000010
        if (self.PrecCheckBox2.isEnabled()):
            dTOS |= 0x0000100
        if (self.DelayCheck.isEnabled()):
            dTOS |= 0x0001000
        if (self.ThrCheck.isEnabled()):
            dTOS |= 0x0001000
        if (self.ReliabCheck.isEnabled()):
            dTOS |= 0x0010000
        if (self.ECNCheckBox0.isEnabled()):
            dTOS |= 0x0100000
        if (self.ECNCheckBox1.isEnabled()):
            dTOS |= 0x1000000
    
        dTL = int(self.TLEdit.toPlainText())
        dIHL = int(self.IHLEdit.toPlainText())

        if (self.MacSrcCheck.isEnabled()):
            sSrcMAC = genRandMAC()
        else:
            sSrcMAC = self.MacSrcEdit.toPlainText()

        if (self.MacDstCheck.isEnabled()):
            sDstMAC = genRandMAC()
        else:
            sDstMAC = self.MacDstEdit.toPlainText()
        

# TCP
        if (dCurIdx == 0):


# UDP
        if (dCurIdx == 1):


# ICMP   
        if (dCurIdx == 2):



        print ('Packet send')    

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()