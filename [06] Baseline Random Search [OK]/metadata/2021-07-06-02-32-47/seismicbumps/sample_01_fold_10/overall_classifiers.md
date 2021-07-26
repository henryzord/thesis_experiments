# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 0 | 0.935345 |
| nbumps <= 1 and gpuls > 1209 and nbumps3 > 0 and seismic = b | 1 | 0.001880 |
| nbumps > 1 and nbumps <= 5 and ghazard = a and seismic = a and seismoacoustic = c | 1 | 0.000230 |
| nbumps > 1 and nbumps <= 5 and ghazard = a and seismic = a and seismoacoustic = a and shift = W and nbumps3 <= 1 and nbumps <= 2 and nbumps4 <= 0 and nbumps2 <= 1 and gpuls > 746 | 1 | 0.001439 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| nbumps <= 1.5 | 0 | 0.920977 |
| nbumps3 <= 3.5 and ghazard != b and nbumps2 > 0.5 and genergy <= 376545.0 and seismic = a | 0 | 0.460986 |
| nbumps2 <= 0.5 | 0 | 0.258232 |
| seismoacoustic != b and genergy <= 188060.0 | 0 | 0.235929 |
|  | 0 | 0.382716 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| nbumps >= 2 and gpuls >= 898 and gdenergy <= -30 and nbumps2 >= 1 and gdpuls >= -45 and genergy <= 600400 | 1 | 0.005044 |
| nbumps >= 3 and gpuls >= 525 and energy <= 40600 and energy >= 19000 | 1 | 0.002555 |
| gdpuls <= 18 and gdpuls >= 0 and nbumps >= 3 | 1 | 0.002743 |
|  | 0 | 0.950504 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

gpuls|gdenergy|nbumps|nbumps5|nbumps6|class
---|---|---|---|---|---
(-inf-1139.5]|all|(1.5-inf)|all|all|0
(1139.5-inf)|all|(1.5-inf)|all|all|0
(1139.5-inf)|all|(0.5-1.5]|all|all|0
(-inf-1139.5]|all|(0.5-1.5]|all|all|0
(1139.5-inf)|all|(-inf-0.5]|all|all|0
(-inf-1139.5]|all|(-inf-0.5]|all|all|0

## JRip

Decision list:

rules | predicted class
---|---
(nbumps >= 2) and (gpuls >= 898) and (gdenergy <= -30) and (nbumps2 >= 1) and (gdpuls >= -45) and (genergy <= 600400)|1 (11.0/0.0)
(nbumps >= 3) and (gpuls >= 525) and (energy <= 40600) and (energy >= 19000)|1 (26.0/14.0)
(gdpuls <= 18) and (gdpuls >= 0) and (nbumps >= 3)|1 (33.0/19.0)
|0 (2250.0/113.0)


## PART

Decision list:

rules | predicted class
---|---
nbumps <= 1.5|0 (1847.0/63.0)
nbumps3 <= 3.5 AND ghazard != b AND nbumps2 > 0.5 AND genergy <= 376545.0 AND seismic = a|0 (165.0/19.0)
nbumps2 <= 0.5|0 (86.0/9.0)
seismoacoustic != b AND genergy <= 188060.0|0 (80.0/10.0)
|0 (142.0/49.0)


## J48 Decision Tree

* nbumps <= 1
	* gpuls <= 1209: 0 (1497.0/41.0)
	* gpuls > 1209
		* nbumps3 <= 0: 0 (69.0/7.0)
		* nbumps3 > 0
			* seismic = a: 0 (12.0/2.0)
			* seismic = b: 1 (9.0/4.0)
			* seismic = c: 0 (0.0)
			* seismic = d: 0 (0.0)
* nbumps > 1
	* nbumps <= 5
		* ghazard = a
			* seismic = a
				* seismoacoustic = a
					* shift = W
						* nbumps3 <= 1
							* nbumps <= 2
								* nbumps4 <= 0
									* nbumps2 <= 1
										* gpuls <= 746: 0 (18.0)
										* gpuls > 746: 1 (6.0/3.0)
									* nbumps2 > 1: 0 (17.0/2.0)
								* nbumps4 > 0: 0 (3.0)
							* nbumps > 2: 0 (20.0/4.0)
						* nbumps3 > 1: 0 (45.0/2.0)
					* shift = N: 0 (10.0/2.0)
				* seismoacoustic = b: 0 (70.0/11.0)
				* seismoacoustic = c: 1 (2.0/1.0)
				* seismoacoustic = d: 0 (0.0)
			* seismic = b: 0 (143.0/29.0)
			* seismic = c: 0 (0.0)
			* seismic = d: 0 (0.0)
		* ghazard = b: 0 (30.0/8.0)
		* ghazard = c: 0 (3.0)
		* ghazard = d: 0 (0.0)
	* nbumps > 5: 0 (35.0/12.0)


## SimpleCart Decision Tree

* : 0(2170.0/150.0)


