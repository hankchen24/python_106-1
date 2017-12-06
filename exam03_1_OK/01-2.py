x = input()
dic = {'A':10,'J':18,'S':26,
       'B':11,'K':19,'T':27,
       'C':12,'L':20,'U':28,
       'D':13,'M':21,'V':29,
       'E':14,'N':22,'W':32,
       'F':15,'O':35,'X':30,
       'G':16,'P':23,'Y':31,
       'H':17,'Q':24,'Z':33,
       'I':34,'R':25}
# x = 'A123456789'

x = str(dic[x[0]] ) + x[1:]

# x = '10123456789'
LIST = []
LIST.append(int(x[0]))
LIST.append(int(x[-1]))
x = x[1:-1]
# x = '012345678'

for i in range(len(x)):
    LIST.append(int(x[i])* (9-i))

if sum(LIST)% 10 == 0:
    print('real')
elif sum(LIST)% 10 != 0:
    print('fake')
    
    
