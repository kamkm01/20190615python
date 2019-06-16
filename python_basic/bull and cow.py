import random as r
num = []
p = 3
for x in range(p):
    rn = r.randint(1,9)
    num.append(rn)
ua = input('guess : ')
UA = []
UA.extend(ua)
for z in range(p):
    UA[z] = int(UA[z])
rs = []
for x in UA:
    if x in num:
        if UA.index(x) == num.index(x):
            rs.append('bulls')
        else:
            rs.append('cow')
C = rs.count('cow')
B = rs.count('bulls')
print('cow : {},bulls : {}'.format(C,B))