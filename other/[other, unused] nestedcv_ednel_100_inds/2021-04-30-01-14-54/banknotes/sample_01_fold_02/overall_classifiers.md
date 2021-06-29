# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| variance >= 0.320165 and curtosis >= -4.373200000000001 and variance >= 1.5922 and variance >= 1.7438500000000001 and variance >= 2.0185 | 0 | 0.414088 |
| variance < 0.320165 and skewness < 7.5653 and variance < -0.4031 and curtosis < 6.21865 and skewness < 7.293150000000001 | 1 | 0.295267 |
| variance < 0.320165 and skewness < 7.5653 and variance < -0.4031 and curtosis >= 6.21865 and skewness < -4.6745 | 1 | 0.145885 |
| variance >= 0.320165 and curtosis >= -4.373200000000001 and variance < 1.5922 and curtosis >= -2.2721999999999998 and entropy < 0.081882 and variance >= 0.42002 | 0 | 0.142188 |
| variance < 0.320165 and skewness >= 7.5653 and variance >= -4.726 | 0 | 0.125796 |
| variance < 0.320165 and skewness < 7.5653 and variance >= -0.4031 and skewness < 5.45355 and curtosis < 2.62465 | 1 | 0.070556 |
| variance >= 0.320165 and curtosis >= -4.373200000000001 and variance >= 1.5922 and variance >= 1.7438500000000001 and variance < 2.0185 | 0 | 0.063184 |
| variance >= 0.320165 and curtosis < -4.373200000000001 and variance < 3.30405 | 1 | 0.041958 |
| variance >= 0.320165 and curtosis >= -4.373200000000001 and variance < 1.5922 and curtosis >= -2.2721999999999998 and entropy >= 0.081882 and curtosis >= 1.91945 | 0 | 0.028319 |
| variance >= 0.320165 and curtosis >= -4.373200000000001 and variance < 1.5922 and curtosis < -2.2721999999999998 and skewness < 5.6667 | 1 | 0.031117 |
| variance >= 0.320165 and curtosis >= -4.373200000000001 and variance < 1.5922 and curtosis >= -2.2721999999999998 and entropy < 0.081882 and variance < 0.42002 | 0 | 0.023250 |
| variance < 0.320165 and skewness >= 7.5653 and variance < -4.726 | 1 | 0.025605 |
| variance < 0.320165 and skewness < 7.5653 and variance < -0.4031 and curtosis >= 6.21865 and skewness >= -4.6745 and variance >= -2.1171 | 0 | 0.021390 |
| variance >= 0.320165 and curtosis >= -4.373200000000001 and variance >= 1.5922 and variance < 1.7438500000000001 | 0 | 0.018038 |
| variance >= 0.320165 and curtosis >= -4.373200000000001 and variance < 1.5922 and curtosis >= -2.2721999999999998 and entropy >= 0.081882 and curtosis < 1.91945 and skewness < 3.5591749999999998 | 1 | 0.022825 |
| variance >= 0.320165 and curtosis < -4.373200000000001 and variance >= 3.30405 | 0 | 0.017889 |
| variance < 0.320165 and skewness < 7.5653 and variance >= -0.4031 and skewness >= 5.45355 | 0 | 0.017889 |
| variance < 0.320165 and skewness < 7.5653 and variance >= -0.4031 and skewness < 5.45355 and curtosis >= 2.62465 | 0 | 0.014542 |
| variance >= 0.320165 and curtosis >= -4.373200000000001 and variance < 1.5922 and curtosis < -2.2721999999999998 and skewness >= 5.6667 | 0 | 0.005435 |
| variance < 0.320165 and skewness < 7.5653 and variance < -0.4031 and curtosis < 6.21865 and skewness >= 7.293150000000001 | 1 | 0.001944 |
| variance >= 0.320165 and curtosis >= -4.373200000000001 and variance < 1.5922 and curtosis >= -2.2721999999999998 and entropy >= 0.081882 and curtosis < 1.91945 and skewness >= 3.5591749999999998 | 0 | 0.003630 |
| variance < 0.320165 and skewness < 7.5653 and variance < -0.4031 and curtosis >= 6.21865 and skewness >= -4.6745 and variance < -2.1171 | 0 | 0.000911 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| variance > 0.30081 and variance > 2.3917 | 0 | 0.399344 |
| skewness > 5.0097 and variance > -3.4605 | 0 | 0.256105 |
| variance <= 0.30081 and curtosis <= 3.0423 | 1 | 0.702517 |
| skewness <= -4.9518 and variance <= -0.59587 | 1 | 0.540636 |
| curtosis > -0.23592 and variance > -0.37013 | 0 | 0.547984 |
| curtosis <= 6.7019 | 1 | 0.842563 |
|  | 0 | 0.941176 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| variance <= -0.30432 and skewness <= 7.259 and curtosis <= 6.2169 | 1 | 0.298888 |
| variance <= 0.75896 and skewness <= -4.7428 | 1 | 0.143792 |
| variance <= 1.7425 and curtosis <= 0.2182 and skewness <= 5.2022 | 1 | 0.128511 |
| variance <= -5.0301 | 1 | 0.028369 |
| skewness <= -0.69529 and variance <= 0.74428 and curtosis <= 2.135 | 1 | 0.015805 |
| curtosis <= -4.8037 | 1 | 0.002624 |
|  | 0 | 0.997089 |


# Text representation of classifiers as-is

## JRip

Decision list:

rules | predicted class
---|---
(variance <= -0.30432) and (skewness <= 7.259) and (curtosis <= 6.2169)|1 (296.0/2.0)
(variance <= 0.75896) and (skewness <= -4.7428)|1 (119.0/2.0)
(variance <= 1.7425) and (curtosis <= 0.2182) and (skewness <= 5.2022)|1 (103.0/1.0)
(variance <= -5.0301)|1 (20.0/0.0)
(skewness <= -0.69529) and (variance <= 0.74428) and (curtosis <= 2.135)|1 (11.0/0.0)
(curtosis <= -4.8037)|1 (5.0/2.0)
|0 (680.0/2.0)


## PART

Decision list:

rules | predicted class
---|---
variance > 0.30081 AND variance > 2.3917|0 (175.0)
skewness > 5.0097 AND variance > -3.4605|0 (94.0)
variance <= 0.30081 AND curtosis <= 3.0423|1 (154.0)
skewness <= -4.9518 AND variance <= -0.59587|1 (80.0)
curtosis > -0.23592 AND variance > -0.37013|0 (68.0/1.0)
curtosis <= 6.7019|1 (41.0/2.0)
|0 (5.0)


## SimpleCart Decision Tree

* variance < 0.320165
	* skewness < 7.5653
		* variance < -0.4031
			* curtosis < 6.21865
				* skewness < 7.293150000000001: 1(287.0/0.0)
				* skewness >= 7.293150000000001: 1(2.0/1.0)
			* curtosis >= 6.21865
				* skewness < -4.6745: 1(117.0/0.0)
				* skewness >= -4.6745
					* variance < -2.1171: 0(1.0/1.0)
					* variance >= -2.1171: 0(12.0/0.0)
		* variance >= -0.4031
			* skewness < 5.45355
				* curtosis < 2.62465: 1(52.0/0.0)
				* curtosis >= 2.62465: 0(9.0/1.0)
			* skewness >= 5.45355: 0(10.0/0.0)
	* skewness >= 7.5653
		* variance < -4.726: 1(18.0/0.0)
		* variance >= -4.726: 0(79.0/0.0)
* variance >= 0.320165
	* curtosis < -4.373200000000001
		* variance < 3.30405: 1(30.0/0.0)
		* variance >= 3.30405: 0(10.0/0.0)
	* curtosis >= -4.373200000000001
		* variance < 1.5922
			* curtosis < -2.2721999999999998
				* skewness < 5.6667: 1(22.0/0.0)
				* skewness >= 5.6667: 0(3.0/0.0)
			* curtosis >= -2.2721999999999998
				* entropy < 0.081882
					* variance < 0.42002: 0(14.0/1.0)
					* variance >= 0.42002: 0(91.0/0.0)
				* entropy >= 0.081882
					* curtosis < 1.91945
						* skewness < 3.5591749999999998: 1(16.0/0.0)
						* skewness >= 3.5591749999999998: 0(2.0/0.0)
					* curtosis >= 1.91945: 0(16.0/0.0)
		* variance >= 1.5922
			* variance < 1.7438500000000001: 0(11.0/1.0)
			* variance >= 1.7438500000000001
				* variance < 2.0185: 0(38.0/1.0)
				* variance >= 2.0185: 0(388.0/0.0)


