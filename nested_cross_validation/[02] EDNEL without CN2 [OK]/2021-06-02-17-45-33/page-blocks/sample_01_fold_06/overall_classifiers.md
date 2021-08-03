# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Height >= 3.5 and Eccen >= 0.236 and Height < 27.5 and Mean_tr < 21.295 | 1 | 0.894324 |
| Height < 3.5 and Mean_tr >= 1.355 and Eccen >= 7.5 | 2 | 0.046560 |
| Height > 3.0 and Eccen <= 0.222 | 4 | 0.012854 |
| Height < 3.5 and Mean_tr < 1.355 | 1 | 0.073260 |
| Height >= 3.5 and Eccen >= 0.236 and Height >= 27.5 and P_black < 0.22999999999999998 | 5 | 0.007731 |
| Height <= 3.0 and Eccen <= 7.5 | 1 | 0.044925 |
| Height > 26.5 and Height <= 89 and Lenght > 32.5 and Lenght <= 535.5 and Wb_trans > 37.5 and Wb_trans <= 781 | 1 | 0.029037 |
| Height > 3.0 and Eccen > 0.222 and Height <= 27.0 and Blackpix > 14.0 and Mean_tr > 21.29 and Eccen <= 6.474 | 1 | 0.033380 |
| Height > 3.0 and Eccen > 0.222 and Height <= 27.0 and Blackpix > 14.0 and Mean_tr > 21.29 and Eccen > 6.474 | 2 | 0.003461 |
| Height > 3.0 and Eccen > 0.222 and Height <= 27.0 and Blackpix <= 14.0 and P_black <= 0.159 | 5 | 0.001934 |
| Height >= 3.5 and Eccen >= 0.236 and Height >= 27.5 and P_black >= 0.22999999999999998 and Eccen < 1.2934999999999999 | 3 | 0.003065 |
| Height > 3.0 and Eccen > 0.222 and Height <= 27.0 and Blackpix > 14.0 and Mean_tr <= 21.29 and P_and <= 0.497 and Height > 12.0 and P_black <= 0.153 | 5 | 0.001594 |
| Height <= 3.0 and Eccen > 7.5 and Mean_tr <= 4.08 and Mean_tr > 1.27 and Eccen <= 12.5 | 1 | 0.017081 |
| Height > 3.0 and Eccen > 0.222 and Height > 27.0 and P_black > 0.331 and Height > 87.0 | 3 | 0.002446 |
| Height <= 2.5 and Lenght > 5.5 and Lenght <= 30.5 and Wb_trans <= 1.5 | 2 | 0.008615 |
| Height > 26.5 and Height <= 89 and Lenght > 32.5 and Lenght <= 535.5 and Wb_trans > 781 | 1 | 0.004581 |
| Height > 12.5 and Height <= 26.5 and Lenght > 2.5 and Lenght <= 5.5 and Wb_trans > 1.5 and Wb_trans <= 7.5 | 5 | 0.000467 |
| Height > 3.5 and Height <= 4.5 and Lenght > 2.5 and Lenght <= 5.5 and Wb_trans > 1.5 and Wb_trans <= 7.5 | 5 | 0.000208 |
| Height <= 2.5 and Lenght > 30.5 and Lenght <= 32.5 and Wb_trans > 1.5 and Wb_trans <= 7.5 | 1 | 0.004500 |
| Height > 12.5 and Height <= 26.5 and Lenght > 5.5 and Lenght <= 30.5 and Wb_trans <= 1.5 | 5 | 0.000104 |
| Height > 26.5 and Height <= 89 and Lenght > 5.5 and Lenght <= 30.5 and Wb_trans > 37.5 and Wb_trans <= 781 | 5 | 0.000467 |
| Height > 89 and Lenght > 32.5 and Lenght <= 535.5 and Wb_trans > 37.5 and Wb_trans <= 781 | 5 | 0.000933 |
| Height > 12.5 and Height <= 26.5 and Lenght > 1.5 and Lenght <= 2.5 and Wb_trans <= 1.5 | 2 | 0.000072 |
| Height > 2.5 and Height <= 3.5 and Lenght > 32.5 and Lenght <= 535.5 and Wb_trans > 37.5 and Wb_trans <= 781 | 1 | 0.002004 |
| Height <= 2.5 and Lenght > 5.5 and Lenght <= 30.5 and Wb_trans > 1.5 and Wb_trans <= 7.5 | 2 | 0.005076 |
| Height > 6.5 and Height <= 12.5 and Lenght > 32.5 and Lenght <= 535.5 and Wb_trans > 1.5 and Wb_trans <= 7.5 | 2 | 0.000288 |
| Height > 3.0 and Eccen > 0.222 and Height > 27.0 and P_black > 0.331 and Height <= 87.0 and Eccen > 1.333 | 1 | 0.021762 |
| Height > 3.0 and Eccen > 0.222 and Height > 27.0 and P_black > 0.331 and Height <= 87.0 and Eccen <= 1.333 | 3 | 0.001836 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Height > 3 and Eccen > 0.222 and Height <= 27 and Blackpix > 14 and Mean_tr <= 21.29 and P_and > 0.497 | 1 | 0.888967 |
| Height <= 3 and P_black > 0.228 and Eccen > 7.5 and Mean_tr > 4.08 | 2 | 0.244636 |
| Eccen > 0.222 and Height <= 11 and Height > 2 and Blackpix <= 610 and Lenght > 2 and P_and > 0.314 and Mean_tr <= 9.5 and Wb_trans <= 7 and P_black > 0.178 | 1 | 0.262355 |
| Eccen > 0.222 and Height <= 11 and Height > 2 and Mean_tr <= 6.5 and Wb_trans > 7 | 1 | 0.305530 |
| Eccen <= 0.222 | 4 | 0.139717 |
| P_black <= 0.324 and Mean_tr > 1.27 and Eccen <= 4.8 and Blackand > 33 and P_black <= 0.229 | 5 | 0.161888 |
| Height <= 27 and Lenght > 5 and Mean_tr > 1.27 and Eccen <= 13.667 and P_and > 0.326 | 1 | 0.242126 |
| Height <= 26 and Eccen > 1.364 and Mean_tr > 1.27 | 2 | 0.235730 |
| Height <= 7 | 1 | 0.444408 |
| P_black > 0.331 and Height <= 87 and Eccen <= 1.8 | 3 | 0.051587 |
| Height > 87 | 3 | 0.105495 |
| P_black <= 0.337 and Lenght <= 283 | 1 | 0.154589 |
| P_black <= 0.337 | 5 | 0.301350 |
|  | 1 | 0.528302 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Height >= 28 and P_black >= 0.338 and Blackpix >= 414 | 3 | 0.003187 |
| Eccen <= 0.222 | 4 | 0.012920 |
| Height >= 29 | 5 | 0.006284 |
| P_black <= 0.159 and Eccen <= 3.529 | 5 | 0.003730 |
| Height <= 3 and Mean_tr >= 9.06 and Eccen >= 43 | 2 | 0.025615 |
| Height <= 2 and P_black >= 0.412 | 2 | 0.022601 |
| Height <= 2 and Mean_tr >= 1.38 and Eccen >= 20 | 2 | 0.002402 |
| Mean_tr >= 30.25 and Lenght >= 39 | 2 | 0.003407 |
|  | 1 | 0.988372 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

height|lenght|wb_trans|class
---|---|---|---
(89-inf)|(535.5-inf)|(781-inf)|1
(6.5-12.5]|(32.5-535.5]|(781-inf)|1
(12.5-26.5]|(32.5-535.5]|(781-inf)|1
(26.5-89]|(32.5-535.5]|(781-inf)|1
(89-inf)|(32.5-535.5]|(781-inf)|3
(6.5-12.5]|(535.5-inf)|(37.5-781]|1
(-inf-2.5]|(535.5-inf)|(37.5-781]|1
(89-inf)|(32.5-535.5]|(37.5-781]|5
(2.5-3.5]|(32.5-535.5]|(37.5-781]|1
(-inf-2.5]|(32.5-535.5]|(37.5-781]|1
(26.5-89]|(32.5-535.5]|(37.5-781]|1
(3.5-4.5]|(32.5-535.5]|(37.5-781]|1
(12.5-26.5]|(32.5-535.5]|(37.5-781]|1
(4.5-6.5]|(32.5-535.5]|(37.5-781]|1
(6.5-12.5]|(32.5-535.5]|(37.5-781]|1
(26.5-89]|(30.5-32.5]|(37.5-781]|3
(2.5-3.5]|(535.5-inf)|(7.5-37.5]|2
(-inf-2.5]|(535.5-inf)|(7.5-37.5]|2
(4.5-6.5]|(30.5-32.5]|(37.5-781]|1
(6.5-12.5]|(30.5-32.5]|(37.5-781]|1
(89-inf)|(32.5-535.5]|(7.5-37.5]|1
(89-inf)|(5.5-30.5]|(37.5-781]|4
(12.5-26.5]|(5.5-30.5]|(37.5-781]|1
(3.5-4.5]|(5.5-30.5]|(37.5-781]|1
(4.5-6.5]|(5.5-30.5]|(37.5-781]|1
(26.5-89]|(5.5-30.5]|(37.5-781]|5
(2.5-3.5]|(32.5-535.5]|(7.5-37.5]|2
(12.5-26.5]|(32.5-535.5]|(7.5-37.5]|5
(26.5-89]|(32.5-535.5]|(7.5-37.5]|5
(4.5-6.5]|(32.5-535.5]|(7.5-37.5]|1
(6.5-12.5]|(32.5-535.5]|(7.5-37.5]|1
(6.5-12.5]|(5.5-30.5]|(37.5-781]|1
(3.5-4.5]|(32.5-535.5]|(7.5-37.5]|1
(-inf-2.5]|(32.5-535.5]|(7.5-37.5]|1
(26.5-89]|(2.5-5.5]|(37.5-781]|4
(2.5-3.5]|(30.5-32.5]|(7.5-37.5]|1
(-inf-2.5]|(30.5-32.5]|(7.5-37.5]|1
(12.5-26.5]|(30.5-32.5]|(7.5-37.5]|1
(4.5-6.5]|(30.5-32.5]|(7.5-37.5]|1
(-inf-2.5]|(535.5-inf)|(1.5-7.5]|2
(3.5-4.5]|(30.5-32.5]|(7.5-37.5]|1
(89-inf)|(2.5-5.5]|(37.5-781]|1
(6.5-12.5]|(30.5-32.5]|(7.5-37.5]|1
(2.5-3.5]|(5.5-30.5]|(7.5-37.5]|1
(26.5-89]|(32.5-535.5]|(1.5-7.5]|1
(-inf-2.5]|(5.5-30.5]|(7.5-37.5]|1
(6.5-12.5]|(32.5-535.5]|(1.5-7.5]|2
(3.5-4.5]|(32.5-535.5]|(1.5-7.5]|2
(4.5-6.5]|(32.5-535.5]|(1.5-7.5]|2
(2.5-3.5]|(32.5-535.5]|(1.5-7.5]|2
(-inf-2.5]|(32.5-535.5]|(1.5-7.5]|2
(26.5-89]|(5.5-30.5]|(7.5-37.5]|5
(12.5-26.5]|(32.5-535.5]|(1.5-7.5]|1
(3.5-4.5]|(5.5-30.5]|(7.5-37.5]|1
(4.5-6.5]|(5.5-30.5]|(7.5-37.5]|1
(12.5-26.5]|(5.5-30.5]|(7.5-37.5]|1
(6.5-12.5]|(5.5-30.5]|(7.5-37.5]|1
(-inf-2.5]|(535.5-inf)|(-inf-1.5]|1
(6.5-12.5]|(535.5-inf)|(-inf-1.5]|1
(26.5-89]|(2.5-5.5]|(7.5-37.5]|4
(89-inf)|(2.5-5.5]|(7.5-37.5]|1
(-inf-2.5]|(30.5-32.5]|(1.5-7.5]|1
(6.5-12.5]|(2.5-5.5]|(7.5-37.5]|1
(6.5-12.5]|(30.5-32.5]|(1.5-7.5]|1
(2.5-3.5]|(32.5-535.5]|(-inf-1.5]|1
(12.5-26.5]|(32.5-535.5]|(-inf-1.5]|1
(12.5-26.5]|(5.5-30.5]|(1.5-7.5]|1
(4.5-6.5]|(32.5-535.5]|(-inf-1.5]|2
(-inf-2.5]|(32.5-535.5]|(-inf-1.5]|2
(2.5-3.5]|(5.5-30.5]|(1.5-7.5]|1
(-inf-2.5]|(5.5-30.5]|(1.5-7.5]|2
(3.5-4.5]|(5.5-30.5]|(1.5-7.5]|1
(6.5-12.5]|(5.5-30.5]|(1.5-7.5]|1
(4.5-6.5]|(5.5-30.5]|(1.5-7.5]|1
(-inf-2.5]|(30.5-32.5]|(-inf-1.5]|1
(2.5-3.5]|(2.5-5.5]|(1.5-7.5]|1
(3.5-4.5]|(2.5-5.5]|(1.5-7.5]|5
(12.5-26.5]|(2.5-5.5]|(1.5-7.5]|5
(4.5-6.5]|(2.5-5.5]|(1.5-7.5]|1
(6.5-12.5]|(2.5-5.5]|(1.5-7.5]|1
(6.5-12.5]|(1.5-2.5]|(1.5-7.5]|1
(-inf-2.5]|(5.5-30.5]|(-inf-1.5]|2
(4.5-6.5]|(5.5-30.5]|(-inf-1.5]|1
(3.5-4.5]|(5.5-30.5]|(-inf-1.5]|1
(12.5-26.5]|(5.5-30.5]|(-inf-1.5]|5
(2.5-3.5]|(5.5-30.5]|(-inf-1.5]|1
(6.5-12.5]|(5.5-30.5]|(-inf-1.5]|1
(12.5-26.5]|(2.5-5.5]|(-inf-1.5]|1
(26.5-89]|(2.5-5.5]|(-inf-1.5]|1
(89-inf)|(2.5-5.5]|(-inf-1.5]|1
(6.5-12.5]|(2.5-5.5]|(-inf-1.5]|1
(4.5-6.5]|(2.5-5.5]|(-inf-1.5]|1
(2.5-3.5]|(2.5-5.5]|(-inf-1.5]|1
(3.5-4.5]|(2.5-5.5]|(-inf-1.5]|1
(89-inf)|(1.5-2.5]|(-inf-1.5]|1
(3.5-4.5]|(1.5-2.5]|(-inf-1.5]|1
(4.5-6.5]|(1.5-2.5]|(-inf-1.5]|1
(12.5-26.5]|(1.5-2.5]|(-inf-1.5]|2
(6.5-12.5]|(1.5-2.5]|(-inf-1.5]|1
(89-inf)|(-inf-1.5]|(-inf-1.5]|1
(12.5-26.5]|(-inf-1.5]|(-inf-1.5]|4
(26.5-89]|(-inf-1.5]|(-inf-1.5]|4
(6.5-12.5]|(-inf-1.5]|(-inf-1.5]|4

## JRip

Decision list:

rules | predicted class
---|---
(Height >= 28) and (P_black >= 0.338) and (Blackpix >= 414)|3 (40.0/15.0)
(Eccen <= 0.222)|4 (80.0/9.0)
(Height >= 29)|5 (57.0/11.0)
(P_black <= 0.159) and (Eccen <= 3.529)|5 (49.0/19.0)
(Height <= 3) and (Mean_tr >= 9.06) and (Eccen >= 43)|2 (119.0/1.0)
(Height <= 2) and (P_black >= 0.412)|2 (140.0/20.0)
(Height <= 2) and (Mean_tr >= 1.38) and (Eccen >= 20)|2 (16.0/1.0)
(Mean_tr >= 30.25) and (Lenght >= 39)|2 (22.0/1.0)
|1 (4395.0/44.0)


## PART

Decision list:

rules | predicted class
---|---
Height > 3 AND Eccen > 0.222 AND Height <= 27 AND Blackpix > 14 AND Mean_tr <= 21.29 AND P_and > 0.497|1 (4003.0/8.0)
Height <= 3 AND P_black > 0.228 AND Eccen > 7.5 AND Mean_tr > 4.08|2 (219.0/8.0)
Eccen > 0.222 AND Height <= 11 AND Height > 2 AND Blackpix <= 610 AND Lenght > 2 AND P_and > 0.314 AND Mean_tr <= 9.5 AND Wb_trans <= 7 AND P_black > 0.178|1 (128.0/14.0)
Eccen > 0.222 AND Height <= 11 AND Height > 2 AND Mean_tr <= 6.5 AND Wb_trans > 7|1 (134.0/3.0)
Eccen <= 0.222|4 (80.0/9.0)
P_black <= 0.324 AND Mean_tr > 1.27 AND Eccen <= 4.8 AND Blackand > 33 AND P_black <= 0.229|5 (73.0/11.0)
Height <= 27 AND Lenght > 5 AND Mean_tr > 1.27 AND Eccen <= 13.667 AND P_and > 0.326|1 (68.0/14.0)
Height <= 26 AND Eccen > 1.364 AND Mean_tr > 1.27|2 (72.0/14.0)
Height <= 7|1 (73.0/10.0)
P_black > 0.331 AND Height <= 87 AND Eccen <= 1.8|3 (23.0/10.0)
Height > 87|3 (13.0/1.0)
P_black <= 0.337 AND Lenght <= 283|1 (12.0/3.0)
P_black <= 0.337|5 (11.0/4.0)
|1 (9.0)


## J48 Decision Tree

* Height <= 3.0
	* Eccen <= 7.5: 1 (36.0/7.0)
	* Eccen > 7.5
		* Mean_tr <= 4.08
			* Mean_tr <= 1.27: 1 (45.0/4.0)
			* Mean_tr > 1.27
				* Eccen <= 12.5: 1 (14.0/3.0)
				* Eccen > 12.5: 2 (43.0/8.0)
		* Mean_tr > 4.08: 2 (220.0/8.0)
* Height > 3.0
	* Eccen <= 0.222: 4 (80.0/9.0)
	* Eccen > 0.222
		* Height <= 27.0
			* Blackpix <= 14.0
				* P_black <= 0.159: 5 (21.0/7.0)
				* P_black > 0.159: 1 (162.0/21.0)
			* Blackpix > 14.0
				* Mean_tr <= 21.29
					* P_and <= 0.497
						* Height <= 12.0: 1 (124.0/10.0)
						* Height > 12.0
							* P_black <= 0.153: 5 (13.0/3.0)
							* P_black > 0.153: 1 (14.0/2.0)
					* P_and > 0.497: 1 (4003.0/8.0)
				* Mean_tr > 21.29
					* Eccen <= 6.474: 1 (21.0/2.0)
					* Eccen > 6.474: 2 (18.0/1.0)
		* Height > 27.0
			* P_black <= 0.331
				* P_black <= 0.21: 5 (44.0/4.0)
				* P_black > 0.21: 1 (19.0/7.0)
			* P_black > 0.331
				* Height <= 87.0
					* Eccen <= 1.333: 3 (16.0/4.0)
					* Eccen > 1.333: 1 (13.0/1.0)
				* Height > 87.0: 3 (12.0)


## SimpleCart Decision Tree

* Height < 3.5
	* Mean_tr < 1.355: 1(43.0/4.0)
	* Mean_tr >= 1.355
		* Eccen < 7.5: 1(27.0/7.0)
		* Eccen >= 7.5: 2(250.0/27.0)
* Height >= 3.5
	* Eccen < 0.236: 4(71.0/9.0)
	* Eccen >= 0.236
		* Height < 27.5
			* Mean_tr < 21.295: 1(4271.0/66.0)
			* Mean_tr >= 21.295
				* Eccen < 6.487: 1(19.0/2.0)
				* Eccen >= 6.487: 2(17.0/1.0)
		* Height >= 27.5
			* P_black < 0.22999999999999998: 5(42.0/5.0)
			* P_black >= 0.22999999999999998
				* Eccen < 1.2934999999999999: 3(19.0/5.0)
				* Eccen >= 1.2934999999999999: 1(24.0/9.0)


