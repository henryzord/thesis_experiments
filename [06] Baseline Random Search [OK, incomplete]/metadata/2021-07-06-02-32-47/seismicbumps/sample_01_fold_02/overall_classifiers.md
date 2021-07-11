# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 0 | 0.935345 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| nbumps <= 1.5 and gpuls <= 1342.5 and seismoacoustic != c and shift != W and nbumps2 <= 0.5 and seismic = a and nbumps <= 0.5 and ghazard = a and seismoacoustic = a | 0 | 0.700139 |
| nbumps <= 1.5 and gpuls <= 1342.5 and seismoacoustic != c and ghazard != c and shift != W and nbumps <= 0.5 and seismic = a and ghazard = a | 0 | 0.478194 |
| nbumps <= 1.5 and gpuls <= 1342.5 and seismoacoustic != c and ghazard != c and shift != W and nbumps <= 0.5 | 0 | 0.421998 |
| nbumps <= 1.5 and gpuls <= 1342.5 and seismoacoustic = c | 0 | 0.189189 |
| nbumps <= 1.5 and gpuls <= 1342.5 and ghazard != c and seismic = a and ghazard != a and nbumps <= 0.5 | 0 | 0.175986 |
| nbumps <= 1.5 and gpuls <= 1342.5 and ghazard != c and seismic = a and ghazard = a and nbumps <= 0.5 and seismoacoustic = a | 0 | 0.560224 |
| nbumps <= 1.5 and ghazard != c and gpuls <= 1342.5 and nbumps3 > 0.5 and shift != W and seismoacoustic = a | 0 | 0.333333 |
| nbumps <= 1.5 and ghazard != c and gpuls <= 1342.5 and nbumps4 > 0.5 and shift = W | 0 | 0.152542 |
| nbumps <= 1.5 and ghazard != c and gpuls <= 1342.5 and nbumps2 > 0.5 and ghazard = a and seismoacoustic != a and shift = W | 0 | 0.234694 |
| nbumps <= 1.5 and ghazard != c and gpuls <= 1252.5 and nbumps3 > 0.5 and energy > 1500.0 and ghazard = a and shift = W and energy <= 7500.0 | 0 | 0.342105 |
| nbumps <= 1.5 and nbumps3 <= 0.5 and ghazard != c and nbumps <= 0.5 and gdenergy <= 84.5 and ghazard = a and seismic = a and seismoacoustic != a | 0 | 0.419139 |
| nbumps <= 1.5 and ghazard != c and nbumps3 <= 0.5 and seismic != a and seismoacoustic = a and shift = W and ghazard = a and nbumps > 0.5 and energy <= 850.0 | 0 | 0.175824 |
| nbumps <= 1.5 and ghazard != c and nbumps3 <= 0.5 and ghazard != a and nbumps <= 0.5 and genergy > 21325.0 | 0 | 0.162191 |
| nbumps <= 1.5 and ghazard != c and nbumps3 <= 0.5 and ghazard = a and nbumps <= 0.5 and gdenergy <= 84.5 and seismic != a and seismoacoustic = a | 0 | 0.464923 |
| shift != W and ghazard != c and nbumps <= 1.5 and nbumps4 <= 0.5 and ghazard = a and nbumps2 > 0.5 and seismic = a and seismoacoustic = a and energy <= 550.0 | 0 | 0.132948 |
| shift != W and ghazard != c and seismoacoustic != a and nbumps3 > 0.5 and nbumps2 <= 0.5 and seismic = a and ghazard = a | 0 | 0.128149 |
| ghazard != c and seismoacoustic != c and nbumps <= 2.5 and nbumps4 > 0.5 and nbumps2 <= 0.5 and seismic != a | 0 | 0.142857 |
| gpuls <= 1136.0 and ghazard != c and nbumps3 <= 2.5 and seismoacoustic = b and nbumps4 <= 0.5 and nbumps <= 1.5 and nbumps > 0.5 and ghazard = a and gpuls <= 713.5 | 0 | 0.162191 |
| ghazard != c and seismoacoustic != c and gpuls <= 1184.0 and nbumps3 <= 2.5 and shift = W and seismoacoustic != a and nbumps <= 1.5 and nbumps2 <= 0.5 and ghazard = a and genergy <= 35695.0 | 0 | 0.279156 |
| ghazard != c and seismoacoustic != c and seismic = a and ghazard != a and nbumps <= 1.5 | 0 | 0.085747 |
| ghazard != c and seismoacoustic != c and seismic = a and shift = W and seismoacoustic = a | 0 | 0.554606 |
| ghazard != c and seismoacoustic != c and nbumps3 <= 2.5 and gpuls <= 1184.0 and nbumps4 > 0.5 and gdenergy > -61.5 and seismic != a and maxenergy > 25000.0 | 0 | 0.096386 |
| ghazard != c and seismoacoustic != c and nbumps4 <= 0.5 and nbumps3 <= 2.5 and nbumps > 3.5 and seismic = a | 0 | 0.092185 |
| ghazard != c and seismoacoustic != c and shift != W and seismic != a and seismoacoustic = a | 0 | 0.050633 |
| ghazard = c | 0 | 0.044586 |
| seismoacoustic != c and nbumps4 <= 0.5 and nbumps3 <= 2.5 and ghazard != a and seismic != a and nbumps3 > 0.5 and nbumps <= 1.5 | 0 | 0.038462 |
| seismoacoustic != c and nbumps4 <= 0.5 and nbumps3 <= 2.5 and seismoacoustic != a and shift != W and gdpuls <= 105.5 | 0 | 0.041026 |
| seismoacoustic != c and nbumps4 <= 0.5 and nbumps3 <= 2.5 and shift = W and seismoacoustic != a and ghazard != a and nbumps3 > 0.5 and seismic = a | 0 | 0.025974 |
| seismoacoustic != c and nbumps4 <= 0.5 and nbumps3 <= 2.5 and shift = W and seismoacoustic != a and seismic != a and maxenergy <= 2500.0 and nbumps > 0.5 and ghazard = a | 0 | 0.074074 |
| seismoacoustic != c and nbumps2 <= 0.5 and nbumps4 > 0.5 and gdenergy > -31.5 | 0 | 0.056604 |
| seismoacoustic != c and nbumps4 <= 0.5 and nbumps3 <= 2.5 and shift = W and seismic != a and genergy <= 108515.0 and seismoacoustic = a | 0 | 0.285661 |
| seismoacoustic = b and shift = W and nbumps <= 4.5 and seismic = a and nbumps4 <= 0.5 | 0 | 0.225641 |
| nbumps3 <= 0.5 and shift = W and seismic != a and maxenergy <= 25000.0 and seismoacoustic != a and nbumps > 0.5 and nbumps2 <= 1.5 | 0 | 0.074074 |
| seismoacoustic != c and nbumps <= 0.5 and ghazard = a | 0 | 0.107642 |
| seismoacoustic != c and seismic = a and seismoacoustic = a and gpuls <= 85.5 | 0 | 0.041026 |
| seismoacoustic != c and shift = W and seismic = a and nbumps2 <= 1.5 | 0 | 0.004767 |
| seismoacoustic != c and shift = W and nbumps4 > 0.5 and nbumps4 <= 1.5 and seismoacoustic != a and gdenergy <= 67.5 and maxenergy <= 25000.0 | 0 | 0.044586 |
| seismoacoustic != c and ghazard != a and genergy <= 19220.0 | 0 | 0.044586 |
| seismoacoustic = a and seismic = a and gpuls > 136.0 | 0 | 0.004831 |
| shift != W and nbumps <= 1.5 | 1 | 0.120040 |
| ghazard = a and seismic != a and seismoacoustic != b | 0 | 0.139885 |
| seismoacoustic = b and nbumps4 > 0.5 and genergy <= 71395.0 | 1 | 0.105263 |
| seismoacoustic = b and ghazard = a and nbumps4 > 0.5 | 0 | 0.029976 |
| seismoacoustic = b and ghazard = a and seismic = a and genergy <= 52350.0 | 0 | 0.005409 |
| seismoacoustic = b and ghazard = a and seismic != a and maxenergy <= 7500.0 and gdpuls > -2.0 and maxenergy > 3500.0 | 1 | 0.084656 |
| seismoacoustic = b and ghazard = a and nbumps2 <= 1.5 and nbumps3 > 1.5 | 0 | 0.033333 |
| seismoacoustic = b and ghazard = a and seismic != a and genergy <= 108505.0 | 0 | 0.019934 |
| ghazard = a and nbumps3 <= 2.5 | 1 | 0.882661 |
|  | 1 | 0.631579 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| nbumps >= 2 and gpuls >= 744 and gdenergy <= -30 | 1 | 0.004034 |
|  | 0 | 0.942249 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

genergy|gpuls|nbumps|nbumps6|class
---|---|---|---|---
(17640-77390]|(1253.5-inf)|(1.5-inf)|all|0
(77390-inf)|(1253.5-inf)|(1.5-inf)|all|0
(-inf-17640]|(-inf-1253.5]|(1.5-inf)|all|0
(17640-77390]|(-inf-1253.5]|(1.5-inf)|all|0
(77390-inf)|(-inf-1253.5]|(1.5-inf)|all|0
(17640-77390]|(1253.5-inf)|(0.5-1.5]|all|0
(77390-inf)|(1253.5-inf)|(0.5-1.5]|all|0
(-inf-17640]|(-inf-1253.5]|(0.5-1.5]|all|0
(77390-inf)|(-inf-1253.5]|(0.5-1.5]|all|0
(17640-77390]|(-inf-1253.5]|(0.5-1.5]|all|0
(17640-77390]|(1253.5-inf)|(-inf-0.5]|all|0
(77390-inf)|(1253.5-inf)|(-inf-0.5]|all|0
(77390-inf)|(-inf-1253.5]|(-inf-0.5]|all|0
(-inf-17640]|(-inf-1253.5]|(-inf-0.5]|all|0
(17640-77390]|(-inf-1253.5]|(-inf-0.5]|all|0

## JRip

Decision list:

rules | predicted class
---|---
(nbumps >= 2) and (gpuls >= 744) and (gdenergy <= -30)|1 (33.0/16.0)
|0 (2287.0/133.0)


## PART

Decision list:

rules | predicted class
---|---
nbumps <= 1.5 AND gpuls <= 1342.5 AND seismoacoustic != c AND shift != W AND nbumps2 <= 0.5 AND seismic = a AND nbumps <= 0.5 AND ghazard = a AND seismoacoustic = a|0 (360.0/5.0)
nbumps <= 1.5 AND gpuls <= 1342.5 AND seismoacoustic != c AND ghazard != c AND shift != W AND nbumps <= 0.5 AND seismic = a AND ghazard = a|0 (144.0/1.0)
nbumps <= 1.5 AND gpuls <= 1342.5 AND seismoacoustic != c AND ghazard != c AND shift != W AND nbumps <= 0.5|0 (115.0)
nbumps <= 1.5 AND gpuls <= 1342.5 AND seismoacoustic = c|0 (35.0)
nbumps <= 1.5 AND gpuls <= 1342.5 AND ghazard != c AND seismic = a AND ghazard != a AND nbumps <= 0.5|0 (34.0/1.0)
nbumps <= 1.5 AND gpuls <= 1342.5 AND ghazard != c AND seismic = a AND ghazard = a AND nbumps <= 0.5 AND seismoacoustic = a|0 (205.0/5.0)
nbumps <= 1.5 AND ghazard != c AND gpuls <= 1342.5 AND nbumps3 > 0.5 AND shift != W AND seismoacoustic = a|0 (75.0)
nbumps <= 1.5 AND ghazard != c AND gpuls <= 1342.5 AND nbumps4 > 0.5 AND shift = W|0 (27.0)
nbumps <= 1.5 AND ghazard != c AND gpuls <= 1342.5 AND nbumps2 > 0.5 AND ghazard = a AND seismoacoustic != a AND shift = W|0 (46.0)
nbumps <= 1.5 AND ghazard != c AND gpuls <= 1252.5 AND nbumps3 > 0.5 AND energy > 1500.0 AND ghazard = a AND shift = W AND energy <= 7500.0|0 (78.0)
nbumps <= 1.5 AND nbumps3 <= 0.5 AND ghazard != c AND nbumps <= 0.5 AND gdenergy <= 84.5 AND ghazard = a AND seismic = a AND seismoacoustic != a|0 (115.0/3.0)
nbumps <= 1.5 AND ghazard != c AND nbumps3 <= 0.5 AND seismic != a AND seismoacoustic = a AND shift = W AND ghazard = a AND nbumps > 0.5 AND energy <= 850.0|0 (32.0)
nbumps <= 1.5 AND ghazard != c AND nbumps3 <= 0.5 AND ghazard != a AND nbumps <= 0.5 AND genergy > 21325.0|0 (30.0)
nbumps <= 1.5 AND ghazard != c AND nbumps3 <= 0.5 AND ghazard = a AND nbumps <= 0.5 AND gdenergy <= 84.5 AND seismic != a AND seismoacoustic = a|0 (140.0/5.0)
shift != W AND ghazard != c AND nbumps <= 1.5 AND nbumps4 <= 0.5 AND ghazard = a AND nbumps2 > 0.5 AND seismic = a AND seismoacoustic = a AND energy <= 550.0|0 (23.0)
shift != W AND ghazard != c AND seismoacoustic != a AND nbumps3 > 0.5 AND nbumps2 <= 0.5 AND seismic = a AND ghazard = a|0 (24.0/1.0)
ghazard != c AND seismoacoustic != c AND nbumps <= 2.5 AND nbumps4 > 0.5 AND nbumps2 <= 0.5 AND seismic != a|0 (25.0)
gpuls <= 1136.0 AND ghazard != c AND nbumps3 <= 2.5 AND seismoacoustic = b AND nbumps4 <= 0.5 AND nbumps <= 1.5 AND nbumps > 0.5 AND ghazard = a AND gpuls <= 713.5|0 (30.0)
ghazard != c AND seismoacoustic != c AND gpuls <= 1184.0 AND nbumps3 <= 2.5 AND shift = W AND seismoacoustic != a AND nbumps <= 1.5 AND nbumps2 <= 0.5 AND ghazard = a AND genergy <= 35695.0|0 (60.0)
ghazard != c AND seismoacoustic != c AND seismic = a AND ghazard != a AND nbumps <= 1.5|0 (15.0)
ghazard != c AND seismoacoustic != c AND seismic = a AND shift = W AND seismoacoustic = a|0 (242.0/31.0)
ghazard != c AND seismoacoustic != c AND nbumps3 <= 2.5 AND gpuls <= 1184.0 AND nbumps4 > 0.5 AND gdenergy > -61.5 AND seismic != a AND maxenergy > 25000.0|0 (16.0)
ghazard != c AND seismoacoustic != c AND nbumps4 <= 0.5 AND nbumps3 <= 2.5 AND nbumps > 3.5 AND seismic = a|0 (17.0)
ghazard != c AND seismoacoustic != c AND shift != W AND seismic != a AND seismoacoustic = a|0 (8.0)
ghazard = c|0 (7.0)
seismoacoustic != c AND nbumps4 <= 0.5 AND nbumps3 <= 2.5 AND ghazard != a AND seismic != a AND nbumps3 > 0.5 AND nbumps <= 1.5|0 (6.0)
seismoacoustic != c AND nbumps4 <= 0.5 AND nbumps3 <= 2.5 AND seismoacoustic != a AND shift != W AND gdpuls <= 105.5|0 (8.0)
seismoacoustic != c AND nbumps4 <= 0.5 AND nbumps3 <= 2.5 AND shift = W AND seismoacoustic != a AND ghazard != a AND nbumps3 > 0.5 AND seismic = a|0 (4.0)
seismoacoustic != c AND nbumps4 <= 0.5 AND nbumps3 <= 2.5 AND shift = W AND seismoacoustic != a AND seismic != a AND maxenergy <= 2500.0 AND nbumps > 0.5 AND ghazard = a|0 (12.0)
seismoacoustic != c AND nbumps2 <= 0.5 AND nbumps4 > 0.5 AND gdenergy > -31.5|0 (9.0)
seismoacoustic != c AND nbumps4 <= 0.5 AND nbumps3 <= 2.5 AND shift = W AND seismic != a AND genergy <= 108515.0 AND seismoacoustic = a|0 (87.0/14.0)
seismoacoustic = b AND shift = W AND nbumps <= 4.5 AND seismic = a AND nbumps4 <= 0.5|0 (73.0/16.0)
nbumps3 <= 0.5 AND shift = W AND seismic != a AND maxenergy <= 25000.0 AND seismoacoustic != a AND nbumps > 0.5 AND nbumps2 <= 1.5|0 (12.0)
seismoacoustic != c AND nbumps <= 0.5 AND ghazard = a|0 (38.0/6.0)
seismoacoustic != c AND seismic = a AND seismoacoustic = a AND gpuls <= 85.5|0 (8.0)
seismoacoustic != c AND shift = W AND seismic = a AND nbumps2 <= 1.5|0 (5.0)
seismoacoustic != c AND shift = W AND nbumps4 > 0.5 AND nbumps4 <= 1.5 AND seismoacoustic != a AND gdenergy <= 67.5 AND maxenergy <= 25000.0|0 (7.0)
seismoacoustic != c AND ghazard != a AND genergy <= 19220.0|0 (7.0)
seismoacoustic = a AND seismic = a AND gpuls > 136.0|0 (6.0/1.0)
shift != W AND nbumps <= 1.5|1 (5.0/1.0)
ghazard = a AND seismic != a AND seismoacoustic != b|0 (67.0/27.0)
seismoacoustic = b AND nbumps4 > 0.5 AND genergy <= 71395.0|1 (4.0)
seismoacoustic = b AND ghazard = a AND nbumps4 > 0.5|0 (6.0/1.0)
seismoacoustic = b AND ghazard = a AND seismic = a AND genergy <= 52350.0|0 (4.0/1.0)
seismoacoustic = b AND ghazard = a AND seismic != a AND maxenergy <= 7500.0 AND gdpuls > -2.0 AND maxenergy > 3500.0|1 (7.0/3.0)
seismoacoustic = b AND ghazard = a AND nbumps2 <= 1.5 AND nbumps3 > 1.5|0 (5.0)
seismoacoustic = b AND ghazard = a AND seismic != a AND genergy <= 108505.0|0 (7.0/2.0)
ghazard = a AND nbumps3 <= 2.5|1 (6.0)
|1 (24.0/12.0)


## SimpleCart Decision Tree

* : 0(2170.0/150.0)


