# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 0 | 0.551724 |
| Educational_level = 9 and DVRT >= 84.5 and Prestige_score >= 42.5 and Sex!=(0) and Prestige_score >= 44.5 and DVRT >= 114.5 | 1 | 0.030934 |
| Educational_level = 9 and DVRT >= 84.5 and Prestige_score >= 42.5 and Sex!=(0) and Prestige_score >= 44.5 and DVRT < 114.5 | 1 | 0.127273 |
| Educational_level = 0 | 1 | 0.168831 |
| Educational_level = 1 | 1 | 0.035176 |
| Educational_level = 9 and DVRT >= 84.5 and Prestige_score < 42.5 | 1 | 0.232000 |
| Educational_level = 9 and DVRT < 84.5 | 1 | 0.040500 |
| Educational_level = 9 and DVRT >= 84.5 and Prestige_score >= 42.5 and Sex!=(0) and Prestige_score < 44.5 | 1 | 0.035734 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Educational_level = 9 | 1 | 0.358126 |
| Educational_level = 5 | 0 | 0.505376 |
| Educational_level = 4 | 0 | 0.483146 |
| Educational_level = 0 | 1 | 0.276596 |
| DVRT <= 103 | 0 | 0.918605 |
| Educational_level = 2 | 0 | 0.533333 |
| Type_school = 1 | 1 | 0.240196 |
|  | 0 | 1.000000 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Educational_level = 9 | 1 | 0.358126 |
| Educational_level = 0 | 1 | 0.168831 |
|  | 0 | 0.964824 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

educational_level|target
---|---
1|1
2|0
?|0
3|0
8|0
6|0
4|0
5|0
7|0
9|1
0|1

## JRip

Decision list:

rules | predicted class
---|---
(Educational_level = 9)|1 (110.0/0.0)
(Educational_level = 0)|1 (39.0/0.0)
|0 (199.0/7.0)


## PART

Decision list:

rules | predicted class
---|---
Educational_level = 9|1 (110.96/0.96)
Educational_level = 5|0 (47.41)
Educational_level = 4|0 (43.37)
Educational_level = 0|1 (39.34/0.34)
DVRT <= 103|0 (78.31)
Educational_level = 2|0 (8.18)
Type_school = 1|1 (10.44/3.44)
|0 (10.0)


## J48 Decision Tree

* Educational_level = 0: 1 (39.34/0.34)
* Educational_level = 1: 1 (7.06/0.06)
* Educational_level = 2: 0 (20.17)
* Educational_level = 3: 0 (35.3)
* Educational_level = 4: 0 (43.37)
* Educational_level = 5: 0 (47.41)
* Educational_level = 6: 0 (26.23)
* Educational_level = 7: 0 (7.06)
* Educational_level = 8: 0 (11.1)
* Educational_level = 9: 1 (110.96/0.96)


## SimpleCart Decision Tree

		* Educational_level=(0)|(1)|(9)
	* DVRT < 84.5: 1(9.0/0.45)
	* DVRT >= 84.5
		* Prestige_score < 42.5: 1(76.66/0.0)
		* Prestige_score >= 42.5
			* Sex=(0): 1(31.4/0.0)
			* Sex!=(0)
				* Prestige_score < 44.5: 1(7.37/0.45)
				* Prestige_score >= 44.5
					* DVRT < 114.5: 1(20.16/0.0)
					* DVRT >= 114.5: 1(11.38/0.45)
		* Educational_level!=(0)|(1)|(9): 0(190.64/0.0)


