#!/usr/bin/env python

import sys
sys.path.append("..")

import puka
from pyrabbit.api import Client
import click

@click.command()
@click.option('--vhost', help='vhost to consume')
def consume(vhost):
    cl = Client('localhost:15672', 'guest', 'guest')

    # for vhost in cl.get_vhost_names():
    #     queues = cl.get_queues(vhost)
    queues = cl.get_queues(vhost)
    client = puka.Client(f"amqp://localhost/{vhost}")
    promise = client.connect()
    client.wait(promise)

    print("  [*] Waiting for messages. Press CTRL+C to quit.")
    queues = [queue['name'] for queue in queues]
    print(queues)
    consume_promise = client.basic_consume_multi(queues=queues, prefetch_count=1)
    while True:
        result = client.wait(consume_promise)
        print(" [x] Received message %r" % (result,))
        client.basic_ack(result)

    promise = client.close()
    client.wait(promise)

if __name__ == '__main__':
    consume()