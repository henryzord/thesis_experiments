# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 1 | 0.898557 |
| Height < 3.5 and Mean_tr >= 1.355 and Eccen >= 7.5 and Blackpix >= 7.5 and P_black >= 0.2285 and Mean_tr >= 2.8600000000000003 | 2 | 0.044291 |
| Height >= 3.5 and Eccen < 0.236 | 4 | 0.013547 |
| Height > 3 and Eccen > 0.222 and Height > 27 and P_black <= 0.331 and P_black <= 0.229 | 5 | 0.008455 |
| Height <= 3 and Mean_tr > 1.35 and Lenght > 7 and P_black > 0.228 and Mean_tr <= 9.95 and Height <= 1 | 2 | 0.014366 |
| Height > 3 and Eccen > 0.222 and Height <= 27 and Mean_tr > 21.29 and Eccen > 1.254 | 2 | 0.003521 |
| Height > 12.5 and Height <= 26.5 and P_black <= 0.1605 | 5 | 0.001693 |
| Height >= 3.5 and Eccen >= 0.236 and Height >= 28.5 and P_black >= 0.3015 and Height >= 90.0 | 3 | 0.002852 |
| Height >= 3.5 and Eccen >= 0.236 and Height < 28.5 and Mean_tr < 30.134999999999998 and Blackpix < 10.5 and P_black < 0.244 | 5 | 0.001593 |
| Height >= 3.5 and Eccen >= 0.236 and Height >= 28.5 and P_black < 0.3015 and P_black >= 0.22999999999999998 | 5 | 0.001021 |
| Height > 3 and Eccen > 0.222 and Height > 27 and P_black > 0.331 and Height <= 87 and Wb_trans <= 235 | 3 | 0.001453 |
| Height < 3.5 and Mean_tr >= 1.355 and Eccen < 7.5 and Eccen >= 2.6665 and Mean_tr >= 3.835 and Blackpix >= 7.5 | 2 | 0.000900 |
| Height <= 2.5 and P_black > 0.3375 and P_black <= 0.4685 | 2 | 0.002229 |
| Height >= 3.5 and Eccen >= 0.236 and Height < 28.5 and Mean_tr < 30.134999999999998 and Blackpix < 10.5 and P_black >= 0.244 and Area < 11.0 | 4 | 0.000574 |
| Height > 3 and Eccen > 0.222 and Height <= 27 and Mean_tr <= 21.29 and Blackpix <= 14 and Area > 11 and P_black > 0.159 and Blackpix <= 8 and Lenght > 4 | 5 | 0.000924 |
| Height < 3.5 and Mean_tr >= 1.355 and Eccen >= 7.5 and Blackpix >= 7.5 and P_black >= 0.2285 and Mean_tr < 2.8600000000000003 | 2 | 0.003449 |
| Height > 3 and Eccen > 0.222 and Height <= 27 and Mean_tr <= 21.29 and Blackpix <= 14 and Area > 11 and P_black <= 0.159 and Mean_tr > 2.36 | 5 | 0.001594 |
| Height <= 2.5 and P_black > 0.9925 | 2 | 0.007258 |
| Height > 2.5 and Height <= 3.5 and P_black > 0.3375 and P_black <= 0.4685 | 2 | 0.002642 |
| Height > 3 and Eccen > 0.222 and Height > 27 and P_black <= 0.331 and P_black > 0.229 and Height > 45 | 5 | 0.001129 |
| Height <= 2.5 and P_black > 0.4685 and P_black <= 0.6105 | 2 | 0.009816 |

## Ordered rules

### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Height >= 28 and P_black >= 0.338 and Lenght >= 31 and Eccen <= 1.333 | 3 | 0.003197 |
| Blackpix >= 17721 | 3 | 0.001021 |
| Eccen <= 0.222 | 4 | 0.013614 |
| Lenght <= 2 and Height <= 5 | 4 | 0.000577 |
| Height >= 28 and P_black <= 0.224 | 5 | 0.008634 |
| P_black <= 0.159 and Eccen <= 3.429 | 5 | 0.003706 |
| Blackand >= 12422 | 5 | 0.001153 |
| Blackand <= 30 and P_black <= 0.467 and Blackpix <= 8 and Lenght >= 5 and Height >= 4 | 5 | 0.000944 |
| Eccen <= 0.833 and Mean_tr <= 5.5 and P_and <= 0.554 | 5 | 0.000662 |
| Height <= 3 and Mean_tr >= 11.2 | 2 | 0.031096 |
| Height <= 2 and Mean_tr >= 1.6 and Blackpix >= 8 | 2 | 0.018347 |
| Mean_tr >= 15.91 and Eccen >= 19 | 2 | 0.003529 |
| Height <= 3 and Blackpix >= 59 | 2 | 0.000805 |
| Height <= 2 and Mean_tr >= 1.38 and Eccen >= 14 | 2 | 0.000376 |
| Wb_trans <= 1 and Eccen >= 2.25 | 2 | 0.000723 |
|  | 1 | 0.993928 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

height|p_black|class
---|---|---
(3.5-4.5]|(0.9925-inf)|1
(2.5-3.5]|(0.9925-inf)|1
(90-inf)|(0.9925-inf)|4
(12.5-26.5]|(0.9925-inf)|4
(26.5-90]|(0.9925-inf)|4
(-inf-2.5]|(0.9925-inf)|2
(6.5-12.5]|(0.9925-inf)|4
(2.5-3.5]|(0.954-0.9925]|1
(-inf-2.5]|(0.954-0.9925]|2
(3.5-4.5]|(0.7175-0.954]|1
(4.5-6.5]|(0.7175-0.954]|1
(90-inf)|(0.7175-0.954]|3
(6.5-12.5]|(0.7175-0.954]|1
(-inf-2.5]|(0.7175-0.954]|2
(12.5-26.5]|(0.7175-0.954]|1
(2.5-3.5]|(0.7175-0.954]|1
(90-inf)|(0.6105-0.7175]|1
(3.5-4.5]|(0.6105-0.7175]|1
(12.5-26.5]|(0.6105-0.7175]|1
(2.5-3.5]|(0.6105-0.7175]|2
(26.5-90]|(0.6105-0.7175]|4
(-inf-2.5]|(0.6105-0.7175]|2
(4.5-6.5]|(0.6105-0.7175]|1
(6.5-12.5]|(0.6105-0.7175]|1
(90-inf)|(0.4685-0.6105]|3
(2.5-3.5]|(0.4685-0.6105]|2
(26.5-90]|(0.4685-0.6105]|3
(-inf-2.5]|(0.4685-0.6105]|2
(3.5-4.5]|(0.4685-0.6105]|1
(12.5-26.5]|(0.4685-0.6105]|1
(4.5-6.5]|(0.4685-0.6105]|1
(6.5-12.5]|(0.4685-0.6105]|1
(90-inf)|(0.3375-0.4685]|3
(3.5-4.5]|(0.3375-0.4685]|1
(2.5-3.5]|(0.3375-0.4685]|2
(26.5-90]|(0.3375-0.4685]|1
(-inf-2.5]|(0.3375-0.4685]|2
(6.5-12.5]|(0.3375-0.4685]|1
(12.5-26.5]|(0.3375-0.4685]|1
(4.5-6.5]|(0.3375-0.4685]|1
(2.5-3.5]|(0.1605-0.3375]|2
(90-inf)|(0.1605-0.3375]|5
(26.5-90]|(0.1605-0.3375]|5
(3.5-4.5]|(0.1605-0.3375]|1
(-inf-2.5]|(0.1605-0.3375]|1
(12.5-26.5]|(0.1605-0.3375]|1
(4.5-6.5]|(0.1605-0.3375]|1
(6.5-12.5]|(0.1605-0.3375]|1
(2.5-3.5]|(-inf-0.1605]|1
(90-inf)|(-inf-0.1605]|5
(26.5-90]|(-inf-0.1605]|5
(12.5-26.5]|(-inf-0.1605]|5
(3.5-4.5]|(-inf-0.1605]|1
(-inf-2.5]|(-inf-0.1605]|1
(4.5-6.5]|(-inf-0.1605]|1
(6.5-12.5]|(-inf-0.1605]|1

## JRip

Decision list:

rules | predicted class
---|---
(Height >= 28) and (P_black >= 0.338) and (Lenght >= 31) and (Eccen <= 1.333)|3 (23.0/4.0)
(Blackpix >= 17721)|3 (5.0/0.0)
(Eccen <= 0.222)|4 (78.0/6.0)
(Lenght <= 2) and (Height <= 5)|4 (9.0/4.0)
(Height >= 28) and (P_black <= 0.224)|5 (45.0/2.0)
(P_black <= 0.159) and (Eccen <= 3.429)|5 (46.0/17.0)
(Blackand >= 12422)|5 (9.0/2.0)
(Blackand <= 30) and (P_black <= 0.467) and (Blackpix <= 8) and (Lenght >= 5) and (Height >= 4)|5 (10.0/3.0)
(Eccen <= 0.833) and (Mean_tr <= 5.5) and (P_and <= 0.554)|5 (7.0/2.0)
(Height <= 3) and (Mean_tr >= 11.2)|2 (154.0/6.0)
(Height <= 2) and (Mean_tr >= 1.6) and (Blackpix >= 8)|2 (106.0/11.0)
(Mean_tr >= 15.91) and (Eccen >= 19)|2 (20.0/1.0)
(Height <= 3) and (Blackpix >= 59)|2 (6.0/1.0)
(Height <= 2) and (Mean_tr >= 1.38) and (Eccen >= 14)|2 (6.0/1.0)
(Wb_trans <= 1) and (Eccen >= 2.25)|2 (14.0/6.0)
|1 (4381.0/20.0)


## J48 Decision Tree

* Height <= 3
	* Mean_tr <= 1.35: 1 (49.0/5.0)
	* Mean_tr > 1.35
		* Lenght <= 7: 1 (25.0/4.0)
		* Lenght > 7
			* P_black <= 0.228: 1 (9.0/2.0)
			* P_black > 0.228
				* Mean_tr <= 9.95
					* Height <= 1: 2 (88.0/11.0)
					* Height > 1
						* Area <= 45: 1 (9.0/4.0)
						* Area > 45: 2 (9.0/3.0)
				* Mean_tr > 9.95: 2 (166.0/4.0)
* Height > 3
	* Eccen <= 0.222: 4 (78.0/6.0)
	* Eccen > 0.222
		* Height <= 27
			* Mean_tr <= 21.29
				* Blackpix <= 14
					* Area <= 11: 4 (9.0/4.0)
					* Area > 11
						* P_black <= 0.159
							* Mean_tr <= 2.36: 1 (9.0/4.0)
							* Mean_tr > 2.36: 5 (13.0/3.0)
						* P_black > 0.159
							* Blackpix <= 8
								* Lenght <= 4: 1 (20.0/1.0)
								* Lenght > 4: 5 (11.0/4.0)
							* Blackpix > 8: 1 (117.0/4.0)
				* Blackpix > 14
					* P_and <= 0.497
						* Wb_trans <= 30
							* Eccen <= 4.7
								* Height <= 10: 1 (27.0/3.0)
								* Height > 10
									* P_black <= 0.156: 5 (10.0/1.0)
									* P_black > 0.156: 1 (10.0/3.0)
							* Eccen > 4.7: 1 (12.0/6.0)
						* Wb_trans > 30: 1 (98.0)
					* P_and > 0.497: 1 (3999.0/8.0)
			* Mean_tr > 21.29
				* Eccen <= 1.254: 1 (19.0)
				* Eccen > 1.254: 2 (27.0/6.0)
		* Height > 27
			* P_black <= 0.331
				* P_black <= 0.229: 5 (45.0/2.0)
				* P_black > 0.229
					* Height <= 45: 1 (11.0/2.0)
					* Height > 45: 5 (9.0/2.0)
			* P_black > 0.331
				* Height <= 87
					* Wb_trans <= 235: 3 (17.0/6.0)
					* Wb_trans > 235: 1 (9.0)
				* Height > 87: 3 (14.0)


## SimpleCart Decision Tree

* Height < 3.5
	* Mean_tr < 1.355: 1(44.0/5.0)
	* Mean_tr >= 1.355
		* Eccen < 7.5
			* Eccen < 2.6665: 1(16.0/0.0)
			* Eccen >= 2.6665
				* Mean_tr < 3.835: 1(5.0/1.0)
				* Mean_tr >= 3.835
					* Blackpix < 7.5: 1(4.0/2.0)
					* Blackpix >= 7.5: 2(5.0/1.0)
		* Eccen >= 7.5
			* Blackpix < 7.5: 1(8.0/3.0)
			* Blackpix >= 7.5
				* P_black < 0.2285: 1(4.0/2.0)
				* P_black >= 0.2285
					* Mean_tr < 2.8600000000000003: 2(20.0/5.0)
					* Mean_tr >= 2.8600000000000003: 2(222.0/8.0)
* Height >= 3.5
	* Eccen < 0.236: 4(72.0/6.0)
	* Eccen >= 0.236
		* Height < 28.5
			* Mean_tr < 30.134999999999998
				* Blackpix < 10.5
					* P_black < 0.244: 5(13.0/9.0)
					* P_black >= 0.244
						* Area < 11.0: 4(5.0/4.0)
						* Area >= 11.0
							* Eccen < 1.225
								* P_and < 0.6645000000000001: 1(16.0/2.0)
								* P_and >= 0.6645000000000001: 1(32.0/0.0)
							* Eccen >= 1.225: 1(3.0/3.0)
				* Blackpix >= 10.5: 1(4226.0/46.0)
			* Mean_tr >= 30.134999999999998
				* Eccen < 6.487: 1(14.0/1.0)
				* Eccen >= 6.487: 2(18.0/1.0)
		* Height >= 28.5
			* P_black < 0.3015
				* P_black < 0.22999999999999998: 5(42.0/2.0)
				* P_black >= 0.22999999999999998: 5(8.0/5.0)
			* P_black >= 0.3015
				* Height < 90.0
					* Eccen < 1.3505: 3(6.0/2.0)
					* Eccen >= 1.3505: 1(12.0/2.0)
				* Height >= 90.0: 3(14.0/0.0)


