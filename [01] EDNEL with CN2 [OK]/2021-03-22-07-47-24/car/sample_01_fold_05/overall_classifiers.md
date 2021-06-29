# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Persons != 4 | unacc | 0.602861 |
| Persons != more | unacc | 0.602525 |
| Persons != 2 and Safety != low and Maint = vhigh and Buying != high and Buying != vhigh | acc | 0.037725 |
| Persons != 2 and Safety != low and Maint != vhigh and Buying != low and Buying != med and Lug_boot != small and Maint != high and Lug_boot != med | acc | 0.047356 |
| Persons != 2 and Safety != low and Maint != vhigh and Buying != low and Buying != med and Lug_boot != small and Maint != high and Lug_boot = med and Doors != 2 | acc | 0.028357 |
| Persons != 2 and Safety != low and Maint != vhigh and Buying != low and Buying = med and Maint != low and Maint = high | acc | 0.021633 |
| Persons != 2 and Safety != low and Maint != vhigh and Buying != low and Buying != med and Lug_boot != small and Maint = high and Buying != vhigh | acc | 0.017136 |
| Persons != 2 and Safety != low and Maint != vhigh and Buying != low and Buying = med and Maint != low and Maint != high and Safety = med | acc | 0.016337 |
| Persons != 2 and Safety != low and Maint != vhigh and Buying = low and Safety != med and Lug_boot != small | vgood | 0.018730 |
| Persons != 2 and Safety != low and Maint != vhigh and Buying != low and Buying != med and Lug_boot = small and Safety != med and Buying != vhigh | acc | 0.014209 |
| Persons != 2 and Safety != low and Maint != vhigh and Buying = low and Safety = med and Lug_boot = small | acc | 0.013417 |
| Persons != 2 and Safety != low and Maint != vhigh and Buying = low and Safety = med and Lug_boot != small and Maint = high | acc | 0.012275 |
| Persons != 2 and Safety != low and Maint != vhigh and Buying = low and Safety != med and Lug_boot = small and Maint != high | good | 0.008682 |
| Persons != 2 and Safety != low and Maint != vhigh and Buying = low and Safety = med and Lug_boot != small and Maint != high and Lug_boot != med | good | 0.009296 |
| Persons != 2 and Safety != low and Maint != vhigh and Buying != low and Buying != med and Lug_boot = small and Safety != med and Buying = vhigh and Maint != high | acc | 0.007654 |
| Persons != 2 and Safety != low and Maint != vhigh and Buying != low and Buying = med and Maint != low and Maint != high and Safety != med and Lug_boot != small | vgood | 0.007023 |
| Persons != 2 and Safety != low and Maint != vhigh and Buying != low and Buying != med and Lug_boot != small and Maint != high and Lug_boot = med and Doors = 2 and Safety != med | acc | 0.005766 |
| Persons != 2 and Safety != low and Maint != vhigh and Buying != low and Buying = med and Maint = low and Safety = med and Lug_boot != small | good | 0.005132 |
| Persons != 2 and Safety != low and Maint != vhigh and Buying != low and Buying = med and Maint != low and Maint != high and Safety != med and Lug_boot = small | acc | 0.005049 |
| Persons != 2 and Safety != low and Maint != vhigh and Buying != low and Buying = med and Maint = low and Safety = med and Lug_boot = small | acc | 0.005049 |
| Persons != 2 and Safety != low and Maint != vhigh and Buying != low and Buying = med and Maint = low and Safety != med and Lug_boot = small | good | 0.004089 |
| Persons != 2 and Safety != low and Maint != vhigh and Buying != low and Buying = med and Maint = low and Safety != med and Lug_boot != small | vgood | 0.005548 |
| Persons != 2 and Safety != low and Maint != vhigh and Buying = low and Safety != med and Lug_boot = small and Maint = high | acc | 0.004243 |
| Persons != 2 and Safety != low and Maint != vhigh and Buying = low and Safety = med and Lug_boot != small and Maint != high and Lug_boot = med and Doors = 5more | good | 0.002674 |
| Persons != 2 and Safety != low and Maint != vhigh and Buying = low and Safety = med and Lug_boot != small and Maint != high and Lug_boot = med and Doors != 5more | acc | 0.002585 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Persons = 2 | unacc | 0.528033 |
| Safety = low | unacc | 0.424845 |
| Maint = vhigh and Buying = vhigh | unacc | 0.088583 |
| Buying != low and Buying != med and Maint != vhigh and Lug_boot != small and Maint != high and Lug_boot != med | acc | 0.165746 |
| Buying = vhigh and Maint = high | unacc | 0.098434 |
| Buying = high and Maint = vhigh | unacc | 0.100446 |
| Safety = med and Lug_boot = small and Buying = high | unacc | 0.049528 |
| Safety = med and Lug_boot = big and Maint != low and Maint != med | acc | 0.157895 |
| Lug_boot != big and Safety = med and Lug_boot = small and Maint != vhigh and Buying != vhigh and Maint != high and Doors != 2 | acc | 0.098592 |
| Safety != med and Lug_boot != small and Maint != vhigh and Buying != high and Buying != vhigh and Maint != high and Lug_boot != med | vgood | 0.076531 |
| Safety != med and Lug_boot != small and Buying != low and Buying != med | acc | 0.198020 |
| Safety = med and Lug_boot = big and Buying != med | good | 0.046053 |
| Safety = med and Lug_boot = small and Buying != low and Doors != 2 | unacc | 0.080702 |
| Doors != 2 and Maint = vhigh and Safety != med | acc | 0.203822 |
| Doors = 2 and Lug_boot = big and Buying = med | acc | 0.045802 |
| Doors = 2 and Lug_boot != big and Safety = med and Buying != vhigh and Maint != vhigh and Buying != high and Persons = 4 and Maint != high | acc | 0.060150 |
| Doors = 2 and Lug_boot != big and Safety = med and Buying != low and Buying != med | unacc | 0.052632 |
| Maint = vhigh and Lug_boot = small and Safety = med | unacc | 0.040000 |
| Doors != 2 and Buying = high and Doors != 3 | acc | 0.161290 |
| Doors != 2 and Safety = med and Maint != low and Doors != 3 and Maint != med | acc | 0.154472 |
| Doors != 2 and Buying = vhigh and Doors != 3 | acc | 0.118644 |
| Maint != low and Buying != low and Doors != 2 and Lug_boot != med | acc | 0.206107 |
| Maint = vhigh and Safety != med and Persons = 4 | acc | 0.045872 |
| Doors = 2 and Lug_boot != big and Persons != 4 and Lug_boot = small | unacc | 0.114865 |
| Maint = vhigh and Persons != 4 | acc | 0.029963 |
| Maint != vhigh and Maint = high and Lug_boot != big and Safety != med and Buying != low | acc | 0.093750 |
| Safety = med and Maint != vhigh and Lug_boot = big | good | 0.065934 |
| Lug_boot = big | vgood | 0.076190 |
| Safety = med and Maint = vhigh | unacc | 0.054545 |
| Safety = med and Doors = 5more and Buying = med | acc | 0.014925 |
| Safety = med and Doors != 5more and Doors = 4 | good | 0.025714 |
| Safety = med and Doors = 5more | good | 0.080000 |
| Safety = med and Persons != 4 and Maint = high and Buying = low | acc | 0.049180 |
| Safety = med and Persons != 4 and Maint != high and Doors = 2 | acc | 0.064516 |
| Safety = med and Persons = 4 and Buying != low and Buying = med | unacc | 0.017442 |
| Safety = med and Persons = 4 and Buying = low | acc | 0.067797 |
| Safety = med and Persons != 4 and Maint != high and Maint = med | acc | 0.055172 |
| Safety = med and Persons = 4 | unacc | 0.019231 |
| Lug_boot = small and Maint != high and Buying != vhigh and Buying != high and Doors != 2 | good | 0.272727 |
| Doors = 2 and Buying = low and Maint != med | good | 0.045000 |
| Lug_boot = small and Doors != 2 | acc | 0.243902 |
| Doors != 2 and Safety != med and Doors != 3 | vgood | 0.363636 |
| Buying != low and Maint != low and Maint != high and Lug_boot != small | acc | 0.219298 |
| Buying != low and Buying != med | acc | 0.318182 |
| Maint != high and Doors = 2 and Lug_boot != small | good | 0.285714 |
| Maint != high and Persons = 4 | good | 0.222222 |
| Buying != med | vgood | 0.187500 |
|  | unacc | 0.111111 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Safety = high and Buying = low and Lug_boot = big and Persons = more | vgood | 0.005374 |
| Safety = high and Lug_boot = big and Buying = low and Persons = 4 | vgood | 0.006839 |
| Safety = high and Buying = med and Lug_boot = big and Maint = med | vgood | 0.003560 |
| Safety = high and Lug_boot = med and Buying = low and Persons = more | vgood | 0.003289 |
| Safety = high and Buying = med and Maint = low and Lug_boot = big | vgood | 0.002976 |
| Safety = high and Lug_boot = med and Buying = med and Persons = more and Maint = med | vgood | 0.001504 |
| Safety = high and Lug_boot = med and Buying = low and Persons = 4 and Doors = 5more | vgood | 0.001504 |
| Buying = low and Maint = med and Safety = med and Lug_boot = big | good | 0.003087 |
| Buying = low and Safety = high and Persons = 4 and Maint = low | good | 0.003559 |
| Buying = low and Maint = low and Safety = med and Lug_boot = big | good | 0.003393 |
| Maint = low and Buying = med and Safety = high and Lug_boot = small | good | 0.003087 |
| Buying = low and Maint = med and Safety = high and Persons = 4 | good | 0.004149 |
| Maint = low and Buying = med and Lug_boot = big and Safety = med | good | 0.002497 |
| Buying = low and Persons = more and Safety = high and Maint = med | good | 0.002218 |
| Buying = low and Maint = low and Safety = high and Persons = more | good | 0.002770 |
| Safety = high and Persons = 4 and Maint = med | acc | 0.022187 |
| Safety = med and Persons = more and Lug_boot = big | acc | 0.028120 |
| Safety = high and Persons = more and Maint = med | acc | 0.018237 |
| Safety = high and Persons = 4 and Buying = med | acc | 0.017385 |
| Persons = 4 and Safety = med and Buying = low | acc | 0.016706 |
| Persons = 4 and Safety = med and Lug_boot = big and Maint = med | acc | 0.009830 |
| Safety = high and Persons = more and Buying = med | acc | 0.014037 |
| Maint = low and Safety = high and Persons = 4 | acc | 0.016319 |
| Safety = med and Persons = 4 and Buying = med and Lug_boot = big | acc | 0.006278 |
| Persons = 4 and Safety = med and Maint = low and Lug_boot = big | acc | 0.006278 |
| Persons = more and Safety = high and Maint = low | acc | 0.013712 |
| Safety = med and Persons = more and Buying = low | acc | 0.009265 |
| Persons = 4 and Safety = high and Buying = low | acc | 0.011656 |
| Safety = med and Lug_boot = med and Persons = more and Buying = med | acc | 0.006412 |
| Maint = high and Buying = high and Safety = high and Persons = 4 | acc | 0.008945 |
| Safety = med and Buying = med and Persons = 4 and Maint = med | acc | 0.007168 |
| Safety = med and Lug_boot = med and Persons = more and Maint = low | acc | 0.002256 |
| Persons = more and Safety = high and Maint = high and Buying = high | acc | 0.007258 |
| Persons = more and Buying = low and Safety = high | acc | 0.009448 |
| Safety = med and Persons = 4 and Lug_boot = med and Doors = 4 | acc | 0.003399 |
| Safety = med and Persons = 4 and Maint = low and Buying = med | acc | 0.004047 |
| Safety = med and Persons = 4 and Lug_boot = big and Maint = high and Buying = high | acc | 0.002700 |
| Safety = med and Persons = more and Maint = med and Lug_boot = med | acc | 0.003243 |
| Safety = med and Lug_boot = med and Doors = 5more and Persons = 4 | acc | 0.002053 |
| Persons = more and Safety = med and Maint = low and Buying = med | acc | 0.001354 |
|  | unacc | 0.981081 |


# Text representation of classifiers as-is

## JRip

Decision list:

rules | predicted class
---|---
(Safety = high) and (Buying = low) and (Lug_boot = big) and (Persons = more)|vgood (15.0/4.0)
(Safety = high) and (Lug_boot = big) and (Buying = low) and (Persons = 4)|vgood (14.0/2.0)
(Safety = high) and (Buying = med) and (Lug_boot = big) and (Maint = med)|vgood (12.0/4.0)
(Safety = high) and (Lug_boot = med) and (Buying = low) and (Persons = more)|vgood (13.0/5.0)
(Safety = high) and (Buying = med) and (Maint = low) and (Lug_boot = big)|vgood (11.0/4.0)
(Safety = high) and (Lug_boot = med) and (Buying = med) and (Persons = more) and (Maint = med)|vgood (4.0/1.0)
(Safety = high) and (Lug_boot = med) and (Buying = low) and (Persons = 4) and (Doors = 5more)|vgood (4.0/1.0)
(Buying = low) and (Maint = med) and (Safety = med) and (Lug_boot = big)|good (11.0/4.0)
(Buying = low) and (Safety = high) and (Persons = 4) and (Maint = low)|good (7.0/1.0)
(Buying = low) and (Maint = low) and (Safety = med) and (Lug_boot = big)|good (10.0/3.0)
(Maint = low) and (Buying = med) and (Safety = high) and (Lug_boot = small)|good (11.0/4.0)
(Buying = low) and (Maint = med) and (Safety = high) and (Persons = 4)|good (6.0/0.0)
(Maint = low) and (Buying = med) and (Lug_boot = big) and (Safety = med)|good (10.0/4.0)
(Buying = low) and (Persons = more) and (Safety = high) and (Maint = med)|good (4.0/1.0)
(Buying = low) and (Maint = low) and (Safety = high) and (Persons = more)|good (3.0/0.0)
(Safety = high) and (Persons = 4) and (Maint = med)|acc (29.0/2.0)
(Safety = med) and (Persons = more) and (Lug_boot = big)|acc (50.0/10.0)
(Safety = high) and (Persons = more) and (Maint = med)|acc (26.0/3.0)
(Safety = high) and (Persons = 4) and (Buying = med)|acc (25.0/2.0)
(Persons = 4) and (Safety = med) and (Buying = low)|acc (36.0/10.0)
(Persons = 4) and (Safety = med) and (Lug_boot = big) and (Maint = med)|acc (11.0/0.0)
(Safety = high) and (Persons = more) and (Buying = med)|acc (26.0/5.0)
(Maint = low) and (Safety = high) and (Persons = 4)|acc (21.0/0.0)
(Safety = med) and (Persons = 4) and (Buying = med) and (Lug_boot = big)|acc (7.0/0.0)
(Persons = 4) and (Safety = med) and (Maint = low) and (Lug_boot = big)|acc (7.0/0.0)
(Persons = more) and (Safety = high) and (Maint = low)|acc (22.0/2.0)
(Safety = med) and (Persons = more) and (Buying = low)|acc (28.0/11.0)
(Persons = 4) and (Safety = high) and (Buying = low)|acc (11.0/0.0)
(Safety = med) and (Lug_boot = med) and (Persons = more) and (Buying = med)|acc (14.0/4.0)
(Maint = high) and (Buying = high) and (Safety = high) and (Persons = 4)|acc (10.0/0.0)
(Safety = med) and (Buying = med) and (Persons = 4) and (Maint = med)|acc (8.0/0.0)
(Safety = med) and (Lug_boot = med) and (Persons = more) and (Maint = low)|acc (7.0/2.0)
(Persons = more) and (Safety = high) and (Maint = high) and (Buying = high)|acc (10.0/1.0)
(Persons = more) and (Buying = low) and (Safety = high)|acc (8.0/2.0)
(Safety = med) and (Persons = 4) and (Lug_boot = med) and (Doors = 4)|acc (11.0/4.0)
(Safety = med) and (Persons = 4) and (Maint = low) and (Buying = med)|acc (7.0/1.0)
(Safety = med) and (Persons = 4) and (Lug_boot = big) and (Maint = high) and (Buying = high)|acc (3.0/0.0)
(Safety = med) and (Persons = more) and (Maint = med) and (Lug_boot = med)|acc (8.0/2.0)
(Safety = med) and (Lug_boot = med) and (Doors = 5more) and (Persons = 4)|acc (8.0/3.0)
(Persons = more) and (Safety = med) and (Maint = low) and (Buying = med)|acc (4.0/1.0)
|unacc (1020.0/2.0)


## PART

Decision list:

rules | predicted class
---|---
Persons = 2|unacc (518.0)
Safety = low|unacc (342.0)
Maint = vhigh AND Buying = vhigh|unacc (45.0)
Buying != low AND Buying != med AND Maint != vhigh AND Lug_boot != small AND Maint != high AND Lug_boot != med|acc (60.0)
Buying = vhigh AND Maint = high|unacc (44.0)
Buying = high AND Maint = vhigh|unacc (45.0)
Safety = med AND Lug_boot = small AND Buying = high|unacc (21.0)
Safety = med AND Lug_boot = big AND Maint != low AND Maint != med|acc (36.0)
Lug_boot != big AND Safety = med AND Lug_boot = small AND Maint != vhigh AND Buying != vhigh AND Maint != high AND Doors != 2|acc (21.0)
Safety != med AND Lug_boot != small AND Maint != vhigh AND Buying != high AND Buying != vhigh AND Maint != high AND Lug_boot != med|vgood (30.0)
Safety != med AND Lug_boot != small AND Buying != low AND Buying != med|acc (40.0)
Safety = med AND Lug_boot = big AND Buying != med|good (14.0)
Safety = med AND Lug_boot = small AND Buying != low AND Doors != 2|unacc (23.0)
Doors != 2 AND Maint = vhigh AND Safety != med|acc (32.0)
Doors = 2 AND Lug_boot = big AND Buying = med|acc (6.0)
Doors = 2 AND Lug_boot != big AND Safety = med AND Buying != vhigh AND Maint != vhigh AND Buying != high AND Persons = 4 AND Maint != high|acc (8.0)
Doors = 2 AND Lug_boot != big AND Safety = med AND Buying != low AND Buying != med|unacc (12.0)
Maint = vhigh AND Lug_boot = small AND Safety = med|unacc (9.0)
Doors != 2 AND Buying = high AND Doors != 3|acc (20.0)
Doors != 2 AND Safety = med AND Maint != low AND Doors != 3 AND Maint != med|acc (19.0)
Doors != 2 AND Buying = vhigh AND Doors != 3|acc (14.0)
Maint != low AND Buying != low AND Doors != 2 AND Lug_boot != med|acc (27.0)
Maint = vhigh AND Safety != med AND Persons = 4|acc (5.0)
Doors = 2 AND Lug_boot != big AND Persons != 4 AND Lug_boot = small|unacc (17.0)
Maint = vhigh AND Persons != 4|acc (6.0/2.0)
Maint != vhigh AND Maint = high AND Lug_boot != big AND Safety != med AND Buying != low|acc (9.0)
Safety = med AND Maint != vhigh AND Lug_boot = big|good (6.0)
Lug_boot = big|vgood (8.0)
Safety = med AND Maint = vhigh|unacc (4.0)
Safety = med AND Doors = 5more AND Buying = med|acc (4.0/2.0)
Safety = med AND Doors != 5more AND Doors = 4|good (5.0/2.0)
Safety = med AND Doors = 5more|good (4.0)
Safety = med AND Persons != 4 AND Maint = high AND Buying = low|acc (3.0)
Safety = med AND Persons != 4 AND Maint != high AND Doors = 2|acc (4.0)
Safety = med AND Persons = 4 AND Buying != low AND Buying = med|unacc (5.0/2.0)
Safety = med AND Persons = 4 AND Buying = low|acc (4.0)
Safety = med AND Persons != 4 AND Maint != high AND Maint = med|acc (4.0/1.0)
Safety = med AND Persons = 4|unacc (3.0)
Lug_boot = small AND Maint != high AND Buying != vhigh AND Buying != high AND Doors != 2|good (18.0)
Doors = 2 AND Buying = low AND Maint != med|good (4.0/1.0)
Lug_boot = small AND Doors != 2|acc (10.0)
Doors != 2 AND Safety != med AND Doors != 3|vgood (16.0)
Buying != low AND Maint != low AND Maint != high AND Lug_boot != small|acc (4.0/1.0)
Buying != low AND Buying != med|acc (7.0)
Maint != high AND Doors = 2 AND Lug_boot != small|good (4.0)
Maint != high AND Persons = 4|good (5.0/1.0)
Buying != med|vgood (4.0/1.0)
|unacc (3.0/2.0)


## J48 Decision Tree

* Persons = 2: unacc (440.0)
* Persons != 2
	* Safety = low: unacc (276.0)
	* Safety != low
		* Maint = vhigh
			* Buying = high: unacc (36.0)
			* Buying != high
				* Buying = vhigh: unacc (35.0)
				* Buying != vhigh: acc (72.0/22.0)
		* Maint != vhigh
			* Buying = low
				* Safety = med
					* Lug_boot = small: acc (19.0/2.0)
					* Lug_boot != small
						* Maint = high: acc (11.0)
						* Maint != high
							* Lug_boot = med
								* Doors = 5more: good (4.0)
								* Doors != 5more: acc (7.0/3.0)
							* Lug_boot != med: good (11.0)
				* Safety != med
					* Lug_boot = small
						* Maint = high: acc (6.0/1.0)
						* Maint != high: good (11.0/1.0)
					* Lug_boot != small: vgood (38.0/8.0)
			* Buying != low
				* Buying = med
					* Maint = low
						* Safety = med
							* Lug_boot = small: acc (7.0)
							* Lug_boot != small: good (12.0/3.0)
						* Safety != med
							* Lug_boot = small: good (6.0/1.0)
							* Lug_boot != small: vgood (10.0/2.0)
					* Maint != low
						* Maint = high: acc (38.0/10.0)
						* Maint != high
							* Safety = med: acc (19.0/1.0)
							* Safety != med
								* Lug_boot = small: acc (6.0/1.0)
								* Lug_boot != small: vgood (13.0/2.0)
				* Buying != med
					* Lug_boot = small
						* Safety = med: unacc (39.0)
						* Safety != med
							* Buying = vhigh
								* Maint = high: unacc (6.0)
								* Maint != high: acc (9.0/2.0)
							* Buying != vhigh: acc (22.0/2.0)
					* Lug_boot != small
						* Maint = high
							* Buying = vhigh: unacc (24.0)
							* Buying != vhigh: acc (18.0)
						* Maint != high
							* Lug_boot = med
								* Doors = 2
									* Safety = med: unacc (7.0)
									* Safety != med: acc (6.0)
								* Doors != 2: acc (34.0/2.0)
							* Lug_boot != med: acc (52.0)


## SimpleCart Decision Tree

	* Persons=(more)|(4)
		* Safety=(high)|(med)
			* Buying=(low)|(med)
				* Maint=(low)|(med)
					* Safety=(high)|(low)
						* Lug_boot=(big)|(med)
								* Doors=(5more)|(4)|(3)
									* Doors=(5more)|(4)|(2): vgood(28.0/0.0)
									* Doors!=(5more)|(4)|(2)
									* Lug_boot=(big)|(small): vgood(8.0/0.0)
									* Lug_boot!=(big)|(small): vgood(3.0/3.0)
								* Doors!=(5more)|(4)|(3)
							* Lug_boot=(big): vgood(7.0/0.0)
							* Lug_boot!=(big)
										* Buying=(low)|(vhigh)|(high): good(4.0/0.0)
										* Buying!=(low)|(vhigh)|(high): acc(2.0/2.0)
						* Lug_boot!=(big)|(med)
						* Buying=(low): good(14.0/1.0)
						* Buying!=(low)
									* Maint=(low)|(vhigh)|(high): good(7.0/1.0)
									* Maint!=(low)|(vhigh)|(high): acc(7.0/1.0)
					* Safety!=(high)|(low)
						* Lug_boot=(big)|(med)
						* Buying=(low)
									* Doors=(5more)|(4)|(3)
										* Doors=(5more)|(4)|(2): good(14.0/0.0)
										* Doors!=(5more)|(4)|(2): good(4.0/1.0)
									* Doors!=(5more)|(4)|(3): acc(4.0/3.0)
						* Buying!=(low)
							* Maint=(low): good(10.0/3.0)
							* Maint!=(low): acc(16.0/0.0)
						* Lug_boot!=(big)|(med)
								* Doors=(5more)|(4)|(3): acc(21.0/0.0)
								* Doors!=(5more)|(4)|(3)
								* Persons=(more)|(2): unacc(4.0/0.0)
								* Persons!=(more)|(2): acc(4.0/0.0)
				* Maint!=(low)|(med)
					* Lug_boot=(big)|(med)
					* Buying=(low)
						* Safety=(high)
									* Maint=(high)|(med)|(low)
									* Lug_boot=(big)|(small): vgood(8.0/0.0)
									* Lug_boot!=(big)|(small): vgood(4.0/2.0)
									* Maint!=(high)|(med)|(low): acc(13.0/0.0)
						* Safety!=(high)
									* Maint=(high)|(med)|(low): acc(15.0/0.0)
									* Maint!=(high)|(med)|(low)
									* Doors=(5more)|(4): acc(7.0/0.0)
									* Doors!=(5more)|(4)
										* Lug_boot=(big)|(small): acc(4.0/0.0)
										* Lug_boot!=(big)|(small): unacc(3.0/1.0)
					* Buying!=(low)
							* Lug_boot=(big)|(small): acc(31.0/0.0)
							* Lug_boot!=(big)|(small)
									* Doors=(5more)|(4)|(3)
										* Doors=(5more)|(4)|(2): acc(14.0/0.0)
										* Doors!=(5more)|(4)|(2)
										* Persons=(more)|(2): acc(4.0/0.0)
										* Persons!=(more)|(2): unacc(2.0/2.0)
									* Doors!=(5more)|(4)|(3): unacc(4.0/3.0)
					* Lug_boot!=(big)|(med)
						* Safety=(high)|(low)
								* Doors=(5more)|(4)|(3): acc(23.0/0.0)
								* Doors!=(5more)|(4)|(3): unacc(4.0/3.0)
						* Safety!=(high)|(low)
						* Maint=(high)
									* Buying=(low)|(vhigh)|(high): acc(6.0/1.0)
									* Buying!=(low)|(vhigh)|(high): unacc(7.0/0.0)
						* Maint!=(high): unacc(15.0/0.0)
			* Buying!=(low)|(med)
				* Maint=(low)|(med)
					* Lug_boot=(big)|(med)
							* Doors=(5more)|(4)|(3)
								* Doors=(5more)|(4)|(2): acc(57.0/0.0)
								* Doors!=(5more)|(4)|(2)
								* Persons=(more)|(2): acc(15.0/0.0)
								* Persons!=(more)|(2)
									* Lug_boot=(big)|(small): acc(7.0/0.0)
									* Lug_boot!=(big)|(small): unacc(3.0/3.0)
							* Doors!=(5more)|(4)|(3)
							* Lug_boot=(big)|(small): acc(16.0/0.0)
							* Lug_boot!=(big)|(small)
							* Safety=(high): acc(7.0/0.0)
							* Safety!=(high): unacc(8.0/0.0)
					* Lug_boot!=(big)|(med)
					* Safety=(high)
								* Doors=(5more)|(4)|(3): acc(20.0/0.0)
								* Doors!=(5more)|(4)|(3)
								* Persons=(more)|(2): unacc(4.0/0.0)
								* Persons!=(more)|(2): acc(4.0/0.0)
					* Safety!=(high): unacc(29.0/0.0)
				* Maint!=(low)|(med)
				* Maint=(high)
					* Buying=(high)
							* Lug_boot=(big)|(med)
									* Doors=(5more)|(4)|(3): acc(16.0/0.0)
									* Doors!=(5more)|(4)|(3): acc(6.0/1.0)
							* Lug_boot!=(big)|(med)
								* Safety=(high)|(low): acc(7.0/1.0)
								* Safety!=(high)|(low): unacc(6.0/0.0)
					* Buying!=(high): unacc(44.0/0.0)
				* Maint!=(high): unacc(90.0/0.0)
		* Safety!=(high)|(med): unacc(342.0/0.0)
	* Persons!=(more)|(4): unacc(518.0/0.0)


