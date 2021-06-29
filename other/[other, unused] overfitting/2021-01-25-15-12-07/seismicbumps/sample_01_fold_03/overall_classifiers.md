# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| nbumps <= 1.5 and gpuls <= 1210 and nbumps4 <= 0.5 | 0 | 0.914956 |
| nbumps >= 1.5 and gpuls < 749.0 and seismoacoustic != d | 0 | 0.573318 |
| nbumps >= 1.5 and gpuls >= 749.0 and nbumps2 >= 0.5 and gdenergy >= -29.5 | 0 | 0.336111 |
| nbumps <= 1.5 and gpuls > 1210 and nbumps3 <= 0.5 | 0 | 0.301010 |
| nbumps >= 1.5 and gpuls >= 749.0 and nbumps2 < 0.5 | 0 | 0.197536 |
| nbumps > 1.5 and nbumps2 > 0.5 and seismic = b and genergy > 198310 and seismoacoustic = a | 1 | 0.004202 |
| nbumps <= 1.5 and gpuls <= 1210 and nbumps4 > 0.5 and gdpuls > -50.5 | 0 | 0.159341 |
| nbumps < 1.5 and gpuls >= 1342.0 and nbumps3 >= 0.5 | 1 | 0.002302 |
| nbumps > 1.5 and nbumps2 > 0.5 and seismic = b and genergy <= 198310 and nbumps3 > 1.5 and seismoacoustic = b and gdenergy <= 67.5 and genergy <= 41045 | 1 | 0.002362 |
| nbumps > 1.5 and nbumps2 > 0.5 and seismic = b and genergy <= 198310 and nbumps3 > 1.5 and seismoacoustic = b and gdenergy > 67.5 | 1 | 0.002297 |
| nbumps > 1.5 and nbumps2 > 0.5 and seismic = b and genergy <= 198310 and nbumps3 <= 1.5 and gdpuls <= 32 and gpuls > 764.5 and seismoacoustic = a and energy > 5800 | 1 | 0.001838 |
| nbumps >= 1.5 and gpuls >= 749.0 and nbumps2 >= 0.5 and gdenergy < -29.5 and gpuls >= 1201.0 | 1 | 0.003263 |
| nbumps > 1.5 and nbumps2 > 0.5 and seismic = b and genergy <= 198310 and nbumps3 > 1.5 and seismoacoustic = a and nbumps2 <= 1.5 and nbumps4 <= 0.5 and energy > 10600 | 1 | 0.001035 |
| seismoacoustic = a and genergy > 44750 and gpuls > 1139.5 and nbumps > 0.5 and nbumps <= 1.5 and nbumps2 <= 0.5 and nbumps4 <= 0.5 and maxenergy > 350 | 0 | 0.045860 |
| nbumps <= 1.5 and gpuls <= 1210 and nbumps4 > 0.5 and gdpuls <= -50.5 | 1 | 0.000920 |
| nbumps > 1.5 and nbumps2 > 0.5 and seismic = b and genergy > 198310 and seismoacoustic = b and gdpuls > 94.5 | 1 | 0.000920 |
| seismoacoustic = a and genergy > 44750 and gpuls <= 1139.5 and nbumps > 1.5 and nbumps2 > 0.5 and nbumps4 <= 0.5 and maxenergy <= 350 | 1 | 0.000460 |
| nbumps <= 1.5 and gpuls > 1210 and nbumps3 > 0.5 and seismic = b and seismoacoustic = b and energy > 2500 | 1 | 0.000920 |
| seismoacoustic = a and genergy <= 17640 and gpuls <= 1139.5 and nbumps > 0.5 and nbumps <= 1.5 and nbumps2 <= 0.5 and nbumps4 <= 0.5 and maxenergy <= 350 | 1 | 0.000460 |
| seismoacoustic = c and genergy > 44750 and gpuls > 1139.5 and nbumps > 1.5 and nbumps2 > 0.5 and nbumps4 <= 0.5 and maxenergy > 350 | 1 | 0.000154 |
| seismoacoustic = c and genergy > 44750 and gpuls > 1139.5 and nbumps > 1.5 and nbumps2 <= 0.5 and nbumps4 > 0.5 and maxenergy > 350 | 1 | 0.000460 |
| nbumps >= 1.5 and gpuls >= 749.0 and nbumps2 >= 0.5 and gdenergy < -29.5 and gpuls < 1201.0 | 0 | 0.028555 |
| seismoacoustic = b and genergy > 44750 and gpuls > 1139.5 and nbumps > 0.5 and nbumps <= 1.5 and nbumps2 <= 0.5 and nbumps4 <= 0.5 and maxenergy > 350 | 0 | 0.031210 |
| nbumps > 1.5 and nbumps2 > 0.5 and seismic = b and genergy > 198310 and seismoacoustic = b and gdpuls <= 94.5 | 0 | 0.028662 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| nbumps <= 1.5 | 0 | 0.919848 |
| nbumps2 > 0.5 and seismic = a | 0 | 0.498894 |
| nbumps2 > 0.5 and genergy <= 189280 | 0 | 0.332071 |
| nbumps2 <= 0.5 | 0 | 0.251678 |
| nbumps2 <= 1.5 | 0 | 0.027230 |
|  | 1 | 0.950311 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| nbumps >= 2 and gpuls >= 751 and nbumps2 >= 1 and energy >= 5800 and energy <= 12700 and gpuls <= 1946 and genergy >= 122640 | 1 | 0.003212 |
| nbumps >= 2 and gpuls >= 1003 and gdpuls <= -4 and energy <= 3700 | 1 | 0.003099 |
| nbumps >= 3 and seismic = b and gdenergy >= 95 | 1 | 0.002252 |
| maxenergy >= 4000 and gdpuls <= 19 and nbumps >= 3 and gdpuls >= 0 | 1 | 0.002532 |
| nbumps >= 2 and genergy <= 21760 and genergy >= 18960 | 1 | 0.001505 |
| genergy >= 40070 and gpuls >= 1140 and nbumps3 >= 1 and gpuls <= 1890 | 1 | 0.003267 |
|  | 0 | 0.960212 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

seismoacoustic|genergy|gpuls|nbumps|nbumps2|nbumps4|maxenergy|class
---|---|---|---|---|---|---|---
c|(44750-inf)|(1139.5-inf)|(1.5-inf)|(0.5-inf)|(0.5-inf)|(350-inf)|1
b|(44750-inf)|(1139.5-inf)|(1.5-inf)|(0.5-inf)|(0.5-inf)|(350-inf)|0
a|(44750-inf)|(1139.5-inf)|(1.5-inf)|(0.5-inf)|(0.5-inf)|(350-inf)|0
c|(44750-inf)|(-inf-1139.5]|(1.5-inf)|(0.5-inf)|(0.5-inf)|(350-inf)|1
a|(44750-inf)|(-inf-1139.5]|(1.5-inf)|(0.5-inf)|(0.5-inf)|(350-inf)|0
b|(44750-inf)|(-inf-1139.5]|(1.5-inf)|(0.5-inf)|(0.5-inf)|(350-inf)|0
b|(17640-44750]|(-inf-1139.5]|(1.5-inf)|(0.5-inf)|(0.5-inf)|(350-inf)|0
a|(17640-44750]|(-inf-1139.5]|(1.5-inf)|(0.5-inf)|(0.5-inf)|(350-inf)|0
c|(44750-inf)|(1139.5-inf)|(1.5-inf)|(-inf-0.5]|(0.5-inf)|(350-inf)|1
b|(-inf-17640]|(-inf-1139.5]|(1.5-inf)|(0.5-inf)|(0.5-inf)|(350-inf)|1
b|(44750-inf)|(1139.5-inf)|(1.5-inf)|(-inf-0.5]|(0.5-inf)|(350-inf)|0
a|(-inf-17640]|(-inf-1139.5]|(1.5-inf)|(0.5-inf)|(0.5-inf)|(350-inf)|0
a|(44750-inf)|(1139.5-inf)|(1.5-inf)|(-inf-0.5]|(0.5-inf)|(350-inf)|0
c|(44750-inf)|(1139.5-inf)|(1.5-inf)|(0.5-inf)|(-inf-0.5]|(350-inf)|1
a|(44750-inf)|(1139.5-inf)|(1.5-inf)|(0.5-inf)|(-inf-0.5]|(350-inf)|0
b|(44750-inf)|(1139.5-inf)|(1.5-inf)|(0.5-inf)|(-inf-0.5]|(350-inf)|0
a|(44750-inf)|(-inf-1139.5]|(1.5-inf)|(-inf-0.5]|(0.5-inf)|(350-inf)|0
b|(17640-44750]|(1139.5-inf)|(1.5-inf)|(0.5-inf)|(-inf-0.5]|(350-inf)|1
b|(44750-inf)|(-inf-1139.5]|(1.5-inf)|(-inf-0.5]|(0.5-inf)|(350-inf)|0
a|(17640-44750]|(-inf-1139.5]|(1.5-inf)|(-inf-0.5]|(0.5-inf)|(350-inf)|0
b|(44750-inf)|(1139.5-inf)|(0.5-1.5]|(-inf-0.5]|(0.5-inf)|(350-inf)|0
b|(17640-44750]|(-inf-1139.5]|(1.5-inf)|(-inf-0.5]|(0.5-inf)|(350-inf)|0
b|(44750-inf)|(-inf-1139.5]|(1.5-inf)|(0.5-inf)|(-inf-0.5]|(350-inf)|0
a|(44750-inf)|(1139.5-inf)|(0.5-1.5]|(-inf-0.5]|(0.5-inf)|(350-inf)|0
a|(44750-inf)|(-inf-1139.5]|(1.5-inf)|(0.5-inf)|(-inf-0.5]|(350-inf)|0
b|(44750-inf)|(1139.5-inf)|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|(350-inf)|1
c|(17640-44750]|(-inf-1139.5]|(1.5-inf)|(0.5-inf)|(-inf-0.5]|(350-inf)|1
a|(44750-inf)|(1139.5-inf)|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|(350-inf)|0
a|(17640-44750]|(-inf-1139.5]|(1.5-inf)|(0.5-inf)|(-inf-0.5]|(350-inf)|0
b|(17640-44750]|(-inf-1139.5]|(1.5-inf)|(0.5-inf)|(-inf-0.5]|(350-inf)|0
a|(17640-44750]|(1139.5-inf)|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|(350-inf)|1
a|(44750-inf)|(1139.5-inf)|(1.5-inf)|(-inf-0.5]|(-inf-0.5]|(350-inf)|0
b|(44750-inf)|(1139.5-inf)|(1.5-inf)|(-inf-0.5]|(-inf-0.5]|(350-inf)|0
a|(-inf-17640]|(-inf-1139.5]|(1.5-inf)|(0.5-inf)|(-inf-0.5]|(350-inf)|0
b|(44750-inf)|(-inf-1139.5]|(0.5-1.5]|(-inf-0.5]|(0.5-inf)|(350-inf)|0
b|(-inf-17640]|(-inf-1139.5]|(1.5-inf)|(0.5-inf)|(-inf-0.5]|(350-inf)|0
a|(44750-inf)|(-inf-1139.5]|(0.5-1.5]|(-inf-0.5]|(0.5-inf)|(350-inf)|0
c|(44750-inf)|(-inf-1139.5]|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|(350-inf)|0
a|(44750-inf)|(-inf-1139.5]|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|(350-inf)|0
b|(44750-inf)|(-inf-1139.5]|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|(350-inf)|0
b|(17640-44750]|(-inf-1139.5]|(0.5-1.5]|(-inf-0.5]|(0.5-inf)|(350-inf)|0
a|(17640-44750]|(-inf-1139.5]|(0.5-1.5]|(-inf-0.5]|(0.5-inf)|(350-inf)|0
b|(-inf-17640]|(-inf-1139.5]|(0.5-1.5]|(-inf-0.5]|(0.5-inf)|(350-inf)|0
c|(44750-inf)|(-inf-1139.5]|(1.5-inf)|(-inf-0.5]|(-inf-0.5]|(350-inf)|1
a|(44750-inf)|(1139.5-inf)|(1.5-inf)|(0.5-inf)|(-inf-0.5]|(-inf-350]|1
b|(44750-inf)|(-inf-1139.5]|(1.5-inf)|(-inf-0.5]|(-inf-0.5]|(350-inf)|0
b|(17640-44750]|(-inf-1139.5]|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|(350-inf)|0
c|(17640-44750]|(-inf-1139.5]|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|(350-inf)|0
a|(44750-inf)|(-inf-1139.5]|(1.5-inf)|(-inf-0.5]|(-inf-0.5]|(350-inf)|0
a|(-inf-17640]|(-inf-1139.5]|(0.5-1.5]|(-inf-0.5]|(0.5-inf)|(350-inf)|0
a|(17640-44750]|(-inf-1139.5]|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|(350-inf)|0
b|(17640-44750]|(-inf-1139.5]|(1.5-inf)|(-inf-0.5]|(-inf-0.5]|(350-inf)|0
a|(17640-44750]|(-inf-1139.5]|(1.5-inf)|(-inf-0.5]|(-inf-0.5]|(350-inf)|0
b|(44750-inf)|(1139.5-inf)|(0.5-1.5]|(-inf-0.5]|(-inf-0.5]|(350-inf)|0
b|(-inf-17640]|(-inf-1139.5]|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|(350-inf)|0
a|(44750-inf)|(1139.5-inf)|(0.5-1.5]|(-inf-0.5]|(-inf-0.5]|(350-inf)|0
a|(-inf-17640]|(-inf-1139.5]|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|(350-inf)|0
a|(44750-inf)|(-inf-1139.5]|(1.5-inf)|(0.5-inf)|(-inf-0.5]|(-inf-350]|1
b|(17640-44750]|(1139.5-inf)|(0.5-1.5]|(-inf-0.5]|(-inf-0.5]|(350-inf)|1
a|(-inf-17640]|(-inf-1139.5]|(1.5-inf)|(-inf-0.5]|(-inf-0.5]|(350-inf)|1
a|(17640-44750]|(1139.5-inf)|(0.5-1.5]|(-inf-0.5]|(-inf-0.5]|(350-inf)|1
b|(44750-inf)|(-inf-1139.5]|(1.5-inf)|(0.5-inf)|(-inf-0.5]|(-inf-350]|0
b|(44750-inf)|(1139.5-inf)|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|(-inf-350]|0
a|(17640-44750]|(-inf-1139.5]|(1.5-inf)|(0.5-inf)|(-inf-0.5]|(-inf-350]|0
b|(17640-44750]|(-inf-1139.5]|(1.5-inf)|(0.5-inf)|(-inf-0.5]|(-inf-350]|1
c|(44750-inf)|(-inf-1139.5]|(0.5-1.5]|(-inf-0.5]|(-inf-0.5]|(350-inf)|0
a|(44750-inf)|(-inf-1139.5]|(0.5-1.5]|(-inf-0.5]|(-inf-0.5]|(350-inf)|0
b|(44750-inf)|(-inf-1139.5]|(0.5-1.5]|(-inf-0.5]|(-inf-0.5]|(350-inf)|0
a|(44750-inf)|(1139.5-inf)|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|(-inf-350]|0
b|(17640-44750]|(1139.5-inf)|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|(-inf-350]|1
a|(-inf-17640]|(-inf-1139.5]|(1.5-inf)|(0.5-inf)|(-inf-0.5]|(-inf-350]|1
c|(17640-44750]|(-inf-1139.5]|(0.5-1.5]|(-inf-0.5]|(-inf-0.5]|(350-inf)|0
b|(17640-44750]|(-inf-1139.5]|(0.5-1.5]|(-inf-0.5]|(-inf-0.5]|(350-inf)|0
a|(17640-44750]|(-inf-1139.5]|(0.5-1.5]|(-inf-0.5]|(-inf-0.5]|(350-inf)|0
c|(44750-inf)|(-inf-1139.5]|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|(-inf-350]|0
a|(44750-inf)|(-inf-1139.5]|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|(-inf-350]|0
a|(-inf-17640]|(-inf-1139.5]|(0.5-1.5]|(-inf-0.5]|(-inf-0.5]|(350-inf)|0
b|(44750-inf)|(-inf-1139.5]|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|(-inf-350]|0
b|(-inf-17640]|(-inf-1139.5]|(0.5-1.5]|(-inf-0.5]|(-inf-0.5]|(350-inf)|0
b|(17640-44750]|(-inf-1139.5]|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|(-inf-350]|0
a|(17640-44750]|(-inf-1139.5]|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|(-inf-350]|0
a|(-inf-17640]|(-inf-1139.5]|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|(-inf-350]|0
b|(-inf-17640]|(-inf-1139.5]|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|(-inf-350]|0
b|(44750-inf)|(1139.5-inf)|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-350]|0
a|(44750-inf)|(1139.5-inf)|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-350]|0
a|(-inf-17640]|(-inf-1139.5]|(0.5-1.5]|(-inf-0.5]|(-inf-0.5]|(-inf-350]|1
a|(17640-44750]|(1139.5-inf)|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-350]|1
b|(17640-44750]|(1139.5-inf)|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-350]|0
c|(44750-inf)|(-inf-1139.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-350]|0
b|(44750-inf)|(-inf-1139.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-350]|0
a|(44750-inf)|(-inf-1139.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-350]|0
c|(17640-44750]|(-inf-1139.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-350]|0
a|(17640-44750]|(-inf-1139.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-350]|0
b|(17640-44750]|(-inf-1139.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-350]|0
c|(-inf-17640]|(-inf-1139.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-350]|1
a|(-inf-17640]|(-inf-1139.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-350]|0
b|(-inf-17640]|(-inf-1139.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-350]|0

## JRip

Decision list:

rules | predicted class
---|---
(nbumps >= 2) and (gpuls >= 751) and (nbumps2 >= 1) and (energy >= 5800) and (energy <= 12700) and (gpuls <= 1946) and (genergy >= 122640)|1 (7.0/0.0)
(nbumps >= 2) and (gpuls >= 1003) and (gdpuls <= -4) and (energy <= 3700)|1 (12.0/3.0)
(nbumps >= 3) and (seismic = b) and (gdenergy >= 95)|1 (10.0/3.0)
(maxenergy >= 4000) and (gdpuls <= 19) and (nbumps >= 3) and (gdpuls >= 0)|1 (22.0/11.0)
(nbumps >= 2) and (genergy <= 21760) and (genergy >= 18960)|1 (15.0/8.0)
(genergy >= 40070) and (gpuls >= 1140) and (nbumps3 >= 1) and (gpuls <= 1890)|1 (67.0/45.0)
|0 (2192.0/90.0)


## PART

Decision list:

rules | predicted class
---|---
nbumps <= 1.5|0 (1615.0/56.0)
nbumps2 > 0.5 AND seismic = a|0 (195.0/31.0)
nbumps2 > 0.5 AND genergy <= 189280|0 (114.0/23.0)
nbumps2 <= 0.5|0 (73.0/5.0)
nbumps2 <= 1.5|0 (22.0/9.0)
|1 (16.0/6.0)


## J48 Decision Tree

* nbumps <= 1.5
	* gpuls <= 1210
		* nbumps4 <= 0.5: 0 (1718.0/42.0)
		* nbumps4 > 0.5
			* gdpuls <= -50.5: 1 (2.0)
			* gdpuls > -50.5: 0 (29.0)
	* gpuls > 1210
		* nbumps3 <= 0.5: 0 (79.0/7.0)
		* nbumps3 > 0.5
			* seismic = a: 0 (12.0/2.0)
			* seismic = b
				* seismoacoustic = a
					* genergy <= 434770: 1 (6.0)
					* genergy > 434770: 0 (4.0/1.0)
				* seismoacoustic = b
					* energy <= 2500: 0 (2.0)
					* energy > 2500: 1 (2.0)
				* seismoacoustic = c: 1 (0.0)
				* seismoacoustic = d: 1 (0.0)
			* seismic = c: 0 (0.0)
			* seismic = d: 0 (0.0)
* nbumps > 1.5
	* nbumps2 <= 0.5: 0 (82.0/6.0)
	* nbumps2 > 0.5
		* seismic = a: 0 (216.0/37.0)
		* seismic = b
			* genergy <= 198310
				* nbumps3 <= 1.5
					* gdpuls <= 32
						* gpuls <= 764.5: 0 (38.0/4.0)
						* gpuls > 764.5
							* seismoacoustic = a
								* energy <= 5800: 0 (4.0/1.0)
								* energy > 5800: 1 (4.0)
							* seismoacoustic = b: 0 (4.0/1.0)
							* seismoacoustic = c: 1 (0.0)
							* seismoacoustic = d: 1 (0.0)
					* gdpuls > 32: 0 (28.0/1.0)
				* nbumps3 > 1.5
					* seismoacoustic = a
						* nbumps2 <= 1.5
							* nbumps4 <= 0.5
								* energy <= 10600: 0 (10.0/1.0)
								* energy > 10600: 1 (4.0/1.0)
							* nbumps4 > 0.5: 0 (6.0/1.0)
						* nbumps2 > 1.5: 0 (7.0)
					* seismoacoustic = b
						* gdenergy <= 67.5
							* genergy <= 41045: 1 (7.0/1.0)
							* genergy > 41045: 0 (16.0/1.0)
						* gdenergy > 67.5: 1 (5.0)
					* seismoacoustic = c: 0 (0.0)
					* seismoacoustic = d: 0 (0.0)
			* genergy > 198310
				* seismoacoustic = a: 1 (28.0/12.0)
				* seismoacoustic = b
					* gdpuls <= 94.5: 0 (8.0/2.0)
					* gdpuls > 94.5: 1 (2.0)
				* seismoacoustic = c: 0 (2.0)
				* seismoacoustic = d: 1 (0.0)
		* seismic = c: 0 (0.0)
		* seismic = d: 0 (0.0)


## SimpleCart Decision Tree

* nbumps < 1.5
	* gpuls < 1342.0
		* genergy < 16885.0
			* energy < 3500.0
				* gdenergy < -84.5: 0(25.0/1.0)
				* gdenergy >= -84.5
					* gpuls < 219.0: 0(429.0/4.0)
					* gpuls >= 219.0: 0(297.0/0.0)
			* energy >= 3500.0: 0(30.0/3.0)
		* genergy >= 16885.0: 0(946.0/38.0)
	* gpuls >= 1342.0
		* nbumps3 < 0.5: 0(55.0/6.0)
		* nbumps3 >= 0.5: 1(10.0/10.0)
* nbumps >= 1.5
	* gpuls < 749.0
				* seismoacoustic=(c)|(a)|(d): 0(150.0/16.0)
				* seismoacoustic!=(c)|(a)|(d): 0(81.0/22.0)
	* gpuls >= 749.0
		* nbumps2 < 0.5: 0(42.0/5.0)
		* nbumps2 >= 0.5
			* gdenergy < -29.5
				* gpuls < 1201.0: 0(7.0/4.0)
				* gpuls >= 1201.0: 1(8.0/1.0)
			* gdenergy >= -29.5: 0(99.0/36.0)


