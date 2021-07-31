# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 1 | 0.898739 |
| Height < 3.5 and Mean_tr >= 1.355 and Eccen >= 7.5 and P_black >= 0.197 | 2 | 0.048117 |
| Height >= 3.5 and Eccen < 0.236 | 4 | 0.012656 |
| Height >= 3.5 and Eccen >= 0.236 and Height >= 27.5 and P_black < 0.3015 and Eccen < 3.8120000000000003 | 5 | 0.008071 |
| Height >= 3.5 and Eccen >= 0.236 and Height >= 27.5 and P_black >= 0.3015 and Eccen < 1.2934999999999999 | 3 | 0.003343 |
| Height > 3 and Eccen > 0.2 and Height <= 27 and Blackpix <= 14 and P_black <= 0.158 | 5 | 0.001934 |
| Height >= 3.5 and Eccen >= 0.236 and Height < 27.5 and Mean_tr >= 36.19 and Eccen >= 9.237 | 2 | 0.002589 |
| Height >= 3.5 and Eccen >= 0.236 and Height >= 27.5 and P_black < 0.3015 and Eccen >= 3.8120000000000003 and P_black < 0.20550000000000002 | 5 | 0.000741 |
| Height <= 3 and Eccen > 2.833 and Mean_tr > 3.58 | 2 | 0.044039 |
| Height < 3.5 and Mean_tr < 1.355 and P_black >= 0.4315 | 2 | 0.000649 |
| Eccen > 0.236 and Eccen <= 0.5485 and Wb_trans > 7.5 and Wb_trans <= 30.5 | 5 | 0.000374 |
| Height >= 3.5 and Eccen >= 0.236 and Height >= 27.5 and P_black >= 0.3015 and Eccen >= 1.2934999999999999 and Lenght >= 355.0 | 3 | 0.000654 |
| Eccen > 1.3605 and Eccen <= 6.755 and Wb_trans > 785 | 5 | 0.001220 |
| Eccen > 34.9445 and Eccen <= 66.9375 and Wb_trans > 1.5 and Wb_trans <= 5.5 | 2 | 0.004982 |
| Height > 3 and Eccen > 0.2 and Height <= 27 and Blackpix > 14 and P_and > 0.507 and Mean_tr > 16.68 and Eccen > 15.222 | 2 | 0.002374 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Height > 3.0 and Eccen > 0.222 and Height <= 27.0 and Blackpix > 14.0 and Mean_tr <= 21.52 and P_and > 0.515 | 1 | 0.888017 |
| Height <= 3.0 and Mean_tr > 1.35 and Lenght > 5.0 and Mean_tr > 7.25 | 2 | 0.211807 |
| Eccen > 0.222 and Height <= 11.0 and Height > 2.0 and Lenght > 2.0 and Mean_tr <= 2.99 | 1 | 0.390358 |
| Eccen > 0.222 and Height <= 11.0 and Eccen <= 2.8 and P_black > 0.277 | 1 | 0.207619 |
| Eccen <= 0.222 | 4 | 0.136620 |
| Height <= 5.0 and Mean_tr > 1.29 and P_black > 0.238 and Eccen > 12.25 | 2 | 0.164228 |
| P_black <= 0.324 and Mean_tr > 1.42 and Eccen <= 3.795 and P_black <= 0.199 | 5 | 0.196169 |
| Height <= 27.0 and Eccen > 0.684 and P_black <= 0.407 | 1 | 0.396748 |
| P_black <= 0.325 and Blackpix <= 4409.0 and Blackand <= 2122.0 | 5 | 0.068224 |
| Height <= 26.0 and Eccen <= 7.5 | 1 | 0.078533 |
| Height <= 26.0 and Blackpix > 15.0 | 2 | 0.155172 |
| P_black <= 0.331 and Blackpix <= 4409.0 | 1 | 0.123288 |
| P_black > 0.331 and Lenght > 21.0 and Height <= 87.0 and Eccen <= 1.333 | 3 | 0.103448 |
| P_black > 0.331 and Height <= 79.0 | 1 | 0.301985 |
| P_black > 0.331 | 3 | 0.134769 |
|  | 5 | 0.355556 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Height >= 28 and P_black >= 0.338 and Lenght >= 31 | 3 | 0.002966 |
| Eccen <= 0.222 | 4 | 0.012721 |
| Height >= 29 | 5 | 0.006573 |
| P_black <= 0.158 and Eccen <= 3.529 | 5 | 0.004043 |
| Height <= 3 and Blackpix >= 26 and Mean_tr >= 2.97 | 2 | 0.034726 |
| Height <= 2 and P_black >= 0.434 | 2 | 0.015046 |
| Height <= 4 and Eccen >= 12 and Mean_tr >= 1.38 and P_and >= 1 | 2 | 0.001805 |
| Mean_tr >= 22 and Eccen >= 2.25 | 2 | 0.002021 |
|  | 1 | 0.989036 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

eccen|wb_trans|class
---|---|---
(6.755-34.9445]|(785-inf)|1
(0.5485-1.3605]|(785-inf)|3
(1.3605-6.755]|(785-inf)|5
(34.9445-66.9375]|(785-inf)|1
(-inf-0.236]|(30.5-785]|4
(0.236-0.5485]|(30.5-785]|1
(66.9375-inf)|(30.5-785]|1
(0.5485-1.3605]|(30.5-785]|5
(34.9445-66.9375]|(30.5-785]|1
(1.3605-6.755]|(30.5-785]|1
(6.755-34.9445]|(30.5-785]|1
(-inf-0.236]|(7.5-30.5]|4
(66.9375-inf)|(7.5-30.5]|2
(34.9445-66.9375]|(7.5-30.5]|2
(0.236-0.5485]|(7.5-30.5]|5
(6.755-34.9445]|(7.5-30.5]|1
(0.5485-1.3605]|(7.5-30.5]|1
(1.3605-6.755]|(7.5-30.5]|1
(-inf-0.236]|(5.5-7.5]|1
(0.236-0.5485]|(5.5-7.5]|1
(66.9375-inf)|(5.5-7.5]|2
(34.9445-66.9375]|(5.5-7.5]|2
(6.755-34.9445]|(5.5-7.5]|2
(1.3605-6.755]|(5.5-7.5]|1
(0.5485-1.3605]|(5.5-7.5]|1
(34.9445-66.9375]|(1.5-5.5]|2
(1.3605-6.755]|(1.5-5.5]|1
(0.5485-1.3605]|(1.5-5.5]|1
(6.755-34.9445]|(1.5-5.5]|2
(66.9375-inf)|(1.5-5.5]|2
(0.236-0.5485]|(1.5-5.5]|1
(34.9445-66.9375]|(-inf-1.5]|2
(1.3605-6.755]|(-inf-1.5]|1
(-inf-0.236]|(-inf-1.5]|4
(66.9375-inf)|(-inf-1.5]|2
(6.755-34.9445]|(-inf-1.5]|2
(0.236-0.5485]|(-inf-1.5]|1
(0.5485-1.3605]|(-inf-1.5]|1

## JRip

Decision list:

rules | predicted class
---|---
(Height >= 28) and (P_black >= 0.338) and (Lenght >= 31)|3 (43.0/18.0)
(Eccen <= 0.222)|4 (79.0/9.0)
(Height >= 29)|5 (61.0/12.0)
(P_black <= 0.158) and (Eccen <= 3.529)|5 (46.0/16.0)
(Height <= 3) and (Blackpix >= 26) and (Mean_tr >= 2.97)|2 (166.0/3.0)
(Height <= 2) and (P_black >= 0.434)|2 (98.0/16.0)
(Height <= 4) and (Eccen >= 12) and (Mean_tr >= 1.38) and (P_and >= 1)|2 (17.0/2.0)
(Mean_tr >= 22) and (Eccen >= 2.25)|2 (19.0/4.0)
|1 (4389.0/39.0)


## PART

Decision list:

rules | predicted class
---|---
Height > 3.0 AND Eccen > 0.222 AND Height <= 27.0 AND Blackpix > 14.0 AND Mean_tr <= 21.52 AND P_and > 0.515|1 (3963.0/7.0)
Height <= 3.0 AND Mean_tr > 1.35 AND Lenght > 5.0 AND Mean_tr > 7.25|2 (191.0/6.0)
Eccen > 0.222 AND Height <= 11.0 AND Height > 2.0 AND Lenght > 2.0 AND Mean_tr <= 2.99|1 (225.0/12.0)
Eccen > 0.222 AND Height <= 11.0 AND Eccen <= 2.8 AND P_black > 0.277|1 (103.0/10.0)
Eccen <= 0.222|4 (79.0/9.0)
Height <= 5.0 AND Mean_tr > 1.29 AND P_black > 0.238 AND Eccen > 12.25|2 (74.0/7.0)
P_black <= 0.324 AND Mean_tr > 1.42 AND Eccen <= 3.795 AND P_black <= 0.199|5 (62.0/7.0)
Height <= 27.0 AND Eccen > 0.684 AND P_black <= 0.407|1 (101.0/16.0)
P_black <= 0.325 AND Blackpix <= 4409.0 AND Blackand <= 2122.0|5 (16.0/5.0)
Height <= 26.0 AND Eccen <= 7.5|1 (14.0/3.0)
Height <= 26.0 AND Blackpix > 15.0|2 (12.0/1.0)
P_black <= 0.331 AND Blackpix <= 4409.0|1 (14.0/2.0)
P_black > 0.331 AND Lenght > 21.0 AND Height <= 87.0 AND Eccen <= 1.333|3 (16.0/4.0)
P_black > 0.331 AND Height <= 79.0|1 (25.0/5.0)
P_black > 0.331|3 (13.0)
|5 (10.0/1.0)


## J48 Decision Tree

* Height <= 3
	* Eccen <= 2.833: 1 (16.0)
	* Eccen > 2.833
		* Mean_tr <= 3.58
			* P_black <= 0.238: 1 (23.0/1.0)
			* P_black > 0.238
				* Eccen <= 12.5: 1 (9.0/2.0)
				* Eccen > 12.5
					* Mean_tr <= 1.27: 1 (14.0/4.0)
					* Mean_tr > 1.27: 2 (24.0/4.0)
		* Mean_tr > 3.58: 2 (158.0/8.0)
* Height > 3
	* Eccen <= 0.2: 4 (51.0/6.0)
	* Eccen > 0.2
		* Height <= 27
			* Blackpix <= 14
				* P_black <= 0.158: 5 (13.0/3.0)
				* P_black > 0.158: 1 (113.0/13.0)
			* Blackpix > 14
				* P_and <= 0.507: 1 (124.0/19.0)
				* P_and > 0.507
					* Mean_tr <= 16.68: 1 (2627.0/2.0)
					* Mean_tr > 16.68
						* Eccen <= 15.222: 1 (25.0/1.0)
						* Eccen > 15.222: 2 (8.0)
		* Height > 27
			* P_black <= 0.341
				* Eccen <= 4.1: 5 (32.0/3.0)
				* Eccen > 4.1: 1 (14.0/6.0)
			* P_black > 0.341
				* Eccen <= 1.235: 3 (14.0/1.0)
				* Eccen > 1.235: 1 (14.0/4.0)


## SimpleCart Decision Tree

* Height < 3.5
	* Mean_tr < 1.355
		* P_black < 0.4315: 1(44.0/1.0)
		* P_black >= 0.4315: 2(3.0/0.0)
	* Mean_tr >= 1.355
		* Eccen < 7.5: 1(27.0/7.0)
		* Eccen >= 7.5
			* P_black < 0.197: 1(6.0/1.0)
			* P_black >= 0.197: 2(253.0/21.0)
* Height >= 3.5
	* Eccen < 0.236: 4(70.0/9.0)
	* Eccen >= 0.236
		* Height < 27.5
			* Mean_tr < 36.19: 1(4277.0/68.0)
			* Mean_tr >= 36.19
				* Eccen < 9.237: 1(9.0/0.0)
				* Eccen >= 9.237: 2(12.0/0.0)
		* Height >= 27.5
			* P_black < 0.3015
				* Eccen < 3.8120000000000003: 5(42.0/3.0)
				* Eccen >= 3.8120000000000003
					* P_black < 0.20550000000000002: 5(5.0/2.0)
					* P_black >= 0.20550000000000002: 1(8.0/2.0)
			* P_black >= 0.3015
				* Eccen < 1.2934999999999999: 3(19.0/3.0)
				* Eccen >= 1.2934999999999999
					* Lenght < 355.0: 1(19.0/2.0)
					* Lenght >= 355.0: 3(4.0/1.0)


