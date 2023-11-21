from collections import deque

# empty deque object that functions as a queue
queue = deque()

# add elements to the queue
queue.append(2)
queue.append(4)
queue.append(6)
queue.append(7)

# print the queue items
print(queue)

# pop an item off the front of the queue
x = queue.popleft()
print(x)
print(queue)