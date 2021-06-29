# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Height >= 3.5 and Eccen >= 0.236 and Height < 27.5 | 1 | 0.894476 |
| Height < 3.5 and Mean_tr >= 1.355 and Eccen >= 7.5 | 2 | 0.046618 |
| Height > 3 and Eccen <= 0.222 | 4 | 0.013413 |
| Height < 3.5 and Mean_tr < 1.355 | 1 | 0.075279 |
| Height >= 3.5 and Eccen >= 0.236 and Height >= 27.5 and P_black < 0.3015 | 5 | 0.008047 |
| Height < 3.5 and Mean_tr >= 1.355 and Eccen < 7.5 | 1 | 0.039623 |
| Height > 3 and Eccen > 0.222 and Height <= 27 and Mean_tr > 21.29 and Eccen > 1.25 | 2 | 0.003656 |
| Height > 3 and Eccen > 0.222 and Height <= 27 and Mean_tr <= 21.29 and P_black <= 0.159 and Eccen <= 3.6 and Wb_trans > 4 and Height > 11 | 5 | 0.002130 |
| Height >= 3.5 and Eccen >= 0.236 and Height >= 27.5 and P_black >= 0.3015 | 3 | 0.002775 |
| Height > 3 and Eccen > 0.222 and Height > 27 and P_black > 0.331 and Height <= 87 and Eccen > 1.375 | 1 | 0.019849 |
| Height > 3 and Eccen > 0.222 and Height <= 27 and Mean_tr <= 21.29 and P_black <= 0.159 and Eccen <= 3.6 and Wb_trans <= 4 | 5 | 0.001399 |
| Height <= 3 and P_black <= 0.228 | 1 | 0.060587 |
| Height <= 3 and P_black > 0.228 and Lenght > 5 | 2 | 0.045659 |
| Height > 3 and Eccen > 0.222 and Height > 27 and P_black <= 0.331 | 5 | 0.007771 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Height > 3.5 and Eccen > 0.236 and Height <= 27.5 and Mean_tr <= 21.295 and Blackpix > 14.5 and P_and > 0.5195 and P_black > 0.1565 | 1 | 0.885912 |
| Lenght <= 2.5 and Eccen <= 0.236 | 4 | 0.056119 |
| Height <= 3.5 and Mean_tr <= 1.355 and Blackpix <= 44.5 | 1 | 0.091903 |
| Height <= 3.5 and Lenght > 7.5 and Mean_tr > 9.975 | 2 | 0.196319 |
| Height <= 2.5 and Blackpix <= 16.5 and Height <= 1.5 | 2 | 0.063180 |
| Height <= 11.5 and Height <= 2.5 and Blackpix > 16 | 2 | 0.054555 |
| Height <= 11.5 and Mean_tr <= 2.635 and Blackand > 56.5 | 1 | 0.525957 |
| Height <= 26 and Mean_tr > 30.135 and Lenght > 20 | 2 | 0.036143 |
| P_black > 0.23 and Height <= 20.5 and Eccen <= 2.2085 and Lenght > 2.5 and Lenght <= 6.5 and Height <= 8.5 and Lenght <= 4.5 and P_and > 0.628 | 1 | 0.267857 |
| Height <= 24.5 and P_black > 0.16 and Area > 14.5 and Eccen <= 2.2085 and Wb_trans <= 1.5 and P_black > 0.268 | 1 | 0.132471 |
| P_black <= 0.23 and Eccen <= 3.693 and Height > 11.5 and Eccen > 0.1825 | 5 | 0.157217 |
| Eccen > 0.528 and Height <= 27.5 and Height <= 3.5 and P_and > 0.5335 and Area > 13 | 1 | 0.144300 |
| Eccen <= 0.528 and Eccen <= 0.1785 | 4 | 0.020425 |
| Height <= 27.5 and Height > 3.5 and Blackand > 10.5 and Mean_tr <= 3.965 and Wb_trans > 7.5 | 1 | 0.313119 |
| Height <= 27.5 and Height > 3.5 and Lenght <= 2.5 and P_black <= 0.866 | 1 | 0.064904 |
| Height <= 27.5 and Area <= 13.5 and Height <= 3 | 2 | 0.002189 |
| Height <= 27.5 and Area > 16.5 and Height > 3.5 and Eccen <= 4.625 and Wb_trans > 1.5 and P_black > 0.1795 and Lenght > 6.5 | 1 | 0.287469 |
| P_black <= 0.3245 and Height <= 82.5 and Blackpix > 808.5 and Height <= 42.5 | 1 | 0.103523 |
| Height <= 26 and Lenght <= 6.5 and Lenght > 2.5 and Height <= 7.5 and Blackpix > 7.5 | 1 | 0.172806 |
| P_black <= 0.3245 and Wb_trans > 92 | 5 | 0.072398 |
| Height > 22.5 and Height <= 90 and Eccen > 1.3505 | 1 | 0.155844 |
| Height > 24.5 | 3 | 0.159847 |
| Lenght > 2.5 and Eccen > 4.3035 and Height <= 6.5 | 2 | 0.045455 |
| Lenght > 2.5 and Mean_tr <= 8.07 and Wb_trans > 3.5 | 1 | 0.232727 |
| Area > 12.5 and Wb_trans <= 6.5 and Wb_trans > 1.5 | 5 | 0.294694 |
| Lenght > 3 and Wb_trans <= 4 and Height <= 6.5 | 2 | 0.044444 |
| Wb_trans > 4 | 2 | 0.087500 |
| Height <= 6 | 4 | 0.043956 |
| Area <= 35.5 | 1 | 0.332418 |
|  | 5 | 0.565217 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Height >= 28 and P_black >= 0.339 and Lenght >= 31 | 3 | 0.003110 |
| Eccen <= 0.222 | 4 | 0.013482 |
| Height >= 28 | 5 | 0.006314 |
| P_black <= 0.159 and Eccen <= 3.529 | 5 | 0.003385 |
| Height <= 3 and Blackpix >= 23 and Mean_tr >= 2.31 | 2 | 0.034141 |
| Height <= 2 and P_black >= 0.43 | 2 | 0.014607 |
| Mean_tr >= 13.9 and Eccen >= 19 | 2 | 0.003678 |
| Height <= 2 and Mean_tr >= 1.38 | 2 | 0.001669 |
|  | 1 | 0.989700 |


# Text representation of classifiers as-is

## JRip

Decision list:

rules | predicted class
---|---
(Height >= 28) and (P_black >= 0.339) and (Lenght >= 31)|3 (41.0/16.0)
(Eccen <= 0.222)|4 (81.0/8.0)
(Height >= 28)|5 (69.0/18.0)
(P_black <= 0.159) and (Eccen <= 3.529)|5 (47.0/19.0)
(Height <= 3) and (Blackpix >= 23) and (Mean_tr >= 2.31)|2 (167.0/5.0)
(Height <= 2) and (P_black >= 0.43)|2 (88.0/11.0)
(Mean_tr >= 13.9) and (Eccen >= 19)|2 (20.0/1.0)
(Height <= 2) and (Mean_tr >= 1.38)|2 (26.0/9.0)
|1 (4379.0/39.0)


## PART

Decision list:

rules | predicted class
---|---
Height > 3.5 AND Eccen > 0.236 AND Height <= 27.5 AND Mean_tr <= 21.295 AND Blackpix > 14.5 AND P_and > 0.5195 AND P_black > 0.1565|1 (3877.0/5.0)
Lenght <= 2.5 AND Eccen <= 0.236|4 (69.0/6.0)
Height <= 3.5 AND Mean_tr <= 1.355 AND Blackpix <= 44.5|1 (46.0/1.0)
Height <= 3.5 AND Lenght > 7.5 AND Mean_tr > 9.975|2 (163.0/3.0)
Height <= 2.5 AND Blackpix <= 16.5 AND Height <= 1.5|2 (64.0/12.0)
Height <= 11.5 AND Height <= 2.5 AND Blackpix > 16|2 (39.0)
Height <= 11.5 AND Mean_tr <= 2.635 AND Blackand > 56.5|1 (205.0)
Height <= 26 AND Mean_tr > 30.135 AND Lenght > 20|2 (21.0/2.0)
P_black > 0.23 AND Height <= 20.5 AND Eccen <= 2.2085 AND Lenght > 2.5 AND Lenght <= 6.5 AND Height <= 8.5 AND Lenght <= 4.5 AND P_and > 0.628|1 (60.0)
Height <= 24.5 AND P_black > 0.16 AND Area > 14.5 AND Eccen <= 2.2085 AND Wb_trans <= 1.5 AND P_black > 0.268|1 (26.0)
P_black <= 0.23 AND Eccen <= 3.693 AND Height > 11.5 AND Eccen > 0.1825|5 (61.0/5.0)
Eccen > 0.528 AND Height <= 27.5 AND Height <= 3.5 AND P_and > 0.5335 AND Area > 13|1 (14.0/2.0)
Eccen <= 0.528 AND Eccen <= 0.1785|4 (11.0/1.0)
Height <= 27.5 AND Height > 3.5 AND Blackand > 10.5 AND Mean_tr <= 3.965 AND Wb_trans > 7.5|1 (49.0/2.0)
Height <= 27.5 AND Height > 3.5 AND Lenght <= 2.5 AND P_black <= 0.866|1 (11.0/2.0)
Height <= 27.5 AND Area <= 13.5 AND Height <= 3|2 (2.0)
Height <= 27.5 AND Area > 16.5 AND Height > 3.5 AND Eccen <= 4.625 AND Wb_trans > 1.5 AND P_black > 0.1795 AND Lenght > 6.5|1 (44.0/2.0)
P_black <= 0.3245 AND Height <= 82.5 AND Blackpix > 808.5 AND Height <= 42.5|1 (12.0)
Height <= 26 AND Lenght <= 6.5 AND Lenght > 2.5 AND Height <= 7.5 AND Blackpix > 7.5|1 (22.0/1.0)
P_black <= 0.3245 AND Wb_trans > 92|5 (14.0/2.0)
Height > 22.5 AND Height <= 90 AND Eccen > 1.3505|1 (17.0/2.0)
Height > 24.5|3 (28.0/4.0)
Lenght > 2.5 AND Eccen > 4.3035 AND Height <= 6.5|2 (6.0)
Lenght > 2.5 AND Mean_tr <= 8.07 AND Wb_trans > 3.5|1 (30.0/12.0)
Area > 12.5 AND Wb_trans <= 6.5 AND Wb_trans > 1.5|5 (14.0/3.0)
Lenght > 3 AND Wb_trans <= 4 AND Height <= 6.5|2 (4.0/1.0)
Wb_trans > 4|2 (3.0)
Height <= 6|4 (2.0)
Area <= 35.5|1 (2.0)
|5 (2.0)


## J48 Decision Tree

* Height <= 3
	* P_black <= 0.228: 1 (30.0/1.0)
	* P_black > 0.228
		* Lenght <= 5: 1 (17.0)
		* Lenght > 5: 2 (258.0/37.0)
* Height > 3
	* Eccen <= 0.222: 4 (71.0/7.0)
	* Eccen > 0.222
		* Height <= 27
			* Mean_tr <= 21.29
				* P_black <= 0.159
					* Eccen <= 3.6
						* Wb_trans <= 4: 5 (10.0/2.0)
						* Wb_trans > 4
							* Height <= 11: 1 (15.0/5.0)
							* Height > 11: 5 (11.0/2.0)
					* Eccen > 3.6: 1 (144.0/3.0)
				* P_black > 0.159: 1 (3529.0/25.0)
			* Mean_tr > 21.29
				* Eccen <= 1.25: 1 (12.0)
				* Eccen > 1.25: 2 (24.0/5.0)
		* Height > 27
			* P_black <= 0.331: 5 (60.0/17.0)
			* P_black > 0.331
				* Height <= 87
					* Eccen <= 1.375: 3 (13.0/4.0)
					* Eccen > 1.375: 1 (11.0/1.0)
				* Height > 87: 3 (11.0)


## SimpleCart Decision Tree

* Height < 3.5
	* Mean_tr < 1.355: 1(45.0/5.0)
	* Mean_tr >= 1.355
		* Eccen < 7.5: 1(26.0/7.0)
		* Eccen >= 7.5: 2(247.0/23.0)
* Height >= 3.5
	* Eccen < 0.236: 4(73.0/8.0)
	* Eccen >= 0.236
		* Height < 27.5: 1(4290.0/84.0)
		* Height >= 27.5
			* P_black < 0.3015: 5(50.0/14.0)
			* P_black >= 0.3015: 3(25.0/21.0)


