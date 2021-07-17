# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| TSH <= 0.00605 | 3 | 0.924209 |
| TSH >= 0.00605 and FTI >= 0.064255 and On_thyroxine < 0.5 and TT4 < 0.1505 | 2 | 0.048042 |
| TSH >= 0.00605 and FTI < 0.064255 | 1 | 0.020819 |
| TSH >= 0.00605 and FTI >= 0.064255 and On_thyroxine < 0.5 and TT4 >= 0.1505 | 3 | 0.040080 |
| TSH > 0.00605 and FTI > 0.064465 and On_thyroxine <= 0.5 and TT4 <= 0.1505 and TT4 > 0.0615 and T3 <= 0.0305 and Sex <= 0.5 and Thyroid_surgery > 0.5 | 3 | 0.018443 |
| TSH >= 0.00605 and FTI >= 0.064255 and On_thyroxine >= 0.5 | 3 | 0.175559 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| TSH <= 0.006 | 3 | 0.924209 |
| FTI > 0.064 and On_thyroxine <= 0 and TT4 <= 0.15 and TT4 > 0.061 and T3 <= 0.028 and Age > 0.42 | 2 | 0.433854 |
| FTI <= 0.064 | 1 | 0.350395 |
| On_thyroxine <= 0 and TT4 <= 0.15 and Thyroid_surgery <= 0 | 2 | 0.325664 |
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
TSH <= 0.006|3 (5196.0)
FTI > 0.064 AND On_thyroxine <= 0 AND TT4 <= 0.15 AND TT4 > 0.061 AND T3 <= 0.028 AND Age > 0.42|2 (213.0)
FTI <= 0.064|1 (149.0/16.0)
On_thyroxine <= 0 AND TT4 <= 0.15 AND Thyroid_surgery <= 0|2 (90.0/10.0)
|3 (112.0)


## J48 Decision Tree

* TSH <= 0.00605: 3 (3899.0)
* TSH > 0.00605
	* FTI <= 0.064465: 1 (114.0/14.0)
	* FTI > 0.064465
		* On_thyroxine <= 0.5
			* TT4 <= 0.1505
				* TT4 <= 0.0615: 2 (8.0/4.0)
				* TT4 > 0.0615
					* T3 <= 0.0305
						* Sex <= 0.5
							* Thyroid_surgery <= 0.5: 2 (170.0)
							* Thyroid_surgery > 0.5: 3 (6.0)
						* Sex > 0.5: 2 (41.0)
					* T3 > 0.0305: 2 (8.0/3.0)
			* TT4 > 0.1505: 3 (9.0)
		* On_thyroxine > 0.5: 3 (65.0)


## SimpleCart Decision Tree

* TSH < 0.00605: 3(5841.0/0.0)
* TSH >= 0.00605
	* FTI < 0.064255: 1(149.0/16.0)
	* FTI >= 0.064255
		* On_thyroxine < 0.5
			* TT4 < 0.1505: 2(330.0/21.0)
			* TT4 >= 0.1505: 3(20.0/0.0)
		* On_thyroxine >= 0.5: 3(102.0/0.0)


