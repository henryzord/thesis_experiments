# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| V2 >= 0.5 and V1 < 0.5 and V7 < 0.5 | 4 | 0.091390 |
| V2 < 0.5 and V4 >= 0.5 and V5 < 0.5 | 3 | 0.079753 |
| V2 < 0.5 and V4 < 0.5 and V1 >= 0.5 and V7 < 0.5 | 7 | 0.077340 |
| V2 >= 0.5 and V1 >= 0.5 and V3 < 0.5 and V5 < 0.5 | 5 | 0.067641 |
| V2 >= 0.5 and V1 >= 0.5 and V3 < 0.5 and V5 >= 0.5 | 6 | 0.052540 |
| V2 < 0.5 and V4 >= 0.5 and V5 >= 0.5 | 2 | 0.051600 |
| V2 < 0.5 and V4 < 0.5 and V1 < 0.5 | 1 | 0.049969 |
| V2 >= 0.5 and V1 >= 0.5 and V3 >= 0.5 and V4 < 0.5 and V5 >= 0.5 | 0 | 0.044190 |
| V1 > 0.5 and V2 > 0.5 and V3 > 0.5 and V4 > 0.5 and V5 > 0.5 | 8 | 0.032356 |
| V2 >= 0.5 and V1 >= 0.5 and V3 >= 0.5 and V4 >= 0.5 and V5 < 0.5 | 9 | 0.029816 |
| V1 <= 0.5 and V2 > 0.5 and V3 <= 0.5 and V4 > 0.5 and V5 > 0.5 | 6 | 0.012618 |
| V2 >= 0.5 and V1 < 0.5 and V7 >= 0.5 and V5 < 0.5 | 4 | 0.010837 |
| V1 <= 0.5 and V2 > 0.5 and V3 > 0.5 and V4 <= 0.5 and V5 > 0.5 | 0 | 0.009494 |
| V1 <= 0.5 and V2 <= 0.5 and V3 <= 0.5 and V4 > 0.5 and V5 <= 0.5 | 5 | 0.006452 |
| V2 >= 0.5 and V1 >= 0.5 and V3 >= 0.5 and V4 < 0.5 and V5 < 0.5 | 0 | 0.003226 |
| V1 > 0.5 and V2 <= 0.5 and V3 <= 0.5 and V4 <= 0.5 and V5 <= 0.5 | 3 | 0.002694 |
| V2 < 0.5 and V4 < 0.5 and V1 >= 0.5 and V7 >= 0.5 | 7 | 0.002347 |
| V1 > 0.5 and V2 <= 0.5 and V3 <= 0.5 and V4 <= 0.5 and V5 > 0.5 | 0 | 0.000804 |
| V2 >= 0.5 and V1 < 0.5 and V7 >= 0.5 and V5 >= 0.5 | 6 | 0.004692 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| V5 > 0 and V6 <= 0 and V2 <= 0 and V4 > 0 | 2 | 0.058282 |
| V2 <= 0 and V7 <= 0 and V1 > 0 and V6 > 0 | 7 | 0.073880 |
| V5 > 0 and V3 <= 0 and V4 > 0 | 6 | 0.074573 |
| V7 <= 0 and V2 > 0 and V1 <= 0 and V5 <= 0 and V3 > 0 | 4 | 0.083506 |
| V4 > 0 and V3 <= 0 and V1 > 0 | 5 | 0.084519 |
| V4 > 0 and V5 > 0 and V7 > 0 and V6 > 0 | 8 | 0.062637 |
| V4 > 0 and V2 <= 0 and V6 > 0 and V1 > 0 | 3 | 0.117769 |
| V4 > 0 and V6 <= 0 and V2 <= 0 | 3 | 0.017042 |
| V4 > 0 and V5 > 0 and V1 > 0 | 2 | 0.018359 |
| V4 > 0 and V7 <= 0 and V3 > 0 | 4 | 0.026864 |
| V4 > 0 and V3 <= 0 and V7 <= 0 | 4 | 0.038462 |
| V4 > 0 and V3 > 0 and V1 > 0 | 9 | 0.076190 |
| V2 > 0 and V5 > 0 | 0 | 0.131929 |
| V2 > 0 and V3 > 0 and V1 > 0 | 0 | 0.003979 |
| V2 > 0 and V3 <= 0 | 5 | 0.020032 |
| V2 <= 0 and V7 <= 0 and V1 <= 0 | 1 | 0.166667 |
| V2 <= 0 and V6 > 0 and V1 > 0 | 7 | 0.009836 |
| V2 <= 0 and V4 > 0 | 3 | 0.030048 |
| V2 > 0 | 4 | 0.027778 |
| V7 <= 0 | 7 | 0.116129 |
|  | 2 | 0.172414 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| V1 <= 0 and V4 <= 0 and V2 <= 0 and V6 >= 1 and V3 <= 0 | 1 | 0.012384 |
| V1 <= 0 and V4 <= 0 and V2 <= 0 and V6 >= 1 | 1 | 0.041452 |
| V3 <= 0 and V5 >= 1 and V2 >= 1 and V4 >= 1 and V1 <= 0 | 6 | 0.013514 |
| V3 <= 0 and V5 >= 1 and V2 >= 1 and V4 >= 1 and V6 >= 1 and V7 >= 1 | 6 | 0.046478 |
| V3 <= 0 and V5 >= 1 and V2 >= 1 and V4 >= 1 | 6 | 0.006849 |
| V5 >= 1 and V3 <= 0 and V6 >= 1 | 6 | 0.005517 |
| V4 <= 0 and V5 >= 1 and V2 >= 1 and V3 >= 1 | 0 | 0.061891 |
| V2 >= 1 and V7 >= 1 and V3 >= 1 and V5 <= 0 and V1 >= 1 and V4 >= 1 | 9 | 0.037500 |
| V5 >= 1 and V2 >= 1 and V1 >= 1 and V6 >= 1 | 8 | 0.047341 |
| V3 <= 0 and V7 >= 1 and V4 >= 1 and V5 <= 0 and V1 >= 1 and V6 <= 0 | 5 | 0.023697 |
| V3 <= 0 and V7 >= 1 and V2 >= 1 and V1 >= 1 and V4 >= 1 | 5 | 0.065682 |
| V3 <= 0 and V6 >= 1 and V7 >= 1 and V1 <= 0 | 5 | 0.012821 |
| V3 <= 0 and V1 >= 1 and V2 >= 1 | 5 | 0.011086 |
| V6 <= 0 and V5 >= 1 and V2 <= 0 and V4 >= 1 | 2 | 0.098446 |
| V6 <= 0 and V7 >= 1 and V4 <= 0 | 2 | 0.027933 |
| V6 <= 0 and V1 >= 1 and V4 >= 1 and V2 >= 1 | 2 | 0.020178 |
| V4 <= 0 and V2 <= 0 and V7 <= 0 and V6 >= 1 | 7 | 0.152351 |
| V4 <= 0 and V2 <= 0 and V6 <= 0 and V1 >= 1 | 7 | 0.028935 |
| V7 <= 0 and V1 <= 0 and V2 >= 1 and V4 >= 1 | 4 | 0.218978 |
|  | 3 | 0.378151 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

v1|v2|v3|v4|v5|target
---|---|---|---|---|---
(-inf-0.5]|(0.5-inf)|(0.5-inf)|(0.5-inf)|(0.5-inf)|4
(0.5-inf)|(0.5-inf)|(0.5-inf)|(0.5-inf)|(0.5-inf)|8
(-inf-0.5]|(-inf-0.5]|(0.5-inf)|(0.5-inf)|(0.5-inf)|2
(0.5-inf)|(-inf-0.5]|(0.5-inf)|(0.5-inf)|(0.5-inf)|2
(-inf-0.5]|(0.5-inf)|(-inf-0.5]|(0.5-inf)|(0.5-inf)|6
(0.5-inf)|(0.5-inf)|(-inf-0.5]|(0.5-inf)|(0.5-inf)|6
(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|(0.5-inf)|0
(-inf-0.5]|(0.5-inf)|(0.5-inf)|(-inf-0.5]|(0.5-inf)|0
(0.5-inf)|(0.5-inf)|(0.5-inf)|(-inf-0.5]|(0.5-inf)|0
(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|(0.5-inf)|2
(-inf-0.5]|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|(0.5-inf)|1
(0.5-inf)|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|(0.5-inf)|7
(-inf-0.5]|(0.5-inf)|(0.5-inf)|(0.5-inf)|(-inf-0.5]|4
(0.5-inf)|(0.5-inf)|(0.5-inf)|(0.5-inf)|(-inf-0.5]|9
(0.5-inf)|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|6
(-inf-0.5]|(-inf-0.5]|(0.5-inf)|(0.5-inf)|(-inf-0.5]|3
(0.5-inf)|(-inf-0.5]|(0.5-inf)|(0.5-inf)|(-inf-0.5]|3
(0.5-inf)|(0.5-inf)|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|5
(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|0
(-inf-0.5]|(0.5-inf)|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|4
(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|5
(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|0
(0.5-inf)|(0.5-inf)|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|0
(-inf-0.5]|(0.5-inf)|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|4
(-inf-0.5]|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|1
(0.5-inf)|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|7
(0.5-inf)|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|5
(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|1
(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|3

## JRip

Decision list:

rules | predicted class
---|---
(V1 <= 0) and (V4 <= 0) and (V2 <= 0) and (V6 >= 1) and (V3 <= 0)|1 (4.0/0.0)
(V1 <= 0) and (V4 <= 0) and (V2 <= 0) and (V6 >= 1)|1 (21.0/4.0)
(V3 <= 0) and (V5 >= 1) and (V2 >= 1) and (V4 >= 1) and (V1 <= 0)|6 (4.0/0.0)
(V3 <= 0) and (V5 >= 1) and (V2 >= 1) and (V4 >= 1) and (V6 >= 1) and (V7 >= 1)|6 (18.0/2.0)
(V3 <= 0) and (V5 >= 1) and (V2 >= 1) and (V4 >= 1)|6 (6.0/2.0)
(V5 >= 1) and (V3 <= 0) and (V6 >= 1)|6 (7.0/3.0)
(V4 <= 0) and (V5 >= 1) and (V2 >= 1) and (V3 >= 1)|0 (23.0/3.0)
(V2 >= 1) and (V7 >= 1) and (V3 >= 1) and (V5 <= 0) and (V1 >= 1) and (V4 >= 1)|9 (24.0/9.0)
(V5 >= 1) and (V2 >= 1) and (V1 >= 1) and (V6 >= 1)|8 (22.0/7.0)
(V3 <= 0) and (V7 >= 1) and (V4 >= 1) and (V5 <= 0) and (V1 >= 1) and (V6 <= 0)|5 (5.0/0.0)
(V3 <= 0) and (V7 >= 1) and (V2 >= 1) and (V1 >= 1) and (V4 >= 1)|5 (19.0/2.0)
(V3 <= 0) and (V6 >= 1) and (V7 >= 1) and (V1 <= 0)|5 (6.0/2.0)
(V3 <= 0) and (V1 >= 1) and (V2 >= 1)|5 (6.0/2.0)
(V6 <= 0) and (V5 >= 1) and (V2 <= 0) and (V4 >= 1)|2 (19.0/0.0)
(V6 <= 0) and (V7 >= 1) and (V4 <= 0)|2 (4.0/0.0)
(V6 <= 0) and (V1 >= 1) and (V4 >= 1) and (V2 >= 1)|2 (6.0/2.0)
(V4 <= 0) and (V2 <= 0) and (V7 <= 0) and (V6 >= 1)|7 (25.0/2.0)
(V4 <= 0) and (V2 <= 0) and (V6 <= 0) and (V1 >= 1)|7 (6.0/1.0)
(V7 <= 0) and (V1 <= 0) and (V2 >= 1) and (V4 >= 1)|4 (30.0/0.0)
|3 (88.0/50.0)


## PART

Decision list:

rules | predicted class
---|---
V5 > 0 AND V6 <= 0 AND V2 <= 0 AND V4 > 0|2 (19.0)
V2 <= 0 AND V7 <= 0 AND V1 > 0 AND V6 > 0|7 (30.0/4.0)
V5 > 0 AND V3 <= 0 AND V4 > 0|6 (29.0/4.0)
V7 <= 0 AND V2 > 0 AND V1 <= 0 AND V5 <= 0 AND V3 > 0|4 (23.0/1.0)
V4 > 0 AND V3 <= 0 AND V1 > 0|5 (25.0/2.0)
V4 > 0 AND V5 > 0 AND V7 > 0 AND V6 > 0|8 (29.0/11.0)
V4 > 0 AND V2 <= 0 AND V6 > 0 AND V1 > 0|3 (26.0/2.0)
V4 > 0 AND V6 <= 0 AND V2 <= 0|3 (9.0/4.0)
V4 > 0 AND V5 > 0 AND V1 > 0|2 (7.0/3.0)
V4 > 0 AND V7 <= 0 AND V3 > 0|4 (9.0/2.0)
V4 > 0 AND V3 <= 0 AND V7 <= 0|4 (6.0)
V4 > 0 AND V3 > 0 AND V1 > 0|9 (24.0/9.0)
V2 > 0 AND V5 > 0|0 (28.0/7.0)
V2 > 0 AND V3 > 0 AND V1 > 0|0 (9.0/6.0)
V2 > 0 AND V3 <= 0|5 (8.0/3.0)
V2 <= 0 AND V7 <= 0 AND V1 <= 0|1 (25.0/5.0)
V2 <= 0 AND V6 > 0 AND V1 > 0|7 (11.0/8.0)
V2 <= 0 AND V4 > 0|3 (7.0/2.0)
V2 > 0|4 (7.0/3.0)
V7 <= 0|7 (6.0/1.0)
|2 (6.0/2.0)


## SimpleCart Decision Tree

* V2 < 0.5
	* V4 < 0.5
		* V1 < 0.5: 1(22.0/7.0)
		* V1 >= 0.5
			* V7 < 0.5: 7(28.0/3.0)
			* V7 >= 0.5: 7(3.0/10.0)
	* V4 >= 0.5
		* V5 < 0.5: 3(35.0/13.0)
		* V5 >= 0.5: 2(20.0/4.0)
* V2 >= 0.5
	* V1 < 0.5
		* V7 < 0.5: 4(33.0/3.0)
		* V7 >= 0.5
			* V5 < 0.5: 4(6.0/5.0)
			* V5 >= 0.5: 6(4.0/7.0)
	* V1 >= 0.5
		* V3 < 0.5
			* V5 < 0.5: 5(25.0/3.0)
			* V5 >= 0.5: 6(22.0/6.0)
		* V3 >= 0.5
			* V4 < 0.5
				* V5 < 0.5: 0(3.0/6.0)
				* V5 >= 0.5: 0(17.0/3.0)
			* V4 >= 0.5
				* V5 < 0.5: 9(16.0/11.0)
				* V5 >= 0.5: 8(17.0/11.0)


