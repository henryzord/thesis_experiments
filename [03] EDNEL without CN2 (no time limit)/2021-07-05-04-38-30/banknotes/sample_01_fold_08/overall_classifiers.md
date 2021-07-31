# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 0 | 0.555105 |
| variance < 0.320165 and skewness >= 7.5653 and variance < -4.726 | 1 | 0.025605 |
| variance >= 0.320165 and curtosis >= -4.38605 and variance < 1.5922 and curtosis >= -2.2859 and entropy >= 0.081882 and curtosis < 1.85305 | 1 | 0.018962 |
| variance <= 0.320165 and skewness <= 7.5653 and variance > -1.78205 and curtosis > 6.824400000000001 and skewness <= -5.5343 | 1 | 0.017319 |
| variance < 0.320165 and skewness < 7.5653 and variance < -0.38902000000000003 and curtosis < 6.21865 | 1 | 0.298874 |
| variance < 0.320165 and skewness < 7.5653 and variance < -0.38902000000000003 and curtosis >= 6.21865 and skewness < -4.6745 | 1 | 0.145885 |
| variance > -2.7952 and variance <= 0.320165 and skewness > -2.3021 and skewness <= 5.21045 and curtosis > -4.42285 and curtosis <= 8.83885 | 1 | 0.214180 |
| variance > 0.320165 and curtosis <= -4.38605 and skewness <= 7.191800000000001 | 1 | 0.040616 |
| variance <= 0.320165 and skewness <= 7.5653 and variance > -1.78205 and curtosis <= 6.824400000000001 and skewness > 3.9285 and variance > 0.222115 | 1 | 0.004651 |
| variance <= 0.320165 and skewness <= 7.5653 and variance > -1.78205 and curtosis <= 6.824400000000001 and skewness <= 3.9285 | 1 | 0.211762 |
| variance >= 0.320165 and curtosis >= -4.38605 and variance < 1.5922 and curtosis < -2.2859 | 1 | 0.026138 |
| variance > 0.320165 and curtosis > -4.38605 and variance <= 2.03655 and curtosis <= -1.7388 and skewness <= 5.6605 | 1 | 0.040616 |
| variance <= 0.320165 and skewness <= 7.5653 and variance <= -1.78205 | 1 | 0.274368 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| variance > 0.31803 and curtosis > -4.3882 and variance > 1.7452 | 0 | 0.438085 |
| skewness <= 5.0097 and variance <= 0.3223 and curtosis <= 4.8486 | 1 | 0.535525 |
| skewness > -4.7428 and variance > -3.3793 and curtosis > -1.6488 and entropy <= 0.12585 | 0 | 0.409315 |
| variance <= -1.3968 | 1 | 0.684021 |
| skewness <= 5.6222 and curtosis <= 1.9079 | 1 | 0.465753 |
|  | 0 | 0.876404 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| skewness <= 5.8333 and curtosis <= 6.2169 and variance <= -0.36372 | 1 | 0.288681 |
| skewness <= -4.7428 and variance <= -0.55355 | 1 | 0.145885 |
| variance <= 1.7425 and curtosis <= 0.2182 and skewness <= 4.2503 | 1 | 0.119537 |
| variance <= -4.1479 and curtosis <= 1.0836 | 1 | 0.048611 |
| curtosis <= -4.7986 and variance <= 2.3917 | 1 | 0.018625 |
| skewness <= -0.69529 and curtosis <= 1.7956 and variance <= 0.74428 | 1 | 0.012968 |
|  | 0 | 0.994194 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

variance|skewness|curtosis|class
---|---|---|---
(1.7907-2.3921]|(9.61695-inf)|(-4.42285-8.83885]|0
(0.320165-1.7907]|(9.61695-inf)|(-4.42285-8.83885]|0
(2.3921-inf)|(9.61695-inf)|(-4.42285-8.83885]|0
(-2.7952-0.320165]|(9.61695-inf)|(-4.42285-8.83885]|0
(1.7907-2.3921]|(5.21045-9.61695]|(-4.42285-8.83885]|0
(-2.7952-0.320165]|(5.21045-9.61695]|(-4.42285-8.83885]|0
(2.3921-inf)|(5.21045-9.61695]|(-4.42285-8.83885]|0
(0.320165-1.7907]|(5.21045-9.61695]|(-4.42285-8.83885]|0
(-inf--2.7952]|(-5.62225--2.3021]|(8.83885-inf)|1
(-inf--2.7952]|(5.21045-9.61695]|(-4.42285-8.83885]|1
(-2.7952-0.320165]|(-6.94555--5.62225]|(8.83885-inf)|1
(2.3921-inf)|(9.61695-inf)|(-inf--4.42285]|0
(1.7907-2.3921]|(-2.3021-5.21045]|(-4.42285-8.83885]|0
(2.3921-inf)|(-2.3021-5.21045]|(-4.42285-8.83885]|0
(-inf--2.7952]|(-6.94555--5.62225]|(8.83885-inf)|1
(0.320165-1.7907]|(-2.3021-5.21045]|(-4.42285-8.83885]|0
(-inf--2.7952]|(-2.3021-5.21045]|(-4.42285-8.83885]|1
(-2.7952-0.320165]|(-2.3021-5.21045]|(-4.42285-8.83885]|1
(2.3921-inf)|(5.21045-9.61695]|(-inf--4.42285]|0
(1.7907-2.3921]|(-5.62225--2.3021]|(-4.42285-8.83885]|0
(0.320165-1.7907]|(-5.62225--2.3021]|(-4.42285-8.83885]|0
(2.3921-inf)|(-5.62225--2.3021]|(-4.42285-8.83885]|0
(-2.7952-0.320165]|(-inf--6.94555]|(8.83885-inf)|1
(-2.7952-0.320165]|(-5.62225--2.3021]|(-4.42285-8.83885]|1
(-inf--2.7952]|(-inf--6.94555]|(8.83885-inf)|1
(-inf--2.7952]|(-6.94555--5.62225]|(-4.42285-8.83885]|0
(0.320165-1.7907]|(-6.94555--5.62225]|(-4.42285-8.83885]|0
(2.3921-inf)|(-6.94555--5.62225]|(-4.42285-8.83885]|0
(1.7907-2.3921]|(-2.3021-5.21045]|(-inf--4.42285]|1
(1.7907-2.3921]|(-6.94555--5.62225]|(-4.42285-8.83885]|0
(-2.7952-0.320165]|(-2.3021-5.21045]|(-inf--4.42285]|1
(0.320165-1.7907]|(-2.3021-5.21045]|(-inf--4.42285]|1
(-2.7952-0.320165]|(-6.94555--5.62225]|(-4.42285-8.83885]|1
(-inf--2.7952]|(-inf--6.94555]|(-4.42285-8.83885]|1
(-2.7952-0.320165]|(-inf--6.94555]|(-4.42285-8.83885]|1

## JRip

Decision list:

rules | predicted class
---|---
(skewness <= 5.8333) and (curtosis <= 6.2169) and (variance <= -0.36372)|1 (278.0/0.0)
(skewness <= -4.7428) and (variance <= -0.55355)|1 (117.0/0.0)
(variance <= 1.7425) and (curtosis <= 0.2182) and (skewness <= 4.2503)|1 (93.0/0.0)
(variance <= -4.1479) and (curtosis <= 1.0836)|1 (35.0/0.0)
(curtosis <= -4.7986) and (variance <= 2.3917)|1 (13.0/0.0)
(skewness <= -0.69529) and (curtosis <= 1.7956) and (variance <= 0.74428)|1 (9.0/0.0)
|0 (689.0/4.0)


## PART

Decision list:

rules | predicted class
---|---
variance > 0.31803 AND curtosis > -4.3882 AND variance > 1.7452|0 (346.0/1.0)
skewness <= 5.0097 AND variance <= 0.3223 AND curtosis <= 4.8486|1 (232.0)
skewness > -4.7428 AND variance > -3.3793 AND curtosis > -1.6488 AND entropy <= 0.12585|0 (147.0)
variance <= -1.3968|1 (148.0/3.0)
skewness <= 5.6222 AND curtosis <= 1.9079|1 (52.0)
|0 (63.0/10.0)


## J48 Decision Tree

* variance <= 0.320165
	* skewness <= 7.5653
		* variance <= -1.78205: 1 (261.0/1.0)
		* variance > -1.78205
			* curtosis <= 6.824400000000001
				* skewness <= 3.9285: 1 (188.0/2.0)
				* skewness > 3.9285
					* variance <= 0.222115: 0 (7.0)
					* variance > 0.222115: 1 (5.0/1.0)
			* curtosis > 6.824400000000001
				* skewness <= -5.5343: 1 (14.0/1.0)
				* skewness > -5.5343: 0 (19.0)
	* skewness > 7.5653
		* variance <= -4.726: 1 (18.0)
		* variance > -4.726: 0 (74.0)
* variance > 0.320165
	* curtosis <= -4.38605
		* skewness <= 7.191800000000001: 1 (29.0)
		* skewness > 7.191800000000001: 0 (7.0)
	* curtosis > -4.38605
		* variance <= 2.03655
			* curtosis <= -1.7388
				* skewness <= 5.6605: 1 (29.0)
				* skewness > 5.6605: 0 (14.0)
			* curtosis > -1.7388
				* entropy <= 0.128435: 0 (129.0)
				* entropy > 0.128435
					* variance <= 0.8104899999999999
						* curtosis <= 1.952: 1 (10.0)
						* curtosis > 1.952: 0 (5.0)
					* variance > 0.8104899999999999: 0 (29.0)
		* variance > 2.03655: 0 (396.0)


## SimpleCart Decision Tree

* variance < 0.320165
	* skewness < 7.5653
		* variance < -0.38902000000000003
			* curtosis < 6.21865: 1(292.0/0.0)
			* curtosis >= 6.21865
				* skewness < -4.6745: 1(117.0/0.0)
				* skewness >= -4.6745: 0(16.0/1.0)
		* variance >= -0.38902000000000003
			* skewness < 5.45355
				* curtosis < 2.6105: 1(52.0/0.0)
				* curtosis >= 2.6105: 0(8.0/1.0)
			* skewness >= 5.45355: 0(7.0/0.0)
	* skewness >= 7.5653
		* variance < -4.726: 1(18.0/0.0)
		* variance >= -4.726: 0(74.0/0.0)
* variance >= 0.320165
	* curtosis < -4.38605
		* variance < 3.3408: 1(29.0/0.0)
		* variance >= 3.3408: 0(7.0/0.0)
	* curtosis >= -4.38605
		* variance < 1.5922
			* curtosis < -2.2859: 1(21.0/3.0)
			* curtosis >= -2.2859
				* entropy < 0.081882: 0(110.0/0.0)
				* entropy >= 0.081882
					* curtosis < 1.85305: 1(15.0/2.0)
					* curtosis >= 1.85305: 0(15.0/0.0)
		* variance >= 1.5922: 0(443.0/3.0)


