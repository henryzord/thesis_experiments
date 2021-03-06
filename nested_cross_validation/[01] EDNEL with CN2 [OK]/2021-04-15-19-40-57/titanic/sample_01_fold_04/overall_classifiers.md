# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Age <= 2.076 and Sex > -0.6995 | -1.0 | 0.621123 |
| Sex < -0.6995 and Class < -0.45080000000000003 and Class < -1.3965 | 1.0 | 0.083532 |
| Sex < -0.6995 and Class < -0.45080000000000003 and Class >= -1.3965 and Age < 2.076 | 1.0 | 0.042074 |
| Sex < -0.6995 and Class >= -0.45080000000000003 and Class < 0.49319999999999997 and Age < 2.076 | -1.0 | 0.070817 |
| Sex < -0.6995 and Class >= -0.45080000000000003 and Class >= 0.49319999999999997 | 1.0 | 0.012101 |
| Sex < -0.6995 and Class < -0.45080000000000003 and Class >= -1.3965 and Age >= 2.076 | 1.0 | 0.008876 |
| Sex >= -0.6995 and Class >= -1.3965 and Age >= 2.076 and Class < -0.45080000000000003 | 1.0 | 0.006672 |
| Sex >= -0.6995 and Class < -1.3965 and Age >= 2.076 | 1.0 | 0.003717 |
| Sex >= -0.6995 and Class >= -1.3965 and Age >= 2.076 and Class >= -0.45080000000000003 | -1.0 | 0.035460 |
| Sex < -0.6995 and Class >= -0.45080000000000003 and Class < 0.49319999999999997 and Age >= 2.076 | -1.0 | 0.012517 |

## Ordered rules

# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

age|sex|survived
---|---|---
(2.076-inf)|(-0.6995-inf)|-1.0
(-inf-2.076]|(-0.6995-inf)|-1.0
(2.076-inf)|(-inf--0.6995]|1.0
(-inf-2.076]|(-inf--0.6995]|1.0

## SimpleCart Decision Tree

* Sex < -0.6995
	* Class < -0.45080000000000003
		* Class < -1.3965: 1.0(126.0/4.0)
		* Class >= -1.3965
			* Age < 2.076: 1.0(69.0/12.0)
			* Age >= 2.076: 1.0(12.0/0.0)
	* Class >= -0.45080000000000003
		* Class < 0.49319999999999997
			* Age < 2.076: -1.0(85.0/71.0)
			* Age >= 2.076: -1.0(15.0/13.0)
		* Class >= 0.49319999999999997: 1.0(19.0/3.0)
* Sex >= -0.6995
	* Class < -1.3965
		* Age < 2.076: -1.0(110.0/53.0)
		* Age >= 2.076: 1.0(5.0/0.0)
	* Class >= -1.3965
		* Age < 2.076
			* Class < -0.45080000000000003: -1.0(137.0/12.0)
			* Class >= -0.45080000000000003
				* Class < 0.49319999999999997: -1.0(341.0/71.0)
				* Class >= 0.49319999999999997: -1.0(602.0/170.0)
		* Age >= 2.076
			* Class < -0.45080000000000003: 1.0(9.0/0.0)
			* Class >= -0.45080000000000003: -1.0(31.0/10.0)


