# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| TSH < 0.00605 | 3 | 0.924209 |
| TSH >= 0.00605 and FTI >= 0.064255 and On_thyroxine < 0.5 and TT4 < 0.1505 and Thyroid_surgery < 0.5 and TT4 >= 0.058499999999999996 and T3 < 0.0295 | 2 | 0.049173 |
| TSH >= 0.00605 and FTI < 0.064255 and T3 < 0.0265 and Thyroid_surgery < 0.5 and On_antithyroid_medication < 0.5 and TSH >= 0.009545000000000001 and I131_treatment < 0.5 | 1 | 0.020427 |
| TSH >= 0.00605 and FTI >= 0.064255 and On_thyroxine >= 0.5 | 3 | 0.175559 |
| TSH >= 0.00605 and FTI >= 0.064255 and On_thyroxine < 0.5 and TT4 >= 0.1505 | 3 | 0.040080 |
| TSH >= 0.00605 and FTI >= 0.064255 and On_thyroxine < 0.5 and TT4 < 0.1505 and Thyroid_surgery >= 0.5 | 3 | 0.018443 |
| TSH >= 0.00605 and FTI < 0.064255 and T3 < 0.0265 and Thyroid_surgery < 0.5 and On_antithyroid_medication < 0.5 and TSH < 0.009545000000000001 and TT4 < 0.0595 | 1 | 0.001420 |
| TSH >= 0.00605 and FTI >= 0.064255 and On_thyroxine < 0.5 and TT4 < 0.1505 and Thyroid_surgery < 0.5 and TT4 < 0.058499999999999996 and T3 >= 0.01755 | 3 | 0.010331 |
| TSH >= 0.00605 and FTI >= 0.064255 and On_thyroxine < 0.5 and TT4 < 0.1505 and Thyroid_surgery < 0.5 and TT4 >= 0.058499999999999996 and T3 >= 0.0295 and T4U < 0.113 | 3 | 0.010331 |
| TSH >= 0.00605 and FTI < 0.064255 and T3 >= 0.0265 | 3 | 0.010331 |
| TSH >= 0.00605 and FTI >= 0.064255 and On_thyroxine < 0.5 and TT4 < 0.1505 and Thyroid_surgery < 0.5 and TT4 >= 0.058499999999999996 and T3 >= 0.0295 and T4U >= 0.113 | 2 | 0.000975 |
| TSH >= 0.00605 and FTI < 0.064255 and T3 < 0.0265 and Thyroid_surgery >= 0.5 and T3 >= 0.0108 | 3 | 0.006224 |
| TSH >= 0.00605 and FTI < 0.064255 and T3 < 0.0265 and Thyroid_surgery < 0.5 and On_antithyroid_medication < 0.5 and TSH >= 0.009545000000000001 and I131_treatment >= 0.5 | 1 | 0.000564 |
| TSH >= 0.00605 and FTI < 0.064255 and T3 < 0.0265 and Thyroid_surgery < 0.5 and On_antithyroid_medication < 0.5 and TSH < 0.009545000000000001 and TT4 >= 0.0595 | 3 | 0.006224 |
| TSH >= 0.00605 and FTI >= 0.064255 and On_thyroxine < 0.5 and TT4 < 0.1505 and Thyroid_surgery < 0.5 and TT4 < 0.058499999999999996 and T3 < 0.01755 | 2 | 0.000677 |
| TSH >= 0.00605 and FTI < 0.064255 and T3 < 0.0265 and Thyroid_surgery < 0.5 and On_antithyroid_medication >= 0.5 | 3 | 0.002778 |
| TSH >= 0.00605 and FTI < 0.064255 and T3 < 0.0265 and Thyroid_surgery >= 0.5 and T3 < 0.0108 | 1 | 0.000211 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| TSH <= 0.006 | 3 | 0.924209 |
| FTI <= 0.064 and T3 <= 0.011 | 1 | 0.185058 |
| FTI <= 0.064 and TSH > 0.017 | 1 | 0.051083 |
| On_thyroxine <= 0.0 and TT4 <= 0.15 and FTI > 0.06548 | 2 | 0.654425 |
|  | 3 | 0.952096 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| FTI <= 0.064 and TSH >= 0.0062 | 1 | 0.020819 |
| TSH >= 0.0061 and On_thyroxine <= 0 and T3 <= 0.02 and Thyroid_surgery <= 0 and TT4 <= 0.146 | 2 | 0.040476 |
| TSH >= 0.0061 and On_thyroxine <= 0 and TT4 <= 0.146 and T3 >= 0.0208 | 2 | 0.010268 |
|  | 3 | 0.999833 |


# Text representation of classifiers as-is

## JRip

Decision list:

rules | predicted class
---|---
(FTI <= 0.064) and (TSH >= 0.0062)|1 (165.0/16.0)
(TSH >= 0.0061) and (On_thyroxine <= 0) and (T3 <= 0.02) and (Thyroid_surgery <= 0) and (TT4 <= 0.146)|2 (259.0/1.0)
(TSH >= 0.0061) and (On_thyroxine <= 0) and (TT4 <= 0.146) and (T3 >= 0.0208)|2 (76.0/5.0)
|3 (5979.0/1.0)


## PART

Decision list:

rules | predicted class
---|---
TSH <= 0.006|3 (5841.0)
FTI <= 0.064 AND T3 <= 0.011|1 (115.0/2.0)
FTI <= 0.064 AND TSH > 0.017|1 (38.0/6.0)
On_thyroxine <= 0.0 AND TT4 <= 0.15 AND FTI > 0.06548|2 (347.0/21.0)
|3 (138.0/8.0)


## SimpleCart Decision Tree

* TSH < 0.00605: 3(5841.0/0.0)
* TSH >= 0.00605
	* FTI < 0.064255
		* T3 < 0.0265
			* Thyroid_surgery < 0.5
				* On_antithyroid_medication < 0.5
					* TSH < 0.009545000000000001
						* TT4 < 0.0595: 1(9.0/0.0)
						* TT4 >= 0.0595: 3(3.0/0.0)
					* TSH >= 0.009545000000000001
						* I131_treatment < 0.5: 1(132.0/0.0)
						* I131_treatment >= 0.5: 1(5.0/2.0)
				* On_antithyroid_medication >= 0.5: 3(2.0/1.0)
			* Thyroid_surgery >= 0.5
				* T3 < 0.0108: 1(2.0/1.0)
				* T3 >= 0.0108: 3(3.0/0.0)
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


