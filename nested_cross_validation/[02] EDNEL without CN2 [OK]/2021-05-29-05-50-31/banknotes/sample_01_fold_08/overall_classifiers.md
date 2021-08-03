# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 0 | 0.555105 |
| variance >= 0.320165 and curtosis < -4.38605 and variance < 3.3408 | 1 | 0.040616 |
| variance < 0.320165 and skewness < 7.5653 and variance < -0.38902000000000003 and curtosis >= 6.21865 and skewness < -4.6745 | 1 | 0.145885 |
| variance < 0.320165 and skewness >= 7.5653 and variance < -4.726 | 1 | 0.025605 |
| variance < 0.320165 and skewness < 7.5653 and variance >= -0.38902000000000003 and skewness < 5.45355 and curtosis < 2.6105 | 1 | 0.070556 |
| variance <= 0.31803 and skewness <= 7.5404 and variance <= -1.786 | 1 | 0.274368 |
| variance >= 0.320165 and curtosis >= -4.38605 and variance < 1.5922 and curtosis >= -2.2859 and entropy >= 0.081882 and curtosis < 1.85305 and skewness < 3.5591749999999998 | 1 | 0.021429 |
| variance <= 0.31803 and skewness <= 7.5404 and variance > -1.786 and curtosis <= 6.7807 and skewness <= 3.9213 | 1 | 0.211762 |
| variance >= 0.320165 and curtosis >= -4.38605 and variance >= 1.5922 and variance < 2.03655 and curtosis < -2.6483499999999998 | 1 | 0.003275 |
| variance >= 0.320165 and curtosis >= -4.38605 and variance < 1.5922 and curtosis < -2.2859 and skewness < 5.6574 | 1 | 0.029745 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| variance > 0.31803 and curtosis > -4.3882 and variance > 2.031 | 0 | 0.418432 |
| skewness > 5.2684 and variance > -3.3793 | 0 | 0.240664 |
| variance <= 0.31803 and curtosis <= 3.0423 | 1 | 0.728972 |
| skewness <= -5.1277 and variance <= -0.46651 | 1 | 0.570370 |
| curtosis <= 0.20021 and curtosis <= -1.4938 | 1 | 0.337143 |
| variance > 0.74841 | 0 | 0.717647 |
| entropy <= -0.1276 | 0 | 0.571954 |
| curtosis <= 6.7807 and skewness <= -0.24832 | 1 | 0.463415 |
| variance <= 0.33111 | 0 | 0.775120 |
|  | 0 | 0.444444 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| variance <= 0.2952 and skewness <= 5.8333 and curtosis <= 6.7156 | 1 | 0.327138 |
| variance <= -1.3887 and skewness <= -4.7428 | 1 | 0.135101 |
| variance <= 1.7875 and curtosis <= -2.3437 and skewness <= 5.2022 | 1 | 0.062927 |
| variance <= -4.1479 | 1 | 0.047327 |
| variance <= 0.74428 and entropy >= 0.097399 and curtosis <= 6.7807 and skewness <= 0.99945 | 1 | 0.018962 |
| curtosis <= -1.6506 and skewness <= 4.5565 and variance <= 2.2279 | 1 | 0.012968 |
|  | 0 | 0.998542 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

variance|skewness|curtosis|entropy|class
---|---|---|---|---
(1.7907-2.3921]|(9.61695-inf)|(-4.42285-8.83885]|all|0
(0.320165-1.7907]|(9.61695-inf)|(-4.42285-8.83885]|all|0
(2.3921-inf)|(9.61695-inf)|(-4.42285-8.83885]|all|0
(-2.7952-0.320165]|(9.61695-inf)|(-4.42285-8.83885]|all|0
(1.7907-2.3921]|(5.21045-9.61695]|(-4.42285-8.83885]|all|0
(-2.7952-0.320165]|(5.21045-9.61695]|(-4.42285-8.83885]|all|0
(2.3921-inf)|(5.21045-9.61695]|(-4.42285-8.83885]|all|0
(0.320165-1.7907]|(5.21045-9.61695]|(-4.42285-8.83885]|all|0
(-inf--2.7952]|(-5.62225--2.3021]|(8.83885-inf)|all|1
(-inf--2.7952]|(5.21045-9.61695]|(-4.42285-8.83885]|all|1
(-2.7952-0.320165]|(-6.94555--5.62225]|(8.83885-inf)|all|1
(2.3921-inf)|(9.61695-inf)|(-inf--4.42285]|all|0
(1.7907-2.3921]|(-2.3021-5.21045]|(-4.42285-8.83885]|all|0
(2.3921-inf)|(-2.3021-5.21045]|(-4.42285-8.83885]|all|0
(-inf--2.7952]|(-6.94555--5.62225]|(8.83885-inf)|all|1
(-inf--2.7952]|(-2.3021-5.21045]|(-4.42285-8.83885]|all|1
(-2.7952-0.320165]|(-2.3021-5.21045]|(-4.42285-8.83885]|all|1
(0.320165-1.7907]|(-2.3021-5.21045]|(-4.42285-8.83885]|all|0
(2.3921-inf)|(5.21045-9.61695]|(-inf--4.42285]|all|0
(1.7907-2.3921]|(-5.62225--2.3021]|(-4.42285-8.83885]|all|0
(2.3921-inf)|(-5.62225--2.3021]|(-4.42285-8.83885]|all|0
(0.320165-1.7907]|(-5.62225--2.3021]|(-4.42285-8.83885]|all|0
(-2.7952-0.320165]|(-inf--6.94555]|(8.83885-inf)|all|1
(-2.7952-0.320165]|(-5.62225--2.3021]|(-4.42285-8.83885]|all|1
(-inf--2.7952]|(-inf--6.94555]|(8.83885-inf)|all|1
(2.3921-inf)|(-6.94555--5.62225]|(-4.42285-8.83885]|all|0
(-inf--2.7952]|(-6.94555--5.62225]|(-4.42285-8.83885]|all|0
(1.7907-2.3921]|(-6.94555--5.62225]|(-4.42285-8.83885]|all|0
(0.320165-1.7907]|(-6.94555--5.62225]|(-4.42285-8.83885]|all|0
(1.7907-2.3921]|(-2.3021-5.21045]|(-inf--4.42285]|all|1
(0.320165-1.7907]|(-2.3021-5.21045]|(-inf--4.42285]|all|1
(-2.7952-0.320165]|(-2.3021-5.21045]|(-inf--4.42285]|all|1
(-2.7952-0.320165]|(-6.94555--5.62225]|(-4.42285-8.83885]|all|1
(-inf--2.7952]|(-inf--6.94555]|(-4.42285-8.83885]|all|1
(-2.7952-0.320165]|(-inf--6.94555]|(-4.42285-8.83885]|all|1

## JRip

Decision list:

rules | predicted class
---|---
(variance <= 0.2952) and (skewness <= 5.8333) and (curtosis <= 6.7156)|1 (339.0/3.0)
(variance <= -1.3887) and (skewness <= -4.7428)|1 (107.0/0.0)
(variance <= 1.7875) and (curtosis <= -2.3437) and (skewness <= 5.2022)|1 (46.0/0.0)
(variance <= -4.1479)|1 (36.0/1.0)
(variance <= 0.74428) and (entropy >= 0.097399) and (curtosis <= 6.7807) and (skewness <= 0.99945)|1 (16.0/1.0)
(curtosis <= -1.6506) and (skewness <= 4.5565) and (variance <= 2.2279)|1 (9.0/0.0)
|0 (681.0/1.0)


## PART

Decision list:

rules | predicted class
---|---
variance > 0.31803 AND curtosis > -4.3882 AND variance > 2.031|0 (395.0)
skewness > 5.2684 AND variance > -3.3793|0 (174.0)
variance <= 0.31803 AND curtosis <= 3.0423|1 (312.0)
skewness <= -5.1277 AND variance <= -0.46651|1 (154.0)
curtosis <= 0.20021 AND curtosis <= -1.4938|1 (59.0)
variance > 0.74841|0 (61.0)
entropy <= -0.1276|0 (34.0/1.0)
curtosis <= 6.7807 AND skewness <= -0.24832|1 (19.0)
variance <= 0.33111|0 (18.0)
|0 (8.0/4.0)


## J48 Decision Tree

* variance <= 0.31803
	* skewness <= 7.5404
		* variance <= -1.786: 1 (261.0/1.0)
		* variance > -1.786
			* curtosis <= 6.7807
				* skewness <= 3.9213: 1 (188.0/2.0)
				* skewness > 3.9213
					* curtosis <= -3.521: 1 (4.0)
					* curtosis > -3.521: 0 (8.0)
			* curtosis > 6.7807
				* skewness <= -5.554: 1 (14.0/1.0)
				* skewness > -5.554: 0 (19.0)
	* skewness > 7.5404
		* variance <= -4.7331: 1 (18.0)
		* variance > -4.7331: 0 (75.0)
* variance > 0.31803
	* curtosis <= -4.3882
		* skewness <= 7.1907: 1 (29.0)
		* skewness > 7.1907: 0 (7.0)
	* curtosis > -4.3882
		* variance <= 2.031
			* curtosis <= -1.7542
				* skewness <= 5.6222: 1 (29.0)
				* skewness > 5.6222: 0 (14.0)
			* curtosis > -1.7542
				* entropy <= 0.12585: 0 (129.0)
				* entropy > 0.12585
					* variance <= 0.77805
						* curtosis <= 1.9507: 1 (10.0)
						* curtosis > 1.9507: 0 (5.0)
					* variance > 0.77805: 0 (29.0)
		* variance > 2.031: 0 (395.0)


## SimpleCart Decision Tree

* variance < 0.320165
	* skewness < 7.5653
		* variance < -0.38902000000000003
			* curtosis < 6.21865: 1(292.0/0.0)
			* curtosis >= 6.21865
				* skewness < -4.6745: 1(117.0/0.0)
				* skewness >= -4.6745
					* variance < -2.1171: 0(1.0/1.0)
					* variance >= -2.1171: 0(15.0/0.0)
		* variance >= -0.38902000000000003
			* skewness < 5.45355
				* curtosis < 2.6105: 1(52.0/0.0)
				* curtosis >= 2.6105: 0(8.0/1.0)
			* skewness >= 5.45355: 0(7.0/0.0)
	* skewness >= 7.5653
		* variance < -4.726: 1(18.0/0.0)
		* variance >= -4.726: 0(75.0/0.0)
* variance >= 0.320165
	* curtosis < -4.38605
		* variance < 3.3408: 1(29.0/0.0)
		* variance >= 3.3408: 0(7.0/0.0)
	* curtosis >= -4.38605
		* variance < 1.5922
			* curtosis < -2.2859
				* skewness < 5.6574: 1(21.0/0.0)
				* skewness >= 5.6574: 0(3.0/0.0)
			* curtosis >= -2.2859
				* entropy < 0.081882: 0(110.0/0.0)
				* entropy >= 0.081882
					* curtosis < 1.85305
						* skewness < 3.5591749999999998: 1(15.0/0.0)
						* skewness >= 3.5591749999999998: 0(2.0/0.0)
					* curtosis >= 1.85305: 0(15.0/0.0)
		* variance >= 1.5922
			* variance < 2.03655
				* curtosis < -2.6483499999999998: 1(3.0/1.0)
				* curtosis >= -2.6483499999999998: 0(46.0/0.0)
			* variance >= 2.03655: 0(395.0/0.0)


