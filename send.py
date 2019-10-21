import sys
sys.path.append("..")


import puka


def load_messages(vhost, queue):
    client = puka.Client(f"amqp://localhost/{vhost}")

    promise = client.connect()
    client.wait(promise)

    promise = client.queue_declare(queue=queue)
    client.wait(promise)

    for i in range(1000):
        promise = client.basic_publish(exchange='', routing_key=queue,
                                    body=f"Hello world! {i}")
        client.wait(promise)

    print(" [*] Message sent")

    promise = client.queue_declare(queue=queue, passive=True)
    print(" [*] Queue size:", client.wait(promise)['message_count'])

    promise = client.close()
    client.wait(promise)