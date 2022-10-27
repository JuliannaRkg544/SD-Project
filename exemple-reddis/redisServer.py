import redis

port = 4000

serv = redis.Redis(host='localhost', port=port)
pool = redis.ConnectionPool(host='localhost', port=port, db=0)
client = redis.Redis(connection_pool=pool)

print('running on port ', port)
#  def getMsg(self, remetente):
#         msg = client.get(input()) 
#         if msg == "exit":
#           finished = True
#         else:
#            print(f'/n voce possui a seguinte menssgem: {msg}/n')
#         client.set(input('Message: ')) 


finished = False
while not finished:
        msg = client.get("mg2") 
        if msg == "exit":
            finished = True
        else:
            print('/n voce possui a seguinte menssgem: {msg}')
        client.set("mg", input('Message: ') ) 

client.close()
serv.close()
