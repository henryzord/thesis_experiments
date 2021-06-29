# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 0 | 0.462366 |
| right-weight > 2.0 and left-distance <= 2.0 | 2 | 0.249227 |
| right-weight > 2.0 and left-distance > 2.0 and left-weight <= 2.0 and right-distance > 2.0 | 2 | 0.135505 |
| right-weight <= 2.0 and left-weight <= 2.0 and left-distance <= 3.0 and right-distance > 1.0 and left-weight <= 1.0 | 2 | 0.051928 |
| right-weight > 2.0 and left-distance > 2.0 and left-weight > 2.0 and right-distance > 3.0 and left-distance <= 3.0 | 2 | 0.042285 |
| left-weight <= 1.5 and left-distance > 2.5 and right-weight > 2.5 and right-distance <= 2.5 | 2 | 0.023337 |
| right-weight > 2.0 and left-distance > 2.0 and left-weight > 2.0 and right-distance > 3.0 and left-distance > 3.0 and left-weight <= 4.0 | 2 | 0.020033 |
| right-weight <= 2.0 and left-weight > 2.0 and left-distance <= 1.0 and right-distance > 3.0 | 2 | 0.022059 |
| right-weight <= 2.0 and left-weight <= 2.0 and left-distance <= 3.0 and right-distance > 1.0 and left-weight > 1.0 and left-distance <= 1.0 | 2 | 0.016862 |
| left-weight > 2.5 and left-distance <= 1.5 and right-weight <= 1.5 and right-distance > 2.5 | 1 | 0.001949 |
| left-weight <= 1.5 and left-distance > 2.5 and right-weight > 1.5 and right-weight <= 2.5 and right-distance > 2.5 | 2 | 0.019608 |
| left-weight > 1.5 and left-weight <= 2.5 and left-distance > 1.5 and left-distance <= 2.5 and right-weight > 1.5 and right-weight <= 2.5 and right-distance > 2.5 | 2 | 0.009901 |
| left-weight > 1.5 and left-weight <= 2.5 and left-distance <= 1.5 and right-weight <= 1.5 and right-distance <= 2.5 | 1 | 0.000969 |
| left-weight <= 1.5 and left-distance > 1.5 and left-distance <= 2.5 and right-weight <= 1.5 and right-distance <= 2.5 | 1 | 0.000969 |
| left-weight <= 1.5 and left-distance > 1.5 and left-distance <= 2.5 and right-weight > 1.5 and right-weight <= 2.5 and right-distance <= 2.5 | 1 | 0.000969 |
| left-weight > 1.5 and left-weight <= 2.5 and left-distance <= 1.5 and right-weight > 1.5 and right-weight <= 2.5 and right-distance <= 2.5 | 1 | 0.000969 |
| left-weight <= 1.5 and left-distance <= 1.5 and right-weight > 1.5 and right-weight <= 2.5 and right-distance <= 2.5 | 2 | 0.006623 |
| left-weight > 2.5 and left-distance <= 1.5 and right-weight > 1.5 and right-weight <= 2.5 and right-distance > 2.5 | 2 | 0.022801 |

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
| right-weight <= 2 and left-distance >= 3 and left-weight >= 3 and right-distance <= 4 | 0 | 0.173554 |
| left-distance >= 4 and left-weight >= 4 and right-distance <= 3 | 0 | 0.090909 |
| left-distance >= 3 and left-weight >= 2 and right-weight <= 1 | 0 | 0.074074 |
| left-distance >= 2 and left-weight >= 3 and right-distance <= 1 | 0 | 0.062500 |
| right-weight <= 3 and right-distance <= 2 and left-weight >= 2 and left-distance >= 4 | 0 | 0.029126 |
| right-distance <= 3 and right-weight <= 1 and left-weight >= 4 | 0 | 0.029126 |
| right-weight <= 3 and left-weight >= 4 and left-distance >= 4 | 0 | 0.038462 |
| right-distance <= 2 and left-distance >= 3 and left-weight >= 3 and right-weight <= 4 | 0 | 0.025974 |
| right-distance <= 2 and right-weight <= 1 and left-distance >= 3 | 0 | 0.019608 |
| right-distance <= 3 and left-weight >= 2 and left-distance >= 2 and right-weight <= 1 | 0 | 0.016393 |
| left-weight >= 3 and left-distance >= 2 and right-weight <= 1 | 0 | 0.019608 |
| right-distance <= 2 and right-weight <= 2 and left-weight >= 3 | 0 | 0.020915 |
| left-distance >= 3 and right-distance <= 1 and left-weight >= 2 | 0 | 0.025974 |
| left-distance >= 5 and right-weight <= 4 and right-distance <= 4 and left-weight >= 3 | 0 | 0.013706 |
| right-weight <= 3 and right-distance <= 3 and left-distance >= 4 | 0 | 0.022113 |
| left-weight >= 5 and left-distance >= 2 and right-distance <= 3 | 0 | 0.016118 |
|  | 2 | 0.788991 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

left-weight|left-distance|right-weight|right-distance|target
---|---|---|---|---
(-inf-1.5]|(2.5-inf)|(2.5-inf)|(2.5-inf)|2
(2.5-inf)|(2.5-inf)|(2.5-inf)|(2.5-inf)|0
(1.5-2.5]|(2.5-inf)|(2.5-inf)|(2.5-inf)|2
(-inf-1.5]|(1.5-2.5]|(2.5-inf)|(2.5-inf)|2
(2.5-inf)|(1.5-2.5]|(2.5-inf)|(2.5-inf)|2
(1.5-2.5]|(1.5-2.5]|(2.5-inf)|(2.5-inf)|2
(1.5-2.5]|(2.5-inf)|(1.5-2.5]|(2.5-inf)|0
(-inf-1.5]|(2.5-inf)|(1.5-2.5]|(2.5-inf)|2
(2.5-inf)|(2.5-inf)|(1.5-2.5]|(2.5-inf)|0
(2.5-inf)|(-inf-1.5]|(2.5-inf)|(2.5-inf)|2
(1.5-2.5]|(-inf-1.5]|(2.5-inf)|(2.5-inf)|2
(-inf-1.5]|(-inf-1.5]|(2.5-inf)|(2.5-inf)|2
(2.5-inf)|(1.5-2.5]|(1.5-2.5]|(2.5-inf)|0
(1.5-2.5]|(1.5-2.5]|(1.5-2.5]|(2.5-inf)|2
(1.5-2.5]|(2.5-inf)|(2.5-inf)|(-inf-2.5]|0
(2.5-inf)|(2.5-inf)|(2.5-inf)|(-inf-2.5]|0
(-inf-1.5]|(1.5-2.5]|(1.5-2.5]|(2.5-inf)|2
(-inf-1.5]|(2.5-inf)|(2.5-inf)|(-inf-2.5]|2
(1.5-2.5]|(1.5-2.5]|(2.5-inf)|(-inf-2.5]|2
(1.5-2.5]|(-inf-1.5]|(1.5-2.5]|(2.5-inf)|2
(-inf-1.5]|(2.5-inf)|(-inf-1.5]|(2.5-inf)|0
(2.5-inf)|(2.5-inf)|(-inf-1.5]|(2.5-inf)|0
(1.5-2.5]|(2.5-inf)|(-inf-1.5]|(2.5-inf)|0
(-inf-1.5]|(-inf-1.5]|(1.5-2.5]|(2.5-inf)|2
(2.5-inf)|(1.5-2.5]|(2.5-inf)|(-inf-2.5]|0
(-inf-1.5]|(1.5-2.5]|(2.5-inf)|(-inf-2.5]|2
(2.5-inf)|(-inf-1.5]|(1.5-2.5]|(2.5-inf)|2
(-inf-1.5]|(1.5-2.5]|(-inf-1.5]|(2.5-inf)|2
(1.5-2.5]|(-inf-1.5]|(2.5-inf)|(-inf-2.5]|2
(2.5-inf)|(2.5-inf)|(1.5-2.5]|(-inf-2.5]|0
(-inf-1.5]|(-inf-1.5]|(2.5-inf)|(-inf-2.5]|2
(2.5-inf)|(-inf-1.5]|(2.5-inf)|(-inf-2.5]|2
(1.5-2.5]|(1.5-2.5]|(-inf-1.5]|(2.5-inf)|0
(1.5-2.5]|(2.5-inf)|(1.5-2.5]|(-inf-2.5]|0
(2.5-inf)|(1.5-2.5]|(-inf-1.5]|(2.5-inf)|0
(-inf-1.5]|(2.5-inf)|(1.5-2.5]|(-inf-2.5]|0
(-inf-1.5]|(-inf-1.5]|(-inf-1.5]|(2.5-inf)|2
(1.5-2.5]|(-inf-1.5]|(-inf-1.5]|(2.5-inf)|2
(1.5-2.5]|(1.5-2.5]|(1.5-2.5]|(-inf-2.5]|0
(2.5-inf)|(-inf-1.5]|(-inf-1.5]|(2.5-inf)|1
(2.5-inf)|(1.5-2.5]|(1.5-2.5]|(-inf-2.5]|0
(-inf-1.5]|(1.5-2.5]|(1.5-2.5]|(-inf-2.5]|1
(2.5-inf)|(-inf-1.5]|(1.5-2.5]|(-inf-2.5]|0
(-inf-1.5]|(2.5-inf)|(-inf-1.5]|(-inf-2.5]|0
(1.5-2.5]|(-inf-1.5]|(1.5-2.5]|(-inf-2.5]|1
(1.5-2.5]|(2.5-inf)|(-inf-1.5]|(-inf-2.5]|0
(2.5-inf)|(2.5-inf)|(-inf-1.5]|(-inf-2.5]|0
(-inf-1.5]|(-inf-1.5]|(1.5-2.5]|(-inf-2.5]|2
(2.5-inf)|(1.5-2.5]|(-inf-1.5]|(-inf-2.5]|0
(1.5-2.5]|(1.5-2.5]|(-inf-1.5]|(-inf-2.5]|0
(-inf-1.5]|(1.5-2.5]|(-inf-1.5]|(-inf-2.5]|1
(-inf-1.5]|(-inf-1.5]|(-inf-1.5]|(-inf-2.5]|2
(1.5-2.5]|(-inf-1.5]|(-inf-1.5]|(-inf-2.5]|1
(2.5-inf)|(-inf-1.5]|(-inf-1.5]|(-inf-2.5]|0

## JRip

Decision list:

rules | predicted class
---|---
(right-weight <= 2) and (left-distance >= 3) and (left-weight >= 3) and (right-distance <= 4)|0 (63.0/0.0)
(left-distance >= 4) and (left-weight >= 4) and (right-distance <= 3)|0 (30.0/0.0)
(left-distance >= 3) and (left-weight >= 2) and (right-weight <= 1)|0 (24.0/0.0)
(left-distance >= 2) and (left-weight >= 3) and (right-distance <= 1)|0 (20.0/0.0)
(right-weight <= 3) and (right-distance <= 2) and (left-weight >= 2) and (left-distance >= 4)|0 (9.0/0.0)
(right-distance <= 3) and (right-weight <= 1) and (left-weight >= 4)|0 (9.0/0.0)
(right-weight <= 3) and (left-weight >= 4) and (left-distance >= 4)|0 (12.0/0.0)
(right-distance <= 2) and (left-distance >= 3) and (left-weight >= 3) and (right-weight <= 4)|0 (8.0/0.0)
(right-distance <= 2) and (right-weight <= 1) and (left-distance >= 3)|0 (6.0/0.0)
(right-distance <= 3) and (left-weight >= 2) and (left-distance >= 2) and (right-weight <= 1)|0 (5.0/0.0)
(left-weight >= 3) and (left-distance >= 2) and (right-weight <= 1)|0 (6.0/0.0)
(right-distance <= 2) and (right-weight <= 2) and (left-weight >= 3)|0 (10.0/2.0)
(left-distance >= 3) and (right-distance <= 1) and (left-weight >= 2)|0 (8.0/0.0)
(left-distance >= 5) and (right-weight <= 4) and (right-distance <= 4) and (left-weight >= 3)|0 (6.0/1.0)
(right-weight <= 3) and (right-distance <= 3) and (left-distance >= 4)|0 (18.0/7.0)
(left-weight >= 5) and (left-distance >= 2) and (right-distance <= 3)|0 (10.0/3.0)
|2 (314.0/66.0)


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

* right-weight <= 2.0
	* left-weight <= 2.0
		* left-distance <= 3.0
			* right-distance <= 1.0: 0 (8.0/3.0)
			* right-distance > 1.0
				* left-weight <= 1.0: 2 (18.0/1.0)
				* left-weight > 1.0
					* left-distance <= 1.0: 2 (7.0/1.0)
					* left-distance > 1.0: 0 (11.0/6.0)
		* left-distance > 3.0: 0 (29.0/7.0)
	* left-weight > 2.0
		* left-distance <= 1.0
			* right-distance <= 3.0: 0 (11.0/2.0)
			* right-distance > 3.0: 2 (9.0/3.0)
		* left-distance > 1.0: 0 (87.0/4.0)
* right-weight > 2.0
	* left-distance <= 2.0: 2 (110.0/16.0)
	* left-distance > 2.0
		* left-weight <= 2.0
			* right-distance <= 2.0
				* left-weight <= 1.0: 2 (15.0/5.0)
				* left-weight > 1.0: 0 (11.0/4.0)
			* right-distance > 2.0: 2 (38.0/1.0)
		* left-weight > 2.0
			* right-distance <= 3.0: 0 (53.0/5.0)
			* right-distance > 3.0
				* left-distance <= 3.0: 2 (13.0/1.0)
				* left-distance > 3.0
					* left-weight <= 4.0: 2 (18.0/9.0)
					* left-weight > 4.0: 0 (9.0/3.0)


