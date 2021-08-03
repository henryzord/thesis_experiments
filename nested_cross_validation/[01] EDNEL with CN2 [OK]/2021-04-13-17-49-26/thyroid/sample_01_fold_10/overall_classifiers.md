# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 3 | 0.926069 |
| TSH > 0.00605 and FTI > 0.064255 and On_thyroxine <= 0.5 and TT4 <= 0.1505 and TT4 > 0.0615 and T3 <= 0.028999999999999998 and Age > 0.425 | 2 | 0.036512 |
| TSH > 0.00605 and FTI <= 0.064255 and Thyroid_surgery <= 0.5 and T3 <= 0.0235 and I131_treatment <= 0.5 | 1 | 0.020280 |
| TSH > 0.00605 and FTI > 0.064255 and On_thyroxine <= 0.5 and TT4 <= 0.1505 and TT4 > 0.0615 and T3 <= 0.028999999999999998 and Age <= 0.425 and Thyroid_surgery <= 0.5 | 2 | 0.012526 |
| TSH > 0.00605 and FTI > 0.064255 and On_thyroxine <= 0.5 and TT4 <= 0.1505 and TT4 <= 0.0615 and T3 <= 0.019549999999999998 | 2 | 0.001476 |
| TSH > 0.00605 and FTI <= 0.064255 and Thyroid_surgery <= 0.5 and T3 > 0.0235 and T3 <= 0.0265 and TSH > 0.0075 | 1 | 0.001105 |
| TSH > 0.00605 and FTI > 0.064255 and On_thyroxine <= 0.5 and TT4 <= 0.1505 and TT4 > 0.0615 and T3 > 0.028999999999999998 and T4U > 0.11649999999999999 | 2 | 0.001137 |
| On_thyroxine <= 0.5 and Query_on_thyroxine = all and On_antithyroid_medication = all and Sick = all and Pregnant <= 0.5 and Thyroid_surgery > 0.5 and I131_treatment = all and Lithium = all and Goitre <= 0.5 and TSH > 0.0195 and TSH <= 0.0415 and FTI > 0.0345 and FTI <= 0.064255 | 1 | 0.000158 |
| TSH > 0.00605 and FTI <= 0.064255 and Thyroid_surgery > 0.5 and T4U <= 0.131 | 1 | 0.000505 |
| On_thyroxine <= 0.5 and Query_on_thyroxine = all and On_antithyroid_medication = all and Sick = all and Pregnant <= 0.5 and Thyroid_surgery <= 0.5 and I131_treatment = all and Lithium = all and Goitre <= 0.5 and TSH > 0.0415 and FTI <= 0.013735 | 1 | 0.005186 |
| On_thyroxine <= 0.5 and Query_on_thyroxine = all and On_antithyroid_medication = all and Sick = all and Pregnant <= 0.5 and Thyroid_surgery <= 0.5 and I131_treatment = all and Lithium = all and Goitre <= 0.5 and TSH > 0.0195 and TSH <= 0.0415 and FTI <= 0.013735 | 1 | 0.001105 |
| TSH > 0.00605 and FTI <= 0.064255 and Thyroid_surgery <= 0.5 and T3 <= 0.0235 and I131_treatment > 0.5 and Age <= 0.655 | 1 | 0.000789 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| TSH <= 0.00605 | 3 | 0.924221 |
| FTI <= 0.064255 and Thyroid_surgery <= 0.5 and T3 <= 0.0235 | 1 | 0.215615 |
| On_thyroxine <= 0.5 and FTI > 0.062965 and TT4 <= 0.1505 and TT4 > 0.0615 and T3 <= 0.029 and Age > 0.425 | 2 | 0.579644 |
| FTI > 0.062755 and On_thyroxine > 0.5 | 3 | 0.480392 |
| FTI > 0.062965 and TT4 <= 0.1505 and Thyroid_surgery <= 0.5 and Age <= 0.56 | 2 | 0.545975 |
| FTI > 0.063 and T3 > 0.0115 | 3 | 0.713338 |
| FTI <= 0.063 and T3 <= 0.0265 | 1 | 0.252083 |
| T3 <= 0.019 | 2 | 0.147929 |
|  | 3 | 0.941176 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| FTI <= 0.064 and TSH >= 0.017 and T3 <= 0.011 | 1 | 0.015401 |
| FTI <= 0.064 and TSH >= 0.0062 and T3 <= 0.022 and I131_treatment <= 0 | 1 | 0.005586 |
| FTI <= 0.064 and TSH >= 0.0077 and T3 <= 0.026 and T3 >= 0.016 | 1 | 0.001278 |
| TSH >= 0.0061 and On_thyroxine <= 0 and T3 <= 0.019 | 2 | 0.036732 |
| TSH >= 0.0061 and On_thyroxine <= 0 and TT4 <= 0.141 and TT4 >= 0.062 | 2 | 0.011878 |
|  | 3 | 0.999833 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

on_thyroxine|query_on_thyroxine|on_antithyroid_medication|sick|pregnant|thyroid_surgery|i131_treatment|lithium|goitre|tsh|fti|class
---|---|---|---|---|---|---|---|---|---|---|---
(-inf-0.5]|all|all|all|(-inf-0.5]|(-inf-0.5]|all|all|(-inf-0.5]|(0.0195-0.0415]|(0.1425-inf)|3
(0.5-inf)|all|all|all|(-inf-0.5]|(-inf-0.5]|all|all|(-inf-0.5]|(0.0415-inf)|(0.097495-0.1425]|1
(0.5-inf)|all|all|all|(-inf-0.5]|(-inf-0.5]|all|all|(-inf-0.5]|(0.00605-0.0195]|(0.1425-inf)|3
(-inf-0.5]|all|all|all|(-inf-0.5]|(-inf-0.5]|all|all|(-inf-0.5]|(0.00605-0.0195]|(0.1425-inf)|3
(0.5-inf)|all|all|all|(-inf-0.5]|(-inf-0.5]|all|all|(0.5-inf)|(-inf-0.00605]|(0.1425-inf)|1
(-inf-0.5]|all|all|all|(-inf-0.5]|(-inf-0.5]|all|all|(0.5-inf)|(-inf-0.00605]|(0.1425-inf)|3
(0.5-inf)|all|all|all|(-inf-0.5]|(-inf-0.5]|all|all|(-inf-0.5]|(0.0195-0.0415]|(0.097495-0.1425]|3
(-inf-0.5]|all|all|all|(-inf-0.5]|(-inf-0.5]|all|all|(-inf-0.5]|(0.0195-0.0415]|(0.097495-0.1425]|2
(-inf-0.5]|all|all|all|(-inf-0.5]|(-inf-0.5]|all|all|(-inf-0.5]|(0.0415-inf)|(0.08104-0.097495]|2
(0.5-inf)|all|all|all|(-inf-0.5]|(0.5-inf)|all|all|(-inf-0.5]|(-inf-0.00605]|(0.1425-inf)|3
(-inf-0.5]|all|all|all|(-inf-0.5]|(0.5-inf)|all|all|(-inf-0.5]|(-inf-0.00605]|(0.1425-inf)|3
(0.5-inf)|all|all|all|(0.5-inf)|(-inf-0.5]|all|all|(-inf-0.5]|(-inf-0.00605]|(0.1425-inf)|1
(-inf-0.5]|all|all|all|(0.5-inf)|(-inf-0.5]|all|all|(-inf-0.5]|(-inf-0.00605]|(0.1425-inf)|3
(-inf-0.5]|all|all|all|(-inf-0.5]|(0.5-inf)|all|all|(-inf-0.5]|(0.00605-0.0195]|(0.097495-0.1425]|3
(0.5-inf)|all|all|all|(-inf-0.5]|(0.5-inf)|all|all|(-inf-0.5]|(0.0195-0.0415]|(0.08104-0.097495]|1
(-inf-0.5]|all|all|all|(-inf-0.5]|(0.5-inf)|all|all|(-inf-0.5]|(0.0195-0.0415]|(0.08104-0.097495]|1
(-inf-0.5]|all|all|all|(0.5-inf)|(-inf-0.5]|all|all|(0.5-inf)|(-inf-0.00605]|(0.097495-0.1425]|1
(0.5-inf)|all|all|all|(-inf-0.5]|(-inf-0.5]|all|all|(-inf-0.5]|(-inf-0.00605]|(0.1425-inf)|3
(-inf-0.5]|all|all|all|(-inf-0.5]|(-inf-0.5]|all|all|(-inf-0.5]|(-inf-0.00605]|(0.1425-inf)|3
(0.5-inf)|all|all|all|(-inf-0.5]|(-inf-0.5]|all|all|(-inf-0.5]|(0.00605-0.0195]|(0.097495-0.1425]|3
(-inf-0.5]|all|all|all|(-inf-0.5]|(-inf-0.5]|all|all|(-inf-0.5]|(0.00605-0.0195]|(0.097495-0.1425]|2
(0.5-inf)|all|all|all|(-inf-0.5]|(-inf-0.5]|all|all|(0.5-inf)|(-inf-0.00605]|(0.097495-0.1425]|3
(-inf-0.5]|all|all|all|(-inf-0.5]|(-inf-0.5]|all|all|(-inf-0.5]|(0.0195-0.0415]|(0.08104-0.097495]|2
(0.5-inf)|all|all|all|(-inf-0.5]|(-inf-0.5]|all|all|(-inf-0.5]|(0.0195-0.0415]|(0.08104-0.097495]|3
(-inf-0.5]|all|all|all|(-inf-0.5]|(-inf-0.5]|all|all|(0.5-inf)|(-inf-0.00605]|(0.097495-0.1425]|3
(-inf-0.5]|all|all|all|(-inf-0.5]|(-inf-0.5]|all|all|(0.5-inf)|(0.00605-0.0195]|(0.08104-0.097495]|1
(0.5-inf)|all|all|all|(-inf-0.5]|(-inf-0.5]|all|all|(-inf-0.5]|(0.0415-inf)|(0.064255-0.08104]|3
(-inf-0.5]|all|all|all|(-inf-0.5]|(-inf-0.5]|all|all|(-inf-0.5]|(0.0415-inf)|(0.064255-0.08104]|2
(0.5-inf)|all|all|all|(-inf-0.5]|(0.5-inf)|all|all|(-inf-0.5]|(-inf-0.00605]|(0.097495-0.1425]|3
(-inf-0.5]|all|all|all|(-inf-0.5]|(0.5-inf)|all|all|(-inf-0.5]|(-inf-0.00605]|(0.097495-0.1425]|3
(-inf-0.5]|all|all|all|(-inf-0.5]|(0.5-inf)|all|all|(-inf-0.5]|(0.00605-0.0195]|(0.08104-0.097495]|3
(0.5-inf)|all|all|all|(0.5-inf)|(-inf-0.5]|all|all|(-inf-0.5]|(-inf-0.00605]|(0.097495-0.1425]|3
(-inf-0.5]|all|all|all|(0.5-inf)|(-inf-0.5]|all|all|(-inf-0.5]|(-inf-0.00605]|(0.097495-0.1425]|3
(0.5-inf)|all|all|all|(0.5-inf)|(-inf-0.5]|all|all|(-inf-0.5]|(0.00605-0.0195]|(0.08104-0.097495]|1
(-inf-0.5]|all|all|all|(0.5-inf)|(-inf-0.5]|all|all|(0.5-inf)|(-inf-0.00605]|(0.08104-0.097495]|1
(-inf-0.5]|all|all|all|(-inf-0.5]|(0.5-inf)|all|all|(-inf-0.5]|(0.0415-inf)|(0.0345-0.064255]|1
(0.5-inf)|all|all|all|(-inf-0.5]|(-inf-0.5]|all|all|(-inf-0.5]|(-inf-0.00605]|(0.097495-0.1425]|3
(-inf-0.5]|all|all|all|(-inf-0.5]|(-inf-0.5]|all|all|(-inf-0.5]|(-inf-0.00605]|(0.097495-0.1425]|3
(0.5-inf)|all|all|all|(-inf-0.5]|(-inf-0.5]|all|all|(-inf-0.5]|(0.00605-0.0195]|(0.08104-0.097495]|3
(-inf-0.5]|all|all|all|(-inf-0.5]|(-inf-0.5]|all|all|(-inf-0.5]|(0.00605-0.0195]|(0.08104-0.097495]|2
(0.5-inf)|all|all|all|(-inf-0.5]|(-inf-0.5]|all|all|(0.5-inf)|(-inf-0.00605]|(0.08104-0.097495]|1
(-inf-0.5]|all|all|all|(-inf-0.5]|(-inf-0.5]|all|all|(0.5-inf)|(-inf-0.00605]|(0.08104-0.097495]|3
(0.5-inf)|all|all|all|(-inf-0.5]|(-inf-0.5]|all|all|(-inf-0.5]|(0.0195-0.0415]|(0.064255-0.08104]|3
(-inf-0.5]|all|all|all|(-inf-0.5]|(-inf-0.5]|all|all|(-inf-0.5]|(0.0195-0.0415]|(0.064255-0.08104]|2
(0.5-inf)|all|all|all|(-inf-0.5]|(-inf-0.5]|all|all|(-inf-0.5]|(0.0415-inf)|(0.0345-0.064255]|1
(-inf-0.5]|all|all|all|(-inf-0.5]|(-inf-0.5]|all|all|(-inf-0.5]|(0.0415-inf)|(0.0345-0.064255]|1
(-inf-0.5]|all|all|all|(-inf-0.5]|(0.5-inf)|all|all|(-inf-0.5]|(-inf-0.00605]|(0.08104-0.097495]|3
(0.5-inf)|all|all|all|(0.5-inf)|(-inf-0.5]|all|all|(-inf-0.5]|(-inf-0.00605]|(0.08104-0.097495]|3
(-inf-0.5]|all|all|all|(0.5-inf)|(-inf-0.5]|all|all|(-inf-0.5]|(-inf-0.00605]|(0.08104-0.097495]|3
(-inf-0.5]|all|all|all|(-inf-0.5]|(0.5-inf)|all|all|(-inf-0.5]|(0.00605-0.0195]|(0.064255-0.08104]|3
(-inf-0.5]|all|all|all|(-inf-0.5]|(0.5-inf)|all|all|(-inf-0.5]|(0.0195-0.0415]|(0.0345-0.064255]|1
(-inf-0.5]|all|all|all|(-inf-0.5]|(0.5-inf)|all|all|(-inf-0.5]|(0.0415-inf)|(0.013735-0.0345]|1
(-inf-0.5]|all|all|all|(0.5-inf)|(-inf-0.5]|all|all|(0.5-inf)|(-inf-0.00605]|(0.064255-0.08104]|1
(0.5-inf)|all|all|all|(-inf-0.5]|(-inf-0.5]|all|all|(-inf-0.5]|(-inf-0.00605]|(0.08104-0.097495]|3
(-inf-0.5]|all|all|all|(-inf-0.5]|(-inf-0.5]|all|all|(-inf-0.5]|(-inf-0.00605]|(0.08104-0.097495]|3
(0.5-inf)|all|all|all|(-inf-0.5]|(-inf-0.5]|all|all|(-inf-0.5]|(0.00605-0.0195]|(0.064255-0.08104]|3
(-inf-0.5]|all|all|all|(-inf-0.5]|(-inf-0.5]|all|all|(-inf-0.5]|(0.00605-0.0195]|(0.064255-0.08104]|2
(0.5-inf)|all|all|all|(-inf-0.5]|(-inf-0.5]|all|all|(0.5-inf)|(-inf-0.00605]|(0.064255-0.08104]|1
(0.5-inf)|all|all|all|(-inf-0.5]|(-inf-0.5]|all|all|(-inf-0.5]|(0.0195-0.0415]|(0.0345-0.064255]|1
(-inf-0.5]|all|all|all|(-inf-0.5]|(-inf-0.5]|all|all|(-inf-0.5]|(0.0195-0.0415]|(0.0345-0.064255]|1
(-inf-0.5]|all|all|all|(-inf-0.5]|(-inf-0.5]|all|all|(0.5-inf)|(-inf-0.00605]|(0.064255-0.08104]|3
(0.5-inf)|all|all|all|(-inf-0.5]|(-inf-0.5]|all|all|(-inf-0.5]|(0.0415-inf)|(0.013735-0.0345]|1
(-inf-0.5]|all|all|all|(-inf-0.5]|(-inf-0.5]|all|all|(-inf-0.5]|(0.0415-inf)|(0.013735-0.0345]|1
(-inf-0.5]|all|all|all|(-inf-0.5]|(0.5-inf)|all|all|(-inf-0.5]|(-inf-0.00605]|(0.064255-0.08104]|3
(0.5-inf)|all|all|all|(0.5-inf)|(-inf-0.5]|all|all|(-inf-0.5]|(-inf-0.00605]|(0.064255-0.08104]|1
(-inf-0.5]|all|all|all|(-inf-0.5]|(0.5-inf)|all|all|(-inf-0.5]|(0.00605-0.0195]|(0.0345-0.064255]|1
(-inf-0.5]|all|all|all|(0.5-inf)|(-inf-0.5]|all|all|(-inf-0.5]|(-inf-0.00605]|(0.064255-0.08104]|3
(-inf-0.5]|all|all|all|(-inf-0.5]|(0.5-inf)|all|all|(-inf-0.5]|(0.0195-0.0415]|(0.013735-0.0345]|1
(-inf-0.5]|all|all|all|(-inf-0.5]|(0.5-inf)|all|all|(-inf-0.5]|(0.0415-inf)|(-inf-0.013735]|1
(0.5-inf)|all|all|all|(-inf-0.5]|(-inf-0.5]|all|all|(-inf-0.5]|(-inf-0.00605]|(0.064255-0.08104]|3
(-inf-0.5]|all|all|all|(-inf-0.5]|(-inf-0.5]|all|all|(-inf-0.5]|(-inf-0.00605]|(0.064255-0.08104]|3
(0.5-inf)|all|all|all|(-inf-0.5]|(-inf-0.5]|all|all|(-inf-0.5]|(0.00605-0.0195]|(0.0345-0.064255]|3
(-inf-0.5]|all|all|all|(-inf-0.5]|(-inf-0.5]|all|all|(-inf-0.5]|(0.00605-0.0195]|(0.0345-0.064255]|1
(-inf-0.5]|all|all|all|(-inf-0.5]|(-inf-0.5]|all|all|(-inf-0.5]|(0.0195-0.0415]|(0.013735-0.0345]|1
(-inf-0.5]|all|all|all|(-inf-0.5]|(-inf-0.5]|all|all|(0.5-inf)|(-inf-0.00605]|(0.0345-0.064255]|3
(0.5-inf)|all|all|all|(-inf-0.5]|(-inf-0.5]|all|all|(-inf-0.5]|(0.0415-inf)|(-inf-0.013735]|1
(-inf-0.5]|all|all|all|(-inf-0.5]|(-inf-0.5]|all|all|(-inf-0.5]|(0.0415-inf)|(-inf-0.013735]|1
(-inf-0.5]|all|all|all|(-inf-0.5]|(0.5-inf)|all|all|(-inf-0.5]|(-inf-0.00605]|(0.0345-0.064255]|1
(-inf-0.5]|all|all|all|(0.5-inf)|(-inf-0.5]|all|all|(-inf-0.5]|(-inf-0.00605]|(0.0345-0.064255]|1
(0.5-inf)|all|all|all|(-inf-0.5]|(-inf-0.5]|all|all|(-inf-0.5]|(-inf-0.00605]|(0.0345-0.064255]|3
(-inf-0.5]|all|all|all|(-inf-0.5]|(-inf-0.5]|all|all|(-inf-0.5]|(-inf-0.00605]|(0.0345-0.064255]|3
(-inf-0.5]|all|all|all|(-inf-0.5]|(-inf-0.5]|all|all|(-inf-0.5]|(0.00605-0.0195]|(0.013735-0.0345]|1
(-inf-0.5]|all|all|all|(-inf-0.5]|(-inf-0.5]|all|all|(-inf-0.5]|(0.0195-0.0415]|(-inf-0.013735]|1
(-inf-0.5]|all|all|all|(-inf-0.5]|(-inf-0.5]|all|all|(-inf-0.5]|(-inf-0.00605]|(0.013735-0.0345]|3
(-inf-0.5]|all|all|all|(-inf-0.5]|(-inf-0.5]|all|all|(-inf-0.5]|(-inf-0.00605]|(-inf-0.013735]|1

## JRip

Decision list:

rules | predicted class
---|---
(FTI <= 0.064) and (TSH >= 0.017) and (T3 <= 0.011)|1 (101.0/1.0)
(FTI <= 0.064) and (TSH >= 0.0062) and (T3 <= 0.022) and (I131_treatment <= 0)|1 (44.0/4.0)
(FTI <= 0.064) and (TSH >= 0.0077) and (T3 <= 0.026) and (T3 >= 0.016)|1 (9.0/0.0)
(TSH >= 0.0061) and (On_thyroxine <= 0) and (T3 <= 0.019)|2 (252.0/10.0)
(TSH >= 0.0061) and (On_thyroxine <= 0) and (TT4 <= 0.141) and (TT4 >= 0.062)|2 (98.0/11.0)
|3 (5975.0/1.0)


## PART

Decision list:

rules | predicted class
---|---
TSH <= 0.00605|3 (5842.0)
FTI <= 0.064255 AND Thyroid_surgery <= 0.5 AND T3 <= 0.0235|1 (142.0/4.0)
On_thyroxine <= 0.5 AND FTI > 0.062965 AND TT4 <= 0.1505 AND TT4 > 0.0615 AND T3 <= 0.029 AND Age > 0.425|2 (237.0/2.0)
FTI > 0.062755 AND On_thyroxine > 0.5|3 (98.0)
FTI > 0.062965 AND TT4 <= 0.1505 AND Thyroid_surgery <= 0.5 AND Age <= 0.56|2 (93.0/4.0)
FTI > 0.063 AND T3 > 0.0115|3 (40.0/2.0)
FTI <= 0.063 AND T3 <= 0.0265|1 (16.0/5.0)
T3 <= 0.019|2 (6.0/2.0)
|3 (5.0)


## J48 Decision Tree

* TSH <= 0.00605: 3 (5842.0)
* TSH > 0.00605
	* FTI <= 0.064255
		* Thyroid_surgery <= 0.5
			* T3 <= 0.0235
				* I131_treatment <= 0.5: 1 (135.0/2.0)
				* I131_treatment > 0.5
					* Age <= 0.655: 1 (5.0)
					* Age > 0.655: 3 (2.0)
			* T3 > 0.0235
				* T3 <= 0.0265
					* TSH <= 0.0075: 3 (2.0)
					* TSH > 0.0075: 1 (7.0)
				* T3 > 0.0265: 3 (5.0)
		* Thyroid_surgery > 0.5
			* T4U <= 0.131: 1 (5.0/1.0)
			* T4U > 0.131: 3 (2.0)
	* FTI > 0.064255
		* On_thyroxine <= 0.5
			* TT4 <= 0.1505
				* TT4 <= 0.0615
					* T3 <= 0.019549999999999998: 2 (11.0/1.0)
					* T3 > 0.019549999999999998: 3 (6.0)
				* TT4 > 0.0615
					* T3 <= 0.028999999999999998
						* Age <= 0.425
							* Thyroid_surgery <= 0.5: 2 (78.0)
							* Thyroid_surgery > 0.5: 3 (9.0)
						* Age > 0.425: 2 (237.0/2.0)
					* T3 > 0.028999999999999998
						* T4U <= 0.11649999999999999: 3 (5.0)
						* T4U > 0.11649999999999999: 2 (7.0)
			* TT4 > 0.1505: 3 (23.0)
		* On_thyroxine > 0.5: 3 (98.0)


