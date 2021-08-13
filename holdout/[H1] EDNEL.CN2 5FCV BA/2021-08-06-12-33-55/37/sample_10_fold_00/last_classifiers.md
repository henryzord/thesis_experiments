# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| plas <= 123.5 and preg <= 6.5 | 0 | 0.507365 |
| plas > 123.5 and mass > 29.95 and pres > 55.0 and age > 24.5 and plas > 147.5 | 1 | 0.129032 |
| plas > 123.5 and mass <= 29.95 | 0 | 0.143566 |
| plas < 123.5 and preg >= 6.5 and plas >= 99.5 and pedi >= 0.238 | 1 | 0.041732 |
| plas >= 123.5 and mass >= 29.95 and plas < 154.5 and mass < 40.95 and age < 40.5 and pedi < 0.8395 | 0 | 0.105919 |
| plas > 123.5 and mass > 29.95 and pres > 55.0 and age > 24.5 and plas <= 147.5 and mass <= 40.900000000000006 and age > 40.5 | 1 | 0.039682 |
| plas >= 123.5 and mass >= 29.95 and plas < 154.5 and mass >= 40.95 | 1 | 0.044848 |
| plas > 123.5 and mass > 29.95 and pres <= 55.0 | 1 | 0.036620 |
| plas < 123.5 and preg >= 6.5 and plas < 99.5 | 0 | 0.074534 |
| plas >= 123.5 and mass < 29.95 and plas >= 160.0 | 1 | 0.014270 |
| plas < 123.5 and preg < 6.5 and plas < 114.5 and pedi >= 0.6735 and pedi < 0.9245 and pres < 67.0 | 1 | 0.008098 |
| plas >= 123.5 and mass >= 29.95 and plas < 154.5 and mass < 40.95 and age < 40.5 and pedi >= 0.8395 | 1 | 0.020057 |
| plas >= 123.5 and mass < 29.95 and plas < 160.0 and plas < 125.5 | 1 | 0.009084 |
| plas >= 123.5 and mass >= 29.95 and plas >= 154.5 and pedi >= 0.431 | 1 | 0.085640 |
| plas < 123.5 and preg >= 6.5 and plas >= 99.5 and pedi < 0.238 | 0 | 0.027637 |
| plas <= 123.5 and preg > 6.5 and skin <= 39.5 and plas > 89.5 | 1 | 0.038866 |
| preg > 6.5 and plas > 99.5 and plas <= 114.5 and pres = all and mass <= 27.35 | 0 | 0.021259 |
| preg <= 6.5 and plas > 154.5 and pres = all and mass <= 27.35 | 1 | 0.006664 |
| plas > 123.5 and mass > 29.95 and pres > 55.0 and age <= 24.5 | 0 | 0.048129 |
| preg > 6.5 and plas > 114.5 and plas <= 154.5 and pres = all and mass <= 27.35 | 0 | 0.018315 |
| preg <= 6.5 and plas > 114.5 and plas <= 154.5 and pres = all and mass > 27.35 | 0 | 0.178667 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| plas <= 114.5 and preg <= 6.5 | 0 | 0.478805 |
| plas > 154.5 and mass > 28.799999999999997 | 1 | 0.265634 |
| pedi <= 0.915 and plas <= 99.5 | 0 | 0.091268 |
| pedi > 0.915 | 1 | 0.095830 |
| pres <= 23.0 | 1 | 0.054555 |
| mass > 40.95 and pedi > 0.1765 and pedi <= 0.373 | 1 | 0.075862 |
| age <= 28.5 and insu <= 199.0 and pedi > 0.20400000000000001 and mass > 25.15 and pedi <= 0.709 and pedi <= 0.527 and pedi <= 0.4335 and pedi <= 0.421 and mass > 32.0 | 0 | 0.100840 |
| age <= 28.5 | 0 | 0.282604 |
| insu > 142.0 and skin > 16.0 and pres > 75.0 | 1 | 0.127259 |
| pres > 71.0 and plas > 164.0 and preg <= 5.5 | 1 | 0.013699 |
|  | 0 | 0.486667 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

preg|plas|pres|mass|target
---|---|---|---|---
(6.5-inf)|(154.5-inf)|all|(27.35-inf)|1
(-inf-6.5]|(154.5-inf)|all|(27.35-inf)|1
(-inf-6.5]|(114.5-154.5]|all|(27.35-inf)|0
(6.5-inf)|(114.5-154.5]|all|(27.35-inf)|1
(6.5-inf)|(99.5-114.5]|all|(27.35-inf)|1
(-inf-6.5]|(99.5-114.5]|all|(27.35-inf)|0
(-inf-6.5]|(154.5-inf)|all|(-inf-27.35]|1
(6.5-inf)|(154.5-inf)|all|(-inf-27.35]|1
(6.5-inf)|(-inf-99.5]|all|(27.35-inf)|0
(-inf-6.5]|(-inf-99.5]|all|(27.35-inf)|0
(6.5-inf)|(114.5-154.5]|all|(-inf-27.35]|0
(-inf-6.5]|(114.5-154.5]|all|(-inf-27.35]|0
(6.5-inf)|(99.5-114.5]|all|(-inf-27.35]|0
(-inf-6.5]|(99.5-114.5]|all|(-inf-27.35]|0
(6.5-inf)|(-inf-99.5]|all|(-inf-27.35]|0
(-inf-6.5]|(-inf-99.5]|all|(-inf-27.35]|0

## PART

Decision list:

rules | predicted class
---|---
plas <= 114.5 AND preg <= 6.5|0 (187.0/16.0)
plas > 154.5 AND mass > 28.799999999999997|1 (61.0/7.0)
pedi <= 0.915 AND plas <= 99.5|0 (18.0/2.0)
pedi > 0.915|1 (17.0/3.0)
pres <= 23.0|1 (10.0/2.0)
mass > 40.95 AND pedi > 0.1765 AND pedi <= 0.373|1 (10.0)
age <= 28.5 AND insu <= 199.0 AND pedi > 0.20400000000000001 AND mass > 25.15 AND pedi <= 0.709 AND pedi <= 0.527 AND pedi <= 0.4335 AND pedi <= 0.421 AND mass > 32.0|0 (11.0/1.0)
age <= 28.5|0 (52.0/11.0)
insu > 142.0 AND skin > 16.0 AND pres > 75.0|1 (12.0)
pres > 71.0 AND plas > 164.0 AND preg <= 5.5|1 (2.0)
|0 (101.0/43.0)


## J48 Decision Tree

* plas <= 123.5
	* preg <= 6.5: 0 (227.0/28.0)
	* preg > 6.5
		* skin <= 39.5
			* plas <= 89.5: 0 (10.0/1.0)
			* plas > 89.5: 1 (30.0/12.0)
		* skin > 39.5: 0 (6.0)
* plas > 123.5
	* mass <= 29.95: 0 (58.0/20.0)
	* mass > 29.95
		* pres <= 55.0: 1 (13.0)
		* pres > 55.0
			* age <= 24.5: 0 (26.0/10.0)
			* age > 24.5
				* plas <= 147.5
					* mass <= 40.900000000000006
						* age <= 40.5: 0 (24.0/10.0)
						* age > 40.5: 1 (21.0/5.0)
					* mass > 40.900000000000006: 1 (8.0)
				* plas > 147.5: 1 (52.0/5.0)


## SimpleCart Decision Tree

* plas < 123.5
	* preg < 6.5
		* plas < 114.5
			* pedi < 0.6735: 0(161.0/7.0)
			* pedi >= 0.6735
				* pedi < 0.9245
					* pres < 67.0: 1(5.0/4.0)
					* pres >= 67.0: 0(11.0/3.0)
				* pedi >= 0.9245: 0(14.0/1.0)
		* plas >= 114.5: 0(31.0/15.0)
	* preg >= 6.5
		* plas < 99.5: 0(18.0/3.0)
		* plas >= 99.5
			* pedi < 0.238: 0(7.0/2.0)
			* pedi >= 0.238: 1(20.0/7.0)
* plas >= 123.5
	* mass < 29.95
		* plas < 160.0
			* plas < 125.5: 1(5.0/3.0)
			* plas >= 125.5: 0(37.0/7.0)
		* plas >= 160.0: 1(8.0/5.0)
	* mass >= 29.95
		* plas < 154.5
			* mass < 40.95
				* age < 40.5
					* pedi < 0.8395: 0(31.0/12.0)
					* pedi >= 0.8395: 1(7.0/0.0)
				* age >= 40.5
					* insu < 109.0: 1(8.0/5.0)
					* insu >= 109.0: 1(12.0/0.0)
			* mass >= 40.95: 1(17.0/1.0)
		* plas >= 154.5
			* pedi < 0.431: 1(27.0/6.0)
			* pedi >= 0.431: 1(33.0/1.0)


