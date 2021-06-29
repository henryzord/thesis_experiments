# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| variance >= 0.320165 and curtosis >= -4.4434000000000005 and variance >= 1.5922 | 0 | 0.446593 |
| variance < 0.320165 and skewness < 7.5653 and variance < -0.458565 and curtosis < 6.21865 | 1 | 0.293818 |
| variance <= 0.31803 and skewness <= 5.8561 and curtosis > 3.0423 and skewness <= -1.8624 | 1 | 0.195072 |
| variance >= 0.320165 and curtosis >= -4.4434000000000005 and variance < 1.5922 and curtosis >= -2.2721999999999998 and entropy < 0.22994 | 0 | 0.159322 |
| variance <= 0.31803 and skewness > 5.8561 and variance > -4.3876 | 0 | 0.127262 |
| variance <= 0.31803 and skewness <= 5.8561 and curtosis <= 3.0423 | 1 | 0.286458 |
| variance > 0.31803 and variance <= 1.7496 and curtosis <= -2.2563 and skewness <= 4.8504 | 1 | 0.061644 |
| variance <= 0.31803 and skewness <= 5.8561 and curtosis > 3.0423 and skewness > -1.8624 | 0 | 0.038798 |
| variance <= 0.31803 and skewness > 5.8561 and variance <= -4.3876 | 1 | 0.045961 |
| variance >= 0.320165 and curtosis >= -4.4434000000000005 and variance < 1.5922 and curtosis >= -2.2721999999999998 and entropy >= 0.22994 and curtosis >= 1.91945 | 0 | 0.024867 |
| variance >= 0.320165 and curtosis >= -4.4434000000000005 and variance < 1.5922 and curtosis >= -2.2721999999999998 and entropy >= 0.22994 and curtosis < 1.91945 | 1 | 0.018962 |
| variance >= 0.320165 and curtosis < -4.4434000000000005 and variance >= 3.30405 | 0 | 0.012590 |
| variance >= 0.320165 and curtosis < -4.4434000000000005 and variance < 3.30405 | 1 | 0.037921 |
| variance > 0.7651 and variance <= 2.3921 and skewness > 5.21045 and skewness <= 9.61695 and curtosis > -4.42285 and curtosis <= 8.83885 and entropy = all | 0 | 0.114516 |
| variance > -0.4031 and variance <= 0.7651 and skewness > -2.3021 and skewness <= 5.21045 and curtosis > -4.42285 and curtosis <= 8.83885 and entropy = all | 1 | 0.058810 |
| variance > 0.31803 and variance > 1.7496 and variance <= 2.1943 and curtosis <= -2.6848 | 1 | 0.004651 |
| variance < 0.320165 and skewness < 7.5653 and variance < -0.458565 and curtosis >= 6.21865 and skewness >= -4.6745 | 0 | 0.024867 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| variance > 0.75896 and curtosis > -1.8785 | 0 | 0.408405 |
| skewness <= 5.2022 and variance <= -1.786 | 1 | 0.439568 |
| skewness > 5.2022 and variance > -3.3793 | 0 | 0.448029 |
| curtosis <= 0.70403 | 1 | 0.795020 |
| variance > 0.31803 and entropy <= 0.66377 | 0 | 0.241379 |
| skewness <= -1.7837 | 1 | 0.702284 |
| curtosis > 2.9986 | 0 | 0.571429 |
|  | 1 | 1.000000 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| variance <= 0.31803 and skewness <= 5.8333 and curtosis <= 6.2109 | 1 | 0.321122 |
| variance <= -1.3887 and skewness <= -4.7428 | 1 | 0.144819 |
| variance <= 1.7875 and curtosis <= 0.67833 and skewness <= 5.2022 | 1 | 0.080621 |
| variance <= -4.1479 | 1 | 0.047327 |
| variance <= 0.74428 and entropy >= 0.23447 and curtosis <= 6.7807 and skewness <= -0.045533 | 1 | 0.007246 |
| curtosis <= -4.8037 | 1 | 0.003275 |
|  | 0 | 0.997089 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

variance|skewness|curtosis|entropy|class
---|---|---|---|---
(-2.7952--0.4031]|(9.61695-inf)|(-4.42285-8.83885]|all|0
(2.3921-inf)|(9.61695-inf)|(-4.42285-8.83885]|all|0
(0.7651-2.3921]|(9.61695-inf)|(-4.42285-8.83885]|all|0
(-0.4031-0.7651]|(9.61695-inf)|(-4.42285-8.83885]|all|0
(-inf--2.7952]|(-5.62225--2.3021]|(8.83885-inf)|all|1
(-inf--2.7952]|(5.21045-9.61695]|(-4.42285-8.83885]|all|1
(-2.7952--0.4031]|(5.21045-9.61695]|(-4.42285-8.83885]|all|0
(-0.4031-0.7651]|(5.21045-9.61695]|(-4.42285-8.83885]|all|0
(0.7651-2.3921]|(5.21045-9.61695]|(-4.42285-8.83885]|all|0
(2.3921-inf)|(5.21045-9.61695]|(-4.42285-8.83885]|all|0
(-2.7952--0.4031]|(-6.94555--5.62225]|(8.83885-inf)|all|1
(-inf--2.7952]|(-6.94555--5.62225]|(8.83885-inf)|all|1
(-inf--2.7952]|(-2.3021-5.21045]|(-4.42285-8.83885]|all|1
(-2.7952--0.4031]|(-2.3021-5.21045]|(-4.42285-8.83885]|all|1
(2.3921-inf)|(9.61695-inf)|(-inf--4.42285]|all|0
(-0.4031-0.7651]|(-2.3021-5.21045]|(-4.42285-8.83885]|all|1
(2.3921-inf)|(-2.3021-5.21045]|(-4.42285-8.83885]|all|0
(0.7651-2.3921]|(-2.3021-5.21045]|(-4.42285-8.83885]|all|0
(2.3921-inf)|(5.21045-9.61695]|(-inf--4.42285]|all|0
(-2.7952--0.4031]|(-5.62225--2.3021]|(-4.42285-8.83885]|all|1
(-inf--2.7952]|(-inf--6.94555]|(8.83885-inf)|all|1
(-2.7952--0.4031]|(-inf--6.94555]|(8.83885-inf)|all|1
(0.7651-2.3921]|(-5.62225--2.3021]|(-4.42285-8.83885]|all|0
(-0.4031-0.7651]|(-5.62225--2.3021]|(-4.42285-8.83885]|all|0
(2.3921-inf)|(-5.62225--2.3021]|(-4.42285-8.83885]|all|0
(-inf--2.7952]|(-6.94555--5.62225]|(-4.42285-8.83885]|all|0
(2.3921-inf)|(-6.94555--5.62225]|(-4.42285-8.83885]|all|0
(0.7651-2.3921]|(-2.3021-5.21045]|(-inf--4.42285]|all|1
(-0.4031-0.7651]|(-2.3021-5.21045]|(-inf--4.42285]|all|1
(-2.7952--0.4031]|(-6.94555--5.62225]|(-4.42285-8.83885]|all|1
(0.7651-2.3921]|(-6.94555--5.62225]|(-4.42285-8.83885]|all|0
(-inf--2.7952]|(-inf--6.94555]|(-4.42285-8.83885]|all|1
(-2.7952--0.4031]|(-inf--6.94555]|(-4.42285-8.83885]|all|1

## JRip

Decision list:

rules | predicted class
---|---
(variance <= 0.31803) and (skewness <= 5.8333) and (curtosis <= 6.2109)|1 (328.0/2.0)
(variance <= -1.3887) and (skewness <= -4.7428)|1 (116.0/0.0)
(variance <= 1.7875) and (curtosis <= 0.67833) and (skewness <= 5.2022)|1 (64.0/2.0)
(variance <= -4.1479)|1 (36.0/1.0)
(variance <= 0.74428) and (entropy >= 0.23447) and (curtosis <= 6.7807) and (skewness <= -0.045533)|1 (5.0/0.0)
(curtosis <= -4.8037)|1 (4.0/1.0)
|0 (681.0/2.0)


## PART

Decision list:

rules | predicted class
---|---
variance > 0.75896 AND curtosis > -1.8785|0 (379.0)
skewness <= 5.2022 AND variance <= -1.786|1 (242.0/1.0)
skewness > 5.2022 AND variance > -3.3793|0 (250.0)
curtosis <= 0.70403|1 (223.0/3.0)
variance > 0.31803 AND entropy <= 0.66377|0 (25.0)
skewness <= -1.7837|1 (68.0/1.0)
curtosis > 2.9986|0 (26.0)
|1 (21.0)


## J48 Decision Tree

* variance <= 0.31803
	* skewness <= 5.8561
		* curtosis <= 3.0423: 1 (215.0)
		* curtosis > 3.0423
			* skewness <= -1.8624: 1 (137.0)
			* skewness > -1.8624: 0 (20.0/2.0)
	* skewness > 5.8561
		* variance <= -4.3876: 1 (29.0)
		* variance > -4.3876: 0 (64.0)
* variance > 0.31803
	* variance <= 1.7496
		* curtosis <= -2.2563
			* skewness <= 4.8504: 1 (40.0)
			* skewness > 4.8504: 0 (4.0/2.0)
		* curtosis > -2.2563
			* entropy <= 0.12843: 0 (90.0)
			* entropy > 0.12843
				* curtosis <= 0.20792: 1 (10.0)
				* curtosis > 0.20792: 0 (21.0/2.0)
	* variance > 1.7496
		* variance <= 2.1943
			* curtosis <= -2.6848: 1 (4.0/1.0)
			* curtosis > -2.6848: 0 (42.0)
		* variance > 2.1943: 0 (312.0)


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


