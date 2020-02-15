from pythontools.core import logger, events, tools
import socket, json, time, base64
from threading import Thread
from pythontools.dev import crypthography

class Client:

    def __init__(self, password, clientID, clientType, reconnect=True):
        self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.password = password
        self.clientID = clientID
        self.clientType = clientType
        self.error = 0
        self.seq = base64.b64encode(self.password.encode('ascii')).decode("utf-8")
        self.connected = False
        self.lostPackages = []
        self.packagePrintBlacklist = []
        self.packagePrintBlacklist.append("ALIVE")
        self.packagePrintBlacklist.append("ALIVE_OK")
        self.reconnect = reconnect
        self.waitReceived = None
        self.aliveInterval = 10
        self.printUnsignedData = True
        self.eventScope = "global"
        self.encrypt = False
        self.client_private_key = None
        self.server_public_key = None

    def connect(self, host, port):
        if self.encrypt is True:
            if not tools.existFile("client_private_key.pem"):
                crypthography.generateKey(private_key="client_private_key.pem", public_key="client_public_key.pem")
                logger.log("§8[§eCLIENT§8] §aNew key created")
            self.client_private_key = crypthography.getPrivateKey(private_key="client_private_key.pem")
            if tools.existFile("server_public_key.pem"):
                self.server_public_key = crypthography.getPublicKey(public_key="server_public_key.pem")
            else:
                logger.log("§8[§eSERVER§8] §8[§cERROR§8] §cFailed to load 'server_public_key.pem'")
                self.error = 1
                return
        def _connect(first):
            logger.log("§8[§eCLIENT§8] §6Connecting...")
            try:
                self.clientSocket.connect((socket.gethostbyname(host), port))
                logger.log("§8[§eCLIENT§8] §aConnected to §6" + str((socket.gethostbyname(host), port)))
                self.connected = True
                self.error = 0
            except Exception as e:
                logger.log("§8[§eCLIENT§8] §8[§cERROR§8] §cConnection failed: " + str(e))
                self.error = 1
            def clientTask():
                if self.error == 0:
                    self.send({"METHOD": "AUTHENTICATION", "CLIENT_ID": self.clientID, "CLIENT_TYPE": self.clientType, "PASSWORD": self.password})
                lastData = ""
                while self.error == 0:
                    try:
                        recvData = self.clientSocket.recv(32768)
                        recvData = str(recvData, "utf-8")
                        if recvData != "":
                            if not recvData.startswith("{"):
                                if recvData.endswith("}" + self.seq):
                                    if lastData != "":
                                        recvData = lastData + recvData
                                        if self.printUnsignedData:
                                            logger.log("§8[§eSERVER§8] §8[§cWARNING§8] §cUnsigned data repaired")
                            if not recvData.endswith("}" + self.seq):
                                lastData += recvData
                                if self.printUnsignedData:
                                    logger.log("§8[§eSERVER§8] §8[§cWARNING§8] §cReceiving unsigned data: §r" + recvData)
                                continue
                            if "}" + self.seq + "{" in recvData:
                                recvDataList = recvData.split("}" + self.seq + "{")
                                recvData = "["
                                for i in range(len(recvDataList)):
                                    if self.encrypt is True:
                                        recvData += crypthography.decrypt(self.client_private_key, base64.b64decode(recvDataList[i].replace("}" + self.seq, "")[1:].encode('ascii')))
                                        if i + 1 < len(recvDataList):
                                            recvData += ", "
                                    else:
                                        recvData += recvDataList[i].replace(self.seq, "")
                                        if i + 1 < len(recvDataList):
                                            recvData += "}, {"
                                recvData += "]"
                                lastData = ""
                            elif "}" + self.seq in recvData:
                                if self.encrypt is True:
                                    recvData = "[" + crypthography.decrypt(self.client_private_key, base64.b64decode(recvData.replace("}" + self.seq, "")[1:].encode('ascii'))) + "]"
                                else:
                                    recvData = "[" + recvData.replace(self.seq, "") + "]"
                                lastData = ""
                            recvData = json.loads(recvData)
                            for data in recvData:
                                if data["METHOD"] not in self.packagePrintBlacklist:
                                    logger.log("§8[§eCLIENT§8] §r[IN] " + data["METHOD"])
                                if data["METHOD"] == "AUTHENTICATION_FAILED":
                                    self.error = 1
                                elif data["METHOD"] == "AUTHENTICATION_OK":
                                    events.call("ON_CONNECT", params=[], scope=self.eventScope)
                                    for package in self.lostPackages:
                                        self.send(package)
                                    self.lostPackages.clear()
                                else:
                                    events.call("ON_RECEIVE", params=[data], scope=self.eventScope)
                    except Exception as e:
                        self.error = 1
                        logger.log("§8[§eCLIENT§8] §8[§cWARNING§8] §cException: §4" + str(e))
                        break
                self.clientSocket.close()
                self.connected = False
                logger.log("§8[§eCLIENT§8] §6Disconnected")
                if self.reconnect is True:
                    logger.log("§8[§eCLIENT§8] §6Reconnect in 10 seconds")
                    time.sleep(10)
                    self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    _connect(False)
            self.startAlive()
            if first is True:
                Thread(target=clientTask).start()
            else:
                clientTask()
        _connect(True)

    def startAlive(self):
        def alive():
            time.sleep(self.aliveInterval)
            while self.error == 0:
                try:
                    self.send({"METHOD": "ALIVE"})
                except:
                    self.error = 1
                    break
                time.sleep(self.aliveInterval)
        Thread(target=alive).start()

    def addPackageToPrintBlacklist(self, package):
        self.packagePrintBlacklist.append(package)

    def send(self, data, savePackage=True):
        try:
            send_data = json.dumps(data)
            if self.encrypt is True:
                send_data = "{" + base64.b64encode(crypthography.encrypt(self.server_public_key, send_data)).decode('utf-8') + "}"
            self.clientSocket.send(bytes(send_data + self.seq, "utf-8"))
            if data["METHOD"] not in self.packagePrintBlacklist:
                logger.log("§8[§eCLIENT§8] §r[OUT] " + data["METHOD"])
        except:
            if not self.connected and savePackage is True:
                self.lostPackages.append(data)

    def sendPackageAndWaitForPackage(self, package, method, maxTime=1.5):
        self.waitReceived = None
        def ON_RECEIVE(params):
            if params[0]["METHOD"] == method:
                self.waitReceived = params[0]
        events.registerEvent("ON_RECEIVE", ON_RECEIVE, scope=self.eventScope)
        self.send(package)
        startTime = time.time()
        while self.waitReceived is None and (time.time() - startTime) <= maxTime:
            pass
        events.unregisterEvent(ON_RECEIVE)
        return self.waitReceived

    def disconnect(self):
        self.reconnect = False
        self.clientSocket.close()
        self.connected = False
        logger.log("§8[§eCLIENT§8] §6Disconnected")