# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 0 | 0.542857 |
| Educational_level = 9 and Prestige_score < 73.0 and Sex!=(0) and DVRT < 109.5 and DVRT >= 106.5 | 1 | 0.056053 |
| Educational_level = 0 | 1 | 0.184549 |
| Educational_level = 9 and Prestige_score < 73.0 and Sex!=(0) and DVRT < 109.5 and DVRT < 106.5 | 1 | 0.221311 |
| Educational_level = 9 and Prestige_score < 73.0 and Sex!=(0) and DVRT >= 109.5 | 1 | 0.177489 |
| Educational_level = 9 | 1 | 0.369026 |
| Educational_level = 1 | 1 | 0.015544 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Educational_level = 5 | 0 | 0.241706 |
| Educational_level = 4 | 0 | 0.191919 |
| Educational_level = 3 | 0 | 0.175258 |
| Educational_level = 6 | 0 | 0.130435 |
| Educational_level = 0 and Sex = 1 | 1 | 0.348485 |
| Educational_level = 9 and Sex = 0 | 1 | 0.598131 |
| Educational_level = 9 | 1 | 0.524109 |
| Educational_level = 2 | 0 | 0.488889 |
| Educational_level = 0 | 1 | 0.487805 |
| Type_school = 2 | 0 | 0.785714 |
|  | 0 | 0.769231 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Educational_level = 9 | 1 | 0.369026 |
| Educational_level = 0 | 1 | 0.184549 |
|  | 0 | 0.984456 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

educational_level|target
---|---
?|0
1|1
0|1
9|1
8|0
4|0
6|0
7|0
3|0
2|0
5|0

## JRip

Decision list:

rules | predicted class
---|---
(Educational_level = 9)|1 (114.0/0.0)
(Educational_level = 0)|1 (43.0/0.0)
|0 (193.0/3.0)


## PART

Decision list:

rules | predicted class
---|---
Educational_level = 5|0 (51.44)
Educational_level = 4|0 (38.33)
Educational_level = 3|0 (34.29)
Educational_level = 6|0 (24.21)
Educational_level = 0 AND Sex = 1|1 (23.37/0.37)
Educational_level = 9 AND Sex = 0|1 (64.0)
Educational_level = 9|1 (50.6/0.6)
Educational_level = 2|0 (22.26)
Educational_level = 0|1 (20.24/0.24)
Type_school = 2|0 (11.0)
|0 (10.25/3.0)


## SimpleCart Decision Tree

		* Educational_level=(0)|(1)|(9)
	* Prestige_score < 73.0
		* Sex=(0): 1(83.78/0.0)
		* Sex!=(0)
			* DVRT < 109.5
				* DVRT < 106.5: 1(19.94/0.0)
				* DVRT >= 106.5: 1(7.94/0.92)
			* DVRT >= 109.5: 1(39.94/0.0)
	* Prestige_score >= 73.0: 1(8.38/0.46)
		* Educational_level!=(0)|(1)|(9): 0(188.61/0.0)


