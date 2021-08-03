# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Sex > -1.92 and Age <= -0.228 | -1.0 | 0.622848 |
| Sex <= -1.92 and Class <= -0.923 | 1.0 | 0.127122 |
| Sex <= -1.92 and Class > -0.923 and Class <= 0.0214 | -1.0 | 0.078311 |
| Sex > -1.92 and Age > -0.228 and Class <= -0.923 | 1.0 | 0.011070 |
| Sex <= -1.92 and Class > -0.923 and Class > 0.0214 | 1.0 | 0.009246 |
| Class > -0.4508 and Age > 2.076 and Sex > -0.6995 | -1.0 | 0.033310 |

## Ordered rules

### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Sex <= -1.92 and Class <= -0.923 | 1.0 | 0.127122 |
| Sex <= -1.92 and Class >= 0.965 | 1.0 | 0.009246 |
|  | -1.0 | 0.763098 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

class|age|sex|survived
---|---|---|---
(-1.3965--0.4508]|(2.076-inf)|(-0.6995-inf)|1.0
(-inf--1.3965]|(2.076-inf)|(-0.6995-inf)|1.0
(-0.4508-inf)|(2.076-inf)|(-0.6995-inf)|-1.0
(-1.3965--0.4508]|(-inf-2.076]|(-0.6995-inf)|-1.0
(-0.4508-inf)|(-inf-2.076]|(-0.6995-inf)|-1.0
(-inf--1.3965]|(-inf-2.076]|(-0.6995-inf)|-1.0
(-inf--1.3965]|(2.076-inf)|(-inf--0.6995]|-1.0
(-1.3965--0.4508]|(2.076-inf)|(-inf--0.6995]|1.0
(-0.4508-inf)|(2.076-inf)|(-inf--0.6995]|-1.0
(-1.3965--0.4508]|(-inf-2.076]|(-inf--0.6995]|1.0
(-inf--1.3965]|(-inf-2.076]|(-inf--0.6995]|1.0
(-0.4508-inf)|(-inf-2.076]|(-inf--0.6995]|-1.0

## JRip

Decision list:

rules | predicted class
---|---
(Sex <= -1.92) and (Class <= -0.923)|1.0 (224.0/15.0)
(Sex <= -1.92) and (Class >= 0.965)|1.0 (18.0/3.0)
|-1.0 (1738.0/416.0)


## J48 Decision Tree

* Sex <= -1.92
	* Class <= -0.923: 1.0 (224.0/15.0)
	* Class > -0.923
		* Class <= 0.0214: -1.0 (172.0/78.0)
		* Class > 0.0214: 1.0 (18.0/3.0)
* Sex > -1.92
	* Age <= -0.228: -1.0 (1510.0/312.0)
	* Age > -0.228
		* Class <= -0.923: 1.0 (15.0)
		* Class > -0.923: -1.0 (41.0/11.0)


