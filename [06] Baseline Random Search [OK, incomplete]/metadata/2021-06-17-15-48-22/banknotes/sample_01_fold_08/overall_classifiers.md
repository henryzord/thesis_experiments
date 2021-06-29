# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 0 | 0.555466 |
| variance > 0.31803 and curtosis <= -4.3882 and skewness <= 7.1907 | 1 | 0.040559 |
| variance < 0.320165 and skewness < 7.5653 and variance < -0.38902000000000003 and curtosis < 6.21865 | 1 | 0.298569 |
| variance <= 0.31803 and skewness <= 7.5404 and variance <= -1.786 | 1 | 0.274078 |
| variance < 0.320165 and skewness < 7.5653 and variance < -0.38902000000000003 and curtosis >= 6.21865 and skewness < -4.6745 | 1 | 0.145704 |
| variance > 0.31803 and curtosis > -4.3882 and variance <= 2.031 and curtosis > -1.7542 and entropy > 0.12585 and variance <= 0.77805 and curtosis <= 1.9507 | 1 | 0.014368 |
| variance > -2.7952 and variance <= 0.320165 and skewness > -2.3021 and skewness <= 5.21045 and curtosis > -4.42285 and curtosis <= 8.83885 | 1 | 0.213934 |
| variance >= 0.320165 and curtosis >= -4.38605 and variance < 1.5922 and curtosis < -2.2859 | 1 | 0.026101 |
| variance >= 0.320165 and curtosis >= -4.38605 and variance < 1.5922 and curtosis >= -2.2859 and entropy >= 0.081882 and curtosis < 1.85305 | 1 | 0.018935 |
| variance < 0.320165 and skewness >= 7.5653 and variance < -4.726 | 1 | 0.025568 |
| variance > 0.31803 and curtosis > -4.3882 and variance <= 2.031 and curtosis <= -1.7542 and skewness <= 5.6222 | 1 | 0.040559 |
| variance <= 0.31803 and skewness <= 7.5404 and variance > -1.786 and curtosis <= 6.7807 and skewness <= 3.9213 | 1 | 0.211519 |
| variance < 0.320165 and skewness < 7.5653 and variance >= -0.38902000000000003 | 1 | 0.057056 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| variance > 0.31803 and curtosis > -4.3882 and variance > 2.031 | 0 | 0.419048 |
| skewness > 5.2684 and variance > -3.3793 | 0 | 0.240664 |
| variance <= 0.31803 and curtosis <= 3.0423 | 1 | 0.728972 |
| skewness <= -5.1277 and variance <= -0.46651 | 1 | 0.570370 |
| curtosis > 0.20278 and variance > -0.37013 | 0 | 0.528926 |
| curtosis <= 6.7156 and curtosis <= -1.4938 | 1 | 0.746835 |
| skewness <= 0.7201 and entropy > -0.059065 | 1 | 0.513256 |
|  | 0 | 0.909091 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| variance <= 0.30081 and skewness <= 5.8333 and curtosis <= 6.7156 | 1 | 0.327477 |
| variance <= -1.3968 and skewness <= -5.1463 | 1 | 0.133838 |
| variance <= 1.7875 and curtosis <= -2.3 and skewness <= 5.2022 | 1 | 0.065395 |
| variance <= -4.1479 | 1 | 0.048581 |
| variance <= 2.1943 and entropy >= 0.003003 and curtosis <= 0.78543 and skewness <= 1.852 | 1 | 0.021398 |
|  | 0 | 0.989899 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

variance|skewness|curtosis|class
---|---|---|---
(1.7907-2.3921]|(9.61695-inf)|(-4.42285-8.83885]|0
(-2.7952-0.320165]|(9.61695-inf)|(-4.42285-8.83885]|0
(2.3921-inf)|(9.61695-inf)|(-4.42285-8.83885]|0
(0.320165-1.7907]|(9.61695-inf)|(-4.42285-8.83885]|0
(-inf--2.7952]|(-5.62225--2.3021]|(8.83885-inf)|1
(-inf--2.7952]|(5.21045-9.61695]|(-4.42285-8.83885]|1
(-2.7952-0.320165]|(5.21045-9.61695]|(-4.42285-8.83885]|0
(1.7907-2.3921]|(5.21045-9.61695]|(-4.42285-8.83885]|0
(0.320165-1.7907]|(5.21045-9.61695]|(-4.42285-8.83885]|0
(2.3921-inf)|(5.21045-9.61695]|(-4.42285-8.83885]|0
(-2.7952-0.320165]|(-6.94555--5.62225]|(8.83885-inf)|1
(-inf--2.7952]|(-6.94555--5.62225]|(8.83885-inf)|1
(-inf--2.7952]|(-2.3021-5.21045]|(-4.42285-8.83885]|1
(2.3921-inf)|(9.61695-inf)|(-inf--4.42285]|0
(-2.7952-0.320165]|(-2.3021-5.21045]|(-4.42285-8.83885]|1
(0.320165-1.7907]|(-2.3021-5.21045]|(-4.42285-8.83885]|0
(2.3921-inf)|(-2.3021-5.21045]|(-4.42285-8.83885]|0
(1.7907-2.3921]|(-2.3021-5.21045]|(-4.42285-8.83885]|0
(-2.7952-0.320165]|(-inf--6.94555]|(8.83885-inf)|1
(-inf--2.7952]|(-inf--6.94555]|(8.83885-inf)|1
(2.3921-inf)|(5.21045-9.61695]|(-inf--4.42285]|0
(1.7907-2.3921]|(-5.62225--2.3021]|(-4.42285-8.83885]|0
(0.320165-1.7907]|(-5.62225--2.3021]|(-4.42285-8.83885]|0
(-2.7952-0.320165]|(-5.62225--2.3021]|(-4.42285-8.83885]|1
(2.3921-inf)|(-5.62225--2.3021]|(-4.42285-8.83885]|0
(-inf--2.7952]|(-6.94555--5.62225]|(-4.42285-8.83885]|0
(2.3921-inf)|(-6.94555--5.62225]|(-4.42285-8.83885]|0
(-2.7952-0.320165]|(-2.3021-5.21045]|(-inf--4.42285]|1
(1.7907-2.3921]|(-2.3021-5.21045]|(-inf--4.42285]|1
(0.320165-1.7907]|(-2.3021-5.21045]|(-inf--4.42285]|1
(-2.7952-0.320165]|(-6.94555--5.62225]|(-4.42285-8.83885]|1
(0.320165-1.7907]|(-6.94555--5.62225]|(-4.42285-8.83885]|0
(1.7907-2.3921]|(-6.94555--5.62225]|(-4.42285-8.83885]|0
(-inf--2.7952]|(-inf--6.94555]|(-4.42285-8.83885]|1
(-2.7952-0.320165]|(-inf--6.94555]|(-4.42285-8.83885]|1

## JRip

Decision list:

rules | predicted class
---|---
(variance <= 0.30081) and (skewness <= 5.8333) and (curtosis <= 6.7156)|1 (340.0/3.0)
(variance <= -1.3968) and (skewness <= -5.1463)|1 (106.0/0.0)
(variance <= 1.7875) and (curtosis <= -2.3) and (skewness <= 5.2022)|1 (48.0/0.0)
(variance <= -4.1479)|1 (37.0/1.0)
(variance <= 2.1943) and (entropy >= 0.003003) and (curtosis <= 0.78543) and (skewness <= 1.852)|1 (15.0/0.0)
|0 (689.0/7.0)


## PART

Decision list:

rules | predicted class
---|---
variance > 0.31803 AND curtosis > -4.3882 AND variance > 2.031|0 (396.0)
skewness > 5.2684 AND variance > -3.3793|0 (174.0)
variance <= 0.31803 AND curtosis <= 3.0423|1 (312.0)
skewness <= -5.1277 AND variance <= -0.46651|1 (154.0)
curtosis > 0.20278 AND variance > -0.37013|0 (99.0/3.0)
curtosis <= 6.7156 AND curtosis <= -1.4938|1 (59.0)
skewness <= 0.7201 AND entropy > -0.059065|1 (20.0/1.0)
|0 (21.0/2.0)


## J48 Decision Tree

* variance <= 0.31803
	* skewness <= 7.5404
		* variance <= -1.786: 1 (261.0/1.0)
		* variance > -1.786
			* curtosis <= 6.7807
				* skewness <= 3.9213: 1 (188.0/2.0)
				* skewness > 3.9213
					* curtosis <= -3.521: 1 (4.0)
					* curtosis > -3.521: 0 (8.0)
			* curtosis > 6.7807
				* skewness <= -5.554: 1 (14.0/1.0)
				* skewness > -5.554: 0 (19.0)
	* skewness > 7.5404
		* variance <= -4.7331: 1 (18.0)
		* variance > -4.7331: 0 (75.0)
* variance > 0.31803
	* curtosis <= -4.3882
		* skewness <= 7.1907: 1 (29.0)
		* skewness > 7.1907: 0 (7.0)
	* curtosis > -4.3882
		* variance <= 2.031
			* curtosis <= -1.7542
				* skewness <= 5.6222: 1 (29.0)
				* skewness > 5.6222: 0 (14.0)
			* curtosis > -1.7542
				* entropy <= 0.12585: 0 (129.0)
				* entropy > 0.12585
					* variance <= 0.77805
						* curtosis <= 1.9507: 1 (10.0)
						* curtosis > 1.9507: 0 (5.0)
					* variance > 0.77805: 0 (29.0)
		* variance > 2.031: 0 (396.0)


## SimpleCart Decision Tree

* variance < 0.320165
	* skewness < 7.5653
		* variance < -0.38902000000000003
			* curtosis < 6.21865: 1(292.0/0.0)
			* curtosis >= 6.21865
				* skewness < -4.6745: 1(117.0/0.0)
				* skewness >= -4.6745: 0(16.0/1.0)
		* variance >= -0.38902000000000003: 1(53.0/15.0)
	* skewness >= 7.5653
		* variance < -4.726: 1(18.0/0.0)
		* variance >= -4.726: 0(75.0/0.0)
* variance >= 0.320165
	* curtosis < -4.38605: 1(29.0/7.0)
	* curtosis >= -4.38605
		* variance < 1.5922
			* curtosis < -2.2859: 1(21.0/3.0)
			* curtosis >= -2.2859
				* entropy < 0.081882: 0(110.0/0.0)
				* entropy >= 0.081882
					* curtosis < 1.85305: 1(15.0/2.0)
					* curtosis >= 1.85305: 0(15.0/0.0)
		* variance >= 1.5922: 0(443.0/3.0)


