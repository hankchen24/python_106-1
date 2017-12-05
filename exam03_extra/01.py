x = int(input())

drinks = x  #一開始買的
caps = x    #一開始買的 所拿到的瓶蓋

while True:
    drinks = drinks + caps // 4     #後來飲料數會變成，原本的飲料+瓶蓋換的
    caps = (caps%4) + (caps // 4)   #頻蓋數 = 換剩下的 + 又換來的飲料的瓶蓋

    if caps == 3:         #如果最後瓶蓋數剩下3就可以借一瓶，所以飲料數+1
        drinks += 1
        break
    elif caps < 3:      #如果小於3就不能借
        break

    
print(drinks)
