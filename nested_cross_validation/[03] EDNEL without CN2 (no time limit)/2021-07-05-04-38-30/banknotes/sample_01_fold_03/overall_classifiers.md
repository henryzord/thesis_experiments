# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| variance >= 0.320165 and curtosis >= -4.38605 and variance >= 1.5922 | 0 | 0.440388 |
| variance < 0.320165 and skewness < 5.86535 and curtosis < 6.7456 and curtosis < 3.0642 | 1 | 0.287201 |
| variance <= 0.75896 and skewness <= 5.0097 and variance <= -1.6244 | 1 | 0.278203 |
| variance >= 0.320165 and curtosis >= -4.38605 and variance < 1.5922 and curtosis >= -2.2721999999999998 and entropy < 0.081882 | 0 | 0.165667 |
| variance < 0.320165 and skewness >= 5.86535 and variance >= -3.4448999999999996 | 0 | 0.136792 |
| variance > 0.75896 and curtosis <= -1.8785 and skewness <= 4.9228 | 1 | 0.050069 |
| variance < 0.320165 and skewness >= 5.86535 and variance < -3.4448999999999996 | 1 | 0.047327 |
| variance <= 0.75896 and skewness <= 5.0097 and variance > -1.6244 and curtosis > 0.4247 and skewness <= -0.8091 and entropy > -0.026738 | 1 | 0.075911 |
| variance < 0.320165 and skewness < 5.86535 and curtosis >= 6.7456 and skewness >= -4.7997 | 0 | 0.035149 |
| variance <= 0.75896 and skewness <= 5.0097 and variance > -1.6244 and curtosis <= 0.4247 | 1 | 0.167679 |
| variance >= 0.320165 and curtosis >= -4.38605 and variance < 1.5922 and curtosis >= -2.2721999999999998 and entropy >= 0.081882 and curtosis >= 1.85305 | 0 | 0.024867 |
| variance > 0.75896 and curtosis <= -1.8785 and skewness > 4.9228 | 0 | 0.202035 |
| variance <= 0.75896 and skewness <= 5.0097 and variance > -1.6244 and curtosis > 0.4247 and skewness <= -0.8091 and entropy <= -0.026738 and variance <= -0.16108 | 1 | 0.005814 |
| variance < 0.320165 and skewness < 5.86535 and curtosis < 6.7456 and curtosis >= 3.0642 and skewness >= -0.475945 | 0 | 0.005435 |
| variance > 0.760295 and variance <= 2.3921 and skewness > 5.21045 and skewness <= 9.61695 and curtosis > -4.38605 and curtosis <= 8.7202 | 0 | 0.118780 |
| variance >= 0.320165 and curtosis < -4.38605 and variance < 3.30405 | 1 | 0.039271 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| variance > 0.75896 and curtosis > -1.8785 | 0 | 0.412834 |
| skewness <= 5.1401 and variance <= -0.46651 and curtosis <= 6.2169 | 1 | 0.470796 |
| skewness > 5.2022 and variance > -3.38 | 0 | 0.459924 |
| curtosis <= 0.7126 | 1 | 0.717360 |
| skewness <= -4.7076 | 1 | 0.668760 |
| curtosis > 2.1624 | 0 | 0.750406 |
| skewness > -0.43663 | 0 | 0.490196 |
|  | 1 | 1.000000 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| variance <= 0.2952 and skewness <= 5.8333 and curtosis <= 6.2169 | 1 | 0.320449 |
| variance <= -1.5078 and skewness <= 7.6584 | 1 | 0.156487 |
| variance <= 1.7875 and curtosis <= -2.2726 and skewness <= 5.2022 | 1 | 0.064208 |
| variance <= -5.3857 | 1 | 0.024217 |
| skewness <= 1.852 and curtosis <= -0.031994 and variance <= 2.031 | 1 | 0.022825 |
| skewness <= -7.4473 | 1 | 0.008683 |
|  | 0 | 0.988456 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

variance|skewness|curtosis|class
---|---|---|---
(-0.4031-0.760295]|(9.61695-inf)|(-4.38605-8.7202]|0
(0.760295-2.3921]|(9.61695-inf)|(-4.38605-8.7202]|0
(-2.7952--0.4031]|(9.61695-inf)|(-4.38605-8.7202]|0
(2.3921-inf)|(9.61695-inf)|(-4.38605-8.7202]|0
(-inf--2.7952]|(5.21045-9.61695]|(-4.38605-8.7202]|1
(-0.4031-0.760295]|(5.21045-9.61695]|(-4.38605-8.7202]|0
(-2.7952--0.4031]|(5.21045-9.61695]|(-4.38605-8.7202]|0
(2.3921-inf)|(5.21045-9.61695]|(-4.38605-8.7202]|0
(0.760295-2.3921]|(5.21045-9.61695]|(-4.38605-8.7202]|0
(-2.7952--0.4031]|(-6.94555--4.9818]|(8.7202-inf)|1
(-inf--2.7952]|(-6.94555--4.9818]|(8.7202-inf)|1
(-inf--2.7952]|(-2.2845-5.21045]|(-4.38605-8.7202]|1
(-0.4031-0.760295]|(-2.2845-5.21045]|(-4.38605-8.7202]|1
(2.3921-inf)|(9.61695-inf)|(-inf--4.38605]|0
(2.3921-inf)|(-2.2845-5.21045]|(-4.38605-8.7202]|0
(0.760295-2.3921]|(-2.2845-5.21045]|(-4.38605-8.7202]|0
(-2.7952--0.4031]|(-2.2845-5.21045]|(-4.38605-8.7202]|1
(-2.7952--0.4031]|(-inf--6.94555]|(8.7202-inf)|1
(-inf--2.7952]|(-inf--6.94555]|(8.7202-inf)|1
(2.3921-inf)|(5.21045-9.61695]|(-inf--4.38605]|0
(0.760295-2.3921]|(-4.9818--2.2845]|(-4.38605-8.7202]|0
(-0.4031-0.760295]|(-4.9818--2.2845]|(-4.38605-8.7202]|0
(-2.7952--0.4031]|(-4.9818--2.2845]|(-4.38605-8.7202]|1
(2.3921-inf)|(-4.9818--2.2845]|(-4.38605-8.7202]|0
(-inf--2.7952]|(-6.94555--4.9818]|(-4.38605-8.7202]|0
(-0.4031-0.760295]|(-6.94555--4.9818]|(-4.38605-8.7202]|0
(-0.4031-0.760295]|(-2.2845-5.21045]|(-inf--4.38605]|1
(-2.7952--0.4031]|(-6.94555--4.9818]|(-4.38605-8.7202]|1
(0.760295-2.3921]|(-2.2845-5.21045]|(-inf--4.38605]|1
(0.760295-2.3921]|(-6.94555--4.9818]|(-4.38605-8.7202]|0
(2.3921-inf)|(-6.94555--4.9818]|(-4.38605-8.7202]|0
(-inf--2.7952]|(-inf--6.94555]|(-4.38605-8.7202]|0
(-2.7952--0.4031]|(-inf--6.94555]|(-4.38605-8.7202]|1

## JRip

Decision list:

rules | predicted class
---|---
(variance <= 0.2952) and (skewness <= 5.8333) and (curtosis <= 6.2169)|1 (327.0/2.0)
(variance <= -1.5078) and (skewness <= 7.6584)|1 (133.0/3.0)
(variance <= 1.7875) and (curtosis <= -2.2726) and (skewness <= 5.2022)|1 (47.0/0.0)
(variance <= -5.3857)|1 (17.0/0.0)
(skewness <= 1.852) and (curtosis <= -0.031994) and (variance <= 2.031)|1 (16.0/0.0)
(skewness <= -7.4473)|1 (6.0/0.0)
|0 (688.0/8.0)


## PART

Decision list:

rules | predicted class
---|---
variance > 0.75896 AND curtosis > -1.8785|0 (386.0)
skewness <= 5.1401 AND variance <= -0.46651 AND curtosis <= 6.2169|1 (266.0)
skewness > 5.2022 AND variance > -3.38|0 (241.0)
curtosis <= 0.7126|1 (153.0/3.0)
skewness <= -4.7076|1 (121.0/2.0)
curtosis > 2.1624|0 (42.0/1.0)
skewness > -0.43663|0 (14.0/2.0)
|1 (11.0)


## J48 Decision Tree

* variance <= 0.75896
	* skewness <= 5.0097
		* variance <= -1.6244: 1 (240.0/1.0)
		* variance > -1.6244
			* curtosis <= 0.4247: 1 (126.0)
			* curtosis > 0.4247
				* skewness <= -0.8091
					* entropy <= -0.026738
						* variance <= -0.16108: 1 (7.0/3.0)
						* variance > -0.16108: 0 (8.0)
					* entropy > -0.026738: 1 (55.0/3.0)
				* skewness > -0.8091: 0 (34.0/2.0)
	* skewness > 5.0097
		* variance <= -3.38: 1 (31.0/1.0)
		* variance > -3.38: 0 (94.0/1.0)
* variance > 0.75896
	* curtosis <= -1.8785
		* skewness <= 4.9228: 1 (36.0/2.0)
		* skewness > 4.9228: 0 (122.0)
	* curtosis > -1.8785: 0 (344.0)


## SimpleCart Decision Tree

* variance < 0.320165
	* skewness < 5.86535
		* curtosis < 6.7456
			* curtosis < 3.0642: 1(276.0/0.0)
			* curtosis >= 3.0642
				* skewness < -0.475945: 1(61.0/0.0)
				* skewness >= -0.475945: 0(3.0/0.0)
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
			* curtosis < -2.2721999999999998
				* skewness < 5.6667: 1(21.0/0.0)
				* skewness >= 5.6667: 0(3.0/0.0)
			* curtosis >= -2.2721999999999998
				* entropy < 0.081882: 0(110.0/1.0)
				* entropy >= 0.081882
					* curtosis < 1.85305
						* skewness < 3.5591749999999998: 1(16.0/0.0)
						* skewness >= 3.5591749999999998: 0(2.0/0.0)
					* curtosis >= 1.85305: 0(14.0/0.0)
		* variance >= 1.5922: 0(435.0/3.0)


