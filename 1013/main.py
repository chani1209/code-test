import re


def main():
    T = int(input())
    pattern = r"^(100+1+|01)+$"

    for _ in range(T):
        s = input().strip()
        if re.match(pattern, s):
            print("YES")
        else:
            print("NO")

main()