# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| variance > 0.75896 and curtosis > -1.8785 | 0 | 0.403909 |
| variance <= 0.75896 and skewness <= 5.1401 and variance <= -0.39416 and curtosis <= 6.2169 | 1 | 0.286458 |
| variance > 0.75896 and curtosis <= -1.8785 and skewness > 4.9228 | 0 | 0.216833 |
| variance <= 0.75896 and skewness <= 5.1401 and variance <= -0.39416 and curtosis > 6.2169 and skewness <= -3.0087 | 1 | 0.145885 |
| variance <= 0.75896 and skewness > 5.1401 and variance > -3.4605 | 0 | 0.159279 |
| variance <= 0.75896 and skewness <= 5.1401 and variance > -0.39416 and curtosis <= 0.46583 | 1 | 0.091512 |
| variance > 0.75896 and curtosis <= -1.8785 and skewness <= 4.9228 | 1 | 0.051382 |
| variance <= 0.75896 and skewness > 5.1401 and variance <= -3.4605 | 1 | 0.048649 |
| variance <= 0.75896 and skewness <= 5.1401 and variance > -0.39416 and curtosis > 0.46583 and entropy <= 0.90946 and curtosis > 1.7151 | 0 | 0.048527 |
| variance <= 0.75896 and skewness <= 5.1401 and variance <= -0.39416 and curtosis > 6.2169 and skewness > -3.0087 | 0 | 0.026596 |
| variance <= 0.75896 and skewness <= 5.1401 and variance > -0.39416 and curtosis > 0.46583 and entropy <= 0.90946 and curtosis <= 1.7151 and variance > 0.3434 | 0 | 0.017889 |
| variance <= 0.75896 and skewness <= 5.1401 and variance > -0.39416 and curtosis > 0.46583 and entropy > 0.90946 | 1 | 0.011544 |
| variance <= 0.75896 and skewness <= 5.1401 and variance > -0.39416 and curtosis > 0.46583 and entropy <= 0.90946 and curtosis <= 1.7151 and variance <= 0.3434 | 1 | 0.005806 |
| variance > 2.3921 and skewness > -2.3021 and skewness <= 5.21045 and curtosis > -4.42285 and curtosis <= 8.83885 and entropy = all | 0 | 0.174436 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| variance > 0.75896 and curtosis > -1.8785 | 0 | 0.403909 |
| skewness <= 5.1401 and variance <= -1.786 | 1 | 0.435025 |
| skewness > 5.2022 and variance > -3.4605 | 0 | 0.453737 |
| curtosis <= 0.7126 | 1 | 0.790758 |
| skewness <= -0.94981 and variance <= -0.46651 | 1 | 0.536000 |
| entropy <= 1.0426 and curtosis > 2.1401 | 0 | 0.704918 |
| variance <= 0.32444 | 1 | 0.516129 |
|  | 0 | 0.882353 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| variance <= 0.27331 and skewness <= 5.1401 and curtosis <= 6.2169 | 1 | 0.320449 |
| variance <= -1.3887 and skewness <= -4.5566 | 1 | 0.143750 |
| variance <= 1.7875 and skewness <= 5.2022 and curtosis <= 0.18307 | 1 | 0.085447 |
| variance <= -4.1479 | 1 | 0.048649 |
| skewness <= -7.4473 | 1 | 0.002911 |
| curtosis <= -4.976 | 1 | 0.002911 |
| skewness <= 1.852 and curtosis <= -2.9581 | 1 | 0.002911 |
| entropy >= 0.88619 and variance <= 0.74428 and variance >= 0.31803 | 1 | 0.004360 |
|  | 0 | 1.000000 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

variance|skewness|curtosis|entropy|class
---|---|---|---|---
(-0.4031-0.760295]|(9.53215-inf)|(-4.42285-8.83885]|all|0
(0.760295-2.3921]|(9.53215-inf)|(-4.42285-8.83885]|all|0
(2.3921-inf)|(9.53215-inf)|(-4.42285-8.83885]|all|0
(-2.7952--0.4031]|(9.53215-inf)|(-4.42285-8.83885]|all|0
(-inf--2.7952]|(-5.436--2.3021]|(8.83885-inf)|all|1
(-2.7952--0.4031]|(5.21045-9.53215]|(-4.42285-8.83885]|all|0
(0.760295-2.3921]|(5.21045-9.53215]|(-4.42285-8.83885]|all|0
(2.3921-inf)|(5.21045-9.53215]|(-4.42285-8.83885]|all|0
(-0.4031-0.760295]|(5.21045-9.53215]|(-4.42285-8.83885]|all|0
(-inf--2.7952]|(5.21045-9.53215]|(-4.42285-8.83885]|all|1
(-2.7952--0.4031]|(-6.94555--5.436]|(8.83885-inf)|all|1
(2.3921-inf)|(9.53215-inf)|(-inf--4.42285]|all|0
(0.760295-2.3921]|(-2.3021-5.21045]|(-4.42285-8.83885]|all|0
(2.3921-inf)|(-2.3021-5.21045]|(-4.42285-8.83885]|all|0
(-inf--2.7952]|(-6.94555--5.436]|(8.83885-inf)|all|1
(-inf--2.7952]|(-2.3021-5.21045]|(-4.42285-8.83885]|all|1
(-0.4031-0.760295]|(-2.3021-5.21045]|(-4.42285-8.83885]|all|1
(-2.7952--0.4031]|(-2.3021-5.21045]|(-4.42285-8.83885]|all|1
(0.760295-2.3921]|(-5.436--2.3021]|(-4.42285-8.83885]|all|0
(2.3921-inf)|(5.21045-9.53215]|(-inf--4.42285]|all|0
(-0.4031-0.760295]|(-5.436--2.3021]|(-4.42285-8.83885]|all|0
(2.3921-inf)|(-5.436--2.3021]|(-4.42285-8.83885]|all|0
(-2.7952--0.4031]|(-inf--6.94555]|(8.83885-inf)|all|1
(-inf--2.7952]|(-inf--6.94555]|(8.83885-inf)|all|1
(-2.7952--0.4031]|(-5.436--2.3021]|(-4.42285-8.83885]|all|1
(-inf--2.7952]|(-6.94555--5.436]|(-4.42285-8.83885]|all|0
(2.3921-inf)|(-6.94555--5.436]|(-4.42285-8.83885]|all|0
(-0.4031-0.760295]|(-6.94555--5.436]|(-4.42285-8.83885]|all|1
(0.760295-2.3921]|(-6.94555--5.436]|(-4.42285-8.83885]|all|0
(0.760295-2.3921]|(-2.3021-5.21045]|(-inf--4.42285]|all|1
(-0.4031-0.760295]|(-2.3021-5.21045]|(-inf--4.42285]|all|1
(-2.7952--0.4031]|(-6.94555--5.436]|(-4.42285-8.83885]|all|1
(-inf--2.7952]|(-inf--6.94555]|(-4.42285-8.83885]|all|1
(-2.7952--0.4031]|(-inf--6.94555]|(-4.42285-8.83885]|all|1

## JRip

Decision list:

rules | predicted class
---|---
(variance <= 0.27331) and (skewness <= 5.1401) and (curtosis <= 6.2169)|1 (327.0/2.0)
(variance <= -1.3887) and (skewness <= -4.5566)|1 (115.0/0.0)
(variance <= 1.7875) and (skewness <= 5.2022) and (curtosis <= 0.18307)|1 (64.0/0.0)
(variance <= -4.1479)|1 (37.0/1.0)
(skewness <= -7.4473)|1 (2.0/0.0)
(curtosis <= -4.976)|1 (2.0/0.0)
(skewness <= 1.852) and (curtosis <= -2.9581)|1 (2.0/0.0)
(entropy >= 0.88619) and (variance <= 0.74428) and (variance >= 0.31803)|1 (3.0/0.0)
|0 (682.0/0.0)


## PART

Decision list:

rules | predicted class
---|---
variance > 0.75896 AND curtosis > -1.8785|0 (372.0)
skewness <= 5.1401 AND variance <= -1.786|1 (243.0/1.0)
skewness > 5.2022 AND variance > -3.4605|0 (255.0)
curtosis <= 0.7126|1 (225.0/3.0)
skewness <= -0.94981 AND variance <= -0.46651|1 (67.0)
entropy <= 1.0426 AND curtosis > 2.1401|0 (42.0)
variance <= 0.32444|1 (16.0)
|0 (14.0/2.0)


## J48 Decision Tree

* variance <= 0.75896
	* skewness <= 5.1401
		* variance <= -0.39416
			* curtosis <= 6.2169: 1 (275.0)
			* curtosis > 6.2169
				* skewness <= -3.0087: 1 (117.0)
				* skewness > -3.0087: 0 (15.0)
		* variance > -0.39416
			* curtosis <= 0.46583: 1 (69.0)
			* curtosis > 0.46583
				* entropy <= 0.90946
					* curtosis <= 1.7151
						* variance <= 0.3434: 1 (4.0)
						* variance > 0.3434: 0 (10.0)
					* curtosis > 1.7151: 0 (28.0)
				* entropy > 0.90946: 1 (8.0)
	* skewness > 5.1401
		* variance <= -3.4605: 1 (37.0/1.0)
		* variance > -3.4605: 0 (106.0/1.0)
* variance > 0.75896
	* curtosis <= -1.8785
		* skewness <= 4.9228: 1 (41.0/2.0)
		* skewness > 4.9228: 0 (152.0)
	* curtosis > -1.8785: 0 (372.0)


