# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 0 | 0.555105 |
| variance < 0.311555 and skewness < 7.76395 and variance < -0.458565 and curtosis >= 6.21865 and skewness < -4.6745 | 1 | 0.144819 |
| variance <= 0.75108 and skewness > 5.1401 and variance <= -3.3793 | 1 | 0.048649 |
| variance > -0.403365 and variance <= 0.75422 and skewness > -2.3021 and skewness <= 5.21045 and curtosis > -4.38605 and curtosis <= 8.83885 | 1 | 0.060074 |
| variance >= 0.311555 and curtosis >= -4.38605 and variance < 1.5922 and curtosis >= -2.2721999999999998 and entropy >= 0.081882 and curtosis < 1.85305 | 1 | 0.020347 |
| variance <= 0.75108 and skewness <= 5.1401 and variance <= -0.46651 and curtosis <= 6.2169 | 1 | 0.281217 |
| variance <= 0.75108 and skewness <= 5.1401 and variance > -0.46651 and curtosis <= 2.1624 and curtosis <= 0.46583 | 1 | 0.098684 |
| variance >= 0.311555 and curtosis >= -4.38605 and variance < 1.5922 and curtosis < -2.2721999999999998 | 1 | 0.027236 |
| variance >= 0.311555 and curtosis < -4.38605 and variance < 3.22215 | 1 | 0.040616 |
| variance > 0.75108 and variance <= 2.2279 and curtosis <= -2.3 | 1 | 0.046505 |
| variance <= 0.75108 and skewness <= 5.1401 and variance > -0.46651 and curtosis <= 2.1624 and curtosis > 0.46583 and skewness <= -0.94981 | 1 | 0.014388 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| variance > 0.75422 and variance > 2.22845 | 0 | 0.405200 |
| skewness > 5.1608 and variance > -3.36765 | 0 | 0.252051 |
| variance <= 0.311555 and curtosis <= 3.0642 | 1 | 0.712644 |
| variance <= -0.49481 and skewness <= -0.351787 | 1 | 0.573399 |
| curtosis > 0.20578 and curtosis > 1.82135 | 0 | 0.613260 |
| curtosis <= 0.20578 | 1 | 0.825184 |
| skewness > -0.42419 | 0 | 0.812500 |
|  | 1 | 0.750000 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| skewness <= 5.8333 and curtosis <= 6.2169 and variance <= -0.36506 | 1 | 0.287201 |
| skewness <= -4.7428 and variance <= -0.55355 | 1 | 0.144819 |
| curtosis <= 0.27818 and skewness <= 5.2022 and variance <= 1.2572 | 1 | 0.114987 |
| variance <= -4.1479 and curtosis <= 1.0836 | 1 | 0.048611 |
| variance <= 2.2279 and curtosis <= -2.9581 and skewness <= 4.78 | 1 | 0.022825 |
| skewness <= 1.0595 and variance <= 1.5631 and curtosis <= 2.135 and entropy >= 0.29653 | 1 | 0.022825 |
|  | 0 | 0.998542 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

variance|skewness|curtosis|class
---|---|---|---
(0.75422-2.22845]|(9.61695-inf)|(-4.38605-8.83885]|0
(2.22845-inf)|(9.61695-inf)|(-4.38605-8.83885]|0
(-2.7952--0.403365]|(9.61695-inf)|(-4.38605-8.83885]|0
(-0.403365-0.75422]|(9.61695-inf)|(-4.38605-8.83885]|0
(-2.7952--0.403365]|(5.21045-9.61695]|(-4.38605-8.83885]|0
(-inf--2.7952]|(5.21045-9.61695]|(-4.38605-8.83885]|1
(2.22845-inf)|(5.21045-9.61695]|(-4.38605-8.83885]|0
(0.75422-2.22845]|(5.21045-9.61695]|(-4.38605-8.83885]|0
(-0.403365-0.75422]|(5.21045-9.61695]|(-4.38605-8.83885]|0
(-2.7952--0.403365]|(-6.8814--4.9818]|(8.83885-inf)|1
(2.22845-inf)|(9.61695-inf)|(-inf--4.38605]|0
(-inf--2.7952]|(-6.8814--4.9818]|(8.83885-inf)|1
(-2.7952--0.403365]|(-2.3021-5.21045]|(-4.38605-8.83885]|1
(-inf--2.7952]|(-2.3021-5.21045]|(-4.38605-8.83885]|1
(0.75422-2.22845]|(-2.3021-5.21045]|(-4.38605-8.83885]|0
(-0.403365-0.75422]|(-2.3021-5.21045]|(-4.38605-8.83885]|1
(2.22845-inf)|(-2.3021-5.21045]|(-4.38605-8.83885]|0
(0.75422-2.22845]|(-4.9818--2.3021]|(-4.38605-8.83885]|0
(2.22845-inf)|(5.21045-9.61695]|(-inf--4.38605]|0
(-2.7952--0.403365]|(-4.9818--2.3021]|(-4.38605-8.83885]|1
(-2.7952--0.403365]|(-inf--6.8814]|(8.83885-inf)|1
(-inf--2.7952]|(-inf--6.8814]|(8.83885-inf)|1
(-0.403365-0.75422]|(-4.9818--2.3021]|(-4.38605-8.83885]|0
(2.22845-inf)|(-4.9818--2.3021]|(-4.38605-8.83885]|0
(-inf--2.7952]|(-6.8814--4.9818]|(-4.38605-8.83885]|0
(2.22845-inf)|(-6.8814--4.9818]|(-4.38605-8.83885]|0
(-2.7952--0.403365]|(-6.8814--4.9818]|(-4.38605-8.83885]|1
(-0.403365-0.75422]|(-2.3021-5.21045]|(-inf--4.38605]|1
(0.75422-2.22845]|(-2.3021-5.21045]|(-inf--4.38605]|1
(0.75422-2.22845]|(-6.8814--4.9818]|(-4.38605-8.83885]|0
(-0.403365-0.75422]|(-6.8814--4.9818]|(-4.38605-8.83885]|0
(-inf--2.7952]|(-inf--6.8814]|(-4.38605-8.83885]|0
(-2.7952--0.403365]|(-inf--6.8814]|(-4.38605-8.83885]|1

## JRip

Decision list:

rules | predicted class
---|---
(skewness <= 5.8333) and (curtosis <= 6.2169) and (variance <= -0.36506)|1 (276.0/0.0)
(skewness <= -4.7428) and (variance <= -0.55355)|1 (116.0/0.0)
(curtosis <= 0.27818) and (skewness <= 5.2022) and (variance <= 1.2572)|1 (89.0/0.0)
(variance <= -4.1479) and (curtosis <= 1.0836)|1 (35.0/0.0)
(variance <= 2.2279) and (curtosis <= -2.9581) and (skewness <= 4.78)|1 (16.0/0.0)
(skewness <= 1.0595) and (variance <= 1.5631) and (curtosis <= 2.135) and (entropy >= 0.29653)|1 (16.0/0.0)
|0 (686.0/1.0)


## PART

Decision list:

rules | predicted class
---|---
variance > 0.75422 AND variance > 2.22845|0 (374.0)
skewness > 5.1608 AND variance > -3.36765|0 (187.0/1.0)
variance <= 0.311555 AND curtosis <= 3.0642|1 (310.0)
variance <= -0.49481 AND skewness <= -0.351787|1 (170.0/1.0)
curtosis > 0.20578 AND curtosis > 1.82135|0 (110.0)
curtosis <= 0.20578|1 (67.0/1.0)
skewness > -0.42419|0 (12.0)
|1 (4.0/1.0)


## J48 Decision Tree

* variance <= 0.75108
	* skewness <= 5.1401
		* variance <= -0.46651
			* curtosis <= 6.2169: 1 (268.0)
			* curtosis > 6.2169
				* skewness <= -4.7428: 1 (116.0)
				* skewness > -4.7428: 0 (14.0/1.0)
		* variance > -0.46651
			* curtosis <= 2.1624
				* curtosis <= 0.46583: 1 (75.0)
				* curtosis > 0.46583
					* skewness <= -0.94981: 1 (10.0)
					* skewness > -0.94981: 0 (9.0/2.0)
			* curtosis > 2.1624: 0 (28.0)
	* skewness > 5.1401
		* variance <= -3.3793: 1 (37.0/1.0)
		* variance > -3.3793: 0 (113.0/1.0)
* variance > 0.75108
	* variance <= 2.2279
		* curtosis <= -2.3: 1 (41.0/4.0)
		* curtosis > -2.3: 0 (149.0/3.0)
	* variance > 2.2279: 0 (374.0)


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
				* entropy < 0.081882
					* variance < 0.42002: 0(14.0/1.0)
					* variance >= 0.42002: 0(88.0/0.0)
				* entropy >= 0.081882
					* curtosis < 1.85305: 1(16.0/2.0)
					* curtosis >= 1.85305: 0(17.0/0.0)
		* variance >= 1.5922
			* variance < 2.03655: 0(51.0/3.0)
			* variance >= 2.03655: 0(386.0/0.0)


