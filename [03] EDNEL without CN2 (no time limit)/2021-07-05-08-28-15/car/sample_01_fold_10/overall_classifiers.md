# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | unacc | 0.701223 |
| Persons = 4 and Safety = high | acc | 0.044299 |
| Persons = 4 and Safety = med | acc | 0.032673 |
| Persons = more and Safety = med | acc | 0.031585 |
| Persons = more and Safety = high | acc | 0.034903 |
| Safety != low and Persons != 2 and Buying != vhigh and Maint != vhigh and Buying != high and Lug_boot != small and Safety != med and Maint != high and Lug_boot != med | vgood | 0.019041 |
| Safety != low and Persons != 2 and Buying != vhigh and Maint != vhigh and Buying != high and Lug_boot != small and Safety = med and Maint != high and Maint != med | good | 0.012080 |
| Safety != low and Persons != 2 and Buying != vhigh and Maint != vhigh and Buying != high and Lug_boot != small and Safety != med and Maint != high and Lug_boot = med and Doors != 2 | vgood | 0.009766 |
| Safety != low and Persons != 2 and Buying != vhigh and Maint != vhigh and Buying != high and Lug_boot = small and Safety != med and Doors != 2 and Maint != high and Maint != med | good | 0.007973 |
| Safety != low and Persons != 2 and Buying != vhigh and Maint != vhigh and Buying != high and Lug_boot != small and Safety != med and Maint = high and Buying != med | vgood | 0.006387 |
| Safety != low and Persons != 2 and Buying != vhigh and Maint != vhigh and Buying != high and Lug_boot != small and Safety != med and Maint != high and Lug_boot = med and Doors = 2 | good | 0.001784 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Safety = low | unacc | 0.530364 |
| Persons = 2 | unacc | 0.422167 |
| Buying = vhigh and Maint = high | unacc | 0.086614 |
| Buying = high and Maint = vhigh | unacc | 0.086614 |
| Safety = med and Lug_boot = small and Buying = low | acc | 0.043666 |
| Buying = high and Safety = high | acc | 0.187147 |
| Safety = med and Lug_boot = small and Buying = vhigh | unacc | 0.051852 |
| Safety = med and Lug_boot = small and Buying = high | unacc | 0.054187 |
| Safety = med and Maint = high and Lug_boot = big | acc | 0.093220 |
| Safety = med and Maint = high and Lug_boot = small | unacc | 0.024259 |
| Buying = high and Lug_boot = big | acc | 0.072398 |
| Maint = vhigh and Buying = low | acc | 0.109031 |
| Buying = high and Doors = 3 | acc | 0.007317 |
| Buying = high and Doors = 4 | acc | 0.028436 |
| Buying = vhigh and Maint = vhigh | unacc | 0.097923 |
| Buying = vhigh | acc | 0.251187 |
| Safety = med and Buying = low and Lug_boot = med | acc | 0.039075 |
| Buying = high and Doors = 2 | unacc | 0.037975 |
| Buying = low and Safety = high and Lug_boot = big | vgood | 0.093617 |
| Buying = med and Maint = high | acc | 0.117078 |
| Safety = med and Buying = med and Maint = med | acc | 0.124506 |
| Maint = vhigh and Safety = high | acc | 0.125259 |
| Safety = med and Buying = low | good | 0.105447 |
| Safety = med and Maint = vhigh and Lug_boot = big | acc | 0.062992 |
| Safety = med and Maint = vhigh | unacc | 0.135870 |
| Lug_boot = big and Safety = high | vgood | 0.132743 |
| Lug_boot = small | acc | 0.099176 |
| Safety = med and Buying = med | good | 0.097826 |
| Doors = 4 | vgood | 0.073370 |
| Safety = high | vgood | 0.080861 |
|  | acc | 0.253731 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Safety = high and Buying = low and Lug_boot = big and Persons = 4 | vgood | 0.005374 |
| Safety = high and Buying = low and Persons = more and Lug_boot = big | vgood | 0.005754 |
| Safety = high and Buying = med and Lug_boot = big and Maint = low | vgood | 0.003271 |
| Safety = high and Buying = med and Maint = med and Persons = more | vgood | 0.002730 |
| Safety = high and Lug_boot = med and Buying = low and Persons = 4 and Doors = 5more | vgood | 0.001504 |
| Safety = high and Lug_boot = med and Buying = low and Persons = more | vgood | 0.002854 |
| Safety = high and Buying = med and Maint = med and Persons = 4 and Lug_boot = big | vgood | 0.002670 |
| Safety = high and Lug_boot = med and Doors = 4 and Persons = 4 and Buying = low | vgood | 0.001504 |
| Buying = low and Maint = med and Safety = high and Persons = 4 | good | 0.003463 |
| Buying = low and Persons = more and Maint = med and Safety = med | good | 0.003089 |
| Maint = low and Buying = low and Lug_boot = big and Safety = med | good | 0.003089 |
| Maint = low and Buying = med and Lug_boot = big and Safety = med | good | 0.003089 |
| Maint = low and Buying = med and Safety = high and Persons = 4 | good | 0.002477 |
| Buying = low and Maint = low and Safety = high and Persons = 4 | good | 0.002772 |
| Maint = low and Persons = more and Buying = med and Safety = high | good | 0.001587 |
| Buying = low and Maint = low and Persons = more and Safety = high | good | 0.002219 |
| Buying = low and Maint = med and Safety = high and Persons = more | good | 0.002219 |
| Safety = med and Lug_boot = med and Maint = low and Persons = more and Buying = low | good | 0.001561 |
| Safety = med and Buying = low and Maint = med and Persons = 4 and Lug_boot = big | good | 0.001388 |
| Safety = med and Lug_boot = med and Maint = low and Buying = med and Persons = more | good | 0.001561 |
| Safety = high and Persons = 4 and Buying = med | acc | 0.022500 |
| Safety = high and Persons = 4 and Maint = med | acc | 0.016159 |
| Persons = more and Safety = high and Maint = low | acc | 0.012986 |
| Safety = med and Lug_boot = big and Persons = more | acc | 0.028067 |
| Persons = 4 and Safety = med and Lug_boot = big and Maint = med | acc | 0.009910 |
| Safety = med and Persons = 4 and Buying = low | acc | 0.018953 |
| Safety = high and Persons = more and Maint = med | acc | 0.018384 |
| Safety = high and Persons = 4 and Maint = low | acc | 0.017150 |
| Safety = med and Persons = 4 and Lug_boot = big and Maint = low | acc | 0.007227 |
| Safety = med and Persons = 4 and Buying = med | acc | 0.012145 |
| Persons = more and Safety = high and Buying = med | acc | 0.012986 |
| Maint = high and Safety = high and Buying = high | acc | 0.012816 |
| Persons = more and Safety = med and Lug_boot = med and Doors = 4 | acc | 0.006658 |
| Persons = more and Safety = med and Buying = low and Maint = high | acc | 0.003778 |
| Persons = 4 and Safety = high and Buying = low | acc | 0.015233 |
| Safety = med and Persons = 4 and Doors = 4 and Lug_boot = med | acc | 0.002525 |
| Safety = med and Persons = more and Buying = med and Maint = med | acc | 0.004658 |
| Safety = med and Persons = 4 and Maint = high and Buying = high and Lug_boot = big | acc | 0.003626 |
| Persons = more and Safety = high and Buying = low | acc | 0.009819 |
| Doors = 5more and Safety = med and Persons = 4 and Lug_boot = med | acc | 0.002070 |
| Safety = med and Persons = more and Doors = 5more and Maint = low | acc | 0.002904 |
| Persons = more and Safety = med and Lug_boot = med and Doors = 3 | acc | 0.003630 |
|  | unacc | 0.981081 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

persons|safety|acceptability
---|---|---
2|high|unacc
more|high|acc
4|high|acc
2|med|unacc
4|med|acc
more|med|acc
2|low|unacc
4|low|unacc
more|low|unacc

## JRip

Decision list:

rules | predicted class
---|---
(Safety = high) and (Buying = low) and (Lug_boot = big) and (Persons = 4)|vgood (15.0/4.0)
(Safety = high) and (Buying = low) and (Persons = more) and (Lug_boot = big)|vgood (14.0/3.0)
(Safety = high) and (Buying = med) and (Lug_boot = big) and (Maint = low)|vgood (10.0/3.0)
(Safety = high) and (Buying = med) and (Maint = med) and (Persons = more)|vgood (12.0/5.0)
(Safety = high) and (Lug_boot = med) and (Buying = low) and (Persons = 4) and (Doors = 5more)|vgood (4.0/1.0)
(Safety = high) and (Lug_boot = med) and (Buying = low) and (Persons = more)|vgood (15.0/7.0)
(Safety = high) and (Buying = med) and (Maint = med) and (Persons = 4) and (Lug_boot = big)|vgood (4.0/0.0)
(Safety = high) and (Lug_boot = med) and (Doors = 4) and (Persons = 4) and (Buying = low)|vgood (4.0/1.0)
(Buying = low) and (Maint = med) and (Safety = high) and (Persons = 4)|good (5.0/0.0)
(Buying = low) and (Persons = more) and (Maint = med) and (Safety = med)|good (11.0/4.0)
(Maint = low) and (Buying = low) and (Lug_boot = big) and (Safety = med)|good (11.0/4.0)
(Maint = low) and (Buying = med) and (Lug_boot = big) and (Safety = med)|good (11.0/4.0)
(Maint = low) and (Buying = med) and (Safety = high) and (Persons = 4)|good (7.0/2.0)
(Buying = low) and (Maint = low) and (Safety = high) and (Persons = 4)|good (4.0/0.0)
(Maint = low) and (Persons = more) and (Buying = med) and (Safety = high)|good (7.0/3.0)
(Buying = low) and (Maint = low) and (Persons = more) and (Safety = high)|good (4.0/1.0)
(Buying = low) and (Maint = med) and (Safety = high) and (Persons = more)|good (4.0/1.0)
(Safety = med) and (Lug_boot = med) and (Maint = low) and (Persons = more) and (Buying = low)|good (4.0/1.0)
(Safety = med) and (Buying = low) and (Maint = med) and (Persons = 4) and (Lug_boot = big)|good (2.0/0.0)
(Safety = med) and (Lug_boot = med) and (Maint = low) and (Buying = med) and (Persons = more)|good (4.0/1.0)
(Safety = high) and (Persons = 4) and (Buying = med)|acc (29.0/1.0)
(Safety = high) and (Persons = 4) and (Maint = med)|acc (19.0/0.0)
(Persons = more) and (Safety = high) and (Maint = low)|acc (21.0/2.0)
(Safety = med) and (Lug_boot = big) and (Persons = more)|acc (48.0/9.0)
(Persons = 4) and (Safety = med) and (Lug_boot = big) and (Maint = med)|acc (11.0/0.0)
(Safety = med) and (Persons = 4) and (Buying = low)|acc (37.0/9.0)
(Safety = high) and (Persons = more) and (Maint = med)|acc (22.0/2.0)
(Safety = high) and (Persons = 4) and (Maint = low)|acc (21.0/0.0)
(Safety = med) and (Persons = 4) and (Lug_boot = big) and (Maint = low)|acc (8.0/0.0)
(Safety = med) and (Persons = 4) and (Buying = med)|acc (36.0/14.0)
(Persons = more) and (Safety = high) and (Buying = med)|acc (21.0/2.0)
(Maint = high) and (Safety = high) and (Buying = high)|acc (31.0/10.0)
(Persons = more) and (Safety = med) and (Lug_boot = med) and (Doors = 4)|acc (11.0/2.0)
(Persons = more) and (Safety = med) and (Buying = low) and (Maint = high)|acc (6.0/1.0)
(Persons = 4) and (Safety = high) and (Buying = low)|acc (11.0/0.0)
(Safety = med) and (Persons = 4) and (Doors = 4) and (Lug_boot = med)|acc (7.0/2.0)
(Safety = med) and (Persons = more) and (Buying = med) and (Maint = med)|acc (7.0/1.0)
(Safety = med) and (Persons = 4) and (Maint = high) and (Buying = high) and (Lug_boot = big)|acc (4.0/0.0)
(Persons = more) and (Safety = high) and (Buying = low)|acc (8.0/2.0)
(Doors = 5more) and (Safety = med) and (Persons = 4) and (Lug_boot = med)|acc (8.0/3.0)
(Safety = med) and (Persons = more) and (Doors = 5more) and (Maint = low)|acc (5.0/1.0)
(Persons = more) and (Safety = med) and (Lug_boot = med) and (Doors = 3)|acc (9.0/3.0)
|unacc (1021.0/6.0)


## PART

Decision list:

rules | predicted class
---|---
Safety = low|unacc (452.0)
Persons = 2|unacc (300.0)
Buying = vhigh AND Maint = high|unacc (41.0)
Buying = high AND Maint = vhigh|unacc (42.0)
Safety = med AND Lug_boot = small AND Buying = low|acc (26.0/9.0)
Buying = high AND Safety = high|acc (63.0/3.0)
Safety = med AND Lug_boot = small AND Buying = vhigh|unacc (18.0)
Safety = med AND Lug_boot = small AND Buying = high|unacc (18.0)
Safety = med AND Maint = high AND Lug_boot = big|acc (22.0)
Safety = med AND Maint = high AND Lug_boot = small|unacc (8.0)
Buying = high AND Lug_boot = big|acc (13.0)
Maint = vhigh AND Buying = low|acc (33.0/4.0)
Buying = high AND Doors = 3|acc (5.0/2.0)
Buying = high AND Doors = 4|acc (5.0)
Buying = vhigh AND Maint = vhigh|unacc (29.0)
Buying = vhigh|acc (53.0/5.0)
Safety = med AND Buying = low AND Lug_boot = med|acc (18.0/9.0)
Buying = high AND Doors = 2|unacc (4.0)
Buying = low AND Safety = high AND Lug_boot = big|vgood (19.0)
Buying = med AND Maint = high|acc (25.0/4.0)
Safety = med AND Buying = med AND Maint = med|acc (18.0/1.0)
Maint = vhigh AND Safety = high|acc (18.0)
Safety = med AND Buying = low|good (12.0)
Safety = med AND Maint = vhigh AND Lug_boot = big|acc (8.0)
Safety = med AND Maint = vhigh|unacc (11.0/3.0)
Lug_boot = big AND Safety = high|vgood (12.0)
Lug_boot = small|acc (37.0/21.0)
Safety = med AND Buying = med|good (14.0/3.0)
Doors = 4|vgood (8.0)
Safety = high|vgood (23.0/11.0)
|acc (4.0)


## J48 Decision Tree

* Safety = low: unacc (423.0)
* Safety != low
	* Persons = 2: unacc (268.0)
	* Persons != 2
		* Buying = vhigh
			* Maint = high: unacc (36.0)
			* Maint != high
				* Maint = vhigh: unacc (29.0)
				* Maint != vhigh
					* Lug_boot = small
						* Safety = med: unacc (14.0)
						* Safety != med: acc (10.0/2.0)
					* Lug_boot != small: acc (49.0/3.0)
		* Buying != vhigh
			* Maint = vhigh
				* Buying = high: unacc (35.0)
				* Buying != high: acc (75.0/20.0)
			* Maint != vhigh
				* Buying = high
					* Lug_boot = big: acc (35.0)
					* Lug_boot != big
						* Safety = med: unacc (31.0/12.0)
						* Safety != med: acc (36.0/3.0)
				* Buying != high
					* Lug_boot = small
						* Safety = med: acc (38.0/13.0)
						* Safety != med
							* Doors = 2: unacc (10.0/4.0)
							* Doors != 2
								* Maint = high: acc (6.0)
								* Maint != high
									* Maint = med: acc (10.0/5.0)
									* Maint != med: good (9.0)
					* Lug_boot != small
						* Safety = med
							* Maint = high: acc (20.0/1.0)
							* Maint != high
								* Maint = med: acc (22.0/10.0)
								* Maint != med: good (21.0/3.0)
						* Safety != med
							* Maint = high
								* Buying = med: acc (9.0)
								* Buying != med: vgood (12.0/2.0)
							* Maint != high
								* Lug_boot = med
									* Doors = 2: good (5.0/2.0)
									* Doors != 2: vgood (18.0/3.0)
								* Lug_boot != med: vgood (22.0)


