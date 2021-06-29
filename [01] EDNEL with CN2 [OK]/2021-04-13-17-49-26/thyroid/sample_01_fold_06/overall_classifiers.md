# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| TSH <= 0.00605 | 3 | 0.924319 |
| TSH >= 0.00605 and FTI >= 0.064255 and On_thyroxine < 0.5 and TT4 < 0.1505 and Thyroid_surgery < 0.5 | 2 | 0.048665 |
| TSH > 0.00605 and FTI <= 0.0645 | 1 | 0.021224 |
| TSH >= 0.00605 and FTI >= 0.064255 and On_thyroxine >= 0.5 | 3 | 0.173010 |
| TSH >= 0.00605 and FTI >= 0.064255 and On_thyroxine < 0.5 and TT4 < 0.1505 and Thyroid_surgery >= 0.5 | 3 | 0.018480 |
| TSH > 0.00605 and FTI > 0.0645 and On_thyroxine <= 0.5 and TT4 > 0.152 | 3 | 0.045908 |
| TSH >= 0.00605 and FTI >= 0.064255 and On_thyroxine < 0.5 and TT4 >= 0.1505 | 3 | 0.049702 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| TSH <= 0.006 | 3 | 0.924319 |
| FTI <= 0.064 and T3 <= 0.011 and T4U <= 0.111 | 1 | 0.143357 |
| FTI <= 0.064 and TSH > 0.017 and Age <= 0.67 and Age > 0.18 and T3 > 0.006 | 1 | 0.068441 |
| FTI > 0.06451 and On_thyroxine <= 0.0 and TT4 <= 0.15 and TT4 > 0.061 and T3 <= 0.028 and Age > 0.42 and TT4 <= 0.133 and T4U <= 0.124 | 2 | 0.530266 |
| FTI <= 0.064 and T3 <= 0.011 and TT4 <= 0.019 | 1 | 0.045775 |
| FTI > 0.064 and On_thyroxine > 0.0 | 3 | 0.438596 |
| FTI > 0.064 and TT4 <= 0.15 and Thyroid_surgery <= 0.0 and TT4 > 0.058 and T3 <= 0.029 and Age <= 0.7 | 2 | 0.531792 |
| FTI > 0.064 and TT4 > 0.149 | 3 | 0.409836 |
| FTI <= 0.064 and T3 <= 0.02 and FTI <= 0.049 | 1 | 0.077576 |
| FTI <= 0.064 and T3 <= 0.02 | 1 | 0.090402 |
| TT4 > 0.127 | 2 | 0.193910 |
| T3 > 0.016 and FTI > 0.065 and TSH <= 0.012 | 3 | 0.619048 |
| Age > 0.515 | 3 | 0.555556 |
|  | 3 | 0.636364 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| FTI <= 0.064 and TSH >= 0.0062 and T3 <= 0.011 | 1 | 0.017240 |
| FTI <= 0.064 and TSH >= 0.0077 and FTI >= 0.054 | 1 | 0.002531 |
| FTI <= 0.054 and TSH >= 0.02 and Age <= 0.65 and Thyroid_surgery <= 0 | 1 | 0.002994 |
| TSH >= 0.0061 and On_thyroxine <= 0 and T3 <= 0.02 and Thyroid_surgery <= 0 and TT4 >= 0.051 and TT4 <= 0.148 | 2 | 0.039834 |
| TSH >= 0.0061 and T3 >= 0.0208 and TT4 <= 0.15 and On_thyroxine <= 0 and Age <= 0.76 | 2 | 0.011601 |
|  | 3 | 0.999167 |


# Text representation of classifiers as-is

## JRip

Decision list:

rules | predicted class
---|---
(FTI <= 0.064) and (TSH >= 0.0062) and (T3 <= 0.011)|1 (113.0/1.0)
(FTI <= 0.064) and (TSH >= 0.0077) and (FTI >= 0.054)|1 (18.0/1.0)
(FTI <= 0.054) and (TSH >= 0.02) and (Age <= 0.65) and (Thyroid_surgery <= 0)|1 (19.0/0.0)
(TSH >= 0.0061) and (On_thyroxine <= 0) and (T3 <= 0.02) and (Thyroid_surgery <= 0) and (TT4 >= 0.051) and (TT4 <= 0.148)|2 (249.0/0.0)
(TSH >= 0.0061) and (T3 >= 0.0208) and (TT4 <= 0.15) and (On_thyroxine <= 0) and (Age <= 0.76)|2 (81.0/5.0)
|3 (5998.0/5.0)


## PART

Decision list:

rules | predicted class
---|---
TSH <= 0.006|3 (5838.0)
FTI <= 0.064 AND T3 <= 0.011 AND T4U <= 0.111|1 (82.0)
FTI <= 0.064 AND TSH > 0.017 AND Age <= 0.67 AND Age > 0.18 AND T3 > 0.006|1 (36.0)
FTI > 0.06451 AND On_thyroxine <= 0.0 AND TT4 <= 0.15 AND TT4 > 0.061 AND T3 <= 0.028 AND Age > 0.42 AND TT4 <= 0.133 AND T4U <= 0.124|2 (219.0)
FTI <= 0.064 AND T3 <= 0.011 AND TT4 <= 0.019|1 (13.0)
FTI > 0.064 AND On_thyroxine > 0.0|3 (100.0)
FTI > 0.064 AND TT4 <= 0.15 AND Thyroid_surgery <= 0.0 AND TT4 > 0.058 AND T3 <= 0.029 AND Age <= 0.7|2 (92.0)
FTI > 0.064 AND TT4 > 0.149|3 (25.0)
FTI <= 0.064 AND T3 <= 0.02 AND FTI <= 0.049|1 (15.0/7.0)
FTI <= 0.064 AND T3 <= 0.02|1 (9.0)
TT4 > 0.127|2 (13.0/2.0)
T3 > 0.016 AND FTI > 0.065 AND TSH <= 0.012|3 (11.0)
Age > 0.515|3 (15.0/8.0)
|3 (10.0)


## J48 Decision Tree

* TSH <= 0.00605: 3 (2922.0)
* TSH > 0.00605
	* FTI <= 0.0645: 1 (80.0/5.0)
	* FTI > 0.0645
		* On_thyroxine <= 0.5
			* TT4 <= 0.152: 2 (174.0/10.0)
			* TT4 > 0.152: 3 (9.0)
		* On_thyroxine > 0.5: 3 (54.0)


## SimpleCart Decision Tree

* TSH < 0.00605: 3(5838.0/0.0)
* TSH >= 0.00605
	* FTI < 0.064255: 1(150.0/14.0)
	* FTI >= 0.064255
		* On_thyroxine < 0.5
			* TT4 < 0.1505
				* Thyroid_surgery < 0.5: 2(328.0/14.0)
				* Thyroid_surgery >= 0.5: 3(9.0/0.0)
			* TT4 >= 0.1505: 3(25.0/0.0)
		* On_thyroxine >= 0.5: 3(100.0/0.0)


