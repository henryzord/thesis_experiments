# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Height >= 3.5 and Eccen >= 0.268 and Height < 27.5 and Mean_tr < 30.134999999999998 | 1 | 0.894032 |
| Height < 3.5 and Mean_tr >= 1.355 and Eccen >= 7.5 and P_black >= 0.2405 | 2 | 0.046517 |
| Height > 3 and Eccen <= 0.25 | 4 | 0.012854 |
| Height < 3.5 and Mean_tr < 1.355 and Blackpix < 44.5 | 1 | 0.084442 |
| Height >= 3.5 and Eccen >= 0.268 and Height >= 27.5 and P_black < 0.3015 | 5 | 0.007451 |
| Height < 3.5 and Mean_tr >= 1.355 and Eccen < 7.5 | 1 | 0.043711 |
| Height >= 3.5 and Eccen >= 0.268 and Height >= 27.5 and P_black >= 0.3015 and Eccen >= 1.2934999999999999 and Wb_trans < 944.0 | 1 | 0.031456 |
| Height > 3 and Eccen > 0.25 and Height <= 27 and Mean_tr > 21.18 and Eccen > 1.254 | 2 | 0.003317 |
| Height >= 3.5 and Eccen >= 0.268 and Height >= 27.5 and P_black >= 0.3015 and Eccen < 1.2934999999999999 | 3 | 0.003342 |
| Height >= 3.5 and Eccen >= 0.268 and Height < 27.5 and Mean_tr >= 30.134999999999998 and Eccen < 6.487 | 1 | 0.023623 |
| Height <= 3 and Lenght > 7 and Mean_tr <= 4.08 and Mean_tr > 1.27 and Eccen <= 12.5 | 1 | 0.023903 |
| Height > 3 and Eccen > 0.25 and Height > 27 and P_black <= 0.331 and Eccen > 2 and P_black > 0.208 and Height <= 45 | 1 | 0.017895 |
| Height <= 3 and Lenght > 7 and Mean_tr <= 4.08 and Mean_tr <= 1.27 and P_black > 0.407 | 2 | 0.000772 |
| Height > 3 and Eccen > 0.25 and Height > 27 and P_black > 0.331 and Height > 87 | 3 | 0.002243 |
| Height < 3.5 and Mean_tr >= 1.355 and Eccen >= 7.5 and P_black < 0.2405 | 1 | 0.009742 |
| Height <= 3 and Lenght > 7 and Mean_tr > 4.08 | 2 | 0.041338 |
| Height > 3 and Eccen > 0.25 and Height > 27 and P_black <= 0.331 and Eccen > 2 and P_black > 0.208 and Height > 45 | 5 | 0.000741 |
| Height <= 3 and Lenght > 7 and Mean_tr <= 4.08 and Mean_tr > 1.27 and Eccen > 12.5 | 2 | 0.006603 |
| Height > 3 and Eccen > 0.25 and Height > 27 and P_black > 0.331 and Height <= 87 and Eccen <= 1.333 | 3 | 0.002028 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Height > 3 and Eccen > 0.25 and Height <= 27 and Blackpix > 11 and Mean_tr <= 21.18 and P_and > 0.523 | 1 | 0.888993 |
| Lenght <= 2 and Eccen <= 0.25 | 4 | 0.060376 |
| Height <= 3 and P_black > 0.228 and Lenght > 7 and Mean_tr > 4.08 | 2 | 0.262054 |
| Height <= 26 and Height <= 2 and Mean_tr <= 1.29 | 1 | 0.148352 |
| Height <= 26 and Height <= 2 and Eccen > 12.5 | 2 | 0.063318 |
| Height <= 26 and P_black <= 0.537 and Wb_trans > 34 | 1 | 0.398114 |
| Height <= 26 and Blackpix > 178 | 2 | 0.037417 |
| Height <= 12 and Lenght > 2 and P_and > 0.319 and Height > 2 and P_black <= 0.467 and Wb_trans <= 7 and P_black > 0.233 | 1 | 0.245270 |
| P_black <= 0.326 and Height > 11 and Eccen > 0.49 and P_black <= 0.202 | 5 | 0.151240 |
| Eccen > 0.541 and Blackpix <= 309 and P_and > 0.319 and Height > 2 and P_black > 0.256 | 1 | 0.283014 |
| P_black <= 0.328 and Eccen > 0.7 and P_and > 0.319 and Eccen <= 7.2 and Blackpix > 9 and Mean_tr <= 3.04 | 1 | 0.166137 |
| Eccen <= 0.7 and P_black > 0.321 and Height <= 10 | 1 | 0.045833 |
| Eccen > 0.167 and P_black <= 0.331 and Eccen <= 7.125 and Mean_tr <= 6.73 | 5 | 0.145349 |
| Eccen > 0.25 and Height <= 9 and Mean_tr <= 3.83 | 1 | 0.174545 |
| Eccen <= 0.25 | 4 | 0.065663 |
| Height <= 9 and Lenght <= 8 | 1 | 0.029132 |
| Height > 12 and P_black > 0.328 and Height <= 87 and Wb_trans <= 235 | 3 | 0.077624 |
| Height <= 87 and Height > 9 | 1 | 0.359574 |
| Height <= 49 | 2 | 0.286172 |
|  | 3 | 0.244444 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Eccen <= 0.125 | 4 | 0.011288 |
| Lenght <= 2 | 4 | 0.001550 |
| P_and <= 0.541 and Eccen <= 3.429 and P_black <= 0.198 and Mean_tr >= 2.83 | 5 | 0.007368 |
| Height >= 30 and P_black <= 0.295 | 5 | 0.003090 |
| P_black <= 0.159 and Eccen <= 3.529 | 5 | 0.001647 |
| Height <= 3 and Mean_tr >= 3.71 and Blackpix >= 26 | 2 | 0.033288 |
| Height <= 2 and Mean_tr >= 1.38 | 2 | 0.016569 |
| Mean_tr >= 21.3 and Eccen >= 6.5 | 2 | 0.003352 |
|  | 1 | 0.983096 |


# Text representation of classifiers as-is

## JRip

Decision list:

rules | predicted class
---|---
(Eccen <= 0.125)|4 (63.0/4.0)
(Lenght <= 2)|4 (26.0/11.0)
(P_and <= 0.541) and (Eccen <= 3.429) and (P_black <= 0.198) and (Mean_tr >= 2.83)|5 (41.0/3.0)
(Height >= 30) and (P_black <= 0.295)|5 (30.0/9.0)
(P_black <= 0.159) and (Eccen <= 3.529)|5 (33.0/16.0)
(Height <= 3) and (Mean_tr >= 3.71) and (Blackpix >= 26)|2 (160.0/3.0)
(Height <= 2) and (Mean_tr >= 1.38)|2 (124.0/27.0)
(Mean_tr >= 21.3) and (Eccen >= 6.5)|2 (21.0/2.0)
|1 (4421.0/67.0)


## PART

Decision list:

rules | predicted class
---|---
Height > 3 AND Eccen > 0.25 AND Height <= 27 AND Blackpix > 11 AND Mean_tr <= 21.18 AND P_and > 0.523|1 (4016.0/10.0)
Lenght <= 2 AND Eccen <= 0.25|4 (65.0/6.0)
Height <= 3 AND P_black > 0.228 AND Lenght > 7 AND Mean_tr > 4.08|2 (216.0/9.0)
Height <= 26 AND Height <= 2 AND Mean_tr <= 1.29|1 (50.0/5.0)
Height <= 26 AND Height <= 2 AND Eccen > 12.5|2 (46.0/7.0)
Height <= 26 AND P_black <= 0.537 AND Wb_trans > 34|1 (126.0)
Height <= 26 AND Blackpix > 178|2 (21.0/3.0)
Height <= 12 AND Lenght > 2 AND P_and > 0.319 AND Height > 2 AND P_black <= 0.467 AND Wb_trans <= 7 AND P_black > 0.233|1 (79.0/13.0)
P_black <= 0.326 AND Height > 11 AND Eccen > 0.49 AND P_black <= 0.202|5 (53.0/5.0)
Eccen > 0.541 AND Blackpix <= 309 AND P_and > 0.319 AND Height > 2 AND P_black > 0.256|1 (57.0/1.0)
P_black <= 0.328 AND Eccen > 0.7 AND P_and > 0.319 AND Eccen <= 7.2 AND Blackpix > 9 AND Mean_tr <= 3.04|1 (31.0/3.0)
Eccen <= 0.7 AND P_black > 0.321 AND Height <= 10|1 (15.0/6.0)
Eccen > 0.167 AND P_black <= 0.331 AND Eccen <= 7.125 AND Mean_tr <= 6.73|5 (34.0/8.0)
Eccen > 0.25 AND Height <= 9 AND Mean_tr <= 3.83|1 (18.0/2.0)
Eccen <= 0.25|4 (13.0/1.0)
Height <= 9 AND Lenght <= 8|1 (11.0/5.0)
Height > 12 AND P_black > 0.328 AND Height <= 87 AND Wb_trans <= 235|3 (22.0/8.0)
Height <= 87 AND Height > 9|1 (24.0/5.0)
Height <= 49|2 (11.0/3.0)
|3 (11.0)


## J48 Decision Tree

* Height <= 3
	* Lenght <= 7: 1 (28.0/4.0)
	* Lenght > 7
		* Mean_tr <= 4.08
			* Mean_tr <= 1.27
				* P_black <= 0.407: 1 (43.0)
				* P_black > 0.407: 2 (7.0/2.0)
			* Mean_tr > 1.27
				* Eccen <= 12.5: 1 (21.0/5.0)
				* Eccen > 12.5: 2 (47.0/9.0)
		* Mean_tr > 4.08: 2 (217.0/9.0)
* Height > 3
	* Eccen <= 0.25: 4 (80.0/9.0)
	* Eccen > 0.25
		* Height <= 27
			* Mean_tr <= 21.18: 1 (4329.0/67.0)
			* Mean_tr > 21.18
				* Eccen <= 1.254: 1 (18.0)
				* Eccen > 1.254: 2 (26.0/6.0)
		* Height > 27
			* P_black <= 0.331
				* Eccen <= 2: 5 (29.0)
				* Eccen > 2
					* P_black <= 0.208: 5 (14.0/3.0)
					* P_black > 0.208
						* Height <= 45: 1 (11.0/1.0)
						* Height > 45: 5 (7.0/2.0)
			* P_black > 0.331
				* Height <= 87
					* Eccen <= 1.333: 3 (17.0/4.0)
					* Eccen > 1.333: 1 (14.0/1.0)
				* Height > 87: 3 (11.0)


## SimpleCart Decision Tree

* Height < 3.5
	* Mean_tr < 1.355
		* Blackpix < 44.5: 1(47.0/1.0)
		* Blackpix >= 44.5: 2(4.0/0.0)
	* Mean_tr >= 1.355
		* Eccen < 7.5: 1(29.0/8.0)
		* Eccen >= 7.5
			* P_black < 0.2405: 1(7.0/3.0)
			* P_black >= 0.2405: 2(244.0/20.0)
* Height >= 3.5
	* Eccen < 0.268: 4(71.0/9.0)
	* Eccen >= 0.268
		* Height < 27.5
			* Mean_tr < 30.134999999999998: 1(4270.0/71.0)
			* Mean_tr >= 30.134999999999998
				* Eccen < 6.487: 1(13.0/1.0)
				* Eccen >= 6.487: 2(17.0/1.0)
		* Height >= 27.5
			* P_black < 0.3015: 5(45.0/11.0)
			* P_black >= 0.3015
				* Eccen < 1.2934999999999999: 3(19.0/3.0)
				* Eccen >= 1.2934999999999999
					* Wb_trans < 944.0: 1(18.0/2.0)
					* Wb_trans >= 944.0: 3(4.0/1.0)


