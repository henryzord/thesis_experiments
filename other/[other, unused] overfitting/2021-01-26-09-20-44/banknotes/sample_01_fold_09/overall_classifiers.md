# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 0 | 0.554745 |
| variance > 0.75422 and variance <= 2.22845 and curtosis > -2.2859 and curtosis <= -1.8378 and skewness <= 3.898495 | 1 | 0.004367 |
| variance > -0.403365 and variance <= 0.75422 and skewness > -2.3021 and skewness <= 5.21045 and curtosis > -4.38605 and curtosis <= 8.83885 | 1 | 0.060157 |
| variance <= 0.75422 and skewness <= 5.1608 and variance > -0.458565 and curtosis <= 2.1670999999999996 and curtosis <= 0.47013499999999997 | 1 | 0.098814 |
| variance <= 0.75422 and skewness <= 5.1608 and variance <= -0.458565 and curtosis > 6.21865 and skewness <= -4.6745 | 1 | 0.145000 |
| variance <= 0.75422 and skewness <= 5.1608 and variance <= -0.458565 and curtosis <= 6.21865 | 1 | 0.281513 |
| variance <= 0.75422 and skewness <= 5.1608 and variance > -0.458565 and curtosis <= 2.1670999999999996 and curtosis > 0.47013499999999997 and skewness <= -0.360045 | 1 | 0.017241 |
| variance > 0.75422 and variance <= 2.22845 and curtosis <= -2.2859 and skewness <= 6.2554 | 1 | 0.051318 |
| variance <= 0.75422 and skewness > 5.1608 and variance <= -3.36765 | 1 | 0.048716 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| variance > 0.75422 and variance > 2.22845 | 0 | 0.404555 |
| skewness > 5.1608 and variance > -3.36765 and skewness > 5.8478 | 0 | 0.243802 |
| variance <= 0.311555 and curtosis <= 3.0642 | 1 | 0.698198 |
| variance <= -0.49481 and skewness <= -0.351787 and variance <= -0.74678 | 1 | 0.544218 |
| curtosis <= 0.031412 and skewness <= 4.3579 | 1 | 0.302083 |
| entropy > -2.4151 and skewness > -0.28143 | 0 | 0.800000 |
| curtosis > 4.5671 and variance > -0.077244 | 0 | 0.618182 |
| curtosis > 1.165415 and entropy > 0.012055 | 1 | 0.360119 |
| curtosis > 1.165415 | 0 | 0.615385 |
|  | 1 | 1.000000 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| variance <= 0.27331 and skewness <= 5.8333 and curtosis <= 6.2169 | 1 | 0.320767 |
| variance <= -1.4454 and skewness <= -4.5566 | 1 | 0.142857 |
| variance <= 1.7425 and curtosis <= 0.68604 and skewness <= 5.2022 | 1 | 0.082060 |
| variance <= -4.1479 | 1 | 0.047392 |
|  | 0 | 0.984173 |


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
(-2.7952--0.403365]|(-6.8814--4.9725]|(8.83885-inf)|1
(2.22845-inf)|(9.61695-inf)|(-inf--4.38605]|0
(-inf--2.7952]|(-2.3021-5.21045]|(-4.38605-8.83885]|1
(-inf--2.7952]|(-6.8814--4.9725]|(8.83885-inf)|1
(-2.7952--0.403365]|(-2.3021-5.21045]|(-4.38605-8.83885]|1
(2.22845-inf)|(-2.3021-5.21045]|(-4.38605-8.83885]|0
(-0.403365-0.75422]|(-2.3021-5.21045]|(-4.38605-8.83885]|1
(0.75422-2.22845]|(-2.3021-5.21045]|(-4.38605-8.83885]|0
(2.22845-inf)|(5.21045-9.61695]|(-inf--4.38605]|0
(-2.7952--0.403365]|(-inf--6.8814]|(8.83885-inf)|1
(-2.7952--0.403365]|(-4.9725--2.3021]|(-4.38605-8.83885]|1
(-inf--2.7952]|(-inf--6.8814]|(8.83885-inf)|1
(-0.403365-0.75422]|(-4.9725--2.3021]|(-4.38605-8.83885]|0
(0.75422-2.22845]|(-4.9725--2.3021]|(-4.38605-8.83885]|0
(2.22845-inf)|(-4.9725--2.3021]|(-4.38605-8.83885]|0
(-inf--2.7952]|(-6.8814--4.9725]|(-4.38605-8.83885]|0
(-0.403365-0.75422]|(-6.8814--4.9725]|(-4.38605-8.83885]|0
(0.75422-2.22845]|(-2.3021-5.21045]|(-inf--4.38605]|1
(-0.403365-0.75422]|(-2.3021-5.21045]|(-inf--4.38605]|1
(-2.7952--0.403365]|(-6.8814--4.9725]|(-4.38605-8.83885]|1
(0.75422-2.22845]|(-6.8814--4.9725]|(-4.38605-8.83885]|0
(2.22845-inf)|(-6.8814--4.9725]|(-4.38605-8.83885]|0
(-inf--2.7952]|(-inf--6.8814]|(-4.38605-8.83885]|0
(-2.7952--0.403365]|(-inf--6.8814]|(-4.38605-8.83885]|1

## JRip

Decision list:

rules | predicted class
---|---
(variance <= 0.27331) and (skewness <= 5.8333) and (curtosis <= 6.2169)|1 (327.0/2.0)
(variance <= -1.4454) and (skewness <= -4.5566)|1 (114.0/0.0)
(variance <= 1.7425) and (curtosis <= 0.68604) and (skewness <= 5.2022)|1 (67.0/3.0)
(variance <= -4.1479)|1 (36.0/1.0)
|0 (689.0/11.0)


## PART

Decision list:

rules | predicted class
---|---
variance > 0.75422 AND variance > 2.22845|0 (373.0)
skewness > 5.1608 AND variance > -3.36765 AND skewness > 5.8478|0 (177.0)
variance <= 0.311555 AND curtosis <= 3.0642|1 (310.0)
variance <= -0.49481 AND skewness <= -0.351787 AND variance <= -0.74678|1 (160.0)
curtosis <= 0.031412 AND skewness <= 4.3579|1 (58.0)
entropy > -2.4151 AND skewness > -0.28143|0 (84.0)
curtosis > 4.5671 AND variance > -0.077244|0 (34.0)
curtosis > 1.165415 AND entropy > 0.012055|1 (14.0/3.0)
curtosis > 1.165415|0 (13.0)
|1 (10.0)


## J48 Decision Tree

* variance <= 0.75422
	* skewness <= 5.1608
		* variance <= -0.458565
			* curtosis <= 6.21865: 1 (268.0)
			* curtosis > 6.21865
				* skewness <= -4.6745: 1 (116.0)
				* skewness > -4.6745: 0 (14.0/1.0)
		* variance > -0.458565
			* curtosis <= 2.1670999999999996
				* curtosis <= 0.47013499999999997: 1 (75.0)
				* curtosis > 0.47013499999999997
					* skewness <= -0.360045: 1 (12.0)
					* skewness > -0.360045: 0 (7.0)
			* curtosis > 2.1670999999999996: 0 (28.0)
	* skewness > 5.1608
		* variance <= -3.36765: 1 (37.0/1.0)
		* variance > -3.36765: 0 (113.0/1.0)
* variance > 0.75422
	* variance <= 2.22845
		* curtosis <= -2.2859
			* skewness <= 6.2554: 1 (37.0)
			* skewness > 6.2554: 0 (4.0)
		* curtosis > -2.2859
			* curtosis <= -1.8378
				* skewness <= 3.898495: 1 (3.0)
				* skewness > 3.898495: 0 (11.0)
			* curtosis > -1.8378: 0 (135.0)
	* variance > 2.22845: 0 (373.0)


