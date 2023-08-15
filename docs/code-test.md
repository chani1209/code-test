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
