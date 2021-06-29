# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Positive < 8.5 | negative | 0.699714 |
| Positive > 4.5 and Age > 42.5 | positive | 0.090546 |
| Age = all and Positive > 4.5 | negative | 0.243056 |
| Positive <= 4.5 and Year <= 59.5 and Positive <= 2.5 and Year <= 58.5 and Age > 60 and Age <= 65.5 | positive | 0.004950 |
| Positive <= 4.5 and Year <= 59.5 and Positive <= 2.5 and Year <= 58.5 and Age > 60 and Age > 65.5 | positive | 0.011029 |
| Positive <= 4.5 and Year <= 59.5 and Positive > 2.5 | positive | 0.011260 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Positive <= 4 and Year > 59 and Age > 38 and Year <= 61 and Age <= 61 | negative | 0.250000 |
| Positive <= 2 and Age <= 40 and Positive > 0 | negative | 0.100000 |
| Positive <= 1 and Age > 47 and Year > 65 and Positive <= 0 | negative | 0.250000 |
| Positive <= 8 and Age <= 40 and Positive <= 1 and Year <= 64 and Age <= 37 | negative | 0.066790 |
| Positive <= 8 and Age > 38 and Positive <= 1 and Age > 47 and Age <= 59 and Age > 53 | negative | 0.172414 |
| Age <= 40 and Year <= 65 | negative | 0.153725 |
| Positive <= 8 and Year > 58 and Age > 61 and Positive <= 0 and Age <= 69 | negative | 0.132530 |
| Positive <= 8 and Age <= 60 and Age <= 57 and Age <= 51 and Age > 47 and Positive > 0 and Positive <= 2 | negative | 0.111111 |
| Positive > 8 and Year <= 60 and Age <= 49 | positive | 0.034043 |
| Positive <= 8 and Age <= 41 and Age > 40 | negative | 0.062500 |
| Positive <= 8 and Age > 40 and Year > 58 and Year <= 68 and Positive <= 4 and Year > 61 and Positive > 1 and Age <= 51 | negative | 0.093333 |
| Positive > 8 and Year > 60 and Year <= 65 and Age <= 59 and Age > 48 | positive | 0.076190 |
| Positive <= 0 and Year <= 66 and Age > 50 and Age > 56 and Year > 58 and Year <= 63 | negative | 0.065104 |
| Age <= 42 and Age > 38 | negative | 0.053651 |
| Age > 40 and Year <= 60 and Positive <= 8 and Age <= 65 and Age > 53 | negative | 0.056689 |
| Year <= 60 and Positive <= 8 and Age > 50 and Age <= 68 | positive | 0.081260 |
| Year <= 60 and Positive <= 8 and Age <= 60 | negative | 0.051440 |
| Year <= 60 and Age <= 66 | positive | 0.124615 |
| Age <= 40 | negative | 0.075988 |
| Age <= 64 and Year <= 67 and Age > 50 and Positive > 5 and Age <= 61 | negative | 0.153846 |
| Positive > 14 and Age <= 58 | positive | 0.068085 |
| Positive <= 0 and Age > 50 and Age > 56 | negative | 0.050000 |
| Positive <= 0 and Age <= 50 and Year <= 64 | positive | 0.093023 |
| Positive <= 0 and Age <= 49 | negative | 0.149184 |
| Positive > 0 and Age <= 46 | positive | 0.127273 |
| Positive > 0 and Age <= 64 and Year <= 64 and Positive <= 5 | positive | 0.041475 |
| Positive > 0 and Age <= 64 and Year > 64 and Age > 53 | negative | 0.148148 |
| Positive > 0 and Age > 51 and Age <= 69 and Age > 64 | positive | 0.165899 |
| Positive <= 7 and Positive > 0 and Year > 64 | positive | 0.177778 |
| Age <= 66 | negative | 0.641026 |
|  | negative | 0.375000 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Age >= 44 and Positive >= 10 and Year <= 65 and Positive <= 13 | positive | 0.042654 |
| Positive >= 3 and Age >= 44 and Year >= 62 | positive | 0.063828 |
|  | negative | 0.841667 |


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
(Age >= 44) and (Positive >= 10) and (Year <= 65) and (Positive <= 13)|positive (9.0/0.0)
(Positive >= 3) and (Age >= 44) and (Year >= 62)|positive (48.0/23.0)
|negative (217.0/38.0)


## PART

Decision list:

rules | predicted class
---|---
Positive <= 4 AND Year > 59 AND Age > 38 AND Year <= 61 AND Age <= 61|negative (24.0)
Positive <= 2 AND Age <= 40 AND Positive > 0|negative (8.0)
Positive <= 1 AND Age > 47 AND Year > 65 AND Positive <= 0|negative (24.0)
Positive <= 8 AND Age <= 40 AND Positive <= 1 AND Year <= 64 AND Age <= 37|negative (7.0/1.0)
Positive <= 8 AND Age > 38 AND Positive <= 1 AND Age > 47 AND Age <= 59 AND Age > 53|negative (15.0)
Age <= 40 AND Year <= 65|negative (14.0)
Positive <= 8 AND Year > 58 AND Age > 61 AND Positive <= 0 AND Age <= 69|negative (11.0)
Positive <= 8 AND Age <= 60 AND Age <= 57 AND Age <= 51 AND Age > 47 AND Positive > 0 AND Positive <= 2|negative (9.0)
Positive > 8 AND Year <= 60 AND Age <= 49|positive (5.0/1.0)
Positive <= 8 AND Age <= 41 AND Age > 40|negative (8.0/2.0)
Positive <= 8 AND Age > 40 AND Year > 58 AND Year <= 68 AND Positive <= 4 AND Year > 61 AND Positive > 1 AND Age <= 51|negative (7.0)
Positive > 8 AND Year > 60 AND Year <= 65 AND Age <= 59 AND Age > 48|positive (10.0/2.0)
Positive <= 0 AND Year <= 66 AND Age > 50 AND Age > 56 AND Year > 58 AND Year <= 63|negative (6.0/1.0)
Age <= 42 AND Age > 38|negative (9.0/3.0)
Age > 40 AND Year <= 60 AND Positive <= 8 AND Age <= 65 AND Age > 53|negative (7.0/2.0)
Year <= 60 AND Positive <= 8 AND Age > 50 AND Age <= 68|positive (7.0/2.0)
Year <= 60 AND Positive <= 8 AND Age <= 60|negative (5.0/2.0)
Year <= 60 AND Age <= 66|positive (5.0)
Age <= 40|negative (6.0/1.0)
Age <= 64 AND Year <= 67 AND Age > 50 AND Positive > 5 AND Age <= 61|negative (6.0)
Positive > 14 AND Age <= 58|positive (5.0/1.0)
Positive <= 0 AND Age > 50 AND Age > 56|negative (7.0/3.0)
Positive <= 0 AND Age <= 50 AND Year <= 64|positive (8.0/3.0)
Positive <= 0 AND Age <= 49|negative (6.0/1.0)
Positive > 0 AND Age <= 46|positive (7.0/2.0)
Positive > 0 AND Age <= 64 AND Year <= 64 AND Positive <= 5|positive (6.0/3.0)
Positive > 0 AND Age <= 64 AND Year > 64 AND Age > 53|negative (9.0/3.0)
Positive > 0 AND Age > 51 AND Age <= 69 AND Age > 64|positive (7.0/1.0)
Positive <= 7 AND Positive > 0 AND Year > 64|positive (9.0/3.0)
Age <= 66|negative (12.0)
|negative (5.0/2.0)


## J48 Decision Tree

* Positive <= 4.5
	* Year <= 59.5
		* Positive <= 2.5
			* Year <= 58.5
				* Age <= 60
					* Positive <= 0.5: negative (7.0)
					* Positive > 0.5: negative (6.0/1.0)
				* Age > 60
					* Age <= 65.5: positive (4.0/2.0)
					* Age > 65.5: positive (4.0/1.0)
			* Year > 58.5: negative (16.0/4.0)
		* Positive > 2.5: positive (7.0/3.0)
	* Year > 59.5
		* Year <= 61.5
			* Year <= 60.5: negative (18.0)
			* Year > 60.5
				* Positive <= 0.5: negative (10.0)
				* Positive > 0.5: negative (7.0/1.0)
		* Year > 61.5: negative (125.0/22.0)
* Positive > 4.5
	* Age <= 42.5: negative (13.0/2.0)
	* Age > 42.5: positive (57.0/24.0)


## SimpleCart Decision Tree

* Positive < 8.5: negative(183.0/46.0)
* Positive >= 8.5
	* Age < 45.5: negative(9.0/4.0)
	* Age >= 45.5: positive(22.0/10.0)


