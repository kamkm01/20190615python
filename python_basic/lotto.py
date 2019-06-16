import random as r

a = list(range(1,46))

for x in range(1,6):
    lotto = r.sample(a,6)
    print(lotto)