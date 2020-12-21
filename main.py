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

        adapt_list = get_if_list()
        for adapt in adapt_list:
            self.AdapterComboBox.addItem(adapt)
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
        sProto = self.ProtocolEdit.toPlainText()
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

        packet = IP(dst=sIPSrc, src=sIPDst, version = dIPVer, ihl = dIHl, tos = dTOS, len = dTL, id = dIPID, flags = dIPFlag, frag = dFrag, ttl = dTTL, proto = sProto, chksum = dChkSum)

        dPortSrc = 0
        dPortDst = 0
        dSeqNum = 0
        dAckNum = 0
        dWinNum = 0
        dTCPChsum = 0
        dUDPChsum = 0
        dUDPLen = 0
        dICMPType = 0
        dICMPCode = 0
        dICMPID = 0
        dICMPSeq = 0
        dICMPMsg = 0
# TCP
        if (dCurIdx == 0):
            if (self.PortSrcCheck.toPlainText())
                dPortSrc = random.randint()
            else:
                dPortSrc = int(self.PortSrcEdit.toPlainText())

            if (self.PortDestCheck.toPlainText())
                dPortDst = random.randint()
            else:
                dPortDst = int(self.PortDestEdit.toPlainText())

            if (self.SeqNCheck.toPlainText())
                dSeqNum = random.randint()
            else:
                dSeqNum = int(self.SeqNEdit.toPlainText())

            if (self.AckNCheck.toPlainText())
                dAckNum = random.randint()
            else:
                dAckNum = int(self.AckNEdit.toPlainText())                

            if (self.WinCheck.toPlainText())
                dWinNum = random.randint()
            else:
                dWinNum = int(self.WinEdit.toPlainText())  

            if (self.UrgCheck.toPlainText())
                dUrgNum = random.randint()
            else:
                dUrgNum = int(self.UrgEdit.toPlainText())  

            dOff = int(self.OffsEdit.toPlainText())  

            if (self.TCPChsumCheck.toPlainText())
                dTCPChsum = random.randint()
            else:
                dTCPChsum = int(self.TCPChsumEdit.toPlainText())  

            if (self.TCPChsumCheck.toPlainText())
                dTCPChsum = random.randint()
            else:
                dTCPChsum = int(self.TCPChsumEdit.toPlainText())  

            dTCPFlags = 0x000000000
            if (self.URGCheck.toPlainText())
                dTCPFlags |= 0x000000001          

            if (self.ACKCheck.toPlainText())
                dTCPFlags |= 0x000000010 

            if (self.PSHCheck.toPlainText())
                dTCPFlags |= 0x000000100 

            if (self.RSTCheck.toPlainText())
                dTCPFlags |= 0x000001000 

            if (self.SYNCheck.toPlainText())
                dTCPFlags |= 0x000010000 

            if (self.FINCheck.toPlainText())
                dTCPFlags |= 0x000100000 

            if (self.CWRCheck.toPlainText())
                dTCPFlags |= 0x001000000

            if (self.ECECheck.toPlainText())
                dTCPFlags |= 0x010000000

            packet /= TCP(sport = dPortSrc, dport = dPortDst, seq = dSeqNum, ack = dAckNum, dataofs = dOff, flags = dTCPFlags, windows = dWinNum, chksum = dTCPChsum, urgptr = dUrgNum)

# UDP
        if (dCurIdx == 1):

            if (self.UDPPortDestCheck.toPlainText())
                dPortSrc = random.randint()
            else:
                dPortSrc = int(self.UDPPortSrcEdit.toPlainText())

            if (self.UDPPortDestCheck.toPlainText())
                dPortDst = random.randint()
            else:
                dPortDst = int(self.UDPPortDestEdit.toPlainText())

            if (self.UDPChsumCheck.toPlainText())
                dUDPChsum = random.randint()
            else:
                dUDPChsum = int(self.UDPChsumEdit.toPlainText())  

            if (self.UDPLenCheck.toPlainText())
                dUDPLen = random.randint()
            else:
                dUDPLen = int(self.UDPLenEdit.toPlainText())  

            packet /= UDP(sport = dPortSrc, dport = dPortDst, chksum = dUDPChsum, len = dUDPLen)

# ICMP   
        if (dCurIdx == 2):
            dICMPCode = int(self.CodeICMPEdit.toPlainText())  
            dICMPID = int(self.IDICMPEdit.toPlainText())  
            dICMPSeq = int(self.SeqICMPEdit.toPlainText())  
            dIdx = self.ICMPMCombo.currentIndex()
            if (dIdx == 0):
                dICMPMsg = 0
            else:
                dICMPMsg = 8
            packet /= ICMP(type = dICMPMsg, code = dICMPCode, id = dICMPID, seq = dICMPSeq)


        sData = self.FinalDataEdit.toPlainText()
        packet /= sData

        sAdapter = self.AdapterComboBox.currentText()
        sendp(packet,sAdapter)
        print ('Packet send')    

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()