# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Persons != 4 | unacc | 0.602281 |
| Persons != more | unacc | 0.601945 |
| Persons = 4 and Safety = high | acc | 0.042816 |
| Persons = more and Safety = med | acc | 0.033857 |
| Persons = 4 and Safety = med | acc | 0.030831 |
| Persons = more and Safety = high | acc | 0.036040 |
| Safety = med and Persons = more and Lug_boot = big and Buying = low and Maint = low | good | 0.002672 |
| Safety = high and Persons = 4 and Buying = low and Maint = med and Lug_boot = big | vgood | 0.002668 |
| Safety = med and Persons = 4 and Buying = low and Maint = med and Lug_boot = big | good | 0.002672 |
| Safety = high and Persons = 4 and Buying = med and Maint = low and Lug_boot = big | vgood | 0.002668 |
| Safety = high and Persons = 4 and Buying = med and Maint = low and Lug_boot = small | good | 0.002672 |
| Safety = high and Persons = more and Buying = med and Maint = med and Lug_boot = big | vgood | 0.002668 |
| Safety = high and Persons = 4 and Buying = low and Maint = low and Lug_boot = small | good | 0.002672 |
| Safety = high and Persons = 4 and Buying = med and Maint = med and Lug_boot = big | vgood | 0.002668 |
| Safety = high and Persons = 4 and Buying = low and Maint = med and Lug_boot = small | good | 0.002672 |
| Safety = high and Persons = more and Buying = low and Maint = high and Lug_boot = big | vgood | 0.002668 |
| Safety = high and Persons = 4 and Buying = low and Maint = low and Lug_boot = big | vgood | 0.002668 |
| Safety = high and Persons = 4 and Buying = low and Maint = high and Lug_boot = big | vgood | 0.002668 |
| Safety = med and Persons = 4 and Buying = low and Maint = low and Lug_boot = big | good | 0.002005 |
| Safety = high and Persons = more and Buying = low and Maint = low and Lug_boot = big | vgood | 0.002668 |
| Safety = med and Persons = more and Lug_boot = big and Buying = low and Maint = med | good | 0.002005 |
| Safety = high and Persons = more and Buying = low and Maint = med and Lug_boot = small | good | 0.001505 |
| Safety = high and Persons = more and Buying = med and Maint = low and Lug_boot = small | good | 0.001505 |
| Safety = high and Persons = more and Buying = low and Maint = low and Lug_boot = small | good | 0.002005 |
| Safety = high and Persons = more and Buying = med and Maint = med and Lug_boot = med | vgood | 0.001503 |
| Safety = med and Persons = more and Lug_boot = big and Buying = med and Maint = low | good | 0.002005 |
| Safety = high and Persons = more and Buying = low and Maint = med and Lug_boot = big | vgood | 0.002003 |
| Safety = med and Persons = 4 and Buying = med and Maint = low and Lug_boot = big | good | 0.002005 |
| Safety = high and Persons = more and Buying = med and Maint = low and Lug_boot = big | vgood | 0.002003 |
| Safety = high and Persons = more and Buying = low and Maint = high and Lug_boot = med | vgood | 0.002003 |
| Safety = med and Persons = 4 and Buying = low and Maint = med and Lug_boot = med | good | 0.000892 |
| Safety = med and Persons = more and Lug_boot = med and Maint = low and Buying = low | good | 0.000892 |
| Safety = high and Persons = more and Buying = low and Maint = low and Lug_boot = med | vgood | 0.001503 |
| Safety = med and Persons = more and Lug_boot = med and Maint = low and Buying = med | good | 0.000892 |
| Safety = high and Persons = 4 and Buying = low and Maint = med and Lug_boot = med | good | 0.000892 |
| Safety = high and Persons = more and Buying = low and Maint = med and Lug_boot = med | vgood | 0.000891 |
| Safety = high and Persons = more and Buying = med and Maint = low and Lug_boot = med | vgood | 0.000891 |
| Safety = high and Persons = 4 and Buying = low and Maint = low and Lug_boot = med | vgood | 0.000669 |
| Safety = high and Persons = 4 and Buying = med and Maint = low and Lug_boot = med | vgood | 0.000334 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Safety = low | unacc | 0.523124 |
| Persons = 2 | unacc | 0.430675 |
| Buying = vhigh and Maint = vhigh | unacc | 0.088409 |
| Buying = high and Maint = vhigh | unacc | 0.088409 |
| Safety = med and Lug_boot = small and Buying = vhigh | unacc | 0.045267 |
| Safety = med and Lug_boot = small and Buying = high | unacc | 0.043299 |
| Buying = high and Doors = 5more | acc | 0.115702 |
| Safety = med and Maint = high and Buying = low | acc | 0.085664 |
| Buying = high and Doors = 4 | acc | 0.108333 |
| Safety = med and Maint = high and Buying = vhigh | unacc | 0.034739 |
| Buying = high and Lug_boot = big | acc | 0.099099 |
| Maint = vhigh and Safety = high | acc | 0.163569 |
| Safety = med and Lug_boot = big and Buying = vhigh | acc | 0.069767 |
| Safety = med and Lug_boot = big and Maint = vhigh | acc | 0.065421 |
| Safety = med and Lug_boot = big and Buying = low | good | 0.042042 |
| Safety = med and Maint = vhigh and Lug_boot = small | unacc | 0.050336 |
| Buying = high and Safety = high and Persons = 4 | acc | 0.050000 |
| Buying = vhigh and Maint = low | acc | 0.116753 |
| Safety = med and Maint = vhigh and Doors = 2 | unacc | 0.015873 |
| Safety = med and Maint = vhigh | acc | 0.042320 |
| Buying = vhigh and Maint = high | unacc | 0.084291 |
| Safety = med and Maint = high and Lug_boot = big | acc | 0.052288 |
| Safety = med and Maint = high and Lug_boot = small | unacc | 0.033473 |
| Safety = med and Lug_boot = small and Persons = 4 | acc | 0.104575 |
| Buying = vhigh and Safety = high | acc | 0.111626 |
| Safety = med and Doors = 4 and Maint = med | acc | 0.049383 |
| Safety = med and Doors = 5more and Maint = med | acc | 0.036217 |
| Safety = med and Doors = 5more | good | 0.023256 |
| Safety = med and Doors = 4 and Persons = 4 | good | 0.018605 |
| Safety = med and Lug_boot = small and Doors = 2 | unacc | 0.022727 |
| Lug_boot = big and Safety = high and Maint = med | vgood | 0.094937 |
| Buying = high and Persons = more and Doors = 3 | acc | 0.060870 |
| Buying = high and Safety = med | unacc | 0.038462 |
| Lug_boot = big and Safety = high and Buying = low | vgood | 0.109589 |
| Maint = high and Buying = med and Safety = high | acc | 0.196668 |
| Safety = med and Maint = low and Lug_boot = med | acc | 0.037618 |
| Lug_boot = small and Doors = 5more and Maint = med | acc | 0.011628 |
| Safety = med and Lug_boot = small | acc | 0.065217 |
| Maint = low and Lug_boot = small | good | 0.120098 |
| Maint = low and Safety = high | vgood | 0.109012 |
| Maint = high and Buying = low and Lug_boot = small | acc | 0.082949 |
| Doors = 2 and Maint = med and Buying = med | acc | 0.097222 |
| Doors = 2 and Lug_boot = med and Safety = med | unacc | 0.075000 |
| Lug_boot = small and Buying = low | good | 0.089091 |
| Lug_boot = small | acc | 0.027778 |
| Safety = high and Doors = 2 | acc | 0.024242 |
| Safety = high and Persons = more | vgood | 0.071349 |
| Doors = 3 and Maint = med | acc | 0.102564 |
| Lug_boot = med and Safety = high | vgood | 0.035165 |
| Maint = low | good | 0.252083 |
|  | acc | 0.275862 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Safety = high and Buying = low and Lug_boot = big and Persons = 4 | vgood | 0.006834 |
| Safety = high and Persons = more and Buying = low and Lug_boot = big | vgood | 0.005371 |
| Safety = high and Buying = med and Maint = med and Lug_boot = big | vgood | 0.003558 |
| Safety = high and Lug_boot = med and Buying = low and Persons = more | vgood | 0.003286 |
| Safety = high and Buying = med and Maint = low and Lug_boot = big | vgood | 0.002974 |
| Buying = low and Maint = low and Safety = high and Persons = 4 | good | 0.003101 |
| Buying = low and Maint = med and Persons = 4 and Safety = high | good | 0.003542 |
| Safety = high and Persons = 4 and Maint = med and Buying = high | acc | 0.009483 |
| Safety = high and Persons = 4 and Buying = med and Maint = vhigh | acc | 0.010336 |
| Safety = high and Persons = 4 and Maint = med and Buying = vhigh | acc | 0.008628 |
| Persons = more and Safety = high and Lug_boot = big and Buying = med | acc | 0.006914 |
| Persons = more and Safety = high and Buying = high and Maint = med | acc | 0.008700 |
| Safety = med and Persons = more and Lug_boot = big and Buying = high | acc | 0.008290 |
| Persons = 4 and Safety = high and Maint = low and Buying = vhigh | acc | 0.009483 |
| Safety = med and Persons = 4 and Lug_boot = big and Buying = med | acc | 0.007470 |
| Persons = more and Safety = high and Maint = low and Buying = vhigh | acc | 0.007851 |
| Safety = med and Persons = more and Lug_boot = big and Buying = med | acc | 0.008290 |
| Safety = med and Persons = 4 and Buying = low and Maint = high | acc | 0.008628 |
| Safety = med and Persons = more and Lug_boot = med and Maint = med | acc | 0.007470 |
| Persons = 4 and Safety = high and Buying = low and Maint = vhigh | acc | 0.007772 |
| Persons = 4 and Safety = high and Maint = high and Buying = med | acc | 0.009483 |
| Safety = med and Persons = 4 and Maint = med and Buying = med | acc | 0.006914 |
| Persons = more and Safety = high and Buying = high and Maint = low | acc | 0.007851 |
| Safety = med and Persons = more and Buying = low and Maint = high | acc | 0.008700 |
| Persons = 4 and Safety = med and Maint = low and Buying = med | acc | 0.002846 |
| Safety = high and Persons = more and Maint = high and Buying = high | acc | 0.007001 |
| Safety = med and Persons = 4 and Lug_boot = big and Buying = high | acc | 0.006184 |
| Persons = more and Safety = high and Buying = med and Maint = high | acc | 0.005303 |
| Safety = med and Persons = more and Maint = low and Buying = vhigh | acc | 0.003548 |
| Persons = 4 and Safety = high and Buying = high and Maint = low | acc | 0.009483 |
| Safety = med and Persons = 4 and Buying = low and Lug_boot = small | acc | 0.004626 |
| Persons = more and Safety = med and Buying = low and Maint = vhigh | acc | 0.003548 |
| Safety = high and Persons = more and Maint = med and Buying = vhigh | acc | 0.007001 |
| Persons = 4 and Safety = high and Maint = high and Buying = high | acc | 0.008628 |
| Safety = med and Persons = 4 and Lug_boot = med and Doors = 4 | acc | 0.003972 |
| Safety = med and Persons = more and Buying = med and Lug_boot = med | acc | 0.003128 |
|  | unacc | 0.893355 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

persons|safety|acceptability
---|---|---
more|high|acc
4|high|acc
2|high|unacc
4|med|acc
more|med|acc
2|med|unacc
more|low|unacc
2|low|unacc
4|low|unacc

## JRip

Decision list:

rules | predicted class
---|---
(Safety = high) and (Buying = low) and (Lug_boot = big) and (Persons = 4)|vgood (14.0/2.0)
(Safety = high) and (Persons = more) and (Buying = low) and (Lug_boot = big)|vgood (15.0/4.0)
(Safety = high) and (Buying = med) and (Maint = med) and (Lug_boot = big)|vgood (12.0/4.0)
(Safety = high) and (Lug_boot = med) and (Buying = low) and (Persons = more)|vgood (13.0/5.0)
(Safety = high) and (Buying = med) and (Maint = low) and (Lug_boot = big)|vgood (11.0/4.0)
(Buying = low) and (Maint = low) and (Safety = high) and (Persons = 4)|good (8.0/2.0)
(Buying = low) and (Maint = med) and (Persons = 4) and (Safety = high)|good (7.0/1.0)
(Safety = high) and (Persons = 4) and (Maint = med) and (Buying = high)|acc (11.0/0.0)
(Safety = high) and (Persons = 4) and (Buying = med) and (Maint = vhigh)|acc (12.0/0.0)
(Safety = high) and (Persons = 4) and (Maint = med) and (Buying = vhigh)|acc (10.0/0.0)
(Persons = more) and (Safety = high) and (Lug_boot = big) and (Buying = med)|acc (8.0/0.0)
(Persons = more) and (Safety = high) and (Buying = high) and (Maint = med)|acc (12.0/1.0)
(Safety = med) and (Persons = more) and (Lug_boot = big) and (Buying = high)|acc (15.0/3.0)
(Persons = 4) and (Safety = high) and (Maint = low) and (Buying = vhigh)|acc (11.0/0.0)
(Safety = med) and (Persons = 4) and (Lug_boot = big) and (Buying = med)|acc (14.0/3.0)
(Persons = more) and (Safety = high) and (Maint = low) and (Buying = vhigh)|acc (11.0/1.0)
(Safety = med) and (Persons = more) and (Lug_boot = big) and (Buying = med)|acc (15.0/3.0)
(Safety = med) and (Persons = 4) and (Buying = low) and (Maint = high)|acc (10.0/0.0)
(Safety = med) and (Persons = more) and (Lug_boot = med) and (Maint = med)|acc (14.0/3.0)
(Persons = 4) and (Safety = high) and (Buying = low) and (Maint = vhigh)|acc (7.0/0.0)
(Persons = 4) and (Safety = high) and (Maint = high) and (Buying = med)|acc (11.0/0.0)
(Safety = med) and (Persons = 4) and (Maint = med) and (Buying = med)|acc (8.0/0.0)
(Persons = more) and (Safety = high) and (Buying = high) and (Maint = low)|acc (11.0/1.0)
(Safety = med) and (Persons = more) and (Buying = low) and (Maint = high)|acc (12.0/1.0)
(Persons = 4) and (Safety = med) and (Maint = low) and (Buying = med)|acc (8.0/2.0)
(Safety = high) and (Persons = more) and (Maint = high) and (Buying = high)|acc (10.0/1.0)
(Safety = med) and (Persons = 4) and (Lug_boot = big) and (Buying = high)|acc (14.0/4.0)
(Persons = more) and (Safety = high) and (Buying = med) and (Maint = high)|acc (8.0/1.0)
(Safety = med) and (Persons = more) and (Maint = low) and (Buying = vhigh)|acc (12.0/5.0)
(Persons = 4) and (Safety = high) and (Buying = high) and (Maint = low)|acc (11.0/0.0)
(Safety = med) and (Persons = 4) and (Buying = low) and (Lug_boot = small)|acc (12.0/4.0)
(Persons = more) and (Safety = med) and (Buying = low) and (Maint = vhigh)|acc (12.0/5.0)
(Safety = high) and (Persons = more) and (Maint = med) and (Buying = vhigh)|acc (10.0/1.0)
(Persons = 4) and (Safety = high) and (Maint = high) and (Buying = high)|acc (10.0/0.0)
(Safety = med) and (Persons = 4) and (Lug_boot = med) and (Doors = 4)|acc (13.0/5.0)
(Safety = med) and (Persons = more) and (Buying = med) and (Lug_boot = med)|acc (10.0/4.0)
|unacc (1151.0/105.0)


## PART

Decision list:

rules | predicted class
---|---
Safety = low|unacc (509.0)
Persons = 2|unacc (351.0)
Buying = vhigh AND Maint = vhigh|unacc (45.0)
Buying = high AND Maint = vhigh|unacc (45.0)
Safety = med AND Lug_boot = small AND Buying = vhigh|unacc (22.0)
Safety = med AND Lug_boot = small AND Buying = high|unacc (21.0)
Buying = high AND Doors = 5more|acc (28.0)
Safety = med AND Maint = high AND Buying = low|acc (22.0/1.0)
Buying = high AND Doors = 4|acc (26.0)
Safety = med AND Maint = high AND Buying = vhigh|unacc (14.0)
Buying = high AND Lug_boot = big|acc (22.0)
Maint = vhigh AND Safety = high|acc (43.0/2.0)
Safety = med AND Lug_boot = big AND Buying = vhigh|acc (15.0)
Safety = med AND Lug_boot = big AND Maint = vhigh|acc (14.0)
Safety = med AND Lug_boot = big AND Buying = low|good (14.0)
Safety = med AND Maint = vhigh AND Lug_boot = small|unacc (15.0)
Buying = high AND Safety = high AND Persons = 4|acc (9.0)
Buying = vhigh AND Maint = low|acc (30.0/4.0)
Safety = med AND Maint = vhigh AND Doors = 2|unacc (4.0)
Safety = med AND Maint = vhigh|acc (11.0/2.0)
Buying = vhigh AND Maint = high|unacc (22.0)
Safety = med AND Maint = high AND Lug_boot = big|acc (8.0)
Safety = med AND Maint = high AND Lug_boot = small|unacc (7.0)
Safety = med AND Lug_boot = small AND Persons = 4|acc (16.0)
Buying = vhigh AND Safety = high|acc (20.0/1.0)
Safety = med AND Doors = 4 AND Maint = med|acc (9.0/1.0)
Safety = med AND Doors = 5more AND Maint = med|acc (7.0/1.0)
Safety = med AND Doors = 5more|good (8.0/3.0)
Safety = med AND Doors = 4 AND Persons = 4|good (4.0/1.0)
Safety = med AND Lug_boot = small AND Doors = 2|unacc (4.0)
Lug_boot = big AND Safety = high AND Maint = med|vgood (15.0)
Buying = high AND Persons = more AND Doors = 3|acc (7.0)
Buying = high AND Safety = med|unacc (6.0)
Lug_boot = big AND Safety = high AND Buying = low|vgood (16.0)
Maint = high AND Buying = med AND Safety = high|acc (23.0/1.0)
Safety = med AND Maint = low AND Lug_boot = med|acc (8.0/2.0)
Lug_boot = small AND Doors = 5more AND Maint = med|acc (4.0/2.0)
Safety = med AND Lug_boot = small|acc (5.0)
Maint = low AND Lug_boot = small|good (16.0/2.0)
Maint = low AND Safety = high|vgood (21.0/6.0)
Maint = high AND Buying = low AND Lug_boot = small|acc (7.0/1.0)
Doors = 2 AND Maint = med AND Buying = med|acc (8.0/1.0)
Doors = 2 AND Lug_boot = med AND Safety = med|unacc (6.0/2.0)
Lug_boot = small AND Buying = low|good (6.0/1.0)
Lug_boot = small|acc (6.0/2.0)
Safety = high AND Doors = 2|acc (5.0/2.0)
Safety = high AND Persons = more|vgood (8.0)
Doors = 3 AND Maint = med|acc (9.0/3.0)
Lug_boot = med AND Safety = high|vgood (5.0/1.0)
Maint = low|good (4.0)
|acc (3.0/1.0)


## J48 Decision Tree

* Safety = low: unacc (509.0)
* Safety = med
	* Persons = 2: unacc (173.0)
	* Persons = 4
		* Buying = vhigh
			* Maint = vhigh: unacc (11.0)
			* Maint = high: unacc (11.0)
			* Maint = med
				* Lug_boot = small: unacc (3.0)
				* Lug_boot = med: unacc (3.0/1.0)
				* Lug_boot = big: acc (4.0)
			* Maint = low
				* Lug_boot = small: unacc (4.0)
				* Lug_boot = med: unacc (4.0/2.0)
				* Lug_boot = big: acc (3.0)
		* Buying = high
			* Lug_boot = small: unacc (15.0)
			* Lug_boot = med
				* Doors = 2: unacc (4.0)
				* Doors = 3: unacc (2.0)
				* Doors = 4: acc (4.0/1.0)
				* Doors = 5more: acc (3.0/1.0)
			* Lug_boot = big
				* Maint = vhigh: unacc (4.0)
				* Maint = high: acc (3.0)
				* Maint = med: acc (3.0)
				* Maint = low: acc (4.0)
		* Buying = med
			* Maint = vhigh
				* Lug_boot = small: unacc (4.0)
				* Lug_boot = med: unacc (4.0/2.0)
				* Lug_boot = big: acc (3.0)
			* Maint = high
				* Lug_boot = small: unacc (4.0)
				* Lug_boot = med: unacc (4.0/2.0)
				* Lug_boot = big: acc (4.0)
			* Maint = med: acc (12.0)
			* Maint = low
				* Lug_boot = small: acc (4.0)
				* Lug_boot = med: acc (4.0/2.0)
				* Lug_boot = big: good (3.0)
		* Buying = low
			* Maint = vhigh
				* Lug_boot = small: unacc (4.0)
				* Lug_boot = med: unacc (4.0/2.0)
				* Lug_boot = big: acc (3.0)
			* Maint = high: acc (10.0)
			* Maint = med
				* Lug_boot = small: acc (4.0)
				* Lug_boot = med: good (3.0/1.0)
				* Lug_boot = big: good (4.0)
			* Maint = low
				* Lug_boot = small: acc (4.0)
				* Lug_boot = med: acc (4.0/2.0)
				* Lug_boot = big: good (3.0)
	* Persons = more
		* Lug_boot = small
			* Buying = vhigh: unacc (13.0)
			* Buying = high: unacc (14.0)
			* Buying = med
				* Maint = vhigh: unacc (3.0)
				* Maint = high: unacc (3.0)
				* Maint = med: unacc (2.0/1.0)
				* Maint = low: acc (4.0/1.0)
			* Buying = low
				* Maint = vhigh: unacc (4.0)
				* Maint = high: acc (4.0/1.0)
				* Maint = med: acc (4.0/1.0)
				* Maint = low: acc (3.0/1.0)
		* Lug_boot = med
			* Maint = vhigh
				* Buying = vhigh: unacc (4.0)
				* Buying = high: unacc (4.0)
				* Buying = med: acc (3.0/1.0)
				* Buying = low: acc (4.0/1.0)
			* Maint = high
				* Buying = vhigh: unacc (4.0)
				* Buying = high: acc (1.0)
				* Buying = med: acc (4.0/1.0)
				* Buying = low: acc (4.0)
			* Maint = med: acc (14.0/3.0)
			* Maint = low
				* Buying = vhigh: acc (4.0/1.0)
				* Buying = high: acc (3.0/1.0)
				* Buying = med: good (3.0/1.0)
				* Buying = low: good (3.0/1.0)
		* Lug_boot = big
			* Buying = vhigh
				* Maint = vhigh: unacc (4.0)
				* Maint = high: unacc (3.0)
				* Maint = med: acc (4.0)
				* Maint = low: acc (4.0)
			* Buying = high
				* Maint = vhigh: unacc (3.0)
				* Maint = high: acc (4.0)
				* Maint = med: acc (4.0)
				* Maint = low: acc (4.0)
			* Buying = med
				* Maint = vhigh: acc (4.0)
				* Maint = high: acc (4.0)
				* Maint = med: acc (4.0)
				* Maint = low: good (3.0)
			* Buying = low
				* Maint = vhigh: acc (4.0)
				* Maint = high: acc (4.0)
				* Maint = med: good (3.0)
				* Maint = low: good (4.0)
* Safety = high
	* Persons = 2: unacc (178.0)
	* Persons = 4
		* Buying = vhigh
			* Maint = vhigh: unacc (12.0)
			* Maint = high: unacc (12.0)
			* Maint = med: acc (10.0)
			* Maint = low: acc (11.0)
		* Buying = high
			* Maint = vhigh: unacc (12.0)
			* Maint = high: acc (10.0)
			* Maint = med: acc (11.0)
			* Maint = low: acc (11.0)
		* Buying = med
			* Maint = vhigh: acc (12.0)
			* Maint = high: acc (11.0)
			* Maint = med
				* Lug_boot = small: acc (4.0)
				* Lug_boot = med: acc (4.0/2.0)
				* Lug_boot = big: vgood (4.0)
			* Maint = low
				* Lug_boot = small: good (4.0)
				* Lug_boot = med: vgood (2.0/1.0)
				* Lug_boot = big: vgood (4.0)
		* Buying = low
			* Maint = vhigh: acc (9.0)
			* Maint = high
				* Lug_boot = small: acc (3.0)
				* Lug_boot = med: acc (3.0/1.0)
				* Lug_boot = big: vgood (4.0)
			* Maint = med
				* Lug_boot = small: good (4.0)
				* Lug_boot = med: good (3.0/1.0)
				* Lug_boot = big: vgood (4.0)
			* Maint = low
				* Lug_boot = small: good (4.0)
				* Lug_boot = med: vgood (4.0/2.0)
				* Lug_boot = big: vgood (4.0)
	* Persons = more
		* Buying = vhigh
			* Maint = vhigh: unacc (12.0)
			* Maint = high: unacc (10.0)
			* Maint = med: acc (10.0/1.0)
			* Maint = low: acc (11.0/1.0)
		* Buying = high
			* Maint = vhigh: unacc (10.0)
			* Maint = high: acc (10.0/1.0)
			* Maint = med: acc (12.0/1.0)
			* Maint = low: acc (11.0/1.0)
		* Buying = med
			* Maint = vhigh: acc (11.0/1.0)
			* Maint = high: acc (12.0/1.0)
			* Maint = med
				* Lug_boot = small: acc (4.0/1.0)
				* Lug_boot = med: vgood (4.0/1.0)
				* Lug_boot = big: vgood (4.0)
			* Maint = low
				* Lug_boot = small: good (4.0/1.0)
				* Lug_boot = med: vgood (3.0/1.0)
				* Lug_boot = big: vgood (3.0)
		* Buying = low
			* Maint = vhigh: acc (11.0/1.0)
			* Maint = high
				* Lug_boot = small: acc (4.0/1.0)
				* Lug_boot = med: vgood (3.0)
				* Lug_boot = big: vgood (4.0)
			* Maint = med
				* Lug_boot = small: good (4.0/1.0)
				* Lug_boot = med: vgood (3.0/1.0)
				* Lug_boot = big: vgood (3.0)
			* Maint = low
				* Lug_boot = small: good (3.0)
				* Lug_boot = med: vgood (4.0/1.0)
				* Lug_boot = big: vgood (4.0)


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
									* Lug_boot!=(big)|(small)
										* Persons=(more)|(2): vgood(3.0/0.0)
										* Persons!=(more)|(2): good(2.0/1.0)
								* Doors!=(5more)|(4)|(3)
							* Lug_boot=(big): vgood(7.0/0.0)
							* Lug_boot!=(big)
										* Buying=(low)|(vhigh)|(high): good(4.0/0.0)
										* Buying!=(low)|(vhigh)|(high): acc(2.0/2.0)
						* Lug_boot!=(big)|(med)
						* Buying=(low)
									* Doors=(5more)|(4)|(3): good(12.0/0.0)
									* Doors!=(5more)|(4)|(3): good(2.0/1.0)
						* Buying!=(low)
									* Maint=(low)|(vhigh)|(high): good(7.0/1.0)
									* Maint!=(low)|(vhigh)|(high): acc(7.0/1.0)
					* Safety!=(high)|(low)
						* Lug_boot=(big)|(med)
						* Buying=(low)
									* Doors=(5more)|(4)|(3)
										* Doors=(5more)|(4)|(2): good(13.0/0.0)
										* Doors!=(5more)|(4)|(2)
										* Persons=(more)|(2): good(3.0/0.0)
										* Persons!=(more)|(2): good(2.0/1.0)
									* Doors!=(5more)|(4)|(3)
								* Lug_boot=(big): good(3.0/0.0)
								* Lug_boot!=(big): acc(4.0/0.0)
						* Buying!=(low)
							* Maint=(low)
										* Doors=(5more)|(4)|(3)
											* Doors=(5more)|(4)|(2): good(6.0/0.0)
											* Doors!=(5more)|(4)|(2): good(3.0/1.0)
										* Doors!=(5more)|(4)|(3): acc(2.0/1.0)
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
									* Lug_boot!=(big)|(small)
										* Doors=(5more)|(4): vgood(3.0/0.0)
										* Doors!=(5more)|(4): acc(2.0/1.0)
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
									* Doors!=(5more)|(4)|(3)
								* Safety=(high): acc(3.0/0.0)
								* Safety!=(high): unacc(4.0/0.0)
					* Lug_boot!=(big)|(med)
						* Safety=(high)|(low)
								* Doors=(5more)|(4)|(3): acc(23.0/0.0)
								* Doors!=(5more)|(4)|(3)
								* Persons=(more)|(2): unacc(4.0/0.0)
								* Persons!=(more)|(2): acc(3.0/0.0)
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
									* Safety=(high)|(low): acc(8.0/0.0)
									* Safety!=(high)|(low)
										* Lug_boot=(big)|(small): acc(3.0/0.0)
										* Lug_boot!=(big)|(small): unacc(3.0/0.0)
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
									* Doors!=(5more)|(4)|(3)
									* Lug_boot=(big)|(small): acc(4.0/0.0)
									* Lug_boot!=(big)|(small): acc(2.0/1.0)
							* Lug_boot!=(big)|(med)
								* Safety=(high)|(low): acc(7.0/1.0)
								* Safety!=(high)|(low): unacc(6.0/0.0)
					* Buying!=(high): unacc(44.0/0.0)
				* Maint!=(high): unacc(90.0/0.0)
		* Safety!=(high)|(med): unacc(342.0/0.0)
	* Persons!=(more)|(4): unacc(518.0/0.0)


