# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| TSH < 0.00605 | 3 | 0.923393 |
| TSH >= 0.00605 and FTI >= 0.064255 and On_thyroxine < 0.5 and TT4 < 0.1505 and Thyroid_surgery < 0.5 and TT4 >= 0.058499999999999996 and T3 < 0.0295 | 2 | 0.049838 |
| TSH >= 0.00605 and FTI < 0.064255 and T3 < 0.0265 | 1 | 0.021734 |
| TSH > 0.006 and FTI > 0.064 and On_thyroxine > 0.0 | 3 | 0.166954 |
| TSH > 0.006 and FTI > 0.064 and On_thyroxine <= 0.0 and TT4 > 0.15 | 3 | 0.041584 |
| TSH >= 0.00605 and FTI >= 0.064255 and On_thyroxine < 0.5 and TT4 < 0.1505 and Thyroid_surgery >= 0.5 | 3 | 0.022222 |
| TSH > 0.006 and FTI > 0.064 and On_thyroxine <= 0.0 and TT4 <= 0.15 and TT4 <= 0.058 and T3 > 0.0174 | 3 | 0.012245 |
| TSH > 0.006 and FTI > 0.064 and On_thyroxine <= 0.0 and TT4 <= 0.15 and TT4 > 0.058 and T3 > 0.029 and T4U <= 0.113 | 3 | 0.012245 |
| TSH > 0.006 and FTI > 0.064 and On_thyroxine <= 0.0 and TT4 <= 0.15 and TT4 > 0.058 and T3 > 0.029 and T4U > 0.113 | 2 | 0.001139 |
| TSH >= 0.00605 and FTI < 0.064255 and T3 >= 0.0265 | 3 | 0.008197 |
| TSH > 0.006 and FTI <= 0.064 and Thyroid_surgery <= 0.0 and T3 <= 0.025 and TSH <= 0.01679 and On_antithyroid_medication <= 0.0 and T4U > 0.12 and Age <= 0.5 | 3 | 0.004115 |
| TSH >= 0.00605 and FTI >= 0.064255 and On_thyroxine < 0.5 and TT4 < 0.1505 and Thyroid_surgery < 0.5 and TT4 < 0.058499999999999996 and T3 < 0.01755 | 2 | 0.000678 |
| TSH > 0.006 and FTI <= 0.064 and Thyroid_surgery <= 0.0 and T3 <= 0.025 and TSH > 0.01679 and I131_treatment > 0.0 and Age > 0.65 | 3 | 0.004115 |
| TSH > 0.006 and FTI <= 0.064 and Thyroid_surgery <= 0.0 and T3 <= 0.025 and TSH <= 0.01679 and On_antithyroid_medication > 0.0 | 3 | 0.004115 |
| TSH > 0.006 and FTI <= 0.064 and Thyroid_surgery > 0.0 and T4U > 0.131 | 3 | 0.004115 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| TSH <= 0.006 | 3 | 0.923393 |
| FTI <= 0.064 and Thyroid_surgery <= 0.0 and T3 <= 0.025 and I131_treatment <= 0.0 and TSH > 0.01679 | 1 | 0.202922 |
| FTI > 0.06451 and On_thyroxine <= 0.0 and TT4 <= 0.15 and TT4 > 0.058 and T3 <= 0.029 and Age > 0.42 and Sex <= 0.0 and Query_hypothyroid <= 0.0 and Query_hyperthyroid <= 0.0 and Sick <= 0.0 | 2 | 0.437587 |
| FTI <= 0.064 and On_antithyroid_medication <= 0.0 and T3 <= 0.026 and T4U <= 0.103 | 1 | 0.043836 |
| On_thyroxine > 0.0 and I131_treatment <= 0.0 | 3 | 0.323232 |
| FTI > 0.062 and TT4 <= 0.15 and Thyroid_surgery <= 0.0 and TT4 > 0.058 and T3 <= 0.029 and Query_hyperthyroid <= 0.0 and Query_hypothyroid <= 0.0 | 2 | 0.622271 |
| FTI > 0.063 and TT4 <= 0.148 and Thyroid_surgery <= 0.0 and I131_treatment <= 0.0 and T3 <= 0.02 and Query_hypothyroid > 0.0 | 2 | 0.376147 |
| FTI <= 0.063 and On_antithyroid_medication <= 0.0 and Thyroid_surgery > 0.0 and T4U <= 0.131 and T4U > 0.114 | 1 | 0.029412 |
| FTI <= 0.063 and On_antithyroid_medication > 0.0 | 3 | 0.063830 |
| FTI <= 0.063 and Thyroid_surgery > 0.0 and Age <= 0.47 | 3 | 0.043478 |
| FTI > 0.062 and TT4 > 0.148 | 3 | 0.323077 |
| FTI > 0.062 and Thyroid_surgery <= 0.0 and On_thyroxine <= 0.0 and Query_hyperthyroid > 0.0 and Tumor <= 0.0 | 2 | 0.338983 |
| FTI > 0.062 and Thyroid_surgery > 0.0 | 3 | 0.314286 |
| FTI <= 0.062 and I131_treatment <= 0.0 and T3 > 0.0083 and T3 <= 0.024 | 1 | 0.086957 |
| On_thyroxine > 0.0 and Age <= 0.55 | 1 | 0.011905 |
| On_thyroxine <= 0.0 and Query_hypothyroid > 0.0 and T3 > 0.0201 | 2 | 0.281250 |
| T4U <= 0.136 and T3 > 0.0174 | 3 | 0.600000 |
| On_thyroxine <= 0.0 and FTI > 0.071 | 2 | 0.529412 |
| I131_treatment > 0.0 | 3 | 0.833333 |
| Age <= 0.64 | 3 | 0.666667 |
|  | 2 | 0.500000 |


# Text representation of classifiers as-is

## PART

Decision list:

rules | predicted class
---|---
TSH <= 0.006|3 (5834.0)
FTI <= 0.064 AND Thyroid_surgery <= 0.0 AND T3 <= 0.025 AND I131_treatment <= 0.0 AND TSH > 0.01679|1 (125.0)
FTI > 0.06451 AND On_thyroxine <= 0.0 AND TT4 <= 0.15 AND TT4 > 0.058 AND T3 <= 0.029 AND Age > 0.42 AND Sex <= 0.0 AND Query_hypothyroid <= 0.0 AND Query_hyperthyroid <= 0.0 AND Sick <= 0.0|2 (144.0/2.0)
FTI <= 0.064 AND On_antithyroid_medication <= 0.0 AND T3 <= 0.026 AND T4U <= 0.103|1 (16.0)
On_thyroxine > 0.0 AND I131_treatment <= 0.0|3 (96.0)
FTI > 0.062 AND TT4 <= 0.15 AND Thyroid_surgery <= 0.0 AND TT4 > 0.058 AND T3 <= 0.029 AND Query_hyperthyroid <= 0.0 AND Query_hypothyroid <= 0.0|2 (113.0)
FTI > 0.063 AND TT4 <= 0.148 AND Thyroid_surgery <= 0.0 AND I131_treatment <= 0.0 AND T3 <= 0.02 AND Query_hypothyroid > 0.0|2 (41.0)
FTI <= 0.063 AND On_antithyroid_medication <= 0.0 AND Thyroid_surgery > 0.0 AND T4U <= 0.131 AND T4U > 0.114|1 (3.0)
FTI <= 0.063 AND On_antithyroid_medication > 0.0|3 (3.0)
FTI <= 0.063 AND Thyroid_surgery > 0.0 AND Age <= 0.47|3 (2.0)
FTI > 0.062 AND TT4 > 0.148|3 (21.0)
FTI > 0.062 AND Thyroid_surgery <= 0.0 AND On_thyroxine <= 0.0 AND Query_hyperthyroid > 0.0 AND Tumor <= 0.0|2 (20.0)
FTI > 0.062 AND Thyroid_surgery > 0.0|3 (10.0)
FTI <= 0.062 AND I131_treatment <= 0.0 AND T3 > 0.0083 AND T3 <= 0.024|1 (4.0)
On_thyroxine > 0.0 AND Age <= 0.55|1 (2.0/1.0)
On_thyroxine <= 0.0 AND Query_hypothyroid > 0.0 AND T3 > 0.0201|2 (9.0)
T4U <= 0.136 AND T3 > 0.0174|3 (14.0)
On_thyroxine <= 0.0 AND FTI > 0.071|2 (9.0)
I131_treatment > 0.0|3 (4.0)
Age <= 0.64|3 (2.0)
|2 (2.0/1.0)


## J48 Decision Tree

* TSH <= 0.006: 3 (5834.0)
* TSH > 0.006
	* FTI <= 0.064
		* Thyroid_surgery <= 0.0
			* T3 <= 0.025
				* TSH <= 0.01679
					* On_antithyroid_medication <= 0.0
						* T4U <= 0.12: 1 (11.0)
						* T4U > 0.12
							* Age <= 0.5: 3 (2.0)
							* Age > 0.5: 1 (2.0)
					* On_antithyroid_medication > 0.0: 3 (2.0)
				* TSH > 0.01679
					* I131_treatment <= 0.0: 1 (125.0)
					* I131_treatment > 0.0
						* Age <= 0.65: 1 (5.0)
						* Age > 0.65: 3 (2.0)
			* T3 > 0.025
				* T3 <= 0.026: 1 (2.0)
				* T3 > 0.026: 3 (4.0)
		* Thyroid_surgery > 0.0
			* T4U <= 0.131: 1 (5.0/1.0)
			* T4U > 0.131: 3 (2.0)
	* FTI > 0.064
		* On_thyroxine <= 0.0
			* TT4 <= 0.15
				* TT4 <= 0.058
					* T3 <= 0.0174: 2 (6.0/1.0)
					* T3 > 0.0174: 3 (6.0)
				* TT4 > 0.058
					* T3 <= 0.029
						* Age <= 0.42
							* Thyroid_surgery <= 0.0: 2 (76.0)
							* Thyroid_surgery > 0.0: 3 (10.0)
						* Age > 0.42: 2 (249.0/2.0)
					* T3 > 0.029
						* T4U <= 0.113: 3 (6.0)
						* T4U > 0.113: 2 (7.0)
			* TT4 > 0.15: 3 (21.0)
		* On_thyroxine > 0.0: 3 (97.0)


## SimpleCart Decision Tree

* TSH < 0.00605: 3(5834.0/0.0)
* TSH >= 0.00605
	* FTI < 0.064255
		* T3 < 0.0265: 1(149.0/9.0)
		* T3 >= 0.0265: 3(4.0/0.0)
	* FTI >= 0.064255
		* On_thyroxine < 0.5
			* TT4 < 0.1505
				* Thyroid_surgery < 0.5
					* TT4 < 0.058499999999999996
						* T3 < 0.01755: 2(5.0/1.0)
						* T3 >= 0.01755: 3(6.0/0.0)
					* TT4 >= 0.058499999999999996
						* T3 < 0.0295: 2(323.0/1.0)
						* T3 >= 0.0295
							* T4U < 0.113: 3(6.0/0.0)
							* T4U >= 0.113: 2(7.0/0.0)
				* Thyroid_surgery >= 0.5: 3(11.0/0.0)
			* TT4 >= 0.1505: 3(21.0/0.0)
		* On_thyroxine >= 0.5: 3(97.0/0.0)


