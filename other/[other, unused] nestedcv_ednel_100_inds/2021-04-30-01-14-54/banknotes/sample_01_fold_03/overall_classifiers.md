# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 0 | 0.555105 |
| variance <= 0.75896 and skewness > 5.1401 and variance <= -3.38 and curtosis <= 0.9885 | 1 | 0.048611 |
| variance < 0.320165 and skewness < 5.86535 and curtosis < 6.7456 | 1 | 0.327798 |
| variance < 0.320165 and skewness >= 5.86535 and variance < -3.4448999999999996 | 1 | 0.047327 |
| variance <= 0.75896 and skewness <= 5.1401 and variance <= -0.39416 and curtosis > 6.2169 and skewness <= -4.7076 | 1 | 0.146949 |
| variance > -0.4031 and variance <= 0.760295 and skewness > -2.2845 and skewness <= 5.21045 and curtosis > -4.38605 and curtosis <= 8.7202 and entropy = all | 1 | 0.054779 |
| variance >= 0.320165 and curtosis >= -4.38605 and variance < 1.5922 and curtosis < -2.2721999999999998 | 1 | 0.026138 |
| variance >= 0.320165 and curtosis < -4.38605 and variance < 3.30405 | 1 | 0.039271 |
| variance <= 0.75896 and skewness <= 5.1401 and variance > -0.39416 and curtosis > 0.4247 and entropy > 0.72326 and curtosis <= 6.2332 | 1 | 0.015805 |
| variance >= 0.320165 and curtosis >= -4.38605 and variance < 1.5922 and curtosis >= -2.2721999999999998 and entropy >= 0.081882 and curtosis < 1.85305 | 1 | 0.020347 |
| variance > 0.75896 and curtosis <= -1.8785 and skewness <= 4.9228 and variance <= 3.4776 | 1 | 0.052559 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| variance > 0.75896 and curtosis > -1.8785 | 0 | 0.412206 |
| skewness <= 5.1401 and variance <= -0.46651 and curtosis <= 6.2169 | 1 | 0.469965 |
| skewness > 5.2022 and variance > -3.38 | 0 | 0.460952 |
| curtosis <= 0.7126 and variance <= 1.8994 | 1 | 0.714286 |
| skewness <= -4.7076 and variance <= -1.3931 | 1 | 0.662791 |
| curtosis <= 6.7807 and entropy <= 0.72326 and curtosis > -2.6196 and skewness > -4.5152 and variance > 0.2346 | 0 | 0.555556 |
| curtosis > 6.7807 | 0 | 0.489362 |
| curtosis <= 2.6225 | 1 | 0.782609 |
| skewness <= -2.4087 | 1 | 0.545455 |
|  | 0 | 1.000000 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| variance <= 0.27331 and skewness <= 5.8333 and curtosis <= 6.103 | 1 | 0.319098 |
| variance <= -1.3887 and skewness <= -4.5566 | 1 | 0.145885 |
| variance <= 1.7875 and curtosis <= 0.68604 and skewness <= 5.2022 | 1 | 0.079487 |
| variance <= -4.1479 | 1 | 0.047327 |
|  | 0 | 0.982783 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

variance|skewness|curtosis|entropy|class
---|---|---|---|---
(-0.4031-0.760295]|(9.61695-inf)|(-4.38605-8.7202]|all|0
(-2.7952--0.4031]|(9.61695-inf)|(-4.38605-8.7202]|all|0
(0.760295-2.3921]|(9.61695-inf)|(-4.38605-8.7202]|all|0
(2.3921-inf)|(9.61695-inf)|(-4.38605-8.7202]|all|0
(-inf--2.7952]|(5.21045-9.61695]|(-4.38605-8.7202]|all|1
(-2.7952--0.4031]|(5.21045-9.61695]|(-4.38605-8.7202]|all|0
(-0.4031-0.760295]|(5.21045-9.61695]|(-4.38605-8.7202]|all|0
(0.760295-2.3921]|(5.21045-9.61695]|(-4.38605-8.7202]|all|0
(2.3921-inf)|(5.21045-9.61695]|(-4.38605-8.7202]|all|0
(2.3921-inf)|(9.61695-inf)|(-inf--4.38605]|all|0
(-2.7952--0.4031]|(-6.94555--4.9818]|(8.7202-inf)|all|1
(-inf--2.7952]|(-2.2845-5.21045]|(-4.38605-8.7202]|all|1
(-inf--2.7952]|(-6.94555--4.9818]|(8.7202-inf)|all|1
(-2.7952--0.4031]|(-2.2845-5.21045]|(-4.38605-8.7202]|all|1
(2.3921-inf)|(-2.2845-5.21045]|(-4.38605-8.7202]|all|0
(0.760295-2.3921]|(-2.2845-5.21045]|(-4.38605-8.7202]|all|0
(-0.4031-0.760295]|(-2.2845-5.21045]|(-4.38605-8.7202]|all|1
(2.3921-inf)|(5.21045-9.61695]|(-inf--4.38605]|all|0
(-2.7952--0.4031]|(-inf--6.94555]|(8.7202-inf)|all|1
(-inf--2.7952]|(-inf--6.94555]|(8.7202-inf)|all|1
(-0.4031-0.760295]|(-4.9818--2.2845]|(-4.38605-8.7202]|all|0
(-2.7952--0.4031]|(-4.9818--2.2845]|(-4.38605-8.7202]|all|1
(0.760295-2.3921]|(-4.9818--2.2845]|(-4.38605-8.7202]|all|0
(2.3921-inf)|(-4.9818--2.2845]|(-4.38605-8.7202]|all|0
(-inf--2.7952]|(-6.94555--4.9818]|(-4.38605-8.7202]|all|0
(-0.4031-0.760295]|(-2.2845-5.21045]|(-inf--4.38605]|all|1
(0.760295-2.3921]|(-2.2845-5.21045]|(-inf--4.38605]|all|1
(-2.7952--0.4031]|(-6.94555--4.9818]|(-4.38605-8.7202]|all|1
(2.3921-inf)|(-6.94555--4.9818]|(-4.38605-8.7202]|all|0
(0.760295-2.3921]|(-6.94555--4.9818]|(-4.38605-8.7202]|all|0
(-0.4031-0.760295]|(-6.94555--4.9818]|(-4.38605-8.7202]|all|0
(-inf--2.7952]|(-inf--6.94555]|(-4.38605-8.7202]|all|0
(-2.7952--0.4031]|(-inf--6.94555]|(-4.38605-8.7202]|all|1

## JRip

Decision list:

rules | predicted class
---|---
(variance <= 0.27331) and (skewness <= 5.8333) and (curtosis <= 6.103)|1 (325.0/2.0)
(variance <= -1.3887) and (skewness <= -4.5566)|1 (117.0/0.0)
(variance <= 1.7875) and (curtosis <= 0.68604) and (skewness <= 5.2022)|1 (65.0/3.0)
(variance <= -4.1479)|1 (36.0/1.0)
|0 (691.0/12.0)


## PART

Decision list:

rules | predicted class
---|---
variance > 0.75896 AND curtosis > -1.8785|0 (385.0)
skewness <= 5.1401 AND variance <= -0.46651 AND curtosis <= 6.2169|1 (266.0)
skewness > 5.2022 AND variance > -3.38|0 (242.0)
curtosis <= 0.7126 AND variance <= 1.8994|1 (145.0)
skewness <= -4.7076 AND variance <= -1.3931|1 (114.0)
curtosis <= 6.7807 AND entropy <= 0.72326 AND curtosis > -2.6196 AND skewness > -4.5152 AND variance > 0.2346|0 (30.0)
curtosis > 6.7807|0 (23.0)
curtosis <= 2.6225|1 (18.0)
skewness <= -2.4087|1 (6.0)
|0 (5.0)


## J48 Decision Tree

* variance <= 0.75896
	* skewness <= 5.1401
		* variance <= -0.39416
			* curtosis <= 6.2169: 1 (273.0)
			* curtosis > 6.2169
				* skewness <= -4.7076: 1 (118.0)
				* skewness > -4.7076
					* variance <= -2.121: 0 (2.0/1.0)
					* variance > -2.121: 0 (12.0)
		* variance > -0.39416
			* curtosis <= 0.4247: 1 (70.0)
			* curtosis > 0.4247
				* entropy <= 0.72326
					* curtosis <= 1.1033
						* skewness <= 0.70975: 0 (2.0/1.0)
						* skewness > 0.70975: 0 (4.0)
					* curtosis > 1.1033: 0 (33.0)
				* entropy > 0.72326
					* curtosis <= 6.2332: 1 (11.0)
					* curtosis > 6.2332: 0 (2.0)
	* skewness > 5.1401
		* variance <= -3.38
			* curtosis <= 0.9885: 1 (35.0)
			* curtosis > 0.9885: 0 (2.0/1.0)
		* variance > -3.38
			* variance <= 0.58836: 0 (99.0)
			* variance > 0.58836
				* variance <= 0.63655: 0 (2.0/1.0)
				* variance > 0.63655: 0 (4.0)
* variance > 0.75896
	* curtosis <= -1.8785
		* skewness <= 4.9228
			* variance <= 3.4776: 1 (38.0)
			* variance > 3.4776: 0 (2.0)
		* skewness > 4.9228: 0 (140.0)
	* curtosis > -1.8785: 0 (385.0)


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
		* variance >= 1.5922: 0(435.0/3.0)


