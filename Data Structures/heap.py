############################################
###### Implementation Using Heapq

############# MIN HEAP⬇️⬇️ ###############
import heapq as hq

h = []

## 1. Push
hq.heappush(h, 1)  # Root
hq.heappush(h, 10) # Left
hq.heappush(h, 5)  # Right

## 2. Pop
hq.heappop(h)
print(h)