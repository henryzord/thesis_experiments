# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| variance > 0.84546 and variance > 1.7425 | 0 | 0.436404 |
| variance <= 0.84546 and skewness <= 5.1401 and variance <= 0.31803 and curtosis <= 6.7156 | 1 | 0.327784 |
| variance <= 0.84546 and skewness > 5.1401 and variance > -3.3793 | 0 | 0.169454 |
| variance <= 0.84546 and skewness <= 5.1401 and variance <= 0.31803 and curtosis > 6.7156 and skewness <= -4.8069 | 1 | 0.134019 |
| variance > 0.84546 and variance <= 1.7425 and curtosis > -2.3 | 0 | 0.134140 |
| variance <= 0.84546 and skewness > 5.1401 and variance <= -3.3793 | 1 | 0.048649 |
| variance >= 0.320165 and curtosis < -4.38605 and variance < 3.30405 | 1 | 0.041958 |
| variance <= 0.84546 and skewness <= 5.1401 and variance > 0.31803 and curtosis > 0.46583 | 0 | 0.044060 |
| variance >= 0.320165 and curtosis >= -4.38605 and variance < 1.5856 and curtosis < -2.2721999999999998 and skewness < 5.6667 | 1 | 0.031117 |
| variance <= 0.84546 and skewness <= 5.1401 and variance <= 0.31803 and curtosis > 6.7156 and skewness > -4.8069 | 0 | 0.036842 |
| variance >= 0.320165 and curtosis >= -4.38605 and variance < 1.5856 and curtosis >= -2.2721999999999998 and entropy >= 0.081882 and curtosis < 1.85305 | 1 | 0.020118 |
| variance > 0.760295 and variance <= 2.3921 and skewness > 5.2353 and skewness <= 9.61695 and curtosis > -4.42285 and curtosis <= 8.83885 | 0 | 0.114516 |
| variance < 0.320165 and skewness < 5.86535 and curtosis < 6.7456 and curtosis >= 4.8777 and skewness >= -2.296935 | 0 | 0.003630 |
| variance >= 0.320165 and curtosis >= -4.38605 and variance >= 1.5856 and variance < 2.03655 and curtosis < -2.67535 | 1 | 0.002911 |
| variance <= 0.84546 and skewness <= 5.1401 and variance > 0.31803 and curtosis <= 0.46583 | 1 | 0.041958 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| variance > 0.7602949999999999 and curtosis > -1.96975 | 0 | 0.412206 |
| skewness <= 5.1608 and variance <= -1.78205 | 1 | 0.450557 |
| skewness > 5.2353000000000005 and variance > -3.36765 | 0 | 0.446886 |
| curtosis <= 0.7177450000000001 and variance <= 1.6109 | 1 | 0.788679 |
| variance <= -0.462635 and skewness <= -0.1045055 | 1 | 0.541104 |
| curtosis > 2.5256999999999996 | 0 | 0.617981 |
| variance > 0.378085 and curtosis > -2.6252500000000003 | 0 | 0.304505 |
|  | 1 | 1.000000 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| skewness <= 7.259 and curtosis <= 6.2169 and variance <= -0.40804 | 1 | 0.296715 |
| skewness <= -4.7428 and variance <= -0.37013 | 1 | 0.146949 |
| curtosis <= 0.27818 and skewness <= 5.2022 and variance <= 1.2572 | 1 | 0.116129 |
| variance <= -4.4779 | 1 | 0.028369 |
| curtosis <= -4.5398 and variance <= 2.3917 | 1 | 0.014388 |
| variance <= 1.7425 and entropy >= -0.12243 and curtosis <= 2.135 and skewness <= 1.9596 | 1 | 0.024217 |
|  | 0 | 0.992754 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

variance|skewness|curtosis|class
---|---|---|---
(-0.4031-0.760295]|(9.61695-inf)|(-4.42285-8.83885]|0
(0.760295-2.3921]|(9.61695-inf)|(-4.42285-8.83885]|0
(-2.80905--0.4031]|(9.61695-inf)|(-4.42285-8.83885]|0
(2.3921-inf)|(9.61695-inf)|(-4.42285-8.83885]|0
(-2.80905--0.4031]|(5.2353-9.61695]|(-4.42285-8.83885]|0
(2.3921-inf)|(5.2353-9.61695]|(-4.42285-8.83885]|0
(0.760295-2.3921]|(5.2353-9.61695]|(-4.42285-8.83885]|0
(-0.4031-0.760295]|(5.2353-9.61695]|(-4.42285-8.83885]|0
(-inf--2.80905]|(5.2353-9.61695]|(-4.42285-8.83885]|1
(2.3921-inf)|(9.61695-inf)|(-inf--4.42285]|0
(2.3921-inf)|(-2.3021-5.2353]|(-4.42285-8.83885]|0
(-2.80905--0.4031]|(-6.94555--4.9818]|(8.83885-inf)|1
(-inf--2.80905]|(-6.94555--4.9818]|(8.83885-inf)|1
(0.760295-2.3921]|(-2.3021-5.2353]|(-4.42285-8.83885]|0
(-inf--2.80905]|(-2.3021-5.2353]|(-4.42285-8.83885]|1
(-2.80905--0.4031]|(-2.3021-5.2353]|(-4.42285-8.83885]|1
(-0.4031-0.760295]|(-2.3021-5.2353]|(-4.42285-8.83885]|1
(2.3921-inf)|(5.2353-9.61695]|(-inf--4.42285]|0
(0.760295-2.3921]|(-4.9818--2.3021]|(-4.42285-8.83885]|0
(2.3921-inf)|(-4.9818--2.3021]|(-4.42285-8.83885]|0
(-0.4031-0.760295]|(-4.9818--2.3021]|(-4.42285-8.83885]|0
(-2.80905--0.4031]|(-inf--6.94555]|(8.83885-inf)|1
(-2.80905--0.4031]|(-4.9818--2.3021]|(-4.42285-8.83885]|1
(-inf--2.80905]|(-inf--6.94555]|(8.83885-inf)|1
(-inf--2.80905]|(-6.94555--4.9818]|(-4.42285-8.83885]|0
(-0.4031-0.760295]|(-6.94555--4.9818]|(-4.42285-8.83885]|0
(2.3921-inf)|(-6.94555--4.9818]|(-4.42285-8.83885]|0
(0.760295-2.3921]|(-6.94555--4.9818]|(-4.42285-8.83885]|0
(0.760295-2.3921]|(-2.3021-5.2353]|(-inf--4.42285]|1
(-2.80905--0.4031]|(-6.94555--4.9818]|(-4.42285-8.83885]|1
(-0.4031-0.760295]|(-2.3021-5.2353]|(-inf--4.42285]|1
(-inf--2.80905]|(-inf--6.94555]|(-4.42285-8.83885]|0
(-2.80905--0.4031]|(-inf--6.94555]|(-4.42285-8.83885]|1

## JRip

Decision list:

rules | predicted class
---|---
(skewness <= 7.259) and (curtosis <= 6.2169) and (variance <= -0.40804)|1 (289.0/0.0)
(skewness <= -4.7428) and (variance <= -0.37013)|1 (118.0/0.0)
(curtosis <= 0.27818) and (skewness <= 5.2022) and (variance <= 1.2572)|1 (90.0/0.0)
(variance <= -4.4779)|1 (20.0/0.0)
(curtosis <= -4.5398) and (variance <= 2.3917)|1 (10.0/0.0)
(variance <= 1.7425) and (entropy >= -0.12243) and (curtosis <= 2.135) and (skewness <= 1.9596)|1 (17.0/0.0)
|0 (690.0/5.0)


## PART

Decision list:

rules | predicted class
---|---
variance > 0.7602949999999999 AND curtosis > -1.96975|0 (385.0)
skewness <= 5.1608 AND variance <= -1.78205|1 (248.0/1.0)
skewness > 5.2353000000000005 AND variance > -3.36765|0 (244.0)
curtosis <= 0.7177450000000001 AND variance <= 1.6109|1 (209.0)
variance <= -0.462635 AND skewness <= -0.1045055|1 (68.0/1.0)
curtosis > 2.5256999999999996|0 (42.0/1.0)
variance > 0.378085 AND curtosis > -2.6252500000000003|0 (15.0/2.0)
|1 (23.0)


## J48 Decision Tree

* variance <= 0.84546
	* skewness <= 5.1401
		* variance <= 0.31803
			* curtosis <= 6.7156: 1 (281.0)
			* curtosis > 6.7156
				* skewness <= -4.8069: 1 (96.0)
				* skewness > -4.8069: 0 (20.0)
		* variance > 0.31803
			* curtosis <= 0.46583: 1 (28.0)
			* curtosis > 0.46583: 0 (26.0/3.0)
	* skewness > 5.1401
		* variance <= -3.3793: 1 (32.0/1.0)
		* variance > -3.3793: 0 (93.0/1.0)
* variance > 0.84546
	* variance <= 1.7425
		* curtosis <= -2.3: 1 (28.0/2.0)
		* curtosis > -2.3: 0 (84.0/2.0)
	* variance > 1.7425: 0 (370.0/2.0)


## SimpleCart Decision Tree

* variance < 0.320165
	* skewness < 5.86535
		* curtosis < 6.7456
			* curtosis < 4.8777: 1(295.0/0.0)
			* curtosis >= 4.8777
				* skewness < -2.296935: 1(42.0/0.0)
				* skewness >= -2.296935: 0(2.0/0.0)
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
			* curtosis < -2.2721999999999998
				* skewness < 5.6667: 1(22.0/0.0)
				* skewness >= 5.6667: 0(3.0/0.0)
			* curtosis >= -2.2721999999999998
				* entropy < 0.081882: 0(109.0/1.0)
				* entropy >= 0.081882
					* curtosis < 1.85305: 1(15.0/1.0)
					* curtosis >= 1.85305: 0(16.0/0.0)
		* variance >= 1.5856
			* variance < 2.03655
				* curtosis < -2.67535: 1(2.0/0.0)
				* curtosis >= -2.67535: 0(46.0/0.0)
			* variance >= 2.03655: 0(389.0/0.0)


