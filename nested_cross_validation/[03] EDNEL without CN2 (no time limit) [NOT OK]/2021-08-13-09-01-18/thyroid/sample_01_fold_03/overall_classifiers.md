# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 3 | 0.926069 |
| TSH >= 0.00605 and FTI >= 0.064255 and On_thyroxine < 0.5 and TT4 < 0.1495 and Thyroid_surgery < 0.5 and TT4 >= 0.058499999999999996 | 2 | 0.049483 |
| TSH >= 0.00605 and FTI < 0.064255 | 1 | 0.020819 |
| On_thyroxine <= 0.5 and Query_on_thyroxine = all and On_antithyroid_medication = all and Thyroid_surgery <= 0.5 and Query_hyperthyroid = all and Lithium = all and Goitre <= 0.5 and Tumor = all and Hypopituitary = all and TSH > 0.00605 and TSH <= 0.0195 and FTI > 0.08308 and FTI <= 0.097355 | 2 | 0.011275 |
| On_thyroxine <= 0.5 and Query_on_thyroxine = all and On_antithyroid_medication = all and Thyroid_surgery <= 0.5 and Query_hyperthyroid = all and Lithium = all and Goitre <= 0.5 and Tumor = all and Hypopituitary = all and TSH > 0.00605 and TSH <= 0.0195 and FTI > 0.064255 and FTI <= 0.08308 | 2 | 0.010197 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| TSH <= 0.006 | 3 | 0.924161 |
| FTI <= 0.064 and Thyroid_surgery <= 0.0 and T3 <= 0.023 | 1 | 0.215243 |
| On_thyroxine <= 0.0 and FTI > 0.062 and TT4 <= 0.149 and TT4 > 0.061 and T3 <= 0.028 and Age > 0.42 | 2 | 0.572182 |
| On_thyroxine > 0.0 | 3 | 0.492936 |
| FTI > 0.062 and TT4 <= 0.148 and Thyroid_surgery <= 0.0 and Age <= 0.56 | 2 | 0.568817 |
|  | 3 | 0.794521 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| FTI <= 0.064 and TSH >= 0.0062 | 1 | 0.020819 |
| TSH >= 0.0061 and On_thyroxine <= 0 and T3 <= 0.02 and Thyroid_surgery <= 0 and TT4 <= 0.148 | 2 | 0.039862 |
| TSH >= 0.0061 and T3 >= 0.0208 and TT4 <= 0.141 and On_thyroxine <= 0 | 2 | 0.011039 |
|  | 3 | 0.999833 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

on_thyroxine|query_on_thyroxine|on_antithyroid_medication|thyroid_surgery|query_hyperthyroid|lithium|goitre|tumor|hypopituitary|tsh|fti|class
---|---|---|---|---|---|---|---|---|---|---|---
(0.5-inf)|all|all|(-inf-0.5]|all|all|(-inf-0.5]|all|all|(0.0195-0.0415]|(0.14225-inf)|1
(-inf-0.5]|all|all|(-inf-0.5]|all|all|(-inf-0.5]|all|all|(0.0195-0.0415]|(0.14225-inf)|3
(0.5-inf)|all|all|(-inf-0.5]|all|all|(-inf-0.5]|all|all|(0.0415-inf)|(0.097355-0.14225]|3
(0.5-inf)|all|all|(-inf-0.5]|all|all|(-inf-0.5]|all|all|(0.00605-0.0195]|(0.14225-inf)|3
(-inf-0.5]|all|all|(-inf-0.5]|all|all|(-inf-0.5]|all|all|(0.00605-0.0195]|(0.14225-inf)|3
(0.5-inf)|all|all|(-inf-0.5]|all|all|(-inf-0.5]|all|all|(0.0195-0.0415]|(0.097355-0.14225]|3
(-inf-0.5]|all|all|(-inf-0.5]|all|all|(-inf-0.5]|all|all|(0.0195-0.0415]|(0.097355-0.14225]|2
(-inf-0.5]|all|all|(-inf-0.5]|all|all|(-inf-0.5]|all|all|(0.0415-inf)|(0.08308-0.097355]|2
(0.5-inf)|all|all|(-inf-0.5]|all|all|(0.5-inf)|all|all|(-inf-0.00605]|(0.14225-inf)|1
(-inf-0.5]|all|all|(-inf-0.5]|all|all|(0.5-inf)|all|all|(-inf-0.00605]|(0.14225-inf)|3
(0.5-inf)|all|all|(0.5-inf)|all|all|(-inf-0.5]|all|all|(-inf-0.00605]|(0.14225-inf)|3
(-inf-0.5]|all|all|(0.5-inf)|all|all|(-inf-0.5]|all|all|(-inf-0.00605]|(0.14225-inf)|3
(-inf-0.5]|all|all|(0.5-inf)|all|all|(-inf-0.5]|all|all|(0.00605-0.0195]|(0.097355-0.14225]|3
(0.5-inf)|all|all|(0.5-inf)|all|all|(-inf-0.5]|all|all|(0.0195-0.0415]|(0.08308-0.097355]|1
(-inf-0.5]|all|all|(0.5-inf)|all|all|(-inf-0.5]|all|all|(0.0195-0.0415]|(0.08308-0.097355]|1
(0.5-inf)|all|all|(-inf-0.5]|all|all|(-inf-0.5]|all|all|(-inf-0.00605]|(0.14225-inf)|3
(-inf-0.5]|all|all|(-inf-0.5]|all|all|(-inf-0.5]|all|all|(-inf-0.00605]|(0.14225-inf)|3
(0.5-inf)|all|all|(-inf-0.5]|all|all|(-inf-0.5]|all|all|(0.00605-0.0195]|(0.097355-0.14225]|3
(-inf-0.5]|all|all|(-inf-0.5]|all|all|(-inf-0.5]|all|all|(0.00605-0.0195]|(0.097355-0.14225]|2
(0.5-inf)|all|all|(-inf-0.5]|all|all|(-inf-0.5]|all|all|(0.0195-0.0415]|(0.08308-0.097355]|3
(-inf-0.5]|all|all|(-inf-0.5]|all|all|(-inf-0.5]|all|all|(0.0195-0.0415]|(0.08308-0.097355]|2
(0.5-inf)|all|all|(-inf-0.5]|all|all|(-inf-0.5]|all|all|(0.0415-inf)|(0.064255-0.08308]|3
(-inf-0.5]|all|all|(-inf-0.5]|all|all|(-inf-0.5]|all|all|(0.0415-inf)|(0.064255-0.08308]|2
(0.5-inf)|all|all|(-inf-0.5]|all|all|(0.5-inf)|all|all|(-inf-0.00605]|(0.097355-0.14225]|3
(-inf-0.5]|all|all|(-inf-0.5]|all|all|(0.5-inf)|all|all|(-inf-0.00605]|(0.097355-0.14225]|3
(-inf-0.5]|all|all|(-inf-0.5]|all|all|(0.5-inf)|all|all|(0.00605-0.0195]|(0.08308-0.097355]|1
(0.5-inf)|all|all|(0.5-inf)|all|all|(-inf-0.5]|all|all|(-inf-0.00605]|(0.097355-0.14225]|3
(-inf-0.5]|all|all|(0.5-inf)|all|all|(-inf-0.5]|all|all|(-inf-0.00605]|(0.097355-0.14225]|3
(-inf-0.5]|all|all|(0.5-inf)|all|all|(-inf-0.5]|all|all|(0.00605-0.0195]|(0.08308-0.097355]|3
(-inf-0.5]|all|all|(0.5-inf)|all|all|(-inf-0.5]|all|all|(0.0415-inf)|(0.0345-0.064255]|1
(0.5-inf)|all|all|(-inf-0.5]|all|all|(-inf-0.5]|all|all|(-inf-0.00605]|(0.097355-0.14225]|3
(-inf-0.5]|all|all|(-inf-0.5]|all|all|(-inf-0.5]|all|all|(-inf-0.00605]|(0.097355-0.14225]|3
(0.5-inf)|all|all|(-inf-0.5]|all|all|(-inf-0.5]|all|all|(0.00605-0.0195]|(0.08308-0.097355]|3
(-inf-0.5]|all|all|(-inf-0.5]|all|all|(-inf-0.5]|all|all|(0.00605-0.0195]|(0.08308-0.097355]|2
(0.5-inf)|all|all|(-inf-0.5]|all|all|(-inf-0.5]|all|all|(0.0195-0.0415]|(0.064255-0.08308]|3
(-inf-0.5]|all|all|(-inf-0.5]|all|all|(-inf-0.5]|all|all|(0.0195-0.0415]|(0.064255-0.08308]|2
(0.5-inf)|all|all|(-inf-0.5]|all|all|(-inf-0.5]|all|all|(0.0415-inf)|(0.0345-0.064255]|1
(-inf-0.5]|all|all|(-inf-0.5]|all|all|(-inf-0.5]|all|all|(0.0415-inf)|(0.0345-0.064255]|1
(-inf-0.5]|all|all|(-inf-0.5]|all|all|(0.5-inf)|all|all|(-inf-0.00605]|(0.08308-0.097355]|3
(-inf-0.5]|all|all|(0.5-inf)|all|all|(-inf-0.5]|all|all|(-inf-0.00605]|(0.08308-0.097355]|3
(-inf-0.5]|all|all|(0.5-inf)|all|all|(-inf-0.5]|all|all|(0.00605-0.0195]|(0.064255-0.08308]|3
(-inf-0.5]|all|all|(0.5-inf)|all|all|(-inf-0.5]|all|all|(0.0195-0.0415]|(0.0345-0.064255]|1
(-inf-0.5]|all|all|(0.5-inf)|all|all|(-inf-0.5]|all|all|(0.0415-inf)|(-inf-0.0345]|1
(0.5-inf)|all|all|(-inf-0.5]|all|all|(-inf-0.5]|all|all|(-inf-0.00605]|(0.08308-0.097355]|3
(-inf-0.5]|all|all|(-inf-0.5]|all|all|(-inf-0.5]|all|all|(-inf-0.00605]|(0.08308-0.097355]|3
(0.5-inf)|all|all|(-inf-0.5]|all|all|(-inf-0.5]|all|all|(0.00605-0.0195]|(0.064255-0.08308]|3
(-inf-0.5]|all|all|(-inf-0.5]|all|all|(-inf-0.5]|all|all|(0.00605-0.0195]|(0.064255-0.08308]|2
(0.5-inf)|all|all|(-inf-0.5]|all|all|(-inf-0.5]|all|all|(0.0195-0.0415]|(0.0345-0.064255]|1
(-inf-0.5]|all|all|(-inf-0.5]|all|all|(-inf-0.5]|all|all|(0.0195-0.0415]|(0.0345-0.064255]|1
(0.5-inf)|all|all|(-inf-0.5]|all|all|(-inf-0.5]|all|all|(0.0415-inf)|(-inf-0.0345]|1
(-inf-0.5]|all|all|(-inf-0.5]|all|all|(-inf-0.5]|all|all|(0.0415-inf)|(-inf-0.0345]|1
(-inf-0.5]|all|all|(-inf-0.5]|all|all|(0.5-inf)|all|all|(-inf-0.00605]|(0.064255-0.08308]|3
(0.5-inf)|all|all|(-inf-0.5]|all|all|(0.5-inf)|all|all|(-inf-0.00605]|(0.064255-0.08308]|3
(-inf-0.5]|all|all|(0.5-inf)|all|all|(-inf-0.5]|all|all|(-inf-0.00605]|(0.064255-0.08308]|3
(-inf-0.5]|all|all|(0.5-inf)|all|all|(-inf-0.5]|all|all|(0.00605-0.0195]|(0.0345-0.064255]|1
(-inf-0.5]|all|all|(0.5-inf)|all|all|(-inf-0.5]|all|all|(0.0195-0.0415]|(-inf-0.0345]|1
(0.5-inf)|all|all|(-inf-0.5]|all|all|(-inf-0.5]|all|all|(-inf-0.00605]|(0.064255-0.08308]|3
(-inf-0.5]|all|all|(-inf-0.5]|all|all|(-inf-0.5]|all|all|(-inf-0.00605]|(0.064255-0.08308]|3
(-inf-0.5]|all|all|(-inf-0.5]|all|all|(-inf-0.5]|all|all|(0.00605-0.0195]|(0.0345-0.064255]|1
(0.5-inf)|all|all|(-inf-0.5]|all|all|(-inf-0.5]|all|all|(0.00605-0.0195]|(0.0345-0.064255]|1
(-inf-0.5]|all|all|(-inf-0.5]|all|all|(-inf-0.5]|all|all|(0.0195-0.0415]|(-inf-0.0345]|1
(-inf-0.5]|all|all|(-inf-0.5]|all|all|(0.5-inf)|all|all|(-inf-0.00605]|(0.0345-0.064255]|3
(-inf-0.5]|all|all|(0.5-inf)|all|all|(-inf-0.5]|all|all|(-inf-0.00605]|(0.0345-0.064255]|3
(0.5-inf)|all|all|(-inf-0.5]|all|all|(-inf-0.5]|all|all|(-inf-0.00605]|(0.0345-0.064255]|3
(-inf-0.5]|all|all|(-inf-0.5]|all|all|(-inf-0.5]|all|all|(-inf-0.00605]|(0.0345-0.064255]|3
(-inf-0.5]|all|all|(-inf-0.5]|all|all|(-inf-0.5]|all|all|(0.00605-0.0195]|(-inf-0.0345]|1
(-inf-0.5]|all|all|(-inf-0.5]|all|all|(-inf-0.5]|all|all|(-inf-0.00605]|(-inf-0.0345]|3

## JRip

Decision list:

rules | predicted class
---|---
(FTI <= 0.064) and (TSH >= 0.0062)|1 (165.0/16.0)
(TSH >= 0.0061) and (On_thyroxine <= 0) and (T3 <= 0.02) and (Thyroid_surgery <= 0) and (TT4 <= 0.148)|2 (255.0/1.0)
(TSH >= 0.0061) and (T3 >= 0.0208) and (TT4 <= 0.141) and (On_thyroxine <= 0)|2 (79.0/4.0)
|3 (5980.0/1.0)


## PART

Decision list:

rules | predicted class
---|---
TSH <= 0.006|3 (5837.0)
FTI <= 0.064 AND Thyroid_surgery <= 0.0 AND T3 <= 0.023|1 (145.0/5.0)
On_thyroxine <= 0.0 AND FTI > 0.062 AND TT4 <= 0.149 AND TT4 > 0.061 AND T3 <= 0.028 AND Age > 0.42|2 (234.0/2.0)
On_thyroxine > 0.0|3 (105.0/1.0)
FTI > 0.062 AND TT4 <= 0.148 AND Thyroid_surgery <= 0.0 AND Age <= 0.56|2 (96.0/4.0)
|3 (62.0/14.0)


## J48 Decision Tree

* TSH <= 0.00605: 3 (5837.0)
* TSH > 0.00605
	* FTI <= 0.064255
		* Thyroid_surgery <= 0.5
			* T3 <= 0.0235: 1 (145.0/5.0)
			* T3 > 0.0235
				* T3 <= 0.0265: 1 (7.0/2.0)
				* T3 > 0.0265: 3 (5.0)
		* Thyroid_surgery > 0.5
			* T3 <= 0.0108: 1 (4.0/1.0)
			* T3 > 0.0108: 3 (4.0/1.0)
	* FTI > 0.064255
		* On_thyroxine <= 0.5
			* TT4 <= 0.1495
				* TT4 <= 0.0615
					* T3 <= 0.01955: 2 (10.0/1.0)
					* T3 > 0.01955: 3 (7.0)
				* TT4 > 0.0615
					* T3 <= 0.0285
						* Age <= 0.425
							* Thyroid_surgery <= 0.5: 2 (81.0)
							* Thyroid_surgery > 0.5: 3 (9.0)
						* Age > 0.425: 2 (234.0/2.0)
					* T3 > 0.0285
						* T4U <= 0.113: 3 (5.0/1.0)
						* T4U > 0.113: 2 (7.0)
			* TT4 > 0.1495: 3 (22.0)
		* On_thyroxine > 0.5: 3 (102.0)


## SimpleCart Decision Tree

* TSH < 0.00605: 3(5837.0/0.0)
* TSH >= 0.00605
	* FTI < 0.064255: 1(149.0/16.0)
	* FTI >= 0.064255
		* On_thyroxine < 0.5
			* TT4 < 0.1495
				* Thyroid_surgery < 0.5
					* TT4 < 0.058499999999999996: 3(7.0/4.0)
					* TT4 >= 0.058499999999999996: 2(326.0/6.0)
				* Thyroid_surgery >= 0.5: 3(10.0/0.0)
			* TT4 >= 0.1495: 3(22.0/0.0)
		* On_thyroxine >= 0.5: 3(102.0/0.0)


