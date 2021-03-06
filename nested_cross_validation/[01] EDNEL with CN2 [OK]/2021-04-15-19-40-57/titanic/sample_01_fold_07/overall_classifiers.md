# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Sex >= -0.6995 and Age < 2.076 and Class >= -1.3965 and Class >= 0.49319999999999997 | -1.0 | 0.434700 |
| Sex >= -0.6995 and Age < 2.076 and Class >= -1.3965 and Class < 0.49319999999999997 and Class >= -0.45080000000000003 | -1.0 | 0.317143 |
| Sex < -0.6995 and Class < -0.45080000000000003 | 1.0 | 0.124851 |
| Sex >= -0.6995 and Age < 2.076 and Class >= -1.3965 and Class < 0.49319999999999997 and Class < -0.45080000000000003 | -1.0 | 0.171114 |
| Sex >= -0.6995 and Age < 2.076 and Class < -1.3965 | -1.0 | 0.102344 |
| Sex < -0.6995 and Class >= -0.45080000000000003 and Class >= 0.49319999999999997 | 1.0 | 0.012668 |
| Sex < -0.6995 and Class >= -0.45080000000000003 and Class < 0.49319999999999997 and Age < 2.076 | -1.0 | 0.068272 |
| Sex < -0.6995 and Class >= -0.45080000000000003 and Class < 0.49319999999999997 and Age >= 2.076 | 1.0 | 0.005617 |
| Sex >= -0.6995 and Age >= 2.076 | -1.0 | 0.030053 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Sex > -0.6995 and Age <= 2.076 and Class > -1.3965 and Class > -0.45080000000000003 and Class > 0.49319999999999997 | -1.0 | 0.434700 |
| Sex > -0.6995 and Class > -1.3965 and Age <= 2.076 and Class > -0.45080000000000003 | -1.0 | 0.276092 |
| Sex > -0.6995 and Age <= 2.076 and Class <= -1.3965 | -1.0 | 0.102344 |
| Sex > -0.6995 and Age <= 2.076 | -1.0 | 0.095536 |
| Class <= -0.45080000000000003 and Age <= 2.076 and Class <= -1.3965 | 1.0 | 0.529143 |
| Class <= -0.45080000000000003 and Age <= 2.076 | 1.0 | 0.335907 |
| Class > -0.45080000000000003 and Class <= 0.49319999999999997 and Sex <= -0.6995 and Age <= 2.076 | -1.0 | 0.112235 |
| Class > -0.45080000000000003 and Class <= 0.49319999999999997 and Sex > -0.6995 | -1.0 | 0.031330 |
| Class <= -0.45080000000000003 | 1.0 | 0.434109 |
| Class <= 0.49319999999999997 | 1.0 | 0.849864 |
|  | 1.0 | 0.868182 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Sex <= -1.92 | 1.0 | 0.148066 |
| Age >= 4.38 and Class <= -0.923 | 1.0 | 0.011799 |
|  | -1.0 | 0.810157 |


# Text representation of classifiers as-is

## JRip

Decision list:

rules | predicted class
---|---
(Sex <= -1.92)|1.0 (422.0/112.0)
(Age >= 4.38) and (Class <= -0.923)|1.0 (16.0/0.0)
|-1.0 (1542.0/314.0)


## PART

Decision list:

rules | predicted class
---|---
Sex > -0.6995 AND Age <= 2.076 AND Class > -1.3965 AND Class > -0.45080000000000003 AND Class > 0.49319999999999997|-1.0 (768.0/172.0)
Sex > -0.6995 AND Class > -1.3965 AND Age <= 2.076 AND Class > -0.45080000000000003|-1.0 (417.0/68.0)
Sex > -0.6995 AND Age <= 2.076 AND Class <= -1.3965|-1.0 (155.0/50.0)
Sex > -0.6995 AND Age <= 2.076|-1.0 (155.0/12.0)
Class <= -0.45080000000000003 AND Age <= 2.076 AND Class <= -1.3965|1.0 (123.0/4.0)
Class <= -0.45080000000000003 AND Age <= 2.076|1.0 (85.0/11.0)
Class > -0.45080000000000003 AND Class <= 0.49319999999999997 AND Sex <= -0.6995 AND Age <= 2.076|-1.0 (155.0/72.0)
Class > -0.45080000000000003 AND Class <= 0.49319999999999997 AND Sex > -0.6995|-1.0 (47.0/12.0)
Class <= -0.45080000000000003|1.0 (28.0)
Class <= 0.49319999999999997|1.0 (26.0/12.0)
|1.0 (21.0/2.0)


## SimpleCart Decision Tree

* Sex < -0.6995
	* Class < -0.45080000000000003: 1.0(205.0/15.0)
	* Class >= -0.45080000000000003
		* Class < 0.49319999999999997
			* Age < 2.076: -1.0(83.0/72.0)
			* Age >= 2.076: 1.0(14.0/12.0)
		* Class >= 0.49319999999999997: 1.0(19.0/2.0)
* Sex >= -0.6995
	* Age < 2.076
		* Class < -1.3965: -1.0(105.0/50.0)
		* Class >= -1.3965
			* Class < 0.49319999999999997
				* Class < -0.45080000000000003: -1.0(143.0/12.0)
				* Class >= -0.45080000000000003: -1.0(349.0/68.0)
			* Class >= 0.49319999999999997: -1.0(596.0/172.0)
	* Age >= 2.076: -1.0(35.0/28.0)


