# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| TSH < 0.00605 | 3 | 0.923101 |
| TSH >= 0.00605 and FTI >= 0.064255 and On_thyroxine < 0.5 and TT4 < 0.1505 and Thyroid_surgery < 0.5 and TT4 >= 0.058499999999999996 | 2 | 0.050301 |
| TSH >= 0.00605 and FTI < 0.064255 | 1 | 0.021204 |
| TSH >= 0.00605 and FTI >= 0.064255 and On_thyroxine >= 0.5 | 3 | 0.166381 |
| TSH >= 0.00605 and FTI >= 0.064255 and On_thyroxine < 0.5 and TT4 >= 0.1505 | 3 | 0.041420 |
| TSH > 0.00605 and FTI > 0.064255 and On_thyroxine <= 0.5 and TT4 <= 0.1505 and Thyroid_surgery > 0.5 | 3 | 0.022133 |
| TSH >= 0.00605 and FTI >= 0.064255 and On_thyroxine < 0.5 and TT4 < 0.1505 and Thyroid_surgery < 0.5 and TT4 < 0.058499999999999996 | 3 | 0.008367 |
| Sex <= 0.5 and On_thyroxine > 0.5 and Query_on_thyroxine = all and On_antithyroid_medication = all and Pregnant <= 0.5 and Thyroid_surgery <= 0.5 and Goitre <= 0.5 and Hypopituitary = all and TSH > 0.00605 and TSH <= 0.0195 | 3 | 0.095007 |
| Sex <= 0.5 and On_thyroxine <= 0.5 and Query_on_thyroxine = all and On_antithyroid_medication = all and Pregnant <= 0.5 and Thyroid_surgery > 0.5 and Goitre <= 0.5 and Hypopituitary = all and TSH > 0.00605 and TSH <= 0.0195 | 3 | 0.022133 |
| TSH > 0.00605 and FTI > 0.064255 and On_thyroxine <= 0.5 and TT4 <= 0.1505 and Thyroid_surgery <= 0.5 | 2 | 0.050071 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| TSH <= 0.00605 | 3 | 0.923101 |
| FTI > 0.064465 and On_thyroxine <= 0.5 and TT4 <= 0.1505 and TT4 > 0.0615 and T3 <= 0.0177 | 2 | 0.403277 |
| FTI <= 0.064465 | 1 | 0.327072 |
| On_thyroxine <= 0.5 and TT4 <= 0.1505 and Thyroid_surgery <= 0.5 and TT4 > 0.056 and Age <= 0.765 | 2 | 0.417199 |
|  | 3 | 0.945455 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| FTI <= 0.064 and TSH >= 0.0062 | 1 | 0.021204 |
| TSH >= 0.0061 and On_thyroxine <= 0 and T3 <= 0.02 and Thyroid_surgery <= 0 and TT4 <= 0.148 | 2 | 0.040541 |
| TSH >= 0.0061 and On_thyroxine <= 0 and TT4 <= 0.141 and T3 >= 0.0208 | 2 | 0.011380 |
| TSH >= 0.016 and T3 >= 0.027 and TSH <= 0.019 | 2 | 0.000334 |
|  | 3 | 1.000000 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

sex|on_thyroxine|query_on_thyroxine|on_antithyroid_medication|pregnant|thyroid_surgery|goitre|hypopituitary|tsh|class
---|---|---|---|---|---|---|---|---|---
(-inf-0.5]|(-inf-0.5]|all|all|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|all|(0.0415-inf)|1
(0.5-inf)|(0.5-inf)|all|all|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|all|(0.0415-inf)|3
(-inf-0.5]|(0.5-inf)|all|all|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|all|(0.0415-inf)|1
(0.5-inf)|(-inf-0.5]|all|all|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|all|(0.0415-inf)|1
(-inf-0.5]|(-inf-0.5]|all|all|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|all|(0.0415-inf)|1
(0.5-inf)|(0.5-inf)|all|all|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|all|(0.0195-0.0415]|1
(-inf-0.5]|(-inf-0.5]|all|all|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|all|(0.0195-0.0415]|1
(-inf-0.5]|(0.5-inf)|all|all|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|all|(0.0195-0.0415]|3
(0.5-inf)|(0.5-inf)|all|all|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|all|(0.0195-0.0415]|1
(0.5-inf)|(-inf-0.5]|all|all|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|all|(0.0195-0.0415]|1
(-inf-0.5]|(-inf-0.5]|all|all|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|all|(0.0195-0.0415]|2
(-inf-0.5]|(-inf-0.5]|all|all|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|all|(0.00605-0.0195]|1
(-inf-0.5]|(-inf-0.5]|all|all|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|all|(0.00605-0.0195]|3
(-inf-0.5]|(-inf-0.5]|all|all|(0.5-inf)|(-inf-0.5]|(0.5-inf)|all|(-inf-0.00605]|3
(0.5-inf)|(0.5-inf)|all|all|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|all|(0.00605-0.0195]|3
(-inf-0.5]|(0.5-inf)|all|all|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|all|(0.00605-0.0195]|3
(0.5-inf)|(-inf-0.5]|all|all|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|all|(0.00605-0.0195]|2
(-inf-0.5]|(-inf-0.5]|all|all|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|all|(0.00605-0.0195]|2
(0.5-inf)|(0.5-inf)|all|all|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|all|(-inf-0.00605]|1
(-inf-0.5]|(0.5-inf)|all|all|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|all|(-inf-0.00605]|3
(-inf-0.5]|(0.5-inf)|all|all|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|all|(-inf-0.00605]|3
(0.5-inf)|(0.5-inf)|all|all|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|all|(-inf-0.00605]|3
(0.5-inf)|(-inf-0.5]|all|all|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|all|(-inf-0.00605]|3
(-inf-0.5]|(-inf-0.5]|all|all|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|all|(-inf-0.00605]|3
(0.5-inf)|(-inf-0.5]|all|all|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|all|(-inf-0.00605]|3
(-inf-0.5]|(0.5-inf)|all|all|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|all|(-inf-0.00605]|3
(-inf-0.5]|(-inf-0.5]|all|all|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|all|(-inf-0.00605]|3
(-inf-0.5]|(-inf-0.5]|all|all|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|all|(-inf-0.00605]|3
(0.5-inf)|(0.5-inf)|all|all|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|all|(-inf-0.00605]|3
(-inf-0.5]|(0.5-inf)|all|all|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|all|(-inf-0.00605]|3
(-inf-0.5]|(-inf-0.5]|all|all|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|all|(-inf-0.00605]|3
(0.5-inf)|(-inf-0.5]|all|all|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|all|(-inf-0.00605]|3

## JRip

Decision list:

rules | predicted class
---|---
(FTI <= 0.064) and (TSH >= 0.0062)|1 (162.0/13.0)
(TSH >= 0.0061) and (On_thyroxine <= 0) and (T3 <= 0.02) and (Thyroid_surgery <= 0) and (TT4 <= 0.148)|2 (259.0/1.0)
(TSH >= 0.0061) and (On_thyroxine <= 0) and (TT4 <= 0.141) and (T3 >= 0.0208)|2 (82.0/5.0)
(TSH >= 0.016) and (T3 >= 0.027) and (TSH <= 0.019)|2 (2.0/0.0)
|3 (5971.0/0.0)


## PART

Decision list:

rules | predicted class
---|---
TSH <= 0.00605|3 (2928.0)
FTI > 0.064465 AND On_thyroxine <= 0.5 AND TT4 <= 0.1505 AND TT4 > 0.0615 AND T3 <= 0.0177|2 (105.0/1.0)
FTI <= 0.064465|1 (81.0/7.0)
On_thyroxine <= 0.5 AND TT4 <= 0.1505 AND Thyroid_surgery <= 0.5 AND TT4 > 0.056 AND Age <= 0.765|2 (63.0/1.0)
|3 (61.0/3.0)


## J48 Decision Tree

* TSH <= 0.00605: 3 (3887.0)
* TSH > 0.00605
	* FTI <= 0.064255: 1 (109.0/9.0)
	* FTI > 0.064255
		* On_thyroxine <= 0.5
			* TT4 <= 0.1505
				* Thyroid_surgery <= 0.5: 2 (234.0/10.0)
				* Thyroid_surgery > 0.5: 3 (9.0)
			* TT4 > 0.1505: 3 (13.0)
		* On_thyroxine > 0.5: 3 (66.0)


## SimpleCart Decision Tree

* TSH < 0.00605: 3(5834.0/0.0)
* TSH >= 0.00605
	* FTI < 0.064255: 1(149.0/13.0)
	* FTI >= 0.064255
		* On_thyroxine < 0.5
			* TT4 < 0.1505
				* Thyroid_surgery < 0.5
					* TT4 < 0.058499999999999996: 3(7.0/5.0)
					* TT4 >= 0.058499999999999996: 2(332.0/7.0)
				* Thyroid_surgery >= 0.5: 3(11.0/0.0)
			* TT4 >= 0.1505: 3(21.0/0.0)
		* On_thyroxine >= 0.5: 3(97.0/0.0)


