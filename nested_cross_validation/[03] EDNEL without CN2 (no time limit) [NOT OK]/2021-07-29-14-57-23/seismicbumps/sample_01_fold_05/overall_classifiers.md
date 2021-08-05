# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 0 | 0.935345 |
| genergy > 17640 and genergy <= 77640 and gpuls > 1137.5 and gdenergy = all and gdpuls = all and nbumps > 1.5 and nbumps2 > 0.5 and nbumps4 <= 0.5 and nbumps5 = all and nbumps6 = all and nbumps7 = all and nbumps89 = all and maxenergy > 650 | 1 | 0.000461 |
| genergy <= 17640 and gpuls <= 1137.5 and gdenergy = all and gdpuls = all and nbumps > 0.5 and nbumps <= 1.5 and nbumps2 <= 0.5 and nbumps4 <= 0.5 and nbumps5 = all and nbumps6 = all and nbumps7 = all and nbumps89 = all and maxenergy <= 650 | 1 | 0.000461 |
| genergy > 77640 and gpuls <= 1137.5 and gdenergy = all and gdpuls = all and nbumps > 0.5 and nbumps <= 1.5 and nbumps2 <= 0.5 and nbumps4 > 0.5 and nbumps5 = all and nbumps6 = all and nbumps7 = all and nbumps89 = all and maxenergy > 650 | 1 | 0.000154 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 0 | 0.935345 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 0 | 0.935345 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

genergy|gpuls|gdenergy|gdpuls|nbumps|nbumps2|nbumps4|nbumps5|nbumps6|nbumps7|nbumps89|maxenergy|class
---|---|---|---|---|---|---|---|---|---|---|---|---
(17640-77640]|(1137.5-inf)|all|all|(1.5-inf)|(0.5-inf)|(0.5-inf)|all|all|all|all|(650-inf)|0
(77640-inf)|(1137.5-inf)|all|all|(1.5-inf)|(0.5-inf)|(0.5-inf)|all|all|all|all|(650-inf)|0
(-inf-17640]|(-inf-1137.5]|all|all|(1.5-inf)|(0.5-inf)|(0.5-inf)|all|all|all|all|(650-inf)|0
(17640-77640]|(-inf-1137.5]|all|all|(1.5-inf)|(0.5-inf)|(0.5-inf)|all|all|all|all|(650-inf)|0
(77640-inf)|(-inf-1137.5]|all|all|(1.5-inf)|(0.5-inf)|(0.5-inf)|all|all|all|all|(650-inf)|0
(17640-77640]|(1137.5-inf)|all|all|(1.5-inf)|(-inf-0.5]|(0.5-inf)|all|all|all|all|(650-inf)|1
(77640-inf)|(1137.5-inf)|all|all|(1.5-inf)|(-inf-0.5]|(0.5-inf)|all|all|all|all|(650-inf)|0
(17640-77640]|(1137.5-inf)|all|all|(1.5-inf)|(0.5-inf)|(-inf-0.5]|all|all|all|all|(650-inf)|1
(17640-77640]|(-inf-1137.5]|all|all|(1.5-inf)|(-inf-0.5]|(0.5-inf)|all|all|all|all|(650-inf)|0
(77640-inf)|(-inf-1137.5]|all|all|(1.5-inf)|(-inf-0.5]|(0.5-inf)|all|all|all|all|(650-inf)|0
(77640-inf)|(1137.5-inf)|all|all|(1.5-inf)|(0.5-inf)|(-inf-0.5]|all|all|all|all|(650-inf)|0
(77640-inf)|(-inf-1137.5]|all|all|(1.5-inf)|(0.5-inf)|(-inf-0.5]|all|all|all|all|(650-inf)|0
(-inf-17640]|(-inf-1137.5]|all|all|(1.5-inf)|(0.5-inf)|(-inf-0.5]|all|all|all|all|(650-inf)|0
(17640-77640]|(-inf-1137.5]|all|all|(1.5-inf)|(0.5-inf)|(-inf-0.5]|all|all|all|all|(650-inf)|0
(17640-77640]|(1137.5-inf)|all|all|(0.5-1.5]|(-inf-0.5]|(0.5-inf)|all|all|all|all|(650-inf)|1
(77640-inf)|(1137.5-inf)|all|all|(0.5-1.5]|(-inf-0.5]|(0.5-inf)|all|all|all|all|(650-inf)|0
(77640-inf)|(-inf-1137.5]|all|all|(0.5-1.5]|(-inf-0.5]|(0.5-inf)|all|all|all|all|(650-inf)|1
(77640-inf)|(1137.5-inf)|all|all|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|all|all|all|all|(650-inf)|0
(-inf-17640]|(-inf-1137.5]|all|all|(0.5-1.5]|(-inf-0.5]|(0.5-inf)|all|all|all|all|(650-inf)|0
(17640-77640]|(-inf-1137.5]|all|all|(0.5-1.5]|(-inf-0.5]|(0.5-inf)|all|all|all|all|(650-inf)|0
(17640-77640]|(1137.5-inf)|all|all|(1.5-inf)|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(650-inf)|0
(77640-inf)|(-inf-1137.5]|all|all|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|all|all|all|all|(650-inf)|0
(17640-77640]|(-inf-1137.5]|all|all|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|all|all|all|all|(650-inf)|0
(-inf-17640]|(-inf-1137.5]|all|all|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|all|all|all|all|(650-inf)|0
(77640-inf)|(1137.5-inf)|all|all|(1.5-inf)|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(650-inf)|0
(-inf-17640]|(-inf-1137.5]|all|all|(1.5-inf)|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(650-inf)|1
(77640-inf)|(-inf-1137.5]|all|all|(1.5-inf)|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(650-inf)|0
(17640-77640]|(-inf-1137.5]|all|all|(1.5-inf)|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(650-inf)|0
(17640-77640]|(1137.5-inf)|all|all|(0.5-1.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(650-inf)|0
(77640-inf)|(1137.5-inf)|all|all|(0.5-1.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(650-inf)|0
(77640-inf)|(-inf-1137.5]|all|all|(0.5-1.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(650-inf)|0
(-inf-17640]|(-inf-1137.5]|all|all|(0.5-1.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(650-inf)|0
(17640-77640]|(-inf-1137.5]|all|all|(0.5-1.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(650-inf)|0
(17640-77640]|(1137.5-inf)|all|all|(1.5-inf)|(0.5-inf)|(-inf-0.5]|all|all|all|all|(-inf-650]|0
(77640-inf)|(1137.5-inf)|all|all|(1.5-inf)|(0.5-inf)|(-inf-0.5]|all|all|all|all|(-inf-650]|0
(-inf-17640]|(-inf-1137.5]|all|all|(1.5-inf)|(0.5-inf)|(-inf-0.5]|all|all|all|all|(-inf-650]|1
(17640-77640]|(-inf-1137.5]|all|all|(1.5-inf)|(0.5-inf)|(-inf-0.5]|all|all|all|all|(-inf-650]|0
(77640-inf)|(-inf-1137.5]|all|all|(1.5-inf)|(0.5-inf)|(-inf-0.5]|all|all|all|all|(-inf-650]|0
(77640-inf)|(1137.5-inf)|all|all|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|all|all|all|all|(-inf-650]|0
(17640-77640]|(1137.5-inf)|all|all|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|all|all|all|all|(-inf-650]|0
(-inf-17640]|(-inf-1137.5]|all|all|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|all|all|all|all|(-inf-650]|0
(77640-inf)|(-inf-1137.5]|all|all|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|all|all|all|all|(-inf-650]|0
(17640-77640]|(-inf-1137.5]|all|all|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|all|all|all|all|(-inf-650]|0
(-inf-17640]|(-inf-1137.5]|all|all|(0.5-1.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(-inf-650]|1
(17640-77640]|(1137.5-inf)|all|all|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(-inf-650]|0
(77640-inf)|(1137.5-inf)|all|all|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(-inf-650]|0
(77640-inf)|(-inf-1137.5]|all|all|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(-inf-650]|0
(-inf-17640]|(-inf-1137.5]|all|all|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(-inf-650]|0
(17640-77640]|(-inf-1137.5]|all|all|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(-inf-650]|0

## JRip

Decision list:

rules | predicted class
---|---
=> class=0 (2320.0/150.0)


## PART

Decision list:

rules | predicted class
---|---
|0 (1740.0/112.0)


## J48 Decision Tree

* : 0 (2088.0/135.0)


## SimpleCart Decision Tree

* : 0(2170.0/150.0)


