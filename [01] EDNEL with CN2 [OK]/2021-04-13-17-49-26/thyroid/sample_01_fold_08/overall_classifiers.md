# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 3 | 0.926069 |
| TSH >= 0.00605 and FTI >= 0.064465 and On_thyroxine < 0.5 and TT4 < 0.1505 | 2 | 0.048042 |
| On_thyroxine <= 0.5 and Query_on_thyroxine = all and Thyroid_surgery <= 0.5 and I131_treatment = all and Query_hyperthyroid = all and TSH > 0.00605 and TSH <= 0.0195 and FTI > 0.0345 and FTI <= 0.064465 | 1 | 0.001546 |
| On_thyroxine <= 0.5 and Query_on_thyroxine = all and Thyroid_surgery <= 0.5 and I131_treatment = all and Query_hyperthyroid = all and TSH > 0.0415 and FTI > 0.0345 and FTI <= 0.064465 | 1 | 0.002843 |
| On_thyroxine <= 0.5 and Query_on_thyroxine = all and Thyroid_surgery > 0.5 and I131_treatment = all and Query_hyperthyroid = all and TSH > 0.0415 and FTI <= 0.0165 | 1 | 0.000158 |
| On_thyroxine <= 0.5 and Query_on_thyroxine = all and Thyroid_surgery <= 0.5 and I131_treatment = all and Query_hyperthyroid = all and TSH > 0.0415 and FTI > 0.0165 and FTI <= 0.0345 | 1 | 0.003777 |
| On_thyroxine <= 0.5 and Query_on_thyroxine = all and Thyroid_surgery <= 0.5 and I131_treatment = all and Query_hyperthyroid = all and TSH > 0.00605 and TSH <= 0.0195 and FTI > 0.0165 and FTI <= 0.0345 | 1 | 0.000316 |
| On_thyroxine > 0.5 and Query_on_thyroxine = all and Thyroid_surgery <= 0.5 and I131_treatment = all and Query_hyperthyroid = all and TSH > 0.0415 and FTI <= 0.0165 | 1 | 0.000316 |
| On_thyroxine <= 0.5 and Query_on_thyroxine = all and Thyroid_surgery <= 0.5 and I131_treatment = all and Query_hyperthyroid = all and TSH > 0.0195 and TSH <= 0.0415 and FTI > 0.0165 and FTI <= 0.0345 | 1 | 0.000316 |
| TSH >= 0.00605 and FTI < 0.064465 | 1 | 0.021068 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| TSH <= 0.00605 | 3 | 0.924197 |
| FTI <= 0.064465 and Thyroid_surgery <= 0.5 and T3 <= 0.0235 and TSH > 0.016895 and Age <= 0.76 | 1 | 0.180602 |
| FTI <= 0.063465 and Age > 0.275 and TSH <= 0.0895 and T4U <= 0.108 and FTI > 0.0475 | 1 | 0.029703 |
| FTI > 0.062965 and On_thyroxine <= 0.5 and TT4 <= 0.1505 and TT4 > 0.0615 and T3 <= 0.0295 and Age > 0.425 and TT4 <= 0.14 and T4U <= 0.1285 | 2 | 0.540741 |
| FTI <= 0.0605 and Age > 0.79 | 1 | 0.039007 |
| FTI > 0.0605 and On_thyroxine > 0.5 | 3 | 0.447368 |
| FTI > 0.062965 and TT4 <= 0.1505 and Thyroid_surgery <= 0.5 and TT4 > 0.0585 and T3 <= 0.029 and Age <= 0.765 | 2 | 0.565476 |
| FTI > 0.0605 and TT4 > 0.1495 | 3 | 0.425926 |
| TT4 > 0.1245 and Age <= 0.565 | 2 | 0.122807 |
| FTI > 0.0605 and T3 > 0.0177 and Age <= 0.745 | 3 | 0.384615 |
| FTI > 0.063 and TT4 > 0.0605 and TT4 <= 0.116 | 3 | 0.200000 |
| FTI > 0.063 and TSH <= 0.008995 | 2 | 0.100000 |
| FTI <= 0.068 and Age > 0.275 and T4U > 0.1145 and Age > 0.47 | 1 | 0.269231 |
| FTI <= 0.068 and TSH <= 0.0895 and Age <= 0.38 | 1 | 0.105263 |
| FTI <= 0.068 and TSH <= 0.0895 | 3 | 0.571429 |
| TSH <= 0.061 | 2 | 0.416667 |
|  | 1 | 0.666667 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| FTI <= 0.064 and TSH >= 0.0062 | 1 | 0.021068 |
| TSH >= 0.0061 and On_thyroxine <= 0 and T3 <= 0.019 | 2 | 0.037163 |
| TSH >= 0.0061 and On_thyroxine <= 0 and TT4 <= 0.146 | 2 | 0.010353 |
|  | 3 | 0.999833 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

on_thyroxine|query_on_thyroxine|thyroid_surgery|i131_treatment|query_hyperthyroid|tsh|fti|class
---|---|---|---|---|---|---|---
(0.5-inf)|all|(-inf-0.5]|all|all|(0.0195-0.0415]|(0.14225-inf)|1
(-inf-0.5]|all|(-inf-0.5]|all|all|(0.0195-0.0415]|(0.14225-inf)|3
(0.5-inf)|all|(-inf-0.5]|all|all|(0.0415-inf)|(0.097495-0.14225]|3
(0.5-inf)|all|(-inf-0.5]|all|all|(0.00605-0.0195]|(0.14225-inf)|3
(-inf-0.5]|all|(-inf-0.5]|all|all|(0.00605-0.0195]|(0.14225-inf)|3
(0.5-inf)|all|(-inf-0.5]|all|all|(0.0195-0.0415]|(0.097495-0.14225]|3
(-inf-0.5]|all|(-inf-0.5]|all|all|(0.0195-0.0415]|(0.097495-0.14225]|2
(0.5-inf)|all|(-inf-0.5]|all|all|(0.0415-inf)|(0.07794-0.097495]|1
(-inf-0.5]|all|(-inf-0.5]|all|all|(0.0415-inf)|(0.07794-0.097495]|2
(-inf-0.5]|all|(0.5-inf)|all|all|(-inf-0.00605]|(0.14225-inf)|3
(0.5-inf)|all|(0.5-inf)|all|all|(-inf-0.00605]|(0.14225-inf)|3
(-inf-0.5]|all|(0.5-inf)|all|all|(0.00605-0.0195]|(0.097495-0.14225]|3
(0.5-inf)|all|(0.5-inf)|all|all|(0.0195-0.0415]|(0.07794-0.097495]|1
(-inf-0.5]|all|(0.5-inf)|all|all|(0.0195-0.0415]|(0.07794-0.097495]|1
(0.5-inf)|all|(-inf-0.5]|all|all|(-inf-0.00605]|(0.14225-inf)|3
(-inf-0.5]|all|(-inf-0.5]|all|all|(-inf-0.00605]|(0.14225-inf)|3
(-inf-0.5]|all|(-inf-0.5]|all|all|(0.00605-0.0195]|(0.097495-0.14225]|2
(0.5-inf)|all|(-inf-0.5]|all|all|(0.00605-0.0195]|(0.097495-0.14225]|3
(-inf-0.5]|all|(-inf-0.5]|all|all|(0.0195-0.0415]|(0.07794-0.097495]|2
(0.5-inf)|all|(-inf-0.5]|all|all|(0.0195-0.0415]|(0.07794-0.097495]|3
(-inf-0.5]|all|(-inf-0.5]|all|all|(0.0415-inf)|(0.064465-0.07794]|2
(0.5-inf)|all|(-inf-0.5]|all|all|(0.0415-inf)|(0.064465-0.07794]|3
(0.5-inf)|all|(0.5-inf)|all|all|(-inf-0.00605]|(0.097495-0.14225]|3
(-inf-0.5]|all|(0.5-inf)|all|all|(-inf-0.00605]|(0.097495-0.14225]|3
(-inf-0.5]|all|(0.5-inf)|all|all|(0.00605-0.0195]|(0.07794-0.097495]|3
(0.5-inf)|all|(-inf-0.5]|all|all|(-inf-0.00605]|(0.097495-0.14225]|3
(-inf-0.5]|all|(-inf-0.5]|all|all|(-inf-0.00605]|(0.097495-0.14225]|3
(-inf-0.5]|all|(0.5-inf)|all|all|(0.0415-inf)|(0.0345-0.064465]|1
(-inf-0.5]|all|(-inf-0.5]|all|all|(0.00605-0.0195]|(0.07794-0.097495]|2
(0.5-inf)|all|(-inf-0.5]|all|all|(0.00605-0.0195]|(0.07794-0.097495]|3
(-inf-0.5]|all|(-inf-0.5]|all|all|(0.0195-0.0415]|(0.064465-0.07794]|2
(0.5-inf)|all|(-inf-0.5]|all|all|(0.0195-0.0415]|(0.064465-0.07794]|3
(0.5-inf)|all|(-inf-0.5]|all|all|(0.0415-inf)|(0.0345-0.064465]|1
(-inf-0.5]|all|(-inf-0.5]|all|all|(0.0415-inf)|(0.0345-0.064465]|1
(-inf-0.5]|all|(0.5-inf)|all|all|(-inf-0.00605]|(0.07794-0.097495]|3
(-inf-0.5]|all|(0.5-inf)|all|all|(0.00605-0.0195]|(0.064465-0.07794]|3
(-inf-0.5]|all|(0.5-inf)|all|all|(0.0195-0.0415]|(0.0345-0.064465]|1
(0.5-inf)|all|(-inf-0.5]|all|all|(-inf-0.00605]|(0.07794-0.097495]|3
(-inf-0.5]|all|(-inf-0.5]|all|all|(-inf-0.00605]|(0.07794-0.097495]|3
(-inf-0.5]|all|(0.5-inf)|all|all|(0.0415-inf)|(0.0165-0.0345]|3
(0.5-inf)|all|(-inf-0.5]|all|all|(0.00605-0.0195]|(0.064465-0.07794]|3
(-inf-0.5]|all|(-inf-0.5]|all|all|(0.00605-0.0195]|(0.064465-0.07794]|2
(0.5-inf)|all|(-inf-0.5]|all|all|(0.0195-0.0415]|(0.0345-0.064465]|1
(-inf-0.5]|all|(-inf-0.5]|all|all|(0.0195-0.0415]|(0.0345-0.064465]|1
(-inf-0.5]|all|(-inf-0.5]|all|all|(0.0415-inf)|(0.0165-0.0345]|1
(0.5-inf)|all|(-inf-0.5]|all|all|(0.0415-inf)|(0.0165-0.0345]|1
(-inf-0.5]|all|(0.5-inf)|all|all|(-inf-0.00605]|(0.064465-0.07794]|3
(-inf-0.5]|all|(0.5-inf)|all|all|(0.00605-0.0195]|(0.0345-0.064465]|1
(-inf-0.5]|all|(0.5-inf)|all|all|(0.0195-0.0415]|(0.0165-0.0345]|1
(0.5-inf)|all|(-inf-0.5]|all|all|(-inf-0.00605]|(0.064465-0.07794]|3
(-inf-0.5]|all|(-inf-0.5]|all|all|(-inf-0.00605]|(0.064465-0.07794]|3
(-inf-0.5]|all|(0.5-inf)|all|all|(0.0415-inf)|(-inf-0.0165]|1
(0.5-inf)|all|(-inf-0.5]|all|all|(0.00605-0.0195]|(0.0345-0.064465]|3
(-inf-0.5]|all|(-inf-0.5]|all|all|(0.00605-0.0195]|(0.0345-0.064465]|1
(-inf-0.5]|all|(-inf-0.5]|all|all|(0.0195-0.0415]|(0.0165-0.0345]|1
(0.5-inf)|all|(-inf-0.5]|all|all|(0.0415-inf)|(-inf-0.0165]|1
(-inf-0.5]|all|(-inf-0.5]|all|all|(0.0415-inf)|(-inf-0.0165]|1
(-inf-0.5]|all|(0.5-inf)|all|all|(-inf-0.00605]|(0.0345-0.064465]|3
(0.5-inf)|all|(-inf-0.5]|all|all|(-inf-0.00605]|(0.0345-0.064465]|3
(-inf-0.5]|all|(-inf-0.5]|all|all|(-inf-0.00605]|(0.0345-0.064465]|3
(-inf-0.5]|all|(-inf-0.5]|all|all|(0.00605-0.0195]|(0.0165-0.0345]|1
(-inf-0.5]|all|(-inf-0.5]|all|all|(0.0195-0.0415]|(-inf-0.0165]|1
(-inf-0.5]|all|(-inf-0.5]|all|all|(-inf-0.00605]|(0.0165-0.0345]|3
(-inf-0.5]|all|(-inf-0.5]|all|all|(-inf-0.00605]|(-inf-0.0165]|1

## JRip

Decision list:

rules | predicted class
---|---
(FTI <= 0.064) and (TSH >= 0.0062)|1 (163.0/14.0)
(TSH >= 0.0061) and (On_thyroxine <= 0) and (T3 <= 0.019)|2 (249.0/6.0)
(TSH >= 0.0061) and (On_thyroxine <= 0) and (TT4 <= 0.146)|2 (101.0/15.0)
|3 (5966.0/1.0)


## PART

Decision list:

rules | predicted class
---|---
TSH <= 0.00605|3 (5840.0)
FTI <= 0.064465 AND Thyroid_surgery <= 0.5 AND T3 <= 0.0235 AND TSH > 0.016895 AND Age <= 0.76|1 (108.0)
FTI <= 0.063465 AND Age > 0.275 AND TSH <= 0.0895 AND T4U <= 0.108 AND FTI > 0.0475|1 (15.0)
FTI > 0.062965 AND On_thyroxine <= 0.5 AND TT4 <= 0.1505 AND TT4 > 0.0615 AND T3 <= 0.0295 AND Age > 0.425 AND TT4 <= 0.14 AND T4U <= 0.1285|2 (219.0)
FTI <= 0.0605 AND Age > 0.79|1 (11.0)
FTI > 0.0605 AND On_thyroxine > 0.5|3 (102.0)
FTI > 0.062965 AND TT4 <= 0.1505 AND Thyroid_surgery <= 0.5 AND TT4 > 0.0585 AND T3 <= 0.029 AND Age <= 0.765|2 (95.0)
FTI > 0.0605 AND TT4 > 0.1495|3 (23.0)
TT4 > 0.1245 AND Age <= 0.565|2 (7.0)
FTI > 0.0605 AND T3 > 0.0177 AND Age <= 0.745|3 (15.0)
FTI > 0.063 AND TT4 > 0.0605 AND TT4 <= 0.116|3 (6.0)
FTI > 0.063 AND TSH <= 0.008995|2 (5.0/1.0)
FTI <= 0.068 AND Age > 0.275 AND T4U > 0.1145 AND Age > 0.47|1 (7.0)
FTI <= 0.068 AND TSH <= 0.0895 AND Age <= 0.38|1 (8.0/4.0)
FTI <= 0.068 AND TSH <= 0.0895|3 (8.0)
TSH <= 0.061|2 (5.0)
|1 (5.0/1.0)


## SimpleCart Decision Tree

* TSH < 0.00605: 3(5840.0/0.0)
* TSH >= 0.00605
	* FTI < 0.064465: 1(149.0/14.0)
	* FTI >= 0.064465
		* On_thyroxine < 0.5
			* TT4 < 0.1505: 2(330.0/21.0)
			* TT4 >= 0.1505: 3(23.0/0.0)
		* On_thyroxine >= 0.5: 3(102.0/0.0)


