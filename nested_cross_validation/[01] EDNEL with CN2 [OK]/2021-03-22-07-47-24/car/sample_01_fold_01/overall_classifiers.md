# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Persons != 4 | unacc | 0.603276 |
| Persons != more | unacc | 0.602608 |
| Persons != 2 and Safety != low and Maint != vhigh and Buying != low and Buying != med and Lug_boot != small and Maint != high and Safety != med | acc | 0.046567 |
| Persons != 2 and Safety != low and Maint = vhigh and Buying != low and Buying = med | acc | 0.018777 |
| Persons != 2 and Safety != low and Maint = vhigh and Buying = low and Lug_boot != small | acc | 0.020388 |
| Persons != 2 and Safety != low and Maint != vhigh and Buying != low and Buying != med and Lug_boot != small and Maint != high and Safety = med and Lug_boot != med | acc | 0.021862 |
| Persons != 2 and Safety != low and Maint != vhigh and Buying != low and Buying != med and Lug_boot != small and Maint = high and Buying != vhigh | acc | 0.018936 |
| Persons != 2 and Safety != low and Maint != vhigh and Buying != low and Buying != med and Lug_boot = small and Safety != med and Maint != high | acc | 0.018320 |
| Persons != 2 and Safety != low and Maint != vhigh and Buying = low and Safety = med and Maint = high | acc | 0.017920 |
| Persons != 2 and Safety != low and Maint != vhigh and Buying != low and Buying = med and Maint != low and Maint != high and Safety = med | acc | 0.015524 |
| Persons != 2 and Safety != low and Maint != vhigh and Buying = low and Safety != med and Lug_boot != small | vgood | 0.018108 |
| Persons != 2 and Safety != low and Maint != vhigh and Buying != low and Buying != med and Lug_boot != small and Maint != high and Safety = med and Lug_boot = med and Doors != 2 | acc | 0.012052 |
| Persons != 2 and Safety != low and Maint != vhigh and Buying != low and Buying = med and Maint != low and Maint = high and Lug_boot = big | acc | 0.013072 |
| Persons != 2 and Safety != low and Maint != vhigh and Buying = low and Safety = med and Maint != high and Lug_boot != small | good | 0.011871 |
| Persons != 2 and Safety != low and Maint != vhigh and Buying != low and Buying = med and Maint != low and Maint = high and Lug_boot != big and Safety != med | acc | 0.009895 |
| Persons != 2 and Safety != low and Maint != vhigh and Buying = low and Safety = med and Maint != high and Lug_boot = small | acc | 0.009087 |
| Persons != 2 and Safety != low and Maint != vhigh and Buying = low and Safety != med and Lug_boot = small and Maint != high | good | 0.008140 |
| Persons != 2 and Safety != low and Maint != vhigh and Buying != low and Buying = med and Maint != low and Maint != high and Safety != med and Lug_boot != small | vgood | 0.007486 |
| Persons != 2 and Safety != low and Maint = vhigh and Buying = low and Lug_boot = small and Safety != med | acc | 0.005045 |
| Persons != 2 and Safety != low and Maint != vhigh and Buying != low and Buying = med and Maint = low and Safety = med and Lug_boot = small | acc | 0.004240 |
| Persons != 2 and Safety != low and Maint != vhigh and Buying != low and Buying = med and Maint = low and Safety = med and Lug_boot != small | good | 0.005552 |
| Persons != 2 and Safety != low and Maint != vhigh and Buying != low and Buying = med and Maint != low and Maint != high and Safety != med and Lug_boot = small | acc | 0.004240 |
| Persons != 2 and Safety != low and Maint != vhigh and Buying = low and Safety != med and Lug_boot = small and Maint = high | acc | 0.004240 |
| Persons != 2 and Safety != low and Maint != vhigh and Buying != low and Buying = med and Maint = low and Safety != med and Lug_boot != small | vgood | 0.006387 |
| Persons != 2 and Safety != low and Maint != vhigh and Buying != low and Buying = med and Maint = low and Safety != med and Lug_boot = small | good | 0.003433 |
| Persons = 4 and Safety = med and Buying = med and Maint != med and Lug_boot = med and Safety!=(high) and Doors = 4 | acc | 0.001103 |
| Persons = 4 and Safety = med and Buying = med and Maint != med and Lug_boot = med and Safety!=(high) and Doors = 5more | acc | 0.001103 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Persons = 2 | unacc | 0.529889 |
| Safety = low | unacc | 0.425031 |
| Buying = vhigh and Maint = vhigh | unacc | 0.093750 |
| Buying != low and Buying != med and Maint != vhigh and Lug_boot != small and Maint != high and Safety != med | acc | 0.167139 |
| Buying = vhigh and Maint = high | unacc | 0.095982 |
| Buying = high and Maint = vhigh | unacc | 0.091928 |
| Safety = med and Lug_boot = small and Buying = high | unacc | 0.051522 |
| Safety = med and Lug_boot = small and Buying != vhigh and Maint != vhigh and Doors != 2 and Maint != high | acc | 0.096154 |
| Safety = med and Lug_boot = small and Maint != high and Doors != 2 | unacc | 0.049383 |
| Safety = med and Lug_boot = small and Buying != low and Persons != 4 | unacc | 0.017857 |
| Safety = med and Lug_boot = big and Buying != low and Maint != low | acc | 0.210784 |
| Maint = vhigh and Doors != 2 and Doors != 3 | acc | 0.178571 |
| Buying = high and Doors != 2 and Doors != 3 | acc | 0.157068 |
| Safety = med and Lug_boot = big and Maint != med and Buying != med and Maint != low | acc | 0.069364 |
| Safety = med and Lug_boot = big and Buying != vhigh and Buying != high | good | 0.074906 |
| Lug_boot = big and Safety != med and Maint != vhigh and Maint != high | vgood | 0.112840 |
| Doors = 2 and Lug_boot = big and Buying != low | acc | 0.066667 |
| Doors = 2 and Safety = med and Buying != vhigh and Buying != high and Maint != vhigh and Maint != high and Persons = 4 | acc | 0.058824 |
| Doors = 2 and Safety = med and Buying != low and Buying != med | unacc | 0.047393 |
| Doors = 2 and Lug_boot != big and Persons != 4 and Lug_boot = small | unacc | 0.073733 |
| Safety = med and Maint = vhigh and Doors = 2 | unacc | 0.019512 |
| Safety = med and Maint = high and Buying = low | acc | 0.154639 |
| Safety = med and Maint = high and Doors != 2 and Persons != 4 | acc | 0.046512 |
| Safety != med and Lug_boot = small and Maint = high | acc | 0.154639 |
| Safety = med and Maint = high and Doors = 2 | unacc | 0.017647 |
| Buying = vhigh and Doors != 3 | acc | 0.185567 |
| Safety = med and Persons != 4 and Doors != 4 and Doors != 5more and Doors != 2 and Buying != low and Buying != med | acc | 0.070588 |
| Safety != med and Lug_boot = small and Buying != high and Buying != vhigh and Maint != vhigh and Buying != med | good | 0.111111 |
| Safety != med and Maint != low and Buying != low and Maint != med | acc | 0.285714 |
| Safety != med and Lug_boot = small and Maint != low | acc | 0.177215 |
| Safety != med and Maint = vhigh | acc | 0.084507 |
| Safety != med and Lug_boot = small and Buying = med | good | 0.083333 |
| Safety != med and Lug_boot != small and Doors != 2 and Doors != 3 | vgood | 0.291139 |
| Safety = med and Doors != 2 and Doors != 3 and Maint != high and Maint != med | good | 0.140000 |
| Safety = med and Persons != 4 and Doors = 2 | acc | 0.121212 |
| Safety = med and Persons != 4 and Maint != vhigh and Buying != med | good | 0.071429 |
| Safety = med and Persons != 4 and Maint = med | acc | 0.103448 |
| Safety = med and Persons = 4 and Doors = 3 and Lug_boot = med and Buying != low and Buying != med | unacc | 0.119048 |
| Safety = med and Persons = 4 and Maint != vhigh and Maint != high and Doors = 3 | acc | 0.192308 |
| Safety = med and Persons = 4 and Doors = 3 | unacc | 0.085714 |
| Maint = high and Lug_boot = med and Doors != 3 | acc | 0.181818 |
| Lug_boot = small and Doors = 3 | acc | 0.181818 |
| Lug_boot != small and Maint != vhigh and Lug_boot = med and Persons = 4 and Maint = low | good | 0.210526 |
| Lug_boot = small | unacc | 0.025000 |
| Maint = vhigh | acc | 0.133333 |
| Lug_boot = med and Persons = 4 and Buying = med | acc | 0.133333 |
| Safety = med | good | 0.166667 |
| Lug_boot = med and Doors = 2 and Buying = med | acc | 0.045455 |
| Maint != med and Persons != 4 | vgood | 0.355556 |
| Maint != high and Doors != 2 | vgood | 0.190476 |
| Maint = high | acc | 0.100000 |
|  | good | 0.666667 |


# Text representation of classifiers as-is

## PART

Decision list:

rules | predicted class
---|---
Persons = 2|unacc (523.0)
Safety = low|unacc (343.0)
Buying = vhigh AND Maint = vhigh|unacc (48.0)
Buying != low AND Buying != med AND Maint != vhigh AND Lug_boot != small AND Maint != high AND Safety != med|acc (59.0)
Buying = vhigh AND Maint = high|unacc (43.0)
Buying = high AND Maint = vhigh|unacc (41.0)
Safety = med AND Lug_boot = small AND Buying = high|unacc (22.0)
Safety = med AND Lug_boot = small AND Buying != vhigh AND Maint != vhigh AND Doors != 2 AND Maint != high|acc (20.0)
Safety = med AND Lug_boot = small AND Maint != high AND Doors != 2|unacc (20.0)
Safety = med AND Lug_boot = small AND Buying != low AND Persons != 4|unacc (7.0)
Safety = med AND Lug_boot = big AND Buying != low AND Maint != low|acc (43.0)
Maint = vhigh AND Doors != 2 AND Doors != 3|acc (35.0)
Buying = high AND Doors != 2 AND Doors != 3|acc (30.0)
Safety = med AND Lug_boot = big AND Maint != med AND Buying != med AND Maint != low|acc (12.0)
Safety = med AND Lug_boot = big AND Buying != vhigh AND Buying != high|good (20.0)
Lug_boot = big AND Safety != med AND Maint != vhigh AND Maint != high|vgood (29.0)
Doors = 2 AND Lug_boot = big AND Buying != low|acc (8.0)
Doors = 2 AND Safety = med AND Buying != vhigh AND Buying != high AND Maint != vhigh AND Maint != high AND Persons = 4|acc (7.0)
Doors = 2 AND Safety = med AND Buying != low AND Buying != med|unacc (10.0)
Doors = 2 AND Lug_boot != big AND Persons != 4 AND Lug_boot = small|unacc (16.0)
Safety = med AND Maint = vhigh AND Doors = 2|unacc (4.0)
Safety = med AND Maint = high AND Buying = low|acc (15.0)
Safety = med AND Maint = high AND Doors != 2 AND Persons != 4|acc (4.0)
Safety != med AND Lug_boot = small AND Maint = high|acc (15.0)
Safety = med AND Maint = high AND Doors = 2|unacc (3.0)
Buying = vhigh AND Doors != 3|acc (18.0)
Safety = med AND Persons != 4 AND Doors != 4 AND Doors != 5more AND Doors != 2 AND Buying != low AND Buying != med|acc (6.0)
Safety != med AND Lug_boot = small AND Buying != high AND Buying != vhigh AND Maint != vhigh AND Buying != med|good (14.0)
Safety != med AND Maint != low AND Buying != low AND Maint != med|acc (26.0)
Safety != med AND Lug_boot = small AND Maint != low|acc (14.0)
Safety != med AND Maint = vhigh|acc (6.0)
Safety != med AND Lug_boot = small AND Buying = med|good (6.0)
Safety != med AND Lug_boot != small AND Doors != 2 AND Doors != 3|vgood (23.0)
Safety = med AND Doors != 2 AND Doors != 3 AND Maint != high AND Maint != med|good (7.0)
Safety = med AND Persons != 4 AND Doors = 2|acc (4.0)
Safety = med AND Persons != 4 AND Maint != vhigh AND Buying != med|good (3.0)
Safety = med AND Persons != 4 AND Maint = med|acc (3.0)
Safety = med AND Persons = 4 AND Doors = 3 AND Lug_boot = med AND Buying != low AND Buying != med|unacc (5.0)
Safety = med AND Persons = 4 AND Maint != vhigh AND Maint != high AND Doors = 3|acc (5.0)
Safety = med AND Persons = 4 AND Doors = 3|unacc (3.0)
Maint = high AND Lug_boot = med AND Doors != 3|acc (4.0)
Lug_boot = small AND Doors = 3|acc (4.0)
Lug_boot != small AND Maint != vhigh AND Lug_boot = med AND Persons = 4 AND Maint = low|good (4.0)
Lug_boot = small|unacc (2.0/1.0)
Maint = vhigh|acc (2.0)
Lug_boot = med AND Persons = 4 AND Buying = med|acc (2.0)
Safety = med|good (2.0)
Lug_boot = med AND Doors = 2 AND Buying = med|acc (2.0/1.0)
Maint != med AND Persons != 4|vgood (4.0)
Maint != high AND Doors != 2|vgood (3.0/1.0)
Maint = high|acc (2.0/1.0)
|good (2.0)


## J48 Decision Tree

* Persons = 2: unacc (399.0)
* Persons != 2
	* Safety = low: unacc (263.0)
	* Safety != low
		* Maint = vhigh
			* Buying = low
				* Lug_boot = small
					* Safety = med: unacc (6.0)
					* Safety != med: acc (6.0/1.0)
				* Lug_boot != small: acc (26.0/2.0)
			* Buying != low
				* Buying = med: acc (21.0/6.0)
				* Buying != med: unacc (62.0)
		* Maint != vhigh
			* Buying = low
				* Safety = med
					* Maint = high: acc (21.0)
					* Maint != high
						* Lug_boot = small: acc (9.0/1.0)
						* Lug_boot != small: good (20.0/2.0)
				* Safety != med
					* Lug_boot = small
						* Maint = high: acc (5.0/1.0)
						* Maint != high: good (12.0/1.0)
					* Lug_boot != small: vgood (32.0/5.0)
			* Buying != low
				* Buying = med
					* Maint = low
						* Safety = med
							* Lug_boot = small: acc (5.0/1.0)
							* Lug_boot != small: good (8.0/2.0)
						* Safety != med
							* Lug_boot = small: good (6.0/1.0)
							* Lug_boot != small: vgood (10.0/2.0)
					* Maint != low
						* Maint = high
							* Lug_boot = big: acc (11.0)
							* Lug_boot != big
								* Safety = med: unacc (9.0/4.0)
								* Safety != med: acc (12.0/1.0)
						* Maint != high
							* Safety = med: acc (19.0)
							* Safety != med
								* Lug_boot = small: acc (6.0/1.0)
								* Lug_boot != small: vgood (10.0/1.0)
				* Buying != med
					* Lug_boot = small
						* Safety = med: unacc (31.0)
						* Safety != med
							* Maint = high: unacc (12.0/5.0)
							* Maint != high: acc (25.0/4.0)
					* Lug_boot != small
						* Maint = high
							* Buying = vhigh: unacc (14.0)
							* Buying != vhigh: acc (23.0/2.0)
						* Maint != high
							* Safety = med
								* Lug_boot = med
									* Doors = 2: unacc (5.0)
									* Doors != 2: acc (15.0/3.0)
								* Lug_boot != med: acc (18.0)
							* Safety != med: acc (44.0)


## SimpleCart Decision Tree

	* Persons=(more)|(4)
		* Safety=(high)|(med)
			* Buying=(low)|(med)
				* Maint=(low)|(med)
					* Safety=(high)|(low)
						* Lug_boot=(big)|(med)
							* Doors=(5more)|(4): vgood(29.0/0.0)
							* Doors!=(5more)|(4)
								* Lug_boot=(big)|(small): vgood(15.0/0.0)
								* Lug_boot!=(big)|(small)
									* Persons=(more)|(2): vgood(4.0/3.0)
									* Persons!=(more)|(2): good(6.0/1.0)
						* Lug_boot!=(big)|(med)
								* Buying=(low)|(vhigh)|(high)
									* Doors=(5more)|(4)|(3): good(12.0/0.0)
									* Doors!=(5more)|(4)|(3): unacc(2.0/2.0)
								* Buying!=(low)|(vhigh)|(high)
									* Maint=(low)|(vhigh)|(high): good(6.0/1.0)
									* Maint!=(low)|(vhigh)|(high): acc(6.0/1.0)
					* Safety!=(high)|(low)
						* Lug_boot=(big)|(med)
								* Buying=(low)|(vhigh)|(high)
								* Lug_boot=(big)|(small): good(15.0/0.0)
								* Lug_boot!=(big)|(small)
									* Doors=(5more)|(4): good(6.0/0.0)
									* Doors!=(5more)|(4): acc(5.0/1.0)
								* Buying!=(low)|(vhigh)|(high)
							* Maint=(low): good(10.0/2.0)
							* Maint!=(low): acc(14.0/0.0)
						* Lug_boot!=(big)|(med)
								* Doors=(5more)|(4)|(3): acc(20.0/0.0)
								* Doors!=(5more)|(4)|(3): acc(4.0/3.0)
				* Maint!=(low)|(med)
					* Lug_boot=(big)|(med)
					* Safety=(high)
						* Buying=(low)
									* Maint=(high)|(med)|(low)
									* Doors=(5more)|(4): vgood(8.0/0.0)
									* Doors!=(5more)|(4): acc(3.0/3.0)
									* Maint!=(high)|(med)|(low): acc(14.0/0.0)
						* Buying!=(low): acc(30.0/0.0)
					* Safety!=(high)
							* Doors=(5more)|(4): acc(32.0/0.0)
							* Doors!=(5more)|(4)
							* Lug_boot=(big): acc(14.0/0.0)
							* Lug_boot!=(big)
								* Buying=(low): acc(5.0/2.0)
								* Buying!=(low)
											* Doors=(3)|(4)|(5more): unacc(2.0/2.0)
											* Doors!=(3)|(4)|(5more): unacc(4.0/0.0)
					* Lug_boot!=(big)|(med)
						* Safety=(high)|(low)
								* Doors=(5more)|(4)|(3): acc(19.0/0.0)
								* Doors!=(5more)|(4)|(3)
								* Persons=(more)|(2): unacc(4.0/0.0)
								* Persons!=(more)|(2): acc(4.0/0.0)
						* Safety!=(high)|(low)
								* Maint=(high)|(med)|(low)
									* Buying=(low)|(vhigh)|(high): acc(7.0/1.0)
									* Buying!=(low)|(vhigh)|(high): unacc(4.0/0.0)
								* Maint!=(high)|(med)|(low): unacc(12.0/0.0)
			* Buying!=(low)|(med)
				* Maint=(low)|(med)
					* Lug_boot=(big)|(med)
						* Safety=(high)|(low): acc(59.0/0.0)
						* Safety!=(high)|(low)
						* Lug_boot=(big): acc(27.0/0.0)
						* Lug_boot!=(big)
								* Doors=(5more)|(4): acc(14.0/0.0)
								* Doors!=(5more)|(4)
								* Persons=(more): acc(4.0/2.0)
								* Persons!=(more): unacc(8.0/0.0)
					* Lug_boot!=(big)|(med)
						* Safety=(high)|(low)
								* Doors=(5more)|(4)|(3): acc(22.0/0.0)
								* Doors!=(5more)|(4)|(3)
								* Persons=(more)|(2): unacc(4.0/0.0)
								* Persons!=(more)|(2): acc(4.0/0.0)
						* Safety!=(high)|(low): unacc(29.0/0.0)
				* Maint!=(low)|(med)
				* Buying=(high)
							* Maint=(high)|(med)|(low)
							* Lug_boot=(big)|(med)
								* Doors=(5more)|(4): acc(14.0/0.0)
								* Doors!=(5more)|(4)
									* Safety=(high)|(low): acc(8.0/0.0)
									* Safety!=(high)|(low): acc(4.0/3.0)
							* Lug_boot!=(big)|(med)
							* Safety=(high): acc(6.0/1.0)
							* Safety!=(high): unacc(8.0/0.0)
							* Maint!=(high)|(med)|(low): unacc(41.0/0.0)
				* Buying!=(high): unacc(91.0/0.0)
		* Safety!=(high)|(med): unacc(343.0/0.0)
	* Persons!=(more)|(4): unacc(523.0/0.0)


