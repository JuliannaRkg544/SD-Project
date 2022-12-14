import redis

port = 6379

serv = redis.Redis(host='localhost', port=port)
pool = redis.ConnectionPool(host='localhost', port=port, db=0)
client = redis.Redis(connection_pool=pool)

print('running on port ', port)


finished = False
while not finished:
        msg = client.get("mg2") 
        if msg == "exit":
            finished = True
        else:
            print('/n voce possui a seguinte menssgem: ', {msg})
        client.set("mg", input('Message: ') ) 

client.close()
serv.close()
