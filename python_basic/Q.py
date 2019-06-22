f = open('./python_basic/word2.txt','w')
list_1 = ['fox','hipo','bird','tiger','bear']
for x in list_1:
    f.write(x)
    f.write('\n')
f.close()