# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| V1 >= 6.5 | 0 | 0.634420 |
| V1 <= 6.5 and V2 <= 4.5 and V3 <= 1125 | 0 | 0.371920 |
| V1 <= 6.5 and V2 > 4.5 and V3 > 1125 | 0 | 0.272811 |
| V1 <= 6 and V2 > 4 and V4 <= 49 and V2 > 6 | 1 | 0.052370 |
| V1 <= 6 and V2 > 4 and V4 <= 49 and V2 <= 6 and V2 <= 5 and V4 <= 33 | 1 | 0.011232 |
| V1 <= 6 and V2 > 4 and V4 <= 49 and V2 <= 6 and V2 > 5 and V1 <= 2 | 1 | 0.011191 |
| V1 <= 6 and V2 > 4 and V4 > 49 and V2 > 12 | 1 | 0.016150 |
| V1 < 6.5 and V2 >= 4.5 and V4 < 49.5 and V2 < 6.5 and V4 < 33.5 | 1 | 0.021485 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| V1 > 6 | 0 | 0.634420 |
| V2 <= 15 and V4 <= 49 and V2 <= 6 | 0 | 0.399362 |
| V4 > 49 and V2 <= 17 | 0 | 0.183715 |
|  | 1 | 0.889503 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| V1 <= 6 and V2 >= 5 and V4 <= 43 | 1 | 0.064252 |
| V1 <= 5 and V2 >= 13 | 1 | 0.020177 |
|  | 0 | 0.853577 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

v1|v2|v3|target
---|---|---|---
(6.5-inf)|(4.5-inf)|(1125-inf)|0
(-inf-6.5]|(4.5-inf)|(1125-inf)|0
(-inf-6.5]|(-inf-4.5]|(-inf-1125]|0
(6.5-inf)|(-inf-4.5]|(-inf-1125]|0

## JRip

Decision list:

rules | predicted class
---|---
(V1 <= 6) and (V2 >= 5) and (V4 <= 43)|1 (88.0/33.0)
(V1 <= 5) and (V2 >= 13)|1 (29.0/11.0)
|0 (557.0/88.0)


## PART

Decision list:

rules | predicted class
---|---
V1 > 6|0 (228.0/21.0)
V2 <= 15 AND V4 <= 49 AND V2 <= 6|0 (133.0/50.0)
V4 > 49 AND V2 <= 17|0 (42.0/5.0)
|1 (47.0/15.0)


## J48 Decision Tree

* V1 <= 6
	* V2 <= 4: 0 (162.0/42.0)
	* V2 > 4
		* V4 <= 49
			* V2 <= 6
				* V2 <= 5
					* V4 <= 33: 1 (11.0/3.0)
					* V4 > 33: 0 (7.0/2.0)
				* V2 > 5
					* V1 <= 2: 1 (14.0/5.0)
					* V1 > 2: 0 (16.0/5.0)
			* V2 > 6: 1 (57.0/17.0)
		* V4 > 49
			* V2 <= 12: 0 (39.0/4.0)
			* V2 > 12: 1 (27.0/12.0)
* V1 > 6: 0 (341.0/36.0)


## SimpleCart Decision Tree

* V1 < 6.5
	* V2 < 4.5: 0(120.0/42.0)
	* V2 >= 4.5
		* V4 < 49.5
			* V2 < 6.5
				* V4 < 33.5: 1(18.0/11.0)
				* V4 >= 33.5: 0(13.0/6.0)
			* V2 >= 6.5: 1(40.0/17.0)
		* V4 >= 49.5: 0(47.0/19.0)
* V1 >= 6.5: 0(305.0/36.0)


