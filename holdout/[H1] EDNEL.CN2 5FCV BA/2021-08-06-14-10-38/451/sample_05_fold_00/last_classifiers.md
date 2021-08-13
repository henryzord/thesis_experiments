# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Educational_level != 1 | 0 | 0.578394 |
| Educational_level = 1 | 1 | 0.033175 |
| Educational_level = 0 and Sex = 0 | 1 | 0.068493 |
| Educational_level = 0 | 1 | 0.139241 |
| Educational_level = 9 and Sex = 1 | 1 | 0.181051 |
| Educational_level = 9 and Sex = 0 | 1 | 0.218391 |

## Ordered rules

### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Educational_level = 9 | 1 | 0.333457 |
| Educational_level = 0 | 1 | 0.139241 |
| Educational_level = 1 | 1 | 0.033175 |
|  | 0 | 1.000000 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

educational_level|target
---|---
?|0
7|0
8|0
6|0
2|0
4|0
5|0
3|0
1|1
9|1
0|1

## JRip

Decision list:

rules | predicted class
---|---
(Educational_level = 9)|1 (104.0/0.0)
(Educational_level = 0)|1 (33.0/0.0)
(Educational_level = 1)|1 (7.0/0.0)
|0 (204.0/0.0)


## J48 Decision Tree

* Educational_level = 0
	* Sex = 0: 1 (15.0)
	* Sex = 1: 1 (18.19/0.19)
* Educational_level = 1: 1 (7.04/0.04)
* Educational_level = 2: 0 (21.12)
* Educational_level = 3: 0 (36.21)
* Educational_level = 4: 0 (50.29)
* Educational_level = 5: 0 (54.31)
* Educational_level = 6: 0 (27.16)
* Educational_level = 7: 0 (7.04)
* Educational_level = 8: 0 (7.04)
* Educational_level = 9
	* Sex = 0: 1 (57.0)
	* Sex = 1: 1 (47.6/0.6)


## SimpleCart Decision Tree

		* Educational_level=(0)|(1)|(9): 1(144.0/0.83)
		* Educational_level!=(0)|(1)|(9): 0(203.16/0.0)


