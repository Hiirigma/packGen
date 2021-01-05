from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import PaGeMain
import random
from scapy.all import *


class ExampleApp(QtWidgets.QMainWindow, PaGeMain.Ui_Dialog):
    dbg = 0
    dIPFlag = 0
    bUDPLen = False
    bUDPChsum = False
    bPortSrc = False
    bPortDst = False
    bTCPChsum = False
    bUrgNum = False
    bWinNum = False
    bAckNum = False
    bSeqNum = False
    bPortSrc2 = False
    bPortDst2 = False
    bChkSum = False
    bDstMAC = False
    bSrcMAC = False
    dPacketCnt = 0

    lPacketList = [0 for i in range(64)]

    def log_write(self,sMsg):
        if self.dbg == 1:
            print (sMsg)


    def __init__(self):
        super().__init__()
        self.setupUi(self)

        adapt_list = get_if_list()
        for adapt in adapt_list:
            self.AdapterComboBox.addItem(adapt)
        
        self.cancelButton.clicked.connect(self.ex_prog)
        self.sendButton.clicked.connect(self.send_packet)
        self.queueButton.clicked.connect(self.create_packet)

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
        if self.bUDPLen == False:
            dUDPLen = random.randint(0,65535)
            self.UDPLenEdit.setText(str(dUDPLen))
            self.bUDPLen = True
        else:
            self.bUDPLen = False
            self.UDPLenEdit.clear()

    def upddUDPChsum(self): 
        if self.bUDPChsum == False:
            dUDPChsum = random.randint(0,65535)
            self.UDPChsumEdit.setText(str(dUDPChsum))
            self.bUDPChsum = True
        else:
            self.UDPChsumEdit.clear()

            bUDPChsum = False

    def updUDPdPortSrc(self): 
        if self.bPortSrc == False:
            dPortSrc = random.randint(0,65535)
            self.UDPPortSrcEdit.setText(str(dPortSrc))
            self.bPortSrc = True
        else:
            self.UDPPortSrcEdit.clear()
            self.bPortSrc = False


    def updUDPdPortDst(self): 
        if bPortDst == False:
            self.dPortDst = random.randint(0,65535)
            self.UDPPortDestEdit.setText(str(dPortDst))
            self.bPortDst = True
        else:
            self.UDPPortDestEdit.clear()
            self.bPortDst = False

    def upddTCPChsum(self):
        if self.bTCPChsum == False:
            dTCPChsum = random.randint(0,65535)
            self.TCPChsumEdit.setText(str(dTCPChsum))
            self.bTCPChsum = True
        else:
            self.TCPChsumEdit.clear()
            self.bTCPChsum = False

    def upddUrgNum(self): 
        if self.bUrgNum == False:
            dUrgNum = random.randint(0,65535)
            self.UrgEdit.setText(str(dUrgNum))
            self.bUrgNum = True
        else:
            self.UrgEdit.clear()
            self.bUrgNum = False


    def upddWinNum(self): 
        if self.bWinNum == False:
            dWinNum = random.randint(0,65535)
            self.WinEdit.setText(str(dWinNum))
            self.bWinNum = True
        else:
            self.WinEdit.clear()
            self.bWinNum = False


    def upddAckNum(self): 
        if self.bAckNum == False:
            dAckNum = random.randint(0,65535)
            self.AckNEdit.setText(str(dAckNum))
            self.bAckNum = True
        else:
            self.AckNEdit.clear()
            self.bAckNum = False



    def upddSeqNum(self): 
        if self.bSeqNum == False:
            dSeqNum = random.randint(0,65535)
            self.SeqNEdit.setText(str(dSeqNum))
            self.bSeqNum = True
        else:
            self.SeqNEdit.clear()
            self.bSeqNum = True


    def updSPort(self):
        if self.bPortSrc2 == False:
            dPortSrc = random.randint(0,65535)
            self.PortSrcEdit.setText(str(dPortSrc))
            self.bPortSrc2 = True
        else:
            self.PortSrcEdit.clear()
            self.bPortSrc2 = False

    def updDPort(self):
        if self.bPortDst2 == False:
            dPortDst = random.randint(0,65535)
            self.PortDestEdit.setText(str(dPortDst))
            self.bPortDst2 = True
        else:
            self.PortDestEdit.clear()
            self.bPortDst2 = False

    def updChSum(self):
        if self.bChkSum == False:
            dChkSum = random.randint(0,65535)
            self.ChsumEdit.setText(str(dChkSum))
            self.bChkSum = True
        else:
            self.ChsumEdit.clear()
            self.bChkSum = False


    def updMacDest(self):
        if self.bDstMAC == False:
            sDstMAC = self.genRandMAC()
            self.MacDestEdit.setText(sDstMAC)
            self.bDstMAC = True
        else:
            self.MacDestEdit.clear()
            self.bDstMAC = False

    def updMacSrc(self):
        if self.bSrcMAC == False:
            sSrcMAC = self.genRandMAC()
            self.MacSrcEdit.setText(sSrcMAC)
            self.bSrcMAC = True
        else:
            self.MacSrcEdit.clear()
            self.bSrcMAC = False


    def genRandMAC(self):
        return "02:00:00:%02x:%02x:%02x" % (random.randint(0, 255),
                             random.randint(0, 255),
                             random.randint(0, 255))

    def ex_prog(self):
        print ('Close app')
        exit(0)



    def create_packet(self):
        sTarget = ""
        dCurIdx = self.PacketTabWidget.currentIndex()
        self.log_write("Log: Target: " + sTarget)

        sIPSrc = self.IPSrcEdit.toPlainText()
        sIPDst = self.IPDstEdit.toPlainText()
        if (self.VersionEdit.toPlainText() != ''):
            dIPVer = int(self.VersionEdit.toPlainText())
        else:
            dIPVer = 4

        if (self.IHLEdit.toPlainText() != ''):
            dIPIhl = int(self.IHLEdit.toPlainText())
        else:
            dIPIhl = None

        if (self.IDEdit.toPlainText() != ''):    
            dIPID = int(self.IDEdit.toPlainText())
        else:
            dIPID = 1

        if (self.TTLEdit.toPlainText() != ''):
            dTTL = int(self.TTLEdit.toPlainText())
        else:
            dTTL = 64
        
        if (self.ChsumEdit.toPlainText() != ''):
            dChkSum = int(self.ChsumEdit.toPlainText())
        else:
            dChkSum = None


        if (self.ProtocolEdit.toPlainText() != ''):
            sProto = self.ProtocolEdit.toPlainText()
        else:
            sProto = 'ip'


        if (self.TypeEdit.toPlainText() != ''):
            dType = int(self.TypeEdit.toPlainText())
        else:
            dType = None
        
        if (self.FragEdit.toPlainText() != ''):
            dFrag = int(self.FragEdit.toPlainText())
        else:
            dFrag = 0

        dIPFlag = 0
        if (self.ResRadioBtn.isChecked()):
            dIPFlag = 0
        if (self.DFRadioBtn.isChecked()):
            dIPFlag = 1
        if (self.MFRadioBtn.isChecked()):
            dIPFlag = 2

        dTOS = 0
        
        if (self.PrecCheckBox0.isChecked()):
            dTOS |= 0x0000001
        if (self.PrecCheckBox1.isChecked()):
            dTOS |= 0x0000010
        if (self.PrecCheckBox2.isChecked()):
            dTOS |= 0x0000100
        if (self.DelayCheck.isChecked()):
            dTOS |= 0x0001000
        if (self.ThrCheck.isChecked()):
            dTOS |= 0x0001000
        if (self.ReliabCheck.isChecked()):
            dTOS |= 0x0010000
        if (self.ECNCheckBox0.isChecked()):
            dTOS |= 0x0100000
        if (self.ECNCheckBox1.isChecked()):
            dTOS |= 0x1000000
    

        if (self.TLEdit.toPlainText() != ''):
            dTL = int(self.TLEdit.toPlainText())
        else:
            dTL = None
        
        if (self.IHLEdit.toPlainText() != ''):
            dIHL = int(self.IHLEdit.toPlainText())
        else:
            dIHL = None


        sSrcMAC = self.MacSrcEdit.toPlainText()
        sDstMAC = self.MacDestEdit.toPlainText()

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
            if (self.PortSrcEdit.toPlainText() != ''):
                dPortSrc = int(self.PortSrcEdit.toPlainText())
            else:
                dPortStc = 21
            
            if (self.PortDestEdit.toPlainText() != ''):
                dPortDst = int(self.PortDestEdit.toPlainText())
            else:
                dPortDst = 80

            if (self.SeqNEdit.toPlainText() != ''):
                dSeqNum = int(self.SeqNEdit.toPlainText())
            else:
                dSeqNum = 0
            
            if (self.AckNEdit.toPlainText() != ''):
                dAckNum = int(self.AckNEdit.toPlainText())  
            else:
                dAckNum = 0

            if (self.WinEdit.toPlainText() != ''):              
                dWinNum = int(self.WinEdit.toPlainText())  
            else:
                dWinNum = 8192
            
            if (self.UrgEdit.toPlainText() != ''):
                dUrgNum = int(self.UrgEdit.toPlainText())  
            else:
                dUrgNum = 0
            
            if (self.OffsEdit.toPlainText() != ''):
                dOff = int(self.OffsEdit.toPlainText())  
            else:
                dOff = 0
            
            if(self.TCPChsumEdit.toPlainText() != ''):
                dTCPChsum = int(self.TCPChsumEdit.toPlainText()) 
            else:
                dTCPChsum = 0

            dTCPFlags = 0x000000000
            if (self.URGCheck.isChecked()):
                dTCPFlags |= 0x000000001          

            if (self.ACKCheck.isChecked()):
                dTCPFlags |= 0x000000010 

            if (self.PSHCheck.isChecked()):
                dTCPFlags |= 0x000000100 

            if (self.RSTCheck.isChecked()):
                dTCPFlags |= 0x000001000 

            if (self.SYNCheck.isChecked()):
                dTCPFlags |= 0x000010000 

            if (self.FINCheck.isChecked()):
                dTCPFlags |= 0x000100000 

            if (self.CWRCheck.isChecked()):
                dTCPFlags |= 0x001000000

            if (self.ECECheck.isChecked()):
                dTCPFlags |= 0x010000000

            packet = IP(src=sIPSrc, dst=sIPDst, version = dIPVer, ihl = dIHL, tos = dTOS, len = dTL, id = dIPID, flags = dIPFlag, frag = dFrag, ttl = dTTL, proto = sProto, chksum = dChkSum)/TCP(sport = dPortSrc, dport = dPortDst, seq = dSeqNum, ack = dAckNum, dataofs = dOff, flags = dTCPFlags, window = dWinNum, chksum = dTCPChsum, urgptr = dUrgNum)/self.FinalDataEdit.toPlainText()

# UDP
        if (dCurIdx == 1):
            if (self.UDPPortSrcEdit.toPlainText() != ''):
                dPortSrc = int(self.UDPPortSrcEdit.toPlainText())
            else:
                dPortSrc = 21

            if (self.UDPPortDestEdit.toPlainText() != ''):
                dPortDst = int(self.UDPPortDestEdit.toPlainText())
            else:
                dPortDst = 80
            
            if (self.UDPChsumEdit.toPlainText() != ''):
                dUDPChsum = int(self.UDPChsumEdit.toPlainText())  
            else:
                dUDPChsum = None
            
            if (self.UDPLenEdit.toPlainText() != ''):
                dUDPLen = int(self.UDPLenEdit.toPlainText())  
            else:
                dUDPLen = None

            packet = IP(src=sIPSrc, dst=sIPDst, version = dIPVer, ihl = dIHL, tos = dTOS, len = dTL, id = dIPID, flags = dIPFlag, frag = dFrag, ttl = dTTL, proto = sProto, chksum = dChkSum) / UDP(sport = dPortSrc, dport = dPortDst, chksum = dUDPChsum, len = dUDPLen)/self.FinalDataEdit.toPlainText()

# ICMP   
        if (dCurIdx == 2):
            if (self.CodeICMPEdit.toPlainText() != ''):
                dICMPCode = int(self.CodeICMPEdit.toPlainText())  
            else:
                dICMPCode = None

            if (self.IDICMPEdit.toPlainText() != ''):
                dICMPID = int(self.IDICMPEdit.toPlainText())  
            else:
                dICMPID = None

            if (self.SeqICMPEdit.toPlainText() != ''):
                dICMPSeq = int(self.SeqICMPEdit.toPlainText())  
            else:
                dICMPSeq = None

            dIdx = self.ICMPMCombo.currentIndex()
            if (dIdx == 0):
                dICMPMsg = 0
            else:
                dICMPMsg = 8
            
            packet = IP(src=sIPSrc, dst=sIPDst, version = dIPVer, ihl = dIHL, tos = dTOS, len = dTL, id = dIPID, flags = dIPFlag, frag = dFrag, ttl = dTTL, proto = sProto, chksum = dChkSum)/ICMP(type = dICMPMsg, code = dICMPCode, id = dICMPID)/self.FinalDataEdit.toPlainText()
            
        
        self.lPacketList.append(packet)
        self.dPacketCnt+=1



    def send_packet(self):
        if self.dPacketCnt == 0:
            self.create_packet()
        
        sAdapter = self.AdapterComboBox.currentText()

        for i in range(self.dPacketCnt):
            if (sAdapter != 'lo'):
                sendp(Ether()/self.lPacketList[i],iface=sAdapter)
            else:
                sendp(Loopback()/self.lPacketList[i],iface=sAdapter)

        self.lPacketList.clear()
        self.dPacketCnt = 0
  

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()