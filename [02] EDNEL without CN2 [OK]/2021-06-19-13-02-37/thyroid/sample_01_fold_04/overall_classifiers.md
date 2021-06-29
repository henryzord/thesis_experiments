# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 3 | 0.926069 |
| TSH > 0.00605 and FTI > 0.064255 and On_thyroxine <= 0.5 and TT4 <= 0.1505 and Thyroid_surgery <= 0.5 | 2 | 0.049102 |
| On_thyroxine <= 0.5 and On_antithyroid_medication = all and Thyroid_surgery <= 0.5 and I131_treatment = all and Lithium = all and Hypopituitary = all and TSH > 0.0415 and TT4 > 0.0525 and TT4 <= 0.0685 | 1 | 0.000237 |
| On_thyroxine > 0.5 and On_antithyroid_medication = all and Thyroid_surgery <= 0.5 and I131_treatment = all and Lithium = all and Hypopituitary = all and TSH > 0.0195 and TSH <= 0.0415 and TT4 > 0.0525 and TT4 <= 0.0685 | 1 | 0.000079 |
| TSH > 0.00605 and FTI <= 0.064255 and TSH > 0.016895 | 1 | 0.020012 |
| On_thyroxine <= 0.5 and On_antithyroid_medication = all and Thyroid_surgery <= 0.5 and I131_treatment = all and Lithium = all and Hypopituitary = all and TSH > 0.00605 and TSH <= 0.0195 and TT4 <= 0.0185 | 1 | 0.000158 |
| On_thyroxine <= 0.5 and On_antithyroid_medication = all and Thyroid_surgery <= 0.5 and I131_treatment = all and Lithium = all and Hypopituitary = all and TSH > 0.00605 and TSH <= 0.0195 and TT4 > 0.0185 and TT4 <= 0.033875 | 1 | 0.000316 |
| TSH > 0.00605 and FTI <= 0.064255 and TSH <= 0.016895 and T3 <= 0.013 | 1 | 0.001434 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| TSH <= 0.006 | 3 | 0.924293 |
| FTI <= 0.064 and Thyroid_surgery <= 0 and T3 <= 0.023 and I131_treatment <= 0 and TSH > 0.01679 | 1 | 0.200663 |
| FTI > 0.06451 and On_thyroxine <= 0 and TT4 <= 0.15 and TT4 > 0.061 and T3 <= 0.03 and Thyroid_surgery <= 0 and Sex <= 0 and Query_hypothyroid <= 0 and Query_hyperthyroid <= 0 and Sick <= 0 | 2 | 0.512209 |
| FTI <= 0.064 and T3 <= 0.026 and On_antithyroid_medication <= 0 and Thyroid_surgery <= 0 and Sex <= 0 and T4U <= 0.103 | 1 | 0.036304 |
| FTI <= 0.062 and T3 <= 0.026 and Sex <= 0 and TSH > 0.00979 and FTI > 0.043 | 1 | 0.026667 |
| On_thyroxine > 0 and I131_treatment <= 0 | 3 | 0.386831 |
| FTI > 0.0635 and TT4 <= 0.15 and Thyroid_surgery <= 0 and TT4 > 0.054 and I131_treatment <= 0 and T3 <= 0.029 and Sex > 0 | 2 | 0.521429 |
| FTI > 0.0635 and TT4 <= 0.148 and Thyroid_surgery <= 0 and Sex <= 0 and I131_treatment <= 0 and TT4 > 0.061 and T3 <= 0.031 | 2 | 0.455425 |
| TT4 > 0.018 and Sex <= 0 and Thyroid_surgery > 0 | 3 | 0.441176 |
| FTI > 0.064 and TT4 > 0.148 | 3 | 0.500000 |
| FTI > 0.064 and T4U <= 0.113 and T3 > 0.019 | 3 | 0.387097 |
| FTI > 0.071 and On_thyroxine <= 0 | 2 | 0.322581 |
| Query_hypothyroid > 0 | 3 | 0.307692 |
| On_antithyroid_medication <= 0 and Sex > 0 and Age <= 0.5 | 1 | 0.148148 |
| Sex <= 0 and TSH <= 0.056 | 3 | 0.500000 |
|  | 1 | 0.875000 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| FTI <= 0.064 and TSH >= 0.0097 and T3 <= 0.011 and Thyroid_surgery <= 0 | 1 | 0.016164 |
| FTI <= 0.064 and TSH >= 0.018 and TT4 >= 0.038 | 1 | 0.003777 |
| FTI <= 0.061 and TSH >= 0.0062 and T3 <= 0.02 and T4U <= 0.119 and TSH <= 0.01029 | 1 | 0.001262 |
| FTI <= 0.02983 and TSH >= 0.035 and Age <= 0.65 and Thyroid_surgery <= 0 | 1 | 0.001420 |
| TSH >= 0.0061 and On_thyroxine <= 0 and T3 <= 0.02 and Thyroid_surgery <= 0 and FTI >= 0.069 and TT4 <= 0.148 | 2 | 0.038899 |
| TSH >= 0.0061 and On_thyroxine <= 0 and T3 >= 0.0208 and T3 <= 0.025 and TT4 <= 0.141 and FTI >= 0.065 | 2 | 0.009241 |
| TSH >= 0.0061 and On_thyroxine <= 0 and TT4 >= 0.064 and FTI <= 0.092 and Thyroid_surgery <= 0 and FTI >= 0.06493 and Lithium <= 0 | 2 | 0.003816 |
| TSH >= 0.0079 and T3 >= 0.026 and T3 <= 0.031 and FTI >= 0.103 and On_thyroxine <= 0 | 2 | 0.000998 |
|  | 3 | 0.999001 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

on_thyroxine|on_antithyroid_medication|thyroid_surgery|i131_treatment|lithium|hypopituitary|tsh|tt4|class
---|---|---|---|---|---|---|---|---
(-inf-0.5]|all|(-inf-0.5]|all|all|all|(0.0195-0.0415]|(0.1505-inf)|3
(0.5-inf)|all|(-inf-0.5]|all|all|all|(0.0415-inf)|(0.0895-0.1505]|3
(-inf-0.5]|all|(-inf-0.5]|all|all|all|(0.0415-inf)|(0.0895-0.1505]|1
(0.5-inf)|all|(-inf-0.5]|all|all|all|(0.00605-0.0195]|(0.1505-inf)|3
(-inf-0.5]|all|(-inf-0.5]|all|all|all|(0.00605-0.0195]|(0.1505-inf)|3
(-inf-0.5]|all|(-inf-0.5]|all|all|all|(0.0195-0.0415]|(0.0895-0.1505]|2
(0.5-inf)|all|(-inf-0.5]|all|all|all|(0.0195-0.0415]|(0.0895-0.1505]|3
(-inf-0.5]|all|(-inf-0.5]|all|all|all|(0.0415-inf)|(0.0685-0.0895]|2
(0.5-inf)|all|(-inf-0.5]|all|all|all|(0.0415-inf)|(0.0685-0.0895]|3
(-inf-0.5]|all|(0.5-inf)|all|all|all|(-inf-0.00605]|(0.1505-inf)|3
(0.5-inf)|all|(0.5-inf)|all|all|all|(-inf-0.00605]|(0.1505-inf)|3
(-inf-0.5]|all|(0.5-inf)|all|all|all|(0.00605-0.0195]|(0.0895-0.1505]|3
(-inf-0.5]|all|(0.5-inf)|all|all|all|(0.0195-0.0415]|(0.0685-0.0895]|1
(0.5-inf)|all|(0.5-inf)|all|all|all|(0.0195-0.0415]|(0.0685-0.0895]|1
(0.5-inf)|all|(-inf-0.5]|all|all|all|(-inf-0.00605]|(0.1505-inf)|3
(-inf-0.5]|all|(-inf-0.5]|all|all|all|(-inf-0.00605]|(0.1505-inf)|3
(-inf-0.5]|all|(-inf-0.5]|all|all|all|(0.00605-0.0195]|(0.0895-0.1505]|2
(-inf-0.5]|all|(0.5-inf)|all|all|all|(0.0415-inf)|(0.0525-0.0685]|1
(0.5-inf)|all|(-inf-0.5]|all|all|all|(0.00605-0.0195]|(0.0895-0.1505]|3
(-inf-0.5]|all|(-inf-0.5]|all|all|all|(0.0195-0.0415]|(0.0685-0.0895]|2
(0.5-inf)|all|(-inf-0.5]|all|all|all|(0.0195-0.0415]|(0.0685-0.0895]|3
(0.5-inf)|all|(-inf-0.5]|all|all|all|(0.0415-inf)|(0.0525-0.0685]|1
(-inf-0.5]|all|(-inf-0.5]|all|all|all|(0.0415-inf)|(0.0525-0.0685]|1
(0.5-inf)|all|(0.5-inf)|all|all|all|(-inf-0.00605]|(0.0895-0.1505]|3
(-inf-0.5]|all|(0.5-inf)|all|all|all|(-inf-0.00605]|(0.0895-0.1505]|3
(-inf-0.5]|all|(0.5-inf)|all|all|all|(0.00605-0.0195]|(0.0685-0.0895]|3
(-inf-0.5]|all|(0.5-inf)|all|all|all|(0.0195-0.0415]|(0.0525-0.0685]|1
(0.5-inf)|all|(-inf-0.5]|all|all|all|(-inf-0.00605]|(0.0895-0.1505]|3
(-inf-0.5]|all|(-inf-0.5]|all|all|all|(-inf-0.00605]|(0.0895-0.1505]|3
(-inf-0.5]|all|(0.5-inf)|all|all|all|(0.0415-inf)|(0.033875-0.0525]|1
(0.5-inf)|all|(-inf-0.5]|all|all|all|(0.00605-0.0195]|(0.0685-0.0895]|3
(-inf-0.5]|all|(-inf-0.5]|all|all|all|(0.00605-0.0195]|(0.0685-0.0895]|2
(0.5-inf)|all|(-inf-0.5]|all|all|all|(0.0195-0.0415]|(0.0525-0.0685]|1
(-inf-0.5]|all|(-inf-0.5]|all|all|all|(0.0195-0.0415]|(0.0525-0.0685]|1
(0.5-inf)|all|(-inf-0.5]|all|all|all|(0.0415-inf)|(0.033875-0.0525]|1
(-inf-0.5]|all|(-inf-0.5]|all|all|all|(0.0415-inf)|(0.033875-0.0525]|1
(-inf-0.5]|all|(0.5-inf)|all|all|all|(-inf-0.00605]|(0.0685-0.0895]|3
(0.5-inf)|all|(-inf-0.5]|all|all|all|(-inf-0.00605]|(0.0685-0.0895]|3
(-inf-0.5]|all|(-inf-0.5]|all|all|all|(-inf-0.00605]|(0.0685-0.0895]|3
(-inf-0.5]|all|(0.5-inf)|all|all|all|(0.0415-inf)|(0.0185-0.033875]|1
(-inf-0.5]|all|(-inf-0.5]|all|all|all|(0.00605-0.0195]|(0.0525-0.0685]|2
(0.5-inf)|all|(-inf-0.5]|all|all|all|(0.00605-0.0195]|(0.0525-0.0685]|3
(0.5-inf)|all|(-inf-0.5]|all|all|all|(0.0195-0.0415]|(0.033875-0.0525]|1
(-inf-0.5]|all|(-inf-0.5]|all|all|all|(0.0195-0.0415]|(0.033875-0.0525]|1
(0.5-inf)|all|(-inf-0.5]|all|all|all|(0.0415-inf)|(0.0185-0.033875]|1
(-inf-0.5]|all|(-inf-0.5]|all|all|all|(0.0415-inf)|(0.0185-0.033875]|1
(-inf-0.5]|all|(0.5-inf)|all|all|all|(-inf-0.00605]|(0.0525-0.0685]|3
(-inf-0.5]|all|(0.5-inf)|all|all|all|(0.0195-0.0415]|(0.0185-0.033875]|1
(0.5-inf)|all|(-inf-0.5]|all|all|all|(-inf-0.00605]|(0.0525-0.0685]|3
(-inf-0.5]|all|(-inf-0.5]|all|all|all|(-inf-0.00605]|(0.0525-0.0685]|3
(0.5-inf)|all|(-inf-0.5]|all|all|all|(0.00605-0.0195]|(0.033875-0.0525]|3
(-inf-0.5]|all|(0.5-inf)|all|all|all|(0.0415-inf)|(-inf-0.0185]|1
(-inf-0.5]|all|(-inf-0.5]|all|all|all|(0.00605-0.0195]|(0.033875-0.0525]|3
(0.5-inf)|all|(-inf-0.5]|all|all|all|(0.0195-0.0415]|(0.0185-0.033875]|1
(-inf-0.5]|all|(-inf-0.5]|all|all|all|(0.0195-0.0415]|(0.0185-0.033875]|1
(0.5-inf)|all|(-inf-0.5]|all|all|all|(0.0415-inf)|(-inf-0.0185]|1
(-inf-0.5]|all|(-inf-0.5]|all|all|all|(0.0415-inf)|(-inf-0.0185]|1
(0.5-inf)|all|(0.5-inf)|all|all|all|(-inf-0.00605]|(0.033875-0.0525]|1
(-inf-0.5]|all|(0.5-inf)|all|all|all|(-inf-0.00605]|(0.033875-0.0525]|1
(0.5-inf)|all|(-inf-0.5]|all|all|all|(-inf-0.00605]|(0.033875-0.0525]|3
(-inf-0.5]|all|(-inf-0.5]|all|all|all|(-inf-0.00605]|(0.033875-0.0525]|3
(-inf-0.5]|all|(-inf-0.5]|all|all|all|(0.00605-0.0195]|(0.0185-0.033875]|1
(-inf-0.5]|all|(-inf-0.5]|all|all|all|(0.0195-0.0415]|(-inf-0.0185]|1
(-inf-0.5]|all|(-inf-0.5]|all|all|all|(-inf-0.00605]|(0.0185-0.033875]|3
(-inf-0.5]|all|(-inf-0.5]|all|all|all|(0.00605-0.0195]|(-inf-0.0185]|1
(-inf-0.5]|all|(-inf-0.5]|all|all|all|(-inf-0.00605]|(-inf-0.0185]|3

## JRip

Decision list:

rules | predicted class
---|---
(FTI <= 0.064) and (TSH >= 0.0097) and (T3 <= 0.011) and (Thyroid_surgery <= 0)|1 (104.0/0.0)
(FTI <= 0.064) and (TSH >= 0.018) and (TT4 >= 0.038)|1 (24.0/0.0)
(FTI <= 0.061) and (TSH >= 0.0062) and (T3 <= 0.02) and (T4U <= 0.119) and (TSH <= 0.01029)|1 (8.0/0.0)
(FTI <= 0.02983) and (TSH >= 0.035) and (Age <= 0.65) and (Thyroid_surgery <= 0)|1 (9.0/0.0)
(TSH >= 0.0061) and (On_thyroxine <= 0) and (T3 <= 0.02) and (Thyroid_surgery <= 0) and (FTI >= 0.069) and (TT4 <= 0.148)|2 (243.0/0.0)
(TSH >= 0.0061) and (On_thyroxine <= 0) and (T3 >= 0.0208) and (T3 <= 0.025) and (TT4 <= 0.141) and (FTI >= 0.065)|2 (56.0/0.0)
(TSH >= 0.0061) and (On_thyroxine <= 0) and (TT4 >= 0.064) and (FTI <= 0.092) and (Thyroid_surgery <= 0) and (FTI >= 0.06493) and (Lithium <= 0)|2 (23.0/0.0)
(TSH >= 0.0079) and (T3 >= 0.026) and (T3 <= 0.031) and (FTI >= 0.103) and (On_thyroxine <= 0)|2 (6.0/0.0)
|3 (6006.0/6.0)


## PART

Decision list:

rules | predicted class
---|---
TSH <= 0.006|3 (5848.0)
FTI <= 0.064 AND Thyroid_surgery <= 0 AND T3 <= 0.023 AND I131_treatment <= 0 AND TSH > 0.01679|1 (121.0)
FTI > 0.06451 AND On_thyroxine <= 0 AND TT4 <= 0.15 AND TT4 > 0.061 AND T3 <= 0.03 AND Thyroid_surgery <= 0 AND Sex <= 0 AND Query_hypothyroid <= 0 AND Query_hyperthyroid <= 0 AND Sick <= 0|2 (191.0/1.0)
FTI <= 0.064 AND T3 <= 0.026 AND On_antithyroid_medication <= 0 AND Thyroid_surgery <= 0 AND Sex <= 0 AND T4U <= 0.103|1 (11.0)
FTI <= 0.062 AND T3 <= 0.026 AND Sex <= 0 AND TSH > 0.00979 AND FTI > 0.043|1 (8.0)
On_thyroxine > 0 AND I131_treatment <= 0|3 (94.0)
FTI > 0.0635 AND TT4 <= 0.15 AND Thyroid_surgery <= 0 AND TT4 > 0.054 AND I131_treatment <= 0 AND T3 <= 0.029 AND Sex > 0|2 (73.0)
FTI > 0.0635 AND TT4 <= 0.148 AND Thyroid_surgery <= 0 AND Sex <= 0 AND I131_treatment <= 0 AND TT4 > 0.061 AND T3 <= 0.031|2 (57.0)
TT4 > 0.018 AND Sex <= 0 AND Thyroid_surgery > 0|3 (15.0)
FTI > 0.064 AND TT4 > 0.148|3 (19.0)
FTI > 0.064 AND T4U <= 0.113 AND T3 > 0.019|3 (11.0)
FTI > 0.071 AND On_thyroxine <= 0|2 (10.0)
Query_hypothyroid > 0|3 (4.0)
On_antithyroid_medication <= 0 AND Sex > 0 AND Age <= 0.5|1 (3.0/1.0)
Sex <= 0 AND TSH <= 0.056|3 (7.0)
|1 (7.0)


## J48 Decision Tree

* TSH <= 0.00605: 3 (5848.0)
* TSH > 0.00605
	* FTI <= 0.064255
		* TSH <= 0.016895
			* T3 <= 0.013: 1 (11.0/1.0)
			* T3 > 0.013: 3 (12.0/4.0)
		* TSH > 0.016895: 1 (141.0/6.0)
	* FTI > 0.064255
		* On_thyroxine <= 0.5
			* TT4 <= 0.1505
				* Thyroid_surgery <= 0.5: 2 (343.0/13.0)
				* Thyroid_surgery > 0.5: 3 (11.0)
			* TT4 > 0.1505: 3 (19.0)
		* On_thyroxine > 0.5: 3 (94.0)


