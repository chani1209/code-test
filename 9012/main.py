t = int(input())

res = []


def check_parenthesis(parenthesis):
    stack = []
    for p in parenthesis:
        if p == '(':
            stack.append(p)
        else:
            if len(stack) == 0:
                return False
            stack.pop()
    return len(stack) == 0


for _ in range(t):
    res.append(check_parenthesis(input()))

for r in res:
    print('YES' if r else 'NO')