# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Educational_level != 1 | 0 | 0.556880 |
| Educational_level = 1 | 1 | 0.024752 |
| Educational_level = 9 | 1 | 0.358559 |
| Educational_level = 0 and Prestige_score <= 63.5 and DVRT <= 105 | 1 | 0.034314 |
| Educational_level = 0 and Prestige_score <= 63.5 and DVRT > 105 | 1 | 0.100457 |
| Educational_level = 0 | 1 | 0.150862 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Educational_level != 9 and Educational_level != 0 | 0 | 0.552999 |
|  | 1 | 0.980769 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Educational_level = 9 | 1 | 0.358559 |
| Educational_level = 0 | 1 | 0.150862 |
| Educational_level = 1 | 1 | 0.024752 |
|  | 0 | 1.000000 |


# Text representation of classifiers as-is

## JRip

Decision list:

rules | predicted class
---|---
(Educational_level = 9)|1 (113.0/0.0)
(Educational_level = 0)|1 (35.0/0.0)
(Educational_level = 1)|1 (5.0/0.0)
|0 (197.0/0.0)


## PART

Decision list:

rules | predicted class
---|---
Educational_level != 9 AND Educational_level != 0|0 (200.72/5.0)
|1 (149.28/1.28)


## J48 Decision Tree

* Educational_level = 0
	* Prestige_score <= 63.5
		* DVRT <= 105: 1 (6.91/0.1)
		* DVRT > 105: 1 (21.81)
	* Prestige_score > 63.5: 1 (6.57/0.2)
* Educational_level = 1: 1 (5.04/0.04)
* Educational_level = 2: 0 (22.19)
* Educational_level = 3: 0 (32.28)
* Educational_level = 4: 0 (49.42)
* Educational_level = 5: 0 (51.44)
* Educational_level = 6: 0 (28.24)
* Educational_level = 7: 0 (6.05)
* Educational_level = 8: 0 (6.05)
* Educational_level = 9
	* Prestige_score <= 65.5
		* DVRT <= 84.5: 1 (8.33/0.33)
		* DVRT > 84.5: 1 (96.6)
	* Prestige_score > 65.5: 1 (9.05/0.65)


## SimpleCart Decision Tree

		* Educational_level=(0)|(1)|(9): 1(153.0/1.32)
		* Educational_level!=(0)|(1)|(9): 0(195.67/0.0)


