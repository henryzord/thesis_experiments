# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 1 | 0.898557 |
| Height <= 3 and P_black > 0.238 and Eccen > 3.583 and Mean_tr > 9.95 | 2 | 0.033860 |
| Height <= 3 and P_black > 0.238 and Eccen > 3.583 and Mean_tr <= 9.95 and Mean_tr > 1.27 | 2 | 0.015347 |
| Height >= 3.5 and Eccen < 0.236 | 4 | 0.013214 |
| Height > 3 and Eccen > 0.222 and Height > 27 and P_black <= 0.309 and Eccen <= 3.8 | 5 | 0.008679 |
| Height >= 3.5 and Eccen >= 0.236 and Height < 28.5 and Mean_tr >= 30.134999999999998 and Eccen >= 6.487 | 2 | 0.003888 |
| Height > 3 and Eccen > 0.222 and Height <= 27 and Mean_tr <= 21.29 and Blackpix > 14 and P_black <= 0.156 and Eccen <= 3.462 | 5 | 0.001767 |
| Height > 3 and Eccen > 0.222 and Height > 27 and P_black > 0.309 and Eccen <= 1.286 | 3 | 0.003702 |
| Height >= 3.5 and Eccen >= 0.236 and Height < 28.5 and Mean_tr < 30.134999999999998 and Wb_trans < 5.5 and P_black < 0.1795 | 5 | 0.001571 |
| Height < 3.5 and Mean_tr < 1.355 and P_black >= 0.4075 | 2 | 0.000692 |
| Height >= 3.5 and Eccen >= 0.236 and Height >= 28.5 and P_black >= 0.3015 and Eccen >= 1.2934999999999999 and Height >= 81.0 | 3 | 0.000653 |
| Height > 26.5 and Height <= 92 and Wb_trans > 30.5 and Wb_trans <= 785 | 5 | 0.003043 |
| Height <= 2.5 and Wb_trans > 1.5 and Wb_trans <= 5.5 | 2 | 0.016525 |
| Height > 26.5 and Height <= 92 and Wb_trans > 785 | 5 | 0.000519 |
| Height > 3 and Eccen > 0.222 and Height <= 27 and Mean_tr <= 21.29 and Blackpix <= 14 and Area > 13 and P_black <= 0.241 and Wb_trans <= 4 | 5 | 0.000989 |
| Height > 3 and Eccen > 0.222 and Height <= 27 and Mean_tr > 21.29 and Eccen > 5.75 | 2 | 0.003536 |
| Height > 6.5 and Height <= 12.5 and Wb_trans <= 1.5 | 4 | 0.002747 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Height > 3 and Eccen > 0.222 and Height <= 27 and Mean_tr <= 21.29 and Blackpix > 14 and P_black > 0.156 and Eccen > 0.667 and Height > 4 and Height <= 24 | 1 | 0.884731 |
| Lenght <= 3 and Eccen <= 0.222 and Lenght <= 1 and Eccen <= 0.105 | 4 | 0.033583 |
| Height <= 3 and Mean_tr <= 1.35 and P_black <= 0.395 | 1 | 0.081349 |
| Height <= 3 and Lenght <= 7 and Height > 2 | 1 | 0.041408 |
| Height <= 3 and Mean_tr > 9.95 and Height <= 1 | 2 | 0.110240 |
| Height <= 3 and Blackpix > 21 and Height <= 2 | 2 | 0.105666 |
| Height <= 3 and P_black > 0.238 and Mean_tr <= 9.95 and Wb_trans <= 14 and Blackpix > 7 and Height <= 1 | 2 | 0.055656 |
| Lenght <= 3 and Eccen <= 0.222 and Lenght > 1 | 4 | 0.015287 |
| Lenght <= 2 and P_black <= 0.866 | 1 | 0.032181 |
| Lenght <= 2 and Area > 8 | 4 | 0.011173 |
| Height <= 27 and Lenght <= 2 and Height <= 7 | 4 | 0.008495 |
| Height <= 27 and Height > 3 and P_black <= 0.728 and Wb_trans > 34 | 1 | 0.467185 |
| Eccen > 6.474 and Mean_tr > 17.75 and Height <= 11 | 2 | 0.060599 |
| Height <= 12 and Lenght > 2 and Lenght <= 105 and Height > 3 and P_black > 0.241 and Lenght > 8 and Blackand > 37 | 1 | 0.127003 |
| Height <= 12 and Lenght > 2 and Lenght <= 105 and Height > 3 and P_and > 0.653 and Height > 4 and Wb_trans > 3 | 1 | 0.342494 |
| Height <= 26 and Lenght > 2 and Eccen > 3.583 and Mean_tr <= 4.71 and Area > 36 | 1 | 0.131694 |
| P_black <= 0.299 and Eccen <= 4.167 and Height > 12 and Lenght > 13 | 5 | 0.172805 |
| Height <= 26 and Lenght > 2 and Eccen <= 3.583 and P_black > 0.241 and Eccen <= 2.125 and Wb_trans > 1 and P_black <= 0.467 | 1 | 0.160150 |
| Eccen > 0.25 and Height <= 27 and P_black > 0.235 and Eccen <= 2.75 and Lenght <= 6 | 1 | 0.226538 |
| Eccen > 1.143 and Height > 55 | 1 | 0.043548 |
| Eccen > 1.143 and Eccen > 15.286 and Wb_trans > 18 | 2 | 0.035955 |
| Eccen > 1.143 and Eccen <= 15.286 and P_black > 0.232 and Wb_trans > 4 | 1 | 0.163743 |
| Blackand > 626 and Eccen <= 1.141 | 3 | 0.090539 |
| Eccen <= 0.25 | 4 | 0.041898 |
| P_black > 0.235 and Height <= 6 and Lenght <= 18 and Height <= 1 | 1 | 0.083104 |
| Height <= 3 and Blackpix <= 11 | 1 | 0.026471 |
| Height > 3 and P_black > 0.281 | 1 | 0.073386 |
| P_black <= 0.235 and Mean_tr <= 3.96 and Wb_trans > 5 and Height <= 8 | 1 | 0.083612 |
| P_black <= 0.235 and P_black > 0.116 and Lenght <= 11 and Lenght <= 8 | 5 | 0.048847 |
| P_black <= 0.228 and Lenght > 11 and P_black > 0.126 | 1 | 0.028617 |
| P_black > 0.223 | 2 | 0.208128 |
| Lenght > 12 | 2 | 0.034028 |
|  | 5 | 0.571429 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Height >= 28 and P_black >= 0.338 and Lenght >= 31 | 3 | 0.003036 |
| Eccen <= 0.222 | 4 | 0.013281 |
| Lenght <= 2 and Height <= 5 | 4 | 0.000519 |
| Height >= 28 | 5 | 0.006145 |
| P_black <= 0.159 and Eccen <= 3.529 | 5 | 0.003320 |
| Lenght <= 9 and P_and <= 0.65 and P_black <= 0.233 and Mean_tr <= 3.5 | 5 | 0.000953 |
| Height <= 3 and Mean_tr >= 9.06 and Eccen >= 41 | 2 | 0.024830 |
| Height <= 2 and P_black >= 0.41 and Blackpix >= 11 | 2 | 0.019739 |
| Height <= 4 and Mean_tr >= 4 and Eccen >= 8 | 2 | 0.005888 |
| Height <= 2 and Mean_tr >= 1.38 and Eccen >= 13 | 2 | 0.002216 |
| Mean_tr >= 21.3 and Eccen >= 6.5 | 2 | 0.003092 |
| Blackand <= 29 and Eccen >= 2.25 and Mean_tr >= 4 | 2 | 0.000553 |
| P_and <= 0.314 and Mean_tr >= 6.53 | 2 | 0.000401 |
|  | 1 | 0.993928 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

height|wb_trans|class
---|---|---
(6.5-12.5]|(785-inf)|1
(92-inf)|(785-inf)|3
(26.5-92]|(785-inf)|5
(12.5-26.5]|(785-inf)|1
(2.5-3.5]|(30.5-785]|1
(92-inf)|(30.5-785]|5
(3.5-4.5]|(30.5-785]|1
(26.5-92]|(30.5-785]|5
(-inf-2.5]|(30.5-785]|1
(4.5-6.5]|(30.5-785]|1
(6.5-12.5]|(30.5-785]|1
(12.5-26.5]|(30.5-785]|1
(92-inf)|(7.5-30.5]|1
(26.5-92]|(7.5-30.5]|1
(2.5-3.5]|(7.5-30.5]|2
(-inf-2.5]|(7.5-30.5]|2
(12.5-26.5]|(7.5-30.5]|1
(3.5-4.5]|(7.5-30.5]|1
(4.5-6.5]|(7.5-30.5]|1
(6.5-12.5]|(7.5-30.5]|1
(26.5-92]|(5.5-7.5]|1
(2.5-3.5]|(5.5-7.5]|1
(3.5-4.5]|(5.5-7.5]|1
(12.5-26.5]|(5.5-7.5]|1
(4.5-6.5]|(5.5-7.5]|1
(-inf-2.5]|(5.5-7.5]|2
(6.5-12.5]|(5.5-7.5]|1
(12.5-26.5]|(1.5-5.5]|1
(2.5-3.5]|(1.5-5.5]|2
(3.5-4.5]|(1.5-5.5]|1
(4.5-6.5]|(1.5-5.5]|1
(-inf-2.5]|(1.5-5.5]|2
(6.5-12.5]|(1.5-5.5]|1
(92-inf)|(-inf-1.5]|4
(26.5-92]|(-inf-1.5]|4
(-inf-2.5]|(-inf-1.5]|2
(3.5-4.5]|(-inf-1.5]|1
(2.5-3.5]|(-inf-1.5]|1
(4.5-6.5]|(-inf-1.5]|1
(12.5-26.5]|(-inf-1.5]|4
(6.5-12.5]|(-inf-1.5]|4

## JRip

Decision list:

rules | predicted class
---|---
(Height >= 28) and (P_black >= 0.338) and (Lenght >= 31)|3 (42.0/17.0)
(Eccen <= 0.222)|4 (80.0/8.0)
(Lenght <= 2) and (Height <= 5)|4 (10.0/5.0)
(Height >= 28)|5 (67.0/17.0)
(P_black <= 0.159) and (Eccen <= 3.529)|5 (48.0/20.0)
(Lenght <= 9) and (P_and <= 0.65) and (P_black <= 0.233) and (Mean_tr <= 3.5)|5 (8.0/2.0)
(Height <= 3) and (Mean_tr >= 9.06) and (Eccen >= 41)|2 (113.0/0.0)
(Height <= 2) and (P_black >= 0.41) and (Blackpix >= 11)|2 (101.0/6.0)
(Height <= 4) and (Mean_tr >= 4) and (Eccen >= 8)|2 (40.0/6.0)
(Height <= 2) and (Mean_tr >= 1.38) and (Eccen >= 13)|2 (19.0/3.0)
(Mean_tr >= 21.3) and (Eccen >= 6.5)|2 (18.0/2.0)
(Blackand <= 29) and (Eccen >= 2.25) and (Mean_tr >= 4)|2 (13.0/6.0)
(P_and <= 0.314) and (Mean_tr >= 6.53)|2 (5.0/2.0)
|1 (4355.0/19.0)


## PART

Decision list:

rules | predicted class
---|---
Height > 3 AND Eccen > 0.222 AND Height <= 27 AND Mean_tr <= 21.29 AND Blackpix > 14 AND P_black > 0.156 AND Eccen > 0.667 AND Height > 4 AND Height <= 24|1 (3834.0/2.0)
Lenght <= 3 AND Eccen <= 0.222 AND Lenght <= 1 AND Eccen <= 0.105|4 (37.0/1.0)
Height <= 3 AND Mean_tr <= 1.35 AND P_black <= 0.395|1 (41.0)
Height <= 3 AND Lenght <= 7 AND Height > 2|1 (20.0)
Height <= 3 AND Mean_tr > 9.95 AND Height <= 1|2 (92.0/3.0)
Height <= 3 AND Blackpix > 21 AND Height <= 2|2 (85.0)
Height <= 3 AND P_black > 0.238 AND Mean_tr <= 9.95 AND Wb_trans <= 14 AND Blackpix > 7 AND Height <= 1|2 (54.0/7.0)
Lenght <= 3 AND Eccen <= 0.222 AND Lenght > 1|4 (15.0/2.0)
Lenght <= 2 AND P_black <= 0.866|1 (14.0/3.0)
Lenght <= 2 AND Area > 8|4 (9.0/1.0)
Height <= 27 AND Lenght <= 2 AND Height <= 7|4 (8.0/1.0)
Height <= 27 AND Height > 3 AND P_black <= 0.728 AND Wb_trans > 34|1 (187.0/1.0)
Eccen > 6.474 AND Mean_tr > 17.75 AND Height <= 11|2 (32.0)
Height <= 12 AND Lenght > 2 AND Lenght <= 105 AND Height > 3 AND P_black > 0.241 AND Lenght > 8 AND Blackand > 37|1 (27.0)
Height <= 12 AND Lenght > 2 AND Lenght <= 105 AND Height > 3 AND P_and > 0.653 AND Height > 4 AND Wb_trans > 3|1 (100.0/3.0)
Height <= 26 AND Lenght > 2 AND Eccen > 3.583 AND Mean_tr <= 4.71 AND Area > 36|1 (30.0/1.0)
P_black <= 0.299 AND Eccen <= 4.167 AND Height > 12 AND Lenght > 13|5 (63.0/5.0)
Height <= 26 AND Lenght > 2 AND Eccen <= 3.583 AND P_black > 0.241 AND Eccen <= 2.125 AND Wb_trans > 1 AND P_black <= 0.467|1 (43.0/11.0)
Eccen > 0.25 AND Height <= 27 AND P_black > 0.235 AND Eccen <= 2.75 AND Lenght <= 6|1 (42.0)
Eccen > 1.143 AND Height > 55|1 (14.0/6.0)
Eccen > 1.143 AND Eccen > 15.286 AND Wb_trans > 18|2 (10.0/2.0)
Eccen > 1.143 AND Eccen <= 15.286 AND P_black > 0.232 AND Wb_trans > 4|1 (28.0/1.0)
Blackand > 626 AND Eccen <= 1.141|3 (18.0/1.0)
Eccen <= 0.25|4 (13.0/3.0)
P_black > 0.235 AND Height <= 6 AND Lenght <= 18 AND Height <= 1|1 (12.0/5.0)
Height <= 3 AND Blackpix <= 11|1 (11.0/5.0)
Height > 3 AND P_black > 0.281|1 (15.0/3.0)
P_black <= 0.235 AND Mean_tr <= 3.96 AND Wb_trans > 5 AND Height <= 8|1 (13.0/3.0)
P_black <= 0.235 AND P_black > 0.116 AND Lenght <= 11 AND Lenght <= 8|5 (11.0/5.0)
P_black <= 0.228 AND Lenght > 11 AND P_black > 0.126|1 (11.0/5.0)
P_black > 0.223|2 (11.0)
Lenght > 12|2 (10.0/5.0)
|5 (9.0)


## J48 Decision Tree

* Height <= 3
	* P_black <= 0.238: 1 (35.0/2.0)
	* P_black > 0.238
		* Eccen <= 3.583: 1 (24.0/1.0)
		* Eccen > 3.583
			* Mean_tr <= 9.95
				* Mean_tr <= 1.27: 1 (13.0/4.0)
				* Mean_tr > 1.27: 2 (92.0/17.0)
			* Mean_tr > 9.95: 2 (138.0/2.0)
* Height > 3
	* Eccen <= 0.222: 4 (65.0/5.0)
	* Eccen > 0.222
		* Height <= 27
			* Mean_tr <= 21.29
				* Blackpix <= 14
					* Area <= 13: 1 (11.0/5.0)
					* Area > 13
						* P_black <= 0.241
							* Wb_trans <= 4: 5 (13.0/7.0)
							* Wb_trans > 4: 1 (20.0/7.0)
						* P_black > 0.241: 1 (116.0/8.0)
				* Blackpix > 14
					* P_black <= 0.156
						* Eccen <= 3.462: 5 (19.0/8.0)
						* Eccen > 3.462: 1 (136.0/2.0)
					* P_black > 0.156: 1 (3288.0/5.0)
			* Mean_tr > 21.29
				* Eccen <= 5.75: 1 (17.0)
				* Eccen > 5.75: 2 (19.0/2.0)
		* Height > 27
			* P_black <= 0.309
				* Eccen <= 3.8: 5 (44.0/3.0)
				* Eccen > 3.8: 1 (13.0/6.0)
			* P_black > 0.309
				* Eccen <= 1.286: 3 (17.0)
				* Eccen > 1.286: 1 (20.0/4.0)


## SimpleCart Decision Tree

* Height < 3.5
	* Mean_tr < 1.355
		* P_black < 0.4075: 1(44.0/0.0)
		* P_black >= 0.4075: 2(4.0/1.0)
	* Mean_tr >= 1.355
		* Eccen < 7.5
			* Eccen < 2.6665: 1(20.0/0.0)
			* Eccen >= 2.6665: 1(9.0/7.0)
		* Eccen >= 7.5
			* P_black < 0.238: 1(8.0/2.0)
			* P_black >= 0.238
				* Blackpix < 7.5: 1(4.0/4.0)
				* Blackpix >= 7.5
					* Mean_tr < 2.875: 2(18.0/5.0)
					* Mean_tr >= 2.875
						* Blackpix < 25.5
							* Lenght < 24.0
								* Blackpix < 10.5
									* P_black < 0.7595000000000001: 2(8.0/0.0)
									* P_black >= 0.7595000000000001: 2(12.0/3.0)
								* Blackpix >= 10.5: 2(38.0/0.0)
							* Lenght >= 24.0: 2(6.0/4.0)
						* Blackpix >= 25.5
							* Eccen < 40.5: 2(34.0/2.0)
							* Eccen >= 40.5: 2(128.0/0.0)
* Height >= 3.5
	* Eccen < 0.236: 4(72.0/8.0)
	* Eccen >= 0.236
		* Height < 28.5
			* Mean_tr < 30.134999999999998
				* Wb_trans < 5.5
					* P_black < 0.1795: 5(12.0/7.0)
					* P_black >= 0.1795
						* Area < 11.0: 1(5.0/5.0)
						* Area >= 11.0: 1(136.0/19.0)
				* Wb_trans >= 5.5: 1(4133.0/33.0)
			* Mean_tr >= 30.134999999999998
				* Eccen < 6.487: 1(13.0/0.0)
				* Eccen >= 6.487: 2(19.0/1.0)
		* Height >= 28.5
			* P_black < 0.3015
				* Eccen < 3.8120000000000003: 5(44.0/2.0)
				* Eccen >= 3.8120000000000003: 1(7.0/5.0)
			* P_black >= 0.3015
				* Eccen < 1.2934999999999999: 3(16.0/0.0)
				* Eccen >= 1.2934999999999999
					* Height < 81.0: 1(15.0/1.0)
					* Height >= 81.0: 3(4.0/1.0)


