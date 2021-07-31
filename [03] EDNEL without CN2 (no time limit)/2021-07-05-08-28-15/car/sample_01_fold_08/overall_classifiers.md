# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | unacc | 0.701675 |
| Safety = high and Persons = 4 and Buying = low and Maint = vhigh | acc | 0.009844 |
| Safety = high and Persons = 4 and Buying = high and Maint = med | acc | 0.009844 |
| Buying = vhigh and Maint = med and Persons = 4 and Safety = high | acc | 0.009844 |
| Buying = med and Maint = vhigh and Persons = 4 and Safety = high | acc | 0.009844 |
| Buying = vhigh and Maint = low and Persons = 4 and Safety = high | acc | 0.009844 |
| Safety = med and Persons = 4 and Buying = med and Maint = med | acc | 0.009844 |
| Safety = high and Persons = 4 and Buying = med and Maint = high | acc | 0.009844 |
| Buying = low and Maint = high and Persons = 4 and Safety = med | acc | 0.009031 |
| Buying = high and Maint = low and Persons = 4 and Safety = high | acc | 0.009031 |
| Safety = high and Persons = more and Buying = vhigh and Maint = low | acc | 0.008285 |
| Buying = high and Maint = high and Persons = more and Safety = high | acc | 0.007476 |
| Buying = high and Maint = high and Persons = 4 and Safety = high | acc | 0.008217 |
| Safety = high and Persons = more and Buying = high and Maint = low | acc | 0.007476 |
| Safety = med and Persons = more and Lug_boot = big and Buying = high | acc | 0.006336 |
| Buying = low and Maint = high and Persons = more and Safety = med | acc | 0.006667 |
| Buying = med and Maint = high and Persons = more and Safety = high | acc | 0.006667 |
| Buying = med and Maint = med and Persons = more and Safety = med | acc | 0.006667 |
| Buying = high and Maint = med and Persons = more and Safety = high | acc | 0.006667 |
| Buying = vhigh and Maint = med and Persons = more and Safety = high | acc | 0.007401 |
| Buying = low and Maint = vhigh and Persons = more and Safety = high | acc | 0.006667 |
| Safety = med and Persons = 4 and Buying = high and Lug_boot = big | acc | 0.005141 |
| Buying = med and Maint = vhigh and Persons = more and Safety = high | acc | 0.005858 |
| Safety = med and Persons = more and Lug_boot = med and Buying = high | acc | 0.003781 |
| Safety = high and Persons = more and Buying = low and Lug_boot = big | vgood | 0.006387 |
| Safety = med and Persons = 4 and Buying = vhigh and Maint = low | acc | 0.002978 |
| Buying = med and Maint = vhigh and Persons = 4 and Safety = med | acc | 0.002486 |
| Buying = low and Maint = vhigh and Persons = more and Safety = med | acc | 0.002978 |
| Safety = med and Persons = 4 and Buying = med and Maint = high | acc | 0.002978 |
| Buying = vhigh and Maint = med and Persons = more and Safety = med | acc | 0.002978 |
| Buying = vhigh and Maint = med and Persons = 4 and Safety = med | acc | 0.002486 |
| Safety = med and Persons = more and Lug_boot = big and Buying = low | good | 0.002525 |
| Buying = vhigh and Maint = low and Persons = more and Safety = med | acc | 0.002978 |
| Buying = low and Maint = vhigh and Persons = 4 and Safety = med | acc | 0.002486 |
| Safety = high and Persons = more and Buying = low and Lug_boot = med | vgood | 0.003384 |
| Safety = high and Persons = more and Buying = low and Lug_boot = small | good | 0.001726 |
| Buying = low and Maint = high and Persons = 4 and Safety = high | acc | 0.003306 |
| Safety = med and Persons = more and Lug_boot = med and Buying = med | acc | 0.004069 |
| Buying = med and Maint = low and Persons = more and Safety = high | vgood | 0.003004 |
| Buying = med and Maint = low and Persons = more and Safety = med | good | 0.002192 |
| Safety = med and Persons = more and Lug_boot = big and Buying = med | acc | 0.005565 |
| Safety = high and Persons = more and Buying = med and Maint = med | vgood | 0.002730 |
| Buying = low and Maint = low and Persons = 4 and Safety = med | acc | 0.002709 |
| Buying = med and Maint = low and Persons = 4 and Safety = high | good | 0.002192 |
| Safety = med and Persons = 4 and Buying = med and Maint = low | acc | 0.002709 |
| Safety = high and Persons = 4 and Buying = low and Maint = low | vgood | 0.002189 |
| Buying = low and Maint = med and Persons = 4 and Safety = med | good | 0.001676 |
| Safety = med and Persons = 4 and Buying = low and Maint = med | acc | 0.002071 |
| Buying = med and Maint = med and Persons = 4 and Safety = high | vgood | 0.001858 |
| Safety = high and Persons = 4 and Buying = low and Maint = med | vgood | 0.001673 |
| Buying = low and Maint = med and Persons = more and Safety = med | good | 0.002980 |
| Buying = low and Maint = low and Persons = more and Safety = med | good | 0.002192 |
| Safety = med and Persons = more and Lug_boot = med and Buying = low | acc | 0.004463 |
| Safety = med and Persons = 4 and Buying != med and Maint = med and Lug_boot = med and Lug_boot!=(big) and Safety != low and Doors = 4 | acc | 0.001104 |
| Safety = med and Persons = 4 and Buying != med and Maint = med and Lug_boot = med and Lug_boot!=(big) and Safety != low and Doors = 5more | acc | 0.001104 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Safety = low | unacc | 0.532795 |
| Persons = 2 | unacc | 0.422693 |
| Buying = vhigh and Maint = vhigh | unacc | 0.083168 |
| Buying = high and Maint = vhigh | unacc | 0.086785 |
| Safety = med and Lug_boot = small and Buying = high | unacc | 0.045361 |
| Buying = high and Doors = 5more | acc | 0.107692 |
| Safety = med and Lug_boot = small and Buying = vhigh | unacc | 0.037611 |
| Safety = med and Maint = high and Buying = vhigh | unacc | 0.033333 |
| Safety = med and Lug_boot = big and Maint = high | acc | 0.074074 |
| Safety = med and Lug_boot = big and Buying = med | acc | 0.045089 |
| Buying = high and Safety = high and Persons = 4 | acc | 0.107143 |
| Safety = med and Lug_boot = big and Buying = vhigh | acc | 0.069767 |
| Safety = med and Lug_boot = big and Buying = high | acc | 0.052133 |
| Safety = med and Lug_boot = big and Persons = 4 | good | 0.021007 |
| Safety = med and Lug_boot = small and Maint = vhigh | unacc | 0.044444 |
| Buying = high and Doors = 2 | unacc | 0.013212 |
| Buying = high and Safety = high | acc | 0.112903 |
| Maint = vhigh and Safety = high and Lug_boot = med | acc | 0.083333 |
| Safety = med and Lug_boot = small and Maint = low | acc | 0.069209 |
| Buying = vhigh and Maint = high | unacc | 0.069620 |
| Safety = med and Lug_boot = small and Maint = high | unacc | 0.015444 |
| Safety = med and Doors = 5more and Persons = more | acc | 0.044964 |
| Safety = med and Doors = 4 and Buying = low | good | 0.010570 |
| Safety = med and Doors = 4 and Persons = 4 | acc | 0.092019 |
| Safety = med and Doors = 2 and Buying = low | acc | 0.052910 |
| Lug_boot = big and Buying = vhigh | acc | 0.097902 |
| Lug_boot = big and Maint = vhigh | acc | 0.116438 |
| Lug_boot = big and Maint = med | vgood | 0.056517 |
| Lug_boot = big and Maint = low | vgood | 0.051068 |
| Buying = vhigh and Safety = high and Persons = 4 | acc | 0.136752 |
| Lug_boot = small and Maint = low | good | 0.044846 |
| Safety = med and Doors = 2 | unacc | 0.051119 |
| Lug_boot = small and Doors = 3 | acc | 0.148711 |
| Buying = vhigh | acc | 0.160556 |
| Maint = vhigh | acc | 0.136116 |
| Buying = med and Maint = high and Persons = 4 | acc | 0.136364 |
| Safety = med and Buying = med | acc | 0.090000 |
| Lug_boot = small | acc | 0.066301 |
| Safety = med | acc | 0.054875 |
| Doors = 3 | vgood | 0.038889 |
| Doors = 4 | vgood | 0.111213 |
| Doors = 5more | vgood | 0.093220 |
|  | good | 0.516667 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Safety = high and Buying = low and Lug_boot = big and Persons = more | vgood | 0.006387 |
| Safety = high and Buying = low and Lug_boot = med and Persons = more | vgood | 0.003384 |
| Safety = high and Buying = med and Maint = low and Persons = more | vgood | 0.003004 |
| Safety = high and Persons = 4 and Buying = low and Lug_boot = big | vgood | 0.003560 |
| Safety = high and Buying = med and Maint = med and Lug_boot = big | vgood | 0.003271 |
| Safety = high and Lug_boot = med and Persons = 4 and Buying = low | vgood | 0.001610 |
| Buying = low and Safety = med and Maint = med and Lug_boot = big | good | 0.003078 |
| Maint = low and Buying = med and Persons = 4 and Safety = high | good | 0.002265 |
| Buying = low and Maint = low and Persons = more and Safety = med | good | 0.002265 |
| Buying = low and Safety = high and Persons = 4 | good | 0.002487 |
| Maint = low and Safety = med and Buying = med and Lug_boot = big | good | 0.003078 |
| Buying = low and Persons = more and Safety = high | good | 0.001857 |
| Safety = high and Persons = 4 | acc | 0.063368 |
| Safety = med and Persons = 4 and Lug_boot = big | acc | 0.022370 |
| Persons = more and Safety = high | acc | 0.044711 |
| Persons = more and Safety = med and Lug_boot = big | acc | 0.020963 |
| Safety = med and Persons = 4 and Buying = low | acc | 0.011550 |
| Safety = med and Persons = more and Lug_boot = med | acc | 0.015135 |
| Safety = med and Persons = 4 and Buying = med | acc | 0.009958 |
|  | unacc | 0.956942 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

buying|maint|persons|safety|acceptability
---|---|---|---|---
med|low|more|high|vgood
vhigh|low|more|high|acc
high|low|more|high|acc
low|low|more|high|vgood
high|med|more|high|acc
vhigh|med|more|high|acc
med|med|more|high|vgood
low|med|more|high|vgood
med|low|4|high|good
low|low|4|high|vgood
high|high|more|high|acc
vhigh|low|4|high|acc
high|low|4|high|acc
low|high|more|high|vgood
med|high|more|high|acc
vhigh|high|more|high|unacc
vhigh|low|more|med|acc
low|med|4|high|vgood
med|vhigh|more|high|acc
vhigh|med|4|high|acc
med|low|more|med|good
high|med|4|high|acc
med|med|4|high|vgood
high|low|more|med|acc
high|vhigh|more|high|unacc
vhigh|vhigh|more|high|unacc
low|low|more|med|good
low|vhigh|more|high|acc
low|high|4|high|acc
low|med|more|med|good
med|high|4|high|acc
high|high|4|high|acc
med|med|more|med|acc
med|low|2|high|unacc
vhigh|low|2|high|unacc
vhigh|high|4|high|unacc
high|med|more|med|acc
high|low|2|high|unacc
low|low|2|high|unacc
vhigh|med|more|med|acc
low|vhigh|4|high|acc
med|vhigh|4|high|acc
low|low|4|med|acc
med|high|more|med|unacc
med|low|4|med|acc
low|high|more|med|acc
high|high|more|med|unacc
low|med|2|high|unacc
med|med|2|high|unacc
high|vhigh|4|high|unacc
vhigh|high|more|med|unacc
high|med|2|high|unacc
vhigh|low|4|med|acc
vhigh|vhigh|4|high|unacc
high|low|4|med|unacc
vhigh|med|2|high|unacc
low|med|4|med|good
low|low|more|low|unacc
high|med|4|med|unacc
med|vhigh|more|med|unacc
med|med|4|med|acc
med|high|2|high|unacc
vhigh|low|more|low|unacc
high|high|2|high|unacc
high|low|more|low|unacc
low|vhigh|more|med|acc
vhigh|high|2|high|unacc
vhigh|med|4|med|acc
med|low|more|low|unacc
low|high|2|high|unacc
vhigh|vhigh|more|med|unacc
high|vhigh|more|med|unacc
high|low|2|med|unacc
low|high|4|med|acc
med|high|4|med|acc
low|vhigh|2|high|unacc
med|low|2|med|unacc
vhigh|high|4|med|unacc
vhigh|med|more|low|unacc
med|med|more|low|unacc
low|low|2|med|unacc
vhigh|vhigh|2|high|unacc
high|vhigh|2|high|unacc
high|high|4|med|unacc
vhigh|low|2|med|unacc
med|vhigh|2|high|unacc
low|med|more|low|unacc
high|med|more|low|unacc
vhigh|low|4|low|unacc
high|vhigh|4|med|unacc
med|low|4|low|unacc
vhigh|med|2|med|unacc
med|med|2|med|unacc
low|vhigh|4|med|acc
med|high|more|low|unacc
low|low|4|low|unacc
low|med|2|med|unacc
low|high|more|low|unacc
med|vhigh|4|med|acc
high|low|4|low|unacc
high|med|2|med|unacc
high|high|more|low|unacc
vhigh|vhigh|4|med|unacc
vhigh|high|more|low|unacc
low|vhigh|more|low|unacc
high|med|4|low|unacc
high|high|2|med|unacc
low|med|4|low|unacc
high|vhigh|more|low|unacc
med|high|2|med|unacc
low|high|2|med|unacc
vhigh|med|4|low|unacc
vhigh|high|2|med|unacc
med|med|4|low|unacc
med|vhigh|more|low|unacc
vhigh|vhigh|more|low|unacc
high|high|4|low|unacc
med|high|4|low|unacc
high|low|2|low|unacc
vhigh|vhigh|2|med|unacc
med|low|2|low|unacc
vhigh|low|2|low|unacc
low|low|2|low|unacc
low|high|4|low|unacc
med|vhigh|2|med|unacc
vhigh|high|4|low|unacc
high|vhigh|2|med|unacc
low|vhigh|2|med|unacc
med|med|2|low|unacc
high|vhigh|4|low|unacc
high|med|2|low|unacc
low|vhigh|4|low|unacc
vhigh|med|2|low|unacc
low|med|2|low|unacc
med|vhigh|4|low|unacc
vhigh|vhigh|4|low|unacc
med|high|2|low|unacc
high|high|2|low|unacc
vhigh|high|2|low|unacc
low|high|2|low|unacc
vhigh|vhigh|2|low|unacc
low|vhigh|2|low|unacc
med|vhigh|2|low|unacc
high|vhigh|2|low|unacc

## JRip

Decision list:

rules | predicted class
---|---
(Safety = high) and (Buying = low) and (Lug_boot = big) and (Persons = more)|vgood (15.0/3.0)
(Safety = high) and (Buying = low) and (Lug_boot = med) and (Persons = more)|vgood (16.0/7.0)
(Safety = high) and (Buying = med) and (Maint = low) and (Persons = more)|vgood (8.0/2.0)
(Safety = high) and (Persons = 4) and (Buying = low) and (Lug_boot = big)|vgood (12.0/4.0)
(Safety = high) and (Buying = med) and (Maint = med) and (Lug_boot = big)|vgood (10.0/3.0)
(Safety = high) and (Lug_boot = med) and (Persons = 4) and (Buying = low)|vgood (15.0/9.0)
(Buying = low) and (Safety = med) and (Maint = med) and (Lug_boot = big)|good (11.0/4.0)
(Maint = low) and (Buying = med) and (Persons = 4) and (Safety = high)|good (11.0/5.0)
(Buying = low) and (Maint = low) and (Persons = more) and (Safety = med)|good (11.0/5.0)
(Buying = low) and (Safety = high) and (Persons = 4)|good (15.0/8.0)
(Maint = low) and (Safety = med) and (Buying = med) and (Lug_boot = big)|good (11.0/4.0)
(Buying = low) and (Persons = more) and (Safety = high)|good (14.0/8.0)
(Safety = high) and (Persons = 4)|acc (119.0/34.0)
(Safety = med) and (Persons = 4) and (Lug_boot = big)|acc (51.0/15.0)
(Persons = more) and (Safety = high)|acc (113.0/43.0)
(Persons = more) and (Safety = med) and (Lug_boot = big)|acc (43.0/11.0)
(Safety = med) and (Persons = 4) and (Buying = low)|acc (30.0/9.0)
(Safety = med) and (Persons = more) and (Lug_boot = med)|acc (52.0/23.0)
(Safety = med) and (Persons = 4) and (Buying = med)|acc (29.0/11.0)
|unacc (966.0/20.0)


## PART

Decision list:

rules | predicted class
---|---
Safety = low|unacc (528.0)
Persons = 2|unacc (339.0)
Buying = vhigh AND Maint = vhigh|unacc (42.0)
Buying = high AND Maint = vhigh|unacc (44.0)
Safety = med AND Lug_boot = small AND Buying = high|unacc (22.0)
Buying = high AND Doors = 5more|acc (28.0)
Safety = med AND Lug_boot = small AND Buying = vhigh|unacc (17.0)
Safety = med AND Maint = high AND Buying = vhigh|unacc (15.0)
Safety = med AND Lug_boot = big AND Maint = high|acc (16.0)
Safety = med AND Lug_boot = big AND Buying = med|acc (21.0/7.0)
Buying = high AND Safety = high AND Persons = 4|acc (24.0)
Safety = med AND Lug_boot = big AND Buying = vhigh|acc (15.0)
Safety = med AND Lug_boot = big AND Buying = high|acc (11.0)
Safety = med AND Lug_boot = big AND Persons = 4|good (11.0/4.0)
Safety = med AND Lug_boot = small AND Maint = vhigh|unacc (16.0)
Buying = high AND Doors = 2|unacc (14.0/6.0)
Buying = high AND Safety = high|acc (15.0)
Maint = vhigh AND Safety = high AND Lug_boot = med|acc (15.0)
Safety = med AND Lug_boot = small AND Maint = low|acc (16.0/2.0)
Buying = vhigh AND Maint = high|unacc (22.0)
Safety = med AND Lug_boot = small AND Maint = high|unacc (14.0/6.0)
Safety = med AND Doors = 5more AND Persons = more|acc (14.0/5.0)
Safety = med AND Doors = 4 AND Buying = low|good (11.0/5.0)
Safety = med AND Doors = 4 AND Persons = 4|acc (10.0/1.0)
Safety = med AND Doors = 2 AND Buying = low|acc (11.0/3.0)
Lug_boot = big AND Buying = vhigh|acc (14.0)
Lug_boot = big AND Maint = vhigh|acc (15.0)
Lug_boot = big AND Maint = med|vgood (15.0/1.0)
Lug_boot = big AND Maint = low|vgood (15.0/1.0)
Buying = vhigh AND Safety = high AND Persons = 4|acc (16.0)
Lug_boot = small AND Maint = low|good (17.0/5.0)
Safety = med AND Doors = 2|unacc (13.0/4.0)
Lug_boot = small AND Doors = 3|acc (14.0/2.0)
Buying = vhigh|acc (17.0/2.0)
Maint = vhigh|acc (18.0/4.0)
Buying = med AND Maint = high AND Persons = 4|acc (12.0)
Safety = med AND Buying = med|acc (10.0/2.0)
Lug_boot = small|acc (18.0/8.0)
Safety = med|acc (16.0/6.0)
Doors = 3|vgood (13.0/6.0)
Doors = 4|vgood (13.0/2.0)
Doors = 5more|vgood (13.0/2.0)
|good (12.0/6.0)


## J48 Decision Tree

* Safety = low: unacc (528.0)
* Safety = med
	* Persons = 2: unacc (174.0)
	* Persons = 4
		* Buying = vhigh
			* Maint = vhigh: unacc (11.0)
			* Maint = high: unacc (12.0)
			* Maint = med: unacc (12.0/6.0)
			* Maint = low: acc (10.0/4.0)
		* Buying = high
			* Lug_boot = small: unacc (16.0)
			* Lug_boot = med: unacc (15.0/6.0)
			* Lug_boot = big: acc (13.0/4.0)
		* Buying = med
			* Maint = vhigh: unacc (12.0/6.0)
			* Maint = high: acc (10.0/4.0)
			* Maint = med: acc (12.0)
			* Maint = low: acc (11.0/5.0)
		* Buying = low
			* Maint = vhigh: unacc (12.0/6.0)
			* Maint = high: acc (11.0)
			* Maint = med: acc (10.0/5.0)
			* Maint = low: acc (11.0/5.0)
	* Persons = more
		* Lug_boot = small
			* Buying = vhigh: unacc (10.0)
			* Buying = high: unacc (13.0)
			* Buying = med: unacc (16.0/6.0)
			* Buying = low: unacc (14.0/7.0)
		* Lug_boot = med
			* Buying = vhigh: unacc (14.0/5.0)
			* Buying = high: acc (14.0/6.0)
			* Buying = med: acc (13.0/5.0)
			* Buying = low: acc (15.0/6.0)
		* Lug_boot = big
			* Buying = vhigh: unacc (15.0/7.0)
			* Buying = high: acc (13.0/3.0)
			* Buying = med: acc (12.0/3.0)
			* Buying = low: good (13.0/6.0)
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
			* Maint = med: vgood (9.0/4.0)
			* Maint = low: good (11.0/5.0)
		* Buying = low
			* Maint = vhigh: acc (12.0)
			* Maint = high: acc (9.0/3.0)
			* Maint = med: vgood (10.0/5.0)
			* Maint = low: vgood (11.0/5.0)
	* Persons = more
		* Buying = vhigh
			* Maint = vhigh: unacc (10.0)
			* Maint = high: unacc (11.0)
			* Maint = med: acc (9.0)
			* Maint = low: acc (12.0/1.0)
		* Buying = high
			* Maint = vhigh: unacc (12.0)
			* Maint = high: acc (11.0/1.0)
			* Maint = med: acc (10.0/1.0)
			* Maint = low: acc (11.0/1.0)
		* Buying = med
			* Maint = vhigh: acc (9.0/1.0)
			* Maint = high: acc (10.0/1.0)
			* Maint = med: vgood (12.0/5.0)
			* Maint = low: vgood (8.0/2.0)
		* Buying = low
			* Lug_boot = small: good (14.0/8.0)
			* Lug_boot = med: vgood (16.0/7.0)
			* Lug_boot = big: vgood (15.0/3.0)


## SimpleCart Decision Tree

	* Safety=(high)|(med)
		* Persons=(more)|(4)
			* Buying=(low)|(med)
				* Maint=(low)|(med)
				* Safety=(high)
						* Lug_boot=(big)|(med): vgood(48.0/11.0)
						* Lug_boot!=(big)|(med): good(18.0/8.0)
				* Safety!=(high)
						* Lug_boot=(big)|(med)
								* Buying=(low)|(vhigh)|(high): good(23.0/6.0)
								* Buying!=(low)|(vhigh)|(high)
									* Maint=(low)|(vhigh)|(high): good(11.0/3.0)
									* Maint!=(low)|(vhigh)|(high): acc(14.0/0.0)
						* Lug_boot!=(big)|(med): acc(26.0/4.0)
				* Maint!=(low)|(med)
					* Lug_boot=(big)|(med): acc(95.0/17.0)
					* Lug_boot!=(big)|(med)
					* Safety=(high): acc(24.0/4.0)
					* Safety!=(high): unacc(24.0/6.0)
			* Buying!=(low)|(med)
				* Maint=(low)|(med)
					* Lug_boot=(big)|(med)
					* Lug_boot=(big): acc(59.0/0.0)
					* Lug_boot!=(big)
							* Safety=(high)|(low): acc(30.0/0.0)
							* Safety!=(high)|(low)
								* Doors=(5more)|(4): acc(15.0/0.0)
								* Doors!=(5more)|(4): unacc(11.0/4.0)
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


