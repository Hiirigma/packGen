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
        adapt_list = get_if_list()
        for adapt in adapt_list:
            self.AdapterComboBox.addItem(adapt)
        self.cancelButton.clicked.connect(self.ex_prog)
        self.sendButton.clicked.connect(self.send_packet)
        self.MacDestCheck.clicked.connect(self.updMacDest)
        self.MacSrcCheck.clicked.connect(self.updMacSrc)
        self.ChsumCheck.clicked.connect(self.updChSum)
        self.PortSrcCheck.clicked.connect(self.updSPort)
        self.PortDestCheck.clicked.connect(self.updDPort)
        self.TCPChsumCheck.clicked.connect(self.upddTCPChsum)        
        self.UrgCheck.clicked.connect(self.upddUrgNum)
        self.WinCheck.clicked.connect(self.upddWinNum)
        self.AckNCheck.clicked.connect(self.upddAckNum)
        self.SeqNCheck.clicked.connect(self.upddSeqNum)
        
        self.UDPLenCheck.clicked.connect(self.upddUDPLen)
        self.UDPChsumCheck.clicked.connect(self.upddUDPChsum)
        self.UDPPortSrcCheck.clicked.connect(self.updUDPdPortSrc)
        self.UDPPortDestCheck.clicked.connect(self.updUDPdPortDst)

    def upddUDPLen(self): 
        dUDPLen = random.randint()
        self.UDPLenEdit.setText(str(dUDPLen))

    def upddUDPChsum(self): 
        dUDPChsum = random.randint()
        self.UDPChsumEdit.setText(str(dUDPChsum))

    def updUDPdPortSrc(self): 
        dPortSrc = random.randint()
        self.UDPPortSrcEdit.setText(str(dPortSrc))

    def updUDPdPortDst(self): 
        dPortDst = random.randint()
        self.UDPPortDestEdit.setText(str(dPortDst))

    def upddTCPChsum(self): 
        dTCPChsum = random.randint()
        self.TCPChsumEdit.setText(str(dTCPChsum))

    def upddUrgNum(self): 
        dUrgNum = random.randint()
        self.UrgEdit.setText(str(dUrgNum))

    def upddWinNum(self): 
        dWinNum = random.randint()
        self.WinEdit.setText(str(dWinNum))

    def upddAckNum(self): 
        dAckNum = random.randint()
        self.AckNEdit.setText(str(dAckNum))

    def upddSeqNum(self): 
        dSeqNum = random.randint()
        self.SeqNEdit.setText(str(dSeqNum))


    def updSPort(self):
        dPortSrc = random.randint()
        self.PortSrcEdit.setText(str(dPortSrc))

    def updDPort(self):
        dPortDst = random.randint()
        self.PortDestEdit.setText(str(dPortDst))

    def updChSum(self):
        dChkSum = random.randint()
        self.ChsumEdit.setText(str(dChkSum))


    def updMacDest(self):
        sDstMAC = self.genRandMAC()
        self.MacDestEdit.setText(sDstMAC)

    def updMacSrc(self):
        sSrcMAC = self.genRandMAC()
        self.MacSrcEdit.setText(sSrcMAC)


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


        sSrcMAC = self.MacSrcEdit.toPlainText()
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

            dPortSrc = int(self.PortSrcEdit.toPlainText())
            dPortDst = int(self.PortDestEdit.toPlainText())
            dSeqNum = int(self.SeqNEdit.toPlainText())
            dAckNum = int(self.AckNEdit.toPlainText())                
            dWinNum = int(self.WinEdit.toPlainText())  
            dUrgNum = int(self.UrgEdit.toPlainText())  
            dOff = int(self.OffsEdit.toPlainText())  
            dTCPChsum = int(self.TCPChsumEdit.toPlainText())  

            dTCPFlags = 0x000000000
            if (self.URGCheck.isEnabled()):
                dTCPFlags |= 0x000000001          

            if (self.ACKCheck.isEnabled()):
                dTCPFlags |= 0x000000010 

            if (self.PSHCheck.isEnabled()):
                dTCPFlags |= 0x000000100 

            if (self.RSTCheck.isEnabled()):
                dTCPFlags |= 0x000001000 

            if (self.SYNCheck.isEnabled()):
                dTCPFlags |= 0x000010000 

            if (self.FINCheck.isEnabled()):
                dTCPFlags |= 0x000100000 

            if (self.CWRCheck.isEnabled()):
                dTCPFlags |= 0x001000000

            if (self.ECECheck.isEnabled()):
                dTCPFlags |= 0x010000000

            packet /= TCP(sport = dPortSrc, dport = dPortDst, seq = dSeqNum, ack = dAckNum, dataofs = dOff, flags = dTCPFlags, windows = dWinNum, chksum = dTCPChsum, urgptr = dUrgNum)

# UDP
        if (dCurIdx == 1):
            dPortSrc = int(self.UDPPortSrcEdit.toPlainText())
            dPortDst = int(self.UDPPortDestEdit.toPlainText())
            dUDPChsum = int(self.UDPChsumEdit.toPlainText())  
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