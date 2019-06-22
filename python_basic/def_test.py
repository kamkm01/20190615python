def add(a,b):
    result = a + b
    print("a =",a,"b =",b)
    return result
print(add(4,5))

def add_many(*args):
    result = 0
    for i in args:
        result = result + i
    return result
print(add_many(1,2,3,4,4,5,6,7))


def print_kwargs(**kwargs):
    print(kwargs)
print_kwargs(name = 'kang',age = 67)

a = 2
def test_1(a):
    a = a + 1
print(test_1(a))
print(a)