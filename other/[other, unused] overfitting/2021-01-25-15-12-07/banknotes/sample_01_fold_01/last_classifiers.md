# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 0 | 0.554745 |
| variance >= 0.320165 and curtosis >= -4.38605 and variance < 1.5922 and curtosis >= -2.2721999999999998 and entropy >= 0.22994 and curtosis < 1.8736000000000002 | 1 | 0.017344 |
| variance > 0.321235 and variance <= 1.74385 and curtosis <= -2.2859 | 1 | 0.063123 |
| variance < 0.320165 and skewness < 5.86535 and curtosis >= 6.21865 and skewness < -4.6745 | 1 | 0.145011 |
| variance > 0.321235 and variance > 1.74385 and curtosis <= -4.26475 and variance <= 2.95365 | 1 | 0.004367 |
| variance > 0.321235 and variance <= 1.74385 and curtosis > -2.2859 and entropy > 0.08964 and curtosis <= 0.32402 | 1 | 0.017241 |
| variance < 0.320165 and skewness < 5.86535 and curtosis < 6.21865 and skewness >= 4.09405 | 1 | 0.015938 |
| variance > -0.4031 and variance <= 0.320165 and skewness > -2.4149 and skewness <= 5.1608 and curtosis > -4.42545 and curtosis <= 8.83885 and entropy = all | 1 | 0.047847 |
| variance < 0.320165 and skewness < 5.86535 and curtosis < 6.21865 and skewness < 4.09405 | 1 | 0.315315 |
| variance < 0.320165 and skewness >= 5.86535 and variance < -3.4833999999999996 | 1 | 0.047392 |
| variance >= 0.320165 and curtosis >= -4.38605 and variance < 1.5922 and curtosis < -2.2721999999999998 | 1 | 0.028646 |
| variance <= 0.321235 and skewness <= 6.10645 and curtosis <= 6.7456 | 1 | 0.328140 |
| variance >= 0.320165 and curtosis >= -4.38605 and variance >= 1.5922 and variance < 2.03655 and curtosis < -2.6483499999999998 | 1 | 0.003280 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| variance > 0.31803 and curtosis > -4.3882 and variance > 2.031 | 0 | 0.412206 |
| skewness > 5.1401 and variance > -3.3793 | 0 | 0.251023 |
| variance <= 0.31803 and curtosis <= 3.0423 | 1 | 0.730047 |
| skewness <= -5.1277 and variance <= -0.46651 | 1 | 0.572491 |
| curtosis <= 0.20792 and curtosis <= -1.3927 | 1 | 0.346591 |
| entropy <= -0.1651 | 0 | 0.732558 |
| skewness > 0.7201 | 0 | 0.616667 |
| curtosis <= 7.0078 and variance <= 0.6818 | 1 | 0.594595 |
|  | 0 | 0.937500 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| variance <= 0.31803 and skewness <= 5.8333 and curtosis <= 6.2169 | 1 | 0.322775 |
| skewness <= -4.5152 and variance <= -0.77288 | 1 | 0.146067 |
| variance <= 1.6799 and curtosis <= 0.25933 and skewness <= 4.987 | 1 | 0.078254 |
| variance <= -4.2249 | 1 | 0.047392 |
| curtosis <= -2.9581 and skewness <= 3.6833 | 1 | 0.004367 |
| curtosis <= -4.7412 and variance <= 2.3917 | 1 | 0.005814 |
| entropy >= 0.74394 and variance <= 0.74428 and curtosis <= 6.7156 | 1 | 0.004367 |
|  | 0 | 1.000000 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

variance|skewness|curtosis|entropy|class
---|---|---|---|---
(1.74385-2.3921]|(9.61695-inf)|(-4.42545-8.83885]|all|0
(0.320165-1.74385]|(9.61695-inf)|(-4.42545-8.83885]|all|0
(2.3921-inf)|(9.61695-inf)|(-4.42545-8.83885]|all|0
(-0.4031-0.320165]|(9.61695-inf)|(-4.42545-8.83885]|all|0
(-2.7952--0.4031]|(9.61695-inf)|(-4.42545-8.83885]|all|0
(-inf--2.7952]|(-5.5074--2.4149]|(8.83885-inf)|all|1
(-inf--2.7952]|(5.1608-9.61695]|(-4.42545-8.83885]|all|1
(1.74385-2.3921]|(5.1608-9.61695]|(-4.42545-8.83885]|all|0
(-0.4031-0.320165]|(5.1608-9.61695]|(-4.42545-8.83885]|all|0
(2.3921-inf)|(5.1608-9.61695]|(-4.42545-8.83885]|all|0
(0.320165-1.74385]|(5.1608-9.61695]|(-4.42545-8.83885]|all|0
(-2.7952--0.4031]|(5.1608-9.61695]|(-4.42545-8.83885]|all|0
(-2.7952--0.4031]|(-6.94555--5.5074]|(8.83885-inf)|all|1
(-inf--2.7952]|(-6.94555--5.5074]|(8.83885-inf)|all|1
(-inf--2.7952]|(-2.4149-5.1608]|(-4.42545-8.83885]|all|1
(-0.4031-0.320165]|(-2.4149-5.1608]|(-4.42545-8.83885]|all|1
(1.74385-2.3921]|(-2.4149-5.1608]|(-4.42545-8.83885]|all|0
(2.3921-inf)|(9.61695-inf)|(-inf--4.42545]|all|0
(2.3921-inf)|(-2.4149-5.1608]|(-4.42545-8.83885]|all|0
(0.320165-1.74385]|(-2.4149-5.1608]|(-4.42545-8.83885]|all|0
(-2.7952--0.4031]|(-2.4149-5.1608]|(-4.42545-8.83885]|all|1
(-2.7952--0.4031]|(-inf--6.94555]|(8.83885-inf)|all|1
(-inf--2.7952]|(-inf--6.94555]|(8.83885-inf)|all|1
(-0.4031-0.320165]|(-5.5074--2.4149]|(-4.42545-8.83885]|all|1
(-2.7952--0.4031]|(-5.5074--2.4149]|(-4.42545-8.83885]|all|1
(0.320165-1.74385]|(-5.5074--2.4149]|(-4.42545-8.83885]|all|0
(1.74385-2.3921]|(-5.5074--2.4149]|(-4.42545-8.83885]|all|0
(2.3921-inf)|(-5.5074--2.4149]|(-4.42545-8.83885]|all|0
(2.3921-inf)|(5.1608-9.61695]|(-inf--4.42545]|all|0
(0.320165-1.74385]|(-6.94555--5.5074]|(-4.42545-8.83885]|all|0
(1.74385-2.3921]|(-2.4149-5.1608]|(-inf--4.42545]|all|1
(-0.4031-0.320165]|(-2.4149-5.1608]|(-inf--4.42545]|all|1
(0.320165-1.74385]|(-2.4149-5.1608]|(-inf--4.42545]|all|1
(-2.7952--0.4031]|(-6.94555--5.5074]|(-4.42545-8.83885]|all|1
(1.74385-2.3921]|(-6.94555--5.5074]|(-4.42545-8.83885]|all|0
(2.3921-inf)|(-6.94555--5.5074]|(-4.42545-8.83885]|all|0
(-0.4031-0.320165]|(-6.94555--5.5074]|(-4.42545-8.83885]|all|1
(-inf--2.7952]|(-inf--6.94555]|(-4.42545-8.83885]|all|1
(-2.7952--0.4031]|(-inf--6.94555]|(-4.42545-8.83885]|all|1

## JRip

Decision list:

rules | predicted class
---|---
(variance <= 0.31803) and (skewness <= 5.8333) and (curtosis <= 6.2169)|1 (328.0/1.0)
(skewness <= -4.5152) and (variance <= -0.77288)|1 (117.0/0.0)
(variance <= 1.6799) and (curtosis <= 0.25933) and (skewness <= 4.987)|1 (62.0/2.0)
(variance <= -4.2249)|1 (36.0/1.0)
(curtosis <= -2.9581) and (skewness <= 3.6833)|1 (3.0/0.0)
(curtosis <= -4.7412) and (variance <= 2.3917)|1 (4.0/0.0)
(entropy >= 0.74394) and (variance <= 0.74428) and (curtosis <= 6.7156)|1 (3.0/0.0)
|0 (680.0/0.0)


## PART

Decision list:

rules | predicted class
---|---
variance > 0.31803 AND curtosis > -4.3882 AND variance > 2.031|0 (385.0)
skewness > 5.1401 AND variance > -3.3793|0 (184.0)
variance <= 0.31803 AND curtosis <= 3.0423|1 (311.0)
skewness <= -5.1277 AND variance <= -0.46651|1 (154.0)
curtosis <= 0.20792 AND curtosis <= -1.3927|1 (61.0)
entropy <= -0.1651|0 (63.0)
skewness > 0.7201|0 (37.0)
curtosis <= 7.0078 AND variance <= 0.6818|1 (22.0)
|0 (16.0/1.0)


## J48 Decision Tree

* variance <= 0.321235
	* skewness <= 6.10645
		* curtosis <= 6.7456: 1 (227.0/1.0)
		* curtosis > 6.7456
			* skewness <= -4.89695: 1 (70.0)
			* skewness > -4.89695: 0 (16.0)
	* skewness > 6.10645
		* variance <= -4.586: 1 (22.0)
		* variance > -4.586: 0 (51.0)
* variance > 0.321235
	* variance <= 1.74385
		* curtosis <= -2.2859: 1 (36.0/1.0)
		* curtosis > -2.2859
			* entropy <= 0.08964: 0 (74.0/1.0)
			* entropy > 0.08964
				* curtosis <= 0.32402: 1 (9.0)
				* curtosis > 0.32402: 0 (19.0/1.0)
	* variance > 1.74385
		* curtosis <= -4.26475
			* variance <= 2.95365: 1 (2.0)
			* variance > 2.95365: 0 (13.0)
		* curtosis > -4.26475: 0 (283.0)


## SimpleCart Decision Tree

* variance < 0.320165
	* skewness < 5.86535
		* curtosis < 6.21865
			* skewness < 4.09405: 1(315.0/0.0)
			* skewness >= 4.09405: 1(12.0/1.0)
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
				* entropy < 0.22994: 0(110.0/2.0)
				* entropy >= 0.22994
					* curtosis < 1.8736000000000002: 1(13.0/1.0)
					* curtosis >= 1.8736000000000002: 0(14.0/0.0)
		* variance >= 1.5922
			* variance < 2.03655
				* curtosis < -2.6483499999999998: 1(3.0/1.0)
				* curtosis >= -2.6483499999999998: 0(49.0/0.0)
			* variance >= 2.03655: 0(385.0/0.0)


