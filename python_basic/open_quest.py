f = open('./python_basic/word.txt','a')
'''쓰기(w)
for i in range(1,11):
    data = '%d번째 줄입니다.\n'%i
    f.write(data)
'''
'''readline()을 이용한 출력
while True:
    line = f.readline()
    if not line:
        break
    print(line)
'''
'''readlines()를 이용한 출력 리스트로 반환
lines = f.readlines()
for line in lines:
    print(line)
'''


f.close()
