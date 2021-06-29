# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| variance >= 0.320165 and curtosis >= -4.38605 and variance >= 1.5922 and variance >= 2.03655 | 0 | 0.419048 |
| variance <= 0.9214249999999999 and skewness <= 5.095599999999999 and variance <= 0.311555 and curtosis <= 6.21865 | 1 | 0.321122 |
| variance <= 0.9214249999999999 and skewness > 5.095599999999999 and variance > -3.36765 | 0 | 0.170708 |
| variance < 0.320165 and skewness < 7.5653 and variance < -0.38902000000000003 and curtosis >= 6.21865 and skewness < -4.6745 | 1 | 0.145885 |
| variance > 0.9214249999999999 and curtosis > -2.0117 | 0 | 0.404558 |
| variance <= 0.9214249999999999 and skewness > 5.095599999999999 and variance <= -3.36765 | 1 | 0.048649 |
| variance >= 0.320165 and curtosis >= -4.38605 and variance < 1.5922 and curtosis >= -2.2859 and entropy < 0.081882 | 0 | 0.166920 |
| variance <= 0.9214249999999999 and skewness <= 5.095599999999999 and variance > 0.311555 and curtosis <= 0.47011500000000006 | 1 | 0.044630 |
| variance > 0.9214249999999999 and curtosis <= -2.0117 and skewness <= 4.8845 | 1 | 0.042002 |
| variance <= 0.9214249999999999 and skewness <= 5.095599999999999 and variance <= 0.311555 and curtosis > 6.21865 and skewness > -3.3066999999999998 | 0 | 0.035149 |
| variance > 0.9214249999999999 and curtosis <= -2.0117 and skewness > 4.8845 | 0 | 0.200873 |
| variance >= 0.320165 and curtosis >= -4.38605 and variance < 1.5922 and curtosis >= -2.2859 and entropy >= 0.081882 and curtosis >= 1.85305 | 0 | 0.026596 |
| variance >= 0.320165 and curtosis >= -4.38605 and variance < 1.5922 and curtosis >= -2.2859 and entropy >= 0.081882 and curtosis < 1.85305 and skewness < 3.5591749999999998 | 1 | 0.021429 |
| variance < 0.320165 and skewness < 7.5653 and variance >= -0.38902000000000003 and skewness < 5.45355 and curtosis >= 2.6105 | 0 | 0.012790 |
| variance < 0.320165 and skewness < 7.5653 and variance >= -0.38902000000000003 and skewness < 5.45355 and curtosis < 2.6105 | 1 | 0.070556 |
| variance < 0.320165 and skewness >= 7.5653 and variance >= -4.726 | 0 | 0.120192 |
| variance <= 0.9214249999999999 and skewness <= 5.095599999999999 and variance <= 0.311555 and curtosis > 6.21865 and skewness <= -3.3066999999999998 | 1 | 0.144861 |
| variance < 0.320165 and skewness < 7.5653 and variance < -0.38902000000000003 and curtosis >= 6.21865 and skewness >= -4.6745 and variance >= -2.1171 | 0 | 0.026596 |
| variance >= 0.320165 and curtosis < -4.38605 and variance < 3.3408 | 1 | 0.040616 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| variance > 0.31803 and curtosis > -4.3882 and variance > 2.031 | 0 | 0.419048 |
| skewness > 5.2684 and variance > -3.3793 | 0 | 0.239612 |
| variance <= 0.31803 and curtosis <= 3.0423 | 1 | 0.728972 |
| skewness <= -5.1277 and variance <= -0.46651 | 1 | 0.570370 |
| curtosis <= 0.20278 and curtosis <= -1.4938 | 1 | 0.337143 |
| variance > 0.74841 | 0 | 0.717647 |
| entropy <= -0.1276 and variance > -3.551 | 0 | 0.571429 |
| skewness > -1.8624 and curtosis > 1.488 and variance > -2.1652 | 0 | 0.478261 |
| variance > -3.4605 | 1 | 0.958333 |
|  | 0 | 0.500000 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| variance <= 0.26877 and skewness <= 4.987 and curtosis <= 6.8964 | 1 | 0.324530 |
| skewness <= 9.6014 and variance <= -1.9409 | 1 | 0.150164 |
| variance <= 1.7875 and skewness <= 5.2022 and curtosis <= -0.031994 | 1 | 0.083020 |
| skewness <= -6.4624 and variance <= -1.3968 | 1 | 0.026989 |
| variance <= 2.031 and entropy >= 0.003003 and curtosis <= 1.7048 and skewness <= 1.852 | 1 | 0.010116 |
|  | 0 | 0.995640 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

variance|skewness|curtosis|class
---|---|---|---
(0.320165-1.7907]|(9.61695-inf)|(-4.42285-8.83885]|0
(1.7907-2.3921]|(9.61695-inf)|(-4.42285-8.83885]|0
(2.3921-inf)|(9.61695-inf)|(-4.42285-8.83885]|0
(-2.7952-0.320165]|(9.61695-inf)|(-4.42285-8.83885]|0
(-inf--2.7952]|(-5.62225--2.3021]|(8.83885-inf)|1
(1.7907-2.3921]|(5.21045-9.61695]|(-4.42285-8.83885]|0
(0.320165-1.7907]|(5.21045-9.61695]|(-4.42285-8.83885]|0
(-2.7952-0.320165]|(5.21045-9.61695]|(-4.42285-8.83885]|0
(2.3921-inf)|(5.21045-9.61695]|(-4.42285-8.83885]|0
(-inf--2.7952]|(5.21045-9.61695]|(-4.42285-8.83885]|1
(-2.7952-0.320165]|(-6.94555--5.62225]|(8.83885-inf)|1
(2.3921-inf)|(9.61695-inf)|(-inf--4.42285]|0
(1.7907-2.3921]|(-2.3021-5.21045]|(-4.42285-8.83885]|0
(2.3921-inf)|(-2.3021-5.21045]|(-4.42285-8.83885]|0
(-inf--2.7952]|(-6.94555--5.62225]|(8.83885-inf)|1
(-inf--2.7952]|(-2.3021-5.21045]|(-4.42285-8.83885]|1
(0.320165-1.7907]|(-2.3021-5.21045]|(-4.42285-8.83885]|0
(-2.7952-0.320165]|(-2.3021-5.21045]|(-4.42285-8.83885]|1
(2.3921-inf)|(5.21045-9.61695]|(-inf--4.42285]|0
(1.7907-2.3921]|(-5.62225--2.3021]|(-4.42285-8.83885]|0
(2.3921-inf)|(-5.62225--2.3021]|(-4.42285-8.83885]|0
(0.320165-1.7907]|(-5.62225--2.3021]|(-4.42285-8.83885]|0
(-2.7952-0.320165]|(-inf--6.94555]|(8.83885-inf)|1
(-2.7952-0.320165]|(-5.62225--2.3021]|(-4.42285-8.83885]|1
(-inf--2.7952]|(-inf--6.94555]|(8.83885-inf)|1
(2.3921-inf)|(-6.94555--5.62225]|(-4.42285-8.83885]|0
(0.320165-1.7907]|(-6.94555--5.62225]|(-4.42285-8.83885]|0
(1.7907-2.3921]|(-6.94555--5.62225]|(-4.42285-8.83885]|0
(-inf--2.7952]|(-6.94555--5.62225]|(-4.42285-8.83885]|0
(0.320165-1.7907]|(-2.3021-5.21045]|(-inf--4.42285]|1
(-2.7952-0.320165]|(-2.3021-5.21045]|(-inf--4.42285]|1
(-2.7952-0.320165]|(-6.94555--5.62225]|(-4.42285-8.83885]|1
(1.7907-2.3921]|(-2.3021-5.21045]|(-inf--4.42285]|1
(-inf--2.7952]|(-inf--6.94555]|(-4.42285-8.83885]|1
(-2.7952-0.320165]|(-inf--6.94555]|(-4.42285-8.83885]|1

## JRip

Decision list:

rules | predicted class
---|---
(variance <= 0.26877) and (skewness <= 4.987) and (curtosis <= 6.8964)|1 (339.0/5.0)
(skewness <= 9.6014) and (variance <= -1.9409)|1 (124.0/1.0)
(variance <= 1.7875) and (skewness <= 5.2022) and (curtosis <= -0.031994)|1 (64.0/1.0)
(skewness <= -6.4624) and (variance <= -1.3968)|1 (19.0/0.0)
(variance <= 2.031) and (entropy >= 0.003003) and (curtosis <= 1.7048) and (skewness <= 1.852)|1 (7.0/0.0)
|0 (681.0/3.0)


## PART

Decision list:

rules | predicted class
---|---
variance > 0.31803 AND curtosis > -4.3882 AND variance > 2.031|0 (396.0)
skewness > 5.2684 AND variance > -3.3793|0 (173.0)
variance <= 0.31803 AND curtosis <= 3.0423|1 (312.0)
skewness <= -5.1277 AND variance <= -0.46651|1 (154.0)
curtosis <= 0.20278 AND curtosis <= -1.4938|1 (59.0)
variance > 0.74841|0 (61.0)
entropy <= -0.1276 AND variance > -3.551|0 (32.0)
skewness > -1.8624 AND curtosis > 1.488 AND variance > -2.1652|0 (22.0)
variance > -3.4605|1 (23.0)
|0 (2.0/1.0)


## J48 Decision Tree

* variance <= 0.9214249999999999
	* skewness <= 5.095599999999999
		* variance <= 0.311555
			* curtosis <= 6.21865: 1 (158.0)
			* curtosis > 6.21865
				* skewness <= -3.3066999999999998: 1 (65.0)
				* skewness > -3.3066999999999998: 0 (10.0)
		* variance > 0.311555
			* curtosis <= 0.47011500000000006: 1 (17.0)
			* curtosis > 0.47011500000000006: 0 (17.0/1.0)
	* skewness > 5.095599999999999
		* variance <= -3.36765: 1 (18.0/1.0)
		* variance > -3.36765: 0 (65.0/1.0)
* variance > 0.9214249999999999
	* curtosis <= -2.0117
		* skewness <= 4.8845: 1 (15.0)
		* skewness > 4.8845: 0 (68.0)
	* curtosis > -2.0117: 0 (184.0)


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
		* variance >= 3.3408: 0(6.0/0.0)
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
			* variance >= 2.03655: 0(396.0/0.0)


