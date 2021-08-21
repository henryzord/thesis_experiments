# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 3 | 0.926069 |
| TSH >= 0.00605 and FTI >= 0.064255 and On_thyroxine < 0.5 and TT4 < 0.1505 and Thyroid_surgery < 0.5 | 2 | 0.049102 |
| On_thyroxine > 0.5 and Query_on_thyroxine = all and On_antithyroid_medication = all and Thyroid_surgery <= 0.5 and Query_hyperthyroid = all and Hypopituitary = all and TSH > 0.0195 and TSH <= 0.0415 and TT4 > 0.033875 and TT4 <= 0.0605 | 1 | 0.000316 |
| On_thyroxine > 0.5 and Query_on_thyroxine = all and On_antithyroid_medication = all and Thyroid_surgery <= 0.5 and Query_hyperthyroid = all and Hypopituitary = all and TSH > 0.0415 and TT4 > 0.0605 and TT4 <= 0.0685 | 1 | 0.000284 |
| On_thyroxine <= 0.5 and Query_on_thyroxine = all and On_antithyroid_medication = all and Thyroid_surgery > 0.5 and Query_hyperthyroid = all and Hypopituitary = all and TSH > 0.0195 and TSH <= 0.0415 and TT4 > 0.0605 and TT4 <= 0.0685 | 1 | 0.000158 |
| On_thyroxine > 0.5 and Query_on_thyroxine = all and On_antithyroid_medication = all and Thyroid_surgery <= 0.5 and Query_hyperthyroid = all and Hypopituitary = all and TSH > 0.0415 and TT4 > 0.033875 and TT4 <= 0.0605 | 1 | 0.000158 |
| TSH > 0.006 and FTI <= 0.064 and TSH > 0.01679 | 1 | 0.019709 |
| On_thyroxine <= 0.5 and Query_on_thyroxine = all and On_antithyroid_medication = all and Thyroid_surgery <= 0.5 and Query_hyperthyroid = all and Hypopituitary = all and TSH > 0.00605 and TSH <= 0.0195 and TT4 > 0.033875 and TT4 <= 0.0605 | 1 | 0.000512 |
| On_thyroxine <= 0.5 and Query_on_thyroxine = all and On_antithyroid_medication = all and Thyroid_surgery <= 0.5 and Query_hyperthyroid = all and Hypopituitary = all and TSH > 0.00605 and TSH <= 0.0195 and TT4 > 0.0185 and TT4 <= 0.033875 | 1 | 0.000316 |
| TSH >= 0.00605 and FTI < 0.064255 and T3 < 0.0265 | 1 | 0.021718 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| TSH <= 0.00605 | 3 | 0.924221 |
| FTI <= 0.064255 and TSH > 0.016895 and T3 <= 0.0115 and T4U <= 0.1115 | 1 | 0.131673 |
| FTI <= 0.064255 and T3 <= 0.0235 and TSH > 0.078 | 1 | 0.050584 |
| FTI <= 0.064255 and T3 <= 0.0235 and T4U <= 0.0965 | 1 | 0.025948 |
| FTI <= 0.064255 and TSH > 0.017395 and TT4 > 0.049 | 1 | 0.027888 |
| FTI > 0.06472 and On_thyroxine <= 0.5 and TT4 <= 0.1505 and TT4 > 0.0615 and T3 <= 0.028999999999999998 and Age > 0.425 and T4U <= 0.1275 and TT4 <= 0.1365 | 2 | 0.548872 |
| FTI <= 0.062755 and T3 <= 0.011 | 1 | 0.040238 |
| On_thyroxine > 0.5 | 3 | 0.454545 |
| FTI > 0.062965 and TT4 <= 0.1505 and Thyroid_surgery <= 0.5 and TT4 > 0.058499999999999996 and T3 <= 0.028999999999999998 and Age <= 0.7 | 2 | 0.575949 |
| FTI > 0.063 and TT4 > 0.1495 | 3 | 0.442308 |
| FTI > 0.063 and T4U <= 0.114 and T3 > 0.0187 | 3 | 0.369565 |
| FTI > 0.063 and TT4 > 0.0975 | 2 | 0.341463 |
| T4U > 0.092 and TSH <= 0.028 | 3 | 0.349650 |
| TSH > 0.0235 | 1 | 0.218182 |
|  | 2 | 0.352941 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| FTI <= 0.064 and TSH >= 0.0077 and T3 <= 0.011 and T4U <= 0.111 | 1 | 0.012172 |
| FTI <= 0.064 and TSH >= 0.018 and Age <= 0.66 and Thyroid_surgery <= 0 | 1 | 0.007526 |
| FTI <= 0.064 and TSH >= 0.0062 and T3 <= 0.01 and Age >= 0.52 | 1 | 0.001577 |
| FTI <= 0.064 and FTI >= 0.051 and TSH >= 0.022 | 1 | 0.000789 |
| FTI <= 0.061 and TSH >= 0.0062 and FTI >= 0.048 and T4U <= 0.097 | 1 | 0.000789 |
| FTI <= 0.059 and TT4 >= 0.068 and TSH >= 0.01029 | 1 | 0.000316 |
| TSH >= 0.0061 and On_thyroxine <= 0 and T3 <= 0.02 and FTI >= 0.069 and Thyroid_surgery <= 0 and TT4 <= 0.148 | 2 | 0.038609 |
| TSH >= 0.0061 and On_thyroxine <= 0 and TT4 <= 0.141 and T3 >= 0.0208 and T3 <= 0.026 and FTI >= 0.06493 | 2 | 0.010552 |
| TSH >= 0.0061 and On_thyroxine <= 0 and FTI <= 0.092 and TT4 >= 0.064 and Thyroid_surgery <= 0 and T4U <= 0.107 | 2 | 0.002162 |
| TSH >= 0.0061 and T3 >= 0.027 and T4U >= 0.123 and TT4 <= 0.141 | 2 | 0.001331 |
| TSH >= 0.0063 and TSH <= 0.0065 and FTI <= 0.067 | 2 | 0.000333 |
| TSH >= 0.00879 and Age <= 0.19 and T3 >= 0.027 | 2 | 0.000333 |
|  | 3 | 0.999833 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

on_thyroxine|query_on_thyroxine|on_antithyroid_medication|thyroid_surgery|query_hyperthyroid|hypopituitary|tsh|tt4|class
---|---|---|---|---|---|---|---|---
(0.5-inf)|all|all|(-inf-0.5]|all|all|(0.0195-0.0415]|(0.1505-inf)|1
(-inf-0.5]|all|all|(-inf-0.5]|all|all|(0.0195-0.0415]|(0.1505-inf)|3
(0.5-inf)|all|all|(-inf-0.5]|all|all|(0.0415-inf)|(0.11159-0.1505]|1
(-inf-0.5]|all|all|(-inf-0.5]|all|all|(0.0415-inf)|(0.11159-0.1505]|1
(0.5-inf)|all|all|(-inf-0.5]|all|all|(0.00605-0.0195]|(0.1505-inf)|3
(-inf-0.5]|all|all|(-inf-0.5]|all|all|(0.00605-0.0195]|(0.1505-inf)|3
(-inf-0.5]|all|all|(-inf-0.5]|all|all|(0.0195-0.0415]|(0.11159-0.1505]|2
(0.5-inf)|all|all|(-inf-0.5]|all|all|(0.0195-0.0415]|(0.11159-0.1505]|3
(-inf-0.5]|all|all|(0.5-inf)|all|all|(-inf-0.00605]|(0.1505-inf)|3
(0.5-inf)|all|all|(0.5-inf)|all|all|(-inf-0.00605]|(0.1505-inf)|3
(-inf-0.5]|all|all|(0.5-inf)|all|all|(0.00605-0.0195]|(0.11159-0.1505]|1
(-inf-0.5]|all|all|(-inf-0.5]|all|all|(-inf-0.00605]|(0.1505-inf)|3
(0.5-inf)|all|all|(-inf-0.5]|all|all|(-inf-0.00605]|(0.1505-inf)|3
(-inf-0.5]|all|all|(-inf-0.5]|all|all|(0.00605-0.0195]|(0.11159-0.1505]|2
(0.5-inf)|all|all|(-inf-0.5]|all|all|(0.00605-0.0195]|(0.11159-0.1505]|3
(0.5-inf)|all|all|(0.5-inf)|all|all|(-inf-0.00605]|(0.11159-0.1505]|3
(-inf-0.5]|all|all|(0.5-inf)|all|all|(-inf-0.00605]|(0.11159-0.1505]|3
(0.5-inf)|all|all|(-inf-0.5]|all|all|(-inf-0.00605]|(0.11159-0.1505]|3
(-inf-0.5]|all|all|(-inf-0.5]|all|all|(-inf-0.00605]|(0.11159-0.1505]|3
(0.5-inf)|all|all|(-inf-0.5]|all|all|(0.00605-0.0195]|(0.11109-0.11159]|1
(-inf-0.5]|all|all|(-inf-0.5]|all|all|(0.0195-0.0415]|(0.0895-0.11109]|2
(0.5-inf)|all|all|(-inf-0.5]|all|all|(0.0195-0.0415]|(0.0895-0.11109]|3
(-inf-0.5]|all|all|(-inf-0.5]|all|all|(0.0415-inf)|(0.0685-0.0895]|2
(0.5-inf)|all|all|(-inf-0.5]|all|all|(0.0415-inf)|(0.0685-0.0895]|3
(-inf-0.5]|all|all|(0.5-inf)|all|all|(0.00605-0.0195]|(0.0895-0.11109]|3
(0.5-inf)|all|all|(0.5-inf)|all|all|(0.0195-0.0415]|(0.0685-0.0895]|1
(-inf-0.5]|all|all|(0.5-inf)|all|all|(0.0195-0.0415]|(0.0685-0.0895]|1
(0.5-inf)|all|all|(-inf-0.5]|all|all|(-inf-0.00605]|(0.11109-0.11159]|3
(-inf-0.5]|all|all|(0.5-inf)|all|all|(0.0415-inf)|(0.0605-0.0685]|1
(-inf-0.5]|all|all|(-inf-0.5]|all|all|(-inf-0.00605]|(0.11109-0.11159]|3
(0.5-inf)|all|all|(-inf-0.5]|all|all|(0.00605-0.0195]|(0.0895-0.11109]|3
(-inf-0.5]|all|all|(-inf-0.5]|all|all|(0.00605-0.0195]|(0.0895-0.11109]|2
(-inf-0.5]|all|all|(-inf-0.5]|all|all|(0.0195-0.0415]|(0.0685-0.0895]|2
(0.5-inf)|all|all|(-inf-0.5]|all|all|(0.0195-0.0415]|(0.0685-0.0895]|3
(0.5-inf)|all|all|(-inf-0.5]|all|all|(0.0415-inf)|(0.0605-0.0685]|1
(-inf-0.5]|all|all|(-inf-0.5]|all|all|(0.0415-inf)|(0.0605-0.0685]|2
(0.5-inf)|all|all|(0.5-inf)|all|all|(-inf-0.00605]|(0.0895-0.11109]|3
(-inf-0.5]|all|all|(0.5-inf)|all|all|(-inf-0.00605]|(0.0895-0.11109]|3
(-inf-0.5]|all|all|(0.5-inf)|all|all|(0.00605-0.0195]|(0.0685-0.0895]|3
(-inf-0.5]|all|all|(0.5-inf)|all|all|(0.0195-0.0415]|(0.0605-0.0685]|1
(0.5-inf)|all|all|(-inf-0.5]|all|all|(-inf-0.00605]|(0.0895-0.11109]|3
(-inf-0.5]|all|all|(-inf-0.5]|all|all|(-inf-0.00605]|(0.0895-0.11109]|3
(-inf-0.5]|all|all|(-inf-0.5]|all|all|(0.00605-0.0195]|(0.0685-0.0895]|2
(0.5-inf)|all|all|(-inf-0.5]|all|all|(0.00605-0.0195]|(0.0685-0.0895]|3
(0.5-inf)|all|all|(-inf-0.5]|all|all|(0.0195-0.0415]|(0.0605-0.0685]|3
(-inf-0.5]|all|all|(-inf-0.5]|all|all|(0.0195-0.0415]|(0.0605-0.0685]|1
(0.5-inf)|all|all|(-inf-0.5]|all|all|(0.0415-inf)|(0.033875-0.0605]|1
(-inf-0.5]|all|all|(-inf-0.5]|all|all|(0.0415-inf)|(0.033875-0.0605]|1
(-inf-0.5]|all|all|(0.5-inf)|all|all|(-inf-0.00605]|(0.0685-0.0895]|3
(-inf-0.5]|all|all|(0.5-inf)|all|all|(0.0415-inf)|(0.0185-0.033875]|1
(0.5-inf)|all|all|(-inf-0.5]|all|all|(-inf-0.00605]|(0.0685-0.0895]|3
(-inf-0.5]|all|all|(-inf-0.5]|all|all|(-inf-0.00605]|(0.0685-0.0895]|3
(0.5-inf)|all|all|(-inf-0.5]|all|all|(0.00605-0.0195]|(0.0605-0.0685]|1
(-inf-0.5]|all|all|(-inf-0.5]|all|all|(0.00605-0.0195]|(0.0605-0.0685]|2
(0.5-inf)|all|all|(-inf-0.5]|all|all|(0.0195-0.0415]|(0.033875-0.0605]|1
(-inf-0.5]|all|all|(-inf-0.5]|all|all|(0.0195-0.0415]|(0.033875-0.0605]|1
(0.5-inf)|all|all|(-inf-0.5]|all|all|(0.0415-inf)|(0.0185-0.033875]|1
(-inf-0.5]|all|all|(-inf-0.5]|all|all|(0.0415-inf)|(0.0185-0.033875]|1
(-inf-0.5]|all|all|(0.5-inf)|all|all|(-inf-0.00605]|(0.0605-0.0685]|3
(-inf-0.5]|all|all|(0.5-inf)|all|all|(0.0195-0.0415]|(0.0185-0.033875]|1
(-inf-0.5]|all|all|(0.5-inf)|all|all|(0.0415-inf)|(-inf-0.0185]|1
(0.5-inf)|all|all|(-inf-0.5]|all|all|(-inf-0.00605]|(0.0605-0.0685]|3
(-inf-0.5]|all|all|(-inf-0.5]|all|all|(-inf-0.00605]|(0.0605-0.0685]|3
(-inf-0.5]|all|all|(-inf-0.5]|all|all|(0.00605-0.0195]|(0.033875-0.0605]|1
(0.5-inf)|all|all|(-inf-0.5]|all|all|(0.00605-0.0195]|(0.033875-0.0605]|3
(-inf-0.5]|all|all|(-inf-0.5]|all|all|(0.0195-0.0415]|(0.0185-0.033875]|1
(0.5-inf)|all|all|(-inf-0.5]|all|all|(0.0195-0.0415]|(0.0185-0.033875]|1
(0.5-inf)|all|all|(-inf-0.5]|all|all|(0.0415-inf)|(-inf-0.0185]|1
(-inf-0.5]|all|all|(-inf-0.5]|all|all|(0.0415-inf)|(-inf-0.0185]|1
(-inf-0.5]|all|all|(0.5-inf)|all|all|(-inf-0.00605]|(0.033875-0.0605]|1
(0.5-inf)|all|all|(0.5-inf)|all|all|(-inf-0.00605]|(0.033875-0.0605]|1
(0.5-inf)|all|all|(-inf-0.5]|all|all|(-inf-0.00605]|(0.033875-0.0605]|3
(-inf-0.5]|all|all|(-inf-0.5]|all|all|(-inf-0.00605]|(0.033875-0.0605]|3
(-inf-0.5]|all|all|(-inf-0.5]|all|all|(0.00605-0.0195]|(0.0185-0.033875]|1
(-inf-0.5]|all|all|(-inf-0.5]|all|all|(0.0195-0.0415]|(-inf-0.0185]|1
(-inf-0.5]|all|all|(-inf-0.5]|all|all|(-inf-0.00605]|(0.0185-0.033875]|3
(-inf-0.5]|all|all|(-inf-0.5]|all|all|(0.00605-0.0195]|(-inf-0.0185]|1
(-inf-0.5]|all|all|(-inf-0.5]|all|all|(-inf-0.00605]|(-inf-0.0185]|3

## JRip

Decision list:

rules | predicted class
---|---
(FTI <= 0.064) and (TSH >= 0.0077) and (T3 <= 0.011) and (T4U <= 0.111)|1 (78.0/0.0)
(FTI <= 0.064) and (TSH >= 0.018) and (Age <= 0.66) and (Thyroid_surgery <= 0)|1 (48.0/0.0)
(FTI <= 0.064) and (TSH >= 0.0062) and (T3 <= 0.01) and (Age >= 0.52)|1 (10.0/0.0)
(FTI <= 0.064) and (FTI >= 0.051) and (TSH >= 0.022)|1 (5.0/0.0)
(FTI <= 0.061) and (TSH >= 0.0062) and (FTI >= 0.048) and (T4U <= 0.097)|1 (5.0/0.0)
(FTI <= 0.059) and (TT4 >= 0.068) and (TSH >= 0.01029)|1 (2.0/0.0)
(TSH >= 0.0061) and (On_thyroxine <= 0) and (T3 <= 0.02) and (FTI >= 0.069) and (Thyroid_surgery <= 0) and (TT4 <= 0.148)|2 (241.0/0.0)
(TSH >= 0.0061) and (On_thyroxine <= 0) and (TT4 <= 0.141) and (T3 >= 0.0208) and (T3 <= 0.026) and (FTI >= 0.06493)|2 (64.0/0.0)
(TSH >= 0.0061) and (On_thyroxine <= 0) and (FTI <= 0.092) and (TT4 >= 0.064) and (Thyroid_surgery <= 0) and (T4U <= 0.107)|2 (13.0/0.0)
(TSH >= 0.0061) and (T3 >= 0.027) and (T4U >= 0.123) and (TT4 <= 0.141)|2 (8.0/0.0)
(TSH >= 0.0063) and (TSH <= 0.0065) and (FTI <= 0.067)|2 (2.0/0.0)
(TSH >= 0.00879) and (Age <= 0.19) and (T3 >= 0.027)|2 (2.0/0.0)
|3 (6001.0/1.0)


## PART

Decision list:

rules | predicted class
---|---
TSH <= 0.00605|3 (5842.0)
FTI <= 0.064255 AND TSH > 0.016895 AND T3 <= 0.0115 AND T4U <= 0.1115|1 (74.0)
FTI <= 0.064255 AND T3 <= 0.0235 AND TSH > 0.078|1 (26.0)
FTI <= 0.064255 AND T3 <= 0.0235 AND T4U <= 0.0965|1 (13.0)
FTI <= 0.064255 AND TSH > 0.017395 AND TT4 > 0.049|1 (14.0)
FTI > 0.06472 AND On_thyroxine <= 0.5 AND TT4 <= 0.1505 AND TT4 > 0.0615 AND T3 <= 0.028999999999999998 AND Age > 0.425 AND T4U <= 0.1275 AND TT4 <= 0.1365|2 (219.0)
FTI <= 0.062755 AND T3 <= 0.011|1 (15.0/2.0)
On_thyroxine > 0.5|3 (100.0)
FTI > 0.062965 AND TT4 <= 0.1505 AND Thyroid_surgery <= 0.5 AND TT4 > 0.058499999999999996 AND T3 <= 0.028999999999999998 AND Age <= 0.7|2 (91.0)
FTI > 0.063 AND TT4 > 0.1495|3 (23.0)
FTI > 0.063 AND T4U <= 0.114 AND T3 > 0.0187|3 (17.0)
FTI > 0.063 AND TT4 > 0.0975|2 (14.0)
T4U > 0.092 AND TSH <= 0.028|3 (12.0/3.0)
TSH > 0.0235|1 (10.0/4.0)
|2 (9.0/3.0)


## J48 Decision Tree

* TSH <= 0.006: 3 (5842.0)
* TSH > 0.006
	* FTI <= 0.064
		* TSH <= 0.01679
			* T3 <= 0.02: 1 (16.0/2.0)
			* T3 > 0.02: 3 (8.0/2.0)
		* TSH > 0.01679: 1 (139.0/6.0)
	* FTI > 0.064
		* On_thyroxine <= 0
			* TT4 <= 0.15
				* TT4 <= 0.061
					* T3 <= 0.019: 2 (11.0/1.0)
					* T3 > 0.019: 3 (6.0)
				* TT4 > 0.061
					* T3 <= 0.028
						* Age <= 0.42
							* Thyroid_surgery <= 0: 2 (78.0)
							* Thyroid_surgery > 0: 3 (9.0)
						* Age > 0.42: 2 (237.0/2.0)
					* T3 > 0.028
						* T4U <= 0.116: 3 (5.0)
						* T4U > 0.116: 2 (7.0)
			* TT4 > 0.15: 3 (23.0)
		* On_thyroxine > 0: 3 (98.0)


## SimpleCart Decision Tree

* TSH < 0.00605: 3(5842.0/0.0)
* TSH >= 0.00605
	* FTI < 0.064255
		* T3 < 0.0265: 1(149.0/9.0)
		* T3 >= 0.0265: 3(5.0/0.0)
	* FTI >= 0.064255
		* On_thyroxine < 0.5
			* TT4 < 0.1505
				* Thyroid_surgery < 0.5: 2(330.0/13.0)
				* Thyroid_surgery >= 0.5: 3(10.0/0.0)
			* TT4 >= 0.1505: 3(23.0/0.0)
		* On_thyroxine >= 0.5: 3(98.0/0.0)


