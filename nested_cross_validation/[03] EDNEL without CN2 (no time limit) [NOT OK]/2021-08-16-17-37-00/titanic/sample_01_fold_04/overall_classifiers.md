# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Sex > -1.92 and Age <= -0.228 and Class > -1.87 and Class > -0.923 and Class > 0.0214 | -1.0 | 0.437427 |
| Sex >= -0.6995 and Class >= -1.3965 and Age < 2.076 and Class >= -0.45080000000000003 and Class < 0.49319999999999997 | -1.0 | 0.310149 |
| Sex < -0.6995 and Class < -0.45080000000000003 | 1.0 | 0.125505 |
| Sex > -1.92 and Age <= -0.228 and Class > -1.87 and Class <= -0.923 | -1.0 | 0.164662 |
| Sex >= -0.6995 and Class < -1.3965 and Age < 2.076 | -1.0 | 0.107633 |
| Sex <= -1.92 and Class > -0.923 and Class <= 0.0214 and Age <= -0.228 | -1.0 | 0.070817 |
| Sex < -0.6995 and Class >= -0.45080000000000003 and Class >= 0.49319999999999997 | 1.0 | 0.012101 |
| Sex > -1.92 and Age > -0.228 and Class <= -0.923 | 1.0 | 0.010340 |
| Sex > -1.92 and Age > -0.228 and Class > -0.923 | -1.0 | 0.035460 |
| Sex <= -1.92 and Class > -0.923 and Class <= 0.0214 and Age > -0.228 | -1.0 | 0.012517 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Sex > -1.92 and Age <= -0.228 and Class > -1.87 and Class > -0.923 and Class > 0.0214 | -1.0 | 0.437427 |
| Sex > -1.92 and Class > -1.87 and Age <= -0.228 and Class > -0.923 | -1.0 | 0.269994 |
| Sex > -1.92 and Class > -1.87 and Age <= -0.228 | -1.0 | 0.091843 |
| Sex <= -1.92 and Class <= -0.923 and Class <= -1.87 | 1.0 | 0.318859 |
| Sex > -1.92 and Age <= -0.228 | -1.0 | 0.092623 |
| Class <= -0.923 and Age <= -0.228 | 1.0 | 0.446667 |
| Class > -0.923 and Class <= 0.0214 and Sex <= -1.92 and Age <= -0.228 | -1.0 | 0.117548 |
| Class > -0.923 and Class <= 0.0214 and Sex > -1.92 | -1.0 | 0.026001 |
| Class > -0.923 and Class <= 0.0214 | -1.0 | 0.005435 |
| Age > -0.228 | 1.0 | 0.720588 |
|  | 1.0 | 0.945714 |


# Text representation of classifiers as-is

## PART

Decision list:

rules | predicted class
---|---
Sex > -1.92 AND Age <= -0.228 AND Class > -1.87 AND Class > -0.923 AND Class > 0.0214|-1.0 (771.0/170.0)
Sex > -1.92 AND Class > -1.87 AND Age <= -0.228 AND Class > -0.923|-1.0 (412.0/71.0)
Sex > -1.92 AND Class > -1.87 AND Age <= -0.228|-1.0 (149.0/12.0)
Sex <= -1.92 AND Class <= -0.923 AND Class <= -1.87|1.0 (130.0/4.0)
Sex > -1.92 AND Age <= -0.228|-1.0 (164.0/53.0)
Class <= -0.923 AND Age <= -0.228|1.0 (81.0/12.0)
Class > -0.923 AND Class <= 0.0214 AND Sex <= -1.92 AND Age <= -0.228|-1.0 (156.0/71.0)
Class > -0.923 AND Class <= 0.0214 AND Sex > -1.92|-1.0 (41.0/10.0)
Class > -0.923 AND Class <= 0.0214|-1.0 (28.0/13.0)
Age > -0.228|1.0 (26.0)
|1.0 (22.0/3.0)


## J48 Decision Tree

* Sex <= -1.92
	* Class <= -0.923
		* Class <= -1.87: 1.0 (130.0/4.0)
		* Class > -1.87
			* Age <= -0.228: 1.0 (81.0/12.0)
			* Age > -0.228: 1.0 (12.0)
	* Class > -0.923
		* Class <= 0.0214
			* Age <= -0.228: -1.0 (156.0/71.0)
			* Age > -0.228: -1.0 (28.0/13.0)
		* Class > 0.0214: 1.0 (22.0/3.0)
* Sex > -1.92
	* Age <= -0.228
		* Class <= -1.87: -1.0 (164.0/53.0)
		* Class > -1.87
			* Class <= -0.923: -1.0 (149.0/12.0)
			* Class > -0.923
				* Class <= 0.0214: -1.0 (412.0/71.0)
				* Class > 0.0214: -1.0 (771.0/170.0)
	* Age > -0.228
		* Class <= -0.923: 1.0 (14.0)
		* Class > -0.923: -1.0 (41.0/10.0)


## SimpleCart Decision Tree

* Sex < -0.6995
	* Class < -0.45080000000000003: 1.0(207.0/16.0)
	* Class >= -0.45080000000000003
		* Class < 0.49319999999999997
			* Age < 2.076: -1.0(85.0/71.0)
			* Age >= 2.076: -1.0(15.0/13.0)
		* Class >= 0.49319999999999997: 1.0(19.0/3.0)
* Sex >= -0.6995
	* Class < -1.3965
		* Age < 2.076: -1.0(111.0/53.0)
		* Age >= 2.076: 1.0(5.0/0.0)
	* Class >= -1.3965
		* Age < 2.076
			* Class < -0.45080000000000003: -1.0(137.0/12.0)
			* Class >= -0.45080000000000003
				* Class < 0.49319999999999997: -1.0(341.0/71.0)
				* Class >= 0.49319999999999997: -1.0(601.0/170.0)
		* Age >= 2.076: -1.0(31.0/19.0)


