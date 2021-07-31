# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| nbumps < 1.5 and gpuls < 1342.5 and genergy >= 16885.0 | 0 | 0.860146 |
| nbumps < 1.5 and gpuls < 1342.5 and genergy < 16885.0 and energy < 650.0 and gdenergy >= -84.5 and gpuls < 219.0 | 0 | 0.725347 |
| nbumps < 1.5 and gpuls < 1342.5 and genergy < 16885.0 and energy < 650.0 and gdenergy >= -84.5 and gpuls >= 219.0 | 0 | 0.655172 |
| nbumps >= 1.5 and gpuls < 677.0 and seismoacoustic = a | 0 | 0.461747 |
| nbumps < 1.5 and gpuls < 1342.5 and genergy < 16885.0 and energy >= 650.0 | 0 | 0.309739 |
| nbumps >= 1.5 and gpuls >= 677.0 and gdpuls >= 36.0 | 0 | 0.276160 |
| nbumps < 1.5 and gpuls >= 1342.5 and nbumps3 < 0.5 | 0 | 0.252083 |
| nbumps >= 1.5 and gpuls >= 677.0 and gdpuls < 36.0 and nbumps2 >= 0.5 | 0 | 0.227240 |
| nbumps >= 1.5 and gpuls < 677.0 and seismoacoustic != d and genergy >= 39510.0 and gdenergy < 67.5 | 0 | 0.379530 |
| nbumps >= 1.5 and gpuls >= 677.0 and gdpuls < 36.0 and nbumps2 < 0.5 | 0 | 0.149325 |
| nbumps < 1.5 and gpuls < 1342.5 and genergy < 16885.0 and energy < 650.0 and gdenergy < -84.5 | 0 | 0.138152 |
| nbumps >= 1.5 and gpuls < 677.0 and seismoacoustic != d and genergy < 39510.0 and nbumps3 >= 1.5 | 1 | 0.001406 |
| nbumps < 1.5 and gpuls >= 1342.5 and nbumps3 >= 0.5 | 1 | 0.002304 |
| nbumps >= 1.5 and gpuls < 677.0 and seismoacoustic != d and genergy < 39510.0 and nbumps3 < 1.5 | 0 | 0.293878 |
| nbumps >= 1.5 and gpuls < 677.0 and seismoacoustic != d and genergy >= 39510.0 and gdenergy >= 67.5 | 0 | 0.078045 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| nbumps <= 1 and gpuls <= 1333 and gpuls > 32 and energy <= 15000 and energy <= 7500 and energy <= 5500 and gdenergy <= 104 | 0 | 0.899375 |
| gpuls > 98 and gdenergy > 128 | 0 | 0.502177 |
| gpuls <= 98 | 0 | 0.501995 |
| nbumps2 <= 0 and gdenergy <= 118 and energy <= 16000 and nbumps <= 2 and gpuls <= 1405 | 0 | 0.309166 |
| energy <= 40600 and nbumps3 <= 0 and maxenergy <= 800 and gpuls > 282 and gdenergy > -27 and genergy > 37710 and gdpuls > -3 | 0 | 0.247480 |
| energy <= 36500 and gpuls <= 669 and gpuls <= 625 and genergy > 21070 | 0 | 0.399948 |
| energy > 36500 | 0 | 0.278696 |
| genergy > 1134540 | 0 | 0.075617 |
| maxenergy > 7000 and nbumps <= 1 | 0 | 0.064286 |
| gdenergy <= 112 and gdpuls > 36 and energy > 9400 | 0 | 0.064879 |
| energy <= 6000 and nbumps3 <= 1 and energy <= 5600 and genergy <= 19240 | 0 | 0.050000 |
| gpuls > 261 and gpuls > 669 and gpuls <= 2457 and maxenergy <= 4000 and energy > 4600 | 0 | 0.086721 |
| gdenergy > -54 and gpuls > 261 and gpuls > 669 and gpuls <= 2597 and genergy > 207930 and gdpuls <= 36 and gpuls <= 2205 and nbumps <= 3 and gdenergy <= -14 | 0 | 0.077885 |
| maxenergy <= 1000 and maxenergy > 800 | 0 | 0.060096 |
| gpuls <= 2597 and gdenergy <= -43 | 1 | 0.306715 |
| gpuls <= 2597 and gdpuls <= -24 | 0 | 0.041727 |
| gpuls <= 2597 and gdpuls > -20 and genergy <= 788650 and gdenergy > -18 and gdenergy <= 12 and gdpuls > -1 | 1 | 0.328614 |
| gpuls <= 2597 and gdpuls > -14 and gdenergy > -17 and gdenergy <= 1 | 1 | 0.160904 |
| gpuls <= 2597 and gdpuls > -13 and gdenergy <= 28 | 0 | 0.113798 |
| energy <= 6100 and energy > 2500 | 0 | 0.085486 |
| energy > 1000 | 1 | 0.896013 |
|  | 0 | 0.133333 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| nbumps >= 2 and gpuls >= 696 and gdpuls <= 21 and nbumps2 >= 1 and energy >= 5800 and nbumps4 <= 0 | 1 | 0.005589 |
|  | 0 | 0.941840 |


# Text representation of classifiers as-is

## JRip

Decision list:

rules | predicted class
---|---
(nbumps >= 2) and (gpuls >= 696) and (gdpuls <= 21) and (nbumps2 >= 1) and (energy >= 5800) and (nbumps4 <= 0)|1 (21.0/5.0)
|0 (2299.0/134.0)


## PART

Decision list:

rules | predicted class
---|---
nbumps <= 1 AND gpuls <= 1333 AND gpuls > 32 AND energy <= 15000 AND energy <= 7500 AND energy <= 5500 AND gdenergy <= 104|0 (1405.0/37.0)
gpuls > 98 AND gdenergy > 128|0 (161.0/5.0)
gpuls <= 98|0 (155.0)
nbumps2 <= 0 AND gdenergy <= 118 AND energy <= 16000 AND nbumps <= 2 AND gpuls <= 1405|0 (94.0/6.0)
energy <= 40600 AND nbumps3 <= 0 AND maxenergy <= 800 AND gpuls > 282 AND gdenergy > -27 AND genergy > 37710 AND gdpuls > -3|0 (62.0/4.0)
energy <= 36500 AND gpuls <= 669 AND gpuls <= 625 AND genergy > 21070|0 (144.0/20.0)
energy > 36500|0 (71.0/7.0)
genergy > 1134540|0 (15.0/1.0)
maxenergy > 7000 AND nbumps <= 1|0 (12.0)
gdenergy <= 112 AND gdpuls > 36 AND energy > 9400|0 (14.0)
energy <= 6000 AND nbumps3 <= 1 AND energy <= 5600 AND genergy <= 19240|0 (18.0/3.0)
gpuls > 261 AND gpuls > 669 AND gpuls <= 2457 AND maxenergy <= 4000 AND energy > 4600|0 (18.0/2.0)
gdenergy > -54 AND gpuls > 261 AND gpuls > 669 AND gpuls <= 2597 AND genergy > 207930 AND gdpuls <= 36 AND gpuls <= 2205 AND nbumps <= 3 AND gdenergy <= -14|0 (24.0/6.0)
maxenergy <= 1000 AND maxenergy > 800|0 (16.0/1.0)
gpuls <= 2597 AND gdenergy <= -43|1 (12.0/3.0)
gpuls <= 2597 AND gdpuls <= -24|0 (12.0/3.0)
gpuls <= 2597 AND gdpuls > -20 AND genergy <= 788650 AND gdenergy > -18 AND gdenergy <= 12 AND gdpuls > -1|1 (12.0/1.0)
gpuls <= 2597 AND gdpuls > -14 AND gdenergy > -17 AND gdenergy <= 1|1 (12.0/4.0)
gpuls <= 2597 AND gdpuls > -13 AND gdenergy <= 28|0 (17.0/1.0)
energy <= 6100 AND energy > 2500|0 (19.0/5.0)
energy > 1000|1 (21.0/2.0)
|0 (6.0/2.0)


## J48 Decision Tree

* : 0 (2320.0/150.0)


## SimpleCart Decision Tree

* nbumps < 1.5
	* gpuls < 1342.5
		* genergy < 16885.0
			* energy < 650.0
				* gdenergy < -84.5: 0(25.0/1.0)
				* gdenergy >= -84.5
					* gpuls < 219.0: 0(400.0/4.0)
					* gpuls >= 219.0: 0(285.0/0.0)
			* energy >= 650.0: 0(71.0/4.0)
		* genergy >= 16885.0: 0(951.0/40.0)
	* gpuls >= 1342.5
		* nbumps3 < 0.5: 0(55.0/5.0)
		* nbumps3 >= 0.5: 1(10.0/10.0)
* nbumps >= 1.5
	* gpuls < 677.0
				* seismoacoustic=(c)|(a)|(d): 0(143.0/15.0)
				* seismoacoustic!=(c)|(a)|(d)
			* genergy < 39510.0
				* nbumps3 < 1.5: 0(21.0/7.0)
				* nbumps3 >= 1.5: 1(7.0/4.0)
			* genergy >= 39510.0
				* gdenergy < 67.5: 0(38.0/1.0)
				* gdenergy >= 67.5: 0(10.0/6.0)
	* gpuls >= 677.0
		* gdpuls < 36.0
			* nbumps2 < 0.5: 0(29.0/3.0)
			* nbumps2 >= 0.5: 0(64.0/39.0)
		* gdpuls >= 36.0: 0(64.0/8.0)


