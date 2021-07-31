# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| variance >= 0.320165 and curtosis >= -4.4434000000000005 and variance >= 1.5922 | 0 | 0.446593 |
| variance < 0.320165 and skewness < 7.5653 and variance < -0.458565 and curtosis < 6.21865 | 1 | 0.293818 |
| variance <= 0.75896 and skewness <= 5.3449 and variance <= 0.31803 and curtosis > 3.0423 and skewness <= -1.8624 and variance <= -0.75793 | 1 | 0.188389 |
| variance >= 0.320165 and curtosis >= -4.4434000000000005 and variance < 1.5922 and curtosis >= -2.2721999999999998 and entropy < 0.22994 | 0 | 0.159322 |
| variance <= 0.75896 and skewness > 5.3449 and variance > -3.3793 | 0 | 0.154083 |
| variance <= 0.75896 and skewness <= 5.3449 and variance <= 0.31803 and curtosis <= 3.0423 | 1 | 0.285714 |
| variance > 0.75896 and curtosis <= -1.8785 and skewness <= 4.9228 and variance <= 1.762 | 1 | 0.044630 |
| variance <= 0.75896 and skewness <= 5.3449 and variance > 0.31803 and curtosis <= 0.46583 | 1 | 0.040616 |
| variance <= 0.75896 and skewness <= 5.3449 and variance <= 0.31803 and curtosis > 3.0423 and skewness > -1.8624 and variance > -1.5075 | 0 | 0.031746 |
| variance < 0.320165 and skewness >= 7.5653 and variance < -4.726 | 1 | 0.025605 |
| variance >= 0.320165 and curtosis >= -4.4434000000000005 and variance < 1.5922 and curtosis >= -2.2721999999999998 and entropy >= 0.22994 and curtosis >= 1.91945 | 0 | 0.024867 |
| variance > 0.75896 and curtosis <= -1.8785 and skewness > 4.9228 | 0 | 0.215714 |
| variance < 0.320165 and skewness < 7.5653 and variance < -0.458565 and curtosis >= 6.21865 and skewness >= -4.6745 | 0 | 0.024867 |
| variance > 0.75896 and curtosis <= -1.8785 and skewness <= 4.9228 and variance > 1.762 | 1 | 0.006531 |
| variance >= 0.320165 and curtosis >= -4.4434000000000005 and variance < 1.5922 and curtosis >= -2.2721999999999998 and entropy >= 0.22994 and curtosis < 1.91945 | 1 | 0.018962 |
| variance > 0.75896 and curtosis > -1.8785 | 0 | 0.408405 |
| variance < 0.320165 and skewness < 7.5653 and variance >= -0.458565 and curtosis >= 0.297461 and entropy >= 0.72843 | 1 | 0.010641 |
| variance < 0.320165 and skewness >= 7.5653 and variance >= -4.726 | 0 | 0.115942 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| variance > 0.75896 and curtosis > -1.8785 | 0 | 0.408405 |
| skewness <= 5.2022 and variance <= -1.786 | 1 | 0.439568 |
| skewness > 5.2022 and variance > -3.3793 | 0 | 0.448029 |
| curtosis <= 0.70403 and variance <= 1.6349 | 1 | 0.790262 |
| skewness <= -5.554 | 1 | 0.416667 |
| curtosis > 4.5641 and skewness > -4.7076 | 0 | 0.366667 |
| variance <= 0.3223 and skewness <= 2.1438 | 1 | 0.646154 |
| curtosis > -2.6196 and variance > -4.9447 and entropy <= 0.72326 | 0 | 0.605263 |
|  | 1 | 1.000000 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| skewness <= 5.8333 and curtosis <= 6.2169 and variance <= -0.36372 | 1 | 0.288681 |
| skewness <= -4.7428 and variance <= -0.77288 | 1 | 0.145885 |
| variance <= 1.5904 and curtosis <= 0.27818 and skewness <= 4.2855 | 1 | 0.113842 |
| variance <= -4.1479 and curtosis <= 1.0836 | 1 | 0.048611 |
| curtosis <= -4.5398 and variance <= 2.3917 | 1 | 0.021429 |
| skewness <= -0.69529 and curtosis <= 2.135 and variance <= 0.74428 | 1 | 0.018625 |
|  | 0 | 0.995640 |


# Text representation of classifiers as-is

## JRip

Decision list:

rules | predicted class
---|---
(skewness <= 5.8333) and (curtosis <= 6.2169) and (variance <= -0.36372)|1 (278.0/0.0)
(skewness <= -4.7428) and (variance <= -0.77288)|1 (117.0/0.0)
(variance <= 1.5904) and (curtosis <= 0.27818) and (skewness <= 4.2855)|1 (88.0/0.0)
(variance <= -4.1479) and (curtosis <= 1.0836)|1 (35.0/0.0)
(curtosis <= -4.5398) and (variance <= 2.3917)|1 (15.0/0.0)
(skewness <= -0.69529) and (curtosis <= 2.135) and (variance <= 0.74428)|1 (13.0/0.0)
|0 (688.0/3.0)


## PART

Decision list:

rules | predicted class
---|---
variance > 0.75896 AND curtosis > -1.8785|0 (379.0)
skewness <= 5.2022 AND variance <= -1.786|1 (242.0/1.0)
skewness > 5.2022 AND variance > -3.3793|0 (250.0)
curtosis <= 0.70403 AND variance <= 1.6349|1 (211.0)
skewness <= -5.554|1 (40.0)
curtosis > 4.5641 AND skewness > -4.7076|0 (32.0)
variance <= 0.3223 AND skewness <= 2.1438|1 (42.0)
curtosis > -2.6196 AND variance > -4.9447 AND entropy <= 0.72326|0 (23.0)
|1 (15.0)


## J48 Decision Tree

* variance <= 0.75896
	* skewness <= 5.3449
		* variance <= 0.31803
			* curtosis <= 3.0423: 1 (274.0)
			* curtosis > 3.0423
				* skewness <= -1.8624
					* variance <= -0.75793: 1 (159.0)
					* variance > -0.75793: 1 (9.0/1.0)
				* skewness > -1.8624
					* variance <= -1.5075: 0 (8.0/2.0)
					* variance > -1.5075: 0 (18.0)
		* variance > 0.31803
			* curtosis <= 0.46583: 1 (29.0)
			* curtosis > 0.46583
				* entropy <= 0.42455: 0 (22.0)
				* entropy > 0.42455: 0 (8.0/3.0)
	* skewness > 5.3449
		* variance <= -3.3793
			* variance <= -5.119: 1 (29.0)
			* variance > -5.119: 1 (8.0/1.0)
		* variance > -3.3793: 0 (100.0)
* variance > 0.75896
	* curtosis <= -1.8785
		* skewness <= 4.9228
			* variance <= 1.762: 1 (32.0)
			* variance > 1.762: 1 (8.0/2.0)
		* skewness > 4.9228: 0 (151.0)
	* curtosis > -1.8785: 0 (379.0)


## SimpleCart Decision Tree

* variance < 0.320165
	* skewness < 7.5653
		* variance < -0.458565
			* curtosis < 6.21865: 1(286.0/1.0)
			* curtosis >= 6.21865
				* skewness < -4.6745: 1(117.0/0.0)
				* skewness >= -4.6745: 0(14.0/0.0)
		* variance >= -0.458565
			* curtosis < 0.297461: 1(47.0/1.0)
			* curtosis >= 0.297461
				* entropy < 0.72843: 0(17.0/2.0)
				* entropy >= 0.72843: 1(9.0/2.0)
	* skewness >= 7.5653
		* variance < -4.726: 1(18.0/0.0)
		* variance >= -4.726: 0(72.0/0.0)
* variance >= 0.320165
	* curtosis < -4.4434000000000005
		* variance < 3.30405: 1(27.0/0.0)
		* variance >= 3.30405: 0(7.0/0.0)
	* curtosis >= -4.4434000000000005
		* variance < 1.5922
			* curtosis < -2.2721999999999998: 1(23.0/3.0)
			* curtosis >= -2.2721999999999998
				* entropy < 0.22994: 0(106.0/2.0)
				* entropy >= 0.22994
					* curtosis < 1.91945: 1(15.0/2.0)
					* curtosis >= 1.91945: 0(14.0/0.0)
		* variance >= 1.5922: 0(446.0/3.0)


