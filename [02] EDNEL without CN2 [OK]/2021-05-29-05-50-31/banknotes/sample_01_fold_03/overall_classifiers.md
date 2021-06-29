# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| variance >= 0.320165 and curtosis >= -4.38605 and variance >= 1.5922 | 0 | 0.440388 |
| variance < 0.320165 and skewness < 5.86535 and curtosis < 6.7456 and curtosis < 3.0642 | 1 | 0.287201 |
| variance <= 0.75896 and skewness <= 5.1401 and variance <= -0.39416 and curtosis > 6.2169 and skewness <= -4.7076 | 1 | 0.146949 |
| variance >= 0.320165 and curtosis >= -4.38605 and variance < 1.5922 and curtosis >= -2.2721999999999998 and entropy < 0.081882 | 0 | 0.165667 |
| variance < 0.320165 and skewness >= 5.86535 and variance >= -3.4448999999999996 | 0 | 0.136792 |
| variance < 0.320165 and skewness < 5.86535 and curtosis < 6.7456 and curtosis >= 3.0642 and skewness < -0.475945 | 1 | 0.081769 |
| variance < 0.320165 and skewness >= 5.86535 and variance < -3.4448999999999996 | 1 | 0.047327 |
| variance > 0.75896 and curtosis <= -1.8785 and skewness <= 4.9228 and curtosis <= -2.3086 | 1 | 0.047288 |
| variance < 0.320165 and skewness < 5.86535 and curtosis >= 6.7456 and skewness >= -4.7997 | 0 | 0.035149 |
| variance <= 0.75896 and skewness <= 5.1401 and variance > -0.39416 and curtosis <= 0.4247 | 1 | 0.092715 |
| variance >= 0.320165 and curtosis >= -4.38605 and variance < 1.5922 and curtosis >= -2.2721999999999998 and entropy >= 0.081882 and curtosis >= 1.85305 | 0 | 0.024867 |
| variance > 0.75896 and curtosis <= -1.8785 and skewness > 4.9228 | 0 | 0.203193 |
| variance >= 0.320165 and curtosis >= -4.38605 and variance < 1.5922 and curtosis >= -2.2721999999999998 and entropy >= 0.081882 and curtosis < 1.85305 | 1 | 0.020347 |
| variance <= 0.75896 and skewness <= 5.1401 and variance > -0.39416 and curtosis > 0.4247 and entropy <= 0.72326 | 0 | 0.063184 |
| variance > 0.760295 and variance <= 2.3921 and skewness > 5.21045 and skewness <= 9.61695 and curtosis > -4.38605 and curtosis <= 8.7202 and entropy = all | 0 | 0.118780 |
| variance <= 0.75896 and skewness <= 5.1401 and variance <= -0.39416 and curtosis > 6.2169 and skewness > -4.7076 | 0 | 0.021518 |
| variance >= 0.320165 and curtosis >= -4.38605 and variance < 1.5922 and curtosis < -2.2721999999999998 and skewness < 5.6667 | 1 | 0.029745 |
| variance >= 0.320165 and curtosis < -4.38605 and variance < 3.30405 | 1 | 0.039271 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| variance > 0.31803 and curtosis > -4.383 and variance > 2.031 | 0 | 0.414088 |
| skewness > 5.2684 and variance > -3.3458 | 0 | 0.247945 |
| variance <= -0.46651 and curtosis <= 6.2169 | 1 | 0.721830 |
| skewness > -6.959 and curtosis <= 0.4247 | 1 | 0.491813 |
| skewness <= -4.8152 and variance <= -1.4217 | 1 | 0.491228 |
| skewness > -0.94981 | 0 | 0.804253 |
| entropy <= -0.37846 | 0 | 0.604167 |
|  | 1 | 0.703704 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| variance <= -0.21888 and skewness <= 7.259 | 1 | 0.371659 |
| variance <= 1.7875 and skewness <= 5.2022 and curtosis <= 0.096532 | 1 | 0.117282 |
| variance <= -4.4779 | 1 | 0.029745 |
| skewness <= -0.82358 and curtosis <= 2.1195 and variance <= 0.74428 | 1 | 0.012968 |
|  | 0 | 0.992754 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

variance|skewness|curtosis|entropy|class
---|---|---|---|---
(0.760295-2.3921]|(9.61695-inf)|(-4.38605-8.7202]|all|0
(2.3921-inf)|(9.61695-inf)|(-4.38605-8.7202]|all|0
(-2.7952--0.4031]|(9.61695-inf)|(-4.38605-8.7202]|all|0
(-0.4031-0.760295]|(9.61695-inf)|(-4.38605-8.7202]|all|0
(-2.7952--0.4031]|(5.21045-9.61695]|(-4.38605-8.7202]|all|0
(-0.4031-0.760295]|(5.21045-9.61695]|(-4.38605-8.7202]|all|0
(2.3921-inf)|(5.21045-9.61695]|(-4.38605-8.7202]|all|0
(0.760295-2.3921]|(5.21045-9.61695]|(-4.38605-8.7202]|all|0
(-inf--2.7952]|(5.21045-9.61695]|(-4.38605-8.7202]|all|1
(-2.7952--0.4031]|(-6.94555--4.9818]|(8.7202-inf)|all|1
(2.3921-inf)|(9.61695-inf)|(-inf--4.38605]|all|0
(2.3921-inf)|(-2.2845-5.21045]|(-4.38605-8.7202]|all|0
(-inf--2.7952]|(-6.94555--4.9818]|(8.7202-inf)|all|1
(0.760295-2.3921]|(-2.2845-5.21045]|(-4.38605-8.7202]|all|0
(-inf--2.7952]|(-2.2845-5.21045]|(-4.38605-8.7202]|all|1
(-2.7952--0.4031]|(-2.2845-5.21045]|(-4.38605-8.7202]|all|1
(-0.4031-0.760295]|(-2.2845-5.21045]|(-4.38605-8.7202]|all|1
(2.3921-inf)|(5.21045-9.61695]|(-inf--4.38605]|all|0
(-0.4031-0.760295]|(-4.9818--2.2845]|(-4.38605-8.7202]|all|0
(0.760295-2.3921]|(-4.9818--2.2845]|(-4.38605-8.7202]|all|0
(2.3921-inf)|(-4.9818--2.2845]|(-4.38605-8.7202]|all|0
(-2.7952--0.4031]|(-inf--6.94555]|(8.7202-inf)|all|1
(-2.7952--0.4031]|(-4.9818--2.2845]|(-4.38605-8.7202]|all|1
(-inf--2.7952]|(-inf--6.94555]|(8.7202-inf)|all|1
(-inf--2.7952]|(-6.94555--4.9818]|(-4.38605-8.7202]|all|0
(2.3921-inf)|(-6.94555--4.9818]|(-4.38605-8.7202]|all|0
(-0.4031-0.760295]|(-6.94555--4.9818]|(-4.38605-8.7202]|all|0
(0.760295-2.3921]|(-6.94555--4.9818]|(-4.38605-8.7202]|all|0
(-0.4031-0.760295]|(-2.2845-5.21045]|(-inf--4.38605]|all|1
(-2.7952--0.4031]|(-6.94555--4.9818]|(-4.38605-8.7202]|all|1
(0.760295-2.3921]|(-2.2845-5.21045]|(-inf--4.38605]|all|1
(-inf--2.7952]|(-inf--6.94555]|(-4.38605-8.7202]|all|0
(-2.7952--0.4031]|(-inf--6.94555]|(-4.38605-8.7202]|all|1

## JRip

Decision list:

rules | predicted class
---|---
(variance <= -0.21888) and (skewness <= 7.259)|1 (440.0/18.0)
(variance <= 1.7875) and (skewness <= 5.2022) and (curtosis <= 0.096532)|1 (93.0/1.0)
(variance <= -4.4779)|1 (21.0/0.0)
(skewness <= -0.82358) and (curtosis <= 2.1195) and (variance <= 0.74428)|1 (9.0/0.0)
|0 (671.0/5.0)


## PART

Decision list:

rules | predicted class
---|---
variance > 0.31803 AND curtosis > -4.383 AND variance > 2.031|0 (262.0)
skewness > 5.2684 AND variance > -3.3458|0 (116.0)
variance <= -0.46651 AND curtosis <= 6.2169|1 (207.0)
skewness > -6.959 AND curtosis <= 0.4247|1 (74.0/2.0)
skewness <= -4.8152 AND variance <= -1.4217|1 (78.0)
skewness > -0.94981|0 (52.0)
entropy <= -0.37846|0 (19.0)
|1 (15.0/6.0)


## J48 Decision Tree

* variance <= 0.75896
	* skewness <= 5.1401
		* variance <= -0.39416
			* curtosis <= 6.2169: 1 (273.0)
			* curtosis > 6.2169
				* skewness <= -4.7076: 1 (118.0)
				* skewness > -4.7076: 0 (14.0/1.0)
		* variance > -0.39416
			* curtosis <= 0.4247: 1 (70.0)
			* curtosis > 0.4247
				* entropy <= 0.72326: 0 (39.0/1.0)
				* entropy > 0.72326
					* skewness <= -1.7051: 1 (7.0)
					* skewness > -1.7051: 1 (6.0/2.0)
	* skewness > 5.1401
		* variance <= -3.38: 1 (37.0/1.0)
		* variance > -3.38: 0 (105.0/1.0)
* variance > 0.75896
	* curtosis <= -1.8785
		* skewness <= 4.9228
			* curtosis <= -2.3086: 1 (34.0)
			* curtosis > -2.3086: 1 (6.0/2.0)
		* skewness > 4.9228: 0 (140.0)
	* curtosis > -1.8785: 0 (385.0)


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
					* curtosis < 1.85305: 1(16.0/2.0)
					* curtosis >= 1.85305: 0(14.0/0.0)
		* variance >= 1.5922: 0(435.0/3.0)


