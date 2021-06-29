# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| TSH <= 0.006 | 3 | 0.924221 |
| TSH > 0.006 and FTI > 0.064 and On_thyroxine <= 0 and TT4 <= 0.15 and TT4 > 0.058 and T3 <= 0.029 and Sex <= 0 and Thyroid_surgery <= 0 | 2 | 0.038468 |
| TSH > 0.006 and FTI <= 0.064 and Thyroid_surgery <= 0 and T3 <= 0.025 and I131_treatment <= 0 and TSH > 0.01679 | 1 | 0.019972 |
| TSH > 0.006 and FTI > 0.064 and On_thyroxine > 0 | 3 | 0.171280 |
| TSH > 0.006 and FTI > 0.064 and On_thyroxine <= 0 and TT4 <= 0.15 and TT4 > 0.058 and T3 <= 0.029 and Sex > 0 | 2 | 0.011256 |
| TSH > 0.006 and FTI > 0.064 and On_thyroxine <= 0 and TT4 > 0.15 | 3 | 0.045817 |
| TSH > 0.006 and FTI > 0.064 and On_thyroxine <= 0 and TT4 <= 0.15 and TT4 > 0.058 and T3 <= 0.029 and Sex <= 0 and Thyroid_surgery > 0 | 3 | 0.018443 |
| TSH > 0.006 and FTI > 0.064 and On_thyroxine <= 0 and TT4 <= 0.15 and TT4 <= 0.058 and T3 > 0.0174 | 3 | 0.012371 |
| TSH > 0.006 and FTI <= 0.064 and Thyroid_surgery <= 0 and T3 <= 0.025 and I131_treatment <= 0 and TSH <= 0.01679 and T4U <= 0.096 | 1 | 0.001105 |
| TSH > 0.006 and FTI > 0.064 and On_thyroxine <= 0 and TT4 <= 0.15 and TT4 > 0.058 and T3 > 0.029 and T4U > 0.113 | 2 | 0.001299 |
| TSH > 0.006 and FTI > 0.064 and On_thyroxine <= 0 and TT4 <= 0.15 and TT4 > 0.058 and T3 > 0.029 and T4U <= 0.113 | 3 | 0.010331 |
| TSH > 0.006 and FTI <= 0.064 and Thyroid_surgery <= 0 and T3 > 0.025 | 3 | 0.008627 |
| TSH > 0.006 and FTI <= 0.064 and Thyroid_surgery <= 0 and T3 <= 0.025 and I131_treatment > 0 | 1 | 0.000564 |
| TSH > 0.006 and FTI > 0.064 and On_thyroxine <= 0 and TT4 <= 0.15 and TT4 <= 0.058 and T3 <= 0.0174 | 2 | 0.000677 |
| TSH > 0.006 and FTI <= 0.064 and Thyroid_surgery <= 0 and T3 <= 0.025 and I131_treatment <= 0 and TSH <= 0.01679 and T4U > 0.096 and Age <= 0.61 | 3 | 0.004678 |
| On_thyroxine <= 0.5 and Query_on_thyroxine = all and Thyroid_surgery <= 0.5 and I131_treatment = all and Query_hyperthyroid = all and Tumor = all and TSH > 0.00605 and TSH <= 0.0195 and FTI > 0.0345 and FTI <= 0.064255 | 1 | 0.001052 |
| On_thyroxine <= 0.5 and Query_on_thyroxine = all and Thyroid_surgery <= 0.5 and I131_treatment = all and Query_hyperthyroid = all and Tumor = all and TSH > 0.00605 and TSH <= 0.0195 and FTI > 0.14225 | 3 | 0.010145 |
| TSH > 0.006 and FTI <= 0.064 and Thyroid_surgery > 0 | 1 | 0.000237 |
| On_thyroxine <= 0.5 and Query_on_thyroxine = all and Thyroid_surgery > 0.5 and I131_treatment = all and Query_hyperthyroid = all and Tumor = all and TSH > 0.0415 and FTI > 0.013735 and FTI <= 0.0345 | 3 | 0.001044 |
| On_thyroxine <= 0.5 and Query_on_thyroxine = all and Thyroid_surgery <= 0.5 and I131_treatment = all and Query_hyperthyroid = all and Tumor = all and TSH > 0.00605 and TSH <= 0.0195 and FTI > 0.013735 and FTI <= 0.0345 | 1 | 0.000316 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| TSH <= 0.006 | 3 | 0.924221 |
| FTI <= 0.064 and Thyroid_surgery <= 0 and T3 <= 0.025 and I131_treatment <= 0 and TSH > 0.01679 | 1 | 0.209076 |
| On_thyroxine <= 0 and FTI > 0.064 and TT4 <= 0.15 and TT4 > 0.058 and T3 <= 0.029 and Sex <= 0 and Thyroid_surgery <= 0 | 2 | 0.580198 |
| FTI > 0.064 and On_thyroxine > 0 | 3 | 0.490099 |
| FTI > 0.064 and Sex > 0 and TT4 > 0.053 and TT4 <= 0.143 | 2 | 0.469799 |
| T3 > 0.01 and FTI > 0.064 and TT4 > 0.15 | 3 | 0.410714 |
| TT4 <= 0.124 and T3 > 0.011 and Query_hypothyroid <= 0 and FTI > 0.066 | 3 | 0.327664 |
| FTI > 0.064 and Query_hypothyroid <= 0 | 2 | 0.200000 |
| T3 <= 0.01 | 1 | 0.401070 |
| Query_hypothyroid <= 0 and FTI <= 0.049 | 3 | 0.600000 |
| Query_hypothyroid > 0 | 3 | 0.355556 |
| Age > 0.48 | 1 | 0.285714 |
|  | 3 | 0.750000 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| FTI <= 0.064 and TSH >= 0.0062 | 1 | 0.021068 |
| TSH >= 0.0061 and On_thyroxine <= 0 and T3 <= 0.02 and Thyroid_surgery <= 0 and TT4 <= 0.148 | 2 | 0.039862 |
| TSH >= 0.0061 and T3 >= 0.0208 and On_thyroxine <= 0 and TT4 <= 0.15 | 2 | 0.011200 |
|  | 3 | 1.000000 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

on_thyroxine|query_on_thyroxine|thyroid_surgery|i131_treatment|query_hyperthyroid|tumor|tsh|fti|class
---|---|---|---|---|---|---|---|---
(0.5-inf)|all|(-inf-0.5]|all|all|all|(0.0195-0.0415]|(0.14225-inf)|1
(-inf-0.5]|all|(-inf-0.5]|all|all|all|(0.0195-0.0415]|(0.14225-inf)|3
(0.5-inf)|all|(-inf-0.5]|all|all|all|(0.0415-inf)|(0.097495-0.14225]|3
(-inf-0.5]|all|(-inf-0.5]|all|all|all|(0.00605-0.0195]|(0.14225-inf)|3
(0.5-inf)|all|(-inf-0.5]|all|all|all|(0.00605-0.0195]|(0.14225-inf)|3
(-inf-0.5]|all|(-inf-0.5]|all|all|all|(0.0195-0.0415]|(0.097495-0.14225]|2
(0.5-inf)|all|(-inf-0.5]|all|all|all|(0.0195-0.0415]|(0.097495-0.14225]|3
(-inf-0.5]|all|(-inf-0.5]|all|all|all|(0.0415-inf)|(0.08104-0.097495]|2
(-inf-0.5]|all|(0.5-inf)|all|all|all|(-inf-0.00605]|(0.14225-inf)|3
(0.5-inf)|all|(0.5-inf)|all|all|all|(-inf-0.00605]|(0.14225-inf)|3
(-inf-0.5]|all|(0.5-inf)|all|all|all|(0.00605-0.0195]|(0.097495-0.14225]|3
(0.5-inf)|all|(0.5-inf)|all|all|all|(0.0195-0.0415]|(0.08104-0.097495]|1
(-inf-0.5]|all|(0.5-inf)|all|all|all|(0.0195-0.0415]|(0.08104-0.097495]|1
(-inf-0.5]|all|(-inf-0.5]|all|all|all|(-inf-0.00605]|(0.14225-inf)|3
(0.5-inf)|all|(-inf-0.5]|all|all|all|(-inf-0.00605]|(0.14225-inf)|3
(0.5-inf)|all|(-inf-0.5]|all|all|all|(0.00605-0.0195]|(0.097495-0.14225]|3
(-inf-0.5]|all|(-inf-0.5]|all|all|all|(0.00605-0.0195]|(0.097495-0.14225]|2
(-inf-0.5]|all|(-inf-0.5]|all|all|all|(0.0195-0.0415]|(0.08104-0.097495]|2
(0.5-inf)|all|(-inf-0.5]|all|all|all|(0.0195-0.0415]|(0.08104-0.097495]|3
(0.5-inf)|all|(-inf-0.5]|all|all|all|(0.0415-inf)|(0.064255-0.08104]|3
(-inf-0.5]|all|(-inf-0.5]|all|all|all|(0.0415-inf)|(0.064255-0.08104]|2
(0.5-inf)|all|(0.5-inf)|all|all|all|(-inf-0.00605]|(0.097495-0.14225]|3
(-inf-0.5]|all|(0.5-inf)|all|all|all|(-inf-0.00605]|(0.097495-0.14225]|3
(-inf-0.5]|all|(0.5-inf)|all|all|all|(0.00605-0.0195]|(0.08104-0.097495]|3
(0.5-inf)|all|(-inf-0.5]|all|all|all|(-inf-0.00605]|(0.097495-0.14225]|3
(-inf-0.5]|all|(-inf-0.5]|all|all|all|(-inf-0.00605]|(0.097495-0.14225]|3
(-inf-0.5]|all|(0.5-inf)|all|all|all|(0.0415-inf)|(0.0345-0.064255]|1
(-inf-0.5]|all|(-inf-0.5]|all|all|all|(0.00605-0.0195]|(0.08104-0.097495]|2
(0.5-inf)|all|(-inf-0.5]|all|all|all|(0.00605-0.0195]|(0.08104-0.097495]|3
(-inf-0.5]|all|(-inf-0.5]|all|all|all|(0.0195-0.0415]|(0.064255-0.08104]|2
(0.5-inf)|all|(-inf-0.5]|all|all|all|(0.0195-0.0415]|(0.064255-0.08104]|3
(0.5-inf)|all|(-inf-0.5]|all|all|all|(0.0415-inf)|(0.0345-0.064255]|1
(-inf-0.5]|all|(-inf-0.5]|all|all|all|(0.0415-inf)|(0.0345-0.064255]|1
(-inf-0.5]|all|(0.5-inf)|all|all|all|(-inf-0.00605]|(0.08104-0.097495]|3
(-inf-0.5]|all|(0.5-inf)|all|all|all|(0.00605-0.0195]|(0.064255-0.08104]|1
(0.5-inf)|all|(-inf-0.5]|all|all|all|(-inf-0.00605]|(0.08104-0.097495]|3
(-inf-0.5]|all|(-inf-0.5]|all|all|all|(-inf-0.00605]|(0.08104-0.097495]|3
(-inf-0.5]|all|(0.5-inf)|all|all|all|(0.0415-inf)|(0.013735-0.0345]|3
(-inf-0.5]|all|(-inf-0.5]|all|all|all|(0.00605-0.0195]|(0.064255-0.08104]|2
(0.5-inf)|all|(-inf-0.5]|all|all|all|(0.00605-0.0195]|(0.064255-0.08104]|3
(0.5-inf)|all|(-inf-0.5]|all|all|all|(0.0195-0.0415]|(0.0345-0.064255]|1
(-inf-0.5]|all|(-inf-0.5]|all|all|all|(0.0195-0.0415]|(0.0345-0.064255]|1
(0.5-inf)|all|(-inf-0.5]|all|all|all|(0.0415-inf)|(0.013735-0.0345]|1
(-inf-0.5]|all|(-inf-0.5]|all|all|all|(0.0415-inf)|(0.013735-0.0345]|1
(-inf-0.5]|all|(0.5-inf)|all|all|all|(-inf-0.00605]|(0.064255-0.08104]|3
(-inf-0.5]|all|(0.5-inf)|all|all|all|(0.00605-0.0195]|(0.0345-0.064255]|1
(-inf-0.5]|all|(0.5-inf)|all|all|all|(0.0195-0.0415]|(0.013735-0.0345]|1
(0.5-inf)|all|(-inf-0.5]|all|all|all|(-inf-0.00605]|(0.064255-0.08104]|3
(-inf-0.5]|all|(-inf-0.5]|all|all|all|(-inf-0.00605]|(0.064255-0.08104]|3
(-inf-0.5]|all|(0.5-inf)|all|all|all|(0.0415-inf)|(-inf-0.013735]|1
(0.5-inf)|all|(-inf-0.5]|all|all|all|(0.00605-0.0195]|(0.0345-0.064255]|3
(-inf-0.5]|all|(-inf-0.5]|all|all|all|(0.00605-0.0195]|(0.0345-0.064255]|1
(-inf-0.5]|all|(-inf-0.5]|all|all|all|(0.0195-0.0415]|(0.013735-0.0345]|1
(-inf-0.5]|all|(-inf-0.5]|all|all|all|(0.0415-inf)|(-inf-0.013735]|1
(0.5-inf)|all|(-inf-0.5]|all|all|all|(0.0415-inf)|(-inf-0.013735]|1
(-inf-0.5]|all|(0.5-inf)|all|all|all|(-inf-0.00605]|(0.0345-0.064255]|3
(0.5-inf)|all|(-inf-0.5]|all|all|all|(-inf-0.00605]|(0.0345-0.064255]|3
(-inf-0.5]|all|(-inf-0.5]|all|all|all|(-inf-0.00605]|(0.0345-0.064255]|3
(-inf-0.5]|all|(-inf-0.5]|all|all|all|(0.00605-0.0195]|(0.013735-0.0345]|1
(-inf-0.5]|all|(-inf-0.5]|all|all|all|(0.0195-0.0415]|(-inf-0.013735]|1
(-inf-0.5]|all|(-inf-0.5]|all|all|all|(-inf-0.00605]|(0.013735-0.0345]|3
(-inf-0.5]|all|(-inf-0.5]|all|all|all|(-inf-0.00605]|(-inf-0.013735]|1

## JRip

Decision list:

rules | predicted class
---|---
(FTI <= 0.064) and (TSH >= 0.0062)|1 (163.0/14.0)
(TSH >= 0.0061) and (On_thyroxine <= 0) and (T3 <= 0.02) and (Thyroid_surgery <= 0) and (TT4 <= 0.148)|2 (255.0/1.0)
(TSH >= 0.0061) and (T3 >= 0.0208) and (On_thyroxine <= 0) and (TT4 <= 0.15)|2 (81.0/5.0)
|3 (5980.0/0.0)


## PART

Decision list:

rules | predicted class
---|---
TSH <= 0.006|3 (5842.0)
FTI <= 0.064 AND Thyroid_surgery <= 0 AND T3 <= 0.025 AND I131_treatment <= 0 AND TSH > 0.01679|1 (129.0)
On_thyroxine <= 0 AND FTI > 0.064 AND TT4 <= 0.15 AND TT4 > 0.058 AND T3 <= 0.029 AND Sex <= 0 AND Thyroid_surgery <= 0|2 (248.0/1.0)
FTI > 0.064 AND On_thyroxine > 0|3 (99.0)
FTI > 0.064 AND Sex > 0 AND TT4 > 0.053 AND TT4 <= 0.143|2 (70.0)
T3 > 0.01 AND FTI > 0.064 AND TT4 > 0.15|3 (23.0)
TT4 <= 0.124 AND T3 > 0.011 AND Query_hypothyroid <= 0 AND FTI > 0.066|3 (18.0/1.0)
FTI > 0.064 AND Query_hypothyroid <= 0|2 (13.0/2.0)
T3 <= 0.01|1 (16.0/1.0)
Query_hypothyroid <= 0 AND FTI <= 0.049|3 (9.0)
Query_hypothyroid > 0|3 (5.0/1.0)
Age > 0.48|1 (4.0)
|3 (3.0/1.0)


## J48 Decision Tree

* TSH <= 0.006: 3 (5842.0)
* TSH > 0.006
	* FTI <= 0.064
		* Thyroid_surgery <= 0
			* T3 <= 0.025
				* I131_treatment <= 0
					* TSH <= 0.01679
						* T4U <= 0.096: 1 (7.0)
						* T4U > 0.096
							* Age <= 0.61: 3 (4.0/1.0)
							* Age > 0.61: 1 (4.0/1.0)
					* TSH > 0.01679: 1 (129.0)
				* I131_treatment > 0: 1 (7.0/2.0)
			* T3 > 0.025: 3 (6.0/1.0)
		* Thyroid_surgery > 0: 1 (6.0/3.0)
	* FTI > 0.064
		* On_thyroxine <= 0
			* TT4 <= 0.15
				* TT4 <= 0.058
					* T3 <= 0.0174: 2 (6.0/1.0)
					* T3 > 0.0174: 3 (6.0)
				* TT4 > 0.058
					* T3 <= 0.029
						* Sex <= 0
							* Thyroid_surgery <= 0: 2 (248.0/1.0)
							* Thyroid_surgery > 0: 3 (9.0)
						* Sex > 0: 2 (70.0)
					* T3 > 0.029
						* T4U <= 0.113: 3 (5.0)
						* T4U > 0.113: 2 (8.0)
			* TT4 > 0.15: 3 (23.0)
		* On_thyroxine > 0: 3 (99.0)


