# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 1 | 0.898191 |
| Height < 3.5 and Mean_tr >= 1.355 and Eccen >= 6.25 | 2 | 0.047014 |
| Height >= 3.5 and Eccen < 0.236 | 4 | 0.012847 |
| Height > 3.5 and Eccen > 0.236 and Height > 27.5 and P_black <= 0.3015 | 5 | 0.008237 |
| Height >= 3.5 and Eccen >= 0.236 and Height < 27.5 and Mean_tr >= 21.295 and Eccen >= 1.2375 | 2 | 0.003038 |
| Height > 12.5 and Height <= 26.5 and P_black <= 0.1595 | 5 | 0.001625 |
| Height >= 3.5 and Eccen >= 0.236 and Height >= 27.5 and P_black >= 0.3015 and Eccen < 1.2934999999999999 | 3 | 0.003500 |
| Height > 3.5 and Eccen > 0.236 and Height <= 27.5 and Blackpix <= 12.5 and Lenght > 2.5 and Area <= 61.5 and Blackpix <= 8.5 and Lenght > 4.5 | 5 | 0.000988 |
| Height <= 2.5 and P_black > 0.3375 and P_black <= 0.504 | 2 | 0.005075 |
| Height > 3.5 and Eccen > 0.236 and Height <= 27.5 and Blackpix <= 12.5 and Lenght > 2.5 and Area > 61.5 | 5 | 0.000782 |
| Height > 92 and P_black > 0.3375 and P_black <= 0.504 | 3 | 0.001111 |
| Height > 3.5 and Eccen > 0.236 and Height <= 27.5 and Blackpix > 12.5 and Mean_tr > 15.905 and Eccen > 17.565 | 2 | 0.003246 |
| Height <= 2.5 and P_black > 0.504 and P_black <= 0.721 | 2 | 0.012951 |
| Height > 26.5 and Height <= 92 and P_black > 0.1595 and P_black <= 0.3375 | 5 | 0.002127 |
| Height > 2.5 and Height <= 3.5 and P_black > 0.3375 and P_black <= 0.504 | 2 | 0.002906 |
| Height > 3.5 and Eccen > 0.236 and Height > 27.5 and P_black > 0.3015 and Height <= 107.5 and Eccen <= 1.3505 | 3 | 0.002153 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Height > 3 and Eccen > 0.222 and Height <= 27 and Blackpix > 12 and Mean_tr <= 15.9 and P_and > 0.522 and Eccen > 0.625 and Height <= 24 and Blackpix > 25 | 1 | 0.877326 |
| Lenght <= 2 and Eccen <= 0.222 and P_black > 0.887 and Height > 9 and Height <= 34 | 4 | 0.017927 |
| Height <= 3 and P_black <= 0.228 and Wb_trans > 5 | 1 | 0.062745 |
| Height <= 3 and Lenght > 5 and Mean_tr > 3.68 and Lenght > 11 and P_black <= 0.998 and Blackpix > 16 and Blackpix <= 675 and Eccen > 40.333 | 2 | 0.102821 |
| Height <= 2 and Mean_tr > 1.27 and Blackpix > 7 and P_black > 0.445 and Height <= 1 and Mean_tr <= 22.5 and Mean_tr <= 12.5 and Wb_trans <= 5 and Mean_tr > 2.83 and Lenght <= 38 and Lenght > 10 and P_black > 0.611 | 2 | 0.028571 |
| Lenght <= 2 and Eccen <= 0.222 and P_black > 0.933 and Height <= 37 and Height > 7 and Height > 8 | 4 | 0.006737 |
| Height <= 3 and Eccen > 2.833 and Mean_tr > 9.95 and Eccen <= 24.75 | 2 | 0.031715 |
| Lenght > 2 and Height <= 26 and Height > 3 and P_and > 0.314 and Mean_tr <= 16.83 and Blackpix > 11 and Height <= 10 and Mean_tr <= 3.13 and P_black > 0.208 | 1 | 0.506689 |
| Lenght <= 2 and Eccen <= 0.222 and Height > 29 | 4 | 0.014537 |
| Height <= 3 and Eccen <= 2.833 | 1 | 0.059801 |
| Height <= 3 and Mean_tr <= 1.35 and Lenght <= 100 and P_black <= 0.415 | 1 | 0.043919 |
| Height <= 3 and Eccen > 14.5 and Lenght > 25 and P_black <= 0.915 and Blackpix > 13 and Blackpix > 20 and Blackpix <= 136 and P_black <= 0.77 | 2 | 0.036641 |
| Height <= 27 and Lenght > 2 and Height > 3 and Mean_tr <= 30 and Wb_trans > 34 and Blackand <= 3988 | 1 | 0.349246 |
| Height <= 27 and Lenght > 2 and Height <= 3 and P_and > 0.963 and Mean_tr > 25 | 2 | 0.027668 |
| Height <= 27 and Lenght > 2 and Eccen <= 6.474 and Eccen > 0.36 and P_black > 0.159 and Eccen <= 2.2 and P_black > 0.467 | 1 | 0.158076 |
| Height <= 27 and Lenght > 2 and Eccen <= 6.474 and Eccen > 0.333 and Height <= 12 and P_black <= 0.591 and P_and > 0.314 and Blackpix > 9 and Eccen <= 3.4 and P_black > 0.157 and Blackpix > 10 and Blackand > 18 and Eccen > 1.235 | 1 | 0.140351 |
| Eccen > 6.727 and Wb_trans > 213 and P_and > 0.434 and Height > 23 and Lenght > 177 | 1 | 0.121864 |
| Eccen > 6.727 and Height <= 30 and P_black > 0.187 and Height <= 21 and Blackpix > 684 | 2 | 0.028721 |
| Eccen > 6.727 and Height <= 30 and Wb_trans > 18 and Height <= 9 | 1 | 0.040984 |
| Eccen > 6.474 and Height <= 30 and Blackand <= 4000 and P_black > 0.162 and P_and > 0.533 and Eccen <= 47 and Blackand > 41 | 2 | 0.032086 |
| Eccen <= 0.222 and Eccen <= 0.167 and P_black <= 0.649 | 4 | 0.032258 |
| Height > 27 and P_black <= 0.331 and Height > 28 and P_and <= 0.271 | 5 | 0.066066 |
| Eccen > 6.875 and Blackpix > 651 and Lenght <= 359 | 1 | 0.007092 |
| Eccen > 6.875 and Lenght <= 352 and P_and <= 0.533 and P_black > 0.091 | 2 | 0.024324 |
| Height <= 27 and Lenght > 2 and Height <= 3 and Mean_tr <= 19.25 and Area <= 41 and P_and <= 0.963 and Blackand <= 21 | 1 | 0.027322 |
| Eccen > 6.875 and Mean_tr <= 15.11 and P_black > 0.248 and Eccen <= 39.364 and P_black <= 0.371 | 2 | 0.018405 |
| Height <= 27 and Lenght > 2 and Height <= 3 and Mean_tr <= 19.25 and P_black <= 0.394 and Height <= 2 | 1 | 0.028249 |
| Height <= 27 and Lenght > 2 and Height <= 3 and Mean_tr <= 19.25 and Eccen > 4.167 and Area <= 39 and Blackpix <= 16 and P_black <= 0.56 and Lenght <= 31 | 2 | 0.030769 |
| P_black <= 0.467 and Height <= 28 and P_and > 0.314 and Wb_trans <= 14 and Eccen > 2.875 and Blackand > 30 | 1 | 0.104972 |
| P_black <= 0.467 and Height <= 28 and P_and > 0.314 and P_black > 0.237 and Eccen <= 3.286 and P_black > 0.247 and Height > 4 and Eccen > 0.833 | 1 | 0.156250 |
| Blackand > 625 and P_black > 0.331 and Height > 87 | 3 | 0.044828 |
| Lenght <= 2 and Eccen > 0.222 and P_black <= 0.866 and P_and <= 0.828 | 1 | 0.017660 |
| Lenght <= 2 and Eccen > 0.25 and P_black <= 0.866 | 1 | 0.029412 |
| Lenght <= 2 and Height <= 9 and Area <= 7 | 4 | 0.015843 |
| Height <= 3 and Mean_tr <= 19.25 and Height <= 1 and Wb_trans <= 6 and Mean_tr > 3.58 and Mean_tr > 7.5 and Mean_tr <= 8.86 | 2 | 0.024590 |
| Lenght <= 2 and Height <= 9 and Mean_tr > 7.5 and Lenght <= 1 | 4 | 0.013951 |
| P_black <= 0.371 and Height > 11 and P_black <= 0.079 | 2 | 0.005698 |
| P_black <= 0.371 and Height > 11 and Mean_tr <= 47.33 and P_and <= 0.289 and Height <= 18 | 1 | 0.010101 |
| P_black <= 0.371 and Height > 12 and Mean_tr <= 47.33 and Eccen <= 3.8 and P_and > 0.314 and P_black <= 0.201 | 5 | 0.137441 |
| P_black <= 0.467 and Height <= 28 and Eccen <= 1.103 and Eccen > 0.36 and Blackpix <= 33 and P_and > 0.653 and Area <= 29 | 1 | 0.142857 |
| Height > 27 and P_black <= 0.331 and Mean_tr > 2.02 and Area <= 3471 | 5 | 0.035088 |
| P_black <= 0.547 and Height <= 27 and Mean_tr > 9.44 and Height > 8 | 1 | 0.086580 |
| P_black <= 0.547 and Height <= 27 and Height > 3 and P_and > 0.314 and Lenght <= 17 and P_black > 0.105 and Mean_tr <= 9.44 and Eccen > 1.756 and Eccen <= 2.071 | 5 | 0.037267 |
| P_black <= 0.547 and Height <= 27 and Height > 3 and P_and > 0.314 and Mean_tr <= 1.71 and Mean_tr <= 1.65 | 1 | 0.100000 |
| Height > 22 and Blackand > 10849 and Mean_tr <= 10 | 5 | 0.033333 |
| Height > 22 and P_and > 0.34 and Eccen > 1.8 | 1 | 0.150588 |
| Blackpix > 314 and Lenght <= 160 and Mean_tr > 5.09 and Eccen <= 1.141 | 3 | 0.051282 |
| Lenght <= 2 and Height <= 9 and Height > 4 | 4 | 0.019425 |
| P_black <= 0.467 and Area <= 4420 and Mean_tr > 9.44 and P_and > 0.377 | 1 | 0.030405 |
| P_black <= 0.467 and Mean_tr <= 9.44 and Eccen <= 1.375 and Blackand > 82 | 1 | 0.100000 |
| Blackpix > 418 and P_black <= 0.305 | 5 | 0.029630 |
| Blackpix > 418 and P_black <= 0.494 and Height <= 67 | 3 | 0.017308 |
| Mean_tr <= 9.44 and Height <= 3 and Area <= 28 and Mean_tr <= 3.58 | 1 | 0.071429 |
| P_black <= 0.467 and Mean_tr <= 9.44 and Eccen <= 1.333 and Eccen <= 1.222 and Blackpix <= 23 and Lenght <= 10 and P_black > 0.197 and P_and <= 0.444 | 1 | 0.097222 |
| P_black > 0.467 and Blackpix > 35 and Height <= 32 | 1 | 0.044118 |
| P_black <= 0.467 and Mean_tr > 9.44 | 2 | 0.026273 |
| P_black <= 0.467 and Eccen <= 1.333 and Eccen <= 1.222 and Blackand <= 51 and Eccen <= 1.13 and Eccen <= 0.909 and Area <= 58 and Eccen > 0.462 and Eccen <= 0.583 | 1 | 0.061538 |
| P_black <= 0.467 and Eccen <= 1.333 and Eccen <= 1.222 and P_black > 0.317 and P_black <= 0.358 | 1 | 0.075758 |
| P_black <= 0.467 and Mean_tr <= 2.91 and Blackpix > 7 and P_black <= 0.204 and Area > 106 and P_black <= 0.164 | 1 | 0.152778 |
| P_black <= 0.467 and Eccen <= 3.125 and Blackpix <= 7 and Lenght <= 5 | 5 | 0.059701 |
| P_black <= 0.459 and Eccen <= 3.125 and Blackand > 12 and P_black > 0.126 and P_and > 0.344 and P_and > 0.613 and P_black <= 0.321 | 5 | 0.073529 |
| P_black > 0.459 and Height <= 28 and Lenght > 2 and Mean_tr <= 17.75 and Lenght <= 28 and Wb_trans <= 3 and Area <= 11 and P_black <= 0.95 | 2 | 0.045198 |
| P_black <= 0.459 and Eccen <= 2.929 and P_and <= 0.353 and Height <= 6 | 5 | 0.022222 |
| P_black <= 0.459 and Eccen <= 2.833 and P_black <= 0.126 | 5 | 0.051613 |
| P_black <= 0.459 and Eccen <= 2.833 and Eccen > 1.375 | 1 | 0.053156 |
| P_black <= 0.459 and Eccen <= 2.375 and P_black > 0.412 and P_black <= 0.443 | 1 | 0.066667 |
| P_black <= 0.459 and Eccen <= 2.375 and Blackand <= 19 | 5 | 0.049383 |
| P_black > 0.456 and Height <= 28 and Lenght > 2 and Lenght > 28 | 2 | 0.111111 |
| P_black > 0.494 and Wb_trans <= 3 and P_black <= 0.686 | 2 | 0.130435 |
| Lenght <= 2 and Height <= 10 | 4 | 0.013937 |
| Mean_tr <= 12.29 and Wb_trans <= 12 and P_and > 0.387 and Height > 3 and Mean_tr <= 4.75 and Area > 32 | 1 | 0.171429 |
| P_and > 0.686 and Lenght > 2 and Area > 8 and P_black > 0.472 and P_black <= 0.829 | 1 | 0.193548 |
| Wb_trans > 8 and Height <= 10 | 5 | 0.047619 |
| Mean_tr <= 12.29 and Height > 8 | 5 | 0.081633 |
| Wb_trans <= 4 and Mean_tr <= 16.33 and Height <= 2 | 1 | 0.090000 |
| P_and <= 0.776 and Height <= 12 | 2 | 0.164474 |
| P_black > 0.594 | 4 | 0.062937 |
|  | 1 | 0.421053 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Height >= 28 and P_black >= 0.338 and Lenght >= 31 and Eccen <= 1.254 and Mean_tr >= 7.05 | 3 | 0.003055 |
| Height >= 72 and Blackand >= 23301 | 3 | 0.001224 |
| Eccen <= 0.091 and Eccen >= 0.029 | 4 | 0.005158 |
| Eccen <= 0.222 and Height >= 38 | 4 | 0.003307 |
| Lenght <= 2 and P_black >= 0.9 and Height <= 10 and Area >= 9 | 4 | 0.002292 |
| Lenght <= 2 and Eccen <= 0.167 and Height <= 19 and Mean_tr >= 8 | 4 | 0.001525 |
| Eccen <= 0.5 and P_black >= 0.875 | 4 | 0.001119 |
| Height >= 29 and P_black <= 0.224 and Eccen <= 3.337 and Eccen >= 0.49 | 5 | 0.007555 |
| P_and <= 0.538 and Eccen <= 2.474 and P_black <= 0.156 and P_and >= 0.319 and Wb_trans <= 34 | 5 | 0.003582 |
| P_and <= 0.534 and Height >= 25 and Mean_tr <= 5.35 and P_black >= 0.128 | 5 | 0.001900 |
| Height <= 3 and Mean_tr >= 9.06 and Eccen >= 41 and Blackpix <= 667 | 2 | 0.023591 |
| Height <= 3 and Mean_tr >= 2.13 and Eccen >= 8 and P_black >= 0.608 and P_black <= 0.775 | 2 | 0.007328 |
| Height <= 3 and Eccen >= 12.5 and Mean_tr >= 4.2 and Eccen <= 24.5 | 2 | 0.006225 |
| Height <= 3 and Mean_tr >= 1.38 and Eccen >= 35 and Mean_tr <= 6.31 | 2 | 0.004898 |
| P_black >= 0.407 and Height <= 2 and Blackpix >= 26 and P_black <= 0.897 | 2 | 0.003344 |
| Height <= 4 and Eccen >= 3 and Mean_tr >= 10 and Lenght <= 22 | 2 | 0.001787 |
| Height <= 4 and Eccen >= 4.75 and Mean_tr >= 26 and Lenght <= 259 | 2 | 0.002455 |
| Height <= 2 and Mean_tr >= 1.38 and Blackpix >= 8 and Blackpix <= 8 and Eccen <= 9 | 2 | 0.002009 |
| Wb_trans <= 8 and Eccen >= 4.75 and P_black >= 0.348 and Lenght >= 17 and P_black <= 0.588 and Eccen <= 30 and Wb_trans >= 3 | 2 | 0.003344 |
| Mean_tr >= 6.53 and Eccen >= 20.059 and Height >= 4 and P_black >= 0.374 | 2 | 0.002232 |
|  | 1 | 0.980479 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

height|p_black|class
---|---|---
(2.5-3.5]|(0.999-inf)|1
(92-inf)|(0.999-inf)|1
(3.5-4.5]|(0.999-inf)|1
(12.5-26.5]|(0.999-inf)|4
(26.5-92]|(0.999-inf)|4
(-inf-2.5]|(0.999-inf)|2
(6.5-12.5]|(0.999-inf)|4
(92-inf)|(0.954-0.999]|1
(2.5-3.5]|(0.954-0.999]|1
(-inf-2.5]|(0.954-0.999]|2
(3.5-4.5]|(0.721-0.954]|1
(92-inf)|(0.721-0.954]|3
(4.5-6.5]|(0.721-0.954]|1
(-inf-2.5]|(0.721-0.954]|2
(6.5-12.5]|(0.721-0.954]|1
(12.5-26.5]|(0.721-0.954]|1
(2.5-3.5]|(0.721-0.954]|1
(26.5-92]|(0.504-0.721]|1
(3.5-4.5]|(0.504-0.721]|1
(92-inf)|(0.504-0.721]|3
(2.5-3.5]|(0.504-0.721]|1
(-inf-2.5]|(0.504-0.721]|2
(12.5-26.5]|(0.504-0.721]|1
(4.5-6.5]|(0.504-0.721]|1
(6.5-12.5]|(0.504-0.721]|1
(92-inf)|(0.3375-0.504]|3
(26.5-92]|(0.3375-0.504]|1
(2.5-3.5]|(0.3375-0.504]|2
(-inf-2.5]|(0.3375-0.504]|2
(3.5-4.5]|(0.3375-0.504]|1
(12.5-26.5]|(0.3375-0.504]|1
(4.5-6.5]|(0.3375-0.504]|1
(6.5-12.5]|(0.3375-0.504]|1
(92-inf)|(0.1595-0.3375]|4
(2.5-3.5]|(0.1595-0.3375]|2
(3.5-4.5]|(0.1595-0.3375]|1
(-inf-2.5]|(0.1595-0.3375]|1
(26.5-92]|(0.1595-0.3375]|5
(12.5-26.5]|(0.1595-0.3375]|1
(4.5-6.5]|(0.1595-0.3375]|1
(6.5-12.5]|(0.1595-0.3375]|1
(2.5-3.5]|(-inf-0.1595]|1
(3.5-4.5]|(-inf-0.1595]|1
(-inf-2.5]|(-inf-0.1595]|1
(12.5-26.5]|(-inf-0.1595]|5
(26.5-92]|(-inf-0.1595]|5
(92-inf)|(-inf-0.1595]|5
(6.5-12.5]|(-inf-0.1595]|1
(4.5-6.5]|(-inf-0.1595]|1

## JRip

Decision list:

rules | predicted class
---|---
(Height >= 28) and (P_black >= 0.338) and (Lenght >= 31) and (Eccen <= 1.254) and (Mean_tr >= 7.05)|3 (15.0/0.0)
(Height >= 72) and (Blackand >= 23301)|3 (6.0/0.0)
(Eccen <= 0.091) and (Eccen >= 0.029)|4 (25.0/0.0)
(Eccen <= 0.222) and (Height >= 38)|4 (16.0/0.0)
(Lenght <= 2) and (P_black >= 0.9) and (Height <= 10) and (Area >= 9)|4 (13.0/1.0)
(Lenght <= 2) and (Eccen <= 0.167) and (Height <= 19) and (Mean_tr >= 8)|4 (10.0/1.0)
(Eccen <= 0.5) and (P_black >= 0.875)|4 (13.0/4.0)
(Height >= 29) and (P_black <= 0.224) and (Eccen <= 3.337) and (Eccen >= 0.49)|5 (36.0/0.0)
(P_and <= 0.538) and (Eccen <= 2.474) and (P_black <= 0.156) and (P_and >= 0.319) and (Wb_trans <= 34)|5 (17.0/0.0)
(P_and <= 0.534) and (Height >= 25) and (Mean_tr <= 5.35) and (P_black >= 0.128)|5 (9.0/0.0)
(Height <= 3) and (Mean_tr >= 9.06) and (Eccen >= 41) and (Blackpix <= 667)|2 (108.0/0.0)
(Height <= 3) and (Mean_tr >= 2.13) and (Eccen >= 8) and (P_black >= 0.608) and (P_black <= 0.775)|2 (33.0/0.0)
(Height <= 3) and (Eccen >= 12.5) and (Mean_tr >= 4.2) and (Eccen <= 24.5)|2 (28.0/0.0)
(Height <= 3) and (Mean_tr >= 1.38) and (Eccen >= 35) and (Mean_tr <= 6.31)|2 (22.0/0.0)
(P_black >= 0.407) and (Height <= 2) and (Blackpix >= 26) and (P_black <= 0.897)|2 (15.0/0.0)
(Height <= 4) and (Eccen >= 3) and (Mean_tr >= 10) and (Lenght <= 22)|2 (8.0/0.0)
(Height <= 4) and (Eccen >= 4.75) and (Mean_tr >= 26) and (Lenght <= 259)|2 (11.0/0.0)
(Height <= 2) and (Mean_tr >= 1.38) and (Blackpix >= 8) and (Blackpix <= 8) and (Eccen <= 9)|2 (9.0/0.0)
(Wb_trans <= 8) and (Eccen >= 4.75) and (P_black >= 0.348) and (Lenght >= 17) and (P_black <= 0.588) and (Eccen <= 30) and (Wb_trans >= 3)|2 (15.0/0.0)
(Mean_tr >= 6.53) and (Eccen >= 20.059) and (Height >= 4) and (P_black >= 0.374)|2 (10.0/0.0)
|1 (4502.0/85.0)


## PART

Decision list:

rules | predicted class
---|---
Height > 3 AND Eccen > 0.222 AND Height <= 27 AND Blackpix > 12 AND Mean_tr <= 15.9 AND P_and > 0.522 AND Eccen > 0.625 AND Height <= 24 AND Blackpix > 25|1 (3583.0)
Lenght <= 2 AND Eccen <= 0.222 AND P_black > 0.887 AND Height > 9 AND Height <= 34|4 (23.0)
Height <= 3 AND P_black <= 0.228 AND Wb_trans > 5|1 (32.0)
Height <= 3 AND Lenght > 5 AND Mean_tr > 3.68 AND Lenght > 11 AND P_black <= 0.998 AND Blackpix > 16 AND Blackpix <= 675 AND Eccen > 40.333|2 (113.0)
Height <= 2 AND Mean_tr > 1.27 AND Blackpix > 7 AND P_black > 0.445 AND Height <= 1 AND Mean_tr <= 22.5 AND Mean_tr <= 12.5 AND Wb_trans <= 5 AND Mean_tr > 2.83 AND Lenght <= 38 AND Lenght > 10 AND P_black > 0.611|2 (29.0)
Lenght <= 2 AND Eccen <= 0.222 AND P_black > 0.933 AND Height <= 37 AND Height > 7 AND Height > 8|4 (11.0/2.0)
Height <= 3 AND Eccen > 2.833 AND Mean_tr > 9.95 AND Eccen <= 24.75|2 (32.0)
Lenght > 2 AND Height <= 26 AND Height > 3 AND P_and > 0.314 AND Mean_tr <= 16.83 AND Blackpix > 11 AND Height <= 10 AND Mean_tr <= 3.13 AND P_black > 0.208|1 (303.0)
Lenght <= 2 AND Eccen <= 0.222 AND Height > 29|4 (12.0)
Height <= 3 AND Eccen <= 2.833|1 (18.0)
Height <= 3 AND Mean_tr <= 1.35 AND Lenght <= 100 AND P_black <= 0.415|1 (13.0)
Height <= 3 AND Eccen > 14.5 AND Lenght > 25 AND P_black <= 0.915 AND Blackpix > 13 AND Blackpix > 20 AND Blackpix <= 136 AND P_black <= 0.77|2 (24.0)
Height <= 27 AND Lenght > 2 AND Height > 3 AND Mean_tr <= 30 AND Wb_trans > 34 AND Blackand <= 3988|1 (139.0)
Height <= 27 AND Lenght > 2 AND Height <= 3 AND P_and > 0.963 AND Mean_tr > 25|2 (14.0)
Height <= 27 AND Lenght > 2 AND Eccen <= 6.474 AND Eccen > 0.36 AND P_black > 0.159 AND Eccen <= 2.2 AND P_black > 0.467|1 (46.0)
Height <= 27 AND Lenght > 2 AND Eccen <= 6.474 AND Eccen > 0.333 AND Height <= 12 AND P_black <= 0.591 AND P_and > 0.314 AND Blackpix > 9 AND Eccen <= 3.4 AND P_black > 0.157 AND Blackpix > 10 AND Blackand > 18 AND Eccen > 1.235|1 (40.0)
Eccen > 6.727 AND Wb_trans > 213 AND P_and > 0.434 AND Height > 23 AND Lenght > 177|1 (34.0)
Eccen > 6.727 AND Height <= 30 AND P_black > 0.187 AND Height <= 21 AND Blackpix > 684|2 (11.0)
Eccen > 6.727 AND Height <= 30 AND Wb_trans > 18 AND Height <= 9|1 (10.0)
Eccen > 6.474 AND Height <= 30 AND Blackand <= 4000 AND P_black > 0.162 AND P_and > 0.533 AND Eccen <= 47 AND Blackand > 41|2 (12.0)
Eccen <= 0.222 AND Eccen <= 0.167 AND P_black <= 0.649|4 (13.0)
Height > 27 AND P_black <= 0.331 AND Height > 28 AND P_and <= 0.271|5 (22.0)
Eccen > 6.875 AND Blackpix > 651 AND Lenght <= 359|1 (3.0/1.0)
Eccen > 6.875 AND Lenght <= 352 AND P_and <= 0.533 AND P_black > 0.091|2 (9.0)
Height <= 27 AND Lenght > 2 AND Height <= 3 AND Mean_tr <= 19.25 AND Area <= 41 AND P_and <= 0.963 AND Blackand <= 21|1 (5.0)
Eccen > 6.875 AND Mean_tr <= 15.11 AND P_black > 0.248 AND Eccen <= 39.364 AND P_black <= 0.371|2 (6.0)
Height <= 27 AND Lenght > 2 AND Height <= 3 AND Mean_tr <= 19.25 AND P_black <= 0.394 AND Height <= 2|1 (5.0)
Height <= 27 AND Lenght > 2 AND Height <= 3 AND Mean_tr <= 19.25 AND Eccen > 4.167 AND Area <= 39 AND Blackpix <= 16 AND P_black <= 0.56 AND Lenght <= 31|2 (10.0)
P_black <= 0.467 AND Height <= 28 AND P_and > 0.314 AND Wb_trans <= 14 AND Eccen > 2.875 AND Blackand > 30|1 (19.0)
P_black <= 0.467 AND Height <= 28 AND P_and > 0.314 AND P_black > 0.237 AND Eccen <= 3.286 AND P_black > 0.247 AND Height > 4 AND Eccen > 0.833|1 (30.0)
Blackand > 625 AND P_black > 0.331 AND Height > 87|3 (13.0)
Lenght <= 2 AND Eccen > 0.222 AND P_black <= 0.866 AND P_and <= 0.828|1 (6.0/2.0)
Lenght <= 2 AND Eccen > 0.25 AND P_black <= 0.866|1 (6.0)
Lenght <= 2 AND Height <= 9 AND Area <= 7|4 (6.0/1.0)
Height <= 3 AND Mean_tr <= 19.25 AND Height <= 1 AND Wb_trans <= 6 AND Mean_tr > 3.58 AND Mean_tr > 7.5 AND Mean_tr <= 8.86|2 (6.0)
Lenght <= 2 AND Height <= 9 AND Mean_tr > 7.5 AND Lenght <= 1|4 (6.0/1.0)
P_black <= 0.371 AND Height > 11 AND P_black <= 0.079|2 (3.0/1.0)
P_black <= 0.371 AND Height > 11 AND Mean_tr <= 47.33 AND P_and <= 0.289 AND Height <= 18|1 (3.0/1.0)
P_black <= 0.371 AND Height > 12 AND Mean_tr <= 47.33 AND Eccen <= 3.8 AND P_and > 0.314 AND P_black <= 0.201|5 (29.0)
P_black <= 0.467 AND Height <= 28 AND Eccen <= 1.103 AND Eccen > 0.36 AND Blackpix <= 33 AND P_and > 0.653 AND Area <= 29|1 (17.0)
Height > 27 AND P_black <= 0.331 AND Mean_tr > 2.02 AND Area <= 3471|5 (6.0)
P_black <= 0.547 AND Height <= 27 AND Mean_tr > 9.44 AND Height > 8|1 (10.0)
P_black <= 0.547 AND Height <= 27 AND Height > 3 AND P_and > 0.314 AND Lenght <= 17 AND P_black > 0.105 AND Mean_tr <= 9.44 AND Eccen > 1.756 AND Eccen <= 2.071|5 (6.0)
P_black <= 0.547 AND Height <= 27 AND Height > 3 AND P_and > 0.314 AND Mean_tr <= 1.71 AND Mean_tr <= 1.65|1 (10.0)
Height > 22 AND Blackand > 10849 AND Mean_tr <= 10|5 (5.0)
Height > 22 AND P_and > 0.34 AND Eccen > 1.8|1 (16.0)
Blackpix > 314 AND Lenght <= 160 AND Mean_tr > 5.09 AND Eccen <= 1.141|3 (8.0)
Lenght <= 2 AND Height <= 9 AND Height > 4|4 (4.0/1.0)
P_black <= 0.467 AND Area <= 4420 AND Mean_tr > 9.44 AND P_and > 0.377|1 (4.0/1.0)
P_black <= 0.467 AND Mean_tr <= 9.44 AND Eccen <= 1.375 AND Blackand > 82|1 (8.0)
Blackpix > 418 AND P_black <= 0.305|5 (4.0/1.0)
Blackpix > 418 AND P_black <= 0.494 AND Height <= 67|3 (3.0)
Mean_tr <= 9.44 AND Height <= 3 AND Area <= 28 AND Mean_tr <= 3.58|1 (5.0)
P_black <= 0.467 AND Mean_tr <= 9.44 AND Eccen <= 1.333 AND Eccen <= 1.222 AND Blackpix <= 23 AND Lenght <= 10 AND P_black > 0.197 AND P_and <= 0.444|1 (7.0)
P_black > 0.467 AND Blackpix > 35 AND Height <= 32|1 (3.0)
P_black <= 0.467 AND Mean_tr > 9.44|2 (5.0/2.0)
P_black <= 0.467 AND Eccen <= 1.333 AND Eccen <= 1.222 AND Blackand <= 51 AND Eccen <= 1.13 AND Eccen <= 0.909 AND Area <= 58 AND Eccen > 0.462 AND Eccen <= 0.583|1 (4.0)
P_black <= 0.467 AND Eccen <= 1.333 AND Eccen <= 1.222 AND P_black > 0.317 AND P_black <= 0.358|1 (5.0)
P_black <= 0.467 AND Mean_tr <= 2.91 AND Blackpix > 7 AND P_black <= 0.204 AND Area > 106 AND P_black <= 0.164|1 (10.0)
P_black <= 0.467 AND Eccen <= 3.125 AND Blackpix <= 7 AND Lenght <= 5|5 (4.0)
P_black <= 0.459 AND Eccen <= 3.125 AND Blackand > 12 AND P_black > 0.126 AND P_and > 0.344 AND P_and > 0.613 AND P_black <= 0.321|5 (5.0)
P_black > 0.459 AND Height <= 28 AND Lenght > 2 AND Mean_tr <= 17.75 AND Lenght <= 28 AND Wb_trans <= 3 AND Area <= 11 AND P_black <= 0.95|2 (6.0/2.0)
P_black <= 0.459 AND Eccen <= 2.929 AND P_and <= 0.353 AND Height <= 6|5 (3.0/1.0)
P_black <= 0.459 AND Eccen <= 2.833 AND P_black <= 0.126|5 (4.0/1.0)
P_black <= 0.459 AND Eccen <= 2.833 AND Eccen > 1.375|1 (4.0)
P_black <= 0.459 AND Eccen <= 2.375 AND P_black > 0.412 AND P_black <= 0.443|1 (3.0)
P_black <= 0.459 AND Eccen <= 2.375 AND Blackand <= 19|5 (5.0/1.0)
P_black > 0.456 AND Height <= 28 AND Lenght > 2 AND Lenght > 28|2 (5.0)
P_black > 0.494 AND Wb_trans <= 3 AND P_black <= 0.686|2 (6.0)
Lenght <= 2 AND Height <= 10|4 (3.0/1.0)
Mean_tr <= 12.29 AND Wb_trans <= 12 AND P_and > 0.387 AND Height > 3 AND Mean_tr <= 4.75 AND Area > 32|1 (6.0)
P_and > 0.686 AND Lenght > 2 AND Area > 8 AND P_black > 0.472 AND P_black <= 0.829|1 (4.0)
Wb_trans > 8 AND Height <= 10|5 (3.0/1.0)
Mean_tr <= 12.29 AND Height > 8|5 (5.0/1.0)
Wb_trans <= 4 AND Mean_tr <= 16.33 AND Height <= 2|1 (5.0/2.0)
P_and <= 0.776 AND Height <= 12|2 (3.0)
P_black > 0.594|4 (5.0/2.0)
|1 (3.0/2.0)


## J48 Decision Tree

* Height <= 3.5
	* Mean_tr <= 1.355: 1 (46.0/5.0)
	* Mean_tr > 1.355
		* Lenght <= 5.5: 1 (16.0)
		* Lenght > 5.5
			* Blackpix <= 16.5
				* Height <= 1.5: 2 (75.0/14.0)
				* Height > 1.5: 1 (19.0/7.0)
			* Blackpix > 16.5: 2 (173.0/7.0)
* Height > 3.5
	* Eccen <= 0.236: 4 (71.0/7.0)
	* Eccen > 0.236
		* Height <= 27.5
			* Blackpix <= 12.5
				* Lenght <= 2.5: 1 (14.0/4.0)
				* Lenght > 2.5
					* Area <= 61.5
						* Blackpix <= 8.5
							* Lenght <= 4.5: 1 (14.0/1.0)
							* Lenght > 4.5: 5 (15.0/7.0)
						* Blackpix > 8.5: 1 (60.0/6.0)
					* Area > 61.5: 5 (12.0/6.0)
			* Blackpix > 12.5
				* Mean_tr <= 15.905: 1 (3747.0/26.0)
				* Mean_tr > 15.905
					* Eccen <= 17.565: 1 (53.0/7.0)
					* Eccen > 17.565: 2 (15.0/1.0)
		* Height > 27.5
			* P_black <= 0.3015: 5 (58.0/14.0)
			* P_black > 0.3015
				* Height <= 107.5
					* Eccen <= 1.3505: 3 (13.0/3.0)
					* Eccen > 1.3505: 1 (16.0/1.0)
				* Height > 107.5: 3 (12.0)


## SimpleCart Decision Tree

* Height < 3.5
	* Mean_tr < 1.355: 1(44.0/5.0)
	* Mean_tr >= 1.355
		* Eccen < 6.25: 1(23.0/4.0)
		* Eccen >= 6.25: 2(254.0/29.0)
* Height >= 3.5
	* Eccen < 0.236: 4(71.0/9.0)
	* Eccen >= 0.236
		* Height < 27.5
			* Mean_tr < 21.295: 1(4268.0/61.0)
			* Mean_tr >= 21.295
				* Eccen < 1.2375: 1(18.0/0.0)
				* Eccen >= 1.2375: 2(18.0/5.0)
		* Height >= 27.5
			* P_black < 0.3015: 5(51.0/14.0)
			* P_black >= 0.3015
				* Eccen < 1.2934999999999999: 3(19.0/2.0)
				* Eccen >= 1.2934999999999999: 1(18.0/8.0)


