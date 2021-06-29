# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Persons != 4 | unacc | 0.607497 |
| Persons != more | unacc | 0.600157 |
| Safety = med and Persons = more and Lug_boot = big | acc | 0.018687 |
| Safety = med and Persons = 4 and Lug_boot = big | acc | 0.018226 |
| Safety = high and Persons = 4 and Buying = low and Maint = vhigh | acc | 0.009844 |
| Safety = high and Persons = 4 and Buying = vhigh and Maint = low | acc | 0.009844 |
| Safety = high and Persons = more and Buying = med and Maint = high | acc | 0.008285 |
| Safety = high and Persons = 4 and Buying = high and Maint = high | acc | 0.009031 |
| Safety = high and Persons = more and Buying = med and Maint = vhigh | acc | 0.008285 |
| Safety = high and Persons = more and Buying = high and Maint = low | acc | 0.008285 |
| Safety = high and Persons = 4 and Buying = vhigh and Maint = med | acc | 0.009031 |
| Safety = high and Persons = more and Buying = vhigh and Maint = low | acc | 0.008217 |
| Safety = high and Persons = 4 and Buying = med and Maint = high | acc | 0.008217 |
| Safety = high and Persons = 4 and Buying = high and Maint = med | acc | 0.008217 |
| Safety = high and Persons = 4 and Buying = med and Maint = vhigh | acc | 0.008217 |
| Safety = high and Persons = more and Buying = high and Maint = high | acc | 0.007476 |
| Safety = high and Persons = more and Buying = high and Maint = med | acc | 0.007476 |
| Safety = high and Persons = 4 and Buying = high and Maint = low | acc | 0.007401 |
| Safety = med and Persons = 4 and Lug_boot = small and Buying = low | acc | 0.005565 |
| Safety = med and Persons = more and Lug_boot = med and Buying = high | acc | 0.004778 |
| Safety = high and Persons = more and Buying = vhigh and Maint = med | acc | 0.006667 |
| Safety = med and Persons = 4 and Lug_boot = med and Doors = 5more | acc | 0.005889 |
| Safety = high and Persons = more and Buying = low | vgood | 0.004856 |
| Safety = med and Persons = 4 and Lug_boot = med and Doors = 4 | acc | 0.004463 |
| Safety = med and Persons = more and Lug_boot = med and Buying = med | acc | 0.005141 |
| Safety = med and Persons = more and Lug_boot = med and Buying = low | acc | 0.002900 |
| Safety = high and Persons = more and Buying = med and Maint = med | vgood | 0.002730 |
| Safety = high and Persons = 4 and Buying = med and Maint = med | acc | 0.002486 |
| Safety = high and Persons = more and Buying = med and Maint = low | vgood | 0.002406 |
| Safety = med and Persons = 4 and Lug_boot = med and Doors = 3 and Buying = low | acc | 0.001861 |
| Persons = 4 and Safety = med and Buying = med and Maint = med and Safety!=(high) and Lug_boot != med and Doors != 3 and Persons != 2 | acc | 0.004946 |
| Safety = med and Persons = more and Lug_boot = med and Buying = vhigh and Maint = low | acc | 0.001861 |
| Safety = med and Persons = more and Lug_boot = med and Buying = vhigh and Maint = med | acc | 0.001861 |
| Safety = high and Persons = 4 and Buying = med and Maint = low | good | 0.001524 |
| Safety = high and Persons = 4 and Buying = low and Maint = low | vgood | 0.002189 |
| Safety = high and Persons = 4 and Buying = low and Maint = high | vgood | 0.001858 |
| Persons = 4 and Safety = med and Buying = med and Maint = med and Safety!=(high) and Lug_boot = med and Buying != high and Maint != high | acc | 0.003303 |
| Safety = high and Persons = 4 and Buying = low and Maint = med | vgood | 0.001673 |
| Persons = 4 and Safety = med and Buying = med and Maint = med and Safety!=(high) and Lug_boot != med and Doors = 3 | acc | 0.000828 |

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
| Safety = med and Lug_boot = small and Maint != high and Buying != med and Doors != 2 | unacc | 0.037915 |
| Buying = high and Doors != 2 and Doors != 3 | acc | 0.257009 |
| Maint = vhigh and Doors != 2 and Doors != 3 | acc | 0.192893 |
| Safety = med and Lug_boot = small and Doors = 2 and Persons != 4 | unacc | 0.018809 |
| Safety = med and Lug_boot = big and Maint = high | acc | 0.100000 |
| Safety = med and Buying = high and Lug_boot = big | acc | 0.037736 |
| Safety = med and Buying = high and Persons = 4 | unacc | 0.020270 |
| Safety = med and Buying = vhigh and Lug_boot = big | acc | 0.092593 |
| Safety = med and Lug_boot = big and Maint != vhigh and Buying != med | good | 0.057915 |
| Safety = med and Maint != low and Lug_boot = big | acc | 0.095890 |
| Lug_boot = big and Safety != med and Buying != high and Maint != vhigh and Buying != vhigh and Maint != high | vgood | 0.121457 |
| Doors = 2 and Lug_boot = big and Safety != med and Buying != low | acc | 0.105263 |
| Doors = 2 and Lug_boot != big and Persons = 4 and Safety != med and Buying != low and Maint != low | acc | 0.089286 |
| Doors != 2 and Maint != low and Buying != low and Safety != med and Maint != med | acc | 0.209302 |
| Doors = 2 and Lug_boot != big and Safety = med and Buying != vhigh and Maint != vhigh and Buying != high and Maint != high | acc | 0.089286 |
| Doors = 2 and Lug_boot != big and Safety = med and Buying != low | unacc | 0.054217 |
| Maint = vhigh and Safety != med and Lug_boot != small | acc | 0.088235 |
| Buying = high and Lug_boot != small | acc | 0.138889 |
| Maint = vhigh and Doors = 2 and Persons = 4 | unacc | 0.009950 |
| Lug_boot = big and Buying != med | vgood | 0.061069 |
| Buying = vhigh and Doors != 3 and Lug_boot != small | acc | 0.107527 |
| Maint = high and Doors != 2 and Safety = med and Doors != 3 | acc | 0.097826 |
| Maint = vhigh and Doors = 2 | unacc | 0.020833 |
| Maint = high and Buying != low and Lug_boot != small | acc | 0.016461 |
| Maint = high and Buying = low and Lug_boot = small and Doors != 2 | acc | 0.069767 |
| Doors = 2 and Lug_boot != small and Maint != high and Maint != med | good | 0.068493 |
| Doors = 2 and Persons = 4 and Maint != med and Buying = low | acc | 0.029221 |
| Doors = 2 and Lug_boot != small and Maint != high | good | 0.020202 |
| Doors = 2 and Persons != 4 and Lug_boot = small | unacc | 0.102041 |
| Safety = med and Doors != 3 and Maint = low | good | 0.166667 |
| Lug_boot != med and Buying != high and Maint != vhigh and Buying = low | good | 0.166667 |
| Safety = med and Buying = vhigh and Persons = 4 | unacc | 0.029412 |
| Maint = vhigh and Persons = 4 | unacc | 0.019900 |
| Safety = med and Lug_boot = med and Maint != high and Buying != low and Maint != low | acc | 0.139535 |
| Doors = 2 | acc | 0.119048 |
| Safety = med and Doors = 3 and Lug_boot = med and Persons = 4 | acc | 0.080000 |
| Lug_boot != med and Maint != low | acc | 0.195652 |
| Safety = med and Maint = med | good | 0.156250 |
| Lug_boot != med and Persons = 4 | good | 0.129032 |
| Doors != 3 and Maint != low | vgood | 0.440000 |
| Doors != 3 and Persons = 4 | vgood | 0.222222 |
| Maint != low and Persons = 4 | acc | 0.095238 |
| Safety = med and Buying = med | good | 0.121212 |
| Safety = med and Maint = low | acc | 0.045455 |
| Safety != med and Lug_boot != small and Persons != 4 | vgood | 0.357143 |
| Maint = low and Buying = med | good | 0.428571 |
| Maint = low | acc | 0.166667 |
|  | acc | 0.400000 |


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
Safety = med AND Lug_boot = small AND Maint != high AND Buying != med AND Doors != 2|unacc (16.0)
Buying = high AND Doors != 2 AND Doors != 3|acc (55.0)
Maint = vhigh AND Doors != 2 AND Doors != 3|acc (38.0)
Safety = med AND Lug_boot = small AND Doors = 2 AND Persons != 4|unacc (6.0)
Safety = med AND Lug_boot = big AND Maint = high|acc (17.0)
Safety = med AND Buying = high AND Lug_boot = big|acc (6.0)
Safety = med AND Buying = high AND Persons = 4|unacc (6.0)
Safety = med AND Buying = vhigh AND Lug_boot = big|acc (15.0)
Safety = med AND Lug_boot = big AND Maint != vhigh AND Buying != med|good (15.0)
Safety = med AND Maint != low AND Lug_boot = big|acc (14.0)
Lug_boot = big AND Safety != med AND Buying != high AND Maint != vhigh AND Buying != vhigh AND Maint != high|vgood (30.0)
Doors = 2 AND Lug_boot = big AND Safety != med AND Buying != low|acc (12.0)
Doors = 2 AND Lug_boot != big AND Persons = 4 AND Safety != med AND Buying != low AND Maint != low|acc (10.0)
Doors != 2 AND Maint != low AND Buying != low AND Safety != med AND Maint != med|acc (27.0)
Doors = 2 AND Lug_boot != big AND Safety = med AND Buying != vhigh AND Maint != vhigh AND Buying != high AND Maint != high|acc (10.0)
Doors = 2 AND Lug_boot != big AND Safety = med AND Buying != low|unacc (9.0)
Maint = vhigh AND Safety != med AND Lug_boot != small|acc (9.0)
Buying = high AND Lug_boot != small|acc (15.0)
Maint = vhigh AND Doors = 2 AND Persons = 4|unacc (3.0/1.0)
Lug_boot = big AND Buying != med|vgood (8.0)
Buying = vhigh AND Doors != 3 AND Lug_boot != small|acc (10.0)
Maint = high AND Doors != 2 AND Safety = med AND Doors != 3|acc (9.0)
Maint = vhigh AND Doors = 2|unacc (3.0)
Maint = high AND Buying != low AND Lug_boot != small|acc (3.0/1.0)
Maint = high AND Buying = low AND Lug_boot = small AND Doors != 2|acc (6.0)
Doors = 2 AND Lug_boot != small AND Maint != high AND Maint != med|good (5.0)
Doors = 2 AND Persons = 4 AND Maint != med AND Buying = low|acc (3.0/1.0)
Doors = 2 AND Lug_boot != small AND Maint != high|good (3.0/1.0)
Doors = 2 AND Persons != 4 AND Lug_boot = small|unacc (10.0)
Safety = med AND Doors != 3 AND Maint = low|good (11.0)
Lug_boot != med AND Buying != high AND Maint != vhigh AND Buying = low|good (10.0)
Safety = med AND Buying = vhigh AND Persons = 4|unacc (2.0)
Maint = vhigh AND Persons = 4|unacc (3.0/1.0)
Safety = med AND Lug_boot = med AND Maint != high AND Buying != low AND Maint != low|acc (6.0)
Doors = 2|acc (4.0)
Safety = med AND Doors = 3 AND Lug_boot = med AND Persons = 4|acc (4.0)
Lug_boot != med AND Maint != low|acc (8.0)
Safety = med AND Maint = med|good (5.0)
Lug_boot != med AND Persons = 4|good (4.0)
Doors != 3 AND Maint != low|vgood (11.0)
Doors != 3 AND Persons = 4|vgood (4.0)
Maint != low AND Persons = 4|acc (2.0)
Safety = med AND Buying = med|good (2.0)
Safety = med AND Maint = low|acc (2.0/1.0)
Safety != med AND Lug_boot != small AND Persons != 4|vgood (5.0)
Maint = low AND Buying = med|good (3.0)
Maint = low|acc (2.0/1.0)
|acc (2.0)


## J48 Decision Tree

* Safety = low: unacc (415.0)
* Safety = med
	* Persons = 2: unacc (134.0)
	* Persons = 4
		* Lug_boot = small
			* Buying = vhigh: unacc (10.0)
			* Buying = high: unacc (11.0)
			* Buying = med: unacc (12.0/6.0)
			* Buying = low: acc (9.0/3.0)
		* Lug_boot = med
			* Doors = 2: unacc (9.0/3.0)
			* Doors = 3
				* Buying = vhigh: unacc (2.0)
				* Buying = high: unacc (4.0)
				* Buying = med: unacc (4.0/2.0)
				* Buying = low: acc (3.0/1.0)
			* Doors = 4: acc (14.0/6.0)
			* Doors = 5more: acc (10.0/1.0)
		* Lug_boot = big: acc (41.0/14.0)
	* Persons = more
		* Lug_boot = small: unacc (50.0/10.0)
		* Lug_boot = med
			* Buying = vhigh
				* Maint = vhigh: unacc (2.0)
				* Maint = high: unacc (4.0)
				* Maint = med: acc (3.0/1.0)
				* Maint = low: acc (4.0/1.0)
			* Buying = high: acc (10.0/4.0)
			* Buying = med: acc (12.0/4.0)
			* Buying = low: acc (12.0/6.0)
		* Lug_boot = big: acc (49.0/18.0)
* Safety = high
	* Persons = 2: unacc (149.0)
	* Persons = 4
		* Buying = vhigh
			* Maint = vhigh: unacc (9.0)
			* Maint = high: unacc (9.0)
			* Maint = med: acc (9.0)
			* Maint = low: acc (10.0)
		* Buying = high
			* Maint = vhigh: unacc (10.0)
			* Maint = high: acc (10.0)
			* Maint = med: acc (9.0)
			* Maint = low: acc (8.0)
		* Buying = med
			* Maint = vhigh: acc (7.0)
			* Maint = high: acc (8.0)
			* Maint = med: acc (11.0/5.0)
			* Maint = low: good (7.0/3.0)
		* Buying = low
			* Maint = vhigh: acc (8.0)
			* Maint = high: vgood (6.0/2.0)
			* Maint = med: vgood (9.0/4.0)
			* Maint = low: vgood (9.0/4.0)
	* Persons = more
		* Buying = vhigh
			* Maint = vhigh: unacc (4.0)
			* Maint = high: unacc (8.0)
			* Maint = med: acc (8.0/1.0)
			* Maint = low: acc (8.0)
		* Buying = high
			* Maint = vhigh: unacc (7.0)
			* Maint = high: acc (9.0/1.0)
			* Maint = med: acc (10.0/1.0)
			* Maint = low: acc (11.0/1.0)
		* Buying = med
			* Maint = vhigh: acc (10.0/1.0)
			* Maint = high: acc (8.0/1.0)
			* Maint = med: vgood (9.0/3.0)
			* Maint = low: vgood (8.0/3.0)
		* Buying = low: vgood (30.0/17.0)


## SimpleCart Decision Tree

	* Persons=(more)|(4)
		* Safety=(high)|(med)
			* Buying=(low)|(med)
				* Maint=(low)|(med)
				* Safety=(high)
						* Lug_boot=(big)|(med)
							* Lug_boot=(big)|(small): vgood(30.0/0.0)
							* Lug_boot!=(big)|(small)
								* Doors=(5more)|(4): vgood(14.0/0.0)
								* Doors!=(5more)|(4)
								* Buying=(low): good(4.0/0.0)
								* Buying!=(low)
											* Maint=(low)|(vhigh)|(high)
												* Doors=(3)|(4)|(5more): vgood(1.0/1.0)
												* Doors!=(3)|(4)|(5more): good(2.0/0.0)
											* Maint!=(low)|(vhigh)|(high)
												* Doors=(3)|(4)|(5more): acc(1.0/1.0)
												* Doors!=(3)|(4)|(5more): acc(2.0/0.0)
						* Lug_boot!=(big)|(med)
						* Buying=(low)
									* Doors=(5more)|(4)|(3): good(9.0/0.0)
									* Doors!=(5more)|(4)|(3)
									* Persons=(more)|(2): unacc(2.0/0.0)
									* Persons!=(more)|(2): good(2.0/0.0)
						* Buying!=(low)
							* Maint=(low): good(5.0/1.0)
							* Maint!=(low)
										* Doors=(5more)|(4)|(3): acc(6.0/0.0)
										* Doors!=(5more)|(4)|(3): unacc(1.0/1.0)
				* Safety!=(high)
						* Lug_boot=(big)|(med)
								* Buying=(low)|(vhigh)|(high)
								* Doors=(5more)|(4): good(15.0/0.0)
								* Doors!=(5more)|(4)
									* Lug_boot=(big)|(small): good(8.0/0.0)
									* Lug_boot!=(big)|(small)
											* Doors=(3)|(4)|(5more)
											* Persons=(more)|(2): good(2.0/0.0)
											* Persons!=(more)|(2): acc(2.0/0.0)
											* Doors!=(3)|(4)|(5more): acc(4.0/0.0)
								* Buying!=(low)|(vhigh)|(high)
									* Maint=(low)|(vhigh)|(high)
									* Doors=(5more)|(4): good(7.0/0.0)
									* Doors!=(5more)|(4)
										* Lug_boot=(big)|(small): good(4.0/0.0)
										* Lug_boot!=(big)|(small)
												* Doors=(3)|(4)|(5more): acc(1.0/1.0)
												* Doors!=(3)|(4)|(5more): acc(2.0/0.0)
									* Maint!=(low)|(vhigh)|(high): acc(13.0/0.0)
						* Lug_boot!=(big)|(med)
								* Doors=(5more)|(4)|(3): acc(22.0/0.0)
								* Doors!=(5more)|(4)|(3)
								* Persons=(more)|(2): unacc(4.0/0.0)
								* Persons!=(more)|(2): acc(2.0/0.0)
				* Maint!=(low)|(med)
					* Lug_boot=(big)|(med)
					* Maint=(high)
						* Buying=(low)
								* Safety=(high)|(low)
									* Lug_boot=(big)|(small): vgood(8.0/0.0)
									* Lug_boot!=(big)|(small)
										* Doors=(5more)|(4): vgood(3.0/0.0)
										* Doors!=(5more)|(4): acc(2.0/1.0)
								* Safety!=(high)|(low): acc(12.0/0.0)
						* Buying!=(low)
								* Doors=(5more)|(4): acc(15.0/0.0)
								* Doors!=(5more)|(4)
									* Safety=(high)|(low): acc(8.0/0.0)
									* Safety!=(high)|(low)
									* Lug_boot=(big): acc(2.0/0.0)
									* Lug_boot!=(big)
												* Doors=(3)|(4)|(5more): unacc(1.0/1.0)
												* Doors!=(3)|(4)|(5more): unacc(2.0/0.0)
					* Maint!=(high)
							* Doors=(5more)|(4): acc(31.0/0.0)
							* Doors!=(5more)|(4)
								* Lug_boot=(big)|(small): acc(15.0/0.0)
								* Lug_boot!=(big)|(small)
									* Safety=(high)|(low): acc(7.0/0.0)
									* Safety!=(high)|(low)
									* Persons=(more): acc(2.0/1.0)
									* Persons!=(more): unacc(4.0/0.0)
					* Lug_boot!=(big)|(med)
						* Safety=(high)|(low)
								* Doors=(5more)|(4)|(3): acc(21.0/0.0)
								* Doors!=(5more)|(4)|(3)
								* Persons=(more)|(2): unacc(4.0/0.0)
								* Persons!=(more)|(2): acc(4.0/0.0)
						* Safety!=(high)|(low)
						* Buying=(low)
							* Maint=(high)
										* Doors=(5more)|(4)|(3): acc(4.0/0.0)
										* Doors!=(5more)|(4)|(3): unacc(1.0/1.0)
							* Maint!=(high): unacc(7.0/0.0)
						* Buying!=(low): unacc(15.0/0.0)
			* Buying!=(low)|(med)
				* Maint=(low)|(med)
					* Lug_boot=(big)|(med)
						* Doors=(5more)|(4): acc(63.0/0.0)
						* Doors!=(5more)|(4)
							* Safety=(high)|(low): acc(28.0/0.0)
							* Safety!=(high)|(low)
							* Lug_boot=(big): acc(13.0/0.0)
							* Lug_boot!=(big)
									* Persons=(more)|(2)
											* Doors=(3)|(4)|(5more): acc(4.0/0.0)
											* Doors!=(3)|(4)|(5more): unacc(3.0/0.0)
									* Persons!=(more)|(2): unacc(7.0/0.0)
					* Lug_boot!=(big)|(med)
					* Safety=(high)
								* Doors=(5more)|(4)|(3): acc(20.0/0.0)
								* Doors!=(5more)|(4)|(3)
								* Persons=(more)|(2): unacc(3.0/0.0)
								* Persons!=(more)|(2): acc(3.0/0.0)
					* Safety!=(high): unacc(27.0/0.0)
				* Maint!=(low)|(med)
				* Buying=(high)
							* Maint=(high)|(med)|(low)
							* Lug_boot=(big)|(med)
								* Lug_boot=(big)|(small): acc(16.0/0.0)
								* Lug_boot!=(big)|(small)
									* Safety=(high)|(low): acc(7.0/0.0)
									* Safety!=(high)|(low)
										* Doors=(5more)|(4): acc(3.0/0.0)
										* Doors!=(5more)|(4): unacc(2.0/1.0)
							* Lug_boot!=(big)|(med)
								* Safety=(high)|(low)
										* Doors=(5more)|(4)|(3): acc(5.0/0.0)
										* Doors!=(5more)|(4)|(3): unacc(1.0/1.0)
								* Safety!=(high)|(low): unacc(7.0/0.0)
							* Maint!=(high)|(med)|(low): unacc(41.0/0.0)
				* Buying!=(high): unacc(85.0/0.0)
		* Safety!=(high)|(med): unacc(345.0/0.0)
	* Persons!=(more)|(4): unacc(525.0/0.0)


