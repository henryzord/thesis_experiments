# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Safety != high | unacc | 0.614024 |
| Persons = 2 | unacc | 0.523614 |
| Persons != 2 and Safety != low and Maint != vhigh and Buying != low and Buying != med and Lug_boot != small and Maint != high and Safety != med | acc | 0.045814 |
| Persons != 2 and Safety != low and Maint = vhigh and Buying != vhigh and Buying != high and Safety != med | acc | 0.032070 |
| Persons != 2 and Safety != low and Maint != vhigh and Buying != low and Buying != med and Lug_boot != small and Maint != high and Safety = med and Lug_boot != med | acc | 0.022654 |
| Persons != 2 and Safety != low and Maint != vhigh and Buying != low and Buying != med and Lug_boot != small and Maint = high and Buying != vhigh | acc | 0.019724 |
| Safety != med | unacc | 0.592317 |
| Persons != 2 and Safety != low and Maint != vhigh and Buying != low and Buying != med and Lug_boot = small and Safety != med and Maint != high and Doors != 2 | acc | 0.017087 |
| Persons != 2 and Safety != low and Maint != vhigh and Buying != low and Buying = med and Maint != low and Safety != med and Maint = high | acc | 0.017087 |
| Persons != 2 and Safety != low and Maint != vhigh and Buying = low and Safety = med and Lug_boot = small | acc | 0.013406 |
| Persons != 2 and Safety != low and Maint != vhigh and Buying != low and Buying != med and Lug_boot != small and Maint != high and Safety = med and Lug_boot = med and Doors != 2 | acc | 0.010492 |
| Persons != 2 and Safety != low and Maint != vhigh and Buying = low and Safety = med and Lug_boot != small and Maint = high | acc | 0.012265 |
| Persons != 2 and Safety != low and Maint != vhigh and Buying != low and Buying = med and Maint != low and Safety = med and Lug_boot != big and Maint != high | acc | 0.011508 |
| Persons != 2 and Safety != low and Maint != vhigh and Buying = low and Safety != med and Lug_boot != small and Lug_boot != med | vgood | 0.013210 |
| Persons != 2 and Safety != low and Maint != vhigh and Buying = low and Safety = med and Lug_boot != small and Maint != high | good | 0.012707 |
| Persons != 2 and Safety != low and Maint != vhigh and Buying != low and Buying = med and Maint != low and Safety = med and Lug_boot = big | acc | 0.011457 |
| Persons != 2 and Safety != low and Maint = vhigh and Buying != vhigh and Buying != high and Safety = med and Lug_boot != small and Lug_boot != med | acc | 0.011457 |
| Persons != 2 and Safety != low and Maint = vhigh and Buying != vhigh and Buying != high and Safety = med and Lug_boot != small and Lug_boot = med and Doors != 2 | acc | 0.006853 |
| Persons != 2 and Safety != low and Maint != vhigh and Buying = low and Safety != med and Lug_boot != small and Lug_boot = med and Doors != 2 | vgood | 0.007661 |
| Persons != 2 and Safety != low and Maint != vhigh and Buying = low and Safety != med and Lug_boot = small and Maint != high | good | 0.007365 |
| Persons != 2 and Safety != low and Maint != vhigh and Buying = low and Safety != med and Lug_boot = small and Maint = high | acc | 0.005761 |
| Persons != 2 and Safety != low and Maint != vhigh and Buying != low and Buying = med and Maint != low and Safety != med and Maint != high and Lug_boot != small | vgood | 0.006387 |
| Persons != 2 and Safety != low and Maint != vhigh and Buying != low and Buying = med and Maint != low and Safety != med and Maint != high and Lug_boot = small | acc | 0.004240 |
| Persons != 2 and Safety != low and Maint != vhigh and Buying != low and Buying = med and Maint = low and Safety = med | good | 0.004810 |
| Persons != 2 and Safety != low and Maint != vhigh and Buying != low and Buying = med and Maint = low and Safety != med | vgood | 0.005369 |
| Persons != 2 and Safety != low and Maint != vhigh and Buying != low and Buying = med and Maint != low and Safety = med and Lug_boot != big and Maint = high and Lug_boot != small and Doors != 2 | acc | 0.002642 |
| Persons != 2 and Safety != low and Maint != vhigh and Buying != low and Buying != med and Lug_boot = small and Safety != med and Maint != high and Doors = 2 and Persons = 4 | acc | 0.002477 |
| Safety = med and Persons = 4 and Buying = med and Maint != med and Safety!=(high) and Lug_boot = med | acc | 0.001883 |
| Safety = med and Persons = 4 and Buying != med and Maint = med and Safety!=(high) and Lug_boot = med | acc | 0.001883 |
| Persons != 2 and Safety != low and Maint != vhigh and Buying = low and Safety != med and Lug_boot != small and Lug_boot = med and Doors = 2 | good | 0.001205 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Safety = low | unacc | 0.529412 |
| Persons = 2 | unacc | 0.417817 |
| Buying = vhigh and Maint = vhigh | unacc | 0.090196 |
| Safety = med and Lug_boot = small and Buying = high | unacc | 0.060729 |
| Buying = high and Maint = vhigh | unacc | 0.077535 |
| Safety = med and Lug_boot = small and Buying = vhigh | unacc | 0.045267 |
| Safety = med and Maint = high and Buying = low | acc | 0.084938 |
| Buying = high and Safety = high | acc | 0.217450 |
| Safety = med and Maint = high and Buying = high | acc | 0.046737 |
| Safety = med and Maint = high and Buying = vhigh | unacc | 0.039063 |
| Safety = med and Lug_boot = big and Buying = vhigh | acc | 0.065116 |
| Safety = med and Lug_boot = big and Buying = high | acc | 0.065116 |
| Safety = med and Lug_boot = big and Maint = vhigh | acc | 0.065116 |
| Safety = med and Lug_boot = big and Buying = low | good | 0.038567 |
| Safety = med and Maint = vhigh and Lug_boot = small | unacc | 0.048632 |
| Buying = vhigh and Maint = med | acc | 0.116753 |
| Safety = med and Lug_boot = small and Maint = med | acc | 0.066940 |
| Maint = vhigh | acc | 0.208581 |
| Buying = high and Persons = 4 | unacc | 0.017778 |
| Buying = vhigh and Maint = low | acc | 0.115869 |
| Buying = vhigh | unacc | 0.135965 |
| Safety = med and Maint = med and Buying = med | acc | 0.088889 |
| Safety = med and Maint = high and Lug_boot = big | acc | 0.056338 |
| Safety = med and Lug_boot = small and Maint = low | acc | 0.065089 |
| Safety = med and Lug_boot = med and Doors = 5more | good | 0.020408 |
| Safety = med and Lug_boot = med and Doors = 2 | acc | 0.014401 |
| Safety = med and Lug_boot = med and Maint = low | good | 0.019640 |
| Safety = med and Lug_boot = med | acc | 0.055856 |
| Safety = med and Maint = high | unacc | 0.082759 |
| Maint = high and Buying = med | acc | 0.160305 |
| Lug_boot = big and Safety = high | vgood | 0.333333 |
| Lug_boot = med and Doors = 5more | vgood | 0.125000 |
| Maint = high | acc | 0.114155 |
| Lug_boot = small and Buying = low | good | 0.187500 |
| Maint = low and Lug_boot = big | good | 0.148936 |
| Lug_boot = med and Doors = 3 | vgood | 0.053419 |
| Maint = low and Doors = 2 | good | 0.071429 |
| Lug_boot = med | vgood | 0.111111 |
|  | acc | 0.250000 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Safety = high and Persons = 4 | acc | 0.044035 |
| Persons = more and Safety = high and Buying = high | acc | 0.015635 |
| Safety = med and Persons = more and Lug_boot = big | acc | 0.018381 |
| Safety = med and Persons = 4 and Buying = low | acc | 0.015306 |
| Safety = med and Persons = 4 and Lug_boot = big | acc | 0.012105 |
| Persons = more and Safety = high and Buying = med | acc | 0.011963 |
| Persons = more and Safety = high and Buying = vhigh and Maint = low | acc | 0.007470 |
| Safety = med and Persons = more and Lug_boot = med | acc | 0.014081 |
| Safety = med and Persons = 4 and Buying = med | acc | 0.006427 |
|  | unacc | 0.869114 |


# Text representation of classifiers as-is

## JRip

Decision list:

rules | predicted class
---|---
(Safety = high) and (Persons = 4)|acc (174.0/77.0)
(Persons = more) and (Safety = high) and (Buying = high)|acc (41.0/13.0)
(Safety = med) and (Persons = more) and (Lug_boot = big)|acc (61.0/24.0)
(Safety = med) and (Persons = 4) and (Buying = low)|acc (45.0/16.0)
(Safety = med) and (Persons = 4) and (Lug_boot = big)|acc (40.0/14.0)
(Persons = more) and (Safety = high) and (Buying = med)|acc (43.0/18.0)
(Persons = more) and (Safety = high) and (Buying = vhigh) and (Maint = low)|acc (11.0/1.0)
(Safety = med) and (Persons = more) and (Lug_boot = med)|acc (60.0/28.0)
(Safety = med) and (Persons = 4) and (Buying = med)|acc (30.0/14.0)
|unacc (1048.0/68.0)


## PART

Decision list:

rules | predicted class
---|---
Safety = low|unacc (522.0)
Persons = 2|unacc (333.0)
Buying = vhigh AND Maint = vhigh|unacc (46.0)
Safety = med AND Lug_boot = small AND Buying = high|unacc (30.0)
Buying = high AND Maint = vhigh|unacc (39.0)
Safety = med AND Lug_boot = small AND Buying = vhigh|unacc (22.0)
Safety = med AND Maint = high AND Buying = low|acc (22.0/1.0)
Buying = high AND Safety = high|acc (62.0/1.0)
Safety = med AND Maint = high AND Buying = high|acc (16.0/3.0)
Safety = med AND Maint = high AND Buying = vhigh|unacc (15.0)
Safety = med AND Lug_boot = big AND Buying = vhigh|acc (14.0)
Safety = med AND Lug_boot = big AND Buying = high|acc (14.0)
Safety = med AND Lug_boot = big AND Maint = vhigh|acc (14.0)
Safety = med AND Lug_boot = big AND Buying = low|good (14.0)
Safety = med AND Maint = vhigh AND Lug_boot = small|unacc (16.0)
Buying = vhigh AND Maint = med|acc (30.0/4.0)
Safety = med AND Lug_boot = small AND Maint = med|acc (16.0/2.0)
Maint = vhigh|acc (58.0/7.0)
Buying = high AND Persons = 4|unacc (7.0/3.0)
Buying = vhigh AND Maint = low|acc (29.0/4.0)
Buying = vhigh|unacc (23.0)
Safety = med AND Maint = med AND Buying = med|acc (14.0)
Safety = med AND Maint = high AND Lug_boot = big|acc (8.0)
Safety = med AND Lug_boot = small AND Maint = low|acc (13.0/2.0)
Safety = med AND Lug_boot = med AND Doors = 5more|good (10.0/4.0)
Safety = med AND Lug_boot = med AND Doors = 2|acc (9.0/4.0)
Safety = med AND Lug_boot = med AND Maint = low|good (9.0/3.0)
Safety = med AND Lug_boot = med|acc (8.0/4.0)
Safety = med AND Maint = high|unacc (7.0)
Maint = high AND Buying = med|acc (21.0)
Lug_boot = big AND Safety = high|vgood (35.0)
Lug_boot = med AND Doors = 5more|vgood (10.0)
Maint = high|acc (12.0/2.0)
Lug_boot = small AND Buying = low|good (13.0/1.0)
Maint = low AND Lug_boot = big|good (7.0)
Lug_boot = med AND Doors = 3|vgood (8.0/4.0)
Maint = low AND Doors = 2|good (6.0/1.0)
Lug_boot = med|vgood (11.0/3.0)
|acc (10.0/4.0)


## J48 Decision Tree

* Persons = 2: unacc (448.0)
* Persons != 2
	* Safety = low: unacc (288.0)
	* Safety != low
		* Maint = vhigh
			* Buying = vhigh: unacc (38.0)
			* Buying != vhigh
				* Buying = high: unacc (38.0)
				* Buying != high
					* Safety = med
						* Lug_boot = small: unacc (14.0)
						* Lug_boot != small
							* Lug_boot = med
								* Doors = 2: unacc (3.0)
								* Doors != 2: acc (9.0/2.0)
							* Lug_boot != med: acc (11.0)
					* Safety != med: acc (36.0/1.0)
		* Maint != vhigh
			* Buying = low
				* Safety = med
					* Lug_boot = small: acc (19.0/3.0)
					* Lug_boot != small
						* Maint = high: acc (14.0)
						* Maint != high: good (28.0/6.0)
				* Safety != med
					* Lug_boot = small
						* Maint = high: acc (5.0)
						* Maint != high: good (10.0/1.0)
					* Lug_boot != small
						* Lug_boot = med
							* Doors = 2: good (3.0/1.0)
							* Doors != 2: vgood (16.0/3.0)
						* Lug_boot != med: vgood (18.0)
			* Buying != low
				* Buying = med
					* Maint = low
						* Safety = med: good (18.0/8.0)
						* Safety != med: vgood (17.0/7.0)
					* Maint != low
						* Safety = med
							* Lug_boot = big: acc (13.0)
							* Lug_boot != big
								* Maint = high
									* Lug_boot = small: unacc (4.0)
									* Lug_boot != small
										* Doors = 2: unacc (2.0)
										* Doors != 2: acc (4.0/1.0)
								* Maint != high: acc (13.0/1.0)
						* Safety != med
							* Maint = high: acc (19.0)
							* Maint != high
								* Lug_boot = small: acc (6.0/1.0)
								* Lug_boot != small: vgood (13.0/3.0)
				* Buying != med
					* Lug_boot = small
						* Safety = med: unacc (37.0)
						* Safety != med
							* Maint = high: unacc (15.0/7.0)
							* Maint != high
								* Doors = 2
									* Persons = 4: acc (3.0)
									* Persons != 4: unacc (2.0)
								* Doors != 2: acc (17.0)
					* Lug_boot != small
						* Maint = high
							* Buying = vhigh: unacc (27.0)
							* Buying != vhigh: acc (25.0/2.0)
						* Maint != high
							* Safety = med
								* Lug_boot = med
									* Doors = 2: unacc (7.0)
									* Doors != 2: acc (19.0/4.0)
								* Lug_boot != med: acc (23.0)
							* Safety != med: acc (50.0)


## SimpleCart Decision Tree

	* Safety=(high)|(med)
		* Persons=(more)|(4)
			* Buying=(low)|(med)
				* Maint=(low)|(med)
				* Safety=(high)
						* Lug_boot=(big)|(med): vgood(48.0/11.0)
						* Lug_boot!=(big)|(med): good(16.0/9.0)
				* Safety!=(high)
						* Lug_boot=(big)|(med)
								* Maint=(low)|(vhigh)|(high): good(24.0/5.0)
								* Maint!=(low)|(vhigh)|(high)
									* Buying=(low)|(vhigh)|(high): good(12.0/3.0)
									* Buying!=(low)|(vhigh)|(high): acc(14.0/0.0)
						* Lug_boot!=(big)|(med): acc(25.0/4.0)
				* Maint!=(low)|(med)
				* Safety=(high): acc(72.0/12.0)
				* Safety!=(high)
						* Lug_boot=(big)|(med): acc(51.0/9.0)
						* Lug_boot!=(big)|(med): unacc(24.0/6.0)
			* Buying!=(low)|(med)
				* Maint=(low)|(med)
				* Safety=(high): acc(82.0/3.0)
				* Safety!=(high)
						* Lug_boot=(big)|(med): acc(44.0/12.0)
						* Lug_boot!=(big)|(med): unacc(30.0/0.0)
				* Maint!=(low)|(med)
				* Maint=(high)
							* Buying=(high)|(med)|(low): acc(34.0/11.0)
							* Buying!=(high)|(med)|(low): unacc(45.0/0.0)
				* Maint!=(high): unacc(92.0/0.0)
		* Persons!=(more)|(4): unacc(333.0/0.0)
	* Safety!=(high)|(med): unacc(522.0/0.0)


