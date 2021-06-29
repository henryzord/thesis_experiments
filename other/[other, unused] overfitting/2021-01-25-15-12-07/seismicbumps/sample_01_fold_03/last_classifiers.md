# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 0 | 0.934194 |
| nbumps > 1.5 and nbumps2 > 0.5 and seismic != a and genergy > 198310.0 and seismoacoustic = a and nbumps2 <= 1.5 and genergy > 412485.0 and gpuls > 2082.0 | 1 | 0.000828 |
| shift = W and gpuls <= 1139.5 and gdpuls = all and nbumps > 1.5 and nbumps2 > 0.5 and nbumps3 > 3.5 and nbumps4 > 0.5 and nbumps6 = all and nbumps7 = all and nbumps89 = all and energy > 550 and maxenergy > 350 | 1 | 0.000460 |
| nbumps > 1.5 and nbumps2 > 0.5 and seismic != a and genergy > 198310.0 and seismoacoustic = a and nbumps2 <= 1.5 and genergy <= 412485.0 | 1 | 0.001915 |
| shift = W and gpuls > 1139.5 and gdpuls = all and nbumps > 1.5 and nbumps2 <= 0.5 and nbumps3 > 3.5 and nbumps4 <= 0.5 and nbumps6 = all and nbumps7 = all and nbumps89 = all and energy > 550 and maxenergy > 350 | 1 | 0.000230 |
| nbumps > 1.5 and nbumps2 > 0.5 and seismic != a and genergy <= 198310.0 and nbumps3 <= 1.5 and shift = W and nbumps3 > 0.5 and genergy > 119765.0 | 1 | 0.001227 |
| shift = W and gpuls > 1139.5 and gdpuls = all and nbumps > 1.5 and nbumps2 > 0.5 and nbumps3 > 3.5 and nbumps4 <= 0.5 and nbumps6 = all and nbumps7 = all and nbumps89 = all and energy > 550 and maxenergy > 350 | 1 | 0.000460 |
| nbumps <= 1.5 and gpuls > 1210.0 and nbumps3 > 0.5 and seismic != a and gdenergy <= -28.0 | 1 | 0.001838 |
| nbumps <= 1.5 and gpuls > 1210.0 and nbumps3 > 0.5 and seismic != a and gdenergy > -28.0 and gdpuls > 2.0 | 1 | 0.001227 |
| nbumps > 1.5 and nbumps2 > 0.5 and seismic = a and seismoacoustic != c and shift != W and gpuls > 97.0 | 1 | 0.000828 |
| shift = N and gpuls <= 1139.5 and gdpuls = all and nbumps > 0.5 and nbumps <= 1.5 and nbumps2 <= 0.5 and nbumps3 <= 0.5 and nbumps4 <= 0.5 and nbumps6 = all and nbumps7 = all and nbumps89 = all and energy <= 550 and maxenergy <= 350 | 1 | 0.000460 |
| nbumps > 1.5 and nbumps2 > 0.5 and seismic != a and genergy <= 198310.0 and nbumps3 > 1.5 and seismoacoustic != a and gdenergy > 67.5 | 1 | 0.002297 |
| nbumps > 1.5 and nbumps2 > 0.5 and seismic != a and genergy <= 198310.0 and nbumps3 > 1.5 and seismoacoustic = a and nbumps2 <= 1.5 and nbumps4 <= 0.5 and energy > 10600.0 | 1 | 0.001035 |
| nbumps > 1.5 and nbumps2 > 0.5 and seismic != a and genergy > 198310.0 and seismoacoustic = a and nbumps2 > 1.5 | 1 | 0.002451 |
| nbumps > 1.5 and nbumps2 > 0.5 and seismic != a and genergy > 198310.0 and seismoacoustic != a and nbumps > 2.5 and gdenergy > 14.0 | 1 | 0.001035 |
| nbumps <= 1.5 and gpuls <= 1210.0 and seismoacoustic != c and shift != W and nbumps > 0.5 and nbumps3 <= 0.5 and nbumps2 <= 0.5 and gdenergy <= -48.5 | 1 | 0.001035 |
| nbumps > 1.5 and nbumps2 > 0.5 and seismic != a and genergy <= 198310.0 and nbumps3 > 1.5 and seismoacoustic != a and gdenergy <= 67.5 and genergy <= 41045.0 | 1 | 0.002362 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| nbumps <= 1.5 and gpuls <= 1210.0 | 0 | 0.916266 |
| seismic = a and seismoacoustic != c and nbumps2 > 0.5 and gdenergy > -36.0 | 0 | 0.476910 |
| nbumps2 <= 0.5 and shift = W and nbumps4 <= 0.5 and seismic = a | 0 | 0.252752 |
| shift = W and nbumps4 > 0.5 and nbumps2 <= 0.5 | 0 | 0.186716 |
| shift = W and seismic != a and maxenergy <= 1500.0 | 0 | 0.201970 |
| shift = W and nbumps > 1.5 and ghazard = a and nbumps4 > 0.5 and nbumps4 <= 1.5 and seismoacoustic != a | 0 | 0.069018 |
| shift = W and nbumps > 1.5 and gpuls <= 1136.0 and seismoacoustic != b and nbumps4 <= 0.5 and nbumps2 <= 1.5 | 0 | 0.168066 |
| shift = W and nbumps > 1.5 and seismic != a and ghazard = a and seismoacoustic != b and gpuls <= 750.0 | 0 | 0.095238 |
| shift != W | 0 | 0.059760 |
| seismoacoustic != a and seismic = a | 0 | 0.016027 |
| seismic = a and gpuls > 246.5 | 1 | 0.522523 |
| seismic != a and seismoacoustic != a and nbumps2 <= 1.5 and genergy > 58835.0 | 0 | 0.092308 |
| seismic != a and seismoacoustic != a and gdenergy <= 63.5 and genergy > 41045.0 | 0 | 0.055102 |
| seismoacoustic = a and nbumps3 > 1.5 | 0 | 0.085034 |
| nbumps3 <= 1.5 and nbumps3 > 0.5 and gpuls <= 1864.0 | 1 | 0.587903 |
| seismoacoustic = a | 0 | 0.102770 |
|  | 1 | 0.985507 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| nbumps >= 2 and gpuls >= 1003 and nbumps2 >= 1 and gdpuls <= -4 | 1 | 0.004879 |
| nbumps >= 3 and gpuls >= 679 and energy <= 12700 and maxenergy >= 5000 | 1 | 0.003673 |
|  | 0 | 0.946818 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

shift|gpuls|gdpuls|nbumps|nbumps2|nbumps3|nbumps4|nbumps6|nbumps7|nbumps89|energy|maxenergy|class
---|---|---|---|---|---|---|---|---|---|---|---|---
w|(1139.5-inf)|all|(1.5-inf)|(0.5-inf)|(3.5-inf)|(0.5-inf)|all|all|all|(550-inf)|(350-inf)|1
w|(-inf-1139.5]|all|(1.5-inf)|(0.5-inf)|(3.5-inf)|(0.5-inf)|all|all|all|(550-inf)|(350-inf)|1
w|(1139.5-inf)|all|(1.5-inf)|(0.5-inf)|(0.5-3.5]|(0.5-inf)|all|all|all|(550-inf)|(350-inf)|0
w|(1139.5-inf)|all|(1.5-inf)|(0.5-inf)|(3.5-inf)|(-inf-0.5]|all|all|all|(550-inf)|(350-inf)|1
w|(-inf-1139.5]|all|(1.5-inf)|(0.5-inf)|(0.5-3.5]|(0.5-inf)|all|all|all|(550-inf)|(350-inf)|0
w|(-inf-1139.5]|all|(1.5-inf)|(0.5-inf)|(3.5-inf)|(-inf-0.5]|all|all|all|(550-inf)|(350-inf)|0
w|(1139.5-inf)|all|(1.5-inf)|(-inf-0.5]|(0.5-3.5]|(0.5-inf)|all|all|all|(550-inf)|(350-inf)|0
w|(1139.5-inf)|all|(1.5-inf)|(-inf-0.5]|(3.5-inf)|(-inf-0.5]|all|all|all|(550-inf)|(350-inf)|1
w|(-inf-1139.5]|all|(1.5-inf)|(-inf-0.5]|(0.5-3.5]|(0.5-inf)|all|all|all|(550-inf)|(350-inf)|0
w|(1139.5-inf)|all|(1.5-inf)|(0.5-inf)|(-inf-0.5]|(0.5-inf)|all|all|all|(550-inf)|(350-inf)|0
w|(-inf-1139.5]|all|(1.5-inf)|(-inf-0.5]|(3.5-inf)|(-inf-0.5]|all|all|all|(550-inf)|(350-inf)|0
n|(-inf-1139.5]|all|(1.5-inf)|(0.5-inf)|(-inf-0.5]|(0.5-inf)|all|all|all|(550-inf)|(350-inf)|1
w|(-inf-1139.5]|all|(1.5-inf)|(0.5-inf)|(-inf-0.5]|(0.5-inf)|all|all|all|(550-inf)|(350-inf)|0
w|(1139.5-inf)|all|(1.5-inf)|(0.5-inf)|(0.5-3.5]|(-inf-0.5]|all|all|all|(550-inf)|(350-inf)|0
n|(-inf-1139.5]|all|(1.5-inf)|(0.5-inf)|(0.5-3.5]|(-inf-0.5]|all|all|all|(550-inf)|(350-inf)|0
w|(-inf-1139.5]|all|(1.5-inf)|(0.5-inf)|(0.5-3.5]|(-inf-0.5]|all|all|all|(550-inf)|(350-inf)|0
w|(1139.5-inf)|all|(1.5-inf)|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|all|all|all|(550-inf)|(350-inf)|0
n|(1139.5-inf)|all|(1.5-inf)|(-inf-0.5]|(0.5-3.5]|(-inf-0.5]|all|all|all|(550-inf)|(350-inf)|1
w|(1139.5-inf)|all|(1.5-inf)|(-inf-0.5]|(0.5-3.5]|(-inf-0.5]|all|all|all|(550-inf)|(350-inf)|0
w|(1139.5-inf)|all|(1.5-inf)|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|all|all|all|(550-inf)|(350-inf)|0
n|(-inf-1139.5]|all|(1.5-inf)|(-inf-0.5]|(0.5-3.5]|(-inf-0.5]|all|all|all|(550-inf)|(350-inf)|0
w|(-inf-1139.5]|all|(1.5-inf)|(-inf-0.5]|(0.5-3.5]|(-inf-0.5]|all|all|all|(550-inf)|(350-inf)|0
w|(1139.5-inf)|all|(0.5-1.5]|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|all|all|all|(550-inf)|(350-inf)|0
n|(-inf-1139.5]|all|(1.5-inf)|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|all|all|all|(550-inf)|(350-inf)|0
w|(-inf-1139.5]|all|(1.5-inf)|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|all|all|all|(550-inf)|(350-inf)|0
n|(-inf-1139.5]|all|(0.5-1.5]|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|all|all|all|(550-inf)|(350-inf)|0
w|(1139.5-inf)|all|(0.5-1.5]|(-inf-0.5]|(0.5-3.5]|(-inf-0.5]|all|all|all|(550-inf)|(350-inf)|0
w|(-inf-1139.5]|all|(0.5-1.5]|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|all|all|all|(550-inf)|(350-inf)|0
w|(1139.5-inf)|all|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|all|all|all|(550-inf)|(350-inf)|0
n|(-inf-1139.5]|all|(0.5-1.5]|(-inf-0.5]|(0.5-3.5]|(-inf-0.5]|all|all|all|(550-inf)|(350-inf)|0
w|(-inf-1139.5]|all|(0.5-1.5]|(-inf-0.5]|(0.5-3.5]|(-inf-0.5]|all|all|all|(550-inf)|(350-inf)|0
n|(-inf-1139.5]|all|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|all|all|all|(550-inf)|(350-inf)|0
w|(-inf-1139.5]|all|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|all|all|all|(550-inf)|(350-inf)|0
w|(-inf-1139.5]|all|(0.5-1.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|(550-inf)|(350-inf)|1
n|(-inf-1139.5]|all|(0.5-1.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|(550-inf)|(350-inf)|1
w|(1139.5-inf)|all|(1.5-inf)|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|all|all|all|(550-inf)|(-inf-350]|1
w|(-inf-1139.5]|all|(1.5-inf)|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|all|all|all|(-inf-550]|(350-inf)|1
w|(-inf-1139.5]|all|(1.5-inf)|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|all|all|all|(550-inf)|(-inf-350]|0
w|(1139.5-inf)|all|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|all|all|all|(-inf-550]|(350-inf)|0
w|(-inf-1139.5]|all|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|all|all|all|(-inf-550]|(350-inf)|0
n|(-inf-1139.5]|all|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|all|all|all|(-inf-550]|(350-inf)|0
w|(-inf-1139.5]|all|(1.5-inf)|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|all|all|all|(-inf-550]|(-inf-350]|0
n|(-inf-1139.5]|all|(1.5-inf)|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|all|all|all|(-inf-550]|(-inf-350]|0
w|(1139.5-inf)|all|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|all|all|all|(-inf-550]|(-inf-350]|0
w|(-inf-1139.5]|all|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|all|all|all|(-inf-550]|(-inf-350]|0
n|(-inf-1139.5]|all|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|all|all|all|(-inf-550]|(-inf-350]|0
n|(-inf-1139.5]|all|(0.5-1.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|(-inf-550]|(-inf-350]|1
n|(1139.5-inf)|all|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|(-inf-550]|(-inf-350]|0
w|(1139.5-inf)|all|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|(-inf-550]|(-inf-350]|0
w|(-inf-1139.5]|all|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|(-inf-550]|(-inf-350]|0
n|(-inf-1139.5]|all|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|(-inf-550]|(-inf-350]|0

## JRip

Decision list:

rules | predicted class
---|---
(nbumps >= 2) and (gpuls >= 1003) and (nbumps2 >= 1) and (gdpuls <= -4)|1 (34.0/15.0)
(nbumps >= 3) and (gpuls >= 679) and (energy <= 12700) and (maxenergy >= 5000)|1 (17.0/5.0)
|0 (2274.0/122.0)


## PART

Decision list:

rules | predicted class
---|---
nbumps <= 1.5 AND gpuls <= 1210.0|0 (1749.0/44.0)
seismic = a AND seismoacoustic != c AND nbumps2 > 0.5 AND gdenergy > -36.0|0 (183.0/24.0)
nbumps2 <= 0.5 AND shift = W AND nbumps4 <= 0.5 AND seismic = a|0 (70.0/5.0)
shift = W AND nbumps4 > 0.5 AND nbumps2 <= 0.5|0 (39.0/2.0)
shift = W AND seismic != a AND maxenergy <= 1500.0|0 (61.0/8.0)
shift = W AND nbumps > 1.5 AND ghazard = a AND nbumps4 > 0.5 AND nbumps4 <= 1.5 AND seismoacoustic != a|0 (20.0/5.0)
shift = W AND nbumps > 1.5 AND gpuls <= 1136.0 AND seismoacoustic != b AND nbumps4 <= 0.5 AND nbumps2 <= 1.5|0 (46.0/7.0)
shift = W AND nbumps > 1.5 AND seismic != a AND ghazard = a AND seismoacoustic != b AND gpuls <= 750.0|0 (21.0/1.0)
shift != W|0 (19.0/2.0)
seismoacoustic != a AND seismic = a|0 (13.0/4.0)
seismic = a AND gpuls > 246.5|1 (8.0)
seismic != a AND seismoacoustic != a AND nbumps2 <= 1.5 AND genergy > 58835.0|0 (13.0/1.0)
seismic != a AND seismoacoustic != a AND gdenergy <= 63.5 AND genergy > 41045.0|0 (12.0/3.0)
seismoacoustic = a AND nbumps3 > 1.5|0 (21.0/6.0)
nbumps3 <= 1.5 AND nbumps3 > 0.5 AND gpuls <= 1864.0|1 (19.0/4.0)
seismoacoustic = a|0 (21.0/8.0)
|1 (10.0)


## J48 Decision Tree

* nbumps <= 1.5
	* gpuls <= 1210.0
		* seismoacoustic = c: 0 (34.0)
		* seismoacoustic != c
			* shift = W: 0 (923.0/34.0)
			* shift != W
				* nbumps <= 0.5: 0 (618.0/4.0)
				* nbumps > 0.5
					* nbumps3 <= 0.5
						* nbumps2 <= 0.5
							* gdenergy <= -48.5: 1 (4.0/1.0)
							* gdenergy > -48.5: 0 (6.0)
						* nbumps2 > 0.5: 0 (52.0/1.0)
					* nbumps3 > 0.5: 0 (112.0/2.0)
	* gpuls > 1210.0
		* nbumps3 <= 0.5: 0 (79.0/7.0)
		* nbumps3 > 0.5
			* seismic = a: 0 (12.0/2.0)
			* seismic != a
				* gdenergy <= -28.0: 1 (4.0)
				* gdenergy > -28.0
					* gdpuls <= 2.0: 0 (4.0/1.0)
					* gdpuls > 2.0: 1 (6.0/2.0)
* nbumps > 1.5
	* nbumps2 <= 0.5: 0 (82.0/6.0)
	* nbumps2 > 0.5
		* seismic = a
			* seismoacoustic = c: 0 (4.0/1.0)
			* seismoacoustic != c
				* shift = W: 0 (195.0/33.0)
				* shift != W
					* gpuls <= 97.0: 0 (12.0)
					* gpuls > 97.0: 1 (5.0/2.0)
		* seismic != a
			* genergy <= 198310.0
				* nbumps3 <= 1.5
					* shift = W
						* nbumps3 <= 0.5: 0 (27.0/3.0)
						* nbumps3 > 0.5
							* genergy <= 119765.0: 0 (41.0/4.0)
							* genergy > 119765.0: 1 (6.0/2.0)
					* shift != W: 0 (4.0)
				* nbumps3 > 1.5
					* seismoacoustic = a
						* nbumps2 <= 1.5
							* nbumps4 <= 0.5
								* energy <= 10600.0: 0 (10.0/1.0)
								* energy > 10600.0: 1 (4.0/1.0)
							* nbumps4 > 0.5: 0 (6.0/1.0)
						* nbumps2 > 1.5: 0 (7.0)
					* seismoacoustic != a
						* gdenergy <= 67.5
							* genergy <= 41045.0: 1 (7.0/1.0)
							* genergy > 41045.0: 0 (16.0/1.0)
						* gdenergy > 67.5: 1 (5.0)
			* genergy > 198310.0
				* seismoacoustic = a
					* nbumps2 <= 1.5
						* genergy <= 412485.0: 1 (6.0/1.0)
						* genergy > 412485.0
							* gpuls <= 2082.0: 0 (5.0)
							* gpuls > 2082.0: 1 (5.0/2.0)
					* nbumps2 > 1.5: 1 (12.0/4.0)
				* seismoacoustic != a
					* nbumps <= 2.5: 0 (4.0)
					* nbumps > 2.5
						* gdenergy <= 14.0: 0 (4.0/1.0)
						* gdenergy > 14.0: 1 (4.0/1.0)


## SimpleCart Decision Tree

* : 0(2172.0/153.0)


