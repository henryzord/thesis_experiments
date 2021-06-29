# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | unacc | 0.701675 |
| Safety != low and Persons != 2 and Buying != vhigh and Buying = high and Maint != vhigh and Lug_boot != small | acc | 0.054538 |
| Persons = 4 and Safety = med | acc | 0.034687 |
| Persons = 4 and Safety = high | acc | 0.044869 |
| Persons = more and Safety = med | acc | 0.029680 |
| Persons = more and Safety = high | acc | 0.035804 |
| Safety != low and Persons != 2 and Buying != vhigh and Buying != high and Maint != vhigh and Maint != high and Safety != med and Lug_boot != small and Lug_boot != med | vgood | 0.017751 |
| Safety != low and Persons != 2 and Buying != vhigh and Buying != high and Maint != vhigh and Maint != high and Safety = med and Lug_boot != small and Buying != med | good | 0.012715 |
| Safety != low and Persons != 2 and Buying != vhigh and Buying != high and Maint != vhigh and Maint != high and Safety != med and Lug_boot != small and Lug_boot = med and Doors != 2 and Doors != 3 | vgood | 0.009940 |
| Safety != low and Persons != 2 and Buying != vhigh and Buying != high and Maint != vhigh and Maint != high and Safety != med and Lug_boot = small and Doors != 2 and Buying != med | good | 0.007319 |
| Safety != low and Persons != 2 and Buying != vhigh and Buying != high and Maint != vhigh and Maint != high and Safety = med and Lug_boot != small and Buying = med and Maint != med | good | 0.005762 |
| Safety != low and Persons != 2 and Buying != vhigh and Buying != high and Maint != vhigh and Maint = high and Lug_boot != small and Buying != med and Safety != med | vgood | 0.006839 |
| Safety != low and Persons != 2 and Buying != vhigh and Buying != high and Maint != vhigh and Maint != high and Safety != med and Lug_boot = small and Doors != 2 and Buying = med and Maint != med | good | 0.003340 |
| Safety != low and Persons != 2 and Buying != vhigh and Buying != high and Maint != vhigh and Maint != high and Safety != med and Lug_boot != small and Lug_boot = med and Doors = 2 | good | 0.002140 |
| Safety != low and Persons != 2 and Buying != vhigh and Buying != high and Maint != vhigh and Maint != high and Safety != med and Lug_boot != small and Lug_boot = med and Doors != 2 and Doors = 3 and Persons != 4 | vgood | 0.002670 |
| Safety != low and Persons != 2 and Buying != vhigh and Buying != high and Maint != vhigh and Maint != high and Safety != med and Lug_boot != small and Lug_boot = med and Doors != 2 and Doors = 3 and Persons = 4 | good | 0.001506 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Safety = low | unacc | 0.528513 |
| Persons = 2 | unacc | 0.429803 |
| Maint = vhigh and Buying = vhigh | unacc | 0.084980 |
| Buying != low and Buying != med and Maint != vhigh and Lug_boot != small and Maint != high and Safety != med | acc | 0.161473 |
| Buying = vhigh and Maint = high | unacc | 0.091723 |
| Buying = high and Maint = vhigh | unacc | 0.095768 |
| Safety = med and Lug_boot = small and Buying != high and Buying != vhigh and Maint != vhigh and Maint != high and Doors != 2 | acc | 0.097872 |
| Safety = med and Lug_boot = small and Buying != low and Doors != 2 | unacc | 0.090261 |
| Safety = med and Lug_boot = small and Maint != vhigh and Doors = 2 and Persons != 4 | unacc | 0.027919 |
| Safety = med and Lug_boot = small and Maint = vhigh | unacc | 0.020460 |
| Safety = med and Lug_boot = big and Maint != low and Buying != low | acc | 0.213198 |
| Safety = med and Lug_boot = big and Buying != med and Maint != med and Buying = low and Maint != low | acc | 0.082840 |
| Buying = high and Doors != 2 and Doors != 3 | acc | 0.175532 |
| Maint = vhigh and Doors != 2 and Safety != med | acc | 0.166667 |
| Safety = med and Lug_boot = big and Buying != vhigh and Buying != high | good | 0.083969 |
| Lug_boot = big and Safety != med and Buying != high and Maint != vhigh and Maint != high | vgood | 0.109312 |
| Doors = 2 and Lug_boot = big and Buying != low | acc | 0.086207 |
| Doors = 2 and Lug_boot != big and Buying = vhigh and Safety = med | unacc | 0.028571 |
| Doors = 2 and Lug_boot != big and Persons != 4 and Lug_boot = small | unacc | 0.051163 |
| Safety = med and Buying = high and Doors = 2 | unacc | 0.028571 |
| Safety = med and Maint = vhigh and Doors != 2 and Doors != 3 | acc | 0.087912 |
| Safety = med and Maint = vhigh and Doors = 2 | unacc | 0.020000 |
| Safety = med and Buying != low and Doors = 4 and Buying != vhigh | acc | 0.032922 |
| Safety = med and Buying != low and Doors = 5more and Maint != low | acc | 0.059524 |
| Safety = med and Buying != low and Doors != 5more and Maint != high and Doors != 3 | acc | 0.105769 |
| Safety = med and Buying = low and Maint = high | acc | 0.150538 |
| Safety != med and Lug_boot = small and Buying != low and Maint != low | acc | 0.247619 |
| Safety = med and Doors != 4 and Doors = 5more and Buying != vhigh | good | 0.044248 |
| Safety = med and Doors = 4 | good | 0.052632 |
| Safety = med and Maint = high and Persons = 4 | unacc | 0.031008 |
| Safety = med and Lug_boot != med | acc | 0.098592 |
| Safety = med and Persons != 4 and Buying != low and Maint != high | acc | 0.085714 |
| Safety = med and Buying != low and Buying = med | acc | 0.027692 |
| Safety = med and Persons != 4 | acc | 0.035165 |
| Safety = med and Buying = low | acc | 0.035165 |
| Safety != med and Lug_boot = small and Maint != high and Buying != vhigh and Buying = low | good | 0.139785 |
| Safety != med and Lug_boot = small and Buying != med | acc | 0.227273 |
| Safety != med and Lug_boot != small and Maint = low and Doors != 2 and Doors != 3 | vgood | 0.142857 |
| Safety != med and Maint = low and Doors != 3 | good | 0.109375 |
| Safety != med and Maint != low and Buying != low and Maint != med | acc | 0.357143 |
| Safety != med and Maint != vhigh and Maint != low and Doors != 2 and Doors != 3 | vgood | 0.416667 |
| Safety != med and Maint = vhigh | acc | 0.160000 |
| Safety != med and Lug_boot = big | vgood | 0.190476 |
| Safety != med and Persons = 4 and Buying != med | good | 0.140625 |
| Safety != med and Maint != low | acc | 0.166667 |
| Safety != med | vgood | 0.222222 |
|  | unacc | 0.600000 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Safety = high and Buying = low and Lug_boot = big | vgood | 0.006239 |
| Safety = high and Buying = med and Lug_boot = big | vgood | 0.003790 |
| Buying = low and Maint = low and Safety = med | good | 0.003335 |
| Maint = low and Buying = med and Persons = 4 | good | 0.002554 |
| Safety = high and Persons = 4 | acc | 0.053096 |
| Safety = med and Persons = 4 and Lug_boot = big | acc | 0.023342 |
| Persons = more and Safety = high | acc | 0.041387 |
| Safety = med and Persons = more and Lug_boot = big | acc | 0.017683 |
| Safety = med and Persons = more and Lug_boot = med | acc | 0.015804 |
| Safety = med and Persons = 4 and Buying = low | acc | 0.013087 |
| Safety = med and Persons = 4 and Maint = med | acc | 0.004829 |
|  | unacc | 0.924448 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

persons|safety|acceptability
---|---|---
more|high|acc
2|high|unacc
4|high|acc
4|med|acc
more|med|acc
2|med|unacc
2|low|unacc
more|low|unacc
4|low|unacc

## JRip

Decision list:

rules | predicted class
---|---
(Safety = high) and (Buying = low) and (Lug_boot = big)|vgood (43.0/23.0)
(Safety = high) and (Buying = med) and (Lug_boot = big)|vgood (40.0/25.0)
(Buying = low) and (Maint = low) and (Safety = med)|good (35.0/22.0)
(Maint = low) and (Buying = med) and (Persons = 4)|good (27.0/17.0)
(Safety = high) and (Persons = 4)|acc (129.0/45.0)
(Safety = med) and (Persons = 4) and (Lug_boot = big)|acc (50.0/13.0)
(Persons = more) and (Safety = high)|acc (144.0/67.0)
(Safety = med) and (Persons = more) and (Lug_boot = big)|acc (53.0/20.0)
(Safety = med) and (Persons = more) and (Lug_boot = med)|acc (55.0/24.0)
(Safety = med) and (Persons = 4) and (Buying = low)|acc (21.0/6.0)
(Safety = med) and (Persons = 4) and (Maint = med)|acc (22.0/10.0)
|unacc (933.0/20.0)


## PART

Decision list:

rules | predicted class
---|---
Safety = low|unacc (519.0)
Persons = 2|unacc (349.0)
Maint = vhigh AND Buying = vhigh|unacc (43.0)
Buying != low AND Buying != med AND Maint != vhigh AND Lug_boot != small AND Maint != high AND Safety != med|acc (57.0)
Buying = vhigh AND Maint = high|unacc (41.0)
Buying = high AND Maint = vhigh|unacc (43.0)
Safety = med AND Lug_boot = small AND Buying != high AND Buying != vhigh AND Maint != vhigh AND Maint != high AND Doors != 2|acc (23.0)
Safety = med AND Lug_boot = small AND Buying != low AND Doors != 2|unacc (38.0)
Safety = med AND Lug_boot = small AND Maint != vhigh AND Doors = 2 AND Persons != 4|unacc (11.0)
Safety = med AND Lug_boot = small AND Maint = vhigh|unacc (8.0)
Safety = med AND Lug_boot = big AND Maint != low AND Buying != low|acc (42.0)
Safety = med AND Lug_boot = big AND Buying != med AND Maint != med AND Buying = low AND Maint != low|acc (14.0)
Buying = high AND Doors != 2 AND Doors != 3|acc (33.0)
Maint = vhigh AND Doors != 2 AND Safety != med|acc (31.0)
Safety = med AND Lug_boot = big AND Buying != vhigh AND Buying != high|good (22.0)
Lug_boot = big AND Safety != med AND Buying != high AND Maint != vhigh AND Maint != high|vgood (27.0)
Doors = 2 AND Lug_boot = big AND Buying != low|acc (10.0)
Doors = 2 AND Lug_boot != big AND Buying = vhigh AND Safety = med|unacc (6.0)
Doors = 2 AND Lug_boot != big AND Persons != 4 AND Lug_boot = small|unacc (11.0)
Safety = med AND Buying = high AND Doors = 2|unacc (6.0)
Safety = med AND Maint = vhigh AND Doors != 2 AND Doors != 3|acc (8.0)
Safety = med AND Maint = vhigh AND Doors = 2|unacc (4.0)
Safety = med AND Buying != low AND Doors = 4 AND Buying != vhigh|acc (6.0/2.0)
Safety = med AND Buying != low AND Doors = 5more AND Maint != low|acc (5.0)
Safety = med AND Buying != low AND Doors != 5more AND Maint != high AND Doors != 3|acc (11.0)
Safety = med AND Buying = low AND Maint = high|acc (14.0)
Safety != med AND Lug_boot = small AND Buying != low AND Maint != low|acc (26.0)
Safety = med AND Doors != 4 AND Doors = 5more AND Buying != vhigh|good (5.0)
Safety = med AND Doors = 4|good (4.0)
Safety = med AND Maint = high AND Persons = 4|unacc (4.0)
Safety = med AND Lug_boot != med|acc (7.0)
Safety = med AND Persons != 4 AND Buying != low AND Maint != high|acc (6.0)
Safety = med AND Buying != low AND Buying = med|acc (5.0/2.0)
Safety = med AND Persons != 4|acc (6.0/2.0)
Safety = med AND Buying = low|acc (5.0/1.0)
Safety != med AND Lug_boot = small AND Maint != high AND Buying != vhigh AND Buying = low|good (13.0)
Safety != med AND Lug_boot = small AND Buying != med|acc (15.0)
Safety != med AND Lug_boot != small AND Maint = low AND Doors != 2 AND Doors != 3|vgood (8.0)
Safety != med AND Maint = low AND Doors != 3|good (7.0)
Safety != med AND Maint != low AND Buying != low AND Maint != med|acc (20.0)
Safety != med AND Maint != vhigh AND Maint != low AND Doors != 2 AND Doors != 3|vgood (15.0)
Safety != med AND Maint = vhigh|acc (4.0)
Safety != med AND Lug_boot = big|vgood (4.0)
Safety != med AND Persons = 4 AND Buying != med|good (4.0/1.0)
Safety != med AND Maint != low|acc (5.0/2.0)
Safety != med|vgood (4.0/2.0)
|unacc (3.0)


## J48 Decision Tree

* Safety = low: unacc (425.0)
* Safety != low
	* Persons = 2: unacc (278.0)
	* Persons != 2
		* Buying = vhigh
			* Maint = high: unacc (35.0)
			* Maint != high
				* Maint = vhigh: unacc (31.0)
				* Maint != vhigh
					* Lug_boot = big: acc (24.0)
					* Lug_boot != big
						* Safety = med: unacc (21.0/6.0)
						* Safety != med: acc (24.0/2.0)
		* Buying != vhigh
			* Buying = high
				* Maint = vhigh: unacc (36.0)
				* Maint != vhigh
					* Lug_boot = small
						* Safety = med: unacc (13.0)
						* Safety != med: acc (16.0/2.0)
					* Lug_boot != small: acc (70.0/6.0)
			* Buying != high
				* Maint = vhigh
					* Lug_boot = big: acc (21.0)
					* Lug_boot != big
						* Safety = med
							* Doors = 2: unacc (6.0)
							* Doors != 2
								* Lug_boot = small: unacc (4.0)
								* Lug_boot != small: acc (7.0/1.0)
						* Safety != med: acc (26.0/2.0)
				* Maint != vhigh
					* Maint = high
						* Lug_boot = small
							* Safety = med: unacc (13.0/6.0)
							* Safety != med: acc (14.0/1.0)
						* Lug_boot != small
							* Buying = med: acc (22.0/1.0)
							* Buying != med
								* Safety = med: acc (11.0)
								* Safety != med: vgood (8.0/2.0)
					* Maint != high
						* Safety = med
							* Lug_boot = small: acc (23.0/4.0)
							* Lug_boot != small
								* Buying = med
									* Maint = med: acc (10.0)
									* Maint != med: good (11.0/2.0)
								* Buying != med: good (24.0/4.0)
						* Safety != med
							* Lug_boot = small
								* Doors = 2: unacc (5.0/2.0)
								* Doors != 2
									* Buying = med
										* Maint = med: acc (5.0)
										* Maint != med: good (3.0)
									* Buying != med: good (8.0)
							* Lug_boot != small
								* Lug_boot = med
									* Doors = 2: good (5.0/1.0)
									* Doors != 2
										* Doors = 3
											* Persons = 4: good (3.0/1.0)
											* Persons != 4: vgood (3.0)
										* Doors != 3: vgood (13.0)
								* Lug_boot != med: vgood (24.0)


## SimpleCart Decision Tree

	* Safety=(high)|(med)
		* Persons=(more)|(4)
			* Buying=(low)|(med)
				* Maint=(low)|(med)
				* Safety=(high)
						* Lug_boot=(big)|(med)
							* Doors=(5more)|(4): vgood(28.0/0.0)
							* Doors!=(5more)|(4)
								* Lug_boot=(big)|(small): vgood(14.0/0.0)
								* Lug_boot!=(big)|(small)
								* Persons=(more): vgood(4.0/1.0)
								* Persons!=(more): good(6.0/2.0)
						* Lug_boot!=(big)|(med)
								* Buying=(low)|(vhigh)|(high): good(13.0/2.0)
								* Buying!=(low)|(vhigh)|(high)
							* Maint=(low): good(5.0/1.0)
							* Maint!=(low): acc(7.0/0.0)
				* Safety!=(high)
						* Lug_boot=(big)|(med)
								* Buying=(low)|(vhigh)|(high)
								* Doors=(5more)|(4): good(16.0/0.0)
								* Doors!=(5more)|(4)
								* Lug_boot=(big): good(6.0/0.0)
								* Lug_boot!=(big): acc(6.0/2.0)
								* Buying!=(low)|(vhigh)|(high)
							* Maint=(low)
									* Lug_boot=(big)|(small): good(8.0/0.0)
									* Lug_boot!=(big)|(small): acc(3.0/3.0)
							* Maint!=(low): acc(15.0/0.0)
						* Lug_boot!=(big)|(med)
								* Doors=(5more)|(4)|(3): acc(23.0/0.0)
								* Doors!=(5more)|(4)|(3): unacc(4.0/4.0)
				* Maint!=(low)|(med)
					* Lug_boot=(big)|(med)
					* Safety=(high)
								* Maint=(high)|(med)|(low)
									* Buying=(low)|(vhigh)|(high): vgood(12.0/2.0)
									* Buying!=(low)|(vhigh)|(high): acc(14.0/0.0)
								* Maint!=(high)|(med)|(low): acc(28.0/0.0)
					* Safety!=(high)
							* Doors=(5more)|(4): acc(30.0/0.0)
							* Doors!=(5more)|(4)
							* Lug_boot=(big): acc(15.0/0.0)
							* Lug_boot!=(big)
										* Buying=(low)|(vhigh)|(high): acc(5.0/3.0)
										* Buying!=(low)|(vhigh)|(high): unacc(6.0/2.0)
					* Lug_boot!=(big)|(med)
						* Safety=(high)|(low)
								* Doors=(5more)|(4)|(3): acc(23.0/0.0)
								* Doors!=(5more)|(4)|(3): unacc(4.0/2.0)
						* Safety!=(high)|(low)
						* Buying=(low)
									* Maint=(high)|(med)|(low): acc(6.0/1.0)
									* Maint!=(high)|(med)|(low): unacc(6.0/0.0)
						* Buying!=(low): unacc(15.0/0.0)
			* Buying!=(low)|(med)
				* Maint=(low)|(med)
					* Lug_boot=(big)|(med)
						* Safety=(high)|(low): acc(57.0/0.0)
						* Safety!=(high)|(low)
							* Lug_boot=(big)|(small): acc(27.0/0.0)
							* Lug_boot!=(big)|(small)
								* Doors=(5more)|(4): acc(13.0/0.0)
								* Doors!=(5more)|(4)
								* Doors=(3): unacc(3.0/3.0)
								* Doors!=(3): unacc(7.0/0.0)
					* Lug_boot!=(big)|(med)
					* Safety=(high)
								* Doors=(5more)|(4)|(3): acc(22.0/0.0)
								* Doors!=(5more)|(4)|(3): unacc(3.0/2.0)
					* Safety!=(high): unacc(28.0/0.0)
				* Maint!=(low)|(med)
						* Maint=(high)|(med)|(low)
							* Buying=(high)|(med)|(low)
							* Lug_boot=(big)|(med)
								* Safety=(high)|(low): acc(16.0/0.0)
								* Safety!=(high)|(low)
									* Doors=(5more)|(4): acc(7.0/0.0)
									* Doors!=(5more)|(4): acc(5.0/3.0)
							* Lug_boot!=(big)|(med)
								* Safety=(high)|(low): acc(6.0/1.0)
								* Safety!=(high)|(low): unacc(7.0/0.0)
							* Buying!=(high)|(med)|(low): unacc(41.0/0.0)
						* Maint!=(high)|(med)|(low): unacc(86.0/0.0)
		* Persons!=(more)|(4): unacc(349.0/0.0)
	* Safety!=(high)|(med): unacc(519.0/0.0)


