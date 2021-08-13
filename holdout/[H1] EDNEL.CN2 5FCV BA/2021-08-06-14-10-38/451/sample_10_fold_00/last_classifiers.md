# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Educational_level != 1 | 0 | 0.586924 |
| Educational_level = 1 | 1 | 0.018957 |
| Educational_level = 0 | 1 | 0.133891 |
| Educational_level = 9 | 1 | 0.328956 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Educational_level = 9 | 1 | 0.328956 |
| Educational_level = 5 | 0 | 0.586207 |
| Educational_level = 4 | 0 | 0.571429 |
| Educational_level = 3 | 0 | 0.506849 |
| Educational_level = 0 | 1 | 0.310680 |
| Educational_level = 6 | 0 | 0.870968 |
|  | 0 | 0.916667 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Educational_level = 9 | 1 | 0.328956 |
| Educational_level = 0 | 1 | 0.133891 |
|  | 0 | 0.981043 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

educational_level|target
---|---
1|1
8|0
?|0
3|0
6|0
7|0
5|0
2|0
4|0
9|1
0|1

## JRip

Decision list:

rules | predicted class
---|---
(Educational_level = 9)|1 (107.0/0.0)
(Educational_level = 0)|1 (32.0/0.0)
|0 (211.0/4.0)


## PART

Decision list:

rules | predicted class
---|---
Educational_level = 9|1 (88.58/1.58)
Educational_level = 5|0 (40.73)
Educational_level = 4|0 (38.69)
Educational_level = 3|0 (30.55)
Educational_level = 0|1 (25.45/0.45)
Educational_level = 6|0 (23.42)
|0 (32.58/3.0)


## J48 Decision Tree

* Educational_level = 0: 1 (32.56/0.56)
* Educational_level = 1: 1 (4.07/0.07)
* Educational_level = 2: 0 (24.42)
* Educational_level = 3: 0 (37.65)
* Educational_level = 4: 0 (48.84)
* Educational_level = 5: 0 (51.89)
* Educational_level = 6: 0 (27.47)
* Educational_level = 7: 0 (5.09)
* Educational_level = 8: 0 (9.16)
* Educational_level = 9: 1 (108.87/1.87)


## SimpleCart Decision Tree

		* Educational_level=(0)|(1)|(9): 1(143.0/2.49)
		* Educational_level!=(0)|(1)|(9): 0(204.5/0.0)


