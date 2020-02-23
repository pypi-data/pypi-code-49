from server_ui import Ui_tcpServer
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtCore import pyqtSlot, QThread,pyqtSignal
import socket
import threading
import time

class server_logical(QWidget):
    pyqtSignal_data_get = pyqtSignal(str) #收到数据信号
    def __init__(self, parent = None):
        super().__init__(parent)
        self.server_ui = Ui_tcpServer()
        self.server_ui.setupUi(self)
        self.list_connections=[] # 用来记录socket产生了多少个会话框或者连接

    def showMessage(self,str):
        self.server_ui.plainTextEditDebug.appendPlainText(
            time.strftime("[%Y-%m-%d %H:%M:%S]: ", time.localtime()) + str)

    @pyqtSlot()
    def on_btnStart_clicked(self):

        # 改变btn状态
        if self.server_ui.btnStart.text() == "start server":
            self.server_ui.btnStart.setText("stop server")

            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 基于文件，实现同一主机不同进程之间的通信, TCPIP
            # 获取服务器IP和port
            try:
                ipText = self.server_ui.lineEditIP.text()
                portValue = int(self.server_ui.lineEditPort.text())
                self.socket.bind((ipText, portValue))  # 套接字绑定
            except Exception as e:
                warningStr = "绑定端口错误：" + str(e)
                QMessageBox.warning(self, "错误", warningStr)
            else:  # 开始监听
                self.setWindowTitle("Listening...")
                self.showMessage("Listening...")

                self.socket.listen(20)  # 开始监听 表示可以使用五个链接排队
                # 创建一个进程，用于处理socket连接和接收数据

                self.listenFromClient_th = threading.Thread(target=self.connect_from_client)
                self.listenFromClient_th.setDaemon(True)
                self.listenFromClient_th.start()


        else:
            self.server_ui.btnStart.setText("start server")
            self.setWindowTitle("Listening stopped")
            self.showMessage("Listening stopped")
            for (connection,addr) in self.list_connections:
                connection.close()
            self.list_connections.clear()
            self.socket.close()



    # socket能产生N读会话的线程, 该线程只生成一次
    def connect_from_client(self):
        while True:
            try:
                connection, addr = self.socket.accept() # 阻塞建立来自客户端的连接，一旦连接就创建一个线程专门接受数据
                self.list_connections.append((connection,addr)) # connectiony用来发数据用的，记录list总表
                # 每接受来自一个新客户端的链接，就产生一组connection和addr对象，然后就产生一个新线程
            except Exception as e:
                # QMessageBox.warning(self,"生成会话错误",str(e)) # 一旦socket.close（）被调用，则上述发生异常，此线程完毕
                break # 终止线程
            else:
                self.showMessage("linked from :" + addr[0] + ":" + str(addr[1]))
                # 产生新线程，用来传递数据
                linked_thread = threading.Thread(target= self.client_linked,args=(connection,addr))
                linked_thread.setDaemon(True)
                linked_thread.start()


    # 会话生成以后，等来来自客户端的消息线程
    def client_linked(self, clientConnection, clientAddr):
        bufferSize =1024
        while True:
            if clientConnection is not None: # 如果connection还在链接
                data = clientConnection.recv(bufferSize).decode('utf-8')  # 阻塞，等待客户端发送数据
                if not data:  # 如果客户端已经关闭了连接
                    if (clientConnection,clientAddr) in self.list_connections:
                        self.list_connections.remove((clientConnection,clientAddr)) # 从总的注册链接中去掉当前链接
                        clientConnection.close()  # 关闭了正在占线的连接
                        self.showMessage("linked closed from :" + clientAddr[0] + ":" + str(clientAddr[1]))
                        break
                else: # 打印来自客户端的消息
                    self.showMessage("data from :" + clientAddr[0] + ":" + str(clientAddr[1])+ "\n"+data)
                    self.pyqtSignal_data_get.emit(data)
            else: # connection 不在了，就退出线程
                break





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    # tcpServer = QtWidgets.QWidget()
    ui = server_logical()
    ui.show()
    sys.exit(app.exec_())







