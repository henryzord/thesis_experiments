# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 1 | 0.898739 |
| Height < 3.5 and Mean_tr >= 1.355 and Eccen >= 9.75 | 2 | 0.045548 |
| Height >= 3.5 and Eccen < 0.236 | 4 | 0.012815 |
| Height > 3 and P_black <= 0.975 and Height > 26 and Eccen > 0.286 and P_black <= 0.331 and P_black <= 0.229 | 5 | 0.008135 |
| Height > 3 and P_black <= 0.975 and Height <= 26 and Eccen > 0.541 and Mean_tr <= 9.95 and P_black <= 0.159 and Eccen <= 3.667 and Mean_tr > 1.79 | 5 | 0.003260 |
| Height > 3 and P_black <= 0.975 and Height <= 26 and Eccen > 0.541 and Mean_tr > 9.95 and Eccen > 17.556 | 2 | 0.003461 |
| Height < 3.5 and Mean_tr >= 1.355 and Eccen < 9.75 and Height < 2.5 | 2 | 0.002153 |
| Height >= 3.5 and Eccen >= 0.236 and Height >= 27.5 and P_black >= 0.331 and Eccen < 1.3784999999999998 | 3 | 0.003542 |
| Height > 3 and P_black <= 0.975 and Height <= 26 and Eccen <= 0.541 and Lenght > 2 and P_black <= 0.336 | 5 | 0.001270 |
| Height <= 2.5 and Lenght > 32.5 and Lenght <= 535.5 | 2 | 0.021606 |
| Height > 26.5 and Height <= 82.5 and Lenght > 32.5 and Lenght <= 535.5 | 5 | 0.002980 |
| Height >= 3.5 and Eccen >= 0.236 and Height < 27.5 and Mean_tr < 30.134999999999998 and Wb_trans < 5.5 and P_black < 0.1795 | 5 | 0.002220 |
| Height >= 3.5 and Eccen >= 0.236 and Height < 27.5 and Mean_tr >= 30.134999999999998 and Eccen >= 6.487 | 2 | 0.003247 |
| Height > 82.5 and Lenght > 32.5 and Lenght <= 535.5 | 5 | 0.001896 |
| Height > 12.5 and Height <= 26.5 and Lenght > 1.5 and Lenght <= 2.5 | 2 | 0.000072 |
| Height > 3 and P_black > 0.975 | 4 | 0.010080 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Height > 3.5 and Eccen > 0.236 and Height <= 27.5 and Mean_tr <= 21.295 and Wb_trans > 5.5 and P_and > 0.5155 | 1 | 0.888369 |
| Height <= 3.5 and P_black > 0.2285 and Eccen > 2.8335 and Mean_tr > 9.975 | 2 | 0.198148 |
| Eccen <= 0.236 | 4 | 0.082011 |
| Height <= 2.5 and P_black > 0.2285 and Mean_tr > 1.275 and Blackpix <= 16.5 and Blackpix > 7.5 | 2 | 0.057236 |
| Height <= 24.5 and Height > 2.5 and Blackpix <= 990 and Lenght > 2.5 and Wb_trans <= 34.5 and P_black > 0.1595 and Lenght <= 35.5 | 1 | 0.440104 |
| Eccen > 4.391 and P_black <= 0.4015 and Area <= 10262 and Mean_tr <= 4.215 | 1 | 0.425578 |
| Eccen > 6.487 and Height <= 29.5 and Lenght > 13 and Wb_trans <= 13.5 | 2 | 0.154279 |
| P_black <= 0.331 and Mean_tr > 1.57 and P_black > 0.243 and Height <= 37.5 | 1 | 0.031034 |
| P_black <= 0.331 and Mean_tr > 1.76 and Eccen <= 8.9325 | 5 | 0.309648 |
| Eccen > 6 and Eccen <= 36.909 and P_black <= 0.7335 | 1 | 0.133704 |
| Eccen <= 6 and Height <= 26 | 1 | 0.191011 |
| Height <= 26 | 2 | 0.229056 |
| Height <= 81 and Eccen <= 1.3785 | 3 | 0.090509 |
| Height > 89 | 3 | 0.188406 |
|  | 1 | 0.500000 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Height >= 28 and P_black >= 0.338 and Lenght >= 31 | 3 | 0.003110 |
| Eccen <= 0.222 | 4 | 0.012881 |
| Height >= 28 | 5 | 0.006431 |
| P_black <= 0.159 and Eccen <= 3.529 | 5 | 0.003316 |
| Height <= 3 and Blackpix >= 26 and Mean_tr >= 2.97 | 2 | 0.034928 |
| Height <= 2 and P_black >= 0.41 | 2 | 0.014331 |
| Mean_tr >= 21.3 and Eccen >= 6.5 | 2 | 0.003299 |
| Height <= 2 and Mean_tr >= 1.38 and Eccen >= 23 | 2 | 0.001996 |
| Wb_trans <= 7 and Eccen >= 3.5 and Mean_tr >= 2.67 and P_black <= 0.364 | 2 | 0.001027 |
|  | 1 | 0.990587 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

height|lenght|class
---|---|---
(82.5-inf)|(535.5-inf)|1
(2.5-3.5]|(535.5-inf)|2
(-inf-2.5]|(535.5-inf)|2
(6.5-12.5]|(535.5-inf)|1
(82.5-inf)|(32.5-535.5]|5
(2.5-3.5]|(32.5-535.5]|2
(26.5-82.5]|(32.5-535.5]|5
(3.5-6.5]|(32.5-535.5]|1
(-inf-2.5]|(32.5-535.5]|2
(12.5-26.5]|(32.5-535.5]|1
(6.5-12.5]|(32.5-535.5]|1
(2.5-3.5]|(30.5-32.5]|1
(26.5-82.5]|(30.5-32.5]|3
(3.5-6.5]|(30.5-32.5]|1
(-inf-2.5]|(30.5-32.5]|2
(6.5-12.5]|(30.5-32.5]|1
(12.5-26.5]|(30.5-32.5]|1
(26.5-82.5]|(5.5-30.5]|5
(2.5-3.5]|(5.5-30.5]|1
(82.5-inf)|(5.5-30.5]|4
(12.5-26.5]|(5.5-30.5]|1
(-inf-2.5]|(5.5-30.5]|2
(6.5-12.5]|(5.5-30.5]|1
(3.5-6.5]|(5.5-30.5]|1
(82.5-inf)|(2.5-5.5]|4
(12.5-26.5]|(2.5-5.5]|5
(26.5-82.5]|(2.5-5.5]|4
(2.5-3.5]|(2.5-5.5]|1
(6.5-12.5]|(2.5-5.5]|1
(3.5-6.5]|(2.5-5.5]|1
(82.5-inf)|(1.5-2.5]|4
(12.5-26.5]|(1.5-2.5]|2
(3.5-6.5]|(1.5-2.5]|1
(6.5-12.5]|(1.5-2.5]|1
(12.5-26.5]|(-inf-1.5]|4
(26.5-82.5]|(-inf-1.5]|4
(82.5-inf)|(-inf-1.5]|4
(6.5-12.5]|(-inf-1.5]|4

## JRip

Decision list:

rules | predicted class
---|---
(Height >= 28) and (P_black >= 0.338) and (Lenght >= 31)|3 (41.0/16.0)
(Eccen <= 0.222)|4 (78.0/8.0)
(Height >= 28)|5 (64.0/14.0)
(P_black <= 0.159) and (Eccen <= 3.529)|5 (48.0/20.0)
(Height <= 3) and (Blackpix >= 26) and (Mean_tr >= 2.97)|2 (167.0/3.0)
(Height <= 2) and (P_black >= 0.41)|2 (98.0/18.0)
(Mean_tr >= 21.3) and (Eccen >= 6.5)|2 (18.0/1.0)
(Height <= 2) and (Mean_tr >= 1.38) and (Eccen >= 23)|2 (14.0/1.0)
(Wb_trans <= 7) and (Eccen >= 3.5) and (Mean_tr >= 2.67) and (P_black <= 0.364)|2 (14.0/6.0)
|1 (4376.0/34.0)


## PART

Decision list:

rules | predicted class
---|---
Height > 3.5 AND Eccen > 0.236 AND Height <= 27.5 AND Mean_tr <= 21.295 AND Wb_trans > 5.5 AND P_and > 0.5155|1 (3979.0/8.0)
Height <= 3.5 AND P_black > 0.2285 AND Eccen > 2.8335 AND Mean_tr > 9.975|2 (169.0/4.0)
Eccen <= 0.236|4 (78.0/8.0)
Height <= 2.5 AND P_black > 0.2285 AND Mean_tr > 1.275 AND Blackpix <= 16.5 AND Blackpix > 7.5|2 (55.0/11.0)
Height <= 24.5 AND Height > 2.5 AND Blackpix <= 990 AND Lenght > 2.5 AND Wb_trans <= 34.5 AND P_black > 0.1595 AND Lenght <= 35.5|1 (214.0/22.0)
Eccen > 4.391 AND P_black <= 0.4015 AND Area <= 10262 AND Mean_tr <= 4.215|1 (168.0/4.0)
Eccen > 6.487 AND Height <= 29.5 AND Lenght > 13 AND Wb_trans <= 13.5|2 (46.0/1.0)
P_black <= 0.331 AND Mean_tr > 1.57 AND P_black > 0.243 AND Height <= 37.5|1 (9.0)
P_black <= 0.331 AND Mean_tr > 1.76 AND Eccen <= 8.9325|5 (88.0/15.0)
Eccen > 6 AND Eccen <= 36.909 AND P_black <= 0.7335|1 (19.0/5.0)
Eccen <= 6 AND Height <= 26|1 (31.0/8.0)
Height <= 26|2 (22.0/3.0)
Height <= 81 AND Eccen <= 1.3785|3 (15.0/3.0)
Height > 89|3 (13.0)
|1 (12.0/1.0)


## J48 Decision Tree

* Height <= 3
	* P_black <= 0.228: 1 (23.0/1.0)
	* P_black > 0.228
		* Eccen <= 6.25: 1 (16.0/1.0)
		* Eccen > 6.25
			* Mean_tr <= 4.08
				* Mean_tr <= 1.25: 1 (12.0/3.0)
				* Mean_tr > 1.25: 2 (26.0/8.0)
			* Mean_tr > 4.08: 2 (158.0/6.0)
* Height > 3
	* P_black <= 0.975
		* Height <= 26
			* Eccen <= 0.541
				* Lenght <= 2
					* Height <= 7: 1 (12.0/5.0)
					* Height > 7: 4 (6.0/2.0)
				* Lenght > 2
					* P_black <= 0.336: 5 (6.0/1.0)
					* P_black > 0.336: 1 (12.0/1.0)
			* Eccen > 0.541
				* Mean_tr <= 9.95
					* P_black <= 0.159
						* Eccen <= 3.667
							* Mean_tr <= 1.79: 1 (8.0/2.0)
							* Mean_tr > 1.79: 5 (18.0/2.0)
						* Eccen > 3.667: 1 (112.0/1.0)
					* P_black > 0.159: 1 (2661.0/9.0)
				* Mean_tr > 9.95
					* Eccen <= 17.556: 1 (77.0/4.0)
					* Eccen > 17.556: 2 (12.0/1.0)
		* Height > 26
			* Eccen <= 0.286: 4 (9.0/1.0)
			* Eccen > 0.286
				* P_black <= 0.331
					* P_black <= 0.229: 5 (35.0/4.0)
					* P_black > 0.229: 1 (12.0/4.0)
				* P_black > 0.331
					* Eccen <= 1.375: 3 (18.0/3.0)
					* Eccen > 1.375: 1 (10.0/2.0)
	* P_black > 0.975: 4 (36.0/2.0)


## SimpleCart Decision Tree

* Height < 3.5
	* Mean_tr < 1.355: 1(41.0/5.0)
	* Mean_tr >= 1.355
		* Eccen < 9.75
			* Height < 2.5: 2(17.0/12.0)
			* Height >= 2.5: 1(20.0/1.0)
		* Eccen >= 9.75: 2(239.0/20.0)
* Height >= 3.5
	* Eccen < 0.236: 4(70.0/8.0)
	* Eccen >= 0.236
		* Height < 27.5
			* Mean_tr < 30.134999999999998
				* Wb_trans < 5.5
					* P_black < 0.1795: 5(15.0/6.0)
					* P_black >= 0.1795: 1(142.0/23.0)
				* Wb_trans >= 5.5: 1(4138.0/27.0)
			* Mean_tr >= 30.134999999999998
				* Eccen < 6.487: 1(11.0/1.0)
				* Eccen >= 6.487: 2(16.0/1.0)
		* Height >= 27.5
			* P_black < 0.331
				* P_black < 0.22999999999999998: 5(44.0/5.0)
				* P_black >= 0.22999999999999998: 1(9.0/6.0)
			* P_black >= 0.331
				* Eccen < 1.3784999999999998: 3(20.0/3.0)
				* Eccen >= 1.3784999999999998: 1(13.0/5.0)


