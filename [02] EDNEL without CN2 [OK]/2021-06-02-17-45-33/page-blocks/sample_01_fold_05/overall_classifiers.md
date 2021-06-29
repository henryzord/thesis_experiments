# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 1 | 0.898739 |
| Height < 3.5 and Mean_tr >= 1.355 and Eccen >= 7.5 and P_black >= 0.238 | 2 | 0.047280 |
| Height >= 3.5 and Eccen < 0.225 | 4 | 0.013015 |
| Height > 3.5 and Eccen > 0.268 and Height > 27.5 and P_black <= 0.331 | 5 | 0.007692 |
| Height >= 3.5 and Eccen >= 0.225 and Height < 27.5 and Mean_tr >= 30.134999999999998 and Eccen >= 6.487 | 2 | 0.003247 |
| Height > 3.5 and Eccen > 0.268 and Height > 27.5 and P_black > 0.331 and Height > 90.0 | 3 | 0.002853 |
| Height > 3.5 and Eccen > 0.268 and Height <= 27.5 and Mean_tr <= 15.905000000000001 and Blackpix <= 14.5 and Lenght > 2.5 and P_black <= 0.2385 and Wb_trans <= 5.5 | 5 | 0.001358 |
| Height >= 3.5 and Eccen >= 0.225 and Height >= 27.5 and P_black >= 0.3015 and Height < 90.0 and Eccen < 1.2934999999999999 | 3 | 0.001570 |
| Height <= 2.5 and Lenght > 32.5 and Lenght <= 535.5 | 2 | 0.020043 |
| Height <= 2.5 and Lenght > 5.5 and Lenght <= 30.5 | 2 | 0.014101 |
| Height > 14.5 and Height <= 26.5 and Lenght > 2.5 and Lenght <= 5.5 | 5 | 0.000415 |
| Height > 14.5 and Height <= 26.5 and Lenght > 1.5 and Lenght <= 2.5 | 2 | 0.000072 |
| Height <= 3.5 and P_black > 0.2285 and Lenght > 7.5 and Mean_tr <= 4.09 and Mean_tr > 1.355 | 2 | 0.007054 |

## Ordered rules

### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Height >= 28 and Blackpix >= 10947 and Height <= 187 | 3 | 0.002446 |
| Height >= 28 and Height <= 29 and Lenght <= 32 and Wb_trans <= 62 | 3 | 0.001429 |
| Height >= 29 and P_black >= 0.338 and P_black <= 0.454 | 3 | 0.000426 |
| Eccen <= 0.091 and Eccen >= 0.029 | 4 | 0.005575 |
| Eccen <= 0.182 and Height >= 38 | 4 | 0.003105 |
| Lenght <= 2 and Eccen <= 0.182 and Height <= 19 and Mean_tr >= 8 and Height >= 10 | 4 | 0.001865 |
| Lenght <= 2 and P_black >= 1 and Area >= 8 and Height <= 8 | 4 | 0.001037 |
| Lenght <= 2 and P_black >= 1 and Height <= 9 and Height >= 9 | 4 | 0.001474 |
| Eccen <= 0.148 and Eccen >= 0.143 | 4 | 0.001067 |
| Lenght <= 2 and Blackand <= 10 | 4 | 0.000371 |
| Height >= 29 and P_black <= 0.201 and Mean_tr >= 2.69 | 5 | 0.006526 |
| P_and <= 0.541 and P_black <= 0.157 and P_and >= 0.338 and Eccen <= 2.033 | 5 | 0.004010 |
| P_and <= 0.655 and Eccen <= 3.795 and Area >= 850 and Wb_trans >= 136 and P_black >= 0.165 | 5 | 0.001714 |
| Wb_trans <= 7 and P_black <= 0.178 and Lenght <= 11 | 5 | 0.000756 |
| Eccen <= 0.833 and P_black <= 0.323 | 5 | 0.000546 |
| Mean_tr >= 9.06 and Area >= 43 and Height <= 2 | 2 | 0.023480 |
| Height <= 3 and Eccen >= 10 and Eccen <= 22 and Mean_tr >= 5.5 | 2 | 0.007361 |
| Height <= 3 and Mean_tr >= 1.38 and Eccen >= 35 and Wb_trans >= 6 | 2 | 0.009129 |
| Height <= 3 and Mean_tr >= 1.5 and Eccen >= 8 and P_black >= 0.632 and P_black <= 0.765 | 2 | 0.003583 |
| Height <= 2 and Eccen >= 28 and Eccen <= 39 and Mean_tr >= 2.13 | 2 | 0.003136 |
| Height <= 4 and Wb_trans <= 5 and Eccen >= 4.75 and Blackpix >= 8 and Blackpix <= 8 and Eccen <= 9 | 2 | 0.001571 |
| Height <= 4 and Wb_trans <= 5 and Eccen >= 12.5 and P_black <= 0.533 and Wb_trans >= 3 | 2 | 0.002913 |
| P_black >= 0.407 and Height <= 2 and Blackpix >= 11 and Lenght <= 20 | 2 | 0.001346 |
| Eccen >= 6.5 and Mean_tr >= 34 and Eccen <= 131 | 2 | 0.003806 |
| P_black >= 0.353 and Height <= 2 | 2 | 0.001660 |
| Mean_tr >= 10 and Eccen >= 20.118 and Mean_tr <= 30.27 | 2 | 0.000702 |
|  | 1 | 0.989478 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

height|lenght|class
---|---|---
(2.5-3.5]|(535.5-inf)|2
(6.5-11.5]|(535.5-inf)|1
(92-inf)|(535.5-inf)|1
(-inf-2.5]|(535.5-inf)|2
(92-inf)|(32.5-535.5]|3
(2.5-3.5]|(32.5-535.5]|2
(-inf-2.5]|(32.5-535.5]|2
(26.5-92]|(32.5-535.5]|5
(3.5-6.5]|(32.5-535.5]|1
(14.5-26.5]|(32.5-535.5]|1
(6.5-11.5]|(32.5-535.5]|1
(11.5-14.5]|(32.5-535.5]|1
(14.5-26.5]|(30.5-32.5]|1
(2.5-3.5]|(30.5-32.5]|1
(-inf-2.5]|(30.5-32.5]|1
(26.5-92]|(30.5-32.5]|3
(3.5-6.5]|(30.5-32.5]|1
(6.5-11.5]|(30.5-32.5]|1
(92-inf)|(5.5-30.5]|1
(26.5-92]|(5.5-30.5]|5
(2.5-3.5]|(5.5-30.5]|1
(-inf-2.5]|(5.5-30.5]|2
(11.5-14.5]|(5.5-30.5]|1
(14.5-26.5]|(5.5-30.5]|1
(3.5-6.5]|(5.5-30.5]|1
(6.5-11.5]|(5.5-30.5]|1
(92-inf)|(2.5-5.5]|4
(26.5-92]|(2.5-5.5]|4
(14.5-26.5]|(2.5-5.5]|5
(11.5-14.5]|(2.5-5.5]|1
(6.5-11.5]|(2.5-5.5]|1
(2.5-3.5]|(2.5-5.5]|1
(3.5-6.5]|(2.5-5.5]|1
(11.5-14.5]|(1.5-2.5]|4
(14.5-26.5]|(1.5-2.5]|2
(92-inf)|(1.5-2.5]|4
(6.5-11.5]|(1.5-2.5]|1
(3.5-6.5]|(1.5-2.5]|1
(92-inf)|(-inf-1.5]|1
(11.5-14.5]|(-inf-1.5]|4
(26.5-92]|(-inf-1.5]|4
(14.5-26.5]|(-inf-1.5]|4
(6.5-11.5]|(-inf-1.5]|4

## JRip

Decision list:

rules | predicted class
---|---
(Height >= 28) and (Blackpix >= 10947) and (Height <= 187)|3 (12.0/0.0)
(Height >= 28) and (Height <= 29) and (Lenght <= 32) and (Wb_trans <= 62)|3 (7.0/0.0)
(Height >= 29) and (P_black >= 0.338) and (P_black <= 0.454)|3 (12.0/7.0)
(Eccen <= 0.091) and (Eccen >= 0.029)|4 (25.0/0.0)
(Eccen <= 0.182) and (Height >= 38)|4 (15.0/0.0)
(Lenght <= 2) and (Eccen <= 0.182) and (Height <= 19) and (Mean_tr >= 8) and (Height >= 10)|4 (9.0/0.0)
(Lenght <= 2) and (P_black >= 1) and (Area >= 8) and (Height <= 8)|4 (5.0/0.0)
(Lenght <= 2) and (P_black >= 1) and (Height <= 9) and (Height >= 9)|4 (9.0/1.0)
(Eccen <= 0.148) and (Eccen >= 0.143)|4 (7.0/1.0)
(Lenght <= 2) and (Blackand <= 10)|4 (12.0/7.0)
(Height >= 29) and (P_black <= 0.201) and (Mean_tr >= 2.69)|5 (31.0/0.0)
(P_and <= 0.541) and (P_black <= 0.157) and (P_and >= 0.338) and (Eccen <= 2.033)|5 (19.0/0.0)
(P_and <= 0.655) and (Eccen <= 3.795) and (Area >= 850) and (Wb_trans >= 136) and (P_black >= 0.165)|5 (9.0/0.0)
(Wb_trans <= 7) and (P_black <= 0.178) and (Lenght <= 11)|5 (7.0/2.0)
(Eccen <= 0.833) and (P_black <= 0.323)|5 (39.0/29.0)
(Mean_tr >= 9.06) and (Area >= 43) and (Height <= 2)|2 (107.0/0.0)
(Height <= 3) and (Eccen >= 10) and (Eccen <= 22) and (Mean_tr >= 5.5)|2 (33.0/0.0)
(Height <= 3) and (Mean_tr >= 1.38) and (Eccen >= 35) and (Wb_trans >= 6)|2 (41.0/0.0)
(Height <= 3) and (Mean_tr >= 1.5) and (Eccen >= 8) and (P_black >= 0.632) and (P_black <= 0.765)|2 (16.0/0.0)
(Height <= 2) and (Eccen >= 28) and (Eccen <= 39) and (Mean_tr >= 2.13)|2 (14.0/0.0)
(Height <= 4) and (Wb_trans <= 5) and (Eccen >= 4.75) and (Blackpix >= 8) and (Blackpix <= 8) and (Eccen <= 9)|2 (7.0/0.0)
(Height <= 4) and (Wb_trans <= 5) and (Eccen >= 12.5) and (P_black <= 0.533) and (Wb_trans >= 3)|2 (13.0/0.0)
(P_black >= 0.407) and (Height <= 2) and (Blackpix >= 11) and (Lenght <= 20)|2 (6.0/0.0)
(Eccen >= 6.5) and (Mean_tr >= 34) and (Eccen <= 131)|2 (17.0/0.0)
(P_black >= 0.353) and (Height <= 2)|2 (49.0/30.0)
(Mean_tr >= 10) and (Eccen >= 20.118) and (Mean_tr <= 30.27)|2 (5.0/0.0)
|1 (4392.0/44.0)


## J48 Decision Tree

* Height <= 3.5
	* P_black <= 0.2285: 1 (30.0)
	* P_black > 0.2285
		* Lenght <= 7.5: 1 (25.0/3.0)
		* Lenght > 7.5
			* Mean_tr <= 4.09
				* Mean_tr <= 1.355: 1 (15.0/3.0)
				* Mean_tr > 1.355: 2 (51.0/12.0)
			* Mean_tr > 4.09: 2 (187.0/8.0)
* Height > 3.5
	* Eccen <= 0.268: 4 (71.0/9.0)
	* Eccen > 0.268
		* Height <= 27.5
			* Mean_tr <= 15.905000000000001
				* Blackpix <= 14.5
					* Lenght <= 2.5: 1 (13.0/5.0)
					* Lenght > 2.5
						* P_black <= 0.2385
							* Wb_trans <= 5.5: 5 (19.0/9.0)
							* Wb_trans > 5.5: 1 (12.0/2.0)
						* P_black > 0.2385: 1 (101.0/7.0)
				* Blackpix > 14.5: 1 (3617.0/26.0)
			* Mean_tr > 15.905000000000001: 1 (68.0/23.0)
		* Height > 27.5
			* P_black <= 0.331: 5 (60.0/16.0)
			* P_black > 0.331
				* Height <= 90.0
					* Eccen <= 1.2934999999999999: 3 (11.0/3.0)
					* Eccen > 1.2934999999999999: 1 (12.0/1.0)
				* Height > 90.0: 3 (12.0)


## SimpleCart Decision Tree

* Height < 3.5
	* Mean_tr < 1.355: 1(45.0/4.0)
	* Mean_tr >= 1.355
		* Eccen < 7.5: 1(28.0/7.0)
		* Eccen >= 7.5
			* P_black < 0.238: 1(8.0/2.0)
			* P_black >= 0.238: 2(247.0/19.0)
* Height >= 3.5
	* Eccen < 0.225: 4(71.0/8.0)
	* Eccen >= 0.225
		* Height < 27.5
			* Mean_tr < 30.134999999999998: 1(4275.0/67.0)
			* Mean_tr >= 30.134999999999998
				* Eccen < 6.487: 1(12.0/1.0)
				* Eccen >= 6.487: 2(16.0/1.0)
		* Height >= 27.5
			* P_black < 0.3015: 5(49.0/13.0)
			* P_black >= 0.3015
				* Height < 90.0
					* Eccen < 1.2934999999999999: 3(10.0/3.0)
					* Eccen >= 1.2934999999999999: 1(16.0/2.0)
				* Height >= 90.0: 3(14.0/0.0)


