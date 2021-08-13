# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 7 | 0.119186 |
| V1 > 0.5 and V2 > 0.5 and V3 <= 0.5 and V4 > 0.5 and V5 <= 0.5 | 5 | 0.064843 |
| V1 <= 0.5 and V2 > 0.5 and V3 > 0.5 and V4 > 0.5 and V5 <= 0.5 | 4 | 0.060471 |
| V1 > 0.5 and V2 > 0.5 and V3 > 0.5 and V4 <= 0.5 and V5 > 0.5 | 0 | 0.053022 |
| V1 > 0.5 and V2 > 0.5 and V3 > 0.5 and V4 > 0.5 and V5 > 0.5 | 8 | 0.050104 |
| V1 > 0.5 and V2 > 0.5 and V3 <= 0.5 and V4 > 0.5 and V5 > 0.5 | 6 | 0.044900 |
| V1 > 0.5 and V2 <= 0.5 and V3 > 0.5 and V4 > 0.5 and V5 <= 0.5 | 3 | 0.039771 |
| V1 > 0.5 and V2 > 0.5 and V3 > 0.5 and V4 > 0.5 and V5 <= 0.5 | 9 | 0.036852 |
| V1 > 0.5 and V2 <= 0.5 and V3 > 0.5 and V4 > 0.5 and V5 > 0.5 | 2 | 0.033608 |
| V1 <= 0.5 and V2 <= 0.5 and V3 > 0.5 and V4 <= 0.5 and V5 <= 0.5 | 1 | 0.021230 |
| V1 <= 0.5 and V2 > 0.5 and V3 <= 0.5 and V4 > 0.5 and V5 <= 0.5 | 4 | 0.020579 |
| V1 <= 0.5 and V2 <= 0.5 and V3 > 0.5 and V4 > 0.5 and V5 <= 0.5 | 3 | 0.017620 |
| V1 <= 0.5 and V2 <= 0.5 and V3 <= 0.5 and V4 <= 0.5 and V5 <= 0.5 | 1 | 0.018405 |
| V1 > 0.5 and V2 > 0.5 and V3 > 0.5 and V4 <= 0.5 and V5 <= 0.5 | 9 | 0.006472 |
| V1 > 0.5 and V2 > 0.5 and V3 <= 0.5 and V4 <= 0.5 and V5 <= 0.5 | 5 | 0.005825 |
| V1 <= 0.5 and V2 <= 0.5 and V3 > 0.5 and V4 <= 0.5 and V5 > 0.5 | 1 | 0.005607 |
| V1 > 0.5 and V2 <= 0.5 and V3 > 0.5 and V4 <= 0.5 and V5 > 0.5 | 0 | 0.003215 |
| V1 <= 0.5 and V2 > 0.5 and V3 <= 0.5 and V4 > 0.5 and V5 > 0.5 | 6 | 0.004233 |
| V1 <= 0.5 and V2 > 0.5 and V3 > 0.5 and V4 <= 0.5 and V5 > 0.5 | 0 | 0.004274 |
| V1 <= 0.5 and V2 > 0.5 and V3 > 0.5 and V4 <= 0.5 and V5 <= 0.5 | 4 | 0.004357 |
| V1 <= 0.5 and V2 > 0.5 and V3 > 0.5 and V4 > 0.5 and V5 > 0.5 | 4 | 0.003713 |
| V1 > 0.5 and V2 <= 0.5 and V3 <= 0.5 and V4 > 0.5 and V5 > 0.5 | 2 | 0.001592 |
| V1 > 0.5 and V2 <= 0.5 and V3 <= 0.5 and V4 > 0.5 and V5 <= 0.5 | 6 | 0.001592 |
| V1 > 0.5 and V2 > 0.5 and V3 <= 0.5 and V4 <= 0.5 and V5 > 0.5 | 0 | 0.001075 |
| V1 <= 0.5 and V2 <= 0.5 and V3 <= 0.5 and V4 > 0.5 and V5 <= 0.5 | 4 | 0.001096 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| V2 <= 0.0 and V7 <= 0.0 and V4 <= 0.0 and V1 > 0.0 and V6 > 0.0 | 7 | 0.062991 |
| V2 <= 0.0 and V7 <= 0.0 and V4 <= 0.0 and V1 <= 0.0 | 1 | 0.046232 |
| V5 > 0.0 and V6 <= 0.0 and V2 <= 0.0 and V7 > 0.0 | 2 | 0.052448 |
| V3 <= 0.0 and V5 > 0.0 and V7 > 0.0 | 6 | 0.059041 |
| V3 <= 0.0 and V1 > 0.0 and V2 > 0.0 and V7 > 0.0 | 5 | 0.073171 |
| V7 <= 0.0 and V1 <= 0.0 and V3 > 0.0 | 4 | 0.093822 |
| V3 <= 0.0 and V1 <= 0.0 and V7 <= 0.0 | 4 | 0.029306 |
| V5 > 0.0 and V4 <= 0.0 and V2 > 0.0 | 0 | 0.097890 |
| V3 <= 0.0 and V1 > 0.0 and V2 > 0.0 | 5 | 0.006426 |
| V5 > 0.0 and V4 > 0.0 and V6 > 0.0 | 8 | 0.104760 |
| V7 <= 0.0 and V4 > 0.0 | 2 | 0.013935 |
| V6 > 0.0 and V3 > 0.0 and V4 > 0.0 and V2 <= 0.0 and V1 > 0.0 | 3 | 0.106230 |
| V2 > 0.0 and V5 <= 0.0 and V4 > 0.0 and V1 > 0.0 | 9 | 0.104095 |
| V3 <= 0.0 and V1 <= 0.0 | 5 | 0.021362 |
| V2 > 0.0 and V5 <= 0.0 and V1 > 0.0 | 9 | 0.012658 |
| V2 > 0.0 and V5 <= 0.0 | 9 | 0.007558 |
| V2 <= 0.0 and V6 <= 0.0 and V7 > 0.0 | 2 | 0.019753 |
| V2 <= 0.0 and V6 > 0.0 and V4 <= 0.0 | 0 | 0.009662 |
| V6 > 0.0 | 3 | 0.128571 |
| V2 <= 0.0 | 7 | 0.147449 |
|  | 8 | 0.189655 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| V4 <= 0 and V1 <= 0 and V2 <= 0 | 1 | 0.041761 |
| V6 <= 0 and V2 <= 0 and V5 >= 1 | 2 | 0.055453 |
| V3 <= 0 and V5 >= 1 | 6 | 0.056019 |
| V5 >= 1 and V4 <= 0 | 0 | 0.076436 |
| V2 >= 1 and V3 >= 1 and V5 <= 0 and V7 >= 1 | 9 | 0.064982 |
| V3 <= 0 and V7 >= 1 | 5 | 0.098728 |
| V5 >= 1 and V1 >= 1 | 8 | 0.093103 |
| V1 <= 0 and V7 <= 0 | 4 | 0.170955 |
| V7 >= 1 and V2 <= 0 and V6 >= 1 and V4 >= 1 | 3 | 0.173611 |
|  | 7 | 0.356522 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

v1|v2|v3|v4|v5|target
---|---|---|---|---|---
(-inf-0.5]|(0.5-inf)|(0.5-inf)|(0.5-inf)|(0.5-inf)|4
(0.5-inf)|(0.5-inf)|(0.5-inf)|(0.5-inf)|(0.5-inf)|8
(-inf-0.5]|(-inf-0.5]|(0.5-inf)|(0.5-inf)|(0.5-inf)|0
(0.5-inf)|(-inf-0.5]|(0.5-inf)|(0.5-inf)|(0.5-inf)|2
(-inf-0.5]|(0.5-inf)|(-inf-0.5]|(0.5-inf)|(0.5-inf)|6
(0.5-inf)|(0.5-inf)|(-inf-0.5]|(0.5-inf)|(0.5-inf)|6
(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|(0.5-inf)|0
(-inf-0.5]|(0.5-inf)|(0.5-inf)|(-inf-0.5]|(0.5-inf)|0
(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|(0.5-inf)|2
(0.5-inf)|(0.5-inf)|(0.5-inf)|(-inf-0.5]|(0.5-inf)|0
(-inf-0.5]|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|(0.5-inf)|1
(0.5-inf)|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|(0.5-inf)|0
(0.5-inf)|(0.5-inf)|(0.5-inf)|(0.5-inf)|(-inf-0.5]|9
(-inf-0.5]|(0.5-inf)|(0.5-inf)|(0.5-inf)|(-inf-0.5]|4
(0.5-inf)|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|0
(-inf-0.5]|(-inf-0.5]|(0.5-inf)|(0.5-inf)|(-inf-0.5]|3
(0.5-inf)|(-inf-0.5]|(0.5-inf)|(0.5-inf)|(-inf-0.5]|3
(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|7
(-inf-0.5]|(0.5-inf)|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|4
(0.5-inf)|(0.5-inf)|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|5
(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|4
(-inf-0.5]|(0.5-inf)|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|4
(0.5-inf)|(0.5-inf)|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|9
(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|6
(-inf-0.5]|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|1
(0.5-inf)|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|7
(0.5-inf)|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|5
(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|1
(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|7

## JRip

Decision list:

rules | predicted class
---|---
(V4 <= 0) and (V1 <= 0) and (V2 <= 0)|1 (32.0/11.0)
(V6 <= 0) and (V2 <= 0) and (V5 >= 1)|2 (20.0/2.0)
(V3 <= 0) and (V5 >= 1)|6 (29.0/7.0)
(V5 >= 1) and (V4 <= 0)|0 (28.0/4.0)
(V2 >= 1) and (V3 >= 1) and (V5 <= 0) and (V7 >= 1)|9 (42.0/17.0)
(V3 <= 0) and (V7 >= 1)|5 (39.0/9.0)
(V5 >= 1) and (V1 >= 1)|8 (35.0/11.0)
(V1 <= 0) and (V7 <= 0)|4 (34.0/0.0)
(V7 >= 1) and (V2 <= 0) and (V6 >= 1) and (V4 >= 1)|3 (27.0/3.0)
|7 (58.0/27.0)


## PART

Decision list:

rules | predicted class
---|---
V2 <= 0.0 AND V7 <= 0.0 AND V4 <= 0.0 AND V1 > 0.0 AND V6 > 0.0|7 (26.0/3.0)
V2 <= 0.0 AND V7 <= 0.0 AND V4 <= 0.0 AND V1 <= 0.0|1 (28.0/8.0)
V5 > 0.0 AND V6 <= 0.0 AND V2 <= 0.0 AND V7 > 0.0|2 (15.0)
V3 <= 0.0 AND V5 > 0.0 AND V7 > 0.0|6 (25.0/5.0)
V3 <= 0.0 AND V1 > 0.0 AND V2 > 0.0 AND V7 > 0.0|5 (28.0/4.0)
V7 <= 0.0 AND V1 <= 0.0 AND V3 > 0.0|4 (27.0)
V3 <= 0.0 AND V1 <= 0.0 AND V7 <= 0.0|4 (8.0/1.0)
V5 > 0.0 AND V4 <= 0.0 AND V2 > 0.0|0 (26.0/4.0)
V3 <= 0.0 AND V1 > 0.0 AND V2 > 0.0|5 (8.0/4.0)
V5 > 0.0 AND V4 > 0.0 AND V6 > 0.0|8 (33.0/11.0)
V7 <= 0.0 AND V4 > 0.0|2 (9.0/5.0)
V6 > 0.0 AND V3 > 0.0 AND V4 > 0.0 AND V2 <= 0.0 AND V1 > 0.0|3 (20.0/3.0)
V2 > 0.0 AND V5 <= 0.0 AND V4 > 0.0 AND V1 > 0.0|9 (28.0/11.0)
V3 <= 0.0 AND V1 <= 0.0|5 (7.0/3.0)
V2 > 0.0 AND V5 <= 0.0 AND V1 > 0.0|9 (8.0/4.0)
V2 > 0.0 AND V5 <= 0.0|9 (7.0/3.0)
V2 <= 0.0 AND V6 <= 0.0 AND V7 > 0.0|2 (9.0/5.0)
V2 <= 0.0 AND V6 > 0.0 AND V4 <= 0.0|0 (12.0/8.0)
V6 > 0.0|3 (8.0/1.0)
V2 <= 0.0|7 (6.0/1.0)
|8 (6.0/2.0)


