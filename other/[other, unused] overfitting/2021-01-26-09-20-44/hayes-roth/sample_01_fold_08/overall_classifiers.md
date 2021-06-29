# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Age <= 3.5 and EducationalLevel <= 3.5 and MaritalStatus <= 3.5 | 1 | 0.344927 |
| EducationalLevel < 3.5 and Age < 3.5 and MaritalStatus < 3.5 and Age >= 1.5 and EducationalLevel >= 1.5 | 2 | 0.189356 |
| EducationalLevel >= 3.5 | 3 | 0.100775 |
| EducationalLevel < 3.5 and Age < 3.5 and MaritalStatus < 3.5 and Age < 1.5 and MaritalStatus >= 1.5 and EducationalLevel >= 1.5 and EducationalLevel < 2.5 | 2 | 0.103952 |
| EducationalLevel < 3.5 and Age < 3.5 and MaritalStatus < 3.5 and Age >= 1.5 and EducationalLevel < 1.5 and MaritalStatus >= 1.5 and MaritalStatus < 2.5 | 2 | 0.112245 |
| EducationalLevel < 3.5 and Age >= 3.5 | 3 | 0.072000 |
| Age <= 3.5 and EducationalLevel <= 3.5 and MaritalStatus > 3.5 | 3 | 0.049180 |
| EducationalLevel < 3.5 and Age < 3.5 and MaritalStatus < 3.5 and Age < 1.5 and MaritalStatus >= 1.5 and EducationalLevel >= 1.5 and EducationalLevel >= 2.5 and MaritalStatus < 2.5 and Hobby < 2.5 and Hobby >= 1.5 | 2 | 0.015152 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| EducationalLevel <= 3.5 and Age <= 3.5 and MaritalStatus <= 3.5 and Age <= 1.5 and MaritalStatus <= 1.5 | 1 | 0.141414 |
| EducationalLevel > 3.5 | 3 | 0.113043 |
| Age <= 3.5 and MaritalStatus <= 3.5 and EducationalLevel > 1.5 and EducationalLevel <= 2.5 and Age <= 2.5 and Age > 1.5 | 2 | 0.154930 |
| Age <= 3.5 and MaritalStatus <= 3.5 and EducationalLevel <= 1.5 and Age <= 1.5 | 1 | 0.152778 |
| Age <= 3.5 and MaritalStatus <= 3.5 and MaritalStatus <= 1.5 and EducationalLevel > 1.5 | 1 | 0.060794 |
| Age <= 3.5 and MaritalStatus <= 3.5 and MaritalStatus > 1.5 and MaritalStatus <= 2.5 and EducationalLevel <= 2.5 | 2 | 0.363636 |
| Age <= 3.5 and MaritalStatus <= 3.5 and MaritalStatus > 1.5 and MaritalStatus > 2.5 and Hobby <= 1.5 | 1 | 0.104701 |
| Age <= 3.5 and MaritalStatus <= 3.5 and MaritalStatus > 1.5 and MaritalStatus <= 2.5 | 2 | 0.123552 |
| Age <= 3.5 and MaritalStatus <= 3.5 and MaritalStatus <= 2.0 | 1 | 0.281955 |
| Age > 3.5 | 3 | 0.321429 |
| MaritalStatus <= 3.5 | 1 | 0.119617 |
|  | 3 | 0.300000 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| EducationalLevel >= 4 | 3 | 0.100775 |
| Age >= 4 | 3 | 0.072000 |
| MaritalStatus >= 4 | 3 | 0.049180 |
| Age >= 2 and EducationalLevel >= 2 and Age <= 2 | 2 | 0.202703 |
| MaritalStatus >= 2 and MaritalStatus <= 2 and Age >= 2 | 2 | 0.202703 |
| EducationalLevel >= 2 and MaritalStatus >= 2 and EducationalLevel <= 2 | 2 | 0.170020 |
|  | 1 | 0.808219 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

age|educationallevel|maritalstatus|class
---|---|---|---
(3.5-inf)|(3.5-inf)|(3.5-inf)|1
(-inf-3.5]|(3.5-inf)|(3.5-inf)|3
(3.5-inf)|(-inf-3.5]|(3.5-inf)|3
(-inf-3.5]|(-inf-3.5]|(3.5-inf)|3
(3.5-inf)|(3.5-inf)|(-inf-3.5]|3
(-inf-3.5]|(3.5-inf)|(-inf-3.5]|3
(-inf-3.5]|(-inf-3.5]|(-inf-3.5]|1
(3.5-inf)|(-inf-3.5]|(-inf-3.5]|3

## JRip

Decision list:

rules | predicted class
---|---
(EducationalLevel >= 4)|3 (13.0/0.0)
(Age >= 4)|3 (9.0/0.0)
(MaritalStatus >= 4)|3 (6.0/0.0)
(Age >= 2) and (EducationalLevel >= 2) and (Age <= 2)|2 (15.0/0.0)
(MaritalStatus >= 2) and (MaritalStatus <= 2) and (Age >= 2)|2 (15.0/0.0)
(EducationalLevel >= 2) and (MaritalStatus >= 2) and (EducationalLevel <= 2)|2 (14.0/1.0)
|1 (72.0/14.0)


## PART

Decision list:

rules | predicted class
---|---
EducationalLevel <= 3.5 AND Age <= 3.5 AND MaritalStatus <= 3.5 AND Age <= 1.5 AND MaritalStatus <= 1.5|1 (14.0)
EducationalLevel > 3.5|3 (13.0)
Age <= 3.5 AND MaritalStatus <= 3.5 AND EducationalLevel > 1.5 AND EducationalLevel <= 2.5 AND Age <= 2.5 AND Age > 1.5|2 (11.0)
Age <= 3.5 AND MaritalStatus <= 3.5 AND EducationalLevel <= 1.5 AND Age <= 1.5|1 (11.0)
Age <= 3.5 AND MaritalStatus <= 3.5 AND MaritalStatus <= 1.5 AND EducationalLevel > 1.5|1 (13.0/6.0)
Age <= 3.5 AND MaritalStatus <= 3.5 AND MaritalStatus > 1.5 AND MaritalStatus <= 2.5 AND EducationalLevel <= 2.5|2 (24.0)
Age <= 3.5 AND MaritalStatus <= 3.5 AND MaritalStatus > 1.5 AND MaritalStatus > 2.5 AND Hobby <= 1.5|1 (12.0/5.0)
Age <= 3.5 AND MaritalStatus <= 3.5 AND MaritalStatus > 1.5 AND MaritalStatus <= 2.5|2 (14.0/6.0)
Age <= 3.5 AND MaritalStatus <= 3.5 AND MaritalStatus <= 2.0|1 (9.0)
Age > 3.5|3 (9.0)
MaritalStatus <= 3.5|1 (8.0/3.0)
|3 (6.0)


## J48 Decision Tree

* EducationalLevel <= 3
	* Age <= 3
		* MaritalStatus <= 3
			* Age <= 1
				* MaritalStatus <= 1: 1 (14.0)
				* MaritalStatus > 1
					* EducationalLevel <= 1: 1 (11.0)
					* EducationalLevel > 1
						* MaritalStatus <= 2
							* EducationalLevel <= 2: 2 (11.0)
							* EducationalLevel > 2: 1 (11.0/5.0)
						* MaritalStatus > 2: 1 (3.0)
			* Age > 1
				* EducationalLevel <= 1
					* MaritalStatus <= 1: 1 (9.0)
					* MaritalStatus > 1
						* MaritalStatus <= 2: 2 (11.0)
						* MaritalStatus > 2: 1 (12.0/4.0)
				* EducationalLevel > 1
					* Age <= 2: 2 (15.0)
					* Age > 2
						* MaritalStatus <= 1: 1 (12.0/5.0)
						* MaritalStatus > 1: 2 (7.0/1.0)
		* MaritalStatus > 3: 3 (6.0)
	* Age > 3: 3 (9.0)
* EducationalLevel > 3: 3 (13.0)


## SimpleCart Decision Tree

* EducationalLevel < 3.5
	* Age < 3.5
		* MaritalStatus < 3.5
			* Age < 1.5
				* MaritalStatus < 1.5: 1(14.0/0.0)
				* MaritalStatus >= 1.5
					* EducationalLevel < 1.5: 1(11.0/0.0)
					* EducationalLevel >= 1.5
						* EducationalLevel < 2.5: 2(11.0/1.0)
						* EducationalLevel >= 2.5
							* MaritalStatus < 2.5
								* Hobby < 2.5
									* Hobby < 1.5: 1(3.0/2.0)
									* Hobby >= 1.5: 2(2.0/1.0)
								* Hobby >= 2.5: 1(2.0/1.0)
							* MaritalStatus >= 2.5: 1(2.0/0.0)
			* Age >= 1.5
				* EducationalLevel < 1.5
					* MaritalStatus < 1.5: 1(9.0/0.0)
					* MaritalStatus >= 1.5
						* MaritalStatus < 2.5: 2(11.0/0.0)
						* MaritalStatus >= 2.5: 1(8.0/4.0)
				* EducationalLevel >= 1.5: 2(26.0/8.0)
		* MaritalStatus >= 3.5: 3(6.0/0.0)
	* Age >= 3.5: 3(9.0/0.0)
* EducationalLevel >= 3.5: 3(13.0/0.0)


