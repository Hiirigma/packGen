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
    bICMPChkSum = False


    lPacketList = []

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
        self.ChsumCheckICMP.clicked.connect(self.upddChkSumICMP)
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
            self.bUDPChsum = False


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

    def upddChkSumICMP(self):
        if self.bICMPChkSum == False:
            dChkSum = random.randint(0,65535)
            self.ChsumEditICMP.setText(str(dChkSum))
            self.bICMPChkSum = True
        else:
            self.ChsumEditICMP.clear()
            self.bICMPChkSum = True
            
            
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

        ipPacket = IP()
        sTarget = ""
        dCurIdx = self.PacketTabWidget.currentIndex()
        self.log_write("Log: Target: " + sTarget)

        ipPacket.src = self.IPSrcEdit.toPlainText()
        ipPacket.dst = self.IPDstEdit.toPlainText()
        if (self.VersionEdit.toPlainText() != ''):
            ipPacket.version = int(self.VersionEdit.toPlainText())

        if (self.IHLEdit.toPlainText() != ''):
            ipPacket.ihl = int(self.IHLEdit.toPlainText())

        if (self.IDEdit.toPlainText() != ''):    
            ipPacket.id = int(self.IDEdit.toPlainText())

        if (self.TTLEdit.toPlainText() != ''):
            ipPacket.ttl = int(self.TTLEdit.toPlainText())
        
        if (self.ChsumEdit.toPlainText() != ''):
            ipPacket.chksum = int(self.ChsumEdit.toPlainText())

        if (self.ProtocolEdit.toPlainText() != ''):
            ipPacket.proto = self.ProtocolEdit.toPlainText()

        if (self.TypeEdit.toPlainText() != ''):
            ipPacket.type = int(self.TypeEdit.toPlainText())
        
        if (self.FragEdit.toPlainText() != ''):
            ipPacket.frag = int(self.FragEdit.toPlainText())

        dFlag = 0
        if (self.ResRadioBtn.isChecked()):
            dFlag |= 0x00
            ipPacket.flags = dFlag
        if (self.DFRadioBtn.isChecked()):
            dFlag |= 0x01
            ipPacket.flags = dFlag
        if (self.MFRadioBtn.isChecked()):
            dFlag |= 0x02
            ipPacket.flags = dFlag


        dTOS = 0
        
        if (self.PrecCheckBox0.isChecked()):
            dTOS |= 0x01
            ipPacket.tos = dTos
        if (self.PrecCheckBox1.isChecked()):
            dTOS |= 0x02
            ipPacket.tos = dTos
        if (self.PrecCheckBox2.isChecked()):
            dTOS |= 0x04
            ipPacket.tos = dTos
        if (self.DelayCheck.isChecked()):
            dTOS |= 0x08
            ipPacket.tos = dTos
        if (self.ThrCheck.isChecked()):
            dTOS |= 0x10
            ipPacket.tos = dTos
        if (self.RelCheck.isChecked()):
            dTOS |= 0x20
            ipPacket.tos = dTos
        if (self.CostCheck.isChecked()):
            dTOS |= 0x40
            ipPacket.tos = dTos

        if (self.TLEdit.toPlainText() != ''):
            ipPacket.len = int(self.TLEdit.toPlainText())
        
        if (self.IHLEdit.toPlainText() != ''):
            ipPacket.ihl = int(self.IHLEdit.toPlainText())

        sSrcMAC = self.MacSrcEdit.toPlainText()
        sDstMAC = self.MacDestEdit.toPlainText()

        if (sSrcMAC != ""):
            ipPacket.src = sSrcMAC
        
        if (sDstMAC != ""):
            ipPacket.dst = sDstMAC
        
        tcp_packet = TCP()
# TCP
        if (dCurIdx == 0):
            if (self.PortSrcEdit.toPlainText() != ''):
                tcp_packet.sport = int(self.PortSrcEdit.toPlainText())
            
            if (self.PortDestEdit.toPlainText() != ''):
                tcp_packet.dport = int(self.PortDestEdit.toPlainText())

            if (self.SeqNEdit.toPlainText() != ''):
                tcp_packet.seq = int(self.SeqNEdit.toPlainText())
            
            if (self.AckNEdit.toPlainText() != ''):
                tcp_packet.ack = int(self.AckNEdit.toPlainText())  

            if (self.WinEdit.toPlainText() != ''):              
                tcp_packet.window = int(self.WinEdit.toPlainText())  
            
            if (self.UrgEdit.toPlainText() != ''):
                tcp_packet.urgptr = int(self.UrgEdit.toPlainText())  
            
            if (self.OffsEdit.toPlainText() != ''):
                tcp_packet.dataofs = int(self.OffsEdit.toPlainText())  
            
            if(self.TCPChsumEdit.toPlainText() != ''):
                tcp_packet.chksum = int(self.TCPChsumEdit.toPlainText()) 

            dTCPFlags = 0x00

            if (self.FINCheck.isChecked()):
                dTCPFlags |= 0x01 

            if (self.SYNCheck.isChecked()):
                dTCPFlags |= 0x02    

            if (self.RSTCheck.isChecked()):
                dTCPFlags |= 0x04

            if (self.PSHCheck.isChecked()):
                dTCPFlags |= 0x08

            if (self.ACKCheck.isChecked()):
                dTCPFlags |= 0x10

            if (self.URGCheck.isChecked()):
                dTCPFlags |= 0x20    

            if (self.ECECheck.isChecked()):
                dTCPFlags |= 0x40

            if (self.CWRCheck.isChecked()):
                dTCPFlags |= 0x80

            tcp_packet.flags = dTCPFlags

            packet = ipPacket/tcp_packet/self.FinalDataEdit.toPlainText()

# UDP
        udp_packet = UDP()
        if (dCurIdx == 1):
            if (self.UDPPortSrcEdit.toPlainText() != ''):
                udp_packet.sport = int(self.UDPPortSrcEdit.toPlainText())

            if (self.UDPPortDestEdit.toPlainText() != ''):
                udp_packet.dport = int(self.UDPPortDestEdit.toPlainText())
            
            if (self.UDPChsumEdit.toPlainText() != ''):
                udp_packet.chksum = int(self.UDPChsumEdit.toPlainText())  
            
            if (self.UDPLenEdit.toPlainText() != ''):
                udp_packet.len = int(self.UDPLenEdit.toPlainText())  

            packet = ipPacket/udp_packet/self.FinalDataEdit.toPlainText()

# ICMP   
        icmp_packet = ICMP()
        if (dCurIdx == 2):
            if (self.CodeICMPEdit.toPlainText() != ''):
                icmp_packet.code = int(self.CodeICMPEdit.toPlainText())  

            if (self.IDICMPEdit.toPlainText() != ''):
                icmp_packet.id = int(self.IDICMPEdit.toPlainText())  

            if (self.SeqICMPEdit.toPlainText() != ''):
                icmp_packet.seq = int(self.SeqICMPEdit.toPlainText())  
                
            if (self.ChsumEditICMP.toPlainText() != ''):
                icmp_packet.chksum = int(self.ChsumEditICMP.toPlainText())                

            dIdx = self.ICMPMCombo.currentIndex()
            if (dIdx == 0):
                icmp_packet.type = 8
            else:
                icmp_packet.type = 0
            
            packet = ipPacket/icmp_packet/self.FinalDataEdit.toPlainText()
            
        
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
