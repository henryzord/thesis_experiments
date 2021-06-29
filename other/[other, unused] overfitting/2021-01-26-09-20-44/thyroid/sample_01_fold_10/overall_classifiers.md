# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 3 | 0.926069 |
| TSH >= 0.00605 and FTI >= 0.064255 and On_thyroxine < 0.5 and TT4 < 0.1505 and Thyroid_surgery < 0.5 | 2 | 0.049102 |
| On_thyroxine <= 0.5 and Thyroid_surgery <= 0.5 and Goitre <= 0.5 and TSH > 0.0195 and TSH <= 0.0415 and FTI <= 0.013735 | 1 | 0.001105 |
| TSH > 0.00605 and FTI <= 0.064255 and TSH > 0.016895 and Thyroid_surgery > 0.5 and Age > 0.51 | 1 | 0.000316 |
| TSH > 0.00605 and FTI <= 0.064255 and TSH > 0.016895 and Thyroid_surgery <= 0.5 and I131_treatment <= 0.5 and T3 > 0.0245 and Age <= 0.63 | 1 | 0.000474 |
| On_thyroxine <= 0.5 and Thyroid_surgery <= 0.5 and Goitre <= 0.5 and TSH > 0.0195 and TSH <= 0.0415 and FTI > 0.013735 and FTI <= 0.0345 | 1 | 0.000474 |
| On_thyroxine > 0.5 and Thyroid_surgery <= 0.5 and Goitre <= 0.5 and TSH > 0.0415 and FTI <= 0.013735 | 1 | 0.000474 |
| TSH > 0.00605 and FTI <= 0.064255 and TSH <= 0.016895 and On_antithyroid_medication <= 0.5 and T4U <= 0.106 | 1 | 0.001892 |
| On_thyroxine <= 0.5 and Thyroid_surgery > 0.5 and Goitre <= 0.5 and TSH > 0.0415 and FTI > 0.0345 and FTI <= 0.064255 | 1 | 0.000158 |
| On_thyroxine > 0.5 and Thyroid_surgery <= 0.5 and Goitre <= 0.5 and TSH > 0.0415 and FTI > 0.0345 and FTI <= 0.064255 | 1 | 0.000632 |
| TSH >= 0.00605 and FTI < 0.064255 and T3 < 0.0265 | 1 | 0.021718 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| TSH <= 0.006 | 3 | 0.924221 |
| FTI <= 0.064 and Thyroid_surgery <= 0.0 and T3 <= 0.023 and I131_treatment <= 0.0 and Sex <= 0.0 and Query_hypothyroid <= 0.0 and On_thyroxine <= 0.0 and Query_hyperthyroid <= 0.0 and Tumor <= 0.0 and TSH > 0.01679 | 1 | 0.111111 |
| FTI <= 0.064 and T3 <= 0.026 and Thyroid_surgery <= 0.0 and On_antithyroid_medication <= 0.0 and I131_treatment <= 0.0 and TT4 <= 0.065 | 1 | 0.127013 |
| On_thyroxine > 0.0 and FTI > 0.064 | 3 | 0.220225 |
| FTI > 0.064 and TT4 <= 0.15 and TT4 > 0.061 and T3 <= 0.028 and Age > 0.42 and Sex <= 0.0 and Query_hypothyroid <= 0.0 and Query_hyperthyroid <= 0.0 and Sick <= 0.0 | 2 | 0.629950 |
| FTI > 0.064 and TT4 <= 0.15 and Thyroid_surgery <= 0.0 and TT4 > 0.058 and T3 <= 0.028 | 2 | 0.705001 |
| FTI > 0.064 and TT4 > 0.143 | 3 | 0.462963 |
| TT4 <= 0.124 and FTI > 0.064 and T3 > 0.016 | 3 | 0.369565 |
| FTI > 0.064 and Thyroid_surgery <= 0.0 and Sex <= 0.0 and Age <= 0.78 | 2 | 0.204545 |
| FTI > 0.066 and Sex <= 0.0 and Thyroid_surgery > 0.0 | 3 | 0.130435 |
| FTI <= 0.071 and T3 <= 0.026 and Sex <= 0.0 and On_thyroxine <= 0.0 and TSH > 0.01 and TT4 > 0.054 | 1 | 0.307692 |
| FTI <= 0.071 and FTI > 0.01347 and On_thyroxine <= 0.0 and Sex <= 0.0 and Thyroid_surgery <= 0.0 | 3 | 0.428571 |
| FTI <= 0.069 and I131_treatment > 0.0 | 1 | 0.357143 |
| FTI > 0.069 | 2 | 0.230769 |
| Thyroid_surgery > 0.0 and Age <= 0.47 | 3 | 0.333333 |
| T3 <= 0.026 and Thyroid_surgery <= 0.0 | 1 | 0.428571 |
| Thyroid_surgery <= 0.0 | 3 | 0.750000 |
|  | 1 | 0.500000 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| FTI <= 0.064 and TSH >= 0.0077 | 1 | 0.020680 |
| FTI <= 0.064 and TSH >= 0.0063 and T3 <= 0.023 and Thyroid_surgery <= 0 | 1 | 0.000439 |
| TSH >= 0.0061 and On_thyroxine <= 0 and T3 <= 0.019 and Thyroid_surgery <= 0 | 2 | 0.037571 |
| TSH >= 0.0061 and On_thyroxine <= 0 and TT4 <= 0.141 and TT4 >= 0.067 and Thyroid_surgery <= 0 | 2 | 0.013040 |
|  | 3 | 0.999167 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

on_thyroxine|thyroid_surgery|goitre|tsh|fti|class
---|---|---|---|---|---
(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(0.0195-0.0415]|(0.1425-inf)|3
(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(0.0415-inf)|(0.097495-0.1425]|1
(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(0.00605-0.0195]|(0.1425-inf)|3
(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(0.00605-0.0195]|(0.1425-inf)|3
(0.5-inf)|(-inf-0.5]|(0.5-inf)|(-inf-0.00605]|(0.1425-inf)|1
(-inf-0.5]|(-inf-0.5]|(0.5-inf)|(-inf-0.00605]|(0.1425-inf)|3
(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(0.0195-0.0415]|(0.097495-0.1425]|3
(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(0.0195-0.0415]|(0.097495-0.1425]|2
(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(0.0415-inf)|(0.08104-0.097495]|2
(-inf-0.5]|(0.5-inf)|(-inf-0.5]|(-inf-0.00605]|(0.1425-inf)|3
(0.5-inf)|(0.5-inf)|(-inf-0.5]|(-inf-0.00605]|(0.1425-inf)|3
(-inf-0.5]|(0.5-inf)|(-inf-0.5]|(0.00605-0.0195]|(0.097495-0.1425]|3
(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(-inf-0.00605]|(0.1425-inf)|3
(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.00605]|(0.1425-inf)|3
(0.5-inf)|(0.5-inf)|(-inf-0.5]|(0.0195-0.0415]|(0.08104-0.097495]|1
(-inf-0.5]|(0.5-inf)|(-inf-0.5]|(0.0195-0.0415]|(0.08104-0.097495]|1
(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(0.00605-0.0195]|(0.097495-0.1425]|2
(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(0.00605-0.0195]|(0.097495-0.1425]|3
(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(0.0195-0.0415]|(0.08104-0.097495]|2
(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(0.0195-0.0415]|(0.08104-0.097495]|3
(0.5-inf)|(-inf-0.5]|(0.5-inf)|(-inf-0.00605]|(0.097495-0.1425]|3
(-inf-0.5]|(-inf-0.5]|(0.5-inf)|(-inf-0.00605]|(0.097495-0.1425]|3
(-inf-0.5]|(-inf-0.5]|(0.5-inf)|(0.00605-0.0195]|(0.08104-0.097495]|1
(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(0.0415-inf)|(0.064255-0.08104]|2
(0.5-inf)|(0.5-inf)|(-inf-0.5]|(-inf-0.00605]|(0.097495-0.1425]|3
(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(0.0415-inf)|(0.064255-0.08104]|3
(-inf-0.5]|(0.5-inf)|(-inf-0.5]|(-inf-0.00605]|(0.097495-0.1425]|3
(-inf-0.5]|(0.5-inf)|(-inf-0.5]|(0.00605-0.0195]|(0.08104-0.097495]|3
(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(-inf-0.00605]|(0.097495-0.1425]|3
(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.00605]|(0.097495-0.1425]|3
(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(0.00605-0.0195]|(0.08104-0.097495]|2
(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(0.00605-0.0195]|(0.08104-0.097495]|3
(-inf-0.5]|(0.5-inf)|(-inf-0.5]|(0.0415-inf)|(0.0345-0.064255]|1
(0.5-inf)|(-inf-0.5]|(0.5-inf)|(-inf-0.00605]|(0.08104-0.097495]|1
(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(0.0195-0.0415]|(0.064255-0.08104]|2
(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(0.0195-0.0415]|(0.064255-0.08104]|3
(-inf-0.5]|(-inf-0.5]|(0.5-inf)|(-inf-0.00605]|(0.08104-0.097495]|3
(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(0.0415-inf)|(0.0345-0.064255]|1
(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(0.0415-inf)|(0.0345-0.064255]|1
(-inf-0.5]|(0.5-inf)|(-inf-0.5]|(-inf-0.00605]|(0.08104-0.097495]|3
(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(-inf-0.00605]|(0.08104-0.097495]|3
(-inf-0.5]|(0.5-inf)|(-inf-0.5]|(0.00605-0.0195]|(0.064255-0.08104]|3
(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.00605]|(0.08104-0.097495]|3
(-inf-0.5]|(0.5-inf)|(-inf-0.5]|(0.0195-0.0415]|(0.0345-0.064255]|1
(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(0.00605-0.0195]|(0.064255-0.08104]|2
(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(0.00605-0.0195]|(0.064255-0.08104]|3
(0.5-inf)|(-inf-0.5]|(0.5-inf)|(-inf-0.00605]|(0.064255-0.08104]|1
(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(0.0195-0.0415]|(0.0345-0.064255]|1
(-inf-0.5]|(0.5-inf)|(-inf-0.5]|(0.0415-inf)|(0.013735-0.0345]|1
(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(0.0195-0.0415]|(0.0345-0.064255]|1
(-inf-0.5]|(-inf-0.5]|(0.5-inf)|(-inf-0.00605]|(0.064255-0.08104]|3
(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(0.0415-inf)|(0.013735-0.0345]|1
(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(0.0415-inf)|(0.013735-0.0345]|1
(-inf-0.5]|(0.5-inf)|(-inf-0.5]|(-inf-0.00605]|(0.064255-0.08104]|3
(-inf-0.5]|(0.5-inf)|(-inf-0.5]|(0.00605-0.0195]|(0.0345-0.064255]|1
(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(-inf-0.00605]|(0.064255-0.08104]|3
(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.00605]|(0.064255-0.08104]|3
(-inf-0.5]|(0.5-inf)|(-inf-0.5]|(0.0195-0.0415]|(0.013735-0.0345]|1
(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(0.00605-0.0195]|(0.0345-0.064255]|1
(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(0.00605-0.0195]|(0.0345-0.064255]|1
(-inf-0.5]|(0.5-inf)|(-inf-0.5]|(0.0415-inf)|(-inf-0.013735]|1
(-inf-0.5]|(-inf-0.5]|(0.5-inf)|(-inf-0.00605]|(0.0345-0.064255]|3
(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(0.0195-0.0415]|(0.013735-0.0345]|1
(-inf-0.5]|(0.5-inf)|(-inf-0.5]|(-inf-0.00605]|(0.0345-0.064255]|1
(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(0.0415-inf)|(-inf-0.013735]|1
(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(0.0415-inf)|(-inf-0.013735]|1
(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(-inf-0.00605]|(0.0345-0.064255]|3
(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.00605]|(0.0345-0.064255]|3
(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(0.00605-0.0195]|(0.013735-0.0345]|1
(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(0.0195-0.0415]|(-inf-0.013735]|1
(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.00605]|(0.013735-0.0345]|3
(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.00605]|(-inf-0.013735]|1

## JRip

Decision list:

rules | predicted class
---|---
(FTI <= 0.064) and (TSH >= 0.0077)|1 (153.0/10.0)
(FTI <= 0.064) and (TSH >= 0.0063) and (T3 <= 0.023) and (Thyroid_surgery <= 0)|1 (5.0/0.0)
(TSH >= 0.0061) and (On_thyroxine <= 0) and (T3 <= 0.019) and (Thyroid_surgery <= 0)|2 (246.0/4.0)
(TSH >= 0.0061) and (On_thyroxine <= 0) and (TT4 <= 0.141) and (TT4 >= 0.067) and (Thyroid_surgery <= 0)|2 (88.0/4.0)
|3 (5987.0/4.0)


## PART

Decision list:

rules | predicted class
---|---
TSH <= 0.006|3 (5842.0)
FTI <= 0.064 AND Thyroid_surgery <= 0.0 AND T3 <= 0.023 AND I131_treatment <= 0.0 AND Sex <= 0.0 AND Query_hypothyroid <= 0.0 AND On_thyroxine <= 0.0 AND Query_hyperthyroid <= 0.0 AND Tumor <= 0.0 AND TSH > 0.01679|1 (61.0)
FTI <= 0.064 AND T3 <= 0.026 AND Thyroid_surgery <= 0.0 AND On_antithyroid_medication <= 0.0 AND I131_treatment <= 0.0 AND TT4 <= 0.065|1 (71.0)
On_thyroxine > 0.0 AND FTI > 0.064|3 (98.0)
FTI > 0.064 AND TT4 <= 0.15 AND TT4 > 0.061 AND T3 <= 0.028 AND Age > 0.42 AND Sex <= 0.0 AND Query_hypothyroid <= 0.0 AND Query_hyperthyroid <= 0.0 AND Sick <= 0.0|2 (135.0/2.0)
FTI > 0.064 AND TT4 <= 0.15 AND Thyroid_surgery <= 0.0 AND TT4 > 0.058 AND T3 <= 0.028|2 (185.0)
FTI > 0.064 AND TT4 > 0.143|3 (24.0)
TT4 <= 0.124 AND FTI > 0.064 AND T3 > 0.016|3 (16.0)
FTI > 0.064 AND Thyroid_surgery <= 0.0 AND Sex <= 0.0 AND Age <= 0.78|2 (9.0)
FTI > 0.066 AND Sex <= 0.0 AND Thyroid_surgery > 0.0|3 (3.0)
FTI <= 0.071 AND T3 <= 0.026 AND Sex <= 0.0 AND On_thyroxine <= 0.0 AND TSH > 0.01 AND TT4 > 0.054|1 (8.0)
FTI <= 0.071 AND FTI > 0.01347 AND On_thyroxine <= 0.0 AND Sex <= 0.0 AND Thyroid_surgery <= 0.0|3 (9.0)
FTI <= 0.069 AND I131_treatment > 0.0|1 (5.0)
FTI > 0.069|2 (3.0)
Thyroid_surgery > 0.0 AND Age <= 0.47|3 (2.0)
T3 <= 0.026 AND Thyroid_surgery <= 0.0|1 (3.0)
Thyroid_surgery <= 0.0|3 (3.0)
|1 (2.0/1.0)


## J48 Decision Tree

* TSH <= 0.00605: 3 (5842.0)
* TSH > 0.00605
	* FTI <= 0.064255
		* TSH <= 0.016895
			* On_antithyroid_medication <= 0.5
				* T4U <= 0.106: 1 (12.0)
				* T4U > 0.106
					* TSH <= 0.009695: 3 (3.0)
					* TSH > 0.009695
						* T3 <= 0.0245: 1 (4.0)
						* T3 > 0.0245: 3 (2.0)
			* On_antithyroid_medication > 0.5: 3 (3.0)
		* TSH > 0.016895
			* Thyroid_surgery <= 0.5
				* I131_treatment <= 0.5
					* T3 <= 0.0245: 1 (121.0)
					* T3 > 0.0245
						* Age <= 0.63: 1 (3.0)
						* Age > 0.63: 3 (2.0)
				* I131_treatment > 0.5
					* Age <= 0.655: 1 (5.0)
					* Age > 0.655: 3 (2.0)
			* Thyroid_surgery > 0.5
				* Age <= 0.51
					* TT4 <= 0.0465: 3 (2.0)
					* TT4 > 0.0465: 1 (2.0)
				* Age > 0.51: 1 (2.0)
	* FTI > 0.064255
		* On_thyroxine <= 0.5
			* TT4 <= 0.1505
				* TT4 <= 0.0615
					* T3 <= 0.019549999999999998
						* T3 <= 0.004: 2 (2.0/1.0)
						* T3 > 0.004: 2 (9.0)
					* T3 > 0.019549999999999998: 3 (6.0)
				* TT4 > 0.0615
					* T3 <= 0.028999999999999998
						* Age <= 0.425
							* Thyroid_surgery <= 0.5: 2 (77.0)
							* Thyroid_surgery > 0.5: 3 (9.0)
						* Age > 0.425
							* TT4 <= 0.14
								* T4U <= 0.127: 2 (222.0)
								* T4U > 0.127
									* TT4 <= 0.10250000000000001: 2 (2.0/1.0)
									* TT4 > 0.10250000000000001: 2 (6.0)
							* TT4 > 0.14
								* Age <= 0.81: 2 (6.0)
								* Age > 0.81: 2 (2.0/1.0)
					* T3 > 0.028999999999999998
						* T4U <= 0.11649999999999999: 3 (5.0)
						* T4U > 0.11649999999999999: 2 (7.0)
			* TT4 > 0.1505: 3 (23.0)
		* On_thyroxine > 0.5: 3 (98.0)


## SimpleCart Decision Tree

* TSH < 0.00605: 3(5842.0/0.0)
* TSH >= 0.00605
	* FTI < 0.064255
		* T3 < 0.0265: 1(149.0/9.0)
		* T3 >= 0.0265: 3(5.0/0.0)
	* FTI >= 0.064255
		* On_thyroxine < 0.5
			* TT4 < 0.1505
				* Thyroid_surgery < 0.5: 2(330.0/13.0)
				* Thyroid_surgery >= 0.5: 3(10.0/0.0)
			* TT4 >= 0.1505: 3(23.0/0.0)
		* On_thyroxine >= 0.5: 3(98.0/0.0)


