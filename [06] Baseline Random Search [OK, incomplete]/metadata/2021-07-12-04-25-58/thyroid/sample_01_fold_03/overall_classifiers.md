# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| TSH < 0.00605 | 3 | 0.924161 |
| TSH >= 0.00605 and FTI >= 0.064255 and On_thyroxine < 0.5 and TT4 < 0.1495 and Thyroid_surgery < 0.5 and TT4 >= 0.058499999999999996 and T3 < 0.0295 | 2 | 0.049173 |
| TSH >= 0.00605 and FTI < 0.064255 and T3 < 0.0265 and Thyroid_surgery < 0.5 and On_antithyroid_medication < 0.5 and TSH >= 0.009545000000000001 and I131_treatment < 0.5 | 1 | 0.020275 |
| TSH >= 0.00605 and FTI >= 0.064255 and On_thyroxine >= 0.5 | 3 | 0.175559 |
| TSH >= 0.00605 and FTI >= 0.064255 and On_thyroxine < 0.5 and TT4 >= 0.1495 | 3 | 0.043912 |
| TSH >= 0.00605 and FTI >= 0.064255 and On_thyroxine < 0.5 and TT4 < 0.1495 and Thyroid_surgery >= 0.5 | 3 | 0.020450 |
| TSH >= 0.00605 and FTI < 0.064255 and T3 < 0.0265 and Thyroid_surgery < 0.5 and On_antithyroid_medication < 0.5 and TSH < 0.009545000000000001 and TT4 < 0.0595 | 1 | 0.001420 |
| TSH >= 0.00605 and FTI >= 0.064255 and On_thyroxine < 0.5 and TT4 < 0.1495 and Thyroid_surgery < 0.5 and TT4 < 0.058499999999999996 and T3 >= 0.01755 | 3 | 0.012371 |
| TSH >= 0.00605 and FTI >= 0.064255 and On_thyroxine < 0.5 and TT4 < 0.1495 and Thyroid_surgery < 0.5 and TT4 >= 0.058499999999999996 and T3 >= 0.0295 and T4U < 0.113 | 3 | 0.010331 |
| TSH >= 0.00605 and FTI >= 0.064255 and On_thyroxine < 0.5 and TT4 < 0.1495 and Thyroid_surgery < 0.5 and TT4 >= 0.058499999999999996 and T3 >= 0.0295 and T4U >= 0.113 | 2 | 0.001137 |
| TSH >= 0.00605 and FTI < 0.064255 and T3 >= 0.0265 | 3 | 0.010331 |
| TSH >= 0.00605 and FTI < 0.064255 and T3 < 0.0265 and Thyroid_surgery < 0.5 and On_antithyroid_medication < 0.5 and TSH >= 0.009545000000000001 and I131_treatment >= 0.5 and Age < 0.655 | 1 | 0.000632 |
| TSH >= 0.00605 and FTI < 0.064255 and T3 < 0.0265 and Thyroid_surgery >= 0.5 and T4U >= 0.131 | 3 | 0.006224 |
| TSH >= 0.00605 and FTI < 0.064255 and T3 < 0.0265 and Thyroid_surgery < 0.5 and On_antithyroid_medication < 0.5 and TSH < 0.009545000000000001 and TT4 >= 0.0595 | 3 | 0.006224 |
| TSH >= 0.00605 and FTI < 0.064255 and T3 < 0.0265 and Thyroid_surgery >= 0.5 and T4U < 0.131 | 1 | 0.000505 |
| TSH >= 0.00605 and FTI >= 0.064255 and On_thyroxine < 0.5 and TT4 < 0.1495 and Thyroid_surgery < 0.5 and TT4 < 0.058499999999999996 and T3 < 0.01755 | 2 | 0.000520 |
| TSH >= 0.00605 and FTI < 0.064255 and T3 < 0.0265 and Thyroid_surgery < 0.5 and On_antithyroid_medication < 0.5 and TSH >= 0.009545000000000001 and I131_treatment >= 0.5 and Age >= 0.655 | 3 | 0.004158 |
| TSH >= 0.00605 and FTI < 0.064255 and T3 < 0.0265 and Thyroid_surgery < 0.5 and On_antithyroid_medication >= 0.5 | 3 | 0.002778 |
| On_thyroxine <= 0.5 and Query_on_thyroxine = all and On_antithyroid_medication = all and Sick = all and Thyroid_surgery <= 0.5 and Query_hyperthyroid = all and Tumor = all and TSH > 0.0195 and TSH <= 0.0415 and TT4 > 0.0525 and TT4 <= 0.0685 | 1 | 0.000777 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| TSH <= 0.00605 | 3 | 0.924161 |
| FTI <= 0.064255 and Thyroid_surgery <= 0.5 and T3 <= 0.0235 | 1 | 0.215243 |
| On_thyroxine <= 0.5 and FTI > 0.062965 and TT4 <= 0.1495 and TT4 > 0.0615 and T3 <= 0.0285 and Age > 0.425 | 2 | 0.572182 |
| On_thyroxine > 0.5 | 3 | 0.492936 |
| FTI > 0.062965 and TT4 <= 0.1485 and Thyroid_surgery <= 0.5 and Age <= 0.56 | 2 | 0.568817 |
| FTI > 0.06 and Sex <= 0.5 and Age <= 0.775 | 3 | 0.711538 |
| TSH <= 0.0195 and T3 > 0.01755 | 3 | 0.362319 |
| TSH > 0.019395 | 1 | 0.264706 |
|  | 2 | 0.352941 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| FTI <= 0.064 and TSH >= 0.00879 and T3 <= 0.011 and T4U <= 0.111 | 1 | 0.011864 |
| FTI <= 0.064 and TSH >= 0.018 and Age <= 0.67 and Thyroid_surgery <= 0 | 1 | 0.007992 |
| FTI <= 0.061 and TSH >= 0.0062 and T3 <= 0.01 and Age >= 0.52 | 1 | 0.001577 |
| FTI <= 0.064 and TSH >= 0.0062 and FTI >= 0.051 | 1 | 0.001127 |
| TSH >= 0.0061 and On_thyroxine <= 0 and T3 <= 0.02 and FTI >= 0.069 and Thyroid_surgery <= 0 and TT4 <= 0.148 | 2 | 0.038449 |
| TSH >= 0.0061 and On_thyroxine <= 0 and T3 >= 0.0208 and TT4 <= 0.141 and T3 <= 0.028 and On_antithyroid_medication <= 0 | 2 | 0.010886 |
| TSH >= 0.0063 and On_thyroxine <= 0 and FTI <= 0.092 and TT4 >= 0.06 and Thyroid_surgery <= 0 and T3 <= 0.019 | 2 | 0.002007 |
|  | 3 | 0.998170 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

on_thyroxine|query_on_thyroxine|on_antithyroid_medication|sick|thyroid_surgery|query_hyperthyroid|tumor|tsh|tt4|class
---|---|---|---|---|---|---|---|---|---
(0.5-inf)|all|all|all|(-inf-0.5]|all|all|(0.0195-0.0415]|(0.1485-inf)|1
(-inf-0.5]|all|all|all|(-inf-0.5]|all|all|(0.0195-0.0415]|(0.1485-inf)|3
(-inf-0.5]|all|all|all|(-inf-0.5]|all|all|(0.0415-inf)|(0.0895-0.1485]|1
(0.5-inf)|all|all|all|(-inf-0.5]|all|all|(0.0415-inf)|(0.0895-0.1485]|3
(0.5-inf)|all|all|all|(-inf-0.5]|all|all|(0.00605-0.0195]|(0.1485-inf)|3
(-inf-0.5]|all|all|all|(-inf-0.5]|all|all|(0.00605-0.0195]|(0.1485-inf)|3
(-inf-0.5]|all|all|all|(-inf-0.5]|all|all|(0.0195-0.0415]|(0.0895-0.1485]|2
(0.5-inf)|all|all|all|(-inf-0.5]|all|all|(0.0195-0.0415]|(0.0895-0.1485]|3
(-inf-0.5]|all|all|all|(-inf-0.5]|all|all|(0.0415-inf)|(0.0685-0.0895]|2
(0.5-inf)|all|all|all|(-inf-0.5]|all|all|(0.0415-inf)|(0.0685-0.0895]|3
(-inf-0.5]|all|all|all|(0.5-inf)|all|all|(-inf-0.00605]|(0.1485-inf)|3
(0.5-inf)|all|all|all|(0.5-inf)|all|all|(-inf-0.00605]|(0.1485-inf)|3
(-inf-0.5]|all|all|all|(0.5-inf)|all|all|(0.00605-0.0195]|(0.0895-0.1485]|3
(0.5-inf)|all|all|all|(0.5-inf)|all|all|(0.0195-0.0415]|(0.0685-0.0895]|1
(-inf-0.5]|all|all|all|(0.5-inf)|all|all|(0.0195-0.0415]|(0.0685-0.0895]|1
(-inf-0.5]|all|all|all|(0.5-inf)|all|all|(0.0415-inf)|(0.0525-0.0685]|1
(0.5-inf)|all|all|all|(-inf-0.5]|all|all|(-inf-0.00605]|(0.1485-inf)|3
(-inf-0.5]|all|all|all|(-inf-0.5]|all|all|(-inf-0.00605]|(0.1485-inf)|3
(-inf-0.5]|all|all|all|(-inf-0.5]|all|all|(0.00605-0.0195]|(0.0895-0.1485]|2
(0.5-inf)|all|all|all|(-inf-0.5]|all|all|(0.00605-0.0195]|(0.0895-0.1485]|3
(0.5-inf)|all|all|all|(-inf-0.5]|all|all|(0.0195-0.0415]|(0.0685-0.0895]|3
(-inf-0.5]|all|all|all|(-inf-0.5]|all|all|(0.0195-0.0415]|(0.0685-0.0895]|2
(0.5-inf)|all|all|all|(-inf-0.5]|all|all|(0.0415-inf)|(0.0525-0.0685]|1
(-inf-0.5]|all|all|all|(-inf-0.5]|all|all|(0.0415-inf)|(0.0525-0.0685]|1
(0.5-inf)|all|all|all|(0.5-inf)|all|all|(-inf-0.00605]|(0.0895-0.1485]|3
(-inf-0.5]|all|all|all|(0.5-inf)|all|all|(-inf-0.00605]|(0.0895-0.1485]|3
(-inf-0.5]|all|all|all|(0.5-inf)|all|all|(0.00605-0.0195]|(0.0685-0.0895]|3
(-inf-0.5]|all|all|all|(0.5-inf)|all|all|(0.0195-0.0415]|(0.0525-0.0685]|1
(-inf-0.5]|all|all|all|(0.5-inf)|all|all|(0.0415-inf)|(0.0345-0.0525]|1
(0.5-inf)|all|all|all|(-inf-0.5]|all|all|(-inf-0.00605]|(0.0895-0.1485]|3
(-inf-0.5]|all|all|all|(-inf-0.5]|all|all|(-inf-0.00605]|(0.0895-0.1485]|3
(-inf-0.5]|all|all|all|(-inf-0.5]|all|all|(0.00605-0.0195]|(0.0685-0.0895]|2
(0.5-inf)|all|all|all|(-inf-0.5]|all|all|(0.00605-0.0195]|(0.0685-0.0895]|3
(0.5-inf)|all|all|all|(-inf-0.5]|all|all|(0.0195-0.0415]|(0.0525-0.0685]|1
(-inf-0.5]|all|all|all|(-inf-0.5]|all|all|(0.0195-0.0415]|(0.0525-0.0685]|1
(0.5-inf)|all|all|all|(-inf-0.5]|all|all|(0.0415-inf)|(0.0345-0.0525]|1
(-inf-0.5]|all|all|all|(-inf-0.5]|all|all|(0.0415-inf)|(0.0345-0.0525]|1
(-inf-0.5]|all|all|all|(0.5-inf)|all|all|(-inf-0.00605]|(0.0685-0.0895]|3
(-inf-0.5]|all|all|all|(0.5-inf)|all|all|(0.0415-inf)|(-inf-0.0345]|1
(0.5-inf)|all|all|all|(-inf-0.5]|all|all|(-inf-0.00605]|(0.0685-0.0895]|3
(-inf-0.5]|all|all|all|(-inf-0.5]|all|all|(-inf-0.00605]|(0.0685-0.0895]|3
(-inf-0.5]|all|all|all|(-inf-0.5]|all|all|(0.00605-0.0195]|(0.0525-0.0685]|2
(0.5-inf)|all|all|all|(-inf-0.5]|all|all|(0.00605-0.0195]|(0.0525-0.0685]|3
(0.5-inf)|all|all|all|(-inf-0.5]|all|all|(0.0195-0.0415]|(0.0345-0.0525]|1
(-inf-0.5]|all|all|all|(-inf-0.5]|all|all|(0.0195-0.0415]|(0.0345-0.0525]|1
(0.5-inf)|all|all|all|(-inf-0.5]|all|all|(0.0415-inf)|(-inf-0.0345]|1
(-inf-0.5]|all|all|all|(-inf-0.5]|all|all|(0.0415-inf)|(-inf-0.0345]|1
(-inf-0.5]|all|all|all|(0.5-inf)|all|all|(-inf-0.00605]|(0.0525-0.0685]|3
(-inf-0.5]|all|all|all|(0.5-inf)|all|all|(0.0195-0.0415]|(-inf-0.0345]|1
(0.5-inf)|all|all|all|(-inf-0.5]|all|all|(-inf-0.00605]|(0.0525-0.0685]|3
(-inf-0.5]|all|all|all|(-inf-0.5]|all|all|(-inf-0.00605]|(0.0525-0.0685]|3
(0.5-inf)|all|all|all|(-inf-0.5]|all|all|(0.00605-0.0195]|(0.0345-0.0525]|3
(-inf-0.5]|all|all|all|(-inf-0.5]|all|all|(0.00605-0.0195]|(0.0345-0.0525]|1
(-inf-0.5]|all|all|all|(-inf-0.5]|all|all|(0.0195-0.0415]|(-inf-0.0345]|1
(0.5-inf)|all|all|all|(-inf-0.5]|all|all|(0.0195-0.0415]|(-inf-0.0345]|1
(0.5-inf)|all|all|all|(0.5-inf)|all|all|(-inf-0.00605]|(0.0345-0.0525]|1
(-inf-0.5]|all|all|all|(0.5-inf)|all|all|(-inf-0.00605]|(0.0345-0.0525]|1
(0.5-inf)|all|all|all|(-inf-0.5]|all|all|(-inf-0.00605]|(0.0345-0.0525]|3
(-inf-0.5]|all|all|all|(-inf-0.5]|all|all|(-inf-0.00605]|(0.0345-0.0525]|3
(-inf-0.5]|all|all|all|(-inf-0.5]|all|all|(0.00605-0.0195]|(-inf-0.0345]|1
(-inf-0.5]|all|all|all|(-inf-0.5]|all|all|(-inf-0.00605]|(-inf-0.0345]|3

## JRip

Decision list:

rules | predicted class
---|---
(FTI <= 0.064) and (TSH >= 0.00879) and (T3 <= 0.011) and (T4U <= 0.111)|1 (76.0/0.0)
(FTI <= 0.064) and (TSH >= 0.018) and (Age <= 0.67) and (Thyroid_surgery <= 0)|1 (51.0/0.0)
(FTI <= 0.061) and (TSH >= 0.0062) and (T3 <= 0.01) and (Age >= 0.52)|1 (10.0/0.0)
(FTI <= 0.064) and (TSH >= 0.0062) and (FTI >= 0.051)|1 (14.0/4.0)
(TSH >= 0.0061) and (On_thyroxine <= 0) and (T3 <= 0.02) and (FTI >= 0.069) and (Thyroid_surgery <= 0) and (TT4 <= 0.148)|2 (240.0/0.0)
(TSH >= 0.0061) and (On_thyroxine <= 0) and (T3 >= 0.0208) and (TT4 <= 0.141) and (T3 <= 0.028) and (On_antithyroid_medication <= 0)|2 (68.0/0.0)
(TSH >= 0.0063) and (On_thyroxine <= 0) and (FTI <= 0.092) and (TT4 >= 0.06) and (Thyroid_surgery <= 0) and (T3 <= 0.019)|2 (13.0/0.0)
|3 (6007.0/11.0)


## PART

Decision list:

rules | predicted class
---|---
TSH <= 0.00605|3 (5837.0)
FTI <= 0.064255 AND Thyroid_surgery <= 0.5 AND T3 <= 0.0235|1 (145.0/5.0)
On_thyroxine <= 0.5 AND FTI > 0.062965 AND TT4 <= 0.1495 AND TT4 > 0.0615 AND T3 <= 0.0285 AND Age > 0.425|2 (234.0/2.0)
On_thyroxine > 0.5|3 (105.0/1.0)
FTI > 0.062965 AND TT4 <= 0.1485 AND Thyroid_surgery <= 0.5 AND Age <= 0.56|2 (96.0/4.0)
FTI > 0.06 AND Sex <= 0.5 AND Age <= 0.775|3 (33.0)
TSH <= 0.0195 AND T3 > 0.01755|3 (10.0/2.0)
TSH > 0.019395|1 (14.0/6.0)
|2 (5.0/1.0)


## SimpleCart Decision Tree

* TSH < 0.00605: 3(5837.0/0.0)
* TSH >= 0.00605
	* FTI < 0.064255
		* T3 < 0.0265
			* Thyroid_surgery < 0.5
				* On_antithyroid_medication < 0.5
					* TSH < 0.009545000000000001
						* TT4 < 0.0595: 1(9.0/0.0)
						* TT4 >= 0.0595: 3(3.0/0.0)
					* TSH >= 0.009545000000000001
						* I131_treatment < 0.5: 1(131.0/0.0)
						* I131_treatment >= 0.5
							* Age < 0.655: 1(4.0/0.0)
							* Age >= 0.655: 3(2.0/0.0)
				* On_antithyroid_medication >= 0.5: 3(2.0/1.0)
			* Thyroid_surgery >= 0.5
				* T4U < 0.131: 1(4.0/1.0)
				* T4U >= 0.131: 3(3.0/0.0)
		* T3 >= 0.0265: 3(5.0/0.0)
	* FTI >= 0.064255
		* On_thyroxine < 0.5
			* TT4 < 0.1495
				* Thyroid_surgery < 0.5
					* TT4 < 0.058499999999999996
						* T3 < 0.01755: 2(4.0/1.0)
						* T3 >= 0.01755: 3(6.0/0.0)
					* TT4 >= 0.058499999999999996
						* T3 < 0.0295: 2(319.0/1.0)
						* T3 >= 0.0295
							* T4U < 0.113: 3(5.0/0.0)
							* T4U >= 0.113: 2(7.0/0.0)
				* Thyroid_surgery >= 0.5: 3(10.0/0.0)
			* TT4 >= 0.1495: 3(22.0/0.0)
		* On_thyroxine >= 0.5: 3(102.0/0.0)


