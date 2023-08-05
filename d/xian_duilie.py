from queue import Queue
from threading import Thread
def worker(q):
    while True:
        item=q.get()
        if item is None:
            break
        print(item)
q= Queue()
t= Thread(target=worker,args=(q,))
t.start()
for item in range(10):
    q.put(item)
q.put(None) 
t.join()