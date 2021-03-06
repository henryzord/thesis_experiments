# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 0 | 0.555105 |
| variance <= 0.75896 and skewness > 5.1401 and variance <= -3.3793 | 1 | 0.048649 |
| variance <= 0.75896 and skewness <= 5.1401 and variance > 0.31803 and curtosis <= 0.46583 | 1 | 0.037921 |
| variance <= 0.75896 and skewness <= 5.1401 and variance <= 0.31803 and curtosis <= 3.0423 | 1 | 0.284222 |
| variance >= 0.320165 and curtosis >= -4.373200000000001 and variance < 1.5922 and curtosis < -2.2721999999999998 and skewness < 5.6667 | 1 | 0.031117 |
| variance <= 0.75896 and skewness <= 5.1401 and variance <= 0.31803 and curtosis > 3.0423 and skewness > -1.8624 and variance <= -2.1652 | 1 | 0.001944 |
| variance > 0.75896 and variance <= 1.7875 and curtosis <= -2.3 and skewness <= 6.2265 | 1 | 0.047288 |
| variance < 0.320165 and skewness < 7.5653 and variance < -0.4031 and curtosis < 6.21865 and skewness < 7.293150000000001 | 1 | 0.295267 |
| variance < 0.320165 and skewness < 7.5653 and variance < -0.4031 and curtosis >= 6.21865 and skewness < -4.6745 | 1 | 0.145885 |
| variance <= 0.75896 and skewness <= 5.1401 and variance <= 0.31803 and curtosis > 3.0423 and skewness <= -1.8624 and variance > -0.69078 and curtosis <= 5.7491 | 1 | 0.008683 |
| variance <= 0.75896 and skewness <= 5.1401 and variance <= 0.31803 and curtosis > 3.0423 and skewness <= -1.8624 and variance <= -0.69078 | 1 | 0.190307 |
| variance <= 0.75896 and skewness <= 5.1401 and variance > 0.31803 and curtosis > 0.46583 and entropy > 0.71808 | 1 | 0.004360 |
| variance >= 0.320165 and curtosis >= -4.373200000000001 and variance < 1.5922 and curtosis >= -2.2721999999999998 and entropy >= 0.081882 and curtosis < 1.91945 and skewness < 3.5591749999999998 | 1 | 0.022825 |
| variance >= 0.320165 and curtosis < -4.373200000000001 and variance < 3.30405 | 1 | 0.041958 |

## Ordered rules

# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

variance|skewness|curtosis|class
---|---|---|---
(0.760295-1.7907]|(9.61695-inf)|(-4.42285-8.83885]|0
(-0.4031-0.760295]|(9.61695-inf)|(-4.42285-8.83885]|0
(-2.7952--0.4031]|(9.61695-inf)|(-4.42285-8.83885]|0
(1.7907-inf)|(9.61695-inf)|(-4.42285-8.83885]|0
(-inf--2.7952]|(5.21045-9.61695]|(-4.42285-8.83885]|1
(-inf--2.7952]|(-5.5074--2.3021]|(8.83885-inf)|1
(0.760295-1.7907]|(5.21045-9.61695]|(-4.42285-8.83885]|0
(1.7907-inf)|(5.21045-9.61695]|(-4.42285-8.83885]|0
(-0.4031-0.760295]|(5.21045-9.61695]|(-4.42285-8.83885]|0
(-2.7952--0.4031]|(5.21045-9.61695]|(-4.42285-8.83885]|0
(-2.7952--0.4031]|(-6.95385--5.5074]|(8.83885-inf)|1
(-inf--2.7952]|(-2.3021-5.21045]|(-4.42285-8.83885]|1
(-inf--2.7952]|(-6.95385--5.5074]|(8.83885-inf)|1
(-2.7952--0.4031]|(-2.3021-5.21045]|(-4.42285-8.83885]|1
(1.7907-inf)|(-2.3021-5.21045]|(-4.42285-8.83885]|0
(1.7907-inf)|(9.61695-inf)|(-inf--4.42285]|0
(-0.4031-0.760295]|(-2.3021-5.21045]|(-4.42285-8.83885]|1
(0.760295-1.7907]|(-2.3021-5.21045]|(-4.42285-8.83885]|0
(1.7907-inf)|(5.21045-9.61695]|(-inf--4.42285]|0
(-2.7952--0.4031]|(-5.5074--2.3021]|(-4.42285-8.83885]|1
(-2.7952--0.4031]|(-inf--6.95385]|(8.83885-inf)|1
(-inf--2.7952]|(-inf--6.95385]|(8.83885-inf)|1
(-0.4031-0.760295]|(-5.5074--2.3021]|(-4.42285-8.83885]|0
(0.760295-1.7907]|(-5.5074--2.3021]|(-4.42285-8.83885]|0
(1.7907-inf)|(-5.5074--2.3021]|(-4.42285-8.83885]|0
(-inf--2.7952]|(-6.95385--5.5074]|(-4.42285-8.83885]|0
(1.7907-inf)|(-2.3021-5.21045]|(-inf--4.42285]|1
(0.760295-1.7907]|(-6.95385--5.5074]|(-4.42285-8.83885]|0
(-0.4031-0.760295]|(-6.95385--5.5074]|(-4.42285-8.83885]|0
(-0.4031-0.760295]|(-2.3021-5.21045]|(-inf--4.42285]|1
(0.760295-1.7907]|(-2.3021-5.21045]|(-inf--4.42285]|1
(-2.7952--0.4031]|(-6.95385--5.5074]|(-4.42285-8.83885]|1
(1.7907-inf)|(-6.95385--5.5074]|(-4.42285-8.83885]|0
(-inf--2.7952]|(-inf--6.95385]|(-4.42285-8.83885]|1
(-2.7952--0.4031]|(-inf--6.95385]|(-4.42285-8.83885]|1

## J48 Decision Tree

* variance <= 0.75896
	* skewness <= 5.1401
		* variance <= 0.31803
			* curtosis <= 3.0423: 1 (272.0)
			* curtosis > 3.0423
				* skewness <= -1.8624
					* variance <= -0.69078: 1 (161.0)
					* variance > -0.69078
						* curtosis <= 5.7491: 1 (6.0)
						* curtosis > 5.7491: 0 (3.0/1.0)
				* skewness > -1.8624
					* variance <= -2.1652: 1 (3.0/1.0)
					* variance > -2.1652: 0 (19.0)
		* variance > 0.31803
			* curtosis <= 0.46583: 1 (27.0)
			* curtosis > 0.46583
				* entropy <= 0.71808: 0 (27.0)
				* entropy > 0.71808: 1 (3.0)
	* skewness > 5.1401
		* variance <= -3.3793: 1 (37.0/1.0)
		* variance > -3.3793: 0 (108.0/1.0)
* variance > 0.75896
	* variance <= 1.7875
		* curtosis <= -2.3
			* skewness <= 6.2265: 1 (34.0)
			* skewness > 6.2265: 0 (3.0)
		* curtosis > -2.3
			* entropy <= 0.63403: 0 (87.0)
			* entropy > 0.63403
				* curtosis <= -0.16823: 1 (3.0)
				* curtosis > -0.16823: 0 (8.0)
	* variance > 1.7875: 0 (433.0/3.0)


## SimpleCart Decision Tree

* variance < 0.320165
	* skewness < 7.5653
		* variance < -0.4031
			* curtosis < 6.21865
				* skewness < 7.293150000000001: 1(287.0/0.0)
				* skewness >= 7.293150000000001: 1(2.0/1.0)
			* curtosis >= 6.21865
				* skewness < -4.6745: 1(117.0/0.0)
				* skewness >= -4.6745
					* variance < -2.1171: 0(1.0/1.0)
					* variance >= -2.1171: 0(12.0/0.0)
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
			* curtosis < -2.2721999999999998
				* skewness < 5.6667: 1(22.0/0.0)
				* skewness >= 5.6667: 0(3.0/0.0)
			* curtosis >= -2.2721999999999998
				* entropy < 0.081882
					* variance < 0.42002: 0(14.0/1.0)
					* variance >= 0.42002: 0(91.0/0.0)
				* entropy >= 0.081882
					* curtosis < 1.91945
						* skewness < 3.5591749999999998: 1(16.0/0.0)
						* skewness >= 3.5591749999999998: 0(2.0/0.0)
					* curtosis >= 1.91945: 0(16.0/0.0)
		* variance >= 1.5922
			* variance < 1.7438500000000001: 0(11.0/1.0)
			* variance >= 1.7438500000000001
				* variance < 2.0185: 0(38.0/1.0)
				* variance >= 2.0185: 0(388.0/0.0)


