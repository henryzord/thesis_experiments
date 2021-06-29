# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 0 | 0.554745 |
| variance <= 1.7452 and skewness <= 5.1401 and variance <= 0.30081 and curtosis <= 4.8486 | 1 | 0.299184 |
| variance <= 1.7452 and skewness > 5.1401 and variance <= -3.3793 | 1 | 0.048716 |
| variance >= 0.311555 and curtosis >= -4.38605 and variance < 1.5922 and curtosis < -2.2721999999999998 | 1 | 0.027274 |
| variance <= 1.7452 and skewness <= 5.1401 and variance <= 0.30081 and curtosis > 4.8486 and skewness <= -3.0336 | 1 | 0.177916 |
| variance > -0.403365 and variance <= 0.75422 and skewness > -2.3021 and skewness <= 5.21045 and curtosis > -4.38605 and curtosis <= 8.83885 | 1 | 0.060157 |
| variance >= 0.311555 and curtosis < -4.38605 and variance < 3.22215 | 1 | 0.040673 |
| variance >= 0.311555 and curtosis >= -4.38605 and variance < 1.5922 and curtosis >= -2.2721999999999998 and entropy >= 0.081882 and curtosis < 1.85305 | 1 | 0.020376 |
| variance <= 1.7452 and skewness <= 5.1401 and variance > 0.30081 and curtosis <= 0.20278 | 1 | 0.080667 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| variance > 0.27451 and curtosis > -4.4044 and variance > 1.7425 | 0 | 0.434030 |
| skewness <= 5.2684 and variance <= 0.30081 and curtosis <= 6.2109 | 1 | 0.553103 |
| skewness <= -4.9518 and variance <= -1.1188 | 1 | 0.300268 |
| variance > -3.3924 and curtosis > -3.8869 and entropy <= -0.32544 | 0 | 0.632853 |
| curtosis <= 0.80685 and variance <= 2.9742 | 1 | 0.594048 |
| skewness > -4.2006 and curtosis > 1.8076 | 0 | 0.813559 |
| variance > 0.80355 | 0 | 0.620690 |
|  | 1 | 1.000000 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| variance <= 0.27331 and curtosis <= 3.0141 and skewness <= 5.1401 | 1 | 0.284519 |
| variance <= -0.539 and skewness <= -4.8359 | 1 | 0.187648 |
| variance <= 1.7875 and curtosis <= -3.9692 | 1 | 0.050000 |
| variance <= -3.9934 | 1 | 0.048716 |
| variance <= 0.83625 and entropy >= -0.32415 and curtosis <= 6.7156 and skewness <= -0.3104 | 1 | 0.022857 |
| skewness <= 2.2638 and curtosis <= -0.031994 and variance <= 2.031 | 1 | 0.039326 |
|  | 0 | 0.995633 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

variance|skewness|curtosis|class
---|---|---|---
(0.75422-2.22845]|(9.61695-inf)|(-4.38605-8.83885]|0
(-0.403365-0.75422]|(9.61695-inf)|(-4.38605-8.83885]|0
(2.22845-inf)|(9.61695-inf)|(-4.38605-8.83885]|0
(-2.7952--0.403365]|(9.61695-inf)|(-4.38605-8.83885]|0
(-inf--2.7952]|(5.21045-9.61695]|(-4.38605-8.83885]|1
(-2.7952--0.403365]|(5.21045-9.61695]|(-4.38605-8.83885]|0
(-0.403365-0.75422]|(5.21045-9.61695]|(-4.38605-8.83885]|0
(0.75422-2.22845]|(5.21045-9.61695]|(-4.38605-8.83885]|0
(2.22845-inf)|(5.21045-9.61695]|(-4.38605-8.83885]|0
(-2.7952--0.403365]|(-6.8814--4.9725]|(8.83885-inf)|1
(-inf--2.7952]|(-6.8814--4.9725]|(8.83885-inf)|1
(-inf--2.7952]|(-2.3021-5.21045]|(-4.38605-8.83885]|1
(2.22845-inf)|(9.61695-inf)|(-inf--4.38605]|0
(-2.7952--0.403365]|(-2.3021-5.21045]|(-4.38605-8.83885]|1
(-0.403365-0.75422]|(-2.3021-5.21045]|(-4.38605-8.83885]|1
(0.75422-2.22845]|(-2.3021-5.21045]|(-4.38605-8.83885]|0
(2.22845-inf)|(-2.3021-5.21045]|(-4.38605-8.83885]|0
(-2.7952--0.403365]|(-inf--6.8814]|(8.83885-inf)|1
(-inf--2.7952]|(-inf--6.8814]|(8.83885-inf)|1
(-2.7952--0.403365]|(-4.9725--2.3021]|(-4.38605-8.83885]|1
(-0.403365-0.75422]|(-4.9725--2.3021]|(-4.38605-8.83885]|0
(0.75422-2.22845]|(-4.9725--2.3021]|(-4.38605-8.83885]|0
(2.22845-inf)|(5.21045-9.61695]|(-inf--4.38605]|0
(2.22845-inf)|(-4.9725--2.3021]|(-4.38605-8.83885]|0
(-inf--2.7952]|(-6.8814--4.9725]|(-4.38605-8.83885]|0
(0.75422-2.22845]|(-2.3021-5.21045]|(-inf--4.38605]|1
(-0.403365-0.75422]|(-2.3021-5.21045]|(-inf--4.38605]|1
(-2.7952--0.403365]|(-6.8814--4.9725]|(-4.38605-8.83885]|1
(2.22845-inf)|(-6.8814--4.9725]|(-4.38605-8.83885]|0
(-0.403365-0.75422]|(-6.8814--4.9725]|(-4.38605-8.83885]|0
(0.75422-2.22845]|(-6.8814--4.9725]|(-4.38605-8.83885]|0
(-inf--2.7952]|(-inf--6.8814]|(-4.38605-8.83885]|0
(-2.7952--0.403365]|(-inf--6.8814]|(-4.38605-8.83885]|1

## JRip

Decision list:

rules | predicted class
---|---
(variance <= 0.27331) and (curtosis <= 3.0141) and (skewness <= 5.1401)|1 (272.0/0.0)
(variance <= -0.539) and (skewness <= -4.8359)|1 (158.0/0.0)
(variance <= 1.7875) and (curtosis <= -3.9692)|1 (36.0/0.0)
(variance <= -3.9934)|1 (37.0/1.0)
(variance <= 0.83625) and (entropy >= -0.32415) and (curtosis <= 6.7156) and (skewness <= -0.3104)|1 (16.0/0.0)
(skewness <= 2.2638) and (curtosis <= -0.031994) and (variance <= 2.031)|1 (28.0/0.0)
|0 (686.0/3.0)


## PART

Decision list:

rules | predicted class
---|---
variance > 0.27451 AND curtosis > -4.4044 AND variance > 1.7425|0 (285.0/1.0)
skewness <= 5.2684 AND variance <= 0.30081 AND curtosis <= 6.2109|1 (224.0/1.0)
skewness <= -4.9518 AND variance <= -1.1188|1 (72.0)
variance > -3.3924 AND curtosis > -3.8869 AND entropy <= -0.32544|0 (130.0/2.0)
curtosis <= 0.80685 AND variance <= 2.9742|1 (64.0/2.0)
skewness > -4.2006 AND curtosis > 1.8076|0 (33.0)
variance > 0.80355|0 (8.0)
|1 (6.0)


## J48 Decision Tree

* variance <= 1.7452
	* skewness <= 5.1401
		* variance <= 0.30081
			* curtosis <= 4.8486: 1 (194.0)
			* curtosis > 4.8486
				* skewness <= -3.0336: 1 (106.0/2.0)
				* skewness > -3.0336: 0 (13.0)
		* variance > 0.30081
			* curtosis <= 0.20278: 1 (43.0/1.0)
			* curtosis > 0.20278: 0 (43.0/2.0)
	* skewness > 5.1401
		* variance <= -3.3793: 1 (22.0/1.0)
		* variance > -3.3793: 0 (101.0)
* variance > 1.7452: 0 (300.0/3.0)


## SimpleCart Decision Tree

* variance < 0.311555
	* skewness < 7.76395
		* variance < -0.458565
			* curtosis < 6.21865: 1(287.0/1.0)
			* curtosis >= 6.21865
				* skewness < -4.6745: 1(116.0/0.0)
				* skewness >= -4.6745: 0(13.0/1.0)
		* variance >= -0.458565
			* curtosis < 0.297461: 1(49.0/3.0)
			* curtosis >= 0.297461: 0(19.0/9.0)
	* skewness >= 7.76395
		* variance < -4.726: 1(17.0/0.0)
		* variance >= -4.726: 0(80.0/0.0)
* variance >= 0.311555
	* curtosis < -4.38605
		* variance < 3.22215: 1(29.0/0.0)
		* variance >= 3.22215: 0(9.0/0.0)
	* curtosis >= -4.38605
		* variance < 1.5922
			* curtosis < -2.2721999999999998: 1(21.0/2.0)
			* curtosis >= -2.2721999999999998
				* entropy < 0.081882: 0(102.0/1.0)
				* entropy >= 0.081882
					* curtosis < 1.85305: 1(16.0/2.0)
					* curtosis >= 1.85305: 0(17.0/0.0)
		* variance >= 1.5922: 0(436.0/3.0)


