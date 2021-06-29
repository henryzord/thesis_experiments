# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| nbumps <= 1.5 | 0 | 0.919973 |
| nbumps > 1.5 and shift = W and ghazard = a and nbumps2 > 0.5 and genergy <= 55650 | 0 | 0.437657 |
| nbumps > 1.5 and shift = W and ghazard = a and nbumps2 <= 0.5 | 0 | 0.285644 |
| nbumps > 1.5 and shift = W and ghazard = a and nbumps2 > 0.5 and genergy > 55650 and seismoacoustic = b | 0 | 0.219968 |
| nbumps > 1.5 and shift = W and ghazard = a and nbumps2 > 0.5 and genergy > 55650 and seismoacoustic = a and nbumps4 <= 0.5 and seismic = a | 0 | 0.152518 |
| nbumps > 1.5 and shift = N | 0 | 0.122605 |
| nbumps > 1.5 and shift = W and ghazard = a and nbumps2 > 0.5 and genergy > 55650 and seismoacoustic = a and nbumps4 > 0.5 | 0 | 0.081527 |
| nbumps > 1.5 and shift = W and ghazard = a and nbumps2 > 0.5 and genergy > 55650 and seismoacoustic = a and nbumps4 <= 0.5 and seismic = b and nbumps <= 3.5 and nbumps2 > 1.5 and genergy > 119985 | 1 | 0.002296 |
| nbumps > 1.5 and shift = W and ghazard = a and nbumps2 > 0.5 and genergy > 55650 and seismoacoustic = a and nbumps4 <= 0.5 and seismic = b and nbumps <= 3.5 and nbumps2 <= 1.5 and gpuls > 930 | 1 | 0.001655 |
| nbumps > 1.5 and shift = W and ghazard = b | 0 | 0.069040 |
| nbumps > 1.5 and shift = W and ghazard = a and nbumps2 > 0.5 and genergy > 55650 and seismoacoustic = a and nbumps4 <= 0.5 and seismic = b and nbumps <= 3.5 and nbumps2 <= 1.5 and gpuls <= 930 | 0 | 0.037736 |
| nbumps > 1.5 and shift = W and ghazard = a and nbumps2 > 0.5 and genergy > 55650 and seismoacoustic = a and nbumps4 <= 0.5 and seismic = b and nbumps > 3.5 | 0 | 0.034459 |
| nbumps > 1.5 and shift = W and ghazard = a and nbumps2 > 0.5 and genergy > 55650 and seismoacoustic = a and nbumps4 <= 0.5 and seismic = b and nbumps <= 3.5 and nbumps2 > 1.5 and genergy <= 119985 | 0 | 0.017204 |
| nbumps > 1.5 and shift = W and ghazard = a and nbumps2 > 0.5 and genergy > 55650 and seismoacoustic = c | 0 | 0.014516 |
| nbumps > 1.5 and shift = W and ghazard = c | 0 | 0.012903 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| nbumps <= 1 and gpuls <= 1333 and shift = N and nbumps <= 0 and seismic = a and ghazard = a and seismoacoustic = a | 0 | 0.697118 |
| nbumps <= 1 and gpuls <= 1333 and shift = N and nbumps <= 0 and seismic = a and ghazard = a | 0 | 0.461892 |
| nbumps <= 1 and gpuls <= 1333 and ghazard = b and shift = N | 0 | 0.227273 |
| nbumps <= 1 and gpuls <= 1333 and ghazard = b and nbumps <= 0 and seismic = b | 0 | 0.182381 |
| nbumps <= 1 and gpuls <= 1333 and ghazard = b and nbumps > 0 | 0 | 0.194737 |
| nbumps <= 1 and gpuls <= 1333 and ghazard = a and nbumps4 <= 0 and shift = N and nbumps <= 0 | 0 | 0.336032 |
| nbumps <= 1 and gpuls <= 1333 and ghazard = a and nbumps4 <= 0 and shift = N and seismoacoustic = a and seismic = a and nbumps2 <= 0 | 0 | 0.293252 |
| nbumps <= 1 and gpuls <= 1333 and ghazard = a and nbumps4 <= 0 and seismic = a and nbumps <= 0 and seismoacoustic = a | 0 | 0.547184 |
| nbumps <= 1 and gpuls <= 1333 and ghazard = a and nbumps3 > 0 and energy > 1500 and shift = W and energy <= 7500 | 0 | 0.372951 |
| nbumps <= 1 and nbumps3 <= 0 and ghazard = a and shift = W and nbumps4 <= 0 and genergy <= 18690 and seismoacoustic = a | 0 | 0.337716 |
| nbumps <= 1 and nbumps3 <= 0 and ghazard = b | 0 | 0.195838 |
| nbumps <= 1 and ghazard = a and nbumps3 <= 0 and seismoacoustic = b and shift = W and nbumps > 0 and seismic = b | 0 | 0.159341 |
| nbumps <= 1 and ghazard = a and gpuls <= 1333 and seismoacoustic = b and nbumps2 > 0 and shift = W | 0 | 0.140449 |
| gpuls <= 1134 and nbumps <= 2 and ghazard = a and nbumps <= 1 and seismoacoustic = b and seismic = a and nbumps2 <= 0 and nbumps <= 0 | 0 | 0.421563 |
| ghazard = a and genergy <= 58230 and nbumps3 <= 1 and gdenergy > -37 and nbumps4 <= 0 and shift = N and seismic = a | 0 | 0.244672 |
| ghazard = c | 0 | 0.145251 |
| nbumps <= 1 and nbumps3 <= 0 and shift = W and nbumps4 > 0 | 0 | 0.150000 |
| gpuls <= 1134 and nbumps <= 2 and ghazard = a and seismic = b and nbumps2 <= 0 and seismoacoustic = b and nbumps <= 0 | 0 | 0.315303 |
| gpuls <= 741 and nbumps4 <= 0 and ghazard = a and seismic = b and seismoacoustic = a and shift = W | 0 | 0.467764 |
| ghazard = a and shift = N and nbumps4 <= 0 and nbumps <= 1 and seismoacoustic = a and seismic = b | 0 | 0.083832 |
| ghazard = a and seismic = a and shift = N and nbumps <= 1 and nbumps2 > 0 and seismoacoustic = a and gdenergy <= -56 | 0 | 0.026539 |
| ghazard = a and seismic = a and shift = N and nbumps <= 1 and nbumps2 > 0 | 0 | 0.056117 |
| ghazard = a and seismic = a and seismoacoustic = a and shift = W | 0 | 0.513111 |
| nbumps2 <= 0 and seismoacoustic = b and seismic = b and nbumps4 <= 0 and shift = W and nbumps > 0 and maxenergy <= 3000 | 0 | 0.049689 |
| ghazard = a and gdpuls > 20 and seismic = a and nbumps <= 3 and nbumps <= 2 and nbumps3 <= 0 | 0 | 0.024768 |
| shift = N and nbumps2 <= 0 and nbumps4 <= 0 and seismic = a | 0 | 0.063523 |
| ghazard = a and gdpuls > 20 and seismoacoustic = a and nbumps2 <= 1 and nbumps2 <= 0 and nbumps4 <= 0 | 0 | 0.089091 |
| ghazard = a and seismoacoustic = b and seismic = a and nbumps4 <= 0 | 0 | 0.256632 |
| nbumps4 > 0 and ghazard = a and shift = W and nbumps2 <= 0 and nbumps3 <= 1 | 0 | 0.083832 |
| nbumps3 <= 0 and ghazard = a and shift = W and nbumps4 <= 0 and seismoacoustic = b and nbumps > 1 | 0 | 0.025641 |
| nbumps4 > 0 and ghazard = a and seismoacoustic = a and genergy <= 189170 and nbumps2 > 1 | 0 | 0.083832 |
| seismoacoustic = b and seismic = a and nbumps3 > 0 | 0 | 0.016667 |
| seismic = b and shift = N and genergy > 17910 | 0 | 0.061350 |
| ghazard = a and seismoacoustic = b and shift = W and nbumps4 > 0 and energy <= 34000 | 0 | 0.061350 |
| seismic = b and nbumps2 <= 1 and seismoacoustic = b and nbumps2 <= 0 and nbumps <= 1 | 0 | 0.042229 |
| seismic = b and shift = W and seismoacoustic = a and genergy <= 85240 and nbumps3 <= 0 | 0 | 0.052017 |
| seismic = b and seismoacoustic = b and nbumps2 > 0 and ghazard = a and nbumps4 <= 0 and nbumps3 <= 1 and maxenergy <= 2000 | 0 | 0.032550 |
| shift = W and seismic = b and seismoacoustic = b and nbumps2 > 0 and gdpuls <= 92 and nbumps4 > 0 and gdpuls <= 37 | 0 | 0.018038 |
| nbumps4 > 0 and nbumps2 <= 1 and maxenergy <= 60000 and nbumps3 <= 2 and ghazard = a and nbumps > 3 | 0 | 0.028662 |
| nbumps4 > 0 and nbumps2 <= 1 and nbumps <= 3 and maxenergy <= 60000 and ghazard = a and nbumps > 2 | 1 | 0.041118 |
| nbumps4 > 0 and nbumps2 <= 1 and energy > 30300 | 0 | 0.089198 |
| shift = N | 1 | 0.169550 |
| ghazard = b and nbumps <= 2 and gdenergy <= 77 | 1 | 0.059524 |
| nbumps4 <= 0 and seismoacoustic = b and maxenergy <= 7000 and ghazard = a and gdpuls <= -2 | 0 | 0.012703 |
| seismoacoustic = a and nbumps4 <= 0 | 0 | 0.087831 |
| gdpuls <= 92 and seismoacoustic = b and maxenergy <= 7000 and nbumps2 > 1 | 1 | 0.252083 |
| gdpuls <= 92 and seismoacoustic = b and maxenergy > 6000 | 0 | 0.038095 |
| nbumps <= 4 and seismoacoustic = a | 1 | 0.806005 |
| nbumps2 <= 1 and genergy <= 122850 | 1 | 0.572344 |
| nbumps2 <= 1 | 0 | 0.267380 |
|  | 1 | 0.730769 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| nbumps >= 2 and gpuls >= 744 and gdenergy <= -30 | 1 | 0.004512 |
|  | 0 | 0.941508 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

class
---
0

## JRip

Decision list:

rules | predicted class
---|---
(nbumps >= 2) and (gpuls >= 744) and (gdenergy <= -30)|1 (33.0/15.0)
|0 (2293.0/135.0)


## PART

Decision list:

rules | predicted class
---|---
nbumps <= 1 AND gpuls <= 1333 AND shift = N AND nbumps <= 0 AND seismic = a AND ghazard = a AND seismoacoustic = a|0 (360.0/4.0)
nbumps <= 1 AND gpuls <= 1333 AND shift = N AND nbumps <= 0 AND seismic = a AND ghazard = a|0 (137.0/1.0)
nbumps <= 1 AND gpuls <= 1333 AND ghazard = b AND shift = N|0 (45.0)
nbumps <= 1 AND gpuls <= 1333 AND ghazard = b AND nbumps <= 0 AND seismic = b|0 (38.0/2.0)
nbumps <= 1 AND gpuls <= 1333 AND ghazard = b AND nbumps > 0|0 (37.0)
nbumps <= 1 AND gpuls <= 1333 AND ghazard = a AND nbumps4 <= 0 AND shift = N AND nbumps <= 0|0 (82.0)
nbumps <= 1 AND gpuls <= 1333 AND ghazard = a AND nbumps4 <= 0 AND shift = N AND seismoacoustic = a AND seismic = a AND nbumps2 <= 0|0 (69.0/1.0)
nbumps <= 1 AND gpuls <= 1333 AND ghazard = a AND nbumps4 <= 0 AND seismic = a AND nbumps <= 0 AND seismoacoustic = a|0 (198.0/5.0)
nbumps <= 1 AND gpuls <= 1333 AND ghazard = a AND nbumps3 > 0 AND energy > 1500 AND shift = W AND energy <= 7500|0 (91.0)
nbumps <= 1 AND nbumps3 <= 0 AND ghazard = a AND shift = W AND nbumps4 <= 0 AND genergy <= 18690 AND seismoacoustic = a|0 (79.0)
nbumps <= 1 AND nbumps3 <= 0 AND ghazard = b|0 (41.0/1.0)
nbumps <= 1 AND ghazard = a AND nbumps3 <= 0 AND seismoacoustic = b AND shift = W AND nbumps > 0 AND seismic = b|0 (29.0)
nbumps <= 1 AND ghazard = a AND gpuls <= 1333 AND seismoacoustic = b AND nbumps2 > 0 AND shift = W|0 (25.0)
gpuls <= 1134 AND nbumps <= 2 AND ghazard = a AND nbumps <= 1 AND seismoacoustic = b AND seismic = a AND nbumps2 <= 0 AND nbumps <= 0|0 (122.0/5.0)
ghazard = a AND genergy <= 58230 AND nbumps3 <= 1 AND gdenergy > -37 AND nbumps4 <= 0 AND shift = N AND seismic = a|0 (54.0)
ghazard = c|0 (26.0)
nbumps <= 1 AND nbumps3 <= 0 AND shift = W AND nbumps4 > 0|0 (27.0)
gpuls <= 1134 AND nbumps <= 2 AND ghazard = a AND seismic = b AND nbumps2 <= 0 AND seismoacoustic = b AND nbumps <= 0|0 (80.0/5.0)
gpuls <= 741 AND nbumps4 <= 0 AND ghazard = a AND seismic = b AND seismoacoustic = a AND shift = W|0 (155.0/11.0)
ghazard = a AND shift = N AND nbumps4 <= 0 AND nbumps <= 1 AND seismoacoustic = a AND seismic = b|0 (14.0)
ghazard = a AND seismic = a AND shift = N AND nbumps <= 1 AND nbumps2 > 0 AND seismoacoustic = a AND gdenergy <= -56|0 (6.0/1.0)
ghazard = a AND seismic = a AND shift = N AND nbumps <= 1 AND nbumps2 > 0|0 (10.0)
ghazard = a AND seismic = a AND seismoacoustic = a AND shift = W|0 (219.0/33.0)
nbumps2 <= 0 AND seismoacoustic = b AND seismic = b AND nbumps4 <= 0 AND shift = W AND nbumps > 0 AND maxenergy <= 3000|0 (8.0)
ghazard = a AND gdpuls > 20 AND seismic = a AND nbumps <= 3 AND nbumps <= 2 AND nbumps3 <= 0|0 (8.0)
shift = N AND nbumps2 <= 0 AND nbumps4 <= 0 AND seismic = a|0 (16.0/1.0)
ghazard = a AND gdpuls > 20 AND seismoacoustic = a AND nbumps2 <= 1 AND nbumps2 <= 0 AND nbumps4 <= 0|0 (23.0/2.0)
ghazard = a AND seismoacoustic = b AND seismic = a AND nbumps4 <= 0|0 (84.0/16.0)
nbumps4 > 0 AND ghazard = a AND shift = W AND nbumps2 <= 0 AND nbumps3 <= 1|0 (14.0)
nbumps3 <= 0 AND ghazard = a AND shift = W AND nbumps4 <= 0 AND seismoacoustic = b AND nbumps > 1|0 (6.0)
nbumps4 > 0 AND ghazard = a AND seismoacoustic = a AND genergy <= 189170 AND nbumps2 > 1|0 (14.0)
seismoacoustic = b AND seismic = a AND nbumps3 > 0|0 (7.0)
seismic = b AND shift = N AND genergy > 17910|0 (10.0)
ghazard = a AND seismoacoustic = b AND shift = W AND nbumps4 > 0 AND energy <= 34000|0 (10.0)
seismic = b AND nbumps2 <= 1 AND seismoacoustic = b AND nbumps2 <= 0 AND nbumps <= 1|0 (15.0/3.0)
seismic = b AND shift = W AND seismoacoustic = a AND genergy <= 85240 AND nbumps3 <= 0|0 (14.0)
seismic = b AND seismoacoustic = b AND nbumps2 > 0 AND ghazard = a AND nbumps4 <= 0 AND nbumps3 <= 1 AND maxenergy <= 2000|0 (7.0/1.0)
shift = W AND seismic = b AND seismoacoustic = b AND nbumps2 > 0 AND gdpuls <= 92 AND nbumps4 > 0 AND gdpuls <= 37|0 (9.0/4.0)
nbumps4 > 0 AND nbumps2 <= 1 AND maxenergy <= 60000 AND nbumps3 <= 2 AND ghazard = a AND nbumps > 3|0 (8.0/2.0)
nbumps4 > 0 AND nbumps2 <= 1 AND nbumps <= 3 AND maxenergy <= 60000 AND ghazard = a AND nbumps > 2|1 (7.0/3.0)
nbumps4 > 0 AND nbumps2 <= 1 AND energy > 30300|0 (15.0)
shift = N|1 (8.0/3.0)
ghazard = b AND nbumps <= 2 AND gdenergy <= 77|1 (6.0/2.0)
nbumps4 <= 0 AND seismoacoustic = b AND maxenergy <= 7000 AND ghazard = a AND gdpuls <= -2|0 (6.0/1.0)
seismoacoustic = a AND nbumps4 <= 0|0 (47.0/22.0)
gdpuls <= 92 AND seismoacoustic = b AND maxenergy <= 7000 AND nbumps2 > 1|1 (8.0/4.0)
gdpuls <= 92 AND seismoacoustic = b AND maxenergy > 6000|0 (8.0)
nbumps <= 4 AND seismoacoustic = a|1 (7.0/3.0)
nbumps2 <= 1 AND genergy <= 122850|1 (6.0/1.0)
nbumps2 <= 1|0 (6.0/1.0)
|1 (5.0)


## J48 Decision Tree

* nbumps <= 1.5: 0 (1666.0/56.0)
* nbumps > 1.5
	* shift = W
		* ghazard = a
			* nbumps2 <= 0.5: 0 (71.0/8.0)
			* nbumps2 > 0.5
				* genergy <= 55650: 0 (137.0/14.0)
				* genergy > 55650
					* seismoacoustic = a
						* nbumps4 <= 0.5
							* seismic = a: 0 (47.0/14.0)
							* seismic = b
								* nbumps <= 3.5
									* nbumps2 <= 1.5
										* gpuls <= 930: 0 (6.0)
										* gpuls > 930: 1 (9.0/4.0)
									* nbumps2 > 1.5
										* genergy <= 119985: 0 (5.0/2.0)
										* genergy > 119985: 1 (5.0)
								* nbumps > 3.5: 0 (6.0/1.0)
							* seismic = c: 0 (0.0)
							* seismic = d: 0 (0.0)
						* nbumps4 > 0.5: 0 (24.0/6.0)
					* seismoacoustic = b: 0 (67.0/17.0)
					* seismoacoustic = c: 0 (4.0/1.0)
					* seismoacoustic = d: 0 (0.0)
		* ghazard = b: 0 (23.0/7.0)
		* ghazard = c: 0 (1.0)
		* ghazard = d: 0 (0.0)
	* shift = N: 0 (23.0/2.0)


## SimpleCart Decision Tree

* : 0(2173.0/153.0)


