# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| variance >= 0.320165 and curtosis >= -4.38605 and variance >= 1.5922 | 0 | 0.440388 |
| variance < 0.320165 and skewness < 5.86535 and curtosis < 6.21865 | 1 | 0.322456 |
| variance >= 0.320165 and curtosis >= -4.38605 and variance < 1.5922 and curtosis >= -2.2721999999999998 | 0 | 0.170600 |
| variance < 0.320165 and skewness < 5.86535 and curtosis >= 6.21865 and skewness < -4.6745 | 1 | 0.144830 |
| variance < 0.320165 and skewness >= 5.86535 and variance >= -3.4833999999999996 | 0 | 0.138148 |
| variance < 0.320165 and skewness >= 5.86535 and variance < -3.4833999999999996 | 1 | 0.047327 |
| variance >= 0.320165 and curtosis < -4.38605 | 1 | 0.031392 |
| variance >= 0.320165 and curtosis >= -4.38605 and variance < 1.5922 and curtosis < -2.2721999999999998 | 1 | 0.028605 |
| variance < 0.320165 and skewness < 5.86535 and curtosis >= 6.21865 and skewness >= -4.6745 | 0 | 0.036918 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| variance > 0.31803 and curtosis > -4.3882 and variance > 2.031 | 0 | 0.412206 |
| skewness > 5.1401 and variance > -3.3793 | 0 | 0.252044 |
| variance <= 0.31803 and curtosis <= 3.0423 | 1 | 0.730047 |
| skewness <= -5.1277 and variance <= -0.46651 | 1 | 0.572491 |
| curtosis <= 0.20792 and curtosis <= -1.3927 | 1 | 0.346591 |
| variance > 0.74841 | 0 | 0.732558 |
| entropy <= -0.1651 | 0 | 0.557692 |
| curtosis <= 6.7807 and skewness <= 0.10139 | 1 | 0.477273 |
| variance <= 0.44125 | 0 | 0.904762 |
|  | 0 | 0.666667 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| variance <= 0.31803 and skewness <= 5.8333 and curtosis <= 6.2169 | 1 | 0.322456 |
| variance <= 0.84546 and skewness <= -5.5167 | 1 | 0.138376 |
| variance <= 1.7425 and curtosis <= 0.23191 and skewness <= 4.987 | 1 | 0.081791 |
| variance <= -4.2249 | 1 | 0.051282 |
|  | 0 | 0.984195 |


# Text representation of classifiers as-is

## JRip

Decision list:

rules | predicted class
---|---
(variance <= 0.31803) and (skewness <= 5.8333) and (curtosis <= 6.2169)|1 (328.0/1.0)
(variance <= 0.84546) and (skewness <= -5.5167)|1 (112.0/1.0)
(variance <= 1.7425) and (curtosis <= 0.23191) and (skewness <= 4.987)|1 (63.0/1.0)
(variance <= -4.2249)|1 (39.0/1.0)
|0 (692.0/11.0)


## PART

Decision list:

rules | predicted class
---|---
variance > 0.31803 AND curtosis > -4.3882 AND variance > 2.031|0 (385.0)
skewness > 5.1401 AND variance > -3.3793|0 (185.0)
variance <= 0.31803 AND curtosis <= 3.0423|1 (311.0)
skewness <= -5.1277 AND variance <= -0.46651|1 (154.0)
curtosis <= 0.20792 AND curtosis <= -1.3927|1 (61.0)
variance > 0.74841|0 (63.0)
entropy <= -0.1651|0 (29.0)
curtosis <= 6.7807 AND skewness <= 0.10139|1 (21.0)
variance <= 0.44125|0 (19.0)
|0 (6.0/2.0)


## SimpleCart Decision Tree

* variance < 0.320165
	* skewness < 5.86535
		* curtosis < 6.21865: 1(327.0/1.0)
		* curtosis >= 6.21865
			* skewness < -4.6745: 1(117.0/1.0)
			* skewness >= -4.6745: 0(22.0/1.0)
	* skewness >= 5.86535
		* variance < -3.4833999999999996: 1(35.0/1.0)
		* variance >= -3.4833999999999996: 0(88.0/0.0)
* variance >= 0.320165
	* curtosis < -4.38605: 1(29.0/9.0)
	* curtosis >= -4.38605
		* variance < 1.5922
			* curtosis < -2.2721999999999998: 1(22.0/2.0)
			* curtosis >= -2.2721999999999998: 0(126.0/15.0)
		* variance >= 1.5922: 0(435.0/3.0)


