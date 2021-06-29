# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 0 | 0.935345 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| nbumps <= 1 and gpuls <= 1332 and shift = N and nbumps <= 0 and seismic = a and ghazard = a and seismoacoustic = a | 0 | 0.701333 |
| nbumps <= 1 and gpuls <= 1332 and shift = N and nbumps <= 0 and seismic = a and ghazard = a | 0 | 0.468972 |
| nbumps <= 1 and gpuls <= 1332 and ghazard = b and shift = N | 0 | 0.238579 |
| nbumps <= 1 and gpuls <= 1332 and ghazard = b and nbumps <= 0 and seismic = a | 0 | 0.193690 |
| nbumps <= 1 and gpuls <= 1332 and ghazard = a and nbumps4 <= 0 and shift = N and nbumps <= 0 | 0 | 0.320177 |
| nbumps <= 1 and gpuls <= 1332 and ghazard = a and nbumps4 <= 0 and seismic = a and nbumps <= 0 and seismoacoustic = a | 0 | 0.554753 |
| nbumps <= 1 and gpuls <= 1332 and ghazard = b and nbumps > 0 | 0 | 0.193548 |
| nbumps <= 1 and gpuls <= 1332 and ghazard = a and nbumps3 > 0 and shift = N and seismic = a and seismoacoustic = a | 0 | 0.311992 |
| nbumps <= 1 and gpuls <= 1332 and ghazard = a and nbumps4 <= 0 and nbumps > 0 and seismoacoustic = b and nbumps2 > 0 and shift = W | 0 | 0.234694 |
| nbumps <= 1 and gpuls <= 1332 and ghazard = a and nbumps3 > 0 and energy > 1500 and seismic = a and shift = W | 0 | 0.282297 |
| gpuls <= 1141 and nbumps3 <= 1 and ghazard = a and nbumps <= 1 and nbumps4 <= 0 and seismoacoustic = b and nbumps2 <= 0 and shift = N and seismic = a | 0 | 0.128801 |
| gpuls <= 1141 and nbumps3 <= 1 and ghazard = a and nbumps <= 1 and nbumps4 <= 0 and seismoacoustic = b and nbumps3 > 0 and seismic = b | 0 | 0.137931 |
| nbumps3 <= 0 and nbumps2 <= 1 and ghazard = a and shift = W and nbumps4 > 0 and nbumps2 <= 0 | 0 | 0.171271 |
| nbumps3 <= 0 and nbumps2 <= 1 and ghazard = a and nbumps <= 0 and gdenergy <= 87 and seismic = b and seismoacoustic = a | 0 | 0.470582 |
| nbumps3 <= 0 and nbumps2 <= 1 and ghazard = a and seismic = a and seismoacoustic = b and nbumps <= 0 | 0 | 0.428589 |
| gpuls <= 1141 and nbumps3 <= 1 and ghazard = a and nbumps3 <= 0 and nbumps4 <= 0 and shift = N and seismic = a and seismoacoustic = a and gdenergy > -55 | 0 | 0.129776 |
| ghazard = c | 0 | 0.142857 |
| gpuls <= 1141 and nbumps3 <= 1 and ghazard = a and seismic = b and nbumps4 > 0 and shift = W | 0 | 0.112426 |
| maxenergy <= 1000 and seismic = b and nbumps3 > 0 and nbumps <= 1 | 0 | 0.045294 |
| nbumps3 <= 0 and nbumps4 <= 0 and nbumps <= 1 and shift = W and nbumps > 0 and seismic = b and energy <= 800 | 0 | 0.171271 |
| nbumps3 <= 0 and nbumps4 <= 0 and nbumps <= 1 and seismoacoustic = b and nbumps <= 0 and ghazard = a | 0 | 0.332092 |
| seismic = a and seismoacoustic = a and shift = W | 0 | 0.554278 |
| nbumps3 <= 2 and genergy <= 292040 and seismoacoustic = a and seismic = b and shift = N and nbumps3 > 0 | 0 | 0.056604 |
| nbumps3 <= 2 and genergy <= 292040 and seismoacoustic = b and seismic = a and ghazard = a and shift = N and nbumps <= 1 | 0 | 0.060377 |
| gdenergy > 131 and seismoacoustic = b | 0 | 0.124756 |
| nbumps3 <= 2 and nbumps2 <= 0 and ghazard = b | 0 | 0.151673 |
| ghazard = a and nbumps3 <= 2 and shift = N and seismoacoustic = a and gdenergy > -43 | 0 | 0.089800 |
| ghazard = a and nbumps3 <= 2 and seismic = a and nbumps4 <= 0 and seismoacoustic = b and shift = W and nbumps3 > 1 and nbumps > 2 | 0 | 0.056604 |
| ghazard = a and nbumps2 <= 0 and nbumps4 > 0 and seismoacoustic = a and maxenergy <= 60000 and gdenergy > -35 | 0 | 0.038462 |
| ghazard = a and nbumps3 <= 2 and seismic = a and nbumps4 <= 0 and seismoacoustic = b and shift = W | 0 | 0.213856 |
| ghazard = a and seismoacoustic = a and genergy <= 90960 and seismic = b and nbumps2 > 1 | 0 | 0.101796 |
| ghazard = a and nbumps2 <= 0 and seismoacoustic = b and nbumps4 > 0 | 0 | 0.033180 |
| ghazard = a and nbumps2 <= 0 and seismoacoustic = a and nbumps4 <= 0 | 0 | 0.195717 |
| ghazard = a and shift = N and seismoacoustic = b and genergy <= 18600 | 0 | 0.010000 |
| ghazard = a and shift = N and seismoacoustic = a and energy <= 600 | 0 | 0.015253 |
| ghazard = a and seismoacoustic = b and shift = W and nbumps3 <= 0 | 0 | 0.023438 |
| ghazard = a and shift = N and seismoacoustic = a | 1 | 0.067204 |
| shift = N | 0 | 0.043403 |
| nbumps4 > 1 | 0 | 0.041952 |
| nbumps4 > 0 and seismoacoustic = b and gdenergy > 11 and energy > 34000 | 1 | 0.022857 |
| nbumps4 > 0 and seismoacoustic = b and nbumps2 <= 2 | 0 | 0.041264 |
| nbumps4 > 0 and seismoacoustic = a and nbumps2 > 0 and nbumps2 <= 1 | 0 | 0.028777 |
| nbumps4 > 0 and seismoacoustic = a and nbumps <= 3 and genergy <= 307540 | 0 | 0.035461 |
| nbumps4 > 0 and seismoacoustic = a and genergy <= 507230 | 1 | 0.053571 |
| nbumps4 > 0 and maxenergy <= 20000 | 0 | 0.033582 |
| seismoacoustic = a and genergy <= 197620 and nbumps2 <= 1 | 0 | 0.085429 |
| seismic = a and ghazard = b | 0 | 0.030934 |
| ghazard = a and maxenergy <= 2000 and nbumps > 2 | 0 | 0.028773 |
| nbumps4 <= 0 and ghazard = a and seismoacoustic = a and nbumps3 <= 1 and nbumps2 > 1 | 1 | 0.240803 |
| nbumps4 <= 0 and ghazard = a and genergy > 39900 and seismoacoustic = b and nbumps3 > 1 and nbumps <= 3 | 0 | 0.048387 |
| nbumps4 <= 0 and ghazard = a and genergy > 39900 and seismoacoustic = b and gpuls <= 896 and gdenergy <= 53 | 0 | 0.047302 |
| nbumps4 <= 0 and seismoacoustic = b and nbumps2 <= 2 and gdenergy <= -10 | 1 | 0.461538 |
| nbumps4 <= 0 and nbumps2 <= 2 and nbumps2 <= 1 and seismoacoustic = b | 1 | 0.501742 |
| nbumps4 <= 0 and seismoacoustic = b and nbumps2 <= 2 | 1 | 0.135338 |
| nbumps4 > 0 | 0 | 0.042857 |
| seismoacoustic = a and genergy <= 401730 | 0 | 0.011260 |
| nbumps <= 4 | 1 | 0.835569 |
|  | 1 | 0.521739 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| gpuls >= 1185 and gdpuls <= 1 and nbumps2 >= 1 and gpuls <= 1545 and gdenergy <= -7 | 1 | 0.004406 |
|  | 0 | 0.940208 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

seismic|shift|gpuls|nbumps|nbumps7|nbumps89|class
---|---|---|---|---|---|---
a|n|(1142.5-inf)|(1.5-inf)|all|all|1
b|w|(1142.5-inf)|(1.5-inf)|all|all|0
a|w|(1142.5-inf)|(1.5-inf)|all|all|0
b|n|(-inf-1142.5]|(1.5-inf)|all|all|0
a|n|(-inf-1142.5]|(1.5-inf)|all|all|0
b|w|(-inf-1142.5]|(1.5-inf)|all|all|0
a|w|(-inf-1142.5]|(1.5-inf)|all|all|0
a|w|(1142.5-inf)|(0.5-1.5]|all|all|0
b|w|(1142.5-inf)|(0.5-1.5]|all|all|0
b|n|(-inf-1142.5]|(0.5-1.5]|all|all|0
a|n|(-inf-1142.5]|(0.5-1.5]|all|all|0
a|n|(1142.5-inf)|(-inf-0.5]|all|all|1
b|n|(1142.5-inf)|(-inf-0.5]|all|all|1
a|w|(-inf-1142.5]|(0.5-1.5]|all|all|0
b|w|(-inf-1142.5]|(0.5-1.5]|all|all|0
b|w|(1142.5-inf)|(-inf-0.5]|all|all|0
a|w|(1142.5-inf)|(-inf-0.5]|all|all|0
b|n|(-inf-1142.5]|(-inf-0.5]|all|all|0
a|n|(-inf-1142.5]|(-inf-0.5]|all|all|0
a|w|(-inf-1142.5]|(-inf-0.5]|all|all|0
b|w|(-inf-1142.5]|(-inf-0.5]|all|all|0

## JRip

Decision list:

rules | predicted class
---|---
(gpuls >= 1185) and (gdpuls <= 1) and (nbumps2 >= 1) and (gpuls <= 1545) and (gdenergy <= -7)|1 (15.0/3.0)
|0 (2305.0/138.0)


## PART

Decision list:

rules | predicted class
---|---
nbumps <= 1 AND gpuls <= 1332 AND shift = N AND nbumps <= 0 AND seismic = a AND ghazard = a AND seismoacoustic = a|0 (362.0/5.0)
nbumps <= 1 AND gpuls <= 1332 AND shift = N AND nbumps <= 0 AND seismic = a AND ghazard = a|0 (139.0/1.0)
nbumps <= 1 AND gpuls <= 1332 AND ghazard = b AND shift = N|0 (47.0)
nbumps <= 1 AND gpuls <= 1332 AND ghazard = b AND nbumps <= 0 AND seismic = a|0 (38.0/1.0)
nbumps <= 1 AND gpuls <= 1332 AND ghazard = a AND nbumps4 <= 0 AND shift = N AND nbumps <= 0|0 (76.0)
nbumps <= 1 AND gpuls <= 1332 AND ghazard = a AND nbumps4 <= 0 AND seismic = a AND nbumps <= 0 AND seismoacoustic = a|0 (199.0/4.0)
nbumps <= 1 AND gpuls <= 1332 AND ghazard = b AND nbumps > 0|0 (36.0)
nbumps <= 1 AND gpuls <= 1332 AND ghazard = a AND nbumps3 > 0 AND shift = N AND seismic = a AND seismoacoustic = a|0 (70.0/1.0)
nbumps <= 1 AND gpuls <= 1332 AND ghazard = a AND nbumps4 <= 0 AND nbumps > 0 AND seismoacoustic = b AND nbumps2 > 0 AND shift = W|0 (46.0)
nbumps <= 1 AND gpuls <= 1332 AND ghazard = a AND nbumps3 > 0 AND energy > 1500 AND seismic = a AND shift = W|0 (59.0)
gpuls <= 1141 AND nbumps3 <= 1 AND ghazard = a AND nbumps <= 1 AND nbumps4 <= 0 AND seismoacoustic = b AND nbumps2 <= 0 AND shift = N AND seismic = a|0 (25.0/1.0)
gpuls <= 1141 AND nbumps3 <= 1 AND ghazard = a AND nbumps <= 1 AND nbumps4 <= 0 AND seismoacoustic = b AND nbumps3 > 0 AND seismic = b|0 (24.0)
nbumps3 <= 0 AND nbumps2 <= 1 AND ghazard = a AND shift = W AND nbumps4 > 0 AND nbumps2 <= 0|0 (31.0)
nbumps3 <= 0 AND nbumps2 <= 1 AND ghazard = a AND nbumps <= 0 AND gdenergy <= 87 AND seismic = b AND seismoacoustic = a|0 (143.0/5.0)
nbumps3 <= 0 AND nbumps2 <= 1 AND ghazard = a AND seismic = a AND seismoacoustic = b AND nbumps <= 0|0 (123.0/5.0)
gpuls <= 1141 AND nbumps3 <= 1 AND ghazard = a AND nbumps3 <= 0 AND nbumps4 <= 0 AND shift = N AND seismic = a AND seismoacoustic = a AND gdenergy > -55|0 (25.0)
ghazard = c|0 (25.0)
gpuls <= 1141 AND nbumps3 <= 1 AND ghazard = a AND seismic = b AND nbumps4 > 0 AND shift = W|0 (19.0)
maxenergy <= 1000 AND seismic = b AND nbumps3 > 0 AND nbumps <= 1|0 (9.0/1.0)
nbumps3 <= 0 AND nbumps4 <= 0 AND nbumps <= 1 AND shift = W AND nbumps > 0 AND seismic = b AND energy <= 800|0 (31.0)
nbumps3 <= 0 AND nbumps4 <= 0 AND nbumps <= 1 AND seismoacoustic = b AND nbumps <= 0 AND ghazard = a|0 (92.0/7.0)
seismic = a AND seismoacoustic = a AND shift = W|0 (237.0/28.0)
nbumps3 <= 2 AND genergy <= 292040 AND seismoacoustic = a AND seismic = b AND shift = N AND nbumps3 > 0|0 (9.0)
nbumps3 <= 2 AND genergy <= 292040 AND seismoacoustic = b AND seismic = a AND ghazard = a AND shift = N AND nbumps <= 1|0 (13.0/1.0)
gdenergy > 131 AND seismoacoustic = b|0 (24.0)
nbumps3 <= 2 AND nbumps2 <= 0 AND ghazard = b|0 (35.0/4.0)
ghazard = a AND nbumps3 <= 2 AND shift = N AND seismoacoustic = a AND gdenergy > -43|0 (18.0)
ghazard = a AND nbumps3 <= 2 AND seismic = a AND nbumps4 <= 0 AND seismoacoustic = b AND shift = W AND nbumps3 > 1 AND nbumps > 2|0 (9.0)
ghazard = a AND nbumps2 <= 0 AND nbumps4 > 0 AND seismoacoustic = a AND maxenergy <= 60000 AND gdenergy > -35|0 (6.0)
ghazard = a AND nbumps3 <= 2 AND seismic = a AND nbumps4 <= 0 AND seismoacoustic = b AND shift = W|0 (66.0/13.0)
ghazard = a AND seismoacoustic = a AND genergy <= 90960 AND seismic = b AND nbumps2 > 1|0 (17.0)
ghazard = a AND nbumps2 <= 0 AND seismoacoustic = b AND nbumps4 > 0|0 (6.0)
ghazard = a AND nbumps2 <= 0 AND seismoacoustic = a AND nbumps4 <= 0|0 (68.0/13.0)
ghazard = a AND shift = N AND seismoacoustic = b AND genergy <= 18600|0 (5.0/2.0)
ghazard = a AND shift = N AND seismoacoustic = a AND energy <= 600|0 (5.0)
ghazard = a AND seismoacoustic = b AND shift = W AND nbumps3 <= 0|0 (9.0)
ghazard = a AND shift = N AND seismoacoustic = a|1 (5.0/2.0)
shift = N|0 (9.0/1.0)
nbumps4 > 1|0 (8.0/1.0)
nbumps4 > 0 AND seismoacoustic = b AND gdenergy > 11 AND energy > 34000|1 (7.0/3.0)
nbumps4 > 0 AND seismoacoustic = b AND nbumps2 <= 2|0 (6.0/1.0)
nbumps4 > 0 AND seismoacoustic = a AND nbumps2 > 0 AND nbumps2 <= 1|0 (9.0/3.0)
nbumps4 > 0 AND seismoacoustic = a AND nbumps <= 3 AND genergy <= 307540|0 (5.0)
nbumps4 > 0 AND seismoacoustic = a AND genergy <= 507230|1 (5.0/2.0)
nbumps4 > 0 AND maxenergy <= 20000|0 (6.0)
seismoacoustic = a AND genergy <= 197620 AND nbumps2 <= 1|0 (32.0/7.0)
seismic = a AND ghazard = b|0 (9.0/2.0)
ghazard = a AND maxenergy <= 2000 AND nbumps > 2|0 (7.0)
nbumps4 <= 0 AND ghazard = a AND seismoacoustic = a AND nbumps3 <= 1 AND nbumps2 > 1|1 (6.0/1.0)
nbumps4 <= 0 AND ghazard = a AND genergy > 39900 AND seismoacoustic = b AND nbumps3 > 1 AND nbumps <= 3|0 (6.0)
nbumps4 <= 0 AND ghazard = a AND genergy > 39900 AND seismoacoustic = b AND gpuls <= 896 AND gdenergy <= 53|0 (8.0)
nbumps4 <= 0 AND seismoacoustic = b AND nbumps2 <= 2 AND gdenergy <= -10|1 (6.0)
nbumps4 <= 0 AND nbumps2 <= 2 AND nbumps2 <= 1 AND seismoacoustic = b|1 (9.0/4.0)
nbumps4 <= 0 AND seismoacoustic = b AND nbumps2 <= 2|1 (8.0/4.0)
nbumps4 > 0|0 (6.0/2.0)
seismoacoustic = a AND genergy <= 401730|0 (5.0/2.0)
nbumps <= 4|1 (6.0/3.0)
|1 (6.0)


## J48 Decision Tree

* : 0 (2320.0/150.0)


## SimpleCart Decision Tree

* : 0(2170.0/150.0)


