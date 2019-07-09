from itertools import combinations
num ,x = input().split()
x = int(x)
sumNum = []
comb = combinations(num,len(num)-x)
for i in comb:
    sumNum.append("".join(i))
print(min(sumNum))
#
