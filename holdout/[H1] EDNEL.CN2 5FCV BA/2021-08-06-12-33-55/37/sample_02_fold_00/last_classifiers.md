# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| plas < 127.5 and age < 28.5 | 0 | 0.421495 |
| plas >= 127.5 and mass >= 29.95 and plas >= 157.5 | 1 | 0.130024 |
| plas < 127.5 and age >= 28.5 and mass >= 26.95 and plas < 107.5 and pedi < 0.6375 | 0 | 0.141317 |
| plas > 120.5 and plas <= 155.5 and mass > 27.35 and pedi = all and age > 30.5 | 1 | 0.087904 |
| plas < 127.5 and age >= 28.5 and mass < 26.95 | 0 | 0.135870 |
| plas > 99.5 and plas <= 120.5 and mass > 27.35 and pedi = all and age > 30.5 | 1 | 0.040375 |
| plas > 120.5 and plas <= 155.5 and mass > 27.35 and pedi = all and age <= 30.5 | 0 | 0.088850 |
| plas >= 127.5 and mass < 29.95 and plas < 160.0 and mass < 27.45 and preg < 2.5 | 0 | 0.066038 |
| plas < 127.5 and age >= 28.5 and mass >= 26.95 and plas >= 107.5 and insu >= 39.0 | 0 | 0.037335 |
| plas >= 127.5 and mass < 29.95 and plas < 160.0 and mass < 27.45 and preg >= 2.5 | 0 | 0.037523 |
| plas >= 127.5 and mass < 29.95 and plas >= 160.0 | 1 | 0.020704 |
| plas >= 127.5 and mass >= 29.95 and plas < 157.5 and age < 42.5 and insu < 199.0 and pedi >= 0.61 | 1 | 0.035613 |
| plas >= 127.5 and mass < 29.95 and plas < 160.0 and mass >= 27.45 | 0 | 0.030941 |
| plas >= 127.5 and mass >= 29.95 and plas < 157.5 and age < 42.5 and insu < 199.0 and pedi < 0.61 | 0 | 0.040404 |
| plas < 127.5 and age >= 28.5 and mass >= 26.95 and plas < 107.5 and pedi >= 0.6375 | 1 | 0.014846 |
| plas >= 127.5 and mass >= 29.95 and plas < 157.5 and age < 42.5 and insu >= 199.0 | 0 | 0.046377 |
| plas <= 99.5 and mass > 27.35 and pedi = all and age > 30.5 | 0 | 0.088090 |
| plas < 127.5 and age >= 28.5 and mass >= 26.95 and plas >= 107.5 and insu < 39.0 | 1 | 0.051781 |
| plas > 155.5 and mass <= 27.35 and pedi = all and age <= 30.5 | 0 | 0.010000 |
| plas > 99.5 and plas <= 120.5 and mass <= 27.35 and pedi = all and age > 30.5 | 0 | 0.066333 |
| plas > 155.5 and mass <= 27.35 and pedi = all and age > 30.5 | 1 | 0.018551 |
| plas > 99.5 and plas <= 120.5 and mass > 27.35 and pedi = all and age <= 30.5 | 0 | 0.157253 |
| plas > 155.5 and mass > 27.35 and pedi = all and age > 30.5 | 1 | 0.094584 |
| plas <= 99.5 and mass > 27.35 and pedi = all and age <= 30.5 | 0 | 0.179725 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| plas <= 120.5 and mass > 26.95 and age <= 30.5 | 0 | 0.300877 |
| mass <= 27.35 and plas <= 153.5 and skin > 13.5 | 0 | 0.232558 |
| plas > 155.5 | 1 | 0.246810 |
| mass <= 26.9 and preg <= 2.5 | 0 | 0.207547 |
| plas <= 94.5 and pedi <= 0.6685 | 0 | 0.162000 |
|  | 1 | 0.510121 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

plas|mass|pedi|age|target
---|---|---|---|---
(155.5-inf)|(27.35-inf)|all|(30.5-inf)|1
(99.5-120.5]|(27.35-inf)|all|(30.5-inf)|1
(-inf-99.5]|(27.35-inf)|all|(30.5-inf)|0
(120.5-155.5]|(27.35-inf)|all|(30.5-inf)|1
(99.5-120.5]|(-inf-27.35]|all|(30.5-inf)|0
(155.5-inf)|(-inf-27.35]|all|(30.5-inf)|1
(120.5-155.5]|(-inf-27.35]|all|(30.5-inf)|0
(-inf-99.5]|(-inf-27.35]|all|(30.5-inf)|0
(155.5-inf)|(27.35-inf)|all|(-inf-30.5]|1
(99.5-120.5]|(27.35-inf)|all|(-inf-30.5]|0
(120.5-155.5]|(27.35-inf)|all|(-inf-30.5]|0
(-inf-99.5]|(27.35-inf)|all|(-inf-30.5]|0
(120.5-155.5]|(-inf-27.35]|all|(-inf-30.5]|0
(-inf-99.5]|(-inf-27.35]|all|(-inf-30.5]|0
(155.5-inf)|(-inf-27.35]|all|(-inf-30.5]|0
(99.5-120.5]|(-inf-27.35]|all|(-inf-30.5]|0

## PART

Decision list:

rules | predicted class
---|---
plas <= 120.5 AND mass > 26.95 AND age <= 30.5|0 (114.0/16.0)
mass <= 27.35 AND plas <= 153.5 AND skin > 13.5|0 (60.0)
plas > 155.5|1 (89.0/17.0)
mass <= 26.9 AND preg <= 2.5|0 (30.0)
plas <= 94.5 AND pedi <= 0.6685|0 (28.0/1.0)
|1 (216.0/107.0)


## SimpleCart Decision Tree

* plas < 127.5
	* age < 28.5: 0(157.0/15.0)
	* age >= 28.5
		* mass < 26.95: 0(33.0/2.0)
		* mass >= 26.95
			* plas < 107.5
				* pedi < 0.6375: 0(39.0/8.0)
				* pedi >= 0.6375: 1(9.0/7.0)
			* plas >= 107.5
				* insu < 39.0: 1(25.0/9.0)
				* insu >= 39.0: 0(12.0/7.0)
* plas >= 127.5
	* mass < 29.95
		* plas < 160.0
			* mass < 27.45
				* preg < 2.5: 0(14.0/0.0)
				* preg >= 2.5: 0(10.0/3.0)
			* mass >= 27.45: 0(10.0/6.0)
		* plas >= 160.0: 1(10.0/4.0)
	* mass >= 29.95
		* plas < 157.5
			* age < 42.5
				* insu < 199.0
					* pedi < 0.61: 0(16.0/16.0)
					* pedi >= 0.61: 1(15.0/3.0)
				* insu >= 199.0: 0(12.0/3.0)
			* age >= 42.5: 1(20.0/3.0)
		* plas >= 157.5: 1(59.0/10.0)


