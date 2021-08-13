# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 0 | 0.551724 |
| Educational_level = 9 | 1 | 0.375244 |
| Educational_level = 0 | 1 | 0.135135 |
| Educational_level = 1 | 1 | 0.030303 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Educational_level = 5 | 0 | 0.239024 |
| Educational_level = 4 | 0 | 0.223881 |
| Educational_level = 3 | 0 | 0.170213 |
| Educational_level = 6 | 0 | 0.147541 |
| Educational_level = 2 | 0 | 0.133333 |
| Educational_level = 0 and Sex = 0 | 1 | 0.531250 |
| Educational_level = 9 and Sex = 0 | 1 | 0.823529 |
| Educational_level = 9 and DVRT <= 120.5 and DVRT <= 112.5 and DVRT <= 107.5 and DVRT > 93.5 | 1 | 0.484914 |
| Educational_level = 0 | 1 | 0.464286 |
| Type_school = 1 and DVRT > 90.5 and DVRT <= 114.5 and DVRT > 109.5 | 1 | 0.375000 |
| Type_school = 1 and DVRT > 90.5 and DVRT > 112 and Prestige_score <= 41 | 1 | 0.334711 |
| Type_school = 1 and DVRT > 90.5 and DVRT > 112 | 1 | 0.280702 |
| Type_school = 1 and DVRT <= 90.5 | 1 | 0.173611 |
| Type_school = 1 | 1 | 0.268908 |
|  | 0 | 0.882353 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Educational_level = 9 | 1 | 0.375244 |
| Educational_level = 0 | 1 | 0.135135 |
|  | 0 | 0.969697 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

educational_level|target
---|---
1|1
0|1
9|1
8|0
2|0
3|0
7|0
?|0
4|0
6|0
5|0

## JRip

Decision list:

rules | predicted class
---|---
(Educational_level = 9)|1 (120.0/0.0)
(Educational_level = 0)|1 (30.0/0.0)
|0 (198.0/6.0)


## PART

Decision list:

rules | predicted class
---|---
Educational_level = 5|0 (49.71)
Educational_level = 4|0 (45.66)
Educational_level = 3|0 (32.47)
Educational_level = 6|0 (27.39)
Educational_level = 2|0 (24.35)
Educational_level = 0 AND Sex = 0|1 (17.0)
Educational_level = 9 AND Sex = 0|1 (70.0)
Educational_level = 9 AND DVRT <= 120.5 AND DVRT <= 112.5 AND DVRT <= 107.5 AND DVRT > 93.5|1 (15.31/0.31)
Educational_level = 0|1 (13.43/0.43)
Type_school = 1 AND DVRT > 90.5 AND DVRT <= 114.5 AND DVRT > 109.5|1 (9.0)
Type_school = 1 AND DVRT > 90.5 AND DVRT > 112 AND Prestige_score <= 41|1 (9.9/1.39)
Type_school = 1 AND DVRT > 90.5 AND DVRT > 112|1 (9.25/0.77)
Type_school = 1 AND DVRT <= 90.5|1 (8.39/3.39)
Type_school = 1|1 (8.14/0.14)
|0 (8.0/2.0)


## J48 Decision Tree

* Educational_level = 0: 1 (28.47/0.47)
* Educational_level = 1: 1 (5.08/0.08)
* Educational_level = 2: 0 (18.3)
* Educational_level = 3: 0 (32.53)
* Educational_level = 4: 0 (39.65)
* Educational_level = 5: 0 (43.72)
* Educational_level = 6: 0 (23.38)
* Educational_level = 7: 0 (2.03)
* Educational_level = 8: 0 (6.1)
* Educational_level = 9: 1 (105.73/1.73)


## SimpleCart Decision Tree

		* Educational_level=(0)|(1)|(9): 1(156.0/2.27)
		* Educational_level!=(0)|(1)|(9): 0(189.72/0.0)


