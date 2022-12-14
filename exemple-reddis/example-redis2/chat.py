class Chat:
    """A simple, mutable calculator used for testing."""

    # def __init__(self):
    #     self.acc = 0.0

    # def __str__(self):
    #     return '%s' % self.acc

    chat = ''
    
    def sendMessage(self, nickname, msg):
       global chat
       chat = nickname + ': ' + msg
       return chat


    def getMessage(self):
        global chat
        return chat


    def checkMessage(self):
        if chat!='':
            self.getMessage()
        

    # def receiveMessage(self,number):
    #     self.acc *= number
    #     return self.acc

    # def pendingMessage(self,number):
    #     self.acc -= number
    #     return self.acc
