# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| variance >= 0.320165 and curtosis >= -4.38605 and variance >= 1.5922 | 0 | 0.440958 |
| variance < 0.320165 and skewness < 5.86535 and curtosis < 6.7456 | 1 | 0.327477 |
| variance > 0.26877 and variance <= 1.7875 and curtosis > -2.2726 and entropy <= 0.087054 | 0 | 0.179384 |
| variance < 0.320165 and skewness < 5.86535 and curtosis >= 6.7456 and skewness < -4.7997 | 1 | 0.134942 |
| variance < 0.320165 and skewness >= 5.86535 and variance >= -3.4448999999999996 | 0 | 0.136792 |
| variance > 0.26877 and variance <= 1.7875 and curtosis <= -2.2726 and skewness <= 5.0097 | 1 | 0.065395 |
| variance < 0.320165 and skewness >= 5.86535 and variance < -3.4448999999999996 | 1 | 0.047261 |
| variance <= 0.26877 and skewness <= 5.8561 and curtosis > 4.8486 and skewness > -3.1039 | 0 | 0.036842 |
| variance >= 0.320165 and curtosis >= -4.38605 and variance < 1.5922 and curtosis >= -2.2721999999999998 and entropy >= 0.081882 and curtosis >= 1.85305 | 0 | 0.024867 |
| variance >= 0.320165 and curtosis >= -4.38605 and variance < 1.5922 and curtosis >= -2.2721999999999998 and entropy >= 0.081882 and curtosis < 1.85305 | 1 | 0.020317 |
| variance >= 0.320165 and curtosis < -4.38605 and variance >= 3.30405 | 0 | 0.016129 |
| variance > 0.760295 and variance <= 2.3921 and skewness > 5.21045 and skewness <= 9.61695 and curtosis > -4.38605 and curtosis <= 8.7202 | 0 | 0.118780 |
| variance >= 0.320165 and curtosis < -4.38605 and variance < 3.30405 | 1 | 0.039216 |
| variance < 0.320165 and skewness < 5.86535 and curtosis >= 6.7456 and skewness >= -4.7997 | 0 | 0.035149 |
| variance > -0.4031 and variance <= 0.760295 and skewness > -2.2845 and skewness <= 5.21045 and curtosis > -4.38605 and curtosis <= 8.7202 | 1 | 0.054703 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| variance > 0.85574 and curtosis > -1.8785 | 0 | 0.409042 |
| skewness <= 5.1401 and variance <= -1.5222 | 1 | 0.475183 |
| skewness > 5.2022 and variance > -3.38 | 0 | 0.477670 |
| curtosis <= 0.7126 | 1 | 0.774596 |
| skewness <= -0.24832 and entropy > -0.75216 and curtosis <= 6.9255 | 1 | 0.469027 |
|  | 0 | 0.895522 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| skewness <= 5.8333 and curtosis <= 6.2169 and variance <= -0.36372 | 1 | 0.287643 |
| skewness <= -4.5152 and variance <= -0.77288 | 1 | 0.146766 |
| curtosis <= 0.27818 and skewness <= 5.2022 and variance <= 1.2572 | 1 | 0.112549 |
| variance <= -4.1479 and curtosis <= 1.0836 | 1 | 0.048544 |
| variance <= 2.3917 and curtosis <= -1.8785 and skewness <= 4.78 | 1 | 0.028329 |
| skewness <= -0.82358 and curtosis <= 2.135 and variance <= 0.74428 | 1 | 0.015782 |
|  | 0 | 0.998544 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

variance|skewness|curtosis|class
---|---|---|---
(0.760295-2.3921]|(9.61695-inf)|(-4.38605-8.7202]|0
(-0.4031-0.760295]|(9.61695-inf)|(-4.38605-8.7202]|0
(2.3921-inf)|(9.61695-inf)|(-4.38605-8.7202]|0
(-2.7952--0.4031]|(9.61695-inf)|(-4.38605-8.7202]|0
(-2.7952--0.4031]|(5.21045-9.61695]|(-4.38605-8.7202]|0
(-inf--2.7952]|(5.21045-9.61695]|(-4.38605-8.7202]|1
(0.760295-2.3921]|(5.21045-9.61695]|(-4.38605-8.7202]|0
(2.3921-inf)|(5.21045-9.61695]|(-4.38605-8.7202]|0
(-0.4031-0.760295]|(5.21045-9.61695]|(-4.38605-8.7202]|0
(-2.7952--0.4031]|(-6.94555--4.9818]|(8.7202-inf)|1
(-inf--2.7952]|(-6.94555--4.9818]|(8.7202-inf)|1
(-inf--2.7952]|(-2.2845-5.21045]|(-4.38605-8.7202]|1
(2.3921-inf)|(9.61695-inf)|(-inf--4.38605]|0
(-0.4031-0.760295]|(-2.2845-5.21045]|(-4.38605-8.7202]|1
(-2.7952--0.4031]|(-2.2845-5.21045]|(-4.38605-8.7202]|1
(2.3921-inf)|(-2.2845-5.21045]|(-4.38605-8.7202]|0
(0.760295-2.3921]|(-2.2845-5.21045]|(-4.38605-8.7202]|0
(2.3921-inf)|(5.21045-9.61695]|(-inf--4.38605]|0
(-2.7952--0.4031]|(-4.9818--2.2845]|(-4.38605-8.7202]|1
(-2.7952--0.4031]|(-inf--6.94555]|(8.7202-inf)|1
(-inf--2.7952]|(-inf--6.94555]|(8.7202-inf)|1
(-0.4031-0.760295]|(-4.9818--2.2845]|(-4.38605-8.7202]|0
(0.760295-2.3921]|(-4.9818--2.2845]|(-4.38605-8.7202]|0
(2.3921-inf)|(-4.9818--2.2845]|(-4.38605-8.7202]|0
(-inf--2.7952]|(-6.94555--4.9818]|(-4.38605-8.7202]|0
(-0.4031-0.760295]|(-6.94555--4.9818]|(-4.38605-8.7202]|0
(-2.7952--0.4031]|(-6.94555--4.9818]|(-4.38605-8.7202]|1
(-0.4031-0.760295]|(-2.2845-5.21045]|(-inf--4.38605]|1
(0.760295-2.3921]|(-2.2845-5.21045]|(-inf--4.38605]|1
(2.3921-inf)|(-6.94555--4.9818]|(-4.38605-8.7202]|0
(0.760295-2.3921]|(-6.94555--4.9818]|(-4.38605-8.7202]|0
(-inf--2.7952]|(-inf--6.94555]|(-4.38605-8.7202]|0
(-2.7952--0.4031]|(-inf--6.94555]|(-4.38605-8.7202]|1

## JRip

Decision list:

rules | predicted class
---|---
(skewness <= 5.8333) and (curtosis <= 6.2169) and (variance <= -0.36372)|1 (277.0/0.0)
(skewness <= -4.5152) and (variance <= -0.77288)|1 (118.0/0.0)
(curtosis <= 0.27818) and (skewness <= 5.2022) and (variance <= 1.2572)|1 (87.0/0.0)
(variance <= -4.1479) and (curtosis <= 1.0836)|1 (35.0/0.0)
(variance <= 2.3917) and (curtosis <= -1.8785) and (skewness <= 4.78)|1 (20.0/0.0)
(skewness <= -0.82358) and (curtosis <= 2.135) and (variance <= 0.74428)|1 (11.0/0.0)
|0 (687.0/1.0)


## PART

Decision list:

rules | predicted class
---|---
variance > 0.85574 AND curtosis > -1.8785|0 (284.0)
skewness <= 5.1401 AND variance <= -1.5222|1 (215.0/1.0)
skewness > 5.2022 AND variance > -3.38|0 (191.0)
curtosis <= 0.7126|1 (155.0/1.0)
skewness <= -0.24832 AND entropy > -0.75216 AND curtosis <= 6.9255|1 (40.0)
|0 (42.0/4.0)


## J48 Decision Tree

* variance <= 0.26877
	* skewness <= 5.8561
		* curtosis <= 4.8486: 1 (216.0)
		* curtosis > 4.8486
			* skewness <= -3.1039: 1 (119.0/2.0)
			* skewness > -3.1039: 0 (16.0)
	* skewness > 5.8561
		* variance <= -3.4917: 1 (25.0/1.0)
		* variance > -3.4917: 0 (68.0)
* variance > 0.26877
	* variance <= 1.7875
		* curtosis <= -2.2726
			* skewness <= 5.0097: 1 (37.0)
			* skewness > 5.0097: 0 (4.0/1.0)
		* curtosis > -2.2726
			* entropy <= 0.087054: 0 (96.0)
			* entropy > 0.087054
				* curtosis <= 1.8513
					* skewness <= 0.74493: 1 (13.0)
					* skewness > 0.74493: 0 (4.0/2.0)
				* curtosis > 1.8513: 0 (16.0)
	* variance > 1.7875: 0 (313.0/2.0)


## SimpleCart Decision Tree

* variance < 0.320165
	* skewness < 5.86535
		* curtosis < 6.7456: 1(337.0/3.0)
		* curtosis >= 6.7456
			* skewness < -4.7997: 1(108.0/1.0)
			* skewness >= -4.7997: 0(20.0/0.0)
	* skewness >= 5.86535
		* variance < -3.4448999999999996: 1(35.0/1.0)
		* variance >= -3.4448999999999996: 0(87.0/0.0)
* variance >= 0.320165
	* curtosis < -4.38605
		* variance < 3.30405: 1(28.0/0.0)
		* variance >= 3.30405: 0(9.0/0.0)
	* curtosis >= -4.38605
		* variance < 1.5922
			* curtosis < -2.2721999999999998: 1(21.0/3.0)
			* curtosis >= -2.2721999999999998
				* entropy < 0.081882: 0(110.0/1.0)
				* entropy >= 0.081882
					* curtosis < 1.85305: 1(16.0/2.0)
					* curtosis >= 1.85305: 0(14.0/0.0)
		* variance >= 1.5922: 0(436.0/3.0)


