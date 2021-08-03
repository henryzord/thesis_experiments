# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Height >= 3.5 and Eccen >= 0.236 and Height < 28.5 and Mean_tr < 21.295 | 1 | 0.894341 |
| Height < 3.5 and Mean_tr >= 1.355 and Eccen >= 7.5 and P_black >= 0.238 | 2 | 0.047840 |
| Height >= 3.5 and Eccen < 0.236 | 4 | 0.012815 |
| Height < 3.5 and Mean_tr < 1.355 | 1 | 0.073260 |
| Height >= 3.5 and Eccen >= 0.236 and Height >= 28.5 and P_black < 0.3015 | 5 | 0.007726 |
| Height < 3.5 and Mean_tr >= 1.355 and Eccen < 7.5 | 1 | 0.043810 |
| Height >= 3.5 and Eccen >= 0.236 and Height < 28.5 and Mean_tr >= 21.295 and Eccen < 6.487 | 1 | 0.035610 |
| Height >= 3.5 and Eccen >= 0.236 and Height < 28.5 and Mean_tr >= 21.295 and Eccen >= 6.487 | 2 | 0.003492 |
| Height >= 3.5 and Eccen >= 0.236 and Height >= 28.5 and P_black >= 0.3015 and Height < 91.0 and Eccen >= 1.3505 | 1 | 0.024020 |
| Height >= 3.5 and Eccen >= 0.236 and Height >= 28.5 and P_black >= 0.3015 and Height >= 91.0 | 3 | 0.002650 |
| Height < 3.5 and Mean_tr >= 1.355 and Eccen >= 7.5 and P_black < 0.238 | 1 | 0.012698 |
| Height > 12.5 and Height <= 26.5 and Blackpix > 17.5 and Blackpix <= 156.5 and Blackand > 37.5 and Blackand <= 76.5 | 5 | 0.000830 |
| Height >= 3.5 and Eccen >= 0.236 and Height >= 28.5 and P_black >= 0.3015 and Height < 91.0 and Eccen < 1.3505 | 3 | 0.001112 |
| Height > 26.5 and Height <= 89 and Blackpix > 156.5 and Blackpix <= 4096.5 and Blackand > 803 and Blackand <= 4249.5 | 1 | 0.014604 |
| Height <= 2.5 and Blackpix > 17.5 and Blackpix <= 156.5 and Blackand > 76.5 and Blackand <= 214.5 | 2 | 0.006818 |
| Height > 26.5 and Height <= 89 and Blackpix > 156.5 and Blackpix <= 4096.5 and Blackand > 4249.5 and Blackand <= 12099.5 | 1 | 0.017081 |
| Height > 12.5 and Height <= 26.5 and Blackpix <= 11.5 and Blackand > 14.5 and Blackand <= 37.5 | 5 | 0.000415 |
| Height > 6.5 and Height <= 12.5 and Blackpix <= 11.5 and Blackand > 37.5 and Blackand <= 76.5 | 5 | 0.000277 |
| Height > 26.5 and Height <= 89 and Blackpix > 156.5 and Blackpix <= 4096.5 and Blackand > 530.5 and Blackand <= 803 | 3 | 0.000460 |
| Height <= 2.5 and Blackpix <= 11.5 and Blackand <= 14.5 | 2 | 0.004316 |
| Height > 2.5 and Height <= 3.5 and Blackpix > 17.5 and Blackpix <= 156.5 and Blackand > 214.5 and Blackand <= 530.5 | 1 | 0.002004 |
| Height <= 2.5 and Blackpix > 11.5 and Blackpix <= 17.5 and Blackand > 37.5 and Blackand <= 76.5 | 1 | 0.026367 |
| Height <= 2.5 and Blackpix > 17.5 and Blackpix <= 156.5 and Blackand > 37.5 and Blackand <= 76.5 | 2 | 0.009433 |
| Height > 2.5 and Height <= 3.5 and Blackpix > 17.5 and Blackpix <= 156.5 and Blackand > 37.5 and Blackand <= 76.5 | 1 | 0.005988 |
| Height > 26.5 and Height <= 89 and Blackpix > 4096.5 and Blackpix <= 10800.5 and Blackand > 12099.5 and Blackand <= 23196.5 | 5 | 0.000933 |
| Height > 26.5 and Height <= 89 and Blackpix > 4096.5 and Blackpix <= 10800.5 and Blackand > 4249.5 and Blackand <= 12099.5 | 1 | 0.006250 |
| Height > 12.5 and Height <= 26.5 and Blackpix > 156.5 and Blackpix <= 4096.5 and Blackand > 803 and Blackand <= 4249.5 | 1 | 0.301549 |
| Height <= 2.5 and Blackpix <= 11.5 and Blackand > 14.5 and Blackand <= 37.5 | 2 | 0.001415 |
| Height > 6.5 and Height <= 12.5 and Blackpix <= 11.5 and Blackand <= 14.5 | 4 | 0.003665 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Height > 3.0 and Eccen > 0.222 and Height <= 27.0 and Blackpix > 14.0 and Mean_tr <= 15.9 and P_and > 0.554 | 1 | 0.884803 |
| Lenght <= 2.0 and Eccen <= 0.222 | 4 | 0.051216 |
| Height <= 3.0 and P_black > 0.228 and Eccen > 7.5 and Mean_tr > 4.08 | 2 | 0.213537 |
| Height <= 26.0 and Height > 2.0 and Mean_tr <= 6.5 and Wb_trans > 34.0 | 1 | 0.448944 |
| Height <= 26.0 and Eccen <= 6.474 and Lenght > 2.0 and P_black > 0.159 and Eccen > 0.529 and Blackand > 32.0 | 1 | 0.320049 |
| Eccen > 6.917 and Mean_tr <= 1.34 and Blackpix <= 44.0 | 1 | 0.156364 |
| Eccen > 10.938 and Wb_trans <= 331.0 and Lenght > 12.0 and P_black > 0.212 | 2 | 0.116875 |
| P_black > 0.299 and Height <= 26.0 and Lenght > 2.0 and Height > 2.0 | 1 | 0.402372 |
| P_black <= 0.328 and Height > 11.0 and Eccen <= 3.8 and Eccen > 0.286 and P_black <= 0.263 | 5 | 0.203998 |
| Eccen <= 0.5 and Height <= 39.0 and P_black > 0.312 and P_black <= 0.866 | 1 | 0.051358 |
| Eccen <= 0.5 and Height > 29.0 | 4 | 0.033778 |
| P_black <= 0.331 and Blackpix <= 4409.0 and Mean_tr <= 6.42 and Height > 3.0 and Wb_trans > 2.0 and Wb_trans > 3.0 and Mean_tr > 1.41 and Wb_trans <= 527.0 and Lenght <= 166.0 and Wb_trans <= 11.0 and Eccen <= 1.444 | 1 | 0.071181 |
| P_black <= 0.331 and Blackpix <= 4409.0 and Mean_tr <= 6.42 and Height > 3.0 and Lenght > 17.0 and P_and > 0.402 | 1 | 0.112875 |
| P_black <= 0.331 and Blackpix <= 4304.0 and Mean_tr <= 6.04 and Height <= 3.0 | 1 | 0.076923 |
| P_black <= 0.331 and Mean_tr <= 6.44 and Mean_tr > 1.73 and P_black > 0.108 and P_black <= 0.198 | 5 | 0.095663 |
| Blackand > 626.0 and P_black > 0.331 and Height <= 91.0 and Eccen <= 1.333 | 3 | 0.058006 |
| Blackpix <= 10654.0 and Height <= 82.0 and Lenght > 3.0 and Blackand > 640.0 and Lenght <= 354.0 | 1 | 0.225559 |
| Height > 38.0 and P_black > 0.331 | 3 | 0.102083 |
| Height <= 38.0 and Lenght > 3.0 and Mean_tr <= 3.83 and Eccen > 3.462 | 1 | 0.122731 |
| Height > 38.0 | 5 | 0.105195 |
| Lenght > 3.0 and Mean_tr <= 3.83 and Mean_tr <= 1.79 | 1 | 0.022599 |
| Mean_tr > 3.83 and Eccen > 1.069 | 2 | 0.187597 |
| Lenght > 3.0 and Blackand > 16.0 | 5 | 0.233100 |
| Height <= 6.0 | 4 | 0.072593 |
|  | 1 | 0.650000 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Height >= 28 and Blackpix >= 10947 and Height <= 187 | 3 | 0.002446 |
| Height >= 28 and P_black >= 0.338 and Lenght >= 31 and Eccen <= 1.254 and Mean_tr >= 6.27 | 3 | 0.002040 |
| Eccen <= 0.118 and Mean_tr <= 27 | 4 | 0.006803 |
| Eccen <= 0.182 and Height >= 38 | 4 | 0.003310 |
| Lenght <= 2 and P_black >= 0.9 and Height <= 34 | 4 | 0.002943 |
| Lenght <= 2 and Eccen <= 0.222 and Height <= 19 | 4 | 0.000747 |
| P_and <= 0.555 and Height >= 13 and P_black <= 0.201 and Eccen <= 3.337 and Lenght >= 37 | 5 | 0.005891 |
| P_and <= 0.554 and Eccen <= 2.4 and P_black <= 0.156 and P_and >= 0.338 and Wb_trans <= 29 | 5 | 0.003585 |
| Height >= 31 and P_black <= 0.299 and Mean_tr >= 3.09 and Eccen <= 3.795 | 5 | 0.001690 |
| P_and <= 0.534 and Height >= 25 and Mean_tr <= 4.84 and P_black >= 0.128 | 5 | 0.001479 |
| Blackpix <= 14 and P_and <= 0.65 and P_black <= 0.178 | 5 | 0.000692 |
| Lenght <= 8 and P_and <= 0.65 and Mean_tr <= 7 | 5 | 0.000590 |
| Height >= 48 | 5 | 0.000519 |
| Height <= 3 and Mean_tr >= 9.06 and Area >= 26 and Blackpix <= 667 | 2 | 0.030105 |
| Height <= 2 and Mean_tr >= 1.38 and Blackpix >= 8 and P_black >= 0.444 and Area >= 28 | 2 | 0.006702 |
| Height <= 2 and Mean_tr >= 1.38 and Area <= 23 and Blackpix >= 11 | 2 | 0.007811 |
| Height <= 2 and Mean_tr >= 1.38 and Blackpix >= 8 and Area <= 23 and Eccen <= 8 | 2 | 0.001572 |
| Height <= 4 and Eccen >= 7 and Mean_tr >= 3 and Wb_trans >= 6 | 2 | 0.002692 |
| Mean_tr >= 1.38 and Blackpix <= 13 and Height <= 1 and P_black <= 0.75 and Blackpix >= 9 | 2 | 0.003139 |
| Height <= 2 and Wb_trans <= 5 and Area <= 11 | 2 | 0.001797 |
| Eccen >= 6.5 and Mean_tr >= 36.38 and Height >= 5 | 2 | 0.002692 |
| Height <= 2 and P_black >= 0.231 | 2 | 0.001017 |
|  | 1 | 0.989700 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

height|blackpix|blackand|class
---|---|---|---
(89-inf)|(10800.5-inf)|(23196.5-inf)|3
(89-inf)|(10800.5-inf)|(12099.5-23196.5]|3
(89-inf)|(4096.5-10800.5]|(12099.5-23196.5]|5
(26.5-89]|(4096.5-10800.5]|(12099.5-23196.5]|5
(6.5-12.5]|(4096.5-10800.5]|(4249.5-12099.5]|2
(89-inf)|(4096.5-10800.5]|(4249.5-12099.5]|5
(26.5-89]|(4096.5-10800.5]|(4249.5-12099.5]|1
(12.5-26.5]|(4096.5-10800.5]|(4249.5-12099.5]|1
(89-inf)|(156.5-4096.5]|(4249.5-12099.5]|1
(6.5-12.5]|(156.5-4096.5]|(4249.5-12099.5]|1
(12.5-26.5]|(156.5-4096.5]|(4249.5-12099.5]|1
(26.5-89]|(156.5-4096.5]|(4249.5-12099.5]|1
(3.5-4.5]|(156.5-4096.5]|(803-4249.5]|1
(2.5-3.5]|(156.5-4096.5]|(803-4249.5]|1
(-inf-2.5]|(156.5-4096.5]|(803-4249.5]|1
(89-inf)|(156.5-4096.5]|(803-4249.5]|4
(4.5-6.5]|(156.5-4096.5]|(803-4249.5]|1
(26.5-89]|(156.5-4096.5]|(803-4249.5]|1
(6.5-12.5]|(156.5-4096.5]|(803-4249.5]|1
(12.5-26.5]|(156.5-4096.5]|(803-4249.5]|1
(6.5-12.5]|(17.5-156.5]|(803-4249.5]|1
(89-inf)|(156.5-4096.5]|(530.5-803]|1
(26.5-89]|(156.5-4096.5]|(530.5-803]|3
(-inf-2.5]|(156.5-4096.5]|(530.5-803]|2
(2.5-3.5]|(156.5-4096.5]|(530.5-803]|2
(4.5-6.5]|(156.5-4096.5]|(530.5-803]|1
(12.5-26.5]|(156.5-4096.5]|(530.5-803]|1
(6.5-12.5]|(156.5-4096.5]|(530.5-803]|1
(3.5-4.5]|(17.5-156.5]|(530.5-803]|1
(6.5-12.5]|(17.5-156.5]|(530.5-803]|1
(4.5-6.5]|(17.5-156.5]|(530.5-803]|1
(2.5-3.5]|(156.5-4096.5]|(214.5-530.5]|2
(3.5-4.5]|(156.5-4096.5]|(214.5-530.5]|1
(26.5-89]|(156.5-4096.5]|(214.5-530.5]|5
(-inf-2.5]|(156.5-4096.5]|(214.5-530.5]|2
(12.5-26.5]|(156.5-4096.5]|(214.5-530.5]|1
(4.5-6.5]|(156.5-4096.5]|(214.5-530.5]|1
(6.5-12.5]|(156.5-4096.5]|(214.5-530.5]|1
(2.5-3.5]|(17.5-156.5]|(214.5-530.5]|1
(4.5-6.5]|(-inf-11.5]|(530.5-803]|1
(3.5-4.5]|(17.5-156.5]|(214.5-530.5]|1
(26.5-89]|(17.5-156.5]|(214.5-530.5]|1
(-inf-2.5]|(17.5-156.5]|(214.5-530.5]|1
(12.5-26.5]|(17.5-156.5]|(214.5-530.5]|1
(4.5-6.5]|(17.5-156.5]|(214.5-530.5]|1
(6.5-12.5]|(17.5-156.5]|(214.5-530.5]|1
(3.5-4.5]|(156.5-4096.5]|(76.5-214.5]|1
(26.5-89]|(156.5-4096.5]|(76.5-214.5]|1
(6.5-12.5]|(156.5-4096.5]|(76.5-214.5]|1
(12.5-26.5]|(156.5-4096.5]|(76.5-214.5]|1
(-inf-2.5]|(156.5-4096.5]|(76.5-214.5]|2
(89-inf)|(17.5-156.5]|(76.5-214.5]|4
(26.5-89]|(17.5-156.5]|(76.5-214.5]|4
(2.5-3.5]|(17.5-156.5]|(76.5-214.5]|2
(-inf-2.5]|(17.5-156.5]|(76.5-214.5]|2
(12.5-26.5]|(17.5-156.5]|(76.5-214.5]|1
(3.5-4.5]|(17.5-156.5]|(76.5-214.5]|1
(4.5-6.5]|(17.5-156.5]|(76.5-214.5]|1
(6.5-12.5]|(17.5-156.5]|(76.5-214.5]|1
(6.5-12.5]|(11.5-17.5]|(76.5-214.5]|1
(12.5-26.5]|(11.5-17.5]|(76.5-214.5]|1
(-inf-2.5]|(11.5-17.5]|(76.5-214.5]|1
(-inf-2.5]|(-inf-11.5]|(76.5-214.5]|1
(3.5-4.5]|(17.5-156.5]|(37.5-76.5]|1
(26.5-89]|(17.5-156.5]|(37.5-76.5]|4
(12.5-26.5]|(17.5-156.5]|(37.5-76.5]|5
(-inf-2.5]|(17.5-156.5]|(37.5-76.5]|2
(2.5-3.5]|(-inf-11.5]|(76.5-214.5]|1
(2.5-3.5]|(17.5-156.5]|(37.5-76.5]|1
(4.5-6.5]|(17.5-156.5]|(37.5-76.5]|1
(6.5-12.5]|(17.5-156.5]|(37.5-76.5]|1
(3.5-4.5]|(11.5-17.5]|(37.5-76.5]|1
(4.5-6.5]|(11.5-17.5]|(37.5-76.5]|1
(-inf-2.5]|(11.5-17.5]|(37.5-76.5]|1
(6.5-12.5]|(11.5-17.5]|(37.5-76.5]|1
(3.5-4.5]|(-inf-11.5]|(37.5-76.5]|1
(6.5-12.5]|(-inf-11.5]|(37.5-76.5]|5
(4.5-6.5]|(-inf-11.5]|(37.5-76.5]|1
(-inf-2.5]|(-inf-11.5]|(37.5-76.5]|1
(4.5-6.5]|(17.5-156.5]|(14.5-37.5]|1
(26.5-89]|(17.5-156.5]|(14.5-37.5]|4
(-inf-2.5]|(17.5-156.5]|(14.5-37.5]|2
(6.5-12.5]|(17.5-156.5]|(14.5-37.5]|1
(12.5-26.5]|(17.5-156.5]|(14.5-37.5]|4
(3.5-4.5]|(17.5-156.5]|(14.5-37.5]|1
(2.5-3.5]|(11.5-17.5]|(14.5-37.5]|1
(12.5-26.5]|(11.5-17.5]|(14.5-37.5]|4
(3.5-4.5]|(11.5-17.5]|(14.5-37.5]|1
(-inf-2.5]|(11.5-17.5]|(14.5-37.5]|2
(4.5-6.5]|(11.5-17.5]|(14.5-37.5]|1
(6.5-12.5]|(11.5-17.5]|(14.5-37.5]|1
(12.5-26.5]|(-inf-11.5]|(14.5-37.5]|5
(3.5-4.5]|(-inf-11.5]|(14.5-37.5]|1
(2.5-3.5]|(-inf-11.5]|(14.5-37.5]|1
(-inf-2.5]|(-inf-11.5]|(14.5-37.5]|2
(6.5-12.5]|(-inf-11.5]|(14.5-37.5]|1
(4.5-6.5]|(-inf-11.5]|(14.5-37.5]|1
(2.5-3.5]|(11.5-17.5]|(-inf-14.5]|1
(6.5-12.5]|(11.5-17.5]|(-inf-14.5]|1
(12.5-26.5]|(11.5-17.5]|(-inf-14.5]|4
(-inf-2.5]|(11.5-17.5]|(-inf-14.5]|2
(3.5-4.5]|(-inf-11.5]|(-inf-14.5]|1
(2.5-3.5]|(-inf-11.5]|(-inf-14.5]|1
(4.5-6.5]|(-inf-11.5]|(-inf-14.5]|1
(-inf-2.5]|(-inf-11.5]|(-inf-14.5]|2
(6.5-12.5]|(-inf-11.5]|(-inf-14.5]|4

## JRip

Decision list:

rules | predicted class
---|---
(Height >= 28) and (Blackpix >= 10947) and (Height <= 187)|3 (12.0/0.0)
(Height >= 28) and (P_black >= 0.338) and (Lenght >= 31) and (Eccen <= 1.254) and (Mean_tr >= 6.27)|3 (10.0/0.0)
(Eccen <= 0.118) and (Mean_tr <= 27)|4 (33.0/0.0)
(Eccen <= 0.182) and (Height >= 38)|4 (16.0/0.0)
(Lenght <= 2) and (P_black >= 0.9) and (Height <= 34)|4 (18.0/2.0)
(Lenght <= 2) and (Eccen <= 0.222) and (Height <= 19)|4 (8.0/2.0)
(P_and <= 0.555) and (Height >= 13) and (P_black <= 0.201) and (Eccen <= 3.337) and (Lenght >= 37)|5 (28.0/0.0)
(P_and <= 0.554) and (Eccen <= 2.4) and (P_black <= 0.156) and (P_and >= 0.338) and (Wb_trans <= 29)|5 (17.0/0.0)
(Height >= 31) and (P_black <= 0.299) and (Mean_tr >= 3.09) and (Eccen <= 3.795)|5 (8.0/0.0)
(P_and <= 0.534) and (Height >= 25) and (Mean_tr <= 4.84) and (P_black >= 0.128)|5 (7.0/0.0)
(Blackpix <= 14) and (P_and <= 0.65) and (P_black <= 0.178)|5 (15.0/8.0)
(Lenght <= 8) and (P_and <= 0.65) and (Mean_tr <= 7)|5 (36.0/26.0)
(Height >= 48)|5 (20.0/13.0)
(Height <= 3) and (Mean_tr >= 9.06) and (Area >= 26) and (Blackpix <= 667)|2 (138.0/0.0)
(Height <= 2) and (Mean_tr >= 1.38) and (Blackpix >= 8) and (P_black >= 0.444) and (Area >= 28)|2 (30.0/0.0)
(Height <= 2) and (Mean_tr >= 1.38) and (Area <= 23) and (Blackpix >= 11)|2 (35.0/0.0)
(Height <= 2) and (Mean_tr >= 1.38) and (Blackpix >= 8) and (Area <= 23) and (Eccen <= 8)|2 (7.0/0.0)
(Height <= 4) and (Eccen >= 7) and (Mean_tr >= 3) and (Wb_trans >= 6)|2 (12.0/0.0)
(Mean_tr >= 1.38) and (Blackpix <= 13) and (Height <= 1) and (P_black <= 0.75) and (Blackpix >= 9)|2 (14.0/0.0)
(Height <= 2) and (Wb_trans <= 5) and (Area <= 11)|2 (18.0/6.0)
(Eccen >= 6.5) and (Mean_tr >= 36.38) and (Height >= 5)|2 (12.0/0.0)
(Height <= 2) and (P_black >= 0.231)|2 (44.0/29.0)
|1 (4380.0/37.0)


## PART

Decision list:

rules | predicted class
---|---
Height > 3.0 AND Eccen > 0.222 AND Height <= 27.0 AND Blackpix > 14.0 AND Mean_tr <= 15.9 AND P_and > 0.554|1 (3833.0/4.0)
Lenght <= 2.0 AND Eccen <= 0.222|4 (66.0/6.0)
Height <= 3.0 AND P_black > 0.228 AND Eccen > 7.5 AND Mean_tr > 4.08|2 (213.0/7.0)
Height <= 26.0 AND Height > 2.0 AND Mean_tr <= 6.5 AND Wb_trans > 34.0|1 (190.0)
Height <= 26.0 AND Eccen <= 6.474 AND Lenght > 2.0 AND P_black > 0.159 AND Eccen > 0.529 AND Blackand > 32.0|1 (115.0/2.0)
Eccen > 6.917 AND Mean_tr <= 1.34 AND Blackpix <= 44.0|1 (43.0)
Eccen > 10.938 AND Wb_trans <= 331.0 AND Lenght > 12.0 AND P_black > 0.212|2 (63.0/4.0)
P_black > 0.299 AND Height <= 26.0 AND Lenght > 2.0 AND Height > 2.0|1 (135.0/10.0)
P_black <= 0.328 AND Height > 11.0 AND Eccen <= 3.8 AND Eccen > 0.286 AND P_black <= 0.263|5 (54.0/3.0)
Eccen <= 0.5 AND Height <= 39.0 AND P_black > 0.312 AND P_black <= 0.866|1 (15.0/4.0)
Eccen <= 0.5 AND Height > 29.0|4 (9.0)
P_black <= 0.331 AND Blackpix <= 4409.0 AND Mean_tr <= 6.42 AND Height > 3.0 AND Wb_trans > 2.0 AND Wb_trans > 3.0 AND Mean_tr > 1.41 AND Wb_trans <= 527.0 AND Lenght <= 166.0 AND Wb_trans <= 11.0 AND Eccen <= 1.444|1 (15.0/3.0)
P_black <= 0.331 AND Blackpix <= 4409.0 AND Mean_tr <= 6.42 AND Height > 3.0 AND Lenght > 17.0 AND P_and > 0.402|1 (16.0)
P_black <= 0.331 AND Blackpix <= 4304.0 AND Mean_tr <= 6.04 AND Height <= 3.0|1 (13.0/2.0)
P_black <= 0.331 AND Mean_tr <= 6.44 AND Mean_tr > 1.73 AND P_black > 0.108 AND P_black <= 0.198|5 (16.0/1.0)
Blackand > 626.0 AND P_black > 0.331 AND Height <= 91.0 AND Eccen <= 1.333|3 (14.0/3.0)
Blackpix <= 10654.0 AND Height <= 82.0 AND Lenght > 3.0 AND Blackand > 640.0 AND Lenght <= 354.0|1 (22.0)
Height > 38.0 AND P_black > 0.331|3 (14.0)
Height <= 38.0 AND Lenght > 3.0 AND Mean_tr <= 3.83 AND Eccen > 3.462|1 (10.0)
Height > 38.0|5 (9.0)
Lenght > 3.0 AND Mean_tr <= 3.83 AND Mean_tr <= 1.79|1 (6.0/2.0)
Mean_tr > 3.83 AND Eccen > 1.069|2 (31.0/10.0)
Lenght > 3.0 AND Blackand > 16.0|5 (8.0/3.0)
Height <= 6.0|4 (4.0/1.0)
|1 (4.0)


## SimpleCart Decision Tree

* Height < 3.5
	* Mean_tr < 1.355: 1(43.0/4.0)
	* Mean_tr >= 1.355
		* Eccen < 7.5: 1(27.0/5.0)
		* Eccen >= 7.5
			* P_black < 0.238: 1(8.0/2.0)
			* P_black >= 0.238: 2(249.0/18.0)
* Height >= 3.5
	* Eccen < 0.236: 4(70.0/8.0)
	* Eccen >= 0.236
		* Height < 28.5
			* Mean_tr < 21.295: 1(4276.0/72.0)
			* Mean_tr >= 21.295
				* Eccen < 6.487: 1(21.0/3.0)
				* Eccen >= 6.487: 2(18.0/2.0)
		* Height >= 28.5
			* P_black < 0.3015: 5(45.0/9.0)
			* P_black >= 0.3015
				* Height < 91.0
					* Eccen < 1.3505: 3(7.0/2.0)
					* Eccen >= 1.3505: 1(14.0/2.0)
				* Height >= 91.0: 3(13.0/0.0)


