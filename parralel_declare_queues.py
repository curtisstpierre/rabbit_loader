import sys
sys.path.append("..")

import logging
FORMAT_CONS = '%(asctime)s %(name)-12s %(levelname)8s\t%(message)s'
logging.basicConfig(level=logging.DEBUG, format=FORMAT_CONS)



import puka
import send

def add_queues(vhost, number_of_queues=10):
    client = puka.Client(f"amqp://localhost/{vhost}")

    promise = client.connect()
    client.wait(promise)

    promises = [client.queue_declare(queue='a%04i' % i) for i in range(number_of_queues)]
    for promise in promises:
        client.wait(promise)

    [send.load_messages(vhost, queue='a%04i' % i) for i in range(number_of_queues)]

    # promises = [client.queue_delete(queue='a%04i' % i) for i in range(number_of_queues)]
    # for promise in promises:
    #     client.wait(promise)

    promise = client.close()
    client.wait(promise)