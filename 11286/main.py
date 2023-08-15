import heapq
import sys

heap = []
for _ in range(int(input())):
    x = int(sys.stdin.readline())
    if x:
        heapq.heappush(heap, (abs(x), x))
    else:
        print(heapq.heappop(heap)[1] if heap else 0)



# 첫번째 시도 : 시간초과
# plus_heap = []
# minus_heap = []
#
# for _ in range(int(input())):
#     num = int(input())
#
#     if num > 0:
#         heapq.heappush(plus_heap, num)
#     elif num < 0:
#         heapq.heappush(minus_heap, -num)
#     else:
#         if len(plus_heap) == 0 and len(minus_heap) == 0:
#             print(0)
#         elif len(plus_heap) == 0:
#             print(-heapq.heappop(minus_heap))
#         elif len(minus_heap) == 0:
#             print(heapq.heappop(plus_heap))
#         else:
#             if plus_heap[0] < minus_heap[0]:
#                 print(heapq.heappop(plus_heap))
#             else:
#                 print(-heapq.heappop(minus_heap))