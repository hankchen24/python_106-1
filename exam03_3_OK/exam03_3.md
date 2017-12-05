# 文字長度判斷 #

## 說明 ##

1.今天讓使用者任意輸入多行文字(while迴圈)，並且輸入-1離開輸入。<br>
2.並且讓所有的文字都向右靠齊。<br>
<br>

```
1.while迴圈
2.包裝
3.split & jion
```


## Input Format ##

字串1(str)<br>
字串2(str)<br>
...<br>
字串n(str)<br>
-1<br>

## Output Format ##

字串1(str)<br>
字串2(str)<br>
...<br>
字串n(str)<br>

## Sample Input 1 ##
```
Hello World!
This is an example.

```

## Sample Output 1 ##
```
       Hello World!
This is an example.
```
## Sample Input 2 ##
```
This night is flawless,
don't you let it go.
I'm wonderstruck, dancing around all alone.
I'll spend forever wondering if you knew
I was enchanted to meet you.
```

## Sample Output 2 ##
```
                    This night is flawless,
                       don't you let it go.
I'm wonderstruck, dancing around all alone.
   I'll spend forever wondering if you knew
               I was enchanted to meet you.
```

## Hint ##

```
1.可利用list先把輸入過的字串儲存起來。
2.尾巴的符號要對齊。
3.輸出的最最最最末端有個換行。
```
