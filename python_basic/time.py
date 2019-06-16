
import time
'''
input('when you ready, press the enter')
a = time.time()
input('you think now is the time that you pass the 20 sceonds, press the enter')
b = time.time()
real_time = b - a
gap = abs(real_time - 20)
print('실제 걸린 시간 : {:.3}초'.format(real_time))
print('차이 : {:.3}초'.format(gap))
'''
import random as r

count = 0
r_num = r.randint(1,100)
input('시작!')
start = time.time()
while True:
    count += 1
    guess_num = int(input('write the number between 1~100   '))
    if guess_num == r_num:
        print('great!')
        break
    elif guess_num > r_num:
            print('write more small number.')
            continue
    elif guess_num < r_num:
            print('write more big number')
            continue
end = time.time()
print('{:.2f}초 동안 {}번 만에 맞추셨네요!'.format(end - start,count))

