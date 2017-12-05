f1 = open('C:\\Users\\user/Desktop/MathScore01.csv','r')
file = f1.readlines()

f1.close()

LIST = []
for i in file:
    LIST.append(i.strip().split(','))

LIST2 = []
for i in range(1,len(LIST)):
    
    total_score = int(LIST[i][1])*0.1 +int(LIST[i][2])*0.25+int(LIST[i][3])*0.25+int(LIST[i][4])*0.4
    LIST2.append([LIST[i][0],total_score])
    
Fail = []
MaxScore = 0

for i in LIST2:
    if i[1]< 60:
        Fail.append( i[0])

    if i[1] > MaxScore:
        MaxScore = i[1]
        ID = i[0]


print(ID)
print(' '.join(Fail))
