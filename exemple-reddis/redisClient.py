import redis

pool = redis.ConnectionPool(host='localhost', port=6379, db=0, charset ="utf-8", decode_responses=True)
client = redis.Redis(connection_pool=pool)

finished = False
print('type exit to close the chat')

while not finished:
  client.set("mg2", input('\nDigite sua Mensagem: ')).key.encode()
  msg = client.get("mg").key.decode()
  if msg == (b'exit'):
    finished = True
  else:
    print("Recebido: ", msg)
    

client.close()
