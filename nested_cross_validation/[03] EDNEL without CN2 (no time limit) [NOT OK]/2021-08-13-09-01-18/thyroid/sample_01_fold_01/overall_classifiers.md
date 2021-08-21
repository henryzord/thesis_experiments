# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 3 | 0.926069 |
| TSH >= 0.00605 and FTI >= 0.064255 and On_thyroxine < 0.5 and TT4 < 0.1505 and Thyroid_surgery < 0.5 | 2 | 0.049102 |
| On_thyroxine > 0.5 and Query_on_thyroxine = all and On_antithyroid_medication = all and Sick <= 0.5 and Pregnant <= 0.5 and Thyroid_surgery <= 0.5 and Query_hyperthyroid = all and Lithium = all and Goitre <= 0.5 and Tumor = all and Hypopituitary = all and TSH > 0.0415 | 1 | 0.000831 |
| On_thyroxine <= 0.5 and Query_on_thyroxine = all and On_antithyroid_medication = all and Sick <= 0.5 and Pregnant <= 0.5 and Thyroid_surgery > 0.5 and Query_hyperthyroid = all and Lithium = all and Goitre <= 0.5 and Tumor = all and Hypopituitary = all and TSH > 0.0415 | 1 | 0.000355 |
| TSH > 0.00605 and FTI <= 0.064255 and T3 <= 0.025500000000000002 | 1 | 0.021567 |
| TSH >= 0.00605 and FTI < 0.064255 | 1 | 0.021068 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| TSH <= 0.00605 | 3 | 0.924221 |
| FTI <= 0.064255 and T3 <= 0.0115 | 1 | 0.188034 |
| FTI <= 0.064255 and TSH > 0.018395 and Age <= 0.665 | 1 | 0.052678 |
| On_thyroxine <= 0.5 and FTI > 0.064465 and TT4 <= 0.1505 and TT4 > 0.058499999999999996 and T3 <= 0.0295 and Sex <= 0.5 and Thyroid_surgery <= 0.5 | 2 | 0.600010 |
| On_thyroxine > 0.5 | 3 | 0.534031 |
| Sex > 0.5 | 2 | 0.519231 |
| FTI > 0.0645 and Thyroid_surgery <= 0.5 and TT4 > 0.1485 | 3 | 0.575000 |
| TT4 <= 0.1245 | 3 | 0.616026 |
|  | 2 | 0.578947 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| FTI <= 0.064 and TSH >= 0.0062 | 1 | 0.021068 |
| TSH >= 0.0061 and On_thyroxine <= 0 and T3 <= 0.019 and Thyroid_surgery <= 0 | 2 | 0.037414 |
| TSH >= 0.0061 and On_thyroxine <= 0 and TT4 <= 0.141 and Thyroid_surgery <= 0 and T4U >= 0.089 | 2 | 0.012650 |
|  | 3 | 0.999167 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

on_thyroxine|query_on_thyroxine|on_antithyroid_medication|sick|pregnant|thyroid_surgery|query_hyperthyroid|lithium|goitre|tumor|hypopituitary|tsh|class
---|---|---|---|---|---|---|---|---|---|---|---|---
(-inf-0.5]|all|all|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|all|all|(-inf-0.5]|all|all|(0.0415-inf)|1
(0.5-inf)|all|all|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|all|all|(-inf-0.5]|all|all|(0.0415-inf)|1
(-inf-0.5]|all|all|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|all|all|(-inf-0.5]|all|all|(0.0415-inf)|1
(0.5-inf)|all|all|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|all|all|(-inf-0.5]|all|all|(0.0195-0.0415]|1
(-inf-0.5]|all|all|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|all|all|(-inf-0.5]|all|all|(0.0195-0.0415]|3
(-inf-0.5]|all|all|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|all|all|(-inf-0.5]|all|all|(0.0195-0.0415]|2
(0.5-inf)|all|all|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|all|all|(-inf-0.5]|all|all|(0.0195-0.0415]|3
(-inf-0.5]|all|all|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|all|all|(-inf-0.5]|all|all|(0.0195-0.0415]|2
(-inf-0.5]|all|all|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|all|all|(0.5-inf)|all|all|(0.00605-0.0195]|1
(-inf-0.5]|all|all|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|all|all|(-inf-0.5]|all|all|(0.00605-0.0195]|3
(0.5-inf)|all|all|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|all|all|(-inf-0.5]|all|all|(0.00605-0.0195]|1
(0.5-inf)|all|all|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|all|all|(-inf-0.5]|all|all|(0.00605-0.0195]|3
(-inf-0.5]|all|all|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|all|all|(-inf-0.5]|all|all|(0.00605-0.0195]|2
(-inf-0.5]|all|all|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|all|all|(0.5-inf)|all|all|(-inf-0.00605]|3
(0.5-inf)|all|all|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|all|all|(-inf-0.5]|all|all|(0.00605-0.0195]|3
(-inf-0.5]|all|all|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|all|all|(-inf-0.5]|all|all|(0.00605-0.0195]|2
(-inf-0.5]|all|all|(0.5-inf)|(-inf-0.5]|(0.5-inf)|all|all|(-inf-0.5]|all|all|(-inf-0.00605]|3
(0.5-inf)|all|all|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|all|all|(0.5-inf)|all|all|(-inf-0.00605]|3
(-inf-0.5]|all|all|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|all|all|(0.5-inf)|all|all|(-inf-0.00605]|3
(0.5-inf)|all|all|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|all|all|(-inf-0.5]|all|all|(-inf-0.00605]|3
(-inf-0.5]|all|all|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|all|all|(-inf-0.5]|all|all|(-inf-0.00605]|3
(0.5-inf)|all|all|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|all|all|(-inf-0.5]|all|all|(-inf-0.00605]|3
(-inf-0.5]|all|all|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|all|all|(-inf-0.5]|all|all|(-inf-0.00605]|3
(0.5-inf)|all|all|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|all|all|(-inf-0.5]|all|all|(-inf-0.00605]|3
(-inf-0.5]|all|all|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|all|all|(-inf-0.5]|all|all|(-inf-0.00605]|3
(0.5-inf)|all|all|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|all|all|(-inf-0.5]|all|all|(-inf-0.00605]|3
(-inf-0.5]|all|all|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|all|all|(-inf-0.5]|all|all|(-inf-0.00605]|3

## JRip

Decision list:

rules | predicted class
---|---
(FTI <= 0.064) and (TSH >= 0.0062)|1 (163.0/14.0)
(TSH >= 0.0061) and (On_thyroxine <= 0) and (T3 <= 0.019) and (Thyroid_surgery <= 0)|2 (243.0/3.0)
(TSH >= 0.0061) and (On_thyroxine <= 0) and (TT4 <= 0.141) and (Thyroid_surgery <= 0) and (T4U >= 0.089)|2 (87.0/2.0)
|3 (5986.0/5.0)


## PART

Decision list:

rules | predicted class
---|---
TSH <= 0.00605|3 (5842.0)
FTI <= 0.064255 AND T3 <= 0.0115|1 (115.0/1.0)
FTI <= 0.064255 AND TSH > 0.018395 AND Age <= 0.665|1 (31.0/2.0)
On_thyroxine <= 0.5 AND FTI > 0.064465 AND TT4 <= 0.1505 AND TT4 > 0.058499999999999996 AND T3 <= 0.0295 AND Sex <= 0.5 AND Thyroid_surgery <= 0.5|2 (248.0/1.0)
On_thyroxine > 0.5|3 (102.0)
Sex > 0.5|2 (78.0/6.0)
FTI > 0.0645 AND Thyroid_surgery <= 0.5 AND TT4 > 0.1485|3 (21.0)
TT4 <= 0.1245|3 (33.0/8.0)
|2 (9.0/1.0)


## J48 Decision Tree

* TSH <= 0.00605: 3 (5842.0)
* TSH > 0.00605
	* FTI <= 0.064255
		* T3 <= 0.025500000000000002: 1 (157.0/9.0)
		* T3 > 0.025500000000000002: 3 (6.0/1.0)
	* FTI > 0.064255
		* On_thyroxine <= 0.5
			* TT4 <= 0.1505
				* TT4 <= 0.058499999999999996
					* T3 <= 0.01755: 2 (6.0/1.0)
					* T3 > 0.01755: 3 (6.0)
				* TT4 > 0.058499999999999996
					* T3 <= 0.0295
						* Thyroid_surgery <= 0.5: 2 (318.0/1.0)
						* Thyroid_surgery > 0.5: 3 (9.0)
					* T3 > 0.0295
						* T4U <= 0.113: 3 (5.0)
						* T4U > 0.113: 2 (8.0)
			* TT4 > 0.1505: 3 (23.0)
		* On_thyroxine > 0.5: 3 (99.0)


## SimpleCart Decision Tree

* TSH < 0.00605: 3(5842.0/0.0)
* TSH >= 0.00605
	* FTI < 0.064255: 1(149.0/14.0)
	* FTI >= 0.064255
		* On_thyroxine < 0.5
			* TT4 < 0.1505
				* Thyroid_surgery < 0.5: 2(330.0/13.0)
				* Thyroid_surgery >= 0.5: 3(9.0/0.0)
			* TT4 >= 0.1505: 3(23.0/0.0)
		* On_thyroxine >= 0.5: 3(99.0/0.0)


