# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 1 | 0.898557 |
| Height <= 3.5 and Lenght > 5.5 and P_black > 0.2285 and Eccen > 9.5 and Mean_tr > 1.275 | 2 | 0.045568 |
| Height > 3.5 and Eccen <= 0.2085 | 4 | 0.013376 |
| Height > 3.5 and Eccen > 0.2085 and Height > 27.5 and P_black <= 0.3315 | 5 | 0.007579 |
| Height > 3.5 and Eccen > 0.2085 and Height <= 27.5 and Mean_tr <= 15.855 and P_black <= 0.1575 and Eccen <= 3.6145 | 5 | 0.003510 |
| Height > 3.5 and Eccen > 0.2085 and Height <= 27.5 and Mean_tr > 15.855 and Eccen > 17.565 | 2 | 0.003889 |
| Height <= 3.5 and Lenght > 5.5 and P_black > 0.2285 and Eccen <= 9.5 and P_black > 0.643 | 2 | 0.002350 |
| Height > 3.5 and Eccen > 0.2085 and Height > 27.5 and P_black > 0.3315 and Eccen <= 1.238 | 3 | 0.003143 |
| Height <= 2.5 and Blackand > 76.5 and Blackand <= 638.5 and Wb_trans > 30.5 and Wb_trans <= 837 | 2 | 0.000541 |
| Height > 90 and Blackand > 23196.5 and Wb_trans > 837 | 3 | 0.001428 |
| Height <= 2.5 and Blackand > 14.5 and Blackand <= 37.5 and Wb_trans > 1.5 and Wb_trans <= 5.5 | 2 | 0.005442 |
| Height <= 2.5 and Blackand > 14.5 and Blackand <= 37.5 and Wb_trans <= 1.5 | 2 | 0.004343 |
| Height > 4.5 and Height <= 6.5 and Blackand > 37.5 and Blackand <= 76.5 and Wb_trans <= 1.5 | 2 | 0.000288 |
| Height > 12.5 and Height <= 26.5 and Blackand > 37.5 and Blackand <= 76.5 and Wb_trans > 7.5 and Wb_trans <= 30.5 | 5 | 0.000415 |
| Height <= 2.5 and Blackand > 76.5 and Blackand <= 638.5 and Wb_trans > 1.5 and Wb_trans <= 5.5 | 2 | 0.005593 |
| Height > 3.5 and Height <= 4.5 and Blackand > 14.5 and Blackand <= 37.5 and Wb_trans <= 1.5 | 2 | 0.000108 |
| Height <= 2.5 and Blackand <= 14.5 and Wb_trans <= 1.5 | 2 | 0.004641 |
| Height <= 2.5 and Blackand > 37.5 and Blackand <= 76.5 and Wb_trans > 1.5 and Wb_trans <= 5.5 | 2 | 0.005441 |
| Height > 2.5 and Height <= 3.5 and Blackand > 14.5 and Blackand <= 37.5 and Wb_trans > 1.5 and Wb_trans <= 5.5 | 2 | 0.000108 |
| Height > 6.5 and Height <= 12.5 and Blackand <= 14.5 and Wb_trans <= 1.5 | 4 | 0.004327 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Height > 3.5 and Eccen > 0.236 and Height <= 27.5 and Mean_tr <= 21.295 and Blackpix > 14.5 and P_and > 0.5195 and P_black > 0.1565 and Mean_tr <= 16.855 and Height <= 24.5 and P_and > 0.5835 and Blackand > 89.5 | 1 | 0.859555 |
| Height <= 3.5 and Mean_tr <= 1.355 and P_black <= 0.4075 | 1 | 0.079336 |
| Height <= 3.5 and Lenght > 7.5 and Mean_tr > 9.975 and Blackpix <= 618.5 and Area > 40.5 | 2 | 0.072340 |
| Eccen <= 0.236 and Blackpix > 7.5 and Mean_tr > 9.5 and Area <= 35.5 | 4 | 0.018127 |
| Height <= 2.5 and Blackpix > 7.5 and P_black > 0.445 and P_black <= 0.5895 | 2 | 0.016437 |
| Height <= 2.5 and Blackpix > 7.5 and P_black > 0.5935 and P_black <= 0.767 | 2 | 0.019016 |
| Eccen <= 0.2085 and Blackpix > 7.5 and Eccen <= 0.108 and Height > 38.5 | 4 | 0.010705 |
| Height <= 2.5 and Blackpix > 7.5 and P_black > 0.803 and P_black > 0.8985 and Lenght <= 23.5 and Lenght > 9.5 | 2 | 0.014000 |
| Height <= 27.5 and Height > 2.5 and Eccen > 0.199 and Mean_tr <= 30.135 and Blackpix > 11.5 and P_and > 0.5225 and Eccen > 0.62 and Blackand <= 3994 and Blackand > 24.5 and Wb_trans > 4.5 and P_black > 0.2085 and Area <= 124 | 1 | 0.695755 |
| Height <= 27.5 and Lenght > 2.5 and Height > 2.5 and Mean_tr <= 30.135 and Wb_trans > 34.5 and Blackpix <= 4356.5 and Wb_trans <= 577 | 1 | 0.578431 |
| Eccen > 6.737 and Wb_trans > 273.5 and P_black > 0.2165 | 1 | 0.071942 |
| Eccen > 6.393 and Area <= 9009 and P_black > 0.1885 and Mean_tr > 25.5 and Lenght <= 341.5 | 2 | 0.031955 |
| Eccen > 6.737 and P_black > 0.1885 and Eccen > 13.5 and P_black > 0.2725 and Wb_trans <= 23.5 and Area > 17.5 and P_black > 0.693 and P_black <= 0.8535 | 2 | 0.022770 |
| Eccen > 6.737 and P_black > 0.1885 and P_black <= 0.2725 and Height <= 1.5 | 2 | 0.011516 |
| Eccen > 6.737 and P_black > 0.201 and Lenght > 50.5 and P_black <= 0.53 | 2 | 0.024621 |
| Eccen <= 0.2085 and Eccen > 0.108 and Blackpix > 7.5 and Eccen > 0.12 | 4 | 0.011765 |
| Eccen > 6.9 and Mean_tr <= 1.555 | 1 | 0.051643 |
| Eccen > 6.9 and P_black > 0.143 and P_and <= 0.7615 | 1 | 0.028107 |
| Eccen > 6.9 and P_black > 0.1895 and Mean_tr > 7.25 and P_black <= 0.8985 | 2 | 0.022044 |
| Area <= 462 and Eccen > 0.1965 and Eccen <= 6.9 and Lenght > 2.5 and P_black > 0.1595 and P_and > 0.387 and Eccen > 2.0625 and Area > 38 and P_and > 0.4735 | 1 | 0.187234 |
| Area <= 462 and Eccen > 0.1965 and Eccen <= 6.9 and Lenght > 2.5 and P_black > 0.21 and Eccen <= 1.9615 and P_black > 0.4675 | 1 | 0.300366 |
| Height <= 11.5 and Lenght > 2.5 and Eccen <= 6.9 and P_and > 0.3155 and Blackpix > 9.5 and Height > 4.5 and P_and > 0.601 and Blackand <= 87.5 and Mean_tr <= 6.75 and P_and <= 0.976 | 1 | 0.143498 |
| P_black <= 0.3515 and Height > 11.5 and Mean_tr <= 10.565 and P_black <= 0.214 and Eccen > 0.4845 and Eccen <= 3.345 and Lenght > 18.5 | 5 | 0.127796 |
| Eccen <= 0.1965 and Height <= 14.5 and Height > 8.5 | 4 | 0.022433 |
| Eccen > 6.9 and Height <= 11.5 and Area <= 8.5 | 2 | 0.018970 |
| Blackand <= 626.5 and Lenght > 2.5 and Eccen <= 8.75 and Height > 11.5 and Blackpix > 30.5 and P_black <= 0.268 | 5 | 0.015326 |
| Blackand <= 626.5 and Lenght > 2.5 and Eccen <= 8.75 and P_black > 0.1595 and P_and > 0.386 and Eccen <= 1.9545 and Mean_tr > 9.5 and Height > 7.5 | 1 | 0.071429 |
| Blackand <= 626.5 and Lenght > 2.5 and Eccen > 8.75 and Lenght <= 123 and P_black <= 0.425 and Eccen > 20.5 | 2 | 0.018977 |
| Blackand <= 626.5 and Eccen <= 0.1965 and Height > 7.5 | 4 | 0.005735 |
| Height <= 26.5 and Lenght <= 2.5 and P_black > 0.866 | 4 | 0.015685 |
| Height <= 26.5 and Eccen <= 8.854 and Lenght <= 2.5 and P_and <= 0.757 | 1 | 0.020050 |
| Height <= 26.5 and Height <= 3.5 and Eccen <= 17.5 and Eccen <= 12.25 and Eccen > 8.75 | 1 | 0.024366 |
| Height <= 26.5 and Eccen <= 3.4645 and P_black > 0.1595 and Mean_tr > 9.5 and Area <= 33 | 1 | 0.050420 |
| Height <= 26.5 and Height <= 3.5 and Area > 17.5 and Area <= 28 | 1 | 0.050420 |
| Height <= 26.5 and Eccen > 12.3335 and Eccen <= 23.417 | 2 | 0.030555 |
| Blackand <= 626.5 and P_and > 0.3155 and Height > 11.5 and Blackpix <= 26.5 | 5 | 0.033654 |
| Blackand <= 626.5 and P_and > 0.3155 and Height > 4.5 and P_and > 0.606 and P_and > 0.776 and Lenght <= 4.5 | 1 | 0.173899 |
| Blackand <= 626.5 and P_and > 0.3155 and Wb_trans > 7.5 and Area > 130 and Lenght <= 38.5 | 1 | 0.198347 |
| P_black <= 0.358 and Height <= 82.5 and Eccen <= 6.4285 and P_black > 0.277 and Height > 4.5 | 1 | 0.163793 |
| P_black > 0.3545 and Height > 26 and Height <= 90 and Eccen > 1.3505 | 1 | 0.085763 |
| Blackand <= 626.5 and Eccen <= 3.4645 and Wb_trans > 1.5 and Blackand <= 79 and Wb_trans <= 3.5 and P_black <= 0.355 | 5 | 0.067843 |
| Blackand <= 626.5 and Blackpix <= 50.5 and Eccen > 3.4645 and Blackand > 32.5 | 1 | 0.096955 |
| Blackand <= 626.5 and P_and > 0.3155 and Area <= 28.5 and P_black <= 0.4275 | 1 | 0.074468 |
| P_black <= 0.3315 and Blackpix <= 2103.5 and P_and > 0.2635 and Mean_tr <= 2.985 and P_and <= 0.4575 | 1 | 0.078337 |
| P_black <= 0.3315 and Height > 34.5 and Eccen > 2.986 | 5 | 0.075472 |
| Blackand <= 626.5 and Wb_trans <= 11 and Eccen <= 3.25 and Wb_trans > 3.5 and Eccen <= 1.775 and Blackand <= 42.5 | 1 | 0.054324 |
| Blackand <= 626.5 and Wb_trans <= 11 and Mean_tr <= 2.835 and Blackand <= 44.5 | 1 | 0.017778 |
| Blackand <= 626.5 and Eccen > 3.5835 | 2 | 0.075789 |
| Height <= 26 and P_and <= 0.87 and P_and <= 0.6875 and Height > 6.5 and Eccen > 1.159 | 1 | 0.035714 |
| Height <= 26 and Lenght > 5.5 and P_and > 0.772 | 1 | 0.122470 |
| Lenght > 30.5 and P_black > 0.306 and Height > 90 | 3 | 0.162162 |
| P_black > 0.4005 and Blackpix > 412.5 and Blackpix <= 445.5 | 3 | 0.101449 |
| Height <= 28.5 and Lenght > 5.5 and Height <= 9.5 | 2 | 0.031915 |
| Eccen > 0.657 and Height <= 28.5 | 1 | 0.174825 |
| P_black <= 0.338 and Height <= 50 | 5 | 0.475626 |
| P_black > 0.338 | 3 | 0.125000 |
|  | 5 | 0.454545 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Height >= 28 and P_black >= 0.339 and Lenght >= 31 and Eccen <= 1.141 and Mean_tr >= 4.25 | 3 | 0.002852 |
| Eccen <= 0.091 and Eccen >= 0.029 | 4 | 0.005358 |
| Eccen <= 0.222 and Height >= 38 | 4 | 0.003304 |
| Lenght <= 2 and Eccen <= 0.222 and Height <= 19 and Area >= 10 | 4 | 0.002067 |
| Lenght <= 2 and P_black >= 0.875 and Height <= 7 | 4 | 0.001267 |
| Eccen <= 0.286 and Area <= 9 and P_black >= 1 and Height >= 9 | 4 | 0.001267 |
| P_and <= 0.555 and Height >= 13 and P_black <= 0.201 and Eccen <= 3.337 and Lenght >= 37 | 5 | 0.007123 |
| P_and <= 0.554 and Eccen <= 2.4 and P_black <= 0.156 and P_and >= 0.338 and Wb_trans <= 29 | 5 | 0.003574 |
| Height >= 31 and P_black <= 0.299 and Mean_tr >= 3.09 and Mean_tr <= 5.69 | 5 | 0.001896 |
| P_and <= 0.6 and Eccen <= 2 and P_black <= 0.275 and Lenght <= 9 | 5 | 0.001068 |
| Height >= 34 and P_black <= 0.299 | 5 | 0.001005 |
| Mean_tr >= 9.06 and Height <= 2 and Area >= 41 | 2 | 0.023403 |
| Height <= 3 and Mean_tr >= 1.38 and Eccen >= 10 and P_black >= 0.616 and P_black <= 0.765 | 2 | 0.004903 |
| Height <= 3 and Eccen >= 10 and Eccen <= 23 and Mean_tr >= 5.5 | 2 | 0.006895 |
| Height <= 3 and Mean_tr >= 1.38 and Eccen >= 35 and Wb_trans >= 6 | 2 | 0.006674 |
| Height <= 2 and Mean_tr >= 1.38 and Blackpix >= 17 and P_black <= 0.897 | 2 | 0.004015 |
| Height <= 2 and P_black >= 0.407 and Lenght >= 14 and Lenght <= 20 | 2 | 0.002235 |
| Height <= 4 and Mean_tr >= 13.5 and Area >= 26 and Eccen <= 131 | 2 | 0.003126 |
| Height <= 2 and Mean_tr >= 1.4 and Lenght <= 9 and Blackpix >= 8 and Eccen <= 8 | 2 | 0.001789 |
| Height <= 2 and Mean_tr >= 1.4 and Wb_trans >= 5 and Eccen >= 27 and Blackpix <= 13 | 2 | 0.001789 |
| Mean_tr >= 30.27 and Eccen >= 6.5 and Lenght <= 342 | 2 | 0.002903 |
|  | 1 | 0.982222 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

height|blackand|wb_trans|class
---|---|---|---
(90-inf)|(23196.5-inf)|(837-inf)|3
(90-inf)|(12099.5-23196.5]|(837-inf)|5
(26.5-90]|(12099.5-23196.5]|(837-inf)|5
(12.5-26.5]|(4884.5-12099.5]|(837-inf)|1
(90-inf)|(4884.5-12099.5]|(837-inf)|3
(26.5-90]|(4884.5-12099.5]|(837-inf)|1
(90-inf)|(12099.5-23196.5]|(30.5-837]|3
(26.5-90]|(12099.5-23196.5]|(30.5-837]|1
(90-inf)|(4884.5-12099.5]|(30.5-837]|5
(26.5-90]|(4884.5-12099.5]|(30.5-837]|1
(6.5-12.5]|(4884.5-12099.5]|(30.5-837]|1
(12.5-26.5]|(4884.5-12099.5]|(30.5-837]|1
(-inf-2.5]|(673.5-4884.5]|(30.5-837]|1
(90-inf)|(673.5-4884.5]|(30.5-837]|4
(26.5-90]|(673.5-4884.5]|(30.5-837]|5
(4.5-6.5]|(673.5-4884.5]|(30.5-837]|1
(12.5-26.5]|(673.5-4884.5]|(30.5-837]|1
(6.5-12.5]|(673.5-4884.5]|(30.5-837]|1
(3.5-4.5]|(638.5-673.5]|(30.5-837]|1
(2.5-3.5]|(638.5-673.5]|(30.5-837]|2
(26.5-90]|(638.5-673.5]|(30.5-837]|3
(12.5-26.5]|(638.5-673.5]|(30.5-837]|1
(6.5-12.5]|(638.5-673.5]|(30.5-837]|1
(6.5-12.5]|(673.5-4884.5]|(7.5-30.5]|2
(3.5-4.5]|(673.5-4884.5]|(7.5-30.5]|1
(2.5-3.5]|(76.5-638.5]|(30.5-837]|1
(2.5-3.5]|(673.5-4884.5]|(7.5-30.5]|1
(90-inf)|(76.5-638.5]|(30.5-837]|1
(4.5-6.5]|(673.5-4884.5]|(7.5-30.5]|1
(12.5-26.5]|(673.5-4884.5]|(7.5-30.5]|1
(-inf-2.5]|(673.5-4884.5]|(7.5-30.5]|2
(26.5-90]|(76.5-638.5]|(30.5-837]|5
(-inf-2.5]|(76.5-638.5]|(30.5-837]|2
(3.5-4.5]|(76.5-638.5]|(30.5-837]|1
(26.5-90]|(673.5-4884.5]|(7.5-30.5]|3
(12.5-26.5]|(76.5-638.5]|(30.5-837]|1
(4.5-6.5]|(76.5-638.5]|(30.5-837]|1
(6.5-12.5]|(76.5-638.5]|(30.5-837]|1
(2.5-3.5]|(638.5-673.5]|(7.5-30.5]|1
(-inf-2.5]|(638.5-673.5]|(7.5-30.5]|2
(26.5-90]|(673.5-4884.5]|(5.5-7.5]|1
(4.5-6.5]|(673.5-4884.5]|(5.5-7.5]|1
(90-inf)|(76.5-638.5]|(7.5-30.5]|1
(2.5-3.5]|(76.5-638.5]|(7.5-30.5]|2
(26.5-90]|(76.5-638.5]|(7.5-30.5]|5
(3.5-4.5]|(76.5-638.5]|(7.5-30.5]|1
(-inf-2.5]|(76.5-638.5]|(7.5-30.5]|2
(4.5-6.5]|(76.5-638.5]|(7.5-30.5]|1
(12.5-26.5]|(76.5-638.5]|(7.5-30.5]|1
(6.5-12.5]|(76.5-638.5]|(7.5-30.5]|1
(26.5-90]|(37.5-76.5]|(7.5-30.5]|1
(12.5-26.5]|(37.5-76.5]|(7.5-30.5]|5
(2.5-3.5]|(37.5-76.5]|(7.5-30.5]|1
(-inf-2.5]|(37.5-76.5]|(7.5-30.5]|1
(3.5-4.5]|(37.5-76.5]|(7.5-30.5]|1
(6.5-12.5]|(37.5-76.5]|(7.5-30.5]|1
(4.5-6.5]|(37.5-76.5]|(7.5-30.5]|1
(4.5-6.5]|(673.5-4884.5]|(1.5-5.5]|1
(2.5-3.5]|(76.5-638.5]|(5.5-7.5]|1
(2.5-3.5]|(673.5-4884.5]|(1.5-5.5]|1
(3.5-4.5]|(76.5-638.5]|(5.5-7.5]|2
(3.5-4.5]|(14.5-37.5]|(7.5-30.5]|1
(-inf-2.5]|(76.5-638.5]|(5.5-7.5]|2
(-inf-2.5]|(14.5-37.5]|(7.5-30.5]|1
(6.5-12.5]|(14.5-37.5]|(7.5-30.5]|1
(4.5-6.5]|(76.5-638.5]|(5.5-7.5]|1
(4.5-6.5]|(14.5-37.5]|(7.5-30.5]|1
(6.5-12.5]|(76.5-638.5]|(5.5-7.5]|1
(12.5-26.5]|(76.5-638.5]|(5.5-7.5]|1
(6.5-12.5]|(4884.5-12099.5]|(-inf-1.5]|1
(12.5-26.5]|(37.5-76.5]|(5.5-7.5]|1
(-inf-2.5]|(37.5-76.5]|(5.5-7.5]|2
(3.5-4.5]|(37.5-76.5]|(5.5-7.5]|1
(6.5-12.5]|(37.5-76.5]|(5.5-7.5]|1
(4.5-6.5]|(37.5-76.5]|(5.5-7.5]|1
(12.5-26.5]|(76.5-638.5]|(1.5-5.5]|1
(4.5-6.5]|(76.5-638.5]|(1.5-5.5]|2
(2.5-3.5]|(76.5-638.5]|(1.5-5.5]|2
(6.5-12.5]|(76.5-638.5]|(1.5-5.5]|1
(6.5-12.5]|(14.5-37.5]|(5.5-7.5]|1
(-inf-2.5]|(76.5-638.5]|(1.5-5.5]|2
(2.5-3.5]|(14.5-37.5]|(5.5-7.5]|1
(-inf-2.5]|(14.5-37.5]|(5.5-7.5]|2
(3.5-4.5]|(14.5-37.5]|(5.5-7.5]|1
(4.5-6.5]|(14.5-37.5]|(5.5-7.5]|1
(4.5-6.5]|(37.5-76.5]|(1.5-5.5]|1
(3.5-4.5]|(37.5-76.5]|(1.5-5.5]|1
(-inf-2.5]|(37.5-76.5]|(1.5-5.5]|2
(6.5-12.5]|(37.5-76.5]|(1.5-5.5]|1
(2.5-3.5]|(76.5-638.5]|(-inf-1.5]|1
(12.5-26.5]|(76.5-638.5]|(-inf-1.5]|1
(12.5-26.5]|(14.5-37.5]|(1.5-5.5]|1
(90-inf)|(76.5-638.5]|(-inf-1.5]|4
(-inf-2.5]|(76.5-638.5]|(-inf-1.5]|2
(3.5-4.5]|(14.5-37.5]|(1.5-5.5]|1
(2.5-3.5]|(14.5-37.5]|(1.5-5.5]|2
(6.5-12.5]|(14.5-37.5]|(1.5-5.5]|1
(4.5-6.5]|(14.5-37.5]|(1.5-5.5]|1
(-inf-2.5]|(14.5-37.5]|(1.5-5.5]|2
(2.5-3.5]|(-inf-14.5]|(1.5-5.5]|1
(3.5-4.5]|(-inf-14.5]|(1.5-5.5]|1
(6.5-12.5]|(-inf-14.5]|(1.5-5.5]|1
(4.5-6.5]|(37.5-76.5]|(-inf-1.5]|2
(26.5-90]|(37.5-76.5]|(-inf-1.5]|4
(-inf-2.5]|(-inf-14.5]|(1.5-5.5]|2
(6.5-12.5]|(37.5-76.5]|(-inf-1.5]|1
(4.5-6.5]|(-inf-14.5]|(1.5-5.5]|1
(-inf-2.5]|(37.5-76.5]|(-inf-1.5]|2
(3.5-4.5]|(14.5-37.5]|(-inf-1.5]|2
(4.5-6.5]|(14.5-37.5]|(-inf-1.5]|1
(26.5-90]|(14.5-37.5]|(-inf-1.5]|4
(12.5-26.5]|(14.5-37.5]|(-inf-1.5]|4
(6.5-12.5]|(14.5-37.5]|(-inf-1.5]|1
(-inf-2.5]|(14.5-37.5]|(-inf-1.5]|2
(4.5-6.5]|(-inf-14.5]|(-inf-1.5]|1
(12.5-26.5]|(-inf-14.5]|(-inf-1.5]|4
(6.5-12.5]|(-inf-14.5]|(-inf-1.5]|4
(3.5-4.5]|(-inf-14.5]|(-inf-1.5]|1
(-inf-2.5]|(-inf-14.5]|(-inf-1.5]|2
(2.5-3.5]|(-inf-14.5]|(-inf-1.5]|1

## JRip

Decision list:

rules | predicted class
---|---
(Height >= 28) and (P_black >= 0.339) and (Lenght >= 31) and (Eccen <= 1.141) and (Mean_tr >= 4.25)|3 (14.0/0.0)
(Eccen <= 0.091) and (Eccen >= 0.029)|4 (26.0/0.0)
(Eccen <= 0.222) and (Height >= 38)|4 (16.0/0.0)
(Lenght <= 2) and (Eccen <= 0.222) and (Height <= 19) and (Area >= 10)|4 (10.0/0.0)
(Lenght <= 2) and (P_black >= 0.875) and (Height <= 7)|4 (8.0/1.0)
(Eccen <= 0.286) and (Area <= 9) and (P_black >= 1) and (Height >= 9)|4 (8.0/1.0)
(P_and <= 0.555) and (Height >= 13) and (P_black <= 0.201) and (Eccen <= 3.337) and (Lenght >= 37)|5 (34.0/0.0)
(P_and <= 0.554) and (Eccen <= 2.4) and (P_black <= 0.156) and (P_and >= 0.338) and (Wb_trans <= 29)|5 (17.0/0.0)
(Height >= 31) and (P_black <= 0.299) and (Mean_tr >= 3.09) and (Mean_tr <= 5.69)|5 (9.0/0.0)
(P_and <= 0.6) and (Eccen <= 2) and (P_black <= 0.275) and (Lenght <= 9)|5 (16.0/7.0)
(Height >= 34) and (P_black <= 0.299)|5 (17.0/8.0)
(Mean_tr >= 9.06) and (Height <= 2) and (Area >= 41)|2 (107.0/0.0)
(Height <= 3) and (Mean_tr >= 1.38) and (Eccen >= 10) and (P_black >= 0.616) and (P_black <= 0.765)|2 (22.0/0.0)
(Height <= 3) and (Eccen >= 10) and (Eccen <= 23) and (Mean_tr >= 5.5)|2 (31.0/0.0)
(Height <= 3) and (Mean_tr >= 1.38) and (Eccen >= 35) and (Wb_trans >= 6)|2 (30.0/0.0)
(Height <= 2) and (Mean_tr >= 1.38) and (Blackpix >= 17) and (P_black <= 0.897)|2 (18.0/0.0)
(Height <= 2) and (P_black >= 0.407) and (Lenght >= 14) and (Lenght <= 20)|2 (10.0/0.0)
(Height <= 4) and (Mean_tr >= 13.5) and (Area >= 26) and (Eccen <= 131)|2 (14.0/0.0)
(Height <= 2) and (Mean_tr >= 1.4) and (Lenght <= 9) and (Blackpix >= 8) and (Eccen <= 8)|2 (8.0/0.0)
(Height <= 2) and (Mean_tr >= 1.4) and (Wb_trans >= 5) and (Eccen >= 27) and (Blackpix <= 13)|2 (8.0/0.0)
(Mean_tr >= 30.27) and (Eccen >= 6.5) and (Lenght <= 342)|2 (13.0/0.0)
|1 (4483.0/78.0)


## PART

Decision list:

rules | predicted class
---|---
Height > 3.5 AND Eccen > 0.236 AND Height <= 27.5 AND Mean_tr <= 21.295 AND Blackpix > 14.5 AND P_and > 0.5195 AND P_black > 0.1565 AND Mean_tr <= 16.855 AND Height <= 24.5 AND P_and > 0.5835 AND Blackand > 89.5|1 (3054.0)
Height <= 3.5 AND Mean_tr <= 1.355 AND P_black <= 0.4075|1 (43.0)
Height <= 3.5 AND Lenght > 7.5 AND Mean_tr > 9.975 AND Blackpix <= 618.5 AND Area > 40.5|2 (119.0)
Eccen <= 0.236 AND Blackpix > 7.5 AND Mean_tr > 9.5 AND Area <= 35.5|4 (30.0)
Height <= 2.5 AND Blackpix > 7.5 AND P_black > 0.445 AND P_black <= 0.5895|2 (25.0)
Height <= 2.5 AND Blackpix > 7.5 AND P_black > 0.5935 AND P_black <= 0.767|2 (29.0)
Eccen <= 0.2085 AND Blackpix > 7.5 AND Eccen <= 0.108 AND Height > 38.5|4 (17.0)
Height <= 2.5 AND Blackpix > 7.5 AND P_black > 0.803 AND P_black > 0.8985 AND Lenght <= 23.5 AND Lenght > 9.5|2 (21.0)
Height <= 27.5 AND Height > 2.5 AND Eccen > 0.199 AND Mean_tr <= 30.135 AND Blackpix > 11.5 AND P_and > 0.5225 AND Eccen > 0.62 AND Blackand <= 3994 AND Blackand > 24.5 AND Wb_trans > 4.5 AND P_black > 0.2085 AND Area <= 124|1 (590.0)
Height <= 27.5 AND Lenght > 2.5 AND Height > 2.5 AND Mean_tr <= 30.135 AND Wb_trans > 34.5 AND Blackpix <= 4356.5 AND Wb_trans <= 577|1 (354.0)
Eccen > 6.737 AND Wb_trans > 273.5 AND P_black > 0.2165|1 (20.0)
Eccen > 6.393 AND Area <= 9009 AND P_black > 0.1885 AND Mean_tr > 25.5 AND Lenght <= 341.5|2 (17.0)
Eccen > 6.737 AND P_black > 0.1885 AND Eccen > 13.5 AND P_black > 0.2725 AND Wb_trans <= 23.5 AND Area > 17.5 AND P_black > 0.693 AND P_black <= 0.8535|2 (12.0)
Eccen > 6.737 AND P_black > 0.1885 AND P_black <= 0.2725 AND Height <= 1.5|2 (6.0)
Eccen > 6.737 AND P_black > 0.201 AND Lenght > 50.5 AND P_black <= 0.53|2 (13.0)
Eccen <= 0.2085 AND Eccen > 0.108 AND Blackpix > 7.5 AND Eccen > 0.12|4 (10.0/2.0)
Eccen > 6.9 AND Mean_tr <= 1.555|1 (11.0)
Eccen > 6.9 AND P_black > 0.143 AND P_and <= 0.7615|1 (11.0/3.0)
Eccen > 6.9 AND P_black > 0.1895 AND Mean_tr > 7.25 AND P_black <= 0.8985|2 (9.0)
Area <= 462 AND Eccen > 0.1965 AND Eccen <= 6.9 AND Lenght > 2.5 AND P_black > 0.1595 AND P_and > 0.387 AND Eccen > 2.0625 AND Area > 38 AND P_and > 0.4735|1 (44.0)
Area <= 462 AND Eccen > 0.1965 AND Eccen <= 6.9 AND Lenght > 2.5 AND P_black > 0.21 AND Eccen <= 1.9615 AND P_black > 0.4675|1 (82.0)
Height <= 11.5 AND Lenght > 2.5 AND Eccen <= 6.9 AND P_and > 0.3155 AND Blackpix > 9.5 AND Height > 4.5 AND P_and > 0.601 AND Blackand <= 87.5 AND Mean_tr <= 6.75 AND P_and <= 0.976|1 (32.0)
P_black <= 0.3515 AND Height > 11.5 AND Mean_tr <= 10.565 AND P_black <= 0.214 AND Eccen > 0.4845 AND Eccen <= 3.345 AND Lenght > 18.5|5 (40.0)
Eccen <= 0.1965 AND Height <= 14.5 AND Height > 8.5|4 (9.0/1.0)
Eccen > 6.9 AND Height <= 11.5 AND Area <= 8.5|2 (9.0/2.0)
Blackand <= 626.5 AND Lenght > 2.5 AND Eccen <= 8.75 AND Height > 11.5 AND Blackpix > 30.5 AND P_black <= 0.268|5 (9.0/3.0)
Blackand <= 626.5 AND Lenght > 2.5 AND Eccen <= 8.75 AND P_black > 0.1595 AND P_and > 0.386 AND Eccen <= 1.9545 AND Mean_tr > 9.5 AND Height > 7.5|1 (10.0)
Blackand <= 626.5 AND Lenght > 2.5 AND Eccen > 8.75 AND Lenght <= 123 AND P_black <= 0.425 AND Eccen > 20.5|2 (7.0/1.0)
Blackand <= 626.5 AND Eccen <= 0.1965 AND Height > 7.5|4 (7.0/3.0)
Height <= 26.5 AND Lenght <= 2.5 AND P_black > 0.866|4 (8.0/1.0)
Height <= 26.5 AND Eccen <= 8.854 AND Lenght <= 2.5 AND P_and <= 0.757|1 (6.0/2.0)
Height <= 26.5 AND Height <= 3.5 AND Eccen <= 17.5 AND Eccen <= 12.25 AND Eccen > 8.75|1 (9.0/4.0)
Height <= 26.5 AND Eccen <= 3.4645 AND P_black > 0.1595 AND Mean_tr > 9.5 AND Area <= 33|1 (6.0)
Height <= 26.5 AND Height <= 3.5 AND Area > 17.5 AND Area <= 28|1 (6.0)
Height <= 26.5 AND Eccen > 12.3335 AND Eccen <= 23.417|2 (11.0/2.0)
Blackand <= 626.5 AND P_and > 0.3155 AND Height > 11.5 AND Blackpix <= 26.5|5 (7.0)
Blackand <= 626.5 AND P_and > 0.3155 AND Height > 4.5 AND P_and > 0.606 AND P_and > 0.776 AND Lenght <= 4.5|1 (21.0)
Blackand <= 626.5 AND P_and > 0.3155 AND Wb_trans > 7.5 AND Area > 130 AND Lenght <= 38.5|1 (23.0)
P_black <= 0.358 AND Height <= 82.5 AND Eccen <= 6.4285 AND P_black > 0.277 AND Height > 4.5|1 (19.0)
P_black > 0.3545 AND Height > 26 AND Height <= 90 AND Eccen > 1.3505|1 (11.0/1.0)
Blackand <= 626.5 AND Eccen <= 3.4645 AND Wb_trans > 1.5 AND Blackand <= 79 AND Wb_trans <= 3.5 AND P_black <= 0.355|5 (11.0/1.0)
Blackand <= 626.5 AND Blackpix <= 50.5 AND Eccen > 3.4645 AND Blackand > 32.5|1 (11.0/1.0)
Blackand <= 626.5 AND P_and > 0.3155 AND Area <= 28.5 AND P_black <= 0.4275|1 (7.0)
P_black <= 0.3315 AND Blackpix <= 2103.5 AND P_and > 0.2635 AND Mean_tr <= 2.985 AND P_and <= 0.4575|1 (9.0/1.0)
P_black <= 0.3315 AND Height > 34.5 AND Eccen > 2.986|5 (8.0)
Blackand <= 626.5 AND Wb_trans <= 11 AND Eccen <= 3.25 AND Wb_trans > 3.5 AND Eccen <= 1.775 AND Blackand <= 42.5|1 (11.0/4.0)
Blackand <= 626.5 AND Wb_trans <= 11 AND Mean_tr <= 2.835 AND Blackand <= 44.5|1 (8.0/4.0)
Blackand <= 626.5 AND Eccen > 3.5835|2 (10.0/3.0)
Height <= 26 AND P_and <= 0.87 AND P_and <= 0.6875 AND Height > 6.5 AND Eccen > 1.159|1 (8.0/4.0)
Height <= 26 AND Lenght > 5.5 AND P_and > 0.772|1 (9.0/1.0)
Lenght > 30.5 AND P_black > 0.306 AND Height > 90|3 (12.0)
P_black > 0.4005 AND Blackpix > 412.5 AND Blackpix <= 445.5|3 (7.0)
Height <= 28.5 AND Lenght > 5.5 AND Height <= 9.5|2 (10.0/4.0)
Eccen > 0.657 AND Height <= 28.5|1 (9.0)
P_black <= 0.338 AND Height <= 50|5 (7.0/3.0)
P_black > 0.338|3 (9.0/4.0)
|5 (6.0/1.0)


## J48 Decision Tree

* Height <= 3.5
	* Lenght <= 5.5: 1 (13.0)
	* Lenght > 5.5
		* P_black <= 0.2285: 1 (25.0/2.0)
		* P_black > 0.2285
			* Eccen <= 9.5
				* P_black <= 0.643: 1 (10.0/2.0)
				* P_black > 0.643: 2 (11.0/3.0)
			* Eccen > 9.5
				* Mean_tr <= 1.275: 1 (12.0/5.0)
				* Mean_tr > 1.275: 2 (161.0/6.0)
* Height > 3.5
	* Eccen <= 0.2085: 4 (55.0/6.0)
	* Eccen > 0.2085
		* Height <= 27.5
			* Mean_tr <= 15.855
				* P_black <= 0.1575
					* Eccen <= 3.6145: 5 (28.0/9.0)
					* Eccen > 3.6145: 1 (99.0/1.0)
				* P_black > 0.1575: 1 (2745.0/22.0)
			* Mean_tr > 15.855
				* Eccen <= 17.565: 1 (41.0/5.0)
				* Eccen > 17.565: 2 (12.0)
		* Height > 27.5
			* P_black <= 0.3315: 5 (44.0/13.0)
			* P_black > 0.3315
				* Eccen <= 1.238: 3 (13.0/1.0)
				* Eccen > 1.238: 1 (11.0/5.0)


