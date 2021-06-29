# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 0 | 0.652174 |
| Age > 37.0 and Ldl > 4.12 and Typea > 67.0 | 1 | 0.036012 |
| Age > 37.0 and Ldl > 4.12 and Typea <= 67.0 and Famhist = Present and Sbp <= 162.0 and Tobacco > 0.04 and Obesity <= 30.42 and Sbp > 121.0 and Ldl > 5.05 | 1 | 0.071637 |
| Tobacco > 0.49 and Tobacco <= 8.04 and Famhist = Present and Typea = all and Obesity = all and Alcohol = all and Age > 50.5 | 1 | 0.084483 |
| Tobacco > 8.04 and Famhist = Absent and Typea = all and Obesity = all and Alcohol = all and Age > 50.5 | 1 | 0.043382 |
| Age > 37.0 and Ldl > 4.12 and Typea <= 67.0 and Famhist = Present and Sbp > 162.0 | 1 | 0.039420 |
| Age >= 49.5 and Tobacco >= 7.470000000000001 | 1 | 0.089363 |
| Tobacco > 8.04 and Famhist = Absent and Typea = all and Obesity = all and Alcohol = all and Age > 30.5 and Age <= 50.5 | 1 | 0.007407 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Age <= 30.0 and Tobacco <= 0.5 and Famhist != Present | 0 | 0.287211 |
| Tobacco > 8.0 and Typea <= 47.0 and Sbp <= 132.0 | 1 | 0.028226 |
| Age <= 49.0 and Famhist != Present and Typea <= 64.0 and Sbp <= 124.0 and Sbp > 114.0 | 0 | 0.110731 |
| Ldl > 8.13 and Age > 52.0 | 1 | 0.053922 |
| Famhist != Present and Tobacco <= 7.6 and Typea <= 65.0 | 0 | 0.365128 |
| Tobacco <= 0.18 and Age > 31.0 and Typea <= 54.0 | 0 | 0.077665 |
| Age > 50.0 and Famhist != Present and Ldl > 4.94 | 0 | 0.014637 |
| Age > 50.0 and Famhist = Present and Ldl > 4.99 | 1 | 0.225225 |
| Famhist != Present and Age <= 50.0 | 1 | 0.193164 |
| Famhist = Present and Age <= 30.0 and Tobacco <= 0.31 | 0 | 0.158537 |
| Famhist = Present | 0 | 0.412071 |
|  | 1 | 0.862500 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Age >= 51 and Tobacco >= 7.6 | 1 | 0.090037 |
| Famhist = Present and Age >= 51 | 1 | 0.083682 |
|  | 0 | 0.789474 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

tobacco|famhist|typea|obesity|alcohol|age|chd
---|---|---|---|---|---|---
(8.04-inf)|absent|all|all|all|(50.5-inf)|1
(-inf-0.49]|absent|all|all|all|(50.5-inf)|0
(0.49-8.04]|absent|all|all|all|(50.5-inf)|0
(8.04-inf)|present|all|all|all|(50.5-inf)|1
(-inf-0.49]|present|all|all|all|(50.5-inf)|0
(0.49-8.04]|present|all|all|all|(50.5-inf)|1
(8.04-inf)|absent|all|all|all|(30.5-50.5]|1
(0.49-8.04]|absent|all|all|all|(30.5-50.5]|0
(-inf-0.49]|absent|all|all|all|(30.5-50.5]|0
(8.04-inf)|present|all|all|all|(30.5-50.5]|0
(-inf-0.49]|present|all|all|all|(30.5-50.5]|0
(0.49-8.04]|present|all|all|all|(30.5-50.5]|0
(0.49-8.04]|absent|all|all|all|(-inf-30.5]|0
(-inf-0.49]|absent|all|all|all|(-inf-30.5]|0
(0.49-8.04]|present|all|all|all|(-inf-30.5]|0
(-inf-0.49]|present|all|all|all|(-inf-30.5]|0

## JRip

Decision list:

rules | predicted class
---|---
(Age >= 51) and (Tobacco >= 7.6)|1 (41.0/8.0)
(Famhist = Present) and (Age >= 51)|1 (61.0/22.0)
|0 (312.0/72.0)


## PART

Decision list:

rules | predicted class
---|---
Age <= 30.0 AND Tobacco <= 0.5 AND Famhist != Present|0 (60.0/1.0)
Tobacco > 8.0 AND Typea <= 47.0 AND Sbp <= 132.0|1 (8.0/1.0)
Age <= 49.0 AND Famhist != Present AND Typea <= 64.0 AND Sbp <= 124.0 AND Sbp > 114.0|0 (18.0)
Ldl > 8.13 AND Age > 52.0|1 (11.0)
Famhist != Present AND Tobacco <= 7.6 AND Typea <= 65.0|0 (117.0/27.0)
Tobacco <= 0.18 AND Age > 31.0 AND Typea <= 54.0|0 (15.0/2.0)
Age > 50.0 AND Famhist != Present AND Ldl > 4.94|0 (10.0/5.0)
Age > 50.0 AND Famhist = Present AND Ldl > 4.99|1 (37.0/7.0)
Famhist != Present AND Age <= 50.0|1 (21.0/10.0)
Famhist = Present AND Age <= 30.0 AND Tobacco <= 0.31|0 (13.0)
Famhist = Present|0 (96.0/42.0)
|1 (8.0)


## J48 Decision Tree

* Age <= 37.0: 0 (79.0/10.0)
* Age > 37.0
	* Ldl <= 4.12: 0 (38.0/9.0)
	* Ldl > 4.12
		* Typea <= 67.0
			* Famhist = Present
				* Sbp <= 162.0
					* Tobacco <= 0.04: 0 (6.0/1.0)
					* Tobacco > 0.04
						* Obesity <= 30.42
							* Sbp <= 121.0: 0 (3.0/1.0)
							* Sbp > 121.0
								* Ldl <= 5.05: 0 (7.0/3.0)
								* Ldl > 5.05: 1 (20.0/1.0)
						* Obesity > 30.42: 0 (4.0/1.0)
				* Sbp > 162.0: 1 (6.0)
			* Famhist != Present: 0 (39.0/17.0)
		* Typea > 67.0: 1 (5.0)


## SimpleCart Decision Tree

* Age < 49.5: 0(198.0/54.0)
* Age >= 49.5
	* Tobacco < 7.470000000000001
		* Famhist=(Present): 1(40.0/24.0)
		* Famhist!=(Present): 0(38.0/16.0)
	* Tobacco >= 7.470000000000001: 1(34.0/10.0)


