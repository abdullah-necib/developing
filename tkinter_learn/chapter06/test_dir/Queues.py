from queue import Queue
from socket import  socket, AF_INET, SOCK_STREAM

def write_to_scroll(inst):
    print('Hi from QUEUE ',inst)
    sock = socket(AF_INET,SOCK_STREAM)
    sock.connect(('localhost',24000))
    for idx in range(10):
        sock.send(b'Message from Queue: ' +bytes(str(idx).encode()))
        recv = sock.recv(8192).decode()
        inst.qui_queue.put(recv)
    inst.create_thread(6)
