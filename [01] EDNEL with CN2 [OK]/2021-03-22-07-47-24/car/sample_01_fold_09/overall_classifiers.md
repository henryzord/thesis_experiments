# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Safety != high | unacc | 0.614697 |
| Safety != low and Persons = 2 | unacc | 0.428221 |
| Safety != low and Persons != 2 and Buying != vhigh and Buying = high and Maint != vhigh and Lug_boot != small | acc | 0.054410 |
| Safety != low and Persons != 2 and Buying = vhigh and Maint != high and Maint != vhigh and Safety != med | acc | 0.032845 |
| Safety != low and Persons != 2 and Buying != vhigh and Buying != high and Maint != vhigh and Safety = med and Maint = high | acc | 0.019659 |
| Safety != low and Persons != 2 and Buying != vhigh and Buying != high and Maint != vhigh and Safety = med and Maint != high and Lug_boot = small | acc | 0.019854 |
| Safety != low and Persons != 2 and Buying != vhigh and Buying != high and Maint = vhigh and Lug_boot = big | acc | 0.022617 |
| Safety != med | unacc | 0.587858 |
| Safety != low and Persons != 2 and Buying != vhigh and Buying != high and Maint = vhigh and Lug_boot != big and Safety != med | acc | 0.019565 |
| Safety != low and Persons != 2 and Buying != vhigh and Buying != high and Maint != vhigh and Safety != med and Lug_boot != small and Maint != high | vgood | 0.024648 |
| Safety != low and Persons != 2 and Buying = vhigh and Maint != high and Maint != vhigh and Safety = med and Lug_boot != small | acc | 0.013333 |
| Safety != low and Persons != 2 and Buying != vhigh and Buying = high and Maint != vhigh and Lug_boot = small and Safety != med | acc | 0.012417 |
| Safety != low and Persons != 2 and Buying != vhigh and Buying != high and Maint != vhigh and Safety = med and Maint != high and Lug_boot != small and Buying != med | good | 0.012715 |
| Safety != low and Persons != 2 and Buying != vhigh and Buying != high and Maint != vhigh and Safety != med and Lug_boot = small and Maint != low | acc | 0.011651 |
| Safety != low and Persons != 2 and Buying != vhigh and Buying != high and Maint != vhigh and Safety = med and Maint != high and Lug_boot != small and Buying = med and Maint = med | acc | 0.012245 |
| Safety != low and Persons != 2 and Buying != vhigh and Buying != high and Maint != vhigh and Safety != med and Lug_boot != small and Maint = high and Buying = med | acc | 0.011438 |
| Safety != low and Persons != 2 and Buying != vhigh and Buying != high and Maint != vhigh and Safety != med and Lug_boot = small and Maint = low | good | 0.007496 |
| Safety != low and Persons != 2 and Buying != vhigh and Buying != high and Maint != vhigh and Safety = med and Maint != high and Lug_boot != small and Buying = med and Maint != med | good | 0.005762 |
| Safety != low and Persons != 2 and Buying != vhigh and Buying != high and Maint != vhigh and Safety != med and Lug_boot != small and Maint = high and Buying != med | vgood | 0.006825 |
| Safety = med and Persons = 4 and Buying = med and Maint != med and Lug_boot = med and Safety!=(high) and Doors = 4 | acc | 0.001101 |
| Safety = med and Persons = 4 and Buying = med and Maint != med and Lug_boot = med and Safety!=(high) and Doors = 5more | acc | 0.001101 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Safety = low | unacc | 0.526904 |
| Persons = 2 | unacc | 0.428221 |
| Maint = vhigh and Buying = vhigh | unacc | 0.084479 |
| Buying != low and Buying != med and Maint != vhigh and Lug_boot != small and Maint != high and Safety != med | acc | 0.157746 |
| Buying = vhigh and Maint = high | unacc | 0.090909 |
| Buying = high and Maint = vhigh | unacc | 0.094923 |
| Safety = med and Lug_boot = small and Buying != high and Buying != vhigh and Maint != vhigh and Maint != high and Doors != 2 | acc | 0.100418 |
| Safety = med and Lug_boot = small and Buying != low and Doors != 2 | unacc | 0.089623 |
| Safety = med and Lug_boot = small and Maint != vhigh and Doors = 2 and Persons != 4 | unacc | 0.027708 |
| Safety = med and Lug_boot = small and Maint = vhigh | unacc | 0.020305 |
| Safety = med and Lug_boot = big and Maint != low and Buying != low | acc | 0.210000 |
| Maint = vhigh and Doors != 2 and Doors != 3 | acc | 0.168421 |
| Buying = high and Doors != 2 and Doors != 3 | acc | 0.172775 |
| Safety = med and Lug_boot = big and Buying != vhigh and Maint != high and Maint != vhigh and Buying != high | good | 0.080000 |
| Lug_boot = big and Safety != med and Maint != vhigh and Buying != high and Maint != high | vgood | 0.102662 |
| Doors = 2 and Lug_boot = big and Buying != low | acc | 0.084034 |
| Doors != 2 and Safety = med and Lug_boot != med | acc | 0.148438 |
| Doors = 2 and Lug_boot = big and Maint = vhigh | acc | 0.035398 |
| Doors = 2 and Lug_boot != big and Buying = vhigh and Safety = med | unacc | 0.029557 |
| Buying = high and Safety != med and Doors != 2 | acc | 0.080357 |
| Buying = high and Safety = med and Doors = 2 | unacc | 0.030928 |
| Maint = vhigh and Safety != med and Doors != 2 | acc | 0.101852 |
| Maint = vhigh and Lug_boot != small and Safety = med and Doors = 2 | unacc | 0.022099 |
| Lug_boot = big and Buying != med and Doors != 2 | vgood | 0.034682 |
| Maint = high and Buying != low and Doors != 2 and Safety != med | acc | 0.155340 |
| Buying = vhigh and Doors != 2 and Doors != 3 | acc | 0.130000 |
| Maint = high and Buying != low and Doors != 4 and Doors != 5more and Safety != med and Persons = 4 | acc | 0.043956 |
| Safety = med and Doors = 4 and Maint = high | acc | 0.043956 |
| Safety = med and Doors = 4 and Buying != med | good | 0.033898 |
| Safety = med and Doors = 5more and Maint != low and Buying = med | acc | 0.045977 |
| Safety = med and Doors = 5more and Maint != high | good | 0.043478 |
| Safety = med and Doors = 4 and Maint = med | acc | 0.025000 |
| Safety = med and Doors != 4 and Buying = low and Maint != vhigh and Doors != 3 | acc | 0.133333 |
| Safety = med and Doors != 4 and Persons != 4 and Buying != low and Maint != high | acc | 0.082353 |
| Maint = vhigh and Lug_boot != small and Doors = 2 | acc | 0.048780 |
| Safety = med and Doors != 4 and Buying != vhigh and Persons = 4 and Maint != med and Maint != low and Buying != low | unacc | 0.049505 |
| Buying = vhigh and Lug_boot = small and Doors != 2 | acc | 0.051948 |
| Buying = vhigh and Maint = med | unacc | 0.014337 |
| Safety = med and Doors != 4 and Persons = 4 and Buying = med | acc | 0.077922 |
| Doors != 2 and Lug_boot = small and Maint != high and Buying != med | good | 0.139241 |
| Lug_boot = small and Doors != 2 and Maint != low | acc | 0.166667 |
| Lug_boot = small and Persons != 4 and Doors = 2 | unacc | 0.136986 |
| Safety != med and Lug_boot = small and Doors != 2 | good | 0.115385 |
| Safety != med and Doors != 2 and Doors != 3 | vgood | 0.345455 |
| Maint = high and Lug_boot != big and Buying != med | acc | 0.218750 |
| Lug_boot != big and Safety != med and Persons = 4 and Buying = low | good | 0.230769 |
| Safety != med and Maint != low and Buying = med and Doors = 2 | acc | 0.136364 |
| Safety != med and Maint != low and Buying != med | vgood | 0.102273 |
| Safety != med and Persons = 4 and Doors = 2 | good | 0.071429 |
| Safety != med and Maint != med and Doors != 2 | vgood | 0.070175 |
| Doors != 3 and Doors = 2 | good | 0.072727 |
| Safety = med and Doors = 3 and Persons = 4 and Buying = low | acc | 0.121212 |
| Maint = low and Buying != med | unacc | 0.090909 |
| Maint != low and Buying = med | acc | 0.125000 |
| Buying = med | good | 0.257143 |
|  | acc | 0.375000 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Safety = high and Lug_boot = big and Buying = low and Persons = more | vgood | 0.004752 |
| Safety = high and Buying = low and Persons = 4 and Lug_boot = big | vgood | 0.004752 |
| Safety = high and Buying = med and Maint = med and Persons = more | vgood | 0.003264 |
| Safety = high and Maint = low and Buying = med and Lug_boot = big | vgood | 0.003874 |
| Safety = high and Lug_boot = med and Buying = low and Persons = more | vgood | 0.003050 |
| Safety = high and Persons = 4 and Lug_boot = med and Buying = low and Doors = 4 | vgood | 0.001501 |
| Safety = high and Persons = 4 and Buying = med and Maint = med and Lug_boot = big | vgood | 0.002000 |
| Safety = high and Maint = low and Buying = med and Lug_boot = med | vgood | 0.001394 |
| Buying = low and Doors = 5more and Safety = high and Persons = 4 and Lug_boot = med | vgood | 0.001334 |
| Buying = low and Maint = low and Persons = 4 and Safety = high | good | 0.003470 |
| Buying = low and Maint = med and Safety = high and Persons = 4 | good | 0.004161 |
| Maint = low and Safety = med and Lug_boot = big and Buying = med | good | 0.004038 |
| Buying = low and Safety = med and Maint = med and Persons = more | good | 0.002840 |
| Maint = low and Buying = low and Safety = med and Lug_boot = big | good | 0.003704 |
| Maint = low and Buying = med and Safety = high | good | 0.003170 |
| Maint = low and Persons = more and Buying = low and Safety = high | good | 0.002224 |
| Persons = more and Buying = low and Safety = high and Maint = med | good | 0.001565 |
| Maint = low and Lug_boot = med and Safety = med and Buying = low and Persons = more | good | 0.001565 |
| Persons = 4 and Safety = high and Maint = low | acc | 0.019608 |
| Safety = high and Persons = 4 and Buying = med | acc | 0.022345 |
| Safety = med and Persons = 4 and Lug_boot = big and Buying = med | acc | 0.009901 |
| Persons = more and Safety = high | acc | 0.050160 |
| Safety = med and Persons = more and Lug_boot = big | acc | 0.021588 |
| Safety = med and Persons = 4 and Buying = low | acc | 0.018454 |
| Persons = 4 and Safety = high and Maint = med | acc | 0.015390 |
| Persons = 4 and Safety = med and Maint = med and Lug_boot = big | acc | 0.005787 |
| Persons = 4 and Safety = med and Maint = low and Lug_boot = big | acc | 0.007220 |
| Safety = med and Persons = more and Lug_boot = med | acc | 0.017390 |
| Persons = 4 and Safety = med and Buying = med and Maint = med | acc | 0.007220 |
| Persons = 4 and Buying = high and Maint = high and Safety = high | acc | 0.010791 |
| Safety = med and Persons = 4 and Lug_boot = med and Doors = 4 | acc | 0.003423 |
| Safety = med and Persons = 4 and Maint = low and Buying = med | acc | 0.004076 |
| Persons = 4 and Safety = high and Buying = low | acc | 0.012567 |
| Safety = med and Persons = 4 and Doors = 5more and Lug_boot = med | acc | 0.002727 |
| Safety = med and Persons = more and Maint = low and Buying = med | acc | 0.001635 |
| Safety = med and Persons = more and Maint = med and Buying = med | acc | 0.002042 |
| Safety = med and Maint = high and Lug_boot = big and Buying = high and Persons = 4 | acc | 0.003623 |
|  | unacc | 0.982852 |


# Text representation of classifiers as-is

## JRip

Decision list:

rules | predicted class
---|---
(Safety = high) and (Lug_boot = big) and (Buying = low) and (Persons = more)|vgood (14.0/4.0)
(Safety = high) and (Buying = low) and (Persons = 4) and (Lug_boot = big)|vgood (14.0/4.0)
(Safety = high) and (Buying = med) and (Maint = med) and (Persons = more)|vgood (10.0/3.0)
(Safety = high) and (Maint = low) and (Buying = med) and (Lug_boot = big)|vgood (11.0/3.0)
(Safety = high) and (Lug_boot = med) and (Buying = low) and (Persons = more)|vgood (14.0/6.0)
(Safety = high) and (Persons = 4) and (Lug_boot = med) and (Buying = low) and (Doors = 4)|vgood (4.0/1.0)
(Safety = high) and (Persons = 4) and (Buying = med) and (Maint = med) and (Lug_boot = big)|vgood (3.0/0.0)
(Safety = high) and (Maint = low) and (Buying = med) and (Lug_boot = med)|vgood (12.0/7.0)
(Buying = low) and (Doors = 5more) and (Safety = high) and (Persons = 4) and (Lug_boot = med)|vgood (2.0/0.0)
(Buying = low) and (Maint = low) and (Persons = 4) and (Safety = high)|good (5.0/0.0)
(Buying = low) and (Maint = med) and (Safety = high) and (Persons = 4)|good (6.0/0.0)
(Maint = low) and (Safety = med) and (Lug_boot = big) and (Buying = med)|good (11.0/3.0)
(Buying = low) and (Safety = med) and (Maint = med) and (Persons = more)|good (12.0/5.0)
(Maint = low) and (Buying = low) and (Safety = med) and (Lug_boot = big)|good (12.0/4.0)
(Maint = low) and (Buying = med) and (Safety = high)|good (12.0/5.0)
(Maint = low) and (Persons = more) and (Buying = low) and (Safety = high)|good (4.0/1.0)
(Persons = more) and (Buying = low) and (Safety = high) and (Maint = med)|good (4.0/1.0)
(Maint = low) and (Lug_boot = med) and (Safety = med) and (Buying = low) and (Persons = more)|good (4.0/1.0)
(Persons = 4) and (Safety = high) and (Maint = low)|acc (22.0/0.0)
(Safety = high) and (Persons = 4) and (Buying = med)|acc (29.0/2.0)
(Safety = med) and (Persons = 4) and (Lug_boot = big) and (Buying = med)|acc (11.0/0.0)
(Persons = more) and (Safety = high)|acc (114.0/40.0)
(Safety = med) and (Persons = more) and (Lug_boot = big)|acc (45.0/12.0)
(Safety = med) and (Persons = 4) and (Buying = low)|acc (38.0/10.0)
(Persons = 4) and (Safety = high) and (Maint = med)|acc (19.0/0.0)
(Persons = 4) and (Safety = med) and (Maint = med) and (Lug_boot = big)|acc (8.0/0.0)
(Persons = 4) and (Safety = med) and (Maint = low) and (Lug_boot = big)|acc (8.0/0.0)
(Safety = med) and (Persons = more) and (Lug_boot = med)|acc (51.0/21.0)
(Persons = 4) and (Safety = med) and (Buying = med) and (Maint = med)|acc (8.0/0.0)
(Persons = 4) and (Buying = high) and (Maint = high) and (Safety = high)|acc (12.0/0.0)
(Safety = med) and (Persons = 4) and (Lug_boot = med) and (Doors = 4)|acc (11.0/4.0)
(Safety = med) and (Persons = 4) and (Maint = low) and (Buying = med)|acc (7.0/1.0)
(Persons = 4) and (Safety = high) and (Buying = low)|acc (9.0/0.0)
(Safety = med) and (Persons = 4) and (Doors = 5more) and (Lug_boot = med)|acc (9.0/3.0)
(Safety = med) and (Persons = more) and (Maint = low) and (Buying = med)|acc (4.0/1.0)
(Safety = med) and (Persons = more) and (Maint = med) and (Buying = med)|acc (4.0/1.0)
(Safety = med) and (Maint = high) and (Lug_boot = big) and (Buying = high) and (Persons = 4)|acc (4.0/0.0)
|unacc (988.0/5.0)


## PART

Decision list:

rules | predicted class
---|---
Safety = low|unacc (519.0)
Persons = 2|unacc (349.0)
Maint = vhigh AND Buying = vhigh|unacc (43.0)
Buying != low AND Buying != med AND Maint != vhigh AND Lug_boot != small AND Maint != high AND Safety != med|acc (56.0)
Buying = vhigh AND Maint = high|unacc (41.0)
Buying = high AND Maint = vhigh|unacc (43.0)
Safety = med AND Lug_boot = small AND Buying != high AND Buying != vhigh AND Maint != vhigh AND Maint != high AND Doors != 2|acc (24.0)
Safety = med AND Lug_boot = small AND Buying != low AND Doors != 2|unacc (38.0)
Safety = med AND Lug_boot = small AND Maint != vhigh AND Doors = 2 AND Persons != 4|unacc (11.0)
Safety = med AND Lug_boot = small AND Maint = vhigh|unacc (8.0)
Safety = med AND Lug_boot = big AND Maint != low AND Buying != low|acc (42.0)
Maint = vhigh AND Doors != 2 AND Doors != 3|acc (32.0)
Buying = high AND Doors != 2 AND Doors != 3|acc (33.0)
Safety = med AND Lug_boot = big AND Buying != vhigh AND Maint != high AND Maint != vhigh AND Buying != high|good (22.0)
Lug_boot = big AND Safety != med AND Maint != vhigh AND Buying != high AND Maint != high|vgood (27.0)
Doors = 2 AND Lug_boot = big AND Buying != low|acc (10.0)
Doors != 2 AND Safety = med AND Lug_boot != med|acc (19.0)
Doors = 2 AND Lug_boot = big AND Maint = vhigh|acc (4.0)
Doors = 2 AND Lug_boot != big AND Buying = vhigh AND Safety = med|unacc (6.0)
Buying = high AND Safety != med AND Doors != 2|acc (9.0)
Buying = high AND Safety = med AND Doors = 2|unacc (6.0)
Maint = vhigh AND Safety != med AND Doors != 2|acc (11.0)
Maint = vhigh AND Lug_boot != small AND Safety = med AND Doors = 2|unacc (4.0)
Lug_boot = big AND Buying != med AND Doors != 2|vgood (6.0)
Maint = high AND Buying != low AND Doors != 2 AND Safety != med|acc (16.0)
Buying = vhigh AND Doors != 2 AND Doors != 3|acc (13.0)
Maint = high AND Buying != low AND Doors != 4 AND Doors != 5more AND Safety != med AND Persons = 4|acc (4.0)
Safety = med AND Doors = 4 AND Maint = high|acc (4.0)
Safety = med AND Doors = 4 AND Buying != med|good (4.0)
Safety = med AND Doors = 5more AND Maint != low AND Buying = med|acc (4.0)
Safety = med AND Doors = 5more AND Maint != high|good (5.0)
Safety = med AND Doors = 4 AND Maint = med|acc (2.0)
Safety = med AND Doors != 4 AND Buying = low AND Maint != vhigh AND Doors != 3|acc (12.0)
Safety = med AND Doors != 4 AND Persons != 4 AND Buying != low AND Maint != high|acc (7.0)
Maint = vhigh AND Lug_boot != small AND Doors = 2|acc (4.0)
Safety = med AND Doors != 4 AND Buying != vhigh AND Persons = 4 AND Maint != med AND Maint != low AND Buying != low|unacc (5.0)
Buying = vhigh AND Lug_boot = small AND Doors != 2|acc (4.0)
Buying = vhigh AND Maint = med|unacc (3.0/1.0)
Safety = med AND Doors != 4 AND Persons = 4 AND Buying = med|acc (6.0)
Doors != 2 AND Lug_boot = small AND Maint != high AND Buying != med|good (11.0)
Lug_boot = small AND Doors != 2 AND Maint != low|acc (12.0)
Lug_boot = small AND Persons != 4 AND Doors = 2|unacc (10.0)
Safety != med AND Lug_boot = small AND Doors != 2|good (6.0)
Safety != med AND Doors != 2 AND Doors != 3|vgood (19.0)
Maint = high AND Lug_boot != big AND Buying != med|acc (7.0)
Lug_boot != big AND Safety != med AND Persons = 4 AND Buying = low|good (6.0)
Safety != med AND Maint != low AND Buying = med AND Doors = 2|acc (3.0)
Safety != med AND Maint != low AND Buying != med|vgood (3.0)
Safety != med AND Persons = 4 AND Doors = 2|good (3.0/1.0)
Safety != med AND Maint != med AND Doors != 2|vgood (3.0/1.0)
Doors != 3 AND Doors = 2|good (3.0/1.0)
Safety = med AND Doors = 3 AND Persons = 4 AND Buying = low|acc (3.0/1.0)
Maint = low AND Buying != med|unacc (3.0/1.0)
Maint != low AND Buying = med|acc (3.0/1.0)
Buying = med|good (2.0)
|acc (2.0/1.0)


## J48 Decision Tree

* Safety = low: unacc (442.0)
* Safety != low
	* Persons = 2: unacc (284.0)
	* Persons != 2
		* Buying = vhigh
			* Maint = high: unacc (36.0)
			* Maint != high
				* Maint = vhigh: unacc (34.0)
				* Maint != vhigh
					* Safety = med
						* Lug_boot = small: unacc (13.0)
						* Lug_boot != small: acc (25.0/5.0)
					* Safety != med: acc (39.0/1.0)
		* Buying != vhigh
			* Buying = high
				* Maint = vhigh: unacc (34.0)
				* Maint != vhigh
					* Lug_boot = small
						* Safety = med: unacc (16.0)
						* Safety != med: acc (14.0/2.0)
					* Lug_boot != small: acc (68.0/7.0)
			* Buying != high
				* Maint = vhigh
					* Lug_boot = big: acc (21.0)
					* Lug_boot != big
						* Safety = med: unacc (25.0/10.0)
						* Safety != med: acc (26.0/2.0)
				* Maint != vhigh
					* Safety = med
						* Maint = high: acc (36.0/11.0)
						* Maint != high
							* Lug_boot = small: acc (23.0/2.0)
							* Lug_boot != small
								* Buying = med
									* Maint = med: acc (14.0)
									* Maint != med: good (11.0/3.0)
								* Buying != med: good (27.0/5.0)
					* Safety != med
						* Lug_boot = small
							* Maint = low: good (13.0/1.0)
							* Maint != low: acc (29.0/10.0)
						* Lug_boot != small
							* Maint = high
								* Buying = med: acc (11.0)
								* Buying != med: vgood (12.0/2.0)
							* Maint != high: vgood (43.0/5.0)


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
								* Persons=(more)
											* Doors=(3)|(4)|(5more): vgood(4.0/0.0)
											* Doors!=(3)|(4)|(5more): good(2.0/0.0)
								* Persons!=(more)
											* Buying=(low)|(vhigh)|(high): good(4.0/0.0)
											* Buying!=(low)|(vhigh)|(high)
												* Maint=(low)|(vhigh)|(high): good(2.0/0.0)
												* Maint!=(low)|(vhigh)|(high): acc(2.0/0.0)
						* Lug_boot!=(big)|(med)
								* Buying=(low)|(vhigh)|(high)
									* Doors=(5more)|(4)|(3): good(11.0/0.0)
									* Doors!=(5more)|(4)|(3)
									* Persons=(more)|(2): unacc(2.0/0.0)
									* Persons!=(more)|(2): good(2.0/0.0)
								* Buying!=(low)|(vhigh)|(high)
									* Maint=(low)|(vhigh)|(high)
										* Doors=(5more)|(4)|(3): good(6.0/0.0)
										* Doors!=(5more)|(4)|(3): unacc(1.0/1.0)
									* Maint!=(low)|(vhigh)|(high): acc(7.0/0.0)
				* Safety!=(high)
						* Lug_boot=(big)|(med)
								* Buying=(low)|(vhigh)|(high)
								* Doors=(5more)|(4): good(16.0/0.0)
								* Doors!=(5more)|(4)
								* Lug_boot=(big): good(6.0/0.0)
								* Lug_boot!=(big)
											* Doors=(3)|(4)|(5more)
											* Persons=(more)|(2): good(2.0/0.0)
											* Persons!=(more)|(2): acc(2.0/0.0)
											* Doors!=(3)|(4)|(5more): acc(4.0/0.0)
								* Buying!=(low)|(vhigh)|(high)
							* Maint=(low)
									* Lug_boot=(big)|(small): good(8.0/0.0)
									* Lug_boot!=(big)|(small)
										* Doors=(5more)|(4): good(3.0/0.0)
										* Doors!=(5more)|(4): acc(3.0/0.0)
							* Maint!=(low): acc(15.0/0.0)
						* Lug_boot!=(big)|(med)
								* Doors=(5more)|(4)|(3): acc(24.0/0.0)
								* Doors!=(5more)|(4)|(3)
								* Persons=(more)|(2): unacc(4.0/0.0)
								* Persons!=(more)|(2): acc(4.0/0.0)
				* Maint!=(low)|(med)
					* Lug_boot=(big)|(med)
					* Safety=(high)
								* Maint=(high)|(med)|(low)
									* Buying=(low)|(vhigh)|(high)
										* Doors=(5more)|(4)|(3): vgood(10.0/0.0)
										* Doors!=(5more)|(4)|(3)
										* Lug_boot=(big)|(small): vgood(2.0/0.0)
										* Lug_boot!=(big)|(small): acc(2.0/0.0)
									* Buying!=(low)|(vhigh)|(high): acc(14.0/0.0)
								* Maint!=(high)|(med)|(low): acc(28.0/0.0)
					* Safety!=(high)
							* Doors=(5more)|(4): acc(30.0/0.0)
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
						* Safety=(high)|(low)
								* Doors=(5more)|(4)|(3): acc(23.0/0.0)
								* Doors!=(5more)|(4)|(3)
								* Persons=(more)|(2): unacc(4.0/0.0)
								* Persons!=(more)|(2): acc(2.0/0.0)
						* Safety!=(high)|(low)
						* Buying=(low)
									* Maint=(high)|(med)|(low)
										* Doors=(5more)|(4)|(3): acc(5.0/0.0)
										* Doors!=(5more)|(4)|(3): unacc(1.0/1.0)
									* Maint!=(high)|(med)|(low): unacc(6.0/0.0)
						* Buying!=(low): unacc(15.0/0.0)
			* Buying!=(low)|(med)
				* Maint=(low)|(med)
					* Lug_boot=(big)|(med)
						* Safety=(high)|(low): acc(56.0/0.0)
						* Safety!=(high)|(low)
							* Lug_boot=(big)|(small): acc(27.0/0.0)
							* Lug_boot!=(big)|(small)
								* Doors=(5more)|(4): acc(13.0/0.0)
								* Doors!=(5more)|(4)
								* Doors=(3)
										* Persons=(more)|(2): acc(3.0/0.0)
										* Persons!=(more)|(2): unacc(3.0/0.0)
								* Doors!=(3): unacc(7.0/0.0)
					* Lug_boot!=(big)|(med)
					* Safety=(high)
								* Doors=(5more)|(4)|(3): acc(22.0/0.0)
								* Doors!=(5more)|(4)|(3)
								* Persons=(more)|(2): unacc(3.0/0.0)
								* Persons!=(more)|(2): acc(2.0/0.0)
					* Safety!=(high): unacc(28.0/0.0)
				* Maint!=(low)|(med)
						* Maint=(high)|(med)|(low)
							* Buying=(high)|(med)|(low)
							* Lug_boot=(big)|(med)
								* Safety=(high)|(low): acc(16.0/0.0)
								* Safety!=(high)|(low)
									* Doors=(5more)|(4): acc(7.0/0.0)
									* Doors!=(5more)|(4)
										* Lug_boot=(big)|(small): acc(4.0/0.0)
										* Lug_boot!=(big)|(small)
												* Doors=(3)|(4)|(5more): unacc(1.0/1.0)
												* Doors!=(3)|(4)|(5more): unacc(2.0/0.0)
							* Lug_boot!=(big)|(med)
								* Safety=(high)|(low)
										* Doors=(5more)|(4)|(3): acc(5.0/0.0)
										* Doors!=(5more)|(4)|(3): unacc(1.0/1.0)
								* Safety!=(high)|(low): unacc(7.0/0.0)
							* Buying!=(high)|(med)|(low): unacc(41.0/0.0)
						* Maint!=(high)|(med)|(low): unacc(86.0/0.0)
		* Persons!=(more)|(4): unacc(349.0/0.0)
	* Safety!=(high)|(med): unacc(519.0/0.0)


