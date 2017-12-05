LIST = []
while True:
    n = input()
    if n == 'q':
        break
    try:
        LIST.append(eval(n))
    except:
        continue
INT = []
FLOAT = []
for i in LIST:
    if type(i) is int:
        INT.append(i)
    elif type(i) == float:
        FLOAT.append(i)
#print(INT)
#print(FLOAT)
print('%.1f'%sum(FLOAT))
print(sum(INT))

if sum(FLOAT) > sum(INT):
    print('Float > Int')
elif sum(FLOAT) == sum(INT):
    print('Float = Int')
else:
    print('Float < Int')
