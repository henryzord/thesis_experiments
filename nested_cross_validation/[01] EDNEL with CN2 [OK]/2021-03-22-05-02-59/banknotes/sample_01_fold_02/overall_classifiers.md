# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| variance >= 0.320165 and curtosis >= -4.373200000000001 and variance >= 1.5922 | 0 | 0.442082 |
| variance < 0.320165 and skewness < 7.5653 and variance < -0.4031 and curtosis < 6.21865 | 1 | 0.295995 |
| variance <= 0.7602949999999999 and skewness <= 5.1608 and variance <= 0.320165 and curtosis > 3.0642 and skewness <= -1.81995 | 1 | 0.195092 |
| variance <= 0.7602949999999999 and skewness > 5.1608 and variance > -3.36765 | 0 | 0.161846 |
| variance >= 0.320165 and curtosis >= -4.373200000000001 and variance < 1.5922 and curtosis >= -2.2721999999999998 and entropy < 0.081882 | 0 | 0.159279 |
| variance < 0.320165 and skewness < 7.5653 and variance >= -0.4031 and skewness < 5.45355 and curtosis < 2.62465 | 1 | 0.070556 |
| variance > 0.7602949999999999 and variance <= 1.7907000000000002 and curtosis <= -2.2859 | 1 | 0.043636 |
| variance <= 0.7602949999999999 and skewness <= 5.1608 and variance > 0.320165 and curtosis <= 0.47011500000000006 | 1 | 0.037921 |
| variance <= 0.7602949999999999 and skewness <= 5.1608 and variance <= 0.320165 and curtosis > 3.0642 and skewness > -1.81995 | 0 | 0.032067 |
| variance >= 0.320165 and curtosis >= -4.373200000000001 and variance < 1.5922 and curtosis >= -2.2721999999999998 and entropy >= 0.081882 and curtosis >= 1.91945 | 0 | 0.028319 |
| variance < 0.320165 and skewness >= 7.5653 and variance < -4.726 | 1 | 0.025605 |
| variance >= 0.320165 and curtosis < -4.373200000000001 and variance >= 3.30405 | 0 | 0.017889 |
| variance >= 0.320165 and curtosis >= -4.373200000000001 and variance < 1.5922 and curtosis >= -2.2721999999999998 and entropy >= 0.081882 and curtosis < 1.91945 | 1 | 0.020347 |
| variance >= 0.320165 and curtosis >= -4.373200000000001 and variance < 1.5922 and curtosis < -2.2721999999999998 and skewness >= 5.6667 | 0 | 0.005435 |
| variance >= 0.320165 and curtosis < -4.373200000000001 and variance < 3.30405 | 1 | 0.041958 |
| variance > 0.7602949999999999 and variance <= 1.7907000000000002 and curtosis > -2.2859 | 0 | 0.143669 |
| variance < 0.320165 and skewness < 7.5653 and variance >= -0.4031 and skewness < 5.45355 and curtosis >= 2.62465 | 0 | 0.014542 |
| variance < 0.320165 and skewness < 7.5653 and variance < -0.4031 and curtosis >= 6.21865 and skewness >= -4.6745 | 0 | 0.021518 |
| variance < 0.320165 and skewness >= 7.5653 and variance >= -4.726 | 0 | 0.125796 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| variance > 0.75896 and variance > 1.7875 and variance > 2.3917 | 0 | 0.399344 |
| skewness > 5.1401 and variance > -3.3793 and skewness > 5.8974 | 0 | 0.247945 |
| variance <= 0.31803 and curtosis <= 3.0423 and variance <= -0.17296 | 1 | 0.662621 |
| variance <= 0.31803 and skewness <= -1.8624 and variance <= -0.65767 | 1 | 0.539735 |
| curtosis <= 0.20278 and variance <= 1.2572 | 1 | 0.356481 |
| curtosis > -1.8511 and skewness > -0.67253 | 0 | 0.723077 |
| curtosis <= 2.3235 and variance <= 1.762 | 1 | 0.357143 |
| variance > -0.26654 and skewness <= -0.76771 | 0 | 0.792453 |
| curtosis <= 4.7749 | 1 | 0.750000 |
|  | 0 | 0.600000 |


# Text representation of classifiers as-is

## PART

Decision list:

rules | predicted class
---|---
variance > 0.75896 AND variance > 1.7875 AND variance > 2.3917|0 (365.0)
skewness > 5.1401 AND variance > -3.3793 AND skewness > 5.8974|0 (181.0)
variance <= 0.31803 AND curtosis <= 3.0423 AND variance <= -0.17296|1 (273.0)
variance <= 0.31803 AND skewness <= -1.8624 AND variance <= -0.65767|1 (163.0)
curtosis <= 0.20278 AND variance <= 1.2572|1 (77.0)
curtosis > -1.8511 AND skewness > -0.67253|0 (94.0)
curtosis <= 2.3235 AND variance <= 1.762|1 (25.0)
variance > -0.26654 AND skewness <= -0.76771|0 (42.0)
curtosis <= 4.7749|1 (9.0)
|0 (5.0/2.0)


## J48 Decision Tree

* variance <= 0.7602949999999999
	* skewness <= 5.1608
		* variance <= 0.320165
			* curtosis <= 3.0642: 1 (272.0)
			* curtosis > 3.0642
				* skewness <= -1.81995: 1 (170.0/2.0)
				* skewness > -1.81995: 0 (22.0/2.0)
		* variance > 0.320165
			* curtosis <= 0.47011500000000006: 1 (27.0)
			* curtosis > 0.47011500000000006: 0 (30.0/3.0)
	* skewness > 5.1608
		* variance <= -3.36765: 1 (37.0/1.0)
		* variance > -3.36765: 0 (108.0/1.0)
* variance > 0.7602949999999999
	* variance <= 1.7907000000000002
		* curtosis <= -2.2859: 1 (37.0/3.0)
		* curtosis > -2.2859: 0 (98.0/3.0)
	* variance > 1.7907000000000002: 0 (433.0/3.0)


## SimpleCart Decision Tree

* variance < 0.320165
	* skewness < 7.5653
		* variance < -0.4031
			* curtosis < 6.21865: 1(289.0/1.0)
			* curtosis >= 6.21865
				* skewness < -4.6745: 1(117.0/0.0)
				* skewness >= -4.6745: 0(13.0/1.0)
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
				* entropy < 0.081882: 0(105.0/1.0)
				* entropy >= 0.081882
					* curtosis < 1.91945: 1(16.0/2.0)
					* curtosis >= 1.91945: 0(16.0/0.0)
		* variance >= 1.5922: 0(437.0/2.0)


