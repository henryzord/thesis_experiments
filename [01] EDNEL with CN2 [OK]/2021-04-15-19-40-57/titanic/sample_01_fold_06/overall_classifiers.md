# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | -1.0 | 0.676768 |
| Sex < -0.6995 | 1.0 | 0.153393 |
| Sex > -1.92 and Age > -0.228 and Class <= -0.923 | 1.0 | 0.010340 |
|  | -1.0 | 0.676768 |
| Sex <= -1.92 and Class > -0.923 and Class > 0.0214 | 1.0 | 0.012101 |
| Sex <= -1.92 and Class <= -0.923 | 1.0 | 0.132188 |
| Sex < -0.6995 | 1.0 | 0.153393 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Sex > -0.6995 | -1.0 | 0.629931 |
| Class <= -0.4508 | 1.0 | 0.721660 |
| Class <= 0.4932 | -1.0 | 0.145112 |
|  | 1.0 | 0.991379 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Sex <= -1.92 and Class <= -0.923 | 1.0 | 0.132188 |
| Sex <= -1.92 and Class >= 0.965 | 1.0 | 0.012101 |
|  | -1.0 | 0.768789 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

sex|survived
---|---
(-inf--0.6995]|1.0
(-0.6995-inf)|-1.0

## JRip

Decision list:

rules | predicted class
---|---
(Sex <= -1.92) and (Class <= -0.923)|1.0 (233.0/15.0)
(Sex <= -1.92) and (Class >= 0.965)|1.0 (22.0/3.0)
|-1.0 (1725.0/403.0)


## PART

Decision list:

rules | predicted class
---|---
Sex > -0.6995|-1.0 (1296.0/270.0)
Class <= -0.4508|1.0 (196.0/10.0)
Class <= 0.4932|-1.0 (137.0/59.0)
|1.0 (21.0/3.0)


## J48 Decision Tree

* Sex <= -1.92
	* Class <= -0.923: 1.0 (198.0/15.0)
	* Class > -0.923
		* Class <= 0.0214: -1.0 (149.0/72.0)
		* Class > 0.0214: 1.0 (21.0/3.0)
* Sex > -1.92: -1.0 (1282.0/260.0)


## SimpleCart Decision Tree

* Sex < -0.6995: 1.0(319.0/109.0)
* Sex >= -0.6995: -1.0(1231.0/321.0)


