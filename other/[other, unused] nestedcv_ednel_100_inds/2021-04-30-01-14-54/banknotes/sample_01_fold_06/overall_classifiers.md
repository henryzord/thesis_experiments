# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 0 | 0.555105 |
| variance < 0.320165 and skewness < 8.185 and variance < -0.4031 and curtosis >= 6.21865 and skewness < -2.9622 | 1 | 0.145885 |
| variance <= 0.31803 and skewness <= 7.5404 and variance <= -1.786 | 1 | 0.274368 |
| variance > 0.31803 and curtosis <= -4.4738 | 1 | 0.030890 |
| variance <= 0.31803 and skewness <= 7.5404 and variance > -1.786 and skewness <= 3.9213 and curtosis <= 6.2109 | 1 | 0.207182 |
| variance < 0.320165 and skewness < 8.185 and variance >= -0.4031 and skewness < 5.4939 and curtosis < 2.62465 | 1 | 0.070556 |
| variance > 0.31803 and curtosis > -4.4738 and variance <= 1.5904 and curtosis <= -2.2726 | 1 | 0.028860 |
| variance > -0.4031 and variance <= 0.760295 and skewness > -2.3021 and skewness <= 5.21045 and curtosis > -4.42285 and curtosis <= 8.83885 | 1 | 0.055944 |
| variance <= 0.31803 and skewness > 7.5404 and variance <= -4.8861 | 1 | 0.025605 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| variance > 0.760295 and curtosis > -1.8648 | 0 | 0.403261 |
| skewness <= 5.1608 and variance <= -1.78205 | 1 | 0.434242 |
| skewness > 5.21045 and variance > -3.4449 | 0 | 0.454707 |
| curtosis <= 0.7216 and variance <= 1.5857 | 1 | 0.785978 |
| skewness <= -0.9436 and variance <= -0.462635 | 1 | 0.536000 |
| curtosis > 2.1671 | 0 | 0.609025 |
| variance > 0.32457 and curtosis > -2.59825 | 0 | 0.330882 |
|  | 1 | 1.000000 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| skewness <= 5.1401 and curtosis <= 6.2169 and variance <= -0.36372 | 1 | 0.287942 |
| skewness <= -4.5152 and variance <= -0.55355 | 1 | 0.145885 |
| variance <= 1.6799 and skewness <= 5.2022 and curtosis <= 0.18307 | 1 | 0.129606 |
| variance <= -4.1479 and curtosis <= 1.0836 | 1 | 0.049931 |
| skewness <= -0.69529 and curtosis <= 2.135 and variance <= 0.74428 | 1 | 0.015805 |
|  | 0 | 0.991317 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

variance|skewness|curtosis|class
---|---|---|---
(2.3921-inf)|(9.53215-inf)|(-4.42285-8.83885]|0
(0.760295-2.3921]|(9.53215-inf)|(-4.42285-8.83885]|0
(-0.4031-0.760295]|(9.53215-inf)|(-4.42285-8.83885]|0
(-2.7952--0.4031]|(9.53215-inf)|(-4.42285-8.83885]|0
(-2.7952--0.4031]|(5.21045-9.53215]|(-4.42285-8.83885]|0
(0.760295-2.3921]|(5.21045-9.53215]|(-4.42285-8.83885]|0
(-0.4031-0.760295]|(5.21045-9.53215]|(-4.42285-8.83885]|0
(2.3921-inf)|(5.21045-9.53215]|(-4.42285-8.83885]|0
(-inf--2.7952]|(-5.436--2.3021]|(8.83885-inf)|1
(-inf--2.7952]|(5.21045-9.53215]|(-4.42285-8.83885]|1
(2.3921-inf)|(9.53215-inf)|(-inf--4.42285]|0
(2.3921-inf)|(-2.3021-5.21045]|(-4.42285-8.83885]|0
(-inf--2.7952]|(-6.94555--5.436]|(8.83885-inf)|1
(-inf--2.7952]|(-2.3021-5.21045]|(-4.42285-8.83885]|1
(-2.7952--0.4031]|(-6.94555--5.436]|(8.83885-inf)|1
(0.760295-2.3921]|(-2.3021-5.21045]|(-4.42285-8.83885]|0
(-0.4031-0.760295]|(-2.3021-5.21045]|(-4.42285-8.83885]|1
(-2.7952--0.4031]|(-2.3021-5.21045]|(-4.42285-8.83885]|1
(2.3921-inf)|(5.21045-9.53215]|(-inf--4.42285]|0
(2.3921-inf)|(-5.436--2.3021]|(-4.42285-8.83885]|0
(0.760295-2.3921]|(-5.436--2.3021]|(-4.42285-8.83885]|0
(-2.7952--0.4031]|(-5.436--2.3021]|(-4.42285-8.83885]|1
(-0.4031-0.760295]|(-5.436--2.3021]|(-4.42285-8.83885]|0
(-inf--2.7952]|(-inf--6.94555]|(8.83885-inf)|1
(-2.7952--0.4031]|(-inf--6.94555]|(8.83885-inf)|1
(2.3921-inf)|(-6.94555--5.436]|(-4.42285-8.83885]|0
(-inf--2.7952]|(-6.94555--5.436]|(-4.42285-8.83885]|0
(-0.4031-0.760295]|(-6.94555--5.436]|(-4.42285-8.83885]|0
(0.760295-2.3921]|(-6.94555--5.436]|(-4.42285-8.83885]|0
(0.760295-2.3921]|(-2.3021-5.21045]|(-inf--4.42285]|1
(-0.4031-0.760295]|(-2.3021-5.21045]|(-inf--4.42285]|1
(-2.7952--0.4031]|(-6.94555--5.436]|(-4.42285-8.83885]|1
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
|0 (691.0/6.0)


## PART

Decision list:

rules | predicted class
---|---
variance > 0.760295 AND curtosis > -1.8648|0 (371.0)
skewness <= 5.1608 AND variance <= -1.78205|1 (243.0/1.0)
skewness > 5.21045 AND variance > -3.4449|0 (256.0)
curtosis <= 0.7216 AND variance <= 1.5857|1 (213.0)
skewness <= -0.9436 AND variance <= -0.462635|1 (67.0)
curtosis > 2.1671|0 (43.0/1.0)
variance > 0.32457 AND curtosis > -2.59825|0 (17.0/2.0)
|1 (24.0)


## J48 Decision Tree

* variance <= 0.31803
	* skewness <= 7.5404
		* variance <= -1.786: 1 (232.0/1.0)
		* variance > -1.786
			* skewness <= 3.9213
				* curtosis <= 6.2109: 1 (156.0/1.0)
				* curtosis > 6.2109
					* skewness <= -3.3315: 1 (17.0/1.0)
					* skewness > -3.3315: 0 (19.0)
			* skewness > 3.9213: 0 (12.0/2.0)
	* skewness > 7.5404
		* variance <= -4.8861: 1 (14.0)
		* variance > -4.8861: 0 (70.0)
* variance > 0.31803
	* curtosis <= -4.4738: 1 (34.0/8.0)
	* curtosis > -4.4738
		* variance <= 1.5904
			* curtosis <= -2.2726: 1 (24.0/3.0)
			* curtosis > -2.2726: 0 (120.0/13.0)
		* variance > 1.5904: 0 (382.0/2.0)


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
	* curtosis < -4.4434000000000005
		* variance < 3.30405: 1(28.0/0.0)
		* variance >= 3.30405: 0(8.0/0.0)
	* curtosis >= -4.4434000000000005
		* variance < 1.5962
			* curtosis < -2.2721999999999998: 1(23.0/3.0)
			* curtosis >= -2.2721999999999998: 0(125.0/16.0)
		* variance >= 1.5962: 0(435.0/2.0)


