# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Sex > -0.6995 and Class > -1.3965 and Age <= 2.076 | -1.0 | 0.601050 |
| Sex <= -0.6995 and Class <= -0.4508 | 1.0 | 0.128422 |
| Sex >= -0.6995 and Age < 2.076 and Class < -1.3965 | -1.0 | 0.099696 |
| Sex < -0.6995 and Class >= -0.45080000000000003 and Class >= 0.49319999999999997 | 1.0 | 0.012816 |
| Sex <= -0.6995 and Class > -0.4508 and Class <= 0.4932 | -1.0 | 0.071245 |
| Sex >= -0.6995 and Age >= 2.076 and Class < -0.45080000000000003 | 1.0 | 0.011070 |
| Sex >= -0.6995 and Age >= 2.076 and Class >= -0.45080000000000003 | -1.0 | 0.036667 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Sex > -1.92 and Age <= -0.228 and Class > -1.87 and Class <= 0.0214 and Class > -0.923 | -1.0 | 0.321301 |
| Sex > -1.92 and Age <= -0.228 and Class > -1.87 and Class > -0.923 | -1.0 | 0.430311 |
| Sex > -1.92 and Age <= -0.228 and Class <= -1.87 | -1.0 | 0.099696 |
| Sex > -1.92 and Age <= -0.228 | -1.0 | 0.094862 |
| Class <= -0.923 and Class <= -1.87 | 1.0 | 0.561013 |
| Class <= -0.923 and Age <= -0.228 | 1.0 | 0.332802 |
| Class > -0.923 and Class <= 0.0214 and Sex <= -1.92 and Age <= -0.228 | -1.0 | 0.102472 |
| Class > -0.923 and Class <= 0.0214 and Sex > -1.92 | -1.0 | 0.030367 |
| Class > -0.923 and Class <= 0.0214 | -1.0 | 0.005013 |
| Class <= -0.923 | 1.0 | 0.520325 |
|  | 1.0 | 0.945652 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

class|sex|survived
---|---|---
(-1.3965--0.4508]|(-0.6995-inf)|-1.0
(-inf--1.3965]|(-0.6995-inf)|-1.0
(-0.4508-inf)|(-0.6995-inf)|-1.0
(-1.3965--0.4508]|(-inf--0.6995]|1.0
(-inf--1.3965]|(-inf--0.6995]|1.0
(-0.4508-inf)|(-inf--0.6995]|1.0

## PART

Decision list:

rules | predicted class
---|---
Sex > -1.92 AND Age <= -0.228 AND Class > -1.87 AND Class <= 0.0214 AND Class > -0.923|-1.0 (416.0/64.0)
Sex > -1.92 AND Age <= -0.228 AND Class > -1.87 AND Class > -0.923|-1.0 (774.0/172.0)
Sex > -1.92 AND Age <= -0.228 AND Class <= -1.87|-1.0 (154.0/51.0)
Sex > -1.92 AND Age <= -0.228|-1.0 (154.0/12.0)
Class <= -0.923 AND Class <= -1.87|1.0 (137.0/4.0)
Class <= -0.923 AND Age <= -0.228|1.0 (84.0/13.0)
Class > -0.923 AND Class <= 0.0214 AND Sex <= -1.92 AND Age <= -0.228|-1.0 (141.0/67.0)
Class > -0.923 AND Class <= 0.0214 AND Sex > -1.92|-1.0 (45.0/12.0)
Class > -0.923 AND Class <= 0.0214|-1.0 (27.0/13.0)
Class <= -0.923|1.0 (24.0)
|1.0 (23.0/3.0)


## J48 Decision Tree

* Sex <= -0.6995
	* Class <= -0.4508: 1.0 (151.0/13.0)
	* Class > -0.4508
		* Class <= 0.4932: -1.0 (123.0/61.0)
		* Class > 0.4932: 1.0 (16.0/3.0)
* Sex > -0.6995
	* Class <= -1.3965: -1.0 (104.0/39.0)
	* Class > -1.3965
		* Age <= 2.076: -1.0 (898.0/163.0)
		* Age > 2.076
			* Class <= -0.4508: 1.0 (8.0)
			* Class > -0.4508: -1.0 (20.0/4.0)


## SimpleCart Decision Tree

* Sex < -0.6995
	* Class < -0.45080000000000003
		* Class < -1.3965: 1.0(129.0/4.0)
		* Class >= -1.3965
			* Age < 2.076: 1.0(71.0/13.0)
			* Age >= 2.076: 1.0(13.0/0.0)
	* Class >= -0.45080000000000003
		* Class < 0.49319999999999997
			* Age < 2.076: -1.0(74.0/67.0)
			* Age >= 2.076: -1.0(14.0/13.0)
		* Class >= 0.49319999999999997: 1.0(20.0/3.0)
* Sex >= -0.6995
	* Age < 2.076
		* Class < -1.3965: -1.0(103.0/51.0)
		* Class >= -1.3965
			* Class < 0.49319999999999997
				* Class < -0.45080000000000003: -1.0(142.0/12.0)
				* Class >= -0.45080000000000003: -1.0(352.0/64.0)
			* Class >= 0.49319999999999997: -1.0(602.0/172.0)
	* Age >= 2.076
		* Class < -0.45080000000000003: 1.0(15.0/0.0)
		* Class >= -0.45080000000000003: -1.0(33.0/12.0)


