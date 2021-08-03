# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 0 | 0.935345 |
| nbumps >= 1.5 and gpuls >= 740.5 and gdenergy >= -29.5 and nbumps2 >= 0.5 and genergy >= 289800.0 and gdpuls < 95.5 and genergy < 799855.0 and gdenergy >= -18.5 and gdpuls < 36.0 and gpuls < 2211.5 and genergy >= 587745.0 and seismoacoustic != d | 1 | 0.000077 |
| nbumps >= 1.5 and gpuls >= 740.5 and gdenergy < -29.5 and gdenergy >= -32.5 | 1 | 0.002757 |
| nbumps < 1.5 and gpuls >= 1410.0 and gpuls < 1443.5 | 1 | 0.001381 |
| nbumps < 1.5 and gpuls >= 1410.0 and gpuls >= 1443.5 and gdenergy >= -32.5 and gpuls < 2800.0 and gdenergy < 7.5 and genergy < 254575.0 | 1 | 0.000614 |
| nbumps > 1 and ghazard = a and seismic = b and nbumps <= 2 and seismoacoustic = a and gpuls > 882 and nbumps2 > 0 | 1 | 0.001880 |
| nbumps >= 1.5 and gpuls >= 740.5 and gdenergy >= -29.5 and nbumps2 >= 0.5 and genergy < 289800.0 and gpuls < 1451.5 and gpuls < 968.5 and nbumps2 >= 2.5 and seismic != c | 1 | 0.000461 |
| nbumps < 1.5 and gpuls >= 1410.0 and gpuls >= 1443.5 and gdenergy >= -32.5 and gpuls >= 2800.0 and genergy < 986310.0 | 1 | 0.000921 |
| nbumps >= 1.5 and gpuls >= 740.5 and gdenergy >= -29.5 and nbumps2 >= 0.5 and genergy < 289800.0 and gpuls < 1451.5 and gpuls >= 968.5 and seismoacoustic!=(b) and energy < 4950.0 | 1 | 0.000961 |
| nbumps >= 1.5 and gpuls >= 740.5 and gdenergy >= -29.5 and nbumps2 >= 0.5 and genergy >= 289800.0 and gdpuls < 95.5 and genergy < 799855.0 and gdenergy >= -18.5 and gdpuls < 36.0 and gpuls < 2211.5 and genergy < 587745.0 and genergy < 551490.0 and nbumps < 3.5 | 1 | 0.001439 |
| nbumps > 1 and ghazard = a and seismic = a and nbumps3 > 3 and genergy > 57440 | 1 | 0.001228 |
| nbumps >= 1.5 and gpuls >= 740.5 and gdenergy >= -29.5 and nbumps2 >= 0.5 and genergy < 289800.0 and gpuls < 1451.5 and gpuls >= 968.5 and seismoacoustic!=(b) and energy >= 4950.0 and genergy >= 119880.0 and nbumps3 >= 0.5 | 1 | 0.000829 |
| genergy <= 18585 and gpuls <= 1139.5 and nbumps2 > 0.5 and nbumps3 > 1.5 and nbumps5 = all and nbumps6 = all and nbumps89 = all and energy > 550 | 1 | 0.000461 |
| nbumps < 1.5 and gpuls >= 1410.0 and gpuls >= 1443.5 and gdenergy < -32.5 and gdenergy >= -40.5 | 1 | 0.001381 |
| nbumps >= 1.5 and gpuls >= 740.5 and gdenergy < -29.5 and gdenergy < -32.5 and gdenergy >= -44.0 and gpuls >= 1291.0 and genergy < 448710.0 | 1 | 0.001917 |
| nbumps >= 1.5 and gpuls >= 740.5 and gdenergy >= -29.5 and nbumps2 >= 0.5 and genergy >= 289800.0 and gdpuls < 95.5 and genergy < 799855.0 and gdenergy >= -18.5 and gdpuls < 36.0 and gpuls >= 2211.5 | 1 | 0.002299 |
| nbumps >= 1.5 and gpuls >= 740.5 and gdenergy < -29.5 and gdenergy < -32.5 and gdenergy < -44.0 and nbumps2 >= 0.5 | 1 | 0.002815 |
| nbumps >= 1.5 and gpuls >= 740.5 and gdenergy >= -29.5 and nbumps2 >= 0.5 and genergy >= 289800.0 and gdpuls >= 95.5 | 1 | 0.001381 |
| nbumps >= 1.5 and gpuls >= 740.5 and gdenergy >= -29.5 and nbumps2 >= 0.5 and genergy >= 289800.0 and gdpuls < 95.5 and genergy < 799855.0 and gdenergy >= -18.5 and gdpuls < 36.0 and gpuls < 2211.5 and genergy < 587745.0 and genergy >= 551490.0 | 1 | 0.001840 |
| nbumps < 1.5 and gpuls < 1410.0 and genergy < 18565.0 and gpuls < 786.0 and energy >= 650.0 and genergy < 3450.0 and energy >= 3500.0 | 1 | 0.000921 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| nbumps <= 1.5 and gpuls <= 1410.0 | 0 | 0.919282 |
| seismic = a and seismoacoustic != c and shift = W and seismoacoustic = a and gdenergy > -36.5 | 0 | 0.398378 |
| gpuls <= 1136.0 and seismoacoustic != c and nbumps2 > 0.5 and ghazard = a and nbumps4 <= 0.5 and seismoacoustic != a and seismic = a | 0 | 0.223307 |
| shift = W and gpuls <= 1136.0 | 0 | 0.430732 |
| shift != W | 0 | 0.075415 |
| nbumps4 > 0.5 and nbumps2 <= 0.5 | 0 | 0.110806 |
| gdenergy > -29.5 and seismoacoustic != a | 0 | 0.151522 |
| seismic = a | 1 | 0.679245 |
| nbumps2 <= 2.5 and nbumps3 > 1.5 and nbumps3 <= 2.5 and nbumps2 <= 1.5 and nbumps2 > 0.5 | 1 | 0.139601 |
| nbumps2 <= 2.5 and nbumps3 <= 1.5 and nbumps3 > 0.5 and gpuls <= 1892.0 | 1 | 0.358491 |
|  | 0 | 0.395349 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| nbumps >= 2 and gpuls >= 744 and gdenergy <= -30 and gdenergy >= -32 | 1 | 0.002757 |
| nbumps >= 2 and gpuls >= 751 and nbumps2 >= 1 and gdenergy <= -45 and nbumps4 <= 0 | 1 | 0.003215 |
| nbumps >= 2 and gpuls >= 979 and nbumps2 >= 1 and energy >= 5800 and energy <= 9200 and gdenergy <= 18 | 1 | 0.003215 |
| nbumps >= 2 and gpuls <= 1584 and energy <= 4200 and gpuls >= 1352 | 1 | 0.001841 |
| nbumps >= 3 and gpuls >= 384 and gdpuls >= 94 and seismic = b and seismoacoustic = b | 1 | 0.002299 |
| nbumps >= 2 and gdpuls <= 10 and gdpuls >= 5 and genergy <= 39700 | 1 | 0.002757 |
|  | 0 | 0.950504 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

genergy|gpuls|nbumps2|nbumps3|nbumps5|nbumps6|nbumps89|energy|class
---|---|---|---|---|---|---|---|---
(48545-inf)|(1139.5-inf)|(0.5-inf)|(1.5-inf)|all|all|all|(550-inf)|0
(48545-inf)|(-inf-1139.5]|(0.5-inf)|(1.5-inf)|all|all|all|(550-inf)|0
(-inf-18585]|(-inf-1139.5]|(0.5-inf)|(1.5-inf)|all|all|all|(550-inf)|1
(18585-48545]|(-inf-1139.5]|(0.5-inf)|(1.5-inf)|all|all|all|(550-inf)|0
(48545-inf)|(1139.5-inf)|(-inf-0.5]|(1.5-inf)|all|all|all|(550-inf)|0
(-inf-18585]|(-inf-1139.5]|(-inf-0.5]|(1.5-inf)|all|all|all|(550-inf)|0
(18585-48545]|(-inf-1139.5]|(-inf-0.5]|(1.5-inf)|all|all|all|(550-inf)|0
(48545-inf)|(-inf-1139.5]|(-inf-0.5]|(1.5-inf)|all|all|all|(550-inf)|0
(48545-inf)|(1139.5-inf)|(0.5-inf)|(0.5-1.5]|all|all|all|(550-inf)|0
(-inf-18585]|(-inf-1139.5]|(0.5-inf)|(0.5-1.5]|all|all|all|(550-inf)|0
(48545-inf)|(-inf-1139.5]|(0.5-inf)|(0.5-1.5]|all|all|all|(550-inf)|0
(18585-48545]|(-inf-1139.5]|(0.5-inf)|(0.5-1.5]|all|all|all|(550-inf)|0
(18585-48545]|(1139.5-inf)|(-inf-0.5]|(0.5-1.5]|all|all|all|(550-inf)|0
(48545-inf)|(1139.5-inf)|(-inf-0.5]|(0.5-1.5]|all|all|all|(550-inf)|0
(18585-48545]|(1139.5-inf)|(0.5-inf)|(-inf-0.5]|all|all|all|(550-inf)|1
(48545-inf)|(1139.5-inf)|(0.5-inf)|(-inf-0.5]|all|all|all|(550-inf)|0
(-inf-18585]|(-inf-1139.5]|(-inf-0.5]|(0.5-1.5]|all|all|all|(550-inf)|0
(18585-48545]|(-inf-1139.5]|(-inf-0.5]|(0.5-1.5]|all|all|all|(550-inf)|0
(48545-inf)|(-inf-1139.5]|(-inf-0.5]|(0.5-1.5]|all|all|all|(550-inf)|0
(-inf-18585]|(-inf-1139.5]|(0.5-inf)|(-inf-0.5]|all|all|all|(550-inf)|0
(48545-inf)|(-inf-1139.5]|(0.5-inf)|(-inf-0.5]|all|all|all|(550-inf)|0
(18585-48545]|(-inf-1139.5]|(0.5-inf)|(-inf-0.5]|all|all|all|(550-inf)|0
(48545-inf)|(1139.5-inf)|(-inf-0.5]|(-inf-0.5]|all|all|all|(550-inf)|0
(48545-inf)|(-inf-1139.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|(550-inf)|0
(-inf-18585]|(-inf-1139.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|(550-inf)|0
(18585-48545]|(-inf-1139.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|(550-inf)|0
(48545-inf)|(1139.5-inf)|(0.5-inf)|(-inf-0.5]|all|all|all|(-inf-550]|0
(18585-48545]|(1139.5-inf)|(0.5-inf)|(-inf-0.5]|all|all|all|(-inf-550]|0
(48545-inf)|(-inf-1139.5]|(0.5-inf)|(-inf-0.5]|all|all|all|(-inf-550]|0
(18585-48545]|(-inf-1139.5]|(0.5-inf)|(-inf-0.5]|all|all|all|(-inf-550]|0
(-inf-18585]|(-inf-1139.5]|(0.5-inf)|(-inf-0.5]|all|all|all|(-inf-550]|0
(18585-48545]|(1139.5-inf)|(-inf-0.5]|(-inf-0.5]|all|all|all|(-inf-550]|0
(48545-inf)|(1139.5-inf)|(-inf-0.5]|(-inf-0.5]|all|all|all|(-inf-550]|0
(18585-48545]|(-inf-1139.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|(-inf-550]|0
(48545-inf)|(-inf-1139.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|(-inf-550]|0
(-inf-18585]|(-inf-1139.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|(-inf-550]|0

## JRip

Decision list:

rules | predicted class
---|---
(nbumps >= 2) and (gpuls >= 744) and (gdenergy <= -30) and (gdenergy >= -32)|1 (6.0/0.0)
(nbumps >= 2) and (gpuls >= 751) and (nbumps2 >= 1) and (gdenergy <= -45) and (nbumps4 <= 0)|1 (7.0/0.0)
(nbumps >= 2) and (gpuls >= 979) and (nbumps2 >= 1) and (energy >= 5800) and (energy <= 9200) and (gdenergy <= 18)|1 (7.0/0.0)
(nbumps >= 2) and (gpuls <= 1584) and (energy <= 4200) and (gpuls >= 1352)|1 (9.0/3.0)
(nbumps >= 3) and (gpuls >= 384) and (gdpuls >= 94) and (seismic = b) and (seismoacoustic = b)|1 (5.0/0.0)
(nbumps >= 2) and (gdpuls <= 10) and (gdpuls >= 5) and (genergy <= 39700)|1 (6.0/0.0)
|0 (2280.0/113.0)


## PART

Decision list:

rules | predicted class
---|---
nbumps <= 1.5 AND gpuls <= 1410.0|0 (1589.0/40.0)
seismic = a AND seismoacoustic != c AND shift = W AND seismoacoustic = a AND gdenergy > -36.5|0 (117.0/10.0)
gpuls <= 1136.0 AND seismoacoustic != c AND nbumps2 > 0.5 AND ghazard = a AND nbumps4 <= 0.5 AND seismoacoustic != a AND seismic = a|0 (49.0/6.0)
shift = W AND gpuls <= 1136.0|0 (157.0/27.0)
shift != W|0 (22.0/3.0)
nbumps4 > 0.5 AND nbumps2 <= 0.5|0 (21.0/2.0)
gdenergy > -29.5 AND seismoacoustic != a|0 (49.0/15.0)
seismic = a|1 (4.0)
nbumps2 <= 2.5 AND nbumps3 > 1.5 AND nbumps3 <= 2.5 AND nbumps2 <= 1.5 AND nbumps2 > 0.5|1 (4.0/2.0)
nbumps2 <= 2.5 AND nbumps3 <= 1.5 AND nbumps3 > 0.5 AND gpuls <= 1892.0|1 (13.0)
|0 (38.0/12.0)


## J48 Decision Tree

* nbumps <= 1: 0 (1384.0/46.0)
* nbumps > 1
	* ghazard = a
		* seismic = a
			* nbumps3 <= 3: 0 (176.0/23.0)
			* nbumps3 > 3
				* genergy <= 57440: 0 (5.0/1.0)
				* genergy > 57440: 1 (5.0/2.0)
		* seismic = b
			* nbumps <= 2
				* seismoacoustic = a
					* gpuls <= 882: 0 (20.0)
					* gpuls > 882
						* nbumps2 <= 0: 0 (8.0/1.0)
						* nbumps2 > 0: 1 (9.0/4.0)
				* seismoacoustic = b: 0 (16.0/1.0)
				* seismoacoustic = c: 0 (2.0)
				* seismoacoustic = d: 0 (0.0)
			* nbumps > 2: 0 (91.0/25.0)
		* seismic = c: 0 (0.0)
		* seismic = d: 0 (0.0)
	* ghazard = b: 0 (22.0/7.0)
	* ghazard = c: 0 (2.0)
	* ghazard = d: 0 (0.0)


## SimpleCart Decision Tree

* nbumps < 1.5
	* gpuls < 1410.0
		* genergy < 18565.0
			* gpuls < 786.0
				* energy < 650.0
					* gdpuls < -0.5
						* genergy < 13675.0: 0(454.0/0.0)
						* genergy >= 13675.0: 0(87.0/1.0)
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
							* energy >= 1500.0: 0(58.0/0.0)
						* gdenergy >= 57.5: 0(2.0/1.0)
			* gpuls >= 786.0: 0(2.0/1.0)
		* genergy >= 18565.0: 0(900.0/37.0)
	* gpuls >= 1410.0
		* gpuls < 1443.5: 1(3.0/0.0)
		* gpuls >= 1443.5
			* gdenergy < -32.5
				* gdenergy < -40.5: 0(2.0/1.0)
				* gdenergy >= -40.5: 1(3.0/0.0)
			* gdenergy >= -32.5
				* gpuls < 2800.0
					* gdenergy < 7.5
						* genergy < 254575.0: 1(2.0/1.0)
						* genergy >= 254575.0
									* seismoacoustic=(a)|(c)|(d): 0(13.0/0.0)
									* seismoacoustic!=(a)|(c)|(d): 0(3.0/1.0)
					* gdenergy >= 7.5: 0(27.0/0.0)
				* gpuls >= 2800.0
					* genergy < 986310.0: 1(2.0/0.0)
					* genergy >= 986310.0: 0(6.0/1.0)
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
				* genergy < 289800.0
					* gpuls < 1451.5
						* gpuls < 968.5
							* nbumps2 < 2.5
								* gdenergy < 11.5: 0(7.0/2.0)
								* gdenergy >= 11.5: 0(13.0/0.0)
							* nbumps2 >= 2.5
										* seismic=(b)|(c)|(d): 0(2.0/0.0)
										* seismic!=(b)|(c)|(d): 1(2.0/0.0)
						* gpuls >= 968.5
							* seismoacoustic=(b)
								* nbumps < 4.5: 0(9.0/0.0)
								* nbumps >= 4.5: 1(2.0/1.0)
							* seismoacoustic!=(b)
								* energy < 4950.0: 1(5.0/0.0)
								* energy >= 4950.0
									* genergy < 119880.0: 0(3.0/0.0)
									* genergy >= 119880.0
										* nbumps3 < 0.5: 0(2.0/0.0)
										* nbumps3 >= 0.5: 1(3.0/0.0)
					* gpuls >= 1451.5: 0(21.0/0.0)
				* genergy >= 289800.0
					* gdpuls < 95.5
						* genergy < 799855.0
							* gdenergy < -18.5: 0(5.0/0.0)
							* gdenergy >= -18.5
								* gdpuls < 36.0
									* gpuls < 2211.5
										* genergy < 587745.0
											* genergy < 551490.0
												* nbumps < 3.5: 1(5.0/3.0)
												* nbumps >= 3.5: 0(3.0/0.0)
											* genergy >= 551490.0: 1(4.0/0.0)
										* genergy >= 587745.0
													* seismoacoustic=(a)|(c)|(d): 0(4.0/0.0)
													* seismoacoustic!=(a)|(c)|(d): 1(1.0/1.0)
									* gpuls >= 2211.5: 1(5.0/0.0)
								* gdpuls >= 36.0: 0(4.0/0.0)
						* genergy >= 799855.0: 0(18.0/3.0)
					* gdpuls >= 95.5: 1(3.0/0.0)


