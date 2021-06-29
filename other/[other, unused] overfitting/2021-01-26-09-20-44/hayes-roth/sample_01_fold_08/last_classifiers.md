# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 1 | 0.409722 |
| EducationalLevel < 3.5 and Age < 3.5 and MaritalStatus < 3.5 and Age >= 1.5 and EducationalLevel >= 1.5 | 2 | 0.189356 |
| EducationalLevel >= 3.5 | 3 | 0.100775 |
| EducationalLevel < 3.5 and Age < 3.5 and MaritalStatus < 3.5 and Age >= 1.5 and EducationalLevel < 1.5 and MaritalStatus >= 1.5 and MaritalStatus < 2.5 | 2 | 0.112245 |
| MaritalStatus <= 3 and Age <= 3 and EducationalLevel <= 3 and EducationalLevel > 1 and Age <= 1 and MaritalStatus > 1 and EducationalLevel <= 2 | 2 | 0.103952 |
| EducationalLevel < 3.5 and Age >= 3.5 | 3 | 0.072000 |
| Age <= 3.5 and EducationalLevel <= 3.5 and MaritalStatus > 3.5 | 3 | 0.049180 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| EducationalLevel <= 3 and Age <= 3 and MaritalStatus <= 3 and Age <= 1 and MaritalStatus <= 1 | 1 | 0.141414 |
| EducationalLevel <= 3 and Age <= 3 and MaritalStatus <= 3 and EducationalLevel > 1 and EducationalLevel <= 2 | 2 | 0.265030 |
| EducationalLevel <= 3 and Age <= 3 and MaritalStatus <= 3 and MaritalStatus > 1 and Age <= 1 | 1 | 0.231884 |
| EducationalLevel <= 3 and Age <= 3 and MaritalStatus <= 3 and MaritalStatus > 1 and MaritalStatus > 2 | 1 | 0.094737 |
| MaritalStatus > 1 and MaritalStatus <= 2 and EducationalLevel <= 3 | 2 | 0.281811 |
| MaritalStatus > 1 | 3 | 0.429825 |
| Age <= 3 and EducationalLevel <= 2 | 1 | 0.453704 |
|  | 3 | 0.437500 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| EducationalLevel >= 4 | 3 | 0.100775 |
| Age >= 4 | 3 | 0.072000 |
| MaritalStatus >= 4 | 3 | 0.049180 |
| Age >= 2 and EducationalLevel >= 2 and Age <= 2 | 2 | 0.202703 |
| MaritalStatus >= 2 and Age >= 2 and MaritalStatus <= 2 | 2 | 0.202703 |
| MaritalStatus >= 2 and EducationalLevel >= 2 and EducationalLevel <= 2 | 2 | 0.170020 |
|  | 1 | 0.808219 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

age|educationallevel|maritalstatus|class
---|---|---|---
(3.5-inf)|(3.5-inf)|(3.5-inf)|1
(-inf-3.5]|(3.5-inf)|(3.5-inf)|3
(3.5-inf)|(-inf-3.5]|(3.5-inf)|3
(-inf-3.5]|(-inf-3.5]|(3.5-inf)|3
(3.5-inf)|(3.5-inf)|(-inf-3.5]|3
(-inf-3.5]|(3.5-inf)|(-inf-3.5]|3
(3.5-inf)|(-inf-3.5]|(-inf-3.5]|3
(-inf-3.5]|(-inf-3.5]|(-inf-3.5]|1

## JRip

Decision list:

rules | predicted class
---|---
(EducationalLevel >= 4)|3 (13.0/0.0)
(Age >= 4)|3 (9.0/0.0)
(MaritalStatus >= 4)|3 (6.0/0.0)
(Age >= 2) and (EducationalLevel >= 2) and (Age <= 2)|2 (15.0/0.0)
(MaritalStatus >= 2) and (Age >= 2) and (MaritalStatus <= 2)|2 (15.0/0.0)
(MaritalStatus >= 2) and (EducationalLevel >= 2) and (EducationalLevel <= 2)|2 (14.0/1.0)
|1 (72.0/14.0)


## PART

Decision list:

rules | predicted class
---|---
EducationalLevel <= 3 AND Age <= 3 AND MaritalStatus <= 3 AND Age <= 1 AND MaritalStatus <= 1|1 (14.0)
EducationalLevel <= 3 AND Age <= 3 AND MaritalStatus <= 3 AND EducationalLevel > 1 AND EducationalLevel <= 2|2 (37.0/6.0)
EducationalLevel <= 3 AND Age <= 3 AND MaritalStatus <= 3 AND MaritalStatus > 1 AND Age <= 1|1 (24.0/5.0)
EducationalLevel <= 3 AND Age <= 3 AND MaritalStatus <= 3 AND MaritalStatus > 1 AND MaritalStatus > 2|1 (15.0/6.0)
MaritalStatus > 1 AND MaritalStatus <= 2 AND EducationalLevel <= 3|2 (16.0/2.0)
MaritalStatus > 1|3 (19.0)
Age <= 3 AND EducationalLevel <= 2|1 (9.0)
|3 (10.0/3.0)


## J48 Decision Tree

* MaritalStatus <= 3
	* Age <= 3
		* EducationalLevel <= 3
			* EducationalLevel <= 1
				* Age <= 1: 1 (9.0)
				* Age > 1
					* MaritalStatus <= 1: 1 (7.0)
					* MaritalStatus > 1
						* MaritalStatus <= 2: 2 (7.0)
						* MaritalStatus > 2: 1 (7.0/2.0)
			* EducationalLevel > 1
				* Age <= 1
					* MaritalStatus <= 1: 1 (8.0)
					* MaritalStatus > 1
						* EducationalLevel <= 2: 2 (8.0/1.0)
						* EducationalLevel > 2: 1 (9.0/4.0)
				* Age > 1
					* Age <= 2: 2 (9.0)
					* Age > 2
						* EducationalLevel <= 2: 2 (10.0/3.0)
						* EducationalLevel > 2: 1 (4.0/2.0)
		* EducationalLevel > 3: 3 (3.0)
	* Age > 3: 3 (6.0)
* MaritalStatus > 3: 3 (9.0)


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
						* EducationalLevel >= 2.5: 1(8.0/5.0)
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


