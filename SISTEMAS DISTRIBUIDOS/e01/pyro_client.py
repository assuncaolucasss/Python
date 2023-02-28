import Pyro4

name = input ("Qual seu nome? ").strip()
server = Pyro4.Proxy("PYRONAME:server")
print(server.welcomeMessage(name))
