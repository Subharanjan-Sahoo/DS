import queue
q = queue.Queue()


q.put(10)
q.put(50)
q.put(60)
print(q)
q.get()
q.get()
q.get()
print(q)