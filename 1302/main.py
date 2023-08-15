res = {}

for _ in range(int(input())):
    book = input()
    if res.keys().__contains__(book):
        res[book] += 1
    else:
        res[book] = 1

sorted_dict = sorted(res.items(), key=lambda x: (-x[1], x[0]))
print(sorted_dict[0][0])