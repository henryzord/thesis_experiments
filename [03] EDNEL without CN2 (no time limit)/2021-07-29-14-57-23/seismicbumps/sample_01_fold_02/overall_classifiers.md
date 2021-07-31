# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 0 | 0.935345 |
| nbumps >= 1.5 and gpuls >= 740.5 and gdenergy < -29.5 | 1 | 0.004034 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| nbumps <= 1.5 and gpuls <= 1342.5 and shift = N | 0 | 0.838323 |
| nbumps <= 1.5 and nbumps4 > 0.5 | 0 | 0.189335 |
| nbumps <= 1.5 and gpuls <= 1342.5 and ghazard = b and nbumps <= 0.5 and seismoacoustic = b and seismic = a | 0 | 0.171438 |
| nbumps <= 1.5 and gpuls <= 1342.5 and ghazard = a | 0 | 0.835323 |
| ghazard = b and nbumps <= 1.5 and nbumps <= 0.5 and genergy > 21325 | 0 | 0.189335 |
| ghazard = b and nbumps4 <= 0.5 and nbumps <= 1.5 and nbumps > 0.5 | 0 | 0.180328 |
| ghazard = c | 0 | 0.112426 |
| seismic = a | 0 | 0.597113 |
| shift = W and ghazard = a and seismoacoustic = b and nbumps2 <= 0.5 | 0 | 0.059416 |
| shift = W and seismoacoustic = a and genergy <= 91035 | 0 | 0.225489 |
| shift = W and seismoacoustic = b and ghazard = a and maxenergy <= 2500 | 0 | 0.025900 |
| shift = W and seismoacoustic = b and nbumps4 > 0.5 and gdpuls <= 93 and maxenergy > 25000 and genergy > 67480 | 0 | 0.051266 |
| shift = W and seismoacoustic = a and nbumps4 > 0.5 and nbumps2 > 0.5 and gdenergy <= 43 | 0 | 0.056654 |
| shift = W and seismoacoustic = b and maxenergy <= 25000 and ghazard = b and genergy <= 19400 | 0 | 0.044586 |
| shift = W and seismoacoustic = a and nbumps2 <= 0.5 and nbumps4 > 0.5 | 0 | 0.057176 |
| shift = W and maxenergy <= 25000 and seismoacoustic = b and nbumps4 > 0.5 and gdpuls <= 93 | 0 | 0.050633 |
| shift = W and nbumps4 > 0.5 | 1 | 0.279551 |
| shift = N | 0 | 0.011201 |
| seismoacoustic = b and ghazard = b and nbumps > 1 and gdenergy <= 88 | 1 | 0.076190 |
| seismoacoustic = b and ghazard = b and nbumps <= 1 | 1 | 0.065041 |
| ghazard = a and nbumps2 <= 3.5 and seismoacoustic = a and gpuls <= 1696 and gpuls > 1201 | 1 | 0.264151 |
| ghazard = a and seismoacoustic = a and nbumps2 <= 2.5 and nbumps2 <= 1.5 and gdenergy <= 4.5 | 0 | 0.028177 |
| ghazard = a and nbumps2 <= 3.5 and seismoacoustic = a and nbumps <= 3.5 and gdenergy <= 31 | 1 | 0.608396 |
|  | 0 | 0.311828 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| nbumps >= 2 and gpuls >= 744 and gdenergy <= -30 | 1 | 0.004034 |
|  | 0 | 0.942249 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

class
---
0

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
nbumps <= 1.5 AND gpuls <= 1342.5 AND shift = N|0 (797.0/10.0)
nbumps <= 1.5 AND nbumps4 > 0.5|0 (36.0)
nbumps <= 1.5 AND gpuls <= 1342.5 AND ghazard = b AND nbumps <= 0.5 AND seismoacoustic = b AND seismic = a|0 (33.0/1.0)
nbumps <= 1.5 AND gpuls <= 1342.5 AND ghazard = a|0 (822.0/32.0)
ghazard = b AND nbumps <= 1.5 AND nbumps <= 0.5 AND genergy > 21325|0 (36.0)
ghazard = b AND nbumps4 <= 0.5 AND nbumps <= 1.5 AND nbumps > 0.5|0 (33.0)
ghazard = c|0 (19.0)
seismic = a|0 (303.0/48.0)
shift = W AND ghazard = a AND seismoacoustic = b AND nbumps2 <= 0.5|0 (18.0/1.0)
shift = W AND seismoacoustic = a AND genergy <= 91035|0 (71.0/7.0)
shift = W AND seismoacoustic = b AND ghazard = a AND maxenergy <= 2500|0 (10.0)
shift = W AND seismoacoustic = b AND nbumps4 > 0.5 AND gdpuls <= 93 AND maxenergy > 25000 AND genergy > 67480|0 (10.0/1.0)
shift = W AND seismoacoustic = a AND nbumps4 > 0.5 AND nbumps2 > 0.5 AND gdenergy <= 43|0 (18.0/5.0)
shift = W AND seismoacoustic = b AND maxenergy <= 25000 AND ghazard = b AND genergy <= 19400|0 (7.0)
shift = W AND seismoacoustic = a AND nbumps2 <= 0.5 AND nbumps4 > 0.5|0 (11.0/1.0)
shift = W AND maxenergy <= 25000 AND seismoacoustic = b AND nbumps4 > 0.5 AND gdpuls <= 93|0 (8.0)
shift = W AND nbumps4 > 0.5|1 (11.0/1.0)
shift = N|0 (5.0)
seismoacoustic = b AND ghazard = b AND nbumps > 1 AND gdenergy <= 88|1 (4.0/1.0)
seismoacoustic = b AND ghazard = b AND nbumps <= 1|1 (5.0/2.0)
ghazard = a AND nbumps2 <= 3.5 AND seismoacoustic = a AND gpuls <= 1696 AND gpuls > 1201|1 (8.0)
ghazard = a AND seismoacoustic = a AND nbumps2 <= 2.5 AND nbumps2 <= 1.5 AND gdenergy <= 4.5|0 (11.0/1.0)
ghazard = a AND nbumps2 <= 3.5 AND seismoacoustic = a AND nbumps <= 3.5 AND gdenergy <= 31|1 (10.0/1.0)
|0 (34.0/10.0)


## SimpleCart Decision Tree

* nbumps < 1.5
	* gpuls < 1342.5
		* genergy < 16885.0
			* genergy < 1865.0: 0(39.0/2.0)
			* genergy >= 1865.0
				* gdpuls < -5.5
					* nbumps < 0.5: 0(424.0/0.0)
					* nbumps >= 0.5: 0(81.0/1.0)
				* gdpuls >= -5.5: 0(238.0/4.0)
		* genergy >= 16885.0: 0(942.0/39.0)
	* gpuls >= 1342.5: 0(62.0/13.0)
* nbumps >= 1.5
	* gpuls < 740.5
		* nbumps3 < 3.5
			* genergy < 21865.0: 0(33.0/11.0)
			* genergy >= 21865.0: 0(194.0/22.0)
		* nbumps3 >= 3.5: 0(9.0/6.0)
	* gpuls >= 740.5
		* gdenergy < -29.5: 1(17.0/16.0)
		* gdenergy >= -29.5
			* nbumps2 < 0.5: 0(36.0/2.0)
			* nbumps2 >= 0.5: 0(96.0/33.0)


