import random as r
import time

print('준비가 되면 enter를 누르세요')
input()
start_time = time.time()

word_list = ['note','time','ping','route','print','import','box']
word_list2 = open('./python_basic/word2.txt','r')
read_line = word_list2.readlines()
choose_word2 = r.choice(read_line)
choose_word2 = choose_word2.replace('\n','')


count = 0
choose_word = r.choice(word_list)
choice_type = input('word_list or word_list2? : ')
while count <= 5:
    if choice_type == 'word_list':
        print(choose_word)
        answer = input('answer:')
        if answer == choose_word:
            print('great!')
            count = count + 1
            choose_word = r.choice(word_list)
        else:
            print('wrong!')
    elif choice_type == 'word_list2':
        print(choose_word2)
        answer = input('answer:')
        if answer == choose_word2:
            print('great!')
            count = count + 1
            choose_word2 = r.choice(read_line)
            choose_word2 = choose_word2.replace('\n','')
        else:
            print('wrong!')
    else:
        continue

end_time = time.time()
print('time: {:.2f}'.format(end_time - start_time))
