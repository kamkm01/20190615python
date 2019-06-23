class cookie:
    pass

a = cookie()
b = cookie()

print(type(a))
print(type(b))

class FourCal:
    #first = 0
    #second = 0
    def setdata(self,first,second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

c = FourCal()
c.first = 10
c.second = 20
print(c.first)
print(c.second)

d = FourCal()
d.setdata(3,4)

print(id(c))
print(id(d))
print(id(c.first))
print(id(d.first))
sumresult = c.add()
print(sumresult)