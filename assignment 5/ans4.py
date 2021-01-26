from collections import deque
q = deque()
q.append('1')
q.append('2')
q.append('3')

print("Initial queue")
print(q)

print("\nElements dequeued from the queue")
print(q.popleft())
print(q.popleft())
print(q.popleft())

print("\nQueue after removing elements")
print(q)