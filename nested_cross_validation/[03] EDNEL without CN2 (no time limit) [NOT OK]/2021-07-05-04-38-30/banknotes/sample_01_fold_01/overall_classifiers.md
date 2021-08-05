# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 0 | 0.555105 |
| variance < 0.320165 and skewness >= 5.86535 and variance < -3.4833999999999996 | 1 | 0.047327 |
| variance >= 0.320165 and curtosis >= -4.38605 and variance < 1.5922 and curtosis >= -2.2721999999999998 and entropy >= 0.22994 and curtosis < 1.8736000000000002 | 1 | 0.017319 |
| variance > -0.4031 and variance <= 0.320165 and skewness > -2.4149 and skewness <= 5.1608 and curtosis > -4.42545 and curtosis <= 8.83885 | 1 | 0.047780 |
| variance > 0.31803 and curtosis > -4.3882 and variance <= 2.031 and curtosis > -2.2726 and entropy > 0.087054 and curtosis <= -0.023425 | 1 | 0.015805 |
| variance >= 0.320165 and curtosis >= -4.38605 and variance < 1.5922 and curtosis < -2.2721999999999998 | 1 | 0.028605 |
| variance < 0.320165 and skewness < 5.86535 and curtosis >= 6.21865 and skewness < -4.6745 | 1 | 0.144830 |
| variance <= 0.31803 and skewness <= 5.8561 and curtosis <= 6.2169 | 1 | 0.322456 |
| variance >= 0.320165 and curtosis < -4.38605 and variance < 3.30405 | 1 | 0.040616 |
| variance > 0.31803 and curtosis > -4.3882 and variance <= 2.031 and curtosis <= -2.2726 and skewness <= 5.6946 | 1 | 0.035211 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| variance > 0.320165 and curtosis > -4.38605 and variance > 2.03655 | 0 | 0.412206 |
| skewness > 5.1608 and variance > -3.36765 | 0 | 0.252044 |
| variance <= 0.320165 and curtosis <= 3.0642 | 1 | 0.730047 |
| skewness <= -5.1215 and variance <= -0.454565 | 1 | 0.572491 |
| curtosis > 0.209635 and variance > -0.365255 | 0 | 0.528319 |
| curtosis <= 6.72675 and curtosis <= -1.3918 | 1 | 0.762500 |
| curtosis <= 6.72675 and skewness <= -0.094161 | 1 | 0.512821 |
|  | 0 | 0.863636 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| variance <= 0.27331 and skewness <= 5.8333 and curtosis <= 6.7156 | 1 | 0.326462 |
| skewness <= 9.6014 and variance <= -1.9966 | 1 | 0.148050 |
| variance <= 1.7331 and skewness <= 4.8856 and curtosis <= -0.031994 | 1 | 0.081791 |
| skewness <= -6.4624 and variance <= -0.90784 | 1 | 0.031117 |
| skewness <= 4.5565 and curtosis <= -0.18794 and variance <= 2.3917 | 1 | 0.007453 |
| skewness <= -0.3104 and curtosis <= 1.6131 and variance <= 0.74428 | 1 | 0.005806 |
|  | 0 | 1.000000 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

variance|skewness|curtosis|class
---|---|---|---
(1.74385-2.3921]|(9.61695-inf)|(-4.42545-8.83885]|0
(0.320165-1.74385]|(9.61695-inf)|(-4.42545-8.83885]|0
(-0.4031-0.320165]|(9.61695-inf)|(-4.42545-8.83885]|0
(2.3921-inf)|(9.61695-inf)|(-4.42545-8.83885]|0
(-2.7952--0.4031]|(9.61695-inf)|(-4.42545-8.83885]|0
(-inf--2.7952]|(-5.5074--2.4149]|(8.83885-inf)|1
(-inf--2.7952]|(5.1608-9.61695]|(-4.42545-8.83885]|1
(1.74385-2.3921]|(5.1608-9.61695]|(-4.42545-8.83885]|0
(0.320165-1.74385]|(5.1608-9.61695]|(-4.42545-8.83885]|0
(2.3921-inf)|(5.1608-9.61695]|(-4.42545-8.83885]|0
(-2.7952--0.4031]|(5.1608-9.61695]|(-4.42545-8.83885]|0
(-0.4031-0.320165]|(5.1608-9.61695]|(-4.42545-8.83885]|0
(-2.7952--0.4031]|(-6.94555--5.5074]|(8.83885-inf)|1
(-inf--2.7952]|(-2.4149-5.1608]|(-4.42545-8.83885]|1
(-inf--2.7952]|(-6.94555--5.5074]|(8.83885-inf)|1
(-0.4031-0.320165]|(-2.4149-5.1608]|(-4.42545-8.83885]|1
(2.3921-inf)|(9.61695-inf)|(-inf--4.42545]|0
(2.3921-inf)|(-2.4149-5.1608]|(-4.42545-8.83885]|0
(-2.7952--0.4031]|(-2.4149-5.1608]|(-4.42545-8.83885]|1
(0.320165-1.74385]|(-2.4149-5.1608]|(-4.42545-8.83885]|0
(1.74385-2.3921]|(-2.4149-5.1608]|(-4.42545-8.83885]|0
(1.74385-2.3921]|(-5.5074--2.4149]|(-4.42545-8.83885]|0
(-0.4031-0.320165]|(-5.5074--2.4149]|(-4.42545-8.83885]|1
(-inf--2.7952]|(-inf--6.94555]|(8.83885-inf)|1
(-2.7952--0.4031]|(-inf--6.94555]|(8.83885-inf)|1
(2.3921-inf)|(5.1608-9.61695]|(-inf--4.42545]|0
(0.320165-1.74385]|(-5.5074--2.4149]|(-4.42545-8.83885]|0
(-2.7952--0.4031]|(-5.5074--2.4149]|(-4.42545-8.83885]|1
(2.3921-inf)|(-5.5074--2.4149]|(-4.42545-8.83885]|0
(2.3921-inf)|(-6.94555--5.5074]|(-4.42545-8.83885]|0
(1.74385-2.3921]|(-2.4149-5.1608]|(-inf--4.42545]|1
(-0.4031-0.320165]|(-6.94555--5.5074]|(-4.42545-8.83885]|0
(-0.4031-0.320165]|(-2.4149-5.1608]|(-inf--4.42545]|1
(0.320165-1.74385]|(-2.4149-5.1608]|(-inf--4.42545]|1
(-2.7952--0.4031]|(-6.94555--5.5074]|(-4.42545-8.83885]|1
(1.74385-2.3921]|(-6.94555--5.5074]|(-4.42545-8.83885]|0
(0.320165-1.74385]|(-6.94555--5.5074]|(-4.42545-8.83885]|0
(-inf--2.7952]|(-inf--6.94555]|(-4.42545-8.83885]|1
(-2.7952--0.4031]|(-inf--6.94555]|(-4.42545-8.83885]|1

## JRip

Decision list:

rules | predicted class
---|---
(variance <= 0.27331) and (skewness <= 5.8333) and (curtosis <= 6.7156)|1 (336.0/2.0)
(skewness <= 9.6014) and (variance <= -1.9966)|1 (123.0/2.0)
(variance <= 1.7331) and (skewness <= 4.8856) and (curtosis <= -0.031994)|1 (63.0/1.0)
(skewness <= -6.4624) and (variance <= -0.90784)|1 (22.0/0.0)
(skewness <= 4.5565) and (curtosis <= -0.18794) and (variance <= 2.3917)|1 (6.0/0.0)
(skewness <= -0.3104) and (curtosis <= 1.6131) and (variance <= 0.74428)|1 (4.0/0.0)
|0 (680.0/0.0)


## PART

Decision list:

rules | predicted class
---|---
variance > 0.320165 AND curtosis > -4.38605 AND variance > 2.03655|0 (385.0)
skewness > 5.1608 AND variance > -3.36765|0 (185.0)
variance <= 0.320165 AND curtosis <= 3.0642|1 (311.0)
skewness <= -5.1215 AND variance <= -0.454565|1 (154.0)
curtosis > 0.209635 AND variance > -0.365255|0 (98.0/2.0)
curtosis <= 6.72675 AND curtosis <= -1.3918|1 (61.0)
curtosis <= 6.72675 AND skewness <= -0.094161|1 (18.0)
|0 (22.0/3.0)


## J48 Decision Tree

* variance <= 0.31803
	* skewness <= 5.8561
		* curtosis <= 6.2169: 1 (328.0/1.0)
		* curtosis > 6.2169
			* skewness <= -4.7076: 1 (118.0/1.0)
			* skewness > -4.7076: 0 (23.0/1.0)
	* skewness > 5.8561
		* variance <= -3.4917: 1 (36.0/1.0)
		* variance > -3.4917: 0 (88.0)
* variance > 0.31803
	* curtosis <= -4.3882
		* skewness <= 7.1328: 1 (29.0)
		* skewness > 7.1328: 0 (9.0)
	* curtosis > -4.3882
		* variance <= 2.031
			* curtosis <= -2.2726
				* skewness <= 5.6946: 1 (25.0)
				* skewness > 5.6946: 0 (4.0)
			* curtosis > -2.2726
				* entropy <= 0.087054: 0 (137.0/1.0)
				* entropy > 0.087054
					* curtosis <= -0.023425: 1 (11.0)
					* curtosis > -0.023425
						* skewness <= -0.30005
							* curtosis <= 3.5573: 1 (3.0)
							* curtosis > 3.5573: 0 (3.0)
						* skewness > -0.30005: 0 (35.0)
		* variance > 2.031: 0 (385.0)


## SimpleCart Decision Tree

* variance < 0.320165
	* skewness < 5.86535
		* curtosis < 6.21865: 1(327.0/1.0)
		* curtosis >= 6.21865
			* skewness < -4.6745: 1(117.0/1.0)
			* skewness >= -4.6745: 0(22.0/1.0)
	* skewness >= 5.86535
		* variance < -3.4833999999999996: 1(35.0/1.0)
		* variance >= -3.4833999999999996: 0(88.0/0.0)
* variance >= 0.320165
	* curtosis < -4.38605
		* variance < 3.30405: 1(29.0/0.0)
		* variance >= 3.30405: 0(9.0/0.0)
	* curtosis >= -4.38605
		* variance < 1.5922
			* curtosis < -2.2721999999999998: 1(22.0/2.0)
			* curtosis >= -2.2721999999999998
				* entropy < 0.22994: 0(111.0/2.0)
				* entropy >= 0.22994
					* curtosis < 1.8736000000000002: 1(13.0/1.0)
					* curtosis >= 1.8736000000000002: 0(14.0/0.0)
		* variance >= 1.5922: 0(435.0/3.0)


