# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| V1 >= 6.5 | 0 | 0.640401 |
| V1 <= 6.0 and V2 <= 4.0 | 0 | 0.369503 |
| V1 <= 6.5 and V2 > 4.5 | 0 | 0.262383 |
| V1 < 6.5 and V2 >= 4.5 and V4 >= 49.5 and V2 >= 18.0 | 1 | 0.013763 |
| V1 < 6.5 and V2 >= 4.5 and V4 < 49.5 and V4 >= 19.0 and V2 >= 6.5 | 1 | 0.045150 |
| V1 <= 6.0 and V2 > 4.0 and V4 <= 49.0 and V4 <= 19.0 | 1 | 0.023333 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| V1 > 6.5 and V2 <= 2.5 and V2 <= 1.5 | 0 | 0.314152 |
| V1 > 6.5 | 0 | 0.565971 |
| V2 <= 4.5 | 0 | 0.359209 |
| V4 > 49.5 and V2 <= 10.5 | 0 | 0.095128 |
| V4 <= 19 and V2 <= 5.5 and V1 > 2.5 | 1 | 0.310345 |
|  | 1 | 0.689119 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| V1 <= 6 and V2 >= 5 and V4 <= 42 | 1 | 0.064870 |
| V1 <= 6 and V2 >= 11 and V4 <= 71 | 1 | 0.012671 |
| V1 <= 9 and V2 >= 26 | 1 | 0.011802 |
|  | 0 | 0.857860 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

v1|v2|target
---|---|---
(6.5-inf)|(4.5-inf)|0
(-inf-6.5]|(4.5-inf)|0
(6.5-inf)|(-inf-4.5]|0
(-inf-6.5]|(-inf-4.5]|0

## JRip

Decision list:

rules | predicted class
---|---
(V1 <= 6) and (V2 >= 5) and (V4 <= 42)|1 (87.0/32.0)
(V1 <= 6) and (V2 >= 11) and (V4 <= 71)|1 (19.0/6.0)
(V1 <= 9) and (V2 >= 26)|1 (8.0/1.0)
|0 (559.0/85.0)


## PART

Decision list:

rules | predicted class
---|---
V1 > 6.5 AND V2 <= 2.5 AND V2 <= 1.5|0 (81.0/4.0)
V1 > 6.5|0 (267.0/33.0)
V2 <= 4.5|0 (159.0/41.0)
V4 > 49.5 AND V2 <= 10.5|0 (25.0/1.0)
V4 <= 19 AND V2 <= 5.5 AND V1 > 2.5|1 (6.0)
|1 (135.0/60.0)


## J48 Decision Tree

* V1 <= 6.0
	* V2 <= 4.0: 0 (159.0/41.0)
	* V2 > 4.0
		* V4 <= 49.0
			* V4 <= 19.0: 1 (16.0/2.0)
			* V4 > 19.0
				* V2 <= 6.0: 0 (35.0/14.0)
				* V2 > 6.0: 1 (51.0/16.0)
		* V4 > 49.0
			* V2 <= 18.0: 0 (50.0/9.0)
			* V2 > 18.0: 1 (14.0/4.0)
* V1 > 6.0: 0 (348.0/37.0)


## SimpleCart Decision Tree

* V1 < 6.5
	* V2 < 4.5: 0(118.0/41.0)
	* V2 >= 4.5
		* V4 < 49.5
			* V4 < 19.0: 1(14.0/2.0)
			* V4 >= 19.0
				* V2 < 6.5: 0(21.0/14.0)
				* V2 >= 6.5: 1(35.0/16.0)
		* V4 >= 49.5
			* V2 < 18.0: 0(41.0/9.0)
			* V2 >= 18.0: 1(10.0/4.0)
* V1 >= 6.5: 0(311.0/37.0)


