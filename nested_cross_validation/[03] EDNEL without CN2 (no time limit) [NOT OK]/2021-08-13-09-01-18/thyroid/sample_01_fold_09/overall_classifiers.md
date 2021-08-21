# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 3 | 0.926069 |
| TSH >= 0.00605 and FTI >= 0.064255 and On_thyroxine < 0.5 and TT4 < 0.1505 and Thyroid_surgery < 0.5 | 2 | 0.049375 |
| TSH >= 0.00605 and FTI < 0.064255 | 1 | 0.021068 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| TSH <= 0.006 | 3 | 0.924185 |
| FTI <= 0.064 and TSH > 0.017 and T3 <= 0.011 and T4U <= 0.111 | 1 | 0.130973 |
| FTI <= 0.064 and T3 <= 0.023 and FTI <= 0.017 | 1 | 0.046602 |
| FTI <= 0.064 and Age > 0.27 and TT4 > 0.037 and T4U <= 0.108 | 1 | 0.037255 |
| FTI > 0.06451 and On_thyroxine <= 0.0 and TT4 <= 0.15 and TT4 > 0.061 and Age > 0.42 and TT4 <= 0.14 and T4U <= 0.122 and T3 <= 0.024 | 2 | 0.522277 |
| FTI <= 0.064 and T3 <= 0.023 and FTI > 0.049 | 1 | 0.051047 |
| FTI <= 0.05745 and TSH > 0.04 and T4U <= 0.114 | 1 | 0.009885 |
| FTI <= 0.05745 and TSH <= 0.04 | 3 | 0.036567 |
| FTI > 0.062 and On_thyroxine > 0.0 | 3 | 0.437229 |
| FTI > 0.05745 and TT4 <= 0.15 and Thyroid_surgery <= 0.0 and TT4 > 0.056 and T3 <= 0.029 and Age <= 0.69 | 2 | 0.607423 |
| FTI > 0.05745 and TT4 > 0.149 | 3 | 0.444444 |
| FTI > 0.05745 and Thyroid_surgery <= 0.0 and T4U > 0.11 | 2 | 0.217195 |
| FTI > 0.05745 and T3 > 0.013 and Age <= 0.59 | 3 | 0.400000 |
| TSH <= 0.033 and T3 <= 0.015 | 2 | 0.112853 |
| TSH <= 0.033 | 3 | 0.457143 |
|  | 1 | 0.647059 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| FTI <= 0.064 and TSH >= 0.0063 | 1 | 0.021068 |
| TSH >= 0.0061 and On_thyroxine <= 0 and T3 <= 0.019 | 2 | 0.036749 |
| TSH >= 0.0061 and On_thyroxine <= 0 and TT4 <= 0.141 | 2 | 0.010288 |
| TSH >= 0.016 and TSH <= 0.019 and On_thyroxine <= 0 | 2 | 0.000167 |
|  | 3 | 1.000000 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

on_thyroxine|sick|thyroid_surgery|query_hyperthyroid|lithium|tsh|t4u|class
---|---|---|---|---|---|---|---
(-inf-0.5]|all|(0.5-inf)|all|all|(0.0415-inf)|(0.1025-inf)|1
(-inf-0.5]|all|(-inf-0.5]|all|all|(0.0415-inf)|(0.1025-inf)|1
(0.5-inf)|all|(-inf-0.5]|all|all|(0.0415-inf)|(0.1025-inf)|1
(-inf-0.5]|all|(0.5-inf)|all|all|(0.0195-0.0415]|(0.1025-inf)|3
(0.5-inf)|all|(-inf-0.5]|all|all|(0.0195-0.0415]|(0.1025-inf)|3
(-inf-0.5]|all|(-inf-0.5]|all|all|(0.0195-0.0415]|(0.1025-inf)|2
(-inf-0.5]|all|(-inf-0.5]|all|all|(0.0415-inf)|(-inf-0.1025]|1
(0.5-inf)|all|(-inf-0.5]|all|all|(0.0415-inf)|(-inf-0.1025]|3
(-inf-0.5]|all|(0.5-inf)|all|all|(0.00605-0.0195]|(0.1025-inf)|3
(-inf-0.5]|all|(0.5-inf)|all|all|(0.0195-0.0415]|(-inf-0.1025]|1
(0.5-inf)|all|(-inf-0.5]|all|all|(0.00605-0.0195]|(0.1025-inf)|3
(-inf-0.5]|all|(-inf-0.5]|all|all|(0.00605-0.0195]|(0.1025-inf)|2
(-inf-0.5]|all|(-inf-0.5]|all|all|(0.0195-0.0415]|(-inf-0.1025]|2
(0.5-inf)|all|(-inf-0.5]|all|all|(0.0195-0.0415]|(-inf-0.1025]|3
(0.5-inf)|all|(0.5-inf)|all|all|(-inf-0.00605]|(0.1025-inf)|3
(-inf-0.5]|all|(0.5-inf)|all|all|(-inf-0.00605]|(0.1025-inf)|3
(-inf-0.5]|all|(0.5-inf)|all|all|(0.00605-0.0195]|(-inf-0.1025]|3
(0.5-inf)|all|(-inf-0.5]|all|all|(-inf-0.00605]|(0.1025-inf)|3
(-inf-0.5]|all|(-inf-0.5]|all|all|(-inf-0.00605]|(0.1025-inf)|3
(-inf-0.5]|all|(-inf-0.5]|all|all|(0.00605-0.0195]|(-inf-0.1025]|2
(0.5-inf)|all|(-inf-0.5]|all|all|(0.00605-0.0195]|(-inf-0.1025]|3
(0.5-inf)|all|(0.5-inf)|all|all|(-inf-0.00605]|(-inf-0.1025]|3
(-inf-0.5]|all|(0.5-inf)|all|all|(-inf-0.00605]|(-inf-0.1025]|3
(0.5-inf)|all|(-inf-0.5]|all|all|(-inf-0.00605]|(-inf-0.1025]|3
(-inf-0.5]|all|(-inf-0.5]|all|all|(-inf-0.00605]|(-inf-0.1025]|3

## JRip

Decision list:

rules | predicted class
---|---
(FTI <= 0.064) and (TSH >= 0.0063)|1 (163.0/14.0)
(TSH >= 0.0061) and (On_thyroxine <= 0) and (T3 <= 0.019)|2 (251.0/8.0)
(TSH >= 0.0061) and (On_thyroxine <= 0) and (TT4 <= 0.141)|2 (99.0/14.0)
(TSH >= 0.016) and (TSH <= 0.019) and (On_thyroxine <= 0)|2 (2.0/0.0)
|3 (5964.0/0.0)


## PART

Decision list:

rules | predicted class
---|---
TSH <= 0.006|3 (5839.0)
FTI <= 0.064 AND TSH > 0.017 AND T3 <= 0.011 AND T4U <= 0.111|1 (74.0)
FTI <= 0.064 AND T3 <= 0.023 AND FTI <= 0.017|1 (24.0)
FTI <= 0.064 AND Age > 0.27 AND TT4 > 0.037 AND T4U <= 0.108|1 (19.0)
FTI > 0.06451 AND On_thyroxine <= 0.0 AND TT4 <= 0.15 AND TT4 > 0.061 AND Age > 0.42 AND TT4 <= 0.14 AND T4U <= 0.122 AND T3 <= 0.024|2 (211.0)
FTI <= 0.064 AND T3 <= 0.023 AND FTI > 0.049|1 (17.0/1.0)
FTI <= 0.05745 AND TSH > 0.04 AND T4U <= 0.114|1 (9.0/4.0)
FTI <= 0.05745 AND TSH <= 0.04|3 (10.0/3.0)
FTI > 0.062 AND On_thyroxine > 0.0|3 (101.0)
FTI > 0.05745 AND TT4 <= 0.15 AND Thyroid_surgery <= 0.0 AND TT4 > 0.056 AND T3 <= 0.029 AND Age <= 0.69|2 (100.0)
FTI > 0.05745 AND TT4 > 0.149|3 (24.0)
FTI > 0.05745 AND Thyroid_surgery <= 0.0 AND T4U > 0.11|2 (12.0)
FTI > 0.05745 AND T3 > 0.013 AND Age <= 0.59|3 (12.0)
TSH <= 0.033 AND T3 <= 0.015|2 (9.0/3.0)
TSH <= 0.033|3 (9.0/1.0)
|1 (9.0/1.0)


## J48 Decision Tree

* TSH <= 0.006: 3 (3900.0)
* TSH > 0.006
	* FTI <= 0.064: 1 (108.0/8.0)
	* FTI > 0.064
		* On_thyroxine <= 0
			* TT4 <= 0.15
				* T3 <= 0.02: 2 (182.0/4.0)
				* T3 > 0.02
					* T4U <= 0.093: 3 (9.0/3.0)
					* T4U > 0.093: 2 (44.0/5.0)
			* TT4 > 0.15: 3 (16.0)
		* On_thyroxine > 0: 3 (61.0)


## SimpleCart Decision Tree

* TSH < 0.00605: 3(5839.0/0.0)
* TSH >= 0.00605
	* FTI < 0.064255: 1(149.0/14.0)
	* FTI >= 0.064255
		* On_thyroxine < 0.5
			* TT4 < 0.1505
				* Thyroid_surgery < 0.5: 2(330.0/11.0)
				* Thyroid_surgery >= 0.5: 3(11.0/0.0)
			* TT4 >= 0.1505: 3(24.0/0.0)
		* On_thyroxine >= 0.5: 3(101.0/0.0)


