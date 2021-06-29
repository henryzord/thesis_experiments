# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 0 | 0.555105 |
| variance > 0.518 and curtosis <= -3.9692 and variance <= 2.8297 | 1 | 0.047288 |
| variance < 0.311555 and skewness < 7.76395 and variance < -0.458565 and curtosis < 6.21865 and skewness < 7.293150000000001 | 1 | 0.292355 |
| variance <= 0.518 and skewness <= 5.2808 and variance <= -1.7479 | 1 | 0.263445 |
| variance > -0.403365 and variance <= 0.75422 and skewness > -2.3021 and skewness <= 5.21045 and curtosis > -4.38605 and curtosis <= 8.83885 | 1 | 0.060074 |
| variance >= 0.311555 and curtosis >= -4.38605 and variance >= 1.5922 and variance < 2.03655 and curtosis < -2.6483499999999998 | 1 | 0.003275 |
| variance <= 0.518 and skewness > 5.2808 and variance <= -3.3553 | 1 | 0.048649 |
| variance < 0.311555 and skewness < 7.76395 and variance < -0.458565 and curtosis >= 6.21865 and skewness < -4.6745 | 1 | 0.144819 |
| variance <= 0.518 and skewness <= 5.2808 and variance > -1.7479 and curtosis <= 6.2109 and variance <= 0.30081 | 1 | 0.206283 |
| variance > 0.518 and curtosis > -3.9692 and variance <= 2.031 and curtosis <= -1.7542 and skewness <= 4.5503 | 1 | 0.029745 |
| variance <= 0.518 and skewness <= 5.2808 and variance > -1.7479 and curtosis <= 6.2109 and variance > 0.30081 and variance > 0.33111 | 1 | 0.012472 |
| variance >= 0.311555 and curtosis >= -4.38605 and variance < 1.5922 and curtosis >= -2.2721999999999998 and entropy >= 0.081882 and curtosis < 1.85305 and skewness < 3.5591749999999998 | 1 | 0.022825 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| variance > 0.75108 and variance > 2.2279 | 0 | 0.405844 |
| skewness > 5.1401 and variance > -3.3793 | 0 | 0.252051 |
| variance <= 0.30081 and curtosis <= 3.0312 | 1 | 0.714286 |
| variance <= -0.49948 and skewness <= -0.38696 | 1 | 0.575363 |
| curtosis > 0.20278 | 0 | 0.631955 |
|  | 1 | 0.985915 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| variance <= 0.2952 and skewness <= 5.8333 and curtosis <= 6.2169 | 1 | 0.321122 |
| variance <= -1.4454 and skewness <= -4.7428 | 1 | 0.141604 |
| variance <= 1.7875 and curtosis <= 0.68604 and skewness <= 5.2022 | 1 | 0.081950 |
| variance <= -4.1479 | 1 | 0.047327 |
|  | 0 | 0.984195 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

variance|skewness|curtosis|class
---|---|---|---
(0.75422-2.22845]|(9.61695-inf)|(-4.38605-8.83885]|0
(2.22845-inf)|(9.61695-inf)|(-4.38605-8.83885]|0
(-0.403365-0.75422]|(9.61695-inf)|(-4.38605-8.83885]|0
(-2.7952--0.403365]|(9.61695-inf)|(-4.38605-8.83885]|0
(-inf--2.7952]|(5.21045-9.61695]|(-4.38605-8.83885]|1
(-2.7952--0.403365]|(5.21045-9.61695]|(-4.38605-8.83885]|0
(-0.403365-0.75422]|(5.21045-9.61695]|(-4.38605-8.83885]|0
(2.22845-inf)|(5.21045-9.61695]|(-4.38605-8.83885]|0
(0.75422-2.22845]|(5.21045-9.61695]|(-4.38605-8.83885]|0
(-2.7952--0.403365]|(-6.8814--4.9818]|(8.83885-inf)|1
(-inf--2.7952]|(-2.3021-5.21045]|(-4.38605-8.83885]|1
(-inf--2.7952]|(-6.8814--4.9818]|(8.83885-inf)|1
(-0.403365-0.75422]|(-2.3021-5.21045]|(-4.38605-8.83885]|1
(2.22845-inf)|(9.61695-inf)|(-inf--4.38605]|0
(-2.7952--0.403365]|(-2.3021-5.21045]|(-4.38605-8.83885]|1
(0.75422-2.22845]|(-2.3021-5.21045]|(-4.38605-8.83885]|0
(2.22845-inf)|(-2.3021-5.21045]|(-4.38605-8.83885]|0
(-2.7952--0.403365]|(-4.9818--2.3021]|(-4.38605-8.83885]|1
(-2.7952--0.403365]|(-inf--6.8814]|(8.83885-inf)|1
(-inf--2.7952]|(-inf--6.8814]|(8.83885-inf)|1
(0.75422-2.22845]|(-4.9818--2.3021]|(-4.38605-8.83885]|0
(2.22845-inf)|(5.21045-9.61695]|(-inf--4.38605]|0
(-0.403365-0.75422]|(-4.9818--2.3021]|(-4.38605-8.83885]|0
(2.22845-inf)|(-4.9818--2.3021]|(-4.38605-8.83885]|0
(-inf--2.7952]|(-6.8814--4.9818]|(-4.38605-8.83885]|0
(-0.403365-0.75422]|(-6.8814--4.9818]|(-4.38605-8.83885]|0
(0.75422-2.22845]|(-2.3021-5.21045]|(-inf--4.38605]|1
(-2.7952--0.403365]|(-6.8814--4.9818]|(-4.38605-8.83885]|1
(-0.403365-0.75422]|(-2.3021-5.21045]|(-inf--4.38605]|1
(0.75422-2.22845]|(-6.8814--4.9818]|(-4.38605-8.83885]|0
(2.22845-inf)|(-6.8814--4.9818]|(-4.38605-8.83885]|0
(-inf--2.7952]|(-inf--6.8814]|(-4.38605-8.83885]|0
(-2.7952--0.403365]|(-inf--6.8814]|(-4.38605-8.83885]|1

## JRip

Decision list:

rules | predicted class
---|---
(variance <= 0.2952) and (skewness <= 5.8333) and (curtosis <= 6.2169)|1 (328.0/2.0)
(variance <= -1.4454) and (skewness <= -4.7428)|1 (113.0/0.0)
(variance <= 1.7875) and (curtosis <= 0.68604) and (skewness <= 5.2022)|1 (67.0/3.0)
(variance <= -4.1479)|1 (36.0/1.0)
|0 (690.0/11.0)


## PART

Decision list:

rules | predicted class
---|---
variance > 0.75108 AND variance > 2.2279|0 (375.0)
skewness > 5.1401 AND variance > -3.3793|0 (187.0/1.0)
variance <= 0.30081 AND curtosis <= 3.0312|1 (310.0)
variance <= -0.49948 AND skewness <= -0.38696|1 (170.0/1.0)
curtosis > 0.20278|0 (125.0/3.0)
|1 (67.0/1.0)


## J48 Decision Tree

* variance <= 0.518
	* skewness <= 5.2808
		* variance <= -1.7479: 1 (159.0)
		* variance > -1.7479
			* curtosis <= 6.2109
				* variance <= 0.30081: 1 (128.0)
				* variance > 0.30081
					* variance <= 0.33111: 0 (3.0)
					* variance > 0.33111: 1 (11.0/1.0)
			* curtosis > 6.2109
				* skewness <= -4.8835: 1 (13.0)
				* skewness > -4.8835: 0 (14.0)
	* skewness > 5.2808
		* variance <= -3.3553: 1 (25.0/1.0)
		* variance > -3.3553: 0 (65.0)
* variance > 0.518
	* curtosis <= -3.9692
		* variance <= 2.8297: 1 (21.0)
		* variance > 2.8297: 0 (25.0)
	* curtosis > -3.9692
		* variance <= 2.031
			* curtosis <= -1.7542
				* skewness <= 4.5503: 1 (10.0)
				* skewness > 4.5503: 0 (12.0)
			* curtosis > -1.7542: 0 (96.0/1.0)
		* variance > 2.031: 0 (241.0)


## SimpleCart Decision Tree

* variance < 0.311555
	* skewness < 7.76395
		* variance < -0.458565
			* curtosis < 6.21865
				* skewness < 7.293150000000001: 1(283.0/0.0)
				* skewness >= 7.293150000000001: 1(4.0/1.0)
			* curtosis >= 6.21865
				* skewness < -4.6745: 1(116.0/0.0)
				* skewness >= -4.6745
					* variance < -2.09525: 0(1.0/1.0)
					* variance >= -2.09525: 0(11.0/0.0)
		* variance >= -0.458565
			* curtosis < 0.297461
				* skewness < 5.63155: 1(49.0/0.0)
				* skewness >= 5.63155: 0(3.0/0.0)
			* curtosis >= 0.297461
				* entropy < 0.91334
					* skewness < -0.672525
						* curtosis < 4.2440999999999995: 1(4.0/0.0)
						* curtosis >= 4.2440999999999995: 0(6.0/0.0)
					* skewness >= -0.672525: 0(13.0/0.0)
				* entropy >= 0.91334: 1(5.0/0.0)
	* skewness >= 7.76395
		* variance < -4.726: 1(17.0/0.0)
		* variance >= -4.726: 0(80.0/0.0)
* variance >= 0.311555
	* curtosis < -4.38605
		* variance < 3.22215: 1(29.0/0.0)
		* variance >= 3.22215: 0(9.0/0.0)
	* curtosis >= -4.38605
		* variance < 1.5922
			* curtosis < -2.2721999999999998
				* skewness < 5.6667: 1(21.0/0.0)
				* skewness >= 5.6667: 0(2.0/0.0)
			* curtosis >= -2.2721999999999998
				* entropy < 0.081882
					* variance < 0.42002: 0(14.0/1.0)
					* variance >= 0.42002: 0(88.0/0.0)
				* entropy >= 0.081882
					* curtosis < 1.85305
						* skewness < 3.5591749999999998: 1(16.0/0.0)
						* skewness >= 3.5591749999999998: 0(2.0/0.0)
					* curtosis >= 1.85305: 0(17.0/0.0)
		* variance >= 1.5922
			* variance < 2.03655
				* curtosis < -2.6483499999999998: 1(3.0/1.0)
				* curtosis >= -2.6483499999999998: 0(50.0/0.0)
			* variance >= 2.03655: 0(387.0/0.0)


