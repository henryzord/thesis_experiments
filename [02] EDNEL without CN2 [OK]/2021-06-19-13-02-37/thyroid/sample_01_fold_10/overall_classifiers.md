# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| TSH <= 0.006 | 3 | 0.924221 |
| TSH >= 0.00605 and FTI >= 0.064255 and On_thyroxine < 0.5 and TT4 < 0.1505 and Thyroid_surgery < 0.5 and TT4 >= 0.058499999999999996 and T3 < 0.028999999999999998 | 2 | 0.049026 |
| TSH >= 0.00605 and FTI < 0.064255 | 1 | 0.021068 |
| TSH >= 0.00605 and FTI >= 0.064255 and On_thyroxine >= 0.5 | 3 | 0.169844 |
| TSH > 0.006 and FTI > 0.064 and On_thyroxine <= 0 and TT4 > 0.15 | 3 | 0.045817 |
| TSH >= 0.00605 and FTI >= 0.064255 and On_thyroxine < 0.5 and TT4 < 0.1505 and Thyroid_surgery >= 0.5 | 3 | 0.020450 |
| TSH >= 0.00605 and FTI >= 0.064255 and On_thyroxine < 0.5 and TT4 < 0.1505 and Thyroid_surgery < 0.5 and TT4 >= 0.058499999999999996 and T3 >= 0.028999999999999998 and T4U < 0.11649999999999999 | 3 | 0.012371 |
| TSH > 0.006 and FTI <= 0.064 and Thyroid_surgery <= 0 and T3 > 0.023 and T3 > 0.026 | 3 | 0.010331 |
| TSH > 0.006 and FTI > 0.064 and On_thyroxine <= 0 and TT4 <= 0.15 and TT4 > 0.061 and T3 > 0.028 and T4U > 0.116 | 2 | 0.001137 |
| TSH >= 0.00605 and FTI >= 0.064255 and On_thyroxine < 0.5 and TT4 < 0.1505 and Thyroid_surgery < 0.5 and TT4 < 0.058499999999999996 | 3 | 0.006818 |
| TSH > 0.006 and FTI > 0.064 and On_thyroxine <= 0 and TT4 <= 0.15 and TT4 <= 0.061 and T3 <= 0.019 and T3 <= 0.013 | 2 | 0.000677 |
| TSH > 0.006 and FTI > 0.064 and On_thyroxine <= 0 and TT4 <= 0.15 and TT4 <= 0.061 and T3 <= 0.019 and T3 > 0.013 | 2 | 0.000812 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| TSH <= 0.00605 | 3 | 0.924221 |
| FTI <= 0.064255 and Thyroid_surgery <= 0.5 and T3 <= 0.0235 and I131_treatment <= 0.5 and Sex <= 0.5 and Query_hypothyroid <= 0.5 and On_thyroxine <= 0.5 and Query_hyperthyroid <= 0.5 and TSH > 0.016895 | 1 | 0.114338 |
| FTI <= 0.064255 and T3 <= 0.0265 and Thyroid_surgery <= 0.5 and I131_treatment <= 0.5 and TSH > 0.017395 | 1 | 0.111111 |
| FTI > 0.06472 and On_thyroxine <= 0.5 and TT4 <= 0.1505 and TT4 > 0.0615 and T3 <= 0.028999999999999998 and Age > 0.425 and Sex <= 0.5 and Query_hypothyroid <= 0.5 and Query_hyperthyroid <= 0.5 and Sick <= 0.5 | 2 | 0.417292 |
| FTI <= 0.064255 and T3 <= 0.011 and T3 > 0.008799999999999999 | 1 | 0.035326 |
| On_thyroxine > 0.5 and Query_hypothyroid <= 0.5 and Sex <= 0.5 | 3 | 0.208400 |
| FTI > 0.06472 and On_thyroxine <= 0.5 and TT4 <= 0.1505 and Thyroid_surgery <= 0.5 and TT4 > 0.058499999999999996 and T3 <= 0.028999999999999998 | 2 | 0.617468 |
| FTI > 0.064255 and On_thyroxine > 0.5 | 3 | 0.641791 |
| FTI > 0.0645 and TT4 > 0.1435 | 3 | 0.510204 |
| TT4 <= 0.1245 and FTI > 0.0645 and T3 > 0.016 | 3 | 0.414634 |
| FTI > 0.0645 and T3 > 0.0225 | 2 | 0.194444 |
| FTI > 0.0645 and T3 <= 0.012 | 2 | 0.100000 |
| Thyroid_surgery <= 0.5 and T4U > 0.0965 and TT4 <= 0.0645 | 3 | 0.350000 |
| Thyroid_surgery > 0.5 | 3 | 0.285714 |
| FTI <= 0.06 and TSH <= 0.00909 | 1 | 0.500000 |
| Age > 0.56 | 1 | 0.300000 |
|  | 1 | 0.444444 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| FTI <= 0.064 and TSH >= 0.0062 | 1 | 0.021068 |
| TSH >= 0.0061 and On_thyroxine <= 0 and T3 <= 0.019 and Thyroid_surgery <= 0 | 2 | 0.037722 |
| TSH >= 0.0061 and On_thyroxine <= 0 and TT4 <= 0.141 and T4U >= 0.089 and Thyroid_surgery <= 0 | 2 | 0.012070 |
| TSH >= 0.0067 and On_thyroxine <= 0 and TT4 <= 0.103 and Thyroid_surgery <= 0 and TT4 >= 0.062 | 2 | 0.000296 |
|  | 3 | 0.999833 |


# Text representation of classifiers as-is

## JRip

Decision list:

rules | predicted class
---|---
(FTI <= 0.064) and (TSH >= 0.0062)|1 (163.0/14.0)
(TSH >= 0.0061) and (On_thyroxine <= 0) and (T3 <= 0.019) and (Thyroid_surgery <= 0)|2 (245.0/3.0)
(TSH >= 0.0061) and (On_thyroxine <= 0) and (TT4 <= 0.141) and (T4U >= 0.089) and (Thyroid_surgery <= 0)|2 (86.0/3.0)
(TSH >= 0.0067) and (On_thyroxine <= 0) and (TT4 <= 0.103) and (Thyroid_surgery <= 0) and (TT4 >= 0.062)|2 (4.0/0.0)
|3 (5981.0/1.0)


## PART

Decision list:

rules | predicted class
---|---
TSH <= 0.00605|3 (5842.0)
FTI <= 0.064255 AND Thyroid_surgery <= 0.5 AND T3 <= 0.0235 AND I131_treatment <= 0.5 AND Sex <= 0.5 AND Query_hypothyroid <= 0.5 AND On_thyroxine <= 0.5 AND Query_hyperthyroid <= 0.5 AND TSH > 0.016895|1 (63.0)
FTI <= 0.064255 AND T3 <= 0.0265 AND Thyroid_surgery <= 0.5 AND I131_treatment <= 0.5 AND TSH > 0.017395|1 (61.0)
FTI > 0.06472 AND On_thyroxine <= 0.5 AND TT4 <= 0.1505 AND TT4 > 0.0615 AND T3 <= 0.028999999999999998 AND Age > 0.425 AND Sex <= 0.5 AND Query_hypothyroid <= 0.5 AND Query_hyperthyroid <= 0.5 AND Sick <= 0.5|2 (135.0/2.0)
FTI <= 0.064255 AND T3 <= 0.011 AND T3 > 0.008799999999999999|1 (13.0)
On_thyroxine > 0.5 AND Query_hypothyroid <= 0.5 AND Sex <= 0.5|3 (57.0/1.0)
FTI > 0.06472 AND On_thyroxine <= 0.5 AND TT4 <= 0.1505 AND Thyroid_surgery <= 0.5 AND TT4 > 0.058499999999999996 AND T3 <= 0.028999999999999998|2 (185.0)
FTI > 0.064255 AND On_thyroxine > 0.5|3 (43.0)
FTI > 0.0645 AND TT4 > 0.1435|3 (24.0)
TT4 <= 0.1245 AND FTI > 0.0645 AND T3 > 0.016|3 (16.0)
FTI > 0.0645 AND T3 > 0.0225|2 (7.0)
FTI > 0.0645 AND T3 <= 0.012|2 (5.0/1.0)
Thyroid_surgery <= 0.5 AND T4U > 0.0965 AND TT4 <= 0.0645|3 (7.0)
Thyroid_surgery > 0.5|3 (7.0/1.0)
FTI <= 0.06 AND TSH <= 0.00909|1 (5.0)
Age > 0.56|1 (5.0/2.0)
|1 (4.0/2.0)


## J48 Decision Tree

* TSH <= 0.006: 3 (5842.0)
* TSH > 0.006
	* FTI <= 0.064
		* Thyroid_surgery <= 0
			* T3 <= 0.023
				* I131_treatment <= 0
					* Sex <= 0
						* Query_hypothyroid <= 0
							* On_thyroxine <= 0
								* Query_hyperthyroid <= 0
									* TSH <= 0.01679
										* Age <= 0.58: 1 (5.0/2.0)
										* Age > 0.58: 1 (6.0)
									* TSH > 0.01679: 1 (63.0)
								* Query_hyperthyroid > 0: 1 (7.0)
							* On_thyroxine > 0: 1 (11.0)
						* Query_hypothyroid > 0: 1 (19.0)
					* Sex > 0: 1 (24.0)
				* I131_treatment > 0: 1 (7.0/2.0)
			* T3 > 0.023
				* T3 <= 0.026: 1 (9.0/2.0)
				* T3 > 0.026: 3 (5.0)
		* Thyroid_surgery > 0: 1 (7.0/3.0)
	* FTI > 0.064
		* On_thyroxine <= 0
			* TT4 <= 0.15
				* TT4 <= 0.061
					* T3 <= 0.019
						* T3 <= 0.013: 2 (6.0/1.0)
						* T3 > 0.013: 2 (5.0)
					* T3 > 0.019: 3 (6.0)
				* TT4 > 0.061
					* T3 <= 0.028
						* Age <= 0.42
							* Thyroid_surgery <= 0: 2 (77.0)
							* Thyroid_surgery > 0: 3 (9.0)
						* Age > 0.42
							* Sex <= 0
								* Query_hypothyroid <= 0
									* Query_hyperthyroid <= 0
										* Sick <= 0: 2 (135.0/2.0)
										* Sick > 0: 2 (5.0)
									* Query_hyperthyroid > 0: 2 (12.0)
								* Query_hypothyroid > 0: 2 (31.0)
							* Sex > 0: 2 (55.0)
					* T3 > 0.028
						* T4U <= 0.116: 3 (5.0)
						* T4U > 0.116: 2 (7.0)
			* TT4 > 0.15: 3 (23.0)
		* On_thyroxine > 0: 3 (98.0)


## SimpleCart Decision Tree

* TSH < 0.00605: 3(5842.0/0.0)
* TSH >= 0.00605
	* FTI < 0.064255: 1(149.0/14.0)
	* FTI >= 0.064255
		* On_thyroxine < 0.5
			* TT4 < 0.1505
				* Thyroid_surgery < 0.5
					* TT4 < 0.058499999999999996: 3(6.0/5.0)
					* TT4 >= 0.058499999999999996
						* T3 < 0.028999999999999998: 2(318.0/1.0)
						* T3 >= 0.028999999999999998
							* T4U < 0.11649999999999999: 3(6.0/0.0)
							* T4U >= 0.11649999999999999: 2(7.0/0.0)
				* Thyroid_surgery >= 0.5: 3(10.0/0.0)
			* TT4 >= 0.1505: 3(23.0/0.0)
		* On_thyroxine >= 0.5: 3(98.0/0.0)


