dic =   {'A':10,'J':18,'S':26,
       'B':11,'K':19,'T':27,
       'C':12,'L':20,'U':28,
       'D':13,'M':21,'V':29,
       'E':14,'N':22,'W':32,
       'F':15,'O':35,'X':30,
       'G':16,'P':23,'Y':31,
       'H':17,'Q':24,'Z':33,
       'I':34,'R':25}
n = input()
n = str(dic[n[0]]) + n[1:]

LIST = []
for i in range(0,len(n)):
    if i == 0:
        LIST.append(int(n[i]) * 1)
    elif i == 10:
        LIST.append(int(n[i]) * 1)

    else:
        LIST.append(int(n[i]) *(10-i))
Total = sum(LIST)

if Total % 10 == 0:
    print('real')
else:
    print('fake')
