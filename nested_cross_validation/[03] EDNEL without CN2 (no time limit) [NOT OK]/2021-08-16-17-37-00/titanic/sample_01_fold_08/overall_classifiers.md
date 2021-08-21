# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Sex > -0.6995 | -1.0 | 0.628697 |
| Sex < -0.6995 and Class < -0.45080000000000003 | 1.0 | 0.128335 |
| Sex <= -0.6995 and Class > -0.45080000000000003 and Class <= 0.49319999999999997 | -1.0 | 0.079823 |
| Sex > -0.6995 and Age > 2.076 and Class <= -0.45080000000000003 | 1.0 | 0.011070 |
| Sex <= -0.6995 and Class > -0.45080000000000003 and Class > 0.49319999999999997 | 1.0 | 0.009958 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Sex > -1.92 and Class > -1.87 and Age <= -0.228 | -1.0 | 0.598503 |
| Sex <= -1.92 and Class <= -0.923 | 1.0 | 0.440006 |
| Sex > -1.92 and Class <= -0.923 and Age <= -0.228 | -1.0 | 0.137050 |
| Class > -0.923 and Class <= 0.0214 | -1.0 | 0.144225 |
|  | 1.0 | 0.957494 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Sex <= -1.92 and Class <= -0.923 | 1.0 | 0.128335 |
| Sex <= -1.92 and Class >= 0.965 | 1.0 | 0.009958 |
|  | -1.0 | 0.764840 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

sex|survived
---|---
(-inf--0.6995]|1.0
(-0.6995-inf)|-1.0

## JRip

Decision list:

rules | predicted class
---|---
(Sex <= -1.92) and (Class <= -0.923)|1.0 (228.0/16.0)
(Sex <= -1.92) and (Class >= 0.965)|1.0 (19.0/3.0)
|-1.0 (1733.0/412.0)


## PART

Decision list:

rules | predicted class
---|---
Sex > -1.92 AND Class > -1.87 AND Age <= -0.228|-1.0 (913.0/183.0)
Sex <= -1.92 AND Class <= -0.923|1.0 (140.0/9.0)
Sex > -1.92 AND Class <= -0.923 AND Age <= -0.228|-1.0 (105.0/37.0)
Class > -0.923 AND Class <= 0.0214|-1.0 (139.0/54.0)
|1.0 (23.0/2.0)


## J48 Decision Tree

* Sex <= -0.6995
	* Class <= -0.45080000000000003: 1.0 (228.0/16.0)
	* Class > -0.45080000000000003
		* Class <= 0.49319999999999997: -1.0 (176.0/80.0)
		* Class > 0.49319999999999997: 1.0 (19.0/3.0)
* Sex > -0.6995
	* Age <= 2.076: -1.0 (1499.0/306.0)
	* Age > 2.076
		* Class <= -0.45080000000000003: 1.0 (15.0)
		* Class > -0.45080000000000003: -1.0 (43.0/11.0)


## SimpleCart Decision Tree

* Sex < -0.6995
	* Class < -0.45080000000000003: 1.0(212.0/16.0)
	* Class >= -0.45080000000000003
		* Class < 0.49319999999999997
			* Age < 2.076: -1.0(81.0/67.0)
			* Age >= 2.076: -1.0(15.0/13.0)
		* Class >= 0.49319999999999997: 1.0(16.0/3.0)
* Sex >= -0.6995
	* Class < -1.3965
		* Age < 2.076: -1.0(105.0/54.0)
		* Age >= 2.076: 1.0(5.0/0.0)
	* Class >= -1.3965
		* Age < 2.076
			* Class < 0.49319999999999997
				* Class < -0.45080000000000003: -1.0(137.0/14.0)
				* Class >= -0.45080000000000003: -1.0(348.0/65.0)
			* Class >= 0.49319999999999997: -1.0(603.0/173.0)
		* Age >= 2.076
			* Class < -0.45080000000000003: 1.0(10.0/0.0)
			* Class >= -0.45080000000000003: -1.0(32.0/11.0)


