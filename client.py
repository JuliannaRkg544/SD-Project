class Usuario:

    def __init__(self, nome):

        self.nome = nome 

    def enviarMsg(self, instancia, msg):

        instancia.receberMsg(self.nome, msg)

    def receberMsg(self, remetente, msg):

            print( remetente + ": " + msg )

if __name__ == '__main__':

    instancia_juliana = Usuario("Juliana")

    instancia_nicole = Usuario("Nicole")

    instancia_juliana.enviarMsg(instancia_nicole, "Olá, tudo bem?")

    instancia_nicole.enviarMsg(instancia_juliana, "Estou bem e você?")

