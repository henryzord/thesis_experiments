# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 0 | 0.555466 |
| variance < 0.320165 and skewness < 5.86535 and curtosis < 6.7456 | 1 | 0.328121 |
| variance <= 0.75896 and skewness > 5.1401 and variance <= -3.3793 | 1 | 0.048581 |
| variance >= 0.320165 and curtosis >= -4.38605 and variance < 1.5856 and curtosis >= -2.2721999999999998 and entropy >= 0.081882 and curtosis < 1.85305 | 1 | 0.020089 |
| variance < 0.320165 and skewness < 5.86535 and curtosis >= 6.7456 and skewness < -4.7997 | 1 | 0.133850 |
| variance >= 0.320165 and curtosis < -4.38605 and variance < 3.30405 | 1 | 0.041899 |
| variance > 0.75896 and curtosis <= -1.9702 and skewness <= 4.9228 | 1 | 0.051311 |
| variance > -0.4031 and variance <= 0.760295 and skewness > -2.3021 and skewness <= 5.2353 and curtosis > -4.42285 and curtosis <= 8.83885 and entropy = all | 1 | 0.059904 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| variance > 0.75896 and curtosis > -1.9702 | 0 | 0.412834 |
| skewness <= 5.1401 and variance <= -1.786 | 1 | 0.450557 |
| skewness > 5.2022 and variance > -3.3793 | 0 | 0.446886 |
| curtosis <= 0.7126 | 1 | 0.793508 |
| variance <= -0.46651 and skewness <= -0.10554 | 1 | 0.541104 |
| entropy <= 1.0426 and curtosis > 2.3457 | 0 | 0.716667 |
| variance <= 0.37637 | 1 | 0.535714 |
|  | 0 | 0.866667 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| variance <= 0.31803 and skewness <= 5.8333 and curtosis <= 6.2169 | 1 | 0.321467 |
| variance <= -1.3887 and skewness <= -4.5566 | 1 | 0.143571 |
| variance <= -4.1479 | 1 | 0.047261 |
| curtosis <= -4.0557 and variance <= 2.3917 | 1 | 0.048544 |
| variance <= 1.581 and entropy >= -0.1457 and curtosis <= 1.7048 and skewness <= 2.2638 | 1 | 0.037868 |
| skewness <= -7.4473 | 1 | 0.004354 |
| curtosis <= -3.0121 and skewness <= 3.6833 | 1 | 0.010101 |
|  | 0 | 0.998544 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

variance|skewness|curtosis|entropy|class
---|---|---|---|---
(0.760295-2.3921]|(9.61695-inf)|(-4.42285-8.83885]|all|0
(-2.80905--0.4031]|(9.61695-inf)|(-4.42285-8.83885]|all|0
(-0.4031-0.760295]|(9.61695-inf)|(-4.42285-8.83885]|all|0
(2.3921-inf)|(9.61695-inf)|(-4.42285-8.83885]|all|0
(-inf--2.80905]|(5.2353-9.61695]|(-4.42285-8.83885]|all|1
(-2.80905--0.4031]|(5.2353-9.61695]|(-4.42285-8.83885]|all|0
(2.3921-inf)|(5.2353-9.61695]|(-4.42285-8.83885]|all|0
(0.760295-2.3921]|(5.2353-9.61695]|(-4.42285-8.83885]|all|0
(-0.4031-0.760295]|(5.2353-9.61695]|(-4.42285-8.83885]|all|0
(-2.80905--0.4031]|(-6.94555--4.9818]|(8.83885-inf)|all|1
(-inf--2.80905]|(-6.94555--4.9818]|(8.83885-inf)|all|1
(-inf--2.80905]|(-2.3021-5.2353]|(-4.42285-8.83885]|all|1
(2.3921-inf)|(9.61695-inf)|(-inf--4.42285]|all|0
(-0.4031-0.760295]|(-2.3021-5.2353]|(-4.42285-8.83885]|all|1
(0.760295-2.3921]|(-2.3021-5.2353]|(-4.42285-8.83885]|all|0
(-2.80905--0.4031]|(-2.3021-5.2353]|(-4.42285-8.83885]|all|1
(2.3921-inf)|(-2.3021-5.2353]|(-4.42285-8.83885]|all|0
(2.3921-inf)|(5.2353-9.61695]|(-inf--4.42285]|all|0
(-2.80905--0.4031]|(-inf--6.94555]|(8.83885-inf)|all|1
(-2.80905--0.4031]|(-4.9818--2.3021]|(-4.42285-8.83885]|all|1
(-inf--2.80905]|(-inf--6.94555]|(8.83885-inf)|all|1
(-0.4031-0.760295]|(-4.9818--2.3021]|(-4.42285-8.83885]|all|0
(0.760295-2.3921]|(-4.9818--2.3021]|(-4.42285-8.83885]|all|0
(2.3921-inf)|(-4.9818--2.3021]|(-4.42285-8.83885]|all|0
(-inf--2.80905]|(-6.94555--4.9818]|(-4.42285-8.83885]|all|0
(2.3921-inf)|(-6.94555--4.9818]|(-4.42285-8.83885]|all|0
(-0.4031-0.760295]|(-6.94555--4.9818]|(-4.42285-8.83885]|all|0
(0.760295-2.3921]|(-2.3021-5.2353]|(-inf--4.42285]|all|1
(-2.80905--0.4031]|(-6.94555--4.9818]|(-4.42285-8.83885]|all|1
(-0.4031-0.760295]|(-2.3021-5.2353]|(-inf--4.42285]|all|1
(0.760295-2.3921]|(-6.94555--4.9818]|(-4.42285-8.83885]|all|0
(-inf--2.80905]|(-inf--6.94555]|(-4.42285-8.83885]|all|0
(-2.80905--0.4031]|(-inf--6.94555]|(-4.42285-8.83885]|all|1

## JRip

Decision list:

rules | predicted class
---|---
(variance <= 0.31803) and (skewness <= 5.8333) and (curtosis <= 6.2169)|1 (327.0/1.0)
(variance <= -1.3887) and (skewness <= -4.5566)|1 (115.0/0.0)
(variance <= -4.1479)|1 (36.0/1.0)
(curtosis <= -4.0557) and (variance <= 2.3917)|1 (35.0/0.0)
(variance <= 1.581) and (entropy >= -0.1457) and (curtosis <= 1.7048) and (skewness <= 2.2638)|1 (27.0/0.0)
(skewness <= -7.4473)|1 (3.0/0.0)
(curtosis <= -3.0121) and (skewness <= 3.6833)|1 (7.0/0.0)
|0 (685.0/1.0)


## PART

Decision list:

rules | predicted class
---|---
variance > 0.75896 AND curtosis > -1.9702|0 (386.0)
skewness <= 5.1401 AND variance <= -1.786|1 (248.0/1.0)
skewness > 5.2022 AND variance > -3.3793|0 (244.0)
curtosis <= 0.7126|1 (221.0/3.0)
variance <= -0.46651 AND skewness <= -0.10554|1 (68.0/1.0)
entropy <= 1.0426 AND curtosis > 2.3457|0 (41.0)
variance <= 0.37637|1 (15.0)
|0 (12.0/2.0)


## J48 Decision Tree

* variance <= 0.75896
	* skewness <= 5.1401
		* variance <= -0.46651
			* curtosis <= 6.2169: 1 (269.0)
			* curtosis > 6.2169
				* skewness <= -4.7076: 1 (117.0)
				* skewness > -4.7076: 0 (14.0/1.0)
		* variance > -0.46651
			* curtosis <= 0.46583: 1 (74.0)
			* curtosis > 0.46583
				* entropy <= 0.72326: 0 (37.0/1.0)
				* entropy > 0.72326: 1 (13.0/2.0)
	* skewness > 5.1401
		* variance <= -3.3793: 1 (37.0/1.0)
		* variance > -3.3793: 0 (108.0/1.0)
* variance > 0.75896
	* curtosis <= -1.9702
		* skewness <= 4.9228: 1 (41.0/2.0)
		* skewness > 4.9228: 0 (139.0)
	* curtosis > -1.9702: 0 (386.0)


## SimpleCart Decision Tree

* variance < 0.320165
	* skewness < 5.86535
		* curtosis < 6.7456: 1(337.0/2.0)
		* curtosis >= 6.7456
			* skewness < -4.7997: 1(107.0/1.0)
			* skewness >= -4.7997: 0(21.0/0.0)
	* skewness >= 5.86535
		* variance < -3.4448999999999996: 1(35.0/1.0)
		* variance >= -3.4448999999999996: 0(88.0/0.0)
* variance >= 0.320165
	* curtosis < -4.38605
		* variance < 3.30405: 1(30.0/0.0)
		* variance >= 3.30405: 0(8.0/0.0)
	* curtosis >= -4.38605
		* variance < 1.5856
			* curtosis < -2.2721999999999998: 1(22.0/3.0)
			* curtosis >= -2.2721999999999998
				* entropy < 0.081882: 0(110.0/1.0)
				* entropy >= 0.081882
					* curtosis < 1.85305: 1(15.0/1.0)
					* curtosis >= 1.85305: 0(16.0/0.0)
		* variance >= 1.5856: 0(435.0/2.0)


