# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| TSH <= 0.006 | 3 | 0.924319 |
| TSH >= 0.00605 and FTI >= 0.064255 and On_thyroxine < 0.5 and TT4 < 0.1505 and Thyroid_surgery < 0.5 and TT4 >= 0.058499999999999996 and T3 < 0.0295 | 2 | 0.049019 |
| TSH > 0.006 and FTI <= 0.064 | 1 | 0.021224 |
| TSH > 0.006 and FTI > 0.064 and On_thyroxine > 0 | 3 | 0.173010 |
| TSH > 0.006 and FTI > 0.064 and On_thyroxine <= 0 and TT4 > 0.15 | 3 | 0.049702 |
| TSH >= 0.00605 and FTI >= 0.064255 and On_thyroxine < 0.5 and TT4 < 0.1505 and Thyroid_surgery >= 0.5 | 3 | 0.018480 |
| TSH > 0.006 and FTI > 0.064 and On_thyroxine <= 0 and TT4 <= 0.15 and TT4 > 0.058 and T3 > 0.029 and Age > 0.37 | 3 | 0.010648 |
| TSH > 0.006 and FTI > 0.064 and On_thyroxine <= 0 and TT4 <= 0.15 and TT4 <= 0.058 | 3 | 0.009261 |
| TSH >= 0.00605 and FTI >= 0.064255 and On_thyroxine < 0.5 and TT4 < 0.1505 and Thyroid_surgery < 0.5 and TT4 >= 0.058499999999999996 and T3 >= 0.0295 | 2 | 0.000488 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| TSH <= 0.006 | 3 | 0.924319 |
| FTI <= 0.064 and Thyroid_surgery <= 0 and T3 <= 0.011 | 1 | 0.181970 |
| FTI <= 0.064 and T3 <= 0.026 and On_antithyroid_medication <= 0 and Thyroid_surgery <= 0 and I131_treatment <= 0 | 1 | 0.065086 |
| On_thyroxine <= 0 and TT4 <= 0.15 and Thyroid_surgery <= 0 and FTI > 0.06548 and TT4 > 0.061 and T3 <= 0.029 | 2 | 0.649166 |
| On_thyroxine > 0 | 3 | 0.817460 |
| FTI > 0.064 and FTI > 0.067 and TT4 > 0.148 | 3 | 0.520833 |
| FTI <= 0.064 and I131_treatment <= 0 and TT4 <= 0.054 | 3 | 0.206897 |
| FTI <= 0.064 and Thyroid_surgery > 0 | 1 | 0.046875 |
| Thyroid_surgery > 0 | 3 | 0.333333 |
| TSH > 0.022 and FTI > 0.066 | 3 | 0.130435 |
| TSH <= 0.026 and Query_hyperthyroid <= 0 and Psych <= 0 and T4U <= 0.119 and T3 > 0.019 and FTI > 0.067 | 3 | 0.333333 |
| FTI > 0.064 | 2 | 0.710526 |
| FTI <= 0.054 | 3 | 0.600000 |
|  | 1 | 0.500000 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| FTI <= 0.064 and TSH >= 0.0062 | 1 | 0.021224 |
| TSH >= 0.0061 and On_thyroxine <= 0 and T3 <= 0.02 and Thyroid_surgery <= 0 and TT4 <= 0.148 | 2 | 0.039395 |
| TSH >= 0.0061 and T3 >= 0.0208 and TT4 <= 0.15 and On_thyroxine <= 0 | 2 | 0.011394 |
|  | 3 | 1.000000 |


# Text representation of classifiers as-is

## JRip

Decision list:

rules | predicted class
---|---
(FTI <= 0.064) and (TSH >= 0.0062)|1 (164.0/14.0)
(TSH >= 0.0061) and (On_thyroxine <= 0) and (T3 <= 0.02) and (Thyroid_surgery <= 0) and (TT4 <= 0.148)|2 (251.0/1.0)
(TSH >= 0.0061) and (T3 >= 0.0208) and (TT4 <= 0.15) and (On_thyroxine <= 0)|2 (84.0/6.0)
|3 (5979.0/0.0)


## PART

Decision list:

rules | predicted class
---|---
TSH <= 0.006|3 (5838.0)
FTI <= 0.064 AND Thyroid_surgery <= 0 AND T3 <= 0.011|1 (109.0)
FTI <= 0.064 AND T3 <= 0.026 AND On_antithyroid_medication <= 0 AND Thyroid_surgery <= 0 AND I131_treatment <= 0|1 (38.0/2.0)
On_thyroxine <= 0 AND TT4 <= 0.15 AND Thyroid_surgery <= 0 AND FTI > 0.06548 AND TT4 > 0.061 AND T3 <= 0.029|2 (311.0/1.0)
On_thyroxine > 0|3 (102.0)
FTI > 0.064 AND FTI > 0.067 AND TT4 > 0.148|3 (25.0)
FTI <= 0.064 AND I131_treatment <= 0 AND TT4 <= 0.054|3 (6.0)
FTI <= 0.064 AND Thyroid_surgery > 0|1 (4.0/1.0)
Thyroid_surgery > 0|3 (9.0)
TSH > 0.022 AND FTI > 0.066|3 (3.0)
TSH <= 0.026 AND Query_hyperthyroid <= 0 AND Psych <= 0 AND T4U <= 0.119 AND T3 > 0.019 AND FTI > 0.067|3 (9.0)
FTI > 0.064|2 (19.0/1.0)
FTI <= 0.054|3 (3.0)
|1 (2.0)


## J48 Decision Tree

* TSH <= 0.006: 3 (5111.0)
* TSH > 0.006
	* FTI <= 0.064: 1 (144.0/12.0)
	* FTI > 0.064
		* On_thyroxine <= 0
			* TT4 <= 0.15
				* TT4 <= 0.058: 3 (11.0/4.0)
				* TT4 > 0.058
					* T3 <= 0.029: 2 (283.0/6.0)
					* T3 > 0.029
						* Age <= 0.37: 2 (5.0)
						* Age > 0.37: 3 (5.0/1.0)
			* TT4 > 0.15: 3 (24.0)
		* On_thyroxine > 0: 3 (86.0)


## SimpleCart Decision Tree

* TSH < 0.00605: 3(5838.0/0.0)
* TSH >= 0.00605
	* FTI < 0.064255: 1(150.0/14.0)
	* FTI >= 0.064255
		* On_thyroxine < 0.5
			* TT4 < 0.1505
				* Thyroid_surgery < 0.5
					* TT4 < 0.058499999999999996: 3(7.0/4.0)
					* TT4 >= 0.058499999999999996
						* T3 < 0.0295: 2(318.0/1.0)
						* T3 >= 0.0295: 2(6.0/6.0)
				* Thyroid_surgery >= 0.5: 3(9.0/0.0)
			* TT4 >= 0.1505: 3(25.0/0.0)
		* On_thyroxine >= 0.5: 3(100.0/0.0)


