# 队列数据存储 队列的使用
import queue
q=queue.Queue()
q.put('apple')
q.put("banana")
q.put("orange")
print(q.qsize())
print(q)