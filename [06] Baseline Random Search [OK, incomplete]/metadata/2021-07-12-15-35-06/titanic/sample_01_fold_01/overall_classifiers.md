# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Sex >= -0.6995 | -1.0 | 0.630559 |
| Sex < -0.6995 | 1.0 | 0.150618 |
| Sex <= -0.6995 and Class > -0.45080000000000003 and Class <= 0.49319999999999997 | -1.0 | 0.071245 |
| Sex > -0.6995 and Age > 2.076 and Class <= -0.45080000000000003 | 1.0 | 0.011070 |

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


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Sex <= -1.92 and Class <= -1.87 | 1.0 | 0.085406 |
| Sex <= -1.92 and Class <= -0.923 and Age >= 4.38 | 1.0 | 0.009608 |
| Sex <= -1.92 and Class <= -0.923 | 1.0 | 0.041093 |
| Sex <= -1.92 and Class >= 0.965 | 1.0 | 0.012816 |
|  | -1.0 | 0.767468 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

class|age|sex|survived
---|---|---|---
(-inf--1.3965]|(2.076-inf)|(-0.6995-inf)|1.0
(-0.4508-inf)|(2.076-inf)|(-0.6995-inf)|-1.0
(-1.3965--0.4508]|(2.076-inf)|(-0.6995-inf)|1.0
(-1.3965--0.4508]|(-inf-2.076]|(-0.6995-inf)|-1.0
(-inf--1.3965]|(-inf-2.076]|(-0.6995-inf)|-1.0
(-0.4508-inf)|(-inf-2.076]|(-0.6995-inf)|-1.0
(-1.3965--0.4508]|(2.076-inf)|(-inf--0.6995]|1.0
(-0.4508-inf)|(2.076-inf)|(-inf--0.6995]|-1.0
(-inf--1.3965]|(2.076-inf)|(-inf--0.6995]|-1.0
(-0.4508-inf)|(-inf-2.076]|(-inf--0.6995]|1.0
(-inf--1.3965]|(-inf-2.076]|(-inf--0.6995]|1.0
(-1.3965--0.4508]|(-inf-2.076]|(-inf--0.6995]|1.0

## JRip

Decision list:

rules | predicted class
---|---
(Sex <= -1.92) and (Class <= -1.87)|1.0 (133.0/4.0)
(Sex <= -1.92) and (Class <= -0.923) and (Age >= 4.38)|1.0 (13.0/0.0)
(Sex <= -1.92) and (Class <= -0.923)|1.0 (84.0/13.0)
(Sex <= -1.92) and (Class >= 0.965)|1.0 (23.0/3.0)
|-1.0 (1726.0/406.0)


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
	* Class <= -0.45080000000000003: 1.0 (230.0/17.0)
	* Class > -0.45080000000000003
		* Class <= 0.49319999999999997: -1.0 (168.0/80.0)
		* Class > 0.49319999999999997: 1.0 (23.0/3.0)
* Sex > -0.6995
	* Age <= 2.076: -1.0 (1498.0/299.0)
	* Age > 2.076
		* Class <= -0.45080000000000003: 1.0 (15.0)
		* Class > -0.45080000000000003: -1.0 (45.0/12.0)


## SimpleCart Decision Tree

* Sex < -0.6995: 1.0(313.0/108.0)
* Sex >= -0.6995: -1.0(1232.0/326.0)


