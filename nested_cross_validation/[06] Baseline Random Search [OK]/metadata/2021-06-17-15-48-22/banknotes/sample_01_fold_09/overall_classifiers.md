# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| variance >= 0.311555 and curtosis >= -4.38605 and variance >= 1.5922 and variance >= 2.03655 | 0 | 0.413462 |
| variance < 0.311555 and skewness < 7.76395 and variance < -0.458565 and curtosis < 6.21865 | 1 | 0.294242 |
| variance > 0.75108 and variance <= 2.2279 and curtosis > -2.3 and curtosis > -1.8511 | 0 | 0.197368 |
| variance <= 0.75108 and skewness <= 5.1401 and variance <= -0.46651 and curtosis > 6.2169 and skewness <= -4.7428 | 1 | 0.144638 |
| variance <= 0.75108 and skewness > 5.1401 and variance > -3.3793 and skewness > 5.9947 | 0 | 0.163110 |
| variance <= 0.75108 and skewness <= 5.1401 and variance > -0.46651 and curtosis <= 2.1624 and curtosis <= 0.46583 | 1 | 0.098555 |
| variance > 0.75108 and variance <= 2.2279 and curtosis <= -2.3 and skewness <= 4.8525 | 1 | 0.049861 |
| variance <= 0.75108 and skewness <= 5.1401 and variance > -0.46651 and curtosis > 2.1624 | 0 | 0.048527 |
| variance >= 0.311555 and curtosis >= -4.38605 and variance < 1.5922 and curtosis >= -2.2721999999999998 and entropy < 0.081882 and variance >= 0.42002 | 0 | 0.138148 |
| variance <= 0.75108 and skewness > 5.1401 and variance <= -3.3793 and variance <= -4.4775 | 1 | 0.044568 |
| variance < 0.311555 and skewness < 7.76395 and variance < -0.458565 and curtosis >= 6.21865 and skewness >= -4.6745 | 0 | 0.021518 |
| variance <= 0.75108 and skewness <= 5.1401 and variance > -0.46651 and curtosis <= 2.1624 and curtosis > 0.46583 and skewness <= -0.38696 | 1 | 0.017192 |
| variance > 0.75108 and variance > 2.2279 | 0 | 0.405844 |
| variance >= 0.311555 and curtosis >= -4.38605 and variance < 1.5922 and curtosis >= -2.2721999999999998 and entropy < 0.081882 and variance < 0.42002 | 0 | 0.023250 |
| variance > 0.75422 and variance <= 2.22845 and skewness > 5.21045 and skewness <= 9.61695 and curtosis > -4.38605 and curtosis <= 8.83885 and entropy = all | 0 | 0.111650 |
| variance > 0.75108 and variance <= 2.2279 and curtosis > -2.3 and curtosis <= -1.8511 and curtosis > -2.0439 | 1 | 0.002620 |
| variance < 0.311555 and skewness < 7.76395 and variance >= -0.458565 and curtosis >= 0.297461 | 0 | 0.023064 |
| variance >= 0.311555 and curtosis < -4.38605 | 1 | 0.031348 |
| variance < 0.311555 and skewness >= 7.76395 and variance >= -4.726 | 0 | 0.127186 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| variance > 0.75108 and variance > 2.2279 | 0 | 0.405844 |
| skewness > 5.1401 and variance > -3.3793 and skewness > 5.8395 | 0 | 0.243802 |
| variance <= 0.30081 and curtosis <= 3.0312 | 1 | 0.698198 |
| variance <= -0.49948 and skewness <= -0.38696 and variance <= -0.75793 | 1 | 0.544218 |
| curtosis <= 0.029699 and skewness <= 4.302 | 1 | 0.302083 |
| entropy > -2.4241 and skewness > -0.30005 | 0 | 0.800000 |
| curtosis > 4.5641 and variance > -0.092194 | 0 | 0.618182 |
| curtosis > 1.1582 and entropy > 0.008175 | 1 | 0.360119 |
| curtosis > 1.1582 | 0 | 0.615385 |
|  | 1 | 1.000000 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| skewness <= 5.8333 and curtosis <= 6.2169 and variance <= -0.36506 | 1 | 0.286902 |
| skewness <= -4.7428 and variance <= -0.55355 | 1 | 0.144638 |
| curtosis <= 0.27818 and skewness <= 5.2022 and variance <= 1.2572 | 1 | 0.114839 |
| variance <= -4.1479 and curtosis <= 1.0836 | 1 | 0.048544 |
| variance <= 2.2279 and curtosis <= -2.9581 and skewness <= 4.78 | 1 | 0.022792 |
| skewness <= 1.0595 and variance <= 1.5631 and curtosis <= 2.135 and entropy >= 0.29653 | 1 | 0.022792 |
|  | 0 | 0.998544 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

variance|skewness|curtosis|entropy|class
---|---|---|---|---
(0.75422-2.22845]|(9.61695-inf)|(-4.38605-8.83885]|all|0
(-0.403365-0.75422]|(9.61695-inf)|(-4.38605-8.83885]|all|0
(2.22845-inf)|(9.61695-inf)|(-4.38605-8.83885]|all|0
(-2.7952--0.403365]|(9.61695-inf)|(-4.38605-8.83885]|all|0
(-inf--2.7952]|(5.21045-9.61695]|(-4.38605-8.83885]|all|1
(-2.7952--0.403365]|(5.21045-9.61695]|(-4.38605-8.83885]|all|0
(0.75422-2.22845]|(5.21045-9.61695]|(-4.38605-8.83885]|all|0
(-0.403365-0.75422]|(5.21045-9.61695]|(-4.38605-8.83885]|all|0
(2.22845-inf)|(5.21045-9.61695]|(-4.38605-8.83885]|all|0
(-2.7952--0.403365]|(-6.8814--4.9818]|(8.83885-inf)|all|1
(-inf--2.7952]|(-2.3021-5.21045]|(-4.38605-8.83885]|all|1
(-inf--2.7952]|(-6.8814--4.9818]|(8.83885-inf)|all|1
(2.22845-inf)|(9.61695-inf)|(-inf--4.38605]|all|0
(-2.7952--0.403365]|(-2.3021-5.21045]|(-4.38605-8.83885]|all|1
(-0.403365-0.75422]|(-2.3021-5.21045]|(-4.38605-8.83885]|all|1
(2.22845-inf)|(-2.3021-5.21045]|(-4.38605-8.83885]|all|0
(0.75422-2.22845]|(-2.3021-5.21045]|(-4.38605-8.83885]|all|0
(-2.7952--0.403365]|(-inf--6.8814]|(8.83885-inf)|all|1
(-inf--2.7952]|(-inf--6.8814]|(8.83885-inf)|all|1
(-2.7952--0.403365]|(-4.9818--2.3021]|(-4.38605-8.83885]|all|1
(2.22845-inf)|(5.21045-9.61695]|(-inf--4.38605]|all|0
(-0.403365-0.75422]|(-4.9818--2.3021]|(-4.38605-8.83885]|all|0
(0.75422-2.22845]|(-4.9818--2.3021]|(-4.38605-8.83885]|all|0
(2.22845-inf)|(-4.9818--2.3021]|(-4.38605-8.83885]|all|0
(-inf--2.7952]|(-6.8814--4.9818]|(-4.38605-8.83885]|all|0
(-0.403365-0.75422]|(-2.3021-5.21045]|(-inf--4.38605]|all|1
(0.75422-2.22845]|(-2.3021-5.21045]|(-inf--4.38605]|all|1
(-2.7952--0.403365]|(-6.8814--4.9818]|(-4.38605-8.83885]|all|1
(-0.403365-0.75422]|(-6.8814--4.9818]|(-4.38605-8.83885]|all|0
(2.22845-inf)|(-6.8814--4.9818]|(-4.38605-8.83885]|all|0
(0.75422-2.22845]|(-6.8814--4.9818]|(-4.38605-8.83885]|all|0
(-inf--2.7952]|(-inf--6.8814]|(-4.38605-8.83885]|all|0
(-2.7952--0.403365]|(-inf--6.8814]|(-4.38605-8.83885]|all|1

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
|0 (687.0/1.0)


## PART

Decision list:

rules | predicted class
---|---
variance > 0.75108 AND variance > 2.2279|0 (375.0)
skewness > 5.1401 AND variance > -3.3793 AND skewness > 5.8395|0 (177.0)
variance <= 0.30081 AND curtosis <= 3.0312|1 (310.0)
variance <= -0.49948 AND skewness <= -0.38696 AND variance <= -0.75793|1 (160.0)
curtosis <= 0.029699 AND skewness <= 4.302|1 (58.0)
entropy > -2.4241 AND skewness > -0.30005|0 (84.0)
curtosis > 4.5641 AND variance > -0.092194|0 (34.0)
curtosis > 1.1582 AND entropy > 0.008175|1 (14.0/3.0)
curtosis > 1.1582|0 (13.0)
|1 (10.0)


## J48 Decision Tree

* variance <= 0.75108
	* skewness <= 5.1401
		* variance <= -0.46651
			* curtosis <= 6.2169: 1 (268.0)
			* curtosis > 6.2169
				* skewness <= -4.7428: 1 (116.0)
				* skewness > -4.7428
					* variance <= -1.5681: 0 (5.0/1.0)
					* variance > -1.5681: 0 (9.0)
		* variance > -0.46651
			* curtosis <= 2.1624
				* curtosis <= 0.46583: 1 (75.0)
				* curtosis > 0.46583
					* skewness <= -0.38696: 1 (12.0)
					* skewness > -0.38696: 0 (7.0)
			* curtosis > 2.1624: 0 (28.0)
	* skewness > 5.1401
		* variance <= -3.3793
			* variance <= -4.4775: 1 (32.0)
			* variance > -4.4775: 1 (5.0/1.0)
		* variance > -3.3793
			* skewness <= 5.9947: 0 (6.0/1.0)
			* skewness > 5.9947: 0 (107.0)
* variance > 0.75108
	* variance <= 2.2279
		* curtosis <= -2.3
			* skewness <= 4.8525: 1 (36.0)
			* skewness > 4.8525: 0 (5.0/1.0)
		* curtosis > -2.3
			* curtosis <= -1.8511
				* curtosis <= -2.0439: 0 (9.0)
				* curtosis > -2.0439: 1 (5.0/2.0)
			* curtosis > -1.8511: 0 (135.0)
	* variance > 2.2279: 0 (375.0)


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
	* curtosis < -4.38605: 1(29.0/9.0)
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
			* variance >= 2.03655: 0(387.0/0.0)


