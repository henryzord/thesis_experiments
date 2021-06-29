# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | unacc | 0.701223 |
| Persons = 4 and Safety = high | acc | 0.047200 |
| Persons = more and Safety = med | acc | 0.032162 |
| Persons = 4 and Safety = med | acc | 0.030851 |
| Persons = more and Safety = high | acc | 0.034591 |
| Persons != 2 and Safety != low and Buying = low and Maint != vhigh and Safety != med and Lug_boot != small and Lug_boot != med | vgood | 0.015162 |
| Persons != 2 and Safety != low and Buying = low and Maint != vhigh and Safety = med and Lug_boot != small and Maint != high and Lug_boot != med | good | 0.009947 |
| Persons != 2 and Safety != low and Buying = low and Maint != vhigh and Safety != med and Lug_boot = small and Maint != high | good | 0.006843 |
| Persons != 2 and Safety != low and Buying != low and Buying = med and Maint = low and Safety != med and Lug_boot != small | vgood | 0.007360 |
| Persons != 2 and Safety != low and Buying = low and Maint != vhigh and Safety = med and Lug_boot != small and Maint != high and Lug_boot = med | good | 0.003884 |
| Persons != 2 and Safety != low and Buying != low and Buying = med and Maint != low and Lug_boot != small and Maint = med and Safety != med | vgood | 0.005125 |
| Persons != 2 and Safety != low and Buying != low and Buying = med and Maint = low and Safety = med and Lug_boot != small and Lug_boot != med | good | 0.004667 |
| Persons != 2 and Safety != low and Buying != low and Buying = med and Maint = low and Safety != med and Lug_boot = small | good | 0.003433 |
| Persons != 2 and Safety != low and Buying = low and Maint != vhigh and Safety != med and Lug_boot != small and Lug_boot = med and Maint = high | vgood | 0.002089 |
| Persons != 2 and Safety != low and Buying != low and Buying = med and Maint = low and Safety = med and Lug_boot != small and Lug_boot = med | good | 0.002090 |
| Persons != 2 and Safety != low and Buying = low and Maint != vhigh and Safety != med and Lug_boot != small and Lug_boot = med and Maint != high and Persons != 4 | vgood | 0.003004 |
| Persons != 2 and Safety != low and Buying = low and Maint != vhigh and Safety != med and Lug_boot != small and Lug_boot = med and Maint != high and Persons = 4 | good | 0.001530 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Persons = 2 | unacc | 0.529412 |
| Safety = low | unacc | 0.428571 |
| Buying != low and Buying != med and Maint = vhigh | unacc | 0.154827 |
| Buying = vhigh and Maint != high and Lug_boot != small and Doors != 2 | acc | 0.136600 |
| Buying = vhigh and Maint = high | unacc | 0.086393 |
| Safety = med and Lug_boot = small and Buying != high and Buying != vhigh and Maint != vhigh and Doors != 2 and Maint != high | acc | 0.089744 |
| Lug_boot = small and Safety = med and Buying != low | unacc | 0.110662 |
| Buying = high and Doors != 2 and Doors != 3 | acc | 0.260274 |
| Maint = vhigh and Lug_boot != small and Doors != 2 | acc | 0.190000 |
| Safety = med and Maint = vhigh and Lug_boot != big | unacc | 0.031546 |
| Buying = high and Lug_boot = big | acc | 0.126437 |
| Buying = high and Safety != med and Doors != 2 | acc | 0.067485 |
| Safety = med and Buying = high and Doors = 2 | unacc | 0.021429 |
| Safety = med and Maint = high and Lug_boot != big and Buying = low | acc | 0.082180 |
| Safety = med and Maint = high and Lug_boot != med | acc | 0.082180 |
| Safety = med and Buying = high and Persons = 4 | unacc | 0.012048 |
| Safety = med and Buying = vhigh and Lug_boot = med | unacc | 0.019920 |
| Lug_boot = small and Doors != 2 and Maint != low and Buying != low | acc | 0.142857 |
| Lug_boot = small and Doors != 2 and Buying != med and Maint != med and Maint != low | acc | 0.073826 |
| Lug_boot = small and Doors != 2 and Buying != vhigh | good | 0.080645 |
| Lug_boot = small and Persons != 4 and Doors = 2 | unacc | 0.075117 |
| Safety = med and Maint = high and Doors != 2 | acc | 0.037538 |
| Safety = med and Maint != high and Buying != vhigh and Maint != vhigh and Buying = low and Lug_boot != small and Lug_boot != med | good | 0.090909 |
| Safety = med and Maint != high and Maint != low and Buying != low | acc | 0.171171 |
| Safety = med and Maint != high and Doors != 2 | good | 0.105675 |
| Doors != 2 and Buying != vhigh and Maint != high and Doors != 3 | vgood | 0.263158 |
| Buying != low and Safety != med and Doors != 3 and Lug_boot != big and Maint != low | acc | 0.301587 |
| Buying = vhigh | acc | 0.241379 |
| Maint = vhigh | acc | 0.169811 |
| Safety = med and Maint != high and Lug_boot != big | acc | 0.185185 |
| Safety = med and Maint = high | unacc | 0.049180 |
| Maint = high and Buying = med | acc | 0.180000 |
| Buying != high and Lug_boot != small and Lug_boot != med and Safety != med | vgood | 0.500000 |
| Doors = 2 and Buying != high and Maint != high | good | 0.370370 |
| Doors != 2 and Persons != 4 | vgood | 0.411765 |
| Doors = 2 | acc | 0.600000 |
| Doors = 3 | acc | 0.250000 |
|  | vgood | 0.500000 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

persons|safety|acceptability
---|---|---
more|high|acc
4|high|acc
2|high|unacc
2|med|unacc
more|med|acc
4|med|acc
more|low|unacc
4|low|unacc
2|low|unacc

## PART

Decision list:

rules | predicted class
---|---
Persons = 2|unacc (522.0)
Safety = low|unacc (348.0)
Buying != low AND Buying != med AND Maint = vhigh|unacc (85.0)
Buying = vhigh AND Maint != high AND Lug_boot != small AND Doors != 2|acc (42.0/1.0)
Buying = vhigh AND Maint = high|unacc (40.0)
Safety = med AND Lug_boot = small AND Buying != high AND Buying != vhigh AND Maint != vhigh AND Doors != 2 AND Maint != high|acc (21.0)
Lug_boot = small AND Safety = med AND Buying != low|unacc (52.0/1.0)
Buying = high AND Doors != 2 AND Doors != 3|acc (57.0)
Maint = vhigh AND Lug_boot != small AND Doors != 2|acc (38.0)
Safety = med AND Maint = vhigh AND Lug_boot != big|unacc (10.0)
Buying = high AND Lug_boot = big|acc (22.0)
Buying = high AND Safety != med AND Doors != 2|acc (11.0)
Safety = med AND Buying = high AND Doors = 2|unacc (6.0)
Safety = med AND Maint = high AND Lug_boot != big AND Buying = low|acc (15.0/1.0)
Safety = med AND Maint = high AND Lug_boot != med|acc (14.0)
Safety = med AND Buying = high AND Persons = 4|unacc (3.0)
Safety = med AND Buying = vhigh AND Lug_boot = med|unacc (4.0)
Lug_boot = small AND Doors != 2 AND Maint != low AND Buying != low|acc (23.0)
Lug_boot = small AND Doors != 2 AND Buying != med AND Maint != med AND Maint != low|acc (11.0)
Lug_boot = small AND Doors != 2 AND Buying != vhigh|good (15.0)
Lug_boot = small AND Persons != 4 AND Doors = 2|unacc (15.0)
Safety = med AND Maint = high AND Doors != 2|acc (6.0/1.0)
Safety = med AND Maint != high AND Buying != vhigh AND Maint != vhigh AND Buying = low AND Lug_boot != small AND Lug_boot != med|good (15.0)
Safety = med AND Maint != high AND Maint != low AND Buying != low|acc (19.0)
Safety = med AND Maint != high AND Doors != 2|good (21.0/3.0)
Doors != 2 AND Buying != vhigh AND Maint != high AND Doors != 3|vgood (30.0)
Buying != low AND Safety != med AND Doors != 3 AND Lug_boot != big AND Maint != low|acc (19.0)
Buying = vhigh|acc (14.0)
Maint = vhigh|acc (9.0)
Safety = med AND Maint != high AND Lug_boot != big|acc (6.0)
Safety = med AND Maint = high|unacc (2.0)
Maint = high AND Buying = med|acc (9.0)
Buying != high AND Lug_boot != small AND Lug_boot != med AND Safety != med|vgood (20.0)
Doors = 2 AND Buying != high AND Maint != high|good (10.0)
Doors != 2 AND Persons != 4|vgood (7.0)
Doors = 2|acc (6.0)
Doors = 3|acc (4.0/2.0)
|vgood (2.0)


## J48 Decision Tree

* Persons = 2: unacc (522.0)
* Persons != 2
	* Safety = low: unacc (348.0)
	* Safety != low
		* Buying = low
			* Maint = vhigh
				* Lug_boot = small
					* Safety = med: unacc (7.0)
					* Safety != med: acc (8.0/1.0)
				* Lug_boot != small
					* Doors = 2: acc (8.0/2.0)
					* Doors != 2: acc (19.0)
			* Maint != vhigh
				* Safety = med
					* Lug_boot = small
						* Persons = 4: acc (11.0)
						* Persons != 4: acc (11.0/3.0)
					* Lug_boot != small
						* Maint = high: acc (14.0)
						* Maint != high
							* Lug_boot = med: good (11.0/3.0)
							* Lug_boot != med: good (15.0)
				* Safety != med
					* Lug_boot = small
						* Maint = high: acc (7.0/1.0)
						* Maint != high: good (14.0/2.0)
					* Lug_boot != small
						* Lug_boot = med
							* Maint = high: vgood (8.0/3.0)
							* Maint != high
								* Persons = 4: good (7.0/3.0)
								* Persons != 4: vgood (8.0/2.0)
						* Lug_boot != med: vgood (23.0)
		* Buying != low
			* Buying = med
				* Maint = low
					* Safety = med
						* Lug_boot = small: acc (7.0/1.0)
						* Lug_boot != small
							* Lug_boot = med: good (8.0/3.0)
							* Lug_boot != med: good (7.0)
					* Safety != med
						* Lug_boot = small: good (7.0/1.0)
						* Lug_boot != small: vgood (13.0/1.0)
				* Maint != low
					* Lug_boot = small
						* Safety = med
							* Maint = med: acc (7.0/1.0)
							* Maint != med: unacc (15.0)
						* Safety != med
							* Persons = 4: acc (10.0)
							* Persons != 4: acc (12.0/3.0)
					* Lug_boot != small
						* Maint = med
							* Safety = med: acc (15.0)
							* Safety != med: vgood (13.0/3.0)
						* Maint != med
							* Lug_boot = med
								* Safety = med: acc (12.0/4.0)
								* Safety != med: acc (14.0)
							* Lug_boot != med: acc (28.0)
			* Buying != med
				* Maint = vhigh: unacc (85.0)
				* Maint != vhigh
					* Lug_boot = small
						* Safety = med: unacc (41.0)
						* Safety != med
							* Maint = high: unacc (13.0/6.0)
							* Maint != high
								* Doors = 2: unacc (8.0/4.0)
								* Doors != 2: acc (24.0)
					* Lug_boot != small
						* Maint = high
							* Buying = vhigh: unacc (27.0)
							* Buying != vhigh
								* Lug_boot = med
									* Safety = med: acc (8.0/3.0)
									* Safety != med: acc (7.0)
								* Lug_boot != med: acc (14.0)
						* Maint != high
							* Lug_boot = med
								* Safety = med
									* Doors = 2: unacc (8.0)
									* Doors != 2
										* Persons = 4: acc (10.0/3.0)
										* Persons != 4: acc (11.0)
								* Safety != med: acc (30.0)
							* Lug_boot != med: acc (58.0)


## SimpleCart Decision Tree

	* Persons=(more)|(4)
		* Safety=(high)|(med)
			* Buying=(low)|(med)
				* Maint=(low)|(med)
					* Safety=(high)|(low)
						* Lug_boot=(big)|(med)
								* Doors=(5more)|(4)|(3)
									* Doors=(5more)|(4)|(2): vgood(30.0/0.0)
									* Doors!=(5more)|(4)|(2)
									* Persons=(more)|(2): vgood(7.0/0.0)
									* Persons!=(more)|(2)
										* Lug_boot=(big)|(small): vgood(3.0/0.0)
										* Lug_boot!=(big)|(small): good(2.0/1.0)
								* Doors!=(5more)|(4)|(3)
							* Lug_boot=(big): vgood(6.0/0.0)
							* Lug_boot!=(big)
										* Buying=(low)|(vhigh)|(high): good(4.0/0.0)
										* Buying!=(low)|(vhigh)|(high): acc(2.0/1.0)
						* Lug_boot!=(big)|(med)
								* Buying=(low)|(vhigh)|(high)
									* Doors=(5more)|(4)|(3): good(10.0/0.0)
									* Doors!=(5more)|(4)|(3)
									* Persons=(more)|(2): unacc(2.0/0.0)
									* Persons!=(more)|(2): good(2.0/0.0)
								* Buying!=(low)|(vhigh)|(high)
									* Maint=(low)|(vhigh)|(high)
										* Doors=(5more)|(4)|(3): good(5.0/0.0)
										* Doors!=(5more)|(4)|(3): unacc(1.0/1.0)
									* Maint!=(low)|(vhigh)|(high): acc(6.0/1.0)
					* Safety!=(high)|(low)
						* Lug_boot=(big)|(med)
						* Buying=(low)
								* Lug_boot=(big)|(small): good(15.0/0.0)
								* Lug_boot!=(big)|(small)
										* Doors=(5more)|(4)|(3)
											* Doors=(5more)|(4)|(2): good(6.0/0.0)
											* Doors!=(5more)|(4)|(2): good(2.0/1.0)
										* Doors!=(5more)|(4)|(3): acc(2.0/0.0)
						* Buying!=(low)
									* Maint=(low)|(vhigh)|(high)
									* Doors=(5more)|(4): good(8.0/0.0)
									* Doors!=(5more)|(4)
									* Lug_boot=(big): good(3.0/0.0)
									* Lug_boot!=(big)
												* Doors=(3)|(4)|(5more): acc(1.0/1.0)
												* Doors!=(3)|(4)|(5more): acc(2.0/0.0)
									* Maint!=(low)|(vhigh)|(high): acc(15.0/0.0)
						* Lug_boot!=(big)|(med)
								* Doors=(5more)|(4)|(3): acc(21.0/0.0)
								* Doors!=(5more)|(4)|(3)
								* Persons=(more)|(2): unacc(4.0/0.0)
								* Persons!=(more)|(2): acc(3.0/0.0)
				* Maint!=(low)|(med)
					* Lug_boot=(big)|(med)
							* Maint=(high)|(med)|(low)
								* Buying=(low)|(vhigh)|(high)
								* Safety=(high)|(low)
									* Doors=(5more)|(4): vgood(8.0/0.0)
									* Doors!=(5more)|(4)
										* Lug_boot=(big)|(small): vgood(4.0/0.0)
										* Lug_boot!=(big)|(small)
												* Doors=(3)|(4)|(5more): acc(1.0/1.0)
												* Doors!=(3)|(4)|(5more): acc(2.0/0.0)
								* Safety!=(high)|(low): acc(14.0/0.0)
								* Buying!=(low)|(vhigh)|(high)
								* Doors=(5more)|(4): acc(14.0/0.0)
								* Doors!=(5more)|(4)
									* Safety=(high)|(low): acc(7.0/0.0)
									* Safety!=(high)|(low)
									* Lug_boot=(big): acc(3.0/0.0)
									* Lug_boot!=(big)
												* Doors=(3)|(4)|(5more): unacc(1.0/1.0)
												* Doors!=(3)|(4)|(5more): unacc(2.0/0.0)
							* Maint!=(high)|(med)|(low)
								* Doors=(5more)|(4)|(3): acc(38.0/0.0)
								* Doors!=(5more)|(4)|(3)
								* Lug_boot=(big)|(small): acc(8.0/0.0)
								* Lug_boot!=(big)|(small)
									* Safety=(high)|(low): acc(4.0/0.0)
									* Safety!=(high)|(low): unacc(3.0/0.0)
					* Lug_boot!=(big)|(med)
						* Safety=(high)|(low)
								* Doors=(5more)|(4)|(3): acc(22.0/0.0)
								* Doors!=(5more)|(4)|(3)
								* Persons=(more)|(2): unacc(4.0/0.0)
								* Persons!=(more)|(2): acc(4.0/0.0)
						* Safety!=(high)|(low)
								* Buying=(low)|(vhigh)|(high)
									* Maint=(high)|(med)|(low)
										* Doors=(5more)|(4)|(3): acc(6.0/0.0)
										* Doors!=(5more)|(4)|(3): unacc(1.0/1.0)
									* Maint!=(high)|(med)|(low): unacc(7.0/0.0)
								* Buying!=(low)|(vhigh)|(high): unacc(15.0/0.0)
			* Buying!=(low)|(med)
				* Maint=(low)|(med)
					* Lug_boot=(big)|(med)
							* Doors=(5more)|(4)|(3)
								* Doors=(5more)|(4)|(2): acc(59.0/0.0)
								* Doors!=(5more)|(4)|(2)
								* Lug_boot=(big)|(small): acc(15.0/0.0)
								* Lug_boot!=(big)|(small)
									* Safety=(high)|(low): acc(7.0/0.0)
									* Safety!=(high)|(low)
										* Persons=(more)|(2): acc(3.0/0.0)
										* Persons!=(more)|(2): unacc(3.0/0.0)
							* Doors!=(5more)|(4)|(3)
						* Lug_boot=(big): acc(14.0/0.0)
						* Lug_boot!=(big)
								* Safety=(high)|(low): acc(8.0/0.0)
								* Safety!=(high)|(low): unacc(8.0/0.0)
					* Lug_boot!=(big)|(med)
						* Safety=(high)|(low)
								* Doors=(5more)|(4)|(3): acc(24.0/0.0)
								* Doors!=(5more)|(4)|(3)
								* Persons=(more)|(2): unacc(4.0/0.0)
								* Persons!=(more)|(2): acc(4.0/0.0)
						* Safety!=(high)|(low): unacc(28.0/0.0)
				* Maint!=(low)|(med)
				* Maint=(high)
							* Buying=(high)|(med)|(low)
							* Lug_boot=(big)|(med)
									* Doors=(5more)|(4)|(3)
										* Doors=(5more)|(4)|(2): acc(14.0/0.0)
										* Doors!=(5more)|(4)|(2)
										* Persons=(more)|(2): acc(4.0/0.0)
										* Persons!=(more)|(2)
											* Lug_boot=(big)|(small): acc(2.0/0.0)
											* Lug_boot!=(big)|(small): unacc(1.0/1.0)
									* Doors!=(5more)|(4)|(3)
									* Lug_boot=(big)|(small): acc(4.0/0.0)
									* Lug_boot!=(big)|(small): unacc(2.0/1.0)
							* Lug_boot!=(big)|(med)
								* Safety=(high)|(low)
										* Doors=(5more)|(4)|(3): acc(5.0/0.0)
										* Doors!=(5more)|(4)|(3): unacc(1.0/1.0)
								* Safety!=(high)|(low): unacc(6.0/0.0)
							* Buying!=(high)|(med)|(low): unacc(40.0/0.0)
				* Maint!=(high): unacc(85.0/0.0)
		* Safety!=(high)|(med): unacc(348.0/0.0)
	* Persons!=(more)|(4): unacc(522.0/0.0)


