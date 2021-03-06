# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 1 | 0.898557 |
| Height < 3.5 and Mean_tr >= 1.355 and Eccen >= 7.5 and Blackpix >= 7.5 | 2 | 0.047023 |
| Height >= 3.5 and Eccen < 0.236 | 4 | 0.013547 |
| Height > 3 and Eccen > 0.222 and Height > 27 and P_black <= 0.301 | 5 | 0.008774 |
| Height > 3 and Eccen > 0.222 and Height <= 27 and Mean_tr > 21.29 and Eccen > 1.254 | 2 | 0.003521 |
| Height >= 3.5 and Eccen >= 0.236 and Height < 28.5 and Mean_tr < 30.134999999999998 and Blackpix < 11.5 and P_black < 0.241 | 5 | 0.001794 |
| Height >= 3.5 and Eccen >= 0.236 and Height >= 28.5 and P_black >= 0.3015 and Height >= 90.0 | 3 | 0.002852 |
| Height > 3 and Eccen > 0.222 and Height > 27 and P_black > 0.301 and Height <= 87 and Eccen <= 1.8 | 3 | 0.001372 |
| Height <= 2.5 and Blackpix <= 17.5 and Wb_trans <= 1.5 | 2 | 0.006685 |
| Height > 3 and Eccen > 0.222 and Height <= 27 and Mean_tr <= 21.29 and Blackpix <= 14 and P_black <= 0.159 and P_and <= 0.548 | 5 | 0.002130 |
| Height <= 2.5 and Blackpix <= 17.5 and Wb_trans > 1.5 and Wb_trans <= 5.5 | 2 | 0.004990 |
| Height > 3.5 and Height <= 4.5 and Blackpix > 156.5 and Blackpix <= 4115.5 and Wb_trans > 7.5 and Wb_trans <= 30.5 | 2 | 0.000432 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Height > 3 and Eccen > 0.222 and Height <= 27 and Mean_tr <= 15.9 and Blackpix > 14 | 1 | 0.890819 |
| Eccen > 6.8 and Mean_tr > 1.29 and Wb_trans <= 269 | 2 | 0.313997 |
| Eccen > 0.222 and Height <= 26 and Lenght > 2 and P_black > 0.159 | 1 | 0.513136 |
| Eccen > 0.222 and P_black <= 0.301 and Height > 5 | 5 | 0.269449 |
| Eccen <= 0.222 | 4 | 0.355409 |
| Height <= 87 and P_black <= 0.693 and Eccen > 1.8 | 1 | 0.266010 |
|  | 3 | 0.271739 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Height >= 28 and Blackpix >= 10947 | 3 | 0.002258 |
| Height >= 28 and P_black >= 0.338 and Eccen >= 0.979 and Eccen <= 1.333 | 3 | 0.001958 |
| Eccen <= 0.182 | 4 | 0.013765 |
| Lenght <= 2 | 4 | 0.000357 |
| Height >= 29 and P_black <= 0.224 | 5 | 0.008426 |
| Height >= 28 and P_black <= 0.256 | 5 | 0.000273 |
| P_black <= 0.159 and Eccen <= 3.429 | 5 | 0.003706 |
| Height <= 3 and Mean_tr >= 10 and Area >= 28 | 2 | 0.029457 |
| Height <= 2 and P_black >= 0.456 | 2 | 0.018593 |
| Height <= 4 and Mean_tr >= 1.6 and Eccen >= 27 and Wb_trans <= 13 | 2 | 0.002655 |
| Mean_tr >= 21.3 and Eccen >= 6.5 | 2 | 0.002945 |
| Height <= 3 and P_black >= 0.239 and P_black <= 0.364 and Mean_tr >= 1.38 | 2 | 0.001515 |
|  | 1 | 0.989257 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

height|blackpix|wb_trans|class
---|---|---|---
(90-inf)|(10800.5-inf)|(836.5-inf)|3
(26.5-90]|(4115.5-10800.5]|(836.5-inf)|5
(90-inf)|(4115.5-10800.5]|(836.5-inf)|3
(26.5-90]|(156.5-4115.5]|(836.5-inf)|1
(90-inf)|(10800.5-inf)|(30.5-836.5]|3
(12.5-26.5]|(156.5-4115.5]|(836.5-inf)|1
(6.5-12.5]|(4115.5-10800.5]|(30.5-836.5]|1
(90-inf)|(4115.5-10800.5]|(30.5-836.5]|5
(26.5-90]|(4115.5-10800.5]|(30.5-836.5]|1
(12.5-26.5]|(4115.5-10800.5]|(30.5-836.5]|1
(2.5-3.5]|(156.5-4115.5]|(30.5-836.5]|2
(90-inf)|(156.5-4115.5]|(30.5-836.5]|5
(-inf-2.5]|(156.5-4115.5]|(30.5-836.5]|2
(3.5-4.5]|(156.5-4115.5]|(30.5-836.5]|1
(26.5-90]|(156.5-4115.5]|(30.5-836.5]|5
(4.5-6.5]|(156.5-4115.5]|(30.5-836.5]|1
(12.5-26.5]|(156.5-4115.5]|(30.5-836.5]|1
(6.5-12.5]|(156.5-4115.5]|(30.5-836.5]|1
(90-inf)|(17.5-156.5]|(30.5-836.5]|1
(26.5-90]|(17.5-156.5]|(30.5-836.5]|4
(-inf-2.5]|(17.5-156.5]|(30.5-836.5]|1
(12.5-26.5]|(17.5-156.5]|(30.5-836.5]|1
(4.5-6.5]|(17.5-156.5]|(30.5-836.5]|1
(3.5-4.5]|(17.5-156.5]|(30.5-836.5]|1
(6.5-12.5]|(17.5-156.5]|(30.5-836.5]|1
(4.5-6.5]|(156.5-4115.5]|(7.5-30.5]|1
(3.5-4.5]|(156.5-4115.5]|(7.5-30.5]|2
(90-inf)|(156.5-4115.5]|(7.5-30.5]|1
(26.5-90]|(156.5-4115.5]|(7.5-30.5]|3
(2.5-3.5]|(156.5-4115.5]|(7.5-30.5]|2
(-inf-2.5]|(156.5-4115.5]|(7.5-30.5]|2
(6.5-12.5]|(156.5-4115.5]|(7.5-30.5]|1
(12.5-26.5]|(156.5-4115.5]|(7.5-30.5]|1
(26.5-90]|(17.5-156.5]|(7.5-30.5]|4
(2.5-3.5]|(17.5-156.5]|(7.5-30.5]|2
(3.5-4.5]|(17.5-156.5]|(7.5-30.5]|1
(12.5-26.5]|(17.5-156.5]|(7.5-30.5]|1
(-inf-2.5]|(17.5-156.5]|(7.5-30.5]|2
(4.5-6.5]|(17.5-156.5]|(7.5-30.5]|1
(6.5-12.5]|(17.5-156.5]|(7.5-30.5]|1
(12.5-26.5]|(-inf-17.5]|(7.5-30.5]|1
(6.5-12.5]|(156.5-4115.5]|(5.5-7.5]|1
(4.5-6.5]|(156.5-4115.5]|(5.5-7.5]|1
(3.5-4.5]|(156.5-4115.5]|(5.5-7.5]|2
(2.5-3.5]|(-inf-17.5]|(7.5-30.5]|1
(-inf-2.5]|(156.5-4115.5]|(5.5-7.5]|2
(12.5-26.5]|(156.5-4115.5]|(5.5-7.5]|1
(3.5-4.5]|(-inf-17.5]|(7.5-30.5]|1
(6.5-12.5]|(-inf-17.5]|(7.5-30.5]|1
(-inf-2.5]|(-inf-17.5]|(7.5-30.5]|1
(4.5-6.5]|(-inf-17.5]|(7.5-30.5]|1
(4.5-6.5]|(17.5-156.5]|(5.5-7.5]|1
(12.5-26.5]|(17.5-156.5]|(5.5-7.5]|1
(-inf-2.5]|(17.5-156.5]|(5.5-7.5]|2
(2.5-3.5]|(17.5-156.5]|(5.5-7.5]|1
(3.5-4.5]|(17.5-156.5]|(5.5-7.5]|1
(6.5-12.5]|(17.5-156.5]|(5.5-7.5]|1
(4.5-6.5]|(156.5-4115.5]|(1.5-5.5]|2
(6.5-12.5]|(156.5-4115.5]|(1.5-5.5]|1
(-inf-2.5]|(156.5-4115.5]|(1.5-5.5]|2
(2.5-3.5]|(-inf-17.5]|(5.5-7.5]|1
(3.5-4.5]|(-inf-17.5]|(5.5-7.5]|1
(-inf-2.5]|(-inf-17.5]|(5.5-7.5]|1
(2.5-3.5]|(156.5-4115.5]|(1.5-5.5]|1
(6.5-12.5]|(-inf-17.5]|(5.5-7.5]|1
(4.5-6.5]|(-inf-17.5]|(5.5-7.5]|1
(6.5-12.5]|(4115.5-10800.5]|(-inf-1.5]|1
(2.5-3.5]|(17.5-156.5]|(1.5-5.5]|2
(12.5-26.5]|(17.5-156.5]|(1.5-5.5]|1
(4.5-6.5]|(17.5-156.5]|(1.5-5.5]|1
(3.5-4.5]|(17.5-156.5]|(1.5-5.5]|1
(6.5-12.5]|(17.5-156.5]|(1.5-5.5]|1
(-inf-2.5]|(17.5-156.5]|(1.5-5.5]|2
(12.5-26.5]|(-inf-17.5]|(1.5-5.5]|1
(2.5-3.5]|(-inf-17.5]|(1.5-5.5]|1
(-inf-2.5]|(156.5-4115.5]|(-inf-1.5]|2
(3.5-4.5]|(-inf-17.5]|(1.5-5.5]|1
(12.5-26.5]|(156.5-4115.5]|(-inf-1.5]|1
(4.5-6.5]|(-inf-17.5]|(1.5-5.5]|1
(6.5-12.5]|(-inf-17.5]|(1.5-5.5]|1
(-inf-2.5]|(-inf-17.5]|(1.5-5.5]|2
(2.5-3.5]|(17.5-156.5]|(-inf-1.5]|1
(3.5-4.5]|(17.5-156.5]|(-inf-1.5]|1
(90-inf)|(17.5-156.5]|(-inf-1.5]|4
(12.5-26.5]|(17.5-156.5]|(-inf-1.5]|4
(26.5-90]|(17.5-156.5]|(-inf-1.5]|4
(-inf-2.5]|(17.5-156.5]|(-inf-1.5]|2
(4.5-6.5]|(17.5-156.5]|(-inf-1.5]|2
(6.5-12.5]|(17.5-156.5]|(-inf-1.5]|1
(3.5-4.5]|(-inf-17.5]|(-inf-1.5]|1
(12.5-26.5]|(-inf-17.5]|(-inf-1.5]|4
(-inf-2.5]|(-inf-17.5]|(-inf-1.5]|2
(6.5-12.5]|(-inf-17.5]|(-inf-1.5]|4
(4.5-6.5]|(-inf-17.5]|(-inf-1.5]|1
(2.5-3.5]|(-inf-17.5]|(-inf-1.5]|1

## JRip

Decision list:

rules | predicted class
---|---
(Height >= 28) and (Blackpix >= 10947)|3 (13.0/1.0)
(Height >= 28) and (P_black >= 0.338) and (Eccen >= 0.979) and (Eccen <= 1.333)|3 (15.0/3.0)
(Eccen <= 0.182)|4 (75.0/4.0)
(Lenght <= 2)|4 (17.0/11.0)
(Height >= 29) and (P_black <= 0.224)|5 (43.0/2.0)
(Height >= 28) and (P_black <= 0.256)|5 (5.0/2.0)
(P_black <= 0.159) and (Eccen <= 3.429)|5 (46.0/17.0)
(Height <= 3) and (Mean_tr >= 10) and (Area >= 28)|2 (139.0/2.0)
(Height <= 2) and (P_black >= 0.456)|2 (113.0/15.0)
(Height <= 4) and (Mean_tr >= 1.6) and (Eccen >= 27) and (Wb_trans <= 13)|2 (17.0/2.0)
(Mean_tr >= 21.3) and (Eccen >= 6.5)|2 (19.0/2.0)
(Height <= 3) and (P_black >= 0.239) and (P_black <= 0.364) and (Mean_tr >= 1.38)|2 (11.0/2.0)
|1 (4406.0/41.0)


## PART

Decision list:

rules | predicted class
---|---
Height > 3 AND Eccen > 0.222 AND Height <= 27 AND Mean_tr <= 15.9 AND Blackpix > 14|1 (3532.0/21.0)
Eccen > 6.8 AND Mean_tr > 1.29 AND Wb_trans <= 269|2 (266.0/30.0)
Eccen > 0.222 AND Height <= 26 AND Lenght > 2 AND P_black > 0.159|1 (219.0/19.0)
Eccen > 0.222 AND P_black <= 0.301 AND Height > 5|5 (70.0/13.0)
Eccen <= 0.222|4 (68.0/6.0)
Height <= 87 AND P_black <= 0.693 AND Eccen > 1.8|1 (20.0/1.0)
|3 (42.0/21.0)


## J48 Decision Tree

* Height <= 3
	* Lenght <= 7: 1 (25.0/4.0)
	* Lenght > 7
		* Mean_tr <= 3.68
			* Mean_tr <= 1.35: 1 (49.0/5.0)
			* Mean_tr > 1.35
				* Eccen <= 12.5: 1 (16.0/3.0)
				* Eccen > 12.5: 2 (40.0/7.0)
		* Mean_tr > 3.68: 2 (225.0/10.0)
* Height > 3
	* Eccen <= 0.222: 4 (78.0/6.0)
	* Eccen > 0.222
		* Height <= 27
			* Mean_tr <= 21.29
				* Blackpix <= 14
					* P_black <= 0.159
						* P_and <= 0.548: 5 (14.0/2.0)
						* P_and > 0.548: 1 (9.0/4.0)
					* P_black > 0.159: 1 (158.0/18.0)
				* Blackpix > 14: 1 (4155.0/28.0)
			* Mean_tr > 21.29
				* Eccen <= 1.254: 1 (19.0)
				* Eccen > 1.254: 2 (27.0/6.0)
		* Height > 27
			* P_black <= 0.301: 5 (61.0/10.0)
			* P_black > 0.301
				* Height <= 87
					* Eccen <= 1.8: 3 (18.0/7.0)
					* Eccen > 1.8: 1 (11.0)
				* Height > 87: 3 (14.0)


## SimpleCart Decision Tree

* Height < 3.5
	* Mean_tr < 1.355: 1(44.0/5.0)
	* Mean_tr >= 1.355
		* Eccen < 7.5: 1(26.0/8.0)
		* Eccen >= 7.5
			* Blackpix < 7.5: 1(8.0/3.0)
			* Blackpix >= 7.5: 2(244.0/17.0)
* Height >= 3.5
	* Eccen < 0.236: 4(72.0/6.0)
	* Eccen >= 0.236
		* Height < 28.5
			* Mean_tr < 30.134999999999998
				* Blackpix < 11.5
					* P_black < 0.241: 5(15.0/11.0)
					* P_black >= 0.241: 1(69.0/12.0)
				* Blackpix >= 11.5: 1(4210.0/43.0)
			* Mean_tr >= 30.134999999999998
				* Eccen < 6.487: 1(14.0/1.0)
				* Eccen >= 6.487: 2(18.0/1.0)
		* Height >= 28.5
			* P_black < 0.3015: 5(50.0/7.0)
			* P_black >= 0.3015
				* Height < 90.0
					* Eccen < 1.3505: 3(6.0/2.0)
					* Eccen >= 1.3505: 1(12.0/1.0)
				* Height >= 90.0: 3(14.0/0.0)


