# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| A8!=(1) | 0 | 0.555556 |
| A2 = all and A4 = 2 and A7 > 168 and A8 = 1 and A9 = 1 and A12 = 2 | 1 | 0.146631 |
| A2 = all and A4 = 2 and A7 <= 168 and A8 = 0 and A9 = 0 and A12 = 3 | 1 | 0.006606 |
| A2 = all and A4 = 2 and A7 <= 168 and A8 = 1 and A9 = 1 and A12 = 2 | 1 | 0.202512 |
| A2 = all and A4 = 1 and A7 <= 168 and A8 = 1 and A9 = 1 and A12 = 2 | 1 | 0.035014 |
| A2 = all and A4 = 2 and A7 > 168 and A8 = 1 and A9 = 0 and A12 = 2 | 1 | 0.033920 |
| A2 = all and A4 = 2 and A7 <= 168 and A8 = 0 and A9 = 1 and A12 = 1 | 1 | 0.001449 |
| A2 = all and A4 = 1 and A7 > 168 and A8 = 1 and A9 = 0 and A12 = 2 | 1 | 0.010263 |
| A2 = all and A4 = 2 and A7 > 168 and A8 = 1 and A9 = 0 and A12 = 1 | 1 | 0.005797 |
| A2 = all and A4 = 1 and A7 > 168 and A8 = 1 and A9 = 1 and A12 = 2 | 1 | 0.021853 |
| A2 = all and A4 = 2 and A7 <= 168 and A8 = 1 and A9 = 0 and A12 = 2 | 1 | 0.065093 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| A8 = 0 | 0 | 0.480635 |
| A9 = 1 | 1 | 0.711894 |
| A14 <= 445 and A4 = 1 | 0 | 0.148179 |
| A14 <= 368 and A6 <= 5 and A13 <= 360 and A5 <= 9 and A1 = 1 and A14 <= 1 and A13 > 112 | 0 | 0.116883 |
| A5 > 8 | 1 | 0.561324 |
| A6 <= 5 and A13 <= 356 and A5 > 3 | 1 | 0.437575 |
| A6 <= 5 | 0 | 0.460952 |
|  | 1 | 0.750000 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| A8 = 1 and A9 = 1 and A14 >= 222 and A2 >= 2392 | 1 | 0.166667 |
| A8 = 1 and A9 = 1 and A13 <= 129 and A3 >= 95 | 1 | 0.096859 |
| A8 = 1 and A14 >= 552 and A1 = 1 | 1 | 0.059946 |
| A8 = 1 and A9 = 1 and A10 >= 4 and A3 >= 171 | 1 | 0.044321 |
| A8 = 1 and A13 <= 110 and A4 = 2 and A5 >= 6 and A7 <= 35 | 1 | 0.070081 |
| A8 = 1 and A5 >= 9 and A13 <= 145 and A2 >= 2017 | 1 | 0.038997 |
| A8 = 1 and A13 >= 220 and A14 >= 8 and A2 <= 3492 | 1 | 0.046961 |
| A8 = 1 and A3 <= 45 and A7 >= 75 and A3 >= 9 and A13 <= 330 | 1 | 0.033613 |
| A8 = 1 and A3 <= 10 | 1 | 0.027090 |
|  | 0 | 0.880102 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

a2|a4|a7|a8|a9|a12|class
---|---|---|---|---|---|---
all|2|(168-inf)|1|1|2|1
all|1|(168-inf)|1|1|2|1
all|2|(-inf-168]|1|1|2|1
all|3|(-inf-168]|0|0|3|0
all|1|(-inf-168]|1|1|2|1
all|2|(168-inf)|0|1|2|0
all|2|(-inf-168]|0|0|3|1
all|2|(168-inf)|1|0|2|1
all|1|(168-inf)|0|1|2|0
all|1|(168-inf)|1|0|2|1
all|2|(-inf-168]|0|1|2|0
all|1|(-inf-168]|0|1|2|0
all|2|(-inf-168]|1|0|2|1
all|2|(-inf-168]|1|1|1|0
all|2|(168-inf)|0|0|2|0
all|1|(-inf-168]|1|0|2|0
all|1|(168-inf)|0|0|2|0
all|2|(168-inf)|1|0|1|1
all|2|(-inf-168]|0|0|2|0
all|2|(-inf-168]|0|1|1|1
all|1|(-inf-168]|0|0|2|0
all|2|(-inf-168]|1|0|1|0
all|1|(-inf-168]|1|0|1|0
all|2|(168-inf)|0|0|1|0
all|3|(-inf-168]|0|0|1|0
all|2|(-inf-168]|0|0|1|0
all|1|(-inf-168]|0|0|1|0

## JRip

Decision list:

rules | predicted class
---|---
(A8 = 1) and (A9 = 1) and (A14 >= 222) and (A2 >= 2392)|1 (69.0/0.0)
(A8 = 1) and (A9 = 1) and (A13 <= 129) and (A3 >= 95)|1 (37.0/0.0)
(A8 = 1) and (A14 >= 552) and (A1 = 1)|1 (22.0/0.0)
(A8 = 1) and (A9 = 1) and (A10 >= 4) and (A3 >= 171)|1 (16.0/0.0)
(A8 = 1) and (A13 <= 110) and (A4 = 2) and (A5 >= 6) and (A7 <= 35)|1 (26.0/0.0)
(A8 = 1) and (A5 >= 9) and (A13 <= 145) and (A2 >= 2017)|1 (14.0/0.0)
(A8 = 1) and (A13 >= 220) and (A14 >= 8) and (A2 <= 3492)|1 (17.0/0.0)
(A8 = 1) and (A3 <= 45) and (A7 >= 75) and (A3 >= 9) and (A13 <= 330)|1 (12.0/0.0)
(A8 = 1) and (A3 <= 10)|1 (27.0/11.0)
|0 (381.0/47.0)


## PART

Decision list:

rules | predicted class
---|---
A8 = 0|0 (298.0/23.0)
A9 = 1|1 (200.0/17.0)
A14 <= 445 AND A4 = 1|0 (25.0/8.0)
A14 <= 368 AND A6 <= 5 AND A13 <= 360 AND A5 <= 9 AND A1 = 1 AND A14 <= 1 AND A13 > 112|0 (23.0/7.0)
A5 > 8|1 (35.0/3.0)
A6 <= 5 AND A13 <= 356 AND A5 > 3|1 (14.0/2.0)
A6 <= 5|0 (14.0/2.0)
|1 (12.0/3.0)


## SimpleCart Decision Tree

* A8=(1): 1(253.0/70.0)
* A8!=(1): 0(275.0/23.0)


