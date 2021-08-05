# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 0 | 0.555105 |
| variance < 0.311555 and skewness < 7.76395 and variance < -0.458565 and curtosis < 6.21865 and skewness >= 7.293150000000001 | 1 | 0.004651 |
| variance >= 0.311555 and curtosis >= -4.38605 and variance < 1.5922 and curtosis >= -2.2721999999999998 and entropy >= 0.081882 and curtosis < 1.85305 and skewness < 3.5591749999999998 | 1 | 0.022825 |
| variance <= 0.75422 and skewness <= 5.0708 and curtosis <= 0.747325 | 1 | 0.243929 |
| variance >= 0.311555 and curtosis >= -4.38605 and variance < 1.5922 and curtosis < -2.2721999999999998 and skewness < 5.6667 | 1 | 0.029745 |
| variance > 0.75422 and variance > 1.7438500000000001 and variance <= 2.22845 and curtosis <= -2.06785 | 1 | 0.005191 |
| variance < 0.311555 and skewness < 7.76395 and variance >= -0.458565 and curtosis >= 0.297461 and entropy >= 0.91334 | 1 | 0.007246 |
| variance < 0.311555 and skewness >= 7.76395 and variance < -4.726 | 1 | 0.024217 |
| variance < 0.311555 and skewness < 7.76395 and variance >= -0.458565 and curtosis >= 0.297461 and entropy < 0.91334 and skewness < -0.672525 and curtosis < 4.2440999999999995 | 1 | 0.005806 |
| variance <= 0.75422 and skewness > 5.0708 and variance <= -3.36765 | 1 | 0.049967 |
| variance < 0.311555 and skewness < 7.76395 and variance < -0.458565 and curtosis >= 6.21865 and skewness < -4.6745 | 1 | 0.144819 |
| variance >= 0.311555 and curtosis < -4.38605 and variance < 3.22215 | 1 | 0.040616 |
| variance > 0.75422 and variance <= 1.7438500000000001 and curtosis <= -2.2859 | 1 | 0.042123 |
| variance < 0.311555 and skewness < 7.76395 and variance < -0.458565 and curtosis < 6.21865 and skewness < 7.293150000000001 | 1 | 0.292355 |
| variance <= 0.75422 and skewness <= 5.0708 and curtosis > 0.747325 and variance <= -0.49481 and skewness <= -0.0144945 | 1 | 0.242262 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| variance > 0.75422 and variance > 2.22845 | 0 | 0.405844 |
| skewness > 5.1608 and variance > -3.36765 | 0 | 0.251031 |
| variance <= 0.311555 and curtosis <= 3.0642 | 1 | 0.712644 |
| variance <= -0.49481 and skewness <= -0.351787 | 1 | 0.573399 |
| curtosis > 0.20578 | 0 | 0.633879 |
|  | 1 | 0.985915 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| skewness <= 7.6584 and variance <= -1.7549 | 1 | 0.276667 |
| variance <= 0.63655 and skewness <= 5.2022 and curtosis <= 0.18307 | 1 | 0.167679 |
| variance <= -0.539 and skewness <= -0.31247 | 1 | 0.090324 |
| variance <= 1.7875 and curtosis <= -2.3 and skewness <= 4.8731 | 1 | 0.052559 |
| variance <= -5.3857 | 1 | 0.022825 |
| variance <= 1.4378 and entropy >= 0.23447 and curtosis <= 2.135 and skewness <= 0.66837 | 1 | 0.025605 |
| curtosis <= -1.9702 and skewness <= 1.852 | 1 | 0.004360 |
|  | 0 | 0.994194 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

variance|skewness|curtosis|entropy|class
---|---|---|---|---
(0.75422-2.22845]|(9.61695-inf)|(-4.38605-8.83885]|all|0
(-0.403365-0.75422]|(9.61695-inf)|(-4.38605-8.83885]|all|0
(-2.7952--0.403365]|(9.61695-inf)|(-4.38605-8.83885]|all|0
(2.22845-inf)|(9.61695-inf)|(-4.38605-8.83885]|all|0
(-2.7952--0.403365]|(5.21045-9.61695]|(-4.38605-8.83885]|all|0
(-inf--2.7952]|(5.21045-9.61695]|(-4.38605-8.83885]|all|1
(0.75422-2.22845]|(5.21045-9.61695]|(-4.38605-8.83885]|all|0
(-0.403365-0.75422]|(5.21045-9.61695]|(-4.38605-8.83885]|all|0
(2.22845-inf)|(5.21045-9.61695]|(-4.38605-8.83885]|all|0
(-2.7952--0.403365]|(-6.8814--4.9818]|(8.83885-inf)|all|1
(2.22845-inf)|(9.61695-inf)|(-inf--4.38605]|all|0
(-inf--2.7952]|(-6.8814--4.9818]|(8.83885-inf)|all|1
(-inf--2.7952]|(-2.3021-5.21045]|(-4.38605-8.83885]|all|1
(-2.7952--0.403365]|(-2.3021-5.21045]|(-4.38605-8.83885]|all|1
(2.22845-inf)|(-2.3021-5.21045]|(-4.38605-8.83885]|all|0
(-0.403365-0.75422]|(-2.3021-5.21045]|(-4.38605-8.83885]|all|1
(0.75422-2.22845]|(-2.3021-5.21045]|(-4.38605-8.83885]|all|0
(2.22845-inf)|(5.21045-9.61695]|(-inf--4.38605]|all|0
(-2.7952--0.403365]|(-inf--6.8814]|(8.83885-inf)|all|1
(-2.7952--0.403365]|(-4.9818--2.3021]|(-4.38605-8.83885]|all|1
(-inf--2.7952]|(-inf--6.8814]|(8.83885-inf)|all|1
(-0.403365-0.75422]|(-4.9818--2.3021]|(-4.38605-8.83885]|all|0
(0.75422-2.22845]|(-4.9818--2.3021]|(-4.38605-8.83885]|all|0
(2.22845-inf)|(-4.9818--2.3021]|(-4.38605-8.83885]|all|0
(-inf--2.7952]|(-6.8814--4.9818]|(-4.38605-8.83885]|all|0
(-0.403365-0.75422]|(-6.8814--4.9818]|(-4.38605-8.83885]|all|0
(0.75422-2.22845]|(-6.8814--4.9818]|(-4.38605-8.83885]|all|0
(2.22845-inf)|(-6.8814--4.9818]|(-4.38605-8.83885]|all|0
(0.75422-2.22845]|(-2.3021-5.21045]|(-inf--4.38605]|all|1
(-0.403365-0.75422]|(-2.3021-5.21045]|(-inf--4.38605]|all|1
(-2.7952--0.403365]|(-6.8814--4.9818]|(-4.38605-8.83885]|all|1
(-inf--2.7952]|(-inf--6.8814]|(-4.38605-8.83885]|all|0
(-2.7952--0.403365]|(-inf--6.8814]|(-4.38605-8.83885]|all|1

## JRip

Decision list:

rules | predicted class
---|---
(skewness <= 7.6584) and (variance <= -1.7549)|1 (264.0/1.0)
(variance <= 0.63655) and (skewness <= 5.2022) and (curtosis <= 0.18307)|1 (138.0/0.0)
(variance <= -0.539) and (skewness <= -0.31247)|1 (70.0/1.0)
(variance <= 1.7875) and (curtosis <= -2.3) and (skewness <= 4.8731)|1 (38.0/0.0)
(variance <= -5.3857)|1 (16.0/0.0)
(variance <= 1.4378) and (entropy >= 0.23447) and (curtosis <= 2.135) and (skewness <= 0.66837)|1 (18.0/0.0)
(curtosis <= -1.9702) and (skewness <= 1.852)|1 (3.0/0.0)
|0 (687.0/4.0)


## PART

Decision list:

rules | predicted class
---|---
variance > 0.75422 AND variance > 2.22845|0 (375.0)
skewness > 5.1608 AND variance > -3.36765|0 (186.0/1.0)
variance <= 0.311555 AND curtosis <= 3.0642|1 (310.0)
variance <= -0.49481 AND skewness <= -0.351787|1 (170.0/1.0)
curtosis > 0.20578|0 (126.0/3.0)
|1 (67.0/1.0)


## J48 Decision Tree

* variance <= 0.75422
	* skewness <= 5.0708
		* curtosis <= 0.747325: 1 (190.0)
		* curtosis > 0.747325
			* variance <= -0.49481
				* skewness <= -0.0144945: 1 (198.0/1.0)
				* skewness > -0.0144945
					* curtosis <= 4.462149999999999: 1 (16.0)
					* curtosis > 4.462149999999999: 0 (11.0)
			* variance > -0.49481: 0 (41.0/11.0)
	* skewness > 5.0708
		* variance <= -3.36765: 1 (33.0/1.0)
		* variance > -3.36765: 0 (99.0/1.0)
* variance > 0.75422
	* variance <= 1.7438500000000001
		* curtosis <= -2.2859: 1 (30.0/2.0)
		* curtosis > -2.2859: 0 (80.0/2.0)
	* variance > 1.7438500000000001
		* variance <= 2.22845
			* curtosis <= -2.06785: 1 (5.0/2.0)
			* curtosis > -2.06785: 0 (50.0)
		* variance > 2.22845: 0 (327.0)


## SimpleCart Decision Tree

* variance < 0.311555
	* skewness < 7.76395
		* variance < -0.458565
			* curtosis < 6.21865
				* skewness < 7.293150000000001: 1(283.0/0.0)
				* skewness >= 7.293150000000001: 1(4.0/1.0)
			* curtosis >= 6.21865
				* skewness < -4.6745: 1(116.0/0.0)
				* skewness >= -4.6745
					* variance < -2.09525: 0(1.0/1.0)
					* variance >= -2.09525: 0(12.0/0.0)
		* variance >= -0.458565
			* curtosis < 0.297461
				* skewness < 5.63155: 1(49.0/0.0)
				* skewness >= 5.63155: 0(3.0/0.0)
			* curtosis >= 0.297461
				* entropy < 0.91334
					* skewness < -0.672525
						* curtosis < 4.2440999999999995: 1(4.0/0.0)
						* curtosis >= 4.2440999999999995: 0(6.0/0.0)
					* skewness >= -0.672525: 0(13.0/0.0)
				* entropy >= 0.91334: 1(5.0/0.0)
	* skewness >= 7.76395
		* variance < -4.726: 1(17.0/0.0)
		* variance >= -4.726: 0(80.0/0.0)
* variance >= 0.311555
	* curtosis < -4.38605
		* variance < 3.22215: 1(29.0/0.0)
		* variance >= 3.22215: 0(9.0/0.0)
	* curtosis >= -4.38605
		* variance < 1.5922
			* curtosis < -2.2721999999999998
				* skewness < 5.6667: 1(21.0/0.0)
				* skewness >= 5.6667: 0(2.0/0.0)
			* curtosis >= -2.2721999999999998
				* entropy < 0.081882
					* variance < 0.42002: 0(14.0/1.0)
					* variance >= 0.42002: 0(88.0/0.0)
				* entropy >= 0.081882
					* curtosis < 1.85305
						* skewness < 3.5591749999999998: 1(16.0/0.0)
						* skewness >= 3.5591749999999998: 0(2.0/0.0)
					* curtosis >= 1.85305: 0(17.0/0.0)
		* variance >= 1.5922
			* variance < 2.03655
				* curtosis < -2.6483499999999998: 1(3.0/1.0)
				* curtosis >= -2.6483499999999998: 0(49.0/0.0)
			* variance >= 2.03655: 0(387.0/0.0)


