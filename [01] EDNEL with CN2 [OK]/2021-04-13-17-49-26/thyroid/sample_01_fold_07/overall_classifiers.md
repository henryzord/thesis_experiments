# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| TSH < 0.00605 | 3 | 0.923442 |
| TSH >= 0.00605 and FTI >= 0.064255 and On_thyroxine < 0.5 and TT4 < 0.1505 and Thyroid_surgery < 0.5 and TT4 >= 0.058499999999999996 and T3 < 0.0295 | 2 | 0.049954 |
| TSH >= 0.00605 and FTI < 0.064255 | 1 | 0.021198 |
| TSH > 0.006 and FTI > 0.064 and On_thyroxine > 0 | 3 | 0.166954 |
| TSH > 0.006 and FTI > 0.064 and On_thyroxine <= 0 and TT4 > 0.15 | 3 | 0.041584 |
| TSH >= 0.00605 and FTI >= 0.064255 and On_thyroxine < 0.5 and TT4 < 0.1505 and Thyroid_surgery >= 0.5 | 3 | 0.022222 |
| TSH >= 0.00605 and FTI >= 0.064255 and On_thyroxine < 0.5 and TT4 < 0.1505 and Thyroid_surgery < 0.5 and TT4 >= 0.058499999999999996 and T3 >= 0.0295 and Age >= 0.37 | 3 | 0.012245 |
| TSH > 0.006 and FTI > 0.064 and On_thyroxine <= 0 and TT4 <= 0.15 and TT4 <= 0.058 and T3 > 0.0174 | 3 | 0.012245 |
| TSH > 0.006 and FTI > 0.064 and On_thyroxine <= 0 and TT4 <= 0.15 and TT4 > 0.058 and T3 > 0.029 and Age <= 0.37 | 2 | 0.000976 |
| TSH > 0.006 and FTI <= 0.064 and Thyroid_surgery <= 0 and T3 > 0.025 and T3 > 0.026 | 3 | 0.008197 |
| TSH > 0.006 and FTI <= 0.064 and Thyroid_surgery <= 0 and T3 <= 0.025 and I131_treatment <= 0 and TSH <= 0.01679 and On_antithyroid_medication > 0 | 3 | 0.004115 |
| TSH >= 0.00605 and FTI >= 0.064255 and On_thyroxine < 0.5 and TT4 < 0.1505 and Thyroid_surgery < 0.5 and TT4 < 0.058499999999999996 and T3 < 0.01755 | 2 | 0.000678 |
| TSH > 0.006 and FTI <= 0.064 and Thyroid_surgery > 0 and T4U > 0.131 | 3 | 0.004115 |
| TSH > 0.006 and FTI <= 0.064 and Thyroid_surgery <= 0 and T3 <= 0.025 and I131_treatment > 0 and Age > 0.65 | 3 | 0.004115 |
| On_thyroxine <= 0.5 and Thyroid_surgery <= 0.5 and TSH > 0.00605 and TSH <= 0.0195 and FTI > 0.14225 | 3 | 0.010041 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| TSH <= 0.006 | 3 | 0.923442 |
| FTI <= 0.064 and Thyroid_surgery <= 0.0 and T3 <= 0.025 and TSH > 0.01679 and I131_treatment <= 0.0 | 1 | 0.202922 |
| FTI > 0.06451 and On_thyroxine <= 0.0 and TT4 <= 0.15 and TT4 > 0.058 and T3 <= 0.029 and Age > 0.42 and TT4 <= 0.134 and T4U <= 0.126 | 2 | 0.563107 |
| FTI <= 0.064 and T3 <= 0.011 and T4U <= 0.108 | 1 | 0.044280 |
| FTI > 0.064 and On_thyroxine > 0.0 | 3 | 0.457547 |
| FTI > 0.064 and TT4 <= 0.15 and Thyroid_surgery <= 0.0 and TT4 > 0.061 and T3 <= 0.03 and Age <= 0.74 | 2 | 0.553459 |
| FTI > 0.064 and TT4 > 0.149 | 3 | 0.437500 |
| FTI > 0.064 and T4U <= 0.133 and T3 > 0.019 and T3 <= 0.031 | 3 | 0.357143 |
| FTI > 0.064 and Thyroid_surgery <= 0.0 and T4U > 0.11 | 2 | 0.186047 |
| T4U <= 0.086 | 2 | 0.105263 |
| FTI > 0.066 | 3 | 0.413223 |
| FTI <= 0.049 and TSH <= 0.056 | 3 | 0.322368 |
| Age > 0.51 | 1 | 0.409091 |
| Age <= 0.41 | 1 | 0.296296 |
|  | 3 | 0.666667 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| FTI <= 0.064 and TSH >= 0.0062 | 1 | 0.021198 |
| TSH >= 0.0061 and On_thyroxine <= 0 and TT4 <= 0.146 and Thyroid_surgery <= 0 | 2 | 0.049674 |
|  | 3 | 0.999666 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

on_thyroxine|thyroid_surgery|tsh|fti|class
---|---|---|---|---
(0.5-inf)|(-inf-0.5]|(0.0195-0.0415]|(0.14225-inf)|1
(-inf-0.5]|(-inf-0.5]|(0.0195-0.0415]|(0.14225-inf)|3
(0.5-inf)|(-inf-0.5]|(0.0415-inf)|(0.097495-0.14225]|1
(0.5-inf)|(-inf-0.5]|(0.00605-0.0195]|(0.14225-inf)|3
(-inf-0.5]|(-inf-0.5]|(0.00605-0.0195]|(0.14225-inf)|3
(0.5-inf)|(0.5-inf)|(-inf-0.00605]|(0.14225-inf)|3
(0.5-inf)|(-inf-0.5]|(0.0195-0.0415]|(0.097495-0.14225]|3
(-inf-0.5]|(-inf-0.5]|(0.0195-0.0415]|(0.097495-0.14225]|2
(-inf-0.5]|(0.5-inf)|(-inf-0.00605]|(0.14225-inf)|3
(-inf-0.5]|(-inf-0.5]|(0.0415-inf)|(0.08002-0.097495]|2
(-inf-0.5]|(0.5-inf)|(0.00605-0.0195]|(0.097495-0.14225]|3
(0.5-inf)|(-inf-0.5]|(-inf-0.00605]|(0.14225-inf)|3
(-inf-0.5]|(-inf-0.5]|(-inf-0.00605]|(0.14225-inf)|3
(-inf-0.5]|(0.5-inf)|(0.0195-0.0415]|(0.08002-0.097495]|1
(0.5-inf)|(0.5-inf)|(0.0195-0.0415]|(0.08002-0.097495]|1
(0.5-inf)|(-inf-0.5]|(0.00605-0.0195]|(0.097495-0.14225]|3
(-inf-0.5]|(-inf-0.5]|(0.00605-0.0195]|(0.097495-0.14225]|2
(0.5-inf)|(-inf-0.5]|(0.0195-0.0415]|(0.08002-0.097495]|3
(-inf-0.5]|(-inf-0.5]|(0.0195-0.0415]|(0.08002-0.097495]|2
(-inf-0.5]|(0.5-inf)|(-inf-0.00605]|(0.097495-0.14225]|3
(0.5-inf)|(0.5-inf)|(-inf-0.00605]|(0.097495-0.14225]|3
(-inf-0.5]|(-inf-0.5]|(0.0415-inf)|(0.064255-0.08002]|2
(0.5-inf)|(-inf-0.5]|(0.0415-inf)|(0.064255-0.08002]|3
(-inf-0.5]|(0.5-inf)|(0.00605-0.0195]|(0.08002-0.097495]|3
(-inf-0.5]|(-inf-0.5]|(-inf-0.00605]|(0.097495-0.14225]|3
(0.5-inf)|(-inf-0.5]|(-inf-0.00605]|(0.097495-0.14225]|3
(-inf-0.5]|(-inf-0.5]|(0.00605-0.0195]|(0.08002-0.097495]|2
(0.5-inf)|(-inf-0.5]|(0.00605-0.0195]|(0.08002-0.097495]|3
(-inf-0.5]|(-inf-0.5]|(0.0195-0.0415]|(0.064255-0.08002]|2
(-inf-0.5]|(0.5-inf)|(0.0415-inf)|(0.0345-0.064255]|1
(0.5-inf)|(-inf-0.5]|(0.0195-0.0415]|(0.064255-0.08002]|3
(-inf-0.5]|(0.5-inf)|(-inf-0.00605]|(0.08002-0.097495]|3
(-inf-0.5]|(0.5-inf)|(0.00605-0.0195]|(0.064255-0.08002]|3
(0.5-inf)|(-inf-0.5]|(0.0415-inf)|(0.0345-0.064255]|1
(-inf-0.5]|(-inf-0.5]|(0.0415-inf)|(0.0345-0.064255]|1
(0.5-inf)|(-inf-0.5]|(-inf-0.00605]|(0.08002-0.097495]|3
(-inf-0.5]|(-inf-0.5]|(-inf-0.00605]|(0.08002-0.097495]|3
(-inf-0.5]|(0.5-inf)|(0.0195-0.0415]|(0.0345-0.064255]|1
(-inf-0.5]|(-inf-0.5]|(0.00605-0.0195]|(0.064255-0.08002]|2
(0.5-inf)|(-inf-0.5]|(0.00605-0.0195]|(0.064255-0.08002]|3
(0.5-inf)|(-inf-0.5]|(0.0195-0.0415]|(0.0345-0.064255]|1
(-inf-0.5]|(-inf-0.5]|(0.0195-0.0415]|(0.0345-0.064255]|1
(-inf-0.5]|(0.5-inf)|(0.0415-inf)|(-inf-0.0345]|1
(-inf-0.5]|(0.5-inf)|(-inf-0.00605]|(0.064255-0.08002]|3
(-inf-0.5]|(-inf-0.5]|(0.0415-inf)|(-inf-0.0345]|1
(0.5-inf)|(-inf-0.5]|(0.0415-inf)|(-inf-0.0345]|1
(-inf-0.5]|(0.5-inf)|(0.00605-0.0195]|(0.0345-0.064255]|1
(0.5-inf)|(-inf-0.5]|(-inf-0.00605]|(0.064255-0.08002]|3
(-inf-0.5]|(-inf-0.5]|(-inf-0.00605]|(0.064255-0.08002]|3
(0.5-inf)|(-inf-0.5]|(0.00605-0.0195]|(0.0345-0.064255]|1
(-inf-0.5]|(-inf-0.5]|(0.00605-0.0195]|(0.0345-0.064255]|1
(-inf-0.5]|(0.5-inf)|(-inf-0.00605]|(0.0345-0.064255]|3
(-inf-0.5]|(-inf-0.5]|(0.0195-0.0415]|(-inf-0.0345]|1
(0.5-inf)|(-inf-0.5]|(-inf-0.00605]|(0.0345-0.064255]|3
(-inf-0.5]|(-inf-0.5]|(-inf-0.00605]|(0.0345-0.064255]|3
(-inf-0.5]|(-inf-0.5]|(0.00605-0.0195]|(-inf-0.0345]|1
(-inf-0.5]|(-inf-0.5]|(-inf-0.00605]|(-inf-0.0345]|3

## JRip

Decision list:

rules | predicted class
---|---
(FTI <= 0.064) and (TSH >= 0.0062)|1 (162.0/13.0)
(TSH >= 0.0061) and (On_thyroxine <= 0) and (TT4 <= 0.146) and (Thyroid_surgery <= 0)|2 (346.0/13.0)
|3 (5970.0/2.0)


## PART

Decision list:

rules | predicted class
---|---
TSH <= 0.006|3 (5838.0)
FTI <= 0.064 AND Thyroid_surgery <= 0.0 AND T3 <= 0.025 AND TSH > 0.01679 AND I131_treatment <= 0.0|1 (125.0)
FTI > 0.06451 AND On_thyroxine <= 0.0 AND TT4 <= 0.15 AND TT4 > 0.058 AND T3 <= 0.029 AND Age > 0.42 AND TT4 <= 0.134 AND T4U <= 0.126|2 (232.0)
FTI <= 0.064 AND T3 <= 0.011 AND T4U <= 0.108|1 (12.0)
FTI > 0.064 AND On_thyroxine > 0.0|3 (97.0)
FTI > 0.064 AND TT4 <= 0.15 AND Thyroid_surgery <= 0.0 AND TT4 > 0.061 AND T3 <= 0.03 AND Age <= 0.74|2 (88.0)
FTI > 0.064 AND TT4 > 0.149|3 (21.0)
FTI > 0.064 AND T4U <= 0.133 AND T3 > 0.019 AND T3 <= 0.031|3 (15.0)
FTI > 0.064 AND Thyroid_surgery <= 0.0 AND T4U > 0.11|2 (8.0)
T4U <= 0.086|2 (9.0/3.0)
FTI > 0.066|3 (9.0/1.0)
FTI <= 0.049 AND TSH <= 0.056|3 (7.0/1.0)
Age > 0.51|1 (7.0/1.0)
Age <= 0.41|1 (5.0/2.0)
|3 (5.0/2.0)


## J48 Decision Tree

* TSH <= 0.006: 3 (5838.0)
* TSH > 0.006
	* FTI <= 0.064
		* Thyroid_surgery <= 0
			* T3 <= 0.025
				* I131_treatment <= 0
					* TSH <= 0.01679
						* On_antithyroid_medication <= 0
							* On_thyroxine <= 0
								* Sex <= 0
									* Query_hypothyroid <= 0
										* TT4 <= 0.065: 1 (7.0)
										* TT4 > 0.065: 1 (2.0/1.0)
									* Query_hypothyroid > 0: 1 (2.0)
								* Sex > 0: 1 (2.0)
							* On_thyroxine > 0: 1 (2.0/1.0)
						* On_antithyroid_medication > 0: 3 (2.0)
					* TSH > 0.01679: 1 (125.0)
				* I131_treatment > 0
					* Age <= 0.65: 1 (5.0)
					* Age > 0.65: 3 (2.0)
			* T3 > 0.025
				* T3 <= 0.026: 1 (2.0)
				* T3 > 0.026: 3 (4.0)
		* Thyroid_surgery > 0
			* T4U <= 0.131
				* T4U <= 0.114: 1 (2.0/1.0)
				* T4U > 0.114: 1 (3.0)
			* T4U > 0.131: 3 (2.0)
	* FTI > 0.064
		* On_thyroxine <= 0
			* TT4 <= 0.15
				* TT4 <= 0.058
					* T3 <= 0.0174
						* T3 <= 0.005: 2 (2.0/1.0)
						* T3 > 0.005: 2 (4.0)
					* T3 > 0.0174: 3 (6.0)
				* TT4 > 0.058
					* T3 <= 0.029
						* Age <= 0.42
							* Thyroid_surgery <= 0: 2 (77.0)
							* Thyroid_surgery > 0: 3 (10.0)
						* Age > 0.42
							* Sex <= 0
								* Query_hypothyroid <= 0
									* Query_hyperthyroid <= 0
										* Sick <= 0: 2 (143.0/2.0)
										* Sick > 0: 2 (7.0)
									* Query_hyperthyroid > 0: 2 (11.0)
								* Query_hypothyroid > 0: 2 (33.0)
							* Sex > 0: 2 (55.0)
					* T3 > 0.029
						* Age <= 0.37: 2 (6.0)
						* Age > 0.37: 3 (6.0)
			* TT4 > 0.15: 3 (21.0)
		* On_thyroxine > 0: 3 (97.0)


## SimpleCart Decision Tree

* TSH < 0.00605: 3(5838.0/0.0)
* TSH >= 0.00605
	* FTI < 0.064255: 1(149.0/13.0)
	* FTI >= 0.064255
		* On_thyroxine < 0.5
			* TT4 < 0.1505
				* Thyroid_surgery < 0.5
					* TT4 < 0.058499999999999996
						* T3 < 0.01755: 2(5.0/1.0)
						* T3 >= 0.01755: 3(6.0/0.0)
					* TT4 >= 0.058499999999999996
						* T3 < 0.0295: 2(324.0/1.0)
						* T3 >= 0.0295
							* Age < 0.37: 2(6.0/0.0)
							* Age >= 0.37: 3(6.0/0.0)
				* Thyroid_surgery >= 0.5: 3(11.0/0.0)
			* TT4 >= 0.1505: 3(21.0/0.0)
		* On_thyroxine >= 0.5: 3(97.0/0.0)


