import random as r

num = r.sample((1,10),3)
while True:
    UN = []
    p_num = input('guess! : ')
    UN.extend(p_num)
    count_awser = []
    for x in UN:
        if x in num:
            if UN.index(x) = num.index(x):
                count_awnser.append('strike')
            else:
                count_awnser.append('ball')
    if count_awser.count('strike') == 3:
        break
    print('strike: ',count_awnser.count('strike'),'ball: 'count_awser.count('ball'))
