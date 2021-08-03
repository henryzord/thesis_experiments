# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| gpuls <= 1139.5 and nbumps <= 0.5 and nbumps2 <= 0.5 and nbumps3 <= 0.5 | 0 | 0.889733 |
| nbumps < 1.5 and gpuls < 1342.5 and genergy >= 16880.0 | 0 | 0.858357 |
| nbumps >= 1.5 and gpuls < 884.0 and nbumps3 < 3.5 | 0 | 0.600232 |
| nbumps < 1.5 and gpuls < 1342.5 and genergy < 16880.0 and energy >= 650.0 | 0 | 0.313397 |
| nbumps < 1.5 and gpuls >= 1342.5 and nbumps3 < 0.5 | 0 | 0.249197 |
| gpuls <= 1139.5 and nbumps > 0.5 and nbumps <= 1.5 and nbumps2 > 0.5 and nbumps3 <= 0.5 | 0 | 0.554301 |
| gpuls > 1139.5 and nbumps > 1.5 and nbumps2 > 0.5 and nbumps3 > 0.5 | 0 | 0.181018 |
| nbumps >= 1.5 and gpuls >= 884.0 and gdenergy >= -29.5 and nbumps2 < 0.5 | 0 | 0.163448 |
| nbumps >= 1.5 and gpuls >= 884.0 and gdenergy < -29.5 and nbumps2 >= 0.5 | 1 | 0.003705 |
| gpuls > 1139.5 and nbumps > 1.5 and nbumps2 > 0.5 and nbumps3 <= 0.5 | 0 | 0.080497 |
| nbumps >= 1.5 and gpuls < 884.0 and nbumps3 >= 3.5 and gpuls >= 364.0 | 1 | 0.001657 |
| gpuls <= 1139.5 and nbumps > 1.5 and nbumps2 > 0.5 and nbumps3 > 0.5 | 0 | 0.508628 |
| nbumps >= 1.5 and gpuls >= 884.0 and gdenergy >= -29.5 and nbumps2 >= 0.5 and genergy < 526430.0 and gpuls < 1545.5 and seismoacoustic != d and nbumps2 < 1.5 | 1 | 0.001277 |
| nbumps >= 1.5 and gpuls >= 884.0 and gdenergy < -29.5 and nbumps2 < 0.5 | 0 | 0.043269 |
| nbumps < 1.5 and gpuls >= 1342.5 and nbumps3 >= 0.5 | 0 | 0.031554 |
| gpuls <= 1139.5 and nbumps > 1.5 and nbumps2 > 0.5 and nbumps3 <= 0.5 | 0 | 0.273705 |
| nbumps >= 1.5 and gpuls < 884.0 and nbumps3 >= 3.5 and gpuls < 364.0 | 0 | 0.044586 |
| nbumps <= 1.0 | 0 | 0.919623 |
| nbumps >= 1.5 and gpuls < 884.0 and nbumps3 < 3.5 | 0 | 0.594859 |
| gpuls > 1139.5 and gdpuls = all and nbumps > 1.5 and nbumps2 > 0.5 | 0 | 0.235459 |
| gpuls > 1139.5 and gdpuls = all and nbumps > 1.5 and nbumps2 <= 0.5 | 0 | 0.167350 |
| nbumps >= 1.5 and gpuls >= 884.0 and gdenergy < -29.5 and nbumps2 >= 0.5 | 1 | 0.004127 |
| nbumps > 1.0 and seismoacoustic != c and ghazard != b and nbumps3 <= 3.0 and seismic != a and nbumps2 > 0.0 and genergy <= 184710.0 and seismoacoustic != a and gpuls <= 626.0 and nbumps3 > 1.0 | 1 | 0.001734 |
| gpuls <= 1139.5 and gdpuls = all and nbumps > 1.5 and nbumps2 > 0.5 | 0 | 0.583777 |
| nbumps >= 1.5 and gpuls < 884.0 and nbumps3 >= 3.5 and gpuls >= 364.0 | 1 | 0.001655 |
| nbumps >= 1.5 and gpuls >= 884.0 and gdenergy >= -29.5 and nbumps2 >= 0.5 and genergy < 526430.0 and gpuls < 1545.5 and seismoacoustic != d and nbumps2 < 1.5 | 1 | 0.001275 |
| nbumps > 1.0 and seismoacoustic != c and ghazard != b and nbumps3 > 3.0 and gpuls > 356.0 and nbumps > 5.0 and maxenergy <= 7000.0 | 1 | 0.001437 |
| nbumps > 1.0 and seismoacoustic != c and ghazard != b and nbumps3 > 3.0 and gpuls > 356.0 and nbumps <= 5.0 | 1 | 0.001226 |
| gpuls <= 1139.5 and gdpuls = all and nbumps > 1.5 and nbumps2 <= 0.5 | 0 | 0.200774 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| nbumps <= 1.0 | 0 | 0.919623 |
| nbumps3 <= 3.0 and ghazard != b and nbumps2 > 0.0 and genergy <= 373180.0 | 0 | 0.582774 |
| nbumps2 <= 0.0 | 0 | 0.253311 |
| seismic = a | 0 | 0.098584 |
| seismoacoustic != a | 0 | 0.036827 |
| nbumps <= 3.0 | 1 | 0.903911 |
|  | 0 | 0.317073 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| nbumps >= 2 and gpuls >= 886 and gdenergy <= -30 and nbumps2 >= 1 and gdpuls >= -45 and genergy <= 600400 | 1 | 0.005037 |
| nbumps >= 3 and nbumps <= 3 and maxenergy >= 5000 and gpuls >= 1764 and gdpuls <= 29 and nbumps3 <= 2 | 1 | 0.002754 |
| nbumps >= 3 and gpuls >= 525 and genergy <= 127110 and genergy >= 122410 | 1 | 0.002296 |
| nbumps >= 5 and seismoacoustic = b and gdenergy >= 71 and seismic = b | 1 | 0.002296 |
| nbumps >= 2 and gdpuls <= 10 and gdpuls >= 0 and genergy <= 59840 and energy >= 3900 and seismic = b and genergy >= 29410 | 1 | 0.003211 |
|  | 0 | 0.948080 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

gpuls|gdpuls|nbumps|nbumps2|class
---|---|---|---|---
(1139.5-inf)|all|(1.5-inf)|(0.5-inf)|0
(-inf-1139.5]|all|(1.5-inf)|(0.5-inf)|0
(1139.5-inf)|all|(0.5-1.5]|(0.5-inf)|0
(-inf-1139.5]|all|(0.5-1.5]|(0.5-inf)|0
(-inf-1139.5]|all|(1.5-inf)|(-inf-0.5]|0
(1139.5-inf)|all|(1.5-inf)|(-inf-0.5]|0
(1139.5-inf)|all|(0.5-1.5]|(-inf-0.5]|0
(-inf-1139.5]|all|(0.5-1.5]|(-inf-0.5]|0
(1139.5-inf)|all|(-inf-0.5]|(-inf-0.5]|0
(-inf-1139.5]|all|(-inf-0.5]|(-inf-0.5]|0

## JRip

Decision list:

rules | predicted class
---|---
(nbumps >= 2) and (gpuls >= 886) and (gdenergy <= -30) and (nbumps2 >= 1) and (gdpuls >= -45) and (genergy <= 600400)|1 (11.0/0.0)
(nbumps >= 3) and (nbumps <= 3) and (maxenergy >= 5000) and (gpuls >= 1764) and (gdpuls <= 29) and (nbumps3 <= 2)|1 (6.0/0.0)
(nbumps >= 3) and (gpuls >= 525) and (genergy <= 127110) and (genergy >= 122410)|1 (5.0/0.0)
(nbumps >= 5) and (seismoacoustic = b) and (gdenergy >= 71) and (seismic = b)|1 (5.0/0.0)
(nbumps >= 2) and (gdpuls <= 10) and (gdpuls >= 0) and (genergy <= 59840) and (energy >= 3900) and (seismic = b) and (genergy >= 29410)|1 (7.0/0.0)
|0 (2292.0/119.0)


## PART

Decision list:

rules | predicted class
---|---
nbumps <= 1.0|0 (1851.0/64.0)
nbumps3 <= 3.0 AND ghazard != b AND nbumps2 > 0.0 AND genergy <= 373180.0|0 (284.0/41.0)
nbumps2 <= 0.0|0 (86.0/9.0)
seismic = a|0 (49.0/14.0)
seismoacoustic != a|0 (30.0/12.0)
nbumps <= 3.0|1 (13.0/4.0)
|0 (13.0/4.0)


## J48 Decision Tree

* nbumps <= 1.0: 0 (1632.0/58.0)
* nbumps > 1.0
	* seismoacoustic = c: 0 (8.0/3.0)
	* seismoacoustic != c
		* ghazard = b: 0 (27.0/8.0)
		* ghazard != b
			* nbumps3 <= 3.0
				* seismic = a: 0 (189.0/25.0)
				* seismic != a
					* nbumps2 <= 0.0: 0 (33.0/3.0)
					* nbumps2 > 0.0
						* genergy <= 184710.0
							* seismoacoustic = a: 0 (59.0/7.0)
							* seismoacoustic != a
								* gpuls <= 626.0
									* nbumps3 <= 1.0: 0 (9.0/2.0)
									* nbumps3 > 1.0: 1 (10.0/5.0)
								* gpuls > 626.0: 0 (15.0)
						* genergy > 184710.0: 0 (31.0/15.0)
			* nbumps3 > 3.0
				* gpuls <= 356.0: 0 (6.0)
				* gpuls > 356.0
					* nbumps <= 5.0: 1 (6.0/2.0)
					* nbumps > 5.0
						* maxenergy <= 7000.0: 1 (6.0/3.0)
						* maxenergy > 7000.0: 0 (5.0/1.0)


## SimpleCart Decision Tree

* nbumps < 1.5
	* gpuls < 1342.5
		* genergy < 16880.0
			* energy < 650.0
				* gdenergy < -84.5: 0(25.0/1.0)
				* gdenergy >= -84.5
					* gpuls < 219.0: 0(405.0/4.0)
					* gpuls >= 219.0: 0(281.0/0.0)
			* energy >= 650.0: 0(73.0/5.0)
		* genergy >= 16880.0: 0(939.0/40.0)
	* gpuls >= 1342.5
		* nbumps3 < 0.5: 0(55.0/6.0)
		* nbumps3 >= 0.5: 0(9.0/8.0)
* nbumps >= 1.5
	* gpuls < 884.0
		* nbumps3 < 3.5: 0(249.0/35.0)
		* nbumps3 >= 3.5
			* gpuls < 364.0: 0(7.0/0.0)
			* gpuls >= 364.0: 1(6.0/4.0)
	* gpuls >= 884.0
		* gdenergy < -29.5
			* nbumps2 < 0.5: 0(9.0/3.0)
			* nbumps2 >= 0.5: 1(12.0/4.0)
		* gdenergy >= -29.5
			* nbumps2 < 0.5: 0(32.0/3.0)
			* nbumps2 >= 0.5
				* genergy < 526430.0
					* gpuls < 1545.5
							* seismoacoustic=(b)|(d): 0(19.0/3.0)
							* seismoacoustic!=(b)|(d)
							* nbumps2 < 1.5: 1(6.0/1.0)
							* nbumps2 >= 1.5: 0(11.0/3.0)
					* gpuls >= 1545.5: 0(25.0/2.0)
				* genergy >= 526430.0: 0(25.0/16.0)


