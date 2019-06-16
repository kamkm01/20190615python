#1번 문제
'''
num = (input('주민번호: '))
while True:
    if len(num) == 14:
        G = int(num[7])
        if G % 2 == 1:
        print('male')
        elif G % 2 == 0:
        print('female')
        break
    else:
        print('주민등록 번호가 올바르지 않습니다')
        continue
'''
##2번 문제
'''
for x in range(1,10):
    print()
    print('[---%d단---]'%x)
    for y in range(2,10):
        print('%d X %d = %2d'%(y,x,x * y),end = ' ,')
        '''

###3번 문제
'''
coffee = {'아메리카노':2500,'카페라떼':3000,'카푸치노':3500}

print(list(coffee.keys()))
c = input('선택 : ')

print(coffee[c])
'''

#4번 문제
'''
import random as r
count = 0

g = ['*','+','-','/']

for x in range(0,5):
    a = r.randint(1,50)
    b = r.randint(1,50)
    G = r.choice(g)
    Q = str(a) + G + str(b)
    print(Q,'=?')
    c = int(input('anwser='))

    if int(eval(Q)) == c:
        print('correct!')
        count +=1
    else:
        print('wrong!')
print('{}개 맞춤'.format(count))
'''

