# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Age < 3.5 | 1 | 0.361682 |
| Age <= 3.0 and MaritalStatus <= 3.0 and EducationalLevel <= 3.0 and Age > 1.0 and EducationalLevel > 1.0 and Age <= 2.0 | 2 | 0.165049 |
| Age <= 3.0 and MaritalStatus <= 3.0 and EducationalLevel <= 3.0 and Age > 1.0 and EducationalLevel <= 1.0 and MaritalStatus > 1.0 and MaritalStatus <= 2.0 | 2 | 0.113402 |
| Age > 3.0 | 3 | 0.100775 |
| Age <= 3.0 and MaritalStatus <= 3.0 and EducationalLevel <= 3.0 and Age <= 1.0 and EducationalLevel > 1.0 and MaritalStatus > 1.0 and EducationalLevel <= 2.0 | 2 | 0.104167 |
| Age <= 3.0 and MaritalStatus > 3.0 | 3 | 0.072000 |
| Age <= 3.0 and MaritalStatus <= 3.0 and EducationalLevel <= 3.0 and Age > 1.0 and EducationalLevel > 1.0 and Age > 2.0 and MaritalStatus > 1.0 and EducationalLevel <= 2.0 | 2 | 0.044444 |
| Age <= 3.0 and MaritalStatus <= 3.0 and EducationalLevel > 3.0 | 3 | 0.049180 |
| Age <= 3.0 and MaritalStatus <= 3.0 and EducationalLevel <= 3.0 and Age > 1.0 and EducationalLevel > 1.0 and Age > 2.0 and MaritalStatus <= 1.0 and EducationalLevel <= 2.0 and Hobby > 2.0 | 2 | 0.015326 |
| Age <= 3.0 and MaritalStatus <= 3.0 and EducationalLevel <= 3.0 and Age <= 1.0 and EducationalLevel > 1.0 and MaritalStatus > 1.0 and EducationalLevel > 2.0 and Hobby > 1.0 and Hobby <= 2.0 | 2 | 0.015326 |
| Age <= 3.0 and MaritalStatus <= 3.0 and EducationalLevel <= 3.0 and Age > 1.0 and EducationalLevel > 1.0 and Age > 2.0 and MaritalStatus > 1.0 and EducationalLevel > 2.0 | 2 | 0.015326 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Age <= 3 and MaritalStatus <= 3 and EducationalLevel <= 3 and Age <= 1 and EducationalLevel <= 1 | 1 | 0.131313 |
| Age <= 3 and MaritalStatus <= 3 and EducationalLevel <= 3 and MaritalStatus > 1 and MaritalStatus <= 2 | 2 | 0.279231 |
| Age <= 3 and MaritalStatus <= 3 and EducationalLevel <= 3 and Age > 1 and EducationalLevel <= 1 | 1 | 0.230818 |
| Age <= 3 and EducationalLevel <= 3 and MaritalStatus <= 3 and Age > 1 and Age <= 2 | 2 | 0.250000 |
| MaritalStatus > 1 | 3 | 0.348485 |
| Age <= 3 | 1 | 0.662745 |
|  | 3 | 0.416667 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Age >= 4 | 3 | 0.100775 |
| MaritalStatus >= 4 | 3 | 0.072000 |
| Age >= 2 and MaritalStatus >= 2 and MaritalStatus <= 2 and EducationalLevel <= 3 | 2 | 0.219512 |
| EducationalLevel >= 2 and EducationalLevel <= 2 and MaritalStatus >= 2 | 2 | 0.179487 |
| EducationalLevel >= 2 and Age >= 2 and EducationalLevel <= 2 and Age <= 2 | 2 | 0.135135 |
|  | 1 | 0.725000 |


# Text representation of classifiers as-is

## JRip

Decision list:

rules | predicted class
---|---
(Age >= 4)|3 (13.0/0.0)
(MaritalStatus >= 4)|3 (9.0/0.0)
(Age >= 2) and (MaritalStatus >= 2) and (MaritalStatus <= 2) and (EducationalLevel <= 3)|2 (18.0/0.0)
(EducationalLevel >= 2) and (EducationalLevel <= 2) and (MaritalStatus >= 2)|2 (14.0/0.0)
(EducationalLevel >= 2) and (Age >= 2) and (EducationalLevel <= 2) and (Age <= 2)|2 (10.0/0.0)
|1 (80.0/22.0)


## PART

Decision list:

rules | predicted class
---|---
Age <= 3 AND MaritalStatus <= 3 AND EducationalLevel <= 3 AND Age <= 1 AND EducationalLevel <= 1|1 (13.0)
Age <= 3 AND MaritalStatus <= 3 AND EducationalLevel <= 3 AND MaritalStatus > 1 AND MaritalStatus <= 2|2 (39.0/6.0)
Age <= 3 AND MaritalStatus <= 3 AND EducationalLevel <= 3 AND Age > 1 AND EducationalLevel <= 1|1 (23.0/4.0)
Age <= 3 AND EducationalLevel <= 3 AND MaritalStatus <= 3 AND Age > 1 AND Age <= 2|2 (14.0)
MaritalStatus > 1|3 (27.0/4.0)
Age <= 3|1 (24.0/6.0)
|3 (4.0)


## J48 Decision Tree

* Age <= 3.0
	* MaritalStatus <= 3.0
		* EducationalLevel <= 3.0
			* Age <= 1.0
				* EducationalLevel <= 1.0: 1 (13.0)
				* EducationalLevel > 1.0
					* MaritalStatus <= 1.0: 1 (12.0)
					* MaritalStatus > 1.0
						* EducationalLevel <= 2.0: 2 (10.0)
						* EducationalLevel > 2.0
							* Hobby <= 1.0: 1 (6.0/2.0)
							* Hobby > 1.0
								* Hobby <= 2.0: 2 (3.0/1.0)
								* Hobby > 2.0: 1 (3.0/1.0)
			* Age > 1.0
				* EducationalLevel <= 1.0
					* MaritalStatus <= 1.0: 1 (13.0)
					* MaritalStatus > 1.0
						* MaritalStatus <= 2.0: 2 (11.0)
						* MaritalStatus > 2.0
							* Hobby <= 2.0
								* Hobby <= 1.0: 1 (5.0/2.0)
								* Hobby > 1.0: 1 (3.0/1.0)
							* Hobby > 2.0: 1 (2.0/1.0)
				* EducationalLevel > 1.0
					* Age <= 2.0: 2 (17.0)
					* Age > 2.0
						* MaritalStatus <= 1.0
							* EducationalLevel <= 2.0
								* Hobby <= 2.0: 1 (6.0/3.0)
								* Hobby > 2.0: 2 (3.0/1.0)
							* EducationalLevel > 2.0: 1 (2.0)
						* MaritalStatus > 1.0
							* EducationalLevel <= 2.0: 2 (4.0)
							* EducationalLevel > 2.0: 2 (3.0/1.0)
		* EducationalLevel > 3.0: 3 (6.0)
	* MaritalStatus > 3.0: 3 (9.0)
* Age > 3.0: 3 (13.0)


## SimpleCart Decision Tree

* Age < 3.5: 1(58.0/73.0)
* Age >= 3.5: 3(13.0/0.0)


