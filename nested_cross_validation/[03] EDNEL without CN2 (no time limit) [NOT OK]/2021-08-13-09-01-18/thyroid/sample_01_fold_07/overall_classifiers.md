# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 3 | 0.925239 |
| TSH > 0.006 and FTI > 0.064 and On_thyroxine <= 0.0 and TT4 <= 0.149 and TT4 > 0.06 and Thyroid_surgery <= 0.0 | 2 | 0.049713 |
| TSH > 0.006 and FTI <= 0.064 | 1 | 0.021211 |
| TSH > 0.006 and FTI > 0.064 and On_thyroxine <= 0.0 and TT4 <= 0.149 and TT4 <= 0.06 | 2 | 0.000451 |
| TSH >= 0.00605 and FTI >= 0.064255 and On_thyroxine < 0.5 and TT4 < 0.1505 and Thyroid_surgery < 0.5 and TT4 >= 0.058499999999999996 and T3 < 0.0295 | 2 | 0.049985 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| TSH <= 0.00605 | 3 | 0.923393 |
| FTI > 0.064465 and On_thyroxine <= 0.5 and TT4 <= 0.1505 and TT4 > 0.0605 and T3 <= 0.0295 and Thyroid_surgery <= 0.5 | 2 | 0.512784 |
| FTI > 0.0645 and On_thyroxine > 0.5 | 3 | 0.374517 |
| FTI <= 0.0645 | 1 | 0.658862 |
| Thyroid_surgery <= 0.5 and TT4 > 0.1485 | 3 | 0.617647 |
| Thyroid_surgery <= 0.5 and T4U <= 0.113 and T3 > 0.019049999999999997 | 3 | 0.566667 |
| Thyroid_surgery <= 0.5 | 2 | 0.312963 |
|  | 3 | 1.000000 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| FTI <= 0.064 and TSH >= 0.0062 | 1 | 0.021211 |
| TSH >= 0.0061 and On_thyroxine <= 0 and T3 <= 0.019 | 2 | 0.036482 |
| TSH >= 0.0061 and On_thyroxine <= 0 and TT4 <= 0.141 and T3 >= 0.0208 and T3 <= 0.029 | 2 | 0.011245 |
| TSH >= 0.0062 and On_thyroxine <= 0 and T3 <= 0.02 | 2 | 0.001336 |
| TSH >= 0.0062 and T3 >= 0.027 and TT4 <= 0.15 and Age <= 0.36 | 2 | 0.000817 |
|  | 3 | 0.999833 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

sex|on_thyroxine|query_on_thyroxine|on_antithyroid_medication|sick|pregnant|thyroid_surgery|i131_treatment|query_hyperthyroid|lithium|goitre|tumor|tsh|class
---|---|---|---|---|---|---|---|---|---|---|---|---|---
(-inf-0.5]|(-inf-0.5]|all|all|all|(-inf-0.5]|(0.5-inf)|all|all|all|(-inf-0.5]|all|(0.0415-inf)|1
(0.5-inf)|(0.5-inf)|all|all|all|(-inf-0.5]|(-inf-0.5]|all|all|all|(-inf-0.5]|all|(0.0415-inf)|3
(-inf-0.5]|(0.5-inf)|all|all|all|(-inf-0.5]|(-inf-0.5]|all|all|all|(-inf-0.5]|all|(0.0415-inf)|1
(0.5-inf)|(-inf-0.5]|all|all|all|(-inf-0.5]|(-inf-0.5]|all|all|all|(-inf-0.5]|all|(0.0415-inf)|1
(-inf-0.5]|(-inf-0.5]|all|all|all|(-inf-0.5]|(-inf-0.5]|all|all|all|(-inf-0.5]|all|(0.0415-inf)|1
(0.5-inf)|(0.5-inf)|all|all|all|(-inf-0.5]|(0.5-inf)|all|all|all|(-inf-0.5]|all|(0.0195-0.0415]|1
(-inf-0.5]|(-inf-0.5]|all|all|all|(-inf-0.5]|(0.5-inf)|all|all|all|(-inf-0.5]|all|(0.0195-0.0415]|1
(0.5-inf)|(0.5-inf)|all|all|all|(-inf-0.5]|(-inf-0.5]|all|all|all|(-inf-0.5]|all|(0.0195-0.0415]|1
(-inf-0.5]|(0.5-inf)|all|all|all|(-inf-0.5]|(-inf-0.5]|all|all|all|(-inf-0.5]|all|(0.0195-0.0415]|3
(0.5-inf)|(-inf-0.5]|all|all|all|(-inf-0.5]|(-inf-0.5]|all|all|all|(-inf-0.5]|all|(0.0195-0.0415]|1
(-inf-0.5]|(-inf-0.5]|all|all|all|(-inf-0.5]|(-inf-0.5]|all|all|all|(-inf-0.5]|all|(0.0195-0.0415]|2
(-inf-0.5]|(-inf-0.5]|all|all|all|(-inf-0.5]|(-inf-0.5]|all|all|all|(0.5-inf)|all|(0.00605-0.0195]|1
(-inf-0.5]|(-inf-0.5]|all|all|all|(-inf-0.5]|(0.5-inf)|all|all|all|(-inf-0.5]|all|(0.00605-0.0195]|3
(-inf-0.5]|(-inf-0.5]|all|all|all|(0.5-inf)|(-inf-0.5]|all|all|all|(0.5-inf)|all|(-inf-0.00605]|3
(0.5-inf)|(0.5-inf)|all|all|all|(-inf-0.5]|(-inf-0.5]|all|all|all|(-inf-0.5]|all|(0.00605-0.0195]|3
(-inf-0.5]|(0.5-inf)|all|all|all|(-inf-0.5]|(-inf-0.5]|all|all|all|(-inf-0.5]|all|(0.00605-0.0195]|3
(0.5-inf)|(-inf-0.5]|all|all|all|(-inf-0.5]|(-inf-0.5]|all|all|all|(-inf-0.5]|all|(0.00605-0.0195]|2
(-inf-0.5]|(-inf-0.5]|all|all|all|(-inf-0.5]|(-inf-0.5]|all|all|all|(-inf-0.5]|all|(0.00605-0.0195]|2
(0.5-inf)|(0.5-inf)|all|all|all|(-inf-0.5]|(-inf-0.5]|all|all|all|(0.5-inf)|all|(-inf-0.00605]|1
(-inf-0.5]|(0.5-inf)|all|all|all|(-inf-0.5]|(-inf-0.5]|all|all|all|(0.5-inf)|all|(-inf-0.00605]|3
(0.5-inf)|(-inf-0.5]|all|all|all|(-inf-0.5]|(-inf-0.5]|all|all|all|(0.5-inf)|all|(-inf-0.00605]|3
(-inf-0.5]|(-inf-0.5]|all|all|all|(-inf-0.5]|(-inf-0.5]|all|all|all|(0.5-inf)|all|(-inf-0.00605]|3
(0.5-inf)|(0.5-inf)|all|all|all|(-inf-0.5]|(0.5-inf)|all|all|all|(-inf-0.5]|all|(-inf-0.00605]|3
(-inf-0.5]|(0.5-inf)|all|all|all|(-inf-0.5]|(0.5-inf)|all|all|all|(-inf-0.5]|all|(-inf-0.00605]|3
(-inf-0.5]|(0.5-inf)|all|all|all|(0.5-inf)|(-inf-0.5]|all|all|all|(-inf-0.5]|all|(-inf-0.00605]|3
(-inf-0.5]|(-inf-0.5]|all|all|all|(-inf-0.5]|(0.5-inf)|all|all|all|(-inf-0.5]|all|(-inf-0.00605]|3
(0.5-inf)|(-inf-0.5]|all|all|all|(-inf-0.5]|(0.5-inf)|all|all|all|(-inf-0.5]|all|(-inf-0.00605]|3
(-inf-0.5]|(-inf-0.5]|all|all|all|(0.5-inf)|(-inf-0.5]|all|all|all|(-inf-0.5]|all|(-inf-0.00605]|3
(0.5-inf)|(0.5-inf)|all|all|all|(-inf-0.5]|(-inf-0.5]|all|all|all|(-inf-0.5]|all|(-inf-0.00605]|3
(-inf-0.5]|(0.5-inf)|all|all|all|(-inf-0.5]|(-inf-0.5]|all|all|all|(-inf-0.5]|all|(-inf-0.00605]|3
(0.5-inf)|(-inf-0.5]|all|all|all|(-inf-0.5]|(-inf-0.5]|all|all|all|(-inf-0.5]|all|(-inf-0.00605]|3
(-inf-0.5]|(-inf-0.5]|all|all|all|(-inf-0.5]|(-inf-0.5]|all|all|all|(-inf-0.5]|all|(-inf-0.00605]|3

## JRip

Decision list:

rules | predicted class
---|---
(FTI <= 0.064) and (TSH >= 0.0062)|1 (162.0/13.0)
(TSH >= 0.0061) and (On_thyroxine <= 0) and (T3 <= 0.019)|2 (248.0/8.0)
(TSH >= 0.0061) and (On_thyroxine <= 0) and (TT4 <= 0.141) and (T3 >= 0.0208) and (T3 <= 0.029)|2 (71.0/0.0)
(TSH >= 0.0062) and (On_thyroxine <= 0) and (T3 <= 0.02)|2 (18.0/2.0)
(TSH >= 0.0062) and (T3 >= 0.027) and (TT4 <= 0.15) and (Age <= 0.36)|2 (9.0/2.0)
|3 (5966.0/1.0)


## PART

Decision list:

rules | predicted class
---|---
TSH <= 0.00605|3 (5186.0)
FTI > 0.064465 AND On_thyroxine <= 0.5 AND TT4 <= 0.1505 AND TT4 > 0.0605 AND T3 <= 0.0295 AND Thyroid_surgery <= 0.5|2 (288.0/1.0)
FTI > 0.0645 AND On_thyroxine > 0.5|3 (85.0)
FTI <= 0.0645|1 (145.0/13.0)
Thyroid_surgery <= 0.5 AND TT4 > 0.1485|3 (19.0)
Thyroid_surgery <= 0.5 AND T4U <= 0.113 AND T3 > 0.019049999999999997|3 (10.0)
Thyroid_surgery <= 0.5|2 (12.0/1.0)
|3 (10.0)


## J48 Decision Tree

* TSH <= 0.006: 3 (5002.0)
* TSH > 0.006
	* FTI <= 0.064: 1 (139.0/11.0)
	* FTI > 0.064
		* On_thyroxine <= 0.0
			* TT4 <= 0.149
				* TT4 <= 0.06: 2 (12.0/6.0)
				* TT4 > 0.06
					* Thyroid_surgery <= 0.0: 2 (285.0/4.0)
					* Thyroid_surgery > 0.0: 3 (10.0)
			* TT4 > 0.149: 3 (17.0)
		* On_thyroxine > 0.0: 3 (85.0)


## SimpleCart Decision Tree

* TSH < 0.00605: 3(5834.0/0.0)
* TSH >= 0.00605
	* FTI < 0.064255
		* T3 < 0.0265
			* On_antithyroid_medication < 0.5
				* Thyroid_surgery < 0.5
					* I131_treatment < 0.5
						* TSH < 0.009545000000000001: 1(9.0/2.0)
						* TSH >= 0.009545000000000001: 1(130.0/0.0)
					* I131_treatment >= 0.5: 1(5.0/2.0)
				* Thyroid_surgery >= 0.5: 1(4.0/3.0)
			* On_antithyroid_medication >= 0.5: 3(2.0/1.0)
		* T3 >= 0.0265: 3(4.0/0.0)
	* FTI >= 0.064255
		* On_thyroxine < 0.5
			* TT4 < 0.1505
				* Thyroid_surgery < 0.5
					* TT4 < 0.058499999999999996
						* T3 < 0.01555: 2(4.0/1.0)
						* T3 >= 0.01555: 3(6.0/0.0)
					* TT4 >= 0.058499999999999996
						* T3 < 0.0295: 2(324.0/1.0)
						* T3 >= 0.0295
							* T4U < 0.113: 3(6.0/0.0)
							* T4U >= 0.113: 2(7.0/0.0)
				* Thyroid_surgery >= 0.5: 3(11.0/0.0)
			* TT4 >= 0.1505: 3(21.0/0.0)
		* On_thyroxine >= 0.5: 3(97.0/0.0)


