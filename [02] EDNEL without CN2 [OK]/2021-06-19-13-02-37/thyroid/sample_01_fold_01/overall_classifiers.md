# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| TSH <= 0.006 | 3 | 0.924221 |
| TSH >= 0.00605 and FTI >= 0.064255 and On_thyroxine < 0.5 and TT4 < 0.1505 and Thyroid_surgery < 0.5 and TT4 >= 0.058499999999999996 and FTI < 0.1625 and T3 < 0.0295 | 2 | 0.049026 |
| TSH >= 0.00605 and FTI < 0.064255 and T3 < 0.0265 and T4U < 0.14100000000000001 | 1 | 0.021826 |
| TSH >= 0.00605 and FTI >= 0.064255 and On_thyroxine >= 0.5 | 3 | 0.171280 |
| TSH > 0.006 and FTI > 0.064 and On_thyroxine <= 0 and TT4 > 0.15 | 3 | 0.045817 |
| TSH >= 0.00605 and FTI >= 0.064255 and On_thyroxine < 0.5 and TT4 < 0.1505 and Thyroid_surgery >= 0.5 | 3 | 0.018443 |
| TSH > 0.006 and FTI <= 0.064 and TSH <= 0.01679 and T4U > 0.096 and Age <= 0.58 | 3 | 0.014403 |
| TSH >= 0.00605 and FTI >= 0.064255 and On_thyroxine < 0.5 and TT4 < 0.1505 and Thyroid_surgery < 0.5 and TT4 < 0.058499999999999996 and T3 >= 0.01755 | 3 | 0.012371 |
| TSH > 0.006 and FTI > 0.064 and On_thyroxine <= 0 and TT4 <= 0.15 and TT4 > 0.058 and T3 > 0.029 and T4U > 0.113 | 2 | 0.001299 |
| TSH > 0.006 and FTI > 0.064 and On_thyroxine <= 0 and TT4 <= 0.15 and TT4 > 0.058 and T3 > 0.029 and T4U <= 0.113 | 3 | 0.010331 |
| TSH > 0.006 and FTI > 0.064 and On_thyroxine <= 0 and TT4 <= 0.15 and TT4 <= 0.058 and T3 <= 0.0174 | 2 | 0.000677 |
| TSH >= 0.00605 and FTI < 0.064255 and T3 < 0.0265 and T4U >= 0.14100000000000001 and Thyroid_surgery >= 0.5 | 3 | 0.006224 |
| TSH >= 0.00605 and FTI < 0.064255 and T3 >= 0.0265 | 3 | 0.010331 |
| TSH >= 0.00605 and FTI >= 0.064255 and On_thyroxine < 0.5 and TT4 < 0.1505 and Thyroid_surgery < 0.5 and TT4 >= 0.058499999999999996 and FTI >= 0.1625 | 3 | 0.004158 |
| TSH >= 0.00605 and FTI < 0.064255 and T3 < 0.0265 and T4U >= 0.14100000000000001 and Thyroid_surgery < 0.5 | 1 | 0.000316 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| TSH <= 0.006 | 3 | 0.924221 |
| FTI > 0.064 and On_thyroxine <= 0 and TT4 <= 0.152 and T3 <= 0.029 and TT4 > 0.061 and Age > 0.37 | 2 | 0.447954 |
| FTI <= 0.064 | 1 | 0.368115 |
| On_thyroxine > 0 | 3 | 0.569832 |
| TT4 <= 0.152 and Thyroid_surgery <= 0 and Age <= 0.37 | 2 | 0.527361 |
| T3 > 0.019 | 3 | 0.792882 |
|  | 2 | 0.458333 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| FTI <= 0.064 and TSH >= 0.0062 | 1 | 0.021068 |
| TSH >= 0.0061 and On_thyroxine <= 0 and T3 <= 0.02 and Thyroid_surgery <= 0 and TT4 <= 0.148 | 2 | 0.040015 |
| TSH >= 0.0061 and T3 >= 0.0208 and TT4 <= 0.141 and On_thyroxine <= 0 | 2 | 0.010848 |
|  | 3 | 0.999667 |


# Text representation of classifiers as-is

## JRip

Decision list:

rules | predicted class
---|---
(FTI <= 0.064) and (TSH >= 0.0062)|1 (163.0/14.0)
(TSH >= 0.0061) and (On_thyroxine <= 0) and (T3 <= 0.02) and (Thyroid_surgery <= 0) and (TT4 <= 0.148)|2 (256.0/1.0)
(TSH >= 0.0061) and (T3 >= 0.0208) and (TT4 <= 0.141) and (On_thyroxine <= 0)|2 (77.0/4.0)
|3 (5983.0/2.0)


## PART

Decision list:

rules | predicted class
---|---
TSH <= 0.006|3 (4386.0)
FTI > 0.064 AND On_thyroxine <= 0 AND TT4 <= 0.152 AND T3 <= 0.029 AND TT4 > 0.061 AND Age > 0.37|2 (189.0/1.0)
FTI <= 0.064|1 (122.0/10.0)
On_thyroxine > 0|3 (76.0)
TT4 <= 0.152 AND Thyroid_surgery <= 0 AND Age <= 0.37|2 (53.0)
T3 > 0.019|3 (23.0)
|2 (11.0/4.0)


## J48 Decision Tree

* TSH <= 0.006: 3 (5842.0)
* TSH > 0.006
	* FTI <= 0.064
		* TSH <= 0.01679
			* T4U <= 0.096: 1 (8.0)
			* T4U > 0.096
				* Age <= 0.58: 3 (7.0)
				* Age > 0.58: 1 (5.0/1.0)
		* TSH > 0.01679: 1 (143.0/6.0)
	* FTI > 0.064
		* On_thyroxine <= 0
			* TT4 <= 0.15
				* TT4 <= 0.058
					* T3 <= 0.0174: 2 (6.0/1.0)
					* T3 > 0.0174: 3 (6.0)
				* TT4 > 0.058
					* T3 <= 0.029
						* Age <= 0.42
							* Thyroid_surgery <= 0: 2 (76.0)
							* Thyroid_surgery > 0: 3 (8.0)
						* Age > 0.42: 2 (243.0/2.0)
					* T3 > 0.029
						* T4U <= 0.113: 3 (5.0)
						* T4U > 0.113: 2 (8.0)
			* TT4 > 0.15: 3 (23.0)
		* On_thyroxine > 0: 3 (99.0)


## SimpleCart Decision Tree

* TSH < 0.00605: 3(5842.0/0.0)
* TSH >= 0.00605
	* FTI < 0.064255
		* T3 < 0.0265
			* T4U < 0.14100000000000001: 1(147.0/6.0)
			* T4U >= 0.14100000000000001
				* Thyroid_surgery < 0.5: 1(2.0/0.0)
				* Thyroid_surgery >= 0.5: 3(3.0/0.0)
		* T3 >= 0.0265: 3(5.0/0.0)
	* FTI >= 0.064255
		* On_thyroxine < 0.5
			* TT4 < 0.1505
				* Thyroid_surgery < 0.5
					* TT4 < 0.058499999999999996
						* T3 < 0.01755: 2(5.0/1.0)
						* T3 >= 0.01755: 3(6.0/0.0)
					* TT4 >= 0.058499999999999996
						* FTI < 0.1625
							* T3 < 0.0295: 2(317.0/0.0)
							* T3 >= 0.0295
								* T4U < 0.113: 3(4.0/0.0)
								* T4U >= 0.113: 2(8.0/0.0)
						* FTI >= 0.1625: 3(2.0/0.0)
				* Thyroid_surgery >= 0.5: 3(9.0/0.0)
			* TT4 >= 0.1505: 3(23.0/0.0)
		* On_thyroxine >= 0.5: 3(99.0/0.0)


