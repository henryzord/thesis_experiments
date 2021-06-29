# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| variance >= 0.320165 and curtosis >= -4.38605 and variance >= 1.5922 and variance >= 2.03655 | 0 | 0.418432 |
| variance < 0.320165 and skewness < 7.5653 and variance < -0.38902000000000003 and curtosis < 6.21865 | 1 | 0.298874 |
| variance > 0.320165 and curtosis > -4.38605 and variance <= 2.03655 and curtosis > -1.7388 and entropy <= 0.128435 | 0 | 0.190265 |
| variance < 0.320165 and skewness < 7.5653 and variance < -0.38902000000000003 and curtosis >= 6.21865 and skewness < -4.6745 | 1 | 0.145885 |
| variance < 0.320165 and skewness >= 7.5653 and variance >= -4.726 | 0 | 0.120192 |
| variance < 0.320165 and skewness < 7.5653 and variance >= -0.38902000000000003 and skewness < 5.45355 and curtosis < 2.6105 | 1 | 0.070556 |
| variance > 0.320165 and curtosis <= -4.38605 and variance <= 3.3408 | 1 | 0.040616 |
| variance > 0.320165 and curtosis > -4.38605 and variance <= 2.03655 and curtosis > -1.7388 and entropy > 0.128435 and variance > 0.8104899999999999 | 0 | 0.050173 |
| variance > 0.320165 and curtosis > -4.38605 and variance <= 2.03655 and curtosis <= -1.7388 and skewness <= 5.6605 | 1 | 0.040616 |
| variance <= 0.320165 and skewness <= 7.5653 and variance > -1.78205 and curtosis > 6.824400000000001 and skewness > -5.5343 | 0 | 0.033451 |
| variance <= 0.320165 and skewness > 7.5653 and variance <= -4.726 | 1 | 0.025605 |
| variance > 0.320165 and curtosis > -4.38605 and variance <= 2.03655 and curtosis <= -1.7388 and skewness > 5.6605 | 0 | 0.024867 |
| variance <= 0.320165 and skewness <= 7.5653 and variance > -1.78205 and curtosis <= 6.824400000000001 and skewness > 3.9285 | 0 | 0.009644 |
| variance >= 0.320165 and curtosis >= -4.38605 and variance < 1.5922 and curtosis >= -2.2859 and entropy >= 0.081882 and curtosis < 1.85305 and skewness < 3.5591749999999998 | 1 | 0.021429 |
| variance >= 0.320165 and curtosis < -4.38605 and variance >= 3.3408 | 0 | 0.012590 |
| variance > 0.320165 and curtosis > -4.38605 and variance <= 2.03655 and curtosis > -1.7388 and entropy > 0.128435 and variance <= 0.8104899999999999 and curtosis > 1.199265 | 0 | 0.006470 |
| variance < 0.320165 and skewness < 7.5653 and variance >= -0.38902000000000003 and skewness < 5.45355 and curtosis >= 2.6105 | 0 | 0.012790 |
| variance < 0.320165 and skewness < 7.5653 and variance < -0.38902000000000003 and curtosis >= 6.21865 and skewness >= -4.6745 and variance >= -2.1171 | 0 | 0.026596 |
| variance <= 0.320165 and skewness <= 7.5653 and variance <= -1.78205 | 1 | 0.274368 |
| variance <= 0.320165 and skewness <= 7.5653 and variance > -1.78205 and curtosis <= 6.824400000000001 and skewness <= 3.9285 | 1 | 0.211762 |
| variance < 0.320165 and skewness < 7.5653 and variance < -0.38902000000000003 and curtosis >= 6.21865 and skewness >= -4.6745 and variance < -2.1171 | 0 | 0.000911 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| variance > 0.320165 and curtosis > -4.38605 and variance > 2.03655 | 0 | 0.418432 |
| skewness > 5.27355 and variance > -3.36765 | 0 | 0.240664 |
| variance <= 0.320165 and curtosis <= 3.0642 | 1 | 0.728972 |
| skewness <= -5.1215 and variance <= -0.454565 | 1 | 0.570370 |
| curtosis <= 0.20578 and curtosis <= -1.49205 | 1 | 0.337143 |
| variance > 0.75082 | 0 | 0.717647 |
| entropy <= -0.125014 and variance > -1.232365 | 0 | 0.555556 |
| skewness > -1.81995 and curtosis > 1.492315 and variance > -1.75625 | 0 | 0.478261 |
| skewness <= 0.389015 | 1 | 0.884615 |
|  | 0 | 0.750000 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| variance <= 0.31803 and skewness <= 4.0537 and curtosis <= 6.7156 | 1 | 0.320449 |
| variance <= -1.7279 and skewness <= 9.6014 | 1 | 0.165948 |
| curtosis <= -2.3 and skewness <= 5.2022 | 1 | 0.076819 |
| variance <= 1.3518 and entropy >= -0.062945 and curtosis <= 1.7048 and skewness <= 1.1857 | 1 | 0.020029 |
| skewness <= -7.1535 | 1 | 0.014388 |
|  | 0 | 0.998542 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

variance|skewness|curtosis|class
---|---|---|---
(1.7907-2.3921]|(9.61695-inf)|(-4.42285-8.83885]|0
(2.3921-inf)|(9.61695-inf)|(-4.42285-8.83885]|0
(0.320165-1.7907]|(9.61695-inf)|(-4.42285-8.83885]|0
(-2.7952-0.320165]|(9.61695-inf)|(-4.42285-8.83885]|0
(-inf--2.7952]|(-5.62225--2.3021]|(8.83885-inf)|1
(1.7907-2.3921]|(5.21045-9.61695]|(-4.42285-8.83885]|0
(0.320165-1.7907]|(5.21045-9.61695]|(-4.42285-8.83885]|0
(-inf--2.7952]|(5.21045-9.61695]|(-4.42285-8.83885]|1
(-2.7952-0.320165]|(5.21045-9.61695]|(-4.42285-8.83885]|0
(2.3921-inf)|(5.21045-9.61695]|(-4.42285-8.83885]|0
(-2.7952-0.320165]|(-6.94555--5.62225]|(8.83885-inf)|1
(-inf--2.7952]|(-6.94555--5.62225]|(8.83885-inf)|1
(-inf--2.7952]|(-2.3021-5.21045]|(-4.42285-8.83885]|1
(2.3921-inf)|(9.61695-inf)|(-inf--4.42285]|0
(-2.7952-0.320165]|(-2.3021-5.21045]|(-4.42285-8.83885]|1
(1.7907-2.3921]|(-2.3021-5.21045]|(-4.42285-8.83885]|0
(0.320165-1.7907]|(-2.3021-5.21045]|(-4.42285-8.83885]|0
(2.3921-inf)|(-2.3021-5.21045]|(-4.42285-8.83885]|0
(-inf--2.7952]|(-inf--6.94555]|(8.83885-inf)|1
(-2.7952-0.320165]|(-inf--6.94555]|(8.83885-inf)|1
(-2.7952-0.320165]|(-5.62225--2.3021]|(-4.42285-8.83885]|1
(1.7907-2.3921]|(-5.62225--2.3021]|(-4.42285-8.83885]|0
(2.3921-inf)|(5.21045-9.61695]|(-inf--4.42285]|0
(0.320165-1.7907]|(-5.62225--2.3021]|(-4.42285-8.83885]|0
(2.3921-inf)|(-5.62225--2.3021]|(-4.42285-8.83885]|0
(2.3921-inf)|(-6.94555--5.62225]|(-4.42285-8.83885]|0
(-inf--2.7952]|(-6.94555--5.62225]|(-4.42285-8.83885]|0
(-2.7952-0.320165]|(-2.3021-5.21045]|(-inf--4.42285]|1
(1.7907-2.3921]|(-2.3021-5.21045]|(-inf--4.42285]|1
(0.320165-1.7907]|(-2.3021-5.21045]|(-inf--4.42285]|1
(0.320165-1.7907]|(-6.94555--5.62225]|(-4.42285-8.83885]|0
(-2.7952-0.320165]|(-6.94555--5.62225]|(-4.42285-8.83885]|1
(1.7907-2.3921]|(-6.94555--5.62225]|(-4.42285-8.83885]|0
(-inf--2.7952]|(-inf--6.94555]|(-4.42285-8.83885]|1
(-2.7952-0.320165]|(-inf--6.94555]|(-4.42285-8.83885]|1

## JRip

Decision list:

rules | predicted class
---|---
(variance <= 0.31803) and (skewness <= 4.0537) and (curtosis <= 6.7156)|1 (327.0/2.0)
(variance <= -1.7279) and (skewness <= 9.6014)|1 (148.0/6.0)
(curtosis <= -2.3) and (skewness <= 5.2022)|1 (57.0/0.0)
(variance <= 1.3518) and (entropy >= -0.062945) and (curtosis <= 1.7048) and (skewness <= 1.1857)|1 (14.0/0.0)
(skewness <= -7.1535)|1 (10.0/0.0)
|0 (678.0/1.0)


## PART

Decision list:

rules | predicted class
---|---
variance > 0.320165 AND curtosis > -4.38605 AND variance > 2.03655|0 (395.0)
skewness > 5.27355 AND variance > -3.36765|0 (174.0)
variance <= 0.320165 AND curtosis <= 3.0642|1 (312.0)
skewness <= -5.1215 AND variance <= -0.454565|1 (154.0)
curtosis <= 0.20578 AND curtosis <= -1.49205|1 (59.0)
variance > 0.75082|0 (61.0)
entropy <= -0.125014 AND variance > -1.232365|0 (30.0)
skewness > -1.81995 AND curtosis > 1.492315 AND variance > -1.75625|0 (22.0)
skewness <= 0.389015|1 (23.0)
|0 (4.0/1.0)


## J48 Decision Tree

* variance <= 0.320165
	* skewness <= 7.5653
		* variance <= -1.78205: 1 (261.0/1.0)
		* variance > -1.78205
			* curtosis <= 6.824400000000001
				* skewness <= 3.9285: 1 (188.0/2.0)
				* skewness > 3.9285: 0 (12.0/4.0)
			* curtosis > 6.824400000000001
				* skewness <= -5.5343: 1 (14.0/1.0)
				* skewness > -5.5343: 0 (19.0)
	* skewness > 7.5653
		* variance <= -4.726: 1 (18.0)
		* variance > -4.726: 0 (75.0)
* variance > 0.320165
	* curtosis <= -4.38605
		* variance <= 3.3408: 1 (29.0)
		* variance > 3.3408: 0 (7.0)
	* curtosis > -4.38605
		* variance <= 2.03655
			* curtosis <= -1.7388
				* skewness <= 5.6605: 1 (29.0)
				* skewness > 5.6605: 0 (14.0)
			* curtosis > -1.7388
				* entropy <= 0.128435: 0 (129.0)
				* entropy > 0.128435
					* variance <= 0.8104899999999999
						* curtosis <= 1.199265: 1 (8.0)
						* curtosis > 1.199265: 0 (7.0/2.0)
					* variance > 0.8104899999999999: 0 (29.0)
		* variance > 2.03655: 0 (395.0)


## SimpleCart Decision Tree

* variance < 0.320165
	* skewness < 7.5653
		* variance < -0.38902000000000003
			* curtosis < 6.21865: 1(292.0/0.0)
			* curtosis >= 6.21865
				* skewness < -4.6745: 1(117.0/0.0)
				* skewness >= -4.6745
					* variance < -2.1171: 0(1.0/1.0)
					* variance >= -2.1171: 0(15.0/0.0)
		* variance >= -0.38902000000000003
			* skewness < 5.45355
				* curtosis < 2.6105: 1(52.0/0.0)
				* curtosis >= 2.6105: 0(8.0/1.0)
			* skewness >= 5.45355: 0(7.0/0.0)
	* skewness >= 7.5653
		* variance < -4.726: 1(18.0/0.0)
		* variance >= -4.726: 0(75.0/0.0)
* variance >= 0.320165
	* curtosis < -4.38605
		* variance < 3.3408: 1(29.0/0.0)
		* variance >= 3.3408: 0(7.0/0.0)
	* curtosis >= -4.38605
		* variance < 1.5922
			* curtosis < -2.2859
				* skewness < 5.6574: 1(21.0/0.0)
				* skewness >= 5.6574: 0(3.0/0.0)
			* curtosis >= -2.2859
				* entropy < 0.081882: 0(110.0/0.0)
				* entropy >= 0.081882
					* curtosis < 1.85305
						* skewness < 3.5591749999999998: 1(15.0/0.0)
						* skewness >= 3.5591749999999998: 0(2.0/0.0)
					* curtosis >= 1.85305: 0(15.0/0.0)
		* variance >= 1.5922
			* variance < 2.03655
				* curtosis < -2.6483499999999998: 1(3.0/1.0)
				* curtosis >= -2.6483499999999998: 0(46.0/0.0)
			* variance >= 2.03655: 0(395.0/0.0)


