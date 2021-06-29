# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 1 | 0.527132 |
| A2 > 2.5 and A5 > 2.5 and A5 <= 3.5 | 0 | 0.056761 |
| A2 > 2.5 and A5 <= 2.5 | 0 | 0.252747 |
| A2 >= 2.5 | 0 | 0.349137 |
| A5 > 3.5 | 0 | 0.317726 |

## Ordered rules

### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| A2 >= 3 and A4 >= 2 | 0 | 0.298969 |
| A5 >= 4 | 0 | 0.266187 |
| A2 >= 3 and A5 <= 2 | 0 | 0.097345 |
|  | 1 | 1.000000 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

a2|a5|class
---|---|---
(2.5-inf)|(3.5-inf)|0
(-inf-2.5]|(3.5-inf)|0
(-inf-2.5]|(2.5-3.5]|1
(2.5-inf)|(2.5-3.5]|0
(-inf-2.5]|(-inf-2.5]|1
(2.5-inf)|(-inf-2.5]|0

## JRip

Decision list:

rules | predicted class
---|---
(A2 >= 3) and (A4 >= 2)|0 (87.0/0.0)
(A5 >= 4)|0 (74.0/0.0)
(A2 >= 3) and (A5 <= 2)|0 (22.0/0.0)
|1 (204.0/0.0)


## J48 Decision Tree

* A5 <= 3.5
	* A2 <= 2.5: 1 (127.0)
	* A2 > 2.5: 0 (68.0/9.0)
* A5 > 3.5: 0 (63.0)


## SimpleCart Decision Tree

* A2 < 2.5
	* A5 < 3.5: 1(193.0/0.0)
	* A5 >= 3.5: 0(64.0/0.0)
* A2 >= 2.5: 0(119.0/11.0)


