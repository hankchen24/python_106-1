﻿# 讀取csv-班上成績 #

## 說明 ##


公館國中的數學老師要計算同學的期末分數，有班上同學的成績檔案<br>
並想知道總分第一名，以及需要補考的人。<br>
計算規則如下：<br>
<br>
總分為：<br>
1. 平時成績*10%<br>
2. 第一次期中考成績*25%<br>
3. 第二次期中考成績*25%<br>
4. 期末考成績*40%<br>
<br>
*若第一名有兩位以上，都把學號列印出來，中間用空個隔開。<br>
*總分未滿60分的人需要補考。<br>
<br>

<br>
ID:學生座號<br>
regular:考試成績<br>
midtern1:第一次期中考成績<br>
midtern2:第二次期中考成績<br>
final:期末考成績<br>
<br>

## Input Format ##

輸入一個字串表示下列檔案的名字。例如 MathScore01.txt。<br>
可讀取../app/MathScore01.txt的文字檔內容。<br>
文字檔內容自行下載。<br>

## Output Format ##

1.總分最高的學生座號（若第一名有兩位以上，都把學號列印出來，中間用空個隔開，座號小到大排列)<br>
2.需要補考的學生座號（中間用空格隔開，座號小到大排列）<br>

## Sample Input 1 ##
```
MathScore01.csv

```

## Sample Output 1 ##
```
12 33
1 11 34 37 40
```

## Hint ##

```

```
