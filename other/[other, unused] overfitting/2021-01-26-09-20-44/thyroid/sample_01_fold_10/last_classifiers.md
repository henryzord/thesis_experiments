# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| TSH < 0.00605 | 3 | 0.924221 |
| TSH >= 0.00605 and FTI >= 0.064255 and On_thyroxine < 0.5 and TT4 < 0.1505 and Thyroid_surgery < 0.5 and TT4 >= 0.058499999999999996 and T3 < 0.028999999999999998 | 2 | 0.049026 |
| TSH >= 0.00605 and FTI < 0.064255 and T3 < 0.0265 | 1 | 0.021718 |
| TSH >= 0.00605 and FTI >= 0.064255 and On_thyroxine >= 0.5 | 3 | 0.169844 |
| TSH >= 0.00605 and FTI >= 0.064255 and On_thyroxine < 0.5 and TT4 >= 0.1505 | 3 | 0.045817 |
| TSH >= 0.00605 and FTI >= 0.064255 and On_thyroxine < 0.5 and TT4 < 0.1505 and Thyroid_surgery >= 0.5 | 3 | 0.020450 |
| TSH >= 0.00605 and FTI >= 0.064255 and On_thyroxine < 0.5 and TT4 < 0.1505 and Thyroid_surgery < 0.5 and TT4 >= 0.058499999999999996 and T3 >= 0.028999999999999998 and T4U < 0.11649999999999999 | 3 | 0.012371 |
| TSH >= 0.00605 and FTI < 0.064255 and T3 >= 0.0265 | 3 | 0.010331 |
| Sex <= 0.5 and On_thyroxine <= 0.5 and Query_on_thyroxine = all and Pregnant <= 0.5 and Thyroid_surgery <= 0.5 and I131_treatment = all and Lithium = all and Goitre <= 0.5 and Tumor = all and Hypopituitary = all and TSH > 0.00605 and TSH <= 0.0195 | 2 | 0.027360 |
| TSH > 0.006 and FTI > 0.064 and On_thyroxine <= 0.0 and TT4 <= 0.15 and TT4 <= 0.061 and T3 > 0.019 | 3 | 0.012371 |
| TSH > 0.006 and FTI <= 0.064 and TSH <= 0.01679 and On_antithyroid_medication <= 0.0 and T4U > 0.104 and TSH <= 0.00959 | 3 | 0.006224 |
| TSH > 0.006 and FTI <= 0.064 and TSH <= 0.01679 and On_antithyroid_medication > 0.0 | 3 | 0.006224 |
| TSH > 0.006 and FTI <= 0.064 and TSH > 0.01679 and Thyroid_surgery > 0.0 and Age <= 0.51 and TT4 <= 0.046 | 3 | 0.004158 |
| TSH > 0.006 and FTI <= 0.064 and TSH > 0.01679 and Thyroid_surgery <= 0.0 and I131_treatment > 0.0 and Age > 0.65 | 3 | 0.004158 |
| Sex > 0.5 and On_thyroxine <= 0.5 and Query_on_thyroxine = all and Pregnant <= 0.5 and Thyroid_surgery <= 0.5 and I131_treatment = all and Lithium = all and Goitre <= 0.5 and Tumor = all and Hypopituitary = all and TSH > 0.00605 and TSH <= 0.0195 | 2 | 0.009928 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| TSH <= 0.006 | 3 | 0.924221 |
| FTI <= 0.064 and Thyroid_surgery <= 0.0 and T3 <= 0.023 and I131_treatment <= 0.0 and Sex <= 0.0 and Query_hypothyroid <= 0.0 and On_thyroxine <= 0.0 and Query_hyperthyroid <= 0.0 and Tumor <= 0.0 and TSH > 0.01679 | 1 | 0.111111 |
| FTI <= 0.064 and T3 <= 0.026 and Thyroid_surgery <= 0.0 and On_antithyroid_medication <= 0.0 and I131_treatment <= 0.0 and TT4 <= 0.065 | 1 | 0.127013 |
| On_thyroxine > 0.0 and FTI > 0.064 | 3 | 0.220225 |
| FTI > 0.064 and TT4 <= 0.15 and TT4 > 0.061 and T3 <= 0.028 and Age > 0.42 and Sex <= 0.0 and Query_hypothyroid <= 0.0 and Query_hyperthyroid <= 0.0 and Sick <= 0.0 | 2 | 0.629950 |
| FTI > 0.064 and TT4 <= 0.15 and Thyroid_surgery <= 0.0 and TT4 > 0.058 and T3 <= 0.028 | 2 | 0.705001 |
| FTI > 0.064 and TT4 > 0.143 | 3 | 0.462963 |
| TT4 <= 0.124 and FTI > 0.064 and T3 > 0.016 | 3 | 0.369565 |
| FTI > 0.064 and Thyroid_surgery <= 0.0 | 2 | 0.240803 |
| TSH <= 0.00959 | 3 | 0.291667 |
| T3 <= 0.026 and Sex <= 0.0 and On_thyroxine <= 0.0 and T3 > 0.018 | 1 | 0.312500 |
| T3 <= 0.011 and Thyroid_surgery <= 0.0 | 1 | 0.360294 |
| Thyroid_surgery <= 0.0 and TT4 <= 0.054 | 3 | 0.583333 |
| Age <= 0.51 | 3 | 0.400000 |
|  | 1 | 1.000000 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| FTI <= 0.064 and TSH >= 0.0062 | 1 | 0.021068 |
| TSH >= 0.0061 and On_thyroxine <= 0 and TT4 <= 0.15 and Thyroid_surgery <= 0 and T3 <= 0.02 | 2 | 0.040169 |
| TSH >= 0.0061 and On_thyroxine <= 0 and TT4 <= 0.15 and T3 >= 0.0208 | 2 | 0.010626 |
|  | 3 | 1.000000 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

sex|on_thyroxine|query_on_thyroxine|pregnant|thyroid_surgery|i131_treatment|lithium|goitre|tumor|hypopituitary|tsh|class
---|---|---|---|---|---|---|---|---|---|---|---
(-inf-0.5]|(-inf-0.5]|all|(-inf-0.5]|(0.5-inf)|all|all|(-inf-0.5]|all|all|(0.0415-inf)|1
(0.5-inf)|(0.5-inf)|all|(-inf-0.5]|(-inf-0.5]|all|all|(-inf-0.5]|all|all|(0.0415-inf)|3
(-inf-0.5]|(0.5-inf)|all|(-inf-0.5]|(-inf-0.5]|all|all|(-inf-0.5]|all|all|(0.0415-inf)|1
(0.5-inf)|(-inf-0.5]|all|(-inf-0.5]|(-inf-0.5]|all|all|(-inf-0.5]|all|all|(0.0415-inf)|1
(-inf-0.5]|(-inf-0.5]|all|(-inf-0.5]|(-inf-0.5]|all|all|(-inf-0.5]|all|all|(0.0415-inf)|1
(0.5-inf)|(0.5-inf)|all|(-inf-0.5]|(0.5-inf)|all|all|(-inf-0.5]|all|all|(0.0195-0.0415]|1
(-inf-0.5]|(-inf-0.5]|all|(-inf-0.5]|(0.5-inf)|all|all|(-inf-0.5]|all|all|(0.0195-0.0415]|1
(0.5-inf)|(0.5-inf)|all|(-inf-0.5]|(-inf-0.5]|all|all|(-inf-0.5]|all|all|(0.0195-0.0415]|1
(-inf-0.5]|(0.5-inf)|all|(-inf-0.5]|(-inf-0.5]|all|all|(-inf-0.5]|all|all|(0.0195-0.0415]|3
(0.5-inf)|(-inf-0.5]|all|(-inf-0.5]|(-inf-0.5]|all|all|(-inf-0.5]|all|all|(0.0195-0.0415]|2
(-inf-0.5]|(-inf-0.5]|all|(-inf-0.5]|(-inf-0.5]|all|all|(-inf-0.5]|all|all|(0.0195-0.0415]|2
(-inf-0.5]|(-inf-0.5]|all|(-inf-0.5]|(-inf-0.5]|all|all|(0.5-inf)|all|all|(0.00605-0.0195]|1
(-inf-0.5]|(0.5-inf)|all|(0.5-inf)|(-inf-0.5]|all|all|(-inf-0.5]|all|all|(0.00605-0.0195]|1
(-inf-0.5]|(-inf-0.5]|all|(-inf-0.5]|(0.5-inf)|all|all|(-inf-0.5]|all|all|(0.00605-0.0195]|3
(-inf-0.5]|(0.5-inf)|all|(-inf-0.5]|(-inf-0.5]|all|all|(-inf-0.5]|all|all|(0.00605-0.0195]|3
(0.5-inf)|(0.5-inf)|all|(-inf-0.5]|(-inf-0.5]|all|all|(-inf-0.5]|all|all|(0.00605-0.0195]|3
(0.5-inf)|(-inf-0.5]|all|(-inf-0.5]|(-inf-0.5]|all|all|(-inf-0.5]|all|all|(0.00605-0.0195]|2
(-inf-0.5]|(-inf-0.5]|all|(-inf-0.5]|(-inf-0.5]|all|all|(-inf-0.5]|all|all|(0.00605-0.0195]|2
(-inf-0.5]|(-inf-0.5]|all|(0.5-inf)|(-inf-0.5]|all|all|(0.5-inf)|all|all|(-inf-0.00605]|3
(-inf-0.5]|(0.5-inf)|all|(-inf-0.5]|(-inf-0.5]|all|all|(0.5-inf)|all|all|(-inf-0.00605]|3
(0.5-inf)|(-inf-0.5]|all|(-inf-0.5]|(-inf-0.5]|all|all|(0.5-inf)|all|all|(-inf-0.00605]|3
(-inf-0.5]|(-inf-0.5]|all|(-inf-0.5]|(-inf-0.5]|all|all|(0.5-inf)|all|all|(-inf-0.00605]|3
(0.5-inf)|(0.5-inf)|all|(-inf-0.5]|(0.5-inf)|all|all|(-inf-0.5]|all|all|(-inf-0.00605]|3
(-inf-0.5]|(0.5-inf)|all|(-inf-0.5]|(0.5-inf)|all|all|(-inf-0.5]|all|all|(-inf-0.00605]|3
(-inf-0.5]|(0.5-inf)|all|(0.5-inf)|(-inf-0.5]|all|all|(-inf-0.5]|all|all|(-inf-0.00605]|3
(-inf-0.5]|(-inf-0.5]|all|(-inf-0.5]|(0.5-inf)|all|all|(-inf-0.5]|all|all|(-inf-0.00605]|3
(0.5-inf)|(-inf-0.5]|all|(-inf-0.5]|(0.5-inf)|all|all|(-inf-0.5]|all|all|(-inf-0.00605]|3
(-inf-0.5]|(-inf-0.5]|all|(0.5-inf)|(-inf-0.5]|all|all|(-inf-0.5]|all|all|(-inf-0.00605]|3
(0.5-inf)|(0.5-inf)|all|(-inf-0.5]|(-inf-0.5]|all|all|(-inf-0.5]|all|all|(-inf-0.00605]|3
(-inf-0.5]|(0.5-inf)|all|(-inf-0.5]|(-inf-0.5]|all|all|(-inf-0.5]|all|all|(-inf-0.00605]|3
(0.5-inf)|(-inf-0.5]|all|(-inf-0.5]|(-inf-0.5]|all|all|(-inf-0.5]|all|all|(-inf-0.00605]|3
(-inf-0.5]|(-inf-0.5]|all|(-inf-0.5]|(-inf-0.5]|all|all|(-inf-0.5]|all|all|(-inf-0.00605]|3

## JRip

Decision list:

rules | predicted class
---|---
(FTI <= 0.064) and (TSH >= 0.0062)|1 (163.0/14.0)
(TSH >= 0.0061) and (On_thyroxine <= 0) and (TT4 <= 0.15) and (Thyroid_surgery <= 0) and (T3 <= 0.02)|2 (257.0/1.0)
(TSH >= 0.0061) and (On_thyroxine <= 0) and (TT4 <= 0.15) and (T3 >= 0.0208)|2 (80.0/6.0)
|3 (5979.0/0.0)


## PART

Decision list:

rules | predicted class
---|---
TSH <= 0.006|3 (5842.0)
FTI <= 0.064 AND Thyroid_surgery <= 0.0 AND T3 <= 0.023 AND I131_treatment <= 0.0 AND Sex <= 0.0 AND Query_hypothyroid <= 0.0 AND On_thyroxine <= 0.0 AND Query_hyperthyroid <= 0.0 AND Tumor <= 0.0 AND TSH > 0.01679|1 (61.0)
FTI <= 0.064 AND T3 <= 0.026 AND Thyroid_surgery <= 0.0 AND On_antithyroid_medication <= 0.0 AND I131_treatment <= 0.0 AND TT4 <= 0.065|1 (71.0)
On_thyroxine > 0.0 AND FTI > 0.064|3 (98.0)
FTI > 0.064 AND TT4 <= 0.15 AND TT4 > 0.061 AND T3 <= 0.028 AND Age > 0.42 AND Sex <= 0.0 AND Query_hypothyroid <= 0.0 AND Query_hyperthyroid <= 0.0 AND Sick <= 0.0|2 (135.0/2.0)
FTI > 0.064 AND TT4 <= 0.15 AND Thyroid_surgery <= 0.0 AND TT4 > 0.058 AND T3 <= 0.028|2 (185.0)
FTI > 0.064 AND TT4 > 0.143|3 (24.0)
TT4 <= 0.124 AND FTI > 0.064 AND T3 > 0.016|3 (16.0)
FTI > 0.064 AND Thyroid_surgery <= 0.0|2 (13.0/1.0)
TSH <= 0.00959|3 (7.0)
T3 <= 0.026 AND Sex <= 0.0 AND On_thyroxine <= 0.0 AND T3 > 0.018|1 (5.0)
T3 <= 0.011 AND Thyroid_surgery <= 0.0|1 (7.0)
Thyroid_surgery <= 0.0 AND TT4 <= 0.054|3 (6.0)
Age <= 0.51|3 (5.0/1.0)
|1 (4.0)


## J48 Decision Tree

* TSH <= 0.006: 3 (5842.0)
* TSH > 0.006
	* FTI <= 0.064
		* TSH <= 0.01679
			* On_antithyroid_medication <= 0.0
				* T4U <= 0.104: 1 (12.0)
				* T4U > 0.104
					* TSH <= 0.00959: 3 (3.0)
					* TSH > 0.00959
						* T3 <= 0.024: 1 (4.0)
						* T3 > 0.024: 3 (2.0)
			* On_antithyroid_medication > 0.0: 3 (3.0)
		* TSH > 0.01679
			* Thyroid_surgery <= 0.0
				* I131_treatment <= 0.0
					* T3 <= 0.024: 1 (121.0)
					* T3 > 0.024
						* Age <= 0.63: 1 (3.0)
						* Age > 0.63: 3 (2.0)
				* I131_treatment > 0.0
					* Age <= 0.65: 1 (5.0)
					* Age > 0.65: 3 (2.0)
			* Thyroid_surgery > 0.0
				* Age <= 0.51
					* TT4 <= 0.046: 3 (2.0)
					* TT4 > 0.046: 1 (2.0)
				* Age > 0.51: 1 (2.0)
	* FTI > 0.064
		* On_thyroxine <= 0.0
			* TT4 <= 0.15
				* TT4 <= 0.061
					* T3 <= 0.019: 2 (11.0/1.0)
					* T3 > 0.019: 3 (6.0)
				* TT4 > 0.061
					* T3 <= 0.028
						* Age <= 0.42
							* Thyroid_surgery <= 0.0: 2 (77.0)
							* Thyroid_surgery > 0.0: 3 (9.0)
						* Age > 0.42: 2 (238.0/2.0)
					* T3 > 0.028
						* T4U <= 0.116: 3 (5.0)
						* T4U > 0.116: 2 (7.0)
			* TT4 > 0.15: 3 (23.0)
		* On_thyroxine > 0.0: 3 (98.0)


## SimpleCart Decision Tree

* TSH < 0.00605: 3(5842.0/0.0)
* TSH >= 0.00605
	* FTI < 0.064255
		* T3 < 0.0265: 1(149.0/9.0)
		* T3 >= 0.0265: 3(5.0/0.0)
	* FTI >= 0.064255
		* On_thyroxine < 0.5
			* TT4 < 0.1505
				* Thyroid_surgery < 0.5
					* TT4 < 0.058499999999999996
						* T3 < 0.01755: 2(5.0/1.0)
						* T3 >= 0.01755: 3(5.0/0.0)
					* TT4 >= 0.058499999999999996
						* T3 < 0.028999999999999998: 2(318.0/1.0)
						* T3 >= 0.028999999999999998
							* T4U < 0.11649999999999999: 3(6.0/0.0)
							* T4U >= 0.11649999999999999: 2(7.0/0.0)
				* Thyroid_surgery >= 0.5: 3(10.0/0.0)
			* TT4 >= 0.1505: 3(23.0/0.0)
		* On_thyroxine >= 0.5: 3(98.0/0.0)


