# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| TSH < 0.00605 | 3 | 0.924161 |
| TSH >= 0.00605 and FTI >= 0.064255 and On_thyroxine < 0.5 and TT4 < 0.1495 and Thyroid_surgery < 0.5 and TT4 >= 0.058499999999999996 and T3 < 0.0295 | 2 | 0.049173 |
| TSH >= 0.00605 and FTI < 0.064255 | 1 | 0.020819 |
| TSH >= 0.00605 and FTI >= 0.064255 and On_thyroxine >= 0.5 | 3 | 0.175559 |
| TSH > 0.00605 and FTI > 0.064255 and On_thyroxine <= 0.5 and TT4 > 0.1505 | 3 | 0.043912 |
| TSH > 0.00605 and FTI > 0.064255 and On_thyroxine <= 0.5 and TT4 <= 0.1505 and TT4 > 0.0615 and T3 <= 0.0295 and Thyroid_surgery > 0.5 | 3 | 0.020450 |
| TSH > 0.00605 and FTI > 0.064255 and On_thyroxine <= 0.5 and TT4 <= 0.1505 and TT4 <= 0.0615 and T3 > 0.019549999999999998 | 3 | 0.014403 |
| TSH > 0.00605 and FTI > 0.064255 and On_thyroxine <= 0.5 and TT4 <= 0.1505 and TT4 > 0.0615 and T3 > 0.0295 | 2 | 0.000724 |
| TSH >= 0.00605 and FTI >= 0.064255 and On_thyroxine < 0.5 and TT4 < 0.1495 and Thyroid_surgery < 0.5 and TT4 < 0.058499999999999996 | 3 | 0.009242 |
| TSH > 0.00605 and FTI > 0.064255 and On_thyroxine <= 0.5 and TT4 <= 0.1505 and TT4 <= 0.0615 and T3 <= 0.019549999999999998 | 2 | 0.001316 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| TSH <= 0.006 | 3 | 0.924161 |
| FTI <= 0.064 and T3 <= 0.011 and Sex <= 0.0 and On_thyroxine <= 0.0 and Query_hypothyroid <= 0.0 | 1 | 0.106999 |
| FTI <= 0.064 and T3 <= 0.011 | 1 | 0.085492 |
| FTI <= 0.064 and TSH > 0.017 and Age <= 0.64 and T3 > 0.0144 | 1 | 0.042718 |
| On_thyroxine <= 0.0 and FTI > 0.064 and TT4 <= 0.149 and TT4 > 0.061 and T3 <= 0.028 and Age > 0.42 and Sex <= 0.0 and Query_hypothyroid <= 0.0 and Query_hyperthyroid <= 0.0 | 2 | 0.436224 |
| On_thyroxine <= 0.0 and FTI > 0.064 and TT4 <= 0.148 and Thyroid_surgery <= 0.0 and TT4 > 0.058 and T3 <= 0.029 | 2 | 0.493013 |
| FTI > 0.064 and On_thyroxine > 0.0 | 3 | 0.778626 |
| FTI > 0.064 and Thyroid_surgery <= 0.0 and TT4 > 0.148 | 3 | 0.431373 |
| FTI > 0.064 and Thyroid_surgery <= 0.0 and TT4 <= 0.118 | 3 | 0.204082 |
| TT4 <= 0.121 and Thyroid_surgery <= 0.0 and T3 <= 0.0208 | 1 | 0.217872 |
| TT4 <= 0.121 and Thyroid_surgery > 0.0 | 3 | 0.518519 |
| TT4 <= 0.097 | 3 | 0.421053 |
|  | 2 | 0.687500 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| FTI <= 0.064 and TSH >= 0.0062 and T3 <= 0.026 | 1 | 0.021453 |
| TSH >= 0.0061 and On_thyroxine <= 0 and TT4 <= 0.144 and Thyroid_surgery <= 0 and TT4 >= 0.06 | 2 | 0.049905 |
|  | 3 | 0.998668 |


# Text representation of classifiers as-is

## JRip

Decision list:

rules | predicted class
---|---
(FTI <= 0.064) and (TSH >= 0.0062) and (T3 <= 0.026)|1 (160.0/11.0)
(TSH >= 0.0061) and (On_thyroxine <= 0) and (TT4 <= 0.144) and (Thyroid_surgery <= 0) and (TT4 >= 0.06)|2 (327.0/5.0)
|3 (5992.0/8.0)


## PART

Decision list:

rules | predicted class
---|---
TSH <= 0.006|3 (5837.0)
FTI <= 0.064 AND T3 <= 0.011 AND Sex <= 0.0 AND On_thyroxine <= 0.0 AND Query_hypothyroid <= 0.0|1 (63.0/2.0)
FTI <= 0.064 AND T3 <= 0.011|1 (48.0)
FTI <= 0.064 AND TSH > 0.017 AND Age <= 0.64 AND T3 > 0.0144|1 (22.0)
On_thyroxine <= 0.0 AND FTI > 0.064 AND TT4 <= 0.149 AND TT4 > 0.061 AND T3 <= 0.028 AND Age > 0.42 AND Sex <= 0.0 AND Query_hypothyroid <= 0.0 AND Query_hyperthyroid <= 0.0|2 (144.0/2.0)
On_thyroxine <= 0.0 AND FTI > 0.064 AND TT4 <= 0.148 AND Thyroid_surgery <= 0.0 AND TT4 > 0.058 AND T3 <= 0.029|2 (177.0)
FTI > 0.064 AND On_thyroxine > 0.0|3 (102.0)
FTI > 0.064 AND Thyroid_surgery <= 0.0 AND TT4 > 0.148|3 (22.0)
FTI > 0.064 AND Thyroid_surgery <= 0.0 AND TT4 <= 0.118|3 (14.0/4.0)
TT4 <= 0.121 AND Thyroid_surgery <= 0.0 AND T3 <= 0.0208|1 (20.0/4.0)
TT4 <= 0.121 AND Thyroid_surgery > 0.0|3 (12.0)
TT4 <= 0.097|3 (9.0/2.0)
|2 (9.0/2.0)


## J48 Decision Tree

* TSH <= 0.00605: 3 (4665.0)
* TSH > 0.00605
	* FTI <= 0.064255: 1 (131.0/11.0)
	* FTI > 0.064255
		* On_thyroxine <= 0.5
			* TT4 <= 0.1505
				* TT4 <= 0.0615
					* T3 <= 0.019549999999999998: 2 (7.0/1.0)
					* T3 > 0.019549999999999998: 3 (6.0)
				* TT4 > 0.0615
					* T3 <= 0.0295
						* Thyroid_surgery <= 0.5: 2 (252.0/1.0)
						* Thyroid_surgery > 0.5: 3 (9.0)
					* T3 > 0.0295: 2 (11.0/4.0)
			* TT4 > 0.1505: 3 (16.0)
		* On_thyroxine > 0.5: 3 (87.0)


## SimpleCart Decision Tree

* TSH < 0.00605: 3(5837.0/0.0)
* TSH >= 0.00605
	* FTI < 0.064255: 1(149.0/16.0)
	* FTI >= 0.064255
		* On_thyroxine < 0.5
			* TT4 < 0.1495
				* Thyroid_surgery < 0.5
					* TT4 < 0.058499999999999996: 3(7.0/4.0)
					* TT4 >= 0.058499999999999996
						* T3 < 0.0295: 2(319.0/1.0)
						* T3 >= 0.0295: 2(7.0/5.0)
				* Thyroid_surgery >= 0.5: 3(10.0/0.0)
			* TT4 >= 0.1495: 3(22.0/0.0)
		* On_thyroxine >= 0.5: 3(102.0/0.0)


