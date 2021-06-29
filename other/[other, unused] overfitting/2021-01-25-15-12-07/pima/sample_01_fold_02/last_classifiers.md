# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | tested_negative | 0.652174 |
| Plas > 119.5 and Mass > 27.55 and Plas <= 155.5 and Mass <= 41.65 and Age > 41.5 | tested_positive | 0.041122 |
| Plas > 157.5 and Mass <= 27.35 and Pedi = all and Age > 28.5 | tested_positive | 0.010793 |
| Plas > 157.5 and Mass > 27.35 and Pedi = all and Age > 28.5 | tested_positive | 0.093506 |
| Plas > 119.5 and Mass > 27.55 and Plas > 155.5 | tested_positive | 0.128167 |
| Plas > 119.5 and Mass > 27.55 and Plas <= 155.5 and Mass <= 41.65 and Age <= 41.5 and Insu <= 192 and Pedi > 0.73 | tested_positive | 0.016584 |
| Plas > 123.5 and Plas <= 157.5 and Mass > 27.35 and Pedi = all and Age > 28.5 | tested_positive | 0.078126 |
| Plas > 119.5 and Mass > 27.55 and Plas <= 155.5 and Mass > 41.65 | tested_positive | 0.033156 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Plas <= 123.0 and Preg <= 4.5 and Mass <= 32.25 | tested_negative | 0.385604 |
| Plas > 143.5 | tested_positive | 0.217517 |
| Plas <= 99.5 and Pres <= 75.0 | tested_negative | 0.239225 |
| Mass > 27.35 and Age <= 31.5 | tested_negative | 0.403062 |
| Mass <= 27.35 | tested_negative | 0.284362 |
| Pedi > 0.52 | tested_positive | 0.388273 |
| Insu > 123.5 | tested_positive | 0.099426 |
| Age <= 38.5 and Preg <= 5.5 and Plas <= 123.0 | tested_negative | 0.045752 |
|  | tested_negative | 0.536000 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Plas >= 156 | tested_positive | 0.133611 |
| Age >= 31 and Mass >= 28.3 and Plas >= 108 | tested_positive | 0.088542 |
| Preg >= 7 and Age <= 32 | tested_positive | 0.014803 |
|  | tested_negative | 0.855513 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

plas|mass|pedi|age|class
---|---|---|---|---
(-inf-99.5]|(27.35-inf)|all|(28.5-inf)|tested_negative
(157.5-inf)|(27.35-inf)|all|(28.5-inf)|tested_positive
(123.5-157.5]|(27.35-inf)|all|(28.5-inf)|tested_positive
(99.5-123.5]|(27.35-inf)|all|(28.5-inf)|tested_negative
(123.5-157.5]|(-inf-27.35]|all|(28.5-inf)|tested_negative
(99.5-123.5]|(-inf-27.35]|all|(28.5-inf)|tested_negative
(-inf-99.5]|(-inf-27.35]|all|(28.5-inf)|tested_negative
(157.5-inf)|(-inf-27.35]|all|(28.5-inf)|tested_positive
(-inf-99.5]|(27.35-inf)|all|(-inf-28.5]|tested_negative
(99.5-123.5]|(27.35-inf)|all|(-inf-28.5]|tested_negative
(123.5-157.5]|(27.35-inf)|all|(-inf-28.5]|tested_negative
(157.5-inf)|(27.35-inf)|all|(-inf-28.5]|tested_positive
(157.5-inf)|(-inf-27.35]|all|(-inf-28.5]|tested_negative
(123.5-157.5]|(-inf-27.35]|all|(-inf-28.5]|tested_negative
(99.5-123.5]|(-inf-27.35]|all|(-inf-28.5]|tested_negative
(-inf-99.5]|(-inf-27.35]|all|(-inf-28.5]|tested_negative

## JRip

Decision list:

rules | predicted class
---|---
(Plas >= 156)|tested_positive (105.0/20.0)
(Age >= 31) and (Mass >= 28.3) and (Plas >= 108)|tested_positive (109.0/39.0)
(Preg >= 7) and (Age <= 32)|tested_positive (12.0/3.0)
|tested_negative (464.0/76.0)


## PART

Decision list:

rules | predicted class
---|---
Plas <= 123.0 AND Preg <= 4.5 AND Mass <= 32.25|tested_negative (80.0/1.0)
Plas > 143.5|tested_positive (71.0/17.0)
Plas <= 99.5 AND Pres <= 75.0|tested_negative (28.0)
Mass > 27.35 AND Age <= 31.5|tested_negative (71.0/22.0)
Mass <= 27.35|tested_negative (31.0/3.0)
Pedi > 0.52|tested_positive (20.0/2.0)
Insu > 123.5|tested_positive (6.0)
Age <= 38.5 AND Preg <= 5.5 AND Plas <= 123.0|tested_negative (3.0/1.0)
|tested_negative (35.0/15.0)


## J48 Decision Tree

* Plas <= 119.5: tested_negative (171.0/24.0)
* Plas > 119.5
	* Mass <= 27.55: tested_negative (30.0/5.0)
	* Mass > 27.55
		* Plas <= 155.5
			* Mass <= 41.65
				* Age <= 41.5
					* Insu <= 192
						* Pedi <= 0.73: tested_negative (37.0/13.0)
						* Pedi > 0.73: tested_positive (11.0/3.0)
					* Insu > 192: tested_negative (11.0/1.0)
				* Age > 41.5: tested_positive (24.0/6.0)
			* Mass > 41.65: tested_positive (14.0/2.0)
		* Plas > 155.5: tested_positive (47.0/8.0)


