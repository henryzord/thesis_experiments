# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 0 | 0.935345 |
| nbumps >= 1.5 and gpuls >= 740.5 and gdenergy >= -29.5 and nbumps2 >= 0.5 and gpuls >= 759.5 and genergy < 526430.0 and energy >= 1550.0 and gpuls < 1451.5 and energy < 27350.0 and energy >= 21900.0 | 1 | 0.001036 |
| nbumps >= 1.5 and gpuls >= 740.5 and gdenergy >= -29.5 and nbumps2 >= 0.5 and gpuls >= 759.5 and genergy < 526430.0 and energy >= 1550.0 and gpuls < 1451.5 and energy < 27350.0 and energy < 21900.0 and energy < 12450.0 and energy >= 7350.0 | 1 | 0.001381 |
| nbumps < 1.5 and gpuls < 1342.5 and genergy < 18565.0 and gpuls < 786.0 and energy >= 650.0 and genergy < 3450.0 and energy >= 3500.0 | 1 | 0.000921 |
| nbumps < 1.5 and gpuls >= 1342.5 and nbumps3 < 0.5 and gpuls >= 1385.0 and gpuls >= 2800.0 and gpuls < 3290.0 | 1 | 0.000614 |
| nbumps >= 1.5 and gpuls >= 740.5 and gdenergy >= -29.5 and nbumps2 >= 0.5 and gpuls >= 759.5 and genergy >= 526430.0 and genergy < 656965.0 and energy < 32750.0 | 1 | 0.002815 |
| nbumps >= 1.5 and gpuls >= 740.5 and gdenergy >= -29.5 and nbumps2 >= 0.5 and gpuls >= 759.5 and genergy < 526430.0 and energy >= 1550.0 and gpuls >= 1451.5 and genergy >= 289800.0 and genergy < 395970.0 | 1 | 0.001036 |
| nbumps >= 1.5 and gpuls >= 740.5 and gdenergy >= -29.5 and nbumps2 >= 0.5 and gpuls >= 759.5 and genergy >= 526430.0 and genergy >= 656965.0 and nbumps < 4.5 and energy < 29900.0 and genergy < 799855.0 and seismoacoustic != c | 1 | 0.000519 |
| nbumps >= 1.5 and gpuls >= 740.5 and gdenergy < -29.5 and gdenergy < -32.5 and gdenergy >= -44.0 and gpuls >= 1291.0 and genergy < 448710.0 | 1 | 0.001917 |
| nbumps >= 1.5 and gpuls >= 740.5 and gdenergy >= -29.5 and nbumps2 >= 0.5 and gpuls < 759.5 | 1 | 0.000921 |
| nbumps >= 1.5 and gpuls >= 740.5 and gdenergy >= -29.5 and nbumps2 >= 0.5 and gpuls >= 759.5 and genergy >= 526430.0 and genergy >= 656965.0 and nbumps < 4.5 and energy >= 29900.0 | 1 | 0.000614 |
| nbumps >= 1.5 and gpuls >= 740.5 and gdenergy >= -29.5 and nbumps2 >= 0.5 and gpuls >= 759.5 and genergy < 526430.0 and energy >= 1550.0 and gpuls < 1451.5 and energy < 27350.0 and energy < 21900.0 and energy < 12450.0 and energy < 7350.0 and energy < 4650.0 and gpuls >= 1131.0 | 1 | 0.001381 |
| nbumps < 1.5 and gpuls >= 1342.5 and nbumps3 < 0.5 and gpuls < 1385.0 | 1 | 0.000614 |
| nbumps >= 1.5 and gpuls >= 740.5 and gdenergy < -29.5 and gdenergy >= -32.5 | 1 | 0.002757 |
| nbumps >= 1.5 and gpuls >= 740.5 and gdenergy >= -29.5 and nbumps2 >= 0.5 and gpuls >= 759.5 and genergy < 526430.0 and energy >= 1550.0 and gpuls < 1451.5 and energy < 27350.0 and energy < 21900.0 and energy < 12450.0 and energy < 7350.0 and energy < 4650.0 and gpuls < 1131.0 and genergy >= 58760.0 and energy < 2450.0 | 1 | 0.000921 |
| nbumps >= 1.5 and gpuls >= 740.5 and gdenergy >= -29.5 and nbumps2 >= 0.5 and gpuls >= 759.5 and genergy >= 526430.0 and genergy >= 656965.0 and nbumps >= 4.5 | 1 | 0.000921 |
| nbumps < 1.5 and gpuls >= 1342.5 and nbumps3 >= 0.5 and genergy < 422215.0 and genergy >= 132915.0 | 1 | 0.002299 |
| nbumps >= 1.5 and gpuls >= 740.5 and gdenergy >= -29.5 and nbumps2 >= 0.5 and gpuls >= 759.5 and genergy < 526430.0 and energy >= 1550.0 and gpuls < 1451.5 and energy < 27350.0 and energy < 21900.0 and energy < 12450.0 and energy < 7350.0 and energy < 4650.0 and gpuls < 1131.0 and genergy >= 58760.0 and energy >= 2450.0 and gpuls < 927.0 | 1 | 0.001036 |
| nbumps >= 1.5 and gpuls >= 740.5 and gdenergy < -29.5 and gdenergy < -32.5 and gdenergy < -44.0 and nbumps2 >= 0.5 | 1 | 0.002815 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| nbumps <= 1.5 and gpuls <= 1342.5 | 0 | 0.919036 |
| gpuls <= 740.5 and genergy <= 108930 and energy > 950 and gpuls > 95 and gdpuls > -55 and nbumps3 <= 3.5 and gpuls <= 677 and seismoacoustic = a | 0 | 0.399825 |
| genergy <= 1133675 and shift = W and gdpuls > 22 and gpuls <= 2904.5 and nbumps3 <= 3.5 and gdenergy <= 53.5 | 0 | 0.236206 |
| gdenergy <= 131 and genergy <= 1062020 and gpuls <= 361.5 | 0 | 0.208604 |
| gdenergy <= 187.5 and genergy <= 1062020 and energy <= 40650 and gpuls <= 2208.5 and gpuls > 413 and genergy <= 614380 and gpuls > 517.5 and nbumps <= 5.5 and gdenergy > -29.5 and gdpuls > -23.5 and energy <= 12300 and energy <= 8950 and maxenergy <= 4500 and genergy <= 207270 and gpuls <= 1445.5 and gpuls <= 899.5 | 0 | 0.082380 |
| gdenergy <= 131.5 and genergy > 1062020 | 0 | 0.139655 |
| gdenergy > 131.5 | 0 | 0.124265 |
| energy > 40650 | 0 | 0.098990 |
| gpuls > 413 and gpuls <= 618 | 0 | 0.067923 |
| gpuls > 630 and gdenergy > -29.5 and gdpuls > -23.5 and gdenergy > -17.5 and energy <= 26350 and gpuls <= 2208.5 and genergy <= 586025 and energy <= 2200 | 0 | 0.057997 |
| gpuls <= 630 | 1 | 0.413729 |
| genergy > 627870 and gdpuls <= -5 | 0 | 0.123711 |
| maxenergy > 7500 and nbumps2 <= 0.5 | 0 | 0.137487 |
| gpuls <= 2208.5 and gpuls <= 1959 and nbumps3 > 0.5 and gdenergy <= 60 and seismoacoustic = a | 1 | 0.267943 |
| gpuls <= 2208.5 and nbumps <= 3.5 and gpuls > 1477.5 | 0 | 0.157343 |
| genergy <= 544010 and nbumps > 3.5 | 0 | 0.217995 |
| genergy > 296350 | 1 | 0.434319 |
| seismoacoustic = b | 0 | 0.172043 |
|  | 1 | 0.723404 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| nbumps >= 2 and gpuls >= 744 and gdenergy <= -30 | 1 | 0.004518 |
|  | 0 | 0.942659 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

gpuls|gdenergy|gdpuls|nbumps|nbumps5|nbumps6|nbumps7|nbumps89|class
---|---|---|---|---|---|---|---|---
(375.5-1139.5]|all|all|(1.5-inf)|all|all|all|all|0
(1139.5-inf)|all|all|(1.5-inf)|all|all|all|all|0
(-inf-375.5]|all|all|(1.5-inf)|all|all|all|all|0
(1139.5-inf)|all|all|(0.5-1.5]|all|all|all|all|0
(-inf-375.5]|all|all|(0.5-1.5]|all|all|all|all|0
(375.5-1139.5]|all|all|(0.5-1.5]|all|all|all|all|0
(1139.5-inf)|all|all|(-inf-0.5]|all|all|all|all|0
(-inf-375.5]|all|all|(-inf-0.5]|all|all|all|all|0
(375.5-1139.5]|all|all|(-inf-0.5]|all|all|all|all|0

## JRip

Decision list:

rules | predicted class
---|---
(nbumps >= 2) and (gpuls >= 744) and (gdenergy <= -30)|1 (33.0/15.0)
|0 (2287.0/132.0)


## PART

Decision list:

rules | predicted class
---|---
nbumps <= 1.5 AND gpuls <= 1342.5|0 (1780.0/46.0)
gpuls <= 740.5 AND genergy <= 108930 AND energy > 950 AND gpuls > 95 AND gdpuls > -55 AND nbumps3 <= 3.5 AND gpuls <= 677 AND seismoacoustic = a|0 (113.0/6.0)
genergy <= 1133675 AND shift = W AND gdpuls > 22 AND gpuls <= 2904.5 AND nbumps3 <= 3.5 AND gdenergy <= 53.5|0 (51.0/1.0)
gdenergy <= 131 AND genergy <= 1062020 AND gpuls <= 361.5|0 (66.0/9.0)
gdenergy <= 187.5 AND genergy <= 1062020 AND energy <= 40650 AND gpuls <= 2208.5 AND gpuls > 413 AND genergy <= 614380 AND gpuls > 517.5 AND nbumps <= 5.5 AND gdenergy > -29.5 AND gdpuls > -23.5 AND energy <= 12300 AND energy <= 8950 AND maxenergy <= 4500 AND genergy <= 207270 AND gpuls <= 1445.5 AND gpuls <= 899.5|0 (31.0/7.0)
gdenergy <= 131.5 AND genergy > 1062020|0 (29.0/2.0)
gdenergy > 131.5|0 (27.0/1.0)
energy > 40650|0 (25.0/4.0)
gpuls > 413 AND gpuls <= 618|0 (24.0/4.0)
gpuls > 630 AND gdenergy > -29.5 AND gdpuls > -23.5 AND gdenergy > -17.5 AND energy <= 26350 AND gpuls <= 2208.5 AND genergy <= 586025 AND energy <= 2200|0 (21.0/4.0)
gpuls <= 630|1 (13.0/4.0)
genergy > 627870 AND gdpuls <= -5|0 (12.0)
maxenergy > 7500 AND nbumps2 <= 0.5|0 (18.0/2.0)
gpuls <= 2208.5 AND gpuls <= 1959 AND nbumps3 > 0.5 AND gdenergy <= 60 AND seismoacoustic = a|1 (37.0/10.0)
gpuls <= 2208.5 AND nbumps <= 3.5 AND gpuls > 1477.5|0 (18.0/4.0)
genergy <= 544010 AND nbumps > 3.5|0 (18.0/1.0)
genergy > 296350|1 (14.0/2.0)
seismoacoustic = b|0 (12.0/3.0)
|1 (11.0/3.0)


## SimpleCart Decision Tree

* nbumps < 1.5
	* gpuls < 1342.5
		* genergy < 18565.0
			* gpuls < 786.0
				* energy < 650.0
					* gdpuls < -0.5
						* genergy < 13675.0: 0(454.0/0.0)
						* genergy >= 13675.0: 0(88.0/1.0)
					* gdpuls >= -0.5
						* gpuls < 199.0: 0(42.0/3.0)
						* gpuls >= 199.0: 0(170.0/0.0)
				* energy >= 650.0
					* genergy < 3450.0
						* energy < 3500.0: 0(3.0/0.0)
						* energy >= 3500.0: 1(2.0/0.0)
					* genergy >= 3450.0
						* gdenergy < 57.5
							* energy < 1500.0
								* gdpuls < -43.0: 0(13.0/0.0)
								* gdpuls >= -43.0: 0(9.0/2.0)
							* energy >= 1500.0: 0(57.0/0.0)
						* gdenergy >= 57.5: 0(2.0/1.0)
			* gpuls >= 786.0: 0(2.0/1.0)
		* genergy >= 18565.0: 0(894.0/36.0)
	* gpuls >= 1342.5
		* nbumps3 < 0.5
			* gpuls < 1385.0: 1(2.0/1.0)
			* gpuls >= 1385.0
				* gpuls < 2800.0
					* genergy < 47485.0: 0(2.0/1.0)
					* genergy >= 47485.0
						* gdenergy < 7.5: 0(18.0/2.0)
						* gdenergy >= 7.5: 0(22.0/0.0)
				* gpuls >= 2800.0
					* gpuls < 3290.0: 1(2.0/1.0)
					* gpuls >= 3290.0: 0(4.0/0.0)
		* nbumps3 >= 0.5
			* genergy < 422215.0
				* genergy < 132915.0: 0(2.0/1.0)
				* genergy >= 132915.0: 1(5.0/0.0)
			* genergy >= 422215.0: 0(8.0/2.0)
* nbumps >= 1.5
	* gpuls < 740.5: 0(231.0/34.0)
	* gpuls >= 740.5
		* gdenergy < -29.5
			* gdenergy < -32.5
				* gdenergy < -44.0
					* nbumps2 < 0.5: 0(2.0/0.0)
					* nbumps2 >= 0.5: 1(7.0/1.0)
				* gdenergy >= -44.0
					* gpuls < 1291.0: 0(6.0/0.0)
					* gpuls >= 1291.0
						* genergy < 448710.0: 1(5.0/1.0)
						* genergy >= 448710.0: 0(5.0/0.0)
			* gdenergy >= -32.5: 1(6.0/0.0)
		* gdenergy >= -29.5
			* nbumps2 < 0.5: 0(36.0/3.0)
			* nbumps2 >= 0.5
				* gpuls < 759.5: 1(2.0/0.0)
				* gpuls >= 759.5
					* genergy < 526430.0
						* energy < 1550.0: 0(14.0/0.0)
						* energy >= 1550.0
							* gpuls < 1451.5
								* energy < 27350.0
									* energy < 21900.0
										* energy < 12450.0
											* energy < 7350.0
												* energy < 4650.0
													* gpuls < 1131.0
														* genergy < 58760.0: 0(4.0/0.0)
														* genergy >= 58760.0
															* energy < 2450.0: 1(2.0/0.0)
															* energy >= 2450.0
																* gpuls < 927.0: 1(3.0/1.0)
																* gpuls >= 927.0: 0(5.0/0.0)
													* gpuls >= 1131.0: 1(3.0/0.0)
												* energy >= 4650.0: 0(7.0/0.0)
											* energy >= 7350.0: 1(3.0/0.0)
										* energy >= 12450.0: 0(7.0/0.0)
									* energy >= 21900.0: 1(3.0/1.0)
								* energy >= 27350.0: 0(5.0/0.0)
							* gpuls >= 1451.5
								* genergy < 289800.0: 0(18.0/0.0)
								* genergy >= 289800.0
									* genergy < 395970.0: 1(3.0/1.0)
									* genergy >= 395970.0: 0(6.0/0.0)
					* genergy >= 526430.0
						* genergy < 656965.0
							* energy < 32750.0: 1(7.0/1.0)
							* energy >= 32750.0: 0(2.0/0.0)
						* genergy >= 656965.0
							* nbumps < 4.5
								* energy < 29900.0
									* genergy < 799855.0
												* seismoacoustic=(c)|(a)|(d): 0(5.0/1.0)
												* seismoacoustic!=(c)|(a)|(d): 1(2.0/1.0)
									* genergy >= 799855.0
										* gpuls < 1581.5: 0(2.0/1.0)
										* gpuls >= 1581.5: 0(15.0/0.0)
								* energy >= 29900.0: 1(2.0/1.0)
							* nbumps >= 4.5: 1(2.0/0.0)


