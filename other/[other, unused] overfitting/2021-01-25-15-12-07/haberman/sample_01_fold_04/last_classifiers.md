# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Positive <= 4.5 | negative | 0.681170 |
| Positive > 4.5 | positive | 0.082531 |
| Positive >= 4.5 and Age < 42.5 | negative | 0.104167 |
| Positive <= 4.5 and Age > 40.5 and Positive > 1.5 and Age > 50.5 and Age <= 54.0 | positive | 0.023786 |
| Positive > 4.5 and Age > 42.5 and Year <= 65.5 and Positive <= 9.5 and Positive > 6.5 and Positive <= 8.5 | negative | 0.066790 |
| Positive <= 4.5 and Age > 40.5 and Positive > 1.5 and Age > 50.5 and Age > 54.0 and Age > 62.5 | positive | 0.008867 |
| Positive > 4.5 and Age > 42.5 and Year > 65.5 | negative | 0.048649 |
| Positive <= 4.5 and Age > 40.5 and Positive <= 1.5 and Age <= 47.5 and Year > 63.5 and Year <= 64.5 | positive | 0.008867 |
| Positive > 4.5 and Age > 42.5 and Year <= 65.5 and Positive > 9.5 and Positive > 13.5 and Positive <= 19.5 | negative | 0.024658 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Positive <= 2 | negative | 0.651042 |
| Age > 43 and Year <= 65 and Positive > 8 | positive | 0.222154 |
| Age <= 43 | negative | 0.171819 |
| Positive > 6 | negative | 0.197802 |
| Age > 50 and Age <= 56 | positive | 0.382353 |
|  | negative | 0.298246 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Positive >= 9 and Year <= 65 and Age <= 53 and Age >= 46 | positive | 0.047170 |
| Positive >= 2 and Age >= 51 and Age <= 57 and Positive <= 15 and Year >= 65 | positive | 0.026302 |
| Positive >= 2 and Age >= 65 | positive | 0.021729 |
|  | negative | 0.808000 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

positive|survival
---|---
(4.5-inf)|positive
(-inf-4.5]|negative

## JRip

Decision list:

rules | predicted class
---|---
(Positive >= 9) and (Year <= 65) and (Age <= 53) and (Age >= 46)|positive (10.0/0.0)
(Positive >= 2) and (Age >= 51) and (Age <= 57) and (Positive <= 15) and (Year >= 65)|positive (9.0/2.0)
(Positive >= 2) and (Age >= 65)|positive (11.0/4.0)
|negative (244.0/48.0)


## PART

Decision list:

rules | predicted class
---|---
Positive <= 2|negative (149.0/25.0)
Age > 43 AND Year <= 65 AND Positive > 8|positive (21.0/4.0)
Age <= 43|negative (18.0/2.0)
Positive > 6|negative (13.0/2.0)
Age > 50 AND Age <= 56|positive (12.0/4.0)
|negative (16.0/6.0)


## J48 Decision Tree

* Positive <= 4.5
	* Age <= 40.5: negative (31.0/2.0)
	* Age > 40.5
		* Positive <= 1.5
			* Age <= 47.5
				* Year <= 63.5: negative (15.0/2.0)
				* Year > 63.5
					* Year <= 64.5: positive (5.0/2.0)
					* Year > 64.5: negative (13.0/5.0)
			* Age > 47.5: negative (105.0/13.0)
		* Positive > 1.5
			* Age <= 50.5: negative (16.0/3.0)
			* Age > 50.5
				* Age <= 54.0: positive (10.0/3.0)
				* Age > 54.0
					* Age <= 62.5: negative (9.0/1.0)
					* Age > 62.5: positive (5.0/2.0)
* Positive > 4.5
	* Age <= 42.5: negative (12.0/2.0)
	* Age > 42.5
		* Year <= 65.5
			* Positive <= 9.5
				* Positive <= 6.5: positive (9.0/3.0)
				* Positive > 6.5
					* Positive <= 8.5: negative (7.0/1.0)
					* Positive > 8.5: positive (5.0/2.0)
			* Positive > 9.5
				* Positive <= 13.5: positive (8.0)
				* Positive > 13.5
					* Positive <= 19.5: negative (5.0/2.0)
					* Positive > 19.5: positive (9.0/2.0)
		* Year > 65.5: negative (10.0/4.0)


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


