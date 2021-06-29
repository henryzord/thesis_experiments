# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| variance > 0.75896 and curtosis > -1.8785 | 0 | 0.412206 |
| variance <= 0.75896 and skewness <= 5.1401 and variance <= -0.39416 and curtosis <= 6.2169 | 1 | 0.284969 |
| variance > 0.75896 and curtosis <= -1.8785 and skewness > 4.9228 | 0 | 0.203193 |
| variance <= 0.75896 and skewness <= 5.1401 and variance <= -0.39416 and curtosis > 6.2169 and skewness <= -4.7076 | 1 | 0.146949 |
| variance <= 0.75896 and skewness > 5.1401 and variance > -3.38 | 0 | 0.157990 |
| variance <= 0.75896 and skewness <= 5.1401 and variance > -0.39416 and curtosis <= 0.4247 | 1 | 0.092715 |
| variance > 0.75896 and curtosis <= -1.8785 and skewness <= 4.9228 | 1 | 0.050069 |
| variance <= 0.75896 and skewness <= 5.1401 and variance > -0.39416 and curtosis > 0.4247 and entropy <= 0.72326 | 0 | 0.063184 |
| variance <= 0.75896 and skewness > 5.1401 and variance <= -3.38 | 1 | 0.048649 |
| variance <= 0.75896 and skewness <= 5.1401 and variance <= -0.39416 and curtosis > 6.2169 and skewness > -4.7076 | 0 | 0.021518 |
| variance <= 0.75896 and skewness <= 5.1401 and variance > -0.39416 and curtosis > 0.4247 and entropy > 0.72326 | 1 | 0.013412 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| variance > 0.31803 and curtosis > -3.9692 and variance > 1.5904 | 0 | 0.426941 |
| skewness <= 5.1401 and variance <= -0.46651 and curtosis <= 6.2169 | 1 | 0.492593 |
| curtosis <= 8.4207 and variance > -4.3667 and skewness > 5.2684 | 0 | 0.395400 |
| variance <= -1.786 | 1 | 0.609124 |
| curtosis <= 0.16594 | 1 | 0.572182 |
| skewness > -0.8091 | 0 | 0.644444 |
| entropy <= 0.71162 and variance > -0.71494 | 0 | 0.448892 |
|  | 1 | 0.969697 |


# Text representation of classifiers as-is

## PART

Decision list:

rules | predicted class
---|---
variance > 0.31803 AND curtosis > -3.9692 AND variance > 1.5904|0 (321.0/1.0)
skewness <= 5.1401 AND variance <= -0.46651 AND curtosis <= 6.2169|1 (215.0)
curtosis <= 8.4207 AND variance > -4.3667 AND skewness > 5.2684|0 (156.0/1.0)
variance <= -1.786|1 (112.0)
curtosis <= 0.16594|1 (86.0/1.0)
skewness > -0.8091|0 (47.0)
entropy <= 0.71162 AND variance > -0.71494|0 (26.0/1.0)
|1 (25.0)


## J48 Decision Tree

* variance <= 0.75896
	* skewness <= 5.1401
		* variance <= -0.39416
			* curtosis <= 6.2169: 1 (273.0)
			* curtosis > 6.2169
				* skewness <= -4.7076: 1 (118.0)
				* skewness > -4.7076: 0 (14.0/1.0)
		* variance > -0.39416
			* curtosis <= 0.4247: 1 (70.0)
			* curtosis > 0.4247
				* entropy <= 0.72326: 0 (39.0/1.0)
				* entropy > 0.72326: 1 (13.0/2.0)
	* skewness > 5.1401
		* variance <= -3.38: 1 (37.0/1.0)
		* variance > -3.38: 0 (105.0/1.0)
* variance > 0.75896
	* curtosis <= -1.8785
		* skewness <= 4.9228: 1 (40.0/2.0)
		* skewness > 4.9228: 0 (140.0)
	* curtosis > -1.8785: 0 (385.0)


