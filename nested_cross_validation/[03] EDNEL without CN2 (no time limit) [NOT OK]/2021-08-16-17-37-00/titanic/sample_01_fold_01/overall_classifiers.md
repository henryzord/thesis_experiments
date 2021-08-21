# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Sex >= -0.6995 and Age < 2.076 and Class >= -1.3965 and Class >= 0.49319999999999997 | -1.0 | 0.438000 |
| Sex >= -0.6995 and Age < 2.076 and Class >= -1.3965 and Class < 0.49319999999999997 and Class >= -0.45080000000000003 | -1.0 | 0.322007 |
| Sex < -0.6995 and Class < -0.45080000000000003 and Class < -1.3965 | 1.0 | 0.085406 |
| Sex >= -0.6995 and Age < 2.076 and Class >= -1.3965 and Class < 0.49319999999999997 and Class < -0.45080000000000003 | -1.0 | 0.170267 |
| Sex < -0.6995 and Class < -0.45080000000000003 and Class >= -1.3965 and Age < 2.076 | 1.0 | 0.042927 |
| Sex >= -0.6995 and Age < 2.076 and Class < -1.3965 | -1.0 | 0.098551 |
| Sex < -0.6995 and Class >= -0.45080000000000003 and Class >= 0.49319999999999997 | 1.0 | 0.012816 |
| Sex >= -0.6995 and Age >= 2.076 and Class < -0.45080000000000003 | 1.0 | 0.011070 |
| Sex < -0.6995 and Class >= -0.45080000000000003 and Class < 0.49319999999999997 and Age < 2.076 | -1.0 | 0.060119 |
| Sex < -0.6995 and Class < -0.45080000000000003 and Class >= -1.3965 and Age >= 2.076 | 1.0 | 0.009608 |
| Sex >= -0.6995 and Age >= 2.076 and Class >= -0.45080000000000003 | -1.0 | 0.036667 |
| Sex < -0.6995 and Class >= -0.45080000000000003 and Class < 0.49319999999999997 and Age >= 2.076 | -1.0 | 0.011343 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Sex > -1.92 and Age <= -0.228 | -1.0 | 0.623574 |
| Class <= -0.923 | 1.0 | 0.662502 |
| Class <= 0.0214 | -1.0 | 0.196289 |
|  | 1.0 | 0.991453 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Sex <= -1.92 | 1.0 | 0.150618 |
| Class <= -1.87 and Age >= 4.38 | 1.0 | 0.002976 |
|  | -1.0 | 0.806258 |


# Text representation of classifiers as-is

## JRip

Decision list:

rules | predicted class
---|---
(Sex <= -1.92)|1.0 (421.0/108.0)
(Class <= -1.87) and (Age >= 4.38)|1.0 (4.0/0.0)
|-1.0 (1554.0/322.0)


## PART

Decision list:

rules | predicted class
---|---
Sex > -1.92 AND Age <= -0.228|-1.0 (1498.0/299.0)
Class <= -0.923|1.0 (245.0/17.0)
Class <= 0.0214|-1.0 (213.0/92.0)
|1.0 (23.0/3.0)


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
		* Class < -1.3965: -1.0(102.0/51.0)
		* Class >= -1.3965
			* Class < 0.49319999999999997
				* Class < -0.45080000000000003: -1.0(142.0/12.0)
				* Class >= -0.45080000000000003: -1.0(353.0/64.0)
			* Class >= 0.49319999999999997: -1.0(602.0/172.0)
	* Age >= 2.076
		* Class < -0.45080000000000003: 1.0(15.0/0.0)
		* Class >= -0.45080000000000003: -1.0(33.0/12.0)


