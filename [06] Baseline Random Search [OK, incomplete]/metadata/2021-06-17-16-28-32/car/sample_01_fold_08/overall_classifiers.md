# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Safety != high | unacc | 0.617321 |
| Safety = high and Persons = 2 | unacc | 0.262321 |
| Safety != med | unacc | 0.591077 |
| Safety = high and Persons = 4 and Buying = med and Maint = vhigh | acc | 0.009844 |
| Safety = high and Persons = 4 and Buying = high and Maint = med | acc | 0.009844 |
| Safety = high and Persons = 4 and Buying = low and Maint = vhigh | acc | 0.009844 |
| Safety = med and Persons = 4 and Buying = med and Maint = med | acc | 0.009844 |
| Safety = high and Persons = 4 and Buying = vhigh and Maint = low | acc | 0.009844 |
| Safety = high and Persons = 4 and Buying = med and Maint = high | acc | 0.009844 |
| Safety = high and Persons = 4 and Buying = vhigh and Maint = med | acc | 0.009844 |
| Safety = high and Persons = 4 and Buying = high and Maint = low | acc | 0.009031 |
| Safety = med and Persons = 4 and Buying = low and Maint = high | acc | 0.009031 |
| Safety = high and Persons = 4 and Buying = high and Maint = high | acc | 0.008217 |
| Safety = high and Persons = more and Buying = vhigh and Maint = med | acc | 0.007401 |
| Safety = med and Persons = 4 and Buying != med and Maint = med and Lug_boot = big | acc | 0.004800 |
| Safety = med and Persons = 4 and Buying = med and Maint != med and Lug_boot = big | acc | 0.004800 |
| Safety = med and Persons = 4 and Buying = med and Maint != med and Lug_boot = med | acc | 0.002978 |
| Safety = med and Persons = 4 and Buying != med and Maint = med and Lug_boot = med | acc | 0.002709 |
| Safety = med and Persons = 4 and Buying = low and Maint = vhigh and Lug_boot = big | acc | 0.003303 |
| Safety = med and Persons = more and Lug_boot = big and Buying = med and Maint = med | acc | 0.003303 |
| Safety = high and Persons = 4 and Buying = low and Maint = high and Lug_boot = small | acc | 0.003303 |
| Safety = med and Persons = 4 and Buying = med and Maint = low and Lug_boot = small | acc | 0.003303 |
| Safety = high and Persons = more and Buying = high and Maint = med and Lug_boot = big | acc | 0.003303 |
| Safety = med and Persons = more and Lug_boot = big and Buying = high and Maint = med | acc | 0.003303 |
| Safety = med and Persons = more and Lug_boot = big and Buying = vhigh and Maint = low | acc | 0.003303 |
| Safety = med and Persons = more and Lug_boot = med and Buying = low and Maint = high | acc | 0.003303 |
| Safety = med and Persons = 4 and Buying = vhigh and Maint = low and Lug_boot = big | acc | 0.003303 |
| Safety = high and Persons = more and Buying = low and Lug_boot = med and Maint = vhigh | acc | 0.003303 |
| Safety = med and Persons = 4 and Buying = low and Maint = low and Lug_boot = small | acc | 0.003303 |
| Safety = med and Persons = more and Lug_boot = big and Buying = high and Maint = low | acc | 0.003303 |
| Safety = med and Persons = more and Lug_boot = small and Buying = low and Doors = 5more | acc | 0.001861 |
| Safety = med and Persons = more and Lug_boot = med and Buying = med and Maint = vhigh | acc | 0.001861 |
| Safety = med and Persons = more and Lug_boot = small and Buying = med and Maint = med | acc | 0.001861 |
| Safety = med and Persons = 4 and Buying = low and Maint = med and Lug_boot = small | acc | 0.002479 |
| Safety = high and Persons = more and Buying = med and Maint = med and Lug_boot = small | acc | 0.001861 |
| Safety = med and Persons = more and Lug_boot = big and Buying = low and Maint = high | acc | 0.002479 |
| Safety = med and Persons = more and Lug_boot = big and Buying = vhigh and Maint = med | acc | 0.002479 |
| Safety = med and Persons = more and Lug_boot = med and Buying = high and Doors = 4 | acc | 0.002479 |
| Safety = med and Persons = more and Lug_boot = med and Buying = low and Maint = vhigh | acc | 0.002479 |
| Safety = high and Persons = more and Buying = vhigh and Maint = low and Doors = 4 | acc | 0.002479 |
| Safety = med and Persons = more and Lug_boot = med and Buying = vhigh and Maint = med | acc | 0.001861 |
| Safety = med and Persons = more and Lug_boot = small and Buying = med and Maint = low | acc | 0.001861 |
| Safety = med and Persons = more and Lug_boot = big and Buying = med and Maint = high | acc | 0.002479 |
| Safety = high and Persons = more and Buying = high and Maint = high and Doors = 4 | acc | 0.002479 |
| Safety = med and Persons = more and Lug_boot = small and Buying = low and Doors = 3 | acc | 0.001861 |
| Safety = med and Persons = 4 and Buying = high and Lug_boot = big and Maint = low | acc | 0.002479 |
| Safety = high and Persons = 4 and Buying = med and Maint = low and Lug_boot = small | good | 0.002672 |
| Safety = high and Persons = more and Buying = high and Maint = high and Doors = 5more | acc | 0.002479 |
| Safety = high and Persons = more and Buying = low and Lug_boot = big and Maint = low | vgood | 0.002668 |
| Safety = med and Persons = more and Lug_boot = med and Buying = med and Maint = high | acc | 0.001861 |
| Safety = med and Persons = 4 and Buying = low and Maint = low and Lug_boot = big | good | 0.002672 |
| Safety = med and Persons = more and Lug_boot = big and Buying = low and Maint = vhigh | acc | 0.002479 |
| Safety = high and Persons = more and Buying = med and Maint = med and Lug_boot = big | vgood | 0.002668 |
| Safety = high and Persons = more and Buying = low and Lug_boot = big and Maint = vhigh | acc | 0.002479 |
| Safety = high and Persons = 4 and Buying = low and Maint = low and Lug_boot = small | good | 0.002672 |
| Safety = high and Persons = more and Buying = high and Maint = med and Lug_boot = med | acc | 0.002479 |
| Safety = high and Persons = 4 and Buying = low and Maint = low and Lug_boot = big | vgood | 0.002668 |
| Safety = high and Persons = more and Buying = high and Maint = low and Doors = 4 | acc | 0.002479 |
| Safety = high and Persons = more and Buying = med and Maint = high and Doors = 5more | acc | 0.002479 |
| Safety = high and Persons = more and Buying = low and Lug_boot = big and Maint = med | vgood | 0.002668 |
| Safety = high and Persons = more and Buying = high and Maint = low and Doors = 3 | acc | 0.002479 |
| Safety = med and Persons = more and Lug_boot = med and Buying = high and Doors = 5more | acc | 0.001861 |
| Safety = high and Persons = more and Buying = low and Lug_boot = big and Maint = high | vgood | 0.002668 |
| Safety = high and Persons = more and Buying = med and Maint = high and Doors = 3 | acc | 0.002479 |
| Safety = high and Persons = more and Buying = vhigh and Maint = low and Doors = 3 | acc | 0.002479 |
| Safety = high and Persons = more and Buying = vhigh and Maint = low and Doors = 5more | acc | 0.002479 |
| Safety = high and Persons = more and Buying = med and Maint = vhigh and Doors = 4 | acc | 0.002479 |
| Safety = med and Persons = 4 and Buying = low and Maint = med and Lug_boot = big | good | 0.002005 |
| Safety = med and Persons = more and Lug_boot = big and Buying = low and Maint = low | good | 0.002005 |
| Safety = high and Persons = more and Buying = med and Maint = low and Lug_boot = small | good | 0.002005 |
| Safety = high and Persons = 4 and Buying = low and Maint = med and Lug_boot = small | good | 0.002005 |
| Safety = high and Persons = 4 and Buying = med and Maint = low and Lug_boot = big | vgood | 0.002003 |
| Safety = med and Persons = more and Lug_boot = big and Buying = med and Maint = low | good | 0.002005 |
| Safety = high and Persons = 4 and Buying = low and Maint = med and Lug_boot = big | vgood | 0.002003 |
| Safety = med and Persons = 4 and Buying = med and Maint = low and Lug_boot = big | good | 0.002005 |
| Safety = high and Persons = 4 and Buying = med and Maint = med and Lug_boot = big | vgood | 0.002003 |
| Safety = med and Persons = more and Lug_boot = big and Buying = low and Maint = med | good | 0.002005 |
| Safety = med and Persons = more and Lug_boot = med and Buying = med and Maint = med | acc | 0.001654 |
| Safety = high and Persons = more and Buying = med and Maint = low and Lug_boot = big | vgood | 0.002003 |
| Safety = med and Persons = more and Lug_boot = med and Buying = vhigh and Maint = low | acc | 0.001104 |
| Safety = med and Persons = 4 and Buying = high and Lug_boot = med and Doors = 5more | acc | 0.001861 |
| Safety = high and Persons = more and Buying = high and Maint = low and Doors = 5more | acc | 0.001654 |
| Safety = high and Persons = more and Buying = high and Maint = high and Doors = 3 | acc | 0.001654 |
| Safety = med and Persons = more and Lug_boot = big and Buying = med and Maint = vhigh | acc | 0.001654 |
| Safety = high and Persons = 4 and Buying = med and Maint = med and Lug_boot = small | acc | 0.001654 |
| Safety = med and Persons = more and Lug_boot = big and Buying = high and Maint = high | acc | 0.001654 |
| Safety = high and Persons = more and Buying = high and Maint = high and Doors = 2 | acc | 0.001104 |
| Safety = med and Persons = more and Lug_boot = med and Buying = high and Doors = 3 | acc | 0.001104 |
| Safety = med and Persons = 4 and Buying = high and Lug_boot = big and Maint = high | acc | 0.001654 |
| Safety = high and Persons = more and Buying = vhigh and Maint = low and Doors = 2 | acc | 0.001104 |
| Safety = med and Persons = 4 and Buying = high and Lug_boot = med and Doors = 4 | acc | 0.001861 |
| Safety = med and Persons = more and Lug_boot = med and Buying = med and Maint = low | good | 0.001505 |
| Safety = high and Persons = more and Buying = low and Lug_boot = med and Maint = med | vgood | 0.001503 |
| Safety = high and Persons = more and Buying = high and Maint = low and Doors = 2 | acc | 0.001104 |
| Safety = med and Persons = more and Lug_boot = med and Buying = low and Maint = med | good | 0.001505 |
| Safety = high and Persons = more and Buying = med and Maint = vhigh and Doors = 3 | acc | 0.001654 |
| Safety = high and Persons = more and Buying = med and Maint = med and Lug_boot = med | vgood | 0.001503 |
| Safety = high and Persons = more and Buying = high and Maint = med and Lug_boot = small | acc | 0.001104 |
| Safety = med and Persons = more and Lug_boot = med and Buying = low and Maint = low | good | 0.001505 |
| Safety = high and Persons = more and Buying = med and Maint = vhigh and Doors = 5more | acc | 0.001654 |
| Safety = high and Persons = more and Buying = med and Maint = low and Lug_boot = med | vgood | 0.001503 |
| Safety = high and Persons = more and Buying = med and Maint = high and Doors = 4 | acc | 0.001654 |
| Safety = high and Persons = more and Buying = low and Lug_boot = med and Maint = high | vgood | 0.001503 |
| Safety = high and Persons = more and Buying = low and Lug_boot = med and Maint = low | vgood | 0.001503 |
| Safety = med and Persons = 4 and Buying = low and Maint = low and Lug_boot = med | acc | 0.001104 |
| Safety = high and Persons = more and Buying = low and Lug_boot = small and Doors = 3 | good | 0.000892 |
| Safety = high and Persons = more and Buying = low and Lug_boot = small and Doors = 4 | good | 0.000892 |
| Safety = high and Persons = more and Buying = low and Lug_boot = small and Doors = 5more | acc | 0.000829 |
| Safety = high and Persons = 4 and Buying = low and Maint = low and Lug_boot = med | vgood | 0.000891 |
| Safety = high and Persons = 4 and Buying = med and Maint = med and Lug_boot = med | acc | 0.000829 |
| Safety = high and Persons = 4 and Buying = low and Maint = high and Lug_boot = med | acc | 0.000829 |
| Safety = high and Persons = 4 and Buying = med and Maint = low and Lug_boot = med | vgood | 0.000669 |
| Safety = high and Persons = 4 and Buying = low and Maint = med and Lug_boot = med | vgood | 0.000669 |
| Safety = high and Persons = 4 and Buying = low and Maint = high and Lug_boot = big | vgood | 0.000668 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Safety = low | unacc | 0.532258 |
| Persons = 2 | unacc | 0.422167 |
| Maint = vhigh and Buying = high | unacc | 0.086614 |
| Buying = vhigh and Maint = vhigh | unacc | 0.083004 |
| Buying = vhigh and Maint = high | unacc | 0.083004 |
| Safety = med and Lug_boot = small and Buying = high | unacc | 0.045267 |
| Safety = med and Lug_boot = small and Maint = vhigh | unacc | 0.033333 |
| Safety = med and Lug_boot = big and Buying != low and Maint != low | acc | 0.186916 |
| Safety = med and Lug_boot = big and Buying != low and Persons != 4 | acc | 0.032504 |
| Safety = med and Lug_boot = big and Maint != low and Persons = 4 | acc | 0.027528 |
| Safety = med and Lug_boot = big and Buying = low | good | 0.021589 |
| Safety = med and Doors = 2 and Buying != low and Persons = 4 | unacc | 0.011486 |
| Safety = med and Doors = 2 and Buying = low | acc | 0.050417 |
| Safety = med and Doors != 2 and Buying = vhigh and Lug_boot != small | acc | 0.063103 |
| Safety = med and Buying != vhigh and Doors != 2 and Maint = high and Buying != low | acc | 0.034615 |
| Safety = med and Buying != vhigh and Doors != 2 and Lug_boot = small | acc | 0.130179 |
| Safety != med and Lug_boot != small and Buying = high | acc | 0.215385 |
| Safety = med and Lug_boot != small and Buying = high | acc | 0.055592 |
| Safety != med and Lug_boot = small and Doors != 2 and Buying != low and Maint != low | acc | 0.168478 |
| Lug_boot != small and Safety != med and Buying != vhigh and Maint != vhigh and Maint != high and Doors != 2 and Doors != 3 | vgood | 0.113971 |
| Lug_boot != small and Safety != med and Buying = vhigh | acc | 0.197368 |
| Buying = vhigh and Safety = med | unacc | 0.068934 |
| Maint = vhigh and Doors != 2 and Doors != 3 | acc | 0.207407 |
| Lug_boot = big and Maint != low and Buying = med | acc | 0.075155 |
| Lug_boot = big and Maint != low | vgood | 0.041753 |
| Lug_boot != big and Maint = high and Doors != 2 and Persons = 4 | acc | 0.066007 |
| Lug_boot != big and Doors != 2 and Maint != high and Buying = low and Doors = 3 | good | 0.026864 |
| Lug_boot != big and Doors != 2 and Maint != high and Buying = low | good | 0.076844 |
| Lug_boot != big and Doors != 2 and Maint != low and Safety != med | acc | 0.076394 |
| Lug_boot != big and Maint != low and Persons = 4 | acc | 0.149979 |
| Lug_boot != big and Doors != 2 and Buying = med | good | 0.061173 |
| Lug_boot != big and Doors = 2 and Lug_boot = small | unacc | 0.164205 |
| Lug_boot != big and Doors != 2 | acc | 0.229688 |
| Lug_boot = med | acc | 0.043269 |
|  | vgood | 0.280702 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Safety = high and Buying = low and Lug_boot = big and Persons = more | vgood | 0.006383 |
| Safety = high and Buying = med and Maint = med | vgood | 0.003026 |
| Safety = high and Buying = low and Lug_boot = med and Persons = more | vgood | 0.003382 |
| Safety = high and Maint = low and Buying = med | vgood | 0.002627 |
| Buying = low and Maint = med and Safety = med | good | 0.002711 |
| Maint = low and Buying = low and Persons = more | good | 0.002568 |
| Safety = high and Persons = 4 and Buying = med | acc | 0.019810 |
| Safety = high and Persons = more | acc | 0.042815 |
| Persons = 4 and Safety = high and Buying = high | acc | 0.021263 |
| Safety = med and Persons = 4 and Lug_boot = big | acc | 0.020690 |
| Safety = med and Persons = more and Lug_boot = big | acc | 0.019190 |
| Safety = med and Persons = 4 and Buying = med | acc | 0.008835 |
| Persons = 4 and Safety = high and Buying = vhigh | acc | 0.011179 |
| Safety = med and Persons = more and Lug_boot = med | acc | 0.016343 |
| Persons = 4 and Safety = med and Buying = low | acc | 0.011963 |
| Persons = 4 and Safety = high and Maint = vhigh | acc | 0.003851 |
|  | unacc | 0.929974 |


# Text representation of classifiers as-is

## JRip

Decision list:

rules | predicted class
---|---
(Safety = high) and (Buying = low) and (Lug_boot = big) and (Persons = more)|vgood (15.0/3.0)
(Safety = high) and (Buying = med) and (Maint = med)|vgood (32.0/20.0)
(Safety = high) and (Buying = low) and (Lug_boot = med) and (Persons = more)|vgood (16.0/7.0)
(Safety = high) and (Maint = low) and (Buying = med)|vgood (31.0/20.0)
(Buying = low) and (Maint = med) and (Safety = med)|good (31.0/20.0)
(Maint = low) and (Buying = low) and (Persons = more)|good (26.0/17.0)
(Safety = high) and (Persons = 4) and (Buying = med)|acc (24.0/0.0)
(Safety = high) and (Persons = more)|acc (115.0/45.0)
(Persons = 4) and (Safety = high) and (Buying = high)|acc (44.0/11.0)
(Safety = med) and (Persons = 4) and (Lug_boot = big)|acc (54.0/18.0)
(Safety = med) and (Persons = more) and (Lug_boot = big)|acc (46.0/14.0)
(Safety = med) and (Persons = 4) and (Buying = med)|acc (29.0/11.0)
(Persons = 4) and (Safety = high) and (Buying = vhigh)|acc (45.0/21.0)
(Safety = med) and (Persons = more) and (Lug_boot = med)|acc (49.0/20.0)
(Persons = 4) and (Safety = med) and (Buying = low)|acc (23.0/7.0)
(Persons = 4) and (Safety = high) and (Maint = vhigh)|acc (12.0/0.0)
|unacc (961.0/48.0)


## PART

Decision list:

rules | predicted class
---|---
Safety = low|unacc (528.0)
Persons = 2|unacc (339.0)
Maint = vhigh AND Buying = high|unacc (44.0)
Buying = vhigh AND Maint = vhigh|unacc (42.0)
Buying = vhigh AND Maint = high|unacc (42.0)
Safety = med AND Lug_boot = small AND Buying = high|unacc (22.0)
Safety = med AND Lug_boot = small AND Maint = vhigh|unacc (16.0)
Safety = med AND Lug_boot = big AND Buying != low AND Maint != low|acc (40.0)
Safety = med AND Lug_boot = big AND Buying != low AND Persons != 4|acc (11.0/3.0)
Safety = med AND Lug_boot = big AND Maint != low AND Persons = 4|acc (10.0/3.0)
Safety = med AND Lug_boot = big AND Buying = low|good (16.0/6.0)
Safety = med AND Doors = 2 AND Buying != low AND Persons = 4|unacc (14.0/6.0)
Safety = med AND Doors = 2 AND Buying = low|acc (13.0/4.0)
Safety = med AND Doors != 2 AND Buying = vhigh AND Lug_boot != small|acc (14.0/2.0)
Safety = med AND Buying != vhigh AND Doors != 2 AND Maint = high AND Buying != low|acc (15.0/6.0)
Safety = med AND Buying != vhigh AND Doors != 2 AND Lug_boot = small|acc (27.0)
Safety != med AND Lug_boot != small AND Buying = high|acc (42.0)
Safety = med AND Lug_boot != small AND Buying = high|acc (17.0/5.0)
Safety != med AND Lug_boot = small AND Doors != 2 AND Buying != low AND Maint != low|acc (31.0)
Lug_boot != small AND Safety != med AND Buying != vhigh AND Maint != vhigh AND Maint != high AND Doors != 2 AND Doors != 3|vgood (31.0)
Lug_boot != small AND Safety != med AND Buying = vhigh|acc (30.0)
Buying = vhigh AND Safety = med|unacc (13.0)
Maint = vhigh AND Doors != 2 AND Doors != 3|acc (27.0)
Lug_boot = big AND Maint != low AND Buying = med|acc (14.0/3.0)
Lug_boot = big AND Maint != low|vgood (12.0/4.0)
Lug_boot != big AND Maint = high AND Doors != 2 AND Persons = 4|acc (12.0/2.0)
Lug_boot != big AND Doors != 2 AND Maint != high AND Buying = low AND Doors = 3|good (16.0/9.0)
Lug_boot != big AND Doors != 2 AND Maint != high AND Buying = low|good (15.0)
Lug_boot != big AND Doors != 2 AND Maint != low AND Safety != med|acc (11.0/4.0)
Lug_boot != big AND Maint != low AND Persons = 4|acc (18.0/2.0)
Lug_boot != big AND Doors != 2 AND Buying = med|good (16.0/5.0)
Lug_boot != big AND Doors = 2 AND Lug_boot = small|unacc (18.0/4.0)
Lug_boot != big AND Doors != 2|acc (15.0)
Lug_boot = med|acc (12.0/7.0)
|vgood (10.0/3.0)


## J48 Decision Tree

* Safety = low: unacc (528.0)
* Safety = med
	* Persons = 2: unacc (174.0)
	* Persons = 4
		* Buying = vhigh
			* Maint = vhigh: unacc (11.0)
			* Maint = high: unacc (12.0)
			* Maint = med
				* Lug_boot = small: unacc (4.0)
				* Lug_boot = med: unacc (4.0/2.0)
				* Lug_boot = big: acc (4.0)
			* Maint = low
				* Lug_boot = small: unacc (2.0)
				* Lug_boot = med: unacc (4.0/2.0)
				* Lug_boot = big: acc (4.0)
		* Buying = high
			* Lug_boot = small: unacc (16.0)
			* Lug_boot = med
				* Doors = 2: unacc (3.0)
				* Doors = 3: unacc (4.0)
				* Doors = 4: acc (4.0/1.0)
				* Doors = 5more: acc (4.0/1.0)
			* Lug_boot = big
				* Maint = vhigh: unacc (4.0)
				* Maint = high: acc (2.0)
				* Maint = med: acc (4.0)
				* Maint = low: acc (3.0)
		* Buying = med
			* Maint = vhigh
				* Lug_boot = small: unacc (4.0)
				* Lug_boot = med: unacc (4.0/2.0)
				* Lug_boot = big: acc (4.0)
			* Maint = high
				* Lug_boot = small: unacc (3.0)
				* Lug_boot = med: acc (3.0/1.0)
				* Lug_boot = big: acc (4.0)
			* Maint = med: acc (12.0)
			* Maint = low
				* Lug_boot = small: acc (4.0)
				* Lug_boot = med: acc (3.0/1.0)
				* Lug_boot = big: good (3.0)
		* Buying = low
			* Maint = vhigh
				* Lug_boot = small: unacc (4.0)
				* Lug_boot = med: unacc (4.0/2.0)
				* Lug_boot = big: acc (4.0)
			* Maint = high: acc (11.0)
			* Maint = med
				* Lug_boot = small: acc (3.0)
				* Lug_boot = med: acc (4.0/2.0)
				* Lug_boot = big: good (3.0)
			* Maint = low
				* Lug_boot = small: acc (4.0)
				* Lug_boot = med: acc (3.0/1.0)
				* Lug_boot = big: good (4.0)
	* Persons = more
		* Lug_boot = small
			* Buying = vhigh: unacc (10.0)
			* Buying = high: unacc (13.0)
			* Buying = med
				* Maint = vhigh: unacc (4.0)
				* Maint = high: unacc (4.0)
				* Maint = med: acc (4.0/1.0)
				* Maint = low: acc (4.0/1.0)
			* Buying = low
				* Doors = 2: unacc (4.0)
				* Doors = 3: acc (4.0/1.0)
				* Doors = 4: unacc (2.0/1.0)
				* Doors = 5more: acc (4.0/1.0)
		* Lug_boot = med
			* Buying = vhigh
				* Maint = vhigh: unacc (4.0)
				* Maint = high: unacc (3.0)
				* Maint = med: acc (4.0/1.0)
				* Maint = low: acc (3.0/1.0)
			* Buying = high
				* Doors = 2: unacc (4.0)
				* Doors = 3: acc (3.0/1.0)
				* Doors = 4: acc (3.0)
				* Doors = 5more: acc (4.0/1.0)
			* Buying = med
				* Maint = vhigh: acc (4.0/1.0)
				* Maint = high: acc (4.0/1.0)
				* Maint = med: acc (2.0)
				* Maint = low: good (4.0/1.0)
			* Buying = low
				* Maint = vhigh: acc (3.0)
				* Maint = high: acc (4.0)
				* Maint = med: good (4.0/1.0)
				* Maint = low: good (4.0/1.0)
		* Lug_boot = big
			* Buying = vhigh
				* Maint = vhigh: unacc (4.0)
				* Maint = high: unacc (4.0)
				* Maint = med: acc (3.0)
				* Maint = low: acc (4.0)
			* Buying = high
				* Maint = vhigh: unacc (3.0)
				* Maint = high: acc (2.0)
				* Maint = med: acc (4.0)
				* Maint = low: acc (4.0)
			* Buying = med
				* Maint = vhigh: acc (2.0)
				* Maint = high: acc (3.0)
				* Maint = med: acc (4.0)
				* Maint = low: good (3.0)
			* Buying = low
				* Maint = vhigh: acc (3.0)
				* Maint = high: acc (3.0)
				* Maint = med: good (3.0)
				* Maint = low: good (3.0)
* Safety = high
	* Persons = 2: unacc (165.0)
	* Persons = 4
		* Buying = vhigh
			* Maint = vhigh: unacc (10.0)
			* Maint = high: unacc (11.0)
			* Maint = med: acc (12.0)
			* Maint = low: acc (12.0)
		* Buying = high
			* Maint = vhigh: unacc (11.0)
			* Maint = high: acc (10.0)
			* Maint = med: acc (12.0)
			* Maint = low: acc (11.0)
		* Buying = med
			* Maint = vhigh: acc (12.0)
			* Maint = high: acc (12.0)
			* Maint = med
				* Lug_boot = small: acc (2.0)
				* Lug_boot = med: acc (4.0/2.0)
				* Lug_boot = big: vgood (3.0)
			* Maint = low
				* Lug_boot = small: good (4.0)
				* Lug_boot = med: vgood (4.0/2.0)
				* Lug_boot = big: vgood (3.0)
		* Buying = low
			* Maint = vhigh: acc (12.0)
			* Maint = high
				* Lug_boot = small: acc (4.0)
				* Lug_boot = med: acc (4.0/2.0)
				* Lug_boot = big: vgood (1.0)
			* Maint = med
				* Lug_boot = small: good (3.0)
				* Lug_boot = med: vgood (4.0/2.0)
				* Lug_boot = big: vgood (3.0)
			* Maint = low
				* Lug_boot = small: good (4.0)
				* Lug_boot = med: vgood (3.0/1.0)
				* Lug_boot = big: vgood (4.0)
	* Persons = more
		* Buying = vhigh
			* Maint = vhigh: unacc (10.0)
			* Maint = high: unacc (11.0)
			* Maint = med: acc (9.0)
			* Maint = low
				* Doors = 2: acc (3.0/1.0)
				* Doors = 3: acc (3.0)
				* Doors = 4: acc (3.0)
				* Doors = 5more: acc (3.0)
		* Buying = high
			* Maint = vhigh: unacc (12.0)
			* Maint = high
				* Doors = 2: acc (3.0/1.0)
				* Doors = 3: acc (2.0)
				* Doors = 4: acc (3.0)
				* Doors = 5more: acc (3.0)
			* Maint = med
				* Lug_boot = small: acc (3.0/1.0)
				* Lug_boot = med: acc (3.0)
				* Lug_boot = big: acc (4.0)
			* Maint = low
				* Doors = 2: acc (3.0/1.0)
				* Doors = 3: acc (3.0)
				* Doors = 4: acc (3.0)
				* Doors = 5more: acc (2.0)
		* Buying = med
			* Maint = vhigh
				* Doors = 2: unacc (2.0/1.0)
				* Doors = 3: acc (2.0)
				* Doors = 4: acc (3.0)
				* Doors = 5more: acc (2.0)
			* Maint = high
				* Doors = 2: unacc (2.0/1.0)
				* Doors = 3: acc (3.0)
				* Doors = 4: acc (2.0)
				* Doors = 5more: acc (3.0)
			* Maint = med
				* Lug_boot = small: acc (4.0/1.0)
				* Lug_boot = med: vgood (4.0/1.0)
				* Lug_boot = big: vgood (4.0)
			* Maint = low
				* Lug_boot = small: good (3.0)
				* Lug_boot = med: vgood (4.0/1.0)
				* Lug_boot = big: vgood (3.0)
		* Buying = low
			* Lug_boot = small
				* Doors = 2: unacc (4.0)
				* Doors = 3: good (3.0/1.0)
				* Doors = 4: good (3.0/1.0)
				* Doors = 5more: acc (4.0/2.0)
			* Lug_boot = med
				* Maint = vhigh: acc (4.0)
				* Maint = high: vgood (4.0/1.0)
				* Maint = med: vgood (4.0/1.0)
				* Maint = low: vgood (4.0/1.0)
			* Lug_boot = big
				* Maint = vhigh: acc (3.0)
				* Maint = high: vgood (4.0)
				* Maint = med: vgood (4.0)
				* Maint = low: vgood (4.0)


## SimpleCart Decision Tree

	* Safety=(high)|(med)
		* Persons=(more)|(4)
			* Buying=(low)|(med)
				* Maint=(low)|(med)
					* Safety=(high)|(low)
						* Lug_boot=(big)|(med): vgood(48.0/11.0)
						* Lug_boot!=(big)|(med): good(20.0/8.0)
					* Safety!=(high)|(low)
						* Lug_boot=(big)|(med)
								* Buying=(low)|(vhigh)|(high): good(22.0/6.0)
								* Buying!=(low)|(vhigh)|(high)
							* Maint=(low): good(10.0/3.0)
							* Maint!=(low): acc(14.0/0.0)
						* Lug_boot!=(big)|(med): acc(26.0/4.0)
				* Maint!=(low)|(med)
					* Lug_boot=(big)|(med): acc(96.0/17.0)
					* Lug_boot!=(big)|(med)
					* Safety=(high): acc(24.0/4.0)
					* Safety!=(high): unacc(24.0/6.0)
			* Buying!=(low)|(med)
				* Maint=(low)|(med)
					* Lug_boot=(big)|(med): acc(108.0/11.0)
					* Lug_boot!=(big)|(med)
						* Safety=(high)|(low): acc(27.0/3.0)
						* Safety!=(high)|(low): unacc(27.0/0.0)
				* Maint!=(low)|(med)
				* Maint=(high)
					* Buying=(high): acc(28.0/11.0)
					* Buying!=(high): unacc(42.0/0.0)
				* Maint!=(high): unacc(86.0/0.0)
		* Persons!=(more)|(4): unacc(339.0/0.0)
	* Safety!=(high)|(med): unacc(528.0/0.0)


