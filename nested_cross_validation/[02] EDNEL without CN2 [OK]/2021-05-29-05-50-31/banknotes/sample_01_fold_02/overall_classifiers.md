# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 0 | 0.555105 |
| variance >= 0.320165 and curtosis >= -4.373200000000001 and variance < 1.5922 and curtosis < -2.2721999999999998 | 1 | 0.027500 |
| variance < 0.320165 and skewness < 7.5653 and variance >= -0.4031 and skewness < 5.45355 and curtosis < 2.62465 | 1 | 0.070556 |
| variance > -0.4031 and variance <= 0.760295 and skewness > -2.3021 and skewness <= 5.21045 and curtosis > -4.42285 and curtosis <= 8.83885 and entropy = all | 1 | 0.061750 |
| variance >= 0.320165 and curtosis >= -4.373200000000001 and variance < 1.5922 and curtosis >= -2.2721999999999998 and entropy >= 0.081882 and curtosis < 1.91945 | 1 | 0.020347 |
| variance < 0.320165 and skewness < 7.5653 and variance < -0.4031 and curtosis < 6.21865 | 1 | 0.295995 |
| variance < 0.320165 and skewness < 7.5653 and variance < -0.4031 and curtosis >= 6.21865 and skewness < -4.6745 | 1 | 0.145885 |
| variance < 0.320165 and skewness >= 7.5653 and variance < -4.726 | 1 | 0.025605 |
| variance >= 0.320165 and curtosis < -4.373200000000001 and variance < 3.30405 | 1 | 0.041958 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| variance > 0.7602949999999999 and variance > 1.7907000000000002 | 0 | 0.437521 |
| skewness <= 5.1608 and variance <= 0.320165 and curtosis <= 3.0642 | 1 | 0.516129 |
| skewness > -4.9363 and curtosis > -3.8779500000000002 and variance > -3.3924 and entropy <= -0.338375 | 0 | 0.406896 |
| variance <= -1.78205 | 1 | 0.708363 |
| curtosis <= 0.20578000000000002 | 1 | 0.519084 |
| skewness > -1.81995 | 0 | 0.500159 |
| variance <= -0.265605 | 1 | 0.881356 |
|  | 0 | 0.700000 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| skewness <= 7.6584 and variance <= -1.8046 | 1 | 0.272828 |
| variance <= 0.84546 and skewness <= 5.0097 and curtosis <= 0.096532 | 1 | 0.173703 |
| variance <= -0.47465 and skewness <= -0.30005 | 1 | 0.098701 |
| variance <= 1.7425 and curtosis <= -3.9692 | 1 | 0.031117 |
| variance <= -5.1661 | 1 | 0.024217 |
| variance <= 1.7875 and entropy >= -0.12243 and curtosis <= 2.135 and skewness <= 2.2638 | 1 | 0.037921 |
|  | 0 | 0.992754 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

variance|skewness|curtosis|entropy|class
---|---|---|---|---
(1.7907-inf)|(9.61695-inf)|(-4.42285-8.83885]|all|0
(-0.4031-0.760295]|(9.61695-inf)|(-4.42285-8.83885]|all|0
(0.760295-1.7907]|(9.61695-inf)|(-4.42285-8.83885]|all|0
(-2.7952--0.4031]|(9.61695-inf)|(-4.42285-8.83885]|all|0
(-inf--2.7952]|(-5.5074--2.3021]|(8.83885-inf)|all|1
(-2.7952--0.4031]|(5.21045-9.61695]|(-4.42285-8.83885]|all|0
(0.760295-1.7907]|(5.21045-9.61695]|(-4.42285-8.83885]|all|0
(-0.4031-0.760295]|(5.21045-9.61695]|(-4.42285-8.83885]|all|0
(1.7907-inf)|(5.21045-9.61695]|(-4.42285-8.83885]|all|0
(-inf--2.7952]|(5.21045-9.61695]|(-4.42285-8.83885]|all|1
(-2.7952--0.4031]|(-6.95385--5.5074]|(8.83885-inf)|all|1
(1.7907-inf)|(9.61695-inf)|(-inf--4.42285]|all|0
(1.7907-inf)|(-2.3021-5.21045]|(-4.42285-8.83885]|all|0
(0.760295-1.7907]|(-2.3021-5.21045]|(-4.42285-8.83885]|all|0
(-inf--2.7952]|(-2.3021-5.21045]|(-4.42285-8.83885]|all|1
(-0.4031-0.760295]|(-2.3021-5.21045]|(-4.42285-8.83885]|all|1
(-inf--2.7952]|(-6.95385--5.5074]|(8.83885-inf)|all|1
(-2.7952--0.4031]|(-2.3021-5.21045]|(-4.42285-8.83885]|all|1
(1.7907-inf)|(5.21045-9.61695]|(-inf--4.42285]|all|0
(1.7907-inf)|(-5.5074--2.3021]|(-4.42285-8.83885]|all|0
(0.760295-1.7907]|(-5.5074--2.3021]|(-4.42285-8.83885]|all|0
(-0.4031-0.760295]|(-5.5074--2.3021]|(-4.42285-8.83885]|all|0
(-2.7952--0.4031]|(-5.5074--2.3021]|(-4.42285-8.83885]|all|1
(-2.7952--0.4031]|(-inf--6.95385]|(8.83885-inf)|all|1
(-inf--2.7952]|(-inf--6.95385]|(8.83885-inf)|all|1
(-0.4031-0.760295]|(-6.95385--5.5074]|(-4.42285-8.83885]|all|0
(1.7907-inf)|(-2.3021-5.21045]|(-inf--4.42285]|all|1
(0.760295-1.7907]|(-6.95385--5.5074]|(-4.42285-8.83885]|all|0
(1.7907-inf)|(-6.95385--5.5074]|(-4.42285-8.83885]|all|0
(-inf--2.7952]|(-6.95385--5.5074]|(-4.42285-8.83885]|all|0
(-2.7952--0.4031]|(-6.95385--5.5074]|(-4.42285-8.83885]|all|1
(-0.4031-0.760295]|(-2.3021-5.21045]|(-inf--4.42285]|all|1
(0.760295-1.7907]|(-2.3021-5.21045]|(-inf--4.42285]|all|1
(-inf--2.7952]|(-inf--6.95385]|(-4.42285-8.83885]|all|1
(-2.7952--0.4031]|(-inf--6.95385]|(-4.42285-8.83885]|all|1

## JRip

Decision list:

rules | predicted class
---|---
(skewness <= 7.6584) and (variance <= -1.8046)|1 (259.0/1.0)
(variance <= 0.84546) and (skewness <= 5.0097) and (curtosis <= 0.096532)|1 (144.0/0.0)
(variance <= -0.47465) and (skewness <= -0.30005)|1 (77.0/1.0)
(variance <= 1.7425) and (curtosis <= -3.9692)|1 (22.0/0.0)
(variance <= -5.1661)|1 (17.0/0.0)
(variance <= 1.7875) and (entropy >= -0.12243) and (curtosis <= 2.135) and (skewness <= 2.2638)|1 (27.0/0.0)
|0 (688.0/5.0)


## PART

Decision list:

rules | predicted class
---|---
variance > 0.7602949999999999 AND variance > 1.7907000000000002|0 (433.0/3.0)
skewness <= 5.1608 AND variance <= 0.320165 AND curtosis <= 3.0642|1 (272.0)
skewness > -4.9363 AND curtosis > -3.8779500000000002 AND variance > -3.3924 AND entropy <= -0.338375|0 (194.0/2.0)
variance <= -1.78205|1 (155.0/1.0)
curtosis <= 0.20578000000000002|1 (63.0)
skewness > -1.81995|0 (56.0/1.0)
variance <= -0.265605|1 (52.0)
|0 (9.0/2.0)


## SimpleCart Decision Tree

* variance < 0.320165
	* skewness < 7.5653
		* variance < -0.4031
			* curtosis < 6.21865: 1(289.0/1.0)
			* curtosis >= 6.21865
				* skewness < -4.6745: 1(117.0/0.0)
				* skewness >= -4.6745: 0(13.0/1.0)
		* variance >= -0.4031
			* skewness < 5.45355
				* curtosis < 2.62465: 1(52.0/0.0)
				* curtosis >= 2.62465: 0(9.0/1.0)
			* skewness >= 5.45355: 0(10.0/0.0)
	* skewness >= 7.5653
		* variance < -4.726: 1(18.0/0.0)
		* variance >= -4.726: 0(79.0/0.0)
* variance >= 0.320165
	* curtosis < -4.373200000000001
		* variance < 3.30405: 1(30.0/0.0)
		* variance >= 3.30405: 0(10.0/0.0)
	* curtosis >= -4.373200000000001
		* variance < 1.5922
			* curtosis < -2.2721999999999998: 1(22.0/3.0)
			* curtosis >= -2.2721999999999998
				* entropy < 0.081882: 0(105.0/1.0)
				* entropy >= 0.081882
					* curtosis < 1.91945: 1(16.0/2.0)
					* curtosis >= 1.91945: 0(16.0/0.0)
		* variance >= 1.5922: 0(437.0/2.0)


