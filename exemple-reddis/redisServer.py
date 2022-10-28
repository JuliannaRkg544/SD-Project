import redis

port = 6379
serv = redis.Redis(host='localhost', port=port, charset ="utf-8", decode_responses=True)
pool = redis.ConnectionPool(host='localhost', port=port, db=0)
client = redis.Redis(connection_pool=pool)

print('running on port ', port)


finished = False
while not finished:
  msg = client.get("mg2").key.decode()
  if msg == "exit":
    finished = True
  else:
    print('\nvoce possui a seguinte menssgem: ', {msg})
  client.set("mg", input('\n Digite sua Mensagem: ')).key.encode()

client.close()
serv.close()
