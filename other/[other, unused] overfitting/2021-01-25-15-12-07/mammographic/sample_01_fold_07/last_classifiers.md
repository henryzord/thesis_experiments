# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 0 | 0.537572 |
| BI-RADS > 4.5 and Age > 39.5 and Age <= 64.5 and Shape > 2.5 and Shape <= 3.5 | 1 | 0.021763 |
| BI-RADS > 4.5 and Age > 64.5 and Shape > 2.5 and Shape <= 3.5 | 1 | 0.032143 |
| BI-RADS < 4.5 and Shape >= 3.5 and Age >= 69.5 | 1 | 0.029358 |
| BI-RADS < 4.5 and Shape >= 3.5 and Age < 69.5 and Margin >= 3.5 | 1 | 0.043462 |
| BI-RADS > 4.5 and Age > 39.5 and Age <= 64.5 and Shape <= 2.5 | 1 | 0.022551 |
| BI-RADS > 4.5 and Age > 27.5 and Age <= 39.5 and Shape <= 2.5 | 1 | 0.004818 |
| BI-RADS > 4.5 and Age = ? and Shape > 3.5 | 1 | 0.006410 |
| BI-RADS <= 4.5 and Age > 64.5 and Shape > 3.5 | 1 | 0.039039 |
| BI-RADS > 4.5 and Age > 64.5 and Shape > 3.5 | 1 | 0.180639 |
| BI-RADS > 4.5 and Age > 39.5 and Age <= 64.5 and Shape > 3.5 | 1 | 0.169212 |
| BI-RADS > 4.5 and Age > 27.5 and Age <= 39.5 and Shape > 3.5 | 1 | 0.013004 |
| BI-RADS >= 4.5 | 1 | 0.354668 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| BI-RADS <= 4.0 and Shape <= 3.0 | 0 | 0.454355 |
| BI-RADS > 4.0 | 1 | 0.740041 |
| Age <= 69.0 and Margin > 3.0 and BI-RADS > 3.0 | 1 | 0.251824 |
| Age <= 66.0 | 0 | 0.503184 |
|  | 1 | 0.800000 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| BI-RADS >= 5 | 1 | 0.354668 |
| Shape >= 3 and Age >= 62 | 1 | 0.047015 |
|  | 0 | 0.869159 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

bi-rads|age|shape|severity
---|---|---|---
(-inf-4.5]|(64.5-inf)|(3.5-inf)|1
(4.5-inf)|(64.5-inf)|(3.5-inf)|1
?|(64.5-inf)|?|0
(4.5-inf)|(64.5-inf)|?|1
(-inf-4.5]|(64.5-inf)|?|0
?|(39.5-64.5]|(3.5-inf)|0
(4.5-inf)|(39.5-64.5]|(3.5-inf)|1
(-inf-4.5]|(39.5-64.5]|(3.5-inf)|0
(-inf-4.5]|?|(3.5-inf)|0
(4.5-inf)|?|(3.5-inf)|1
(4.5-inf)|(39.5-64.5]|?|1
(-inf-4.5]|(39.5-64.5]|?|0
(4.5-inf)|(27.5-39.5]|(3.5-inf)|1
(-inf-4.5]|(27.5-39.5]|(3.5-inf)|0
(4.5-inf)|(64.5-inf)|(2.5-3.5]|1
(-inf-4.5]|(64.5-inf)|(2.5-3.5]|0
(-inf-4.5]|(39.5-64.5]|(2.5-3.5]|0
(4.5-inf)|(39.5-64.5]|(2.5-3.5]|1
(-inf-4.5]|(27.5-39.5]|(2.5-3.5]|0
(4.5-inf)|(64.5-inf)|(-inf-2.5]|1
(-inf-4.5]|(64.5-inf)|(-inf-2.5]|0
(-inf-4.5]|(-inf-27.5]|(2.5-3.5]|0
(4.5-inf)|(39.5-64.5]|(-inf-2.5]|1
(-inf-4.5]|(39.5-64.5]|(-inf-2.5]|0
(4.5-inf)|(27.5-39.5]|(-inf-2.5]|1
(-inf-4.5]|(27.5-39.5]|(-inf-2.5]|0
(-inf-4.5]|(-inf-27.5]|(-inf-2.5]|0

## JRip

Decision list:

rules | predicted class
---|---
(BI-RADS >= 5)|1 (328.0/40.0)
(Shape >= 3) and (Age >= 62)|1 (68.0/26.0)
|0 (469.0/70.0)


## PART

Decision list:

rules | predicted class
---|---
BI-RADS <= 4.0 AND Shape <= 3.0|0 (414.96/47.35)
BI-RADS > 4.0|1 (329.11/40.73)
Age <= 69.0 AND Margin > 3.0 AND BI-RADS > 3.0|1 (75.75/35.92)
Age <= 66.0|0 (26.45/7.16)
|1 (18.74/1.45)


## SimpleCart Decision Tree

* BI-RADS < 4.5
	* Shape < 3.5: 0(367.6/47.34)
	* Shape >= 3.5
		* Age < 69.5
			* Margin < 3.5: 0(14.62/5.65)
			* Margin >= 3.5: 1(43.25/40.93)
		* Age >= 69.5: 1(15.36/1.45)
* BI-RADS >= 4.5: 1(288.38/40.38)


