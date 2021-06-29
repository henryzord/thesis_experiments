# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| variance >= 0.320165 and curtosis >= -4.4434000000000005 and variance >= 1.5922 and variance >= 2.03655 | 0 | 0.419662 |
| variance < 0.320165 and skewness < 7.5653 and variance < -0.458565 and curtosis < 6.21865 and skewness < 7.293150000000001 | 1 | 0.292355 |
| variance > 0.7651 and curtosis > -1.8648 | 0 | 0.408405 |
| variance <= 0.7651 and skewness <= 5.3646 and variance <= 0.320165 and curtosis > 3.05645 and skewness <= -1.81995 | 1 | 0.195072 |
| variance <= 0.7651 and skewness > 5.3646 and variance > -3.36765 | 0 | 0.154083 |
| variance <= 0.7651 and skewness <= 5.3646 and variance <= 0.320165 and curtosis <= 3.05645 | 1 | 0.285714 |
| variance > 0.7651 and curtosis <= -1.8648 and skewness <= 4.92485 and variance <= 3.4798 | 1 | 0.052559 |
| variance <= 0.7651 and skewness <= 5.3646 and variance > 0.320165 and curtosis > 0.470115 and entropy <= 0.73037 | 0 | 0.046875 |
| variance <= 0.7651 and skewness <= 5.3646 and variance > 0.320165 and curtosis <= 0.470115 | 1 | 0.040616 |
| variance <= 0.7651 and skewness <= 5.3646 and variance <= 0.320165 and curtosis > 3.05645 and skewness > -1.81995 and variance > -2.15635 | 0 | 0.040210 |
| variance > 0.7651 and curtosis <= -1.8648 and skewness > 4.92485 | 0 | 0.215714 |
| variance <= 0.7651 and skewness > 5.3646 and variance <= -3.36765 | 1 | 0.048649 |
| variance <= 0.7651 and skewness <= 5.3646 and variance > 0.320165 and curtosis > 0.470115 and entropy > 0.73037 | 1 | 0.004360 |
| variance < 0.320165 and skewness >= 7.5653 and variance >= -4.726 | 0 | 0.115942 |
| variance < 0.320165 and skewness < 7.5653 and variance < -0.458565 and curtosis >= 6.21865 and skewness >= -4.6745 | 0 | 0.024867 |

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
| variance <= 0.3223 | 1 | 0.652805 |
| curtosis > -2.6196 and entropy <= 0.68058 | 0 | 0.647059 |
|  | 1 | 0.923077 |


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

## Decision Table

Non matches covered by IB1

variance|skewness|curtosis|class
---|---|---|---
(0.7651-2.3921]|(9.61695-inf)|(-4.42285-8.83885]|0
(-0.4031-0.7651]|(9.61695-inf)|(-4.42285-8.83885]|0
(-2.7952--0.4031]|(9.61695-inf)|(-4.42285-8.83885]|0
(2.3921-inf)|(9.61695-inf)|(-4.42285-8.83885]|0
(-inf--2.7952]|(5.21045-9.61695]|(-4.42285-8.83885]|1
(-inf--2.7952]|(-5.62225--2.3021]|(8.83885-inf)|1
(-2.7952--0.4031]|(5.21045-9.61695]|(-4.42285-8.83885]|0
(-0.4031-0.7651]|(5.21045-9.61695]|(-4.42285-8.83885]|0
(0.7651-2.3921]|(5.21045-9.61695]|(-4.42285-8.83885]|0
(2.3921-inf)|(5.21045-9.61695]|(-4.42285-8.83885]|0
(-2.7952--0.4031]|(-6.94555--5.62225]|(8.83885-inf)|1
(-inf--2.7952]|(-6.94555--5.62225]|(8.83885-inf)|1
(-inf--2.7952]|(-2.3021-5.21045]|(-4.42285-8.83885]|1
(-2.7952--0.4031]|(-2.3021-5.21045]|(-4.42285-8.83885]|1
(2.3921-inf)|(9.61695-inf)|(-inf--4.42285]|0
(-0.4031-0.7651]|(-2.3021-5.21045]|(-4.42285-8.83885]|1
(0.7651-2.3921]|(-2.3021-5.21045]|(-4.42285-8.83885]|0
(2.3921-inf)|(-2.3021-5.21045]|(-4.42285-8.83885]|0
(2.3921-inf)|(5.21045-9.61695]|(-inf--4.42285]|0
(-inf--2.7952]|(-inf--6.94555]|(8.83885-inf)|1
(-0.4031-0.7651]|(-5.62225--2.3021]|(-4.42285-8.83885]|0
(-2.7952--0.4031]|(-inf--6.94555]|(8.83885-inf)|1
(-2.7952--0.4031]|(-5.62225--2.3021]|(-4.42285-8.83885]|1
(0.7651-2.3921]|(-5.62225--2.3021]|(-4.42285-8.83885]|0
(2.3921-inf)|(-5.62225--2.3021]|(-4.42285-8.83885]|0
(-inf--2.7952]|(-6.94555--5.62225]|(-4.42285-8.83885]|0
(-0.4031-0.7651]|(-2.3021-5.21045]|(-inf--4.42285]|1
(0.7651-2.3921]|(-2.3021-5.21045]|(-inf--4.42285]|1
(-2.7952--0.4031]|(-6.94555--5.62225]|(-4.42285-8.83885]|1
(0.7651-2.3921]|(-6.94555--5.62225]|(-4.42285-8.83885]|0
(2.3921-inf)|(-6.94555--5.62225]|(-4.42285-8.83885]|0
(-inf--2.7952]|(-inf--6.94555]|(-4.42285-8.83885]|1
(-2.7952--0.4031]|(-inf--6.94555]|(-4.42285-8.83885]|1

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
variance <= 0.3223|1 (47.0/2.0)
curtosis > -2.6196 AND entropy <= 0.68058|0 (20.0)
|1 (13.0/1.0)


## J48 Decision Tree

* variance <= 0.7651
	* skewness <= 5.3646
		* variance <= 0.320165
			* curtosis <= 3.05645: 1 (274.0)
			* curtosis > 3.05645
				* skewness <= -1.81995: 1 (168.0/1.0)
				* skewness > -1.81995
					* variance <= -2.15635: 1 (3.0/1.0)
					* variance > -2.15635: 0 (23.0)
		* variance > 0.320165
			* curtosis <= 0.470115: 1 (29.0)
			* curtosis > 0.470115
				* entropy <= 0.73037: 0 (27.0)
				* entropy > 0.73037: 1 (3.0)
	* skewness > 5.3646
		* variance <= -3.36765: 1 (37.0/1.0)
		* variance > -3.36765: 0 (100.0)
* variance > 0.7651
	* curtosis <= -1.8648
		* skewness <= 4.92485
			* variance <= 3.4798: 1 (38.0)
			* variance > 3.4798: 0 (2.0)
		* skewness > 4.92485: 0 (151.0)
	* curtosis > -1.8648: 0 (379.0)


## SimpleCart Decision Tree

* variance < 0.320165
	* skewness < 7.5653
		* variance < -0.458565
			* curtosis < 6.21865
				* skewness < 7.293150000000001: 1(283.0/0.0)
				* skewness >= 7.293150000000001: 1(3.0/1.0)
			* curtosis >= 6.21865
				* skewness < -4.6745: 1(117.0/0.0)
				* skewness >= -4.6745: 0(14.0/0.0)
		* variance >= -0.458565
			* curtosis < 0.297461: 1(47.0/1.0)
			* curtosis >= 0.297461
				* entropy < 0.72843
					* variance < 0.0962325: 0(16.0/0.0)
					* variance >= 0.0962325: 1(2.0/1.0)
				* entropy >= 0.72843
					* curtosis < 6.2508: 1(9.0/0.0)
					* curtosis >= 6.2508: 0(2.0/0.0)
	* skewness >= 7.5653
		* variance < -4.726: 1(18.0/0.0)
		* variance >= -4.726: 0(72.0/0.0)
* variance >= 0.320165
	* curtosis < -4.4434000000000005
		* variance < 3.30405: 1(27.0/0.0)
		* variance >= 3.30405: 0(7.0/0.0)
	* curtosis >= -4.4434000000000005
		* variance < 1.5922
			* curtosis < -2.2721999999999998
				* skewness < 5.6667: 1(23.0/0.0)
				* skewness >= 5.6667: 0(3.0/0.0)
			* curtosis >= -2.2721999999999998
				* entropy < 0.22994
					* variance < 0.42002
						* curtosis < 0.20492500000000002: 1(2.0/1.0)
						* curtosis >= 0.20492500000000002: 0(12.0/0.0)
					* variance >= 0.42002: 0(93.0/0.0)
				* entropy >= 0.22994
					* curtosis < 1.91945
						* skewness < 3.507445: 1(15.0/0.0)
						* skewness >= 3.507445: 0(2.0/0.0)
					* curtosis >= 1.91945: 0(14.0/0.0)
		* variance >= 1.5922
			* variance < 2.03655
				* curtosis < -2.6483499999999998: 1(3.0/1.0)
				* curtosis >= -2.6483499999999998: 0(48.0/0.0)
			* variance >= 2.03655: 0(397.0/0.0)


