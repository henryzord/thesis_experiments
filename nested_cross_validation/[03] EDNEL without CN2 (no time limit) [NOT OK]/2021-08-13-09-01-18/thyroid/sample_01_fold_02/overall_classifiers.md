# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 3 | 0.926069 |
| TSH >= 0.00605 and FTI >= 0.064255 and On_thyroxine < 0.5 and TT4 < 0.1505 and Thyroid_surgery < 0.5 | 2 | 0.049238 |
| TSH > 0.00605 and FTI <= 0.064255 and Thyroid_surgery <= 0.5 and T3 > 0.0235 and T3 <= 0.0265 and TSH > 0.01385 | 1 | 0.000789 |
| On_thyroxine <= 0.5 and On_antithyroid_medication = all and Thyroid_surgery > 0.5 and Query_hyperthyroid = all and Hypopituitary = all and TSH > 0.0415 and FTI > 0.013735 and FTI <= 0.064255 | 1 | 0.000053 |
| On_thyroxine <= 0.5 and On_antithyroid_medication = all and Thyroid_surgery <= 0.5 and Query_hyperthyroid = all and Hypopituitary = all and TSH > 0.0415 and FTI > 0.013735 and FTI <= 0.064255 | 1 | 0.006916 |
| On_thyroxine > 0.5 and On_antithyroid_medication = all and Thyroid_surgery <= 0.5 and Query_hyperthyroid = all and Hypopituitary = all and TSH > 0.0415 and FTI > 0.013735 and FTI <= 0.064255 | 1 | 0.001122 |
| TSH > 0.00605 and FTI <= 0.064255 and Thyroid_surgery > 0.5 and T3 <= 0.0108 | 1 | 0.000211 |
| On_thyroxine <= 0.5 and On_antithyroid_medication = all and Thyroid_surgery <= 0.5 and Query_hyperthyroid = all and Hypopituitary = all and TSH > 0.00605 and TSH <= 0.0195 and FTI > 0.013735 and FTI <= 0.064255 | 1 | 0.001835 |
| TSH >= 0.00605 and FTI < 0.064255 | 1 | 0.020819 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| TSH <= 0.00605 | 3 | 0.924209 |
| FTI <= 0.064255 and Thyroid_surgery <= 0.5 and T3 <= 0.0235 and I131_treatment <= 0.5 and TSH > 0.016895 | 1 | 0.199673 |
| FTI > 0.06472 and On_thyroxine <= 0.5 and TT4 <= 0.1505 and TT4 > 0.0615 and T3 <= 0.0195 and T4U <= 0.1105 | 2 | 0.527931 |
| FTI <= 0.064255 and T4U <= 0.14100000000000001 and T3 <= 0.0265 and T4U <= 0.096 | 1 | 0.034483 |
| FTI <= 0.0605 and T3 <= 0.0265 and T3 > 0.008799999999999999 and T4U <= 0.14250000000000002 and T3 <= 0.011 | 1 | 0.034483 |
| On_thyroxine <= 0.5 and FTI > 0.062965 and TT4 <= 0.1505 and Thyroid_surgery <= 0.5 and TT4 > 0.0615 and T3 <= 0.0305 | 2 | 0.391975 |
| FTI > 0.06 and TT4 > 0.0605 and T3 <= 0.0305 | 3 | 0.861111 |
| FTI <= 0.062 and T3 <= 0.018500000000000003 | 3 | 0.285714 |
| FTI > 0.062 and Age > 0.29000000000000004 and T3 > 0.0185 and T4U <= 0.113 | 3 | 0.411765 |
| FTI > 0.062 and TT4 <= 0.156 and On_thyroxine <= 0.5 | 2 | 0.377232 |
| T3 > 0.0265 | 3 | 0.588235 |
| TSH > 0.0165 | 1 | 0.625000 |
| TT4 <= 0.0625 | 3 | 0.600000 |
|  | 1 | 1.000000 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| FTI <= 0.064 and TSH >= 0.00879 and T3 <= 0.011 and T4U <= 0.111 | 1 | 0.012172 |
| FTI <= 0.064 and TSH >= 0.018 and Age <= 0.67 and Thyroid_surgery <= 0 | 1 | 0.008148 |
| FTI <= 0.064 and TSH >= 0.0062 and T3 <= 0.01 | 1 | 0.001468 |
| On_thyroxine <= 0 and T3 <= 0.019 and FTI >= 0.069 and TSH >= 0.0078 | 2 | 0.025624 |
| TSH >= 0.0061 and On_thyroxine <= 0 and TT4 <= 0.146 and TT4 >= 0.072 and Thyroid_surgery <= 0 and TSH <= 0.01 | 2 | 0.018943 |
| TSH >= 0.0062 and On_thyroxine <= 0 and TT4 <= 0.15 and FTI >= 0.06493 and Thyroid_surgery <= 0 and T4U >= 0.097 and T3 <= 0.03 | 2 | 0.005627 |
| TSH >= 0.0062 and On_thyroxine <= 0 and T4U <= 0.096 and Age >= 0.43 and TT4 >= 0.062 and TT4 <= 0.091 | 2 | 0.002159 |
|  | 3 | 0.997340 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

on_thyroxine|on_antithyroid_medication|thyroid_surgery|query_hyperthyroid|hypopituitary|tsh|fti|class
---|---|---|---|---|---|---|---
(0.5-inf)|all|(-inf-0.5]|all|all|(0.0195-0.0415]|(0.14225-inf)|1
(-inf-0.5]|all|(-inf-0.5]|all|all|(0.0195-0.0415]|(0.14225-inf)|3
(0.5-inf)|all|(-inf-0.5]|all|all|(0.0415-inf)|(0.097495-0.14225]|3
(-inf-0.5]|all|(-inf-0.5]|all|all|(0.00605-0.0195]|(0.14225-inf)|3
(0.5-inf)|all|(-inf-0.5]|all|all|(0.00605-0.0195]|(0.14225-inf)|3
(-inf-0.5]|all|(-inf-0.5]|all|all|(0.0195-0.0415]|(0.097495-0.14225]|2
(0.5-inf)|all|(-inf-0.5]|all|all|(0.0195-0.0415]|(0.097495-0.14225]|3
(-inf-0.5]|all|(-inf-0.5]|all|all|(0.0415-inf)|(0.08002-0.097495]|2
(0.5-inf)|all|(0.5-inf)|all|all|(-inf-0.00605]|(0.14225-inf)|3
(-inf-0.5]|all|(0.5-inf)|all|all|(-inf-0.00605]|(0.14225-inf)|3
(-inf-0.5]|all|(0.5-inf)|all|all|(0.00605-0.0195]|(0.097495-0.14225]|3
(0.5-inf)|all|(-inf-0.5]|all|all|(-inf-0.00605]|(0.14225-inf)|3
(0.5-inf)|all|(0.5-inf)|all|all|(0.0195-0.0415]|(0.08002-0.097495]|1
(-inf-0.5]|all|(-inf-0.5]|all|all|(-inf-0.00605]|(0.14225-inf)|3
(-inf-0.5]|all|(-inf-0.5]|all|all|(0.00605-0.0195]|(0.097495-0.14225]|2
(0.5-inf)|all|(-inf-0.5]|all|all|(0.00605-0.0195]|(0.097495-0.14225]|3
(-inf-0.5]|all|(-inf-0.5]|all|all|(0.0195-0.0415]|(0.08002-0.097495]|2
(0.5-inf)|all|(-inf-0.5]|all|all|(0.0195-0.0415]|(0.08002-0.097495]|3
(0.5-inf)|all|(-inf-0.5]|all|all|(0.0415-inf)|(0.064255-0.08002]|3
(-inf-0.5]|all|(-inf-0.5]|all|all|(0.0415-inf)|(0.064255-0.08002]|2
(0.5-inf)|all|(0.5-inf)|all|all|(-inf-0.00605]|(0.097495-0.14225]|3
(-inf-0.5]|all|(0.5-inf)|all|all|(-inf-0.00605]|(0.097495-0.14225]|3
(-inf-0.5]|all|(0.5-inf)|all|all|(0.00605-0.0195]|(0.08002-0.097495]|3
(0.5-inf)|all|(-inf-0.5]|all|all|(-inf-0.00605]|(0.097495-0.14225]|3
(-inf-0.5]|all|(-inf-0.5]|all|all|(-inf-0.00605]|(0.097495-0.14225]|3
(-inf-0.5]|all|(0.5-inf)|all|all|(0.0415-inf)|(0.013735-0.064255]|1
(-inf-0.5]|all|(-inf-0.5]|all|all|(0.00605-0.0195]|(0.08002-0.097495]|2
(0.5-inf)|all|(-inf-0.5]|all|all|(0.00605-0.0195]|(0.08002-0.097495]|3
(0.5-inf)|all|(-inf-0.5]|all|all|(0.0195-0.0415]|(0.064255-0.08002]|3
(-inf-0.5]|all|(-inf-0.5]|all|all|(0.0195-0.0415]|(0.064255-0.08002]|2
(-inf-0.5]|all|(-inf-0.5]|all|all|(0.0415-inf)|(0.013735-0.064255]|1
(0.5-inf)|all|(-inf-0.5]|all|all|(0.0415-inf)|(0.013735-0.064255]|1
(-inf-0.5]|all|(0.5-inf)|all|all|(-inf-0.00605]|(0.08002-0.097495]|3
(-inf-0.5]|all|(0.5-inf)|all|all|(0.00605-0.0195]|(0.064255-0.08002]|3
(-inf-0.5]|all|(0.5-inf)|all|all|(0.0195-0.0415]|(0.013735-0.064255]|1
(0.5-inf)|all|(-inf-0.5]|all|all|(-inf-0.00605]|(0.08002-0.097495]|3
(-inf-0.5]|all|(-inf-0.5]|all|all|(-inf-0.00605]|(0.08002-0.097495]|3
(-inf-0.5]|all|(-inf-0.5]|all|all|(0.00605-0.0195]|(0.064255-0.08002]|2
(0.5-inf)|all|(-inf-0.5]|all|all|(0.00605-0.0195]|(0.064255-0.08002]|3
(0.5-inf)|all|(-inf-0.5]|all|all|(0.0195-0.0415]|(0.013735-0.064255]|1
(-inf-0.5]|all|(-inf-0.5]|all|all|(0.0195-0.0415]|(0.013735-0.064255]|1
(0.5-inf)|all|(-inf-0.5]|all|all|(0.0415-inf)|(-inf-0.013735]|1
(-inf-0.5]|all|(-inf-0.5]|all|all|(0.0415-inf)|(-inf-0.013735]|1
(-inf-0.5]|all|(0.5-inf)|all|all|(-inf-0.00605]|(0.064255-0.08002]|3
(-inf-0.5]|all|(0.5-inf)|all|all|(0.00605-0.0195]|(0.013735-0.064255]|1
(0.5-inf)|all|(-inf-0.5]|all|all|(-inf-0.00605]|(0.064255-0.08002]|3
(-inf-0.5]|all|(-inf-0.5]|all|all|(-inf-0.00605]|(0.064255-0.08002]|3
(0.5-inf)|all|(-inf-0.5]|all|all|(0.00605-0.0195]|(0.013735-0.064255]|3
(-inf-0.5]|all|(-inf-0.5]|all|all|(0.00605-0.0195]|(0.013735-0.064255]|1
(-inf-0.5]|all|(-inf-0.5]|all|all|(0.0195-0.0415]|(-inf-0.013735]|1
(-inf-0.5]|all|(0.5-inf)|all|all|(-inf-0.00605]|(0.013735-0.064255]|3
(0.5-inf)|all|(-inf-0.5]|all|all|(-inf-0.00605]|(0.013735-0.064255]|3
(-inf-0.5]|all|(-inf-0.5]|all|all|(-inf-0.00605]|(0.013735-0.064255]|3

## JRip

Decision list:

rules | predicted class
---|---
(FTI <= 0.064) and (TSH >= 0.00879) and (T3 <= 0.011) and (T4U <= 0.111)|1 (78.0/0.0)
(FTI <= 0.064) and (TSH >= 0.018) and (Age <= 0.67) and (Thyroid_surgery <= 0)|1 (52.0/0.0)
(FTI <= 0.064) and (TSH >= 0.0062) and (T3 <= 0.01)|1 (13.0/2.0)
(On_thyroxine <= 0) and (T3 <= 0.019) and (FTI >= 0.069) and (TSH >= 0.0078)|2 (158.0/0.0)
(TSH >= 0.0061) and (On_thyroxine <= 0) and (TT4 <= 0.146) and (TT4 >= 0.072) and (Thyroid_surgery <= 0) and (TSH <= 0.01)|2 (117.0/0.0)
(TSH >= 0.0062) and (On_thyroxine <= 0) and (TT4 <= 0.15) and (FTI >= 0.06493) and (Thyroid_surgery <= 0) and (T4U >= 0.097) and (T3 <= 0.03)|2 (34.0/0.0)
(TSH >= 0.0062) and (On_thyroxine <= 0) and (T4U <= 0.096) and (Age >= 0.43) and (TT4 >= 0.062) and (TT4 <= 0.091)|2 (13.0/0.0)
|3 (6014.0/16.0)


## PART

Decision list:

rules | predicted class
---|---
TSH <= 0.00605|3 (5841.0)
FTI <= 0.064255 AND Thyroid_surgery <= 0.5 AND T3 <= 0.0235 AND I131_treatment <= 0.5 AND TSH > 0.016895|1 (122.0)
FTI > 0.06472 AND On_thyroxine <= 0.5 AND TT4 <= 0.1505 AND TT4 > 0.0615 AND T3 <= 0.0195 AND T4U <= 0.1105|2 (210.0/1.0)
FTI <= 0.064255 AND T4U <= 0.14100000000000001 AND T3 <= 0.0265 AND T4U <= 0.096|1 (10.0)
FTI <= 0.0605 AND T3 <= 0.0265 AND T3 > 0.008799999999999999 AND T4U <= 0.14250000000000002 AND T3 <= 0.011|1 (10.0)
On_thyroxine <= 0.5 AND FTI > 0.062965 AND TT4 <= 0.1505 AND Thyroid_surgery <= 0.5 AND TT4 > 0.0615 AND T3 <= 0.0305|2 (109.0/1.0)
FTI > 0.06 AND TT4 > 0.0605 AND T3 <= 0.0305|3 (122.0)
FTI <= 0.062 AND T3 <= 0.018500000000000003|3 (8.0)
FTI > 0.062 AND Age > 0.29000000000000004 AND T3 > 0.0185 AND T4U <= 0.113|3 (14.0)
FTI > 0.062 AND TT4 <= 0.156 AND On_thyroxine <= 0.5|2 (14.0/1.0)
T3 > 0.0265|3 (10.0)
TSH > 0.0165|1 (5.0)
TT4 <= 0.0625|3 (2.0)
|1 (2.0)


## J48 Decision Tree

* TSH <= 0.00605: 3 (5841.0)
* TSH > 0.00605
	* FTI <= 0.064255
		* Thyroid_surgery <= 0.5
			* T3 <= 0.0235: 1 (146.0/5.0)
			* T3 > 0.0235
				* T3 <= 0.0265
					* TSH <= 0.01385: 3 (3.0/1.0)
					* TSH > 0.01385: 1 (5.0)
				* T3 > 0.0265: 3 (5.0)
		* Thyroid_surgery > 0.5
			* T3 <= 0.0108: 1 (3.0/1.0)
			* T3 > 0.0108: 3 (3.0)
	* FTI > 0.064255
		* On_thyroxine <= 0.5
			* TT4 <= 0.1505
				* TT4 <= 0.0615
					* T3 <= 0.01905: 2 (9.0/1.0)
					* T3 > 0.01905: 3 (6.0)
				* TT4 > 0.0615
					* T3 <= 0.0195: 2 (239.0/3.0)
					* T3 > 0.0195
						* Thyroid_surgery <= 0.5
							* T3 <= 0.0305: 2 (82.0/1.0)
							* T3 > 0.0305
								* T4U <= 0.113: 3 (4.0)
								* T4U > 0.113: 2 (5.0)
						* Thyroid_surgery > 0.5: 3 (6.0)
			* TT4 > 0.1505: 3 (20.0)
		* On_thyroxine > 0.5: 3 (102.0)


## SimpleCart Decision Tree

* TSH < 0.00605: 3(5841.0/0.0)
* TSH >= 0.00605
	* FTI < 0.064255: 1(149.0/16.0)
	* FTI >= 0.064255
		* On_thyroxine < 0.5
			* TT4 < 0.1505
				* Thyroid_surgery < 0.5: 2(330.0/12.0)
				* Thyroid_surgery >= 0.5: 3(9.0/0.0)
			* TT4 >= 0.1505: 3(20.0/0.0)
		* On_thyroxine >= 0.5: 3(102.0/0.0)


