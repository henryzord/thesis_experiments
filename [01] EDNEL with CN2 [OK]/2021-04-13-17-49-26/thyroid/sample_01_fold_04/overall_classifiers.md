# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| TSH < 0.00605 | 3 | 0.924293 |
| TSH >= 0.00605 and FTI >= 0.064255 and On_thyroxine < 0.5 and TT4 < 0.1505 and Thyroid_surgery < 0.5 and TT4 >= 0.054 and T3 < 0.0295 | 2 | 0.049322 |
| TSH >= 0.00605 and FTI < 0.064255 | 1 | 0.020942 |
| TSH > 0.006 and FTI > 0.064 and On_thyroxine > 0.0 | 3 | 0.164049 |
| TSH >= 0.00605 and FTI >= 0.064255 and On_thyroxine < 0.5 and TT4 >= 0.1505 | 3 | 0.038153 |
| TSH >= 0.00605 and FTI >= 0.064255 and On_thyroxine < 0.5 and TT4 < 0.1505 and Thyroid_surgery >= 0.5 | 3 | 0.022449 |
| TSH >= 0.00605 and FTI >= 0.064255 and On_thyroxine < 0.5 and TT4 < 0.1505 and Thyroid_surgery < 0.5 and TT4 >= 0.054 and T3 >= 0.0295 and T4U < 0.113 | 3 | 0.012371 |
| TSH > 0.006 and FTI <= 0.064 and Thyroid_surgery <= 0.0 and T3 > 0.023 and T3 > 0.026 | 3 | 0.010331 |
| TSH > 0.006 and FTI > 0.064 and On_thyroxine <= 0.0 and TT4 <= 0.15 and TT4 <= 0.061 and T3 > 0.019 | 3 | 0.012371 |
| TSH >= 0.00605 and FTI >= 0.064255 and On_thyroxine < 0.5 and TT4 < 0.1505 and Thyroid_surgery < 0.5 and TT4 >= 0.054 and T3 >= 0.0295 and T4U >= 0.113 | 2 | 0.001299 |
| TSH > 0.006 and FTI <= 0.064 and Thyroid_surgery > 0.0 and T3 > 0.01 | 3 | 0.004678 |
| TSH >= 0.00605 and FTI >= 0.064255 and On_thyroxine < 0.5 and TT4 < 0.1505 and Thyroid_surgery < 0.5 and TT4 < 0.054 | 3 | 0.008627 |
| TSH > 0.006 and FTI > 0.064 and On_thyroxine <= 0.0 and TT4 <= 0.15 and TT4 <= 0.061 and T3 <= 0.019 | 2 | 0.000836 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| TSH <= 0.00605 | 3 | 0.924293 |
| FTI > 0.064255 and On_thyroxine <= 0.5 and TT4 <= 0.1515 and T3 <= 0.0195 | 2 | 0.438705 |
| FTI <= 0.064255 | 1 | 0.360992 |
| On_thyroxine > 0.5 | 3 | 0.521505 |
| TT4 <= 0.1515 and Thyroid_surgery <= 0.5 and T4U > 0.0965 | 2 | 0.522706 |
| TT4 > 0.11149999999999999 | 3 | 0.521739 |
| T3 > 0.0207 | 2 | 0.303940 |
|  | 3 | 0.885714 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| FTI <= 0.064 and TSH >= 0.0097 and T3 <= 0.011 and Thyroid_surgery <= 0 | 1 | 0.016164 |
| FTI <= 0.064 and TSH >= 0.018 and TT4 >= 0.038 | 1 | 0.003777 |
| FTI <= 0.061 and TSH >= 0.0062 and T3 <= 0.02 and T4U <= 0.119 | 1 | 0.002124 |
| TSH >= 0.0061 and On_thyroxine <= 0 and T3 <= 0.02 and Thyroid_surgery <= 0 and T4U <= 0.13 and T3 >= 0.012 | 2 | 0.034258 |
| TSH >= 0.0061 and On_thyroxine <= 0 and TT4 <= 0.142 and TT4 >= 0.072 and Thyroid_surgery <= 0 and T3 <= 0.03 and FTI >= 0.066 | 2 | 0.016541 |
|  | 3 | 0.996843 |


# Text representation of classifiers as-is

## JRip

Decision list:

rules | predicted class
---|---
(FTI <= 0.064) and (TSH >= 0.0097) and (T3 <= 0.011) and (Thyroid_surgery <= 0)|1 (104.0/0.0)
(FTI <= 0.064) and (TSH >= 0.018) and (TT4 >= 0.038)|1 (24.0/0.0)
(FTI <= 0.061) and (TSH >= 0.0062) and (T3 <= 0.02) and (T4U <= 0.119)|1 (19.0/3.0)
(TSH >= 0.0061) and (On_thyroxine <= 0) and (T3 <= 0.02) and (Thyroid_surgery <= 0) and (T4U <= 0.13) and (T3 >= 0.012)|2 (215.0/0.0)
(TSH >= 0.0061) and (On_thyroxine <= 0) and (TT4 <= 0.142) and (TT4 >= 0.072) and (Thyroid_surgery <= 0) and (T3 <= 0.03) and (FTI >= 0.066)|2 (101.0/0.0)
|3 (6016.0/19.0)


## PART

Decision list:

rules | predicted class
---|---
TSH <= 0.00605|3 (4684.0)
FTI > 0.064255 AND On_thyroxine <= 0.5 AND TT4 <= 0.1515 AND T3 <= 0.0195|2 (198.0/3.0)
FTI <= 0.064255|1 (131.0/11.0)
On_thyroxine > 0.5|3 (74.0)
TT4 <= 0.1515 AND Thyroid_surgery <= 0.5 AND T4U > 0.0965|2 (50.0)
TT4 > 0.11149999999999999|3 (19.0)
T3 > 0.0207|2 (18.0/2.0)
|3 (10.0/3.0)


## J48 Decision Tree

* TSH <= 0.006: 3 (5848.0)
* TSH > 0.006
	* FTI <= 0.064
		* Thyroid_surgery <= 0.0
			* T3 <= 0.023
				* I131_treatment <= 0.0
					* TSH <= 0.01679: 1 (16.0/3.0)
					* TSH > 0.01679: 1 (121.0)
				* I131_treatment > 0.0: 1 (5.0/1.0)
			* T3 > 0.023
				* T3 <= 0.026
					* T3 <= 0.024: 1 (5.0/2.0)
					* T3 > 0.024: 1 (4.0)
				* T3 > 0.026: 3 (5.0)
		* Thyroid_surgery > 0.0
			* T3 <= 0.01: 1 (4.0/1.0)
			* T3 > 0.01: 3 (4.0/1.0)
	* FTI > 0.064
		* On_thyroxine <= 0.0
			* TT4 <= 0.15
				* TT4 <= 0.061
					* T3 <= 0.019: 2 (7.0/1.0)
					* T3 > 0.019: 3 (6.0)
				* TT4 > 0.061
					* T3 <= 0.03
						* Thyroid_surgery <= 0.0
							* Sex <= 0.0
								* Query_hypothyroid <= 0.0
									* Query_hyperthyroid <= 0.0
										* Sick <= 0.0: 2 (192.0/1.0)
										* Sick > 0.0: 2 (8.0)
									* Query_hyperthyroid > 0.0: 2 (13.0)
								* Query_hypothyroid > 0.0: 2 (34.0)
							* Sex > 0.0: 2 (71.0)
						* Thyroid_surgery > 0.0: 3 (11.0)
					* T3 > 0.03
						* T4U <= 0.113: 3 (5.0)
						* T4U > 0.113: 2 (7.0)
			* TT4 > 0.15: 3 (19.0)
		* On_thyroxine > 0.0: 3 (94.0)


## SimpleCart Decision Tree

* TSH < 0.00605: 3(5848.0/0.0)
* TSH >= 0.00605
	* FTI < 0.064255: 1(149.0/15.0)
	* FTI >= 0.064255
		* On_thyroxine < 0.5
			* TT4 < 0.1505
				* Thyroid_surgery < 0.5
					* TT4 < 0.054: 3(5.0/1.0)
					* TT4 >= 0.054
						* T3 < 0.0295: 2(321.0/2.0)
						* T3 >= 0.0295
							* T4U < 0.113: 3(6.0/0.0)
							* T4U >= 0.113: 2(8.0/0.0)
				* Thyroid_surgery >= 0.5: 3(11.0/0.0)
			* TT4 >= 0.1505: 3(19.0/0.0)
		* On_thyroxine >= 0.5: 3(94.0/0.0)


