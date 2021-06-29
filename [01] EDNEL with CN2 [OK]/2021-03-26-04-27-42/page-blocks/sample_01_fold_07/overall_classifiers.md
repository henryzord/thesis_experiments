# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 1 | 0.898009 |
| Height <= 2.5 and Eccen > 6.755 and Eccen <= 34.9445 and Blackpix <= 17.5 | 2 | 0.010817 |
| Height <= 2.5 and Eccen > 66.9375 and Blackpix > 42.5 and Blackpix <= 156.5 | 2 | 0.008788 |
| Height <= 2.5 and Eccen > 34.9445 and Eccen <= 66.9375 and Blackpix > 17.5 and Blackpix <= 42.5 | 2 | 0.005191 |
| Height <= 2.5 and Eccen > 66.9375 and Blackpix > 478.5 and Blackpix <= 693.5 | 2 | 0.005374 |
| Height <= 2.5 and Eccen > 66.9375 and Blackpix > 156.5 and Blackpix <= 400.5 | 2 | 0.004946 |
| Height <= 2.5 and Eccen > 6.755 and Eccen <= 34.9445 and Blackpix > 17.5 and Blackpix <= 42.5 | 2 | 0.004340 |
| Height > 6.5 and Height <= 12.5 and Eccen <= 0.236 and Blackpix <= 17.5 | 4 | 0.004283 |
| Height <= 2.5 and Eccen > 34.9445 and Eccen <= 66.9375 and Blackpix > 42.5 and Blackpix <= 156.5 | 2 | 0.002372 |
| Height > 26.5 and Height <= 89 and Eccen > 1.3605 and Eccen <= 6.755 and Blackpix > 156.5 and Blackpix <= 400.5 | 5 | 0.001865 |
| Height <= 2.5 and Eccen > 6.755 and Eccen <= 34.9445 and Blackpix > 42.5 and Blackpix <= 156.5 | 2 | 0.002157 |
| Height > 26.5 and Height <= 89 and Eccen > 0.5485 and Eccen <= 1.3605 and Blackpix > 156.5 and Blackpix <= 400.5 | 5 | 0.001658 |
| Height > 12.5 and Height <= 26.5 and Eccen <= 0.236 and Blackpix <= 17.5 | 4 | 0.002060 |
| Height > 26.5 and Height <= 89 and Eccen <= 0.236 and Blackpix > 17.5 and Blackpix <= 42.5 | 4 | 0.001873 |
| Height > 26.5 and Height <= 89 and Eccen <= 0.236 and Blackpix > 42.5 and Blackpix <= 156.5 | 4 | 0.001669 |
| Height > 26.5 and Height <= 89 and Eccen > 1.3605 and Eccen <= 6.755 and Blackpix > 4096.5 and Blackpix <= 10800.5 | 5 | 0.000782 |
| Height > 12.5 and Height <= 26.5 and Eccen > 0.5485 and Eccen <= 1.3605 and Blackpix > 17.5 and Blackpix <= 42.5 | 5 | 0.000933 |
| Height > 89 and Eccen > 1.3605 and Eccen <= 6.755 and Blackpix > 4096.5 and Blackpix <= 10800.5 | 5 | 0.001244 |
| Height > 2.5 and Height <= 3.5 and Eccen > 34.9445 and Eccen <= 66.9375 and Blackpix > 42.5 and Blackpix <= 156.5 | 2 | 0.001295 |
| Height > 2.5 and Height <= 3.5 and Eccen > 66.9375 and Blackpix > 478.5 and Blackpix <= 693.5 | 2 | 0.001110 |
| Height > 89 and Eccen > 0.5485 and Eccen <= 1.3605 and Blackpix > 10800.5 | 3 | 0.001224 |
| Height > 89 and Eccen <= 0.236 and Blackpix > 42.5 and Blackpix <= 156.5 | 4 | 0.001237 |
| Height > 26.5 and Height <= 89 and Eccen > 0.5485 and Eccen <= 1.3605 and Blackpix > 400.5 and Blackpix <= 478.5 | 3 | 0.000909 |
| Height > 12.5 and Height <= 26.5 and Eccen <= 0.236 and Blackpix > 17.5 and Blackpix <= 42.5 | 4 | 0.001123 |
| Height > 2.5 and Height <= 3.5 and Eccen > 66.9375 and Blackpix > 156.5 and Blackpix <= 400.5 | 2 | 0.000648 |
| Height > 26.5 and Height <= 89 and Eccen > 0.5485 and Eccen <= 1.3605 and Blackpix > 693.5 and Blackpix <= 4096.5 | 3 | 0.000567 |
| Height > 12.5 and Height <= 26.5 and Eccen > 0.236 and Eccen <= 0.5485 and Blackpix <= 17.5 | 5 | 0.000415 |
| Height > 89 and Eccen > 1.3605 and Eccen <= 6.755 and Blackpix > 10800.5 | 3 | 0.000653 |
| Height <= 2.5 and Eccen > 66.9375 and Blackpix > 400.5 and Blackpix <= 478.5 | 2 | 0.000432 |
| Height > 26.5 and Height <= 89 and Eccen > 0.236 and Eccen <= 0.5485 and Blackpix > 156.5 and Blackpix <= 400.5 | 5 | 0.000104 |
| Height > 26.5 and Height <= 89 and Eccen > 1.3605 and Eccen <= 6.755 and Blackpix > 478.5 and Blackpix <= 693.5 | 5 | 0.000104 |
| Height > 89 and Eccen > 0.5485 and Eccen <= 1.3605 and Blackpix > 4096.5 and Blackpix <= 10800.5 | 3 | 0.000204 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Height > 3.5 and Eccen > 0.236 and Height <= 27.5 and Blackpix > 14.5 and Mean_tr <= 21.645 and P_and > 0.5195000000000001 and P_black > 0.1565 and Mean_tr <= 16.77 and Height <= 24.5 and P_and > 0.5834999999999999 and Blackand > 89.5 | 1 | 0.858989 |
| Height <= 3.5 and Mean_tr <= 1.355 and P_black <= 0.3855 | 1 | 0.070370 |
| Height <= 3.5 and Lenght > 5.5 and Mean_tr > 7.25 and Eccen > 40.5 and Blackpix <= 593.0 | 2 | 0.064181 |
| Eccen <= 0.236 and Mean_tr > 9.5 and Eccen <= 0.093 and Eccen > 0.028999999999999998 | 4 | 0.014397 |
| Height <= 2.5 and Blackpix > 7.5 and P_black > 0.445 and Area <= 40.5 and Blackpix <= 24.5 and Mean_tr > 5.125 | 2 | 0.027114 |
| Eccen <= 0.236 and Height > 37.5 | 4 | 0.011728 |
| Height > 3.5 and Eccen > 0.236 and Height <= 27.5 and Blackpix > 9.5 and Mean_tr <= 30.5 and P_black > 0.1585 and Eccen > 0.6755 and P_and > 0.4455 and Mean_tr <= 9.7 and Wb_trans <= 563.5 and P_black > 0.2085 and Area <= 127.0 | 1 | 0.659760 |
| Height <= 3.5 and Lenght > 5.5 and Blackpix > 20.5 and Height <= 2.5 and P_black <= 0.866 | 2 | 0.057631 |
| Lenght > 2.5 and Height <= 27.5 and Height > 4.5 and Wb_trans > 34.5 and Blackpix <= 4418.5 and Wb_trans <= 577.0 | 1 | 0.576355 |
| Lenght <= 2.5 and Eccen > 0.236 | 1 | 0.030303 |
| Lenght <= 2.5 and Area <= 14.0 and Height <= 8.5 | 4 | 0.019541 |
| Height <= 27.5 and Lenght > 2.5 and Eccen <= 6.737 and P_black > 0.1585 and Height <= 19.5 and P_and > 0.386 and Eccen <= 1.9545 and P_black > 0.4675 | 1 | 0.242236 |
| Height <= 4.5 and P_black > 0.238 and Lenght > 7.5 and Wb_trans <= 13.5 and P_and > 0.544 and Eccen > 12.25 and Wb_trans > 2.5 and P_black > 0.425 and P_black > 0.6125 | 2 | 0.029630 |
| Height <= 27.5 and Lenght > 2.5 and Eccen <= 6.737 and P_black > 0.1585 and Eccen > 0.5425 and Eccen <= 2.95 and Blackpix > 8.5 and Wb_trans > 1.5 and Wb_trans > 4.5 and P_black <= 0.388 and Height <= 9.5 | 1 | 0.178571 |
| Height <= 27.5 and Lenght > 2.5 and Eccen > 6.737 and Mean_tr <= 20.2 and Wb_trans > 15.5 and P_and <= 0.6855 | 1 | 0.080000 |
| Eccen > 6.737 and P_and > 0.445 and Wb_trans > 273.5 | 1 | 0.057633 |
| Eccen > 6.857 and Height <= 11.5 and P_and > 0.497 and Mean_tr > 7.5 | 2 | 0.028242 |
| Eccen > 6.857 and Height <= 9.0 and P_and > 0.497 and P_and > 0.972 and Eccen > 10.25 and P_black <= 0.3745 | 2 | 0.028565 |
| Eccen <= 0.236 and Mean_tr <= 10.5 | 4 | 0.020833 |
| P_black <= 0.3245 and Height > 11.5 and P_black <= 0.2025 and Eccen <= 3.9735 and Eccen > 0.6845 | 5 | 0.134557 |
| Height <= 26.5 and P_black <= 0.46799999999999997 and Lenght <= 82.0 and Height <= 3.5 and Area > 33.5 | 1 | 0.096720 |
| Eccen > 6.857 and P_black > 0.307 and P_and > 0.902 and Eccen > 13.5 and Mean_tr > 2.21 | 2 | 0.011427 |
| Eccen > 6.5225 and P_black > 0.33999999999999997 and Eccen > 13.5 and Height <= 2.0 | 2 | 0.017582 |
| Height <= 26.5 and Lenght <= 58.5 and Eccen > 0.345 and P_black <= 0.597 and P_and > 0.3225 and Lenght > 19.5 and P_and > 0.484 | 1 | 0.162723 |
| Height <= 26.5 and Lenght > 3.5 and Lenght <= 58.5 and P_black <= 0.597 and P_black > 0.294 and Eccen <= 1.65 and Mean_tr > 7.335 | 1 | 0.135484 |
| P_black <= 0.3355 and Eccen <= 6.5225 and Eccen > 0.556 and Wb_trans > 1.5 and P_black <= 0.2955 and Height <= 33.5 and Eccen > 3.4645 | 1 | 0.079513 |
| P_black <= 0.3245 and Eccen <= 6.5225 and Mean_tr <= 9.605 and Area <= 35.5 | 1 | 0.069519 |
| P_black <= 0.3245 and Eccen <= 6.5225 and Mean_tr <= 9.605 and Wb_trans > 2.5 and Eccen <= 0.8345 | 5 | 0.071669 |
| Height <= 26.5 and Lenght > 3.5 and Eccen <= 2.9165 and P_black > 0.16949999999999998 and Eccen <= 1.0835 and Wb_trans > 2.5 and P_black <= 0.4065 | 1 | 0.119403 |
| Height <= 26.5 and Lenght > 3.5 and Eccen > 2.9165 and P_black > 0.16749999999999998 and P_and <= 0.907 | 2 | 0.073143 |
| Blackand > 626.5 and P_black <= 0.331 and Area > 13001.5 | 5 | 0.055188 |
| Blackand > 626.5 and P_black > 0.3285 and Height <= 90.0 and Eccen <= 1.3505 | 3 | 0.056250 |
| Height <= 81.0 and Lenght > 2.5 and P_black > 0.597 | 2 | 0.032701 |
| Height <= 81.0 and Lenght > 2.5 and P_black > 0.2605 and Eccen > 1.3090000000000002 and Lenght > 48.5 | 1 | 0.204545 |
| Height > 60.0 | 3 | 0.074746 |
| Lenght > 2.5 and P_and <= 0.8795 and Mean_tr <= 9.5 and Blackand <= 87.5 and P_black > 0.211 and Mean_tr > 3.25 | 1 | 0.069209 |
| Lenght > 2.5 and P_black > 0.40349999999999997 | 1 | 0.316744 |
| Lenght <= 3.0 | 4 | 0.042982 |
| Mean_tr <= 9.5 and Wb_trans <= 2.5 | 5 | 0.184906 |
| Mean_tr <= 6.155 and P_and <= 0.5215000000000001 | 5 | 0.133333 |
| P_black > 0.1325 | 1 | 0.404858 |
|  | 2 | 0.424242 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Height >= 28 and P_black >= 0.338 and Lenght >= 31 and Eccen <= 1.254 and Mean_tr >= 7.05 | 3 | 0.002648 |
| Height >= 28 and Wb_trans >= 1028 and P_black >= 0.339 | 3 | 0.001427 |
| Height >= 28 and P_black >= 0.388 and P_and <= 0.726 and Mean_tr <= 28.77 | 3 | 0.000729 |
| Eccen <= 0.091 and Eccen >= 0.031 | 4 | 0.005777 |
| Eccen <= 0.182 and Height >= 38 | 4 | 0.003103 |
| Lenght <= 2 and Eccen <= 0.182 and Height <= 19 and Height >= 10 | 4 | 0.001657 |
| Lenght <= 2 and P_black >= 0.9 and Height <= 9 and Area >= 9 | 4 | 0.001474 |
| Lenght <= 2 and P_black >= 1 and Height <= 8 and Area >= 8 | 4 | 0.000864 |
| Eccen <= 0.222 and Height <= 9 | 4 | 0.000576 |
| P_and <= 0.555 and Height >= 13 and P_black <= 0.201 and Eccen <= 3.529 and Lenght >= 37 | 5 | 0.007146 |
| P_and <= 0.554 and Eccen <= 2.4 and P_black <= 0.156 and P_and >= 0.338 and Wb_trans <= 29 | 5 | 0.003796 |
| Height >= 31 and P_black <= 0.299 and Eccen <= 3.795 and Mean_tr >= 3.09 | 5 | 0.001691 |
| P_black <= 0.224 and Mean_tr >= 2.02 and Height >= 36 | 5 | 0.001691 |
| Wb_trans <= 9 and P_black <= 0.158 and P_and <= 0.319 and P_and >= 0.238 and Height <= 8 | 5 | 0.001480 |
| P_black <= 0.323 and Eccen <= 0.444 | 5 | 0.001057 |
| Mean_tr >= 9.06 and Height <= 2 and Area >= 41 | 2 | 0.024535 |
| Height <= 3 and Eccen >= 10 and Eccen <= 23 and Mean_tr >= 5.5 | 2 | 0.007577 |
| Height <= 3 and Mean_tr >= 1.5 and Eccen >= 35 and Wb_trans >= 6 | 2 | 0.008020 |
| Mean_tr >= 1.38 and Height <= 1 and Blackpix >= 8 and Mean_tr <= 11.67 and P_black >= 0.632 and Lenght >= 14 | 2 | 0.004026 |
| Mean_tr >= 1.38 and Height <= 2 and Blackpix >= 8 and Eccen <= 9 and P_black >= 0.464 | 2 | 0.003357 |
| Height <= 2 and Mean_tr >= 1.38 and Eccen >= 26 and Blackpix <= 13 | 2 | 0.002241 |
| Height <= 4 and Mean_tr >= 13.5 and Area >= 26 and Eccen <= 131 | 2 | 0.002911 |
| Height <= 2 and P_black <= 0.536 and P_black >= 0.465 | 2 | 0.001793 |
| Wb_trans <= 5 and Eccen >= 11 and Area >= 36 and Eccen <= 36 | 2 | 0.001346 |
| Wb_trans <= 5 and Eccen >= 3.5 and Blackand <= 17 and Lenght >= 13 and P_black <= 0.692 | 2 | 0.000935 |
| Mean_tr >= 31 and Lenght >= 280 and Lenght <= 342 | 2 | 0.001346 |
|  | 1 | 0.985507 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

height|eccen|blackpix|class
---|---|---|---
(6.5-12.5]|(34.9445-66.9375]|(4096.5-10800.5]|1
(89-inf)|(1.3605-6.755]|(10800.5-inf)|3
(2.5-3.5]|(66.9375-inf)|(693.5-4096.5]|1
(3.5-6.5]|(66.9375-inf)|(693.5-4096.5]|1
(26.5-89]|(6.755-34.9445]|(4096.5-10800.5]|1
(89-inf)|(0.5485-1.3605]|(10800.5-inf)|3
(12.5-26.5]|(6.755-34.9445]|(4096.5-10800.5]|1
(12.5-26.5]|(34.9445-66.9375]|(693.5-4096.5]|1
(3.5-6.5]|(34.9445-66.9375]|(693.5-4096.5]|1
(89-inf)|(1.3605-6.755]|(4096.5-10800.5]|5
(6.5-12.5]|(34.9445-66.9375]|(693.5-4096.5]|1
(26.5-89]|(1.3605-6.755]|(4096.5-10800.5]|5
(26.5-89]|(6.755-34.9445]|(693.5-4096.5]|1
(89-inf)|(0.5485-1.3605]|(4096.5-10800.5]|3
(2.5-3.5]|(66.9375-inf)|(478.5-693.5]|2
(-inf-2.5]|(66.9375-inf)|(478.5-693.5]|2
(6.5-12.5]|(6.755-34.9445]|(693.5-4096.5]|1
(12.5-26.5]|(6.755-34.9445]|(693.5-4096.5]|1
(3.5-6.5]|(34.9445-66.9375]|(478.5-693.5]|1
(12.5-26.5]|(1.3605-6.755]|(693.5-4096.5]|1
(6.5-12.5]|(34.9445-66.9375]|(478.5-693.5]|1
(26.5-89]|(1.3605-6.755]|(693.5-4096.5]|1
(2.5-3.5]|(66.9375-inf)|(400.5-478.5]|1
(3.5-6.5]|(6.755-34.9445]|(478.5-693.5]|1
(89-inf)|(0.5485-1.3605]|(693.5-4096.5]|1
(-inf-2.5]|(66.9375-inf)|(400.5-478.5]|2
(26.5-89]|(0.5485-1.3605]|(693.5-4096.5]|3
(26.5-89]|(6.755-34.9445]|(478.5-693.5]|1
(12.5-26.5]|(6.755-34.9445]|(478.5-693.5]|1
(6.5-12.5]|(6.755-34.9445]|(478.5-693.5]|1
(26.5-89]|(1.3605-6.755]|(478.5-693.5]|5
(12.5-26.5]|(1.3605-6.755]|(478.5-693.5]|1
(6.5-12.5]|(1.3605-6.755]|(478.5-693.5]|1
(6.5-12.5]|(34.9445-66.9375]|(400.5-478.5]|1
(3.5-6.5]|(34.9445-66.9375]|(400.5-478.5]|1
(89-inf)|(-inf-0.236]|(693.5-4096.5]|1
(89-inf)|(0.5485-1.3605]|(478.5-693.5]|1
(6.5-12.5]|(66.9375-inf)|(156.5-400.5]|1
(-inf-2.5]|(66.9375-inf)|(156.5-400.5]|2
(2.5-3.5]|(66.9375-inf)|(156.5-400.5]|2
(12.5-26.5]|(6.755-34.9445]|(400.5-478.5]|1
(6.5-12.5]|(6.755-34.9445]|(400.5-478.5]|1
(26.5-89]|(1.3605-6.755]|(400.5-478.5]|1
(6.5-12.5]|(1.3605-6.755]|(400.5-478.5]|1
(26.5-89]|(0.236-0.5485]|(478.5-693.5]|1
(2.5-3.5]|(34.9445-66.9375]|(156.5-400.5]|1
(12.5-26.5]|(1.3605-6.755]|(400.5-478.5]|1
(6.5-12.5]|(34.9445-66.9375]|(156.5-400.5]|1
(3.5-6.5]|(34.9445-66.9375]|(156.5-400.5]|1
(2.5-3.5]|(6.755-34.9445]|(156.5-400.5]|1
(12.5-26.5]|(6.755-34.9445]|(156.5-400.5]|1
(89-inf)|(-inf-0.236]|(478.5-693.5]|1
(26.5-89]|(0.5485-1.3605]|(400.5-478.5]|3
(-inf-2.5]|(66.9375-inf)|(42.5-156.5]|2
(3.5-6.5]|(6.755-34.9445]|(156.5-400.5]|1
(6.5-12.5]|(6.755-34.9445]|(156.5-400.5]|1
(89-inf)|(0.236-0.5485]|(400.5-478.5]|1
(6.5-12.5]|(34.9445-66.9375]|(42.5-156.5]|1
(-inf-2.5]|(34.9445-66.9375]|(42.5-156.5]|2
(26.5-89]|(1.3605-6.755]|(156.5-400.5]|5
(2.5-3.5]|(34.9445-66.9375]|(42.5-156.5]|2
(12.5-26.5]|(1.3605-6.755]|(156.5-400.5]|1
(6.5-12.5]|(1.3605-6.755]|(156.5-400.5]|1
(89-inf)|(-inf-0.236]|(400.5-478.5]|1
(26.5-89]|(0.5485-1.3605]|(156.5-400.5]|5
(12.5-26.5]|(0.5485-1.3605]|(156.5-400.5]|1
(2.5-3.5]|(6.755-34.9445]|(42.5-156.5]|1
(-inf-2.5]|(6.755-34.9445]|(42.5-156.5]|2
(-inf-2.5]|(66.9375-inf)|(17.5-42.5]|1
(6.5-12.5]|(6.755-34.9445]|(42.5-156.5]|1
(3.5-6.5]|(6.755-34.9445]|(42.5-156.5]|1
(26.5-89]|(0.236-0.5485]|(156.5-400.5]|5
(-inf-2.5]|(34.9445-66.9375]|(17.5-42.5]|2
(12.5-26.5]|(1.3605-6.755]|(42.5-156.5]|1
(3.5-6.5]|(1.3605-6.755]|(42.5-156.5]|1
(6.5-12.5]|(1.3605-6.755]|(42.5-156.5]|1
(3.5-6.5]|(66.9375-inf)|(-inf-17.5]|1
(2.5-3.5]|(6.755-34.9445]|(17.5-42.5]|1
(-inf-2.5]|(66.9375-inf)|(-inf-17.5]|1
(6.5-12.5]|(6.755-34.9445]|(17.5-42.5]|1
(3.5-6.5]|(6.755-34.9445]|(17.5-42.5]|1
(-inf-2.5]|(6.755-34.9445]|(17.5-42.5]|2
(6.5-12.5]|(0.5485-1.3605]|(42.5-156.5]|1
(12.5-26.5]|(0.5485-1.3605]|(42.5-156.5]|1
(26.5-89]|(0.236-0.5485]|(42.5-156.5]|1
(2.5-3.5]|(1.3605-6.755]|(17.5-42.5]|1
(-inf-2.5]|(34.9445-66.9375]|(-inf-17.5]|1
(3.5-6.5]|(1.3605-6.755]|(17.5-42.5]|1
(6.5-12.5]|(1.3605-6.755]|(17.5-42.5]|1
(89-inf)|(-inf-0.236]|(42.5-156.5]|4
(26.5-89]|(-inf-0.236]|(42.5-156.5]|4
(12.5-26.5]|(0.5485-1.3605]|(17.5-42.5]|5
(2.5-3.5]|(6.755-34.9445]|(-inf-17.5]|1
(3.5-6.5]|(0.5485-1.3605]|(17.5-42.5]|1
(-inf-2.5]|(6.755-34.9445]|(-inf-17.5]|2
(6.5-12.5]|(0.5485-1.3605]|(17.5-42.5]|1
(6.5-12.5]|(0.236-0.5485]|(17.5-42.5]|1
(6.5-12.5]|(1.3605-6.755]|(-inf-17.5]|1
(12.5-26.5]|(0.236-0.5485]|(17.5-42.5]|1
(-inf-2.5]|(1.3605-6.755]|(-inf-17.5]|1
(2.5-3.5]|(1.3605-6.755]|(-inf-17.5]|1
(3.5-6.5]|(1.3605-6.755]|(-inf-17.5]|1
(12.5-26.5]|(0.5485-1.3605]|(-inf-17.5]|1
(26.5-89]|(-inf-0.236]|(17.5-42.5]|4
(12.5-26.5]|(-inf-0.236]|(17.5-42.5]|4
(2.5-3.5]|(0.5485-1.3605]|(-inf-17.5]|1
(6.5-12.5]|(0.5485-1.3605]|(-inf-17.5]|1
(3.5-6.5]|(0.5485-1.3605]|(-inf-17.5]|1
(12.5-26.5]|(0.236-0.5485]|(-inf-17.5]|5
(3.5-6.5]|(0.236-0.5485]|(-inf-17.5]|1
(6.5-12.5]|(0.236-0.5485]|(-inf-17.5]|1
(12.5-26.5]|(-inf-0.236]|(-inf-17.5]|4
(6.5-12.5]|(-inf-0.236]|(-inf-17.5]|4

## JRip

Decision list:

rules | predicted class
---|---
(Height >= 28) and (P_black >= 0.338) and (Lenght >= 31) and (Eccen <= 1.254) and (Mean_tr >= 7.05)|3 (13.0/0.0)
(Height >= 28) and (Wb_trans >= 1028) and (P_black >= 0.339)|3 (7.0/0.0)
(Height >= 28) and (P_black >= 0.388) and (P_and <= 0.726) and (Mean_tr <= 28.77)|3 (7.0/2.0)
(Eccen <= 0.091) and (Eccen >= 0.031)|4 (27.0/0.0)
(Eccen <= 0.182) and (Height >= 38)|4 (15.0/0.0)
(Lenght <= 2) and (Eccen <= 0.182) and (Height <= 19) and (Height >= 10)|4 (8.0/0.0)
(Lenght <= 2) and (P_black >= 0.9) and (Height <= 9) and (Area >= 9)|4 (9.0/1.0)
(Lenght <= 2) and (P_black >= 1) and (Height <= 8) and (Area >= 8)|4 (6.0/1.0)
(Eccen <= 0.222) and (Height <= 9)|4 (7.0/2.0)
(P_and <= 0.555) and (Height >= 13) and (P_black <= 0.201) and (Eccen <= 3.529) and (Lenght >= 37)|5 (34.0/0.0)
(P_and <= 0.554) and (Eccen <= 2.4) and (P_black <= 0.156) and (P_and >= 0.338) and (Wb_trans <= 29)|5 (18.0/0.0)
(Height >= 31) and (P_black <= 0.299) and (Eccen <= 3.795) and (Mean_tr >= 3.09)|5 (8.0/0.0)
(P_black <= 0.224) and (Mean_tr >= 2.02) and (Height >= 36)|5 (8.0/0.0)
(Wb_trans <= 9) and (P_black <= 0.158) and (P_and <= 0.319) and (P_and >= 0.238) and (Height <= 8)|5 (7.0/0.0)
(P_black <= 0.323) and (Eccen <= 0.444)|5 (5.0/0.0)
(Mean_tr >= 9.06) and (Height <= 2) and (Area >= 41)|2 (112.0/0.0)
(Height <= 3) and (Eccen >= 10) and (Eccen <= 23) and (Mean_tr >= 5.5)|2 (34.0/0.0)
(Height <= 3) and (Mean_tr >= 1.5) and (Eccen >= 35) and (Wb_trans >= 6)|2 (36.0/0.0)
(Mean_tr >= 1.38) and (Height <= 1) and (Blackpix >= 8) and (Mean_tr <= 11.67) and (P_black >= 0.632) and (Lenght >= 14)|2 (18.0/0.0)
(Mean_tr >= 1.38) and (Height <= 2) and (Blackpix >= 8) and (Eccen <= 9) and (P_black >= 0.464)|2 (15.0/0.0)
(Height <= 2) and (Mean_tr >= 1.38) and (Eccen >= 26) and (Blackpix <= 13)|2 (10.0/0.0)
(Height <= 4) and (Mean_tr >= 13.5) and (Area >= 26) and (Eccen <= 131)|2 (13.0/0.0)
(Height <= 2) and (P_black <= 0.536) and (P_black >= 0.465)|2 (8.0/0.0)
(Wb_trans <= 5) and (Eccen >= 11) and (Area >= 36) and (Eccen <= 36)|2 (6.0/0.0)
(Wb_trans <= 5) and (Eccen >= 3.5) and (Blackand <= 17) and (Lenght >= 13) and (P_black <= 0.692)|2 (6.0/1.0)
(Mean_tr >= 31) and (Lenght >= 280) and (Lenght <= 342)|2 (6.0/0.0)
|1 (4479.0/63.0)


## PART

Decision list:

rules | predicted class
---|---
Height > 3.5 AND Eccen > 0.236 AND Height <= 27.5 AND Blackpix > 14.5 AND Mean_tr <= 21.645 AND P_and > 0.5195000000000001 AND P_black > 0.1565 AND Mean_tr <= 16.77 AND Height <= 24.5 AND P_and > 0.5834999999999999 AND Blackand > 89.5|1 (3058.0)
Height <= 3.5 AND Mean_tr <= 1.355 AND P_black <= 0.3855|1 (38.0)
Height <= 3.5 AND Lenght > 5.5 AND Mean_tr > 7.25 AND Eccen > 40.5 AND Blackpix <= 593.0|2 (105.0)
Eccen <= 0.236 AND Mean_tr > 9.5 AND Eccen <= 0.093 AND Eccen > 0.028999999999999998|4 (24.0)
Height <= 2.5 AND Blackpix > 7.5 AND P_black > 0.445 AND Area <= 40.5 AND Blackpix <= 24.5 AND Mean_tr > 5.125|2 (42.0)
Eccen <= 0.236 AND Height > 37.5|4 (19.0)
Height > 3.5 AND Eccen > 0.236 AND Height <= 27.5 AND Blackpix > 9.5 AND Mean_tr <= 30.5 AND P_black > 0.1585 AND Eccen > 0.6755 AND P_and > 0.4455 AND Mean_tr <= 9.7 AND Wb_trans <= 563.5 AND P_black > 0.2085 AND Area <= 127.0|1 (605.0)
Height <= 3.5 AND Lenght > 5.5 AND Blackpix > 20.5 AND Height <= 2.5 AND P_black <= 0.866|2 (54.0)
Lenght > 2.5 AND Height <= 27.5 AND Height > 4.5 AND Wb_trans > 34.5 AND Blackpix <= 4418.5 AND Wb_trans <= 577.0|1 (351.0)
Lenght <= 2.5 AND Eccen > 0.236|1 (18.0/6.0)
Lenght <= 2.5 AND Area <= 14.0 AND Height <= 8.5|4 (11.0/3.0)
Height <= 27.5 AND Lenght > 2.5 AND Eccen <= 6.737 AND P_black > 0.1585 AND Height <= 19.5 AND P_and > 0.386 AND Eccen <= 1.9545 AND P_black > 0.4675|1 (78.0)
Height <= 4.5 AND P_black > 0.238 AND Lenght > 7.5 AND Wb_trans <= 13.5 AND P_and > 0.544 AND Eccen > 12.25 AND Wb_trans > 2.5 AND P_black > 0.425 AND P_black > 0.6125|2 (15.0/1.0)
Height <= 27.5 AND Lenght > 2.5 AND Eccen <= 6.737 AND P_black > 0.1585 AND Eccen > 0.5425 AND Eccen <= 2.95 AND Blackpix > 8.5 AND Wb_trans > 1.5 AND Wb_trans > 4.5 AND P_black <= 0.388 AND Height <= 9.5|1 (50.0)
Height <= 27.5 AND Lenght > 2.5 AND Eccen > 6.737 AND Mean_tr <= 20.2 AND Wb_trans > 15.5 AND P_and <= 0.6855|1 (20.0)
Eccen > 6.737 AND P_and > 0.445 AND Wb_trans > 273.5|1 (16.0/1.0)
Eccen > 6.857 AND Height <= 11.5 AND P_and > 0.497 AND Mean_tr > 7.5|2 (16.0/3.0)
Eccen > 6.857 AND Height <= 9.0 AND P_and > 0.497 AND P_and > 0.972 AND Eccen > 10.25 AND P_black <= 0.3745|2 (12.0/1.0)
Eccen <= 0.236 AND Mean_tr <= 10.5|4 (15.0/3.0)
P_black <= 0.3245 AND Height > 11.5 AND P_black <= 0.2025 AND Eccen <= 3.9735 AND Eccen > 0.6845|5 (44.0)
Height <= 26.5 AND P_black <= 0.46799999999999997 AND Lenght <= 82.0 AND Height <= 3.5 AND Area > 33.5|1 (17.0/1.0)
Eccen > 6.857 AND P_black > 0.307 AND P_and > 0.902 AND Eccen > 13.5 AND Mean_tr > 2.21|2 (13.0/6.0)
Eccen > 6.5225 AND P_black > 0.33999999999999997 AND Eccen > 13.5 AND Height <= 2.0|2 (10.0/1.0)
Height <= 26.5 AND Lenght <= 58.5 AND Eccen > 0.345 AND P_black <= 0.597 AND P_and > 0.3225 AND Lenght > 19.5 AND P_and > 0.484|1 (24.0)
Height <= 26.5 AND Lenght > 3.5 AND Lenght <= 58.5 AND P_black <= 0.597 AND P_black > 0.294 AND Eccen <= 1.65 AND Mean_tr > 7.335|1 (21.0)
P_black <= 0.3355 AND Eccen <= 6.5225 AND Eccen > 0.556 AND Wb_trans > 1.5 AND P_black <= 0.2955 AND Height <= 33.5 AND Eccen > 3.4645|1 (17.0/3.0)
P_black <= 0.3245 AND Eccen <= 6.5225 AND Mean_tr <= 9.605 AND Area <= 35.5|1 (17.0/4.0)
P_black <= 0.3245 AND Eccen <= 6.5225 AND Mean_tr <= 9.605 AND Wb_trans > 2.5 AND Eccen <= 0.8345|5 (17.0/3.0)
Height <= 26.5 AND Lenght > 3.5 AND Eccen <= 2.9165 AND P_black > 0.16949999999999998 AND Eccen <= 1.0835 AND Wb_trans > 2.5 AND P_black <= 0.4065|1 (15.0)
Height <= 26.5 AND Lenght > 3.5 AND Eccen > 2.9165 AND P_black > 0.16749999999999998 AND P_and <= 0.907|2 (15.0)
Blackand > 626.5 AND P_black <= 0.331 AND Area > 13001.5|5 (12.0/2.0)
Blackand > 626.5 AND P_black > 0.3285 AND Height <= 90.0 AND Eccen <= 1.3505|3 (16.0/4.0)
Height <= 81.0 AND Lenght > 2.5 AND P_black > 0.597|2 (18.0/8.0)
Height <= 81.0 AND Lenght > 2.5 AND P_black > 0.2605 AND Eccen > 1.3090000000000002 AND Lenght > 48.5|1 (14.0)
Height > 60.0|3 (13.0)
Lenght > 2.5 AND P_and <= 0.8795 AND Mean_tr <= 9.5 AND Blackand <= 87.5 AND P_black > 0.211 AND Mean_tr > 3.25|1 (12.0/5.0)
Lenght > 2.5 AND P_black > 0.40349999999999997|1 (16.0)
Lenght <= 3.0|4 (10.0/3.0)
Mean_tr <= 9.5 AND Wb_trans <= 2.5|5 (10.0/1.0)
Mean_tr <= 6.155 AND P_and <= 0.5215000000000001|5 (19.0/8.0)
P_black > 0.1325|1 (15.0/6.0)
|2 (10.0/5.0)


