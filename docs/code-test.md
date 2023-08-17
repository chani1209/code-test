## 브루트포스
- 가능한 모든 경우의 수를 탐색하는 알고리즘
- 모든 경우의 수를 다 탐색하므로 정확한 답을 찾을 수 있다.
- 시간이 오래 걸린다. -> 시간초과가 나지 않을지 확인
- 될 거 같으면 완전탐색으로 풀이 -> 안되면 더 효율적인 방법(그리디, dp, 이분법 ...)으로 풀이

## 그리디
- 현재 상황에서 가장 좋은 것만 고르는 방법
- 이 문제가 그리디인지 아닌지 어려움..
- 다른 경우 고려하지 않는다. -> 최적의 해를 보장할 수 없다.

### 입력
```python
# 입력에서 너무 지연될 수도 있다.
for _ in range(10000):
    n = input()
    print(n)

# sys.stdin.readline()을 사용하면 빠르게 입력을 받을 수 있다.
import sys
for _ in range(10000):
    n = sys.stdin.readline()
    print(n)
```

### 순열
```python
from itertools import permutations

data = ['A', 'B', 'C'] # 데이터 준비

for x in permutations(data, 2): # 모든 순열 구하기
    print(x)
```

### 조합
```python
from itertools import combinations

data = ['A', 'B', 'C'] # 데이터 준비

for x in combinations(data, 2): # 모든 조합 구하기
    print(x)
```