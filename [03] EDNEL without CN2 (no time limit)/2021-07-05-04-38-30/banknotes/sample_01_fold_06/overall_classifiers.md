# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 0 | 0.555105 |
| variance > 0.74841 and curtosis <= -1.8511 and skewness <= 4.8773 | 1 | 0.051382 |
| variance <= 0.74841 and skewness <= 7.5404 and variance > -0.46651 and curtosis > 0.26019 and entropy > 0.72326 | 1 | 0.012025 |
| variance >= 0.320165 and curtosis < -4.4434000000000005 and variance < 3.30405 | 1 | 0.039271 |
| variance <= 0.74841 and skewness <= 7.5404 and variance > -0.46651 and curtosis <= 0.26019 | 1 | 0.095376 |
| variance < 0.320165 and skewness < 8.185 and variance < -0.4031 and curtosis < 6.21865 | 1 | 0.301747 |
| variance < 0.320165 and skewness >= 8.185 and variance < -4.8358 | 1 | 0.017217 |
| variance <= 0.74841 and skewness <= 7.5404 and variance <= -0.46651 and curtosis > 6.2169 and skewness <= -2.2535 | 1 | 0.145885 |
| variance > -0.4031 and variance <= 0.760295 and skewness > -2.3021 and skewness <= 5.21045 and curtosis > -4.42285 and curtosis <= 8.83885 and entropy = all | 1 | 0.055944 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| variance > 0.75896 and curtosis > -1.8785 | 0 | 0.403909 |
| skewness <= 5.1401 and variance <= -1.786 | 1 | 0.435025 |
| skewness > 5.2022 and variance > -3.4605 | 0 | 0.453737 |
| curtosis <= 0.7126 and variance <= 1.581 | 1 | 0.785978 |
| skewness <= -0.94981 and variance <= -0.46651 | 1 | 0.536000 |
| curtosis > 2.1624 | 0 | 0.609025 |
| variance <= 0.32444 | 1 | 0.516129 |
| curtosis > -2.6196 and entropy <= -0.30993 | 0 | 0.500000 |
| curtosis <= -2.6196 | 1 | 0.692308 |
|  | 0 | 0.666667 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| variance <= 0.27331 and skewness <= 5.0097 and curtosis <= 3.0141 | 1 | 0.283473 |
| variance <= -0.539 and skewness <= -0.77392 | 1 | 0.197892 |
| variance <= 1.7875 and skewness <= 5.2022 and curtosis <= 0.18307 | 1 | 0.086667 |
| variance <= -4.1479 | 1 | 0.048649 |
| variance <= 2.1943 and entropy >= 0.003003 and curtosis <= 1.7048 and skewness <= 1.852 | 1 | 0.007246 |
|  | 0 | 0.995640 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

variance|skewness|curtosis|entropy|class
---|---|---|---|---
(-0.4031-0.760295]|(9.53215-inf)|(-4.42285-8.83885]|all|0
(0.760295-2.3921]|(9.53215-inf)|(-4.42285-8.83885]|all|0
(2.3921-inf)|(9.53215-inf)|(-4.42285-8.83885]|all|0
(-2.7952--0.4031]|(9.53215-inf)|(-4.42285-8.83885]|all|0
(-inf--2.7952]|(-5.436--2.3021]|(8.83885-inf)|all|1
(-inf--2.7952]|(5.21045-9.53215]|(-4.42285-8.83885]|all|1
(-2.7952--0.4031]|(5.21045-9.53215]|(-4.42285-8.83885]|all|0
(2.3921-inf)|(5.21045-9.53215]|(-4.42285-8.83885]|all|0
(-0.4031-0.760295]|(5.21045-9.53215]|(-4.42285-8.83885]|all|0
(0.760295-2.3921]|(5.21045-9.53215]|(-4.42285-8.83885]|all|0
(-inf--2.7952]|(-6.94555--5.436]|(8.83885-inf)|all|1
(-2.7952--0.4031]|(-6.94555--5.436]|(8.83885-inf)|all|1
(-inf--2.7952]|(-2.3021-5.21045]|(-4.42285-8.83885]|all|1
(2.3921-inf)|(9.53215-inf)|(-inf--4.42285]|all|0
(-0.4031-0.760295]|(-2.3021-5.21045]|(-4.42285-8.83885]|all|1
(0.760295-2.3921]|(-2.3021-5.21045]|(-4.42285-8.83885]|all|0
(-2.7952--0.4031]|(-2.3021-5.21045]|(-4.42285-8.83885]|all|1
(2.3921-inf)|(-2.3021-5.21045]|(-4.42285-8.83885]|all|0
(-2.7952--0.4031]|(-5.436--2.3021]|(-4.42285-8.83885]|all|1
(-inf--2.7952]|(-inf--6.94555]|(8.83885-inf)|all|1
(-2.7952--0.4031]|(-inf--6.94555]|(8.83885-inf)|all|1
(2.3921-inf)|(5.21045-9.53215]|(-inf--4.42285]|all|0
(-0.4031-0.760295]|(-5.436--2.3021]|(-4.42285-8.83885]|all|0
(0.760295-2.3921]|(-5.436--2.3021]|(-4.42285-8.83885]|all|0
(2.3921-inf)|(-5.436--2.3021]|(-4.42285-8.83885]|all|0
(-inf--2.7952]|(-6.94555--5.436]|(-4.42285-8.83885]|all|0
(-0.4031-0.760295]|(-6.94555--5.436]|(-4.42285-8.83885]|all|1
(-0.4031-0.760295]|(-2.3021-5.21045]|(-inf--4.42285]|all|1
(0.760295-2.3921]|(-2.3021-5.21045]|(-inf--4.42285]|all|1
(-2.7952--0.4031]|(-6.94555--5.436]|(-4.42285-8.83885]|all|1
(2.3921-inf)|(-6.94555--5.436]|(-4.42285-8.83885]|all|0
(0.760295-2.3921]|(-6.94555--5.436]|(-4.42285-8.83885]|all|0
(-inf--2.7952]|(-inf--6.94555]|(-4.42285-8.83885]|all|1
(-2.7952--0.4031]|(-inf--6.94555]|(-4.42285-8.83885]|all|1

## JRip

Decision list:

rules | predicted class
---|---
(variance <= 0.27331) and (skewness <= 5.0097) and (curtosis <= 3.0141)|1 (271.0/0.0)
(variance <= -0.539) and (skewness <= -0.77392)|1 (169.0/0.0)
(variance <= 1.7875) and (skewness <= 5.2022) and (curtosis <= 0.18307)|1 (65.0/0.0)
(variance <= -4.1479)|1 (37.0/1.0)
(variance <= 2.1943) and (entropy >= 0.003003) and (curtosis <= 1.7048) and (skewness <= 1.852)|1 (5.0/0.0)
|0 (687.0/3.0)


## PART

Decision list:

rules | predicted class
---|---
variance > 0.75896 AND curtosis > -1.8785|0 (372.0)
skewness <= 5.1401 AND variance <= -1.786|1 (243.0/1.0)
skewness > 5.2022 AND variance > -3.4605|0 (255.0)
curtosis <= 0.7126 AND variance <= 1.581|1 (213.0)
skewness <= -0.94981 AND variance <= -0.46651|1 (67.0)
curtosis > 2.1624|0 (43.0/1.0)
variance <= 0.32444|1 (15.0)
curtosis > -2.6196 AND entropy <= -0.30993|0 (11.0)
curtosis <= -2.6196|1 (9.0)
|0 (6.0/2.0)


## J48 Decision Tree

* variance <= 0.74841
	* skewness <= 7.5404
		* variance <= -0.46651
			* curtosis <= 6.2169: 1 (192.0)
			* curtosis > 6.2169
				* skewness <= -2.2535: 1 (79.0)
				* skewness > -2.2535: 0 (11.0)
		* variance > -0.46651
			* curtosis <= 0.26019: 1 (51.0)
			* curtosis > 0.26019
				* entropy <= 0.72326: 0 (37.0/2.0)
				* entropy > 0.72326: 1 (8.0/2.0)
	* skewness > 7.5404
		* variance <= -4.7331: 1 (10.0)
		* variance > -4.7331: 0 (56.0)
* variance > 0.74841
	* curtosis <= -1.8511
		* skewness <= 4.8773: 1 (27.0/1.0)
		* skewness > 4.8773: 0 (100.0)
	* curtosis > -1.8511: 0 (252.0)


## SimpleCart Decision Tree

* variance < 0.320165
	* skewness < 8.185
		* variance < -0.4031
			* curtosis < 6.21865: 1(298.0/2.0)
			* curtosis >= 6.21865
				* skewness < -2.9622: 1(117.0/0.0)
				* skewness >= -2.9622: 0(15.0/0.0)
		* variance >= -0.4031
			* skewness < 5.4939
				* curtosis < 2.62465: 1(52.0/0.0)
				* curtosis >= 2.62465: 0(11.0/1.0)
			* skewness >= 5.4939: 0(14.0/0.0)
	* skewness >= 8.185
		* variance < -4.8358: 1(12.0/0.0)
		* variance >= -4.8358: 0(71.0/0.0)
* variance >= 0.320165
	* curtosis < -4.4434000000000005
		* variance < 3.30405: 1(28.0/0.0)
		* variance >= 3.30405: 0(8.0/0.0)
	* curtosis >= -4.4434000000000005
		* variance < 1.5962
			* curtosis < -2.2721999999999998: 1(23.0/3.0)
			* curtosis >= -2.2721999999999998
				* entropy < 0.081882: 0(106.0/1.0)
				* entropy >= 0.081882
					* curtosis < 1.85305: 1(15.0/2.0)
					* curtosis >= 1.85305: 0(17.0/0.0)
		* variance >= 1.5962: 0(436.0/2.0)


