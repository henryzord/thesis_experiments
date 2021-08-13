# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 0 | 0.551724 |
| Educational_level = 9 and Sex!=(0) and DVRT >= 84.5 and Prestige_score < 65.5 and Prestige_score < 22.5 and DVRT < 117.0 | 1 | 0.045228 |
| Educational_level = 9 and Sex!=(0) and DVRT >= 84.5 and Prestige_score < 65.5 and Prestige_score >= 22.5 and Prestige_score < 41.5 | 1 | 0.203320 |
| Educational_level = 9 and Sex!=(0) and DVRT >= 84.5 and Prestige_score < 65.5 and Prestige_score >= 22.5 and Prestige_score >= 41.5 and DVRT < 109.5 and DVRT >= 107.5 | 1 | 0.016410 |
| Educational_level = 9 and Sex!=(0) and DVRT >= 84.5 and Prestige_score < 65.5 and Prestige_score >= 22.5 and Prestige_score >= 41.5 and DVRT >= 109.5 | 1 | 0.085714 |
| Educational_level = 0 | 1 | 0.157895 |
| Educational_level = 9 and Sex!=(0) and DVRT >= 84.5 and Prestige_score >= 65.5 and Prestige_score >= 67.5 and DVRT < 119.5 | 1 | 0.035176 |
| Educational_level = 9 and Sex!=(0) and DVRT >= 84.5 and Prestige_score < 65.5 and Prestige_score >= 22.5 and Prestige_score >= 41.5 and DVRT < 109.5 and DVRT < 107.5 | 1 | 0.072464 |
| Educational_level = 9 and Sex!=(0) and DVRT >= 84.5 and Prestige_score < 65.5 and Prestige_score < 22.5 and DVRT >= 117.0 | 1 | 0.010309 |
| Educational_level = 1 | 1 | 0.030303 |
| Educational_level = 9 | 1 | 0.362824 |

## Ordered rules

### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Educational_level = 9 | 1 | 0.362824 |
| Educational_level = 0 | 1 | 0.157895 |
|  | 0 | 0.969697 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

educational_level|target
---|---
?|0
8|0
6|0
7|0
5|0
3|0
4|0
2|0
1|1
0|1
9|1

## JRip

Decision list:

rules | predicted class
---|---
(Educational_level = 9)|1 (114.0/0.0)
(Educational_level = 0)|1 (36.0/0.0)
|0 (198.0/6.0)


## J48 Decision Tree

* Educational_level = 0: 1 (28.44/0.44)
* Educational_level = 1: 1 (6.09/0.09)
* Educational_level = 2: 0 (15.23)
* Educational_level = 3: 0 (24.37)
* Educational_level = 4: 0 (28.44)
* Educational_level = 5: 0 (37.58)
* Educational_level = 6: 0 (25.39)
* Educational_level = 7: 0 (6.09)
* Educational_level = 8: 0 (5.08)
* Educational_level = 9: 1 (84.29/1.29)


## SimpleCart Decision Tree

		* Educational_level=(0)|(1)|(9)
	* Sex=(0): 1(86.0/0.0)
	* Sex!=(0)
		* DVRT < 84.5: 1(2.0/0.45)
		* DVRT >= 84.5
			* Prestige_score < 65.5
				* Prestige_score < 22.5
					* DVRT < 117.0: 1(3.29/0.45)
					* DVRT >= 117.0: 1(3.09/0.0)
				* Prestige_score >= 22.5
					* Prestige_score < 41.5: 1(30.76/0.0)
					* Prestige_score >= 41.5
						* DVRT < 109.5
							* DVRT < 107.5: 1(6.29/0.0)
							* DVRT >= 107.5: 1(1.29/0.45)
						* DVRT >= 109.5: 1(12.59/0.0)
			* Prestige_score >= 65.5
				* Prestige_score < 67.5: 0(0.45/0.02)
				* Prestige_score >= 67.5
					* DVRT < 119.5: 1(9.47/0.0)
					* DVRT >= 119.5: 1(1.15/0.45)
		* Educational_level!=(0)|(1)|(9): 0(189.72/0.0)


