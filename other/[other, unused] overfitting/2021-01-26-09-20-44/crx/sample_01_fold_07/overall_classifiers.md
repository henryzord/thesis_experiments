# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| A9!=(f) | positive | 0.444444 |
| A3 = all and A9 = f and A10 = t and A13 = g and A14 > 289 and A15 <= 254.5 | negative | 0.021277 |
| A3 = all and A9 = f and A10 = f and A13 = s and A14 > 99.5 and A14 <= 289 and A15 <= 254.5 | negative | 0.044983 |
| A3 = all and A9 = f and A10 = f and A13 = g and A14 > 289 and A15 <= 254.5 | negative | 0.081000 |
| A3 = all and A9 = f and A10 = f and A13 = g and A14 > 99.5 and A14 <= 289 and A15 <= 254.5 | negative | 0.267101 |
| A3 = all and A9 = f and A10 = f and A13 = g and A14 <= 99.5 and A15 <= 254.5 | negative | 0.101076 |
| A3 = all and A9 = f and A10 = f and A13 = s and A14 > 289 and A15 <= 254.5 | negative | 0.005435 |
| A3 = all and A9 = f and A10 = t and A13 = g and A14 > 99.5 and A14 <= 289 and A15 > 254.5 | negative | 0.011470 |
| A3 = all and A9 = f and A10 = f and A13 = s and A14 <= 99.5 and A15 <= 254.5 | negative | 0.025128 |
| A3 = all and A9 = t and A10 = f and A13 = g and A14 > 99.5 and A14 <= 289 and A15 <= 254.5 | negative | 0.048521 |
| A3 = all and A9 = f and A10 = f and A13 = g and A14 > 289 and A15 > 254.5 | negative | 0.017794 |
| A3 = all and A9 = f and A10 = t and A13 = g and A14 > 289 and A15 > 254.5 | negative | 0.007194 |
| A3 = all and A9 = t and A10 = f and A13 = s and A14 > 289 and A15 <= 254.5 | negative | 0.021277 |
| A3 = all and A9 = f and A10 = t and A13 = g and A14 <= 99.5 and A15 <= 254.5 | negative | 0.038328 |
| A3 = all and A9 = f and A10 = f and A13 = g and A14 <= 99.5 and A15 > 254.5 | negative | 0.018302 |
| A3 = all and A9 = f and A10 = f and A13 = g and A14 > 99.5 and A14 <= 289 and A15 > 254.5 | negative | 0.061224 |
| A3 = all and A9 = f and A10 = t and A13 = g and A14 <= 99.5 and A15 > 254.5 | negative | 0.010753 |
| A3 = all and A9 = f and A10 = t and A13 = g and A14 > 99.5 and A14 <= 289 and A15 <= 254.5 | negative | 0.089109 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| A9 != t | negative | 0.481341 |
| A15 > 422.0 | positive | 0.633550 |
| A10 = t and A6 != cc and A6 != x and A14 <= 93.5 | positive | 0.327935 |
| A6 != cc and A6 != x and A4 = u and A13 = g and A3 > 6.5 and A15 <= 140.0 and A1 = b | negative | 0.093220 |
| A10 = t | positive | 0.471076 |
| A4 = u and A13 = g | positive | 0.419465 |
|  | negative | 0.657534 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| A9 = t and A15 >= 444 and A8 >= 2 | positive | 0.243421 |
| A9 = t and A10 = t and A14 <= 93 and A3 >= 6 | positive | 0.106218 |
| A9 = t and A10 = t and A11 >= 4 and A15 <= 3 | positive | 0.041667 |
| A9 = t and A14 <= 70 and A2 <= 4133 and A15 <= 15 | positive | 0.036499 |
| A9 = t and A15 >= 99 and A4 = u and A2 <= 4133 | positive | 0.054795 |
| A9 = t and A3 >= 2875 and A8 >= 458 | positive | 0.014286 |
| A9 = t and A1 = a and A6 = c and A15 <= 0 | positive | 0.017094 |
| A9 = t and A2 >= 4433 and A15 <= 100 and A14 >= 230 | positive | 0.014286 |
| A9 = t and A2 <= 3267 and A3 <= 9 and A14 >= 100 | positive | 0.017450 |
| A9 = t and A14 <= 120 and A8 >= 55 and A3 >= 29 and A15 <= 14 | positive | 0.019886 |
| A9 = t and A14 >= 220 and A2 <= 3067 | positive | 0.013843 |
|  | negative | 0.907895 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

a3|a9|a10|a13|a14|a15|class
---|---|---|---|---|---|---
all|f|f|g|(289-inf)|(254.5-inf)|negative
all|f|f|p|?|(-inf-254.5]|positive
all|t|f|g|(289-inf)|(254.5-inf)|positive
all|f|f|g|?|(254.5-inf)|positive
all|f|t|g|(289-inf)|(254.5-inf)|negative
all|f|f|s|(289-inf)|(-inf-254.5]|negative
all|t|f|s|(289-inf)|(-inf-254.5]|negative
all|t|t|g|(289-inf)|(254.5-inf)|positive
all|f|t|s|(289-inf)|(-inf-254.5]|positive
all|f|f|g|(99.5-289]|(254.5-inf)|negative
all|t|t|g|?|(254.5-inf)|positive
all|t|f|g|(99.5-289]|(254.5-inf)|positive
all|f|f|g|(289-inf)|(-inf-254.5]|negative
all|f|t|g|(99.5-289]|(254.5-inf)|negative
all|t|f|g|(289-inf)|(-inf-254.5]|positive
all|f|f|s|(99.5-289]|(-inf-254.5]|negative
all|f|f|g|?|(-inf-254.5]|negative
all|t|f|s|(99.5-289]|(-inf-254.5]|positive
all|t|t|g|(99.5-289]|(254.5-inf)|positive
all|f|t|g|(289-inf)|(-inf-254.5]|negative
all|t|t|g|(289-inf)|(-inf-254.5]|positive
all|f|f|g|(-inf-99.5]|(254.5-inf)|negative
all|f|t|g|?|(-inf-254.5]|positive
all|t|f|g|(-inf-99.5]|(254.5-inf)|positive
all|f|f|g|(99.5-289]|(-inf-254.5]|negative
all|t|f|g|(99.5-289]|(-inf-254.5]|negative
all|f|t|g|(-inf-99.5]|(254.5-inf)|negative
all|f|f|s|(-inf-99.5]|(-inf-254.5]|negative
all|t|f|s|(-inf-99.5]|(-inf-254.5]|positive
all|t|t|g|(-inf-99.5]|(254.5-inf)|positive
all|f|t|g|(99.5-289]|(-inf-254.5]|negative
all|f|t|s|(-inf-99.5]|(-inf-254.5]|positive
all|t|t|g|(99.5-289]|(-inf-254.5]|positive
all|f|f|g|(-inf-99.5]|(-inf-254.5]|negative
all|t|f|g|(-inf-99.5]|(-inf-254.5]|positive
all|f|t|g|(-inf-99.5]|(-inf-254.5]|negative
all|t|t|g|(-inf-99.5]|(-inf-254.5]|positive

## JRip

Decision list:

rules | predicted class
---|---
(A9 = t) and (A15 >= 444) and (A8 >= 2)|positive (111.0/0.0)
(A9 = t) and (A10 = t) and (A14 <= 93) and (A3 >= 6)|positive (41.0/0.0)
(A9 = t) and (A10 = t) and (A11 >= 4) and (A15 <= 3)|positive (15.0/0.0)
(A9 = t) and (A14 <= 70) and (A2 <= 4133) and (A15 <= 15)|positive (13.0/0.0)
(A9 = t) and (A15 >= 99) and (A4 = u) and (A2 <= 4133)|positive (20.0/0.0)
(A9 = t) and (A3 >= 2875) and (A8 >= 458)|positive (5.0/0.0)
(A9 = t) and (A1 = a) and (A6 = c) and (A15 <= 0)|positive (6.0/0.0)
(A9 = t) and (A2 >= 4433) and (A15 <= 100) and (A14 >= 230)|positive (5.0/0.0)
(A9 = t) and (A2 <= 3267) and (A3 <= 9) and (A14 >= 100)|positive (7.0/0.0)
(A9 = t) and (A14 <= 120) and (A8 >= 55) and (A3 >= 29) and (A15 <= 14)|positive (8.0/0.0)
(A9 = t) and (A14 >= 220) and (A2 <= 3067)|positive (19.0/9.0)
|negative (371.0/35.0)


## PART

Decision list:

rules | predicted class
---|---
A9 != t|negative (297.0/22.0)
A15 > 422.0|positive (121.0/1.0)
A10 = t AND A6 != cc AND A6 != x AND A14 <= 93.5|positive (38.0/2.0)
A6 != cc AND A6 != x AND A4 = u AND A13 = g AND A3 > 6.5 AND A15 <= 140.0 AND A1 = b|negative (38.0/16.0)
A10 = t|positive (52.0/9.0)
A4 = u AND A13 = g|positive (34.0/9.0)
|negative (41.0/14.0)


## SimpleCart Decision Tree

* A9=(f): negative(275.0/22.0)
* A9!=(f): positive(254.0/70.0)


