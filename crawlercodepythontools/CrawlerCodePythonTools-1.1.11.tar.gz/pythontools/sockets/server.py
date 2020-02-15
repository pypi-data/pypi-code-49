from pythontools.core import logger, events, tools
import socket, json, base64
from threading import Thread
from pythontools.dev import crypthography

class Server:

    def __init__(self, password):
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.password = password
        self.clientSocks = []
        self.clients = []
        self.seq = base64.b64encode(self.password.encode('ascii')).decode("utf-8")
        self.packagePrintBlacklist = []
        self.packagePrintBlacklist.append("ALIVE")
        self.packagePrintBlacklist.append("ALIVE_OK")
        self.maxClients = 10
        self.printUnsignedData = True
        self.eventScope = "global"
        self.encrypt = False
        self.server_private_key = None
        self.client_public_key = None

    def start(self, host, port):
        if self.encrypt is True:
            if not tools.existFile("server_private_key.pem"):
                crypthography.generateKey(private_key="server_private_key.pem", public_key="server_public_key.pem")
                logger.log("§8[§eSERVER§8] §aNew key created")
            self.server_private_key = crypthography.getPrivateKey(private_key="server_private_key.pem")
            if tools.existFile("client_public_key.pem"):
                self.client_public_key = crypthography.getPublicKey(public_key="client_public_key.pem")
            else:
                logger.log("§8[§eSERVER§8] §8[§cERROR§8] §cFailed to load 'client_public_key.pem'")
                self.error = 1
                return
        #host = socket.gethostbyname(socket.gethostname())
        logger.log("§8[§eSERVER§8] §6Starting...")
        try:
            self.serverSocket.bind((host, port))
            self.serverSocket.listen(self.maxClients)
            logger.log("§8[§eSERVER§8] §aListening on §6" + str((host, port)))
        except Exception as e:
            logger.log("§8[§eSERVER§8] §8[§cERROR§8] §cFailed: " + str(e))
            self.error = 1
        def clientTask(clientSocket, address):
            logger.log("§8[§eSERVER§8] §aClient connected from §6" + str(address))
            lastData = ""
            while True:
                try:
                    recvData = clientSocket.recv(32768)
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
                                    recvData += crypthography.decrypt(self.server_private_key, base64.b64decode(recvDataList[i].replace("}" + self.seq, "")[1:].encode('ascii')))
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
                                recvData = "[" + crypthography.decrypt(self.server_private_key, base64.b64decode(recvData.replace("}" + self.seq, "")[1:].encode('ascii'))) + "]"
                            else:
                                recvData = "[" + recvData.replace(self.seq, "") + "]"
                            lastData = ""
                        recvData = json.loads(recvData)
                        for data in recvData:
                            if data["METHOD"] == "ALIVE":
                                self.sendTo(clientSocket, {"METHOD": "ALIVE_OK"})
                            elif data["METHOD"] == "AUTHENTICATION":
                                logger.log("§8[§eSERVER§8] §r[IN] " + data["METHOD"])
                                if data["PASSWORD"] == self.password:
                                    for c in self.clients:
                                        if c["clientID"] == data["CLIENT_ID"]:
                                            self.sendTo(clientSocket, {"METHOD": "AUTHENTICATION_FAILED"})
                                            break
                                    client = {"clientSocket": clientSocket, "clientID": data["CLIENT_ID"], "clientType": data["CLIENT_TYPE"]}
                                    self.clients.append(client)
                                    self.sendTo(clientSocket, {"METHOD": "AUTHENTICATION_OK"})
                                    logger.log("§8[§eSERVER§8] §aClient '" + data["CLIENT_ID"] + "' authenticated")
                                    events.call("ON_CLIENT_CONNECT", params=[client], scope=self.eventScope)
                                else:
                                    self.sendTo(clientSocket, {"METHOD": "AUTHENTICATION_FAILED"})
                                    break
                            else:
                                client = self.getClient(clientSocket)
                                if client is not None:
                                    if data["METHOD"] not in self.packagePrintBlacklist:
                                        logger.log("§8[§eSERVER§8] §r[IN] " + data["METHOD"])
                                    events.call("ON_RECEIVE", params=[client, data], scope=self.eventScope)
                                else:
                                    logger.log("§8[§eSERVER§8] §8[§cWARNING§8] §cReceiving not authenticated package: §r" + data["METHOD"])
                except Exception as e:
                    logger.log("§8[§eSERVER§8] §8[§cWARNING§8] §cException: §4" + str(e))
                    break
            self.clientSocks.remove(clientSocket)
            for client in self.clients:
                if client["clientSocket"] == clientSocket:
                    events.call("ON_CLIENT_DISCONNECT", params=[client], scope=self.eventScope)
                    logger.log("§8[§eSERVER§8] §6Client '" + client["clientID"] + "' disconnected")
                    self.clients.remove(client)
            clientSocket.close()
            logger.log("§8[§eSERVER§8] §6Client disconnected")
        while True:
            (client, clientAddress) = self.serverSocket.accept()
            self.clientSocks.append(client)
            Thread(target=clientTask, args=[client, clientAddress]).start()

    def addPackageToPrintBlacklist(self, package):
        self.packagePrintBlacklist.append(package)

    def getClient(self, clientSocket):
        for client in self.clients:
            if client["clientSocket"] == clientSocket:
                return client
        return None

    def sendToAll(self, message):
        for sSock in self.clientSocks:
            self.sendTo(sSock, message)

    def sendTo(self, sock, data):
        try:
            send_data = json.dumps(data)
            if self.encrypt is True:
                send_data = "{" + base64.b64encode(crypthography.encrypt(self.client_public_key, send_data)).decode('utf-8') + "}"
            sock.send(bytes(send_data + self.seq, "utf-8"))
            if data["METHOD"] not in self.packagePrintBlacklist:
                logger.log("§8[§eSERVER§8] §r[OUT] " + data["METHOD"])
        except Exception as e:
            logger.log("§8[§eSERVER§8] §8[§cWARNING§8] §cFailed to send data: " + str(e))
            if e == BrokenPipeError:
                sock.close()

    def sendToClientID(self, clientID, data):
        for client in self.clients:
            if client["clientID"] == clientID:
                self.sendTo(clientID["clientSocket"], data)

    def close(self):
        self.serverSocket.close()
        logger.log("§8[§eSERVER§8] §6Closed")

