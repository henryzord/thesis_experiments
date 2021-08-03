# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| variance > 0.7651 and variance > 1.7907000000000002 | 0 | 0.440425 |
| variance <= 0.7651 and skewness <= 5.3646 and curtosis <= 0.7473050000000001 | 1 | 0.248079 |
| variance <= 0.7651 and skewness <= 5.3646 and curtosis > 0.7473050000000001 and variance <= -0.462635 and skewness <= 0.021718 | 1 | 0.241423 |
| variance <= 0.7651 and skewness > 5.3646 and variance > -3.36765 | 0 | 0.154083 |
| variance > 0.7651 and variance <= 1.7907000000000002 and curtosis > -2.2859 | 0 | 0.139647 |
| variance <= 0.7651 and skewness > 5.3646 and variance <= -3.36765 | 1 | 0.048649 |
| variance <= 0.7651 and skewness <= 5.3646 and curtosis > 0.7473050000000001 and variance > -0.462635 and entropy <= 0.72843 | 0 | 0.058500 |
| variance > 0.7651 and variance <= 1.7907000000000002 and curtosis <= -2.2859 | 1 | 0.038304 |
| variance <= 0.7651 and skewness <= 5.3646 and curtosis > 0.7473050000000001 and variance <= -0.462635 and skewness > 0.021718 and curtosis <= 4.462149999999999 | 1 | 0.022825 |
| variance <= 0.7651 and skewness <= 5.3646 and curtosis > 0.7473050000000001 and variance <= -0.462635 and skewness > 0.021718 and curtosis > 4.462149999999999 | 0 | 0.023132 |
| variance <= 0.7651 and skewness <= 5.3646 and curtosis > 0.7473050000000001 and variance > -0.462635 and entropy > 0.72843 | 1 | 0.014800 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| variance > 0.75896 and curtosis > -1.8785 | 0 | 0.408405 |
| skewness <= 5.2187 and variance <= -1.786 | 1 | 0.439568 |
| skewness > 5.2187 and variance > -3.3793 | 0 | 0.447038 |
| curtosis <= 0.70403 and variance <= 1.6988 | 1 | 0.788104 |
| skewness <= -5.554 | 1 | 0.412371 |
| curtosis > 2.9986 and skewness > -1.8624 | 0 | 0.363636 |
| variance <= 0.3223 | 1 | 0.637996 |
| curtosis > -2.6196 | 0 | 0.676407 |
|  | 1 | 1.000000 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| variance <= 0.31803 and skewness <= 5.8333 and curtosis <= 6.2169 | 1 | 0.321794 |
| variance <= -1.3887 and skewness <= -4.7428 | 1 | 0.143750 |
| variance <= 1.7425 and curtosis <= 0.27818 and skewness <= 5.2022 | 1 | 0.079386 |
| variance <= -4.1479 | 1 | 0.047327 |
|  | 0 | 0.984195 |


# Text representation of classifiers as-is

## JRip

Decision list:

rules | predicted class
---|---
(variance <= 0.31803) and (skewness <= 5.8333) and (curtosis <= 6.2169)|1 (329.0/2.0)
(variance <= -1.3887) and (skewness <= -4.7428)|1 (115.0/0.0)
(variance <= 1.7425) and (curtosis <= 0.27818) and (skewness <= 5.2022)|1 (63.0/2.0)
(variance <= -4.1479)|1 (36.0/1.0)
|0 (691.0/11.0)


## PART

Decision list:

rules | predicted class
---|---
variance > 0.75896 AND curtosis > -1.8785|0 (339.0)
skewness <= 5.2187 AND variance <= -1.786|1 (210.0/1.0)
skewness > 5.2187 AND variance > -3.3793|0 (208.0)
curtosis <= 0.70403 AND variance <= 1.6988|1 (190.0)
skewness <= -5.554|1 (36.0)
curtosis > 2.9986 AND skewness > -1.8624|0 (29.0)
variance <= 0.3223|1 (37.0/1.0)
curtosis > -2.6196|0 (24.0/3.0)
|1 (7.0)


## J48 Decision Tree

* variance <= 0.7651
	* skewness <= 5.3646
		* curtosis <= 0.7473050000000001: 1 (201.0)
		* curtosis > 0.7473050000000001
			* variance <= -0.462635
				* skewness <= 0.021718: 1 (182.0/1.0)
				* skewness > 0.021718
					* curtosis <= 4.462149999999999: 1 (14.0)
					* curtosis > 4.462149999999999: 0 (12.0)
			* variance > -0.462635
				* entropy <= 0.72843: 0 (33.0/2.0)
				* entropy > 0.72843: 1 (13.0/2.0)
	* skewness > 5.3646
		* variance <= -3.36765: 1 (31.0/1.0)
		* variance > -3.36765: 0 (90.0)
* variance > 0.7651
	* variance <= 1.7907000000000002
		* curtosis <= -2.2859: 1 (28.0/3.0)
		* curtosis > -2.2859: 0 (77.0/3.0)
	* variance > 1.7907000000000002: 0 (377.0/3.0)


