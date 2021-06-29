# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| nbumps <= 1 and gpuls <= 1209 | 0 | 0.916121 |
| nbumps > 1 | 0 | 0.693531 |
| nbumps <= 1 and gpuls > 1209 and nbumps3 <= 0 | 0 | 0.304167 |
| nbumps >= 1.5 and gpuls >= 740.5 and gdenergy < -29.5 and nbumps2 >= 0.5 | 1 | 0.004913 |
| nbumps <= 1 and gpuls > 1209 and nbumps3 > 0 and seismic = b | 1 | 0.002263 |
| seismic = a and shift = W and gpuls > 1142.5 and gdenergy = all and nbumps <= 1.5 and nbumps2 <= 0.5 and nbumps4 <= 0.5 and nbumps5 = all and nbumps6 = all and nbumps7 = all and nbumps89 = all and energy > 550 | 0 | 0.089636 |
| seismic = a and shift = N and gpuls > 54.5 and gpuls <= 1142.5 and gdenergy = all and nbumps <= 1.5 and nbumps2 <= 0.5 and nbumps4 > 0.5 and nbumps5 = all and nbumps6 = all and nbumps7 = all and nbumps89 = all and energy > 550 | 1 | 0.000154 |
| seismic = a and shift = W and gpuls > 1142.5 and gdenergy = all and nbumps > 1.5 and nbumps2 <= 0.5 and nbumps4 > 0.5 and nbumps5 = all and nbumps6 = all and nbumps7 = all and nbumps89 = all and energy > 550 | 1 | 0.000230 |
| seismic = b and shift = N and gpuls > 54.5 and gpuls <= 1142.5 and gdenergy = all and nbumps > 1.5 and nbumps2 > 0.5 and nbumps4 <= 0.5 and nbumps5 = all and nbumps6 = all and nbumps7 = all and nbumps89 = all and energy > 550 | 1 | 0.000154 |
| nbumps < 1.5 and gpuls >= 1342.5 and nbumps3 >= 0.5 | 0 | 0.030940 |
| nbumps < 1.5 and gpuls < 1342.5 and genergy >= 16885.0 | 0 | 0.856984 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| nbumps <= 1 and gpuls <= 1333 | 0 | 0.917267 |
| seismic = a | 0 | 0.593859 |
| gdpuls > 35 and ghazard = a | 0 | 0.223084 |
| nbumps2 > 0 and seismoacoustic = a and genergy <= 186280 | 0 | 0.164746 |
| nbumps2 <= 0 | 0 | 0.115842 |
| seismoacoustic = a and nbumps4 <= 0 | 1 | 0.656596 |
| nbumps3 <= 1 | 0 | 0.245935 |
| genergy > 49520 and gdenergy > -15 | 1 | 0.749554 |
| genergy <= 54990 | 1 | 0.780488 |
|  | 0 | 0.500000 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| nbumps >= 2 and gpuls >= 744 and gdenergy <= -30 and nbumps2 >= 1 and maxenergy >= 2000 and nbumps4 <= 0 | 1 | 0.005495 |
| nbumps >= 2 and genergy >= 306400 and nbumps2 >= 2 and seismic = b and gdenergy >= 5 and genergy <= 788650 | 1 | 0.001838 |
| nbumps >= 2 and genergy >= 320110 and maxenergy >= 6000 and energy <= 9700 | 1 | 0.001838 |
| nbumps >= 3 and gpuls >= 679 and gdpuls >= 90 and nbumps3 >= 2 | 1 | 0.001838 |
|  | 0 | 0.943937 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

seismic|shift|gpuls|gdenergy|nbumps|nbumps2|nbumps4|nbumps5|nbumps6|nbumps7|nbumps89|energy|class
---|---|---|---|---|---|---|---|---|---|---|---|---
a|w|(1142.5-inf)|all|(1.5-inf)|(0.5-inf)|(0.5-inf)|all|all|all|all|(550-inf)|0
b|w|(1142.5-inf)|all|(1.5-inf)|(0.5-inf)|(0.5-inf)|all|all|all|all|(550-inf)|0
b|n|(54.5-1142.5]|all|(1.5-inf)|(0.5-inf)|(0.5-inf)|all|all|all|all|(550-inf)|1
a|w|(54.5-1142.5]|all|(1.5-inf)|(0.5-inf)|(0.5-inf)|all|all|all|all|(550-inf)|0
b|w|(54.5-1142.5]|all|(1.5-inf)|(0.5-inf)|(0.5-inf)|all|all|all|all|(550-inf)|0
a|w|(1142.5-inf)|all|(1.5-inf)|(-inf-0.5]|(0.5-inf)|all|all|all|all|(550-inf)|1
b|w|(1142.5-inf)|all|(1.5-inf)|(-inf-0.5]|(0.5-inf)|all|all|all|all|(550-inf)|0
b|w|(1142.5-inf)|all|(1.5-inf)|(0.5-inf)|(-inf-0.5]|all|all|all|all|(550-inf)|0
a|w|(1142.5-inf)|all|(1.5-inf)|(0.5-inf)|(-inf-0.5]|all|all|all|all|(550-inf)|0
b|n|(54.5-1142.5]|all|(1.5-inf)|(0.5-inf)|(-inf-0.5]|all|all|all|all|(550-inf)|1
a|w|(54.5-1142.5]|all|(1.5-inf)|(-inf-0.5]|(0.5-inf)|all|all|all|all|(550-inf)|0
b|w|(54.5-1142.5]|all|(1.5-inf)|(-inf-0.5]|(0.5-inf)|all|all|all|all|(550-inf)|0
a|n|(54.5-1142.5]|all|(1.5-inf)|(0.5-inf)|(-inf-0.5]|all|all|all|all|(550-inf)|0
b|w|(54.5-1142.5]|all|(1.5-inf)|(0.5-inf)|(-inf-0.5]|all|all|all|all|(550-inf)|0
a|w|(54.5-1142.5]|all|(1.5-inf)|(0.5-inf)|(-inf-0.5]|all|all|all|all|(550-inf)|0
a|n|(-inf-54.5]|all|(1.5-inf)|(0.5-inf)|(-inf-0.5]|all|all|all|all|(550-inf)|0
b|w|(1142.5-inf)|all|(-inf-1.5]|(-inf-0.5]|(0.5-inf)|all|all|all|all|(550-inf)|0
b|w|(1142.5-inf)|all|(-inf-1.5]|(0.5-inf)|(-inf-0.5]|all|all|all|all|(550-inf)|1
a|n|(54.5-1142.5]|all|(-inf-1.5]|(-inf-0.5]|(0.5-inf)|all|all|all|all|(550-inf)|1
b|n|(54.5-1142.5]|all|(-inf-1.5]|(-inf-0.5]|(0.5-inf)|all|all|all|all|(550-inf)|0
a|w|(1142.5-inf)|all|(-inf-1.5]|(0.5-inf)|(-inf-0.5]|all|all|all|all|(550-inf)|0
b|n|(54.5-1142.5]|all|(-inf-1.5]|(0.5-inf)|(-inf-0.5]|all|all|all|all|(550-inf)|0
a|w|(1142.5-inf)|all|(1.5-inf)|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(550-inf)|0
b|w|(1142.5-inf)|all|(1.5-inf)|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(550-inf)|0
b|w|(54.5-1142.5]|all|(-inf-1.5]|(-inf-0.5]|(0.5-inf)|all|all|all|all|(550-inf)|0
a|w|(54.5-1142.5]|all|(-inf-1.5]|(-inf-0.5]|(0.5-inf)|all|all|all|all|(550-inf)|0
a|n|(54.5-1142.5]|all|(-inf-1.5]|(0.5-inf)|(-inf-0.5]|all|all|all|all|(550-inf)|0
a|n|(54.5-1142.5]|all|(1.5-inf)|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(550-inf)|0
b|n|(54.5-1142.5]|all|(1.5-inf)|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(550-inf)|1
a|w|(54.5-1142.5]|all|(-inf-1.5]|(0.5-inf)|(-inf-0.5]|all|all|all|all|(550-inf)|0
b|w|(54.5-1142.5]|all|(-inf-1.5]|(0.5-inf)|(-inf-0.5]|all|all|all|all|(550-inf)|0
a|n|(-inf-54.5]|all|(-inf-1.5]|(0.5-inf)|(-inf-0.5]|all|all|all|all|(550-inf)|0
b|w|(54.5-1142.5]|all|(1.5-inf)|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(550-inf)|0
a|w|(54.5-1142.5]|all|(1.5-inf)|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(550-inf)|0
a|w|(-inf-54.5]|all|(-inf-1.5]|(0.5-inf)|(-inf-0.5]|all|all|all|all|(550-inf)|1
a|w|(1142.5-inf)|all|(-inf-1.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(550-inf)|0
b|w|(1142.5-inf)|all|(-inf-1.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(550-inf)|1
b|n|(54.5-1142.5]|all|(-inf-1.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(550-inf)|0
a|n|(54.5-1142.5]|all|(-inf-1.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(550-inf)|0
b|w|(54.5-1142.5]|all|(-inf-1.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(550-inf)|0
a|w|(54.5-1142.5]|all|(-inf-1.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(550-inf)|0
a|n|(54.5-1142.5]|all|(1.5-inf)|(0.5-inf)|(-inf-0.5]|all|all|all|all|(-inf-550]|1
a|n|(-inf-54.5]|all|(-inf-1.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(550-inf)|0
b|n|(54.5-1142.5]|all|(1.5-inf)|(0.5-inf)|(-inf-0.5]|all|all|all|all|(-inf-550]|1
a|w|(-inf-54.5]|all|(-inf-1.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(550-inf)|0
a|w|(54.5-1142.5]|all|(1.5-inf)|(0.5-inf)|(-inf-0.5]|all|all|all|all|(-inf-550]|0
b|w|(54.5-1142.5]|all|(1.5-inf)|(0.5-inf)|(-inf-0.5]|all|all|all|all|(-inf-550]|0
a|w|(1142.5-inf)|all|(-inf-1.5]|(0.5-inf)|(-inf-0.5]|all|all|all|all|(-inf-550]|0
b|w|(1142.5-inf)|all|(-inf-1.5]|(0.5-inf)|(-inf-0.5]|all|all|all|all|(-inf-550]|0
b|n|(54.5-1142.5]|all|(-inf-1.5]|(0.5-inf)|(-inf-0.5]|all|all|all|all|(-inf-550]|0
a|n|(54.5-1142.5]|all|(-inf-1.5]|(0.5-inf)|(-inf-0.5]|all|all|all|all|(-inf-550]|0
b|w|(54.5-1142.5]|all|(-inf-1.5]|(0.5-inf)|(-inf-0.5]|all|all|all|all|(-inf-550]|0
a|w|(54.5-1142.5]|all|(-inf-1.5]|(0.5-inf)|(-inf-0.5]|all|all|all|all|(-inf-550]|0
a|n|(-inf-54.5]|all|(-inf-1.5]|(0.5-inf)|(-inf-0.5]|all|all|all|all|(-inf-550]|0
a|n|(1142.5-inf)|all|(-inf-1.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(-inf-550]|1
b|n|(1142.5-inf)|all|(-inf-1.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(-inf-550]|1
a|w|(1142.5-inf)|all|(-inf-1.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(-inf-550]|0
b|w|(1142.5-inf)|all|(-inf-1.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(-inf-550]|0
a|n|(54.5-1142.5]|all|(-inf-1.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(-inf-550]|0
b|n|(54.5-1142.5]|all|(-inf-1.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(-inf-550]|0
b|w|(54.5-1142.5]|all|(-inf-1.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(-inf-550]|0
a|w|(54.5-1142.5]|all|(-inf-1.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(-inf-550]|0
b|n|(-inf-54.5]|all|(-inf-1.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(-inf-550]|1
a|n|(-inf-54.5]|all|(-inf-1.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(-inf-550]|0

## JRip

Decision list:

rules | predicted class
---|---
(nbumps >= 2) and (gpuls >= 744) and (gdenergy <= -30) and (nbumps2 >= 1) and (maxenergy >= 2000) and (nbumps4 <= 0)|1 (12.0/0.0)
(nbumps >= 2) and (genergy >= 306400) and (nbumps2 >= 2) and (seismic = b) and (gdenergy >= 5) and (genergy <= 788650)|1 (4.0/0.0)
(nbumps >= 2) and (genergy >= 320110) and (maxenergy >= 6000) and (energy <= 9700)|1 (4.0/0.0)
(nbumps >= 3) and (gpuls >= 679) and (gdpuls >= 90) and (nbumps3 >= 2)|1 (4.0/0.0)
|0 (2301.0/129.0)


## PART

Decision list:

rules | predicted class
---|---
nbumps <= 1 AND gpuls <= 1333|0 (1778.0/49.0)
seismic = a|0 (304.0/47.0)
gdpuls > 35 AND ghazard = a|0 (64.0/5.0)
nbumps2 > 0 AND seismoacoustic = a AND genergy <= 186280|0 (55.0/9.0)
nbumps2 <= 0|0 (47.0/8.0)
seismoacoustic = a AND nbumps4 <= 0|1 (11.0/3.0)
nbumps3 <= 1|0 (45.0/14.0)
genergy > 49520 AND gdenergy > -15|1 (9.0/3.0)
genergy <= 54990|1 (6.0)
|0 (6.0/1.0)


## J48 Decision Tree

* nbumps <= 1
	* gpuls <= 1209: 0 (1574.0/42.0)
	* gpuls > 1209
		* nbumps3 <= 0: 0 (74.0/7.0)
		* nbumps3 > 0
			* seismic = a: 0 (12.0/1.0)
			* seismic = b: 1 (10.0/4.0)
			* seismic = c: 0 (0.0)
			* seismic = d: 0 (0.0)
* nbumps > 1: 0 (423.0/82.0)


## SimpleCart Decision Tree

* nbumps < 1.5
	* gpuls < 1342.5
		* genergy < 16885.0: 0(784.0/10.0)
		* genergy >= 16885.0: 0(945.0/39.0)
	* gpuls >= 1342.5
		* nbumps3 < 0.5: 0(54.0/6.0)
		* nbumps3 >= 0.5: 0(9.0/8.0)
* nbumps >= 1.5
	* gpuls < 740.5: 0(233.0/36.0)
	* gpuls >= 740.5
		* gdenergy < -29.5
			* nbumps2 < 0.5: 0(9.0/2.0)
			* nbumps2 >= 0.5: 1(15.0/6.0)
		* gdenergy >= -29.5: 0(132.0/37.0)


