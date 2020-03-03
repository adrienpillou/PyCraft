from mcstatus import MinecraftServer #https://github.com/Dinnerbone/mcstatus
#Useful examples : https://python.hotexamples.com/examples/mcstatus/MinecraftServer/-/python-minecraftserver-class-examples.html#0xa8ff2058f18a4d85d219258bc137c1d632e4d4b931ba7deab80676d10d0bfaa5-6,,30,

class Server:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.address = ip + ":" + port
        self.instance = MinecraftServer.lookup(self.address)
        self.isOnline = False

    def GetAddress(self):
        return self.ip + ":" + self.port

    def GetSlotsInfos(self):
        return str(self.instance.status().players.online) + "/" + str(self.instance.status().players.max)
    
    def GetLatency(self):
        return int(self.instance.ping())
    
    def GetPlayerList(self):
        players = self.instance.query().players.names
        return players

    def TestIfServerIsAvailable(self):
        online = False
        try :
            p = self.instance.ping()
            
        except :
            online = False
            self.isOnline = False
            online = False
        
        else :
            online = True
            self.isOnline = True
            return online