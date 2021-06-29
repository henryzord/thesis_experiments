# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| variance >= 0.311555 and curtosis >= -4.38605 and variance >= 1.5922 and variance >= 2.03655 | 0 | 0.413462 |
| variance < 0.311555 and skewness < 7.76395 and variance < -0.458565 and curtosis < 6.21865 and skewness < 7.293150000000001 | 1 | 0.292355 |
| variance > 0.75108 and variance <= 2.2279 and curtosis > -2.3 | 0 | 0.205587 |
| variance < 0.311555 and skewness < 7.76395 and variance < -0.458565 and curtosis >= 6.21865 and skewness < -4.6745 | 1 | 0.144819 |
| variance <= 0.75108 and skewness > 5.1401 and variance > -3.3793 | 0 | 0.168195 |
| variance <= 0.75108 and skewness <= 5.1401 and variance > -0.46651 and curtosis <= 2.1624 and curtosis <= 0.46583 | 1 | 0.098684 |
| variance > 0.75108 and variance <= 2.2279 and curtosis <= -2.3 and skewness <= 4.8028 | 1 | 0.048611 |
| variance <= 0.75108 and skewness <= 5.1401 and variance > -0.46651 and curtosis > 2.1624 | 0 | 0.048527 |
| variance <= 0.75108 and skewness > 5.1401 and variance <= -3.3793 | 1 | 0.048649 |
| variance < 0.311555 and skewness < 7.76395 and variance < -0.458565 and curtosis >= 6.21865 and skewness >= -4.6745 | 0 | 0.021518 |
| variance <= 0.75108 and skewness <= 5.1401 and variance > -0.46651 and curtosis <= 2.1624 and curtosis > 0.46583 and skewness <= -0.38696 | 1 | 0.017217 |
| variance >= 0.311555 and curtosis < -4.38605 and variance >= 3.22215 | 0 | 0.016129 |
| variance <= 0.75108 and skewness <= 5.1401 and variance > -0.46651 and curtosis <= 2.1624 and curtosis > 0.46583 and skewness > -0.38696 | 0 | 0.012590 |
| variance >= 0.311555 and curtosis >= -4.38605 and variance < 1.5922 and curtosis >= -2.2721999999999998 and entropy >= 0.081882 and curtosis < 1.85305 | 1 | 0.020347 |
| variance > 0.75108 and variance <= 2.2279 and curtosis <= -2.3 and skewness > 4.8028 | 0 | 0.004840 |
| variance >= 0.311555 and curtosis < -4.38605 and variance < 3.22215 | 1 | 0.040616 |
| variance < 0.311555 and skewness >= 7.76395 and variance >= -4.726 | 0 | 0.127186 |

## Ordered rules

### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| skewness <= 5.8333 and curtosis <= 6.2169 and variance <= -0.36506 | 1 | 0.287201 |
| skewness <= -4.7428 and variance <= -0.55355 | 1 | 0.144819 |
| curtosis <= 0.27818 and skewness <= 5.2022 and variance <= 1.2572 | 1 | 0.114987 |
| variance <= -4.1479 and curtosis <= 1.0836 | 1 | 0.048611 |
| variance <= 2.2279 and curtosis <= -2.9581 and skewness <= 4.78 | 1 | 0.022825 |
| skewness <= 1.0595 and variance <= 1.5631 and curtosis <= 2.135 and entropy >= 0.29653 | 1 | 0.022825 |
|  | 0 | 0.998542 |


# Text representation of classifiers as-is

## JRip

Decision list:

rules | predicted class
---|---
(skewness <= 5.8333) and (curtosis <= 6.2169) and (variance <= -0.36506)|1 (276.0/0.0)
(skewness <= -4.7428) and (variance <= -0.55355)|1 (116.0/0.0)
(curtosis <= 0.27818) and (skewness <= 5.2022) and (variance <= 1.2572)|1 (89.0/0.0)
(variance <= -4.1479) and (curtosis <= 1.0836)|1 (35.0/0.0)
(variance <= 2.2279) and (curtosis <= -2.9581) and (skewness <= 4.78)|1 (16.0/0.0)
(skewness <= 1.0595) and (variance <= 1.5631) and (curtosis <= 2.135) and (entropy >= 0.29653)|1 (16.0/0.0)
|0 (686.0/1.0)


## J48 Decision Tree

* variance <= 0.75108
	* skewness <= 5.1401
		* variance <= -0.46651
			* curtosis <= 6.2169: 1 (268.0)
			* curtosis > 6.2169
				* skewness <= -4.7428: 1 (116.0)
				* skewness > -4.7428: 0 (14.0/1.0)
		* variance > -0.46651
			* curtosis <= 2.1624
				* curtosis <= 0.46583: 1 (75.0)
				* curtosis > 0.46583
					* skewness <= -0.38696: 1 (12.0)
					* skewness > -0.38696: 0 (7.0)
			* curtosis > 2.1624: 0 (28.0)
	* skewness > 5.1401
		* variance <= -3.3793: 1 (37.0/1.0)
		* variance > -3.3793: 0 (113.0/1.0)
* variance > 0.75108
	* variance <= 2.2279
		* curtosis <= -2.3
			* skewness <= 4.8028: 1 (35.0)
			* skewness > 4.8028: 0 (6.0/2.0)
		* curtosis > -2.3: 0 (148.0/3.0)
	* variance > 2.2279: 0 (375.0)


## SimpleCart Decision Tree

* variance < 0.311555
	* skewness < 7.76395
		* variance < -0.458565
			* curtosis < 6.21865
				* skewness < 7.293150000000001: 1(283.0/0.0)
				* skewness >= 7.293150000000001: 1(4.0/1.0)
			* curtosis >= 6.21865
				* skewness < -4.6745: 1(116.0/0.0)
				* skewness >= -4.6745: 0(13.0/1.0)
		* variance >= -0.458565
			* curtosis < 0.297461: 1(49.0/3.0)
			* curtosis >= 0.297461
				* entropy < 0.91334
					* skewness < -0.672525: 0(6.0/4.0)
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
			* curtosis < -2.2721999999999998: 1(21.0/2.0)
			* curtosis >= -2.2721999999999998
				* entropy < 0.081882
					* variance < 0.42002: 0(14.0/1.0)
					* variance >= 0.42002: 0(87.0/0.0)
				* entropy >= 0.081882
					* curtosis < 1.85305: 1(16.0/2.0)
					* curtosis >= 1.85305: 0(17.0/0.0)
		* variance >= 1.5922
			* variance < 2.03655: 0(51.0/3.0)
			* variance >= 2.03655: 0(387.0/0.0)


