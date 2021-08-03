# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 0 | 0.555105 |
| variance <= 0.321235 and skewness <= 5.86535 and curtosis <= 3.0642 | 1 | 0.287942 |
| variance <= 0.321235 and skewness > 5.86535 and variance <= -3.4449 and variance <= -4.4223 | 1 | 0.045961 |
| variance <= 0.321235 and skewness <= 5.86535 and curtosis > 3.0642 and skewness > -1.81995 and variance <= -1.75625 | 1 | 0.001944 |
| variance <= 0.321235 and skewness <= 5.86535 and curtosis > 3.0642 and skewness <= -1.81995 and variance <= -0.684375 | 1 | 0.189349 |
| variance > 0.321235 and variance <= 2.3921 and curtosis > -2.2722 and entropy > 0.092227 and curtosis <= -0.17937 | 1 | 0.015805 |
| variance <= 0.321235 and skewness <= 5.86535 and curtosis > 3.0642 and skewness <= -1.81995 and variance > -0.684375 and curtosis <= 5.74995 | 1 | 0.008683 |
| variance > 0.321235 and variance <= 2.3921 and curtosis > -2.2722 and entropy > 0.092227 and curtosis > -0.17937 and variance <= 0.60077 | 1 | 0.003275 |
| variance <= 0.321235 and skewness > 5.86535 and variance <= -3.4449 and variance > -4.4223 | 1 | 0.001944 |
| variance > 0.321235 and variance <= 2.3921 and curtosis <= -2.2722 and skewness <= 6.41995 | 1 | 0.071816 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| variance > 0.31803 and variance > 2.3917 | 0 | 0.396040 |
| skewness > 5.2808 and variance > -3.3793 | 0 | 0.250000 |
| variance <= 0.31803 and curtosis <= 3.0423 | 1 | 0.687225 |
| variance <= -1.3968 and skewness <= -1.4733 | 1 | 0.506944 |
| curtosis <= -0.17594 and curtosis <= -1.3927 | 1 | 0.300493 |
| variance > 0.67886 | 0 | 0.752066 |
| skewness <= -4.7428 and variance <= -0.63298 | 1 | 0.215385 |
| curtosis > 0.46583 and skewness > -0.77392 | 0 | 0.680000 |
| entropy <= -0.017686 | 0 | 0.466667 |
| curtosis <= 4.7749 | 1 | 0.823529 |
|  | 0 | 0.600000 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| skewness <= 7.259 and variance <= -1.786 | 1 | 0.272824 |
| variance <= 0.75896 and skewness <= 5.0097 and curtosis <= 0.18307 | 1 | 0.175692 |
| variance <= -0.47465 and skewness <= -0.30005 and entropy >= -1.7168 | 1 | 0.092715 |
| variance <= 1.7875 and curtosis <= -2.3 and skewness <= 5.2022 | 1 | 0.044630 |
| variance <= -4.4779 | 1 | 0.029745 |
| entropy >= 0.65472 and variance <= 1.5631 and curtosis <= 2.135 and skewness <= 0.89599 | 1 | 0.021429 |
|  | 0 | 0.988456 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

variance|skewness|curtosis|entropy|class
---|---|---|---|---
(-0.4031-0.321235]|(9.6242-inf)|(-4.42285-8.83885]|all|0
(1.74385-2.3921]|(9.6242-inf)|(-4.42285-8.83885]|all|0
(0.321235-1.74385]|(9.6242-inf)|(-4.42285-8.83885]|all|0
(-2.7571--0.4031]|(9.6242-inf)|(-4.42285-8.83885]|all|0
(2.3921-inf)|(9.6242-inf)|(-4.42285-8.83885]|all|0
(-inf--2.7571]|(5.21045-9.6242]|(-4.42285-8.83885]|all|1
(1.74385-2.3921]|(5.21045-9.6242]|(-4.42285-8.83885]|all|0
(-2.7571--0.4031]|(5.21045-9.6242]|(-4.42285-8.83885]|all|0
(-0.4031-0.321235]|(5.21045-9.6242]|(-4.42285-8.83885]|all|0
(0.321235-1.74385]|(5.21045-9.6242]|(-4.42285-8.83885]|all|0
(2.3921-inf)|(5.21045-9.6242]|(-4.42285-8.83885]|all|0
(2.3921-inf)|(9.6242-inf)|(-inf--4.42285]|all|0
(-inf--2.7571]|(-5.62225--4.3455]|(8.83885-inf)|all|1
(-inf--2.7571]|(-2.4149-5.21045]|(-4.42285-8.83885]|all|1
(0.321235-1.74385]|(-2.4149-5.21045]|(-4.42285-8.83885]|all|0
(-0.4031-0.321235]|(-2.4149-5.21045]|(-4.42285-8.83885]|all|1
(-2.7571--0.4031]|(-2.4149-5.21045]|(-4.42285-8.83885]|all|1
(1.74385-2.3921]|(-2.4149-5.21045]|(-4.42285-8.83885]|all|0
(2.3921-inf)|(-2.4149-5.21045]|(-4.42285-8.83885]|all|0
(-2.7571--0.4031]|(-6.94555--5.62225]|(8.83885-inf)|all|1
(-2.7571--0.4031]|(-4.3455--2.4149]|(-4.42285-8.83885]|all|1
(-0.4031-0.321235]|(-4.3455--2.4149]|(-4.42285-8.83885]|all|1
(-inf--2.7571]|(-6.94555--5.62225]|(8.83885-inf)|all|1
(2.3921-inf)|(5.21045-9.6242]|(-inf--4.42285]|all|0
(1.74385-2.3921]|(-4.3455--2.4149]|(-4.42285-8.83885]|all|0
(2.3921-inf)|(-4.3455--2.4149]|(-4.42285-8.83885]|all|0
(0.321235-1.74385]|(-4.3455--2.4149]|(-4.42285-8.83885]|all|0
(-0.4031-0.321235]|(-5.62225--4.3455]|(-4.42285-8.83885]|all|1
(-0.4031-0.321235]|(-2.4149-5.21045]|(-inf--4.42285]|all|1
(1.74385-2.3921]|(-2.4149-5.21045]|(-inf--4.42285]|all|1
(0.321235-1.74385]|(-2.4149-5.21045]|(-inf--4.42285]|all|1
(-inf--2.7571]|(-inf--6.94555]|(8.83885-inf)|all|1
(-2.7571--0.4031]|(-inf--6.94555]|(8.83885-inf)|all|1
(1.74385-2.3921]|(-5.62225--4.3455]|(-4.42285-8.83885]|all|0
(0.321235-1.74385]|(-5.62225--4.3455]|(-4.42285-8.83885]|all|0
(-2.7571--0.4031]|(-5.62225--4.3455]|(-4.42285-8.83885]|all|1
(2.3921-inf)|(-5.62225--4.3455]|(-4.42285-8.83885]|all|0
(-0.4031-0.321235]|(-6.94555--5.62225]|(-4.42285-8.83885]|all|0
(0.321235-1.74385]|(-6.94555--5.62225]|(-4.42285-8.83885]|all|0
(-2.7571--0.4031]|(-6.94555--5.62225]|(-4.42285-8.83885]|all|1
(-inf--2.7571]|(-6.94555--5.62225]|(-4.42285-8.83885]|all|1
(1.74385-2.3921]|(-6.94555--5.62225]|(-4.42285-8.83885]|all|0
(-inf--2.7571]|(-inf--6.94555]|(-4.42285-8.83885]|all|1
(-2.7571--0.4031]|(-inf--6.94555]|(-4.42285-8.83885]|all|1

## JRip

Decision list:

rules | predicted class
---|---
(skewness <= 7.259) and (variance <= -1.786)|1 (257.0/0.0)
(variance <= 0.75896) and (skewness <= 5.0097) and (curtosis <= 0.18307)|1 (146.0/0.0)
(variance <= -0.47465) and (skewness <= -0.30005) and (entropy >= -1.7168)|1 (70.0/0.0)
(variance <= 1.7875) and (curtosis <= -2.3) and (skewness <= 5.2022)|1 (32.0/0.0)
(variance <= -4.4779)|1 (21.0/0.0)
(entropy >= 0.65472) and (variance <= 1.5631) and (curtosis <= 2.135) and (skewness <= 0.89599)|1 (15.0/0.0)
|0 (693.0/8.0)


## PART

Decision list:

rules | predicted class
---|---
variance > 0.31803 AND variance > 2.3917|0 (360.0)
skewness > 5.2808 AND variance > -3.3793|0 (183.0)
variance <= 0.31803 AND curtosis <= 3.0423|1 (312.0)
variance <= -1.3968 AND skewness <= -1.4733|1 (146.0)
curtosis <= -0.17594 AND curtosis <= -1.3927|1 (61.0)
variance > 0.67886|0 (91.0)
skewness <= -4.7428 AND variance <= -0.63298|1 (14.0)
curtosis > 0.46583 AND skewness > -0.77392|0 (34.0)
entropy <= -0.017686|0 (14.0)
curtosis <= 4.7749|1 (14.0)
|0 (5.0/2.0)


## J48 Decision Tree

* variance <= 0.321235
	* skewness <= 5.86535
		* curtosis <= 3.0642: 1 (277.0)
		* curtosis > 3.0642
			* skewness <= -1.81995
				* variance <= -0.684375: 1 (160.0)
				* variance > -0.684375
					* curtosis <= 5.74995: 1 (6.0)
					* curtosis > 5.74995: 0 (3.0/1.0)
			* skewness > -1.81995
				* variance <= -1.75625: 1 (3.0/1.0)
				* variance > -1.75625: 0 (22.0)
	* skewness > 5.86535
		* variance <= -3.4449
			* variance <= -4.4223: 1 (33.0)
			* variance > -4.4223: 1 (3.0/1.0)
		* variance > -3.4449: 0 (87.0)
* variance > 0.321235
	* variance <= 2.3921
		* curtosis <= -2.2722
			* skewness <= 6.41995: 1 (53.0)
			* skewness > 6.41995: 0 (8.0)
		* curtosis > -2.2722
			* entropy <= 0.092227
				* variance <= 0.450925
					* variance <= 0.38231: 0 (13.0)
					* variance > 0.38231: 0 (3.0/1.0)
				* variance > 0.450925: 0 (147.0)
			* entropy > 0.092227
				* curtosis <= -0.17937: 1 (11.0)
				* curtosis > -0.17937
					* variance <= 0.60077: 1 (4.0/1.0)
					* variance > 0.60077: 0 (41.0)
	* variance > 2.3921: 0 (360.0)


