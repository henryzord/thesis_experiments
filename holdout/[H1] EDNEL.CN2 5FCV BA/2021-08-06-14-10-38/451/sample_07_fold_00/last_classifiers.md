# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Educational_level != 1 | 0 | 0.553445 |
| Educational_level = 0 and Sex = 0 | 1 | 0.080189 |
| Educational_level = 1 | 1 | 0.015152 |
| Educational_level = 9 | 1 | 0.353173 |
| Educational_level = 0 | 1 | 0.170213 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Educational_level = 5 | 0 | 0.240196 |
| Educational_level = 4 | 0 | 0.217172 |
| Educational_level = 3 | 0 | 0.179894 |
| Educational_level = 6 | 0 | 0.153005 |
| Educational_level = 0 and Sex = 1 | 1 | 0.359375 |
| Educational_level = 9 and Sex = 0 | 1 | 0.601942 |
| Educational_level = 9 and Type_school = 1 | 1 | 0.502374 |
| Educational_level = 2 | 0 | 0.478261 |
| Educational_level = 0 | 1 | 0.472222 |
| Educational_level = 8 | 0 | 0.500000 |
| Sex = 0 | 0 | 0.416667 |
| Type_school = 1 | 1 | 0.300000 |
|  | 1 | 0.363636 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Educational_level = 9 | 1 | 0.353173 |
| Educational_level = 0 | 1 | 0.170213 |
|  | 0 | 0.984848 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

educational_level|target
---|---
1|1
0|1
9|1
7|0
8|0
?|0
6|0
4|0
3|0
5|0
2|0

## JRip

Decision list:

rules | predicted class
---|---
(Educational_level = 9)|1 (112.0/0.0)
(Educational_level = 0)|1 (40.0/0.0)
|0 (198.0/3.0)


## PART

Decision list:

rules | predicted class
---|---
Educational_level = 5|0 (49.85)
Educational_level = 4|0 (43.75)
Educational_level = 3|0 (34.59)
Educational_level = 6|0 (28.49)
Educational_level = 0 AND Sex = 1|1 (23.7/0.7)
Educational_level = 9 AND Sex = 0|1 (62.0)
Educational_level = 9 AND Type_school = 1|1 (47.25/1.25)
Educational_level = 2|0 (22.51)
Educational_level = 0|1 (17.39/0.39)
Educational_level = 8|0 (7.16)
Sex = 0|0 (5.0)
Type_school = 1|1 (4.3/1.3)
|1 (4.0)


## J48 Decision Tree

* Educational_level = 0
	* Sex = 0: 1 (17.0)
	* Sex = 1: 1 (23.7/0.7)
* Educational_level = 1: 1 (3.05/0.05)
* Educational_level = 2: 0 (22.38)
* Educational_level = 3: 0 (34.59)
* Educational_level = 4: 0 (43.75)
* Educational_level = 5: 0 (49.85)
* Educational_level = 6: 0 (28.49)
* Educational_level = 7: 0 (6.1)
* Educational_level = 8: 0 (7.12)
* Educational_level = 9
	* Sex = 0: 1 (62.0)
	* Sex = 1: 1 (51.95/1.95)


## SimpleCart Decision Tree

		* Educational_level=(0)|(1)|(9): 1(155.0/2.7)
		* Educational_level!=(0)|(1)|(9): 0(192.29/0.0)


