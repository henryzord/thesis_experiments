# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 0 | 0.591429 |
| Educational_level = 9 | 1 | 0.324279 |
| Educational_level = 1 | 1 | 0.023585 |
| Educational_level = 0 | 1 | 0.141079 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Educational_level != 9 and Educational_level != 0 | 0 | 0.579767 |
|  | 1 | 0.966216 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Educational_level = 9 | 1 | 0.324279 |
| Educational_level = 0 | 1 | 0.141079 |
| Educational_level = 1 | 1 | 0.023585 |
|  | 0 | 1.000000 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

educational_level|target
---|---
1|1
0|1
9|1
8|0
?|0
4|0
3|0
6|0
5|0
2|0
7|0

## JRip

Decision list:

rules | predicted class
---|---
(Educational_level = 9)|1 (104.0/0.0)
(Educational_level = 0)|1 (34.0/0.0)
(Educational_level = 1)|1 (5.0/0.0)
|0 (207.0/0.0)


## PART

Decision list:

rules | predicted class
---|---
Educational_level != 9 AND Educational_level != 0|0 (139.99/4.0)
|1 (94.01/2.01)


## SimpleCart Decision Tree

		* Educational_level=(0)|(1)|(9): 1(143.0/2.07)
		* Educational_level!=(0)|(1)|(9): 0(204.92/0.0)


