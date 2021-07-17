# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | -1.0 | 0.676768 |
| Sex <= -1.92 and Class <= -0.923 | 1.0 | 0.127122 |
| Sex >= -0.6995 and Age >= 2.076 and Class < -0.45080000000000003 | 1.0 | 0.009608 |
| Sex <= -1.92 and Class > -0.923 and Class > 0.0214 | 1.0 | 0.011947 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Sex > -1.92 and Age <= -0.228 and Class > -1.87 and Class <= 0.0214 and Class > -0.923 | -1.0 | 0.312966 |
| Sex > -1.92 and Age <= -0.228 and Class > -1.87 and Class > -0.923 | -1.0 | 0.431257 |
| Sex > -1.92 and Class > -1.87 and Age <= -0.228 | -1.0 | 0.088012 |
| Sex <= -1.92 and Class <= -0.923 and Class <= -1.87 | 1.0 | 0.327353 |
| Sex > -1.92 and Age <= -0.228 | -1.0 | 0.088499 |
| Class <= -0.923 and Age <= -0.228 | 1.0 | 0.442668 |
| Class > -0.923 and Class <= 0.0214 and Sex <= -1.92 and Age <= -0.228 | -1.0 | 0.120495 |
| Class > -0.923 and Class <= 0.0214 and Sex > -1.92 | -1.0 | 0.029199 |
| Class > -0.923 and Class <= 0.0214 | -1.0 | 0.006181 |
| Class <= -0.923 | 1.0 | 0.556842 |
|  | 1.0 | 0.954424 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Sex <= -1.92 and Class <= -1.87 | 1.0 | 0.085969 |
| Sex <= -1.92 and Class <= -0.923 and Age >= 4.38 | 1.0 | 0.007407 |
| Sex <= -1.92 and Class <= -0.923 | 1.0 | 0.041989 |
| Sex <= -1.92 and Class >= 0.965 | 1.0 | 0.011947 |
| Sex <= -1.92 and Age >= 4.38 | 1.0 | 0.004359 |
| Sex <= -1.92 | 1.0 | 0.019631 |
| Class <= -1.87 and Age >= 4.38 | 1.0 | 0.003717 |
|  | -1.0 | 0.804322 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

class|age|sex|survived
---|---|---|---
(-1.3965--0.4508]|(2.076-inf)|(-0.6995-inf)|1.0
(-inf--1.3965]|(2.076-inf)|(-0.6995-inf)|1.0
(-0.4508-inf)|(2.076-inf)|(-0.6995-inf)|-1.0
(-1.3965--0.4508]|(-inf-2.076]|(-0.6995-inf)|-1.0
(-inf--1.3965]|(-inf-2.076]|(-0.6995-inf)|-1.0
(-0.4508-inf)|(-inf-2.076]|(-0.6995-inf)|-1.0
(-inf--1.3965]|(2.076-inf)|(-inf--0.6995]|-1.0
(-1.3965--0.4508]|(2.076-inf)|(-inf--0.6995]|1.0
(-0.4508-inf)|(2.076-inf)|(-inf--0.6995]|-1.0
(-inf--1.3965]|(-inf-2.076]|(-inf--0.6995]|1.0
(-0.4508-inf)|(-inf-2.076]|(-inf--0.6995]|-1.0
(-1.3965--0.4508]|(-inf-2.076]|(-inf--0.6995]|1.0

## JRip

Decision list:

rules | predicted class
---|---
(Sex <= -1.92) and (Class <= -1.87)|1.0 (130.0/2.0)
(Sex <= -1.92) and (Class <= -0.923) and (Age >= 4.38)|1.0 (10.0/0.0)
(Sex <= -1.92) and (Class <= -0.923)|1.0 (84.0/13.0)
(Sex <= -1.92) and (Class >= 0.965)|1.0 (20.0/2.0)
(Sex <= -1.92) and (Age >= 4.38)|1.0 (29.0/16.0)
(Sex <= -1.92)|1.0 (155.0/86.0)
(Class <= -1.87) and (Age >= 4.38)|1.0 (5.0/0.0)
|-1.0 (1547.0/326.0)


## PART

Decision list:

rules | predicted class
---|---
Sex > -1.92 AND Age <= -0.228 AND Class > -1.87 AND Class <= 0.0214 AND Class > -0.923|-1.0 (408.0/66.0)
Sex > -1.92 AND Age <= -0.228 AND Class > -1.87 AND Class > -0.923|-1.0 (783.0/177.0)
Sex > -1.92 AND Class > -1.87 AND Age <= -0.228|-1.0 (145.0/12.0)
Sex <= -1.92 AND Class <= -0.923 AND Class <= -1.87|1.0 (130.0/2.0)
Sex > -1.92 AND Age <= -0.228|-1.0 (157.0/50.0)
Class <= -0.923 AND Age <= -0.228|1.0 (84.0/13.0)
Class > -0.923 AND Class <= 0.0214 AND Sex <= -1.92 AND Age <= -0.228|-1.0 (155.0/69.0)
Class > -0.923 AND Class <= 0.0214 AND Sex > -1.92|-1.0 (46.0/13.0)
Class > -0.923 AND Class <= 0.0214|-1.0 (29.0/13.0)
Class <= -0.923|1.0 (23.0)
|1.0 (20.0/2.0)


## J48 Decision Tree

* Sex <= -1.92
	* Class <= -0.923: 1.0 (116.0/10.0)
	* Class > -0.923
		* Class <= 0.0214: -1.0 (87.0/36.0)
		* Class > 0.0214: 1.0 (13.0/1.0)
* Sex > -1.92: -1.0 (774.0/166.0)


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


