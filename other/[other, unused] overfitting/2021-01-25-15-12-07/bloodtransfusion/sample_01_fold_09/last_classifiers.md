# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 0 | 0.761128 |
| V1 < 6.5 and V2 >= 4.5 and V4 < 49.5 and V2 < 6.5 and V4 < 33.5 | 1 | 0.021485 |
| V1 <= 6.5 and V2 > 4.5 and V4 <= 49.5 and V2 > 6.5 | 1 | 0.052370 |
| V1 < 6.5 and V2 >= 4.5 and V4 >= 49.5 and V2 >= 12.5 and V2 >= 25.0 | 1 | 0.009928 |
| V1 <= 6.5 and V2 > 4.5 and V4 > 49.5 and V2 > 12.5 | 1 | 0.016150 |
| V1 <= 6.5 and V2 > 4.5 and V4 <= 49.5 and V2 <= 6.5 and V2 > 5.5 and V1 <= 2.5 | 1 | 0.011191 |

## Ordered rules

### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| V1 <= 6 and V2 >= 5 and V4 <= 34 | 1 | 0.047046 |
| V1 <= 6 and V2 >= 11 | 1 | 0.028265 |
|  | 0 | 0.846535 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

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
(V1 <= 6) and (V2 >= 5) and (V4 <= 34)|1 (61.0/22.0)
(V1 <= 6) and (V2 >= 11)|1 (55.0/26.0)
|0 (558.0/93.0)


## J48 Decision Tree

* V1 <= 6.5
	* V2 <= 4.5: 0 (162.0/42.0)
	* V2 > 4.5
		* V4 <= 49.5
			* V2 <= 6.5
				* V2 <= 5.5
					* V4 <= 24.5: 1 (8.0/2.0)
					* V4 > 24.5: 0 (10.0/4.0)
				* V2 > 5.5
					* V1 <= 2.5: 1 (14.0/5.0)
					* V1 > 2.5: 0 (16.0/5.0)
			* V2 > 6.5: 1 (57.0/17.0)
		* V4 > 49.5
			* V2 <= 12.5: 0 (39.0/4.0)
			* V2 > 12.5: 1 (27.0/12.0)
* V1 > 6.5: 0 (341.0/36.0)


## SimpleCart Decision Tree

* V1 < 6.5
	* V2 < 4.5: 0(120.0/42.0)
	* V2 >= 4.5
		* V4 < 49.5
			* V2 < 6.5
				* V4 < 33.5: 1(18.0/11.0)
				* V4 >= 33.5: 0(13.0/6.0)
			* V2 >= 6.5: 1(40.0/17.0)
		* V4 >= 49.5
			* V2 < 12.5: 0(35.0/4.0)
			* V2 >= 12.5
				* V2 < 25.0: 0(11.0/9.0)
				* V2 >= 25.0: 1(6.0/1.0)
* V1 >= 6.5: 0(305.0/36.0)


