from queue import Queue
from threading import Thread
def worker(q):
    while True:
        task = q.get()
        if task is None:
            break
        do_work(task)
        q.task_done()

def do_work(task):
    print(f'Processing {task}')
    
q = Queue()
num_worker_threads = 5
threads = []
for i in range(num_worker_threads):
    t = Thread(target=worker, args=(q,))
    t.start()
    threads.append(t)

for item in threads:
    q.put(item)

# block until all tasks are done
q.join()

# stop workers
for i in range(num_worker_threads):
    q.put(None)
for t in threads:
    t.join()


Woaini33279@!@12@!

ffmpeg -ss 00:00:00 -t 24:28 -i 2023-08-03\ 21-44-20.mp4 -c:v copy -c:a copy output.mp4