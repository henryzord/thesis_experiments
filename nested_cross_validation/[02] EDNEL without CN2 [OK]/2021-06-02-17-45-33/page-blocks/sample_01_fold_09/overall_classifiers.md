# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 1 | 0.898739 |
| Height <= 3 and P_black > 0.228 and Eccen > 7.5 and Mean_tr > 4.08 | 2 | 0.041515 |
| Height > 3 and Eccen <= 0.222 | 4 | 0.012815 |
| Height > 3 and Eccen > 0.222 and Height > 27 and P_black <= 0.331 and Eccen <= 3.8 | 5 | 0.007529 |
| Height <= 3 and P_black > 0.228 and Eccen > 7.5 and Mean_tr <= 4.08 and Mean_tr > 1.27 and Eccen > 12.5 | 2 | 0.007212 |
| Height > 3 and Eccen > 0.222 and Height <= 27 and Blackpix > 11 and Mean_tr > 15.9 and Eccen > 17.556 | 2 | 0.003461 |
| Height > 12.5 and Height <= 26.5 and P_black <= 0.1605 | 5 | 0.001966 |
| Height >= 3.5 and Eccen >= 0.236 and Height >= 27.5 and P_black >= 0.3015 and Eccen < 1.2934999999999999 | 3 | 0.003300 |
| Height > 3 and Eccen > 0.222 and Height <= 27 and Blackpix <= 11 and P_black <= 0.241 and Mean_tr <= 6 | 5 | 0.002059 |
| Height <= 2.5 and P_black > 0.3255 and P_black <= 0.4595 | 2 | 0.002618 |
| Height > 26.5 and Height <= 89 and P_black > 0.1605 and P_black <= 0.3255 | 5 | 0.002080 |
| Height > 89 and P_black > 0.3255 and P_black <= 0.4595 | 3 | 0.001050 |
| Height > 3 and Eccen > 0.222 and Height <= 27 and Blackpix > 11 and Mean_tr > 15.9 and Eccen <= 17.556 and P_black <= 0.289 | 2 | 0.000385 |
| Height < 3.5 and Mean_tr >= 1.355 and Eccen >= 7.5 and P_black >= 0.238 and Blackpix >= 7.5 and Mean_tr >= 2.8600000000000003 and Blackpix < 25.5 and Eccen < 24.0 and Blackpix < 10.5 | 2 | 0.003748 |
| Height > 3 and Eccen > 0.222 and Height > 27 and P_black <= 0.331 and Eccen > 3.8 and P_black <= 0.201 | 5 | 0.000553 |
| Height <= 2.5 and P_black > 0.4595 and P_black <= 0.6105 | 2 | 0.011282 |
| Height <= 2.5 and P_black > 0.9925 | 2 | 0.007469 |
| Height >= 3.5 and Eccen >= 0.236 and Height < 27.5 and Mean_tr < 21.295 and Blackpix >= 11.5 and P_and < 0.4975 and Height >= 11.5 and P_black < 0.1925 | 5 | 0.001568 |
| Height < 3.5 and Mean_tr >= 1.355 and Eccen >= 7.5 and P_black >= 0.238 and Blackpix >= 7.5 and Mean_tr < 2.8600000000000003 | 2 | 0.003244 |
| Height <= 2.5 and P_black > 0.6105 and P_black <= 0.7175 | 2 | 0.004522 |
| Height > 3 and Eccen > 0.222 and Height > 27 and P_black > 0.331 and Height <= 91 and Eccen <= 1.333 | 3 | 0.001763 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Height > 3.0 and Eccen > 0.222 and Height <= 27.0 and Mean_tr <= 21.29 and Blackpix > 14.0 and P_black > 0.158 | 1 | 0.887466 |
| Lenght <= 3.0 and Eccen <= 0.222 | 4 | 0.061987 |
| Height <= 3.0 and Mean_tr > 1.35 and Eccen > 7.5 and P_black > 0.24 | 2 | 0.272342 |
| Height <= 11.0 and Mean_tr <= 6.73 and Blackpix > 11.0 | 1 | 0.590804 |
| P_black <= 0.243 and Eccen <= 3.75 and Eccen > 0.25 and Wb_trans > 1.0 and Mean_tr > 1.91 | 5 | 0.147197 |
| Height <= 26.0 and Blackpix <= 182.0 and P_and > 0.326 and Lenght > 2.0 and P_black > 0.163 and Height > 1.0 and Mean_tr <= 9.5 and Eccen > 0.5 | 1 | 0.347620 |
| Height <= 26.0 and Eccen <= 1.141 and P_black > 0.44 and Blackpix > 9.0 | 1 | 0.108725 |
| Eccen > 1.143 and Mean_tr <= 13.0 and Wb_trans > 2.0 and Lenght > 12.0 and Height <= 82.0 | 1 | 0.160274 |
| Eccen <= 0.727 and Height <= 82.0 and P_black > 0.5 and Blackand <= 11.0 and P_and > 0.707 | 4 | 0.012768 |
| Height <= 26.0 and Blackand <= 16.0 | 1 | 0.152033 |
| Height <= 26.0 and Mean_tr > 9.5 and Eccen > 1.141 and Mean_tr > 34.88 | 2 | 0.101240 |
| Eccen > 0.25 and P_black <= 0.307 | 5 | 0.206897 |
| Mean_tr > 3.26 and Height > 26.0 and Lenght > 21.0 and Eccen <= 1.286 | 3 | 0.167010 |
| Eccen > 0.286 and Mean_tr > 32.11 | 1 | 0.178995 |
| Height > 20.0 and P_black <= 0.522 and Lenght <= 63.0 | 4 | 0.041459 |
| Height <= 20.0 | 2 | 0.381406 |
| Height <= 55.0 | 1 | 0.244482 |
|  | 3 | 0.250000 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

height|p_black|class
---|---|---
(3.5-4.5]|(0.9925-inf)|1
(89-inf)|(0.9925-inf)|4
(6.5-12.5]|(0.9925-inf)|4
(26.5-89]|(0.9925-inf)|4
(12.5-26.5]|(0.9925-inf)|4
(-inf-2.5]|(0.9925-inf)|2
(2.5-3.5]|(0.956-0.9925]|1
(-inf-2.5]|(0.956-0.9925]|2
(89-inf)|(0.7175-0.956]|3
(3.5-4.5]|(0.7175-0.956]|1
(4.5-6.5]|(0.7175-0.956]|1
(-inf-2.5]|(0.7175-0.956]|2
(6.5-12.5]|(0.7175-0.956]|1
(12.5-26.5]|(0.7175-0.956]|1
(2.5-3.5]|(0.7175-0.956]|1
(26.5-89]|(0.6105-0.7175]|1
(89-inf)|(0.6105-0.7175]|1
(3.5-4.5]|(0.6105-0.7175]|1
(-inf-2.5]|(0.6105-0.7175]|2
(2.5-3.5]|(0.6105-0.7175]|1
(12.5-26.5]|(0.6105-0.7175]|1
(6.5-12.5]|(0.6105-0.7175]|1
(4.5-6.5]|(0.6105-0.7175]|1
(89-inf)|(0.4595-0.6105]|3
(2.5-3.5]|(0.4595-0.6105]|2
(3.5-4.5]|(0.4595-0.6105]|1
(-inf-2.5]|(0.4595-0.6105]|2
(26.5-89]|(0.4595-0.6105]|3
(12.5-26.5]|(0.4595-0.6105]|1
(6.5-12.5]|(0.4595-0.6105]|1
(4.5-6.5]|(0.4595-0.6105]|1
(2.5-3.5]|(0.3255-0.4595]|2
(89-inf)|(0.3255-0.4595]|3
(-inf-2.5]|(0.3255-0.4595]|2
(3.5-4.5]|(0.3255-0.4595]|1
(12.5-26.5]|(0.3255-0.4595]|1
(26.5-89]|(0.3255-0.4595]|1
(4.5-6.5]|(0.3255-0.4595]|1
(6.5-12.5]|(0.3255-0.4595]|1
(89-inf)|(0.1605-0.3255]|5
(3.5-4.5]|(0.1605-0.3255]|1
(-inf-2.5]|(0.1605-0.3255]|1
(26.5-89]|(0.1605-0.3255]|5
(2.5-3.5]|(0.1605-0.3255]|2
(12.5-26.5]|(0.1605-0.3255]|1
(4.5-6.5]|(0.1605-0.3255]|1
(6.5-12.5]|(0.1605-0.3255]|1
(26.5-89]|(-inf-0.1605]|5
(89-inf)|(-inf-0.1605]|5
(2.5-3.5]|(-inf-0.1605]|1
(3.5-4.5]|(-inf-0.1605]|5
(12.5-26.5]|(-inf-0.1605]|5
(-inf-2.5]|(-inf-0.1605]|1
(4.5-6.5]|(-inf-0.1605]|1
(6.5-12.5]|(-inf-0.1605]|1

## PART

Decision list:

rules | predicted class
---|---
Height > 3.0 AND Eccen > 0.222 AND Height <= 27.0 AND Mean_tr <= 21.29 AND Blackpix > 14.0 AND P_black > 0.158|1 (2950.0/8.0)
Lenght <= 3.0 AND Eccen <= 0.222|4 (54.0/5.0)
Height <= 3.0 AND Mean_tr > 1.35 AND Eccen > 7.5 AND P_black > 0.24|2 (202.0/13.0)
Height <= 11.0 AND Mean_tr <= 6.73 AND Blackpix > 11.0|1 (222.0/5.0)
P_black <= 0.243 AND Eccen <= 3.75 AND Eccen > 0.25 AND Wb_trans > 1.0 AND Mean_tr > 1.91|5 (41.0)
Height <= 26.0 AND Blackpix <= 182.0 AND P_and > 0.326 AND Lenght > 2.0 AND P_black > 0.163 AND Height > 1.0 AND Mean_tr <= 9.5 AND Eccen > 0.5|1 (70.0/6.0)
Height <= 26.0 AND Eccen <= 1.141 AND P_black > 0.44 AND Blackpix > 9.0|1 (13.0)
Eccen > 1.143 AND Mean_tr <= 13.0 AND Wb_trans > 2.0 AND Lenght > 12.0 AND Height <= 82.0|1 (37.0/7.0)
Eccen <= 0.727 AND Height <= 82.0 AND P_black > 0.5 AND Blackand <= 11.0 AND P_and > 0.707|4 (5.0/2.0)
Height <= 26.0 AND Blackand <= 16.0|1 (20.0/4.0)
Height <= 26.0 AND Mean_tr > 9.5 AND Eccen > 1.141 AND Mean_tr > 34.88|2 (13.0)
Eccen > 0.25 AND P_black <= 0.307|5 (20.0/8.0)
Mean_tr > 3.26 AND Height > 26.0 AND Lenght > 21.0 AND Eccen <= 1.286|3 (17.0/2.0)
Eccen > 0.286 AND Mean_tr > 32.11|1 (10.0)
Height > 20.0 AND P_black <= 0.522 AND Lenght <= 63.0|4 (5.0)
Height <= 20.0|2 (4.0/1.0)
Height <= 55.0|1 (3.0)
|3 (3.0)


## J48 Decision Tree

* Height <= 3
	* P_black <= 0.228: 1 (36.0/1.0)
	* P_black > 0.228
		* Eccen <= 7.5: 1 (34.0/5.0)
		* Eccen > 7.5
			* Mean_tr <= 4.08
				* Mean_tr <= 1.27
					* Lenght <= 84: 1 (11.0)
					* Lenght > 84: 2 (6.0/2.0)
				* Mean_tr > 1.27
					* Eccen <= 12.5: 1 (12.0/5.0)
					* Eccen > 12.5: 2 (43.0/5.0)
			* Mean_tr > 4.08: 2 (214.0/7.0)
* Height > 3
	* Eccen <= 0.222: 4 (78.0/8.0)
	* Eccen > 0.222
		* Height <= 27
			* Blackpix <= 11
				* P_black <= 0.241
					* Mean_tr <= 6: 5 (17.0/4.0)
					* Mean_tr > 6: 1 (7.0/4.0)
				* P_black > 0.241: 1 (88.0/14.0)
			* Blackpix > 11
				* Mean_tr <= 15.9
					* P_and <= 0.519
						* Wb_trans <= 34
							* Height <= 10: 1 (52.0/8.0)
							* Height > 10
								* P_black <= 0.156: 5 (11.0)
								* P_black > 0.156: 1 (13.0/3.0)
						* Wb_trans > 34: 1 (124.0)
					* P_and > 0.519: 1 (3987.0/10.0)
				* Mean_tr > 15.9
					* Eccen <= 17.556
						* P_black <= 0.289: 2 (9.0/5.0)
						* P_black > 0.289: 1 (52.0/1.0)
					* Eccen > 17.556: 2 (18.0/1.0)
		* Height > 27
			* P_black <= 0.331
				* Eccen <= 3.8: 5 (46.0/5.0)
				* Eccen > 3.8
					* P_black <= 0.201: 5 (6.0/2.0)
					* P_black > 0.201: 1 (13.0/3.0)
			* P_black > 0.331
				* Height <= 91
					* Eccen <= 1.333: 3 (14.0/3.0)
					* Eccen > 1.333: 1 (14.0/1.0)
				* Height > 91: 3 (13.0)


## SimpleCart Decision Tree

* Height < 3.5
	* Mean_tr < 1.355: 1(43.0/4.0)
	* Mean_tr >= 1.355
		* Eccen < 7.5
			* Height < 2.5: 1(6.0/5.0)
			* Height >= 2.5: 1(21.0/0.0)
		* Eccen >= 7.5
			* P_black < 0.238: 1(8.0/2.0)
			* P_black >= 0.238
				* Blackpix < 7.5: 1(5.0/5.0)
				* Blackpix >= 7.5
					* Mean_tr < 2.8600000000000003: 2(19.0/5.0)
					* Mean_tr >= 2.8600000000000003
						* Blackpix < 25.5
							* Eccen < 24.0
								* Blackpix < 10.5: 2(20.0/3.0)
								* Blackpix >= 10.5: 2(39.0/0.0)
							* Eccen >= 24.0: 2(5.0/4.0)
						* Blackpix >= 25.5: 2(161.0/1.0)
* Height >= 3.5
	* Eccen < 0.236: 4(70.0/8.0)
	* Eccen >= 0.236
		* Height < 27.5
			* Mean_tr < 21.295
				* Blackpix < 11.5
					* P_black < 0.241: 5(14.0/10.0)
					* P_black >= 0.241
						* Area < 11.0: 1(5.0/5.0)
						* Area >= 11.0
							* Eccen < 1.225
								* Height < 7.5: 1(56.0/3.0)
								* Height >= 7.5: 1(7.0/2.0)
							* Eccen >= 1.225: 1(6.0/4.0)
				* Blackpix >= 11.5
					* P_and < 0.4975
						* Height < 11.5
							* Mean_tr < 5.465
								* Blackpix < 25.5
									* P_black < 0.1565: 1(6.0/3.0)
									* P_black >= 0.1565: 1(8.0/1.0)
								* Blackpix >= 25.5: 1(103.0/0.0)
							* Mean_tr >= 5.465: 1(7.0/5.0)
						* Height >= 11.5
							* P_black < 0.1925: 5(11.0/5.0)
							* P_black >= 0.1925: 1(11.0/1.0)
					* P_and >= 0.4975: 1(4049.0/13.0)
			* Mean_tr >= 21.295
				* Eccen < 6.487: 1(21.0/3.0)
				* Eccen >= 6.487: 2(17.0/2.0)
		* Height >= 27.5
			* P_black < 0.3015
				* Eccen < 3.8120000000000003
					* Eccen < 2.6985: 5(32.0/1.0)
					* Eccen >= 2.6985: 5(9.0/3.0)
				* Eccen >= 3.8120000000000003: 1(8.0/7.0)
			* P_black >= 0.3015
				* Eccen < 1.2934999999999999: 3(18.0/2.0)
				* Eccen >= 1.2934999999999999: 1(18.0/8.0)


