# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 0 | 0.935345 |
| nbumps > 1.5 and ghazard != c and seismoacoustic != c and nbumps2 > 0.5 and seismic != a and seismoacoustic = a and genergy > 189465.0 and gpuls > 1560.5 and nbumps <= 3.5 | 1 | 0.001880 |
| nbumps > 1.5 and ghazard != c and seismoacoustic = c | 1 | 0.000593 |
| nbumps > 1.5 and ghazard != c and seismoacoustic != c and nbumps2 > 0.5 and seismic != a and seismoacoustic = a and genergy > 189465.0 and gpuls <= 1560.5 | 1 | 0.002815 |
| nbumps <= 1.5 and gpuls > 1207.0 and nbumps3 > 0.5 and seismic != a | 1 | 0.002266 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| nbumps <= 1.5 and gpuls <= 1210.0 | 0 | 0.917540 |
| genergy <= 1048490.0 and gpuls <= 744.0 and genergy <= 108930.0 and gpuls > 98.5 and energy > 900.0 and genergy > 21025.0 and genergy > 31145.0 and gdpuls > 19.5 | 0 | 0.289391 |
| genergy <= 1133675.0 and maxenergy <= 1500.0 and genergy <= 625370.0 and gpuls <= 1752.0 | 0 | 0.341414 |
| genergy > 1133675.0 | 0 | 0.138752 |
| energy > 40500.0 and energy <= 70700.0 | 0 | 0.123061 |
| gdpuls > -68.5 and energy > 850.0 and energy > 2450.0 and energy > 3150.0 and gdpuls > -51.5 and genergy > 31145.0 and genergy > 40250.0 and gpuls > 687.0 and gdenergy > -29.5 and gdenergy > -16.5 and energy <= 71650.0 and gpuls > 770.0 and gpuls > 835.5 and gpuls <= 3011.0 and energy > 3650.0 | 0 | 0.192697 |
| gdpuls > -69.5 and gdenergy <= 108.5 and gdpuls > -55.0 and gpuls <= 665.0 and genergy <= 62570.0 and gdpuls <= -1.0 and seismoacoustic = a | 0 | 0.209843 |
| gdpuls > -69.5 and gdenergy <= 108.5 and energy > 850.0 and gdenergy > -48.0 and energy <= 16500.0 and seismic = a and gdpuls <= 71.0 and gpuls <= 1328.5 and energy <= 9600.0 | 0 | 0.166193 |
| gdpuls > -69.5 and gdenergy <= 108.5 and energy > 850.0 and energy > 13000.0 and gdenergy > -46.0 and genergy <= 585400.0 and nbumps2 <= 1.5 and nbumps <= 3.5 | 0 | 0.109375 |
| gdpuls > -69.5 and gdenergy <= 108.5 and energy > 850.0 and shift = W and nbumps3 > 0.5 and gpuls <= 1936.0 and energy <= 31350.0 and gpuls <= 1417.0 and energy > 3400.0 | 1 | 0.244455 |
| gdpuls > -69.5 and shift = W and gdenergy > -29.5 and gpuls <= 2904.5 and gpuls > 442.5 and energy > 3250.0 | 0 | 0.114950 |
| gdpuls > -69.5 and energy > 850.0 and shift = W and genergy <= 817385.0 and genergy <= 693510.0 and nbumps3 > 0.5 and genergy > 213640.0 | 1 | 0.146850 |
| energy <= 30700.0 and shift = W and gdenergy <= -36.5 | 0 | 0.160133 |
| gdenergy > -24.5 and energy <= 850.0 | 0 | 0.110693 |
| gdenergy <= -24.0 | 1 | 0.502759 |
| genergy <= 815830.0 and genergy <= 653045.0 and genergy <= 278380.0 and genergy <= 77165.0 and gpuls <= 540.5 | 1 | 0.479433 |
| genergy <= 815830.0 and seismoacoustic = a and genergy <= 278380.0 | 0 | 0.071637 |
| genergy <= 815830.0 | 0 | 0.213333 |
|  | 1 | 0.953488 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| nbumps >= 2 and gpuls >= 744 and gdenergy <= -30 | 1 | 0.004158 |
|  | 0 | 0.942249 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

gpuls|gdenergy|gdpuls|nbumps|nbumps2|nbumps5|nbumps6|class
---|---|---|---|---|---|---|---
(-inf-54.5]|all|all|(1.5-inf)|(0.5-inf)|all|all|0
(1142.5-inf)|all|all|(1.5-inf)|(0.5-inf)|all|all|0
(54.5-1142.5]|all|all|(1.5-inf)|(0.5-inf)|all|all|0
(-inf-54.5]|all|all|(-inf-1.5]|(0.5-inf)|all|all|0
(1142.5-inf)|all|all|(-inf-1.5]|(0.5-inf)|all|all|0
(54.5-1142.5]|all|all|(-inf-1.5]|(0.5-inf)|all|all|0
(54.5-1142.5]|all|all|(1.5-inf)|(-inf-0.5]|all|all|0
(1142.5-inf)|all|all|(1.5-inf)|(-inf-0.5]|all|all|0
(-inf-54.5]|all|all|(-inf-1.5]|(-inf-0.5]|all|all|0
(1142.5-inf)|all|all|(-inf-1.5]|(-inf-0.5]|all|all|0
(54.5-1142.5]|all|all|(-inf-1.5]|(-inf-0.5]|all|all|0

## JRip

Decision list:

rules | predicted class
---|---
(nbumps >= 2) and (gpuls >= 744) and (gdenergy <= -30)|1 (32.0/15.0)
|0 (2288.0/133.0)


## PART

Decision list:

rules | predicted class
---|---
nbumps <= 1.5 AND gpuls <= 1210.0|0 (1460.0/39.0)
genergy <= 1048490.0 AND gpuls <= 744.0 AND genergy <= 108930.0 AND gpuls > 98.5 AND energy > 900.0 AND genergy > 21025.0 AND genergy > 31145.0 AND gdpuls > 19.5|0 (60.0/2.0)
genergy <= 1133675.0 AND maxenergy <= 1500.0 AND genergy <= 625370.0 AND gpuls <= 1752.0|0 (97.0/12.0)
genergy > 1133675.0|0 (23.0)
energy > 40500.0 AND energy <= 70700.0|0 (20.0)
gdpuls > -68.5 AND energy > 850.0 AND energy > 2450.0 AND energy > 3150.0 AND gdpuls > -51.5 AND genergy > 31145.0 AND genergy > 40250.0 AND gpuls > 687.0 AND gdenergy > -29.5 AND gdenergy > -16.5 AND energy <= 71650.0 AND gpuls > 770.0 AND gpuls > 835.5 AND gpuls <= 3011.0 AND energy > 3650.0|0 (55.0/17.0)
gdpuls > -69.5 AND gdenergy <= 108.5 AND gdpuls > -55.0 AND gpuls <= 665.0 AND genergy <= 62570.0 AND gdpuls <= -1.0 AND seismoacoustic = a|0 (44.0/2.0)
gdpuls > -69.5 AND gdenergy <= 108.5 AND energy > 850.0 AND gdenergy > -48.0 AND energy <= 16500.0 AND seismic = a AND gdpuls <= 71.0 AND gpuls <= 1328.5 AND energy <= 9600.0|0 (38.0/3.0)
gdpuls > -69.5 AND gdenergy <= 108.5 AND energy > 850.0 AND energy > 13000.0 AND gdenergy > -46.0 AND genergy <= 585400.0 AND nbumps2 <= 1.5 AND nbumps <= 3.5|0 (16.0)
gdpuls > -69.5 AND gdenergy <= 108.5 AND energy > 850.0 AND shift = W AND nbumps3 > 0.5 AND gpuls <= 1936.0 AND energy <= 31350.0 AND gpuls <= 1417.0 AND energy > 3400.0|1 (34.0/12.0)
gdpuls > -69.5 AND shift = W AND gdenergy > -29.5 AND gpuls <= 2904.5 AND gpuls > 442.5 AND energy > 3250.0|0 (17.0)
gdpuls > -69.5 AND energy > 850.0 AND shift = W AND genergy <= 817385.0 AND genergy <= 693510.0 AND nbumps3 > 0.5 AND genergy > 213640.0|1 (16.0/4.0)
energy <= 30700.0 AND shift = W AND gdenergy <= -36.5|0 (15.0)
gdenergy > -24.5 AND energy <= 850.0|0 (15.0/1.0)
gdenergy <= -24.0|1 (5.0)
genergy <= 815830.0 AND genergy <= 653045.0 AND genergy <= 278380.0 AND genergy <= 77165.0 AND gpuls <= 540.5|1 (4.0/1.0)
genergy <= 815830.0 AND seismoacoustic = a AND genergy <= 278380.0|0 (4.0/1.0)
genergy <= 815830.0|0 (8.0/3.0)
|1 (3.0)


## J48 Decision Tree

* nbumps <= 1.5
	* gpuls <= 1207.0: 0 (1382.0/36.0)
	* gpuls > 1207.0
		* nbumps3 <= 0.5: 0 (62.0/6.0)
		* nbumps3 > 0.5
			* seismic = a: 0 (9.0/1.0)
			* seismic != a: 1 (12.0/5.0)
* nbumps > 1.5
	* ghazard = c: 0 (3.0)
	* ghazard != c
		* seismoacoustic = c: 1 (6.0/3.0)
		* seismoacoustic != c
			* nbumps2 <= 0.5: 0 (65.0/6.0)
			* nbumps2 > 0.5
				* seismic = a: 0 (174.0/26.0)
				* seismic != a
					* seismoacoustic = a
						* genergy <= 189465.0: 0 (60.0/7.0)
						* genergy > 189465.0
							* gpuls <= 1560.5: 1 (7.0/1.0)
							* gpuls > 1560.5
								* nbumps <= 3.5: 1 (10.0/5.0)
								* nbumps > 3.5: 0 (9.0/1.0)
					* seismoacoustic != a: 0 (57.0/16.0)


## SimpleCart Decision Tree

* : 0(2170.0/150.0)


