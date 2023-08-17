from itertools import combinations

dwarf_list = [ int(input()) for _ in range(9) ]

for comb in combinations(dwarf_list, 7):
    if sum(comb) == 100:
        for dwarf in sorted(comb):
            print(dwarf)
        break