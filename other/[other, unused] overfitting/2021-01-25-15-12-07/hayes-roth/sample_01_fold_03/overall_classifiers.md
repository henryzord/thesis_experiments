# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| MaritalStatus <= 3.5 and Age <= 3.5 and EducationalLevel <= 3.5 and EducationalLevel > 1.5 | 2 | 0.260166 |
| MaritalStatus <= 3.5 and Age <= 3.5 and EducationalLevel <= 3.5 and EducationalLevel <= 1.5 and MaritalStatus <= 1.5 | 1 | 0.140000 |
| MaritalStatus <= 3.5 and Age <= 3.5 and EducationalLevel <= 3.5 and EducationalLevel <= 1.5 and MaritalStatus > 1.5 and Age <= 1.5 | 1 | 0.122449 |
| Age < 3.5 and MaritalStatus < 3.5 and EducationalLevel < 3.5 and Age < 1.5 and EducationalLevel >= 1.5 and MaritalStatus < 1.5 | 1 | 0.122449 |
| Age >= 3.5 | 3 | 0.100775 |
| MaritalStatus <= 3.5 and Age <= 3.5 and EducationalLevel <= 3.5 and EducationalLevel <= 1.5 and MaritalStatus > 1.5 and Age > 1.5 | 2 | 0.112782 |
| Age < 3.5 and MaritalStatus < 3.5 and EducationalLevel < 3.5 and Age < 1.5 and EducationalLevel >= 1.5 and MaritalStatus >= 1.5 and EducationalLevel >= 2.5 | 1 | 0.046402 |
| Age < 3.5 and MaritalStatus >= 3.5 | 3 | 0.072000 |
| Age < 3.5 and MaritalStatus < 3.5 and EducationalLevel < 3.5 and Age >= 1.5 and EducationalLevel < 1.5 and MaritalStatus >= 1.5 and MaritalStatus >= 2.5 | 1 | 0.040909 |
| Age < 3.5 and MaritalStatus < 3.5 and EducationalLevel < 3.5 and Age >= 1.5 and EducationalLevel >= 1.5 and Age >= 2.5 and MaritalStatus < 1.5 | 1 | 0.037618 |
| Age < 3.5 and MaritalStatus < 3.5 and EducationalLevel >= 3.5 | 3 | 0.049180 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Age <= 3 and MaritalStatus <= 3 and EducationalLevel <= 3 and Age <= 1 and EducationalLevel <= 1 | 1 | 0.131313 |
| Age <= 3 and MaritalStatus <= 3 and EducationalLevel <= 3 and MaritalStatus > 1 and MaritalStatus <= 2 | 2 | 0.279231 |
| Age <= 3 and MaritalStatus <= 3 and EducationalLevel <= 3 and Age > 1 and EducationalLevel <= 1 | 1 | 0.230818 |
| Age <= 3 and MaritalStatus <= 1 and Age > 1 | 2 | 0.176674 |
| Age <= 1 and MaritalStatus <= 1 | 1 | 0.244898 |
| Age > 3 | 3 | 0.361111 |
| MaritalStatus > 3 | 3 | 0.281250 |
| EducationalLevel <= 3 | 2 | 0.234783 |
|  | 3 | 0.300000 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Age >= 4 | 3 | 0.100775 |
| MaritalStatus >= 4 | 3 | 0.072000 |
| EducationalLevel >= 4 | 3 | 0.049180 |
| Age >= 2 and EducationalLevel >= 2 and Age <= 2 | 2 | 0.226667 |
| MaritalStatus >= 2 and Age >= 2 and MaritalStatus <= 2 | 2 | 0.205479 |
| EducationalLevel >= 2 and MaritalStatus >= 2 and EducationalLevel <= 2 | 2 | 0.171429 |
| EducationalLevel >= 2 and Age >= 3 and EducationalLevel <= 2 | 2 | 0.047081 |
|  | 1 | 0.865672 |


# Text representation of classifiers as-is

## JRip

Decision list:

rules | predicted class
---|---
(Age >= 4)|3 (13.0/0.0)
(MaritalStatus >= 4)|3 (9.0/0.0)
(EducationalLevel >= 4)|3 (6.0/0.0)
(Age >= 2) and (EducationalLevel >= 2) and (Age <= 2)|2 (17.0/0.0)
(MaritalStatus >= 2) and (Age >= 2) and (MaritalStatus <= 2)|2 (15.0/0.0)
(EducationalLevel >= 2) and (MaritalStatus >= 2) and (EducationalLevel <= 2)|2 (12.0/0.0)
(EducationalLevel >= 2) and (Age >= 3) and (EducationalLevel <= 2)|2 (9.0/4.0)
|1 (63.0/9.0)


## PART

Decision list:

rules | predicted class
---|---
Age <= 3 AND MaritalStatus <= 3 AND EducationalLevel <= 3 AND Age <= 1 AND EducationalLevel <= 1|1 (13.0)
Age <= 3 AND MaritalStatus <= 3 AND EducationalLevel <= 3 AND MaritalStatus > 1 AND MaritalStatus <= 2|2 (39.0/6.0)
Age <= 3 AND MaritalStatus <= 3 AND EducationalLevel <= 3 AND Age > 1 AND EducationalLevel <= 1|1 (23.0/4.0)
Age <= 3 AND MaritalStatus <= 1 AND Age > 1|2 (23.0/7.0)
Age <= 1 AND MaritalStatus <= 1|1 (12.0)
Age > 3|3 (13.0)
MaritalStatus > 3|3 (9.0)
EducationalLevel <= 3|2 (7.0/2.0)
|3 (5.0)


## J48 Decision Tree

* MaritalStatus <= 3.5
	* Age <= 3.5
		* EducationalLevel <= 3.5
			* EducationalLevel <= 1.5
				* MaritalStatus <= 1.5: 1 (12.0)
				* MaritalStatus > 1.5
					* Age <= 1.5: 1 (9.0)
					* Age > 1.5: 2 (18.0/6.0)
			* EducationalLevel > 1.5: 2 (66.0/26.0)
		* EducationalLevel > 3.5: 3 (5.0)
	* Age > 3.5: 3 (8.0)
* MaritalStatus > 3.5: 3 (12.0)


## SimpleCart Decision Tree

* Age < 3.5
	* MaritalStatus < 3.5
		* EducationalLevel < 3.5
			* Age < 1.5
				* EducationalLevel < 1.5: 1(13.0/0.0)
				* EducationalLevel >= 1.5
					* MaritalStatus < 1.5: 1(12.0/0.0)
					* MaritalStatus >= 1.5
						* EducationalLevel < 2.5: 2(10.0/0.0)
						* EducationalLevel >= 2.5: 1(7.0/5.0)
			* Age >= 1.5
				* EducationalLevel < 1.5
					* MaritalStatus < 1.5: 1(13.0/0.0)
					* MaritalStatus >= 1.5
						* MaritalStatus < 2.5: 2(11.0/0.0)
						* MaritalStatus >= 2.5: 1(6.0/4.0)
				* EducationalLevel >= 1.5
					* Age < 2.5: 2(17.0/0.0)
					* Age >= 2.5
						* MaritalStatus < 1.5: 1(6.0/5.0)
						* MaritalStatus >= 1.5
							* EducationalLevel < 2.5: 2(4.0/0.0)
							* EducationalLevel >= 2.5: 2(2.0/1.0)
		* EducationalLevel >= 3.5: 3(6.0/0.0)
	* MaritalStatus >= 3.5: 3(9.0/0.0)
* Age >= 3.5: 3(13.0/0.0)


