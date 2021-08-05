# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 0 | 0.935345 |
| nbumps <= 1.5 and gpuls > 1357 and nbumps3 > 0.5 and seismic = b and genergy > 422215 and genergy > 542500 | 1 | 0.000614 |
| nbumps <= 1.5 and gpuls <= 1357 and shift = N and nbumps > 0.5 and nbumps4 <= 0.5 and seismic = a and ghazard = a and nbumps3 <= 0.5 and seismoacoustic = a and gdenergy <= -54.5 and gpuls > 55.5 | 1 | 0.000614 |
| nbumps <= 1.5 and gpuls > 1357 and nbumps3 > 0.5 and seismic = b and genergy <= 422215 | 1 | 0.002757 |
| nbumps > 1.5 and nbumps2 <= 0.5 and nbumps3 > 2.5 and nbumps3 > 3.5 | 1 | 0.000614 |
| nbumps <= 1.5 and gpuls <= 1357 and shift = N and nbumps > 0.5 and nbumps4 > 0.5 and gdenergy <= -48.5 | 1 | 0.000614 |
| nbumps > 1.5 and nbumps2 > 0.5 and seismic = b and genergy <= 189465 and seismoacoustic = b and ghazard = b and nbumps2 <= 2.5 and genergy > 42730 | 1 | 0.001036 |
| nbumps <= 1.5 and gpuls <= 1357 and shift = W and nbumps4 <= 0.5 and ghazard = b and nbumps <= 0.5 and seismic = b and genergy <= 21325 and genergy > 19400 | 1 | 0.000829 |
| nbumps > 1.5 and nbumps2 > 0.5 and seismic = b and genergy > 189465 and seismoacoustic = a | 1 | 0.004062 |
| nbumps > 1.5 and nbumps2 > 0.5 and seismic = b and genergy <= 189465 and seismoacoustic = a and nbumps4 <= 0.5 and gdenergy <= -57 | 1 | 0.001036 |
| nbumps > 1.5 and nbumps2 > 0.5 and seismic = b and genergy <= 189465 and seismoacoustic = b and ghazard = a and maxenergy > 2500 and nbumps4 <= 0.5 and genergy > 41045 and maxenergy <= 6000 and gdenergy > 4.5 | 1 | 0.001036 |
| nbumps > 1.5 and nbumps2 > 0.5 and seismic = b and genergy > 189465 and seismoacoustic = b and maxenergy <= 3500 | 1 | 0.001473 |
| nbumps <= 1.5 and gpuls <= 1357 and shift = W and nbumps4 <= 0.5 and ghazard = a and seismic = b and nbumps2 <= 0.5 and seismoacoustic = a and nbumps <= 0.5 and gdpuls > 100 and genergy <= 39260 | 1 | 0.001036 |
| nbumps > 1.5 and nbumps2 > 0.5 and seismic = b and genergy <= 189465 and seismoacoustic = b and ghazard = a and maxenergy > 2500 and nbumps4 <= 0.5 and genergy <= 41045 | 1 | 0.002299 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| nbumps <= 1 and gpuls <= 1349 | 0 | 0.918683 |
| seismic = a | 0 | 0.599274 |
| genergy <= 117120 | 0 | 0.398644 |
| nbumps4 > 0 and nbumps2 <= 0 | 0 | 0.089800 |
| seismoacoustic = b and maxenergy > 1000 and nbumps4 <= 0 | 1 | 0.375193 |
| seismoacoustic = a and nbumps <= 3 and genergy <= 415690 | 1 | 0.593537 |
| seismoacoustic = a and nbumps2 <= 1 | 0 | 0.139891 |
| nbumps2 > 1 and genergy > 189170 | 1 | 0.219601 |
|  | 0 | 0.351351 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| nbumps >= 2 and genergy >= 372470 | 1 | 0.003878 |
|  | 0 | 0.946358 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

genergy|gpuls|gdenergy|gdpuls|nbumps|nbumps2|nbumps3|nbumps5|nbumps6|nbumps7|nbumps89|energy|class
---|---|---|---|---|---|---|---|---|---|---|---|---
(48545-inf)|(1137.5-inf)|all|all|(1.5-inf)|(0.5-inf)|(0.5-inf)|all|all|all|all|(550-inf)|0
(-inf-17640]|(-inf-1137.5]|all|all|(1.5-inf)|(0.5-inf)|(0.5-inf)|all|all|all|all|(550-inf)|0
(17640-48545]|(-inf-1137.5]|all|all|(1.5-inf)|(0.5-inf)|(0.5-inf)|all|all|all|all|(550-inf)|0
(48545-inf)|(-inf-1137.5]|all|all|(1.5-inf)|(0.5-inf)|(0.5-inf)|all|all|all|all|(550-inf)|0
(48545-inf)|(1137.5-inf)|all|all|(1.5-inf)|(-inf-0.5]|(0.5-inf)|all|all|all|all|(550-inf)|0
(17640-48545]|(1137.5-inf)|all|all|(1.5-inf)|(0.5-inf)|(-inf-0.5]|all|all|all|all|(550-inf)|1
(-inf-17640]|(-inf-1137.5]|all|all|(1.5-inf)|(-inf-0.5]|(0.5-inf)|all|all|all|all|(550-inf)|1
(48545-inf)|(-inf-1137.5]|all|all|(1.5-inf)|(-inf-0.5]|(0.5-inf)|all|all|all|all|(550-inf)|0
(48545-inf)|(1137.5-inf)|all|all|(1.5-inf)|(0.5-inf)|(-inf-0.5]|all|all|all|all|(550-inf)|0
(17640-48545]|(-inf-1137.5]|all|all|(1.5-inf)|(-inf-0.5]|(0.5-inf)|all|all|all|all|(550-inf)|0
(-inf-17640]|(-inf-1137.5]|all|all|(1.5-inf)|(0.5-inf)|(-inf-0.5]|all|all|all|all|(550-inf)|0
(48545-inf)|(-inf-1137.5]|all|all|(1.5-inf)|(0.5-inf)|(-inf-0.5]|all|all|all|all|(550-inf)|0
(17640-48545]|(-inf-1137.5]|all|all|(1.5-inf)|(0.5-inf)|(-inf-0.5]|all|all|all|all|(550-inf)|0
(17640-48545]|(1137.5-inf)|all|all|(0.5-1.5]|(-inf-0.5]|(0.5-inf)|all|all|all|all|(550-inf)|1
(48545-inf)|(1137.5-inf)|all|all|(0.5-1.5]|(-inf-0.5]|(0.5-inf)|all|all|all|all|(550-inf)|0
(17640-48545]|(1137.5-inf)|all|all|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|all|all|all|all|(550-inf)|1
(48545-inf)|(1137.5-inf)|all|all|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|all|all|all|all|(550-inf)|0
(-inf-17640]|(-inf-1137.5]|all|all|(0.5-1.5]|(-inf-0.5]|(0.5-inf)|all|all|all|all|(550-inf)|0
(17640-48545]|(-inf-1137.5]|all|all|(0.5-1.5]|(-inf-0.5]|(0.5-inf)|all|all|all|all|(550-inf)|0
(48545-inf)|(-inf-1137.5]|all|all|(0.5-1.5]|(-inf-0.5]|(0.5-inf)|all|all|all|all|(550-inf)|0
(48545-inf)|(1137.5-inf)|all|all|(1.5-inf)|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(550-inf)|0
(-inf-17640]|(-inf-1137.5]|all|all|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|all|all|all|all|(550-inf)|0
(48545-inf)|(-inf-1137.5]|all|all|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|all|all|all|all|(550-inf)|0
(17640-48545]|(-inf-1137.5]|all|all|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|all|all|all|all|(550-inf)|0
(48545-inf)|(1137.5-inf)|all|all|(0.5-1.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(550-inf)|0
(-inf-17640]|(-inf-1137.5]|all|all|(0.5-1.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(550-inf)|0
(17640-48545]|(-inf-1137.5]|all|all|(0.5-1.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(550-inf)|0
(48545-inf)|(-inf-1137.5]|all|all|(0.5-1.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(550-inf)|0
(-inf-17640]|(-inf-1137.5]|all|all|(1.5-inf)|(0.5-inf)|(-inf-0.5]|all|all|all|all|(-inf-550]|1
(17640-48545]|(-inf-1137.5]|all|all|(1.5-inf)|(0.5-inf)|(-inf-0.5]|all|all|all|all|(-inf-550]|0
(48545-inf)|(-inf-1137.5]|all|all|(1.5-inf)|(0.5-inf)|(-inf-0.5]|all|all|all|all|(-inf-550]|0
(48545-inf)|(1137.5-inf)|all|all|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|all|all|all|all|(-inf-550]|0
(17640-48545]|(1137.5-inf)|all|all|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|all|all|all|all|(-inf-550]|0
(48545-inf)|(-inf-1137.5]|all|all|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|all|all|all|all|(-inf-550]|0
(-inf-17640]|(-inf-1137.5]|all|all|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|all|all|all|all|(-inf-550]|0
(17640-48545]|(-inf-1137.5]|all|all|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|all|all|all|all|(-inf-550]|0
(-inf-17640]|(-inf-1137.5]|all|all|(0.5-1.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(-inf-550]|1
(48545-inf)|(1137.5-inf)|all|all|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(-inf-550]|0
(17640-48545]|(1137.5-inf)|all|all|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(-inf-550]|0
(17640-48545]|(-inf-1137.5]|all|all|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(-inf-550]|0
(-inf-17640]|(-inf-1137.5]|all|all|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(-inf-550]|0
(48545-inf)|(-inf-1137.5]|all|all|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(-inf-550]|0

## JRip

Decision list:

rules | predicted class
---|---
(nbumps >= 2) and (genergy >= 372470)|1 (88.0/61.0)
|0 (2232.0/123.0)


## PART

Decision list:

rules | predicted class
---|---
nbumps <= 1 AND gpuls <= 1349|0 (1776.0/49.0)
seismic = a|0 (300.0/43.0)
genergy <= 117120|0 (150.0/24.0)
nbumps4 > 0 AND nbumps2 <= 0|0 (19.0/1.0)
seismoacoustic = b AND maxenergy > 1000 AND nbumps4 <= 0|1 (8.0/2.0)
seismoacoustic = a AND nbumps <= 3 AND genergy <= 415690|1 (18.0/3.0)
seismoacoustic = a AND nbumps2 <= 1|0 (18.0/4.0)
nbumps2 > 1 AND genergy > 189170|1 (14.0/6.0)
|0 (17.0)


## J48 Decision Tree

* nbumps <= 1.5
	* gpuls <= 1357
		* shift = W
			* nbumps4 <= 0.5
				* ghazard = a
					* seismic = a: 0 (478.0/17.0)
					* seismic = b
						* nbumps2 <= 0.5
							* seismoacoustic = a
								* nbumps <= 0.5
									* gdpuls <= 100: 0 (158.0/4.0)
									* gdpuls > 100
										* genergy <= 39260: 1 (4.0/1.0)
										* genergy > 39260: 0 (5.0)
								* nbumps > 0.5: 0 (25.0/1.0)
							* seismoacoustic = b: 0 (103.0/6.0)
							* seismoacoustic = c: 0 (0.0)
							* seismoacoustic = d: 0 (0.0)
						* nbumps2 > 0.5: 0 (58.0/2.0)
					* seismic = c: 0 (0.0)
					* seismic = d: 0 (0.0)
				* ghazard = b
					* nbumps <= 0.5
						* seismic = a: 0 (38.0/1.0)
						* seismic = b
							* genergy <= 21325
								* genergy <= 19400: 0 (5.0)
								* genergy > 19400: 1 (5.0/2.0)
							* genergy > 21325: 0 (23.0)
						* seismic = c: 0 (0.0)
						* seismic = d: 0 (0.0)
					* nbumps > 0.5: 0 (31.0)
				* ghazard = c: 0 (17.0)
				* ghazard = d: 0 (0.0)
			* nbumps4 > 0.5: 0 (25.0)
		* shift = N
			* nbumps <= 0.5: 0 (623.0/6.0)
			* nbumps > 0.5
				* nbumps4 <= 0.5
					* seismic = a
						* ghazard = a
							* nbumps3 <= 0.5
								* seismoacoustic = a
									* gdenergy <= -54.5
										* gpuls <= 55.5: 0 (3.0)
										* gpuls > 55.5: 1 (3.0/1.0)
									* gdenergy > -54.5: 0 (22.0)
								* seismoacoustic = b: 0 (12.0)
								* seismoacoustic = c: 0 (0.0)
								* seismoacoustic = d: 0 (0.0)
							* nbumps3 > 0.5: 0 (93.0/2.0)
						* ghazard = b: 0 (4.0)
						* ghazard = c: 0 (3.0)
						* ghazard = d: 0 (0.0)
					* seismic = b: 0 (29.0)
					* seismic = c: 0 (0.0)
					* seismic = d: 0 (0.0)
				* nbumps4 > 0.5
					* gdenergy <= -48.5: 1 (3.0/1.0)
					* gdenergy > -48.5: 0 (6.0)
	* gpuls > 1357
		* nbumps3 <= 0.5: 0 (56.0/6.0)
		* nbumps3 > 0.5
			* seismic = a: 0 (8.0/2.0)
			* seismic = b
				* genergy <= 422215: 1 (6.0)
				* genergy > 422215
					* genergy <= 542500: 0 (3.0)
					* genergy > 542500: 1 (3.0/1.0)
			* seismic = c: 1 (0.0)
			* seismic = d: 1 (0.0)
* nbumps > 1.5
	* nbumps2 <= 0.5
		* nbumps3 <= 2.5: 0 (74.0/4.0)
		* nbumps3 > 2.5
			* nbumps3 <= 3.5: 0 (7.0/1.0)
			* nbumps3 > 3.5: 1 (3.0/1.0)
	* nbumps2 > 0.5
		* seismic = a: 0 (210.0/32.0)
		* seismic = b
			* genergy <= 189465
				* seismoacoustic = a
					* nbumps4 <= 0.5
						* gdenergy <= -57: 1 (4.0/1.0)
						* gdenergy > -57: 0 (46.0/5.0)
					* nbumps4 > 0.5: 0 (23.0/2.0)
				* seismoacoustic = b
					* ghazard = a
						* maxenergy <= 2500: 0 (11.0)
						* maxenergy > 2500
							* nbumps4 <= 0.5
								* genergy <= 41045: 1 (5.0)
								* genergy > 41045
									* maxenergy <= 6000
										* gdenergy <= 4.5: 0 (4.0)
										* gdenergy > 4.5: 1 (4.0/1.0)
									* maxenergy > 6000: 0 (4.0)
							* nbumps4 > 0.5: 0 (17.0/4.0)
					* ghazard = b
						* nbumps2 <= 2.5
							* genergy <= 42730: 0 (4.0)
							* genergy > 42730: 1 (4.0/1.0)
						* nbumps2 > 2.5: 0 (3.0)
					* ghazard = c: 0 (1.0)
					* ghazard = d: 0 (0.0)
				* seismoacoustic = c: 0 (0.0)
				* seismoacoustic = d: 0 (0.0)
			* genergy > 189465
				* seismoacoustic = a: 1 (29.0/13.0)
				* seismoacoustic = b
					* maxenergy <= 3500: 1 (5.0/1.0)
					* maxenergy > 3500: 0 (8.0/1.0)
				* seismoacoustic = c: 0 (2.0)
				* seismoacoustic = d: 0 (0.0)
		* seismic = c: 0 (0.0)
		* seismic = d: 0 (0.0)


