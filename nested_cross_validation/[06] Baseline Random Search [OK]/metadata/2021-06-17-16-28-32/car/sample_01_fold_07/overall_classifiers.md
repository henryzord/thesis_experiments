# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Persons != 4 | unacc | 0.606920 |
| Persons != more | unacc | 0.599575 |
| Safety = med and Persons = more and Lug_boot = big | acc | 0.018687 |
| Safety = med and Persons = more and Lug_boot = med | acc | 0.014393 |
| Safety = med and Persons = 4 and Buying = med | acc | 0.013919 |
| Safety = med and Persons = 4 and Buying = low | acc | 0.012928 |
| Buying = low and Maint = vhigh and Persons = 4 and Safety = high | acc | 0.009844 |
| Buying = vhigh and Maint = low and Persons = 4 and Safety = high | acc | 0.009844 |
| Buying = high and Maint = high and Persons = 4 and Safety = high | acc | 0.009844 |
| Buying = med and Maint = high and Persons = more and Safety = high | acc | 0.008285 |
| Buying = high and Maint = low and Persons = more and Safety = high | acc | 0.008285 |
| Buying = vhigh and Maint = med and Persons = 4 and Safety = high | acc | 0.009031 |
| Safety = high and Persons = more and Buying = med and Maint = vhigh | acc | 0.008285 |
| Buying = low and Maint = vhigh and Persons = more and Safety = high | acc | 0.007476 |
| Safety = high and Persons = more and Buying = high and Maint = high | acc | 0.007476 |
| Safety = high and Persons = 4 and Buying = med and Maint = high | acc | 0.008217 |
| Safety = high and Persons = 4 and Buying = med and Maint = vhigh | acc | 0.008217 |
| Safety = high and Persons = 4 and Buying = high and Maint = med | acc | 0.008217 |
| Buying = high and Maint = med and Persons = more and Safety = high | acc | 0.007476 |
| Buying = vhigh and Maint = low and Persons = more and Safety = high | acc | 0.008217 |
| Safety = med and Persons = 4 and Buying = high and Lug_boot = big | acc | 0.006859 |
| Safety = high and Persons = 4 and Buying = high and Maint = low | acc | 0.007401 |
| Safety = high and Persons = more and Buying = vhigh and Maint = med | acc | 0.006667 |
| Buying = low and Maint = med and Persons = 4 and Safety = med | good | 0.002009 |
| Buying = low and Maint = low and Persons = 4 and Safety = med | good | 0.002408 |
| Buying = vhigh and Maint = med and Persons = 4 and Safety = med | acc | 0.002709 |
| Safety = high and Persons = more and Buying = low and Maint = high | vgood | 0.002728 |
| Buying = med and Maint = low and Persons = 4 and Safety = med | good | 0.001674 |
| Safety = high and Persons = more and Buying = med and Maint = med | vgood | 0.002728 |
| Buying = med and Maint = low and Persons = more and Safety = med | good | 0.002731 |
| Buying = vhigh and Maint = low and Persons = 4 and Safety = med | acc | 0.002299 |
| Buying = low and Maint = low and Persons = more and Safety = med | good | 0.002408 |
| Safety = high and Persons = more and Buying = med and Maint = low | vgood | 0.002405 |
| Buying = low and Maint = med and Persons = more and Safety = med | good | 0.002191 |
| Buying = low and Maint = low and Persons = more and Safety = high | vgood | 0.002088 |
| Buying = low and Maint = low and Persons = 4 and Safety = high | vgood | 0.002188 |
| Safety = high and Persons = 4 and Buying = med and Maint = med | acc | 0.002486 |
| Safety = high and Persons = 4 and Buying = med and Maint = low | vgood | 0.002188 |
| Buying = med and Maint = med and Persons = more and Safety = med | acc | 0.006667 |
| Safety = high and Persons = more and Buying = low and Maint = med | vgood | 0.001672 |
| Buying = low and Maint = med and Persons = 4 and Safety = high | good | 0.001674 |
| Safety = high and Persons = 4 and Buying = low and Maint = med | vgood | 0.001672 |
| Buying = low and Maint = high and Persons = more and Safety = med | acc | 0.005049 |
| Buying = high and Maint = med and Persons = 4 and Safety = med | acc | 0.002709 |
| Safety = high and Persons = 4 and Buying = low and Maint = high | vgood | 0.001857 |
| Buying = high and Maint = high and Persons = 4 and Safety = med | acc | 0.002299 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Persons = 2 | unacc | 0.530839 |
| Safety = low | unacc | 0.426452 |
| Buying = vhigh and Maint = high | unacc | 0.090196 |
| Maint = vhigh and Buying = high | unacc | 0.081188 |
| Lug_boot = small and Safety = med and Buying = vhigh | unacc | 0.043299 |
| Maint = vhigh and Buying = vhigh | unacc | 0.064516 |
| Safety = med and Lug_boot = small and Buying = high | unacc | 0.041322 |
| Safety = med and Lug_boot = small and Maint != vhigh and Maint != high and Persons != 4 | acc | 0.043841 |
| Safety = med and Lug_boot = small and Maint = vhigh | unacc | 0.029979 |
| Buying = high and Doors != 2 and Doors != 3 | acc | 0.255708 |
| Safety = med and Lug_boot = big and Maint != low and Buying != low | acc | 0.185000 |
| Safety = med and Lug_boot = big and Maint != low and Persons = 4 | acc | 0.031936 |
| Safety = med and Lug_boot = big and Persons != 4 and Buying = low | good | 0.011152 |
| Safety = med and Lug_boot = big and Persons = 4 | good | 0.025052 |
| Lug_boot = big and Safety != med and Maint != vhigh and Buying != low and Buying != med | acc | 0.152047 |
| Lug_boot = big and Safety != med and Maint != vhigh and Maint != high | vgood | 0.092308 |
| Maint = vhigh and Doors != 2 and Safety != med | acc | 0.222973 |
| Buying = vhigh and Safety != med and Persons = 4 | acc | 0.115385 |
| Safety = med and Maint = high and Buying != low | unacc | 0.037531 |
| Buying = high and Doors = 2 | acc | 0.051429 |
| Maint = vhigh and Doors = 2 | acc | 0.062305 |
| Buying = vhigh and Safety = med | acc | 0.115231 |
| Maint = high and Lug_boot = small and Persons != 4 | acc | 0.058231 |
| Maint = high and Buying != low | acc | 0.197936 |
| Lug_boot != big and Safety = med and Lug_boot = small | acc | 0.107880 |
| Maint = high and Lug_boot = med | acc | 0.042424 |
| Maint != high and Buying = vhigh | acc | 0.074074 |
| Maint != high and Maint = vhigh | acc | 0.078241 |
| Buying != high and Maint != high and Doors != 2 and Safety = med and Persons = 4 | acc | 0.022959 |
| Buying != high and Lug_boot = small and Maint != low | acc | 0.038986 |
| Buying != high and Lug_boot != small and Safety = med | good | 0.101250 |
| Buying != high and Lug_boot != small and Doors != 2 and Maint != med | vgood | 0.133796 |
| Buying != high and Maint != low | vgood | 0.046682 |
| Buying != high | good | 0.222997 |
|  | acc | 0.428571 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Safety = high and Buying = low and Lug_boot = big and Persons = 4 | vgood | 0.005371 |
| Safety = high and Persons = more and Buying = low and Lug_boot = big | vgood | 0.005371 |
| Safety = high and Buying = med and Lug_boot = big and Maint = med | vgood | 0.003558 |
| Safety = high and Buying = med and Maint = low and Lug_boot = big | vgood | 0.003558 |
| Safety = high and Lug_boot = med and Buying = low | vgood | 0.001953 |
| Buying = med and Safety = high and Lug_boot = med | vgood | 0.001253 |
| Buying = low and Maint = med and Safety = med and Lug_boot = big | good | 0.003706 |
| Maint = low and Safety = med and Buying = low | good | 0.003153 |
| Maint = low and Buying = med and Safety = med | good | 0.002972 |
| Buying = low and Safety = high | good | 0.001984 |
| Safety = high and Persons = 4 and Maint = med | acc | 0.023936 |
| Safety = med and Lug_boot = big and Persons = 4 and Maint = med | acc | 0.009892 |
| Safety = high and Persons = more and Maint = med | acc | 0.017493 |
| Safety = med and Persons = more and Lug_boot = big and Maint = med | acc | 0.010782 |
| Safety = med and Persons = 4 and Buying = low and Maint = high | acc | 0.009001 |
| Safety = high and Persons = 4 and Maint = low and Buying = vhigh | acc | 0.010782 |
| Safety = med and Persons = more and Lug_boot = big and Maint = low | acc | 0.007214 |
| Safety = med and Persons = more and Lug_boot = med and Doors = 3 | acc | 0.007514 |
| Safety = high and Persons = more and Maint = low and Buying = vhigh | acc | 0.009001 |
| Safety = med and Persons = 4 and Lug_boot = big | acc | 0.012404 |
| Safety = high and Persons = 4 and Buying = med and Maint = vhigh | acc | 0.009001 |
| Persons = more and Safety = high and Buying = med and Lug_boot = big | acc | 0.007214 |
| Safety = med and Persons = more and Buying = low | acc | 0.010434 |
| Safety = high and Buying = high and Maint = high and Persons = 4 | acc | 0.010782 |
| Safety = med and Persons = 4 and Maint = med and Buying = med | acc | 0.007214 |
| Persons = more and Safety = high and Buying = high and Maint = low | acc | 0.009076 |
| Safety = med and Persons = more and Buying = med | acc | 0.010851 |
| Safety = high and Persons = more and Maint = high and Buying = high | acc | 0.008190 |
| Persons = 4 and Safety = med and Lug_boot = med and Doors = 5more | acc | 0.005781 |
| Persons = 4 and Safety = high and Maint = low and Buying = high | acc | 0.008108 |
| Safety = med and Lug_boot = med and Doors = 4 | acc | 0.003996 |
|  | unacc | 0.923664 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

buying|maint|persons|safety|acceptability
---|---|---|---|---
med|low|more|high|vgood
vhigh|low|more|high|acc
high|low|more|high|acc
low|low|more|high|vgood
low|med|more|high|vgood
high|med|more|high|acc
med|med|more|high|vgood
vhigh|med|more|high|acc
low|low|4|high|vgood
med|low|4|high|vgood
high|high|more|high|acc
high|low|4|high|acc
vhigh|low|4|high|acc
med|high|more|high|acc
low|high|more|high|vgood
vhigh|high|more|high|unacc
low|low|more|med|good
med|med|4|high|acc
low|med|4|high|good
med|vhigh|more|high|acc
high|med|4|high|acc
vhigh|med|4|high|acc
med|low|more|med|good
high|low|more|med|acc
vhigh|vhigh|more|high|unacc
vhigh|low|more|med|acc
high|vhigh|more|high|unacc
low|vhigh|more|high|acc
low|med|more|med|good
high|med|more|med|acc
high|high|4|high|acc
low|high|4|high|vgood
med|med|more|med|acc
med|high|4|high|acc
vhigh|med|more|med|acc
med|low|2|high|unacc
high|low|2|high|unacc
low|low|2|high|unacc
vhigh|low|2|high|unacc
vhigh|high|4|high|unacc
vhigh|vhigh|4|high|unacc
low|low|4|med|good
med|vhigh|4|high|acc
med|low|4|med|good
low|vhigh|4|high|acc
low|high|more|med|acc
vhigh|low|4|med|acc
high|low|4|med|unacc
low|med|2|high|unacc
high|high|more|med|acc
med|high|more|med|acc
high|med|2|high|unacc
high|vhigh|4|high|unacc
med|med|2|high|unacc
vhigh|med|2|high|unacc
vhigh|high|more|med|unacc
low|med|4|med|good
med|med|4|med|acc
low|vhigh|more|med|acc
high|high|2|high|unacc
high|low|more|low|unacc
med|low|more|low|unacc
low|high|2|high|unacc
vhigh|low|more|low|unacc
low|low|more|low|unacc
vhigh|med|4|med|acc
vhigh|high|2|high|unacc
high|med|4|med|acc
high|vhigh|more|med|unacc
med|high|2|high|unacc
vhigh|vhigh|more|med|unacc
med|vhigh|more|med|acc
low|high|4|med|acc
high|low|2|med|unacc
high|high|4|med|acc
vhigh|low|2|med|unacc
med|vhigh|2|high|unacc
med|low|2|med|unacc
med|med|more|low|unacc
low|med|more|low|unacc
high|med|more|low|unacc
high|vhigh|2|high|unacc
vhigh|med|more|low|unacc
med|high|4|med|unacc
vhigh|vhigh|2|high|unacc
vhigh|high|4|med|unacc
low|vhigh|2|high|unacc
low|low|2|med|unacc
med|vhigh|4|med|unacc
vhigh|vhigh|4|med|unacc
vhigh|med|2|med|unacc
low|med|2|med|unacc
low|vhigh|4|med|acc
high|med|2|med|unacc
high|low|4|low|unacc
med|med|2|med|unacc
vhigh|low|4|low|unacc
vhigh|high|more|low|unacc
high|vhigh|4|med|unacc
med|low|4|low|unacc
med|high|more|low|unacc
low|low|4|low|unacc
low|high|more|low|unacc
high|high|more|low|unacc
med|med|4|low|unacc
med|high|2|med|unacc
vhigh|med|4|low|unacc
vhigh|high|2|med|unacc
high|vhigh|more|low|unacc
med|vhigh|more|low|unacc
vhigh|vhigh|more|low|unacc
high|med|4|low|unacc
low|high|2|med|unacc
high|high|2|med|unacc
low|med|4|low|unacc
low|vhigh|more|low|unacc
vhigh|high|4|low|unacc
med|vhigh|2|med|unacc
low|vhigh|2|med|unacc
high|vhigh|2|med|unacc
med|low|2|low|unacc
low|low|2|low|unacc
low|high|4|low|unacc
vhigh|vhigh|2|med|unacc
med|high|4|low|unacc
high|low|2|low|unacc
vhigh|low|2|low|unacc
high|high|4|low|unacc
med|med|2|low|unacc
vhigh|med|2|low|unacc
low|vhigh|4|low|unacc
med|vhigh|4|low|unacc
vhigh|vhigh|4|low|unacc
low|med|2|low|unacc
high|med|2|low|unacc
high|vhigh|4|low|unacc
low|high|2|low|unacc
med|high|2|low|unacc
high|high|2|low|unacc
vhigh|high|2|low|unacc
low|vhigh|2|low|unacc
vhigh|vhigh|2|low|unacc
high|vhigh|2|low|unacc
med|vhigh|2|low|unacc

## JRip

Decision list:

rules | predicted class
---|---
(Safety = high) and (Buying = low) and (Lug_boot = big) and (Persons = 4)|vgood (15.0/4.0)
(Safety = high) and (Persons = more) and (Buying = low) and (Lug_boot = big)|vgood (15.0/4.0)
(Safety = high) and (Buying = med) and (Lug_boot = big) and (Maint = med)|vgood (12.0/4.0)
(Safety = high) and (Buying = med) and (Maint = low) and (Lug_boot = big)|vgood (12.0/4.0)
(Safety = high) and (Lug_boot = med) and (Buying = low)|vgood (42.0/31.0)
(Buying = med) and (Safety = high) and (Lug_boot = med)|vgood (44.0/35.0)
(Buying = low) and (Maint = med) and (Safety = med) and (Lug_boot = big)|good (12.0/4.0)
(Maint = low) and (Safety = med) and (Buying = low)|good (32.0/20.0)
(Maint = low) and (Buying = med) and (Safety = med)|good (34.0/22.0)
(Buying = low) and (Safety = high)|good (55.0/44.0)
(Safety = high) and (Persons = 4) and (Maint = med)|acc (25.0/0.0)
(Safety = med) and (Lug_boot = big) and (Persons = 4) and (Maint = med)|acc (11.0/0.0)
(Safety = high) and (Persons = more) and (Maint = med)|acc (25.0/3.0)
(Safety = med) and (Persons = more) and (Lug_boot = big) and (Maint = med)|acc (12.0/0.0)
(Safety = med) and (Persons = 4) and (Buying = low) and (Maint = high)|acc (10.0/0.0)
(Safety = high) and (Persons = 4) and (Maint = low) and (Buying = vhigh)|acc (12.0/0.0)
(Safety = med) and (Persons = more) and (Lug_boot = big) and (Maint = low)|acc (8.0/0.0)
(Safety = med) and (Persons = more) and (Lug_boot = med) and (Doors = 3)|acc (12.0/2.0)
(Safety = high) and (Persons = more) and (Maint = low) and (Buying = vhigh)|acc (10.0/0.0)
(Safety = med) and (Persons = 4) and (Lug_boot = big)|acc (29.0/9.0)
(Safety = high) and (Persons = 4) and (Buying = med) and (Maint = vhigh)|acc (8.0/0.0)
(Persons = more) and (Safety = high) and (Buying = med) and (Lug_boot = big)|acc (8.0/0.0)
(Safety = med) and (Persons = more) and (Buying = low)|acc (24.0/9.0)
(Safety = high) and (Buying = high) and (Maint = high) and (Persons = 4)|acc (12.0/0.0)
(Safety = med) and (Persons = 4) and (Maint = med) and (Buying = med)|acc (8.0/0.0)
(Persons = more) and (Safety = high) and (Buying = high) and (Maint = low)|acc (12.0/1.0)
(Safety = med) and (Persons = more) and (Buying = med)|acc (25.0/10.0)
(Safety = high) and (Persons = more) and (Maint = high) and (Buying = high)|acc (11.0/1.0)
(Persons = 4) and (Safety = med) and (Lug_boot = med) and (Doors = 5more)|acc (10.0/2.0)
(Persons = 4) and (Safety = high) and (Maint = low) and (Buying = high)|acc (9.0/0.0)
(Safety = med) and (Lug_boot = med) and (Doors = 4)|acc (30.0/18.0)
|unacc (969.0/32.0)


## PART

Decision list:

rules | predicted class
---|---
Persons = 2|unacc (525.0)
Safety = low|unacc (345.0)
Buying = vhigh AND Maint = high|unacc (46.0)
Maint = vhigh AND Buying = high|unacc (41.0)
Lug_boot = small AND Safety = med AND Buying = vhigh|unacc (21.0)
Maint = vhigh AND Buying = vhigh|unacc (32.0)
Safety = med AND Lug_boot = small AND Buying = high|unacc (20.0)
Safety = med AND Lug_boot = small AND Maint != vhigh AND Maint != high AND Persons != 4|acc (15.0/4.0)
Safety = med AND Lug_boot = small AND Maint = vhigh|unacc (14.0)
Buying = high AND Doors != 2 AND Doors != 3|acc (56.0)
Safety = med AND Lug_boot = big AND Maint != low AND Buying != low|acc (37.0)
Safety = med AND Lug_boot = big AND Maint != low AND Persons = 4|acc (12.0/4.0)
Safety = med AND Lug_boot = big AND Persons != 4 AND Buying = low|good (13.0/6.0)
Safety = med AND Lug_boot = big AND Persons = 4|good (10.0/3.0)
Lug_boot = big AND Safety != med AND Maint != vhigh AND Buying != low AND Buying != med|acc (26.0)
Lug_boot = big AND Safety != med AND Maint != vhigh AND Maint != high|vgood (30.0)
Maint = vhigh AND Doors != 2 AND Safety != med|acc (33.0)
Buying = vhigh AND Safety != med AND Persons = 4|acc (15.0)
Safety = med AND Maint = high AND Buying != low|unacc (19.0/6.0)
Buying = high AND Doors = 2|acc (15.0/6.0)
Maint = vhigh AND Doors = 2|acc (15.0/5.0)
Buying = vhigh AND Safety = med|acc (19.0/5.0)
Maint = high AND Lug_boot = small AND Persons != 4|acc (12.0/3.0)
Maint = high AND Buying != low|acc (21.0)
Lug_boot != big AND Safety = med AND Lug_boot = small|acc (16.0)
Maint = high AND Lug_boot = med|acc (11.0/4.0)
Maint != high AND Buying = vhigh|acc (13.0/1.0)
Maint != high AND Maint = vhigh|acc (12.0/2.0)
Buying != high AND Maint != high AND Doors != 2 AND Safety = med AND Persons = 4|acc (12.0/6.0)
Buying != high AND Lug_boot = small AND Maint != low|acc (19.0/9.0)
Buying != high AND Lug_boot != small AND Safety = med|good (21.0/9.0)
Buying != high AND Lug_boot != small AND Doors != 2 AND Maint != med|vgood (15.0/2.0)
Buying != high AND Maint != low|vgood (16.0/5.0)
Buying != high|good (15.0/2.0)
|acc (11.0/2.0)


## J48 Decision Tree

* Safety = low: unacc (520.0)
* Safety = med
	* Persons = 2: unacc (173.0)
	* Persons = 4
		* Buying = vhigh: unacc (38.0/11.0)
		* Buying = high
			* Lug_boot = small: unacc (12.0)
			* Lug_boot = med: unacc (13.0/5.0)
			* Lug_boot = big: acc (12.0/2.0)
		* Buying = med: acc (43.0/16.0)
		* Buying = low: acc (43.0/17.0)
	* Persons = more
		* Lug_boot = small: unacc (60.0/13.0)
		* Lug_boot = med: acc (55.0/24.0)
		* Lug_boot = big: acc (60.0/23.0)
* Safety = high
	* Persons = 2: unacc (177.0)
	* Persons = 4
		* Buying = vhigh
			* Maint = vhigh: unacc (12.0)
			* Maint = high: unacc (11.0)
			* Maint = med: acc (11.0)
			* Maint = low: acc (12.0)
		* Buying = high
			* Maint = vhigh: unacc (12.0)
			* Maint = high: acc (12.0)
			* Maint = med: acc (10.0)
			* Maint = low: acc (9.0)
		* Buying = med
			* Maint = vhigh: acc (10.0)
			* Maint = high: acc (10.0)
			* Maint = med: acc (12.0/6.0)
			* Maint = low: vgood (11.0/5.0)
		* Buying = low
			* Maint = vhigh: acc (12.0)
			* Maint = high: vgood (9.0/4.0)
			* Maint = med: vgood (10.0/5.0)
			* Maint = low: vgood (11.0/5.0)
	* Persons = more
		* Buying = vhigh
			* Maint = vhigh: unacc (9.0)
			* Maint = high: unacc (12.0)
			* Maint = med: acc (10.0/1.0)
			* Maint = low: acc (10.0)
		* Buying = high
			* Maint = vhigh: unacc (11.0)
			* Maint = high: acc (11.0/1.0)
			* Maint = med: acc (11.0/1.0)
			* Maint = low: acc (12.0/1.0)
		* Buying = med
			* Maint = vhigh: acc (12.0/1.0)
			* Maint = high: acc (12.0/1.0)
			* Maint = med: vgood (12.0/5.0)
			* Maint = low: vgood (10.0/4.0)
		* Buying = low
			* Maint = vhigh: acc (11.0/1.0)
			* Maint = high: vgood (12.0/5.0)
			* Maint = med: vgood (10.0/5.0)
			* Maint = low: vgood (8.0/3.0)


## SimpleCart Decision Tree

	* Persons=(more)|(4)
		* Safety=(high)|(med)
			* Buying=(low)|(med)
				* Maint=(low)|(med)
				* Safety=(high)
						* Lug_boot=(big)|(med)
								* Doors=(5more)|(4)|(3): vgood(39.0/3.0)
								* Doors!=(5more)|(4)|(3)
							* Lug_boot=(big): vgood(7.0/0.0)
							* Lug_boot!=(big): good(6.0/2.0)
						* Lug_boot!=(big)|(med)
						* Buying=(low): good(11.0/2.0)
						* Buying!=(low)
							* Maint=(low): good(5.0/1.0)
							* Maint!=(low): acc(7.0/1.0)
				* Safety!=(high)
						* Lug_boot=(big)|(med)
								* Buying=(low)|(vhigh)|(high)
								* Doors=(5more)|(4): good(15.0/0.0)
								* Doors!=(5more)|(4)
									* Lug_boot=(big)|(small): good(8.0/0.0)
									* Lug_boot!=(big)|(small): acc(6.0/1.0)
								* Buying!=(low)|(vhigh)|(high)
									* Maint=(low)|(vhigh)|(high): good(12.0/3.0)
									* Maint!=(low)|(vhigh)|(high): acc(13.0/0.0)
						* Lug_boot!=(big)|(med)
								* Doors=(5more)|(4)|(3): acc(22.0/0.0)
								* Doors!=(5more)|(4)|(3): unacc(4.0/2.0)
				* Maint!=(low)|(med)
					* Lug_boot=(big)|(med)
					* Maint=(high)
						* Buying=(low)
								* Safety=(high)|(low): vgood(12.0/2.0)
								* Safety!=(high)|(low): acc(12.0/0.0)
						* Buying!=(low): acc(26.0/3.0)
					* Maint!=(high): acc(55.0/5.0)
					* Lug_boot!=(big)|(med)
						* Safety=(high)|(low): acc(25.0/4.0)
						* Safety!=(high)|(low)
						* Buying=(low)
							* Maint=(high): acc(5.0/1.0)
							* Maint!=(high): unacc(7.0/0.0)
						* Buying!=(low): unacc(15.0/0.0)
			* Buying!=(low)|(med)
				* Maint=(low)|(med)
					* Lug_boot=(big)|(med)
						* Doors=(5more)|(4): acc(63.0/0.0)
						* Doors!=(5more)|(4)
							* Safety=(high)|(low): acc(28.0/0.0)
							* Safety!=(high)|(low)
							* Lug_boot=(big): acc(13.0/0.0)
							* Lug_boot!=(big): unacc(10.0/4.0)
					* Lug_boot!=(big)|(med)
					* Safety=(high): acc(23.0/3.0)
					* Safety!=(high): unacc(27.0/0.0)
				* Maint!=(low)|(med)
						* Buying=(high)|(med)|(low)
							* Maint=(high)|(med)|(low)
							* Lug_boot=(big)|(med): acc(28.0/2.0)
							* Lug_boot!=(big)|(med)
								* Safety=(high)|(low): acc(6.0/1.0)
								* Safety!=(high)|(low): unacc(7.0/0.0)
							* Maint!=(high)|(med)|(low): unacc(41.0/0.0)
						* Buying!=(high)|(med)|(low): unacc(85.0/0.0)
		* Safety!=(high)|(med): unacc(345.0/0.0)
	* Persons!=(more)|(4): unacc(525.0/0.0)


