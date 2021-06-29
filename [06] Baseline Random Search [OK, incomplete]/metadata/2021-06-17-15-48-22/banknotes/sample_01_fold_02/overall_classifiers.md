# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| variance >= 0.320165 and curtosis >= -4.373200000000001 and variance >= 1.5922 | 0 | 0.442082 |
| variance < 0.320165 and skewness < 7.5653 and variance < -0.4031 and curtosis < 6.21865 | 1 | 0.295995 |
| variance <= 0.75896 and skewness <= 5.1401 and variance <= 0.31803 and curtosis > 3.0423 and skewness <= -1.8624 | 1 | 0.195092 |
| variance >= 0.320165 and curtosis >= -4.373200000000001 and variance < 1.5922 and curtosis >= -2.2721999999999998 | 0 | 0.164984 |
| variance <= 0.75896 and skewness > 5.1401 and variance > -3.3793 | 0 | 0.161846 |
| variance > -0.4031 and variance <= 0.760295 and skewness > -2.3021 and skewness <= 5.21045 and curtosis > -4.42285 and curtosis <= 8.83885 | 1 | 0.061750 |
| variance > 0.75896 and variance <= 1.7875 and curtosis <= -2.3 | 1 | 0.043636 |
| variance < 0.320165 and skewness >= 7.5653 and variance < -4.726 | 1 | 0.025605 |
| variance <= 0.75896 and skewness <= 5.1401 and variance <= 0.31803 and curtosis > 3.0423 and skewness > -1.8624 | 0 | 0.032067 |
| variance >= 0.320165 and curtosis < -4.373200000000001 and variance < 3.30405 | 1 | 0.041958 |
| variance >= 0.320165 and curtosis < -4.373200000000001 and variance >= 3.30405 | 0 | 0.017889 |
| variance < 0.320165 and skewness < 7.5653 and variance >= -0.4031 and skewness < 5.45355 and curtosis < 2.62465 | 1 | 0.070556 |
| variance > 0.760295 and variance <= 1.7907 and skewness > 5.21045 and skewness <= 9.61695 and curtosis > -4.42285 and curtosis <= 8.83885 | 0 | 0.081940 |
| variance < 0.320165 and skewness < 7.5653 and variance < -0.4031 and curtosis >= 6.21865 and skewness >= -4.6745 | 0 | 0.021518 |
| variance < 0.320165 and skewness < 7.5653 and variance >= -0.4031 and skewness < 5.45355 and curtosis >= 2.62465 | 0 | 0.014542 |
| variance < 0.320165 and skewness >= 7.5653 and variance >= -4.726 | 0 | 0.125796 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| variance > 0.75896 and variance > 1.7875 | 0 | 0.437521 |
| skewness <= 5.1401 and variance <= 0.31803 and curtosis <= 3.0423 | 1 | 0.516129 |
| skewness > -4.9518 and curtosis > -3.8869 and variance > -3.3924 and entropy <= -0.33967 | 0 | 0.406896 |
| variance <= -1.786 | 1 | 0.708363 |
| curtosis <= 0.20278 | 1 | 0.519084 |
| skewness > -1.8624 | 0 | 0.500159 |
| variance <= -0.46651 | 1 | 0.879310 |
|  | 0 | 0.636364 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| skewness <= 5.8333 and curtosis <= 6.2169 and variance <= -0.36372 | 1 | 0.286458 |
| skewness <= -4.5152 and variance <= -0.77288 | 1 | 0.145885 |
| curtosis <= 0.27818 and skewness <= 6.2699 and variance <= 1.2572 | 1 | 0.116129 |
| variance <= -4.1479 and curtosis <= 1.0836 | 1 | 0.047288 |
| variance <= 1.7875 and skewness <= 4.78 and curtosis <= -1.8785 | 1 | 0.024217 |
| skewness <= -0.69529 and curtosis <= 2.135 and variance <= 0.74428 | 1 | 0.017217 |
|  | 0 | 0.994194 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

variance|skewness|curtosis|class
---|---|---|---
(-0.4031-0.760295]|(9.61695-inf)|(-4.42285-8.83885]|0
(0.760295-1.7907]|(9.61695-inf)|(-4.42285-8.83885]|0
(1.7907-inf)|(9.61695-inf)|(-4.42285-8.83885]|0
(-2.7952--0.4031]|(9.61695-inf)|(-4.42285-8.83885]|0
(-inf--2.7952]|(-5.5074--2.3021]|(8.83885-inf)|1
(-inf--2.7952]|(5.21045-9.61695]|(-4.42285-8.83885]|1
(-2.7952--0.4031]|(5.21045-9.61695]|(-4.42285-8.83885]|0
(-0.4031-0.760295]|(5.21045-9.61695]|(-4.42285-8.83885]|0
(0.760295-1.7907]|(5.21045-9.61695]|(-4.42285-8.83885]|0
(1.7907-inf)|(5.21045-9.61695]|(-4.42285-8.83885]|0
(-2.7952--0.4031]|(-6.95385--5.5074]|(8.83885-inf)|1
(-inf--2.7952]|(-6.95385--5.5074]|(8.83885-inf)|1
(1.7907-inf)|(9.61695-inf)|(-inf--4.42285]|0
(-inf--2.7952]|(-2.3021-5.21045]|(-4.42285-8.83885]|1
(0.760295-1.7907]|(-2.3021-5.21045]|(-4.42285-8.83885]|0
(-2.7952--0.4031]|(-2.3021-5.21045]|(-4.42285-8.83885]|1
(-0.4031-0.760295]|(-2.3021-5.21045]|(-4.42285-8.83885]|1
(1.7907-inf)|(-2.3021-5.21045]|(-4.42285-8.83885]|0
(-2.7952--0.4031]|(-inf--6.95385]|(8.83885-inf)|1
(-inf--2.7952]|(-inf--6.95385]|(8.83885-inf)|1
(-2.7952--0.4031]|(-5.5074--2.3021]|(-4.42285-8.83885]|1
(1.7907-inf)|(5.21045-9.61695]|(-inf--4.42285]|0
(-0.4031-0.760295]|(-5.5074--2.3021]|(-4.42285-8.83885]|0
(1.7907-inf)|(-5.5074--2.3021]|(-4.42285-8.83885]|0
(0.760295-1.7907]|(-5.5074--2.3021]|(-4.42285-8.83885]|0
(-inf--2.7952]|(-6.95385--5.5074]|(-4.42285-8.83885]|0
(0.760295-1.7907]|(-6.95385--5.5074]|(-4.42285-8.83885]|0
(1.7907-inf)|(-2.3021-5.21045]|(-inf--4.42285]|1
(-0.4031-0.760295]|(-6.95385--5.5074]|(-4.42285-8.83885]|0
(-2.7952--0.4031]|(-6.95385--5.5074]|(-4.42285-8.83885]|1
(0.760295-1.7907]|(-2.3021-5.21045]|(-inf--4.42285]|1
(-0.4031-0.760295]|(-2.3021-5.21045]|(-inf--4.42285]|1
(1.7907-inf)|(-6.95385--5.5074]|(-4.42285-8.83885]|0
(-2.7952--0.4031]|(-inf--6.95385]|(-4.42285-8.83885]|1
(-inf--2.7952]|(-inf--6.95385]|(-4.42285-8.83885]|1

## JRip

Decision list:

rules | predicted class
---|---
(skewness <= 5.8333) and (curtosis <= 6.2169) and (variance <= -0.36372)|1 (275.0/0.0)
(skewness <= -4.5152) and (variance <= -0.77288)|1 (117.0/0.0)
(curtosis <= 0.27818) and (skewness <= 6.2699) and (variance <= 1.2572)|1 (90.0/0.0)
(variance <= -4.1479) and (curtosis <= 1.0836)|1 (34.0/0.0)
(variance <= 1.7875) and (skewness <= 4.78) and (curtosis <= -1.8785)|1 (17.0/0.0)
(skewness <= -0.69529) and (curtosis <= 2.135) and (variance <= 0.74428)|1 (12.0/0.0)
|0 (689.0/4.0)


## PART

Decision list:

rules | predicted class
---|---
variance > 0.75896 AND variance > 1.7875|0 (433.0/3.0)
skewness <= 5.1401 AND variance <= 0.31803 AND curtosis <= 3.0423|1 (272.0)
skewness > -4.9518 AND curtosis > -3.8869 AND variance > -3.3924 AND entropy <= -0.33967|0 (194.0/2.0)
variance <= -1.786|1 (155.0/1.0)
curtosis <= 0.20278|1 (63.0)
skewness > -1.8624|0 (56.0/1.0)
variance <= -0.46651|1 (51.0)
|0 (10.0/3.0)


## J48 Decision Tree

* variance <= 0.75896
	* skewness <= 5.1401
		* variance <= 0.31803
			* curtosis <= 3.0423: 1 (272.0)
			* curtosis > 3.0423
				* skewness <= -1.8624: 1 (170.0/2.0)
				* skewness > -1.8624: 0 (22.0/2.0)
		* variance > 0.31803
			* curtosis <= 0.46583: 1 (27.0)
			* curtosis > 0.46583: 0 (30.0/3.0)
	* skewness > 5.1401
		* variance <= -3.3793: 1 (37.0/1.0)
		* variance > -3.3793: 0 (108.0/1.0)
* variance > 0.75896
	* variance <= 1.7875
		* curtosis <= -2.3: 1 (37.0/3.0)
		* curtosis > -2.3: 0 (98.0/3.0)
	* variance > 1.7875: 0 (433.0/3.0)


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
			* curtosis >= -2.2721999999999998: 0(123.0/17.0)
		* variance >= 1.5922: 0(437.0/2.0)


