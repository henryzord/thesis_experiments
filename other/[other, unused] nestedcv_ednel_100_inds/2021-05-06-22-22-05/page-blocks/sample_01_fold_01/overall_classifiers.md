# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 1 | 0.898557 |
| Height < 3.5 and Mean_tr >= 1.355 and Eccen >= 7.5 and P_black >= 0.2405 and Mean_tr >= 4.09 | 2 | 0.040727 |
| Height >= 3.5 and Eccen < 0.268 | 4 | 0.012854 |
| Height >= 3.5 and Eccen >= 0.268 and Height >= 27.5 and P_black < 0.257 and Eccen < 3.333 | 5 | 0.007415 |
| Height < 3.5 and Mean_tr >= 1.355 and Eccen >= 7.5 and P_black >= 0.2405 and Mean_tr < 4.09 and Eccen >= 12.5 | 2 | 0.006630 |
| Height >= 3.5 and Eccen >= 0.268 and Height < 27.5 and Mean_tr >= 30.134999999999998 and Eccen >= 6.487 | 2 | 0.003460 |
| Height >= 3.5 and Eccen >= 0.268 and Height >= 27.5 and P_black >= 0.257 and Eccen < 1.2934999999999999 | 3 | 0.003342 |
| Height >= 3.5 and Eccen >= 0.268 and Height < 27.5 and Mean_tr < 30.134999999999998 and Blackpix < 11.5 and P_black < 0.241 | 5 | 0.001626 |
| Height > 3.0 and Eccen > 0.25 and Height <= 27.0 and Blackpix > 11.0 and Mean_tr <= 21.18 and P_and <= 0.523 and Wb_trans <= 34.0 and Height > 12.0 and P_black <= 0.139 | 5 | 0.001678 |
| Height <= 2.5 and Wb_trans > 1.5 and Wb_trans <= 5.5 | 2 | 0.015913 |
| Height <= 3.0 and P_black > 0.228 and Lenght > 7.0 and Mean_tr <= 4.08 and Height <= 2.0 and Mean_tr <= 1.27 and P_black > 0.402 | 2 | 0.000676 |
| Height > 26.5 and Wb_trans > 37.5 and Wb_trans <= 785 | 5 | 0.002598 |
| Height <= 2.5 and Wb_trans <= 1.5 | 2 | 0.013614 |
| Height >= 3.5 and Eccen >= 0.268 and Height < 27.5 and Mean_tr < 30.134999999999998 and Blackpix < 11.5 and P_black >= 0.241 and P_black >= 0.6835 | 4 | 0.000574 |
| Height > 3.0 and Eccen > 0.25 and Height <= 27.0 and Blackpix > 11.0 and Mean_tr <= 21.18 and P_and <= 0.523 and Wb_trans <= 34.0 and Height <= 12.0 and Mean_tr > 5.1 and Eccen > 3.636 | 2 | 0.000676 |
| Height > 12.5 and Height <= 26.5 and Wb_trans > 1.5 and Wb_trans <= 5.5 | 5 | 0.000277 |
| Height > 3.0 and Eccen > 0.25 and Height > 27.0 and P_black > 0.331 and Height > 87.0 | 3 | 0.002243 |
| Height > 3.0 and Eccen > 0.25 and Height <= 27.0 and Blackpix > 11.0 and Mean_tr > 21.18 and Eccen > 1.254 and Height <= 11.0 and Height > 5.0 | 2 | 0.001536 |
| Height > 3.0 and Eccen > 0.25 and Height <= 27.0 and Blackpix > 11.0 and Mean_tr > 21.18 and Eccen > 1.254 and Height <= 11.0 and Height <= 5.0 | 2 | 0.001727 |
| Height <= 3.0 and P_black > 0.228 and Lenght > 7.0 and Mean_tr <= 4.08 and Height <= 2.0 and Mean_tr > 1.27 and Eccen > 12.5 and Wb_trans > 7.0 | 2 | 0.002804 |
| Height > 2.5 and Height <= 3.5 and Wb_trans > 1.5 and Wb_trans <= 5.5 | 2 | 0.000433 |
| Height > 3.0 and Eccen > 0.25 and Height > 27.0 and P_black > 0.331 and Height <= 87.0 and Eccen <= 1.333 and Wb_trans > 59.0 | 3 | 0.000638 |
| Height > 6.5 and Height <= 12.5 and Wb_trans <= 1.5 | 4 | 0.002616 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Height > 3.5 and Eccen > 0.3305 and Height <= 27.5 and Blackpix > 12.5 and Mean_tr <= 16.854999999999997 and P_black > 0.1585 | 1 | 0.887746 |
| Lenght <= 3.5 and Eccen <= 0.3305 | 4 | 0.060804 |
| Height <= 3.5 and Eccen > 5.8335 and P_black > 0.235 and Mean_tr <= 12.335 and Mean_tr > 1.255 | 2 | 0.131632 |
| Mean_tr <= 12.335 and Height <= 12.0 | 1 | 0.503274 |
| Height <= 6.5 | 2 | 0.388773 |
| P_black <= 0.3145 and Eccen <= 1.9064999999999999 | 5 | 0.263333 |
| Height <= 90.0 and P_black > 0.289 and Eccen > 1.3505 | 1 | 0.230880 |
| P_black <= 0.336 and P_and <= 0.4875 | 5 | 0.124008 |
| Blackpix <= 4353.5 | 1 | 0.328319 |
|  | 3 | 0.328947 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Height >= 28 and P_black >= 0.338 and Lenght >= 31 and Eccen <= 1.254 | 3 | 0.003342 |
| Height >= 72 and Blackpix >= 17721 | 3 | 0.000817 |
| Eccen <= 0.286 | 4 | 0.012654 |
| P_and <= 0.541 and Eccen <= 2.474 and P_black <= 0.194 and Height >= 22 | 5 | 0.006519 |
| P_and <= 0.555 and Eccen <= 3.529 and P_black <= 0.148 | 5 | 0.003683 |
| Height >= 31 and P_black <= 0.256 | 5 | 0.001790 |
| Area >= 19278 | 5 | 0.000484 |
| Mean_tr >= 9.06 and Height <= 2 | 2 | 0.031093 |
| Height <= 3 and Mean_tr >= 1.5 and Eccen >= 12.5 | 2 | 0.015532 |
| Height <= 2 and P_black >= 0.407 | 2 | 0.003045 |
| Mean_tr >= 30.27 and Eccen >= 6.5 | 2 | 0.003621 |
| Wb_trans <= 5 and Lenght >= 11 and Blackand <= 32 | 2 | 0.000524 |
| Mean_tr >= 6.53 and Eccen >= 23.167 | 2 | 0.000432 |
|  | 1 | 0.989036 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

height|wb_trans|class
---|---|---
(12.5-26.5]|(785-inf)|1
(6.5-12.5]|(785-inf)|1
(26.5-inf)|(785-inf)|3
(-inf-2.5]|(37.5-785]|2
(3.5-4.5]|(37.5-785]|1
(2.5-3.5]|(37.5-785]|1
(26.5-inf)|(37.5-785]|5
(4.5-6.5]|(37.5-785]|1
(12.5-26.5]|(37.5-785]|1
(6.5-12.5]|(37.5-785]|1
(3.5-4.5]|(7.5-37.5]|1
(26.5-inf)|(7.5-37.5]|5
(12.5-26.5]|(7.5-37.5]|1
(2.5-3.5]|(7.5-37.5]|2
(4.5-6.5]|(7.5-37.5]|1
(-inf-2.5]|(7.5-37.5]|2
(6.5-12.5]|(7.5-37.5]|1
(3.5-4.5]|(5.5-7.5]|1
(26.5-inf)|(5.5-7.5]|1
(12.5-26.5]|(5.5-7.5]|1
(2.5-3.5]|(5.5-7.5]|1
(-inf-2.5]|(5.5-7.5]|2
(6.5-12.5]|(5.5-7.5]|1
(4.5-6.5]|(5.5-7.5]|1
(12.5-26.5]|(1.5-5.5]|5
(2.5-3.5]|(1.5-5.5]|2
(3.5-4.5]|(1.5-5.5]|1
(-inf-2.5]|(1.5-5.5]|2
(6.5-12.5]|(1.5-5.5]|1
(4.5-6.5]|(1.5-5.5]|1
(12.5-26.5]|(-inf-1.5]|4
(26.5-inf)|(-inf-1.5]|4
(6.5-12.5]|(-inf-1.5]|4
(4.5-6.5]|(-inf-1.5]|1
(2.5-3.5]|(-inf-1.5]|1
(-inf-2.5]|(-inf-1.5]|2
(3.5-4.5]|(-inf-1.5]|1

## JRip

Decision list:

rules | predicted class
---|---
(Height >= 28) and (P_black >= 0.338) and (Lenght >= 31) and (Eccen <= 1.254)|3 (22.0/3.0)
(Height >= 72) and (Blackpix >= 17721)|3 (4.0/0.0)
(Eccen <= 0.286)|4 (84.0/12.0)
(P_and <= 0.541) and (Eccen <= 2.474) and (P_black <= 0.194) and (Height >= 22)|5 (31.0/0.0)
(P_and <= 0.555) and (Eccen <= 3.529) and (P_black <= 0.148)|5 (33.0/9.0)
(Height >= 31) and (P_black <= 0.256)|5 (16.0/4.0)
(Area >= 19278)|5 (6.0/2.0)
(Mean_tr >= 9.06) and (Height <= 2)|2 (149.0/3.0)
(Height <= 3) and (Mean_tr >= 1.5) and (Eccen >= 12.5)|2 (95.0/12.0)
(Height <= 2) and (P_black >= 0.407)|2 (38.0/13.0)
(Mean_tr >= 30.27) and (Eccen >= 6.5)|2 (19.0/1.0)
(Wb_trans <= 5) and (Lenght >= 11) and (Blackand <= 32)|2 (9.0/3.0)
(Mean_tr >= 6.53) and (Eccen >= 23.167)|2 (6.0/1.0)
|1 (4407.0/42.0)


## PART

Decision list:

rules | predicted class
---|---
Height > 3.5 AND Eccen > 0.3305 AND Height <= 27.5 AND Blackpix > 12.5 AND Mean_tr <= 16.854999999999997 AND P_black > 0.1585|1 (1998.0/2.0)
Lenght <= 3.5 AND Eccen <= 0.3305|4 (38.0/3.0)
Height <= 3.5 AND Eccen > 5.8335 AND P_black > 0.235 AND Mean_tr <= 12.335 AND Mean_tr > 1.255|2 (72.0/14.0)
Mean_tr <= 12.335 AND Height <= 12.0|1 (178.0/23.0)
Height <= 6.5|2 (80.0/2.0)
P_black <= 0.3145 AND Eccen <= 1.9064999999999999|5 (23.0/1.0)
Height <= 90.0 AND P_black > 0.289 AND Eccen > 1.3505|1 (20.0/1.0)
P_black <= 0.336 AND P_and <= 0.4875|5 (18.0/6.0)
Blackpix <= 4353.5|1 (25.0/7.0)
|3 (8.0/1.0)


## J48 Decision Tree

* Height <= 3.0
	* P_black <= 0.228
		* Mean_tr <= 1.29: 1 (32.0)
		* Mean_tr > 1.29: 1 (8.0/2.0)
	* P_black > 0.228
		* Lenght <= 7.0
			* Height <= 2.0: 1 (9.0/4.0)
			* Height > 2.0: 1 (19.0)
		* Lenght > 7.0
			* Mean_tr <= 4.08
				* Height <= 2.0
					* Mean_tr <= 1.27
						* P_black <= 0.402: 1 (10.0)
						* P_black > 0.402: 2 (8.0/3.0)
					* Mean_tr > 1.27
						* Eccen <= 12.5: 1 (11.0/4.0)
						* Eccen > 12.5
							* Wb_trans <= 7.0: 2 (29.0/5.0)
							* Wb_trans > 7.0: 2 (13.0)
				* Height > 2.0: 1 (8.0/1.0)
			* Mean_tr > 4.08
				* Height <= 2.0
					* Blackpix <= 37.0
						* Height <= 1.0: 2 (66.0/6.0)
						* Height > 1.0
							* P_black <= 0.572: 2 (8.0/1.0)
							* P_black > 0.572: 2 (8.0)
					* Blackpix > 37.0: 2 (109.0)
				* Height > 2.0
					* P_black <= 0.41: 2 (17.0)
					* P_black > 0.41: 2 (8.0/2.0)
* Height > 3.0
	* Eccen <= 0.25
		* Lenght <= 3.0
			* Lenght <= 1.0
				* Mean_tr <= 7.5: 4 (8.0/2.0)
				* Mean_tr > 7.5: 4 (48.0/2.0)
			* Lenght > 1.0: 4 (14.0/2.0)
		* Lenght > 3.0: 4 (10.0/3.0)
	* Eccen > 0.25
		* Height <= 27.0
			* Blackpix <= 11.0
				* Lenght <= 2.0: 1 (14.0/6.0)
				* Lenght > 2.0
					* P_black <= 0.241
						* Wb_trans <= 1.0: 1 (8.0/5.0)
						* Wb_trans > 1.0
							* Wb_trans <= 4.0: 5 (8.0)
							* Wb_trans > 4.0: 1 (9.0/4.0)
					* P_black > 0.241
						* Height <= 4.0: 1 (13.0/4.0)
						* Height > 4.0
							* Height <= 7.0
								* Height <= 6.0
									* Eccen <= 0.909
										* Wb_trans <= 1.0: 1 (8.0)
										* Wb_trans > 1.0: 1 (15.0/3.0)
									* Eccen > 0.909: 1 (16.0)
								* Height > 6.0: 1 (12.0)
							* Height > 7.0: 1 (8.0/2.0)
			* Blackpix > 11.0
				* Mean_tr <= 21.18
					* P_and <= 0.523
						* Wb_trans <= 34.0
							* Height <= 12.0
								* Mean_tr <= 5.1
									* Height <= 6.0: 1 (11.0/1.0)
									* Height > 6.0
										* P_black <= 0.145: 1 (10.0/3.0)
										* P_black > 0.145: 1 (22.0)
								* Mean_tr > 5.1
									* Eccen <= 3.636: 1 (8.0/2.0)
									* Eccen > 3.636: 2 (8.0/3.0)
							* Height > 12.0
								* P_black <= 0.139: 5 (10.0/1.0)
								* P_black > 0.139: 1 (8.0/3.0)
						* Wb_trans > 34.0: 1 (125.0)
					* P_and > 0.523
						* Eccen <= 0.619
							* Height <= 9.0
								* Area <= 30.0: 1 (9.0)
								* Area > 30.0: 1 (12.0/1.0)
							* Height > 9.0: 1 (9.0/3.0)
						* Eccen > 0.619
							* P_black <= 0.156
								* Mean_tr <= 2.34: 1 (81.0)
								* Mean_tr > 2.34: 1 (8.0/4.0)
							* P_black > 0.156: 1 (3898.0/3.0)
				* Mean_tr > 21.18
					* Eccen <= 1.254: 1 (18.0)
					* Eccen > 1.254
						* Height <= 11.0
							* Height <= 5.0: 2 (8.0)
							* Height > 5.0: 2 (9.0/1.0)
						* Height > 11.0: 2 (9.0/5.0)
		* Height > 27.0
			* P_black <= 0.331
				* Eccen <= 2.0: 5 (29.0)
				* Eccen > 2.0
					* P_black <= 0.208: 5 (14.0/3.0)
					* P_black > 0.208
						* Lenght <= 297.0: 1 (9.0/1.0)
						* Lenght > 297.0: 1 (8.0/4.0)
			* P_black > 0.331
				* Height <= 87.0
					* Eccen <= 1.333
						* Wb_trans <= 59.0: 3 (9.0/1.0)
						* Wb_trans > 59.0: 3 (8.0/3.0)
					* Eccen > 1.333: 1 (14.0/1.0)
				* Height > 87.0: 3 (11.0)


## SimpleCart Decision Tree

* Height < 3.5
	* Mean_tr < 1.355: 1(47.0/5.0)
	* Mean_tr >= 1.355
		* Eccen < 7.5
			* Eccen < 2.6665: 1(19.0/0.0)
			* Eccen >= 2.6665: 1(10.0/8.0)
		* Eccen >= 7.5
			* P_black < 0.2405: 1(7.0/3.0)
			* P_black >= 0.2405
				* Mean_tr < 4.09
					* Eccen < 12.5: 1(6.0/4.0)
					* Eccen >= 12.5: 2(36.0/6.0)
				* Mean_tr >= 4.09: 2(204.0/8.0)
* Height >= 3.5
	* Eccen < 0.268: 4(71.0/9.0)
	* Eccen >= 0.268
		* Height < 27.5
			* Mean_tr < 30.134999999999998
				* Blackpix < 11.5
					* P_black < 0.241: 5(14.0/11.0)
					* P_black >= 0.241
						* P_black < 0.6835
							* Eccen < 1.225: 1(60.0/6.0)
							* Eccen >= 1.225: 1(7.0/4.0)
						* P_black >= 0.6835: 4(5.0/4.0)
				* Blackpix >= 11.5: 1(4191.0/40.0)
			* Mean_tr >= 30.134999999999998
				* Eccen < 6.487: 1(13.0/1.0)
				* Eccen >= 6.487: 2(17.0/1.0)
		* Height >= 27.5
			* P_black < 0.257
				* Eccen < 3.333: 5(36.0/0.0)
				* Eccen >= 3.333: 1(5.0/6.0)
			* P_black >= 0.257
				* Eccen < 1.2934999999999999: 3(19.0/3.0)
				* Eccen >= 1.2934999999999999: 1(23.0/10.0)


