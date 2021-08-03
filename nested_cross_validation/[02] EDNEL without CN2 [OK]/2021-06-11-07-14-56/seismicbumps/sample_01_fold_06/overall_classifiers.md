# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| gpuls > 54.5 and gpuls <= 1142.5 and nbumps <= 1.5 and nbumps4 <= 0.5 and energy <= 550 | 0 | 0.884239 |
| gpuls > 54.5 and gpuls <= 1142.5 and nbumps <= 1.5 and nbumps4 <= 0.5 and energy > 550 | 0 | 0.634712 |
| gpuls > 54.5 and gpuls <= 1142.5 and nbumps > 1.5 and nbumps4 <= 0.5 and energy > 550 | 0 | 0.569885 |
| gpuls <= 54.5 and nbumps <= 1.5 and nbumps4 <= 0.5 and energy <= 550 | 0 | 0.565217 |
| gpuls > 1142.5 and nbumps <= 1.5 and nbumps4 <= 0.5 and energy <= 550 | 0 | 0.267380 |
| gpuls > 1142.5 and nbumps > 1.5 and nbumps4 <= 0.5 and energy > 550 | 0 | 0.211553 |
| gpuls > 54.5 and gpuls <= 1142.5 and nbumps > 1.5 and nbumps4 > 0.5 and energy > 550 | 0 | 0.203978 |
| gpuls > 54.5 and gpuls <= 1142.5 and nbumps <= 1.5 and nbumps4 > 0.5 and energy > 550 | 0 | 0.162688 |
| gpuls > 1142.5 and nbumps > 1.5 and nbumps4 > 0.5 and energy > 550 | 0 | 0.159650 |
| gpuls > 1142.5 and nbumps <= 1.5 and nbumps4 <= 0.5 and energy > 550 | 0 | 0.141750 |
| gpuls <= 54.5 and nbumps <= 1.5 and nbumps4 <= 0.5 and energy > 550 | 0 | 0.117647 |
| gpuls > 1142.5 and nbumps <= 1.5 and nbumps4 > 0.5 and energy > 550 | 0 | 0.068323 |
| gpuls <= 54.5 and nbumps > 1.5 and nbumps4 <= 0.5 and energy > 550 | 0 | 0.062500 |
| gpuls > 54.5 and gpuls <= 1142.5 and nbumps > 1.5 and nbumps4 <= 0.5 and energy <= 550 | 0 | 0.056604 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| nbumps <= 1.5 and gpuls <= 1342.5 and nbumps4 <= 0.5 and shift = N | 0 | 0.837271 |
| nbumps <= 1.5 and shift = W and gpuls <= 1342.5 and ghazard = b | 0 | 0.398191 |
| nbumps <= 1.5 and shift = W and gpuls <= 1210 and ghazard = a and nbumps > 0.5 and seismoacoustic = b | 0 | 0.369748 |
| nbumps <= 1.5 and shift = W and nbumps3 <= 0.5 | 0 | 0.823993 |
| gpuls <= 743 | 0 | 0.634002 |
| ghazard = a and seismoacoustic = b | 0 | 0.182131 |
| ghazard = a and gdpuls > -5.5 | 0 | 0.236489 |
| shift = W and seismic = a | 0 | 0.060150 |
| shift = W and genergy > 80265 and nbumps4 <= 1.5 | 1 | 0.662291 |
|  | 0 | 0.228814 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| nbumps >= 2 and gpuls >= 744 and gdenergy <= -30 and nbumps2 >= 1 and maxenergy >= 2000 and nbumps4 <= 0 | 1 | 0.005500 |
| nbumps >= 2 and genergy >= 306400 and energy >= 6100 and genergy <= 434360 and seismoacoustic = a and nbumps4 <= 1 | 1 | 0.002757 |
| nbumps >= 2 and genergy >= 538060 and nbumps2 >= 2 and seismic = b and energy <= 7000 | 1 | 0.002299 |
| nbumps >= 2 and gdpuls <= 19 and gdpuls >= 0 and genergy <= 59840 and energy >= 3900 and seismic = b | 1 | 0.003673 |
| nbumps >= 2 and gpuls >= 979 and gpuls <= 1471 and genergy <= 206610 and genergy >= 192650 | 1 | 0.001381 |
|  | 0 | 0.949256 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

gpuls|nbumps|nbumps4|energy|class
---|---|---|---|---
(54.5-1142.5]|(1.5-inf)|(0.5-inf)|(550-inf)|0
(1142.5-inf)|(1.5-inf)|(0.5-inf)|(550-inf)|0
(1142.5-inf)|(-inf-1.5]|(0.5-inf)|(550-inf)|0
(54.5-1142.5]|(-inf-1.5]|(0.5-inf)|(550-inf)|0
(1142.5-inf)|(1.5-inf)|(-inf-0.5]|(550-inf)|0
(-inf-54.5]|(1.5-inf)|(-inf-0.5]|(550-inf)|0
(54.5-1142.5]|(1.5-inf)|(-inf-0.5]|(550-inf)|0
(1142.5-inf)|(-inf-1.5]|(-inf-0.5]|(550-inf)|0
(-inf-54.5]|(-inf-1.5]|(-inf-0.5]|(550-inf)|0
(54.5-1142.5]|(-inf-1.5]|(-inf-0.5]|(550-inf)|0
(54.5-1142.5]|(1.5-inf)|(-inf-0.5]|(-inf-550]|0
(1142.5-inf)|(-inf-1.5]|(-inf-0.5]|(-inf-550]|0
(-inf-54.5]|(-inf-1.5]|(-inf-0.5]|(-inf-550]|0
(54.5-1142.5]|(-inf-1.5]|(-inf-0.5]|(-inf-550]|0

## JRip

Decision list:

rules | predicted class
---|---
(nbumps >= 2) and (gpuls >= 744) and (gdenergy <= -30) and (nbumps2 >= 1) and (maxenergy >= 2000) and (nbumps4 <= 0)|1 (12.0/0.0)
(nbumps >= 2) and (genergy >= 306400) and (energy >= 6100) and (genergy <= 434360) and (seismoacoustic = a) and (nbumps4 <= 1)|1 (6.0/0.0)
(nbumps >= 2) and (genergy >= 538060) and (nbumps2 >= 2) and (seismic = b) and (energy <= 7000)|1 (5.0/0.0)
(nbumps >= 2) and (gdpuls <= 19) and (gdpuls >= 0) and (genergy <= 59840) and (energy >= 3900) and (seismic = b)|1 (8.0/0.0)
(nbumps >= 2) and (gpuls >= 979) and (gpuls <= 1471) and (genergy <= 206610) and (genergy >= 192650)|1 (3.0/0.0)
|0 (2286.0/116.0)


## PART

Decision list:

rules | predicted class
---|---
nbumps <= 1.5 AND gpuls <= 1342.5 AND nbumps4 <= 0.5 AND shift = N|0 (694.0/10.0)
nbumps <= 1.5 AND shift = W AND gpuls <= 1342.5 AND ghazard = b|0 (96.0/2.0)
nbumps <= 1.5 AND shift = W AND gpuls <= 1210 AND ghazard = a AND nbumps > 0.5 AND seismoacoustic = b|0 (80.0)
nbumps <= 1.5 AND shift = W AND nbumps3 <= 0.5|0 (680.0/30.0)
gpuls <= 743|0 (302.0/34.0)
ghazard = a AND seismoacoustic = b|0 (61.0/11.0)
ghazard = a AND gdpuls > -5.5|0 (77.0/15.0)
shift = W AND seismic = a|0 (32.0/11.0)
shift = W AND genergy > 80265 AND nbumps4 <= 1.5|1 (30.0/9.0)
|0 (11.0)


## J48 Decision Tree

* : 0 (2320.0/150.0)


## SimpleCart Decision Tree

* : 0(2170.0/150.0)


