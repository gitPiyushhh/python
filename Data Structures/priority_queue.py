##############################################
###### Creation {Using sorting}

q = []

## Adding elements 

q.append(3)
q.append(1)
q.append(2)

## Creting priority queue{Lower the value higher the priority}

q.sort()

## Getting elems 

print(q.pop(0))
print(q.pop(0))
print(q.pop(0))


##############################################
###### Creation {Using binary heap}

import queue 

q2 = queue.PriorityQueue ()

q2.put(10)
q2.put(10)
q2.put(30)
q2.put(20)

print(q2.get())
print(q2.get())
print(q2.get())
print(q2.get())