# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Positive < 8.5 | negative | 0.699714 |
| Positive > 2.0 and Age > 43.0 and Positive > 10.0 | positive | 0.062893 |
| Age = all and Positive > 4.5 | negative | 0.243056 |
| Positive > 2.0 and Age > 43.0 and Positive <= 10.0 and Age <= 46.0 | positive | 0.015610 |
| Positive >= 8.5 and Age >= 45.5 and Year < 65.5 and Age < 53.5 | positive | 0.047170 |
| Positive >= 8.5 and Age >= 45.5 and Year < 65.5 and Age >= 53.5 | positive | 0.030340 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Positive <= 4.0 and Year > 59.0 and Age > 38.0 and Year <= 61.0 and Age <= 59.0 | negative | 0.242105 |
| Positive <= 2.0 and Age <= 38.0 and Age > 35.0 | negative | 0.132530 |
| Positive <= 2.0 and Age > 47.0 and Year > 65.0 and Year <= 67.0 | negative | 0.250000 |
| Positive <= 8.0 and Age <= 40.0 and Positive > 0.0 | negative | 0.132530 |
| Positive <= 1.0 and Age > 50.0 and Age <= 59.0 and Year <= 64.0 | negative | 0.208791 |
| Positive <= 0.0 and Year <= 67.0 and Age > 62.0 and Year > 60.0 and Age <= 68.0 | negative | 0.111111 |
| Positive <= 8.0 and Positive <= 0.0 and Year <= 67.0 and Age <= 40.0 | negative | 0.070707 |
| Positive <= 8.0 and Year > 58.0 and Positive <= 0.0 and Year > 67.0 | negative | 0.111111 |
| Positive <= 8.0 and Year <= 64.0 and Positive > 5.0 | negative | 0.093211 |
| Positive <= 4.0 and Year <= 67.0 and Age <= 50.0 and Positive <= 2.0 and Year <= 63.0 and Age > 47.0 | negative | 0.078526 |
| Age <= 44.0 and Positive <= 15.0 and Positive <= 2.0 and Year > 63.0 | positive | 0.044226 |
| Age <= 44.0 and Positive <= 15.0 and Year > 59.0 and Age <= 41.0 | negative | 0.085069 |
| Positive > 4.0 and Positive <= 24.0 and Age > 45.0 and Age > 51.0 and Year <= 62.0 | positive | 0.100872 |
| Age <= 44.0 and Year <= 61.0 | negative | 0.043860 |
| Age <= 43.0 | negative | 0.090000 |
| Age <= 53.0 and Positive > 0.0 and Age > 50.0 and Year <= 62.0 | positive | 0.090226 |
| Positive <= 4.0 and Year > 58.0 and Year <= 64.0 and Age > 51.0 and Age > 63.0 | negative | 0.097222 |
| Positive > 4.0 and Age <= 53.0 and Age <= 47.0 | positive | 0.132353 |
| Positive <= 5.0 and Age <= 61.0 and Year <= 64.0 and Age <= 51.0 | negative | 0.067542 |
| Age <= 53.0 and Positive <= 5.0 and Positive > 0.0 | positive | 0.106061 |
| Year <= 58.0 | positive | 0.124031 |
| Positive <= 5.0 and Year > 64.0 and Age > 59.0 | positive | 0.069444 |
| Positive <= 5.0 and Age > 53.0 | negative | 0.395062 |
| Positive > 3.0 and Age <= 56.0 and Year <= 65.0 | positive | 0.136364 |
| Positive > 3.0 and Year <= 66.0 | negative | 0.418803 |
| Positive <= 3.0 | negative | 0.147929 |
|  | positive | 0.800000 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Positive >= 5 and Age >= 43 | positive | 0.090546 |
|  | negative | 0.838174 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

age|positive|survival
---|---|---
all|(4.5-inf)|negative
all|(-inf-4.5]|negative

## JRip

Decision list:

rules | predicted class
---|---
(Positive >= 5) and (Age >= 43)|positive (57.0/24.0)
|negative (217.0/39.0)


## PART

Decision list:

rules | predicted class
---|---
Positive <= 4.0 AND Year > 59.0 AND Age > 38.0 AND Year <= 61.0 AND Age <= 59.0|negative (23.0)
Positive <= 2.0 AND Age <= 38.0 AND Age > 35.0|negative (11.0)
Positive <= 2.0 AND Age > 47.0 AND Year > 65.0 AND Year <= 67.0|negative (24.0)
Positive <= 8.0 AND Age <= 40.0 AND Positive > 0.0|negative (11.0)
Positive <= 1.0 AND Age > 50.0 AND Age <= 59.0 AND Year <= 64.0|negative (19.0)
Positive <= 0.0 AND Year <= 67.0 AND Age > 62.0 AND Year > 60.0 AND Age <= 68.0|negative (9.0)
Positive <= 8.0 AND Positive <= 0.0 AND Year <= 67.0 AND Age <= 40.0|negative (9.0/2.0)
Positive <= 8.0 AND Year > 58.0 AND Positive <= 0.0 AND Year > 67.0|negative (9.0)
Positive <= 8.0 AND Year <= 64.0 AND Positive > 5.0|negative (11.0/2.0)
Positive <= 4.0 AND Year <= 67.0 AND Age <= 50.0 AND Positive <= 2.0 AND Year <= 63.0 AND Age > 47.0|negative (8.0/1.0)
Age <= 44.0 AND Positive <= 15.0 AND Positive <= 2.0 AND Year > 63.0|positive (10.0/5.0)
Age <= 44.0 AND Positive <= 15.0 AND Year > 59.0 AND Age <= 41.0|negative (6.0/1.0)
Positive > 4.0 AND Positive <= 24.0 AND Age > 45.0 AND Age > 51.0 AND Year <= 62.0|positive (11.0/2.0)
Age <= 44.0 AND Year <= 61.0|negative (9.0/4.0)
Age <= 43.0|negative (6.0)
Age <= 53.0 AND Positive > 0.0 AND Age > 50.0 AND Year <= 62.0|positive (6.0)
Positive <= 4.0 AND Year > 58.0 AND Year <= 64.0 AND Age > 51.0 AND Age > 63.0|negative (9.0/2.0)
Positive > 4.0 AND Age <= 53.0 AND Age <= 47.0|positive (8.0/3.0)
Positive <= 5.0 AND Age <= 61.0 AND Year <= 64.0 AND Age <= 51.0|negative (9.0/3.0)
Age <= 53.0 AND Positive <= 5.0 AND Positive > 0.0|positive (8.0/3.0)
Year <= 58.0|positive (12.0/4.0)
Positive <= 5.0 AND Year > 64.0 AND Age > 59.0|positive (9.0/4.0)
Positive <= 5.0 AND Age > 53.0|negative (8.0)
Positive > 3.0 AND Age <= 56.0 AND Year <= 65.0|positive (7.0/1.0)
Positive > 3.0 AND Year <= 66.0|negative (10.0/3.0)
Positive <= 3.0|negative (6.0/1.0)
|positive (6.0/2.0)


## J48 Decision Tree

* Positive <= 2.0: negative (144.0/23.0)
* Positive > 2.0
	* Age <= 43.0: negative (19.0/3.0)
	* Age > 43.0
		* Positive <= 10.0
			* Age <= 46.0: positive (4.0/1.0)
			* Age > 46.0: negative (38.0/14.0)
		* Positive > 10.0: positive (24.0/7.0)


## SimpleCart Decision Tree

* Positive < 8.5: negative(183.0/46.0)
* Positive >= 8.5
	* Age < 45.5: negative(9.0/4.0)
	* Age >= 45.5
		* Year < 65.5
			* Age < 53.5: positive(10.0/0.0)
			* Age >= 53.5: positive(10.0/6.0)
		* Year >= 65.5: negative(4.0/2.0)


