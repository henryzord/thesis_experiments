# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 0 | 0.935345 |
| gpuls > 1253.5 and nbumps > 1.5 and nbumps3 > 3.5 | 1 | 0.000461 |

## Ordered rules

### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| nbumps >= 2 and gpuls >= 1031 and energy <= 3700 and gdpuls <= -1 | 1 | 0.003102 |
|  | 0 | 0.938987 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

gpuls|nbumps|nbumps3|class
---|---|---|---
(1253.5-inf)|(1.5-inf)|(3.5-inf)|1
(-inf-1253.5]|(1.5-inf)|(3.5-inf)|0
(1253.5-inf)|(1.5-inf)|(0.5-3.5]|0
(-inf-1253.5]|(1.5-inf)|(0.5-3.5]|0
(1253.5-inf)|(0.5-1.5]|(0.5-3.5]|0
(-inf-1253.5]|(0.5-1.5]|(0.5-3.5]|0
(1253.5-inf)|(1.5-inf)|(-inf-0.5]|0
(-inf-1253.5]|(1.5-inf)|(-inf-0.5]|0
(1253.5-inf)|(0.5-1.5]|(-inf-0.5]|0
(-inf-1253.5]|(0.5-1.5]|(-inf-0.5]|0
(1253.5-inf)|(-inf-0.5]|(-inf-0.5]|0
(-inf-1253.5]|(-inf-0.5]|(-inf-0.5]|0

## JRip

Decision list:

rules | predicted class
---|---
(nbumps >= 2) and (gpuls >= 1031) and (energy <= 3700) and (gdpuls <= -1)|1 (12.0/3.0)
|0 (2308.0/141.0)


## J48 Decision Tree

* : 0 (2320.0/150.0)


## SimpleCart Decision Tree

* : 0(2170.0/150.0)


