# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| TSH <= 0.00605 | 3 | 0.924003 |
| TSH >= 0.00605 and FTI >= 0.064255 and On_thyroxine < 0.5 and TT4 < 0.1505 and Thyroid_surgery < 0.5 and TT4 >= 0.058499999999999996 and T3 < 0.0305 | 2 | 0.049165 |
| TSH >= 0.00605 and FTI < 0.064255 | 1 | 0.021218 |
| TSH > 0.00605 and FTI > 0.064255 and On_thyroxine > 0.5 | 3 | 0.178082 |
| TSH >= 0.00605 and FTI >= 0.064255 and On_thyroxine < 0.5 and TT4 >= 0.1505 | 3 | 0.049505 |
| TSH >= 0.00605 and FTI >= 0.064255 and On_thyroxine < 0.5 and TT4 < 0.1505 and Thyroid_surgery >= 0.5 | 3 | 0.018405 |
| TSH > 0.00605 and FTI > 0.064255 and On_thyroxine <= 0.5 and TT4 <= 0.1505 and TT4 <= 0.058499999999999996 and T3 > 0.01755 | 3 | 0.012346 |
| TSH > 0.00605 and FTI <= 0.064255 and T3 > 0.0235 and TSH <= 0.017 | 3 | 0.008609 |
| Age = all and Sex <= 0.5 and On_thyroxine <= 0.5 and Sick = all and Pregnant <= 0.5 and Thyroid_surgery <= 0.5 and I131_treatment = all and Goitre <= 0.5 and Tumor = all and TSH > 0.00605 and TSH <= 0.0195 | 2 | 0.028169 |
| TSH > 0.00605 and FTI > 0.064255 and On_thyroxine <= 0.5 and TT4 <= 0.1505 and TT4 > 0.058499999999999996 and T3 > 0.0305 and Age > 0.37 | 3 | 0.008609 |
| Age = all and Sex <= 0.5 and On_thyroxine <= 0.5 and Sick = all and Pregnant <= 0.5 and Thyroid_surgery > 0.5 and I131_treatment = all and Goitre <= 0.5 and Tumor = all and TSH > 0.00605 and TSH <= 0.0195 | 3 | 0.018405 |
| TSH >= 0.00605 and FTI >= 0.064255 and On_thyroxine < 0.5 and TT4 < 0.1505 and Thyroid_surgery < 0.5 and TT4 < 0.058499999999999996 | 3 | 0.008472 |
| Age = all and Sex <= 0.5 and On_thyroxine > 0.5 and Sick = all and Pregnant <= 0.5 and Thyroid_surgery <= 0.5 and I131_treatment = all and Goitre <= 0.5 and Tumor = all and TSH > 0.00605 and TSH <= 0.0195 | 3 | 0.101157 |
| TSH > 0.00605 and FTI > 0.064255 and On_thyroxine <= 0.5 and TT4 <= 0.1505 and TT4 <= 0.058499999999999996 and T3 <= 0.01755 | 2 | 0.000677 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| TSH <= 0.00605 | 3 | 0.924003 |
| FTI <= 0.064255 and Thyroid_surgery <= 0.5 and T3 <= 0.0235 and I131_treatment <= 0.5 and TSH > 0.009545000000000001 | 1 | 0.203226 |
| FTI > 0.06472 and On_thyroxine <= 0.5 and TT4 <= 0.1505 and TT4 > 0.058499999999999996 and T3 <= 0.0305 and Age > 0.425 | 2 | 0.556604 |
| FTI <= 0.064255 and T4U <= 0.1235 and T3 <= 0.0265 and T4U <= 0.1035 | 1 | 0.054945 |
| FTI > 0.057499999999999996 and On_thyroxine > 0.5 | 3 | 0.502415 |
| FTI > 0.062965 and TT4 <= 0.1505 and Thyroid_surgery <= 0.5 and Age <= 0.56 and T4U > 0.0795 and T3 <= 0.0315 | 2 | 0.540000 |
| FTI > 0.057499999999999996 and TT4 > 0.1485 | 3 | 0.531915 |
| TSH <= 0.0195 and T4U <= 0.1475 and TSH <= 0.0142 and T3 > 0.01875 and Age > 0.255 | 3 | 0.435897 |
| FTI > 0.062 and Thyroid_surgery <= 0.5 and TSH <= 0.009645 | 2 | 0.250000 |
| TSH <= 0.0195 and TSH <= 0.011 | 3 | 0.350000 |
| TSH <= 0.0195 | 2 | 0.121212 |
| T4U > 0.1015 and T3 <= 0.016399999999999998 and T3 <= 0.0108 | 1 | 0.228571 |
| T3 > 0.02045 | 1 | 0.240385 |
|  | 3 | 1.000000 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| FTI <= 0.064 and TSH >= 0.0077 and T3 <= 0.011 and T4U <= 0.111 | 1 | 0.011555 |
| FTI <= 0.064 and TSH >= 0.018 and FTI >= 0.026 and I131_treatment <= 0 | 1 | 0.006123 |
| TSH >= 0.0062 and T3 <= 0.01 and FTI <= 0.018 | 1 | 0.003307 |
| FTI <= 0.064 and TSH >= 0.0062 and T4U <= 0.096 and On_thyroxine <= 0 | 1 | 0.001105 |
| FTI <= 0.06 and TT4 >= 0.068 and TSH >= 0.01 | 1 | 0.000632 |
| FTI <= 0.03249 and TSH >= 0.0067 and T3 >= 0.014 and Age <= 0.59 | 1 | 0.000632 |
| TSH >= 0.0061 and On_thyroxine <= 0 and T3 <= 0.02 and T3 >= 0.014 and Age >= 0.38 | 2 | 0.025020 |
| TSH >= 0.0061 and On_thyroxine <= 0 and TT4 <= 0.142 and TT4 >= 0.067 and Thyroid_surgery <= 0 and T3 <= 0.03 and FTI >= 0.066 | 2 | 0.025337 |
| TSH >= 0.0062 and On_thyroxine <= 0 and TT4 <= 0.15 and TT4 >= 0.126 and Age <= 0.36 | 2 | 0.001165 |
| TSH >= 0.0062 and TT4 <= 0.065 and FTI >= 0.06493 and T3 <= 0.017 and On_thyroxine <= 0 and Age <= 0.78 | 2 | 0.001498 |
|  | 3 | 0.999167 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

age|sex|on_thyroxine|sick|pregnant|thyroid_surgery|i131_treatment|goitre|tumor|tsh|class
---|---|---|---|---|---|---|---|---|---|---
all|(-inf-0.5]|(-inf-0.5]|all|(-inf-0.5]|(0.5-inf)|all|(-inf-0.5]|all|(0.0415-inf)|1
all|(0.5-inf)|(0.5-inf)|all|(-inf-0.5]|(-inf-0.5]|all|(-inf-0.5]|all|(0.0415-inf)|3
all|(-inf-0.5]|(0.5-inf)|all|(-inf-0.5]|(-inf-0.5]|all|(-inf-0.5]|all|(0.0415-inf)|1
all|(0.5-inf)|(-inf-0.5]|all|(-inf-0.5]|(-inf-0.5]|all|(-inf-0.5]|all|(0.0415-inf)|1
all|(-inf-0.5]|(-inf-0.5]|all|(-inf-0.5]|(-inf-0.5]|all|(-inf-0.5]|all|(0.0415-inf)|1
all|(0.5-inf)|(0.5-inf)|all|(-inf-0.5]|(0.5-inf)|all|(-inf-0.5]|all|(0.0195-0.0415]|1
all|(-inf-0.5]|(-inf-0.5]|all|(-inf-0.5]|(0.5-inf)|all|(-inf-0.5]|all|(0.0195-0.0415]|1
all|(0.5-inf)|(0.5-inf)|all|(-inf-0.5]|(-inf-0.5]|all|(-inf-0.5]|all|(0.0195-0.0415]|3
all|(-inf-0.5]|(0.5-inf)|all|(-inf-0.5]|(-inf-0.5]|all|(-inf-0.5]|all|(0.0195-0.0415]|3
all|(0.5-inf)|(-inf-0.5]|all|(-inf-0.5]|(-inf-0.5]|all|(-inf-0.5]|all|(0.0195-0.0415]|2
all|(-inf-0.5]|(-inf-0.5]|all|(-inf-0.5]|(-inf-0.5]|all|(-inf-0.5]|all|(0.0195-0.0415]|2
all|(-inf-0.5]|(-inf-0.5]|all|(-inf-0.5]|(-inf-0.5]|all|(0.5-inf)|all|(0.00605-0.0195]|1
all|(-inf-0.5]|(0.5-inf)|all|(0.5-inf)|(-inf-0.5]|all|(-inf-0.5]|all|(0.00605-0.0195]|1
all|(-inf-0.5]|(-inf-0.5]|all|(-inf-0.5]|(0.5-inf)|all|(-inf-0.5]|all|(0.00605-0.0195]|3
all|(0.5-inf)|(0.5-inf)|all|(-inf-0.5]|(-inf-0.5]|all|(-inf-0.5]|all|(0.00605-0.0195]|3
all|(-inf-0.5]|(-inf-0.5]|all|(0.5-inf)|(-inf-0.5]|all|(0.5-inf)|all|(-inf-0.00605]|3
all|(-inf-0.5]|(0.5-inf)|all|(-inf-0.5]|(-inf-0.5]|all|(-inf-0.5]|all|(0.00605-0.0195]|3
all|(0.5-inf)|(0.5-inf)|all|(-inf-0.5]|(-inf-0.5]|all|(0.5-inf)|all|(-inf-0.00605]|1
all|(0.5-inf)|(-inf-0.5]|all|(-inf-0.5]|(-inf-0.5]|all|(-inf-0.5]|all|(0.00605-0.0195]|2
all|(-inf-0.5]|(0.5-inf)|all|(-inf-0.5]|(-inf-0.5]|all|(0.5-inf)|all|(-inf-0.00605]|3
all|(-inf-0.5]|(-inf-0.5]|all|(-inf-0.5]|(-inf-0.5]|all|(-inf-0.5]|all|(0.00605-0.0195]|2
all|(0.5-inf)|(0.5-inf)|all|(-inf-0.5]|(0.5-inf)|all|(-inf-0.5]|all|(-inf-0.00605]|3
all|(0.5-inf)|(-inf-0.5]|all|(-inf-0.5]|(-inf-0.5]|all|(0.5-inf)|all|(-inf-0.00605]|3
all|(-inf-0.5]|(-inf-0.5]|all|(-inf-0.5]|(-inf-0.5]|all|(0.5-inf)|all|(-inf-0.00605]|3
all|(-inf-0.5]|(0.5-inf)|all|(-inf-0.5]|(0.5-inf)|all|(-inf-0.5]|all|(-inf-0.00605]|3
all|(-inf-0.5]|(0.5-inf)|all|(0.5-inf)|(-inf-0.5]|all|(-inf-0.5]|all|(-inf-0.00605]|3
all|(0.5-inf)|(-inf-0.5]|all|(-inf-0.5]|(0.5-inf)|all|(-inf-0.5]|all|(-inf-0.00605]|3
all|(-inf-0.5]|(-inf-0.5]|all|(-inf-0.5]|(0.5-inf)|all|(-inf-0.5]|all|(-inf-0.00605]|3
all|(-inf-0.5]|(-inf-0.5]|all|(0.5-inf)|(-inf-0.5]|all|(-inf-0.5]|all|(-inf-0.00605]|3
all|(0.5-inf)|(0.5-inf)|all|(-inf-0.5]|(-inf-0.5]|all|(-inf-0.5]|all|(-inf-0.00605]|3
all|(-inf-0.5]|(0.5-inf)|all|(-inf-0.5]|(-inf-0.5]|all|(-inf-0.5]|all|(-inf-0.00605]|3
all|(0.5-inf)|(-inf-0.5]|all|(-inf-0.5]|(-inf-0.5]|all|(-inf-0.5]|all|(-inf-0.00605]|3
all|(-inf-0.5]|(-inf-0.5]|all|(-inf-0.5]|(-inf-0.5]|all|(-inf-0.5]|all|(-inf-0.00605]|3

## JRip

Decision list:

rules | predicted class
---|---
(FTI <= 0.064) and (TSH >= 0.0077) and (T3 <= 0.011) and (T4U <= 0.111)|1 (74.0/0.0)
(FTI <= 0.064) and (TSH >= 0.018) and (FTI >= 0.026) and (I131_treatment <= 0)|1 (39.0/0.0)
(TSH >= 0.0062) and (T3 <= 0.01) and (FTI <= 0.018)|1 (21.0/0.0)
(FTI <= 0.064) and (TSH >= 0.0062) and (T4U <= 0.096) and (On_thyroxine <= 0)|1 (7.0/0.0)
(FTI <= 0.06) and (TT4 >= 0.068) and (TSH >= 0.01)|1 (4.0/0.0)
(FTI <= 0.03249) and (TSH >= 0.0067) and (T3 >= 0.014) and (Age <= 0.59)|1 (4.0/0.0)
(TSH >= 0.0061) and (On_thyroxine <= 0) and (T3 <= 0.02) and (T3 >= 0.014) and (Age >= 0.38)|2 (154.0/0.0)
(TSH >= 0.0061) and (On_thyroxine <= 0) and (TT4 <= 0.142) and (TT4 >= 0.067) and (Thyroid_surgery <= 0) and (T3 <= 0.03) and (FTI >= 0.066)|2 (156.0/0.0)
(TSH >= 0.0062) and (On_thyroxine <= 0) and (TT4 <= 0.15) and (TT4 >= 0.126) and (Age <= 0.36)|2 (7.0/0.0)
(TSH >= 0.0062) and (TT4 <= 0.065) and (FTI >= 0.06493) and (T3 <= 0.017) and (On_thyroxine <= 0) and (Age <= 0.78)|2 (9.0/0.0)
|3 (6005.0/5.0)


## PART

Decision list:

rules | predicted class
---|---
TSH <= 0.00605|3 (5836.0)
FTI <= 0.064255 AND Thyroid_surgery <= 0.5 AND T3 <= 0.0235 AND I131_treatment <= 0.5 AND TSH > 0.009545000000000001|1 (126.0)
FTI > 0.06472 AND On_thyroxine <= 0.5 AND TT4 <= 0.1505 AND TT4 > 0.058499999999999996 AND T3 <= 0.0305 AND Age > 0.425|2 (236.0)
FTI <= 0.064255 AND T4U <= 0.1235 AND T3 <= 0.0265 AND T4U <= 0.1035|1 (15.0)
FTI > 0.057499999999999996 AND On_thyroxine > 0.5|3 (104.0)
FTI > 0.062965 AND TT4 <= 0.1505 AND Thyroid_surgery <= 0.5 AND Age <= 0.56 AND T4U > 0.0795 AND T3 <= 0.0315|2 (81.0)
FTI > 0.057499999999999996 AND TT4 > 0.1485|3 (25.0)
TSH <= 0.0195 AND T4U <= 0.1475 AND TSH <= 0.0142 AND T3 > 0.01875 AND Age > 0.255|3 (17.0)
FTI > 0.062 AND Thyroid_surgery <= 0.5 AND TSH <= 0.009645|2 (9.0)
TSH <= 0.0195 AND TSH <= 0.011|3 (7.0)
TSH <= 0.0195|2 (6.0/2.0)
T4U > 0.1015 AND T3 <= 0.016399999999999998 AND T3 <= 0.0108|1 (5.0/1.0)
T3 > 0.02045|1 (7.0/2.0)
|3 (6.0)


## J48 Decision Tree

* TSH <= 0.00605: 3 (5836.0)
* TSH > 0.00605
	* FTI <= 0.064255
		* T3 <= 0.0235: 1 (151.0/8.0)
		* T3 > 0.0235
			* TSH <= 0.017: 3 (6.0/1.0)
			* TSH > 0.017: 1 (7.0/1.0)
	* FTI > 0.064255
		* On_thyroxine <= 0.5
			* TT4 <= 0.1505
				* TT4 <= 0.058499999999999996
					* T3 <= 0.01755: 2 (6.0/1.0)
					* T3 > 0.01755: 3 (6.0)
				* TT4 > 0.058499999999999996
					* T3 <= 0.0305
						* Age <= 0.425
							* Thyroid_surgery <= 0.5: 2 (82.0)
							* Thyroid_surgery > 0.5: 3 (9.0)
						* Age > 0.425: 2 (236.0)
					* T3 > 0.0305
						* Age <= 0.37: 2 (6.0)
						* Age > 0.37: 3 (6.0/1.0)
			* TT4 > 0.1505: 3 (25.0)
		* On_thyroxine > 0.5: 3 (104.0)


## SimpleCart Decision Tree

* TSH < 0.00605: 3(5836.0/0.0)
* TSH >= 0.00605
	* FTI < 0.064255: 1(150.0/14.0)
	* FTI >= 0.064255
		* On_thyroxine < 0.5
			* TT4 < 0.1505
				* Thyroid_surgery < 0.5
					* TT4 < 0.058499999999999996: 3(7.0/5.0)
					* TT4 >= 0.058499999999999996
						* T3 < 0.0305: 2(318.0/0.0)
						* T3 >= 0.0305: 2(7.0/5.0)
				* Thyroid_surgery >= 0.5: 3(9.0/0.0)
			* TT4 >= 0.1505: 3(25.0/0.0)
		* On_thyroxine >= 0.5: 3(104.0/0.0)


