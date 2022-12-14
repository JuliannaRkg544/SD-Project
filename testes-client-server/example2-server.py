class Servidor:
    def _init_(self, serverPorta,serverHost, clients):

        self.serverPorta = 7777 #vai receber um servidor, mas ainda nao esta implementado 
        self.serverHost = 'localhost'
        clients = []

        while True:
              client, address = serverPorta()
              clients.append(client) #adicionar o cliente na lista

    def getMsg(self, remetente): 
        while True:
            try: 
                msg = remetente.msg #armazena em msg a mensgem enviada pelo remetente
                print(f'/n voce possui a seguinte menssgem: {remetente} : {msg}/n')
            except:
                return print(f'/n voce não possui nenhuma menssgem :( /n')

    def receiveMsg(self, remetente, msg):
        print(f'Remetente>{remetente} : {msg}')