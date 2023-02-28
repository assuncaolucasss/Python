import Pyro4

class Server(object):
    @Pyro4.expose
    def welcomeMessage(self, name):
        return ("Olá, bem vindo" + str(name) )

def startServer():
    server = Server()
    daemon = Pyro4.Daemon()
    ns = Pyro4.locateNS()
    uri = daemon.register(server)
    ns.register("server", uri)
    print("Ready. object uri = ", uri)
    daemon.requestLoop()

if __name__ == "__main__":
    startServer()
