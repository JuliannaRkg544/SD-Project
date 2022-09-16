class Usuario:
    def _init_(self, nome):
        self.nome = nome

    def sendMsg(self, client, msg):
        client.receiveMsg(self.nome, msg)

    def checkMsg(self, remetente, msg):
        remetente.getMsg(self, msg) #pegar mensagem do remetente (quem enviou)


if _name_ == '_main_':
    client_larissa = Usuario('larissa')
    client_juliana = Usuario('juliana')
    serverPorta = client_juliana #apenas uma ideia de conexao com servidor
    serverPorta = client_larissa
    client_juliana.sendMsg(client_larissa, "Olá! Tudo bem?")
    client_larissa.checkMsg()

