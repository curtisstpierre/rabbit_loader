from pyrabbit.api import Client
import parralel_declare_queues
cl = Client('localhost:15672', 'guest', 'guest')
print(cl.is_alive())

# for i in range(15):
#     vhost_name = f'{i}'
#     cl.create_vhost(vhost_name)
#     parralel_declare_queues.add_queues(vhost_name)

# print(cl.get_vhost_names())
    

for i in range(15):
    vhost_name = f'{i}'
    try:
        cl.delete_vhost(vhost_name)
    except Exception as e:
        print(e)
        

print(cl.get_vhost_names())