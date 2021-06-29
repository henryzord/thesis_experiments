# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | negative | 0.737226 |
| Positive > 4.0 and Age > 42.0 and Year <= 65.0 and Positive > 9.0 and Age <= 53.0 | positive | 0.044112 |
| Positive >= 4.5 and Age >= 42.5 | positive | 0.085934 |
| Year = all and Positive > 4.5 | positive | 0.082531 |
| Positive < 4.5 and Positive >= 1.5 and Age >= 50.5 and Age < 54.0 | positive | 0.023786 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Positive <= 4 and Positive <= 1 and Positive <= 0 | negative | 0.568894 |
| Age > 42 and Positive <= 4 | negative | 0.321076 |
| Age > 42 | positive | 0.529199 |
|  | negative | 0.857143 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Positive >= 2 and Age >= 44 | positive | 0.107901 |
|  | negative | 0.874459 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

year|positive|survival
---|---|---
all|(4.5-inf)|positive
all|(-inf-4.5]|negative

## JRip

Decision list:

rules | predicted class
---|---
(Positive >= 2) and (Age >= 44)|positive (84.0/41.0)
|negative (190.0/29.0)


## PART

Decision list:

rules | predicted class
---|---
Positive <= 4 AND Positive <= 1 AND Positive <= 0|negative (125.0/18.0)
Age > 42 AND Positive <= 4|negative (67.0/20.0)
Age > 42|positive (53.0/22.0)
|negative (29.0/3.0)


## J48 Decision Tree

* Positive <= 4.0
	* Age <= 40.0
		* Positive <= 0.0
			* Age <= 37.0: negative (10.0/1.0)
			* Age > 37.0: negative (9.0/1.0)
		* Positive > 0.0: negative (12.0)
	* Age > 40.0
		* Positive <= 1.0
			* Age <= 47.0
				* Year <= 63.0: negative (15.0/2.0)
				* Year > 63.0: negative (18.0/8.0)
			* Age > 47.0
				* Year <= 65.0
					* Age <= 59.0
						* Year <= 62.0: negative (27.0)
						* Year > 62.0: negative (16.0/4.0)
					* Age > 59.0
						* Year <= 58.0: negative (10.0/4.0)
						* Year > 58.0
							* Year <= 62.0: negative (11.0/1.0)
							* Year > 62.0: negative (12.0/3.0)
				* Year > 65.0
					* Year <= 67.0: negative (20.0)
					* Year > 67.0: negative (9.0/1.0)
		* Positive > 1.0
			* Age <= 50.0: negative (16.0/3.0)
			* Age > 50.0
				* Age <= 54.0: positive (10.0/3.0)
				* Age > 54.0: negative (14.0/4.0)
* Positive > 4.0
	* Age <= 42.0: negative (12.0/2.0)
	* Age > 42.0
		* Year <= 65.0
			* Positive <= 9.0
				* Positive <= 6.0: positive (9.0/3.0)
				* Positive > 6.0: negative (12.0/4.0)
			* Positive > 9.0
				* Age <= 53.0: positive (13.0/2.0)
				* Age > 53.0: positive (9.0/3.0)
		* Year > 65.0: negative (10.0/4.0)


## SimpleCart Decision Tree

* Positive < 4.5
	* Positive < 1.5
		* Age < 47.5
			* Year < 63.5: negative(28.0/3.0)
			* Year >= 63.5: negative(17.0/9.0)
		* Age >= 47.5
			* Year < 65.5
				* Age < 61.5
					* Year < 62.5: negative(31.0/0.0)
					* Year >= 62.5: negative(13.0/5.0)
				* Age >= 61.5
					* Year < 60.5: negative(7.0/5.0)
					* Year >= 60.5: negative(13.0/2.0)
			* Year >= 65.5: negative(28.0/1.0)
	* Positive >= 1.5
		* Age < 50.5: negative(20.0/3.0)
		* Age >= 50.5
			* Age < 54.0: positive(7.0/3.0)
			* Age >= 54.0: negative(10.0/4.0)
* Positive >= 4.5
	* Age < 42.5: negative(10.0/2.0)
	* Age >= 42.5: positive(31.0/22.0)


