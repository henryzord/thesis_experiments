# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 0 | 0.652174 |
| Famhist = Present and Ldl > 5.17 | 1 | 0.126995 |
| Tobacco > 0.49 and Tobacco <= 8.04 and Famhist = Present and Typea > 68.5 and Age > 31.5 and Age <= 50.5 | 1 | 0.018182 |
| Tobacco > 0.49 and Tobacco <= 8.04 and Famhist = Absent and Typea > 68.5 and Age > 31.5 and Age <= 50.5 | 1 | 0.001852 |
| Tobacco > 8.04 and Famhist = Present and Typea <= 68.5 and Age > 50.5 | 1 | 0.035631 |
| Tobacco > 8.04 and Famhist = Absent and Typea <= 68.5 and Age > 50.5 | 1 | 0.032111 |
| Tobacco <= 0.49 and Famhist = Absent and Typea > 68.5 and Age > 31.5 and Age <= 50.5 | 1 | 0.007353 |
| Tobacco > 8.04 and Famhist = Absent and Typea <= 68.5 and Age > 31.5 and Age <= 50.5 | 1 | 0.007407 |
| Famhist = Present and Ldl <= 5.17 and Age > 48 and Age > 57 | 1 | 0.029805 |
| Tobacco > 0.49 and Tobacco <= 8.04 and Famhist = Present and Typea <= 68.5 and Age > 50.5 | 1 | 0.078739 |
| Tobacco > 8.04 and Famhist = Present and Typea <= 68.5 and Age > 31.5 and Age <= 50.5 | 1 | 0.003704 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Age <= 31.0 and Tobacco <= 0.5 | 0 | 0.333396 |
| Typea <= 68.0 and Famhist != Present and Tobacco <= 7.9 | 0 | 0.395207 |
| Typea <= 68.0 and Age > 50.0 and Ldl <= 7.67 and Tobacco > 0.81 and Famhist = Present | 1 | 0.261974 |
| Typea > 68.0 | 1 | 0.174006 |
| Ldl > 7.32 and Famhist = Present and Age > 50.0 | 1 | 0.091011 |
| Famhist = Present | 0 | 0.414973 |
|  | 1 | 0.877778 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Age >= 51 and Famhist = Present and Ldl >= 5.08 and Age <= 59 and Tobacco >= 4.18 | 1 | 0.075342 |
| Age >= 39 and Famhist = Present and Ldl >= 6.73 and Obesity <= 28.25 and Obesity >= 23.23 | 1 | 0.045936 |
| Tobacco >= 8.08 | 1 | 0.060333 |
| Age >= 32 and Typea >= 69 and Tobacco <= 6 | 1 | 0.039146 |
| Tobacco <= 4.6 and Age >= 45 and Alcohol <= 2.06 and Tobacco >= 1.75 and Typea >= 43 | 1 | 0.039146 |
| Tobacco >= 0.5 and Tobacco <= 2.78 and Obesity >= 28.11 | 1 | 0.026915 |
|  | 0 | 0.851735 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

tobacco|famhist|typea|age|chd
---|---|---|---|---
(0.49-8.04]|absent|(68.5-inf)|(50.5-inf)|0
(-inf-0.49]|present|(68.5-inf)|(50.5-inf)|0
(0.49-8.04]|present|(68.5-inf)|(50.5-inf)|0
(8.04-inf)|present|(68.5-inf)|(50.5-inf)|1
(8.04-inf)|absent|(-inf-68.5]|(50.5-inf)|1
(0.49-8.04]|absent|(-inf-68.5]|(50.5-inf)|0
(-inf-0.49]|absent|(-inf-68.5]|(50.5-inf)|0
(-inf-0.49]|absent|(68.5-inf)|(31.5-50.5]|1
(0.49-8.04]|absent|(68.5-inf)|(31.5-50.5]|1
(0.49-8.04]|present|(-inf-68.5]|(50.5-inf)|1
(8.04-inf)|present|(-inf-68.5]|(50.5-inf)|1
(-inf-0.49]|present|(-inf-68.5]|(50.5-inf)|0
(8.04-inf)|present|(68.5-inf)|(31.5-50.5]|0
(0.49-8.04]|present|(68.5-inf)|(31.5-50.5]|1
(-inf-0.49]|present|(68.5-inf)|(31.5-50.5]|0
(8.04-inf)|absent|(-inf-68.5]|(31.5-50.5]|1
(-inf-0.49]|absent|(-inf-68.5]|(31.5-50.5]|0
(0.49-8.04]|absent|(-inf-68.5]|(31.5-50.5]|0
(0.49-8.04]|absent|(68.5-inf)|(-inf-31.5]|0
(-inf-0.49]|absent|(68.5-inf)|(-inf-31.5]|0
(8.04-inf)|present|(-inf-68.5]|(31.5-50.5]|1
(-inf-0.49]|present|(-inf-68.5]|(31.5-50.5]|0
(0.49-8.04]|present|(-inf-68.5]|(31.5-50.5]|0
(-inf-0.49]|present|(68.5-inf)|(-inf-31.5]|0
(-inf-0.49]|absent|(-inf-68.5]|(-inf-31.5]|0
(0.49-8.04]|absent|(-inf-68.5]|(-inf-31.5]|0
(8.04-inf)|present|(-inf-68.5]|(-inf-31.5]|0
(0.49-8.04]|present|(-inf-68.5]|(-inf-31.5]|0
(-inf-0.49]|present|(-inf-68.5]|(-inf-31.5]|0

## JRip

Decision list:

rules | predicted class
---|---
(Age >= 51) and (Famhist = Present) and (Ldl >= 5.08) and (Age <= 59) and (Tobacco >= 4.18)|1 (22.0/0.0)
(Age >= 39) and (Famhist = Present) and (Ldl >= 6.73) and (Obesity <= 28.25) and (Obesity >= 23.23)|1 (13.0/0.0)
(Tobacco >= 8.08)|1 (43.0/16.0)
(Age >= 32) and (Typea >= 69) and (Tobacco <= 6)|1 (11.0/0.0)
(Tobacco <= 4.6) and (Age >= 45) and (Alcohol <= 2.06) and (Tobacco >= 1.75) and (Typea >= 43)|1 (11.0/0.0)
(Tobacco >= 0.5) and (Tobacco <= 2.78) and (Obesity >= 28.11)|1 (23.0/10.0)
|0 (291.0/47.0)


## PART

Decision list:

rules | predicted class
---|---
Age <= 31.0 AND Tobacco <= 0.5|0 (74.0/1.0)
Typea <= 68.0 AND Famhist != Present AND Tobacco <= 7.9|0 (151.0/35.0)
Typea <= 68.0 AND Age > 50.0 AND Ldl <= 7.67 AND Tobacco > 0.81 AND Famhist = Present|1 (53.0/15.0)
Typea > 68.0|1 (19.0/1.0)
Ldl > 7.32 AND Famhist = Present AND Age > 50.0|1 (9.0)
Famhist = Present|0 (81.0/26.0)
|1 (27.0/10.0)


## J48 Decision Tree

* Famhist = Present
	* Ldl <= 5.17
		* Age <= 48: 0 (23.0/3.0)
		* Age > 48
			* Age <= 57: 0 (11.0/5.0)
			* Age > 57: 1 (11.0/4.0)
	* Ldl > 5.17: 1 (35.0/7.0)
* Famhist = Absent: 0 (127.0/29.0)


