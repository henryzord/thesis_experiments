# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 3 | 0.926069 |
| TSH >= 0.00605 and FTI >= 0.064255 and On_thyroxine < 0.5 and TT4 < 0.1505 and Thyroid_surgery < 0.5 and TT4 >= 0.0565 and T3 < 0.0295 | 2 | 0.049320 |
| TSH > 0.00605 and FTI <= 0.064255 | 1 | 0.021068 |
| On_thyroxine <= 0.5 and Query_on_thyroxine = all and Thyroid_surgery <= 0.5 and Query_hyperthyroid = all and Goitre <= 0.5 and Hypopituitary = all and TSH > 0.00605 and TSH <= 0.0195 and T4U > 0.1025 and T4U <= 0.1415 | 2 | 0.011071 |
| TSH > 0.00605 and FTI > 0.064255 and On_thyroxine <= 0.5 and TT4 <= 0.1505 and TT4 > 0.0615 and T3 > 0.0285 | 2 | 0.000724 |
| TSH >= 0.00605 and FTI >= 0.064255 and On_thyroxine < 0.5 and TT4 < 0.1505 and Thyroid_surgery < 0.5 and TT4 < 0.0565 and T3 < 0.01555 | 2 | 0.000520 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| TSH <= 0.006 | 3 | 0.924185 |
| FTI <= 0.064 and Thyroid_surgery <= 0 and T3 <= 0.011 | 1 | 0.176190 |
| FTI <= 0.064 and T3 <= 0.027 | 1 | 0.066578 |
| On_thyroxine <= 0 and TT4 <= 0.15 and TT4 > 0.058 and T3 <= 0.028 and Thyroid_surgery <= 0 | 2 | 0.661824 |
| On_thyroxine > 0 | 3 | 0.896552 |
| Thyroid_surgery <= 0 and TT4 > 0.148 | 3 | 0.666667 |
| Thyroid_surgery <= 0 and T4U <= 0.113 and T3 > 0.0174 | 3 | 0.522667 |
| Thyroid_surgery <= 0 | 2 | 0.325792 |
|  | 3 | 1.000000 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| FTI <= 0.064 and TSH >= 0.0063 | 1 | 0.021068 |
| TSH >= 0.0061 and On_thyroxine <= 0 and T3 <= 0.02 and TT4 <= 0.144 and Thyroid_surgery <= 0 | 2 | 0.039862 |
| TSH >= 0.0061 and T3 >= 0.0208 and TT4 <= 0.118 and On_thyroxine <= 0 and T3 <= 0.029 | 2 | 0.008944 |
| TSH >= 0.0061 and On_thyroxine <= 0 and TT4 <= 0.15 and TT4 >= 0.123 and T4U >= 0.095 | 2 | 0.002999 |
|  | 3 | 1.000000 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

on_thyroxine|query_on_thyroxine|thyroid_surgery|query_hyperthyroid|goitre|hypopituitary|tsh|t4u|class
---|---|---|---|---|---|---|---|---
(-inf-0.5]|all|(0.5-inf)|all|(-inf-0.5]|all|(0.0415-inf)|(0.1415-inf)|1
(-inf-0.5]|all|(0.5-inf)|all|(-inf-0.5]|all|(0.0195-0.0415]|(0.1415-inf)|1
(-inf-0.5]|all|(0.5-inf)|all|(-inf-0.5]|all|(0.0415-inf)|(0.1025-0.1415]|1
(-inf-0.5]|all|(-inf-0.5]|all|(-inf-0.5]|all|(0.0195-0.0415]|(0.1415-inf)|3
(0.5-inf)|all|(-inf-0.5]|all|(-inf-0.5]|all|(0.0415-inf)|(0.1025-0.1415]|1
(-inf-0.5]|all|(-inf-0.5]|all|(-inf-0.5]|all|(0.0415-inf)|(0.1025-0.1415]|1
(-inf-0.5]|all|(-inf-0.5]|all|(0.5-inf)|all|(0.00605-0.0195]|(0.1415-inf)|1
(-inf-0.5]|all|(0.5-inf)|all|(-inf-0.5]|all|(0.0195-0.0415]|(0.1025-0.1415]|1
(0.5-inf)|all|(-inf-0.5]|all|(-inf-0.5]|all|(0.00605-0.0195]|(0.1415-inf)|3
(-inf-0.5]|all|(-inf-0.5]|all|(-inf-0.5]|all|(0.00605-0.0195]|(0.1415-inf)|3
(0.5-inf)|all|(-inf-0.5]|all|(-inf-0.5]|all|(0.0195-0.0415]|(0.1025-0.1415]|3
(-inf-0.5]|all|(-inf-0.5]|all|(-inf-0.5]|all|(0.0195-0.0415]|(0.1025-0.1415]|1
(-inf-0.5]|all|(-inf-0.5]|all|(0.5-inf)|all|(-inf-0.00605]|(0.1415-inf)|1
(0.5-inf)|all|(-inf-0.5]|all|(-inf-0.5]|all|(0.0415-inf)|(-inf-0.1025]|3
(0.5-inf)|all|(-inf-0.5]|all|(0.5-inf)|all|(-inf-0.00605]|(0.1415-inf)|1
(-inf-0.5]|all|(-inf-0.5]|all|(-inf-0.5]|all|(0.0415-inf)|(-inf-0.1025]|1
(0.5-inf)|all|(0.5-inf)|all|(-inf-0.5]|all|(-inf-0.00605]|(0.1415-inf)|1
(-inf-0.5]|all|(0.5-inf)|all|(-inf-0.5]|all|(0.00605-0.0195]|(0.1025-0.1415]|3
(-inf-0.5]|all|(0.5-inf)|all|(-inf-0.5]|all|(0.0195-0.0415]|(-inf-0.1025]|1
(-inf-0.5]|all|(-inf-0.5]|all|(-inf-0.5]|all|(-inf-0.00605]|(0.1415-inf)|3
(0.5-inf)|all|(-inf-0.5]|all|(-inf-0.5]|all|(-inf-0.00605]|(0.1415-inf)|3
(-inf-0.5]|all|(-inf-0.5]|all|(-inf-0.5]|all|(0.00605-0.0195]|(0.1025-0.1415]|2
(0.5-inf)|all|(-inf-0.5]|all|(-inf-0.5]|all|(0.00605-0.0195]|(0.1025-0.1415]|3
(-inf-0.5]|all|(-inf-0.5]|all|(-inf-0.5]|all|(0.0195-0.0415]|(-inf-0.1025]|2
(0.5-inf)|all|(-inf-0.5]|all|(-inf-0.5]|all|(0.0195-0.0415]|(-inf-0.1025]|3
(0.5-inf)|all|(-inf-0.5]|all|(0.5-inf)|all|(-inf-0.00605]|(0.1025-0.1415]|3
(-inf-0.5]|all|(-inf-0.5]|all|(0.5-inf)|all|(-inf-0.00605]|(0.1025-0.1415]|3
(0.5-inf)|all|(0.5-inf)|all|(-inf-0.5]|all|(-inf-0.00605]|(0.1025-0.1415]|3
(-inf-0.5]|all|(0.5-inf)|all|(-inf-0.5]|all|(-inf-0.00605]|(0.1025-0.1415]|3
(-inf-0.5]|all|(0.5-inf)|all|(-inf-0.5]|all|(0.00605-0.0195]|(-inf-0.1025]|3
(0.5-inf)|all|(-inf-0.5]|all|(-inf-0.5]|all|(-inf-0.00605]|(0.1025-0.1415]|3
(-inf-0.5]|all|(-inf-0.5]|all|(-inf-0.5]|all|(-inf-0.00605]|(0.1025-0.1415]|3
(-inf-0.5]|all|(-inf-0.5]|all|(-inf-0.5]|all|(0.00605-0.0195]|(-inf-0.1025]|2
(0.5-inf)|all|(-inf-0.5]|all|(-inf-0.5]|all|(0.00605-0.0195]|(-inf-0.1025]|3
(0.5-inf)|all|(-inf-0.5]|all|(0.5-inf)|all|(-inf-0.00605]|(-inf-0.1025]|3
(-inf-0.5]|all|(-inf-0.5]|all|(0.5-inf)|all|(-inf-0.00605]|(-inf-0.1025]|3
(0.5-inf)|all|(0.5-inf)|all|(-inf-0.5]|all|(-inf-0.00605]|(-inf-0.1025]|3
(-inf-0.5]|all|(0.5-inf)|all|(-inf-0.5]|all|(-inf-0.00605]|(-inf-0.1025]|3
(0.5-inf)|all|(-inf-0.5]|all|(-inf-0.5]|all|(-inf-0.00605]|(-inf-0.1025]|3
(-inf-0.5]|all|(-inf-0.5]|all|(-inf-0.5]|all|(-inf-0.00605]|(-inf-0.1025]|3

## JRip

Decision list:

rules | predicted class
---|---
(FTI <= 0.064) and (TSH >= 0.0063)|1 (163.0/14.0)
(TSH >= 0.0061) and (On_thyroxine <= 0) and (T3 <= 0.02) and (TT4 <= 0.144) and (Thyroid_surgery <= 0)|2 (255.0/1.0)
(TSH >= 0.0061) and (T3 >= 0.0208) and (TT4 <= 0.118) and (On_thyroxine <= 0) and (T3 <= 0.029)|2 (57.0/0.0)
(TSH >= 0.0061) and (On_thyroxine <= 0) and (TT4 <= 0.15) and (TT4 >= 0.123) and (T4U >= 0.095)|2 (20.0/1.0)
|3 (5984.0/0.0)


## PART

Decision list:

rules | predicted class
---|---
TSH <= 0.006|3 (5839.0)
FTI <= 0.064 AND Thyroid_surgery <= 0 AND T3 <= 0.011|1 (107.0/1.0)
FTI <= 0.064 AND T3 <= 0.027|1 (52.0/9.0)
On_thyroxine <= 0 AND TT4 <= 0.15 AND TT4 > 0.058 AND T3 <= 0.028 AND Thyroid_surgery <= 0|2 (319.0/1.0)
On_thyroxine > 0|3 (103.0)
Thyroid_surgery <= 0 AND TT4 > 0.148|3 (24.0)
Thyroid_surgery <= 0 AND T4U <= 0.113 AND T3 > 0.0174|3 (12.0/1.0)
Thyroid_surgery <= 0|2 (12.0/1.0)
|3 (11.0)


## J48 Decision Tree

* TSH <= 0.00605: 3 (5107.0)
* TSH > 0.00605
	* FTI <= 0.064255: 1 (144.0/13.0)
	* FTI > 0.064255
		* On_thyroxine <= 0.5
			* TT4 <= 0.1505
				* TT4 <= 0.0615: 2 (16.0/6.0)
				* TT4 > 0.0615
					* T3 <= 0.0285
						* Age <= 0.425
							* Thyroid_surgery <= 0.5: 2 (67.0)
							* Thyroid_surgery > 0.5: 3 (7.0)
						* Age > 0.425: 2 (208.0/2.0)
					* T3 > 0.0285: 2 (10.0/4.0)
			* TT4 > 0.1505: 3 (22.0)
		* On_thyroxine > 0.5: 3 (89.0)


## SimpleCart Decision Tree

* TSH < 0.00605: 3(5839.0/0.0)
* TSH >= 0.00605
	* FTI < 0.064255
		* T3 < 0.0275
			* On_antithyroid_medication < 0.5
				* T4U < 0.14250000000000002
					* TSH < 0.009545000000000001
						* TT4 < 0.0595: 1(9.0/0.0)
						* TT4 >= 0.0595: 3(3.0/0.0)
					* TSH >= 0.009545000000000001
						* I131_treatment < 0.5: 1(133.0/1.0)
						* I131_treatment >= 0.5
							* Age < 0.6000000000000001: 1(5.0/0.0)
							* Age >= 0.6000000000000001: 3(2.0/0.0)
				* T4U >= 0.14250000000000002: 3(2.0/1.0)
			* On_antithyroid_medication >= 0.5: 3(2.0/1.0)
		* T3 >= 0.0275: 3(4.0/0.0)
	* FTI >= 0.064255
		* On_thyroxine < 0.5
			* TT4 < 0.1505
				* Thyroid_surgery < 0.5
					* TT4 < 0.0565
						* T3 < 0.01555: 2(4.0/1.0)
						* T3 >= 0.01555: 3(4.0/0.0)
					* TT4 >= 0.0565
						* T3 < 0.0295: 2(320.0/1.0)
						* T3 >= 0.0295
							* Age < 0.37: 2(6.0/0.0)
							* Age >= 0.37: 3(5.0/0.0)
				* Thyroid_surgery >= 0.5: 3(11.0/0.0)
			* TT4 >= 0.1505: 3(24.0/0.0)
		* On_thyroxine >= 0.5: 3(101.0/0.0)


