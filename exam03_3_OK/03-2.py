X = []
while 1 == 1:
    n = input()
    if n == '-1':
        break
    X.append(n)


MaxLen = 0
for i in X:
    if len(i) > MaxLen:
        MaxLen = len(i)

for i in X:
    print(' '*(MaxLen-len(i)),i,sep="")
        
