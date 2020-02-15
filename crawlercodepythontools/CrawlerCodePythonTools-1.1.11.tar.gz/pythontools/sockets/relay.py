from pythontools.core import events
from pythontools.sockets import server, client
from threading import Thread

class Relay:

    def __init__(self, password):
        self.password = password
        self.relayServer = server.Server(password=self.password)
        self.clients = []
        self.relayServerEncrypt = False
        self.serverClientEncrypt = False

    def start(self, relayHost, relayPort, serverHost, serverPort):
        def ON_CLIENT_CONNECT(params):
            relayClient = params[0]
            serverClient = client.Client(password=self.password, clientID=relayClient["clientID"], clientType=relayClient["clientType"])
            serverClient.eventScope = relayClient["clientID"]

            def ON_RECEIVE(params):
                data = params[0]
                self.relayServer.sendTo(relayClient["clientSocket"], data)

            events.registerEvent("ON_RECEIVE", ON_RECEIVE, scope=serverClient.eventScope)

            serverClient.encrypt = self.serverClientEncrypt
            Thread(target=serverClient.connect, args=[serverHost, serverPort]).start()
            self.clients.append({"relayClient": relayClient, "serverClient": serverClient})

        def ON_CLIENT_DISCONNECT(params):
            client = params[0]
            for c in self.clients:
                if c["relayClient"] == client:
                    c["serverClient"].disconnect()
                    self.clients.remove(c)

        def ON_RECEIVE(params):
            client = params[0]
            data = params[1]
            for c in self.clients:
                if c["relayClient"] == client:
                    c["serverClient"].send(data)

        events.registerEvent("ON_CLIENT_CONNECT", ON_CLIENT_CONNECT)
        events.registerEvent("ON_CLIENT_DISCONNECT", ON_CLIENT_DISCONNECT)
        events.registerEvent("ON_RECEIVE", ON_RECEIVE)
        self.relayServer.encrypt = self.relayServerEncrypt
        Thread(target=self.relayServer.start, args=[relayHost, relayPort]).start()