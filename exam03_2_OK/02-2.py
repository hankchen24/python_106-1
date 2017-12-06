LIST = []
while True:
    n = input()
    if n == 'q':
        break
    try:
        LIST.append(eval(n))
    except:
        continue

    
#LIST = [1, 2, 3.2, 4.3]

INT = []
FLOAT = []

for i in LIST:
    if type(i) is int:
        INT.append(i)
    elif type(i) == float:
        FLOAT.append(i)

print('%.1f'%sum(FLOAT))
print(sum(INT))

if sum(FLOAT) > sum(INT):
    print('Float > Int')
elif sum(FLOAT) == sum(INT):
    print('Float = Int')
else:
    print('Float < Int')
