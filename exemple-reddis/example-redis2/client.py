#!/usr/bin/env python

import argparse
import logging
import traceback
import sys

import redis

# Allow this script to run without installing redisrpc.
sys.path.append('..')
import redisrpc

import chat


# Direct all RedisPRC logging messages to stderr.
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

parser = argparse.ArgumentParser(description='Example calculator server')
parser.add_argument('--transport', choices=('json', 'pickle'), default='json',
    help='data encoding used for transport')
args = parser.parse_args()
 
def do_chat(chatService):
    chatService.sendMessage('juju','says hello ')
    msg = chatService.getMessage()
    print(msg)



# 1. Local object
chatService = chat.Chat()
do_chat(chatService)

# 2. Remote object, should act like local object
redis_server = redis.Redis()
message_queue = 'chat'
chatService = redisrpc.Client(redis_server, message_queue, timeout=1, transport=args.transport)
do_chat(chatService)
print('success!')