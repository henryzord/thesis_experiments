# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| TSH < 0.00605 | 3 | 0.924209 |
| TSH >= 0.00605 and FTI >= 0.064255 and On_thyroxine < 0.5 and TT4 < 0.1505 and Thyroid_surgery < 0.5 and TT4 >= 0.058499999999999996 and T3 < 0.0295 | 2 | 0.049173 |
| TSH >= 0.00605 and FTI < 0.064255 and T3 < 0.0265 and Thyroid_surgery < 0.5 and On_antithyroid_medication < 0.5 and TSH >= 0.009545000000000001 and I131_treatment < 0.5 | 1 | 0.020427 |
| TSH >= 0.00605 and FTI >= 0.064255 and On_thyroxine >= 0.5 | 3 | 0.175559 |
| TSH >= 0.00605 and FTI >= 0.064255 and On_thyroxine < 0.5 and TT4 >= 0.1505 | 3 | 0.040080 |
| TSH >= 0.00605 and FTI >= 0.064255 and On_thyroxine < 0.5 and TT4 < 0.1505 and Thyroid_surgery >= 0.5 | 3 | 0.018443 |
| TSH >= 0.00605 and FTI < 0.064255 and T3 < 0.0265 and Thyroid_surgery < 0.5 and On_antithyroid_medication < 0.5 and TSH < 0.009545000000000001 and TT4 < 0.0595 | 1 | 0.001420 |
| TSH > 0.006 and FTI > 0.064 and On_thyroxine <= 0 and TT4 <= 0.15 and TT4 <= 0.061 and T3 > 0.019 | 3 | 0.012371 |
| TSH > 0.006 and FTI <= 0.064 and Thyroid_surgery <= 0 and T3 > 0.023 and TSH <= 0.017 | 3 | 0.008627 |
| TSH >= 0.00605 and FTI >= 0.064255 and On_thyroxine < 0.5 and TT4 < 0.1505 and Thyroid_surgery < 0.5 and TT4 >= 0.058499999999999996 and T3 >= 0.0295 and T4U >= 0.113 | 2 | 0.000975 |
| TSH >= 0.00605 and FTI >= 0.064255 and On_thyroxine < 0.5 and TT4 < 0.1505 and Thyroid_surgery < 0.5 and TT4 >= 0.058499999999999996 and T3 >= 0.0295 and T4U < 0.113 | 3 | 0.010331 |
| TSH >= 0.00605 and FTI < 0.064255 and T3 < 0.0265 and Thyroid_surgery < 0.5 and On_antithyroid_medication < 0.5 and TSH >= 0.009545000000000001 and I131_treatment >= 0.5 and Age < 0.655 | 1 | 0.000789 |
| TSH >= 0.00605 and FTI < 0.064255 and T3 < 0.0265 and Thyroid_surgery >= 0.5 and T3 >= 0.0108 | 3 | 0.006224 |
| TSH >= 0.00605 and FTI >= 0.064255 and On_thyroxine < 0.5 and TT4 < 0.1505 and Thyroid_surgery < 0.5 and TT4 < 0.058499999999999996 and T3 < 0.01755 | 2 | 0.000677 |
| TSH >= 0.00605 and FTI < 0.064255 and T3 < 0.0265 and Thyroid_surgery < 0.5 and On_antithyroid_medication < 0.5 and TSH < 0.009545000000000001 and TT4 >= 0.0595 | 3 | 0.006224 |
| TSH >= 0.00605 and FTI < 0.064255 and T3 < 0.0265 and Thyroid_surgery < 0.5 and On_antithyroid_medication < 0.5 and TSH >= 0.009545000000000001 and I131_treatment >= 0.5 and Age >= 0.655 | 3 | 0.004158 |
| TSH >= 0.00605 and FTI < 0.064255 and T3 >= 0.0265 | 3 | 0.010331 |
| TSH >= 0.00605 and FTI < 0.064255 and T3 < 0.0265 and Thyroid_surgery >= 0.5 and T3 < 0.0108 | 1 | 0.000211 |
| On_thyroxine <= 0.5 and Query_on_thyroxine = all and Thyroid_surgery > 0.5 and Lithium = all and Tumor = all and TSH > 0.0415 and TT4 > 0.0185 and TT4 <= 0.0525 | 3 | 0.004158 |
| TSH >= 0.00605 and FTI < 0.064255 and T3 < 0.0265 and Thyroid_surgery < 0.5 and On_antithyroid_medication >= 0.5 | 3 | 0.002778 |
| TSH > 0.006 and FTI <= 0.064 and Thyroid_surgery <= 0 and T3 > 0.023 and TSH > 0.017 | 1 | 0.000564 |

## Ordered rules

### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| FTI <= 0.064 and TSH >= 0.0062 | 1 | 0.020819 |
| TSH >= 0.0061 and On_thyroxine <= 0 and T3 <= 0.02 | 2 | 0.039193 |
| TSH >= 0.0061 and On_thyroxine <= 0 and TT4 <= 0.141 and T3 >= 0.0208 | 2 | 0.010234 |
|  | 3 | 0.999667 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

on_thyroxine|query_on_thyroxine|thyroid_surgery|lithium|tumor|tsh|tt4|class
---|---|---|---|---|---|---|---
(0.5-inf)|all|(-inf-0.5]|all|all|(0.0195-0.0415]|(0.1505-inf)|1
(-inf-0.5]|all|(-inf-0.5]|all|all|(0.0195-0.0415]|(0.1505-inf)|3
(0.5-inf)|all|(-inf-0.5]|all|all|(0.0415-inf)|(0.091795-0.1505]|3
(-inf-0.5]|all|(-inf-0.5]|all|all|(0.0415-inf)|(0.091795-0.1505]|1
(0.5-inf)|all|(-inf-0.5]|all|all|(0.00605-0.0195]|(0.1505-inf)|3
(-inf-0.5]|all|(-inf-0.5]|all|all|(0.00605-0.0195]|(0.1505-inf)|3
(-inf-0.5]|all|(-inf-0.5]|all|all|(0.0195-0.0415]|(0.091795-0.1505]|2
(0.5-inf)|all|(-inf-0.5]|all|all|(0.0195-0.0415]|(0.091795-0.1505]|3
(-inf-0.5]|all|(-inf-0.5]|all|all|(0.0415-inf)|(0.0685-0.091795]|2
(0.5-inf)|all|(-inf-0.5]|all|all|(0.0415-inf)|(0.0685-0.091795]|3
(0.5-inf)|all|(0.5-inf)|all|all|(-inf-0.00605]|(0.1505-inf)|3
(-inf-0.5]|all|(0.5-inf)|all|all|(-inf-0.00605]|(0.1505-inf)|3
(-inf-0.5]|all|(0.5-inf)|all|all|(0.00605-0.0195]|(0.091795-0.1505]|3
(0.5-inf)|all|(0.5-inf)|all|all|(0.0195-0.0415]|(0.0685-0.091795]|1
(0.5-inf)|all|(-inf-0.5]|all|all|(-inf-0.00605]|(0.1505-inf)|3
(-inf-0.5]|all|(-inf-0.5]|all|all|(-inf-0.00605]|(0.1505-inf)|3
(-inf-0.5]|all|(-inf-0.5]|all|all|(0.00605-0.0195]|(0.091795-0.1505]|2
(0.5-inf)|all|(-inf-0.5]|all|all|(0.00605-0.0195]|(0.091795-0.1505]|3
(0.5-inf)|all|(-inf-0.5]|all|all|(0.0195-0.0415]|(0.0685-0.091795]|3
(-inf-0.5]|all|(-inf-0.5]|all|all|(0.0195-0.0415]|(0.0685-0.091795]|2
(-inf-0.5]|all|(-inf-0.5]|all|all|(0.0415-inf)|(0.0525-0.0685]|1
(0.5-inf)|all|(-inf-0.5]|all|all|(0.0415-inf)|(0.0525-0.0685]|1
(0.5-inf)|all|(0.5-inf)|all|all|(-inf-0.00605]|(0.091795-0.1505]|3
(-inf-0.5]|all|(0.5-inf)|all|all|(-inf-0.00605]|(0.091795-0.1505]|3
(-inf-0.5]|all|(0.5-inf)|all|all|(0.00605-0.0195]|(0.0685-0.091795]|3
(-inf-0.5]|all|(0.5-inf)|all|all|(0.0195-0.0415]|(0.0525-0.0685]|1
(0.5-inf)|all|(-inf-0.5]|all|all|(-inf-0.00605]|(0.091795-0.1505]|3
(-inf-0.5]|all|(-inf-0.5]|all|all|(-inf-0.00605]|(0.091795-0.1505]|3
(-inf-0.5]|all|(0.5-inf)|all|all|(0.0415-inf)|(0.0185-0.0525]|3
(-inf-0.5]|all|(-inf-0.5]|all|all|(0.00605-0.0195]|(0.0685-0.091795]|2
(0.5-inf)|all|(-inf-0.5]|all|all|(0.00605-0.0195]|(0.0685-0.091795]|3
(-inf-0.5]|all|(-inf-0.5]|all|all|(0.0195-0.0415]|(0.0525-0.0685]|1
(0.5-inf)|all|(-inf-0.5]|all|all|(0.0195-0.0415]|(0.0525-0.0685]|1
(0.5-inf)|all|(-inf-0.5]|all|all|(0.0415-inf)|(0.0185-0.0525]|1
(-inf-0.5]|all|(-inf-0.5]|all|all|(0.0415-inf)|(0.0185-0.0525]|1
(-inf-0.5]|all|(0.5-inf)|all|all|(-inf-0.00605]|(0.0685-0.091795]|3
(-inf-0.5]|all|(0.5-inf)|all|all|(0.0195-0.0415]|(0.0185-0.0525]|1
(0.5-inf)|all|(-inf-0.5]|all|all|(-inf-0.00605]|(0.0685-0.091795]|3
(-inf-0.5]|all|(-inf-0.5]|all|all|(-inf-0.00605]|(0.0685-0.091795]|3
(-inf-0.5]|all|(0.5-inf)|all|all|(0.0415-inf)|(-inf-0.0185]|1
(-inf-0.5]|all|(-inf-0.5]|all|all|(0.00605-0.0195]|(0.0525-0.0685]|2
(0.5-inf)|all|(-inf-0.5]|all|all|(0.00605-0.0195]|(0.0525-0.0685]|3
(0.5-inf)|all|(-inf-0.5]|all|all|(0.0195-0.0415]|(0.0185-0.0525]|1
(-inf-0.5]|all|(-inf-0.5]|all|all|(0.0195-0.0415]|(0.0185-0.0525]|1
(0.5-inf)|all|(-inf-0.5]|all|all|(0.0415-inf)|(-inf-0.0185]|1
(-inf-0.5]|all|(-inf-0.5]|all|all|(0.0415-inf)|(-inf-0.0185]|1
(-inf-0.5]|all|(0.5-inf)|all|all|(-inf-0.00605]|(0.0525-0.0685]|3
(0.5-inf)|all|(-inf-0.5]|all|all|(-inf-0.00605]|(0.0525-0.0685]|3
(-inf-0.5]|all|(-inf-0.5]|all|all|(-inf-0.00605]|(0.0525-0.0685]|3
(0.5-inf)|all|(-inf-0.5]|all|all|(0.00605-0.0195]|(0.0185-0.0525]|1
(-inf-0.5]|all|(-inf-0.5]|all|all|(0.00605-0.0195]|(0.0185-0.0525]|1
(-inf-0.5]|all|(-inf-0.5]|all|all|(0.0195-0.0415]|(-inf-0.0185]|1
(0.5-inf)|all|(0.5-inf)|all|all|(-inf-0.00605]|(0.0185-0.0525]|1
(-inf-0.5]|all|(0.5-inf)|all|all|(-inf-0.00605]|(0.0185-0.0525]|1
(0.5-inf)|all|(-inf-0.5]|all|all|(-inf-0.00605]|(0.0185-0.0525]|3
(-inf-0.5]|all|(-inf-0.5]|all|all|(-inf-0.00605]|(0.0185-0.0525]|3
(-inf-0.5]|all|(-inf-0.5]|all|all|(0.00605-0.0195]|(-inf-0.0185]|1
(-inf-0.5]|all|(-inf-0.5]|all|all|(-inf-0.00605]|(-inf-0.0185]|3

## JRip

Decision list:

rules | predicted class
---|---
(FTI <= 0.064) and (TSH >= 0.0062)|1 (165.0/16.0)
(TSH >= 0.0061) and (On_thyroxine <= 0) and (T3 <= 0.02)|2 (265.0/7.0)
(TSH >= 0.0061) and (On_thyroxine <= 0) and (TT4 <= 0.141) and (T3 >= 0.0208)|2 (74.0/4.0)
|3 (5975.0/2.0)


## J48 Decision Tree

* TSH <= 0.006: 3 (5841.0)
* TSH > 0.006
	* FTI <= 0.064
		* Thyroid_surgery <= 0
			* T3 <= 0.023
				* I131_treatment <= 0
					* TSH <= 0.01679
						* Age <= 0.58: 1 (9.0/3.0)
						* Age > 0.58: 1 (8.0)
					* TSH > 0.01679: 1 (122.0)
				* I131_treatment > 0: 1 (7.0/2.0)
			* T3 > 0.023
				* TSH <= 0.017: 3 (6.0/1.0)
				* TSH > 0.017: 1 (7.0/2.0)
		* Thyroid_surgery > 0: 3 (6.0/2.0)
	* FTI > 0.064
		* On_thyroxine <= 0
			* TT4 <= 0.15
				* TT4 <= 0.061
					* T3 <= 0.019: 2 (9.0/1.0)
					* T3 > 0.019: 3 (6.0)
				* TT4 > 0.061
					* T3 <= 0.019
						* Sex <= 0
							* Query_hypothyroid <= 0
								* Query_hyperthyroid <= 0
									* Sick <= 0: 2 (142.0/3.0)
									* Sick > 0: 2 (6.0)
								* Query_hyperthyroid > 0: 2 (9.0)
							* Query_hypothyroid > 0: 2 (31.0)
						* Sex > 0: 2 (51.0)
					* T3 > 0.019
						* Thyroid_surgery <= 0
							* T3 <= 0.03
								* Sex <= 0
									* Query_hypothyroid <= 0
										* T3 <= 0.0201: 2 (8.0/1.0)
										* T3 > 0.0201: 2 (47.0)
									* Query_hypothyroid > 0: 2 (7.0)
								* Sex > 0: 2 (20.0)
							* T3 > 0.03: 2 (9.0/4.0)
						* Thyroid_surgery > 0: 3 (6.0)
			* TT4 > 0.15: 3 (20.0)
		* On_thyroxine > 0: 3 (102.0)


## SimpleCart Decision Tree

* TSH < 0.00605: 3(5841.0/0.0)
* TSH >= 0.00605
	* FTI < 0.064255
		* T3 < 0.0265
			* Thyroid_surgery < 0.5
				* On_antithyroid_medication < 0.5
					* TSH < 0.009545000000000001
						* TT4 < 0.0595: 1(9.0/0.0)
						* TT4 >= 0.0595: 3(3.0/0.0)
					* TSH >= 0.009545000000000001
						* I131_treatment < 0.5: 1(132.0/0.0)
						* I131_treatment >= 0.5
							* Age < 0.655: 1(5.0/0.0)
							* Age >= 0.655: 3(2.0/0.0)
				* On_antithyroid_medication >= 0.5: 3(2.0/1.0)
			* Thyroid_surgery >= 0.5
				* T3 < 0.0108: 1(2.0/1.0)
				* T3 >= 0.0108: 3(3.0/0.0)
		* T3 >= 0.0265: 3(5.0/0.0)
	* FTI >= 0.064255
		* On_thyroxine < 0.5
			* TT4 < 0.1505
				* Thyroid_surgery < 0.5
					* TT4 < 0.058499999999999996
						* T3 < 0.01755: 2(5.0/1.0)
						* T3 >= 0.01755: 3(5.0/0.0)
					* TT4 >= 0.058499999999999996
						* T3 < 0.0295: 2(319.0/1.0)
						* T3 >= 0.0295
							* T4U < 0.113: 3(5.0/0.0)
							* T4U >= 0.113: 2(6.0/0.0)
				* Thyroid_surgery >= 0.5: 3(9.0/0.0)
			* TT4 >= 0.1505: 3(20.0/0.0)
		* On_thyroxine >= 0.5: 3(102.0/0.0)


