# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| variance >= 0.320165 and curtosis >= -4.4434000000000005 and variance >= 1.5962 | 0 | 0.441515 |
| variance < 0.320165 and skewness < 8.185 and variance < -0.4031 and curtosis < 6.21865 | 1 | 0.301439 |
| variance < 0.320165 and skewness < 8.185 and variance < -0.4031 and curtosis >= 6.21865 and skewness < -2.9622 | 1 | 0.145704 |
| variance >= 0.320165 and curtosis >= -4.4434000000000005 and variance < 1.5962 and curtosis >= -2.2721999999999998 | 0 | 0.168413 |
| variance <= 0.760295 and skewness > 5.1608 and variance > -3.4449 | 0 | 0.159279 |
| variance <= 0.760295 and skewness <= 5.1608 and variance > -0.38902 and curtosis <= 0.470115 | 1 | 0.091391 |
| variance > 0.760295 and curtosis <= -1.8648 and skewness <= 4.9414 | 1 | 0.051311 |
| variance <= 0.760295 and skewness <= 5.1608 and variance <= -0.38902 and curtosis > 6.21865 and skewness > -2.9622 | 0 | 0.026596 |
| variance < 0.320165 and skewness >= 8.185 and variance < -4.8358 | 1 | 0.017192 |
| variance > 0.760295 and curtosis <= -1.8648 and skewness > 4.9414 | 0 | 0.217949 |
| variance < 0.320165 and skewness < 8.185 and variance >= -0.4031 and skewness < 5.4939 and curtosis < 2.62465 | 1 | 0.070461 |
| variance < 0.320165 and skewness < 8.185 and variance >= -0.4031 and skewness < 5.4939 and curtosis >= 2.62465 | 0 | 0.018038 |
| variance <= 0.760295 and skewness <= 5.1608 and variance > -0.38902 and curtosis > 0.470115 and entropy > 0.72843 | 1 | 0.012008 |
| variance >= 0.320165 and curtosis < -4.4434000000000005 | 1 | 0.030847 |
| variance < 0.320165 and skewness >= 8.185 and variance >= -4.8358 | 0 | 0.115942 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| variance > 0.760295 and curtosis > -1.8648 | 0 | 0.403909 |
| skewness <= 5.1608 and variance <= -1.78205 | 1 | 0.434242 |
| skewness > 5.21045 and variance > -3.4449 | 0 | 0.454707 |
| curtosis <= 0.7216 and variance <= 1.5857 | 1 | 0.785978 |
| skewness <= -0.9436 and variance <= -0.462635 | 1 | 0.536000 |
| curtosis > 2.1671 | 0 | 0.609025 |
| variance <= 0.32457 | 1 | 0.516129 |
| curtosis > -2.59825 and curtosis <= 1.4276 | 0 | 0.560000 |
|  | 1 | 0.916667 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| skewness <= 5.1401 and curtosis <= 6.2169 and variance <= -0.36372 | 1 | 0.287643 |
| skewness <= -4.5152 and variance <= -0.55355 | 1 | 0.145704 |
| variance <= 1.6799 and skewness <= 5.2022 and curtosis <= 0.18307 | 1 | 0.129442 |
| variance <= -4.1479 and curtosis <= 1.0836 | 1 | 0.049861 |
| skewness <= -0.69529 and curtosis <= 2.135 and variance <= 0.74428 | 1 | 0.015782 |
|  | 0 | 0.991329 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

variance|skewness|curtosis|class
---|---|---|---
(-0.4031-0.760295]|(9.53215-inf)|(-4.42285-8.83885]|0
(2.3921-inf)|(9.53215-inf)|(-4.42285-8.83885]|0
(-2.7952--0.4031]|(9.53215-inf)|(-4.42285-8.83885]|0
(0.760295-2.3921]|(9.53215-inf)|(-4.42285-8.83885]|0
(-inf--2.7952]|(-5.436--2.3021]|(8.83885-inf)|1
(-2.7952--0.4031]|(5.21045-9.53215]|(-4.42285-8.83885]|0
(-0.4031-0.760295]|(5.21045-9.53215]|(-4.42285-8.83885]|0
(2.3921-inf)|(5.21045-9.53215]|(-4.42285-8.83885]|0
(0.760295-2.3921]|(5.21045-9.53215]|(-4.42285-8.83885]|0
(-inf--2.7952]|(5.21045-9.53215]|(-4.42285-8.83885]|1
(2.3921-inf)|(9.53215-inf)|(-inf--4.42285]|0
(2.3921-inf)|(-2.3021-5.21045]|(-4.42285-8.83885]|0
(-inf--2.7952]|(-6.94555--5.436]|(8.83885-inf)|1
(-2.7952--0.4031]|(-6.94555--5.436]|(8.83885-inf)|1
(0.760295-2.3921]|(-2.3021-5.21045]|(-4.42285-8.83885]|0
(-2.7952--0.4031]|(-2.3021-5.21045]|(-4.42285-8.83885]|1
(-inf--2.7952]|(-2.3021-5.21045]|(-4.42285-8.83885]|1
(-0.4031-0.760295]|(-2.3021-5.21045]|(-4.42285-8.83885]|1
(2.3921-inf)|(5.21045-9.53215]|(-inf--4.42285]|0
(0.760295-2.3921]|(-5.436--2.3021]|(-4.42285-8.83885]|0
(2.3921-inf)|(-5.436--2.3021]|(-4.42285-8.83885]|0
(-inf--2.7952]|(-inf--6.94555]|(8.83885-inf)|1
(-0.4031-0.760295]|(-5.436--2.3021]|(-4.42285-8.83885]|0
(-2.7952--0.4031]|(-5.436--2.3021]|(-4.42285-8.83885]|1
(-2.7952--0.4031]|(-inf--6.94555]|(8.83885-inf)|1
(2.3921-inf)|(-6.94555--5.436]|(-4.42285-8.83885]|0
(0.760295-2.3921]|(-6.94555--5.436]|(-4.42285-8.83885]|0
(-inf--2.7952]|(-6.94555--5.436]|(-4.42285-8.83885]|0
(-0.4031-0.760295]|(-6.94555--5.436]|(-4.42285-8.83885]|0
(0.760295-2.3921]|(-2.3021-5.21045]|(-inf--4.42285]|1
(-2.7952--0.4031]|(-6.94555--5.436]|(-4.42285-8.83885]|1
(-0.4031-0.760295]|(-2.3021-5.21045]|(-inf--4.42285]|1
(-inf--2.7952]|(-inf--6.94555]|(-4.42285-8.83885]|1
(-2.7952--0.4031]|(-inf--6.94555]|(-4.42285-8.83885]|1

## JRip

Decision list:

rules | predicted class
---|---
(skewness <= 5.1401) and (curtosis <= 6.2169) and (variance <= -0.36372)|1 (277.0/0.0)
(skewness <= -4.5152) and (variance <= -0.55355)|1 (117.0/0.0)
(variance <= 1.6799) and (skewness <= 5.2022) and (curtosis <= 0.18307)|1 (102.0/0.0)
(variance <= -4.1479) and (curtosis <= 1.0836)|1 (36.0/0.0)
(skewness <= -0.69529) and (curtosis <= 2.135) and (variance <= 0.74428)|1 (11.0/0.0)
|0 (692.0/6.0)


## PART

Decision list:

rules | predicted class
---|---
variance > 0.760295 AND curtosis > -1.8648|0 (372.0)
skewness <= 5.1608 AND variance <= -1.78205|1 (243.0/1.0)
skewness > 5.21045 AND variance > -3.4449|0 (256.0)
curtosis <= 0.7216 AND variance <= 1.5857|1 (213.0)
skewness <= -0.9436 AND variance <= -0.462635|1 (67.0)
curtosis > 2.1671|0 (43.0/1.0)
variance <= 0.32457|1 (15.0)
curtosis > -2.59825 AND curtosis <= 1.4276|0 (14.0)
|1 (12.0/1.0)


## J48 Decision Tree

* variance <= 0.760295
	* skewness <= 5.1608
		* variance <= -0.38902
			* curtosis <= 6.21865: 1 (275.0)
			* curtosis > 6.21865
				* skewness <= -2.9622: 1 (117.0)
				* skewness > -2.9622: 0 (15.0)
		* variance > -0.38902
			* curtosis <= 0.470115: 1 (69.0)
			* curtosis > 0.470115
				* entropy <= 0.72843: 0 (38.0/2.0)
				* entropy > 0.72843: 1 (12.0/2.0)
	* skewness > 5.1608
		* variance <= -3.4449: 1 (37.0/1.0)
		* variance > -3.4449: 0 (106.0/1.0)
* variance > 0.760295
	* curtosis <= -1.8648
		* skewness <= 4.9414: 1 (41.0/2.0)
		* skewness > 4.9414: 0 (153.0)
	* curtosis > -1.8648: 0 (372.0)


## SimpleCart Decision Tree

* variance < 0.320165
	* skewness < 8.185
		* variance < -0.4031
			* curtosis < 6.21865: 1(298.0/2.0)
			* curtosis >= 6.21865
				* skewness < -2.9622: 1(117.0/0.0)
				* skewness >= -2.9622: 0(15.0/0.0)
		* variance >= -0.4031
			* skewness < 5.4939
				* curtosis < 2.62465: 1(52.0/0.0)
				* curtosis >= 2.62465: 0(11.0/1.0)
			* skewness >= 5.4939: 0(14.0/0.0)
	* skewness >= 8.185
		* variance < -4.8358: 1(12.0/0.0)
		* variance >= -4.8358: 0(72.0/0.0)
* variance >= 0.320165
	* curtosis < -4.4434000000000005: 1(28.0/8.0)
	* curtosis >= -4.4434000000000005
		* variance < 1.5962
			* curtosis < -2.2721999999999998: 1(23.0/3.0)
			* curtosis >= -2.2721999999999998: 0(125.0/16.0)
		* variance >= 1.5962: 0(436.0/2.0)


