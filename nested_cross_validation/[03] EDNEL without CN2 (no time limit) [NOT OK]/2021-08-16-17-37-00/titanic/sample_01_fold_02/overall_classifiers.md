# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | -1.0 | 0.676768 |
| Sex < -0.6995 and Class < -0.45080000000000003 | 1.0 | 0.127122 |
| Sex >= -0.6995 and Age >= 2.076 and Class < -0.45080000000000003 | 1.0 | 0.009608 |
| Sex < -0.6995 and Class >= -0.45080000000000003 and Class >= 0.49319999999999997 | 1.0 | 0.011947 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Sex > -1.92 and Age <= -0.228 and Class > -1.87 and Class <= 0.0214 and Class > -0.923 | -1.0 | 0.312966 |
| Sex > -1.92 and Age <= -0.228 and Class > -1.87 and Class > -0.923 | -1.0 | 0.431257 |
| Sex > -1.92 and Age <= -0.228 and Class <= -1.87 | -1.0 | 0.104625 |
| Class > -1.87 and Sex > -1.92 and Age <= -0.228 | -1.0 | 0.088012 |
| Class <= -0.923 and Class <= -1.87 | 1.0 | 0.543608 |
| Class <= -0.923 and Age <= -0.228 | 1.0 | 0.319527 |
| Class > -0.923 and Class <= 0.0214 and Sex <= -1.92 and Age <= -0.228 | -1.0 | 0.122036 |
| Class > -0.923 and Class <= 0.0214 and Sex > -1.92 | -1.0 | 0.029644 |
| Class > -0.923 and Class <= 0.0214 | -1.0 | 0.006316 |
| Class > -0.923 | 1.0 | 0.954208 |
|  | 1.0 | 0.514286 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Sex <= -1.92 and Class <= -0.923 | 1.0 | 0.127122 |
| Sex <= -1.92 and Class >= 0.965 | 1.0 | 0.011947 |
|  | -1.0 | 0.764404 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

class|age|sex|survived
---|---|---|---
(-inf--1.3965]|(2.076-inf)|(-0.6995-inf)|1.0
(-1.3965--0.4508]|(2.076-inf)|(-0.6995-inf)|1.0
(-0.4508-inf)|(2.076-inf)|(-0.6995-inf)|-1.0
(-1.3965--0.4508]|(-inf-2.076]|(-0.6995-inf)|-1.0
(-inf--1.3965]|(-inf-2.076]|(-0.6995-inf)|-1.0
(-0.4508-inf)|(-inf-2.076]|(-0.6995-inf)|-1.0
(-0.4508-inf)|(2.076-inf)|(-inf--0.6995]|-1.0
(-inf--1.3965]|(2.076-inf)|(-inf--0.6995]|-1.0
(-1.3965--0.4508]|(2.076-inf)|(-inf--0.6995]|1.0
(-0.4508-inf)|(-inf-2.076]|(-inf--0.6995]|-1.0
(-1.3965--0.4508]|(-inf-2.076]|(-inf--0.6995]|1.0
(-inf--1.3965]|(-inf-2.076]|(-inf--0.6995]|1.0

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
Sex > -1.92 AND Age <= -0.228 AND Class > -1.87 AND Class <= 0.0214 AND Class > -0.923|-1.0 (408.0/66.0)
Sex > -1.92 AND Age <= -0.228 AND Class > -1.87 AND Class > -0.923|-1.0 (783.0/177.0)
Sex > -1.92 AND Age <= -0.228 AND Class <= -1.87|-1.0 (157.0/50.0)
Class > -1.87 AND Sex > -1.92 AND Age <= -0.228|-1.0 (145.0/12.0)
Class <= -0.923 AND Class <= -1.87|1.0 (135.0/2.0)
Class <= -0.923 AND Age <= -0.228|1.0 (84.0/13.0)
Class > -0.923 AND Class <= 0.0214 AND Sex <= -1.92 AND Age <= -0.228|-1.0 (155.0/69.0)
Class > -0.923 AND Class <= 0.0214 AND Sex > -1.92|-1.0 (46.0/13.0)
Class > -0.923 AND Class <= 0.0214|-1.0 (29.0/13.0)
Class > -0.923|1.0 (20.0/2.0)
|1.0 (18.0)


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


