# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Plas < 127.5 | tested_negative | 0.560030 |
| Plas >= 127.5 and Mass >= 29.95 | tested_positive | 0.182747 |
| Plas >= 127.5 and Mass < 29.95 | tested_negative | 0.122125 |
| Plas > 123.5 and Plas <= 157.5 and Pres = all and Mass > 27.35 and Pedi = all and Age > 28.5 | tested_positive | 0.078126 |
| Plas > 123.5 and Plas <= 157.5 and Pres = all and Mass > 27.35 and Pedi = all and Age <= 28.5 | tested_negative | 0.087972 |
| Plas > 157.5 and Pres = all and Mass <= 27.35 and Pedi = all and Age > 28.5 | tested_positive | 0.010793 |
| Plas > 123.0 and Age > 24.0 and Mass > 29.9 | tested_positive | 0.172686 |
| Plas > 157.5 and Pres = all and Mass > 27.35 and Pedi = all and Age > 28.5 | tested_positive | 0.093506 |
| Plas > 123.0 and Age <= 24.0 and Plas <= 168.0 | tested_negative | 0.116627 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Plas <= 123.5 and Age <= 25.5 | tested_negative | 0.384852 |
| Mass <= 26.700000000000003 and Plas <= 124.5 | tested_negative | 0.186670 |
| Plas > 157.5 | tested_positive | 0.226397 |
| Mass > 42.25 and Plas > 114.5 | tested_positive | 0.068809 |
| Pedi <= 0.85 and Age <= 30.5 | tested_negative | 0.393124 |
| Plas > 94.5 | tested_positive | 0.465313 |
|  | tested_negative | 0.932331 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Plas >= 128 and Mass >= 30 | tested_positive | 0.182747 |
| Age >= 29 and Insu >= 144 | tested_positive | 0.021259 |
| Age >= 30 and Plas >= 107 and Mass >= 28.2 and Pres <= 84 | tested_positive | 0.025548 |
|  | tested_negative | 0.884086 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

plas|pres|mass|pedi|age|class
---|---|---|---|---|---
(157.5-inf)|all|(27.35-inf)|all|(28.5-inf)|tested_positive
(99.5-123.5]|all|(27.35-inf)|all|(28.5-inf)|tested_negative
(123.5-157.5]|all|(27.35-inf)|all|(28.5-inf)|tested_positive
(-inf-99.5]|all|(27.35-inf)|all|(28.5-inf)|tested_negative
(-inf-99.5]|all|(-inf-27.35]|all|(28.5-inf)|tested_negative
(157.5-inf)|all|(-inf-27.35]|all|(28.5-inf)|tested_positive
(123.5-157.5]|all|(-inf-27.35]|all|(28.5-inf)|tested_negative
(99.5-123.5]|all|(-inf-27.35]|all|(28.5-inf)|tested_negative
(157.5-inf)|all|(27.35-inf)|all|(-inf-28.5]|tested_positive
(-inf-99.5]|all|(27.35-inf)|all|(-inf-28.5]|tested_negative
(99.5-123.5]|all|(27.35-inf)|all|(-inf-28.5]|tested_negative
(123.5-157.5]|all|(27.35-inf)|all|(-inf-28.5]|tested_negative
(157.5-inf)|all|(-inf-27.35]|all|(-inf-28.5]|tested_negative
(123.5-157.5]|all|(-inf-27.35]|all|(-inf-28.5]|tested_negative
(99.5-123.5]|all|(-inf-27.35]|all|(-inf-28.5]|tested_negative
(-inf-99.5]|all|(-inf-27.35]|all|(-inf-28.5]|tested_negative

## JRip

Decision list:

rules | predicted class
---|---
(Plas >= 128) and (Mass >= 30)|tested_positive (184.0/50.0)
(Age >= 29) and (Insu >= 144)|tested_positive (33.0/13.0)
(Age >= 30) and (Plas >= 107) and (Mass >= 28.2) and (Pres <= 84)|tested_positive (37.0/10.0)
|tested_negative (436.0/59.0)


## PART

Decision list:

rules | predicted class
---|---
Plas <= 123.5 AND Age <= 25.5|tested_negative (110.0/2.0)
Mass <= 26.700000000000003 AND Plas <= 124.5|tested_negative (43.0/1.0)
Plas > 157.5|tested_positive (65.0/12.0)
Mass > 42.25 AND Plas > 114.5|tested_positive (14.0)
Pedi <= 0.85 AND Age <= 30.5|tested_negative (94.0/22.0)
Plas > 94.5|tested_positive (115.0/50.0)
|tested_negative (19.0/3.0)


## J48 Decision Tree

* Plas <= 123.0: tested_negative (310.0/57.0)
* Plas > 123.0
	* Age <= 24.0
		* Plas <= 168.0: tested_negative (33.0/4.0)
		* Plas > 168.0: tested_positive (10.0/2.0)
	* Age > 24.0
		* Mass <= 29.9: tested_negative (44.0/19.0)
		* Mass > 29.9: tested_positive (121.0/29.0)


## SimpleCart Decision Tree

* Plas < 127.5: tested_negative(353.0/85.0)
* Plas >= 127.5
	* Mass < 29.95: tested_negative(47.0/21.0)
	* Mass >= 29.95: tested_positive(134.0/50.0)


