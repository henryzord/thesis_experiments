# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | tested_negative | 0.652174 |
| Plas > 157.5 and Mass > 27.35 and Age <= 28.5 | tested_positive | 0.037773 |
| Plas > 110.5 and Mass > 27.45 and Plas <= 157.5 and Preg > 7.5 | tested_positive | 0.046804 |
| Plas > 157.5 and Mass > 27.35 and Age > 28.5 | tested_positive | 0.093506 |
| Plas > 123.5 and Plas <= 157.5 and Mass > 27.35 and Age > 28.5 | tested_positive | 0.078126 |
| Plas > 157.5 and Mass <= 27.35 and Age > 28.5 | tested_positive | 0.010793 |
| Plas >= 127.5 and Mass >= 29.95 | tested_positive | 0.182747 |
| Plas > 110.5 and Mass > 27.45 and Plas <= 157.5 and Preg <= 7.5 and Age > 44.5 | tested_positive | 0.017988 |
| Plas > 110.5 and Mass > 27.45 and Plas <= 157.5 and Preg <= 7.5 and Age <= 44.5 and Mass > 42.5 | tested_positive | 0.025296 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Plas <= 123.5 | tested_negative | 0.545080 |
| Plas > 157.5 | tested_positive | 0.367432 |
| Age <= 24.5 and Mass <= 28.8 | tested_negative | 0.118212 |
| Preg > 7.5 | tested_positive | 0.264915 |
| Mass <= 42.5 and Pres > 73 and Age <= 31 | tested_negative | 0.147437 |
|  | tested_positive | 0.619565 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

plas|mass|age|class
---|---|---|---
(157.5-inf)|(27.35-inf)|(28.5-inf)|tested_positive
(99.5-123.5]|(27.35-inf)|(28.5-inf)|tested_negative
(123.5-157.5]|(27.35-inf)|(28.5-inf)|tested_positive
(-inf-99.5]|(27.35-inf)|(28.5-inf)|tested_negative
(-inf-99.5]|(-inf-27.35]|(28.5-inf)|tested_negative
(157.5-inf)|(-inf-27.35]|(28.5-inf)|tested_positive
(123.5-157.5]|(-inf-27.35]|(28.5-inf)|tested_negative
(99.5-123.5]|(-inf-27.35]|(28.5-inf)|tested_negative
(157.5-inf)|(27.35-inf)|(-inf-28.5]|tested_positive
(-inf-99.5]|(27.35-inf)|(-inf-28.5]|tested_negative
(123.5-157.5]|(27.35-inf)|(-inf-28.5]|tested_negative
(99.5-123.5]|(27.35-inf)|(-inf-28.5]|tested_negative
(157.5-inf)|(-inf-27.35]|(-inf-28.5]|tested_negative
(123.5-157.5]|(-inf-27.35]|(-inf-28.5]|tested_negative
(99.5-123.5]|(-inf-27.35]|(-inf-28.5]|tested_negative
(-inf-99.5]|(-inf-27.35]|(-inf-28.5]|tested_negative

## PART

Decision list:

rules | predicted class
---|---
Plas <= 123.5|tested_negative (350.0/60.0)
Plas > 157.5|tested_positive (88.0/14.0)
Age <= 24.5 AND Mass <= 28.8|tested_negative (21.0)
Preg > 7.5|tested_positive (30.0/7.0)
Mass <= 42.5 AND Pres > 73 AND Age <= 31|tested_negative (25.0/3.0)
|tested_positive (78.0/32.0)


## J48 Decision Tree

* Plas <= 110.5: tested_negative (146.0/16.0)
* Plas > 110.5
	* Mass <= 27.45: tested_negative (39.0/6.0)
	* Mass > 27.45
		* Plas <= 157.5
			* Preg <= 7.5
				* Age <= 44.5
					* Mass <= 42.5: tested_negative (78.0/30.0)
					* Mass > 42.5: tested_positive (9.0/2.0)
				* Age > 44.5: tested_positive (8.0/1.0)
			* Preg > 7.5: tested_positive (20.0/4.0)
		* Plas > 157.5: tested_positive (45.0/7.0)


## SimpleCart Decision Tree

* Plas < 127.5: tested_negative(353.0/85.0)
* Plas >= 127.5
	* Mass < 29.95: tested_negative(47.0/21.0)
	* Mass >= 29.95: tested_positive(134.0/50.0)


