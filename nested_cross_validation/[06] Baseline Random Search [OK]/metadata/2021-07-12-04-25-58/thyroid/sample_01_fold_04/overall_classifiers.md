# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| TSH <= 0.006 | 3 | 0.924293 |
| TSH >= 0.00605 and FTI >= 0.064255 and On_thyroxine < 0.5 and TT4 < 0.1505 and Thyroid_surgery < 0.5 | 2 | 0.049102 |
| TSH >= 0.00605 and FTI < 0.064255 | 1 | 0.020942 |
| On_thyroxine <= 0.5 and Thyroid_surgery > 0.5 and I131_treatment = all and Query_hyperthyroid = all and Lithium = all and Tumor = all and Hypopituitary = all and TSH > 0.00605 and TSH <= 0.0195 | 3 | 0.022449 |
| TSH > 0.006 and FTI > 0.064 and On_thyroxine <= 0 and TT4 <= 0.15 and TT4 > 0.061 and T3 <= 0.03 and Thyroid_surgery > 0 | 3 | 0.022449 |
| On_thyroxine > 0.5 and Thyroid_surgery <= 0.5 and I131_treatment = all and Query_hyperthyroid = all and Lithium = all and Tumor = all and Hypopituitary = all and TSH > 0.00605 and TSH <= 0.0195 | 3 | 0.127530 |
| TSH > 0.006 and FTI > 0.064 and On_thyroxine <= 0 and TT4 <= 0.15 and TT4 <= 0.061 | 3 | 0.007853 |
| On_thyroxine > 0.5 and Thyroid_surgery <= 0.5 and I131_treatment = all and Query_hyperthyroid = all and Lithium = all and Tumor = all and Hypopituitary = all and TSH > 0.0195 and TSH <= 0.0415 | 3 | 0.024168 |
| TSH > 0.006 and FTI > 0.064 and On_thyroxine > 0 | 3 | 0.164049 |
| TSH >= 0.00605 and FTI >= 0.064255 and On_thyroxine < 0.5 and TT4 >= 0.1505 | 3 | 0.038153 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| TSH <= 0.006 | 3 | 0.924293 |
| FTI <= 0.064 and Thyroid_surgery <= 0.0 and T3 <= 0.023 and I131_treatment <= 0.0 and TSH > 0.01679 | 1 | 0.200663 |
| FTI > 0.06451 and On_thyroxine <= 0.0 and TT4 <= 0.15 and TT4 > 0.061 and T3 <= 0.03 and Thyroid_surgery <= 0.0 and Sex <= 0.0 and Query_hypothyroid <= 0.0 and Query_hyperthyroid <= 0.0 and Sick <= 0.0 | 2 | 0.512209 |
| FTI <= 0.064 and T3 <= 0.026 and On_antithyroid_medication <= 0.0 and Thyroid_surgery <= 0.0 and Sex <= 0.0 and T4U <= 0.103 | 1 | 0.036304 |
| FTI <= 0.062 and T3 <= 0.026 and Sex <= 0.0 and TSH > 0.00979 and FTI > 0.043 | 1 | 0.026667 |
| On_thyroxine > 0.0 and I131_treatment <= 0.0 | 3 | 0.386831 |
| FTI > 0.0635 and TT4 <= 0.15 and Thyroid_surgery <= 0.0 and TT4 > 0.054 and I131_treatment <= 0.0 and T3 <= 0.029 and Sex > 0.0 | 2 | 0.521429 |
| FTI > 0.0635 and TT4 <= 0.148 and Thyroid_surgery <= 0.0 and Sex <= 0.0 and I131_treatment <= 0.0 and TT4 > 0.061 and T3 <= 0.031 | 2 | 0.455425 |
| TT4 > 0.018 and Sex <= 0.0 and Thyroid_surgery > 0.0 | 3 | 0.441176 |
| FTI > 0.064 and TT4 > 0.148 | 3 | 0.500000 |
| Thyroid_surgery <= 0.0 and FTI <= 0.071 and Sex <= 0.0 and FTI > 0.027 | 3 | 0.344828 |
| FTI <= 0.067 and Thyroid_surgery <= 0.0 and Sex > 0.0 and Age > 0.46 | 1 | 0.142857 |
| FTI <= 0.052 and I131_treatment <= 0.0 | 1 | 0.111111 |
| TSH <= 0.056 and Sex <= 0.0 and T4U <= 0.113 and T4U > 0.087 | 3 | 0.333333 |
| Sex <= 0.0 and T4U > 0.051 and TSH <= 0.04 | 2 | 0.478469 |
| T3 > 0.01 | 3 | 0.800000 |
|  | 1 | 1.000000 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

on_thyroxine|thyroid_surgery|i131_treatment|query_hyperthyroid|lithium|tumor|hypopituitary|tsh|class
---|---|---|---|---|---|---|---|---
(-inf-0.5]|(0.5-inf)|all|all|all|all|all|(0.0415-inf)|1
(-inf-0.5]|(-inf-0.5]|all|all|all|all|all|(0.0415-inf)|1
(0.5-inf)|(-inf-0.5]|all|all|all|all|all|(0.0415-inf)|1
(0.5-inf)|(0.5-inf)|all|all|all|all|all|(0.0195-0.0415]|1
(-inf-0.5]|(0.5-inf)|all|all|all|all|all|(0.0195-0.0415]|1
(-inf-0.5]|(-inf-0.5]|all|all|all|all|all|(0.0195-0.0415]|2
(0.5-inf)|(-inf-0.5]|all|all|all|all|all|(0.0195-0.0415]|3
(-inf-0.5]|(0.5-inf)|all|all|all|all|all|(0.00605-0.0195]|3
(-inf-0.5]|(-inf-0.5]|all|all|all|all|all|(0.00605-0.0195]|2
(0.5-inf)|(-inf-0.5]|all|all|all|all|all|(0.00605-0.0195]|3
(0.5-inf)|(0.5-inf)|all|all|all|all|all|(-inf-0.00605]|3
(-inf-0.5]|(0.5-inf)|all|all|all|all|all|(-inf-0.00605]|3
(0.5-inf)|(-inf-0.5]|all|all|all|all|all|(-inf-0.00605]|3
(-inf-0.5]|(-inf-0.5]|all|all|all|all|all|(-inf-0.00605]|3

## PART

Decision list:

rules | predicted class
---|---
TSH <= 0.006|3 (5848.0)
FTI <= 0.064 AND Thyroid_surgery <= 0.0 AND T3 <= 0.023 AND I131_treatment <= 0.0 AND TSH > 0.01679|1 (121.0)
FTI > 0.06451 AND On_thyroxine <= 0.0 AND TT4 <= 0.15 AND TT4 > 0.061 AND T3 <= 0.03 AND Thyroid_surgery <= 0.0 AND Sex <= 0.0 AND Query_hypothyroid <= 0.0 AND Query_hyperthyroid <= 0.0 AND Sick <= 0.0|2 (191.0/1.0)
FTI <= 0.064 AND T3 <= 0.026 AND On_antithyroid_medication <= 0.0 AND Thyroid_surgery <= 0.0 AND Sex <= 0.0 AND T4U <= 0.103|1 (11.0)
FTI <= 0.062 AND T3 <= 0.026 AND Sex <= 0.0 AND TSH > 0.00979 AND FTI > 0.043|1 (8.0)
On_thyroxine > 0.0 AND I131_treatment <= 0.0|3 (94.0)
FTI > 0.0635 AND TT4 <= 0.15 AND Thyroid_surgery <= 0.0 AND TT4 > 0.054 AND I131_treatment <= 0.0 AND T3 <= 0.029 AND Sex > 0.0|2 (73.0)
FTI > 0.0635 AND TT4 <= 0.148 AND Thyroid_surgery <= 0.0 AND Sex <= 0.0 AND I131_treatment <= 0.0 AND TT4 > 0.061 AND T3 <= 0.031|2 (57.0)
TT4 > 0.018 AND Sex <= 0.0 AND Thyroid_surgery > 0.0|3 (15.0)
FTI > 0.064 AND TT4 > 0.148|3 (19.0)
Thyroid_surgery <= 0.0 AND FTI <= 0.071 AND Sex <= 0.0 AND FTI > 0.027|3 (10.0)
FTI <= 0.067 AND Thyroid_surgery <= 0.0 AND Sex > 0.0 AND Age > 0.46|1 (4.0)
FTI <= 0.052 AND I131_treatment <= 0.0|1 (3.0)
TSH <= 0.056 AND Sex <= 0.0 AND T4U <= 0.113 AND T4U > 0.087|3 (6.0)
Sex <= 0.0 AND T4U > 0.051 AND TSH <= 0.04|2 (10.0)
T3 > 0.01|3 (7.0)
|1 (2.0)


## J48 Decision Tree

* TSH <= 0.006: 3 (5848.0)
* TSH > 0.006
	* FTI <= 0.064
		* Thyroid_surgery <= 0
			* T3 <= 0.023
				* TSH <= 0.01679
					* Age <= 0.55: 1 (8.0/2.0)
					* Age > 0.55: 1 (8.0/1.0)
				* TSH > 0.01679
					* T3 <= 0.011: 1 (100.0)
					* T3 > 0.011
						* Age <= 0.6: 1 (18.0)
						* Age > 0.6: 1 (8.0/1.0)
			* T3 > 0.023: 1 (14.0/7.0)
		* Thyroid_surgery > 0: 1 (8.0/4.0)
	* FTI > 0.064
		* On_thyroxine <= 0
			* TT4 <= 0.15
				* TT4 <= 0.061: 3 (13.0/6.0)
				* TT4 > 0.061
					* T3 <= 0.03
						* Thyroid_surgery <= 0
							* TT4 <= 0.14: 2 (307.0)
							* TT4 > 0.14: 2 (11.0/1.0)
						* Thyroid_surgery > 0: 3 (11.0)
					* T3 > 0.03: 2 (12.0/5.0)
			* TT4 > 0.15: 3 (19.0)
		* On_thyroxine > 0: 3 (94.0)


## SimpleCart Decision Tree

* TSH < 0.00605: 3(5848.0/0.0)
* TSH >= 0.00605
	* FTI < 0.064255: 1(149.0/15.0)
	* FTI >= 0.064255
		* On_thyroxine < 0.5
			* TT4 < 0.1505
				* Thyroid_surgery < 0.5: 2(330.0/13.0)
				* Thyroid_surgery >= 0.5: 3(11.0/0.0)
			* TT4 >= 0.1505: 3(19.0/0.0)
		* On_thyroxine >= 0.5: 3(94.0/0.0)


