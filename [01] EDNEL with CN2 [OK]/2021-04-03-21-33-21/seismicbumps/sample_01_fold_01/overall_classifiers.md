# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| nbumps <= 1.5 and gpuls <= 1342 | 0 | 0.917282 |
| nbumps > 1.5 and nbumps2 > 0.5 and ghazard = a and nbumps4 <= 0.5 | 0 | 0.558800 |
| nbumps > 1.5 and nbumps2 <= 0.5 | 0 | 0.316517 |
| nbumps <= 1.5 and gpuls > 1342 and nbumps3 <= 0.5 | 0 | 0.248358 |
| nbumps >= 1.5 and gpuls < 677.0 and seismoacoustic != d and genergy < 39510.0 and nbumps3 >= 1.5 | 1 | 0.001406 |
| nbumps > 1.5 and nbumps2 > 0.5 and ghazard = b | 0 | 0.079024 |
| nbumps > 1.5 and nbumps2 > 0.5 and ghazard = a and nbumps4 > 0.5 and seismic = b and nbumps4 <= 1.5 and seismoacoustic = b | 0 | 0.072208 |
| nbumps < 1.5 and gpuls >= 1342.5 and nbumps3 >= 0.5 | 1 | 0.002304 |
| nbumps > 1.5 and nbumps2 > 0.5 and ghazard = a and nbumps4 > 0.5 and seismic = b and nbumps4 <= 1.5 and seismoacoustic = a and nbumps2 > 1.5 | 0 | 0.072208 |
| nbumps > 1.5 and nbumps2 > 0.5 and ghazard = a and nbumps4 > 0.5 and seismic = a | 0 | 0.043750 |
| nbumps > 1.5 and nbumps2 > 0.5 and ghazard = a and nbumps4 > 0.5 and seismic = b and nbumps4 <= 1.5 and seismoacoustic = a and nbumps2 <= 1.5 and energy <= 37250 | 1 | 0.001228 |
| nbumps > 1.5 and nbumps2 > 0.5 and ghazard = a and nbumps4 > 0.5 and seismic = b and nbumps4 > 1.5 | 0 | 0.034459 |
| nbumps > 1.5 and nbumps2 > 0.5 and ghazard = a and nbumps4 > 0.5 and seismic = b and nbumps4 <= 1.5 and seismoacoustic = a and nbumps2 <= 1.5 and energy > 37250 | 0 | 0.037736 |
| nbumps <= 1.5 and gpuls > 1342 and nbumps3 > 0.5 and seismic = a | 0 | 0.022894 |
| nbumps > 1.5 and nbumps2 > 0.5 and ghazard = c | 0 | 0.012903 |
| nbumps > 1.5 and nbumps2 > 0.5 and ghazard = a and nbumps4 > 0.5 and seismic = b and nbumps4 <= 1.5 and seismoacoustic = c | 0 | 0.006494 |
| nbumps >= 1.5 and gpuls >= 677.0 and gdpuls < 36.0 and nbumps2 >= 0.5 | 0 | 0.222512 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| nbumps <= 1.5 and gpuls <= 1342.5 and seismoacoustic != c and ghazard != c and shift != W and nbumps <= 0.5 and seismic = a and ghazard = a and seismoacoustic = a | 0 | 0.696566 |
| nbumps <= 1.5 and gpuls <= 1342.5 and seismoacoustic != c and ghazard != c and shift != W and nbumps <= 0.5 and seismic = a and ghazard = a | 0 | 0.469600 |
| nbumps <= 1.5 and gpuls <= 1342.5 and seismoacoustic != c and ghazard != c and ghazard != a and seismic = a | 0 | 0.264423 |
| nbumps <= 1.5 and gpuls <= 1342.5 and seismoacoustic != c and ghazard != c and shift != W and nbumps <= 0.5 | 0 | 0.403567 |
| nbumps <= 1.5 and gpuls <= 1342.5 and seismoacoustic != c and ghazard != c and nbumps3 > 0.5 and ghazard = a and shift != W and seismic = a and seismoacoustic = a | 0 | 0.301437 |
| nbumps <= 1.5 and gpuls <= 1342.5 and seismoacoustic != c and ghazard != c and shift = W and nbumps4 <= 0.5 and ghazard = a and seismic = a and nbumps2 <= 0.5 and energy <= 1500.0 and seismoacoustic = a | 0 | 0.562470 |
| nbumps <= 1.5 and seismoacoustic != c and gpuls <= 1342.5 and ghazard != c and nbumps3 > 0.5 and ghazard = a and seismoacoustic = a and energy <= 7500.0 | 0 | 0.311351 |
| nbumps <= 1.5 and seismoacoustic != c and nbumps3 <= 0.5 and ghazard != c and shift = W and nbumps4 <= 0.5 and genergy <= 18755.0 and seismoacoustic = a | 0 | 0.343552 |
| nbumps <= 1.5 and seismoacoustic != c and nbumps3 <= 0.5 and ghazard != c and seismoacoustic != a and shift = W and nbumps > 0.5 and seismic != a | 0 | 0.181818 |
| nbumps <= 1.5 and seismoacoustic = c | 0 | 0.177419 |
| nbumps <= 1.5 and nbumps3 <= 0.5 and ghazard != c and seismoacoustic != a and shift = W and ghazard = a and nbumps > 0.5 and nbumps2 > 0.5 and energy > 250.0 | 0 | 0.115607 |
| nbumps <= 1.5 and nbumps3 <= 0.5 and ghazard != c and nbumps <= 0.5 and seismoacoustic != a and ghazard = a and seismic = a | 0 | 0.426263 |
| nbumps <= 1.5 and ghazard != c and nbumps3 <= 0.5 and seismic != a and shift = W and nbumps4 <= 0.5 and ghazard = a and seismoacoustic = a and nbumps <= 0.5 and gdpuls <= 100.0 | 0 | 0.383691 |
| nbumps <= 2.5 and ghazard != c and gpuls <= 1253.5 and ghazard = a and shift != W and nbumps4 <= 0.5 and seismoacoustic != a and seismic = a and nbumps2 <= 0.5 | 0 | 0.131524 |
| nbumps <= 2.5 and ghazard != c and gpuls <= 1253.5 and nbumps <= 1.5 and nbumps3 > 0.5 and seismoacoustic != a and seismic != a | 0 | 0.168478 |
| nbumps3 <= 0.5 and ghazard != c and nbumps <= 1.5 and nbumps4 > 0.5 and shift = W | 0 | 0.154696 |
| nbumps3 <= 0.5 and ghazard != c and nbumps4 <= 0.5 and nbumps <= 1.5 and seismoacoustic != a and nbumps <= 0.5 and ghazard = a | 0 | 0.335327 |
| ghazard != c and seismic = a and seismoacoustic != c and shift != W and nbumps2 > 0.5 and nbumps3 <= 0.5 and maxenergy <= 650.0 | 0 | 0.203125 |
| ghazard = c | 0 | 0.049689 |
| seismoacoustic != c and seismic = a and shift = W and ghazard != a and maxenergy > 1500.0 | 0 | 0.037736 |
| seismoacoustic != c and seismic = a and ghazard = a and shift = W and seismoacoustic = a | 0 | 0.518221 |
| seismoacoustic != c and seismic = a and ghazard = a and seismoacoustic != a and nbumps4 <= 0.5 and shift = W and nbumps2 <= 0.5 and nbumps3 <= 1.5 | 0 | 0.121096 |
| nbumps3 <= 0.5 and seismic != a and nbumps4 <= 0.5 and shift != W and seismoacoustic = a | 0 | 0.043750 |
| nbumps3 <= 0.5 and seismic != a and ghazard != a and seismoacoustic != a and nbumps <= 1.5 and genergy > 21325.0 | 0 | 0.159341 |
| seismoacoustic != c and seismic = a and ghazard = a and seismoacoustic != a and shift != W and genergy <= 32650.0 | 0 | 0.020513 |
| seismoacoustic != c and nbumps4 > 0.5 and nbumps2 <= 0.5 and shift = W and nbumps3 <= 1.5 | 0 | 0.089286 |
| seismoacoustic != c and seismic = a and ghazard = a and shift = W | 0 | 0.211156 |
| nbumps3 <= 0.5 and gdenergy > -48.0 and shift != W and seismoacoustic = a | 0 | 0.031210 |
| seismic != a and genergy <= 108515.0 and nbumps3 <= 2.5 and shift = W and seismoacoustic = a and ghazard = a and nbumps > 0.5 and nbumps4 > 0.5 and nbumps2 > 1.5 | 0 | 0.067073 |
| seismic != a and genergy <= 91035.0 and seismoacoustic = a and ghazard = a and nbumps > 0.5 and maxenergy <= 750.0 | 0 | 0.140449 |
| gdenergy <= 185.0 and nbumps > 1.5 and ghazard = a and nbumps2 <= 0.5 and gdpuls > -20.0 | 0 | 0.107456 |
| gdenergy > 185.0 | 0 | 0.083832 |
| nbumps2 > 0.5 and ghazard = a and seismoacoustic != c and seismic = a and gpuls <= 110.0 | 0 | 0.037736 |
| seismic != a and nbumps2 > 0.5 and shift = W and ghazard = a and seismoacoustic != a and maxenergy <= 2500.0 | 0 | 0.061350 |
| seismic != a and nbumps2 > 0.5 and seismoacoustic != b | 0 | 0.239106 |
| seismoacoustic != b and shift = W | 1 | 0.558449 |
| seismoacoustic != a and nbumps4 > 0.5 and ghazard = a and nbumps2 > 1.5 and maxenergy <= 25000.0 | 0 | 0.049603 |
| seismoacoustic = a | 1 | 0.100000 |
| nbumps4 > 0.5 and nbumps2 <= 2.5 and gdenergy > 0.5 and energy > 35300.0 | 0 | 0.093750 |
| ghazard != a and genergy > 19220.0 and seismic != a | 1 | 0.078431 |
| nbumps <= 0.5 | 0 | 0.120000 |
| ghazard != a | 0 | 0.157757 |
| nbumps2 > 1.5 and gdpuls <= 35.5 and nbumps <= 4.5 | 0 | 0.018182 |
| nbumps2 > 1.5 and gdpuls <= 35.5 | 1 | 0.311688 |
| nbumps2 <= 1.5 and maxenergy > 3500.0 and nbumps > 2.5 and genergy > 43255.0 | 0 | 0.066667 |
| nbumps2 <= 1.5 and maxenergy > 3500.0 | 1 | 0.403226 |
| gdenergy <= 26.0 | 0 | 0.323276 |
|  | 1 | 0.851852 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| nbumps >= 2 and gpuls >= 679 and gdpuls <= 21 and nbumps2 >= 1 and nbumps <= 3 and energy >= 5800 and nbumps4 <= 0 and gdenergy >= -32 | 1 | 0.004130 |
| nbumps >= 2 and gpuls >= 768 and gdenergy <= -30 and nbumps2 >= 1 | 1 | 0.003676 |
| nbumps >= 3 and seismic = b | 1 | 0.002887 |
|  | 0 | 0.953846 |


# Text representation of classifiers as-is

## JRip

Decision list:

rules | predicted class
---|---
(nbumps >= 2) and (gpuls >= 679) and (gdpuls <= 21) and (nbumps2 >= 1) and (nbumps <= 3) and (energy >= 5800) and (nbumps4 <= 0) and (gdenergy >= -32)|1 (9.0/0.0)
(nbumps >= 2) and (gpuls >= 768) and (gdenergy <= -30) and (nbumps2 >= 1)|1 (18.0/6.0)
(nbumps >= 3) and (seismic = b)|1 (117.0/90.0)
|0 (2179.0/105.0)


## PART

Decision list:

rules | predicted class
---|---
nbumps <= 1.5 AND gpuls <= 1342.5 AND seismoacoustic != c AND ghazard != c AND shift != W AND nbumps <= 0.5 AND seismic = a AND ghazard = a AND seismoacoustic = a|0 (361.0/5.0)
nbumps <= 1.5 AND gpuls <= 1342.5 AND seismoacoustic != c AND ghazard != c AND shift != W AND nbumps <= 0.5 AND seismic = a AND ghazard = a|0 (142.0/1.0)
nbumps <= 1.5 AND gpuls <= 1342.5 AND seismoacoustic != c AND ghazard != c AND ghazard != a AND seismic = a|0 (55.0)
nbumps <= 1.5 AND gpuls <= 1342.5 AND seismoacoustic != c AND ghazard != c AND shift != W AND nbumps <= 0.5|0 (109.0)
nbumps <= 1.5 AND gpuls <= 1342.5 AND seismoacoustic != c AND ghazard != c AND nbumps3 > 0.5 AND ghazard = a AND shift != W AND seismic = a AND seismoacoustic = a|0 (68.0/1.0)
nbumps <= 1.5 AND gpuls <= 1342.5 AND seismoacoustic != c AND ghazard != c AND shift = W AND nbumps4 <= 0.5 AND ghazard = a AND seismic = a AND nbumps2 <= 0.5 AND energy <= 1500.0 AND seismoacoustic = a|0 (212.0/8.0)
nbumps <= 1.5 AND seismoacoustic != c AND gpuls <= 1342.5 AND ghazard != c AND nbumps3 > 0.5 AND ghazard = a AND seismoacoustic = a AND energy <= 7500.0|0 (72.0)
nbumps <= 1.5 AND seismoacoustic != c AND nbumps3 <= 0.5 AND ghazard != c AND shift = W AND nbumps4 <= 0.5 AND genergy <= 18755.0 AND seismoacoustic = a|0 (82.0)
nbumps <= 1.5 AND seismoacoustic != c AND nbumps3 <= 0.5 AND ghazard != c AND seismoacoustic != a AND shift = W AND nbumps > 0.5 AND seismic != a|0 (34.0)
nbumps <= 1.5 AND seismoacoustic = c|0 (33.0)
nbumps <= 1.5 AND nbumps3 <= 0.5 AND ghazard != c AND seismoacoustic != a AND shift = W AND ghazard = a AND nbumps > 0.5 AND nbumps2 > 0.5 AND energy > 250.0|0 (20.0)
nbumps <= 1.5 AND nbumps3 <= 0.5 AND ghazard != c AND nbumps <= 0.5 AND seismoacoustic != a AND ghazard = a AND seismic = a|0 (126.0/6.0)
nbumps <= 1.5 AND ghazard != c AND nbumps3 <= 0.5 AND seismic != a AND shift = W AND nbumps4 <= 0.5 AND ghazard = a AND seismoacoustic = a AND nbumps <= 0.5 AND gdpuls <= 100.0|0 (103.0/4.0)
nbumps <= 2.5 AND ghazard != c AND gpuls <= 1253.5 AND ghazard = a AND shift != W AND nbumps4 <= 0.5 AND seismoacoustic != a AND seismic = a AND nbumps2 <= 0.5|0 (26.0/1.0)
nbumps <= 2.5 AND ghazard != c AND gpuls <= 1253.5 AND nbumps <= 1.5 AND nbumps3 > 0.5 AND seismoacoustic != a AND seismic != a|0 (31.0)
nbumps3 <= 0.5 AND ghazard != c AND nbumps <= 1.5 AND nbumps4 > 0.5 AND shift = W|0 (28.0)
nbumps3 <= 0.5 AND ghazard != c AND nbumps4 <= 0.5 AND nbumps <= 1.5 AND seismoacoustic != a AND nbumps <= 0.5 AND ghazard = a|0 (92.0/5.0)
ghazard != c AND seismic = a AND seismoacoustic != c AND shift != W AND nbumps2 > 0.5 AND nbumps3 <= 0.5 AND maxenergy <= 650.0|0 (39.0)
ghazard = c|0 (8.0)
seismoacoustic != c AND seismic = a AND shift = W AND ghazard != a AND maxenergy > 1500.0|0 (6.0)
seismoacoustic != c AND seismic = a AND ghazard = a AND shift = W AND seismoacoustic = a|0 (218.0/29.0)
seismoacoustic != c AND seismic = a AND ghazard = a AND seismoacoustic != a AND nbumps4 <= 0.5 AND shift = W AND nbumps2 <= 0.5 AND nbumps3 <= 1.5|0 (29.0/2.0)
nbumps3 <= 0.5 AND seismic != a AND nbumps4 <= 0.5 AND shift != W AND seismoacoustic = a|0 (7.0)
nbumps3 <= 0.5 AND seismic != a AND ghazard != a AND seismoacoustic != a AND nbumps <= 1.5 AND genergy > 21325.0|0 (29.0)
seismoacoustic != c AND seismic = a AND ghazard = a AND seismoacoustic != a AND shift != W AND genergy <= 32650.0|0 (4.0)
seismoacoustic != c AND nbumps4 > 0.5 AND nbumps2 <= 0.5 AND shift = W AND nbumps3 <= 1.5|0 (15.0)
seismoacoustic != c AND seismic = a AND ghazard = a AND shift = W|0 (77.0/13.0)
nbumps3 <= 0.5 AND gdenergy > -48.0 AND shift != W AND seismoacoustic = a|0 (7.0)
seismic != a AND genergy <= 108515.0 AND nbumps3 <= 2.5 AND shift = W AND seismoacoustic = a AND ghazard = a AND nbumps > 0.5 AND nbumps4 > 0.5 AND nbumps2 > 1.5|0 (11.0)
seismic != a AND genergy <= 91035.0 AND seismoacoustic = a AND ghazard = a AND nbumps > 0.5 AND maxenergy <= 750.0|0 (25.0)
gdenergy <= 185.0 AND nbumps > 1.5 AND ghazard = a AND nbumps2 <= 0.5 AND gdpuls > -20.0|0 (21.0)
gdenergy > 185.0|0 (14.0)
nbumps2 > 0.5 AND ghazard = a AND seismoacoustic != c AND seismic = a AND gpuls <= 110.0|0 (6.0)
seismic != a AND nbumps2 > 0.5 AND shift = W AND ghazard = a AND seismoacoustic != a AND maxenergy <= 2500.0|0 (10.0)
seismic != a AND nbumps2 > 0.5 AND seismoacoustic != b|0 (93.0/28.0)
seismoacoustic != b AND shift = W|1 (26.0/11.0)
seismoacoustic != a AND nbumps4 > 0.5 AND ghazard = a AND nbumps2 > 1.5 AND maxenergy <= 25000.0|0 (7.0/2.0)
seismoacoustic = a|1 (6.0/1.0)
nbumps4 > 0.5 AND nbumps2 <= 2.5 AND gdenergy > 0.5 AND energy > 35300.0|0 (6.0)
ghazard != a AND genergy > 19220.0 AND seismic != a|1 (16.0/8.0)
nbumps <= 0.5|0 (7.0)
ghazard != a|0 (6.0/2.0)
nbumps2 > 1.5 AND gdpuls <= 35.5 AND nbumps <= 4.5|0 (5.0/2.0)
nbumps2 > 1.5 AND gdpuls <= 35.5|1 (5.0/2.0)
nbumps2 <= 1.5 AND maxenergy > 3500.0 AND nbumps > 2.5 AND genergy > 43255.0|0 (5.0/2.0)
nbumps2 <= 1.5 AND maxenergy > 3500.0|1 (8.0)
gdenergy <= 26.0|0 (8.0)
|1 (5.0/2.0)


## J48 Decision Tree

* nbumps <= 1.5
	* gpuls <= 1342: 0 (1433.0/43.0)
	* gpuls > 1342
		* nbumps3 <= 0.5: 0 (49.0/5.0)
		* nbumps3 > 0.5
			* seismic = a: 0 (6.0/2.0)
			* seismic = b: 1 (11.0/5.0)
			* seismic = c: 0 (0.0)
			* seismic = d: 0 (0.0)
* nbumps > 1.5
	* nbumps2 <= 0.5: 0 (64.0/5.0)
	* nbumps2 > 0.5
		* ghazard = a
			* nbumps4 <= 0.5: 0 (225.0/49.0)
			* nbumps4 > 0.5
				* seismic = a: 0 (7.0)
				* seismic = b
					* nbumps4 <= 1.5
						* seismoacoustic = a
							* nbumps2 <= 1.5
								* energy <= 37250: 1 (3.0/1.0)
								* energy > 37250: 0 (6.0)
							* nbumps2 > 1.5: 0 (14.0/2.0)
						* seismoacoustic = b: 0 (12.0/1.0)
						* seismoacoustic = c: 0 (1.0)
						* seismoacoustic = d: 0 (0.0)
					* nbumps4 > 1.5: 0 (8.0/2.0)
				* seismic = c: 0 (0.0)
				* seismic = d: 0 (0.0)
		* ghazard = b: 0 (20.0/6.0)
		* ghazard = c: 0 (0.0)
		* ghazard = d: 0 (0.0)


## SimpleCart Decision Tree

* nbumps < 1.5
	* gpuls < 1342.5
		* genergy < 16885.0: 0(780.0/11.0)
		* genergy >= 16885.0: 0(950.0/40.0)
	* gpuls >= 1342.5
		* nbumps3 < 0.5: 0(55.0/5.0)
		* nbumps3 >= 0.5: 1(10.0/10.0)
* nbumps >= 1.5
	* gpuls < 677.0
				* seismoacoustic=(c)|(a)|(d): 0(144.0/15.0)
				* seismoacoustic!=(c)|(a)|(d)
			* genergy < 39510.0
				* nbumps3 < 1.5: 0(21.0/7.0)
				* nbumps3 >= 1.5: 1(7.0/4.0)
			* genergy >= 39510.0
				* gdenergy < 67.5: 0(38.0/1.0)
				* gdenergy >= 67.5: 0(10.0/6.0)
	* gpuls >= 677.0
		* gdpuls < 36.0
			* nbumps2 < 0.5: 0(30.0/3.0)
			* nbumps2 >= 0.5: 0(64.0/40.0)
		* gdpuls >= 36.0: 0(64.0/8.0)


