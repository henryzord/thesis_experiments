# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Persons != 4 | unacc | 0.607495 |
| Persons != more | unacc | 0.600155 |
| Persons != 2 and Safety != low and Buying != vhigh and Buying = high and Maint != vhigh and Lug_boot != small and Safety != med | acc | 0.035942 |
| Persons != 2 and Safety != low and Buying != vhigh and Buying != high and Maint = vhigh and Lug_boot != small and Lug_boot != med | acc | 0.025040 |
| Persons != 2 and Safety != low and Buying = vhigh and Maint != high and Maint != vhigh and Lug_boot != small and Lug_boot != med | acc | 0.024252 |
| Persons != 2 and Safety != low and Buying != vhigh and Buying != high and Maint != vhigh and Safety = med and Lug_boot != small and Maint = high | acc | 0.016582 |
| Persons != 2 and Safety != low and Buying != vhigh and Buying != high and Maint != vhigh and Safety = med and Lug_boot = small and Maint != high and Doors != 2 | acc | 0.017901 |
| Persons != 2 and Safety != low and Buying != vhigh and Buying = high and Maint != vhigh and Lug_boot != small and Safety = med and Lug_boot != med | acc | 0.017101 |
| Persons != 2 and Safety != low and Buying != vhigh and Buying != high and Maint != vhigh and Safety != med and Lug_boot != small and Maint != high and Lug_boot != med | vgood | 0.019685 |
| Persons != 2 and Safety != low and Buying != vhigh and Buying != high and Maint != vhigh and Safety != med and Lug_boot != small and Maint = high and Buying = med | acc | 0.012275 |
| Persons != 2 and Safety != low and Buying = vhigh and Maint != high and Maint != vhigh and Lug_boot != small and Lug_boot = med and Safety != med | acc | 0.012275 |
| Persons != 2 and Safety != low and Buying != vhigh and Buying = high and Maint != vhigh and Lug_boot = small and Safety != med and Doors != 2 | acc | 0.011466 |
| Persons != 2 and Safety != low and Buying != vhigh and Buying != high and Maint = vhigh and Lug_boot != small and Lug_boot = med and Safety != med | acc | 0.011466 |
| Persons != 2 and Safety != low and Buying != vhigh and Buying != high and Maint = vhigh and Lug_boot = small and Safety != med | acc | 0.009250 |
| Persons != 2 and Safety != low and Buying != vhigh and Buying != high and Maint != vhigh and Safety = med and Lug_boot != small and Maint != high and Buying = med and Maint = med | acc | 0.010656 |
| Persons != 2 and Safety != low and Buying = vhigh and Maint != high and Maint != vhigh and Lug_boot = small and Safety != med | acc | 0.009094 |
| Persons != 2 and Safety != low and Buying != vhigh and Buying != high and Maint != vhigh and Safety = med and Lug_boot != small and Maint != high and Buying != med and Lug_boot != med | good | 0.009954 |
| Persons != 2 and Safety != low and Buying != vhigh and Buying != high and Maint != vhigh and Safety != med and Lug_boot = small and Doors != 2 and Maint != low and Buying = med | acc | 0.009031 |
| Persons != 2 and Safety != low and Buying != vhigh and Buying = high and Maint != vhigh and Lug_boot != small and Safety = med and Lug_boot = med and Doors != 2 and Doors != 3 | acc | 0.009031 |
| Persons != 2 and Safety != low and Buying != vhigh and Buying != high and Maint = vhigh and Lug_boot != small and Lug_boot = med and Safety = med and Doors != 2 | acc | 0.006859 |
| Persons != 2 and Safety != low and Buying != vhigh and Buying != high and Maint != vhigh and Safety != med and Lug_boot != small and Maint != high and Lug_boot = med and Doors != 2 | vgood | 0.008941 |
| Persons != 2 and Safety != low and Buying = vhigh and Maint != high and Maint != vhigh and Lug_boot != small and Lug_boot = med and Safety = med and Doors != 2 | acc | 0.006859 |
| Persons != 2 and Safety != low and Buying != vhigh and Buying != high and Maint != vhigh and Safety != med and Lug_boot = small and Doors != 2 and Maint = low | good | 0.005996 |
| Persons != 2 and Safety != low and Buying != vhigh and Buying != high and Maint != vhigh and Safety = med and Lug_boot != small and Maint != high and Buying != med and Lug_boot = med and Doors != 2 | good | 0.005556 |
| Persons != 2 and Safety != low and Buying != vhigh and Buying != high and Maint != vhigh and Safety != med and Lug_boot != small and Maint = high and Buying != med | vgood | 0.006839 |
| Persons != 2 and Safety != low and Buying != vhigh and Buying != high and Maint != vhigh and Safety = med and Lug_boot != small and Maint != high and Buying = med and Maint != med | good | 0.005132 |
| Persons != 2 and Safety != low and Buying != vhigh and Buying != high and Maint != vhigh and Safety = med and Lug_boot = small and Maint = high and Buying != med | acc | 0.003441 |
| Persons != 2 and Safety != low and Buying != vhigh and Buying != high and Maint != vhigh and Safety != med and Lug_boot = small and Doors != 2 and Maint != low and Buying != med and Maint = high | acc | 0.004125 |
| Persons != 2 and Safety != low and Buying != vhigh and Buying != high and Maint != vhigh and Safety = med and Lug_boot != small and Maint != high and Buying != med and Lug_boot = med and Doors = 2 | acc | 0.003303 |
| Persons != 2 and Safety != low and Buying != vhigh and Buying != high and Maint != vhigh and Safety != med and Lug_boot = small and Doors != 2 and Maint != low and Buying != med and Maint != high | good | 0.004005 |
| Persons != 2 and Safety != low and Buying != vhigh and Buying = high and Maint != vhigh and Lug_boot != small and Safety = med and Lug_boot = med and Doors != 2 and Doors = 3 and Persons != 4 | acc | 0.002479 |
| Persons != 2 and Safety != low and Buying != vhigh and Buying = high and Maint != vhigh and Lug_boot = small and Safety != med and Doors = 2 and Persons = 4 | acc | 0.002479 |
| Persons != 2 and Safety != low and Buying != vhigh and Buying != high and Maint != vhigh and Safety != med and Lug_boot != small and Maint != high and Lug_boot = med and Doors = 2 | good | 0.003008 |
| Persons != 2 and Safety != low and Buying != vhigh and Buying != high and Maint != vhigh and Safety != med and Lug_boot = small and Doors = 2 and Persons = 4 | acc | 0.001490 |
| Persons = 4 and Safety = med and Buying = med and Maint != med and Lug_boot = med and Maint!=(high) | acc | 0.002486 |
| Persons = 4 and Safety = med and Buying = med and Maint = med and Safety != low and Lug_boot != big | acc | 0.006584 |
| Persons = 4 and Safety = med and Buying != med and Maint != med and Buying = low and Maint = low and Lug_boot = med | acc | 0.000829 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Persons = 2 | unacc | 0.531377 |
| Safety = low | unacc | 0.426980 |
| Buying = vhigh and Maint = high | unacc | 0.090373 |
| Maint = vhigh and Buying = high | unacc | 0.081349 |
| Lug_boot = small and Safety = med and Buying != vhigh and Buying != high and Maint != vhigh and Maint != high and Doors != 2 | acc | 0.080882 |
| Lug_boot = small and Safety = med and Buying != low and Maint != med | unacc | 0.088843 |
| Buying = vhigh and Maint != vhigh and Safety != med and Doors != 2 | acc | 0.144628 |
| Buying = vhigh and Maint = vhigh | unacc | 0.073059 |
| Safety = med and Lug_boot = small and Maint != high and Doors != 2 | unacc | 0.037915 |
| Buying = high and Doors != 2 and Doors != 3 | acc | 0.257009 |
| Maint = vhigh and Doors != 2 and Doors != 3 | acc | 0.192893 |
| Safety = med and Lug_boot = big and Buying != low and Maint != low | acc | 0.171875 |
| Safety = med and Lug_boot = big and Maint != med and Maint != low | acc | 0.059172 |
| Safety = med and Lug_boot = big and Buying != vhigh and Buying = low | good | 0.056391 |
| Lug_boot = big and Safety = med and Buying = vhigh | acc | 0.046358 |
| Lug_boot = big and Safety != med and Buying != high and Maint != vhigh and Buying = low | vgood | 0.086957 |
| Safety = med and Doors = 2 and Buying != med and Buying != low | unacc | 0.038685 |
| Buying = high and Safety != med and Lug_boot != small | acc | 0.164179 |
| Maint = vhigh and Safety != med and Lug_boot != small | acc | 0.118110 |
| Lug_boot = big and Safety != med and Maint != high and Doors != 2 | vgood | 0.061224 |
| Maint = vhigh and Doors = 2 | unacc | 0.029915 |
| Maint = high and Doors != 2 and Buying != low and Safety != med | acc | 0.162162 |
| Maint = high and Doors = 2 and Persons != 4 | unacc | 0.017361 |
| Maint = high and Safety = med and Buying = low | acc | 0.102041 |
| Buying = vhigh and Maint != med | acc | 0.093721 |
| Maint = low and Buying != high and Lug_boot = small and Persons != 4 | good | 0.020050 |
| Buying = high and Lug_boot != med | acc | 0.061174 |
| Maint = low and Safety != med and Lug_boot != small and Doors != 2 | vgood | 0.042535 |
| Maint = low and Lug_boot != big and Safety = med and Doors != 3 | good | 0.048265 |
| Maint = low and Doors != 3 | good | 0.064806 |
| Safety = med and Buying != high and Maint != low and Buying != low and Doors != 3 and Persons = 4 | acc | 0.111111 |
| Safety = med and Buying != high and Maint != low and Buying != low and Doors = 3 | acc | 0.052966 |
| Buying != high and Lug_boot = small and Doors != 2 and Maint != med | acc | 0.124615 |
| Safety = med and Buying != high and Doors != 2 and Buying = low | good | 0.045570 |
| Buying != high and Lug_boot != small and Safety = med | acc | 0.164474 |
| Safety = med | unacc | 0.120301 |
| Lug_boot != small and Doors != 2 and Persons != 4 | vgood | 0.096531 |
| Buying != low and Lug_boot != small | acc | 0.198347 |
| Buying != low | acc | 0.135000 |
| Lug_boot = small | good | 0.187135 |
|  | vgood | 0.321429 |


# Text representation of classifiers as-is

## PART

Decision list:

rules | predicted class
---|---
Persons = 2|unacc (525.0)
Safety = low|unacc (345.0)
Buying = vhigh AND Maint = high|unacc (46.0)
Maint = vhigh AND Buying = high|unacc (41.0)
Lug_boot = small AND Safety = med AND Buying != vhigh AND Buying != high AND Maint != vhigh AND Maint != high AND Doors != 2|acc (22.0)
Lug_boot = small AND Safety = med AND Buying != low AND Maint != med|unacc (43.0)
Buying = vhigh AND Maint != vhigh AND Safety != med AND Doors != 2|acc (35.0)
Buying = vhigh AND Maint = vhigh|unacc (32.0)
Safety = med AND Lug_boot = small AND Maint != high AND Doors != 2|unacc (16.0)
Buying = high AND Doors != 2 AND Doors != 3|acc (55.0)
Maint = vhigh AND Doors != 2 AND Doors != 3|acc (38.0)
Safety = med AND Lug_boot = big AND Buying != low AND Maint != low|acc (33.0)
Safety = med AND Lug_boot = big AND Maint != med AND Maint != low|acc (10.0)
Safety = med AND Lug_boot = big AND Buying != vhigh AND Buying = low|good (15.0)
Lug_boot = big AND Safety = med AND Buying = vhigh|acc (7.0)
Lug_boot = big AND Safety != med AND Buying != high AND Maint != vhigh AND Buying = low|vgood (22.0)
Safety = med AND Doors = 2 AND Buying != med AND Buying != low|unacc (11.0/1.0)
Buying = high AND Safety != med AND Lug_boot != small|acc (22.0)
Maint = vhigh AND Safety != med AND Lug_boot != small|acc (15.0)
Lug_boot = big AND Safety != med AND Maint != high AND Doors != 2|vgood (12.0)
Maint = vhigh AND Doors = 2|unacc (9.0/2.0)
Maint = high AND Doors != 2 AND Buying != low AND Safety != med|acc (18.0)
Maint = high AND Doors = 2 AND Persons != 4|unacc (9.0/4.0)
Maint = high AND Safety = med AND Buying = low|acc (9.0)
Buying = vhigh AND Maint != med|acc (11.0/1.0)
Maint = low AND Buying != high AND Lug_boot = small AND Persons != 4|good (7.0/3.0)
Buying = high AND Lug_boot != med|acc (8.0/2.0)
Maint = low AND Safety != med AND Lug_boot != small AND Doors != 2|vgood (9.0/2.0)
Maint = low AND Lug_boot != big AND Safety = med AND Doors != 3|good (12.0/4.0)
Maint = low AND Doors != 3|good (14.0/2.0)
Safety = med AND Buying != high AND Maint != low AND Buying != low AND Doors != 3 AND Persons = 4|acc (9.0/1.0)
Safety = med AND Buying != high AND Maint != low AND Buying != low AND Doors = 3|acc (8.0/3.0)
Buying != high AND Lug_boot = small AND Doors != 2 AND Maint != med|acc (10.0/1.0)
Safety = med AND Buying != high AND Doors != 2 AND Buying = low|good (10.0/4.0)
Buying != high AND Lug_boot != small AND Safety = med|acc (11.0/3.0)
Safety = med|unacc (9.0/4.0)
Lug_boot != small AND Doors != 2 AND Persons != 4|vgood (8.0)
Buying != low AND Lug_boot != small|acc (11.0/4.0)
Buying != low|acc (10.0/2.0)
Lug_boot = small|good (9.0/2.0)
|vgood (6.0/3.0)


## J48 Decision Tree

* Persons = 2: unacc (525.0)
* Persons != 2
	* Safety = low: unacc (345.0)
	* Safety != low
		* Buying = vhigh
			* Maint = high: unacc (46.0)
			* Maint != high
				* Maint = vhigh: unacc (39.0)
				* Maint != vhigh
					* Lug_boot = small
						* Safety = med: unacc (14.0)
						* Safety != med: acc (13.0/1.0)
					* Lug_boot != small
						* Lug_boot = med
							* Safety = med
								* Doors = 2: unacc (3.0)
								* Doors != 2: acc (12.0/2.0)
							* Safety != med: acc (15.0)
						* Lug_boot != med: acc (30.0)
		* Buying != vhigh
			* Buying = high
				* Maint = vhigh: unacc (41.0)
				* Maint != vhigh
					* Lug_boot = small
						* Safety = med: unacc (20.0)
						* Safety != med
							* Doors = 2
								* Persons = 4: acc (3.0)
								* Persons != 4: unacc (3.0)
							* Doors != 2: acc (14.0)
					* Lug_boot != small
						* Safety = med
							* Lug_boot = med
								* Doors = 2: unacc (4.0)
								* Doors != 2
									* Doors = 3
										* Persons = 4: unacc (3.0)
										* Persons != 4: acc (3.0)
									* Doors != 3: acc (11.0)
							* Lug_boot != med: acc (21.0)
						* Safety != med: acc (45.0)
			* Buying != high
				* Maint = vhigh
					* Lug_boot = small
						* Safety = med: unacc (14.0)
						* Safety != med: acc (15.0/2.0)
					* Lug_boot != small
						* Lug_boot = med
							* Safety = med
								* Doors = 2: unacc (3.0)
								* Doors != 2: acc (12.0/2.0)
							* Safety != med: acc (14.0)
						* Lug_boot != med: acc (31.0)
				* Maint != vhigh
					* Safety = med
						* Lug_boot = small
							* Maint = high
								* Buying = med: unacc (8.0)
								* Buying != med: acc (6.0/1.0)
							* Maint != high
								* Doors = 2: unacc (6.0/2.0)
								* Doors != 2: acc (22.0)
						* Lug_boot != small
							* Maint = high: acc (26.0/3.0)
							* Maint != high
								* Buying = med
									* Maint = med: acc (13.0)
									* Maint != med: good (13.0/3.0)
								* Buying != med
									* Lug_boot = med
										* Doors = 2: acc (4.0)
										* Doors != 2: good (12.0/2.0)
									* Lug_boot != med: good (15.0)
					* Safety != med
						* Lug_boot = small
							* Doors = 2
								* Persons = 4: acc (5.0/2.0)
								* Persons != 4: unacc (6.0)
							* Doors != 2
								* Maint = low: good (9.0)
								* Maint != low
									* Buying = med: acc (11.0)
									* Buying != med
										* Maint = high: acc (5.0)
										* Maint != high: good (6.0)
						* Lug_boot != small
							* Maint = high
								* Buying = med: acc (15.0)
								* Buying != med: vgood (14.0/2.0)
							* Maint != high
								* Lug_boot = med
									* Doors = 2: good (8.0/2.0)
									* Doors != 2: vgood (19.0/3.0)
								* Lug_boot != med: vgood (30.0)


## SimpleCart Decision Tree

	* Persons=(more)|(4)
		* Safety=(high)|(med)
			* Buying=(low)|(med)
				* Maint=(low)|(med)
					* Safety=(high)|(low)
						* Lug_boot=(big)|(med): vgood(46.0/11.0)
						* Lug_boot!=(big)|(med): good(17.0/11.0)
					* Safety!=(high)|(low)
						* Lug_boot=(big)|(med)
								* Buying=(low)|(vhigh)|(high): good(25.0/6.0)
								* Buying!=(low)|(vhigh)|(high)
									* Maint=(low)|(vhigh)|(high): good(10.0/3.0)
									* Maint!=(low)|(vhigh)|(high): acc(13.0/0.0)
						* Lug_boot!=(big)|(med): acc(24.0/4.0)
				* Maint!=(low)|(med)
					* Lug_boot=(big)|(med)
					* Maint=(high)
						* Buying=(low)
								* Safety=(high)|(low): vgood(12.0/2.0)
								* Safety!=(high)|(low): acc(12.0/0.0)
						* Buying!=(low): acc(26.0/3.0)
					* Maint!=(high): acc(55.0/5.0)
					* Lug_boot!=(big)|(med)
						* Safety=(high)|(low): acc(25.0/4.0)
						* Safety!=(high)|(low): unacc(23.0/5.0)
			* Buying!=(low)|(med)
				* Maint=(low)|(med)
					* Lug_boot=(big)|(med)
						* Doors=(5more)|(4): acc(62.0/0.0)
						* Doors!=(5more)|(4)
							* Safety=(high)|(low): acc(28.0/0.0)
							* Safety!=(high)|(low)
							* Lug_boot=(big): acc(13.0/0.0)
							* Lug_boot!=(big): unacc(10.0/4.0)
					* Lug_boot!=(big)|(med)
					* Safety=(high): acc(23.0/3.0)
					* Safety!=(high): unacc(27.0/0.0)
				* Maint!=(low)|(med)
						* Buying=(high)|(med)|(low)
							* Maint=(high)|(med)|(low)
							* Lug_boot=(big)|(med): acc(28.0/2.0)
							* Lug_boot!=(big)|(med): unacc(8.0/6.0)
							* Maint!=(high)|(med)|(low): unacc(41.0/0.0)
						* Buying!=(high)|(med)|(low): unacc(85.0/0.0)
		* Safety!=(high)|(med): unacc(345.0/0.0)
	* Persons!=(more)|(4): unacc(525.0/0.0)


