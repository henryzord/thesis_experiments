# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | -1.0 | 0.676768 |
| Sex > -1.92 and Age > -0.228 and Class <= -0.923 | 1.0 | 0.011799 |
| Sex <= -1.92 and Class <= -0.923 | 1.0 | 0.124851 |
| Sex <= -1.92 and Class > -0.923 and Class <= 0.0214 and Age > -0.228 | 1.0 | 0.005617 |
| Sex <= -1.92 and Class > -0.923 and Class > 0.0214 | 1.0 | 0.012668 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Sex > -1.92 and Age <= -0.228 | -1.0 | 0.621599 |
| Class <= -0.923 | 1.0 | 0.646046 |
| Class <= 0.0214 | -1.0 | 0.202731 |
|  | 1.0 | 0.994429 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Sex <= -1.92 and Class <= -0.923 | 1.0 | 0.124851 |
| Sex <= -1.92 and Class >= 0.965 | 1.0 | 0.012668 |
|  | -1.0 | 0.763098 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

class|age|sex|survived
---|---|---|---
(-inf--1.3965]|(2.076-inf)|(-0.6995-inf)|1.0
(-1.3965--0.4508]|(2.076-inf)|(-0.6995-inf)|1.0
(-0.4508-inf)|(2.076-inf)|(-0.6995-inf)|-1.0
(-1.3965--0.4508]|(-inf-2.076]|(-0.6995-inf)|-1.0
(-0.4508-inf)|(-inf-2.076]|(-0.6995-inf)|-1.0
(-inf--1.3965]|(-inf-2.076]|(-0.6995-inf)|-1.0
(-inf--1.3965]|(2.076-inf)|(-inf--0.6995]|-1.0
(-1.3965--0.4508]|(2.076-inf)|(-inf--0.6995]|1.0
(-0.4508-inf)|(2.076-inf)|(-inf--0.6995]|1.0
(-0.4508-inf)|(-inf-2.076]|(-inf--0.6995]|1.0
(-1.3965--0.4508]|(-inf-2.076]|(-inf--0.6995]|1.0
(-inf--1.3965]|(-inf-2.076]|(-inf--0.6995]|1.0

## JRip

Decision list:

rules | predicted class
---|---
(Sex <= -1.92) and (Class <= -0.923)|1.0 (220.0/15.0)
(Sex <= -1.92) and (Class >= 0.965)|1.0 (21.0/2.0)
|-1.0 (1739.0/416.0)


## PART

Decision list:

rules | predicted class
---|---
Sex > -1.92 AND Age <= -0.228|-1.0 (1494.0/302.0)
Class <= -0.923|1.0 (236.0/15.0)
Class <= 0.0214|-1.0 (229.0/98.0)
|1.0 (21.0/2.0)


## J48 Decision Tree

* Sex <= -1.92
	* Class <= -0.923: 1.0 (220.0/15.0)
	* Class > -0.923
		* Class <= 0.0214
			* Age <= -0.228: -1.0 (156.0/72.0)
			* Age > -0.228: 1.0 (26.0/12.0)
		* Class > 0.0214: 1.0 (21.0/2.0)
* Sex > -1.92
	* Age <= -0.228: -1.0 (1494.0/302.0)
	* Age > -0.228
		* Class <= -0.923: 1.0 (16.0)
		* Class > -0.923: -1.0 (47.0/12.0)


## SimpleCart Decision Tree

* Sex < -0.6995
	* Class < -0.45080000000000003: 1.0(205.0/15.0)
	* Class >= -0.45080000000000003
		* Class < 0.49319999999999997
			* Age < 2.076: -1.0(84.0/72.0)
			* Age >= 2.076: 1.0(14.0/12.0)
		* Class >= 0.49319999999999997: 1.0(19.0/2.0)
* Sex >= -0.6995
	* Age < 2.076
		* Class < -1.3965: -1.0(104.0/50.0)
		* Class >= -1.3965
			* Class < 0.49319999999999997
				* Class < -0.45080000000000003: -1.0(143.0/12.0)
				* Class >= -0.45080000000000003: -1.0(349.0/68.0)
			* Class >= 0.49319999999999997: -1.0(596.0/172.0)
	* Age >= 2.076
		* Class < -0.45080000000000003: 1.0(16.0/0.0)
		* Class >= -0.45080000000000003: -1.0(35.0/12.0)


