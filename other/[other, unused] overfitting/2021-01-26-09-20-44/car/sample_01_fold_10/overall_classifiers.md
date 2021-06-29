# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Safety != high | unacc | 0.615360 |
| Safety != med | unacc | 0.590333 |
| Persons = 4 and Safety = high | acc | 0.044925 |
| Persons = 4 and Safety = med | acc | 0.032673 |
| Persons = more and Safety = med | acc | 0.031585 |
| Persons = more and Safety = high | acc | 0.034903 |
| Safety != low and Persons != 2 and Buying != vhigh and Buying != high and Maint != vhigh and Safety != med and Lug_boot != small and Maint != high and Lug_boot != med | vgood | 0.019029 |
| Safety != low and Persons != 2 and Buying != vhigh and Buying != high and Maint != vhigh and Safety = med and Lug_boot != small and Maint != high and Buying != med and Lug_boot != med | good | 0.008626 |
| Safety != low and Persons != 2 and Buying != vhigh and Buying != high and Maint != vhigh and Safety != med and Lug_boot != small and Maint != high and Lug_boot = med and Doors != 2 and Doors != 3 | vgood | 0.009278 |
| Safety != low and Persons != 2 and Buying != vhigh and Buying != high and Maint != vhigh and Safety = med and Lug_boot != small and Maint != high and Buying != med and Lug_boot = med and Doors != 2 and Doors != 3 | good | 0.004664 |
| Safety != low and Persons != 2 and Buying != vhigh and Buying != high and Maint != vhigh and Safety = med and Lug_boot != small and Maint != high and Buying = med and Maint != med and Lug_boot != med | good | 0.004664 |
| Safety != low and Persons != 2 and Buying != vhigh and Buying != high and Maint != vhigh and Safety != med and Lug_boot = small and Maint = low and Persons = 4 | good | 0.004664 |
| Safety != low and Persons != 2 and Buying != vhigh and Buying != high and Maint != vhigh and Safety != med and Lug_boot = small and Maint = low and Persons != 4 | good | 0.003004 |
| Safety != low and Persons != 2 and Buying != vhigh and Buying != high and Maint != vhigh and Safety != med and Lug_boot != small and Maint = high and Buying != med and Lug_boot != med | vgood | 0.005323 |
| Safety != low and Persons != 2 and Buying != vhigh and Buying != high and Maint != vhigh and Safety != med and Lug_boot = small and Maint != low and Doors != 2 and Buying != med and Maint != high | good | 0.003336 |
| Safety != low and Persons != 2 and Buying != vhigh and Buying != high and Maint != vhigh and Safety != med and Lug_boot != small and Maint != high and Lug_boot = med and Doors = 2 | good | 0.001783 |
| Safety != low and Persons != 2 and Buying != vhigh and Buying != high and Maint != vhigh and Safety = med and Lug_boot != small and Maint != high and Buying = med and Maint != med and Lug_boot = med and Persons != 4 | good | 0.001504 |
| Safety != low and Persons != 2 and Buying != vhigh and Buying != high and Maint != vhigh and Safety != med and Lug_boot != small and Maint = high and Buying != med and Lug_boot = med | vgood | 0.001528 |
| Safety != low and Persons != 2 and Buying != vhigh and Buying != high and Maint != vhigh and Safety != med and Lug_boot != small and Maint != high and Lug_boot = med and Doors != 2 and Doors = 3 and Persons = 4 | good | 0.001504 |
| Safety != low and Persons != 2 and Buying != vhigh and Buying != high and Maint != vhigh and Safety != med and Lug_boot != small and Maint != high and Lug_boot = med and Doors != 2 and Doors = 3 and Persons != 4 | vgood | 0.002668 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Safety = low | unacc | 0.529828 |
| Persons = 2 | unacc | 0.421642 |
| Buying = vhigh and Maint = high | unacc | 0.086444 |
| Maint = vhigh and Buying = high | unacc | 0.086444 |
| Buying = vhigh and Maint = vhigh | unacc | 0.077381 |
| Lug_boot = small and Safety = med and Buying = high | unacc | 0.045175 |
| Safety = med and Lug_boot = small and Buying != vhigh and Maint != vhigh and Maint != high and Doors != 2 | acc | 0.096774 |
| Lug_boot != small and Safety != med and Buying = high | acc | 0.179916 |
| Safety = med and Lug_boot = small and Buying != low and Doors != 2 | unacc | 0.052009 |
| Safety = med and Lug_boot = small and Maint = vhigh | unacc | 0.021951 |
| Safety = med and Lug_boot = small and Doors = 2 and Persons != 4 | unacc | 0.019560 |
| Safety = med and Lug_boot = big and Buying != low and Maint != low | acc | 0.222772 |
| Maint = vhigh and Doors != 2 and Safety != med | acc | 0.182292 |
| Buying = vhigh and Doors != 2 and Doors != 3 | acc | 0.164894 |
| Buying = high and Doors != 2 and Doors != 3 | acc | 0.146739 |
| Safety = med and Lug_boot = big and Buying != med and Maint != med and Maint != low | acc | 0.087209 |
| Safety = med and Lug_boot = big and Buying != vhigh and Buying != high | good | 0.081301 |
| Lug_boot = big and Buying != vhigh and Buying != high and Maint != vhigh and Maint != high | vgood | 0.122881 |
| Doors = 2 and Lug_boot = big and Buying != low | acc | 0.092437 |
| Doors = 2 and Lug_boot != big and Buying = high and Persons != 4 | unacc | 0.030928 |
| Doors = 2 and Lug_boot != big and Safety = med and Buying != vhigh and Maint != vhigh and Buying != high and Maint != high | acc | 0.105263 |
| Doors = 2 and Lug_boot != big and Safety = med and Buying != low | unacc | 0.068783 |
| Maint = vhigh and Doors != 5more and Doors != 4 and Safety != med and Persons = 4 | acc | 0.053191 |
| Maint = vhigh and Lug_boot != small and Doors = 5more | acc | 0.032609 |
| Maint = vhigh and Doors != 4 and Persons = 4 | unacc | 0.017544 |
| Maint = high and Lug_boot != big and Buying != low and Safety != med and Doors != 2 | acc | 0.113402 |
| Buying = vhigh and Lug_boot != big and Safety != med and Doors != 2 | acc | 0.075269 |
| Maint = high and Lug_boot != big and Buying = low and Safety = med | acc | 0.131313 |
| Buying = high and Lug_boot != med | acc | 0.094737 |
| Buying = vhigh and Lug_boot = big | acc | 0.054945 |
| Lug_boot = big and Buying != med | vgood | 0.068376 |
| Maint = low and Buying != vhigh and Safety = med and Buying != high and Doors != 3 | good | 0.071429 |
| Doors = 2 and Persons = 4 and Maint = high | acc | 0.053333 |
| Doors = 2 and Lug_boot != small and Maint != vhigh and Buying != low and Maint != low | acc | 0.065789 |
| Doors = 2 and Persons = 4 and Buying = vhigh | acc | 0.027397 |
| Doors = 2 and Persons = 4 and Buying = med | acc | 0.007042 |
| Doors = 2 and Lug_boot = small and Maint != med | unacc | 0.060049 |
| Buying = high and Persons = 4 | unacc | 0.030303 |
| Doors = 2 and Lug_boot = small and Buying = low | unacc | 0.005208 |
| Maint = vhigh and Doors != 2 | acc | 0.062500 |
| Maint = high and Lug_boot != med | acc | 0.142857 |
| Safety = med and Buying != low and Maint != low and Doors != 3 | acc | 0.104478 |
| Lug_boot = small and Doors != 2 and Maint != med | good | 0.203390 |
| Buying = vhigh | unacc | 0.015873 |
| Safety = med and Buying = high | acc | 0.061224 |
| Safety = med and Doors != 3 and Doors != 4 | good | 0.031008 |
| Lug_boot = small and Buying != med | good | 0.125000 |
| Lug_boot = small and Persons != 4 | acc | 0.056250 |
| Lug_boot = small | acc | 0.046154 |
| Safety != med and Maint != vhigh and Doors = 2 and Maint != med | good | 0.048649 |
| Safety != med and Maint != vhigh and Doors != 2 and Doors != 3 | vgood | 0.414634 |
| Maint != high and Maint != vhigh and Doors != 3 | good | 0.126984 |
| Maint != high and Maint != vhigh and Persons = 4 and Safety = med | acc | 0.176471 |
| Maint = vhigh | acc | 0.088889 |
| Maint != high and Persons = 4 and Buying = med | acc | 0.035714 |
| Safety != med and Persons != 4 | vgood | 0.195313 |
| Maint != high and Buying != med | good | 0.253968 |
| Maint = high | unacc | 0.055556 |
|  | acc | 0.555556 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Safety = high and Buying = low and Lug_boot = big and Persons = more | vgood | 0.005750 |
| Safety = high and Buying = low and Persons = 4 and Lug_boot = big | vgood | 0.005371 |
| Safety = high and Buying = med and Lug_boot = big | vgood | 0.003698 |
| Safety = high and Lug_boot = med and Buying = low | vgood | 0.003012 |
| Maint = low and Buying = med and Safety = high | good | 0.002349 |
| Buying = low and Maint = med and Safety = med | good | 0.003043 |
| Maint = low and Safety = med and Buying = med | good | 0.003043 |
| Buying = low and Maint = low and Persons = more | good | 0.002579 |
| Buying = low and Safety = high | good | 0.001376 |
| Safety = high and Persons = 4 and Maint = med and Lug_boot = small | acc | 0.009892 |
| Safety = high and Persons = 4 and Maint = low | acc | 0.017120 |
| Persons = more and Safety = high and Maint = low | acc | 0.012962 |
| Safety = med and Lug_boot = big and Persons = more and Buying = med | acc | 0.010782 |
| Safety = med and Persons = 4 and Lug_boot = big and Maint = med | acc | 0.009892 |
| Safety = med and Persons = more and Lug_boot = big | acc | 0.018097 |
| Safety = high and Persons = more and Maint = med | acc | 0.016620 |
| Persons = 4 and Safety = high and Buying = med | acc | 0.019014 |
| Safety = med and Persons = 4 and Lug_boot = big | acc | 0.015184 |
| Safety = med and Lug_boot = med and Persons = more and Maint = med | acc | 0.008190 |
| Safety = high and Persons = 4 and Maint = med | acc | 0.009961 |
| Safety = med and Persons = 4 and Buying = low | acc | 0.012001 |
| Persons = more and Safety = high and Buying = med | acc | 0.011605 |
| Safety = med and Lug_boot = med and Persons = more | acc | 0.008400 |
| Persons = 4 and Safety = med and Maint = med | acc | 0.005229 |
| Maint = high and Safety = high and Buying = high and Persons = 4 | acc | 0.010782 |
| Maint = high and Persons = more and Safety = high and Buying = high | acc | 0.008190 |
| Safety = med and Persons = 4 and Lug_boot = med | acc | 0.002935 |
|  | unacc | 0.947781 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

persons|safety|acceptability
---|---|---
2|high|unacc
4|high|acc
more|high|acc
2|med|unacc
more|med|acc
4|med|acc
more|low|unacc
2|low|unacc
4|low|unacc

## JRip

Decision list:

rules | predicted class
---|---
(Safety = high) and (Buying = low) and (Lug_boot = big) and (Persons = more)|vgood (14.0/3.0)
(Safety = high) and (Buying = low) and (Persons = 4) and (Lug_boot = big)|vgood (15.0/4.0)
(Safety = high) and (Buying = med) and (Lug_boot = big)|vgood (41.0/26.0)
(Safety = high) and (Lug_boot = med) and (Buying = low)|vgood (44.0/30.0)
(Maint = low) and (Buying = med) and (Safety = high)|good (21.0/12.0)
(Buying = low) and (Maint = med) and (Safety = med)|good (33.0/21.0)
(Maint = low) and (Safety = med) and (Buying = med)|good (33.0/21.0)
(Buying = low) and (Maint = low) and (Persons = more)|good (26.0/17.0)
(Buying = low) and (Safety = high)|good (52.0/43.0)
(Safety = high) and (Persons = 4) and (Maint = med) and (Lug_boot = small)|acc (11.0/0.0)
(Safety = high) and (Persons = 4) and (Maint = low)|acc (21.0/0.0)
(Persons = more) and (Safety = high) and (Maint = low)|acc (21.0/2.0)
(Safety = med) and (Lug_boot = big) and (Persons = more) and (Buying = med)|acc (12.0/0.0)
(Safety = med) and (Persons = 4) and (Lug_boot = big) and (Maint = med)|acc (11.0/0.0)
(Safety = med) and (Persons = more) and (Lug_boot = big)|acc (36.0/9.0)
(Safety = high) and (Persons = more) and (Maint = med)|acc (30.0/6.0)
(Persons = 4) and (Safety = high) and (Buying = med)|acc (18.0/1.0)
(Safety = med) and (Persons = 4) and (Lug_boot = big)|acc (40.0/14.0)
(Safety = med) and (Lug_boot = med) and (Persons = more) and (Maint = med)|acc (10.0/1.0)
(Safety = high) and (Persons = 4) and (Maint = med)|acc (12.0/0.0)
(Safety = med) and (Persons = 4) and (Buying = low)|acc (21.0/7.0)
(Persons = more) and (Safety = high) and (Buying = med)|acc (14.0/2.0)
(Safety = med) and (Lug_boot = med) and (Persons = more)|acc (32.0/16.0)
(Persons = 4) and (Safety = med) and (Maint = med)|acc (21.0/10.0)
(Maint = high) and (Safety = high) and (Buying = high) and (Persons = 4)|acc (12.0/0.0)
(Maint = high) and (Persons = more) and (Safety = high) and (Buying = high)|acc (11.0/1.0)
(Safety = med) and (Persons = 4) and (Lug_boot = med)|acc (29.0/20.0)
|unacc (913.0/6.0)


## PART

Decision list:

rules | predicted class
---|---
Safety = low|unacc (524.0)
Persons = 2|unacc (339.0)
Buying = vhigh AND Maint = high|unacc (44.0)
Maint = vhigh AND Buying = high|unacc (44.0)
Buying = vhigh AND Maint = vhigh|unacc (39.0)
Lug_boot = small AND Safety = med AND Buying = high|unacc (22.0)
Safety = med AND Lug_boot = small AND Buying != vhigh AND Maint != vhigh AND Maint != high AND Doors != 2|acc (21.0)
Lug_boot != small AND Safety != med AND Buying = high|acc (43.0)
Safety = med AND Lug_boot = small AND Buying != low AND Doors != 2|unacc (22.0)
Safety = med AND Lug_boot = small AND Maint = vhigh|unacc (9.0)
Safety = med AND Lug_boot = small AND Doors = 2 AND Persons != 4|unacc (8.0)
Safety = med AND Lug_boot = big AND Buying != low AND Maint != low|acc (45.0)
Maint = vhigh AND Doors != 2 AND Safety != med|acc (35.0)
Buying = vhigh AND Doors != 2 AND Doors != 3|acc (31.0)
Buying = high AND Doors != 2 AND Doors != 3|acc (27.0)
Safety = med AND Lug_boot = big AND Buying != med AND Maint != med AND Maint != low|acc (15.0)
Safety = med AND Lug_boot = big AND Buying != vhigh AND Buying != high|good (20.0)
Lug_boot = big AND Buying != vhigh AND Buying != high AND Maint != vhigh AND Maint != high|vgood (29.0)
Doors = 2 AND Lug_boot = big AND Buying != low|acc (11.0)
Doors = 2 AND Lug_boot != big AND Buying = high AND Persons != 4|unacc (6.0)
Doors = 2 AND Lug_boot != big AND Safety = med AND Buying != vhigh AND Maint != vhigh AND Buying != high AND Maint != high|acc (12.0)
Doors = 2 AND Lug_boot != big AND Safety = med AND Buying != low|unacc (13.0)
Maint = vhigh AND Doors != 5more AND Doors != 4 AND Safety != med AND Persons = 4|acc (5.0)
Maint = vhigh AND Lug_boot != small AND Doors = 5more|acc (3.0)
Maint = vhigh AND Doors != 4 AND Persons = 4|unacc (3.0)
Maint = high AND Lug_boot != big AND Buying != low AND Safety != med AND Doors != 2|acc (11.0)
Buying = vhigh AND Lug_boot != big AND Safety != med AND Doors != 2|acc (7.0)
Maint = high AND Lug_boot != big AND Buying = low AND Safety = med|acc (13.0)
Buying = high AND Lug_boot != med|acc (9.0)
Buying = vhigh AND Lug_boot = big|acc (5.0)
Lug_boot = big AND Buying != med|vgood (8.0)
Maint = low AND Buying != vhigh AND Safety = med AND Buying != high AND Doors != 3|good (7.0)
Doors = 2 AND Persons = 4 AND Maint = high|acc (4.0)
Doors = 2 AND Lug_boot != small AND Maint != vhigh AND Buying != low AND Maint != low|acc (5.0)
Doors = 2 AND Persons = 4 AND Buying = vhigh|acc (2.0)
Doors = 2 AND Persons = 4 AND Buying = med|acc (2.0/1.0)
Doors = 2 AND Lug_boot = small AND Maint != med|unacc (7.0)
Buying = high AND Persons = 4|unacc (3.0)
Doors = 2 AND Lug_boot = small AND Buying = low|unacc (2.0/1.0)
Maint = vhigh AND Doors != 2|acc (4.0)
Maint = high AND Lug_boot != med|acc (10.0)
Safety = med AND Buying != low AND Maint != low AND Doors != 3|acc (7.0)
Lug_boot = small AND Doors != 2 AND Maint != med|good (12.0)
Buying = vhigh|unacc (4.0/2.0)
Safety = med AND Buying = high|acc (3.0)
Safety = med AND Doors != 3 AND Doors != 4|good (3.0/1.0)
Lug_boot = small AND Buying != med|good (5.0)
Lug_boot = small AND Persons != 4|acc (4.0/1.0)
Lug_boot = small|acc (3.0)
Safety != med AND Maint != vhigh AND Doors = 2 AND Maint != med|good (3.0/1.0)
Safety != med AND Maint != vhigh AND Doors != 2 AND Doors != 3|vgood (17.0)
Maint != high AND Maint != vhigh AND Doors != 3|good (4.0)
Maint != high AND Maint != vhigh AND Persons = 4 AND Safety = med|acc (3.0)
Maint = vhigh|acc (2.0)
Maint != high AND Persons = 4 AND Buying = med|acc (2.0/1.0)
Safety != med AND Persons != 4|vgood (5.0)
Maint != high AND Buying != med|good (4.0)
Maint = high|unacc (2.0/1.0)
|acc (2.0/1.0)


## J48 Decision Tree

* Safety = low: unacc (524.0)
* Safety != low
	* Persons = 2: unacc (339.0)
	* Persons != 2
		* Buying = vhigh
			* Maint = high: unacc (44.0)
			* Maint != high
				* Maint = vhigh: unacc (39.0)
				* Maint != vhigh
					* Lug_boot = small
						* Safety = med: unacc (15.0)
						* Safety != med
							* Doors = 2: unacc (4.0/2.0)
							* Doors != 2: acc (8.0)
					* Lug_boot != small
						* Lug_boot = med
							* Doors = 2: unacc (6.0/3.0)
							* Doors != 2
								* Doors = 3: acc (6.0/1.0)
								* Doors != 3: acc (14.0)
						* Lug_boot != med: acc (31.0)
		* Buying != vhigh
			* Buying = high
				* Maint = vhigh: unacc (44.0)
				* Maint != vhigh
					* Lug_boot = big: acc (46.0)
					* Lug_boot != big
						* Safety = med
							* Lug_boot = small: unacc (22.0)
							* Lug_boot != small
								* Doors = 2: unacc (6.0)
								* Doors != 2
									* Doors = 3: unacc (6.0/3.0)
									* Doors != 3: acc (11.0)
						* Safety != med
							* Doors = 2
								* Persons = 4: acc (6.0)
								* Persons != 4: unacc (6.0/3.0)
							* Doors != 2: acc (32.0)
			* Buying != high
				* Maint = vhigh
					* Safety = med
						* Lug_boot = small: unacc (14.0)
						* Lug_boot != small
							* Lug_boot = med
								* Doors = 2: unacc (4.0)
								* Doors != 2
									* Doors = 3: unacc (4.0/2.0)
									* Doors != 3: acc (5.0)
							* Lug_boot != med: acc (15.0)
					* Safety != med
						* Doors = 2
							* Lug_boot = small: unacc (4.0/2.0)
							* Lug_boot != small: acc (7.0)
						* Doors != 2: acc (35.0)
				* Maint != vhigh
					* Safety = med
						* Lug_boot = small
							* Maint = high
								* Buying = med: unacc (8.0)
								* Buying != med: acc (7.0/1.0)
							* Maint != high
								* Doors = 2
									* Persons = 4: acc (4.0)
									* Persons != 4: unacc (4.0)
								* Doors != 2: acc (21.0)
						* Lug_boot != small
							* Maint = high
								* Buying = med
									* Lug_boot = med: unacc (6.0/3.0)
									* Lug_boot != med: acc (6.0)
								* Buying != med: acc (15.0)
							* Maint != high
								* Buying = med
									* Maint = med: acc (14.0)
									* Maint != med
										* Lug_boot = med
											* Persons = 4: acc (4.0/2.0)
											* Persons != 4: good (4.0/1.0)
										* Lug_boot != med: good (7.0)
								* Buying != med
									* Lug_boot = med
										* Doors = 2: acc (4.0)
										* Doors != 2
											* Doors = 3: acc (4.0/2.0)
											* Doors != 3: good (7.0)
									* Lug_boot != med: good (13.0)
					* Safety != med
						* Lug_boot = small
							* Maint = low
								* Persons = 4: good (7.0)
								* Persons != 4: good (8.0/2.0)
							* Maint != low
								* Doors = 2
									* Persons = 4: acc (4.0/1.0)
									* Persons != 4: unacc (4.0)
								* Doors != 2
									* Buying = med: acc (11.0)
									* Buying != med
										* Maint = high: acc (5.0)
										* Maint != high: good (5.0)
						* Lug_boot != small
							* Maint = high
								* Buying = med: acc (13.0)
								* Buying != med
									* Lug_boot = med: vgood (7.0/3.0)
									* Lug_boot != med: vgood (8.0)
							* Maint != high
								* Lug_boot = med
									* Doors = 2: good (6.0/2.0)
									* Doors != 2
										* Doors = 3
											* Persons = 4: good (4.0/1.0)
											* Persons != 4: vgood (4.0)
										* Doors != 3: vgood (14.0)
								* Lug_boot != med: vgood (29.0)


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
										* Persons!=(more)|(2): good(3.0/1.0)
										* Doors!=(3)|(4)|(5more)
											* Buying=(low)|(vhigh)|(high): good(3.0/0.0)
											* Buying!=(low)|(vhigh)|(high): acc(2.0/1.0)
						* Lug_boot!=(big)|(med)
								* Maint=(low)|(vhigh)|(high)
									* Doors=(5more)|(4)|(3): good(12.0/0.0)
									* Doors!=(5more)|(4)|(3): unacc(2.0/1.0)
								* Maint!=(low)|(vhigh)|(high)
							* Buying=(low): good(6.0/1.0)
							* Buying!=(low): acc(7.0/1.0)
					* Safety!=(high)|(low)
						* Lug_boot=(big)|(med)
						* Buying=(low)
							* Lug_boot=(big): good(13.0/0.0)
							* Lug_boot!=(big)
									* Doors=(5more)|(4): good(7.0/0.0)
									* Doors!=(5more)|(4)
											* Doors=(3)|(4)|(5more)
											* Persons=(more)|(2): good(2.0/0.0)
											* Persons!=(more)|(2): acc(2.0/0.0)
											* Doors!=(3)|(4)|(5more): acc(4.0/0.0)
						* Buying!=(low)
									* Maint=(low)|(vhigh)|(high)
									* Doors=(5more)|(4): good(7.0/0.0)
									* Doors!=(5more)|(4)
										* Lug_boot=(big)|(small): good(4.0/0.0)
										* Lug_boot!=(big)|(small): acc(3.0/1.0)
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
										* Doors!=(5more)|(4): acc(3.0/1.0)
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
							* Lug_boot=(big)|(med): acc(29.0/3.0)
							* Lug_boot!=(big)|(med)
							* Safety=(high): acc(6.0/1.0)
							* Safety!=(high): unacc(8.0/0.0)
							* Maint!=(high)|(med)|(low): unacc(44.0/0.0)
						* Buying!=(high)|(med)|(low): unacc(83.0/0.0)
		* Persons!=(more)|(4): unacc(339.0/0.0)
	* Safety!=(high)|(med): unacc(524.0/0.0)


