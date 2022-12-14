import argparse
import logging
import sys
import redis
sys.path.append('..')
import redisrpc
import chat

# import chat fazer analago ao exemplo da calculadora


# Direct all RedisPRC logging messages to stderr.
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

redis_server = redis.Redis()
message_queue = 'chat'
local_object = chat.Chat()
server = redisrpc.Server(redis_server, message_queue, local_object)
server.run()