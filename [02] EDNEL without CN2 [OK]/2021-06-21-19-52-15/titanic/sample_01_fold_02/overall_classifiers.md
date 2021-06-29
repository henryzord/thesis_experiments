# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | -1.0 | 0.676768 |
| Sex < -0.6995 and Class >= -0.45080000000000003 and Class >= 0.49319999999999997 | 1.0 | 0.011947 |
| Sex <= -1.92 and Class <= -0.923 | 1.0 | 0.127122 |
| Sex >= -0.6995 and Age >= 2.076 and Class < -0.45080000000000003 | 1.0 | 0.009608 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Sex > -1.92 | -1.0 | 0.627839 |
| Class <= -0.923 | 1.0 | 0.695238 |
| Class <= 0.0214 | -1.0 | 0.157824 |
|  | 1.0 | 0.994413 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Sex <= -1.92 and Class <= -0.923 | 1.0 | 0.127122 |
| Sex <= -1.92 and Class >= 0.965 | 1.0 | 0.011947 |
|  | -1.0 | 0.764404 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

class|sex|survived
---|---|---
(-1.3965--0.4508]|(-0.6995-inf)|-1.0
(-inf--1.3965]|(-0.6995-inf)|-1.0
(-0.4508-inf)|(-0.6995-inf)|-1.0
(-1.3965--0.4508]|(-inf--0.6995]|1.0
(-inf--1.3965]|(-inf--0.6995]|1.0
(-0.4508-inf)|(-inf--0.6995]|-1.0

## JRip

Decision list:

rules | predicted class
---|---
(Sex <= -1.92) and (Class <= -0.923)|1.0 (224.0/15.0)
(Sex <= -1.92) and (Class >= 0.965)|1.0 (20.0/2.0)
|-1.0 (1736.0/413.0)


## PART

Decision list:

rules | predicted class
---|---
Sex > -1.92|-1.0 (1363.0/293.0)
Class <= -0.923|1.0 (191.0/12.0)
Class <= 0.0214|-1.0 (161.0/72.0)
|1.0 (18.0/2.0)


## J48 Decision Tree

* Sex <= -1.92
	* Class <= -0.923: 1.0 (224.0/15.0)
	* Class > -0.923
		* Class <= 0.0214: -1.0 (184.0/82.0)
		* Class > 0.0214: 1.0 (20.0/2.0)
* Sex > -1.92
	* Age <= -0.228: -1.0 (1493.0/305.0)
	* Age > -0.228
		* Class <= -0.923: 1.0 (13.0)
		* Class > -0.923: -1.0 (46.0/13.0)


## SimpleCart Decision Tree

* Sex < -0.6995
	* Class < -0.45080000000000003: 1.0(209.0/15.0)
	* Class >= -0.45080000000000003
		* Class < 0.49319999999999997
			* Age < 2.076: -1.0(86.0/69.0)
			* Age >= 2.076: -1.0(16.0/13.0)
		* Class >= 0.49319999999999997: 1.0(18.0/2.0)
* Sex >= -0.6995
	* Age < 2.076
		* Class < -1.3965: -1.0(107.0/50.0)
		* Class >= -1.3965
			* Class < 0.49319999999999997
				* Class < -0.45080000000000003: -1.0(133.0/12.0)
				* Class >= -0.45080000000000003: -1.0(342.0/66.0)
			* Class >= 0.49319999999999997: -1.0(606.0/177.0)
	* Age >= 2.076
		* Class < -0.45080000000000003: 1.0(13.0/0.0)
		* Class >= -0.45080000000000003: -1.0(33.0/13.0)


