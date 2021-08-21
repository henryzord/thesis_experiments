# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 3 | 0.926212 |
| TSH >= 0.00605 and FTI >= 0.064255 and On_thyroxine < 0.5 and TT4 < 0.1505 and Thyroid_surgery < 0.5 | 2 | 0.048665 |
| TSH > 0.006 and FTI <= 0.064 and T3 > 0.011 and TSH > 0.017 | 1 | 0.004700 |
| On_thyroxine > 0.5 and Query_on_thyroxine = all and On_antithyroid_medication = all and Thyroid_surgery <= 0.5 and Query_hyperthyroid = all and Lithium = all and Goitre <= 0.5 and Tumor = all and TSH > 0.0415 | 1 | 0.000674 |
| On_thyroxine <= 0.5 and Query_on_thyroxine = all and On_antithyroid_medication = all and Thyroid_surgery <= 0.5 and Query_hyperthyroid = all and Lithium = all and Goitre <= 0.5 and Tumor = all and TSH > 0.0415 | 1 | 0.011028 |
| TSH >= 0.00605 and FTI < 0.064255 | 1 | 0.021224 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| TSH <= 0.006 | 3 | 0.924319 |
| FTI <= 0.064 and Thyroid_surgery <= 0 and T3 <= 0.011 | 1 | 0.181970 |
| FTI <= 0.064 and TSH > 0.017 and T3 > 0.012 | 1 | 0.057919 |
| On_thyroxine <= 0 and FTI > 0.064 and TT4 <= 0.15 and TT4 > 0.061 and T3 <= 0.028 and Age > 0.42 | 2 | 0.574669 |
| FTI > 0.064 and On_thyroxine > 0 | 3 | 0.490196 |
| FTI > 0.064 and TT4 <= 0.15 and Thyroid_surgery <= 0 and TT4 > 0.058 and T3 <= 0.029 | 2 | 0.542011 |
| FTI > 0.064 and T3 > 0.011 and T3 <= 0.028 | 3 | 0.620000 |
| FTI > 0.064 and TT4 > 0.151 | 3 | 0.344828 |
| FTI > 0.064 and T4U <= 0.113 and T3 > 0.0201 | 3 | 0.240000 |
| FTI > 0.064 | 2 | 0.275482 |
| T4U <= 0.103 | 1 | 0.173611 |
| T3 <= 0.02 and TSH <= 0.034 | 1 | 0.091837 |
|  | 3 | 0.937500 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| FTI <= 0.064 and TSH >= 0.0062 | 1 | 0.021224 |
| TSH >= 0.0061 and On_thyroxine <= 0 and TT4 <= 0.144 and Thyroid_surgery <= 0 and T3 <= 0.02 | 2 | 0.039088 |
| TSH >= 0.0061 and On_thyroxine <= 0 and TT4 <= 0.141 and T4U >= 0.097 and Thyroid_surgery <= 0 | 2 | 0.008847 |
| TSH >= 0.0061 and On_thyroxine <= 0 and TT4 <= 0.15 and TT4 >= 0.062 and Thyroid_surgery <= 0 and T3 <= 0.027 | 2 | 0.002728 |
| TSH >= 0.019 and TSH <= 0.02 | 2 | 0.000222 |
|  | 3 | 1.000000 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

on_thyroxine|query_on_thyroxine|on_antithyroid_medication|thyroid_surgery|query_hyperthyroid|lithium|goitre|tumor|tsh|class
---|---|---|---|---|---|---|---|---|---
(-inf-0.5]|all|all|(0.5-inf)|all|all|(-inf-0.5]|all|(0.0415-inf)|1
(-inf-0.5]|all|all|(-inf-0.5]|all|all|(-inf-0.5]|all|(0.0415-inf)|1
(0.5-inf)|all|all|(-inf-0.5]|all|all|(-inf-0.5]|all|(0.0415-inf)|1
(0.5-inf)|all|all|(0.5-inf)|all|all|(-inf-0.5]|all|(0.0195-0.0415]|1
(-inf-0.5]|all|all|(0.5-inf)|all|all|(-inf-0.5]|all|(0.0195-0.0415]|3
(0.5-inf)|all|all|(-inf-0.5]|all|all|(-inf-0.5]|all|(0.0195-0.0415]|3
(-inf-0.5]|all|all|(-inf-0.5]|all|all|(-inf-0.5]|all|(0.0195-0.0415]|2
(-inf-0.5]|all|all|(-inf-0.5]|all|all|(0.5-inf)|all|(0.00605-0.0195]|1
(-inf-0.5]|all|all|(0.5-inf)|all|all|(-inf-0.5]|all|(0.00605-0.0195]|3
(0.5-inf)|all|all|(-inf-0.5]|all|all|(-inf-0.5]|all|(0.00605-0.0195]|3
(-inf-0.5]|all|all|(-inf-0.5]|all|all|(-inf-0.5]|all|(0.00605-0.0195]|2
(0.5-inf)|all|all|(-inf-0.5]|all|all|(0.5-inf)|all|(-inf-0.00605]|3
(-inf-0.5]|all|all|(-inf-0.5]|all|all|(0.5-inf)|all|(-inf-0.00605]|3
(0.5-inf)|all|all|(0.5-inf)|all|all|(-inf-0.5]|all|(-inf-0.00605]|3
(-inf-0.5]|all|all|(0.5-inf)|all|all|(-inf-0.5]|all|(-inf-0.00605]|3
(0.5-inf)|all|all|(-inf-0.5]|all|all|(-inf-0.5]|all|(-inf-0.00605]|3
(-inf-0.5]|all|all|(-inf-0.5]|all|all|(-inf-0.5]|all|(-inf-0.00605]|3

## JRip

Decision list:

rules | predicted class
---|---
(FTI <= 0.064) and (TSH >= 0.0062)|1 (164.0/14.0)
(TSH >= 0.0061) and (On_thyroxine <= 0) and (TT4 <= 0.144) and (Thyroid_surgery <= 0) and (T3 <= 0.02)|2 (249.0/1.0)
(TSH >= 0.0061) and (On_thyroxine <= 0) and (TT4 <= 0.141) and (T4U >= 0.097) and (Thyroid_surgery <= 0)|2 (59.0/0.0)
(TSH >= 0.0061) and (On_thyroxine <= 0) and (TT4 <= 0.15) and (TT4 >= 0.062) and (Thyroid_surgery <= 0) and (T3 <= 0.027)|2 (20.0/1.0)
(TSH >= 0.019) and (TSH <= 0.02)|2 (3.0/1.0)
|3 (5983.0/0.0)


## PART

Decision list:

rules | predicted class
---|---
TSH <= 0.006|3 (5838.0)
FTI <= 0.064 AND Thyroid_surgery <= 0 AND T3 <= 0.011|1 (109.0)
FTI <= 0.064 AND TSH > 0.017 AND T3 > 0.012|1 (34.0/2.0)
On_thyroxine <= 0 AND FTI > 0.064 AND TT4 <= 0.15 AND TT4 > 0.061 AND T3 <= 0.028 AND Age > 0.42|2 (235.0/2.0)
FTI > 0.064 AND On_thyroxine > 0|3 (100.0)
FTI > 0.064 AND TT4 <= 0.15 AND Thyroid_surgery <= 0 AND TT4 > 0.058 AND T3 <= 0.029|2 (85.0)
FTI > 0.064 AND T3 > 0.011 AND T3 <= 0.028|3 (29.0)
FTI > 0.064 AND TT4 > 0.151|3 (10.0)
FTI > 0.064 AND T4U <= 0.113 AND T3 > 0.0201|3 (6.0)
FTI > 0.064|2 (11.0/1.0)
T4U <= 0.103|1 (6.0/1.0)
T3 <= 0.02 AND TSH <= 0.034|1 (5.0/2.0)
|3 (10.0/1.0)


## J48 Decision Tree

* TSH <= 0.006: 3 (5838.0)
* TSH > 0.006
	* FTI <= 0.064
		* T3 <= 0.011: 1 (112.0/1.0)
		* T3 > 0.011
			* TSH <= 0.017: 3 (11.0/4.0)
			* TSH > 0.017: 1 (41.0/6.0)
	* FTI > 0.064
		* On_thyroxine <= 0.0
			* TT4 <= 0.15
				* TT4 <= 0.061
					* T3 <= 0.019: 2 (10.0/1.0)
					* T3 > 0.019: 3 (7.0)
				* TT4 > 0.061
					* Thyroid_surgery <= 0.0: 2 (325.0/6.0)
					* Thyroid_surgery > 0.0: 3 (9.0)
			* TT4 > 0.15: 3 (25.0)
		* On_thyroxine > 0.0: 3 (100.0)


## SimpleCart Decision Tree

* TSH < 0.00605: 3(5838.0/0.0)
* TSH >= 0.00605
	* FTI < 0.064255: 1(150.0/14.0)
	* FTI >= 0.064255
		* On_thyroxine < 0.5
			* TT4 < 0.1505
				* Thyroid_surgery < 0.5: 2(328.0/14.0)
				* Thyroid_surgery >= 0.5: 3(9.0/0.0)
			* TT4 >= 0.1505: 3(25.0/0.0)
		* On_thyroxine >= 0.5: 3(100.0/0.0)


