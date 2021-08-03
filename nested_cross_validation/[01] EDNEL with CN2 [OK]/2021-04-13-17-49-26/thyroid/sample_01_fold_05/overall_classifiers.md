# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| TSH < 0.00605 | 3 | 0.924003 |
| TSH >= 0.00605 and FTI >= 0.064255 and On_thyroxine < 0.5 and TT4 < 0.1505 | 2 | 0.048035 |
| TSH >= 0.00605 and FTI < 0.064255 | 1 | 0.021218 |
| TSH >= 0.00605 and FTI >= 0.064255 and On_thyroxine >= 0.5 | 3 | 0.178082 |
| On_thyroxine <= 0.5 and Thyroid_surgery <= 0.5 and Query_hyperthyroid = all and Tumor = all and Hypopituitary = all and TSH > 0.00605 and TSH <= 0.0195 and FTI > 0.14225 | 3 | 0.010124 |
| On_thyroxine <= 0.5 and Thyroid_surgery > 0.5 and Query_hyperthyroid = all and Tumor = all and Hypopituitary = all and TSH > 0.00605 and TSH <= 0.0195 and FTI > 0.09753 and FTI <= 0.14225 | 3 | 0.006211 |
| TSH > 0.00605 and FTI > 0.064255 and On_thyroxine <= 0.5 and TT4 > 0.1495 | 3 | 0.047695 |
| On_thyroxine <= 0.5 and Thyroid_surgery > 0.5 and Query_hyperthyroid = all and Tumor = all and Hypopituitary = all and TSH > 0.00605 and TSH <= 0.0195 and FTI > 0.08104 and FTI <= 0.09753 | 3 | 0.008264 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| TSH <= 0.006 | 3 | 0.924003 |
| FTI <= 0.064 and T3 <= 0.025 and Thyroid_surgery <= 0.0 and TSH > 0.0095 | 1 | 0.213422 |
| On_thyroxine <= 0.0 and FTI > 0.062 and TT4 <= 0.15 and TT4 > 0.06 and T3 <= 0.03 and Age > 0.42 | 2 | 0.566910 |
| FTI <= 0.062 and On_thyroxine <= 0.0 and On_antithyroid_medication <= 0.0 and T4U <= 0.127 | 1 | 0.038207 |
| On_thyroxine > 0.0 | 3 | 0.524510 |
| TT4 <= 0.15 and Thyroid_surgery <= 0.0 and TT4 > 0.058 | 2 | 0.600284 |
| T3 > 0.011 | 3 | 0.912606 |
|  | 2 | 0.555556 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| FTI <= 0.064 and TSH >= 0.01 | 1 | 0.020494 |
| FTI <= 0.064 and TSH >= 0.0062 | 1 | 0.000659 |
| TSH >= 0.0061 and On_thyroxine <= 0 and TT4 <= 0.15 and Thyroid_surgery <= 0 | 2 | 0.049443 |
|  | 3 | 1.000000 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

on_thyroxine|thyroid_surgery|query_hyperthyroid|tumor|hypopituitary|tsh|fti|class
---|---|---|---|---|---|---|---
(0.5-inf)|(-inf-0.5]|all|all|all|(0.0195-0.0415]|(0.14225-inf)|1
(-inf-0.5]|(-inf-0.5]|all|all|all|(0.0195-0.0415]|(0.14225-inf)|3
(0.5-inf)|(-inf-0.5]|all|all|all|(0.0415-inf)|(0.09753-0.14225]|3
(0.5-inf)|(-inf-0.5]|all|all|all|(0.00605-0.0195]|(0.14225-inf)|3
(-inf-0.5]|(-inf-0.5]|all|all|all|(0.00605-0.0195]|(0.14225-inf)|3
(0.5-inf)|(-inf-0.5]|all|all|all|(0.0195-0.0415]|(0.09753-0.14225]|3
(-inf-0.5]|(-inf-0.5]|all|all|all|(0.0195-0.0415]|(0.09753-0.14225]|2
(-inf-0.5]|(-inf-0.5]|all|all|all|(0.0415-inf)|(0.08104-0.09753]|2
(0.5-inf)|(0.5-inf)|all|all|all|(-inf-0.00605]|(0.14225-inf)|3
(-inf-0.5]|(0.5-inf)|all|all|all|(-inf-0.00605]|(0.14225-inf)|3
(-inf-0.5]|(0.5-inf)|all|all|all|(0.00605-0.0195]|(0.09753-0.14225]|3
(0.5-inf)|(-inf-0.5]|all|all|all|(-inf-0.00605]|(0.14225-inf)|3
(-inf-0.5]|(-inf-0.5]|all|all|all|(-inf-0.00605]|(0.14225-inf)|3
(-inf-0.5]|(0.5-inf)|all|all|all|(0.0195-0.0415]|(0.08104-0.09753]|1
(0.5-inf)|(0.5-inf)|all|all|all|(0.0195-0.0415]|(0.08104-0.09753]|1
(-inf-0.5]|(-inf-0.5]|all|all|all|(0.00605-0.0195]|(0.09753-0.14225]|2
(0.5-inf)|(-inf-0.5]|all|all|all|(0.00605-0.0195]|(0.09753-0.14225]|3
(0.5-inf)|(-inf-0.5]|all|all|all|(0.0195-0.0415]|(0.08104-0.09753]|3
(-inf-0.5]|(-inf-0.5]|all|all|all|(0.0195-0.0415]|(0.08104-0.09753]|2
(-inf-0.5]|(-inf-0.5]|all|all|all|(0.0415-inf)|(0.064255-0.08104]|2
(0.5-inf)|(-inf-0.5]|all|all|all|(0.0415-inf)|(0.064255-0.08104]|3
(-inf-0.5]|(0.5-inf)|all|all|all|(-inf-0.00605]|(0.09753-0.14225]|3
(0.5-inf)|(0.5-inf)|all|all|all|(-inf-0.00605]|(0.09753-0.14225]|3
(-inf-0.5]|(0.5-inf)|all|all|all|(0.00605-0.0195]|(0.08104-0.09753]|3
(0.5-inf)|(-inf-0.5]|all|all|all|(-inf-0.00605]|(0.09753-0.14225]|3
(-inf-0.5]|(-inf-0.5]|all|all|all|(-inf-0.00605]|(0.09753-0.14225]|3
(-inf-0.5]|(-inf-0.5]|all|all|all|(0.00605-0.0195]|(0.08104-0.09753]|2
(0.5-inf)|(-inf-0.5]|all|all|all|(0.00605-0.0195]|(0.08104-0.09753]|3
(0.5-inf)|(-inf-0.5]|all|all|all|(0.0195-0.0415]|(0.064255-0.08104]|3
(-inf-0.5]|(0.5-inf)|all|all|all|(0.0415-inf)|(0.0345-0.064255]|1
(-inf-0.5]|(-inf-0.5]|all|all|all|(0.0195-0.0415]|(0.064255-0.08104]|2
(0.5-inf)|(-inf-0.5]|all|all|all|(0.0415-inf)|(0.0345-0.064255]|1
(-inf-0.5]|(-inf-0.5]|all|all|all|(0.0415-inf)|(0.0345-0.064255]|1
(-inf-0.5]|(0.5-inf)|all|all|all|(-inf-0.00605]|(0.08104-0.09753]|3
(-inf-0.5]|(0.5-inf)|all|all|all|(0.00605-0.0195]|(0.064255-0.08104]|1
(0.5-inf)|(-inf-0.5]|all|all|all|(-inf-0.00605]|(0.08104-0.09753]|3
(-inf-0.5]|(-inf-0.5]|all|all|all|(-inf-0.00605]|(0.08104-0.09753]|3
(-inf-0.5]|(0.5-inf)|all|all|all|(0.0195-0.0415]|(0.0345-0.064255]|1
(0.5-inf)|(-inf-0.5]|all|all|all|(0.00605-0.0195]|(0.064255-0.08104]|3
(-inf-0.5]|(-inf-0.5]|all|all|all|(0.00605-0.0195]|(0.064255-0.08104]|2
(-inf-0.5]|(-inf-0.5]|all|all|all|(0.0195-0.0415]|(0.0345-0.064255]|1
(0.5-inf)|(-inf-0.5]|all|all|all|(0.0195-0.0415]|(0.0345-0.064255]|1
(-inf-0.5]|(0.5-inf)|all|all|all|(0.0415-inf)|(0.0135-0.0345]|1
(0.5-inf)|(-inf-0.5]|all|all|all|(0.0415-inf)|(0.0135-0.0345]|1
(-inf-0.5]|(-inf-0.5]|all|all|all|(0.0415-inf)|(0.0135-0.0345]|1
(-inf-0.5]|(0.5-inf)|all|all|all|(-inf-0.00605]|(0.064255-0.08104]|3
(-inf-0.5]|(0.5-inf)|all|all|all|(0.00605-0.0195]|(0.0345-0.064255]|1
(0.5-inf)|(-inf-0.5]|all|all|all|(-inf-0.00605]|(0.064255-0.08104]|3
(-inf-0.5]|(-inf-0.5]|all|all|all|(-inf-0.00605]|(0.064255-0.08104]|3
(-inf-0.5]|(0.5-inf)|all|all|all|(0.0195-0.0415]|(0.0135-0.0345]|1
(0.5-inf)|(-inf-0.5]|all|all|all|(0.00605-0.0195]|(0.0345-0.064255]|1
(-inf-0.5]|(-inf-0.5]|all|all|all|(0.00605-0.0195]|(0.0345-0.064255]|1
(-inf-0.5]|(-inf-0.5]|all|all|all|(0.0195-0.0415]|(0.0135-0.0345]|1
(-inf-0.5]|(0.5-inf)|all|all|all|(0.0415-inf)|(-inf-0.0135]|1
(0.5-inf)|(-inf-0.5]|all|all|all|(0.0415-inf)|(-inf-0.0135]|1
(-inf-0.5]|(-inf-0.5]|all|all|all|(0.0415-inf)|(-inf-0.0135]|1
(-inf-0.5]|(0.5-inf)|all|all|all|(-inf-0.00605]|(0.0345-0.064255]|1
(0.5-inf)|(-inf-0.5]|all|all|all|(-inf-0.00605]|(0.0345-0.064255]|3
(-inf-0.5]|(-inf-0.5]|all|all|all|(-inf-0.00605]|(0.0345-0.064255]|3
(-inf-0.5]|(-inf-0.5]|all|all|all|(0.00605-0.0195]|(0.0135-0.0345]|1
(-inf-0.5]|(-inf-0.5]|all|all|all|(0.0195-0.0415]|(-inf-0.0135]|1
(-inf-0.5]|(-inf-0.5]|all|all|all|(-inf-0.00605]|(0.0135-0.0345]|3
(-inf-0.5]|(-inf-0.5]|all|all|all|(-inf-0.00605]|(-inf-0.0135]|1

## JRip

Decision list:

rules | predicted class
---|---
(FTI <= 0.064) and (TSH >= 0.01)|1 (148.0/8.0)
(FTI <= 0.064) and (TSH >= 0.0062)|1 (16.0/6.0)
(TSH >= 0.0061) and (On_thyroxine <= 0) and (TT4 <= 0.15) and (Thyroid_surgery <= 0)|2 (342.0/12.0)
|3 (5974.0/0.0)


## PART

Decision list:

rules | predicted class
---|---
TSH <= 0.006|3 (5008.0)
FTI <= 0.064 AND T3 <= 0.025 AND Thyroid_surgery <= 0.0 AND TSH > 0.0095|1 (118.0/1.0)
On_thyroxine <= 0.0 AND FTI > 0.062 AND TT4 <= 0.15 AND TT4 > 0.06 AND T3 <= 0.03 AND Age > 0.42|2 (197.0)
FTI <= 0.062 AND On_thyroxine <= 0.0 AND On_antithyroid_medication <= 0.0 AND T4U <= 0.127|1 (13.0/1.0)
On_thyroxine > 0.0|3 (91.0)
TT4 <= 0.15 AND Thyroid_surgery <= 0.0 AND TT4 > 0.058|2 (89.0/6.0)
T3 > 0.011|3 (34.0)
|2 (5.0/2.0)


## J48 Decision Tree

* TSH <= 0.00605: 3 (5189.0)
* TSH > 0.00605
	* FTI <= 0.064255: 1 (145.0/12.0)
	* FTI > 0.064255
		* On_thyroxine <= 0.5
			* TT4 <= 0.1495: 2 (308.0/15.0)
			* TT4 > 0.1495: 3 (23.0)
		* On_thyroxine > 0.5: 3 (95.0)


## SimpleCart Decision Tree

* TSH < 0.00605: 3(5836.0/0.0)
* TSH >= 0.00605
	* FTI < 0.064255: 1(150.0/14.0)
	* FTI >= 0.064255
		* On_thyroxine < 0.5
			* TT4 < 0.1505: 2(330.0/21.0)
			* TT4 >= 0.1505: 3(25.0/0.0)
		* On_thyroxine >= 0.5: 3(104.0/0.0)


