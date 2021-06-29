# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Height >= 3.5 and Eccen >= 0.236 and Height < 27.5 and Mean_tr < 21.295 | 1 | 0.893486 |
| Height < 3.5 and Mean_tr >= 1.355 and Eccen >= 7.5 | 2 | 0.047070 |
| Height >= 3.5 and Eccen < 0.236 | 4 | 0.012805 |
| Height < 3.5 and Mean_tr < 1.355 | 1 | 0.072718 |
| Height >= 3.5 and Eccen >= 0.236 and Height >= 27.5 and P_black < 0.3015 | 5 | 0.007978 |
| Height < 3.5 and Mean_tr >= 1.355 and Eccen < 7.5 | 1 | 0.043476 |
| Height >= 3.5 and Eccen >= 0.236 and Height < 27.5 and Mean_tr >= 21.295 and Eccen < 6.487 | 1 | 0.036802 |
| Height >= 3.5 and Eccen >= 0.236 and Height < 27.5 and Mean_tr >= 21.295 and Eccen >= 6.487 | 2 | 0.003277 |
| Height >= 3.5 and Eccen >= 0.236 and Height >= 27.5 and P_black >= 0.3015 and Eccen >= 1.2934999999999999 | 1 | 0.024339 |
| Height > 3.0 and Eccen > 0.222 and Height <= 27.0 and Blackpix > 14.0 and Mean_tr <= 15.9 and P_and <= 0.554 and Wb_trans <= 34.0 and Height > 10.0 and P_black <= 0.156 | 5 | 0.002691 |
| Height >= 3.5 and Eccen >= 0.236 and Height >= 27.5 and P_black >= 0.3015 and Eccen < 1.2934999999999999 | 3 | 0.003297 |
| Height > 3.0 and Eccen > 0.222 and Height <= 27.0 and Blackpix <= 14.0 and Lenght > 2.0 and P_black <= 0.241 and Wb_trans <= 5.0 and Mean_tr <= 5.75 and Blackand <= 30.0 | 5 | 0.001016 |
| Height > 3.0 and Eccen > 0.222 and Height <= 27.0 and Blackpix <= 14.0 and Lenght > 2.0 and P_black <= 0.241 and Wb_trans <= 5.0 and Mean_tr <= 5.75 and Blackand > 30.0 | 5 | 0.001066 |
| Height > 3.0 and Eccen > 0.222 and Height > 27.0 and P_black <= 0.331 and P_black > 0.248 and Area <= 15580.0 and Height > 36.0 | 1 | 0.011811 |
| Height <= 3.0 and P_black > 0.228 and Eccen > 7.5 and Mean_tr <= 4.08 and Mean_tr > 1.27 and Eccen <= 12.5 and Eccen <= 10.5 | 1 | 0.005291 |
| Height <= 3.0 and P_black <= 0.228 and Area > 46.0 | 1 | 0.054614 |
| Height <= 3.0 and P_black > 0.228 and Eccen > 7.5 and Mean_tr <= 4.08 and Mean_tr <= 1.27 and Lenght > 84.0 | 2 | 0.000576 |
| Height > 3.0 and Eccen > 0.222 and Height > 27.0 and P_black > 0.331 and Height > 91.0 | 3 | 0.002648 |
| Height > 3.0 and Eccen > 0.222 and Height > 27.0 and P_black <= 0.331 and P_black > 0.248 and Area <= 15580.0 and Height <= 36.0 | 1 | 0.008235 |
| Height <= 3.0 and P_black > 0.228 and Eccen > 7.5 and Mean_tr <= 4.08 and Mean_tr > 1.27 and Eccen > 12.5 and Eccen <= 32.455 and Mean_tr > 1.94 and P_black <= 0.611 and Blackpix > 13.0 | 1 | 0.002988 |
| Height <= 3.0 and P_black <= 0.228 and Area <= 46.0 | 1 | 0.010144 |
| Height <= 3.0 and P_black > 0.228 and Eccen > 7.5 and Mean_tr <= 4.08 and Mean_tr > 1.27 and Eccen <= 12.5 and Eccen > 10.5 | 1 | 0.002988 |
| Height > 3.0 and Eccen > 0.222 and Height <= 27.0 and Blackpix > 14.0 and Mean_tr > 15.9 and Eccen > 17.556 and Height <= 14.0 | 2 | 0.002587 |
| Height > 3.0 and Eccen > 0.222 and Height > 27.0 and P_black > 0.331 and Height <= 91.0 and Eccen <= 1.333 and P_black > 0.461 | 3 | 0.001427 |
| Height > 3.0 and Eccen > 0.222 and Height > 27.0 and P_black <= 0.331 and P_black > 0.248 and Area > 15580.0 | 5 | 0.001270 |
| Height > 3.0 and Eccen > 0.222 and Height <= 27.0 and Blackpix > 14.0 and Mean_tr > 15.9 and Eccen > 17.556 and Height > 14.0 | 2 | 0.000900 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Height > 3.5 and Eccen > 0.236 and Height <= 27.5 and Blackpix > 14.5 and Mean_tr <= 15.905000000000001 and P_and > 0.5545 and Mean_tr > 1.1749999999999998 and Height <= 24.5 and P_and > 0.5834999999999999 and Blackand > 89.5 | 1 | 0.859187 |
| Height <= 3.5 and P_black <= 0.2285 and Area > 55.0 | 1 | 0.052830 |
| Height <= 3.5 and Eccen > 7.5 and Mean_tr > 3.585 and Blackpix > 25.5 and Blackpix <= 615.5 | 2 | 0.089508 |
| Eccen <= 0.236 and Eccen <= 0.1215 and Mean_tr <= 29.0 | 4 | 0.020183 |
| Height > 2.5 and Eccen > 0.236 and Height <= 27.5 and Mean_tr <= 21.295 and Eccen > 0.5425 and P_black > 0.1595 and Blackpix > 11.5 and P_and > 0.5195000000000001 and Blackand <= 3994.0 and P_black > 0.2085 and Area <= 127.0 | 1 | 0.668750 |
| Height <= 2.5 and Mean_tr <= 1.275 and Lenght <= 48.5 | 1 | 0.039275 |
| Height <= 2.5 and Blackpix > 7.5 and P_black > 0.3965 and Mean_tr <= 20.0 and Mean_tr > 9.5 | 2 | 0.030857 |
| Lenght <= 2.5 and Eccen <= 0.236 and Height <= 37.5 and Height <= 9.5 | 4 | 0.010334 |
| Height <= 2.5 and Blackpix > 7.5 and Mean_tr > 1.245 and P_black <= 0.9445 and Eccen > 10.25 and Blackpix > 16.5 | 2 | 0.025641 |
| Height <= 27.5 and Height > 2.5 and Mean_tr <= 8.100000000000001 and Wb_trans > 34.5 and P_and <= 0.945 | 1 | 0.562925 |
| Eccen > 6.487 and Wb_trans > 209.0 and Height <= 31.5 and P_and > 0.9484999999999999 | 1 | 0.048148 |
| Eccen > 6.487 and Height <= 29.5 and P_black > 0.187 and Height <= 24.5 and Area <= 1447.5 and Eccen <= 48.75 and Blackpix > 7.5 and Mean_tr <= 20.91 and Height <= 1.5 and Mean_tr > 1.94 and P_black > 0.6125 and P_black > 0.767 | 2 | 0.019162 |
| Eccen > 6.487 and Height <= 29.5 and Eccen > 12.5835 and Mean_tr > 1.245 and P_black <= 0.8465 and P_black > 0.6125 | 2 | 0.029702 |
| Lenght <= 2.5 and Height > 9.0 and Height > 37.5 | 4 | 0.024119 |
| Eccen > 6.487 and Height <= 29.5 and P_black > 0.187 and Height <= 22.0 and Blackand <= 734.5 and P_black <= 0.8265 and Eccen <= 48.75 and Eccen > 18.5 and P_black <= 0.432 | 2 | 0.026423 |
| Height <= 26.5 and Lenght > 2.5 and Eccen <= 6.487 and P_black > 0.1595 and P_black > 0.454 and Eccen <= 1.9585 | 1 | 0.216216 |
| Height <= 26.5 and Lenght > 2.5 and Eccen <= 6.487 and P_black > 0.1595 and Lenght > 12.5 and P_and > 0.4495 and Lenght > 16.5 | 1 | 0.233962 |
| Eccen > 6.487 and Height <= 29.5 and Mean_tr <= 20.875 and P_black > 0.40149999999999997 and P_black <= 0.581 and Mean_tr > 1.94 | 2 | 0.013425 |
| P_black <= 0.3245 and Height > 11.5 and Eccen <= 3.8120000000000003 and P_black <= 0.229 and P_and > 0.323 | 5 | 0.100592 |
| Height <= 26.5 and Lenght > 2.5 and Eccen <= 6.487 and Mean_tr > 9.5 and Blackand > 29.5 | 1 | 0.079545 |
| Height <= 26.5 and Lenght <= 2.5 and Mean_tr <= 9.5 | 1 | 0.033875 |
| Height <= 26.5 and P_black <= 0.4575 and Lenght > 105.0 | 2 | 0.023754 |
| P_black <= 0.453 and Height <= 28.5 and P_and > 0.3155 and Height <= 3.5 and Lenght > 17.5 | 1 | 0.067073 |
| Eccen <= 0.186 | 4 | 0.026721 |
| Height <= 27.0 and Mean_tr <= 19.875 and Height <= 2.5 and Blackpix <= 7.5 | 1 | 0.039901 |
| Height <= 27.0 and Mean_tr <= 19.875 and Height > 2.5 and P_and > 0.3155 and Mean_tr <= 9.5 and Blackand > 71.0 and Mean_tr <= 2.465 | 1 | 0.113208 |
| Height <= 27.0 and Mean_tr <= 19.875 and Height <= 2.5 | 2 | 0.042483 |
| Height <= 27.0 and Mean_tr > 19.875 | 2 | 0.032579 |
| P_black <= 0.3265 and Area <= 25841.5 and Mean_tr <= 3.0700000000000003 and Eccen <= 3.4645 and Mean_tr > 1.415 and P_black > 0.1595 and Eccen <= 1.8090000000000002 and Eccen > 0.7244999999999999 | 1 | 0.046552 |
| P_black <= 0.3265 and Area <= 25841.5 and Mean_tr <= 3.0700000000000003 and Blackpix > 17.5 and Area > 178.5 | 1 | 0.117647 |
| P_and <= 0.3325 and Wb_trans > 7.5 and Height > 36.5 | 5 | 0.106383 |
| Height <= 27.0 and P_and > 0.3155 and Mean_tr <= 9.5 and Area <= 111.0 and P_black > 0.1955 and Height <= 8.5 and Height > 4.5 and Eccen > 0.854 | 1 | 0.170068 |
| Blackand <= 626.5 and P_and > 0.3155 and Mean_tr <= 9.5 and Blackand <= 55.5 and Area <= 35.5 and P_black <= 0.3385 | 1 | 0.142857 |
| Height > 91.0 | 3 | 0.077381 |
| P_black > 0.3285 and Height <= 27.0 and Mean_tr > 7.5 and Height <= 8.5 | 1 | 0.097363 |
| P_black > 0.3675 and Height <= 27.0 and P_and > 0.6975 | 1 | 0.126311 |
| Blackand > 626.5 and Eccen > 1.8054999999999999 and P_black <= 0.3015 | 5 | 0.059341 |
| Blackand > 626.5 and Eccen > 1.3505 and Height <= 40.0 | 1 | 0.183908 |
| Blackand > 626.5 and Eccen <= 1.3784999999999998 | 3 | 0.079292 |
| Mean_tr <= 9.5 and Wb_trans <= 14.5 and Blackand <= 74.0 and Mean_tr <= 5.125 and Blackpix <= 9.5 | 5 | 0.160131 |
| Mean_tr > 9.5 | 1 | 0.101377 |
| Area <= 325.5 and Area <= 111.0 and Blackand > 26.5 and Mean_tr <= 2.3 | 5 | 0.052411 |
| Area <= 325.5 and Area <= 111.0 and P_black > 0.3335 | 1 | 0.127368 |
| Area <= 325.5 and Wb_trans > 5.5 and P_black <= 0.172 | 1 | 0.153409 |
| Lenght <= 25.0 and Area <= 111.0 | 5 | 0.148810 |
| Lenght <= 25.0 | 1 | 0.177419 |
|  | 5 | 0.363636 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Height >= 28 and Blackpix >= 10947 and Height <= 187 | 3 | 0.002444 |
| Height >= 28 and P_black >= 0.338 and Lenght >= 31 and Eccen <= 1.254 and Mean_tr >= 6.27 | 3 | 0.002038 |
| Eccen <= 0.118 and Mean_tr <= 27 | 4 | 0.006797 |
| Eccen <= 0.182 and Height >= 38 | 4 | 0.003307 |
| Lenght <= 2 and P_black >= 0.9 and Height <= 34 and Area >= 10 | 4 | 0.001036 |
| Lenght <= 2 and Eccen <= 0.182 and Height <= 19 and Mean_tr >= 8 and Height >= 11 | 4 | 0.000829 |
| Lenght <= 2 and Area <= 8 and P_black >= 1 | 4 | 0.001927 |
| P_and <= 0.555 and Height >= 13 and P_black <= 0.201 and Eccen <= 3.337 and Lenght >= 37 | 5 | 0.006724 |
| P_and <= 0.554 and Eccen <= 2.4 and P_black <= 0.156 and P_and >= 0.338 and Wb_trans <= 29 | 5 | 0.003583 |
| Height >= 31 and P_black <= 0.299 and Mean_tr >= 3.09 and Eccen <= 3.795 | 5 | 0.001690 |
| Eccen <= 12.167 and P_and <= 0.337 and Blackpix >= 793 and Height <= 52 | 5 | 0.000845 |
| Blackpix <= 14 and P_and <= 0.65 and P_black <= 0.178 and Lenght <= 9 | 5 | 0.000845 |
| P_black <= 0.323 and Eccen <= 0.529 and P_and >= 0.436 | 5 | 0.001690 |
| Height <= 3 and Mean_tr >= 9.06 and Area >= 26 and Blackpix <= 667 | 2 | 0.030204 |
| Height <= 2 and P_black >= 0.407 and Blackpix >= 26 | 2 | 0.005349 |
| Height <= 2 and Mean_tr >= 1.38 and Area <= 23 and Blackpix >= 11 | 2 | 0.007781 |
| Height <= 3 and Mean_tr >= 1.38 and P_and >= 0.971 and Wb_trans >= 5 and Lenght >= 33 | 2 | 0.002904 |
| Height <= 4 and Mean_tr >= 3 and Eccen >= 8 and Wb_trans >= 3 and P_black <= 0.536 | 2 | 0.002236 |
| Height <= 2 and Area <= 34 and Blackpix >= 8 and Lenght <= 12 and Eccen <= 8 | 2 | 0.001566 |
| Height <= 2 and Blackpix >= 8 and Area <= 23 and P_black <= 0.75 and P_black >= 0.643 | 2 | 0.001566 |
| Eccen >= 6.5 and Wb_trans <= 207 and Mean_tr >= 36.38 and Height >= 4 | 2 | 0.002904 |
| Height <= 2 and Area <= 34 and Mean_tr <= 2.4 and Mean_tr >= 1.4 and P_black <= 0.412 | 2 | 0.001119 |
| Height <= 2 and P_black >= 0.464 and Area >= 28 | 2 | 0.001343 |
| Eccen >= 6.571 and Wb_trans <= 207 and Eccen <= 23.667 and Mean_tr >= 8 and P_black >= 0.11 and Lenght >= 10 | 2 | 0.001789 |
| Wb_trans <= 3 and Eccen >= 1.4 and Blackand <= 11 and Lenght >= 8 | 2 | 0.000700 |
|  | 1 | 0.985288 |


# Text representation of classifiers as-is

## JRip

Decision list:

rules | predicted class
---|---
(Height >= 28) and (Blackpix >= 10947) and (Height <= 187)|3 (12.0/0.0)
(Height >= 28) and (P_black >= 0.338) and (Lenght >= 31) and (Eccen <= 1.254) and (Mean_tr >= 6.27)|3 (10.0/0.0)
(Eccen <= 0.118) and (Mean_tr <= 27)|4 (33.0/0.0)
(Eccen <= 0.182) and (Height >= 38)|4 (16.0/0.0)
(Lenght <= 2) and (P_black >= 0.9) and (Height <= 34) and (Area >= 10)|4 (5.0/0.0)
(Lenght <= 2) and (Eccen <= 0.182) and (Height <= 19) and (Mean_tr >= 8) and (Height >= 11)|4 (4.0/0.0)
(Lenght <= 2) and (Area <= 8) and (P_black >= 1)|4 (13.0/2.0)
(P_and <= 0.555) and (Height >= 13) and (P_black <= 0.201) and (Eccen <= 3.337) and (Lenght >= 37)|5 (32.0/0.0)
(P_and <= 0.554) and (Eccen <= 2.4) and (P_black <= 0.156) and (P_and >= 0.338) and (Wb_trans <= 29)|5 (17.0/0.0)
(Height >= 31) and (P_black <= 0.299) and (Mean_tr >= 3.09) and (Eccen <= 3.795)|5 (8.0/0.0)
(Eccen <= 12.167) and (P_and <= 0.337) and (Blackpix >= 793) and (Height <= 52)|5 (4.0/0.0)
(Blackpix <= 14) and (P_and <= 0.65) and (P_black <= 0.178) and (Lenght <= 9)|5 (4.0/0.0)
(P_black <= 0.323) and (Eccen <= 0.529) and (P_and >= 0.436)|5 (8.0/0.0)
(Height <= 3) and (Mean_tr >= 9.06) and (Area >= 26) and (Blackpix <= 667)|2 (139.0/0.0)
(Height <= 2) and (P_black >= 0.407) and (Blackpix >= 26)|2 (24.0/0.0)
(Height <= 2) and (Mean_tr >= 1.38) and (Area <= 23) and (Blackpix >= 11)|2 (35.0/0.0)
(Height <= 3) and (Mean_tr >= 1.38) and (P_and >= 0.971) and (Wb_trans >= 5) and (Lenght >= 33)|2 (13.0/0.0)
(Height <= 4) and (Mean_tr >= 3) and (Eccen >= 8) and (Wb_trans >= 3) and (P_black <= 0.536)|2 (10.0/0.0)
(Height <= 2) and (Area <= 34) and (Blackpix >= 8) and (Lenght <= 12) and (Eccen <= 8)|2 (7.0/0.0)
(Height <= 2) and (Blackpix >= 8) and (Area <= 23) and (P_black <= 0.75) and (P_black >= 0.643)|2 (7.0/0.0)
(Eccen >= 6.5) and (Wb_trans <= 207) and (Mean_tr >= 36.38) and (Height >= 4)|2 (13.0/0.0)
(Height <= 2) and (Area <= 34) and (Mean_tr <= 2.4) and (Mean_tr >= 1.4) and (P_black <= 0.412)|2 (5.0/0.0)
(Height <= 2) and (P_black >= 0.464) and (Area >= 28)|2 (6.0/0.0)
(Eccen >= 6.571) and (Wb_trans <= 207) and (Eccen <= 23.667) and (Mean_tr >= 8) and (P_black >= 0.11) and (Lenght >= 10)|2 (8.0/0.0)
(Wb_trans <= 3) and (Eccen >= 1.4) and (Blackand <= 11) and (Lenght >= 8)|2 (8.0/3.0)
|1 (4481.0/65.0)


## PART

Decision list:

rules | predicted class
---|---
Height > 3.5 AND Eccen > 0.236 AND Height <= 27.5 AND Blackpix > 14.5 AND Mean_tr <= 15.905000000000001 AND P_and > 0.5545 AND Mean_tr > 1.1749999999999998 AND Height <= 24.5 AND P_and > 0.5834999999999999 AND Blackand > 89.5|1 (3063.0)
Height <= 3.5 AND P_black <= 0.2285 AND Area > 55.0|1 (28.0)
Height <= 3.5 AND Eccen > 7.5 AND Mean_tr > 3.585 AND Blackpix > 25.5 AND Blackpix <= 615.5|2 (151.0)
Eccen <= 0.236 AND Eccen <= 0.1215 AND Mean_tr <= 29.0|4 (33.0)
Height > 2.5 AND Eccen > 0.236 AND Height <= 27.5 AND Mean_tr <= 21.295 AND Eccen > 0.5425 AND P_black > 0.1595 AND Blackpix > 11.5 AND P_and > 0.5195000000000001 AND Blackand <= 3994.0 AND P_black > 0.2085 AND Area <= 127.0|1 (642.0)
Height <= 2.5 AND Mean_tr <= 1.275 AND Lenght <= 48.5|1 (13.0)
Height <= 2.5 AND Blackpix > 7.5 AND P_black > 0.3965 AND Mean_tr <= 20.0 AND Mean_tr > 9.5|2 (27.0)
Lenght <= 2.5 AND Eccen <= 0.236 AND Height <= 37.5 AND Height <= 9.5|4 (15.0/3.0)
Height <= 2.5 AND Blackpix > 7.5 AND Mean_tr > 1.245 AND P_black <= 0.9445 AND Eccen > 10.25 AND Blackpix > 16.5|2 (22.0)
Height <= 27.5 AND Height > 2.5 AND Mean_tr <= 8.100000000000001 AND Wb_trans > 34.5 AND P_and <= 0.945|1 (331.0)
Eccen > 6.487 AND Wb_trans > 209.0 AND Height <= 31.5 AND P_and > 0.9484999999999999|1 (13.0)
Eccen > 6.487 AND Height <= 29.5 AND P_black > 0.187 AND Height <= 24.5 AND Area <= 1447.5 AND Eccen <= 48.75 AND Blackpix > 7.5 AND Mean_tr <= 20.91 AND Height <= 1.5 AND Mean_tr > 1.94 AND P_black > 0.6125 AND P_black > 0.767|2 (15.0/3.0)
Eccen > 6.487 AND Height <= 29.5 AND Eccen > 12.5835 AND Mean_tr > 1.245 AND P_black <= 0.8465 AND P_black > 0.6125|2 (16.0)
Lenght <= 2.5 AND Height > 9.0 AND Height > 37.5|4 (13.0)
Eccen > 6.487 AND Height <= 29.5 AND P_black > 0.187 AND Height <= 22.0 AND Blackand <= 734.5 AND P_black <= 0.8265 AND Eccen <= 48.75 AND Eccen > 18.5 AND P_black <= 0.432|2 (13.0)
Height <= 26.5 AND Lenght > 2.5 AND Eccen <= 6.487 AND P_black > 0.1595 AND P_black > 0.454 AND Eccen <= 1.9585|1 (56.0)
Height <= 26.5 AND Lenght > 2.5 AND Eccen <= 6.487 AND P_black > 0.1595 AND Lenght > 12.5 AND P_and > 0.4495 AND Lenght > 16.5|1 (62.0)
Eccen > 6.487 AND Height <= 29.5 AND Mean_tr <= 20.875 AND P_black > 0.40149999999999997 AND P_black <= 0.581 AND Mean_tr > 1.94|2 (10.0/3.0)
P_black <= 0.3245 AND Height > 11.5 AND Eccen <= 3.8120000000000003 AND P_black <= 0.229 AND P_and > 0.323|5 (34.0)
Height <= 26.5 AND Lenght > 2.5 AND Eccen <= 6.487 AND Mean_tr > 9.5 AND Blackand > 29.5|1 (14.0)
Height <= 26.5 AND Lenght <= 2.5 AND Mean_tr <= 9.5|1 (15.0/6.0)
Height <= 26.5 AND P_black <= 0.4575 AND Lenght > 105.0|2 (11.0/2.0)
P_black <= 0.453 AND Height <= 28.5 AND P_and > 0.3155 AND Height <= 3.5 AND Lenght > 17.5|1 (10.0)
Eccen <= 0.186|4 (15.0/3.0)
Height <= 27.0 AND Mean_tr <= 19.875 AND Height <= 2.5 AND Blackpix <= 7.5|1 (14.0/5.0)
Height <= 27.0 AND Mean_tr <= 19.875 AND Height > 2.5 AND P_and > 0.3155 AND Mean_tr <= 9.5 AND Blackand > 71.0 AND Mean_tr <= 2.465|1 (18.0)
Height <= 27.0 AND Mean_tr <= 19.875 AND Height <= 2.5|2 (14.0/3.0)
Height <= 27.0 AND Mean_tr > 19.875|2 (14.0/3.0)
P_black <= 0.3265 AND Area <= 25841.5 AND Mean_tr <= 3.0700000000000003 AND Eccen <= 3.4645 AND Mean_tr > 1.415 AND P_black > 0.1595 AND Eccen <= 1.8090000000000002 AND Eccen > 0.7244999999999999|1 (15.0/6.0)
P_black <= 0.3265 AND Area <= 25841.5 AND Mean_tr <= 3.0700000000000003 AND Blackpix > 17.5 AND Area > 178.5|1 (16.0)
P_and <= 0.3325 AND Wb_trans > 7.5 AND Height > 36.5|5 (20.0)
Height <= 27.0 AND P_and > 0.3155 AND Mean_tr <= 9.5 AND Area <= 111.0 AND P_black > 0.1955 AND Height <= 8.5 AND Height > 4.5 AND Eccen > 0.854|1 (19.0)
Blackand <= 626.5 AND P_and > 0.3155 AND Mean_tr <= 9.5 AND Blackand <= 55.5 AND Area <= 35.5 AND P_black <= 0.3385|1 (17.0)
Height > 91.0|3 (13.0)
P_black > 0.3285 AND Height <= 27.0 AND Mean_tr > 7.5 AND Height <= 8.5|1 (9.0)
P_black > 0.3675 AND Height <= 27.0 AND P_and > 0.6975|1 (13.0)
Blackand > 626.5 AND Eccen > 1.8054999999999999 AND P_black <= 0.3015|5 (14.0/5.0)
Blackand > 626.5 AND Eccen > 1.3505 AND Height <= 40.0|1 (11.0)
Blackand > 626.5 AND Eccen <= 1.3784999999999998|3 (14.0/3.0)
Mean_tr <= 9.5 AND Wb_trans <= 14.5 AND Blackand <= 74.0 AND Mean_tr <= 5.125 AND Blackpix <= 9.5|5 (13.0/3.0)
Mean_tr > 9.5|1 (12.0/5.0)
Area <= 325.5 AND Area <= 111.0 AND Blackand > 26.5 AND Mean_tr <= 2.3|5 (9.0/4.0)
Area <= 325.5 AND Area <= 111.0 AND P_black > 0.3335|1 (11.0/3.0)
Area <= 325.5 AND Wb_trans > 5.5 AND P_black <= 0.172|1 (9.0/2.0)
Lenght <= 25.0 AND Area <= 111.0|5 (9.0/3.0)
Lenght <= 25.0|1 (8.0/3.0)
|5 (8.0/1.0)


## J48 Decision Tree

* Height <= 3.0
	* P_black <= 0.228
		* Area <= 46.0: 1 (7.0/1.0)
		* Area > 46.0: 1 (29.0)
	* P_black > 0.228
		* Eccen <= 7.5
			* Height <= 2.0: 1 (11.0/5.0)
			* Height > 2.0: 1 (23.0)
		* Eccen > 7.5
			* Mean_tr <= 4.08
				* Mean_tr <= 1.27
					* Lenght <= 84.0: 1 (11.0)
					* Lenght > 84.0: 2 (6.0/2.0)
				* Mean_tr > 1.27
					* Eccen <= 12.5
						* Eccen <= 10.5: 1 (6.0/2.0)
						* Eccen > 10.5: 1 (6.0/3.0)
					* Eccen > 12.5
						* Eccen <= 32.455
							* Mean_tr <= 1.94: 2 (8.0)
							* Mean_tr > 1.94
								* P_black <= 0.611
									* Blackpix <= 13.0: 2 (8.0/2.0)
									* Blackpix > 13.0: 1 (6.0/3.0)
								* P_black > 0.611: 2 (7.0)
						* Eccen > 32.455: 2 (15.0)
			* Mean_tr > 4.08
				* Blackpix <= 25.0
					* Eccen <= 24.0
						* Blackpix <= 10.0
							* Lenght <= 8.0: 2 (6.0)
							* Lenght > 8.0
								* P_black <= 0.833: 2 (6.0/2.0)
								* P_black > 0.833: 2 (7.0/1.0)
						* Blackpix > 10.0: 2 (32.0)
					* Eccen > 24.0: 2 (7.0/3.0)
				* Blackpix > 25.0
					* Blackpix <= 651.0: 2 (150.0)
					* Blackpix > 651.0: 2 (6.0/1.0)
* Height > 3.0
	* Eccen <= 0.222
		* Eccen <= 0.118
			* Mean_tr <= 29.0: 4 (33.0)
			* Mean_tr > 29.0
				* Height <= 37.0: 4 (7.0/2.0)
				* Height > 37.0: 4 (15.0)
		* Eccen > 0.118
			* Eccen <= 0.139: 4 (9.0/3.0)
			* Eccen > 0.139
				* Blackand <= 12.0: 4 (7.0/2.0)
				* Blackand > 12.0: 4 (7.0/1.0)
	* Eccen > 0.222
		* Height <= 27.0
			* Blackpix <= 14.0
				* Lenght <= 2.0
					* Height <= 5.0: 1 (10.0/5.0)
					* Height > 5.0: 1 (7.0/1.0)
				* Lenght > 2.0
					* P_black <= 0.241
						* Wb_trans <= 5.0
							* Mean_tr <= 5.75
								* Blackand <= 30.0: 5 (10.0/3.0)
								* Blackand > 30.0: 5 (7.0/1.0)
							* Mean_tr > 5.75: 1 (8.0/4.0)
						* Wb_trans > 5.0
							* P_black <= 0.159: 1 (6.0/3.0)
							* P_black > 0.159: 1 (9.0)
					* P_black > 0.241
						* Height <= 4.0
							* P_black <= 0.383: 1 (9.0/4.0)
							* P_black > 0.383: 1 (6.0)
						* Height > 4.0
							* Height <= 7.0
								* Eccen <= 0.833
									* Eccen <= 0.754: 1 (34.0)
									* Eccen > 0.754
										* P_and <= 0.75: 1 (6.0/1.0)
										* P_and > 0.75: 1 (9.0/1.0)
								* Eccen > 0.833: 1 (47.0)
							* Height > 7.0
								* Area <= 34.0: 1 (11.0/1.0)
								* Area > 34.0: 1 (6.0/3.0)
			* Blackpix > 14.0
				* Mean_tr <= 15.9
					* P_and <= 0.554
						* Wb_trans <= 34.0
							* Height <= 10.0
								* Area <= 315.0
									* Blackpix <= 22.0
										* Blackpix <= 16.0: 1 (7.0)
										* Blackpix > 16.0
											* Lenght <= 12.0: 1 (8.0/1.0)
											* Lenght > 12.0: 1 (6.0/2.0)
									* Blackpix > 22.0
										* Blackand <= 57.0: 1 (7.0/1.0)
										* Blackand > 57.0: 1 (29.0)
								* Area > 315.0: 1 (6.0/3.0)
							* Height > 10.0
								* P_black <= 0.156: 5 (13.0)
								* P_black > 0.156
									* Lenght <= 12.0: 1 (6.0/3.0)
									* Lenght > 12.0: 1 (9.0/1.0)
						* Wb_trans > 34.0: 1 (192.0)
					* P_and > 0.554
						* Mean_tr <= 1.17
							* Lenght <= 15.0: 1 (6.0/1.0)
							* Lenght > 15.0: 1 (23.0)
						* Mean_tr > 1.17
							* Height <= 24.0
								* P_and <= 0.583
									* Lenght <= 16.0: 1 (6.0/1.0)
									* Lenght > 16.0: 1 (111.0)
								* P_and > 0.583
									* Blackand <= 89.0
										* Area <= 127.0: 1 (577.0)
										* Area > 127.0
											* Height <= 7.0: 1 (7.0)
											* Height > 7.0: 1 (6.0/1.0)
									* Blackand > 89.0: 1 (3063.0)
							* Height > 24.0
								* P_black <= 0.261: 1 (6.0/1.0)
								* P_black > 0.261: 1 (28.0)
				* Mean_tr > 15.9
					* Eccen <= 17.556
						* P_black <= 0.267: 1 (8.0/5.0)
						* P_black > 0.267
							* Area <= 51.0: 1 (6.0/1.0)
							* Area > 51.0: 1 (46.0)
					* Eccen > 17.556
						* Height <= 14.0: 2 (12.0)
						* Height > 14.0: 2 (6.0/1.0)
		* Height > 27.0
			* P_black <= 0.331
				* P_black <= 0.248
					* Eccen <= 3.342
						* Lenght <= 42.0: 5 (6.0/1.0)
						* Lenght > 42.0: 5 (30.0)
					* Eccen > 3.342: 5 (11.0/4.0)
				* P_black > 0.248
					* Area <= 15580.0
						* Height <= 36.0: 1 (6.0/1.0)
						* Height > 36.0: 1 (6.0)
					* Area > 15580.0: 5 (8.0/1.0)
			* P_black > 0.331
				* Height <= 91.0
					* Eccen <= 1.333
						* P_black <= 0.461: 3 (7.0/3.0)
						* P_black > 0.461: 3 (7.0)
					* Eccen > 1.333
						* Height <= 39.0: 1 (8.0)
						* Height > 39.0: 1 (6.0/1.0)
				* Height > 91.0: 3 (13.0)


## SimpleCart Decision Tree

* Height < 3.5
	* Mean_tr < 1.355: 1(43.0/4.0)
	* Mean_tr >= 1.355
		* Eccen < 7.5: 1(27.0/5.0)
		* Eccen >= 7.5: 2(252.0/26.0)
* Height >= 3.5
	* Eccen < 0.236: 4(70.0/8.0)
	* Eccen >= 0.236
		* Height < 27.5
			* Mean_tr < 21.295: 1(4269.0/68.0)
			* Mean_tr >= 21.295
				* Eccen < 6.487: 1(21.0/2.0)
				* Eccen >= 6.487: 2(17.0/2.0)
		* Height >= 27.5
			* P_black < 0.3015: 5(49.0/13.0)
			* P_black >= 0.3015
				* Eccen < 1.2934999999999999: 3(18.0/2.0)
				* Eccen >= 1.2934999999999999: 1(18.0/8.0)


