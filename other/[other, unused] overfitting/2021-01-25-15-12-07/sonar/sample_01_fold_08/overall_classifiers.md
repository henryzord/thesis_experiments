# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Band11 >= 0.1985 | M | 0.423722 |
| Band11 < 0.1985 | R | 0.340992 |
| Band4 > 0.051 and Band6 = all and Band11 <= 0.1985 and Band27 = all and Band33 = all and Band38 = all and Band49 > 0.0445 | M | 0.075988 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Band11 > 0.197 and Band27 > 0.814 | M | 0.343439 |
| Band54 <= 0.022 and Band1 > 0.011 and Band36 > 0.478 | R | 0.368902 |
| Band58 <= 0.006 | R | 0.398374 |
| Band49 > 0.023 | M | 0.771838 |
|  | R | 0.722222 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Band11 <= 0.197 and Band45 <= 0.158 | R | 0.320320 |
| Band27 <= 0.834 and Band58 <= 0.005 and Band36 >= 0.286 | R | 0.116667 |
| Band37 >= 0.483 and Band45 <= 0.264 | R | 0.072569 |
|  | M | 0.883929 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

band4|band6|band11|band27|band33|band38|band49|type
---|---|---|---|---|---|---|---
(-inf-0.051]|all|(0.1985-inf)|all|all|all|(0.0445-inf)|m
(0.051-inf)|all|(0.1985-inf)|all|all|all|(0.0445-inf)|m
(0.051-inf)|all|(-inf-0.1985]|all|all|all|(0.0445-inf)|m
(-inf-0.051]|all|(-inf-0.1985]|all|all|all|(0.0445-inf)|r
(0.051-inf)|all|(0.1985-inf)|all|all|all|(-inf-0.0445]|m
(-inf-0.051]|all|(0.1985-inf)|all|all|all|(-inf-0.0445]|m
(0.051-inf)|all|(-inf-0.1985]|all|all|all|(-inf-0.0445]|r
(-inf-0.051]|all|(-inf-0.1985]|all|all|all|(-inf-0.0445]|r

## JRip

Decision list:

rules | predicted class
---|---
(Band11 <= 0.197) and (Band45 <= 0.158)|R (56.0/5.0)
(Band27 <= 0.834) and (Band58 <= 0.005) and (Band36 >= 0.286)|R (14.0/0.0)
(Band37 >= 0.483) and (Band45 <= 0.264)|R (12.0/2.0)
|M (105.0/13.0)


## PART

Decision list:

rules | predicted class
---|---
Band11 > 0.197 AND Band27 > 0.814|M (48.0/1.0)
Band54 <= 0.022 AND Band1 > 0.011 AND Band36 > 0.478|R (36.0/3.0)
Band58 <= 0.006|R (52.0/11.0)
Band49 > 0.023|M (42.0/6.0)
|R (9.0/2.0)


## SimpleCart Decision Tree

* Band11 < 0.1985: R(64.0/20.0)
* Band11 >= 0.1985: M(79.0/24.0)


