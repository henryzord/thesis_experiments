# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Sex > -0.6995 and Age <= 2.076 | -1.0 | 0.622639 |
| Sex <= -0.6995 and Class <= -0.4508 | 1.0 | 0.124937 |
| Sex <= -0.6995 and Class > -0.4508 and Class <= 0.4932 | -1.0 | 0.077648 |
| Sex < -0.6995 and Class >= -0.45080000000000003 and Class >= 0.49319999999999997 | 1.0 | 0.011386 |
| Sex > -0.6995 and Age > 2.076 and Class <= -0.4508 | 1.0 | 0.010340 |
| Sex >= -0.6995 and Age >= 2.076 and Class >= -0.45080000000000003 | -1.0 | 0.032566 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Sex > -0.6995 and Age <= 2.076 and Class > -1.3965 and Class <= 0.4932 and Class > -0.4508 | -1.0 | 0.325185 |
| Sex > -0.6995 and Age <= 2.076 and Class > -1.3965 and Class > 0.021 | -1.0 | 0.426551 |
| Sex > -0.6995 and Age <= 2.076 and Class <= -1.3965 | -1.0 | 0.101834 |
| Class > -1.3965 and Sex > -0.6995 and Age <= 2.076 | -1.0 | 0.088718 |
| Class <= -0.4508 and Class <= -1.3965 | 1.0 | 0.550589 |
| Class <= -0.4508 and Age <= 2.076 | 1.0 | 0.331361 |
| Class > -0.4508 and Class <= 0.4932 and Sex <= -0.6995 and Age <= 2.076 | -1.0 | 0.109141 |
| Class > -0.4508 and Class <= 0.4932 and Sex > -0.6995 | -1.0 | 0.024795 |
| Class > -0.4508 and Class <= 0.4932 | -1.0 | 0.005510 |
| Class <= 0.021 | 1.0 | 0.496622 |
|  | 1.0 | 0.949468 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Sex <= -1.92 | 1.0 | 0.144756 |
|  | -1.0 | 0.799523 |


# Text representation of classifiers as-is

## JRip

Decision list:

rules | predicted class
---|---
(Sex <= -1.92)|1.0 (417.0/113.0)
|-1.0 (1563.0/336.0)


## PART

Decision list:

rules | predicted class
---|---
Sex > -0.6995 AND Age <= 2.076 AND Class > -1.3965 AND Class <= 0.4932 AND Class > -0.4508|-1.0 (430.0/69.0)
Sex > -0.6995 AND Age <= 2.076 AND Class > -1.3965 AND Class > 0.021|-1.0 (775.0/178.0)
Sex > -0.6995 AND Age <= 2.076 AND Class <= -1.3965|-1.0 (156.0/51.0)
Class > -1.3965 AND Sex > -0.6995 AND Age <= 2.076|-1.0 (146.0/12.0)
Class <= -0.4508 AND Class <= -1.3965|1.0 (132.0/4.0)
Class <= -0.4508 AND Age <= 2.076|1.0 (83.0/12.0)
Class > -0.4508 AND Class <= 0.4932 AND Sex <= -0.6995 AND Age <= 2.076|-1.0 (147.0/68.0)
Class > -0.4508 AND Class <= 0.4932 AND Sex > -0.6995|-1.0 (42.0/12.0)
Class > -0.4508 AND Class <= 0.4932|-1.0 (27.0/12.0)
Class <= 0.021|1.0 (21.0)
|1.0 (21.0/3.0)


## J48 Decision Tree

* Sex <= -0.6995
	* Class <= -0.4508: 1.0 (202.0/14.0)
	* Class > -0.4508
		* Class <= 0.4932: -1.0 (149.0/69.0)
		* Class > 0.4932: 1.0 (17.0/3.0)
* Sex > -0.6995
	* Age <= 2.076: -1.0 (1314.0/265.0)
	* Age > 2.076
		* Class <= -0.4508: 1.0 (13.0)
		* Class > -0.4508: -1.0 (38.0/11.0)


## SimpleCart Decision Tree

* Sex < -0.6995
	* Class < -0.45080000000000003
		* Class < -1.3965: 1.0(124.0/4.0)
		* Class >= -1.3965
			* Age < 2.076: 1.0(71.0/12.0)
			* Age >= 2.076: 1.0(11.0/0.0)
	* Class >= -0.45080000000000003
		* Class < 0.49319999999999997
			* Age < 2.076: -1.0(79.0/68.0)
			* Age >= 2.076: -1.0(15.0/12.0)
		* Class >= 0.49319999999999997: 1.0(18.0/3.0)
* Sex >= -0.6995
	* Age < 2.076
		* Class < -1.3965: -1.0(105.0/51.0)
		* Class >= -1.3965
			* Class < 0.49319999999999997
				* Class < -0.45080000000000003: -1.0(134.0/12.0)
				* Class >= -0.45080000000000003: -1.0(361.0/69.0)
			* Class >= 0.49319999999999997: -1.0(597.0/178.0)
	* Age >= 2.076
		* Class < -0.45080000000000003: 1.0(14.0/0.0)
		* Class >= -0.45080000000000003: -1.0(30.0/12.0)


