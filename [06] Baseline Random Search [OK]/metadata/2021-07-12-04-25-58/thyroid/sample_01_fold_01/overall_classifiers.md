# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 3 | 0.926069 |
| TSH >= 0.00605 and FTI >= 0.064255 and On_thyroxine < 0.5 and TT4 < 0.1505 and Thyroid_surgery < 0.5 and TT4 >= 0.058499999999999996 | 2 | 0.049337 |
| TSH >= 0.00605 and FTI < 0.064255 | 1 | 0.021068 |
| On_thyroxine <= 0.5 and Query_on_thyroxine = all and On_antithyroid_medication = all and Tumor = all and TSH > 0.00605 and TSH <= 0.0195 and FTI > 0.08104 and FTI <= 0.097495 | 2 | 0.012139 |
| TSH >= 0.00605 and FTI >= 0.064255 and On_thyroxine < 0.5 and TT4 < 0.1505 and Thyroid_surgery < 0.5 and TT4 < 0.058499999999999996 and T3 < 0.01755 | 2 | 0.000677 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| TSH <= 0.006 | 3 | 0.924221 |
| FTI <= 0.064 and TSH > 0.01679 | 1 | 0.212038 |
| FTI > 0.06451 and On_thyroxine <= 0.0 and TT4 <= 0.15 and TT4 > 0.058 and T3 <= 0.029 and Age > 0.42 | 2 | 0.584392 |
| FTI > 0.062 and On_thyroxine > 0.0 | 3 | 0.495000 |
| FTI > 0.062 and TT4 <= 0.15 and Thyroid_surgery <= 0.0 and Age <= 0.56 | 2 | 0.536616 |
| TSH > 0.0064 and FTI > 0.064 | 3 | 0.725637 |
| T4U <= 0.096 | 1 | 0.217687 |
| Age <= 0.58 | 3 | 0.555556 |
|  | 1 | 0.307692 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| FTI <= 0.064 and TSH >= 0.0077 and T3 <= 0.011 and TT4 <= 0.075 | 1 | 0.016928 |
| FTI <= 0.064 and TSH >= 0.02 and Age <= 0.65 and T4U <= 0.135 | 1 | 0.004717 |
| FTI <= 0.064 and TSH >= 0.0062 and FTI >= 0.051 and TT4 <= 0.059 | 1 | 0.000789 |
| FTI <= 0.064 and TSH >= 0.0064 and Age >= 0.53 and TT4 >= 0.071 | 1 | 0.000474 |
| TSH >= 0.0061 and On_thyroxine <= 0 and T3 <= 0.02 and FTI >= 0.06493 and Thyroid_surgery <= 0 and TT4 <= 0.148 and TT4 >= 0.044 | 2 | 0.040601 |
| TSH >= 0.0061 and T3 >= 0.0208 and TT4 <= 0.141 and On_thyroxine <= 0 and T3 <= 0.026 and Age <= 0.83 | 2 | 0.010387 |
| TSH >= 0.0072 and T3 >= 0.027 and T3 <= 0.041 and TSH <= 0.009 and On_thyroxine <= 0 | 2 | 0.001331 |
| T3 >= 0.027 and TSH <= 0.02 and TSH >= 0.016 | 2 | 0.000666 |
|  | 3 | 0.999500 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

on_thyroxine|query_on_thyroxine|on_antithyroid_medication|tumor|tsh|fti|class
---|---|---|---|---|---|---
(-inf-0.5]|all|all|all|(0.0195-0.0415]|(0.14225-inf)|3
(0.5-inf)|all|all|all|(0.0195-0.0415]|(0.14225-inf)|1
(0.5-inf)|all|all|all|(0.0415-inf)|(0.097495-0.14225]|3
(0.5-inf)|all|all|all|(0.00605-0.0195]|(0.14225-inf)|3
(-inf-0.5]|all|all|all|(0.00605-0.0195]|(0.14225-inf)|3
(-inf-0.5]|all|all|all|(0.0195-0.0415]|(0.097495-0.14225]|2
(0.5-inf)|all|all|all|(0.0195-0.0415]|(0.097495-0.14225]|3
(-inf-0.5]|all|all|all|(0.0415-inf)|(0.08104-0.097495]|2
(0.5-inf)|all|all|all|(-inf-0.00605]|(0.14225-inf)|3
(-inf-0.5]|all|all|all|(-inf-0.00605]|(0.14225-inf)|3
(-inf-0.5]|all|all|all|(0.00605-0.0195]|(0.097495-0.14225]|2
(0.5-inf)|all|all|all|(0.00605-0.0195]|(0.097495-0.14225]|3
(-inf-0.5]|all|all|all|(0.0195-0.0415]|(0.08104-0.097495]|2
(0.5-inf)|all|all|all|(0.0195-0.0415]|(0.08104-0.097495]|3
(-inf-0.5]|all|all|all|(0.0415-inf)|(0.064255-0.08104]|2
(0.5-inf)|all|all|all|(0.0415-inf)|(0.064255-0.08104]|3
(0.5-inf)|all|all|all|(-inf-0.00605]|(0.097495-0.14225]|3
(-inf-0.5]|all|all|all|(-inf-0.00605]|(0.097495-0.14225]|3
(-inf-0.5]|all|all|all|(0.00605-0.0195]|(0.08104-0.097495]|2
(0.5-inf)|all|all|all|(0.00605-0.0195]|(0.08104-0.097495]|3
(-inf-0.5]|all|all|all|(0.0195-0.0415]|(0.064255-0.08104]|2
(0.5-inf)|all|all|all|(0.0195-0.0415]|(0.064255-0.08104]|3
(0.5-inf)|all|all|all|(0.0415-inf)|(0.0345-0.064255]|1
(-inf-0.5]|all|all|all|(0.0415-inf)|(0.0345-0.064255]|1
(-inf-0.5]|all|all|all|(-inf-0.00605]|(0.08104-0.097495]|3
(0.5-inf)|all|all|all|(-inf-0.00605]|(0.08104-0.097495]|3
(-inf-0.5]|all|all|all|(0.00605-0.0195]|(0.064255-0.08104]|2
(0.5-inf)|all|all|all|(0.00605-0.0195]|(0.064255-0.08104]|3
(0.5-inf)|all|all|all|(0.0195-0.0415]|(0.0345-0.064255]|1
(-inf-0.5]|all|all|all|(0.0195-0.0415]|(0.0345-0.064255]|1
(-inf-0.5]|all|all|all|(0.0415-inf)|(0.013735-0.0345]|1
(0.5-inf)|all|all|all|(0.0415-inf)|(0.013735-0.0345]|1
(0.5-inf)|all|all|all|(-inf-0.00605]|(0.064255-0.08104]|3
(-inf-0.5]|all|all|all|(-inf-0.00605]|(0.064255-0.08104]|3
(0.5-inf)|all|all|all|(0.00605-0.0195]|(0.0345-0.064255]|3
(-inf-0.5]|all|all|all|(0.00605-0.0195]|(0.0345-0.064255]|1
(-inf-0.5]|all|all|all|(0.0195-0.0415]|(0.013735-0.0345]|3
(0.5-inf)|all|all|all|(0.0415-inf)|(-inf-0.013735]|1
(-inf-0.5]|all|all|all|(0.0415-inf)|(-inf-0.013735]|1
(0.5-inf)|all|all|all|(-inf-0.00605]|(0.0345-0.064255]|3
(-inf-0.5]|all|all|all|(-inf-0.00605]|(0.0345-0.064255]|3
(-inf-0.5]|all|all|all|(0.00605-0.0195]|(0.013735-0.0345]|1
(-inf-0.5]|all|all|all|(0.0195-0.0415]|(-inf-0.013735]|1
(-inf-0.5]|all|all|all|(-inf-0.00605]|(0.013735-0.0345]|3
(-inf-0.5]|all|all|all|(-inf-0.00605]|(-inf-0.013735]|1

## JRip

Decision list:

rules | predicted class
---|---
(FTI <= 0.064) and (TSH >= 0.0077) and (T3 <= 0.011) and (TT4 <= 0.075)|1 (109.0/0.0)
(FTI <= 0.064) and (TSH >= 0.02) and (Age <= 0.65) and (T4U <= 0.135)|1 (30.0/0.0)
(FTI <= 0.064) and (TSH >= 0.0062) and (FTI >= 0.051) and (TT4 <= 0.059)|1 (5.0/0.0)
(FTI <= 0.064) and (TSH >= 0.0064) and (Age >= 0.53) and (TT4 >= 0.071)|1 (3.0/0.0)
(TSH >= 0.0061) and (On_thyroxine <= 0) and (T3 <= 0.02) and (FTI >= 0.06493) and (Thyroid_surgery <= 0) and (TT4 <= 0.148) and (TT4 >= 0.044)|2 (254.0/0.0)
(TSH >= 0.0061) and (T3 >= 0.0208) and (TT4 <= 0.141) and (On_thyroxine <= 0) and (T3 <= 0.026) and (Age <= 0.83)|2 (63.0/0.0)
(TSH >= 0.0072) and (T3 >= 0.027) and (T3 <= 0.041) and (TSH <= 0.009) and (On_thyroxine <= 0)|2 (8.0/0.0)
(T3 >= 0.027) and (TSH <= 0.02) and (TSH >= 0.016)|2 (4.0/0.0)
|3 (6003.0/3.0)


## PART

Decision list:

rules | predicted class
---|---
TSH <= 0.006|3 (5842.0)
FTI <= 0.064 AND TSH > 0.01679|1 (143.0/6.0)
FTI > 0.06451 AND On_thyroxine <= 0.0 AND TT4 <= 0.15 AND TT4 > 0.058 AND T3 <= 0.029 AND Age > 0.42|2 (243.0/2.0)
FTI > 0.062 AND On_thyroxine > 0.0|3 (99.0)
FTI > 0.062 AND TT4 <= 0.15 AND Thyroid_surgery <= 0.0 AND Age <= 0.56|2 (88.0/3.0)
TSH > 0.0064 AND FTI > 0.064|3 (42.0/2.0)
T4U <= 0.096|1 (10.0/2.0)
Age <= 0.58|3 (7.0)
|1 (5.0/1.0)


## J48 Decision Tree

* TSH <= 0.006: 3 (5842.0)
* TSH > 0.006
	* FTI <= 0.064
		* Thyroid_surgery <= 0
			* T3 <= 0.025
				* TSH <= 0.01679
					* T4U <= 0.096: 1 (7.0)
					* T4U > 0.096
						* Age <= 0.58: 3 (3.0)
						* Age > 0.58: 1 (5.0/1.0)
				* TSH > 0.01679: 1 (136.0/2.0)
			* T3 > 0.025: 3 (6.0/1.0)
		* Thyroid_surgery > 0
			* T4U <= 0.13: 1 (3.0)
			* T4U > 0.13: 3 (3.0)
	* FTI > 0.064
		* On_thyroxine <= 0
			* TT4 <= 0.15
				* TT4 <= 0.058
					* T3 <= 0.0174: 2 (6.0/1.0)
					* T3 > 0.0174: 3 (6.0)
				* TT4 > 0.058
					* T3 <= 0.029
						* Thyroid_surgery <= 0: 2 (318.0/1.0)
						* Thyroid_surgery > 0: 3 (9.0)
					* T3 > 0.029
						* T4U <= 0.113: 3 (5.0)
						* T4U > 0.113: 2 (8.0)
			* TT4 > 0.15: 3 (23.0)
		* On_thyroxine > 0: 3 (99.0)


## SimpleCart Decision Tree

* TSH < 0.00605: 3(5842.0/0.0)
* TSH >= 0.00605
	* FTI < 0.064255: 1(149.0/14.0)
	* FTI >= 0.064255
		* On_thyroxine < 0.5
			* TT4 < 0.1505
				* Thyroid_surgery < 0.5
					* TT4 < 0.058499999999999996
						* T3 < 0.01755: 2(5.0/1.0)
						* T3 >= 0.01755: 3(6.0/0.0)
					* TT4 >= 0.058499999999999996: 2(325.0/6.0)
				* Thyroid_surgery >= 0.5: 3(9.0/0.0)
			* TT4 >= 0.1505: 3(23.0/0.0)
		* On_thyroxine >= 0.5: 3(99.0/0.0)


