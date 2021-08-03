# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 3 | 0.926069 |
| TSH >= 0.00605 and FTI >= 0.064465 and On_thyroxine < 0.5 and TT4 < 0.1505 | 2 | 0.048042 |
| Age = all and On_thyroxine > 0.5 and Sick = all and Thyroid_surgery <= 0.5 and Tumor = all and TSH > 0.0415 and FTI <= 0.0165 | 1 | 0.000316 |
| Age = all and On_thyroxine <= 0.5 and Sick = all and Thyroid_surgery > 0.5 and Tumor = all and TSH > 0.0415 and FTI > 0.0165 and FTI <= 0.0345 | 1 | 0.000053 |
| TSH > 0.00605 and FTI <= 0.064465 and TSH <= 0.016895 and T3 <= 0.013000000000000001 | 1 | 0.001590 |
| Age = all and On_thyroxine <= 0.5 and Sick = all and Thyroid_surgery <= 0.5 and Tumor = all and TSH > 0.00605 and TSH <= 0.0195 and FTI > 0.0345 and FTI <= 0.064465 | 1 | 0.001546 |
| Age = all and On_thyroxine <= 0.5 and Sick = all and Thyroid_surgery > 0.5 and Tumor = all and TSH > 0.0415 and FTI > 0.0345 and FTI <= 0.064465 | 1 | 0.000158 |
| Age = all and On_thyroxine <= 0.5 and Sick = all and Thyroid_surgery > 0.5 and Tumor = all and TSH > 0.0195 and TSH <= 0.0415 and FTI > 0.0345 and FTI <= 0.064465 | 1 | 0.000158 |
| Age = all and On_thyroxine <= 0.5 and Sick = all and Thyroid_surgery <= 0.5 and Tumor = all and TSH > 0.0415 and FTI <= 0.0165 | 1 | 0.005967 |
| Age = all and On_thyroxine <= 0.5 and Sick = all and Thyroid_surgery <= 0.5 and Tumor = all and TSH > 0.0415 and FTI > 0.0345 and FTI <= 0.064465 | 1 | 0.002843 |
| TSH > 0.00605 and FTI <= 0.064465 and TSH > 0.016895 | 1 | 0.020000 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| TSH <= 0.00605 | 3 | 0.924197 |
| FTI <= 0.064465 and Thyroid_surgery <= 0.5 and T3 <= 0.0235 and TSH > 0.016895 and Age <= 0.76 | 1 | 0.180602 |
| FTI <= 0.063465 and Age <= 0.275 and Age > 0.165 | 3 | 0.010667 |
| FTI <= 0.063465 and T3 <= 0.0265 and T4U <= 0.141 and On_antithyroid_medication <= 0.5 and T4U <= 0.108 | 1 | 0.054475 |
| FTI > 0.062965 and On_thyroxine <= 0.5 and TT4 <= 0.1505 and TT4 > 0.0615 and T3 <= 0.0295 and Age > 0.425 and TT4 <= 0.14 and T4U <= 0.1285 | 2 | 0.563307 |
| FTI <= 0.0605 and T3 <= 0.026 and T4U > 0.1145 and Age > 0.455 | 1 | 0.032491 |
| On_thyroxine > 0.5 | 3 | 0.470320 |
| FTI > 0.062965 and TT4 <= 0.1505 and Thyroid_surgery <= 0.5 and TT4 > 0.0585 and T3 <= 0.029 and Age <= 0.775 | 2 | 0.629870 |
| FTI > 0.06 and T3 > 0.0115 and TT4 > 0.1495 | 3 | 0.547619 |
| TT4 > 0.1245 and Age <= 0.81 | 2 | 0.209302 |
| FTI > 0.06 and T3 > 0.0177 | 3 | 0.655172 |
| T4U <= 0.088 and TSH <= 0.0162 | 2 | 0.210526 |
| FTI <= 0.0725 and TT4 <= 0.05 | 3 | 0.454545 |
| Age <= 0.605 and TT4 > 0.071 | 3 | 0.454545 |
| FTI <= 0.068 and Age <= 0.385 | 1 | 0.500000 |
| FTI <= 0.0655 | 1 | 0.166667 |
|  | 2 | 0.666667 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| FTI <= 0.064 and TSH >= 0.00939 | 1 | 0.020511 |
| FTI <= 0.061 and TSH >= 0.0062 | 1 | 0.000460 |
| TSH >= 0.0061 and On_thyroxine <= 0 and T3 <= 0.02 and Thyroid_surgery <= 0 and TT4 <= 0.148 | 2 | 0.040620 |
| TSH >= 0.0061 and T3 >= 0.0208 and TT4 <= 0.15 and On_thyroxine <= 0 and T3 <= 0.028 | 2 | 0.010087 |
| TSH >= 0.0072 and T3 >= 0.029 and T3 <= 0.041 and TT4 >= 0.116 | 2 | 0.001226 |
|  | 3 | 1.000000 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

age|on_thyroxine|sick|thyroid_surgery|tumor|tsh|fti|class
---|---|---|---|---|---|---|---
all|(0.5-inf)|all|(-inf-0.5]|all|(0.0195-0.0415]|(0.14225-inf)|1
all|(-inf-0.5]|all|(-inf-0.5]|all|(0.0195-0.0415]|(0.14225-inf)|3
all|(0.5-inf)|all|(-inf-0.5]|all|(0.0415-inf)|(0.097495-0.14225]|3
all|(0.5-inf)|all|(-inf-0.5]|all|(0.00605-0.0195]|(0.14225-inf)|3
all|(-inf-0.5]|all|(-inf-0.5]|all|(0.00605-0.0195]|(0.14225-inf)|3
all|(0.5-inf)|all|(-inf-0.5]|all|(0.0195-0.0415]|(0.097495-0.14225]|3
all|(0.5-inf)|all|(0.5-inf)|all|(-inf-0.00605]|(0.14225-inf)|3
all|(-inf-0.5]|all|(-inf-0.5]|all|(0.0195-0.0415]|(0.097495-0.14225]|2
all|(0.5-inf)|all|(-inf-0.5]|all|(0.0415-inf)|(0.07794-0.097495]|1
all|(-inf-0.5]|all|(-inf-0.5]|all|(0.0415-inf)|(0.07794-0.097495]|2
all|(-inf-0.5]|all|(0.5-inf)|all|(-inf-0.00605]|(0.14225-inf)|3
all|(0.5-inf)|all|(0.5-inf)|all|(0.0195-0.0415]|(0.07794-0.097495]|1
all|(-inf-0.5]|all|(0.5-inf)|all|(0.00605-0.0195]|(0.097495-0.14225]|3
all|(-inf-0.5]|all|(0.5-inf)|all|(0.0195-0.0415]|(0.07794-0.097495]|1
all|(0.5-inf)|all|(-inf-0.5]|all|(-inf-0.00605]|(0.14225-inf)|3
all|(0.5-inf)|all|(-inf-0.5]|all|(0.00605-0.0195]|(0.097495-0.14225]|3
all|(-inf-0.5]|all|(-inf-0.5]|all|(-inf-0.00605]|(0.14225-inf)|3
all|(-inf-0.5]|all|(-inf-0.5]|all|(0.00605-0.0195]|(0.097495-0.14225]|2
all|(0.5-inf)|all|(-inf-0.5]|all|(0.0195-0.0415]|(0.07794-0.097495]|3
all|(-inf-0.5]|all|(-inf-0.5]|all|(0.0195-0.0415]|(0.07794-0.097495]|2
all|(0.5-inf)|all|(0.5-inf)|all|(-inf-0.00605]|(0.097495-0.14225]|3
all|(0.5-inf)|all|(-inf-0.5]|all|(0.0415-inf)|(0.064465-0.07794]|3
all|(-inf-0.5]|all|(-inf-0.5]|all|(0.0415-inf)|(0.064465-0.07794]|2
all|(-inf-0.5]|all|(0.5-inf)|all|(-inf-0.00605]|(0.097495-0.14225]|3
all|(-inf-0.5]|all|(0.5-inf)|all|(0.00605-0.0195]|(0.07794-0.097495]|3
all|(0.5-inf)|all|(-inf-0.5]|all|(-inf-0.00605]|(0.097495-0.14225]|3
all|(-inf-0.5]|all|(0.5-inf)|all|(0.0415-inf)|(0.0345-0.064465]|1
all|(0.5-inf)|all|(-inf-0.5]|all|(0.00605-0.0195]|(0.07794-0.097495]|3
all|(-inf-0.5]|all|(-inf-0.5]|all|(-inf-0.00605]|(0.097495-0.14225]|3
all|(-inf-0.5]|all|(-inf-0.5]|all|(0.00605-0.0195]|(0.07794-0.097495]|2
all|(0.5-inf)|all|(-inf-0.5]|all|(0.0195-0.0415]|(0.064465-0.07794]|3
all|(-inf-0.5]|all|(-inf-0.5]|all|(0.0195-0.0415]|(0.064465-0.07794]|2
all|(0.5-inf)|all|(-inf-0.5]|all|(0.0415-inf)|(0.0345-0.064465]|1
all|(-inf-0.5]|all|(-inf-0.5]|all|(0.0415-inf)|(0.0345-0.064465]|1
all|(-inf-0.5]|all|(0.5-inf)|all|(-inf-0.00605]|(0.07794-0.097495]|3
all|(-inf-0.5]|all|(0.5-inf)|all|(0.00605-0.0195]|(0.064465-0.07794]|3
all|(-inf-0.5]|all|(0.5-inf)|all|(0.0195-0.0415]|(0.0345-0.064465]|1
all|(0.5-inf)|all|(-inf-0.5]|all|(-inf-0.00605]|(0.07794-0.097495]|3
all|(0.5-inf)|all|(-inf-0.5]|all|(0.00605-0.0195]|(0.064465-0.07794]|3
all|(-inf-0.5]|all|(0.5-inf)|all|(0.0415-inf)|(0.0165-0.0345]|1
all|(-inf-0.5]|all|(-inf-0.5]|all|(-inf-0.00605]|(0.07794-0.097495]|3
all|(0.5-inf)|all|(-inf-0.5]|all|(0.0195-0.0415]|(0.0345-0.064465]|1
all|(-inf-0.5]|all|(-inf-0.5]|all|(0.00605-0.0195]|(0.064465-0.07794]|2
all|(0.5-inf)|all|(-inf-0.5]|all|(0.0415-inf)|(0.0165-0.0345]|1
all|(-inf-0.5]|all|(-inf-0.5]|all|(0.0195-0.0415]|(0.0345-0.064465]|1
all|(-inf-0.5]|all|(-inf-0.5]|all|(0.0415-inf)|(0.0165-0.0345]|1
all|(-inf-0.5]|all|(0.5-inf)|all|(-inf-0.00605]|(0.064465-0.07794]|3
all|(-inf-0.5]|all|(0.5-inf)|all|(0.00605-0.0195]|(0.0345-0.064465]|1
all|(-inf-0.5]|all|(0.5-inf)|all|(0.0195-0.0415]|(0.0165-0.0345]|1
all|(0.5-inf)|all|(-inf-0.5]|all|(-inf-0.00605]|(0.064465-0.07794]|3
all|(0.5-inf)|all|(-inf-0.5]|all|(0.00605-0.0195]|(0.0345-0.064465]|1
all|(-inf-0.5]|all|(0.5-inf)|all|(0.0415-inf)|(-inf-0.0165]|1
all|(-inf-0.5]|all|(-inf-0.5]|all|(-inf-0.00605]|(0.064465-0.07794]|3
all|(-inf-0.5]|all|(-inf-0.5]|all|(0.00605-0.0195]|(0.0345-0.064465]|1
all|(-inf-0.5]|all|(-inf-0.5]|all|(0.0195-0.0415]|(0.0165-0.0345]|1
all|(0.5-inf)|all|(-inf-0.5]|all|(0.0415-inf)|(-inf-0.0165]|1
all|(-inf-0.5]|all|(-inf-0.5]|all|(0.0415-inf)|(-inf-0.0165]|1
all|(-inf-0.5]|all|(0.5-inf)|all|(-inf-0.00605]|(0.0345-0.064465]|3
all|(0.5-inf)|all|(-inf-0.5]|all|(-inf-0.00605]|(0.0345-0.064465]|3
all|(-inf-0.5]|all|(-inf-0.5]|all|(-inf-0.00605]|(0.0345-0.064465]|3
all|(-inf-0.5]|all|(-inf-0.5]|all|(0.00605-0.0195]|(0.0165-0.0345]|1
all|(-inf-0.5]|all|(-inf-0.5]|all|(0.0195-0.0415]|(-inf-0.0165]|1
all|(-inf-0.5]|all|(-inf-0.5]|all|(-inf-0.00605]|(0.0165-0.0345]|3
all|(-inf-0.5]|all|(-inf-0.5]|all|(-inf-0.00605]|(-inf-0.0165]|1

## JRip

Decision list:

rules | predicted class
---|---
(FTI <= 0.064) and (TSH >= 0.00939)|1 (150.0/9.0)
(FTI <= 0.061) and (TSH >= 0.0062)|1 (13.0/5.0)
(TSH >= 0.0061) and (On_thyroxine <= 0) and (T3 <= 0.02) and (Thyroid_surgery <= 0) and (TT4 <= 0.148)|2 (257.0/0.0)
(TSH >= 0.0061) and (T3 >= 0.0208) and (TT4 <= 0.15) and (On_thyroxine <= 0) and (T3 <= 0.028)|2 (64.0/0.0)
(TSH >= 0.0072) and (T3 >= 0.029) and (T3 <= 0.041) and (TT4 >= 0.116)|2 (11.0/2.0)
|3 (5984.0/0.0)


## PART

Decision list:

rules | predicted class
---|---
TSH <= 0.00605|3 (5840.0)
FTI <= 0.064465 AND Thyroid_surgery <= 0.5 AND T3 <= 0.0235 AND TSH > 0.016895 AND Age <= 0.76|1 (108.0)
FTI <= 0.063465 AND Age <= 0.275 AND Age > 0.165|3 (4.0)
FTI <= 0.063465 AND T3 <= 0.0265 AND T4U <= 0.141 AND On_antithyroid_medication <= 0.5 AND T4U <= 0.108|1 (28.0)
FTI > 0.062965 AND On_thyroxine <= 0.5 AND TT4 <= 0.1505 AND TT4 > 0.0615 AND T3 <= 0.0295 AND Age > 0.425 AND TT4 <= 0.14 AND T4U <= 0.1285|2 (218.0)
FTI <= 0.0605 AND T3 <= 0.026 AND T4U > 0.1145 AND Age > 0.455|1 (9.0)
On_thyroxine > 0.5|3 (103.0)
FTI > 0.062965 AND TT4 <= 0.1505 AND Thyroid_surgery <= 0.5 AND TT4 > 0.0585 AND T3 <= 0.029 AND Age <= 0.775|2 (97.0)
FTI > 0.06 AND T3 > 0.0115 AND TT4 > 0.1495|3 (23.0)
TT4 > 0.1245 AND Age <= 0.81|2 (9.0)
FTI > 0.06 AND T3 > 0.0177|3 (19.0)
T4U <= 0.088 AND TSH <= 0.0162|2 (4.0)
FTI <= 0.0725 AND TT4 <= 0.05|3 (5.0)
Age <= 0.605 AND TT4 > 0.071|3 (5.0)
FTI <= 0.068 AND Age <= 0.385|1 (3.0)
FTI <= 0.0655|1 (2.0/1.0)
|2 (2.0)


## J48 Decision Tree

* TSH <= 0.00605: 3 (5840.0)
* TSH > 0.00605
	* FTI <= 0.064465
		* TSH <= 0.016895
			* T3 <= 0.013000000000000001: 1 (12.0/1.0)
			* T3 > 0.013000000000000001: 3 (12.0/4.0)
		* TSH > 0.016895: 1 (139.0/5.0)
	* FTI > 0.064465
		* On_thyroxine <= 0.5
			* TT4 <= 0.1505: 2 (351.0/21.0)
			* TT4 > 0.1505: 3 (23.0)
		* On_thyroxine > 0.5: 3 (102.0)


## SimpleCart Decision Tree

* TSH < 0.00605: 3(5840.0/0.0)
* TSH >= 0.00605
	* FTI < 0.064465: 1(149.0/14.0)
	* FTI >= 0.064465
		* On_thyroxine < 0.5
			* TT4 < 0.1505: 2(330.0/21.0)
			* TT4 >= 0.1505: 3(23.0/0.0)
		* On_thyroxine >= 0.5: 3(102.0/0.0)


