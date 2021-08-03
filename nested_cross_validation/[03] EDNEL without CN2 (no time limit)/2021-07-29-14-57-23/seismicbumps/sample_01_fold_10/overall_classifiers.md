# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 0 | 0.935345 |
| nbumps > 1.0 and nbumps3 <= 3.0 and gpuls > 740.0 and gdenergy > -30.0 and maxenergy <= 40000.0 and gdpuls > -24.0 and genergy > 50580.0 and gdpuls > -20.0 and gdenergy > -15.0 and gdenergy <= -5.0 and genergy <= 514800.0 | 1 | 0.001644 |
| nbumps >= 1.5 and gpuls >= 884.0 and gdenergy < -29.5 and nbumps2 < 0.5 and genergy < 438160.0 | 1 | 0.000691 |
| nbumps >= 1.5 and gpuls < 884.0 and nbumps3 >= 3.5 and gpuls >= 364.0 | 1 | 0.001657 |
| nbumps >= 1.5 and gpuls >= 884.0 and gdenergy >= -29.5 and gpuls < 2211.5 and energy < 28650.0 and energy >= 21000.0 | 1 | 0.001917 |
| nbumps >= 1.5 and gpuls >= 884.0 and gdenergy >= -29.5 and gpuls >= 2211.5 and genergy >= 289800.0 and genergy < 1124825.0 | 1 | 0.003272 |
| nbumps > 1.0 and nbumps3 <= 3.0 and gpuls > 740.0 and gdenergy > -30.0 and maxenergy <= 40000.0 and gdpuls > -24.0 and genergy > 50580.0 and gdpuls > -20.0 and gdenergy > -15.0 and gdenergy > -5.0 and gdpuls > 5.0 and maxenergy > 900.0 and nbumps2 > 0.0 and genergy <= 1034700.0 and genergy <= 532290.0 and gpuls <= 1777.0 and energy <= 4400.0 | 1 | 0.001841 |
| nbumps > 1.0 and nbumps3 > 3.0 and gpuls > 364.0 and genergy <= 69070.0 | 1 | 0.002070 |
| nbumps >= 1.5 and gpuls >= 884.0 and gdenergy < -29.5 and nbumps2 >= 0.5 | 1 | 0.004132 |
| nbumps > 1.0 and nbumps3 <= 3.0 and gpuls > 740.0 and gdenergy > -30.0 and maxenergy <= 40000.0 and gdpuls > -24.0 and genergy > 50580.0 and gdpuls <= -20.0 | 1 | 0.001053 |
| nbumps > 1.0 and nbumps3 <= 3.0 and gpuls > 740.0 and gdenergy <= -30.0 and nbumps2 > 0.0 | 1 | 0.003891 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| nbumps <= 1.5 and gpuls <= 1342.5 and seismoacoustic != c and shift != W and nbumps <= 0.5 and seismic = a and seismoacoustic = a | 0 | 0.706543 |
| nbumps <= 1.5 and gpuls <= 1342.5 and seismoacoustic != c and shift != W and nbumps <= 0.5 and seismic = a | 0 | 0.483333 |
| nbumps <= 1.5 and gpuls <= 1342.5 and seismoacoustic != c and nbumps4 <= 0.5 and shift != W and nbumps <= 0.5 | 0 | 0.400909 |
| nbumps <= 1.5 and gpuls <= 1342.5 and seismoacoustic = c | 0 | 0.189189 |
| nbumps <= 1.5 and gpuls <= 1342.5 and nbumps4 <= 0.5 and seismic = a and ghazard != a and nbumps <= 0.5 | 0 | 0.180484 |
| nbumps <= 1.5 and gpuls <= 1342.5 and nbumps4 <= 0.5 and seismic = a and ghazard = a and shift != W and nbumps3 > 0.5 and seismoacoustic = a and energy <= 4500.0 | 0 | 0.242424 |
| nbumps <= 1.5 and gpuls <= 1342.5 and shift = W and nbumps4 <= 0.5 and seismic = a and seismoacoustic = a and nbumps2 <= 0.5 and nbumps <= 0.5 | 0 | 0.556587 |
| nbumps <= 1.5 and gpuls <= 1342.5 and nbumps2 > 0.5 and ghazard = a and seismoacoustic != a and shift = W | 0 | 0.234694 |
| nbumps <= 1.5 and gpuls <= 1252.5 and nbumps3 > 0.5 and energy > 1500.0 and ghazard = a and shift = W and seismic = a | 0 | 0.285714 |
| nbumps <= 1.5 and nbumps3 <= 0.5 and shift = W and nbumps4 <= 0.5 and genergy <= 18755.0 and seismoacoustic = a | 0 | 0.359169 |
| nbumps <= 1.5 and nbumps3 <= 0.5 and nbumps4 > 0.5 and gdpuls > -24.0 | 0 | 0.184783 |
| gpuls <= 1139.5 and nbumps <= 1.5 and seismoacoustic != a and nbumps3 > 0.5 and seismic = a | 0 | 0.171902 |
| nbumps <= 1.5 and nbumps3 <= 0.5 and ghazard != a and genergy > 21310.0 | 0 | 0.234800 |
| gpuls <= 1137.5 and ghazard != b and nbumps <= 2.5 and nbumps3 <= 0.5 and maxenergy <= 650.0 and nbumps2 > 0.5 and shift != W and seismoacoustic = a | 0 | 0.162011 |
| gpuls <= 1137.5 and ghazard != b and nbumps <= 2.5 and nbumps <= 0.5 and seismoacoustic != a and seismic = a | 0 | 0.417918 |
| gpuls <= 1137.5 and ghazard != b and nbumps <= 2.5 and seismic != a and nbumps2 <= 0.5 and seismoacoustic != a and nbumps <= 0.5 | 0 | 0.334190 |
| nbumps3 <= 3.5 and ghazard != b and gpuls <= 1137.5 and seismoacoustic = a and nbumps <= 4.5 and seismic != a and gdpuls > -51.5 and nbumps4 <= 0.5 | 0 | 0.538623 |
| nbumps3 <= 3.5 and seismic = a and ghazard != b and gdenergy > -27.0 and shift != W and seismoacoustic != a | 0 | 0.096720 |
| nbumps3 <= 3.5 and seismic = a and ghazard != b and seismoacoustic = a and nbumps <= 4.5 and shift = W | 0 | 0.499862 |
| nbumps3 <= 3.5 and seismic = a and ghazard != b and seismoacoustic = a and genergy > 14350.0 and shift = W | 0 | 0.051064 |
| nbumps2 <= 0.5 and seismoacoustic = b and nbumps3 > 0.5 and seismic != a and nbumps <= 1.5 and energy <= 3500.0 | 0 | 0.112426 |
| seismic = a and nbumps3 <= 2.5 and ghazard != b and seismoacoustic = a and nbumps2 <= 0.5 and energy <= 5500.0 | 0 | 0.039643 |
| seismic = a and nbumps3 <= 2.5 and ghazard != b and seismoacoustic = b and nbumps3 > 1.5 | 0 | 0.102112 |
| nbumps2 <= 0.5 and shift != W and gpuls <= 252.5 | 0 | 0.025266 |
| nbumps4 > 0.5 and nbumps2 <= 0.5 and seismoacoustic != b | 0 | 0.082661 |
| seismoacoustic = b and nbumps <= 4.5 and nbumps4 > 0.5 and nbumps2 > 0.5 | 0 | 0.060377 |
| seismoacoustic = b and nbumps <= 4.5 and nbumps4 <= 0.5 and seismic = a and nbumps3 <= 0.5 and gdenergy <= -1.0 | 0 | 0.045920 |
| seismoacoustic = b and nbumps <= 4.5 and nbumps4 <= 0.5 and nbumps2 > 1.5 and nbumps3 <= 0.5 and energy <= 1150.0 | 0 | 0.054702 |
| seismoacoustic = b and nbumps <= 4.5 and nbumps4 <= 0.5 and seismic = a and ghazard = a and maxenergy <= 2500.0 and energy <= 1850.0 | 0 | 0.046327 |
| nbumps4 > 0.5 and nbumps2 > 0.5 and seismoacoustic != b and nbumps2 > 1.5 | 0 | 0.077160 |
| seismoacoustic = b and nbumps <= 4.5 and nbumps4 <= 0.5 and shift = W and ghazard != a and nbumps3 <= 0.5 | 0 | 0.054167 |
| nbumps2 <= 0.5 and nbumps4 <= 0.5 and shift = W and seismoacoustic != a and gpuls > 1172.0 | 0 | 0.045920 |
| nbumps2 <= 0.5 and seismoacoustic != a | 0 | 0.113174 |
| seismic = a and ghazard = a and maxenergy <= 5500.0 and gdenergy > -30.5 and nbumps2 > 1.5 | 0 | 0.064879 |
| shift != W | 0 | 0.053333 |
| ghazard = a and nbumps4 > 0.5 and seismoacoustic != b | 0 | 0.053030 |
| ghazard = a and gpuls > 184.0 and nbumps3 <= 0.5 | 0 | 0.020891 |
| ghazard != a | 0 | 0.032925 |
| gpuls > 184.0 and nbumps4 <= 0.5 and seismoacoustic = b and nbumps2 <= 1.5 and maxenergy <= 3500.0 | 0 | 0.024714 |
| gpuls > 184.0 and nbumps4 <= 0.5 and seismic = a | 1 | 0.494777 |
| gpuls > 234.5 and gdpuls > 20.5 and nbumps <= 4.5 | 0 | 0.066984 |
| gpuls > 234.5 and nbumps4 <= 0.5 and nbumps3 <= 1.5 | 1 | 0.480516 |
| gdenergy > -30.5 and nbumps4 <= 0.5 | 1 | 0.215282 |
| nbumps4 > 0.5 | 0 | 0.164300 |
|  | 0 | 0.540984 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| nbumps >= 2 and gpuls >= 744 and gdenergy <= -30 | 1 | 0.004290 |
| nbumps >= 2 and seismic = b and gdenergy >= -14 and gdpuls <= 17 | 1 | 0.004451 |
|  | 0 | 0.951754 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

gpuls|nbumps2|nbumps7|energy|class
---|---|---|---|---
(1139.5-inf)|(0.5-inf)|all|(650-inf)|0
(-inf-1139.5]|(0.5-inf)|all|(650-inf)|0
(1139.5-inf)|(-inf-0.5]|all|(650-inf)|0
(-inf-1139.5]|(-inf-0.5]|all|(650-inf)|0
(1139.5-inf)|(0.5-inf)|all|(-inf-650]|0
(-inf-1139.5]|(0.5-inf)|all|(-inf-650]|0
(1139.5-inf)|(-inf-0.5]|all|(-inf-650]|0
(-inf-1139.5]|(-inf-0.5]|all|(-inf-650]|0

## JRip

Decision list:

rules | predicted class
---|---
(nbumps >= 2) and (gpuls >= 744) and (gdenergy <= -30)|1 (31.0/14.0)
(nbumps >= 2) and (seismic = b) and (gdenergy >= -14) and (gdpuls <= 17)|1 (55.0/32.0)
|0 (2234.0/110.0)


## PART

Decision list:

rules | predicted class
---|---
nbumps <= 1.5 AND gpuls <= 1342.5 AND seismoacoustic != c AND shift != W AND nbumps <= 0.5 AND seismic = a AND seismoacoustic = a|0 (369.0/4.0)
nbumps <= 1.5 AND gpuls <= 1342.5 AND seismoacoustic != c AND shift != W AND nbumps <= 0.5 AND seismic = a|0 (146.0/1.0)
nbumps <= 1.5 AND gpuls <= 1342.5 AND seismoacoustic != c AND nbumps4 <= 0.5 AND shift != W AND nbumps <= 0.5|0 (105.0)
nbumps <= 1.5 AND gpuls <= 1342.5 AND seismoacoustic = c|0 (35.0)
nbumps <= 1.5 AND gpuls <= 1342.5 AND nbumps4 <= 0.5 AND seismic = a AND ghazard != a AND nbumps <= 0.5|0 (35.0/1.0)
nbumps <= 1.5 AND gpuls <= 1342.5 AND nbumps4 <= 0.5 AND seismic = a AND ghazard = a AND shift != W AND nbumps3 > 0.5 AND seismoacoustic = a AND energy <= 4500.0|0 (48.0)
nbumps <= 1.5 AND gpuls <= 1342.5 AND shift = W AND nbumps4 <= 0.5 AND seismic = a AND seismoacoustic = a AND nbumps2 <= 0.5 AND nbumps <= 0.5|0 (198.0/5.0)
nbumps <= 1.5 AND gpuls <= 1342.5 AND nbumps2 > 0.5 AND ghazard = a AND seismoacoustic != a AND shift = W|0 (46.0)
nbumps <= 1.5 AND gpuls <= 1252.5 AND nbumps3 > 0.5 AND energy > 1500.0 AND ghazard = a AND shift = W AND seismic = a|0 (60.0)
nbumps <= 1.5 AND nbumps3 <= 0.5 AND shift = W AND nbumps4 <= 0.5 AND genergy <= 18755.0 AND seismoacoustic = a|0 (86.0)
nbumps <= 1.5 AND nbumps3 <= 0.5 AND nbumps4 > 0.5 AND gdpuls > -24.0|0 (34.0)
gpuls <= 1139.5 AND nbumps <= 1.5 AND seismoacoustic != a AND nbumps3 > 0.5 AND seismic = a|0 (35.0/2.0)
nbumps <= 1.5 AND nbumps3 <= 0.5 AND ghazard != a AND genergy > 21310.0|0 (47.0)
gpuls <= 1137.5 AND ghazard != b AND nbumps <= 2.5 AND nbumps3 <= 0.5 AND maxenergy <= 650.0 AND nbumps2 > 0.5 AND shift != W AND seismoacoustic = a|0 (29.0)
gpuls <= 1137.5 AND ghazard != b AND nbumps <= 2.5 AND nbumps <= 0.5 AND seismoacoustic != a AND seismic = a|0 (120.0/6.0)
gpuls <= 1137.5 AND ghazard != b AND nbumps <= 2.5 AND seismic != a AND nbumps2 <= 0.5 AND seismoacoustic != a AND nbumps <= 0.5|0 (83.0/4.0)
nbumps3 <= 3.5 AND ghazard != b AND gpuls <= 1137.5 AND seismoacoustic = a AND nbumps <= 4.5 AND seismic != a AND gdpuls > -51.5 AND nbumps4 <= 0.5|0 (201.0/14.0)
nbumps3 <= 3.5 AND seismic = a AND ghazard != b AND gdenergy > -27.0 AND shift != W AND seismoacoustic != a|0 (17.0)
nbumps3 <= 3.5 AND seismic = a AND ghazard != b AND seismoacoustic = a AND nbumps <= 4.5 AND shift = W|0 (193.0/23.0)
nbumps3 <= 3.5 AND seismic = a AND ghazard != b AND seismoacoustic = a AND genergy > 14350.0 AND shift = W|0 (18.0)
nbumps2 <= 0.5 AND seismoacoustic = b AND nbumps3 > 0.5 AND seismic != a AND nbumps <= 1.5 AND energy <= 3500.0|0 (19.0)
seismic = a AND nbumps3 <= 2.5 AND ghazard != b AND seismoacoustic = a AND nbumps2 <= 0.5 AND energy <= 5500.0|0 (15.0/2.0)
seismic = a AND nbumps3 <= 2.5 AND ghazard != b AND seismoacoustic = b AND nbumps3 > 1.5|0 (19.0/1.0)
nbumps2 <= 0.5 AND shift != W AND gpuls <= 252.5|0 (10.0/2.0)
nbumps4 > 0.5 AND nbumps2 <= 0.5 AND seismoacoustic != b|0 (18.0/2.0)
seismoacoustic = b AND nbumps <= 4.5 AND nbumps4 > 0.5 AND nbumps2 > 0.5|0 (15.0/3.0)
seismoacoustic = b AND nbumps <= 4.5 AND nbumps4 <= 0.5 AND seismic = a AND nbumps3 <= 0.5 AND gdenergy <= -1.0|0 (15.0/4.0)
seismoacoustic = b AND nbumps <= 4.5 AND nbumps4 <= 0.5 AND nbumps2 > 1.5 AND nbumps3 <= 0.5 AND energy <= 1150.0|0 (12.0/1.0)
seismoacoustic = b AND nbumps <= 4.5 AND nbumps4 <= 0.5 AND seismic = a AND ghazard = a AND maxenergy <= 2500.0 AND energy <= 1850.0|0 (13.0)
nbumps4 > 0.5 AND nbumps2 > 0.5 AND seismoacoustic != b AND nbumps2 > 1.5|0 (18.0/3.0)
seismoacoustic = b AND nbumps <= 4.5 AND nbumps4 <= 0.5 AND shift = W AND ghazard != a AND nbumps3 <= 0.5|0 (17.0/4.0)
nbumps2 <= 0.5 AND nbumps4 <= 0.5 AND shift = W AND seismoacoustic != a AND gpuls > 1172.0|0 (17.0/6.0)
nbumps2 <= 0.5 AND seismoacoustic != a|0 (32.0)
seismic = a AND ghazard = a AND maxenergy <= 5500.0 AND gdenergy > -30.5 AND nbumps2 > 1.5|0 (16.0/2.0)
shift != W|0 (22.0/6.0)
ghazard = a AND nbumps4 > 0.5 AND seismoacoustic != b|0 (19.0/5.0)
ghazard = a AND gpuls > 184.0 AND nbumps3 <= 0.5|0 (15.0/3.0)
ghazard != a|0 (15.0/4.0)
gpuls > 184.0 AND nbumps4 <= 0.5 AND seismoacoustic = b AND nbumps2 <= 1.5 AND maxenergy <= 3500.0|0 (14.0/3.0)
gpuls > 184.0 AND nbumps4 <= 0.5 AND seismic = a|1 (18.0/8.0)
gpuls > 234.5 AND gdpuls > 20.5 AND nbumps <= 4.5|0 (13.0/2.0)
gpuls > 234.5 AND nbumps4 <= 0.5 AND nbumps3 <= 1.5|1 (19.0/6.0)
gdenergy > -30.5 AND nbumps4 <= 0.5|1 (19.0/9.0)
nbumps4 > 0.5|0 (13.0/4.0)
|0 (12.0)


## J48 Decision Tree

* nbumps <= 1.0: 0 (1848.0/63.0)
* nbumps > 1.0
	* nbumps3 <= 3.0
		* gpuls <= 740.0: 0 (256.0/29.0)
		* gpuls > 740.0
			* gdenergy <= -30.0
				* nbumps2 <= 0.0: 0 (12.0/3.0)
				* nbumps2 > 0.0: 1 (17.0/5.0)
			* gdenergy > -30.0
				* maxenergy <= 40000.0
					* gdpuls <= -24.0: 0 (11.0)
					* gdpuls > -24.0
						* genergy <= 50580.0: 0 (7.0)
						* genergy > 50580.0
							* gdpuls <= -20.0: 1 (7.0/3.0)
							* gdpuls > -20.0
								* gdenergy <= -15.0: 0 (10.0)
								* gdenergy > -15.0
									* gdenergy <= -5.0
										* genergy <= 514800.0: 1 (7.0/2.0)
										* genergy > 514800.0: 0 (7.0/3.0)
									* gdenergy > -5.0
										* gdpuls <= 5.0: 0 (16.0)
										* gdpuls > 5.0
											* maxenergy <= 900.0: 0 (10.0)
											* maxenergy > 900.0
												* nbumps2 <= 0.0: 0 (15.0/1.0)
												* nbumps2 > 0.0
													* genergy <= 1034700.0
														* genergy <= 532290.0
															* gpuls <= 1777.0
																* energy <= 4400.0: 1 (9.0/3.0)
																* energy > 4400.0: 0 (15.0/3.0)
															* gpuls > 1777.0: 0 (9.0/1.0)
														* genergy > 532290.0
															* gdenergy <= 26.0: 0 (7.0/3.0)
															* gdenergy > 26.0: 1 (7.0/1.0)
													* genergy > 1034700.0: 0 (11.0/1.0)
				* maxenergy > 40000.0: 0 (13.0)
	* nbumps3 > 3.0
		* gpuls <= 364.0: 0 (7.0)
		* gpuls > 364.0
			* genergy <= 69070.0: 1 (8.0/2.0)
			* genergy > 69070.0: 0 (11.0/4.0)


## SimpleCart Decision Tree

* nbumps < 1.5
	* gpuls < 1342.5
		* genergy < 16880.0
			* energy < 650.0
				* gdenergy < -84.5: 0(25.0/1.0)
				* gdenergy >= -84.5
					* gpuls < 219.0: 0(405.0/4.0)
					* gpuls >= 219.0: 0(281.0/0.0)
			* energy >= 650.0: 0(73.0/5.0)
		* genergy >= 16880.0: 0(937.0/39.0)
	* gpuls >= 1342.5
		* nbumps3 < 0.5: 0(55.0/6.0)
		* nbumps3 >= 0.5: 0(9.0/8.0)
* nbumps >= 1.5
	* gpuls < 884.0
		* nbumps3 < 3.5: 0(249.0/34.0)
		* nbumps3 >= 3.5
			* gpuls < 364.0: 0(7.0/0.0)
			* gpuls >= 364.0: 1(6.0/4.0)
	* gpuls >= 884.0
		* gdenergy < -29.5
			* nbumps2 < 0.5
				* genergy < 438160.0: 1(3.0/3.0)
				* genergy >= 438160.0: 0(6.0/0.0)
			* nbumps2 >= 0.5: 1(12.0/4.0)
		* gdenergy >= -29.5
			* gpuls < 2211.5
				* energy < 28650.0
					* energy < 21000.0
						* maxenergy < 6500.0: 0(53.0/15.0)
						* maxenergy >= 6500.0: 0(14.0/0.0)
					* energy >= 21000.0: 1(5.0/1.0)
				* energy >= 28650.0
					* gpuls < 1748.5: 0(18.0/0.0)
					* gpuls >= 1748.5: 0(8.0/1.0)
			* gpuls >= 2211.5
				* genergy < 289800.0: 0(6.0/0.0)
				* genergy >= 289800.0
					* genergy < 1124825.0: 1(11.0/6.0)
					* genergy >= 1124825.0: 0(6.0/0.0)


