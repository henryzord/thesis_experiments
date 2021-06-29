# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Sex > -1.92 | -1.0 | 0.628697 |
| Sex <= -1.92 and Class <= -0.923 | 1.0 | 0.128335 |
| Sex <= -1.92 and Class > -0.923 and Class <= 0.0214 | -1.0 | 0.079823 |
| Sex <= -1.92 and Class > -0.923 and Class > 0.0214 | 1.0 | 0.009958 |

## Ordered rules

### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Sex <= -1.92 | 1.0 | 0.146291 |
|  | -1.0 | 0.801435 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

class|age|sex|survived
---|---|---|---
(-inf--1.3965]|(2.076-inf)|(-0.6995-inf)|1.0
(-1.3965--0.4508]|(2.076-inf)|(-0.6995-inf)|1.0
(-0.4508-inf)|(2.076-inf)|(-0.6995-inf)|-1.0
(-1.3965--0.4508]|(-inf-2.076]|(-0.6995-inf)|-1.0
(-inf--1.3965]|(-inf-2.076]|(-0.6995-inf)|-1.0
(-0.4508-inf)|(-inf-2.076]|(-0.6995-inf)|-1.0
(-inf--1.3965]|(2.076-inf)|(-inf--0.6995]|-1.0
(-1.3965--0.4508]|(2.076-inf)|(-inf--0.6995]|1.0
(-0.4508-inf)|(2.076-inf)|(-inf--0.6995]|-1.0
(-inf--1.3965]|(-inf-2.076]|(-inf--0.6995]|1.0
(-1.3965--0.4508]|(-inf-2.076]|(-inf--0.6995]|1.0
(-0.4508-inf)|(-inf-2.076]|(-inf--0.6995]|-1.0

## JRip

Decision list:

rules | predicted class
---|---
(Sex <= -1.92)|1.0 (423.0/115.0)
|-1.0 (1557.0/332.0)


## J48 Decision Tree

* Sex <= -1.92
	* Class <= -0.923: 1.0 (206.0/15.0)
	* Class > -0.923
		* Class <= 0.0214: -1.0 (153.0/71.0)
		* Class > 0.0214: 1.0 (17.0/3.0)
* Sex > -1.92: -1.0 (1406.0/300.0)


