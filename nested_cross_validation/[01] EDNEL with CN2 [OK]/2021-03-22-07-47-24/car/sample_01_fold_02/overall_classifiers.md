# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Safety != high | unacc | 0.614024 |
| Safety = high and Persons = 2 | unacc | 0.273865 |
| Safety = med and Persons = more and Lug_boot = big | acc | 0.018381 |
| Safety = med and Persons = more and Lug_boot = med | acc | 0.014081 |
| Safety = med and Persons = 4 and Buying = med | acc | 0.013214 |
| Safety = med and Persons = 4 and Buying = low | acc | 0.014986 |
| Safety != med | unacc | 0.592317 |
| Safety = high and Persons = more and Buying = high | acc | 0.015635 |
| Safety = high and Persons = 4 and Buying = med | acc | 0.013908 |
| Safety = high and Persons = 4 and Buying = high and Maint = high | acc | 0.009836 |
| Safety = high and Persons = more and Buying = med and Maint = vhigh | acc | 0.009024 |
| Safety = high and Persons = 4 and Buying = vhigh and Maint = low | acc | 0.009024 |
| Safety = high and Persons = 4 and Buying = high and Maint = low | acc | 0.009024 |
| Safety = high and Persons = 4 and Buying = low and Maint = vhigh | acc | 0.008210 |
| Safety = high and Persons = 4 and Buying = high and Maint = med | acc | 0.008210 |
| Safety = med and Persons = 4 and Buying = high and Lug_boot = big | acc | 0.005884 |
| Safety = high and Persons = more and Buying = med and Maint = high | acc | 0.008210 |
| Safety = high and Persons = 4 and Buying = vhigh and Maint = med | acc | 0.008210 |
| Safety = high and Persons = more and Buying = low | vgood | 0.004977 |
| Safety = high and Persons = more and Buying = med and Maint = low | vgood | 0.003632 |
| Safety = high and Persons = more and Buying = med and Maint = med | vgood | 0.002730 |
| Safety = high and Persons = 4 and Buying = low and Maint = high | acc | 0.002483 |
| Safety = high and Persons = 4 and Buying = low and Maint = low | good | 0.002191 |
| Safety = high and Persons = 4 and Buying = low and Maint = med | vgood | 0.002189 |
| Safety = med and Persons = 4 and Buying != med and Maint = med and Safety!=(high) and Lug_boot = med and Lug_boot != small and Doors = 5more | acc | 0.001103 |
| Safety = med and Persons = 4 and Buying != med and Maint = med and Safety!=(high) and Lug_boot = med and Lug_boot != small and Doors = 4 | acc | 0.000414 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Safety = low | unacc | 0.529412 |
| Persons = 2 | unacc | 0.417817 |
| Buying != low and Buying != med and Maint = vhigh | unacc | 0.165468 |
| Buying = vhigh and Maint = high | unacc | 0.088409 |
| Safety != med and Lug_boot = small and Doors != 2 and Buying != low | acc | 0.157014 |
| Lug_boot = small and Safety = med and Buying != high and Maint != vhigh and Buying != vhigh and Maint != high | acc | 0.090936 |
| Lug_boot = small and Safety = med and Buying != low | unacc | 0.121951 |
| Safety = med and Lug_boot = small and Maint = vhigh | unacc | 0.019802 |
| Safety = med and Lug_boot = big and Buying != low and Maint != low | acc | 0.211340 |
| Safety = med and Lug_boot = big and Maint != med and Buying != med and Buying != low | acc | 0.094675 |
| Safety != med and Lug_boot != small and Buying = high | acc | 0.219388 |
| Safety = med and Lug_boot = big and Maint != vhigh and Maint != high | good | 0.072165 |
| Safety = med and Doors = 2 and Buying != low | unacc | 0.040313 |
| Maint = vhigh | acc | 0.287507 |
| Buying = vhigh | acc | 0.236128 |
| Maint = high and Safety = med | acc | 0.188088 |
| Lug_boot = big and Maint != high | vgood | 0.197183 |
| Buying != high and Maint = high and Buying = med | acc | 0.143417 |
| Buying != high and Lug_boot != big and Maint != high and Lug_boot = small | good | 0.113422 |
| Buying != high and Safety = med and Maint != med | good | 0.049975 |
| Buying = high | acc | 0.091629 |
| Lug_boot != small and Safety = med and Buying != med | good | 0.018275 |
| Lug_boot != small and Safety != med and Doors != 2 and Doors != 3 | vgood | 0.278481 |
| Maint != low and Lug_boot != small and Buying != med | vgood | 0.036735 |
| Maint != low | acc | 0.391604 |
|  | good | 0.200000 |


# Text representation of classifiers as-is

## PART

Decision list:

rules | predicted class
---|---
Safety = low|unacc (522.0)
Persons = 2|unacc (333.0)
Buying != low AND Buying != med AND Maint = vhigh|unacc (92.0)
Buying = vhigh AND Maint = high|unacc (45.0)
Safety != med AND Lug_boot = small AND Doors != 2 AND Buying != low|acc (46.0/3.0)
Lug_boot = small AND Safety = med AND Buying != high AND Maint != vhigh AND Buying != vhigh AND Maint != high|acc (29.0/4.0)
Lug_boot = small AND Safety = med AND Buying != low|unacc (53.0)
Safety = med AND Lug_boot = small AND Maint = vhigh|unacc (8.0)
Safety = med AND Lug_boot = big AND Buying != low AND Maint != low|acc (41.0)
Safety = med AND Lug_boot = big AND Maint != med AND Buying != med AND Buying != low|acc (16.0)
Safety != med AND Lug_boot != small AND Buying = high|acc (43.0)
Safety = med AND Lug_boot = big AND Maint != vhigh AND Maint != high|good (21.0)
Safety = med AND Doors = 2 AND Buying != low|unacc (17.0/3.0)
Maint = vhigh|acc (57.0/5.0)
Buying = vhigh|acc (44.0/4.0)
Maint = high AND Safety = med|acc (33.0/3.0)
Lug_boot = big AND Maint != high|vgood (28.0)
Buying != high AND Maint = high AND Buying = med|acc (16.0)
Buying != high AND Lug_boot != big AND Maint != high AND Lug_boot = small|good (18.0/4.0)
Buying != high AND Safety = med AND Maint != med|good (14.0/4.0)
Buying = high|acc (12.0/3.0)
Lug_boot != small AND Safety = med AND Buying != med|good (8.0/3.0)
Lug_boot != small AND Safety != med AND Doors != 2 AND Doors != 3|vgood (22.0)
Maint != low AND Lug_boot != small AND Buying != med|vgood (11.0/5.0)
Maint != low|acc (17.0/1.0)
|good (7.0/2.0)


## J48 Decision Tree

* Safety = low: unacc (464.0)
* Safety = med
	* Persons = 2: unacc (148.0)
	* Persons = 4
		* Buying = vhigh: unacc (38.0/7.0)
		* Buying = high
			* Lug_boot = small: unacc (14.0)
			* Lug_boot = med: unacc (12.0/3.0)
			* Lug_boot = big: acc (13.0/4.0)
		* Buying = med: acc (36.0/14.0)
		* Buying = low: acc (41.0/15.0)
	* Persons = more
		* Lug_boot = small: unacc (54.0/11.0)
		* Lug_boot = med: acc (54.0/23.0)
		* Lug_boot = big: acc (53.0/21.0)
* Safety = high
	* Persons = 2: unacc (144.0)
	* Persons = 4
		* Buying = vhigh
			* Maint = vhigh: unacc (10.0)
			* Maint = high: unacc (8.0)
			* Maint = med: acc (9.0)
			* Maint = low: acc (9.0)
		* Buying = high
			* Maint = vhigh: unacc (10.0)
			* Maint = high: acc (10.0)
			* Maint = med: acc (7.0)
			* Maint = low: acc (9.0)
		* Buying = med: acc (40.0/16.0)
		* Buying = low
			* Maint = vhigh: acc (10.0)
			* Maint = high: acc (12.0/6.0)
			* Maint = med: vgood (8.0/4.0)
			* Maint = low: good (11.0/5.0)
	* Persons = more
		* Buying = vhigh: unacc (45.0/21.0)
		* Buying = high: acc (39.0/13.0)
		* Buying = med
			* Maint = vhigh: acc (11.0)
			* Maint = high: acc (8.0)
			* Maint = med: vgood (10.0/5.0)
			* Maint = low: vgood (7.0/2.0)
		* Buying = low: vgood (37.0/20.0)


## SimpleCart Decision Tree

	* Safety=(high)|(med)
		* Persons=(more)|(4)
			* Buying=(low)|(med)
				* Maint=(low)|(med)
				* Safety=(high)
						* Lug_boot=(big)|(med)
							* Doors=(5more)|(4): vgood(29.0/0.0)
							* Doors!=(5more)|(4)
								* Lug_boot=(big)|(small): vgood(15.0/0.0)
								* Lug_boot!=(big)|(small)
									* Persons=(more)|(2)
											* Doors=(3)|(4)|(5more): vgood(4.0/0.0)
											* Doors!=(3)|(4)|(5more): good(2.0/1.0)
									* Persons!=(more)|(2)
											* Maint=(low)|(vhigh)|(high): good(4.0/0.0)
											* Maint!=(low)|(vhigh)|(high): acc(2.0/1.0)
						* Lug_boot!=(big)|(med)
								* Buying=(low)|(vhigh)|(high)
									* Doors=(5more)|(4)|(3): good(11.0/0.0)
									* Doors!=(5more)|(4)|(3): good(2.0/1.0)
								* Buying!=(low)|(vhigh)|(high)
							* Maint=(low)
										* Doors=(5more)|(4)|(3): good(3.0/0.0)
										* Doors!=(5more)|(4)|(3): unacc(1.0/1.0)
							* Maint!=(low)
										* Doors=(5more)|(4)|(3): acc(5.0/0.0)
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
							* Maint=(low)
									* Doors=(5more)|(4): good(8.0/0.0)
									* Doors!=(5more)|(4)
										* Persons=(more)|(2): good(3.0/0.0)
										* Persons!=(more)|(2): acc(2.0/0.0)
							* Maint!=(low): acc(14.0/0.0)
						* Lug_boot!=(big)|(med)
								* Doors=(5more)|(4)|(3): acc(21.0/0.0)
								* Doors!=(5more)|(4)|(3)
								* Persons=(more)|(2): unacc(4.0/0.0)
								* Persons!=(more)|(2): acc(4.0/0.0)
				* Maint!=(low)|(med)
				* Safety=(high)
					* Buying=(low)
								* Maint=(high)|(med)|(low)
								* Lug_boot=(big)|(med)
									* Lug_boot=(big)|(small): vgood(7.0/0.0)
									* Lug_boot!=(big)|(small)
										* Doors=(5more)|(4): vgood(3.0/0.0)
										* Doors!=(5more)|(4)
												* Doors=(3)|(4)|(5more): acc(1.0/1.0)
												* Doors!=(3)|(4)|(5more): acc(2.0/0.0)
								* Lug_boot!=(big)|(med): acc(7.0/0.0)
								* Maint!=(high)|(med)|(low)
									* Doors=(5more)|(4)|(3): acc(15.0/0.0)
									* Doors!=(5more)|(4)|(3)
								* Persons=(more): unacc(1.0/1.0)
								* Persons!=(more): acc(3.0/0.0)
					* Buying!=(low): acc(43.0/0.0)
				* Safety!=(high)
						* Lug_boot=(big)|(med)
							* Doors=(5more)|(4): acc(29.0/0.0)
							* Doors!=(5more)|(4)
							* Lug_boot=(big): acc(15.0/0.0)
							* Lug_boot!=(big)
										* Buying=(low)|(vhigh)|(high)
											* Maint=(high)|(med)|(low): acc(4.0/0.0)
											* Maint!=(high)|(med)|(low)
												* Doors=(3)|(4)|(5more): unacc(1.0/1.0)
												* Doors!=(3)|(4)|(5more): unacc(2.0/0.0)
										* Buying!=(low)|(vhigh)|(high)
											* Doors=(3)|(4)|(5more)
											* Persons=(more)|(2): acc(2.0/0.0)
											* Persons!=(more)|(2): unacc(2.0/0.0)
											* Doors!=(3)|(4)|(5more): unacc(4.0/0.0)
						* Lug_boot!=(big)|(med)
						* Maint=(high)
									* Buying=(low)|(vhigh)|(high)
										* Doors=(5more)|(4)|(3): acc(5.0/0.0)
										* Doors!=(5more)|(4)|(3): unacc(1.0/1.0)
									* Buying!=(low)|(vhigh)|(high): unacc(7.0/0.0)
						* Maint!=(high): unacc(16.0/0.0)
			* Buying!=(low)|(med)
				* Maint=(low)|(med)
				* Safety=(high)
							* Doors=(5more)|(4)|(3): acc(65.0/0.0)
							* Doors!=(5more)|(4)|(3)
							* Lug_boot=(big)|(med): acc(14.0/0.0)
							* Lug_boot!=(big)|(med)
								* Persons=(more)|(2): unacc(3.0/0.0)
								* Persons!=(more)|(2): acc(3.0/0.0)
				* Safety!=(high)
						* Lug_boot=(big)|(med)
							* Lug_boot=(big)|(small): acc(28.0/0.0)
							* Lug_boot!=(big)|(small)
								* Doors=(5more)|(4): acc(13.0/0.0)
								* Doors!=(5more)|(4)
								* Doors=(3)
									* Persons=(more): acc(3.0/0.0)
									* Persons!=(more): unacc(4.0/0.0)
								* Doors!=(3): unacc(8.0/0.0)
						* Lug_boot!=(big)|(med): unacc(30.0/0.0)
				* Maint!=(low)|(med)
				* Maint=(high)
							* Buying=(high)|(med)|(low)
						* Safety=(high): acc(21.0/0.0)
						* Safety!=(high)
								* Lug_boot=(big)|(med)
									* Doors=(5more)|(4): acc(8.0/0.0)
									* Doors!=(5more)|(4)
										* Lug_boot=(big)|(small): acc(4.0/0.0)
										* Lug_boot!=(big)|(small)
												* Doors=(3)|(4)|(5more): unacc(1.0/1.0)
												* Doors!=(3)|(4)|(5more): unacc(2.0/0.0)
								* Lug_boot!=(big)|(med): unacc(8.0/0.0)
							* Buying!=(high)|(med)|(low): unacc(45.0/0.0)
				* Maint!=(high): unacc(92.0/0.0)
		* Persons!=(more)|(4): unacc(333.0/0.0)
	* Safety!=(high)|(med): unacc(522.0/0.0)


