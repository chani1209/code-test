# 자료구조  
### 배열 Array
- 삽입/삭제 : O(N)
- 탐색 : O(1)
- Python은 list 사용.

### 연결 리스트 Linked List
- 삽입/삭제 : O(1)
- 탐색 : O(N)

### 스택 Stack (LIFO)
- 삽입/삭제 : O(1)
- Python은 list 사용. (append, pop)

### 큐 Queue (FIFO)
- 삽입/삭제 : O(1)
- Python은 collections.deque 사용. (append, popleft)
```python
from collections import deque

q = deque()
q.append(1)
q.append(2)
q.append(3)
print("size:", len(q)) # 3
while q:
    print(q.popleft()) # 1 2 3
```

### 힙 Heap(prirority queue)
- python은 min-heap -> heapq 모듈 or queue.PriorityQueue 사용
- 삽입/삭제 : O(logN)
- 삭제시 -> 루트 노드 삭제(최솟값)
- heapq가 더 빠르지만, thread-safe하지 않다. -> 코테에서는 heqpq를 사용하자.
```python
from queue import PriorityQueue
pq = PriorityQueue()
pq.put(1)
pq.put(2)
while not pq.empty():
    print(pq.get()) # 1 2

import heapq
q = []
heapq.heappush(q, 1)
heapq.heappush(q, 2)
while q:
    print(heapq.heappop(q)) # 1 2 
```

### 딕셔너리(map) Dictionary
- 삽입/삭제/탐색 : O(1)
- Python은 dict 사용.

### 집합 Set
- 삽입/삭제/탐색 : O(1)
- pop() : 임의의 원소 삭제 -> 쓸일이 없지 않을까...?
- remove(x) : x 삭제 -> 없으면 에러