# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| variance >= 0.321235 and curtosis >= -4.38605 and variance >= 1.5922 | 0 | 0.439817 |
| variance < 0.321235 and skewness < 7.5653 and variance < -0.4031 and curtosis < 6.21565 | 1 | 0.298878 |
| variance < 0.321235 and skewness < 7.5653 and variance < -0.4031 and curtosis >= 6.21565 and skewness < -4.6745 | 1 | 0.145885 |
| variance >= 0.321235 and curtosis >= -4.38605 and variance < 1.5922 and curtosis >= -2.2721999999999998 and entropy < 0.0353305 | 0 | 0.165667 |
| variance <= 0.31803 and skewness > 7.2797 and variance > -4.6765 | 0 | 0.123023 |
| variance < 0.321235 and skewness < 7.5653 and variance >= -0.4031 and skewness < 5.45355 and curtosis < 2.62465 | 1 | 0.069293 |
| variance > 0.31803 and curtosis > -4.3882 and variance <= 1.6032 and curtosis <= -1.4501 and skewness <= 6.0299 | 1 | 0.041958 |
| variance >= 0.321235 and curtosis < -4.38605 and variance < 3.30405 | 1 | 0.039271 |
| variance <= 0.31803 and skewness <= 7.2797 and variance > -1.6988 and curtosis > 6.7019 | 0 | 0.023124 |
| variance >= 0.321235 and curtosis >= -4.38605 and variance < 1.5922 and curtosis >= -2.2721999999999998 and entropy >= 0.0353305 and skewness >= 1.647125 | 0 | 0.024867 |
| variance <= 0.31803 and skewness > 7.2797 and variance <= -4.6765 | 1 | 0.028369 |
| variance < 0.321235 and skewness < 7.5653 and variance >= -0.4031 and skewness >= 5.45355 | 0 | 0.017889 |
| variance >= 0.321235 and curtosis < -4.38605 and variance >= 3.30405 | 0 | 0.016129 |
| variance >= 0.321235 and curtosis >= -4.38605 and variance < 1.5922 and curtosis >= -2.2721999999999998 and entropy >= 0.0353305 and skewness < 1.647125 | 1 | 0.017575 |
| variance > 0.31803 and curtosis > -4.3882 and variance <= 1.6032 and curtosis <= -1.4501 and skewness > 6.0299 | 0 | 0.035149 |
| variance < 0.321235 and skewness < 7.5653 and variance < -0.4031 and curtosis >= 6.21565 and skewness >= -4.6745 | 0 | 0.023250 |
| variance > 0.31803 and curtosis > -4.3882 and variance <= 1.6032 and curtosis > -1.4501 | 0 | 0.161180 |
| variance <= 0.31803 and skewness <= 7.2797 and variance > -1.6988 and curtosis <= 6.7019 | 1 | 0.195159 |
| variance <= 0.31803 and skewness <= 7.2797 and variance <= -1.6988 | 1 | 0.281986 |
| variance < 0.321235 and skewness < 7.5653 and variance >= -0.4031 and skewness < 5.45355 and curtosis >= 2.62465 | 0 | 0.018038 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| variance > 1.55935 and variance > 2.3943 | 0 | 0.394708 |
| skewness > 5.1608 and variance > -3.34615 | 0 | 0.252051 |
| variance <= 0.323615 and curtosis <= 6.85355 | 1 | 0.724692 |
| curtosis > -0.1738 and variance > -1.39495 | 0 | 0.429724 |
|  | 1 | 0.961326 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| variance <= 0.31803 and skewness <= 5.8333 and curtosis <= 2.9618 | 1 | 0.286458 |
| variance <= -0.55355 and skewness <= -0.78427 | 1 | 0.196016 |
| variance <= 1.7875 and skewness <= 5.2022 and curtosis <= -1.4501 | 1 | 0.075574 |
| variance <= -4.3667 | 1 | 0.047288 |
| variance <= 0.66365 and entropy >= 0.00171 and curtosis <= 4.7749 and skewness <= 0.65388 | 1 | 0.014388 |
|  | 0 | 0.991317 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

variance|skewness|curtosis|class
---|---|---|---
(-0.4031-0.321235]|(9.6242-inf)|(-4.42285-8.83885]|0
(0.321235-1.74385]|(9.6242-inf)|(-4.42285-8.83885]|0
(1.74385-2.3921]|(9.6242-inf)|(-4.42285-8.83885]|0
(-2.7571--0.4031]|(9.6242-inf)|(-4.42285-8.83885]|0
(2.3921-inf)|(9.6242-inf)|(-4.42285-8.83885]|0
(0.321235-1.74385]|(5.21045-9.6242]|(-4.42285-8.83885]|0
(-2.7571--0.4031]|(5.21045-9.6242]|(-4.42285-8.83885]|0
(1.74385-2.3921]|(5.21045-9.6242]|(-4.42285-8.83885]|0
(2.3921-inf)|(5.21045-9.6242]|(-4.42285-8.83885]|0
(-0.4031-0.321235]|(5.21045-9.6242]|(-4.42285-8.83885]|0
(-inf--2.7571]|(5.21045-9.6242]|(-4.42285-8.83885]|1
(2.3921-inf)|(9.6242-inf)|(-inf--4.42285]|0
(-inf--2.7571]|(-5.62225--4.3455]|(8.83885-inf)|1
(2.3921-inf)|(-2.4149-5.21045]|(-4.42285-8.83885]|0
(1.74385-2.3921]|(-2.4149-5.21045]|(-4.42285-8.83885]|0
(0.321235-1.74385]|(-2.4149-5.21045]|(-4.42285-8.83885]|0
(-0.4031-0.321235]|(-2.4149-5.21045]|(-4.42285-8.83885]|1
(-inf--2.7571]|(-2.4149-5.21045]|(-4.42285-8.83885]|1
(-2.7571--0.4031]|(-2.4149-5.21045]|(-4.42285-8.83885]|1
(-0.4031-0.321235]|(-4.3455--2.4149]|(-4.42285-8.83885]|1
(1.74385-2.3921]|(-4.3455--2.4149]|(-4.42285-8.83885]|0
(-2.7571--0.4031]|(-6.94555--5.62225]|(8.83885-inf)|1
(2.3921-inf)|(5.21045-9.6242]|(-inf--4.42285]|0
(0.321235-1.74385]|(-4.3455--2.4149]|(-4.42285-8.83885]|0
(2.3921-inf)|(-4.3455--2.4149]|(-4.42285-8.83885]|0
(-inf--2.7571]|(-6.94555--5.62225]|(8.83885-inf)|1
(-2.7571--0.4031]|(-4.3455--2.4149]|(-4.42285-8.83885]|1
(1.74385-2.3921]|(-2.4149-5.21045]|(-inf--4.42285]|1
(-0.4031-0.321235]|(-5.62225--4.3455]|(-4.42285-8.83885]|1
(0.321235-1.74385]|(-5.62225--4.3455]|(-4.42285-8.83885]|0
(2.3921-inf)|(-5.62225--4.3455]|(-4.42285-8.83885]|0
(1.74385-2.3921]|(-5.62225--4.3455]|(-4.42285-8.83885]|0
(-0.4031-0.321235]|(-2.4149-5.21045]|(-inf--4.42285]|1
(-2.7571--0.4031]|(-5.62225--4.3455]|(-4.42285-8.83885]|1
(-2.7571--0.4031]|(-inf--6.94555]|(8.83885-inf)|1
(0.321235-1.74385]|(-2.4149-5.21045]|(-inf--4.42285]|1
(-inf--2.7571]|(-inf--6.94555]|(8.83885-inf)|1
(0.321235-1.74385]|(-6.94555--5.62225]|(-4.42285-8.83885]|0
(-0.4031-0.321235]|(-6.94555--5.62225]|(-4.42285-8.83885]|0
(-inf--2.7571]|(-6.94555--5.62225]|(-4.42285-8.83885]|1
(1.74385-2.3921]|(-6.94555--5.62225]|(-4.42285-8.83885]|0
(-2.7571--0.4031]|(-6.94555--5.62225]|(-4.42285-8.83885]|1
(-inf--2.7571]|(-inf--6.94555]|(-4.42285-8.83885]|1
(-2.7571--0.4031]|(-inf--6.94555]|(-4.42285-8.83885]|1

## JRip

Decision list:

rules | predicted class
---|---
(variance <= 0.31803) and (skewness <= 5.8333) and (curtosis <= 2.9618)|1 (275.0/0.0)
(variance <= -0.55355) and (skewness <= -0.78427)|1 (169.0/1.0)
(variance <= 1.7875) and (skewness <= 5.2022) and (curtosis <= -1.4501)|1 (56.0/0.0)
(variance <= -4.3667)|1 (34.0/0.0)
(variance <= 0.66365) and (entropy >= 0.00171) and (curtosis <= 4.7749) and (skewness <= 0.65388)|1 (10.0/0.0)
|0 (690.0/6.0)


## PART

Decision list:

rules | predicted class
---|---
variance > 1.55935 AND variance > 2.3943|0 (182.0)
skewness > 5.1608 AND variance > -3.34615|0 (95.0)
variance <= 0.323615 AND curtosis <= 6.85355|1 (190.0/1.0)
curtosis > -0.1738 AND variance > -1.39495|0 (63.0/1.0)
|1 (87.0/3.0)


## J48 Decision Tree

* variance <= 0.31803
	* skewness <= 7.2797
		* variance <= -1.6988: 1 (133.0)
		* variance > -1.6988
			* curtosis <= 6.7019: 1 (97.0/4.0)
			* curtosis > 6.7019: 0 (18.0/5.0)
	* skewness > 7.2797
		* variance <= -4.6765: 1 (11.0)
		* variance > -4.6765: 0 (40.0)
* variance > 0.31803
	* curtosis <= -4.3882: 1 (20.0/3.0)
	* curtosis > -4.3882
		* variance <= 1.6032
			* curtosis <= -1.4501
				* skewness <= 6.0299: 1 (13.0)
				* skewness > 6.0299: 0 (10.0)
			* curtosis > -1.4501: 0 (55.0/2.0)
		* variance > 1.6032: 0 (220.0)


## SimpleCart Decision Tree

* variance < 0.321235
	* skewness < 7.5653
		* variance < -0.4031
			* curtosis < 6.21565: 1(293.0/1.0)
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
			* curtosis < -2.2721999999999998: 1(22.0/3.0)
			* curtosis >= -2.2721999999999998
				* entropy < 0.0353305: 0(110.0/1.0)
				* entropy >= 0.0353305
					* skewness < 1.647125: 1(14.0/2.0)
					* skewness >= 1.647125: 0(14.0/0.0)
		* variance >= 1.5922: 0(434.0/3.0)


