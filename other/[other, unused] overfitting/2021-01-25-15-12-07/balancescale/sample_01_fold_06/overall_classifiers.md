# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| left-distance <= 2 and right-weight > 1 and right-distance > 2 | 2 | 0.235873 |
| left-distance > 2 and left-weight > 2 and right-weight <= 2 | 0 | 0.208476 |
| left-distance > 2 and left-weight > 2 and right-weight > 2 and right-distance <= 3 | 0 | 0.152213 |
| left-distance > 2 and left-weight <= 2 and right-distance > 1 and right-weight > 1 and right-distance > 2 | 2 | 0.144516 |
| left-distance > 2 and left-weight <= 2 and right-distance <= 1 | 0 | 0.057544 |
| left-distance <= 2 and right-weight <= 1 and left-weight > 2 | 0 | 0.054702 |
| left-distance <= 2 and right-weight > 1 and right-distance <= 2 and left-weight > 1 and left-distance <= 1 | 2 | 0.044351 |
| left-distance <= 2 and right-weight > 1 and right-distance <= 2 and left-weight <= 1 | 2 | 0.041747 |
| left-distance > 2 and left-weight <= 2 and right-distance > 1 and right-weight <= 1 | 0 | 0.045006 |
| left-distance > 2 and left-weight > 2 and right-weight > 2 and right-distance > 3 and left-weight <= 3 | 2 | 0.039263 |
| left-distance <= 2 and right-weight > 1 and right-distance <= 2 and left-weight > 1 and left-distance > 1 | 0 | 0.030075 |
| left-weight <= 1.5 and left-distance > 2.5 and right-weight > 2.5 and right-distance <= 2.5 | 2 | 0.023337 |
| left-distance > 2 and left-weight > 2 and right-weight > 2 and right-distance > 3 and left-weight > 3 and left-distance > 3 | 0 | 0.026386 |
| left-distance <= 2 and right-weight <= 1 and left-weight <= 2 and right-distance > 2 | 2 | 0.023986 |
| left-distance > 2 and left-weight > 2 and right-weight > 2 and right-distance > 3 and left-weight > 3 and left-distance <= 3 | 2 | 0.023986 |
| left-distance > 2 and left-weight <= 2 and right-distance > 1 and right-weight > 1 and right-distance <= 2 and right-weight <= 3 | 0 | 0.010000 |
| left-weight > 1.5 and left-weight <= 2.5 and left-distance > 1.5 and left-distance <= 2.5 and right-weight > 2.5 and right-distance <= 2.5 | 2 | 0.008830 |
| left-weight > 2.5 and left-distance <= 1.5 and right-weight > 1.5 and right-weight <= 2.5 and right-distance <= 2.5 | 0 | 0.005980 |
| left-distance <= 2 and right-weight <= 1 and left-weight <= 2 and right-distance <= 2 | 0 | 0.006667 |
| left-weight > 1.5 and left-weight <= 2.5 and left-distance <= 1.5 and right-weight <= 1.5 and right-distance <= 2.5 | 1 | 0.000969 |
| left-weight > 1.5 and left-weight <= 2.5 and left-distance > 2.5 and right-weight > 1.5 and right-weight <= 2.5 and right-distance > 2.5 | 0 | 0.004300 |
| left-weight > 1.5 and left-weight <= 2.5 and left-distance > 1.5 and left-distance <= 2.5 and right-weight > 1.5 and right-weight <= 2.5 and right-distance <= 2.5 | 1 | 0.000969 |
| left-distance > 2 and left-weight <= 2 and right-distance > 1 and right-weight > 1 and right-distance <= 2 and right-weight > 3 | 2 | 0.019076 |
| left-weight > 2.5 and left-distance > 1.5 and left-distance <= 2.5 and right-weight > 1.5 and right-weight <= 2.5 and right-distance > 2.5 | 0 | 0.003775 |
| left-weight > 1.5 and left-weight <= 2.5 and left-distance > 1.5 and left-distance <= 2.5 and right-weight <= 1.5 and right-distance > 2.5 | 1 | 0.000647 |
| left-weight <= 1.5 and left-distance <= 1.5 and right-weight <= 1.5 and right-distance <= 2.5 | 2 | 0.001667 |
| left-weight > 2.5 and left-distance > 2.5 and right-weight > 2.5 and right-distance > 2.5 | 0 | 0.051446 |
| left-weight > 1.5 and left-weight <= 2.5 and left-distance > 2.5 and right-weight > 2.5 and right-distance <= 2.5 | 0 | 0.026144 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| right-weight <= 2 and left-distance > 2 and left-weight > 1 and left-weight > 2 and right-distance <= 4 | 0 | 0.173554 |
| left-distance <= 1 and right-weight > 1 and right-distance > 2 | 2 | 0.177083 |
| left-weight <= 1 and right-distance > 1 and right-weight > 2 | 2 | 0.168421 |
| left-distance > 3 and right-distance <= 2 and left-weight > 2 | 0 | 0.122271 |
| right-weight > 3 and right-distance > 3 and left-distance <= 3 | 2 | 0.129167 |
| left-weight > 3 and right-weight <= 3 and left-distance > 3 | 0 | 0.105263 |
| left-weight > 4 and right-distance <= 4 and right-weight <= 4 and right-weight <= 2 | 0 | 0.065934 |
| left-distance <= 1 and right-weight > 3 and left-weight <= 3 | 2 | 0.053476 |
| right-distance <= 1 and left-distance > 1 and left-weight > 1 and right-weight <= 4 and right-weight <= 3 | 0 | 0.101124 |
| right-weight <= 1 and left-distance > 1 and left-weight > 1 and left-distance > 2 | 0 | 0.096045 |
| right-distance > 3 and left-weight <= 3 and right-weight <= 3 and left-distance <= 4 and left-weight <= 2 and right-distance > 4 | 2 | 0.089744 |
| right-distance > 3 and left-weight <= 4 and right-weight > 2 and left-weight > 2 and left-distance <= 4 | 2 | 0.067669 |
| left-distance > 2 and left-weight > 3 and right-distance <= 4 and right-distance > 2 and left-distance <= 4 | 0 | 0.044826 |
| right-distance <= 1 and left-distance > 2 and left-weight <= 1 | 0 | 0.039416 |
| left-weight <= 2 and right-distance > 2 and right-weight > 2 and left-distance <= 4 | 2 | 0.094891 |
| left-distance > 2 and right-distance > 1 and left-weight > 3 and right-distance <= 4 | 0 | 0.076471 |
| right-distance <= 1 and left-distance <= 2 and left-weight <= 2 | 2 | 0.027027 |
| right-distance <= 1 and left-distance > 1 | 0 | 0.080185 |
| right-weight > 4 and left-distance <= 4 | 2 | 0.115741 |
| right-weight > 3 and right-weight <= 4 and left-distance <= 3 | 2 | 0.062500 |
| right-weight <= 4 and right-distance <= 3 and left-distance > 3 and left-distance > 4 | 0 | 0.085034 |
| right-weight > 3 and right-weight > 4 | 2 | 0.032579 |
| left-weight <= 2 and left-distance > 1 and right-distance > 2 and right-weight > 1 | 2 | 0.104644 |
| right-weight <= 3 and left-distance > 3 | 0 | 0.098214 |
| left-weight > 1 and right-weight <= 2 and left-distance > 1 and right-weight > 1 | 0 | 0.035294 |
| left-weight <= 2 and left-distance > 1 | 2 | 0.025714 |
| left-weight > 2 and right-weight <= 2 and left-distance > 1 | 0 | 0.079412 |
| left-weight > 2 and right-distance > 3 | 2 | 0.078370 |
| left-weight > 2 and left-weight <= 3 | 0 | 0.033333 |
| left-weight > 3 | 0 | 0.064286 |
|  | 2 | 0.220339 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| right-distance <= 2 and left-distance <= 2 and right-weight <= 2 and left-weight <= 1 and left-distance >= 2 | 1 | 0.001938 |
| right-distance <= 2 and left-weight >= 2 and left-weight <= 2 and right-weight <= 2 and left-distance <= 1 | 1 | 0.001938 |
| left-weight >= 4 and right-weight >= 4 and right-distance <= 1 and left-distance <= 1 | 1 | 0.002579 |
| left-distance >= 4 and right-weight >= 4 and left-weight <= 1 and right-distance <= 1 | 1 | 0.001938 |
| left-distance <= 2 and right-weight <= 2 and left-weight >= 4 and right-distance >= 4 and left-weight <= 4 and right-distance <= 4 | 1 | 0.001938 |
| right-weight <= 2 and left-distance >= 3 and left-weight >= 3 and right-distance <= 4 | 0 | 0.178470 |
| right-distance <= 2 and left-distance >= 3 and left-weight >= 3 and right-weight <= 4 | 0 | 0.090909 |
| right-distance <= 2 and left-distance >= 2 and right-weight <= 1 | 0 | 0.064516 |
| left-distance >= 4 and left-weight >= 4 and right-weight <= 3 | 0 | 0.064516 |
| right-weight <= 2 and left-weight >= 2 and right-distance <= 3 and left-distance >= 3 | 0 | 0.033333 |
| right-distance <= 1 and left-weight >= 2 and left-distance >= 3 | 0 | 0.046053 |
| left-weight >= 3 and left-distance >= 2 and right-weight <= 1 | 0 | 0.046053 |
| left-weight >= 4 and right-distance <= 3 and left-distance >= 4 | 0 | 0.039735 |
| right-weight <= 2 and left-weight >= 3 and right-distance <= 1 | 0 | 0.020270 |
| right-weight <= 3 and right-distance <= 3 and left-distance >= 2 and left-weight >= 5 | 0 | 0.016949 |
| left-distance >= 3 and left-weight >= 2 and right-weight <= 1 | 0 | 0.020270 |
| left-weight >= 3 and left-distance >= 2 and right-distance <= 1 | 0 | 0.020270 |
| right-distance <= 3 and left-weight >= 4 and right-weight <= 1 | 0 | 0.013605 |
| left-distance >= 5 and right-weight <= 3 and right-distance <= 3 and left-weight >= 2 | 0 | 0.010239 |
| left-distance >= 4 and right-distance <= 1 | 0 | 0.014172 |
| left-distance >= 3 and right-weight <= 2 and left-weight >= 4 | 0 | 0.006849 |
| left-distance >= 5 and right-weight <= 4 and left-weight >= 5 | 0 | 0.006849 |
| right-weight <= 2 and right-distance <= 3 and left-distance >= 2 and left-weight >= 4 | 0 | 0.006849 |
| left-weight >= 3 and right-weight <= 3 and left-distance >= 5 | 0 | 0.006849 |
| right-distance <= 2 and left-distance >= 3 and left-weight >= 4 | 0 | 0.006849 |
| right-weight <= 2 and right-distance <= 2 and left-weight >= 2 | 0 | 0.009546 |
| left-distance >= 4 and right-weight <= 1 and right-distance <= 4 | 0 | 0.010239 |
| left-weight >= 5 and right-distance <= 4 and left-distance >= 3 and right-weight <= 4 | 0 | 0.007705 |
| left-distance >= 4 and right-distance <= 2 and left-weight >= 3 | 0 | 0.006849 |
| left-distance >= 5 and right-distance <= 4 and left-weight >= 4 | 0 | 0.006849 |
| right-weight <= 3 and left-distance >= 2 and right-distance <= 1 | 0 | 0.004582 |
| right-weight <= 3 and left-weight >= 4 and right-distance <= 4 and left-distance >= 2 | 0 | 0.006186 |
|  | 2 | 0.857143 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

left-weight|left-distance|right-weight|right-distance|target
---|---|---|---|---
(-inf-1.5]|(2.5-inf)|(2.5-inf)|(2.5-inf)|2
(2.5-inf)|(2.5-inf)|(2.5-inf)|(2.5-inf)|0
(1.5-2.5]|(2.5-inf)|(2.5-inf)|(2.5-inf)|2
(-inf-1.5]|(1.5-2.5]|(2.5-inf)|(2.5-inf)|2
(1.5-2.5]|(1.5-2.5]|(2.5-inf)|(2.5-inf)|2
(2.5-inf)|(1.5-2.5]|(2.5-inf)|(2.5-inf)|2
(1.5-2.5]|(-inf-1.5]|(2.5-inf)|(2.5-inf)|2
(-inf-1.5]|(2.5-inf)|(1.5-2.5]|(2.5-inf)|2
(2.5-inf)|(2.5-inf)|(1.5-2.5]|(2.5-inf)|0
(1.5-2.5]|(2.5-inf)|(1.5-2.5]|(2.5-inf)|0
(-inf-1.5]|(-inf-1.5]|(2.5-inf)|(2.5-inf)|2
(2.5-inf)|(-inf-1.5]|(2.5-inf)|(2.5-inf)|2
(1.5-2.5]|(1.5-2.5]|(1.5-2.5]|(2.5-inf)|2
(2.5-inf)|(1.5-2.5]|(1.5-2.5]|(2.5-inf)|0
(1.5-2.5]|(2.5-inf)|(2.5-inf)|(-inf-2.5]|0
(2.5-inf)|(2.5-inf)|(2.5-inf)|(-inf-2.5]|0
(-inf-1.5]|(2.5-inf)|(2.5-inf)|(-inf-2.5]|2
(-inf-1.5]|(1.5-2.5]|(1.5-2.5]|(2.5-inf)|2
(-inf-1.5]|(-inf-1.5]|(1.5-2.5]|(2.5-inf)|2
(1.5-2.5]|(1.5-2.5]|(2.5-inf)|(-inf-2.5]|2
(-inf-1.5]|(2.5-inf)|(-inf-1.5]|(2.5-inf)|0
(2.5-inf)|(2.5-inf)|(-inf-1.5]|(2.5-inf)|0
(1.5-2.5]|(2.5-inf)|(-inf-1.5]|(2.5-inf)|0
(1.5-2.5]|(-inf-1.5]|(1.5-2.5]|(2.5-inf)|2
(-inf-1.5]|(1.5-2.5]|(2.5-inf)|(-inf-2.5]|2
(2.5-inf)|(-inf-1.5]|(1.5-2.5]|(2.5-inf)|2
(2.5-inf)|(1.5-2.5]|(2.5-inf)|(-inf-2.5]|0
(1.5-2.5]|(1.5-2.5]|(-inf-1.5]|(2.5-inf)|1
(1.5-2.5]|(2.5-inf)|(1.5-2.5]|(-inf-2.5]|0
(1.5-2.5]|(-inf-1.5]|(2.5-inf)|(-inf-2.5]|2
(2.5-inf)|(2.5-inf)|(1.5-2.5]|(-inf-2.5]|0
(-inf-1.5]|(2.5-inf)|(1.5-2.5]|(-inf-2.5]|0
(2.5-inf)|(1.5-2.5]|(-inf-1.5]|(2.5-inf)|0
(-inf-1.5]|(1.5-2.5]|(-inf-1.5]|(2.5-inf)|2
(-inf-1.5]|(-inf-1.5]|(2.5-inf)|(-inf-2.5]|2
(2.5-inf)|(-inf-1.5]|(2.5-inf)|(-inf-2.5]|2
(-inf-1.5]|(1.5-2.5]|(1.5-2.5]|(-inf-2.5]|2
(1.5-2.5]|(-inf-1.5]|(-inf-1.5]|(2.5-inf)|2
(2.5-inf)|(1.5-2.5]|(1.5-2.5]|(-inf-2.5]|0
(1.5-2.5]|(1.5-2.5]|(1.5-2.5]|(-inf-2.5]|1
(-inf-1.5]|(-inf-1.5]|(-inf-1.5]|(2.5-inf)|2
(2.5-inf)|(-inf-1.5]|(-inf-1.5]|(2.5-inf)|0
(1.5-2.5]|(-inf-1.5]|(1.5-2.5]|(-inf-2.5]|2
(-inf-1.5]|(2.5-inf)|(-inf-1.5]|(-inf-2.5]|0
(2.5-inf)|(-inf-1.5]|(1.5-2.5]|(-inf-2.5]|0
(-inf-1.5]|(-inf-1.5]|(1.5-2.5]|(-inf-2.5]|2
(1.5-2.5]|(2.5-inf)|(-inf-1.5]|(-inf-2.5]|0
(2.5-inf)|(2.5-inf)|(-inf-1.5]|(-inf-2.5]|0
(1.5-2.5]|(1.5-2.5]|(-inf-1.5]|(-inf-2.5]|0
(-inf-1.5]|(1.5-2.5]|(-inf-1.5]|(-inf-2.5]|0
(2.5-inf)|(1.5-2.5]|(-inf-1.5]|(-inf-2.5]|0
(1.5-2.5]|(-inf-1.5]|(-inf-1.5]|(-inf-2.5]|1
(-inf-1.5]|(-inf-1.5]|(-inf-1.5]|(-inf-2.5]|2
(2.5-inf)|(-inf-1.5]|(-inf-1.5]|(-inf-2.5]|0

## JRip

Decision list:

rules | predicted class
---|---
(right-distance <= 2) and (left-distance <= 2) and (right-weight <= 2) and (left-weight <= 1) and (left-distance >= 2)|1 (4.0/2.0)
(right-distance <= 2) and (left-weight >= 2) and (left-weight <= 2) and (right-weight <= 2) and (left-distance <= 1)|1 (4.0/2.0)
(left-weight >= 4) and (right-weight >= 4) and (right-distance <= 1) and (left-distance <= 1)|1 (3.0/1.0)
(left-distance >= 4) and (right-weight >= 4) and (left-weight <= 1) and (right-distance <= 1)|1 (4.0/2.0)
(left-distance <= 2) and (right-weight <= 2) and (left-weight >= 4) and (right-distance >= 4) and (left-weight <= 4) and (right-distance <= 4)|1 (4.0/2.0)
(right-weight <= 2) and (left-distance >= 3) and (left-weight >= 3) and (right-distance <= 4)|0 (63.0/0.0)
(right-distance <= 2) and (left-distance >= 3) and (left-weight >= 3) and (right-weight <= 4)|0 (29.0/0.0)
(right-distance <= 2) and (left-distance >= 2) and (right-weight <= 1)|0 (19.0/0.0)
(left-distance >= 4) and (left-weight >= 4) and (right-weight <= 3)|0 (20.0/0.0)
(right-weight <= 2) and (left-weight >= 2) and (right-distance <= 3) and (left-distance >= 3)|0 (10.0/0.0)
(right-distance <= 1) and (left-weight >= 2) and (left-distance >= 3)|0 (14.0/0.0)
(left-weight >= 3) and (left-distance >= 2) and (right-weight <= 1)|0 (13.0/0.0)
(left-weight >= 4) and (right-distance <= 3) and (left-distance >= 4)|0 (12.0/0.0)
(right-weight <= 2) and (left-weight >= 3) and (right-distance <= 1)|0 (6.0/0.0)
(right-weight <= 3) and (right-distance <= 3) and (left-distance >= 2) and (left-weight >= 5)|0 (5.0/0.0)
(left-distance >= 3) and (left-weight >= 2) and (right-weight <= 1)|0 (6.0/0.0)
(left-weight >= 3) and (left-distance >= 2) and (right-distance <= 1)|0 (6.0/0.0)
(right-distance <= 3) and (left-weight >= 4) and (right-weight <= 1)|0 (4.0/0.0)
(left-distance >= 5) and (right-weight <= 3) and (right-distance <= 3) and (left-weight >= 2)|0 (3.0/0.0)
(left-distance >= 4) and (right-distance <= 1)|0 (4.0/0.0)
(left-distance >= 3) and (right-weight <= 2) and (left-weight >= 4)|0 (2.0/0.0)
(left-distance >= 5) and (right-weight <= 4) and (left-weight >= 5)|0 (2.0/0.0)
(right-weight <= 2) and (right-distance <= 3) and (left-distance >= 2) and (left-weight >= 4)|0 (2.0/0.0)
(left-weight >= 3) and (right-weight <= 3) and (left-distance >= 5)|0 (2.0/0.0)
(right-distance <= 2) and (left-distance >= 3) and (left-weight >= 4)|0 (2.0/0.0)
(right-weight <= 2) and (right-distance <= 2) and (left-weight >= 2)|0 (7.0/3.0)
(left-distance >= 4) and (right-weight <= 1) and (right-distance <= 4)|0 (3.0/0.0)
(left-weight >= 5) and (right-distance <= 4) and (left-distance >= 3) and (right-weight <= 4)|0 (4.0/1.0)
(left-distance >= 4) and (right-distance <= 2) and (left-weight >= 3)|0 (2.0/0.0)
(left-distance >= 5) and (right-distance <= 4) and (left-weight >= 4)|0 (2.0/0.0)
(right-weight <= 3) and (left-distance >= 2) and (right-distance <= 1)|0 (3.0/1.0)
(right-weight <= 3) and (left-weight >= 4) and (right-distance <= 4) and (left-distance >= 2)|0 (5.0/2.0)
|2 (289.0/40.0)


## PART

Decision list:

rules | predicted class
---|---
right-weight <= 2 AND left-distance > 2 AND left-weight > 1 AND left-weight > 2 AND right-distance <= 4|0 (63.0)
left-distance <= 1 AND right-weight > 1 AND right-distance > 2|2 (51.0)
left-weight <= 1 AND right-distance > 1 AND right-weight > 2|2 (48.0)
left-distance > 3 AND right-distance <= 2 AND left-weight > 2|0 (28.0)
right-weight > 3 AND right-distance > 3 AND left-distance <= 3|2 (31.0)
left-weight > 3 AND right-weight <= 3 AND left-distance > 3|0 (20.0)
left-weight > 4 AND right-distance <= 4 AND right-weight <= 4 AND right-weight <= 2|0 (12.0)
left-distance <= 1 AND right-weight > 3 AND left-weight <= 3|2 (10.0)
right-distance <= 1 AND left-distance > 1 AND left-weight > 1 AND right-weight <= 4 AND right-weight <= 3|0 (18.0)
right-weight <= 1 AND left-distance > 1 AND left-weight > 1 AND left-distance > 2|0 (17.0)
right-distance > 3 AND left-weight <= 3 AND right-weight <= 3 AND left-distance <= 4 AND left-weight <= 2 AND right-distance > 4|2 (14.0)
right-distance > 3 AND left-weight <= 4 AND right-weight > 2 AND left-weight > 2 AND left-distance <= 4|2 (14.0/2.0)
left-distance > 2 AND left-weight > 3 AND right-distance <= 4 AND right-distance > 2 AND left-distance <= 4|0 (12.0/3.0)
right-distance <= 1 AND left-distance > 2 AND left-weight <= 1|0 (15.0/6.0)
left-weight <= 2 AND right-distance > 2 AND right-weight > 2 AND left-distance <= 4|2 (13.0)
left-distance > 2 AND right-distance > 1 AND left-weight > 3 AND right-distance <= 4|0 (13.0)
right-distance <= 1 AND left-distance <= 2 AND left-weight <= 2|2 (12.0/6.0)
right-distance <= 1 AND left-distance > 1|0 (14.0)
right-weight > 4 AND left-distance <= 4|2 (14.0/2.0)
right-weight > 3 AND right-weight <= 4 AND left-distance <= 3|2 (13.0/4.0)
right-weight <= 4 AND right-distance <= 3 AND left-distance > 3 AND left-distance > 4|0 (12.0/2.0)
right-weight > 3 AND right-weight > 4|2 (9.0/3.0)
left-weight <= 2 AND left-distance > 1 AND right-distance > 2 AND right-weight > 1|2 (15.0/4.0)
right-weight <= 3 AND left-distance > 3|0 (11.0/2.0)
left-weight > 1 AND right-weight <= 2 AND left-distance > 1 AND right-weight > 1|0 (13.0/7.0)
left-weight <= 2 AND left-distance > 1|2 (14.0/8.0)
left-weight > 2 AND right-weight <= 2 AND left-distance > 1|0 (9.0)
left-weight > 2 AND right-distance > 3|2 (13.0/6.0)
left-weight > 2 AND left-weight <= 3|0 (11.0/7.0)
left-weight > 3|0 (11.0/4.0)
|2 (8.0/1.0)


## J48 Decision Tree

* left-distance <= 2
	* right-weight <= 1
		* left-weight <= 2
			* right-distance <= 2: 0 (7.0/4.0)
			* right-distance > 2: 2 (8.0/1.0)
		* left-weight > 2: 0 (21.0/5.0)
	* right-weight > 1
		* right-distance <= 2
			* left-weight <= 1: 2 (12.0/1.0)
			* left-weight > 1
				* left-distance <= 1: 2 (21.0/7.0)
				* left-distance > 1: 0 (21.0/9.0)
		* right-distance > 2: 2 (82.0/4.0)
* left-distance > 2
	* left-weight <= 2
		* right-distance <= 1: 0 (22.0/4.0)
		* right-distance > 1
			* right-weight <= 1: 0 (18.0/4.0)
			* right-weight > 1
				* right-distance <= 2
					* right-weight <= 3: 0 (8.0/5.0)
					* right-weight > 3: 2 (5.0/1.0)
				* right-distance > 2: 2 (47.0/4.0)
	* left-weight > 2
		* right-weight <= 2: 0 (62.0/1.0)
		* right-weight > 2
			* right-distance <= 3: 0 (53.0/5.0)
			* right-distance > 3
				* left-weight <= 3: 2 (11.0/1.0)
				* left-weight > 3
					* left-distance <= 3: 2 (7.0/2.0)
					* left-distance > 3: 0 (14.0/4.0)


