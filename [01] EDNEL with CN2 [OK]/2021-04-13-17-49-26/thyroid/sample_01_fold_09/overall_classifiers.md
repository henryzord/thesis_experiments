# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 3 | 0.926069 |
| TSH >= 0.00605 and FTI >= 0.064255 and On_thyroxine < 0.5 and TT4 < 0.1505 and Thyroid_surgery < 0.5 | 2 | 0.049375 |
| On_thyroxine <= 0.5 and Thyroid_surgery <= 0.5 and Tumor = all and TSH > 0.0195 and TSH <= 0.0415 and FTI > 0.0345 and FTI <= 0.064255 | 1 | 0.003783 |
| On_thyroxine <= 0.5 and Thyroid_surgery <= 0.5 and Tumor = all and TSH > 0.00605 and TSH <= 0.0195 and FTI > 0.013735 and FTI <= 0.0345 | 1 | 0.000316 |
| On_thyroxine <= 0.5 and Thyroid_surgery > 0.5 and Tumor = all and TSH > 0.0415 and FTI <= 0.013735 | 1 | 0.000158 |
| On_thyroxine <= 0.5 and Thyroid_surgery <= 0.5 and Tumor = all and TSH > 0.0415 and FTI > 0.0345 and FTI <= 0.064255 | 1 | 0.003000 |
| On_thyroxine > 0.5 and Thyroid_surgery <= 0.5 and Tumor = all and TSH > 0.0415 and FTI > 0.013735 and FTI <= 0.0345 | 1 | 0.000355 |
| On_thyroxine > 0.5 and Thyroid_surgery <= 0.5 and Tumor = all and TSH > 0.00605 and TSH <= 0.0195 and FTI > 0.0345 and FTI <= 0.064255 | 1 | 0.000053 |
| On_thyroxine <= 0.5 and Thyroid_surgery <= 0.5 and Tumor = all and TSH > 0.0415 and FTI <= 0.013735 | 1 | 0.005030 |
| On_thyroxine <= 0.5 and Thyroid_surgery <= 0.5 and Tumor = all and TSH > 0.0195 and TSH <= 0.0415 and FTI <= 0.013735 | 1 | 0.001105 |
| On_thyroxine <= 0.5 and Thyroid_surgery <= 0.5 and Tumor = all and TSH > 0.0415 and FTI > 0.013735 and FTI <= 0.0345 | 1 | 0.004566 |
| On_thyroxine > 0.5 and Thyroid_surgery <= 0.5 and Tumor = all and TSH > 0.0195 and TSH <= 0.0415 and FTI > 0.0345 and FTI <= 0.064255 | 1 | 0.000789 |
| On_thyroxine > 0.5 and Thyroid_surgery <= 0.5 and Tumor = all and TSH > 0.0415 and FTI <= 0.013735 | 1 | 0.000474 |
| On_thyroxine <= 0.5 and Thyroid_surgery <= 0.5 and Tumor = all and TSH > 0.0195 and TSH <= 0.0415 and FTI > 0.013735 and FTI <= 0.0345 | 1 | 0.000474 |
| On_thyroxine <= 0.5 and Thyroid_surgery > 0.5 and Tumor = all and TSH > 0.0415 and FTI > 0.0345 and FTI <= 0.064255 | 1 | 0.000158 |
| On_thyroxine > 0.5 and Thyroid_surgery <= 0.5 and Tumor = all and TSH > 0.0415 and FTI > 0.0345 and FTI <= 0.064255 | 1 | 0.000316 |
| On_thyroxine <= 0.5 and Thyroid_surgery > 0.5 and Tumor = all and TSH > 0.0415 and FTI > 0.013735 and FTI <= 0.0345 | 1 | 0.000053 |
| TSH > 0.006 and FTI <= 0.064 | 1 | 0.021068 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| TSH <= 0.00605 | 3 | 0.924185 |
| FTI <= 0.064255 and Thyroid_surgery <= 0.5 and TSH > 0.017395 and I131_treatment <= 0.5 and T3 <= 0.0224 | 1 | 0.197712 |
| FTI > 0.06472 and On_thyroxine <= 0.5 and TT4 <= 0.1505 and TT4 > 0.0615 and Age > 0.425 and TT4 <= 0.1415 and T4U <= 0.1255 and T3 <= 0.0245 | 2 | 0.529851 |
| FTI <= 0.062755 and Sex <= 0.5 and FTI > 0.0495 and TSH > 0.009995 | 1 | 0.031359 |
| FTI <= 0.062755 and T3 <= 0.011 and T3 > 0.0088 | 1 | 0.034722 |
| On_thyroxine > 0.5 and T3 > 0.008 | 3 | 0.440000 |
| FTI > 0.062965 and TT4 <= 0.1505 and Thyroid_surgery <= 0.5 and T3 > 0.009 and TT4 > 0.0565 and T3 <= 0.0295 and Age <= 0.73 | 2 | 0.582353 |
| FTI > 0.063 and TT4 > 0.1495 | 3 | 0.470588 |
| TT4 > 0.125 and TT4 <= 0.145 | 2 | 0.145455 |
| FTI > 0.063 and Thyroid_surgery <= 0.5 and T3 > 0.01875 | 3 | 0.324675 |
| FTI > 0.063 and Thyroid_surgery > 0.5 | 3 | 0.366667 |
| FTI > 0.063 and TT4 > 0.066 | 3 | 0.131579 |
| FTI <= 0.063 and T4U <= 0.1005 | 1 | 0.228571 |
| T4U > 0.0935 | 3 | 0.416667 |
|  | 2 | 0.769231 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| FTI <= 0.064 and TSH >= 0.00879 | 1 | 0.020529 |
| FTI <= 0.064 and TSH >= 0.0063 | 1 | 0.000369 |
| TSH >= 0.0061 and On_thyroxine <= 0 and TT4 <= 0.144 and Thyroid_surgery <= 0 | 2 | 0.048961 |
|  | 3 | 0.999167 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

on_thyroxine|thyroid_surgery|tumor|tsh|fti|class
---|---|---|---|---|---
(-inf-0.5]|(-inf-0.5]|all|(0.0195-0.0415]|(0.14225-inf)|3
(0.5-inf)|(-inf-0.5]|all|(0.0195-0.0415]|(0.14225-inf)|1
(0.5-inf)|(-inf-0.5]|all|(0.0415-inf)|(0.097495-0.14225]|3
(0.5-inf)|(-inf-0.5]|all|(0.00605-0.0195]|(0.14225-inf)|3
(-inf-0.5]|(-inf-0.5]|all|(0.00605-0.0195]|(0.14225-inf)|3
(0.5-inf)|(-inf-0.5]|all|(0.0195-0.0415]|(0.097495-0.14225]|3
(-inf-0.5]|(-inf-0.5]|all|(0.0195-0.0415]|(0.097495-0.14225]|2
(-inf-0.5]|(-inf-0.5]|all|(0.0415-inf)|(0.08002-0.097495]|2
(0.5-inf)|(0.5-inf)|all|(-inf-0.00605]|(0.14225-inf)|3
(-inf-0.5]|(0.5-inf)|all|(-inf-0.00605]|(0.14225-inf)|3
(-inf-0.5]|(0.5-inf)|all|(0.00605-0.0195]|(0.097495-0.14225]|3
(-inf-0.5]|(-inf-0.5]|all|(-inf-0.00605]|(0.14225-inf)|3
(0.5-inf)|(-inf-0.5]|all|(-inf-0.00605]|(0.14225-inf)|3
(-inf-0.5]|(0.5-inf)|all|(0.0195-0.0415]|(0.08002-0.097495]|1
(0.5-inf)|(-inf-0.5]|all|(0.00605-0.0195]|(0.097495-0.14225]|3
(-inf-0.5]|(-inf-0.5]|all|(0.00605-0.0195]|(0.097495-0.14225]|2
(0.5-inf)|(-inf-0.5]|all|(0.0195-0.0415]|(0.08002-0.097495]|3
(-inf-0.5]|(-inf-0.5]|all|(0.0195-0.0415]|(0.08002-0.097495]|2
(-inf-0.5]|(-inf-0.5]|all|(0.0415-inf)|(0.064255-0.08002]|2
(-inf-0.5]|(0.5-inf)|all|(-inf-0.00605]|(0.097495-0.14225]|3
(0.5-inf)|(0.5-inf)|all|(-inf-0.00605]|(0.097495-0.14225]|3
(0.5-inf)|(-inf-0.5]|all|(0.0415-inf)|(0.064255-0.08002]|3
(-inf-0.5]|(0.5-inf)|all|(0.00605-0.0195]|(0.08002-0.097495]|3
(0.5-inf)|(-inf-0.5]|all|(-inf-0.00605]|(0.097495-0.14225]|3
(-inf-0.5]|(-inf-0.5]|all|(-inf-0.00605]|(0.097495-0.14225]|3
(0.5-inf)|(-inf-0.5]|all|(0.00605-0.0195]|(0.08002-0.097495]|3
(-inf-0.5]|(-inf-0.5]|all|(0.00605-0.0195]|(0.08002-0.097495]|2
(-inf-0.5]|(0.5-inf)|all|(0.0415-inf)|(0.0345-0.064255]|1
(-inf-0.5]|(-inf-0.5]|all|(0.0195-0.0415]|(0.064255-0.08002]|2
(0.5-inf)|(-inf-0.5]|all|(0.0195-0.0415]|(0.064255-0.08002]|3
(0.5-inf)|(-inf-0.5]|all|(0.0415-inf)|(0.0345-0.064255]|1
(-inf-0.5]|(0.5-inf)|all|(-inf-0.00605]|(0.08002-0.097495]|3
(-inf-0.5]|(-inf-0.5]|all|(0.0415-inf)|(0.0345-0.064255]|1
(-inf-0.5]|(0.5-inf)|all|(0.00605-0.0195]|(0.064255-0.08002]|3
(0.5-inf)|(-inf-0.5]|all|(-inf-0.00605]|(0.08002-0.097495]|3
(-inf-0.5]|(-inf-0.5]|all|(-inf-0.00605]|(0.08002-0.097495]|3
(-inf-0.5]|(0.5-inf)|all|(0.0195-0.0415]|(0.0345-0.064255]|1
(-inf-0.5]|(-inf-0.5]|all|(0.00605-0.0195]|(0.064255-0.08002]|2
(0.5-inf)|(-inf-0.5]|all|(0.00605-0.0195]|(0.064255-0.08002]|3
(-inf-0.5]|(0.5-inf)|all|(0.0415-inf)|(0.013735-0.0345]|1
(0.5-inf)|(-inf-0.5]|all|(0.0195-0.0415]|(0.0345-0.064255]|1
(-inf-0.5]|(-inf-0.5]|all|(0.0195-0.0415]|(0.0345-0.064255]|1
(-inf-0.5]|(0.5-inf)|all|(-inf-0.00605]|(0.064255-0.08002]|3
(0.5-inf)|(-inf-0.5]|all|(0.0415-inf)|(0.013735-0.0345]|1
(-inf-0.5]|(-inf-0.5]|all|(0.0415-inf)|(0.013735-0.0345]|1
(0.5-inf)|(-inf-0.5]|all|(-inf-0.00605]|(0.064255-0.08002]|3
(-inf-0.5]|(-inf-0.5]|all|(-inf-0.00605]|(0.064255-0.08002]|3
(-inf-0.5]|(0.5-inf)|all|(0.0195-0.0415]|(0.013735-0.0345]|1
(-inf-0.5]|(-inf-0.5]|all|(0.00605-0.0195]|(0.0345-0.064255]|1
(0.5-inf)|(-inf-0.5]|all|(0.00605-0.0195]|(0.0345-0.064255]|1
(-inf-0.5]|(0.5-inf)|all|(0.0415-inf)|(-inf-0.013735]|1
(-inf-0.5]|(-inf-0.5]|all|(0.0195-0.0415]|(0.013735-0.0345]|1
(-inf-0.5]|(0.5-inf)|all|(-inf-0.00605]|(0.0345-0.064255]|3
(0.5-inf)|(-inf-0.5]|all|(0.0415-inf)|(-inf-0.013735]|1
(-inf-0.5]|(-inf-0.5]|all|(0.0415-inf)|(-inf-0.013735]|1
(0.5-inf)|(-inf-0.5]|all|(-inf-0.00605]|(0.0345-0.064255]|3
(-inf-0.5]|(-inf-0.5]|all|(-inf-0.00605]|(0.0345-0.064255]|3
(-inf-0.5]|(-inf-0.5]|all|(0.00605-0.0195]|(0.013735-0.0345]|1
(-inf-0.5]|(-inf-0.5]|all|(0.0195-0.0415]|(-inf-0.013735]|1
(-inf-0.5]|(-inf-0.5]|all|(-inf-0.00605]|(0.013735-0.0345]|3
(-inf-0.5]|(-inf-0.5]|all|(-inf-0.00605]|(-inf-0.013735]|1

## JRip

Decision list:

rules | predicted class
---|---
(FTI <= 0.064) and (TSH >= 0.00879)|1 (152.0/10.0)
(FTI <= 0.064) and (TSH >= 0.0063)|1 (11.0/4.0)
(TSH >= 0.0061) and (On_thyroxine <= 0) and (TT4 <= 0.144) and (Thyroid_surgery <= 0)|2 (334.0/9.0)
|3 (5982.0/5.0)


## PART

Decision list:

rules | predicted class
---|---
TSH <= 0.00605|3 (5839.0)
FTI <= 0.064255 AND Thyroid_surgery <= 0.5 AND TSH > 0.017395 AND I131_treatment <= 0.5 AND T3 <= 0.0224|1 (121.0)
FTI > 0.06472 AND On_thyroxine <= 0.5 AND TT4 <= 0.1505 AND TT4 > 0.0615 AND Age > 0.425 AND TT4 <= 0.1415 AND T4U <= 0.1255 AND T3 <= 0.0245|2 (213.0)
FTI <= 0.062755 AND Sex <= 0.5 AND FTI > 0.0495 AND TSH > 0.009995|1 (9.0)
FTI <= 0.062755 AND T3 <= 0.011 AND T3 > 0.0088|1 (10.0)
On_thyroxine > 0.5 AND T3 > 0.008|3 (99.0)
FTI > 0.062965 AND TT4 <= 0.1505 AND Thyroid_surgery <= 0.5 AND T3 > 0.009 AND TT4 > 0.0565 AND T3 <= 0.0295 AND Age <= 0.73|2 (99.0)
FTI > 0.063 AND TT4 > 0.1495|3 (24.0)
TT4 > 0.125 AND TT4 <= 0.145|2 (8.0)
FTI > 0.063 AND Thyroid_surgery <= 0.5 AND T3 > 0.01875|3 (11.0/1.0)
FTI > 0.063 AND Thyroid_surgery > 0.5|3 (11.0)
FTI > 0.063 AND TT4 > 0.066|3 (9.0/4.0)
FTI <= 0.063 AND T4U <= 0.1005|1 (10.0/2.0)
T4U > 0.0935|3 (10.0/1.0)
|2 (6.0/1.0)


## J48 Decision Tree

* TSH <= 0.006: 3 (5839.0)
* TSH > 0.006
	* FTI <= 0.064: 1 (163.0/14.0)
	* FTI > 0.064
		* On_thyroxine <= 0.0
			* TT4 <= 0.15
				* TT4 <= 0.061: 2 (16.0/6.0)
				* TT4 > 0.061
					* Age <= 0.42
						* Thyroid_surgery <= 0.0: 2 (87.0/2.0)
						* Thyroid_surgery > 0.0: 3 (10.0)
					* Age > 0.42: 2 (239.0/4.0)
			* TT4 > 0.15: 3 (24.0)
		* On_thyroxine > 0.0: 3 (101.0)


## SimpleCart Decision Tree

* TSH < 0.00605: 3(5839.0/0.0)
* TSH >= 0.00605
	* FTI < 0.064255: 1(149.0/14.0)
	* FTI >= 0.064255
		* On_thyroxine < 0.5
			* TT4 < 0.1505
				* Thyroid_surgery < 0.5: 2(330.0/11.0)
				* Thyroid_surgery >= 0.5: 3(11.0/0.0)
			* TT4 >= 0.1505: 3(24.0/0.0)
		* On_thyroxine >= 0.5: 3(101.0/0.0)


