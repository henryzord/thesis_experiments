# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Sex > -1.92 and Age <= -0.228 | -1.0 | 0.622870 |
| Sex <= -1.92 and Class <= -0.923 | 1.0 | 0.126555 |
| Sex <= -1.92 and Class > -0.923 and Class <= 0.0214 | -1.0 | 0.078311 |
| Sex <= -1.92 and Class > -0.923 and Class > 0.0214 | 1.0 | 0.011947 |
| Sex >= -0.6995 and Age >= 2.076 and Class < -0.45080000000000003 | 1.0 | 0.011070 |
| Class > -0.4508 and Age > 2.076 and Sex > -0.6995 | -1.0 | 0.033193 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Sex > -0.6995 and Age <= 2.076 and Class > -1.3965 and Class > -0.4508 and Class > 0.4932 | -1.0 | 0.443289 |
| Sex > -0.6995 and Age <= 2.076 and Class > -1.3965 and Class > -0.4508 | -1.0 | 0.273003 |
| Sex > -0.6995 and Age <= 2.076 and Class <= -1.3965 | -1.0 | 0.101972 |
| Class > -1.3965 and Sex > -0.6995 and Age <= 2.076 | -1.0 | 0.088012 |
| Class <= -0.4508 and Class <= -1.3965 | 1.0 | 0.559156 |
| Class <= -0.4508 and Age <= 2.076 | 1.0 | 0.337785 |
| Class > -0.4508 and Class <= 0.4932 and Sex <= -0.6995 and Age <= 2.076 | -1.0 | 0.108802 |
| Class > -0.4508 and Class <= 0.4932 and Sex > -0.6995 | -1.0 | 0.026411 |
| Class > -0.4508 and Class <= 0.4932 | -1.0 | 0.006352 |
| Class <= 0.021 | 1.0 | 0.556842 |
|  | 1.0 | 0.953678 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Sex <= -1.92 and Class <= -0.923 | 1.0 | 0.126555 |
| Sex <= -1.92 and Class >= 0.965 | 1.0 | 0.011947 |
|  | -1.0 | 0.763968 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

class|age|sex|survived
---|---|---|---
(-1.3965--0.4508]|(2.076-inf)|(-0.6995-inf)|1.0
(-inf--1.3965]|(2.076-inf)|(-0.6995-inf)|1.0
(-0.4508-inf)|(2.076-inf)|(-0.6995-inf)|-1.0
(-inf--1.3965]|(-inf-2.076]|(-0.6995-inf)|-1.0
(-1.3965--0.4508]|(-inf-2.076]|(-0.6995-inf)|-1.0
(-0.4508-inf)|(-inf-2.076]|(-0.6995-inf)|-1.0
(-inf--1.3965]|(2.076-inf)|(-inf--0.6995]|-1.0
(-1.3965--0.4508]|(2.076-inf)|(-inf--0.6995]|1.0
(-0.4508-inf)|(2.076-inf)|(-inf--0.6995]|-1.0
(-inf--1.3965]|(-inf-2.076]|(-inf--0.6995]|1.0
(-0.4508-inf)|(-inf-2.076]|(-inf--0.6995]|1.0
(-1.3965--0.4508]|(-inf-2.076]|(-inf--0.6995]|1.0

## JRip

Decision list:

rules | predicted class
---|---
(Sex <= -1.92) and (Class <= -0.923)|1.0 (223.0/15.0)
(Sex <= -1.92) and (Class >= 0.965)|1.0 (20.0/2.0)
|-1.0 (1737.0/414.0)


## PART

Decision list:

rules | predicted class
---|---
Sex > -0.6995 AND Age <= 2.076 AND Class > -1.3965 AND Class > -0.4508 AND Class > 0.4932|-1.0 (786.0/172.0)
Sex > -0.6995 AND Age <= 2.076 AND Class > -1.3965 AND Class > -0.4508|-1.0 (414.0/69.0)
Sex > -0.6995 AND Age <= 2.076 AND Class <= -1.3965|-1.0 (159.0/53.0)
Class > -1.3965 AND Sex > -0.6995 AND Age <= 2.076|-1.0 (147.0/14.0)
Class <= -0.4508 AND Class <= -1.3965|1.0 (133.0/3.0)
Class <= -0.4508 AND Age <= 2.076|1.0 (82.0/12.0)
Class > -0.4508 AND Class <= 0.4932 AND Sex <= -0.6995 AND Age <= 2.076|-1.0 (146.0/68.0)
Class > -0.4508 AND Class <= 0.4932 AND Sex > -0.6995|-1.0 (44.0/13.0)
Class > -0.4508 AND Class <= 0.4932|-1.0 (26.0/10.0)
Class <= 0.021|1.0 (23.0)
|1.0 (20.0/2.0)


## J48 Decision Tree

* Sex <= -1.92
	* Class <= -0.923: 1.0 (139.0/9.0)
	* Class > -0.923
		* Class <= 0.0214: -1.0 (113.0/54.0)
		* Class > 0.0214: 1.0 (12.0/1.0)
* Sex > -1.92
	* Age <= -0.228: -1.0 (1016.0/214.0)
	* Age > -0.228
		* Class <= -0.923: 1.0 (11.0)
		* Class > -0.923: -1.0 (29.0/7.0)


## SimpleCart Decision Tree

* Sex < -0.6995
	* Class < -0.45080000000000003
		* Class < -1.3965: 1.0(125.0/3.0)
		* Class >= -1.3965
			* Age < 2.076: 1.0(70.0/12.0)
			* Age >= 2.076: 1.0(13.0/0.0)
	* Class >= -0.45080000000000003
		* Class < 0.49319999999999997
			* Age < 2.076: -1.0(78.0/68.0)
			* Age >= 2.076: -1.0(16.0/10.0)
		* Class >= 0.49319999999999997: 1.0(18.0/2.0)
* Sex >= -0.6995
	* Age < 2.076
		* Class < -1.3965: -1.0(106.0/53.0)
		* Class >= -1.3965
			* Class < 0.49319999999999997
				* Class < -0.45080000000000003: -1.0(133.0/14.0)
				* Class >= -0.45080000000000003: -1.0(345.0/69.0)
			* Class >= 0.49319999999999997: -1.0(614.0/172.0)
	* Age >= 2.076
		* Class < -0.45080000000000003: 1.0(15.0/0.0)
		* Class >= -0.45080000000000003: -1.0(31.0/13.0)


