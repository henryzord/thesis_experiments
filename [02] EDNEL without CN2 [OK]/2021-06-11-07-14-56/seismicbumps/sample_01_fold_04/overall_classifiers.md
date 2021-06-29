# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| gpuls <= 1252.0 and nbumps <= 1.0 | 0 | 0.918092 |
| gpuls <= 1253.5 and nbumps > 1.5 and nbumps3 > 0.5 | 0 | 0.574600 |
| gpuls > 1253.5 and nbumps > 1.5 and nbumps3 > 0.5 | 0 | 0.269356 |
| gpuls <= 1253.5 and nbumps > 1.5 and nbumps3 <= 0.5 | 0 | 0.264301 |
| gpuls > 1252.0 and gdenergy > -30.0 and gdenergy > -17.0 and gdenergy <= 180.0 and genergy <= 1138340.0 and gpuls <= 2205.0 and energy <= 35900.0 and nbumps3 <= 0.0 | 0 | 0.201790 |
| gpuls > 1252.0 and gdenergy > -30.0 and gdenergy > -17.0 and gdenergy <= 180.0 and genergy <= 1138340.0 and gpuls <= 2205.0 and energy <= 35900.0 and nbumps3 > 0.0 and seismic != a | 1 | 0.003272 |
| gpuls > 1252.0 and gdenergy <= -30.0 and nbumps2 > 0.0 | 1 | 0.002815 |
| gpuls <= 1252.0 and nbumps > 1.0 and gpuls > 740.0 and gdpuls <= 95.0 and energy > 1100.0 and gpuls <= 774.0 | 1 | 0.001507 |
| gpuls > 1253.5 and nbumps > 0.5 and nbumps <= 1.5 and nbumps3 <= 0.5 | 0 | 0.138752 |
| gpuls > 1252.0 and gdenergy > -30.0 and gdenergy > -17.0 and gdenergy <= 180.0 and genergy <= 1138340.0 and gpuls > 2205.0 and genergy > 289580.0 and gdenergy > 46.0 | 1 | 0.002365 |
| gpuls <= 1252.0 and nbumps > 1.0 and gpuls <= 740.0 and nbumps3 <= 3.0 and genergy <= 81480.0 and gpuls > 98.0 and energy > 900.0 and shift = W and genergy <= 55570.0 and gdenergy <= 6.0 and gdpuls > 1.0 and gdpuls <= 10.0 | 1 | 0.001439 |
| gpuls <= 1252.0 and nbumps > 1.0 and gpuls > 740.0 and gdpuls <= 95.0 and energy > 1100.0 and gpuls > 774.0 and genergy <= 250030.0 and genergy > 121870.0 | 1 | 0.001279 |
| gpuls > 1252.0 and gdenergy > -30.0 and gdenergy > -17.0 and gdenergy <= 180.0 and genergy <= 1138340.0 and gpuls > 2205.0 and genergy > 289580.0 and gdenergy <= 46.0 and genergy <= 698810.0 | 1 | 0.001644 |
| gpuls <= 1252.0 and nbumps > 1.0 and gpuls <= 740.0 and nbumps3 > 3.0 and energy > 13500.0 | 1 | 0.001053 |
| gpuls <= 1252.0 and nbumps > 1.0 and gpuls <= 740.0 and nbumps3 <= 3.0 and genergy <= 81480.0 and gpuls > 98.0 and energy > 900.0 and shift = W and genergy <= 55570.0 and gdenergy <= 6.0 and gdpuls <= 1.0 and seismoacoustic != a and gpuls <= 304.0 and gpuls > 205.0 | 1 | 0.001053 |
| gpuls > 1253.5 and nbumps <= 0.5 and nbumps3 <= 0.5 | 0 | 0.178022 |
| gpuls > 1253.5 and nbumps > 0.5 and nbumps <= 1.5 and nbumps3 > 0.5 | 1 | 0.002425 |
| gpuls > 1253.5 and nbumps > 1.5 and nbumps3 <= 0.5 | 0 | 0.088183 |
| gpuls > 1252.0 and gdenergy > -30.0 and gdenergy <= -17.0 | 0 | 0.132948 |
| gpuls > 1252.0 and gdenergy > -30.0 and gdenergy > -17.0 and gdenergy <= 180.0 and genergy > 1138340.0 | 0 | 0.128801 |
| gpuls > 1252.0 and gdenergy > -30.0 and gdenergy > -17.0 and gdenergy <= 180.0 and genergy <= 1138340.0 and gpuls <= 2205.0 and energy <= 35900.0 and nbumps3 > 0.0 and seismic = a | 0 | 0.093506 |
| gpuls > 1252.0 and gdenergy <= -30.0 and nbumps2 <= 0.0 | 0 | 0.051282 |

## Ordered rules

### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| nbumps >= 2 and gpuls >= 744 and gdenergy <= -30 and gdenergy >= -32 | 1 | 0.002299 |
| gpuls >= 751 and nbumps >= 3 and gpuls <= 886 and nbumps2 >= 2 | 1 | 0.001840 |
| nbumps >= 2 and genergy >= 306400 and nbumps2 >= 1 and energy >= 5800 and energy <= 9700 and genergy <= 1132810 and nbumps3 <= 2 | 1 | 0.003673 |
| nbumps >= 2 and gdpuls <= 10 and genergy <= 59840 and gdpuls >= 5 and gdenergy <= 6 | 1 | 0.003673 |
| nbumps >= 2 and gpuls >= 979 and nbumps2 >= 1 and energy >= 21300 and energy <= 31000 and gdpuls <= -9 | 1 | 0.001840 |
|  | 0 | 0.947185 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

gpuls|nbumps|nbumps3|class
---|---|---|---
(1253.5-inf)|(1.5-inf)|(0.5-inf)|0
(-inf-1253.5]|(1.5-inf)|(0.5-inf)|0
(1253.5-inf)|(0.5-1.5]|(0.5-inf)|1
(-inf-1253.5]|(0.5-1.5]|(0.5-inf)|0
(1253.5-inf)|(1.5-inf)|(-inf-0.5]|0
(-inf-1253.5]|(1.5-inf)|(-inf-0.5]|0
(1253.5-inf)|(0.5-1.5]|(-inf-0.5]|0
(-inf-1253.5]|(0.5-1.5]|(-inf-0.5]|0
(1253.5-inf)|(-inf-0.5]|(-inf-0.5]|0
(-inf-1253.5]|(-inf-0.5]|(-inf-0.5]|0

## JRip

Decision list:

rules | predicted class
---|---
(nbumps >= 2) and (gpuls >= 744) and (gdenergy <= -30) and (gdenergy >= -32)|1 (5.0/0.0)
(gpuls >= 751) and (nbumps >= 3) and (gpuls <= 886) and (nbumps2 >= 2)|1 (4.0/0.0)
(nbumps >= 2) and (genergy >= 306400) and (nbumps2 >= 1) and (energy >= 5800) and (energy <= 9700) and (genergy <= 1132810) and (nbumps3 <= 2)|1 (8.0/0.0)
(nbumps >= 2) and (gdpuls <= 10) and (genergy <= 59840) and (gdpuls >= 5) and (gdenergy <= 6)|1 (8.0/0.0)
(nbumps >= 2) and (gpuls >= 979) and (nbumps2 >= 1) and (energy >= 21300) and (energy <= 31000) and (gdpuls <= -9)|1 (4.0/0.0)
|0 (2291.0/121.0)


## J48 Decision Tree

* gpuls <= 1252.0
	* nbumps <= 1.0: 0 (1760.0/47.0)
	* nbumps > 1.0
		* gpuls <= 740.0
			* nbumps3 <= 3.0
				* genergy <= 81480.0
					* gpuls <= 98.0: 0 (15.0)
					* gpuls > 98.0
						* energy <= 900.0: 0 (11.0/4.0)
						* energy > 900.0
							* shift = W
								* genergy <= 55570.0
									* gdenergy <= 6.0
										* gdpuls <= 1.0
											* seismoacoustic = a: 0 (61.0/2.0)
											* seismoacoustic != a
												* gpuls <= 304.0
													* gpuls <= 205.0: 0 (7.0/1.0)
													* gpuls > 205.0: 1 (7.0/3.0)
												* gpuls > 304.0: 0 (10.0/1.0)
										* gdpuls > 1.0
											* gdpuls <= 10.0: 1 (8.0/3.0)
											* gdpuls > 10.0: 0 (9.0/1.0)
									* gdenergy > 6.0: 0 (52.0)
								* genergy > 55570.0: 0 (30.0/8.0)
							* shift != W: 0 (8.0/3.0)
				* genergy > 81480.0: 0 (33.0)
			* nbumps3 > 3.0
				* energy <= 13500.0: 0 (7.0/1.0)
				* energy > 13500.0: 1 (7.0/3.0)
		* gpuls > 740.0
			* gdpuls <= 95.0
				* energy <= 1100.0: 0 (7.0)
				* energy > 1100.0
					* gpuls <= 774.0: 1 (11.0/5.0)
					* gpuls > 774.0
						* genergy <= 250030.0
							* genergy <= 121870.0: 0 (38.0/9.0)
							* genergy > 121870.0: 1 (9.0/4.0)
						* genergy > 250030.0: 0 (9.0)
			* gdpuls > 95.0: 0 (7.0)
* gpuls > 1252.0
	* gdenergy <= -30.0
		* nbumps2 <= 0.0: 0 (18.0/6.0)
		* nbumps2 > 0.0: 1 (8.0/1.0)
	* gdenergy > -30.0
		* gdenergy <= -17.0: 0 (23.0)
		* gdenergy > -17.0
			* gdenergy <= 180.0
				* genergy <= 1138340.0
					* gpuls <= 2205.0
						* energy <= 35900.0
							* nbumps3 <= 0.0: 0 (49.0/6.0)
							* nbumps3 > 0.0
								* seismic = a: 0 (21.0/3.0)
								* seismic != a: 1 (17.0/6.0)
						* energy > 35900.0: 0 (12.0)
					* gpuls > 2205.0
						* genergy <= 289580.0: 0 (9.0/1.0)
						* genergy > 289580.0
							* gdenergy <= 46.0
								* genergy <= 698810.0: 1 (7.0/2.0)
								* genergy > 698810.0: 0 (7.0/2.0)
							* gdenergy > 46.0: 1 (7.0/1.0)
				* genergy > 1138340.0: 0 (26.0/2.0)
			* gdenergy > 180.0: 0 (10.0)


## SimpleCart Decision Tree

* : 0(2170.0/150.0)


