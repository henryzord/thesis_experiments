# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 3 | 0.926069 |
| TSH >= 0.00605 and FTI >= 0.064465 and On_thyroxine < 0.5 and TT4 < 0.1505 and Thyroid_surgery < 0.5 and TT4 >= 0.058499999999999996 and FTI < 0.1625 and T3 < 0.0295 | 2 | 0.049173 |
| TSH >= 0.00605 and FTI < 0.064465 and T3 < 0.0265 and T4U < 0.14100000000000001 and On_antithyroid_medication < 0.5 and TSH >= 0.009545000000000001 and Thyroid_surgery < 0.5 and I131_treatment < 0.5 | 1 | 0.020275 |
| TSH >= 0.00605 and FTI < 0.064465 and T3 < 0.0265 and T4U < 0.14100000000000001 and On_antithyroid_medication < 0.5 and TSH < 0.009545000000000001 and TT4 < 0.0595 | 1 | 0.001420 |
| Age = all and On_thyroxine <= 0.5 and Sick = all and Thyroid_surgery <= 0.5 and Hypopituitary = all and TSH > 0.00605 and TSH <= 0.0195 and TT4 > 0.0895 and TT4 <= 0.1505 | 2 | 0.024294 |
| TSH >= 0.00605 and FTI < 0.064465 and T3 < 0.0265 and T4U < 0.14100000000000001 and On_antithyroid_medication < 0.5 and TSH >= 0.009545000000000001 and Thyroid_surgery >= 0.5 | 1 | 0.000505 |
| Age = all and On_thyroxine <= 0.5 and Sick = all and Thyroid_surgery <= 0.5 and Hypopituitary = all and TSH > 0.00605 and TSH <= 0.0195 and TT4 > 0.0435 and TT4 <= 0.0605 | 2 | 0.000443 |
| Age = all and On_thyroxine <= 0.5 and Sick = all and Thyroid_surgery <= 0.5 and Hypopituitary = all and TSH > 0.0195 and TSH <= 0.0415 and TT4 <= 0.0185 | 1 | 0.000947 |
| Age = all and On_thyroxine > 0.5 and Sick = all and Thyroid_surgery <= 0.5 and Hypopituitary = all and TSH > 0.0415 and TT4 > 0.0605 and TT4 <= 0.0685 | 1 | 0.000355 |
| TSH >= 0.00605 and FTI < 0.064465 and T3 < 0.0265 and T4U < 0.14100000000000001 and On_antithyroid_medication < 0.5 and TSH >= 0.009545000000000001 and Thyroid_surgery < 0.5 and I131_treatment >= 0.5 | 1 | 0.000355 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| TSH <= 0.006 | 3 | 0.924197 |
| FTI <= 0.064 and Thyroid_surgery <= 0 and T3 <= 0.023 | 1 | 0.214924 |
| On_thyroxine <= 0 and FTI > 0.062 and TT4 <= 0.15 and TT4 > 0.061 and T3 <= 0.029 and Age > 0.42 | 2 | 0.574669 |
| FTI > 0.062 and On_thyroxine <= 0 and TT4 <= 0.15 and Thyroid_surgery <= 0 | 2 | 0.338990 |
| FTI > 0.063 | 3 | 0.929936 |
| TSH <= 0.017 | 3 | 0.426316 |
| TT4 <= 0.041 | 3 | 0.190476 |
|  | 1 | 0.916667 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| FTI <= 0.064 and TSH >= 0.0077 and T3 <= 0.011 and T4U <= 0.111 | 1 | 0.012172 |
| FTI <= 0.064 and TSH >= 0.018 and Thyroid_surgery <= 0 and Age <= 0.76 | 1 | 0.008459 |
| FTI <= 0.061 and TSH >= 0.0062 and T3 <= 0.01 and Age >= 0.52 | 1 | 0.001105 |
| FTI <= 0.061 and TSH >= 0.0062 and FTI >= 0.051 and Age <= 0.33 | 1 | 0.000632 |
| FTI <= 0.061 and TSH >= 0.0067 and T4U <= 0.103 and On_antithyroid_medication <= 0 and TSH <= 0.029 | 1 | 0.000789 |
| TSH >= 0.0061 and On_thyroxine <= 0 and T3 <= 0.02 and Thyroid_surgery <= 0 and FTI >= 0.06493 and TT4 <= 0.148 | 2 | 0.041067 |
| TSH >= 0.0061 and T3 >= 0.0208 and TT4 <= 0.15 and On_thyroxine <= 0 and TT4 >= 0.072 and T3 <= 0.03 | 2 | 0.010552 |
| TSH >= 0.0064 and T3 >= 0.031 and FTI <= 0.092 and TSH <= 0.0087 | 2 | 0.000833 |
| TSH >= 0.0064 and T3 >= 0.0208 and Age <= 0.55 and On_thyroxine <= 0 and Age >= 0.46 | 2 | 0.000333 |
|  | 3 | 0.999500 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

age|on_thyroxine|sick|thyroid_surgery|hypopituitary|tsh|tt4|class
---|---|---|---|---|---|---|---
all|(0.5-inf)|all|(-inf-0.5]|all|(0.0195-0.0415]|(0.1505-inf)|1
all|(0.5-inf)|all|(-inf-0.5]|all|(0.0415-inf)|(0.0895-0.1505]|3
all|(-inf-0.5]|all|(-inf-0.5]|all|(0.0195-0.0415]|(0.1505-inf)|3
all|(-inf-0.5]|all|(-inf-0.5]|all|(0.0415-inf)|(0.0895-0.1505]|1
all|(0.5-inf)|all|(-inf-0.5]|all|(0.00605-0.0195]|(0.1505-inf)|3
all|(-inf-0.5]|all|(-inf-0.5]|all|(0.00605-0.0195]|(0.1505-inf)|3
all|(0.5-inf)|all|(-inf-0.5]|all|(0.0195-0.0415]|(0.0895-0.1505]|3
all|(0.5-inf)|all|(0.5-inf)|all|(-inf-0.00605]|(0.1505-inf)|3
all|(0.5-inf)|all|(-inf-0.5]|all|(0.0415-inf)|(0.0685-0.0895]|3
all|(-inf-0.5]|all|(-inf-0.5]|all|(0.0195-0.0415]|(0.0895-0.1505]|2
all|(-inf-0.5]|all|(-inf-0.5]|all|(0.0415-inf)|(0.0685-0.0895]|2
all|(-inf-0.5]|all|(0.5-inf)|all|(-inf-0.00605]|(0.1505-inf)|3
all|(0.5-inf)|all|(0.5-inf)|all|(0.0195-0.0415]|(0.0685-0.0895]|1
all|(-inf-0.5]|all|(0.5-inf)|all|(0.00605-0.0195]|(0.0895-0.1505]|3
all|(-inf-0.5]|all|(0.5-inf)|all|(0.0195-0.0415]|(0.0685-0.0895]|1
all|(0.5-inf)|all|(-inf-0.5]|all|(-inf-0.00605]|(0.1505-inf)|3
all|(-inf-0.5]|all|(0.5-inf)|all|(0.0415-inf)|(0.0605-0.0685]|1
all|(-inf-0.5]|all|(-inf-0.5]|all|(-inf-0.00605]|(0.1505-inf)|3
all|(0.5-inf)|all|(-inf-0.5]|all|(0.00605-0.0195]|(0.0895-0.1505]|3
all|(0.5-inf)|all|(-inf-0.5]|all|(0.0195-0.0415]|(0.0685-0.0895]|3
all|(-inf-0.5]|all|(-inf-0.5]|all|(0.00605-0.0195]|(0.0895-0.1505]|2
all|(0.5-inf)|all|(-inf-0.5]|all|(0.0415-inf)|(0.0605-0.0685]|1
all|(-inf-0.5]|all|(-inf-0.5]|all|(0.0195-0.0415]|(0.0685-0.0895]|2
all|(0.5-inf)|all|(0.5-inf)|all|(-inf-0.00605]|(0.0895-0.1505]|3
all|(-inf-0.5]|all|(-inf-0.5]|all|(0.0415-inf)|(0.0605-0.0685]|2
all|(-inf-0.5]|all|(0.5-inf)|all|(-inf-0.00605]|(0.0895-0.1505]|3
all|(-inf-0.5]|all|(0.5-inf)|all|(0.00605-0.0195]|(0.0685-0.0895]|3
all|(-inf-0.5]|all|(0.5-inf)|all|(0.0195-0.0415]|(0.0605-0.0685]|1
all|(0.5-inf)|all|(-inf-0.5]|all|(-inf-0.00605]|(0.0895-0.1505]|3
all|(0.5-inf)|all|(-inf-0.5]|all|(0.00605-0.0195]|(0.0685-0.0895]|3
all|(-inf-0.5]|all|(-inf-0.5]|all|(-inf-0.00605]|(0.0895-0.1505]|3
all|(0.5-inf)|all|(-inf-0.5]|all|(0.0195-0.0415]|(0.0605-0.0685]|3
all|(-inf-0.5]|all|(-inf-0.5]|all|(0.00605-0.0195]|(0.0685-0.0895]|2
all|(0.5-inf)|all|(-inf-0.5]|all|(0.0415-inf)|(0.0435-0.0605]|1
all|(-inf-0.5]|all|(-inf-0.5]|all|(0.0195-0.0415]|(0.0605-0.0685]|2
all|(-inf-0.5]|all|(-inf-0.5]|all|(0.0415-inf)|(0.0435-0.0605]|1
all|(-inf-0.5]|all|(0.5-inf)|all|(-inf-0.00605]|(0.0685-0.0895]|3
all|(0.5-inf)|all|(-inf-0.5]|all|(-inf-0.00605]|(0.0685-0.0895]|3
all|(-inf-0.5]|all|(0.5-inf)|all|(0.0415-inf)|(0.0185-0.0435]|3
all|(0.5-inf)|all|(-inf-0.5]|all|(0.00605-0.0195]|(0.0605-0.0685]|1
all|(-inf-0.5]|all|(-inf-0.5]|all|(-inf-0.00605]|(0.0685-0.0895]|3
all|(0.5-inf)|all|(-inf-0.5]|all|(0.0195-0.0415]|(0.0435-0.0605]|1
all|(-inf-0.5]|all|(-inf-0.5]|all|(0.00605-0.0195]|(0.0605-0.0685]|2
all|(0.5-inf)|all|(-inf-0.5]|all|(0.0415-inf)|(0.0185-0.0435]|1
all|(-inf-0.5]|all|(-inf-0.5]|all|(0.0195-0.0415]|(0.0435-0.0605]|1
all|(-inf-0.5]|all|(-inf-0.5]|all|(0.0415-inf)|(0.0185-0.0435]|1
all|(-inf-0.5]|all|(0.5-inf)|all|(-inf-0.00605]|(0.0605-0.0685]|3
all|(-inf-0.5]|all|(0.5-inf)|all|(0.0195-0.0415]|(0.0185-0.0435]|1
all|(0.5-inf)|all|(-inf-0.5]|all|(-inf-0.00605]|(0.0605-0.0685]|3
all|(-inf-0.5]|all|(0.5-inf)|all|(0.0415-inf)|(-inf-0.0185]|1
all|(0.5-inf)|all|(-inf-0.5]|all|(0.00605-0.0195]|(0.0435-0.0605]|3
all|(-inf-0.5]|all|(-inf-0.5]|all|(-inf-0.00605]|(0.0605-0.0685]|3
all|(0.5-inf)|all|(-inf-0.5]|all|(0.0195-0.0415]|(0.0185-0.0435]|1
all|(-inf-0.5]|all|(-inf-0.5]|all|(0.00605-0.0195]|(0.0435-0.0605]|2
all|(0.5-inf)|all|(0.5-inf)|all|(-inf-0.00605]|(0.0435-0.0605]|1
all|(-inf-0.5]|all|(-inf-0.5]|all|(0.0195-0.0415]|(0.0185-0.0435]|1
all|(0.5-inf)|all|(-inf-0.5]|all|(0.0415-inf)|(-inf-0.0185]|1
all|(-inf-0.5]|all|(0.5-inf)|all|(-inf-0.00605]|(0.0435-0.0605]|3
all|(-inf-0.5]|all|(-inf-0.5]|all|(0.0415-inf)|(-inf-0.0185]|1
all|(0.5-inf)|all|(-inf-0.5]|all|(-inf-0.00605]|(0.0435-0.0605]|3
all|(0.5-inf)|all|(-inf-0.5]|all|(0.00605-0.0195]|(0.0185-0.0435]|1
all|(-inf-0.5]|all|(-inf-0.5]|all|(-inf-0.00605]|(0.0435-0.0605]|3
all|(-inf-0.5]|all|(-inf-0.5]|all|(0.00605-0.0195]|(0.0185-0.0435]|1
all|(-inf-0.5]|all|(-inf-0.5]|all|(0.0195-0.0415]|(-inf-0.0185]|1
all|(0.5-inf)|all|(-inf-0.5]|all|(-inf-0.00605]|(0.0185-0.0435]|1
all|(-inf-0.5]|all|(-inf-0.5]|all|(-inf-0.00605]|(0.0185-0.0435]|3
all|(-inf-0.5]|all|(-inf-0.5]|all|(-inf-0.00605]|(-inf-0.0185]|1

## JRip

Decision list:

rules | predicted class
---|---
(FTI <= 0.064) and (TSH >= 0.0077) and (T3 <= 0.011) and (T4U <= 0.111)|1 (78.0/0.0)
(FTI <= 0.064) and (TSH >= 0.018) and (Thyroid_surgery <= 0) and (Age <= 0.76)|1 (54.0/0.0)
(FTI <= 0.061) and (TSH >= 0.0062) and (T3 <= 0.01) and (Age >= 0.52)|1 (7.0/0.0)
(FTI <= 0.061) and (TSH >= 0.0062) and (FTI >= 0.051) and (Age <= 0.33)|1 (4.0/0.0)
(FTI <= 0.061) and (TSH >= 0.0067) and (T4U <= 0.103) and (On_antithyroid_medication <= 0) and (TSH <= 0.029)|1 (5.0/0.0)
(TSH >= 0.0061) and (On_thyroxine <= 0) and (T3 <= 0.02) and (Thyroid_surgery <= 0) and (FTI >= 0.06493) and (TT4 <= 0.148)|2 (257.0/0.0)
(TSH >= 0.0061) and (T3 >= 0.0208) and (TT4 <= 0.15) and (On_thyroxine <= 0) and (TT4 >= 0.072) and (T3 <= 0.03)|2 (64.0/0.0)
(TSH >= 0.0064) and (T3 >= 0.031) and (FTI <= 0.092) and (TSH <= 0.0087)|2 (5.0/0.0)
(TSH >= 0.0064) and (T3 >= 0.0208) and (Age <= 0.55) and (On_thyroxine <= 0) and (Age >= 0.46)|2 (2.0/0.0)
|3 (6003.0/3.0)


## PART

Decision list:

rules | predicted class
---|---
TSH <= 0.006|3 (5840.0)
FTI <= 0.064 AND Thyroid_surgery <= 0 AND T3 <= 0.023|1 (142.0/4.0)
On_thyroxine <= 0 AND FTI > 0.062 AND TT4 <= 0.15 AND TT4 > 0.061 AND T3 <= 0.029 AND Age > 0.42|2 (235.0/2.0)
FTI > 0.062 AND On_thyroxine <= 0 AND TT4 <= 0.15 AND Thyroid_surgery <= 0|2 (107.0/10.0)
FTI > 0.063|3 (134.0)
TSH <= 0.017|3 (7.0/1.0)
TT4 <= 0.041|3 (7.0/3.0)
|1 (7.0)


## SimpleCart Decision Tree

* TSH < 0.00605: 3(5840.0/0.0)
* TSH >= 0.00605
	* FTI < 0.064465
		* T3 < 0.0265
			* T4U < 0.14100000000000001
				* On_antithyroid_medication < 0.5
					* TSH < 0.009545000000000001
						* TT4 < 0.0595: 1(9.0/0.0)
						* TT4 >= 0.0595: 3(3.0/0.0)
					* TSH >= 0.009545000000000001
						* Thyroid_surgery < 0.5
							* I131_treatment < 0.5: 1(131.0/0.0)
							* I131_treatment >= 0.5: 1(3.0/1.0)
						* Thyroid_surgery >= 0.5: 1(4.0/1.0)
				* On_antithyroid_medication >= 0.5: 3(2.0/1.0)
			* T4U >= 0.14100000000000001: 3(3.0/1.0)
		* T3 >= 0.0265: 3(4.0/0.0)
	* FTI >= 0.064465
		* On_thyroxine < 0.5
			* TT4 < 0.1505
				* Thyroid_surgery < 0.5
					* TT4 < 0.058499999999999996
						* T3 < 0.01755: 2(4.0/0.0)
						* T3 >= 0.01755: 3(5.0/0.0)
					* TT4 >= 0.058499999999999996
						* FTI < 0.1625
							* T3 < 0.0295: 2(318.0/0.0)
							* T3 >= 0.0295
								* TT4 < 0.119645: 3(4.0/0.0)
								* TT4 >= 0.119645: 2(8.0/0.0)
						* FTI >= 0.1625: 3(2.0/0.0)
				* Thyroid_surgery >= 0.5: 3(10.0/0.0)
			* TT4 >= 0.1505: 3(23.0/0.0)
		* On_thyroxine >= 0.5: 3(102.0/0.0)


