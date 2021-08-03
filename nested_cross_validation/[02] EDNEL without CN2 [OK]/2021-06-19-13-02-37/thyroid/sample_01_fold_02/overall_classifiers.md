# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| TSH <= 0.00605 | 3 | 0.924209 |
| TSH >= 0.00605 and FTI >= 0.064255 and On_thyroxine < 0.5 and TT4 < 0.1505 and Thyroid_surgery < 0.5 and TT4 >= 0.058499999999999996 and T3 < 0.0295 | 2 | 0.049173 |
| TSH >= 0.00605 and FTI < 0.064255 and T3 < 0.0265 and Thyroid_surgery < 0.5 | 1 | 0.021688 |
| TSH > 0.00605 and FTI > 0.064255 and On_thyroxine > 0.5 | 3 | 0.175559 |
| TSH > 0.00605 and FTI > 0.064255 and On_thyroxine <= 0.5 and TT4 > 0.1505 | 3 | 0.040080 |
| TSH >= 0.00605 and FTI >= 0.064255 and On_thyroxine < 0.5 and TT4 < 0.1505 and Thyroid_surgery >= 0.5 | 3 | 0.018443 |
| TSH > 0.00605 and FTI > 0.064255 and On_thyroxine <= 0.5 and TT4 <= 0.1505 and TT4 <= 0.0615 and T3 > 0.019049999999999997 | 3 | 0.012371 |
| TSH >= 0.00605 and FTI < 0.064255 and T3 >= 0.0265 | 3 | 0.010331 |
| TSH >= 0.00605 and FTI >= 0.064255 and On_thyroxine < 0.5 and TT4 < 0.1505 and Thyroid_surgery < 0.5 and TT4 >= 0.058499999999999996 and T3 >= 0.0295 and T4U >= 0.113 | 2 | 0.000975 |
| TSH > 0.00605 and FTI > 0.064255 and On_thyroxine <= 0.5 and TT4 <= 0.1505 and TT4 > 0.0615 and T3 > 0.0195 and Thyroid_surgery <= 0.5 and T3 > 0.0305 and T4U <= 0.113 | 3 | 0.008282 |
| TSH > 0.00605 and FTI <= 0.064255 and Thyroid_surgery > 0.5 | 3 | 0.005544 |
| TSH >= 0.00605 and FTI >= 0.064255 and On_thyroxine < 0.5 and TT4 < 0.1505 and Thyroid_surgery < 0.5 and TT4 < 0.058499999999999996 and T3 < 0.01755 | 2 | 0.000677 |
| TSH > 0.00605 and FTI <= 0.064255 and Thyroid_surgery <= 0.5 and T3 > 0.0235 and T3 <= 0.0265 and TSH <= 0.0075 | 3 | 0.004158 |
| On_thyroxine <= 0.5 and On_antithyroid_medication = all and Sick = all and Thyroid_surgery <= 0.5 and Goitre <= 0.5 and TSH > 0.00605 and TSH <= 0.0195 and FTI > 0.14225 | 3 | 0.011249 |
| On_thyroxine <= 0.5 and On_antithyroid_medication = all and Sick = all and Thyroid_surgery > 0.5 and Goitre <= 0.5 and TSH > 0.0415 and FTI > 0.013735 and FTI <= 0.064255 | 1 | 0.000053 |
| On_thyroxine <= 0.5 and On_antithyroid_medication = all and Sick = all and Thyroid_surgery > 0.5 and Goitre <= 0.5 and TSH > 0.0195 and TSH <= 0.0415 and FTI > 0.013735 and FTI <= 0.064255 | 1 | 0.000079 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| TSH <= 0.006 | 3 | 0.924209 |
| FTI > 0.064 and On_thyroxine <= 0.0 and TT4 <= 0.15 and TT4 > 0.061 | 2 | 0.500947 |
| FTI > 0.064 and TT4 > 0.06 | 3 | 0.460481 |
| FTI <= 0.06548 | 1 | 0.810551 |
| T3 <= 0.018 | 2 | 0.154589 |
|  | 3 | 1.000000 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| FTI <= 0.064 and TSH >= 0.00879 and T3 <= 0.011 and T4U <= 0.111 | 1 | 0.012172 |
| FTI <= 0.064 and TSH >= 0.018 and Age <= 0.67 and Thyroid_surgery <= 0 | 1 | 0.008148 |
| FTI <= 0.064 and TSH >= 0.0062 and T3 <= 0.01 and Age >= 0.53 | 1 | 0.001262 |
| FTI <= 0.064 and TSH >= 0.0062 and FTI >= 0.051 | 1 | 0.000984 |
| TSH >= 0.0061 and On_thyroxine <= 0 and T3 <= 0.02 and FTI >= 0.069 and Thyroid_surgery <= 0 and TT4 <= 0.146 | 2 | 0.038911 |
| TSH >= 0.0061 and On_thyroxine <= 0 and T3 >= 0.0208 and TT4 <= 0.141 and T3 <= 0.028 and On_antithyroid_medication <= 0 | 2 | 0.010397 |
| TSH >= 0.0063 and On_thyroxine <= 0 and FTI <= 0.068 and TT4 >= 0.056 and Thyroid_surgery <= 0 | 2 | 0.001917 |
| TSH >= 0.0072 and T3 >= 0.027 and T4U >= 0.102 and TT4 <= 0.15 and On_thyroxine <= 0 and FTI <= 0.125 | 2 | 0.001019 |
|  | 3 | 0.999500 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

on_thyroxine|on_antithyroid_medication|sick|thyroid_surgery|goitre|tsh|fti|class
---|---|---|---|---|---|---|---
(-inf-0.5]|all|all|(-inf-0.5]|(-inf-0.5]|(0.0195-0.0415]|(0.14225-inf)|3
(0.5-inf)|all|all|(-inf-0.5]|(-inf-0.5]|(0.0195-0.0415]|(0.14225-inf)|1
(0.5-inf)|all|all|(-inf-0.5]|(-inf-0.5]|(0.0415-inf)|(0.097495-0.14225]|3
(0.5-inf)|all|all|(-inf-0.5]|(-inf-0.5]|(0.00605-0.0195]|(0.14225-inf)|3
(-inf-0.5]|all|all|(-inf-0.5]|(-inf-0.5]|(0.00605-0.0195]|(0.14225-inf)|3
(0.5-inf)|all|all|(-inf-0.5]|(0.5-inf)|(-inf-0.00605]|(0.14225-inf)|1
(-inf-0.5]|all|all|(-inf-0.5]|(0.5-inf)|(-inf-0.00605]|(0.14225-inf)|3
(0.5-inf)|all|all|(-inf-0.5]|(-inf-0.5]|(0.0195-0.0415]|(0.097495-0.14225]|3
(-inf-0.5]|all|all|(-inf-0.5]|(-inf-0.5]|(0.0195-0.0415]|(0.097495-0.14225]|2
(-inf-0.5]|all|all|(-inf-0.5]|(-inf-0.5]|(0.0415-inf)|(0.08002-0.097495]|2
(-inf-0.5]|all|all|(0.5-inf)|(-inf-0.5]|(-inf-0.00605]|(0.14225-inf)|3
(0.5-inf)|all|all|(0.5-inf)|(-inf-0.5]|(-inf-0.00605]|(0.14225-inf)|3
(-inf-0.5]|all|all|(0.5-inf)|(-inf-0.5]|(0.00605-0.0195]|(0.097495-0.14225]|3
(0.5-inf)|all|all|(0.5-inf)|(-inf-0.5]|(0.0195-0.0415]|(0.08002-0.097495]|1
(0.5-inf)|all|all|(-inf-0.5]|(-inf-0.5]|(-inf-0.00605]|(0.14225-inf)|3
(-inf-0.5]|all|all|(-inf-0.5]|(-inf-0.5]|(-inf-0.00605]|(0.14225-inf)|3
(-inf-0.5]|all|all|(-inf-0.5]|(-inf-0.5]|(0.00605-0.0195]|(0.097495-0.14225]|2
(0.5-inf)|all|all|(-inf-0.5]|(-inf-0.5]|(0.00605-0.0195]|(0.097495-0.14225]|3
(0.5-inf)|all|all|(-inf-0.5]|(-inf-0.5]|(0.0195-0.0415]|(0.08002-0.097495]|3
(-inf-0.5]|all|all|(-inf-0.5]|(-inf-0.5]|(0.0195-0.0415]|(0.08002-0.097495]|2
(-inf-0.5]|all|all|(-inf-0.5]|(0.5-inf)|(-inf-0.00605]|(0.097495-0.14225]|3
(0.5-inf)|all|all|(-inf-0.5]|(0.5-inf)|(-inf-0.00605]|(0.097495-0.14225]|3
(-inf-0.5]|all|all|(-inf-0.5]|(0.5-inf)|(0.00605-0.0195]|(0.08002-0.097495]|1
(0.5-inf)|all|all|(-inf-0.5]|(-inf-0.5]|(0.0415-inf)|(0.064255-0.08002]|3
(-inf-0.5]|all|all|(-inf-0.5]|(-inf-0.5]|(0.0415-inf)|(0.064255-0.08002]|2
(-inf-0.5]|all|all|(0.5-inf)|(-inf-0.5]|(-inf-0.00605]|(0.097495-0.14225]|3
(0.5-inf)|all|all|(0.5-inf)|(-inf-0.5]|(-inf-0.00605]|(0.097495-0.14225]|3
(-inf-0.5]|all|all|(0.5-inf)|(-inf-0.5]|(0.00605-0.0195]|(0.08002-0.097495]|3
(-inf-0.5]|all|all|(0.5-inf)|(-inf-0.5]|(0.0415-inf)|(0.013735-0.064255]|1
(0.5-inf)|all|all|(-inf-0.5]|(-inf-0.5]|(-inf-0.00605]|(0.097495-0.14225]|3
(-inf-0.5]|all|all|(-inf-0.5]|(-inf-0.5]|(-inf-0.00605]|(0.097495-0.14225]|3
(-inf-0.5]|all|all|(-inf-0.5]|(-inf-0.5]|(0.00605-0.0195]|(0.08002-0.097495]|2
(0.5-inf)|all|all|(-inf-0.5]|(-inf-0.5]|(0.00605-0.0195]|(0.08002-0.097495]|3
(0.5-inf)|all|all|(-inf-0.5]|(0.5-inf)|(-inf-0.00605]|(0.08002-0.097495]|1
(0.5-inf)|all|all|(-inf-0.5]|(-inf-0.5]|(0.0195-0.0415]|(0.064255-0.08002]|3
(-inf-0.5]|all|all|(-inf-0.5]|(-inf-0.5]|(0.0195-0.0415]|(0.064255-0.08002]|2
(-inf-0.5]|all|all|(-inf-0.5]|(0.5-inf)|(-inf-0.00605]|(0.08002-0.097495]|3
(0.5-inf)|all|all|(-inf-0.5]|(-inf-0.5]|(0.0415-inf)|(0.013735-0.064255]|1
(-inf-0.5]|all|all|(-inf-0.5]|(-inf-0.5]|(0.0415-inf)|(0.013735-0.064255]|1
(-inf-0.5]|all|all|(0.5-inf)|(-inf-0.5]|(-inf-0.00605]|(0.08002-0.097495]|3
(-inf-0.5]|all|all|(0.5-inf)|(-inf-0.5]|(0.00605-0.0195]|(0.064255-0.08002]|3
(-inf-0.5]|all|all|(0.5-inf)|(-inf-0.5]|(0.0195-0.0415]|(0.013735-0.064255]|1
(0.5-inf)|all|all|(-inf-0.5]|(-inf-0.5]|(-inf-0.00605]|(0.08002-0.097495]|3
(-inf-0.5]|all|all|(-inf-0.5]|(-inf-0.5]|(-inf-0.00605]|(0.08002-0.097495]|3
(0.5-inf)|all|all|(-inf-0.5]|(-inf-0.5]|(0.00605-0.0195]|(0.064255-0.08002]|3
(-inf-0.5]|all|all|(-inf-0.5]|(-inf-0.5]|(0.00605-0.0195]|(0.064255-0.08002]|2
(0.5-inf)|all|all|(-inf-0.5]|(-inf-0.5]|(0.0195-0.0415]|(0.013735-0.064255]|1
(0.5-inf)|all|all|(-inf-0.5]|(0.5-inf)|(-inf-0.00605]|(0.064255-0.08002]|3
(-inf-0.5]|all|all|(-inf-0.5]|(0.5-inf)|(-inf-0.00605]|(0.064255-0.08002]|3
(-inf-0.5]|all|all|(-inf-0.5]|(-inf-0.5]|(0.0195-0.0415]|(0.013735-0.064255]|1
(-inf-0.5]|all|all|(0.5-inf)|(-inf-0.5]|(-inf-0.00605]|(0.064255-0.08002]|3
(0.5-inf)|all|all|(-inf-0.5]|(-inf-0.5]|(0.0415-inf)|(-inf-0.013735]|1
(-inf-0.5]|all|all|(-inf-0.5]|(-inf-0.5]|(0.0415-inf)|(-inf-0.013735]|1
(-inf-0.5]|all|all|(0.5-inf)|(-inf-0.5]|(0.00605-0.0195]|(0.013735-0.064255]|1
(0.5-inf)|all|all|(-inf-0.5]|(-inf-0.5]|(-inf-0.00605]|(0.064255-0.08002]|3
(-inf-0.5]|all|all|(-inf-0.5]|(-inf-0.5]|(-inf-0.00605]|(0.064255-0.08002]|3
(0.5-inf)|all|all|(-inf-0.5]|(-inf-0.5]|(0.00605-0.0195]|(0.013735-0.064255]|1
(-inf-0.5]|all|all|(-inf-0.5]|(-inf-0.5]|(0.00605-0.0195]|(0.013735-0.064255]|1
(-inf-0.5]|all|all|(-inf-0.5]|(0.5-inf)|(-inf-0.00605]|(0.013735-0.064255]|3
(-inf-0.5]|all|all|(-inf-0.5]|(-inf-0.5]|(0.0195-0.0415]|(-inf-0.013735]|1
(-inf-0.5]|all|all|(0.5-inf)|(-inf-0.5]|(-inf-0.00605]|(0.013735-0.064255]|3
(0.5-inf)|all|all|(-inf-0.5]|(-inf-0.5]|(-inf-0.00605]|(0.013735-0.064255]|3
(-inf-0.5]|all|all|(-inf-0.5]|(-inf-0.5]|(-inf-0.00605]|(0.013735-0.064255]|3

## JRip

Decision list:

rules | predicted class
---|---
(FTI <= 0.064) and (TSH >= 0.00879) and (T3 <= 0.011) and (T4U <= 0.111)|1 (78.0/0.0)
(FTI <= 0.064) and (TSH >= 0.018) and (Age <= 0.67) and (Thyroid_surgery <= 0)|1 (52.0/0.0)
(FTI <= 0.064) and (TSH >= 0.0062) and (T3 <= 0.01) and (Age >= 0.53)|1 (8.0/0.0)
(FTI <= 0.064) and (TSH >= 0.0062) and (FTI >= 0.051)|1 (13.0/4.0)
(TSH >= 0.0061) and (On_thyroxine <= 0) and (T3 <= 0.02) and (FTI >= 0.069) and (Thyroid_surgery <= 0) and (TT4 <= 0.146)|2 (243.0/0.0)
(TSH >= 0.0061) and (On_thyroxine <= 0) and (T3 >= 0.0208) and (TT4 <= 0.141) and (T3 <= 0.028) and (On_antithyroid_medication <= 0)|2 (65.0/0.0)
(TSH >= 0.0063) and (On_thyroxine <= 0) and (FTI <= 0.068) and (TT4 >= 0.056) and (Thyroid_surgery <= 0)|2 (14.0/0.0)
(TSH >= 0.0072) and (T3 >= 0.027) and (T4U >= 0.102) and (TT4 <= 0.15) and (On_thyroxine <= 0) and (FTI <= 0.125)|2 (7.0/0.0)
|3 (5999.0/3.0)


## PART

Decision list:

rules | predicted class
---|---
TSH <= 0.006|3 (5188.0)
FTI > 0.064 AND On_thyroxine <= 0.0 AND TT4 <= 0.15 AND TT4 > 0.061|2 (299.0/12.0)
FTI > 0.064 AND TT4 > 0.06|3 (109.0)
FTI <= 0.06548|1 (149.0/16.0)
T3 <= 0.018|2 (8.0/2.0)
|3 (7.0)


## J48 Decision Tree

* TSH <= 0.00605: 3 (5841.0)
* TSH > 0.00605
	* FTI <= 0.064255
		* Thyroid_surgery <= 0.5
			* T3 <= 0.0235: 1 (146.0/5.0)
			* T3 > 0.0235
				* T3 <= 0.0265
					* TSH <= 0.0075: 3 (2.0)
					* TSH > 0.0075: 1 (6.0)
				* T3 > 0.0265: 3 (5.0)
		* Thyroid_surgery > 0.5: 3 (6.0/2.0)
	* FTI > 0.064255
		* On_thyroxine <= 0.5
			* TT4 <= 0.1505
				* TT4 <= 0.0615
					* T3 <= 0.019049999999999997: 2 (9.0/1.0)
					* T3 > 0.019049999999999997: 3 (6.0)
				* TT4 > 0.0615
					* T3 <= 0.0195: 2 (238.0/3.0)
					* T3 > 0.0195
						* Thyroid_surgery <= 0.5
							* T3 <= 0.0305: 2 (83.0/1.0)
							* T3 > 0.0305
								* T4U <= 0.113: 3 (4.0)
								* T4U > 0.113: 2 (5.0)
						* Thyroid_surgery > 0.5: 3 (6.0)
			* TT4 > 0.1505: 3 (20.0)
		* On_thyroxine > 0.5: 3 (102.0)


## SimpleCart Decision Tree

* TSH < 0.00605: 3(5841.0/0.0)
* TSH >= 0.00605
	* FTI < 0.064255
		* T3 < 0.0265
			* Thyroid_surgery < 0.5: 1(147.0/7.0)
			* Thyroid_surgery >= 0.5: 3(4.0/2.0)
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


