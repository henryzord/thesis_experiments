# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Age <= 31.0 | 0 | 0.385223 |
| Age > 31.0 and Typea <= 68.0 and Famhist != Present and Ldl > 2.7 and Tobacco <= 8.0 | 0 | 0.321852 |
| Age > 31.0 and Typea <= 68.0 and Famhist = Present and Age > 50.0 | 1 | 0.114134 |
| Age > 31.0 and Typea <= 68.0 and Famhist = Present and Age <= 50.0 | 0 | 0.153682 |
| Age > 31.0 and Typea > 68.0 | 1 | 0.056138 |
| Age > 31.0 and Typea <= 68.0 and Famhist != Present and Ldl > 2.7 and Tobacco > 8.0 | 1 | 0.039983 |
| Age > 31.0 and Typea <= 68.0 and Famhist != Present and Ldl <= 2.7 | 0 | 0.077381 |
| Tobacco > 0.49 and Tobacco <= 8.04 and Adiposity > 21.83 and Famhist = Present and Alcohol = all | 1 | 0.098304 |
| Tobacco <= 0.49 and Adiposity > 21.83 and Famhist = Present and Alcohol = all | 0 | 0.099445 |
| Tobacco > 8.04 and Adiposity > 21.83 and Famhist = Present and Alcohol = all | 1 | 0.058275 |
| Tobacco > 0.49 and Tobacco <= 8.04 and Adiposity <= 21.83 and Famhist = Present and Alcohol = all | 0 | 0.067815 |
| Tobacco > 8.04 and Adiposity <= 21.83 and Famhist = Present and Alcohol = all | 0 | 0.009195 |
| Tobacco > 0.49 and Tobacco <= 8.04 and Adiposity > 21.83 and Famhist = Absent and Alcohol = all | 0 | 0.247815 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Age <= 31.5 and Tobacco <= 0.51 and Famhist = Absent | 0 | 0.290721 |
| Typea > 68.5 and Obesity > 26.495 | 1 | 0.066667 |
| Tobacco > 8.04 and Obesity <= 23.415 | 1 | 0.045455 |
| Age <= 50.5 and Famhist = Absent | 0 | 0.359101 |
| Age <= 38.5 and Ldl <= 5.205 and Adiposity > 12.165 | 0 | 0.136166 |
| Famhist = Absent | 0 | 0.182263 |
| Age > 50.5 and Ldl > 4.99 and Age <= 59.5 and Obesity <= 29.4 | 1 | 0.283951 |
|  | 0 | 0.376623 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Age >= 51 and Famhist = Present | 1 | 0.129801 |
| Tobacco >= 8 | 1 | 0.044161 |
| Age >= 32 and Typea >= 69 | 1 | 0.032584 |
|  | 0 | 0.828221 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

tobacco|adiposity|famhist|alcohol|chd
---|---|---|---|---
(-inf-0.49]|(21.83-inf)|absent|all|0
(8.04-inf)|(21.83-inf)|absent|all|1
(0.49-8.04]|(21.83-inf)|absent|all|0
(8.04-inf)|(-inf-21.83]|absent|all|1
(-inf-0.49]|(-inf-21.83]|absent|all|0
(0.49-8.04]|(-inf-21.83]|absent|all|0
(-inf-0.49]|(21.83-inf)|present|all|0
(8.04-inf)|(21.83-inf)|present|all|1
(0.49-8.04]|(21.83-inf)|present|all|1
(8.04-inf)|(-inf-21.83]|present|all|0
(-inf-0.49]|(-inf-21.83]|present|all|0
(0.49-8.04]|(-inf-21.83]|present|all|0

## JRip

Decision list:

rules | predicted class
---|---
(Age >= 51) and (Famhist = Present)|1 (80.0/24.0)
(Tobacco >= 8)|1 (36.0/14.0)
(Age >= 32) and (Typea >= 69)|1 (11.0/1.0)
|0 (287.0/56.0)


## PART

Decision list:

rules | predicted class
---|---
Age <= 31.5 AND Tobacco <= 0.51 AND Famhist = Absent|0 (61.0/1.0)
Typea > 68.5 AND Obesity > 26.495|1 (15.0)
Tobacco > 8.04 AND Obesity <= 23.415|1 (10.0)
Age <= 50.5 AND Famhist = Absent|0 (108.0/25.0)
Age <= 38.5 AND Ldl <= 5.205 AND Adiposity > 12.165|0 (25.0)
Famhist = Absent|0 (68.0/24.0)
Age > 50.5 AND Ldl > 4.99 AND Age <= 59.5 AND Obesity <= 29.4|1 (19.0)
|0 (108.0/50.0)


## J48 Decision Tree

* Age <= 31.0: 0 (68.0/4.0)
* Age > 31.0
	* Typea <= 68.0
		* Famhist = Present
			* Age <= 50.0: 0 (35.0/13.0)
			* Age > 50.0: 1 (44.0/12.0)
		* Famhist != Present
			* Ldl <= 2.7: 0 (12.0)
			* Ldl > 2.7
				* Tobacco <= 8.0: 0 (86.0/23.0)
				* Tobacco > 8.0: 1 (18.0/7.0)
	* Typea > 68.0: 1 (13.0)


