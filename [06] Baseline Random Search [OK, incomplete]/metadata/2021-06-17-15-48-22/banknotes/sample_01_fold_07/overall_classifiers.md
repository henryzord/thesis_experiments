# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| variance >= 0.320165 and curtosis >= -4.4434000000000005 and variance >= 1.5922 and variance >= 2.03655 | 0 | 0.420275 |
| variance < 0.320165 and skewness < 7.5653 and variance < -0.458565 and curtosis < 6.21865 | 1 | 0.293515 |
| variance > 0.75896 and curtosis > -1.8785 | 0 | 0.409042 |
| variance <= 0.75896 and skewness <= 5.3449 and variance <= 0.31803 and curtosis > 3.0423 and skewness <= -1.8624 | 1 | 0.194843 |
| variance <= 0.75896 and skewness > 5.3449 and variance > -3.3793 | 0 | 0.154083 |
| variance <= 0.75896 and skewness <= 5.3449 and variance <= 0.31803 and curtosis <= 3.0423 | 1 | 0.285417 |
| variance > 0.75896 and curtosis <= -1.8785 and skewness <= 4.9228 | 1 | 0.050000 |
| variance <= 0.75896 and skewness <= 5.3449 and variance > 0.31803 and curtosis > 0.46583 and entropy <= 0.66377 | 0 | 0.043554 |
| variance <= 0.75896 and skewness <= 5.3449 and variance > 0.31803 and curtosis <= 0.46583 | 1 | 0.040559 |
| variance <= 0.75896 and skewness <= 5.3449 and variance <= 0.31803 and curtosis > 3.0423 and skewness > -1.8624 | 0 | 0.038798 |
| variance > 0.75896 and curtosis <= -1.8785 and skewness > 4.9228 | 0 | 0.215714 |
| variance < 0.320165 and skewness >= 7.5653 and variance < -4.726 | 1 | 0.025568 |
| variance >= 0.320165 and curtosis >= -4.4434000000000005 and variance < 1.5922 and curtosis >= -2.2721999999999998 and entropy >= 0.22994 and curtosis < 1.91945 | 1 | 0.018935 |
| variance < 0.320165 and skewness < 7.5653 and variance < -0.458565 and curtosis >= 6.21865 and skewness >= -4.6745 | 0 | 0.024867 |
| variance < 0.320165 and skewness >= 7.5653 and variance >= -4.726 | 0 | 0.115942 |
| variance >= 0.320165 and curtosis >= -4.4434000000000005 and variance < 1.5922 and curtosis >= -2.2721999999999998 and entropy >= 0.22994 and curtosis >= 1.91945 | 0 | 0.024867 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| variance > 0.7651 and curtosis > -1.8648 | 0 | 0.409042 |
| skewness <= 5.21045 and variance <= -1.78205 | 1 | 0.439568 |
| skewness > 5.21045 and variance > -3.36765 | 0 | 0.448029 |
| curtosis <= 0.7216 | 1 | 0.795020 |
| variance <= 0.320165 and skewness <= -1.7806 | 1 | 0.533460 |
| curtosis > 3.0068 | 0 | 0.651515 |
| variance <= 0.32457 | 1 | 0.606061 |
|  | 0 | 0.812500 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| variance <= 0.31803 and skewness <= 5.1401 and curtosis <= 6.2169 | 1 | 0.320804 |
| variance <= -1.3887 and skewness <= -4.7428 | 1 | 0.143571 |
| variance <= 1.7425 and curtosis <= 0.67833 and skewness <= 5.2022 | 1 | 0.079280 |
| variance <= -3.9934 | 1 | 0.048581 |
| skewness <= -7.4473 | 1 | 0.002907 |
| curtosis <= -4.8037 | 1 | 0.004644 |
| skewness <= 1.852 and curtosis <= -2.9581 | 1 | 0.002907 |
| entropy >= 0.74524 and variance <= 0.74428 and variance >= 0.37637 | 1 | 0.004354 |
|  | 0 | 1.000000 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

variance|skewness|curtosis|class
---|---|---|---
(-0.4031-0.7651]|(9.61695-inf)|(-4.42285-8.83885]|0
(-2.7952--0.4031]|(9.61695-inf)|(-4.42285-8.83885]|0
(0.7651-2.3921]|(9.61695-inf)|(-4.42285-8.83885]|0
(2.3921-inf)|(9.61695-inf)|(-4.42285-8.83885]|0
(-inf--2.7952]|(-5.62225--2.3021]|(8.83885-inf)|1
(-2.7952--0.4031]|(5.21045-9.61695]|(-4.42285-8.83885]|0
(-inf--2.7952]|(5.21045-9.61695]|(-4.42285-8.83885]|1
(-0.4031-0.7651]|(5.21045-9.61695]|(-4.42285-8.83885]|0
(0.7651-2.3921]|(5.21045-9.61695]|(-4.42285-8.83885]|0
(2.3921-inf)|(5.21045-9.61695]|(-4.42285-8.83885]|0
(-2.7952--0.4031]|(-6.94555--5.62225]|(8.83885-inf)|1
(-inf--2.7952]|(-2.3021-5.21045]|(-4.42285-8.83885]|1
(-inf--2.7952]|(-6.94555--5.62225]|(8.83885-inf)|1
(2.3921-inf)|(9.61695-inf)|(-inf--4.42285]|0
(-2.7952--0.4031]|(-2.3021-5.21045]|(-4.42285-8.83885]|1
(2.3921-inf)|(-2.3021-5.21045]|(-4.42285-8.83885]|0
(0.7651-2.3921]|(-2.3021-5.21045]|(-4.42285-8.83885]|0
(-0.4031-0.7651]|(-2.3021-5.21045]|(-4.42285-8.83885]|1
(2.3921-inf)|(5.21045-9.61695]|(-inf--4.42285]|0
(-2.7952--0.4031]|(-inf--6.94555]|(8.83885-inf)|1
(-2.7952--0.4031]|(-5.62225--2.3021]|(-4.42285-8.83885]|1
(-inf--2.7952]|(-inf--6.94555]|(8.83885-inf)|1
(-0.4031-0.7651]|(-5.62225--2.3021]|(-4.42285-8.83885]|0
(0.7651-2.3921]|(-5.62225--2.3021]|(-4.42285-8.83885]|0
(2.3921-inf)|(-5.62225--2.3021]|(-4.42285-8.83885]|0
(2.3921-inf)|(-6.94555--5.62225]|(-4.42285-8.83885]|0
(0.7651-2.3921]|(-6.94555--5.62225]|(-4.42285-8.83885]|0
(-inf--2.7952]|(-6.94555--5.62225]|(-4.42285-8.83885]|0
(-0.4031-0.7651]|(-2.3021-5.21045]|(-inf--4.42285]|1
(0.7651-2.3921]|(-2.3021-5.21045]|(-inf--4.42285]|1
(-2.7952--0.4031]|(-6.94555--5.62225]|(-4.42285-8.83885]|1
(-inf--2.7952]|(-inf--6.94555]|(-4.42285-8.83885]|1
(-2.7952--0.4031]|(-inf--6.94555]|(-4.42285-8.83885]|1

## JRip

Decision list:

rules | predicted class
---|---
(variance <= 0.31803) and (skewness <= 5.1401) and (curtosis <= 6.2169)|1 (328.0/2.0)
(variance <= -1.3887) and (skewness <= -4.7428)|1 (115.0/0.0)
(variance <= 1.7425) and (curtosis <= 0.67833) and (skewness <= 5.2022)|1 (63.0/2.0)
(variance <= -3.9934)|1 (37.0/1.0)
(skewness <= -7.4473)|1 (2.0/0.0)
(curtosis <= -4.8037)|1 (5.0/1.0)
(skewness <= 1.852) and (curtosis <= -2.9581)|1 (2.0/0.0)
(entropy >= 0.74524) and (variance <= 0.74428) and (variance >= 0.37637)|1 (3.0/0.0)
|0 (680.0/0.0)


## PART

Decision list:

rules | predicted class
---|---
variance > 0.7651 AND curtosis > -1.8648|0 (380.0)
skewness <= 5.21045 AND variance <= -1.78205|1 (242.0/1.0)
skewness > 5.21045 AND variance > -3.36765|0 (250.0)
curtosis <= 0.7216|1 (223.0/3.0)
variance <= 0.320165 AND skewness <= -1.7806|1 (66.0/1.0)
curtosis > 3.0068|0 (41.0)
variance <= 0.32457|1 (20.0)
|0 (13.0/3.0)


## J48 Decision Tree

* variance <= 0.75896
	* skewness <= 5.3449
		* variance <= 0.31803
			* curtosis <= 3.0423: 1 (274.0)
			* curtosis > 3.0423
				* skewness <= -1.8624: 1 (168.0/1.0)
				* skewness > -1.8624: 0 (26.0/2.0)
		* variance > 0.31803
			* curtosis <= 0.46583: 1 (29.0)
			* curtosis > 0.46583
				* entropy <= 0.66377: 0 (25.0)
				* entropy > 0.66377: 1 (5.0/2.0)
	* skewness > 5.3449
		* variance <= -3.3793: 1 (37.0/1.0)
		* variance > -3.3793: 0 (100.0)
* variance > 0.75896
	* curtosis <= -1.8785
		* skewness <= 4.9228: 1 (40.0/2.0)
		* skewness > 4.9228: 0 (151.0)
	* curtosis > -1.8785: 0 (380.0)


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
				* entropy < 0.22994
					* variance < 0.42002: 0(13.0/2.0)
					* variance >= 0.42002: 0(93.0/0.0)
				* entropy >= 0.22994
					* curtosis < 1.91945: 1(15.0/2.0)
					* curtosis >= 1.91945: 0(14.0/0.0)
		* variance >= 1.5922
			* variance < 2.03655: 0(49.0/3.0)
			* variance >= 2.03655: 0(398.0/0.0)


