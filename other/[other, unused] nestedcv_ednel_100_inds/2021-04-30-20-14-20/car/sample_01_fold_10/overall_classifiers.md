# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Safety != high | unacc | 0.615914 |
| Safety != med | unacc | 0.590902 |
| Persons = 4 and Safety = high | acc | 0.044299 |
| Persons = 4 and Safety = med | acc | 0.032515 |
| Persons = more and Safety = med | acc | 0.031746 |
| Persons = more and Safety = high | acc | 0.034903 |
| Safety != low and Persons != 2 and Buying = low and Maint != vhigh and Safety != med and Lug_boot != small and Lug_boot != med | vgood | 0.014512 |
| Safety != low and Persons != 2 and Buying = low and Maint != vhigh and Safety = med and Lug_boot != small and Maint != high and Lug_boot != med | good | 0.009290 |
| Safety != low and Persons != 2 and Buying = low and Maint != vhigh and Safety != med and Lug_boot = small | good | 0.004584 |
| Safety != low and Persons != 2 and Buying != low and Buying = med and Maint = low and Safety = med | good | 0.003857 |
| Safety != low and Persons != 2 and Buying != low and Buying = med and Maint != low and Maint = med and Safety != med and Persons != 4 | vgood | 0.002730 |
| Safety != low and Persons != 2 and Buying = low and Maint != vhigh and Safety = med and Lug_boot != small and Maint != high and Lug_boot = med | good | 0.003610 |
| Safety != low and Persons != 2 and Buying = low and Maint != vhigh and Safety != med and Lug_boot != small and Lug_boot = med and Persons != 4 | vgood | 0.003881 |
| Safety != low and Persons != 2 and Buying = low and Maint != vhigh and Safety != med and Lug_boot != small and Lug_boot = med and Persons = 4 | vgood | 0.002189 |
| Safety != low and Persons != 2 and Buying != low and Buying = med and Maint = low and Safety != med and Persons != 4 | vgood | 0.002189 |
| Safety != low and Persons != 2 and Buying != low and Buying = med and Maint = low and Safety != med and Persons = 4 | vgood | 0.001673 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Safety = low | unacc | 0.530364 |
| Persons = 2 | unacc | 0.422167 |
| Buying != low and Buying != med and Maint = vhigh | unacc | 0.151737 |
| Lug_boot = small and Safety = med and Buying = vhigh | unacc | 0.047228 |
| Buying != low and Buying != med and Lug_boot = big and Maint != high | acc | 0.203333 |
| Buying = vhigh and Maint != high | acc | 0.101688 |
| Buying = vhigh | unacc | 0.101695 |
| Safety = med and Lug_boot = small and Buying = high | unacc | 0.055980 |
| Safety = med and Lug_boot = small and Maint != vhigh and Doors != 2 and Maint != high | acc | 0.107143 |
| Safety = med and Lug_boot = small and Buying = med | unacc | 0.041673 |
| Buying = high and Doors != 2 | acc | 0.255425 |
| Maint != low and Maint != med and Lug_boot = big and Buying != low | acc | 0.168421 |
| Maint = vhigh and Safety != med | acc | 0.177632 |
| Maint = vhigh and Lug_boot != small | acc | 0.059036 |
| Buying = high and Safety != med | acc | 0.041159 |
| Safety = med and Buying != high and Maint != vhigh and Maint = high | acc | 0.115570 |
| Safety = med and Buying != high and Lug_boot != small and Lug_boot != med and Maint != med | good | 0.076471 |
| Lug_boot = big and Safety != med | vgood | 0.203297 |
| Buying != high and Maint != vhigh and Doors = 2 and Lug_boot != small and Safety = med | acc | 0.055140 |
| Doors = 2 and Safety = med | unacc | 0.090204 |
| Maint != vhigh and Maint = high | acc | 0.148694 |
| Maint != vhigh and Buying != med and Lug_boot != med and Doors != 2 | good | 0.179775 |
| Maint != vhigh and Lug_boot != med and Buying = med and Doors != 2 | acc | 0.097561 |
| Maint != vhigh and Lug_boot != small and Safety = med | good | 0.140659 |
| Lug_boot = small | unacc | 0.169006 |
| Doors = 2 and Buying != med | good | 0.057971 |
| Doors != 2 and Persons != 4 | vgood | 0.222368 |
| Doors != 4 and Maint = med | acc | 0.223214 |
| Doors != 4 | good | 0.225000 |
|  | vgood | 0.391304 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

persons|safety|acceptability
---|---|---
4|high|acc
more|high|acc
2|high|unacc
4|med|acc
2|med|unacc
more|med|acc
4|low|unacc
more|low|unacc
2|low|unacc

## PART

Decision list:

rules | predicted class
---|---
Safety = low|unacc (356.0)
Persons = 2|unacc (212.0)
Buying != low AND Buying != med AND Maint = vhigh|unacc (53.0)
Lug_boot = small AND Safety = med AND Buying = vhigh|unacc (18.0)
Buying != low AND Buying != med AND Lug_boot = big AND Maint != high|acc (42.0)
Buying = vhigh AND Maint != high|acc (25.0/6.0)
Buying = vhigh|unacc (21.0)
Safety = med AND Lug_boot = small AND Buying = high|unacc (14.0)
Safety = med AND Lug_boot = small AND Maint != vhigh AND Doors != 2 AND Maint != high|acc (12.0)
Safety = med AND Lug_boot = small AND Buying = med|unacc (16.0)
Buying = high AND Doors != 2|acc (47.0/3.0)
Maint != low AND Maint != med AND Lug_boot = big AND Buying != low|acc (22.0)
Maint = vhigh AND Safety != med|acc (24.0/2.0)
Maint = vhigh AND Lug_boot != small|acc (15.0/5.0)
Buying = high AND Safety != med|acc (10.0/3.0)
Safety = med AND Buying != high AND Maint != vhigh AND Maint = high|acc (16.0/1.0)
Safety = med AND Buying != high AND Lug_boot != small AND Lug_boot != med AND Maint != med|good (10.0)
Lug_boot = big AND Safety != med|vgood (27.0)
Buying != high AND Maint != vhigh AND Doors = 2 AND Lug_boot != small AND Safety = med|acc (8.0/1.0)
Doors = 2 AND Safety = med|unacc (9.0/1.0)
Maint != vhigh AND Maint = high|acc (21.0/5.0)
Maint != vhigh AND Buying != med AND Lug_boot != med AND Doors != 2|good (11.0)
Maint != vhigh AND Lug_boot != med AND Buying = med AND Doors != 2|acc (8.0/1.0)
Maint != vhigh AND Lug_boot != small AND Safety = med|good (12.0/3.0)
Lug_boot = small|unacc (8.0/2.0)
Doors = 2 AND Buying != med|good (3.0)
Doors != 2 AND Persons != 4|vgood (8.0)
Doors != 4 AND Maint = med|acc (3.0/1.0)
Doors != 4|good (3.0)
|vgood (2.0)


## J48 Decision Tree

* Safety = low: unacc (524.0)
* Safety != low
	* Persons = 2: unacc (339.0)
	* Persons != 2
		* Buying = low
			* Maint = vhigh
				* Safety = med: acc (21.0/10.0)
				* Safety != med
					* Persons = 4: acc (12.0)
					* Persons != 4: acc (11.0/1.0)
			* Maint != vhigh
				* Safety = med
					* Lug_boot = small
						* Persons = 4: acc (10.0)
						* Persons != 4: acc (11.0/3.0)
					* Lug_boot != small
						* Maint = high: acc (15.0)
						* Maint != high
							* Lug_boot = med: good (15.0/6.0)
							* Lug_boot != med: good (14.0)
				* Safety != med
					* Lug_boot = small: good (21.0/9.0)
					* Lug_boot != small
						* Lug_boot = med
							* Persons = 4: vgood (11.0/5.0)
							* Persons != 4: vgood (11.0/3.0)
						* Lug_boot != med: vgood (22.0)
		* Buying != low
			* Buying = med
				* Maint = low
					* Safety = med: good (21.0/10.0)
					* Safety != med
						* Persons = 4: vgood (10.0/5.0)
						* Persons != 4: vgood (11.0/5.0)
				* Maint != low
					* Maint = med
						* Safety = med
							* Persons = 4: acc (10.0)
							* Persons != 4: acc (12.0/1.0)
						* Safety != med
							* Persons = 4: acc (11.0/5.0)
							* Persons != 4: vgood (12.0/5.0)
					* Maint != med
						* Safety = med
							* Lug_boot = big: acc (14.0)
							* Lug_boot != big
								* Lug_boot = small: unacc (15.0)
								* Lug_boot != small: unacc (12.0/6.0)
						* Safety != med
							* Doors = 2: acc (11.0/2.0)
							* Doors != 2: acc (32.0)
			* Buying != med
				* Maint = vhigh: unacc (83.0)
				* Maint != vhigh
					* Lug_boot = small
						* Safety = med: unacc (45.0)
						* Safety != med
							* Maint = high: unacc (14.0/6.0)
							* Maint != high
								* Persons = 4: acc (15.0)
								* Persons != 4: acc (13.0/4.0)
					* Lug_boot != small
						* Maint = high
							* Buying = vhigh: unacc (29.0)
							* Buying != vhigh
								* Lug_boot = med: acc (16.0/3.0)
								* Lug_boot != med: acc (15.0)
						* Maint != high
							* Lug_boot = med
								* Safety = med
									* Persons = 4: acc (15.0/7.0)
									* Persons != 4: acc (13.0/3.0)
								* Safety != med: acc (26.0)
							* Lug_boot != med: acc (61.0)


## SimpleCart Decision Tree

	* Safety=(high)|(med)
		* Persons=(more)|(4)
			* Buying=(low)|(med)
				* Maint=(low)|(med)
					* Safety=(high)|(low)
						* Lug_boot=(big)|(med)
							* Doors=(5more)|(4): vgood(29.0/0.0)
							* Doors!=(5more)|(4)
								* Lug_boot=(big)|(small): vgood(14.0/0.0)
								* Lug_boot!=(big)|(small)
										* Doors=(3)|(4)|(5more)
										* Persons=(more)|(2): vgood(4.0/0.0)
										* Persons!=(more)|(2)
												* Buying=(low)|(vhigh)|(high): good(2.0/0.0)
												* Buying!=(low)|(vhigh)|(high): acc(1.0/1.0)
										* Doors!=(3)|(4)|(5more)
											* Buying=(low)|(vhigh)|(high): good(3.0/0.0)
											* Buying!=(low)|(vhigh)|(high): acc(2.0/1.0)
						* Lug_boot!=(big)|(med)
								* Maint=(low)|(vhigh)|(high)
									* Doors=(5more)|(4)|(3): good(12.0/0.0)
									* Doors!=(5more)|(4)|(3): unacc(2.0/1.0)
								* Maint!=(low)|(vhigh)|(high)
							* Buying=(low)
										* Doors=(5more)|(4)|(3): good(5.0/0.0)
										* Doors!=(5more)|(4)|(3): unacc(1.0/1.0)
							* Buying!=(low)
										* Doors=(5more)|(4)|(3): acc(6.0/0.0)
										* Doors!=(5more)|(4)|(3): unacc(1.0/1.0)
					* Safety!=(high)|(low)
						* Lug_boot=(big)|(med)
								* Buying=(low)|(vhigh)|(high)
							* Lug_boot=(big): good(14.0/0.0)
							* Lug_boot!=(big)
									* Doors=(5more)|(4): good(7.0/0.0)
									* Doors!=(5more)|(4)
											* Doors=(3)|(4)|(5more)
											* Persons=(more)|(2): good(2.0/0.0)
											* Persons!=(more)|(2): acc(2.0/0.0)
											* Doors!=(3)|(4)|(5more): acc(4.0/0.0)
								* Buying!=(low)|(vhigh)|(high)
									* Maint=(low)|(vhigh)|(high)
									* Doors=(5more)|(4): good(6.0/0.0)
									* Doors!=(5more)|(4)
										* Lug_boot=(big)|(small): good(4.0/0.0)
										* Lug_boot!=(big)|(small)
												* Doors=(3)|(4)|(5more): acc(1.0/1.0)
												* Doors!=(3)|(4)|(5more): acc(2.0/0.0)
									* Maint!=(low)|(vhigh)|(high): acc(14.0/0.0)
						* Lug_boot!=(big)|(med)
								* Doors=(5more)|(4)|(3): acc(21.0/0.0)
								* Doors!=(5more)|(4)|(3)
								* Persons=(more)|(2): unacc(4.0/0.0)
								* Persons!=(more)|(2): acc(4.0/0.0)
				* Maint!=(low)|(med)
					* Lug_boot=(big)|(med)
					* Maint=(high)
							* Safety=(high)|(low)
									* Buying=(low)|(vhigh)|(high)
									* Lug_boot=(big)|(small): vgood(8.0/0.0)
									* Lug_boot!=(big)|(small)
										* Doors=(5more)|(4): vgood(3.0/0.0)
										* Doors!=(5more)|(4)
												* Doors=(3)|(4)|(5more): acc(1.0/1.0)
												* Doors!=(3)|(4)|(5more): acc(2.0/0.0)
									* Buying!=(low)|(vhigh)|(high): acc(13.0/0.0)
							* Safety!=(high)|(low)
									* Buying=(low)|(vhigh)|(high): acc(15.0/0.0)
									* Buying!=(low)|(vhigh)|(high)
									* Lug_boot=(big)|(small): acc(6.0/0.0)
									* Lug_boot!=(big)|(small)
										* Doors=(5more)|(4): acc(3.0/0.0)
										* Doors!=(5more)|(4): unacc(3.0/0.0)
					* Maint!=(high)
							* Safety=(high)|(low): acc(31.0/0.0)
							* Safety!=(high)|(low)
								* Lug_boot=(big)|(small): acc(15.0/0.0)
								* Lug_boot!=(big)|(small)
									* Doors=(5more)|(4): acc(5.0/0.0)
									* Doors!=(5more)|(4)
											* Doors=(3)|(4)|(5more)
											* Persons=(more)|(2): acc(2.0/0.0)
											* Persons!=(more)|(2): unacc(2.0/0.0)
											* Doors!=(3)|(4)|(5more): unacc(4.0/0.0)
					* Lug_boot!=(big)|(med)
						* Safety=(high)|(low)
								* Doors=(5more)|(4)|(3): acc(21.0/0.0)
								* Doors!=(5more)|(4)|(3)
								* Persons=(more)|(2): unacc(4.0/0.0)
								* Persons!=(more)|(2): acc(4.0/0.0)
						* Safety!=(high)|(low)
						* Buying=(low)
									* Maint=(high)|(med)|(low): acc(6.0/1.0)
									* Maint!=(high)|(med)|(low): unacc(7.0/0.0)
						* Buying!=(low): unacc(15.0/0.0)
			* Buying!=(low)|(med)
				* Maint=(low)|(med)
					* Lug_boot=(big)|(med)
						* Lug_boot=(big)|(small): acc(61.0/0.0)
						* Lug_boot!=(big)|(small)
								* Doors=(5more)|(4)|(3)
									* Doors=(5more)|(4)|(2): acc(27.0/0.0)
									* Doors!=(5more)|(4)|(2)
									* Persons=(more)|(2): acc(7.0/0.0)
									* Persons!=(more)|(2)
										* Safety=(high)|(low): acc(3.0/0.0)
										* Safety!=(high)|(low): unacc(3.0/0.0)
								* Doors!=(5more)|(4)|(3)
								* Safety=(high)|(low): acc(7.0/0.0)
								* Safety!=(high)|(low): unacc(7.0/0.0)
					* Lug_boot!=(big)|(med)
					* Safety=(high)
								* Doors=(5more)|(4)|(3): acc(20.0/0.0)
								* Doors!=(5more)|(4)|(3)
								* Persons=(more)|(2): unacc(4.0/0.0)
								* Persons!=(more)|(2): acc(4.0/0.0)
					* Safety!=(high): unacc(29.0/0.0)
				* Maint!=(low)|(med)
						* Buying=(high)|(med)|(low)
							* Maint=(high)|(med)|(low)
							* Lug_boot=(big)|(med)
								* Doors=(5more)|(4): acc(15.0/0.0)
								* Doors!=(5more)|(4)
									* Lug_boot=(big)|(small): acc(8.0/0.0)
									* Lug_boot!=(big)|(small)
										* Safety=(high)|(low): acc(4.0/0.0)
										* Safety!=(high)|(low)
												* Doors=(3)|(4)|(5more): unacc(1.0/1.0)
												* Doors!=(3)|(4)|(5more): unacc(2.0/0.0)
							* Lug_boot!=(big)|(med)
							* Safety=(high)
										* Doors=(5more)|(4)|(3): acc(5.0/0.0)
										* Doors!=(5more)|(4)|(3): unacc(1.0/1.0)
							* Safety!=(high): unacc(8.0/0.0)
							* Maint!=(high)|(med)|(low): unacc(44.0/0.0)
						* Buying!=(high)|(med)|(low): unacc(83.0/0.0)
		* Persons!=(more)|(4): unacc(339.0/0.0)
	* Safety!=(high)|(med): unacc(524.0/0.0)


