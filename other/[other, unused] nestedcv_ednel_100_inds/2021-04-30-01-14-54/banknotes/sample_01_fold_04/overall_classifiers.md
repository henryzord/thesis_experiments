# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 0 | 0.555105 |
| variance >= 0.321235 and curtosis >= -4.38605 and variance >= 1.5922 and variance < 2.03655 and curtosis < -2.11625 | 1 | 0.003275 |
| variance > 0.321235 and variance <= 2.3921 and curtosis <= -2.2722 and skewness <= 6.41995 | 1 | 0.071816 |
| variance < 0.321235 and skewness < 7.5653 and variance < -0.4031 and curtosis >= 6.21565 and skewness < -4.6745 | 1 | 0.145885 |
| variance <= 0.321235 and skewness <= 5.86535 and curtosis <= 3.0642 | 1 | 0.287942 |
| variance > 0.321235 and variance <= 2.3921 and curtosis > -2.2722 and entropy > 0.092227 and curtosis > -0.17937 and variance <= 0.691345 | 1 | 0.002624 |
| variance <= 0.321235 and skewness <= 5.86535 and curtosis > 3.0642 and skewness <= -1.81995 | 1 | 0.194145 |
| variance > 0.321235 and variance <= 2.3921 and curtosis > -2.2722 and entropy > 0.092227 and curtosis <= -0.17937 | 1 | 0.015805 |
| variance < 0.321235 and skewness >= 7.5653 and variance < -4.726 | 1 | 0.025605 |
| variance < 0.321235 and skewness < 7.5653 and variance < -0.4031 and curtosis < 6.21565 and skewness >= 7.293150000000001 | 1 | 0.003275 |
| variance <= 0.321235 and skewness > 5.86535 and variance <= -3.4449 | 1 | 0.047327 |
| variance < 0.321235 and skewness < 7.5653 and variance < -0.4031 and curtosis < 6.21565 and skewness < 7.293150000000001 | 1 | 0.297436 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| variance > 0.31803 and variance > 2.3917 | 0 | 0.396040 |
| skewness > 5.2808 and variance > -3.3793 | 0 | 0.251023 |
| variance <= 0.31803 and curtosis <= 3.0423 | 1 | 0.688742 |
| variance <= -1.3968 and skewness <= -1.4733 | 1 | 0.508711 |
| curtosis > -0.17594 and variance > -0.37013 and curtosis > 1.8076 | 0 | 0.530928 |
| curtosis <= -1.3927 | 1 | 0.616162 |
| skewness > -0.045533 and curtosis > -0.23592 | 0 | 0.531250 |
| entropy > -0.23105 | 1 | 0.879765 |
|  | 0 | 1.000000 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

variance|skewness|curtosis|entropy|class
---|---|---|---|---
(-0.4031-0.321235]|(9.6242-inf)|(-4.42285-8.83885]|all|0
(0.321235-1.74385]|(9.6242-inf)|(-4.42285-8.83885]|all|0
(1.74385-2.3921]|(9.6242-inf)|(-4.42285-8.83885]|all|0
(-2.7571--0.4031]|(9.6242-inf)|(-4.42285-8.83885]|all|0
(2.3921-inf)|(9.6242-inf)|(-4.42285-8.83885]|all|0
(-2.7571--0.4031]|(5.21045-9.6242]|(-4.42285-8.83885]|all|0
(1.74385-2.3921]|(5.21045-9.6242]|(-4.42285-8.83885]|all|0
(-0.4031-0.321235]|(5.21045-9.6242]|(-4.42285-8.83885]|all|0
(0.321235-1.74385]|(5.21045-9.6242]|(-4.42285-8.83885]|all|0
(2.3921-inf)|(5.21045-9.6242]|(-4.42285-8.83885]|all|0
(-inf--2.7571]|(-5.62225--2.4149]|(8.83885-inf)|all|1
(-inf--2.7571]|(5.21045-9.6242]|(-4.42285-8.83885]|all|1
(2.3921-inf)|(9.6242-inf)|(-inf--4.42285]|all|0
(2.3921-inf)|(-2.4149-5.21045]|(-4.42285-8.83885]|all|0
(-2.7571--0.4031]|(-6.94555--5.62225]|(8.83885-inf)|all|1
(1.74385-2.3921]|(-2.4149-5.21045]|(-4.42285-8.83885]|all|0
(-0.4031-0.321235]|(-2.4149-5.21045]|(-4.42285-8.83885]|all|1
(-inf--2.7571]|(-6.94555--5.62225]|(8.83885-inf)|all|1
(0.321235-1.74385]|(-2.4149-5.21045]|(-4.42285-8.83885]|all|0
(-inf--2.7571]|(-2.4149-5.21045]|(-4.42285-8.83885]|all|1
(-2.7571--0.4031]|(-2.4149-5.21045]|(-4.42285-8.83885]|all|1
(2.3921-inf)|(5.21045-9.6242]|(-inf--4.42285]|all|0
(1.74385-2.3921]|(-5.62225--2.4149]|(-4.42285-8.83885]|all|0
(2.3921-inf)|(-5.62225--2.4149]|(-4.42285-8.83885]|all|0
(0.321235-1.74385]|(-5.62225--2.4149]|(-4.42285-8.83885]|all|0
(-0.4031-0.321235]|(-5.62225--2.4149]|(-4.42285-8.83885]|all|1
(-2.7571--0.4031]|(-inf--6.94555]|(8.83885-inf)|all|1
(-2.7571--0.4031]|(-5.62225--2.4149]|(-4.42285-8.83885]|all|1
(-inf--2.7571]|(-inf--6.94555]|(8.83885-inf)|all|1
(-0.4031-0.321235]|(-6.94555--5.62225]|(-4.42285-8.83885]|all|0
(0.321235-1.74385]|(-6.94555--5.62225]|(-4.42285-8.83885]|all|0
(-inf--2.7571]|(-6.94555--5.62225]|(-4.42285-8.83885]|all|1
(1.74385-2.3921]|(-2.4149-5.21045]|(-inf--4.42285]|all|1
(1.74385-2.3921]|(-6.94555--5.62225]|(-4.42285-8.83885]|all|0
(0.321235-1.74385]|(-2.4149-5.21045]|(-inf--4.42285]|all|1
(-0.4031-0.321235]|(-2.4149-5.21045]|(-inf--4.42285]|all|1
(-2.7571--0.4031]|(-6.94555--5.62225]|(-4.42285-8.83885]|all|1
(-inf--2.7571]|(-inf--6.94555]|(-4.42285-8.83885]|all|1
(-2.7571--0.4031]|(-inf--6.94555]|(-4.42285-8.83885]|all|1

## PART

Decision list:

rules | predicted class
---|---
variance > 0.31803 AND variance > 2.3917|0 (360.0)
skewness > 5.2808 AND variance > -3.3793|0 (184.0)
variance <= 0.31803 AND curtosis <= 3.0423|1 (312.0)
variance <= -1.3968 AND skewness <= -1.4733|1 (146.0)
curtosis > -0.17594 AND variance > -0.37013 AND curtosis > 1.8076|0 (103.0)
curtosis <= -1.3927|1 (61.0)
skewness > -0.045533 AND curtosis > -0.23592|0 (34.0)
entropy > -0.23105|1 (31.0/1.0)
|0 (3.0)


## J48 Decision Tree

* variance <= 0.321235
	* skewness <= 5.86535
		* curtosis <= 3.0642: 1 (277.0)
		* curtosis > 3.0642
			* skewness <= -1.81995: 1 (169.0/2.0)
			* skewness > -1.81995: 0 (25.0/2.0)
	* skewness > 5.86535
		* variance <= -3.4449: 1 (36.0/1.0)
		* variance > -3.4449: 0 (87.0)
* variance > 0.321235
	* variance <= 2.3921
		* curtosis <= -2.2722
			* skewness <= 6.41995: 1 (53.0)
			* skewness > 6.41995: 0 (8.0)
		* curtosis > -2.2722
			* entropy <= 0.092227: 0 (162.0/1.0)
			* entropy > 0.092227
				* curtosis <= -0.17937: 1 (11.0)
				* curtosis > -0.17937
					* variance <= 0.691345: 1 (5.0/2.0)
					* variance > 0.691345: 0 (41.0)
	* variance > 2.3921: 0 (360.0)


## SimpleCart Decision Tree

* variance < 0.321235
	* skewness < 7.5653
		* variance < -0.4031
			* curtosis < 6.21565
				* skewness < 7.293150000000001: 1(290.0/0.0)
				* skewness >= 7.293150000000001: 1(3.0/1.0)
			* curtosis >= 6.21565
				* skewness < -4.6745: 1(117.0/0.0)
				* skewness >= -4.6745: 0(14.0/1.0)
		* variance >= -0.4031
			* skewness < 5.45355
				* curtosis < 2.62465: 1(51.0/0.0)
				* curtosis >= 2.62465: 0(11.0/1.0)
			* skewness >= 5.45355: 0(10.0/0.0)
	* skewness >= 7.5653
		* variance < -4.726: 1(18.0/0.0)
		* variance >= -4.726: 0(77.0/0.0)
* variance >= 0.321235
	* curtosis < -4.38605
		* variance < 3.30405: 1(28.0/0.0)
		* variance >= 3.30405: 0(9.0/0.0)
	* curtosis >= -4.38605
		* variance < 1.5922
			* curtosis < -2.2721999999999998
				* skewness < 5.6667: 1(22.0/0.0)
				* skewness >= 5.6667: 0(3.0/0.0)
			* curtosis >= -2.2721999999999998
				* entropy < 0.0353305
					* variance < 0.450925: 0(15.0/1.0)
					* variance >= 0.450925: 0(94.0/0.0)
				* entropy >= 0.0353305
					* skewness < 1.647125
						* curtosis < 1.952: 1(14.0/0.0)
						* curtosis >= 1.952: 0(2.0/0.0)
					* skewness >= 1.647125: 0(14.0/0.0)
		* variance >= 1.5922
			* variance < 2.03655
				* curtosis < -2.11625: 1(3.0/1.0)
				* curtosis >= -2.11625: 0(48.0/0.0)
			* variance >= 2.03655: 0(386.0/0.0)


