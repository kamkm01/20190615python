import re

p = re.compile('[a-z]+')

m = p.finditer("cc3 Python king")
print(m)
for x in m:
    print(x)