# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Band11 >= 0.1985 and Band27 >= 0.8165 | M | 0.343439 |
| Band11 < 0.1985 and Band4 < 0.051000000000000004 | R | 0.336336 |
| Band11 >= 0.1985 and Band27 < 0.8165 and Band39 >= 0.1625 and Band47 >= 0.063 and Band37 < 0.504 | M | 0.193059 |
| Band11 < 0.1985 and Band4 >= 0.051000000000000004 and Band45 >= 0.162 | M | 0.102041 |
| Band11 >= 0.1985 and Band27 < 0.8165 and Band39 >= 0.1625 and Band47 < 0.063 and Band8 >= 0.17049999999999998 | R | 0.083333 |
| Band11 >= 0.1985 and Band27 < 0.8165 and Band39 < 0.1625 | R | 0.075701 |
| Band11 >= 0.1985 and Band27 < 0.8165 and Band39 >= 0.1625 and Band47 >= 0.063 and Band37 >= 0.504 and Band2 >= 0.0595 | M | 0.053763 |
| Band11 < 0.1985 and Band4 >= 0.051000000000000004 and Band45 < 0.162 | R | 0.055944 |
| Band11 >= 0.1985 and Band27 < 0.8165 and Band39 >= 0.1625 and Band47 < 0.063 and Band8 < 0.17049999999999998 | M | 0.043478 |
| Band11 >= 0.1985 and Band27 < 0.8165 and Band39 >= 0.1625 and Band47 >= 0.063 and Band37 >= 0.504 and Band2 < 0.0595 | R | 0.038835 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Band11 > 0.197 and Band27 > 0.814 | M | 0.343439 |
| Band54 <= 0.022 and Band2 <= 0.082 and Band1 > 0.011 and Band36 > 0.478 | R | 0.359521 |
| Band54 <= 0.022 and Band1 > 0.011 and Band43 <= 0.278 and Band26 > 0.622 | R | 0.275952 |
| Band1 > 0.011 and Band42 > 0.268 | M | 0.442623 |
| Band21 > 0.54 and Band3 > 0.025 | M | 0.314869 |
|  | R | 0.829268 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Band12 <= 0.212 and Band20 <= 0.522 | R | 0.294225 |
| Band48 <= 0.075 and Band22 <= 0.726 and Band11 <= 0.299 | R | 0.132095 |
| Band11 <= 0.158 and Band42 <= 0.147 | R | 0.100000 |
| Band17 >= 0.54 and Band23 <= 0.784 and Band25 >= 0.316 | R | 0.080774 |
|  | M | 0.942857 |


# Text representation of classifiers as-is

## JRip

Decision list:

rules | predicted class
---|---
(Band12 <= 0.212) and (Band20 <= 0.522)|R (47.0/3.0)
(Band48 <= 0.075) and (Band22 <= 0.726) and (Band11 <= 0.299)|R (17.0/1.0)
(Band11 <= 0.158) and (Band42 <= 0.147)|R (11.0/0.0)
(Band17 >= 0.54) and (Band23 <= 0.784) and (Band25 >= 0.316)|R (13.0/2.0)
|M (99.0/6.0)


## PART

Decision list:

rules | predicted class
---|---
Band11 > 0.197 AND Band27 > 0.814|M (48.0/1.0)
Band54 <= 0.022 AND Band2 <= 0.082 AND Band1 > 0.011 AND Band36 > 0.478|R (33.0/2.0)
Band54 <= 0.022 AND Band1 > 0.011 AND Band43 <= 0.278 AND Band26 > 0.622|R (25.0/3.0)
Band1 > 0.011 AND Band42 > 0.268|M (25.0)
Band21 > 0.54 AND Band3 > 0.025|M (21.0/3.0)
|R (35.0/4.0)


## SimpleCart Decision Tree

* Band11 < 0.1985
	* Band4 < 0.051000000000000004: R(56.0/7.0)
	* Band4 >= 0.051000000000000004
		* Band45 < 0.162: R(8.0/3.0)
		* Band45 >= 0.162: M(10.0/0.0)
* Band11 >= 0.1985
	* Band27 < 0.8165
		* Band39 < 0.1625: R(9.0/1.0)
		* Band39 >= 0.1625
			* Band47 < 0.063
				* Band8 < 0.17049999999999998: M(4.0/0.0)
				* Band8 >= 0.17049999999999998: R(9.0/0.0)
			* Band47 >= 0.063
				* Band37 < 0.504: M(22.0/1.0)
				* Band37 >= 0.504
					* Band2 < 0.0595: R(4.0/0.0)
					* Band2 >= 0.0595: M(5.0/0.0)
	* Band27 >= 0.8165: M(47.0/1.0)


