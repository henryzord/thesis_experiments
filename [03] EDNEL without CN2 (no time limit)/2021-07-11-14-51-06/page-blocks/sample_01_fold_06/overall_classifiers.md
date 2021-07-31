# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 1 | 0.898739 |
| Height < 3.5 and Mean_tr >= 1.355 and Eccen >= 7.5 | 2 | 0.046366 |
| Height > 3 and Eccen <= 0.222 | 4 | 0.012854 |
| Height >= 3.5 and Eccen >= 0.236 and Height >= 27.5 and P_black < 0.22999999999999998 | 5 | 0.007529 |
| Height >= 3.5 and Eccen >= 0.236 and Height < 27.5 and Mean_tr >= 21.295 and Eccen >= 6.487 | 2 | 0.003461 |
| Height >= 3.5 and Eccen >= 0.236 and Height >= 27.5 and P_black >= 0.22999999999999998 and Eccen < 1.2934999999999999 | 3 | 0.003065 |
| Height > 3 and Eccen > 0.222 and Height <= 27 and Mean_tr <= 21.29 and Blackpix > 14 and P_and <= 0.497 and Height > 12 and Wb_trans <= 39 and Mean_tr <= 7.38 and P_black <= 0.156 | 5 | 0.002278 |
| Height > 3 and Eccen > 0.222 and Height <= 27 and Mean_tr <= 21.29 and Blackpix <= 14 and P_black <= 0.159 and Mean_tr <= 9.5 and Wb_trans <= 4 | 5 | 0.001865 |
| Height > 3 and Eccen > 0.222 and Height <= 27 and Mean_tr <= 21.29 and Blackpix <= 14 and P_black > 0.159 and Lenght > 2 and Blackpix <= 8 and Eccen > 1.222 and Wb_trans > 2 | 5 | 0.000864 |
| Height > 3 and Eccen > 0.222 and Height > 27 and P_black <= 0.331 and P_black > 0.21 and Height > 82 | 5 | 0.000830 |
| Height > 3 and Eccen > 0.222 and Height <= 27 and Mean_tr <= 21.29 and Blackpix <= 14 and P_black <= 0.159 and Mean_tr <= 9.5 and Wb_trans > 4 and Height > 5 and Wb_trans <= 5 | 5 | 0.000622 |
| Height > 3 and Eccen > 0.222 and Height <= 27 and Mean_tr <= 21.29 and Blackpix > 14 and P_and <= 0.497 and Height <= 12 and Mean_tr > 5.2 and Eccen > 4.077 and Height <= 6 | 2 | 0.000649 |
| Height > 3 and Eccen > 0.222 and Height <= 27 and Mean_tr <= 21.29 and Blackpix <= 14 and P_black > 0.159 and Lenght > 2 and Blackpix > 8 and Wb_trans <= 2 and Area > 31 and Area <= 38 | 5 | 0.000622 |
| Eccen > 66.55 and Wb_trans > 25.5 and Wb_trans <= 781 | 2 | 0.001925 |
| Height > 3 and Eccen > 0.222 and Height > 27 and P_black > 0.331 and Height > 87 | 3 | 0.002446 |
| Eccen > 6.755 and Eccen <= 34.857 and Wb_trans <= 1.5 | 2 | 0.009985 |
| Height > 3 and Eccen > 0.222 and Height <= 27 and Mean_tr <= 21.29 and Blackpix <= 14 and P_black <= 0.159 and Mean_tr <= 9.5 and Wb_trans > 4 and Height > 5 and Wb_trans > 5 and Area <= 74 | 5 | 0.000415 |
| Eccen > 0.236 and Eccen <= 0.5485 and Wb_trans > 7.5 and Wb_trans <= 25.5 | 5 | 0.000467 |
| Height <= 3 and P_black > 0.228 and Eccen <= 7.5 and Height <= 2 and Mean_tr <= 9.5 and P_and > 0.977 and Height > 1 | 2 | 0.000432 |
| Height > 3 and Eccen > 0.222 and Height <= 27 and Mean_tr <= 21.29 and Blackpix > 14 and P_and <= 0.497 and Height <= 12 and Mean_tr > 5.2 and Eccen > 4.077 and Height > 6 and Mean_tr <= 7.42 | 5 | 0.000415 |
| Height > 3 and Eccen > 0.222 and Height <= 27 and Mean_tr > 21.29 and Eccen <= 6.474 and Height <= 6 | 2 | 0.000288 |
| Height > 3 and Eccen > 0.222 and Height <= 27 and Mean_tr <= 21.29 and Blackpix > 14 and P_and <= 0.497 and Height <= 12 and Mean_tr > 5.2 and Eccen > 4.077 and Height > 6 and Mean_tr > 7.42 | 2 | 0.000288 |
| Height > 3 and Eccen > 0.222 and Height <= 27 and Mean_tr <= 21.29 and Blackpix <= 14 and P_black > 0.159 and Lenght <= 2 and P_black > 0.887 | 4 | 0.000413 |
| Height > 3 and Eccen > 0.222 and Height > 27 and P_black <= 0.331 and P_black > 0.21 and Height <= 82 and Area <= 3471 | 5 | 0.000467 |
| Eccen > 1.3605 and Eccen <= 6.755 and Wb_trans > 781 | 5 | 0.000782 |
| Height <= 3 and P_black > 0.228 and Eccen <= 7.5 and Height <= 2 and Mean_tr > 9.5 | 2 | 0.000432 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Height > 3.5 and Eccen > 0.236 and Height <= 27.5 and Mean_tr <= 21.295 and Blackpix > 14.5 and P_and > 0.4975 | 1 | 0.888966 |
| Height <= 3.5 and P_black > 0.2285 and Eccen > 7.5 and Mean_tr > 4.09 | 2 | 0.243434 |
| Eccen > 0.236 and Height <= 11.5 and Height > 2.5 and Blackpix <= 617.0 and Lenght > 2.5 and P_and > 0.3155 and Mean_tr <= 9.5 and Wb_trans <= 7.5 and P_black > 0.1785 | 1 | 0.264924 |
| Eccen > 0.236 and Height <= 11.5 and P_black <= 0.1895 and Lenght > 17.5 and Mean_tr <= 4.234999999999999 | 1 | 0.251974 |
| Eccen <= 0.236 | 4 | 0.129923 |
| P_black <= 0.1895 and Eccen <= 6.2795000000000005 and Mean_tr > 2.95 | 5 | 0.103817 |
| Height <= 27.5 and P_black > 0.1885 and Eccen <= 6.0 | 1 | 0.289487 |
| Eccen > 4.281000000000001 and Height <= 29.5 and Mean_tr <= 7.815 and Height <= 6.5 and Mean_tr <= 1.275 and P_black <= 0.4145 | 1 | 0.128713 |
| Eccen > 4.281000000000001 and Wb_trans <= 50.5 and Eccen > 12.5835 | 2 | 0.181065 |
| P_black <= 0.331 and Eccen <= 4.173 | 5 | 0.160531 |
| Eccen <= 4.281000000000001 and Height <= 90.0 and Eccen <= 1.3505 | 3 | 0.026608 |
| Height <= 80.0 and Mean_tr <= 3.9450000000000003 | 1 | 0.405605 |
| Height <= 80.0 and Eccen > 6.487 and Height <= 29.5 and Mean_tr <= 7.815 | 1 | 0.105230 |
| Height > 80.0 | 3 | 0.122464 |
| Eccen > 6.487 and Height <= 29.5 | 2 | 0.235332 |
| Lenght <= 289.5 | 1 | 0.326667 |
|  | 5 | 0.365854 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Height >= 28 and P_black >= 0.338 and Blackpix >= 414 and Eccen <= 1.254 and Mean_tr >= 7.05 | 3 | 0.002853 |
| Height >= 72 and Wb_trans >= 1028 and P_black >= 0.359 | 3 | 0.001429 |
| Height >= 28 and P_black >= 0.388 and P_and <= 0.726 and Mean_tr <= 28.77 and Height <= 29 | 3 | 0.000409 |
| Eccen <= 0.091 and Eccen >= 0.029 | 4 | 0.005984 |
| Eccen <= 0.182 and Height >= 39 | 4 | 0.002692 |
| Lenght <= 2 and P_black >= 0.9 and Height <= 10 and Area >= 10 | 4 | 0.000830 |
| Lenght <= 2 and Eccen <= 0.182 and Height <= 19 and Height >= 11 | 4 | 0.000830 |
| Lenght <= 2 and P_black >= 1 and Height <= 9 and Height >= 9 | 4 | 0.001474 |
| Lenght <= 2 and P_black >= 1 and Height <= 8 and Area >= 8 | 4 | 0.001067 |
| Eccen <= 0.148 and Eccen >= 0.143 and Height >= 27 | 4 | 0.000415 |
| Lenght <= 1 and Height <= 7 | 4 | 0.000664 |
| Lenght <= 2 and Eccen <= 0.222 and Height <= 9 | 4 | 0.000138 |
| Lenght <= 2 and Blackand <= 8 | 4 | 0.000092 |
| Lenght <= 2 | 4 | 0.000042 |
| P_and <= 0.555 and Height >= 13 and P_black <= 0.201 and Eccen <= 3.337 and Lenght >= 37 | 5 | 0.006735 |
| P_and <= 0.554 and Eccen <= 2.4 and P_black <= 0.156 and P_and >= 0.338 and Wb_trans <= 29 | 5 | 0.003590 |
| Height >= 31 and P_black <= 0.298 and Mean_tr >= 3.09 and Mean_tr <= 5.69 | 5 | 0.001692 |
| Blackpix <= 14 and P_and <= 0.65 and P_black <= 0.157 and P_black >= 0.114 and Mean_tr >= 2.4 | 5 | 0.001270 |
| P_black <= 0.298 and Height >= 83 | 5 | 0.001270 |
| P_black <= 0.323 and Eccen <= 0.448 | 5 | 0.001270 |
| Height >= 4 and Eccen >= 1.25 and Blackpix <= 8 and P_and >= 0.8 and Lenght <= 11 | 5 | 0.000847 |
| P_and <= 0.65 and Wb_trans <= 20 and P_black <= 0.237 and Lenght <= 9 and Mean_tr <= 2.67 and Height <= 6 | 5 | 0.000635 |
| P_and <= 0.6 and Wb_trans <= 20 and Mean_tr <= 7.35 and Mean_tr >= 5.5 and Lenght >= 8 and Height >= 7 | 5 | 0.000635 |
| Eccen <= 0.833 and P_and <= 0.65 and Mean_tr <= 4.5 and Height <= 5 | 5 | 0.000424 |
| Mean_tr >= 9.06 and Height <= 2 and Area >= 41 | 2 | 0.024406 |
| Height <= 3 and Mean_tr >= 2.97 and Eccen >= 8 and Blackpix >= 11 and Eccen <= 23 | 2 | 0.009598 |
| Height <= 3 and Blackpix >= 21 and Mean_tr >= 2.4 and P_black <= 0.505 | 2 | 0.006048 |
| Height <= 4 and P_black >= 0.464 and Eccen >= 8 and Lenght >= 28 and P_and >= 0.978 and P_black <= 0.897 | 2 | 0.005826 |
| Height <= 4 and Eccen >= 8 and P_black >= 0.643 and Mean_tr >= 26 | 2 | 0.001800 |
| P_black >= 0.424 and Height <= 2 and Mean_tr >= 8 and Lenght <= 14 and Area >= 10 | 2 | 0.001575 |
| Height <= 1 and Mean_tr >= 1.38 and Mean_tr <= 2.33 and P_black <= 0.412 | 2 | 0.002249 |
| P_black >= 0.424 and Height <= 2 and Blackpix >= 8 and Blackpix <= 9 and Lenght <= 8 | 2 | 0.001575 |
| Eccen >= 20.059 and Height >= 4 and Mean_tr >= 15.91 | 2 | 0.003593 |
| P_black >= 0.424 and Height <= 1 and Blackpix <= 11 and Lenght >= 14 and P_black <= 0.55 | 2 | 0.001126 |
| Wb_trans <= 4 and Eccen >= 3.5 and P_black >= 0.643 and P_black <= 0.692 | 2 | 0.000676 |
| Eccen >= 2 and Wb_trans <= 1 and P_and <= 0.611 and Height <= 7 | 2 | 0.001126 |
| Area <= 10 and Height <= 1 and P_black <= 0.889 and P_black >= 0.875 | 2 | 0.000451 |
| P_black >= 0.424 and Height <= 1 and Blackpix >= 27 and Lenght >= 106 | 2 | 0.000451 |
|  | 1 | 0.991031 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

eccen|wb_trans|class
---|---|---
(6.755-34.857]|(781-inf)|1
(0.5485-1.3605]|(781-inf)|3
(1.3605-6.755]|(781-inf)|5
(34.857-66.55]|(781-inf)|1
(-inf-0.236]|(25.5-781]|4
(66.55-inf)|(25.5-781]|2
(0.236-0.5485]|(25.5-781]|5
(34.857-66.55]|(25.5-781]|1
(0.5485-1.3605]|(25.5-781]|1
(1.3605-6.755]|(25.5-781]|1
(6.755-34.857]|(25.5-781]|1
(0.236-0.5485]|(7.5-25.5]|5
(-inf-0.236]|(7.5-25.5]|4
(66.55-inf)|(7.5-25.5]|2
(6.755-34.857]|(7.5-25.5]|1
(34.857-66.55]|(7.5-25.5]|2
(1.3605-6.755]|(7.5-25.5]|1
(0.5485-1.3605]|(7.5-25.5]|1
(-inf-0.236]|(1.5-7.5]|1
(34.857-66.55]|(1.5-7.5]|2
(66.55-inf)|(1.5-7.5]|2
(0.236-0.5485]|(1.5-7.5]|1
(1.3605-6.755]|(1.5-7.5]|1
(6.755-34.857]|(1.5-7.5]|2
(0.5485-1.3605]|(1.5-7.5]|1
(66.55-inf)|(-inf-1.5]|2
(34.857-66.55]|(-inf-1.5]|2
(-inf-0.236]|(-inf-1.5]|4
(0.236-0.5485]|(-inf-1.5]|1
(1.3605-6.755]|(-inf-1.5]|1
(0.5485-1.3605]|(-inf-1.5]|1
(6.755-34.857]|(-inf-1.5]|2

## JRip

Decision list:

rules | predicted class
---|---
(Height >= 28) and (P_black >= 0.338) and (Blackpix >= 414) and (Eccen <= 1.254) and (Mean_tr >= 7.05)|3 (14.0/0.0)
(Height >= 72) and (Wb_trans >= 1028) and (P_black >= 0.359)|3 (7.0/0.0)
(Height >= 28) and (P_black >= 0.388) and (P_and <= 0.726) and (Mean_tr <= 28.77) and (Height <= 29)|3 (2.0/0.0)
(Eccen <= 0.091) and (Eccen >= 0.029)|4 (29.0/0.0)
(Eccen <= 0.182) and (Height >= 39)|4 (13.0/0.0)
(Lenght <= 2) and (P_black >= 0.9) and (Height <= 10) and (Area >= 10)|4 (4.0/0.0)
(Lenght <= 2) and (Eccen <= 0.182) and (Height <= 19) and (Height >= 11)|4 (4.0/0.0)
(Lenght <= 2) and (P_black >= 1) and (Height <= 9) and (Height >= 9)|4 (9.0/1.0)
(Lenght <= 2) and (P_black >= 1) and (Height <= 8) and (Area >= 8)|4 (7.0/1.0)
(Eccen <= 0.148) and (Eccen >= 0.143) and (Height >= 27)|4 (2.0/0.0)
(Lenght <= 1) and (Height <= 7)|4 (5.0/1.0)
(Lenght <= 2) and (Eccen <= 0.222) and (Height <= 9)|4 (3.0/1.0)
(Lenght <= 2) and (Blackand <= 8)|4 (6.0/4.0)
(Lenght <= 2)|4 (12.0/10.0)
(P_and <= 0.555) and (Height >= 13) and (P_black <= 0.201) and (Eccen <= 3.337) and (Lenght >= 37)|5 (32.0/0.0)
(P_and <= 0.554) and (Eccen <= 2.4) and (P_black <= 0.156) and (P_and >= 0.338) and (Wb_trans <= 29)|5 (17.0/0.0)
(Height >= 31) and (P_black <= 0.298) and (Mean_tr >= 3.09) and (Mean_tr <= 5.69)|5 (8.0/0.0)
(Blackpix <= 14) and (P_and <= 0.65) and (P_black <= 0.157) and (P_black >= 0.114) and (Mean_tr >= 2.4)|5 (6.0/0.0)
(P_black <= 0.298) and (Height >= 83)|5 (6.0/0.0)
(P_black <= 0.323) and (Eccen <= 0.448)|5 (6.0/0.0)
(Height >= 4) and (Eccen >= 1.25) and (Blackpix <= 8) and (P_and >= 0.8) and (Lenght <= 11)|5 (4.0/0.0)
(P_and <= 0.65) and (Wb_trans <= 20) and (P_black <= 0.237) and (Lenght <= 9) and (Mean_tr <= 2.67) and (Height <= 6)|5 (3.0/0.0)
(P_and <= 0.6) and (Wb_trans <= 20) and (Mean_tr <= 7.35) and (Mean_tr >= 5.5) and (Lenght >= 8) and (Height >= 7)|5 (3.0/0.0)
(Eccen <= 0.833) and (P_and <= 0.65) and (Mean_tr <= 4.5) and (Height <= 5)|5 (2.0/0.0)
(Mean_tr >= 9.06) and (Height <= 2) and (Area >= 41)|2 (111.0/0.0)
(Height <= 3) and (Mean_tr >= 2.97) and (Eccen >= 8) and (Blackpix >= 11) and (Eccen <= 23)|2 (43.0/0.0)
(Height <= 3) and (Blackpix >= 21) and (Mean_tr >= 2.4) and (P_black <= 0.505)|2 (27.0/0.0)
(Height <= 4) and (P_black >= 0.464) and (Eccen >= 8) and (Lenght >= 28) and (P_and >= 0.978) and (P_black <= 0.897)|2 (26.0/0.0)
(Height <= 4) and (Eccen >= 8) and (P_black >= 0.643) and (Mean_tr >= 26)|2 (8.0/0.0)
(P_black >= 0.424) and (Height <= 2) and (Mean_tr >= 8) and (Lenght <= 14) and (Area >= 10)|2 (7.0/0.0)
(Height <= 1) and (Mean_tr >= 1.38) and (Mean_tr <= 2.33) and (P_black <= 0.412)|2 (10.0/0.0)
(P_black >= 0.424) and (Height <= 2) and (Blackpix >= 8) and (Blackpix <= 9) and (Lenght <= 8)|2 (7.0/0.0)
(Eccen >= 20.059) and (Height >= 4) and (Mean_tr >= 15.91)|2 (16.0/0.0)
(P_black >= 0.424) and (Height <= 1) and (Blackpix <= 11) and (Lenght >= 14) and (P_black <= 0.55)|2 (5.0/0.0)
(Wb_trans <= 4) and (Eccen >= 3.5) and (P_black >= 0.643) and (P_black <= 0.692)|2 (3.0/0.0)
(Eccen >= 2) and (Wb_trans <= 1) and (P_and <= 0.611) and (Height <= 7)|2 (5.0/0.0)
(Area <= 10) and (Height <= 1) and (P_black <= 0.889) and (P_black >= 0.875)|2 (2.0/0.0)
(P_black >= 0.424) and (Height <= 1) and (Blackpix >= 27) and (Lenght >= 106)|2 (2.0/0.0)
|1 (4442.0/35.0)


## PART

Decision list:

rules | predicted class
---|---
Height > 3.5 AND Eccen > 0.236 AND Height <= 27.5 AND Mean_tr <= 21.295 AND Blackpix > 14.5 AND P_and > 0.4975|1 (4001.0/7.0)
Height <= 3.5 AND P_black > 0.2285 AND Eccen > 7.5 AND Mean_tr > 4.09|2 (218.0/8.0)
Eccen > 0.236 AND Height <= 11.5 AND Height > 2.5 AND Blackpix <= 617.0 AND Lenght > 2.5 AND P_and > 0.3155 AND Mean_tr <= 9.5 AND Wb_trans <= 7.5 AND P_black > 0.1785|1 (128.0/13.0)
Eccen > 0.236 AND Height <= 11.5 AND P_black <= 0.1895 AND Lenght > 17.5 AND Mean_tr <= 4.234999999999999|1 (99.0/1.0)
Eccen <= 0.236|4 (80.0/9.0)
P_black <= 0.1895 AND Eccen <= 6.2795000000000005 AND Mean_tr > 2.95|5 (43.0/3.0)
Height <= 27.5 AND P_black > 0.1885 AND Eccen <= 6.0|1 (108.0/16.0)
Eccen > 4.281000000000001 AND Height <= 29.5 AND Mean_tr <= 7.815 AND Height <= 6.5 AND Mean_tr <= 1.275 AND P_black <= 0.4145|1 (26.0)
Eccen > 4.281000000000001 AND Wb_trans <= 50.5 AND Eccen > 12.5835|2 (59.0/8.0)
P_black <= 0.331 AND Eccen <= 4.173|5 (49.0/16.0)
Eccen <= 4.281000000000001 AND Height <= 90.0 AND Eccen <= 1.3505|3 (16.0/4.0)
Height <= 80.0 AND Mean_tr <= 3.9450000000000003|1 (37.0/3.0)
Height <= 80.0 AND Eccen > 6.487 AND Height <= 29.5 AND Mean_tr <= 7.815|1 (14.0/5.0)
Height > 80.0|3 (13.0)
Eccen > 6.487 AND Height <= 29.5|2 (11.0/1.0)
Lenght <= 289.5|1 (10.0)
|5 (6.0/2.0)


## J48 Decision Tree

* Height <= 3
	* P_black <= 0.228
		* Mean_tr <= 1.5: 1 (30.0)
		* Mean_tr > 1.5
			* Height <= 1: 2 (2.0)
			* Height > 1: 1 (3.0)
	* P_black > 0.228
		* Eccen <= 7.5
			* Height <= 2
				* Mean_tr <= 9.5
					* P_and <= 0.977: 1 (4.0)
					* P_and > 0.977
						* Height <= 1: 1 (5.0/2.0)
						* Height > 1: 2 (2.0)
				* Mean_tr > 9.5: 2 (2.0)
			* Height > 2: 1 (23.0/1.0)
		* Eccen > 7.5
			* Mean_tr <= 4.08
				* Mean_tr <= 1.27
					* Blackpix <= 41: 1 (15.0/1.0)
					* Blackpix > 41: 2 (3.0)
				* Mean_tr > 1.27
					* Height <= 2
						* Eccen <= 12.5
							* Blackpix <= 7: 1 (3.0)
							* Blackpix > 7
								* Eccen <= 9.75: 1 (2.0)
								* Eccen > 9.75: 2 (4.0/1.0)
						* Eccen > 12.5: 2 (39.0/5.0)
					* Height > 2: 1 (2.0)
			* Mean_tr > 4.08: 2 (218.0/8.0)
* Height > 3
	* Eccen <= 0.222: 4 (80.0/9.0)
	* Eccen > 0.222
		* Height <= 27
			* Mean_tr <= 21.29
				* Blackpix <= 14
					* P_black <= 0.159
						* Mean_tr <= 9.5
							* Wb_trans <= 4: 5 (9.0)
							* Wb_trans > 4
								* Height <= 5: 1 (2.0)
								* Height > 5
									* Wb_trans <= 5: 5 (3.0)
									* Wb_trans > 5
										* Area <= 74: 5 (2.0)
										* Area > 74: 1 (4.0/1.0)
						* Mean_tr > 9.5: 1 (2.0/1.0)
					* P_black > 0.159
						* Lenght <= 2
							* P_black <= 0.887: 1 (14.0/3.0)
							* P_black > 0.887: 4 (2.0)
						* Lenght > 2
							* Blackpix <= 8
								* Eccen <= 1.222: 1 (20.0/2.0)
								* Eccen > 1.222
									* Wb_trans <= 2: 1 (2.0/1.0)
									* Wb_trans > 2: 5 (6.0/1.0)
							* Blackpix > 8
								* Wb_trans <= 2
									* Area <= 31: 1 (19.0/1.0)
									* Area > 31
										* Area <= 38: 5 (3.0)
										* Area > 38: 1 (5.0/1.0)
								* Wb_trans > 2: 1 (91.0/2.0)
				* Blackpix > 14
					* P_and <= 0.497
						* Height <= 12
							* Mean_tr <= 5.2: 1 (109.0/3.0)
							* Mean_tr > 5.2
								* Eccen <= 4.077: 1 (7.0)
								* Eccen > 4.077
									* Height <= 6: 2 (3.0)
									* Height > 6
										* Mean_tr <= 7.42: 5 (2.0)
										* Mean_tr > 7.42: 2 (3.0/1.0)
						* Height > 12
							* Wb_trans <= 39
								* Mean_tr <= 7.38
									* P_black <= 0.156: 5 (11.0)
									* P_black > 0.156
										* Lenght <= 11: 5 (2.0)
										* Lenght > 11: 1 (2.0)
								* Mean_tr > 7.38: 1 (5.0)
							* Wb_trans > 39: 1 (8.0)
					* P_and > 0.497: 1 (4001.0/7.0)
			* Mean_tr > 21.29
				* Eccen <= 6.474
					* Height <= 6: 2 (3.0/1.0)
					* Height > 6: 1 (19.0/1.0)
				* Eccen > 6.474: 2 (18.0/1.0)
		* Height > 27
			* P_black <= 0.331
				* P_black <= 0.21
					* P_black <= 0.109
						* P_and <= 0.271: 5 (10.0/1.0)
						* P_and > 0.271: 1 (4.0/1.0)
					* P_black > 0.109: 5 (29.0)
				* P_black > 0.21
					* Height <= 82
						* Area <= 3471: 5 (4.0/1.0)
						* Area > 3471: 1 (12.0/1.0)
					* Height > 82: 5 (4.0)
			* P_black > 0.331
				* Height <= 87
					* Eccen <= 1.333
						* Wb_trans <= 63: 3 (12.0/1.0)
						* Wb_trans > 63: 1 (4.0/1.0)
					* Eccen > 1.333: 1 (13.0/1.0)
				* Height > 87: 3 (12.0)


## SimpleCart Decision Tree

* Height < 3.5
	* Mean_tr < 1.355: 1(43.0/4.0)
	* Mean_tr >= 1.355
		* Eccen < 7.5: 1(27.0/7.0)
		* Eccen >= 7.5: 2(249.0/27.0)
* Height >= 3.5
	* Eccen < 0.236: 4(71.0/9.0)
	* Eccen >= 0.236
		* Height < 27.5
			* Mean_tr < 21.295: 1(4271.0/66.0)
			* Mean_tr >= 21.295
				* Eccen < 6.487: 1(19.0/3.0)
				* Eccen >= 6.487: 2(17.0/1.0)
		* Height >= 27.5
			* P_black < 0.22999999999999998: 5(41.0/5.0)
			* P_black >= 0.22999999999999998
				* Eccen < 1.2934999999999999: 3(19.0/5.0)
				* Eccen >= 1.2934999999999999: 1(24.0/10.0)


