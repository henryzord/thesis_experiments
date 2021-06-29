# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| variance >= 0.320165 and curtosis >= -4.38605 and variance >= 1.5922 and variance >= 2.03655 | 0 | 0.412206 |
| variance <= 0.320165 and skewness <= 5.86535 and curtosis <= 6.21865 | 1 | 0.322775 |
| variance > 0.320165 and curtosis > -4.38605 and variance <= 2.03655 and curtosis > -2.2722 and entropy <= 0.092227 | 0 | 0.196204 |
| variance < 0.320165 and skewness < 5.86535 and curtosis >= 6.21865 and skewness < -4.6745 | 1 | 0.145011 |
| variance < 0.320165 and skewness >= 5.86535 and variance >= -3.4833999999999996 | 0 | 0.138148 |
| variance < 0.320165 and skewness >= 5.86535 and variance < -3.4833999999999996 | 1 | 0.047392 |
| variance > 0.320165 and curtosis > -4.38605 and variance <= 2.03655 and curtosis > -2.2722 and entropy > 0.092227 and curtosis > -0.011002 | 0 | 0.060307 |
| variance > 0.320165 and curtosis <= -4.38605 and variance <= 3.30405 | 1 | 0.040673 |
| variance > 0.320165 and curtosis > -4.38605 and variance <= 2.03655 and curtosis <= -2.2722 | 1 | 0.030570 |
| variance <= 0.320165 and skewness <= 5.86535 and curtosis > 6.21865 and skewness > -4.6745 | 0 | 0.036918 |
| variance >= 0.320165 and curtosis >= -4.38605 and variance < 1.5922 and curtosis >= -2.2721999999999998 and entropy >= 0.22994 and curtosis < 1.8736000000000002 | 1 | 0.017344 |
| variance >= 0.320165 and curtosis < -4.38605 and variance >= 3.30405 | 0 | 0.016129 |
| variance > 0.320165 and variance <= 1.74385 and skewness > 5.1608 and skewness <= 9.61695 and curtosis > -4.42545 and curtosis <= 8.83885 | 0 | 0.095552 |
| variance > 1.74385 and variance <= 2.3921 and skewness > 5.1608 and skewness <= 9.61695 and curtosis > -4.42545 and curtosis <= 8.83885 | 0 | 0.050173 |
| variance > 0.320165 and curtosis > -4.38605 and variance <= 2.03655 and curtosis > -2.2722 and entropy > 0.092227 and curtosis <= -0.011002 | 1 | 0.015827 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| variance > 0.91315 and variance > 1.7425 | 0 | 0.437559 |
| skewness <= 5.0097 and variance <= 0.30081 and curtosis <= 6.2169 | 1 | 0.561744 |
| curtosis <= 8.8294 and curtosis > -3.8869 and variance > -4.3876 and skewness > 2.2948 | 0 | 0.442017 |
| variance <= -1.786 | 1 | 0.658453 |
| curtosis > 0.46583 and skewness > -4.8773 | 0 | 0.402200 |
|  | 1 | 0.947917 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| variance <= 0.31803 and skewness <= 5.8333 and curtosis <= 6.2169 | 1 | 0.322775 |
| variance <= -1.3887 and skewness <= -4.5566 | 1 | 0.143930 |
| variance <= 1.7425 and curtosis <= 0.23191 and skewness <= 4.8731 | 1 | 0.081901 |
| variance <= -4.2249 | 1 | 0.047392 |
|  | 0 | 0.985591 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

variance|skewness|curtosis|class
---|---|---|---
(-0.4031-0.320165]|(9.61695-inf)|(-4.42545-8.83885]|0
(0.320165-1.74385]|(9.61695-inf)|(-4.42545-8.83885]|0
(1.74385-2.3921]|(9.61695-inf)|(-4.42545-8.83885]|0
(-2.7952--0.4031]|(9.61695-inf)|(-4.42545-8.83885]|0
(2.3921-inf)|(9.61695-inf)|(-4.42545-8.83885]|0
(-inf--2.7952]|(-5.5074--2.4149]|(8.83885-inf)|1
(-inf--2.7952]|(5.1608-9.61695]|(-4.42545-8.83885]|1
(-2.7952--0.4031]|(5.1608-9.61695]|(-4.42545-8.83885]|0
(-0.4031-0.320165]|(5.1608-9.61695]|(-4.42545-8.83885]|0
(0.320165-1.74385]|(5.1608-9.61695]|(-4.42545-8.83885]|0
(2.3921-inf)|(5.1608-9.61695]|(-4.42545-8.83885]|0
(1.74385-2.3921]|(5.1608-9.61695]|(-4.42545-8.83885]|0
(-2.7952--0.4031]|(-6.94555--5.5074]|(8.83885-inf)|1
(2.3921-inf)|(9.61695-inf)|(-inf--4.42545]|0
(-inf--2.7952]|(-2.4149-5.1608]|(-4.42545-8.83885]|1
(-inf--2.7952]|(-6.94555--5.5074]|(8.83885-inf)|1
(-0.4031-0.320165]|(-2.4149-5.1608]|(-4.42545-8.83885]|1
(1.74385-2.3921]|(-2.4149-5.1608]|(-4.42545-8.83885]|0
(-2.7952--0.4031]|(-2.4149-5.1608]|(-4.42545-8.83885]|1
(0.320165-1.74385]|(-2.4149-5.1608]|(-4.42545-8.83885]|0
(2.3921-inf)|(-2.4149-5.1608]|(-4.42545-8.83885]|0
(2.3921-inf)|(5.1608-9.61695]|(-inf--4.42545]|0
(-0.4031-0.320165]|(-5.5074--2.4149]|(-4.42545-8.83885]|1
(-2.7952--0.4031]|(-5.5074--2.4149]|(-4.42545-8.83885]|1
(-inf--2.7952]|(-inf--6.94555]|(8.83885-inf)|1
(-2.7952--0.4031]|(-inf--6.94555]|(8.83885-inf)|1
(0.320165-1.74385]|(-5.5074--2.4149]|(-4.42545-8.83885]|0
(2.3921-inf)|(-5.5074--2.4149]|(-4.42545-8.83885]|0
(1.74385-2.3921]|(-5.5074--2.4149]|(-4.42545-8.83885]|0
(2.3921-inf)|(-6.94555--5.5074]|(-4.42545-8.83885]|0
(0.320165-1.74385]|(-6.94555--5.5074]|(-4.42545-8.83885]|0
(-0.4031-0.320165]|(-6.94555--5.5074]|(-4.42545-8.83885]|1
(1.74385-2.3921]|(-2.4149-5.1608]|(-inf--4.42545]|1
(-2.7952--0.4031]|(-6.94555--5.5074]|(-4.42545-8.83885]|1
(-0.4031-0.320165]|(-2.4149-5.1608]|(-inf--4.42545]|1
(0.320165-1.74385]|(-2.4149-5.1608]|(-inf--4.42545]|1
(1.74385-2.3921]|(-6.94555--5.5074]|(-4.42545-8.83885]|0
(-inf--2.7952]|(-inf--6.94555]|(-4.42545-8.83885]|1
(-2.7952--0.4031]|(-inf--6.94555]|(-4.42545-8.83885]|1

## JRip

Decision list:

rules | predicted class
---|---
(variance <= 0.31803) and (skewness <= 5.8333) and (curtosis <= 6.2169)|1 (328.0/1.0)
(variance <= -1.3887) and (skewness <= -4.5566)|1 (115.0/0.0)
(variance <= 1.7425) and (curtosis <= 0.23191) and (skewness <= 4.8731)|1 (63.0/1.0)
(variance <= -4.2249)|1 (36.0/1.0)
|0 (691.0/10.0)


## PART

Decision list:

rules | predicted class
---|---
variance > 0.91315 AND variance > 1.7425|0 (287.0/3.0)
skewness <= 5.0097 AND variance <= 0.30081 AND curtosis <= 6.2169|1 (213.0)
curtosis <= 8.8294 AND curtosis > -3.8869 AND variance > -4.3876 AND skewness > 2.2948|0 (123.0/2.0)
variance <= -1.786|1 (87.0/1.0)
curtosis > 0.46583 AND skewness > -4.8773|0 (47.0/1.0)
|1 (65.0/4.0)


## J48 Decision Tree

* variance <= 0.320165
	* skewness <= 5.86535
		* curtosis <= 6.21865: 1 (328.0/1.0)
		* curtosis > 6.21865
			* skewness <= -4.6745: 1 (118.0/1.0)
			* skewness > -4.6745: 0 (23.0/1.0)
	* skewness > 5.86535
		* variance <= -3.4834: 1 (36.0/1.0)
		* variance > -3.4834: 0 (88.0)
* variance > 0.320165
	* curtosis <= -4.38605
		* variance <= 3.30405: 1 (29.0)
		* variance > 3.30405: 0 (9.0)
	* curtosis > -4.38605
		* variance <= 2.03655
			* curtosis <= -2.2722: 1 (29.0/4.0)
			* curtosis > -2.2722
				* entropy <= 0.092227: 0 (136.0/1.0)
				* entropy > 0.092227
					* curtosis <= -0.011002: 1 (11.0)
					* curtosis > -0.011002: 0 (41.0/3.0)
		* variance > 2.03655: 0 (385.0)


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
				* entropy < 0.22994
					* curtosis < -2.1898999999999997: 0(2.0/1.0)
					* curtosis >= -2.1898999999999997
						* variance < 0.42002: 0(15.0/1.0)
						* variance >= 0.42002: 0(93.0/0.0)
				* entropy >= 0.22994
					* curtosis < 1.8736000000000002: 1(13.0/1.0)
					* curtosis >= 1.8736000000000002: 0(14.0/0.0)
		* variance >= 1.5922
			* variance < 2.03655
				* curtosis < -2.6483499999999998: 1(3.0/1.0)
				* curtosis >= -2.6483499999999998: 0(49.0/0.0)
			* variance >= 2.03655: 0(385.0/0.0)


