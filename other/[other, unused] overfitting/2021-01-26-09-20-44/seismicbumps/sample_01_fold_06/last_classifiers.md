# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| nbumps <= 1.5 and gpuls <= 1210.0 | 0 | 0.916121 |
| nbumps > 1.5 | 0 | 0.693531 |
| nbumps <= 1.5 and gpuls > 1210.0 and nbumps3 <= 0.5 | 0 | 0.304167 |
| nbumps >= 1.5 and gpuls >= 740.5 and gdenergy < -29.5 and nbumps2 >= 0.5 | 1 | 0.004913 |
| seismic = b and shift = W and gpuls > 1142.5 and gdenergy = all and nbumps <= 1.5 and nbumps2 <= 0.5 and nbumps4 <= 0.5 and nbumps5 = all and nbumps6 = all and nbumps7 = all and nbumps89 = all and energy > 550 | 1 | 0.001963 |
| seismic = a and shift = W and gpuls > 1142.5 and gdenergy = all and nbumps <= 1.5 and nbumps2 <= 0.5 and nbumps4 <= 0.5 and nbumps5 = all and nbumps6 = all and nbumps7 = all and nbumps89 = all and energy > 550 | 0 | 0.089636 |
| seismic = a and shift = W and gpuls > 1142.5 and gdenergy = all and nbumps > 1.5 and nbumps2 <= 0.5 and nbumps4 > 0.5 and nbumps5 = all and nbumps6 = all and nbumps7 = all and nbumps89 = all and energy > 550 | 1 | 0.000230 |
| seismic = a and shift = N and gpuls > 54.5 and gpuls <= 1142.5 and gdenergy = all and nbumps <= 1.5 and nbumps2 <= 0.5 and nbumps4 > 0.5 and nbumps5 = all and nbumps6 = all and nbumps7 = all and nbumps89 = all and energy > 550 | 1 | 0.000154 |
| seismic = b and shift = N and gpuls > 54.5 and gpuls <= 1142.5 and gdenergy = all and nbumps > 1.5 and nbumps2 > 0.5 and nbumps4 <= 0.5 and nbumps5 = all and nbumps6 = all and nbumps7 = all and nbumps89 = all and energy > 550 | 1 | 0.000154 |
| nbumps < 1.5 and gpuls >= 1342.5 and nbumps3 >= 0.5 and seismic!=(a) | 1 | 0.001734 |
| nbumps < 1.5 and gpuls < 1342.5 and genergy >= 16885.0 | 0 | 0.856984 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| nbumps <= 1 and shift = N | 0 | 0.835853 |
| nbumps <= 1 and nbumps4 <= 0 and seismoacoustic = a and nbumps3 <= 0 | 0 | 0.747959 |
| nbumps <= 1 and nbumps2 <= 0 and nbumps4 <= 0 and gpuls <= 1401 | 0 | 0.710264 |
| energy > 500 and ghazard = a and gpuls <= 519 | 0 | 0.512550 |
| energy > 500 and nbumps2 <= 0 | 0 | 0.298988 |
| nbumps > 1 and gdenergy > -30 and ghazard = a and seismoacoustic = a | 0 | 0.263969 |
| nbumps <= 1 | 0 | 0.237037 |
| seismoacoustic = b and ghazard = a and nbumps4 > 0 | 0 | 0.071389 |
| seismoacoustic = b | 0 | 0.193604 |
| nbumps4 <= 0 | 1 | 0.884794 |
|  | 0 | 0.472222 |


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
nbumps <= 1 AND shift = N|0 (507.0/10.0)
nbumps <= 1 AND nbumps4 <= 0 AND seismoacoustic = a AND nbumps3 <= 0|0 (324.0/16.0)
nbumps <= 1 AND nbumps2 <= 0 AND nbumps4 <= 0 AND gpuls <= 1401|0 (294.0/10.0)
energy > 500 AND ghazard = a AND gpuls <= 519|0 (152.0/12.0)
energy > 500 AND nbumps2 <= 0|0 (69.0/8.0)
nbumps > 1 AND gdenergy > -30 AND ghazard = a AND seismoacoustic = a|0 (72.0/16.0)
nbumps <= 1|0 (47.0)
seismoacoustic = b AND ghazard = a AND nbumps4 > 0|0 (16.0/2.0)
seismoacoustic = b|0 (49.0/16.0)
nbumps4 <= 0|1 (14.0/4.0)
|0 (6.0/2.0)


## J48 Decision Tree

* nbumps <= 1.5
	* gpuls <= 1210.0: 0 (1574.0/42.0)
	* gpuls > 1210.0
		* nbumps3 <= 0.5: 0 (74.0/7.0)
		* nbumps3 > 0.5
			* seismic = a: 0 (12.0/1.0)
			* seismic != a: 1 (10.0/4.0)
* nbumps > 1.5: 0 (423.0/82.0)


## SimpleCart Decision Tree

* nbumps < 1.5
	* gpuls < 1342.5
		* genergy < 16885.0: 0(784.0/10.0)
		* genergy >= 16885.0: 0(945.0/39.0)
	* gpuls >= 1342.5
		* nbumps3 < 0.5: 0(54.0/6.0)
		* nbumps3 >= 0.5
			* seismic=(a): 0(5.0/1.0)
			* seismic!=(a): 1(7.0/4.0)
* nbumps >= 1.5
	* gpuls < 740.5: 0(233.0/36.0)
	* gpuls >= 740.5
		* gdenergy < -29.5
			* nbumps2 < 0.5: 0(9.0/2.0)
			* nbumps2 >= 0.5: 1(15.0/6.0)
		* gdenergy >= -29.5: 0(132.0/37.0)


