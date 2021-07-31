# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 0 | 0.935345 |
| nbumps <= 1 and gpuls > 1209 and nbumps3 > 0 and seismic = b | 1 | 0.002661 |
| nbumps > 1 and nbumps2 > 0 and genergy <= 373180 and nbumps3 > 3 and gdenergy > 22 | 1 | 0.001439 |
| nbumps > 1 and nbumps2 > 0 and genergy > 373180 and energy > 5700 and genergy <= 951410 and energy <= 10300 | 1 | 0.003266 |
| nbumps > 1 and nbumps2 > 0 and genergy > 373180 and energy > 5700 and genergy <= 951410 and energy > 10300 and gpuls <= 1848 | 1 | 0.001841 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| nbumps <= 1.0 and gpuls <= 1252.0 | 0 | 0.918143 |
| shift = W and seismic = a | 0 | 0.583143 |
| shift = W and ghazard = a and nbumps4 <= 0.0 and genergy <= 117120.0 | 0 | 0.236667 |
| genergy <= 114540.0 | 0 | 0.263184 |
| nbumps2 <= 0.0 | 0 | 0.111410 |
| seismoacoustic = a and nbumps <= 3.0 | 1 | 0.694444 |
|  | 0 | 0.292453 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| gpuls >= 751 and nbumps >= 3 and gpuls <= 886 and nbumps2 >= 2 | 1 | 0.001840 |
| nbumps >= 2 and nbumps2 >= 1 and gdpuls <= -4 and gdenergy <= -30 and gpuls >= 1255 | 1 | 0.003673 |
| nbumps >= 2 and seismic = b and gdenergy >= -17 and gdpuls >= 5 and gdenergy <= 6 and gdpuls <= 10 | 1 | 0.003215 |
| nbumps >= 2 and gpuls >= 979 and genergy >= 95180 and genergy <= 107100 | 1 | 0.001840 |
| genergy >= 568200 and nbumps2 >= 2 and nbumps >= 5 | 1 | 0.001840 |
|  | 0 | 0.946358 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

shift|genergy|gpuls|gdenergy|nbumps|nbumps5|nbumps6|class
---|---|---|---|---|---|---|---
n|(44750-inf)|(1139.5-inf)|all|(1.5-inf)|all|all|1
w|(44750-inf)|(1139.5-inf)|all|(1.5-inf)|all|all|0
w|(17640-44750]|(1139.5-inf)|all|(1.5-inf)|all|all|1
n|(44750-inf)|(-inf-1139.5]|all|(1.5-inf)|all|all|0
w|(44750-inf)|(-inf-1139.5]|all|(1.5-inf)|all|all|0
n|(17640-44750]|(-inf-1139.5]|all|(1.5-inf)|all|all|0
w|(17640-44750]|(-inf-1139.5]|all|(1.5-inf)|all|all|0
w|(-inf-17640]|(-inf-1139.5]|all|(1.5-inf)|all|all|0
w|(44750-inf)|(1139.5-inf)|all|(0.5-1.5]|all|all|0
n|(-inf-17640]|(-inf-1139.5]|all|(1.5-inf)|all|all|0
w|(17640-44750]|(1139.5-inf)|all|(0.5-1.5]|all|all|0
w|(44750-inf)|(-inf-1139.5]|all|(0.5-1.5]|all|all|0
n|(44750-inf)|(-inf-1139.5]|all|(0.5-1.5]|all|all|0
n|(17640-44750]|(-inf-1139.5]|all|(0.5-1.5]|all|all|0
w|(17640-44750]|(-inf-1139.5]|all|(0.5-1.5]|all|all|0
n|(44750-inf)|(1139.5-inf)|all|(-inf-0.5]|all|all|0
w|(44750-inf)|(1139.5-inf)|all|(-inf-0.5]|all|all|0
w|(-inf-17640]|(-inf-1139.5]|all|(0.5-1.5]|all|all|0
n|(-inf-17640]|(-inf-1139.5]|all|(0.5-1.5]|all|all|0
n|(17640-44750]|(1139.5-inf)|all|(-inf-0.5]|all|all|1
w|(17640-44750]|(1139.5-inf)|all|(-inf-0.5]|all|all|0
w|(44750-inf)|(-inf-1139.5]|all|(-inf-0.5]|all|all|0
n|(44750-inf)|(-inf-1139.5]|all|(-inf-0.5]|all|all|0
n|(17640-44750]|(-inf-1139.5]|all|(-inf-0.5]|all|all|0
w|(17640-44750]|(-inf-1139.5]|all|(-inf-0.5]|all|all|0
n|(-inf-17640]|(-inf-1139.5]|all|(-inf-0.5]|all|all|0
w|(-inf-17640]|(-inf-1139.5]|all|(-inf-0.5]|all|all|0

## JRip

Decision list:

rules | predicted class
---|---
(gpuls >= 751) and (nbumps >= 3) and (gpuls <= 886) and (nbumps2 >= 2)|1 (4.0/0.0)
(nbumps >= 2) and (nbumps2 >= 1) and (gdpuls <= -4) and (gdenergy <= -30) and (gpuls >= 1255)|1 (8.0/0.0)
(nbumps >= 2) and (seismic = b) and (gdenergy >= -17) and (gdpuls >= 5) and (gdenergy <= 6) and (gdpuls <= 10)|1 (7.0/0.0)
(nbumps >= 2) and (gpuls >= 979) and (genergy >= 95180) and (genergy <= 107100)|1 (4.0/0.0)
(genergy >= 568200) and (nbumps2 >= 2) and (nbumps >= 5)|1 (4.0/0.0)
|0 (2293.0/123.0)


## PART

Decision list:

rules | predicted class
---|---
nbumps <= 1.0 AND gpuls <= 1252.0|0 (1314.0/30.0)
shift = W AND seismic = a|0 (206.0/33.0)
shift = W AND ghazard = a AND nbumps4 <= 0.0 AND genergy <= 117120.0|0 (75.0/15.0)
genergy <= 114540.0|0 (70.0/6.0)
nbumps2 <= 0.0|0 (36.0/8.0)
seismoacoustic = a AND nbumps <= 3.0|1 (15.0/4.0)
|0 (24.0/9.0)


## J48 Decision Tree

* nbumps <= 1
	* gpuls <= 1209: 0 (1746.0/43.0)
	* gpuls > 1209
		* nbumps3 <= 0: 0 (79.0/7.0)
		* nbumps3 > 0
			* seismic = a: 0 (12.0/2.0)
			* seismic = b: 1 (14.0/5.0)
			* seismic = c: 0 (0.0)
			* seismic = d: 0 (0.0)
* nbumps > 1
	* nbumps2 <= 0: 0 (82.0/6.0)
	* nbumps2 > 0
		* genergy <= 373180
			* nbumps3 <= 3: 0 (309.0/53.0)
			* nbumps3 > 3
				* gdenergy <= 22: 0 (9.0/2.0)
				* gdenergy > 22: 1 (8.0/3.0)
		* genergy > 373180
			* energy <= 5700: 0 (27.0/5.0)
			* energy > 5700
				* genergy <= 951410
					* energy <= 10300: 1 (9.0/1.0)
					* energy > 10300
						* gpuls <= 1848: 1 (9.0/3.0)
						* gpuls > 1848: 0 (8.0/2.0)
				* genergy > 951410: 0 (8.0/2.0)


## SimpleCart Decision Tree

* : 0(2170.0/150.0)


