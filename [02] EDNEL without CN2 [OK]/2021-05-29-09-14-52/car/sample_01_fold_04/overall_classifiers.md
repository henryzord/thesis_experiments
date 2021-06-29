# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Persons != 4 | unacc | 0.604302 |
| Persons != more | unacc | 0.600277 |
| Safety = med and Persons = more and Lug_boot = big | acc | 0.018868 |
| Safety = med and Persons = more and Lug_boot = med | acc | 0.015597 |
| Safety = med and Persons = 4 and Buying = med | acc | 0.014227 |
| Safety = med and Persons = 4 and Buying = low | acc | 0.013603 |
| Buying = high and Maint = med and Persons = 4 and Safety = high | acc | 0.009836 |
| Safety = high and Persons = 4 and Buying = vhigh and Maint = med | acc | 0.009836 |
| Safety = high and Persons = 4 and Buying = high and Maint = low | acc | 0.009836 |
| Safety = med and Persons = 4 and Buying = high and Lug_boot = big | acc | 0.007401 |
| Safety = high and Persons = 4 and Buying = med and Maint = vhigh | acc | 0.009024 |
| Buying = high and Maint = high and Persons = more and Safety = high | acc | 0.008279 |
| Buying = vhigh and Maint = med and Persons = more and Safety = high | acc | 0.008279 |
| Safety = high and Persons = 4 and Buying = low and Maint = vhigh | acc | 0.008210 |
| Buying = med and Maint = high and Persons = 4 and Safety = high | acc | 0.008210 |
| Safety = high and Persons = 4 and Buying = vhigh and Maint = low | acc | 0.008210 |
| Buying = low and Maint = vhigh and Persons = more and Safety = high | acc | 0.007470 |
| Safety = high and Persons = more and Buying = med and Maint = vhigh | acc | 0.007470 |
| Safety = high and Persons = more and Buying = high and Maint = med | acc | 0.006661 |
| Buying = vhigh and Maint = low and Persons = more and Safety = high | acc | 0.006661 |
| Buying = high and Maint = high and Persons = 4 and Safety = high | acc | 0.007395 |
| Safety = med and Persons = more and Lug_boot = small and Buying = low | acc | 0.005137 |
| Buying = med and Maint = high and Persons = more and Safety = high | acc | 0.006661 |
| Safety = high and Persons = more and Buying = high and Maint = low | acc | 0.005853 |
| Buying = low and Maint = med and Persons = 4 and Safety = med | good | 0.002009 |
| Safety = high and Persons = more and Buying = low and Maint = low | vgood | 0.002976 |
| Buying = med and Maint = low and Persons = 4 and Safety = med | good | 0.001859 |
| Buying = low and Maint = low and Persons = more and Safety = med | good | 0.001859 |
| Buying = med and Maint = low and Persons = more and Safety = high | vgood | 0.002730 |
| Buying = med and Maint = low and Persons = more and Safety = med | good | 0.002978 |
| Buying = low and Maint = med and Persons = more and Safety = high | vgood | 0.002406 |
| Buying = low and Maint = med and Persons = more and Safety = med | good | 0.001340 |
| Safety = high and Persons = more and Buying = low and Maint = high | vgood | 0.002189 |
| Safety = high and Persons = 4 and Buying = low and Maint = high | acc | 0.002483 |
| Buying = low and Maint = high and Persons = 4 and Safety = high | vgood | 0.002008 |
| Buying = med and Maint = low and Persons = 4 and Safety = high | good | 0.002191 |
| Buying = med and Maint = med and Persons = 4 and Safety = high | vgood | 0.002189 |
| Buying = low and Maint = low and Persons = 4 and Safety = high | good | 0.002191 |
| Safety = high and Persons = 4 and Buying = low and Maint = med | vgood | 0.002008 |
| Buying = low and Maint = med and Persons = 4 and Safety = high | good | 0.002009 |
| Persons = 4 and Safety = med and Buying != med and Maint = med and Lug_boot = med and Doors = 4 | acc | 0.001103 |
| Buying = med and Maint = med and Persons = more and Safety = med | acc | 0.006579 |
| Safety = high and Persons = more and Buying = med and Maint = med | vgood | 0.001673 |
| Buying = high and Maint = high and Persons = 4 and Safety = med | acc | 0.002483 |
| Persons = 4 and Safety = med and Buying != med and Maint = med and Lug_boot = med and Doors = 5more | acc | 0.001103 |
| Buying = high and Maint = low and Persons = 4 and Safety = med | acc | 0.002707 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Safety = low | unacc | 0.527495 |
| Persons = 2 | unacc | 0.426452 |
| Buying = vhigh and Maint = high | unacc | 0.086614 |
| Buying = high and Maint = vhigh | unacc | 0.086614 |
| Safety = med and Lug_boot = small and Buying = vhigh | unacc | 0.047228 |
| Safety = med and Lug_boot = small and Buying = high | unacc | 0.045267 |
| Maint = high and Safety = med and Lug_boot = big | acc | 0.094017 |
| Maint = vhigh and Buying = vhigh | unacc | 0.075314 |
| Safety = med and Lug_boot = big and Buying = high | acc | 0.078534 |
| Safety = med and Lug_boot = big and Maint = vhigh | acc | 0.078534 |
| Safety = med and Lug_boot = small and Maint = vhigh | unacc | 0.035129 |
| Safety = med and Lug_boot = small and Maint = low | acc | 0.069777 |
| Safety = med and Lug_boot = small and Buying = low | acc | 0.075096 |
| Safety = med and Lug_boot = small and Maint = high | unacc | 0.017857 |
| Buying = vhigh | acc | 0.273413 |
| Buying = high and Safety = high | acc | 0.274248 |
| Maint = vhigh and Safety = high | acc | 0.202555 |
| Safety = med and Lug_boot = big and Maint = low | good | 0.058252 |
| Safety = med and Buying = high and Doors = 2 | unacc | 0.028169 |
| Safety = med and Maint = high | acc | 0.100732 |
| Safety = med and Maint = vhigh and Persons = more | acc | 0.032143 |
| Safety = med and Buying = med and Maint = med | acc | 0.122581 |
| Safety = med and Buying = low and Maint = med | good | 0.050277 |
| Lug_boot = big and Maint = med | vgood | 0.107143 |
| Lug_boot = big and Buying = low | vgood | 0.107143 |
| Maint = high and Buying = med | acc | 0.152128 |
| Lug_boot = small and Maint = low | good | 0.089418 |
| Safety = med and Maint = vhigh | unacc | 0.041667 |
| Lug_boot = small | acc | 0.081193 |
| Safety = high and Doors = 5more | vgood | 0.121486 |
| Safety = med and Buying = high | acc | 0.105374 |
| Lug_boot = med and Safety = med | good | 0.073368 |
| Doors = 4 | vgood | 0.121065 |
| Maint = low and Doors = 2 | good | 0.028571 |
| Doors = 2 | acc | 0.076190 |
| Persons = 4 | good | 0.088889 |
|  | vgood | 0.195122 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Safety = high and Buying = low and Lug_boot = big and Persons = 4 | vgood | 0.006387 |
| Safety = high and Persons = more and Buying = low and Lug_boot = big | vgood | 0.005374 |
| Safety = high and Buying = med and Lug_boot = big and Maint = low | vgood | 0.003271 |
| Safety = high and Lug_boot = med and Buying = low and Persons = more | vgood | 0.002854 |
| Safety = high and Buying = med and Maint = med and Persons = 4 and Lug_boot = big | vgood | 0.002670 |
| Safety = high and Buying = med and Persons = more and Maint = med | vgood | 0.001673 |
| Safety = high and Lug_boot = med and Buying = med and Maint = low and Persons = more | vgood | 0.001504 |
| Safety = high and Lug_boot = med and Persons = 4 and Buying = low and Doors = 4 | vgood | 0.001504 |
| Maint = low and Buying = low and Persons = 4 and Safety = high | good | 0.004149 |
| Maint = low and Buying = med and Safety = med and Persons = more | good | 0.003087 |
| Buying = low and Maint = med and Persons = 4 and Safety = high | good | 0.003559 |
| Maint = low and Buying = med and Persons = 4 and Safety = high | good | 0.003116 |
| Maint = low and Safety = med and Buying = low and Lug_boot = big | good | 0.002167 |
| Buying = low and Safety = med and Maint = med and Lug_boot = big and Persons = 4 | good | 0.002770 |
| Buying = low and Persons = more and Safety = med and Maint = med | good | 0.001389 |
| Maint = low and Safety = med and Buying = low and Lug_boot = med and Persons = more | good | 0.002079 |
| Maint = low and Buying = med and Safety = med and Persons = 4 | good | 0.001928 |
| Buying = low and Maint = med and Safety = high and Persons = more | good | 0.001560 |
| Maint = low and Buying = low and Persons = more and Safety = high | good | 0.001560 |
| Maint = low and Buying = med and Safety = high and Persons = more | good | 0.002218 |
| Safety = high and Persons = 4 | acc | 0.060584 |
| Persons = more and Safety = high and Maint = med | acc | 0.018384 |
| Safety = med and Persons = more and Lug_boot = big | acc | 0.024219 |
| Safety = med and Persons = 4 and Lug_boot = big | acc | 0.023230 |
| Persons = more and Safety = high and Maint = low | acc | 0.012376 |
| Persons = more and Safety = high and Buying = med | acc | 0.014089 |
| Safety = med and Lug_boot = med and Persons = more | acc | 0.019579 |
| Safety = med and Persons = 4 and Buying = low | acc | 0.012023 |
| Safety = med and Persons = 4 and Lug_boot = med and Doors = 5more | acc | 0.004467 |
| Persons = more and Safety = high and Maint = high and Buying = high | acc | 0.009092 |
| Safety = med and Persons = 4 and Buying = med and Maint = med | acc | 0.005430 |
| Safety = med and Doors = 4 and Persons = 4 and Lug_boot = med | acc | 0.003709 |
| Persons = more and Buying = low and Safety = med | acc | 0.005245 |
| Persons = more and Safety = high and Buying = low | acc | 0.009819 |
|  | unacc | 0.982852 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

buying|maint|persons|safety|acceptability
---|---|---|---|---
med|low|more|high|vgood
vhigh|low|more|high|acc
low|low|more|high|vgood
high|low|more|high|acc
low|med|more|high|vgood
high|med|more|high|acc
vhigh|med|more|high|acc
med|med|more|high|vgood
low|low|4|high|good
med|low|4|high|good
low|high|more|high|vgood
high|high|more|high|acc
vhigh|low|4|high|acc
high|low|4|high|acc
med|high|more|high|acc
vhigh|high|more|high|unacc
low|med|4|high|good
med|med|4|high|vgood
low|low|more|med|good
high|med|4|high|acc
med|vhigh|more|high|acc
med|low|more|med|good
vhigh|med|4|high|acc
low|vhigh|more|high|acc
high|vhigh|more|high|unacc
high|low|more|med|acc
vhigh|vhigh|more|high|unacc
vhigh|low|more|med|acc
med|med|more|med|acc
low|high|4|high|vgood
med|high|4|high|acc
low|med|more|med|good
high|high|4|high|acc
low|low|2|high|unacc
high|low|2|high|unacc
vhigh|med|more|med|acc
vhigh|low|2|high|unacc
high|med|more|med|acc
vhigh|high|4|high|unacc
med|low|2|high|unacc
med|low|4|med|good
low|high|more|med|acc
low|low|4|med|acc
low|vhigh|4|high|acc
med|vhigh|4|high|acc
med|high|more|med|acc
vhigh|low|4|med|unacc
low|med|2|high|unacc
high|high|more|med|acc
high|low|4|med|acc
vhigh|med|2|high|unacc
vhigh|vhigh|4|high|unacc
high|vhigh|4|high|unacc
vhigh|high|more|med|unacc
high|med|2|high|unacc
med|med|2|high|unacc
low|med|4|med|good
med|med|4|med|acc
vhigh|med|4|med|unacc
med|high|2|high|unacc
high|med|4|med|acc
med|low|more|low|unacc
high|low|more|low|unacc
vhigh|low|more|low|unacc
low|vhigh|more|med|acc
high|vhigh|more|med|unacc
med|vhigh|more|med|acc
vhigh|vhigh|more|med|unacc
vhigh|high|2|high|unacc
low|low|more|low|unacc
high|high|2|high|unacc
low|high|2|high|unacc
low|high|4|med|acc
low|med|more|low|unacc
high|high|4|med|acc
med|high|4|med|acc
vhigh|vhigh|2|high|unacc
high|vhigh|2|high|unacc
high|low|2|med|unacc
vhigh|high|4|med|unacc
high|med|more|low|unacc
vhigh|med|more|low|unacc
vhigh|low|2|med|unacc
low|vhigh|2|high|unacc
med|vhigh|2|high|unacc
low|low|2|med|unacc
med|low|2|med|unacc
med|med|more|low|unacc
med|vhigh|4|med|acc
low|vhigh|4|med|unacc
high|vhigh|4|med|unacc
low|low|4|low|unacc
vhigh|med|2|med|unacc
low|med|2|med|unacc
med|med|2|med|unacc
vhigh|low|4|low|unacc
med|high|more|low|unacc
low|high|more|low|unacc
high|low|4|low|unacc
high|high|more|low|unacc
med|low|4|low|unacc
vhigh|vhigh|4|med|unacc
high|med|2|med|unacc
vhigh|high|more|low|unacc
med|high|2|med|unacc
low|vhigh|more|low|unacc
vhigh|vhigh|more|low|unacc
low|high|2|med|unacc
high|high|2|med|unacc
vhigh|med|4|low|unacc
med|vhigh|more|low|unacc
high|med|4|low|unacc
low|med|4|low|unacc
med|med|4|low|unacc
vhigh|high|2|med|unacc
high|vhigh|more|low|unacc
low|vhigh|2|med|unacc
vhigh|vhigh|2|med|unacc
vhigh|low|2|low|unacc
high|low|2|low|unacc
med|vhigh|2|med|unacc
med|low|2|low|unacc
vhigh|high|4|low|unacc
low|low|2|low|unacc
high|vhigh|2|med|unacc
high|high|4|low|unacc
low|high|4|low|unacc
med|high|4|low|unacc
med|vhigh|4|low|unacc
high|med|2|low|unacc
low|med|2|low|unacc
vhigh|vhigh|4|low|unacc
high|vhigh|4|low|unacc
vhigh|med|2|low|unacc
med|med|2|low|unacc
low|vhigh|4|low|unacc
low|high|2|low|unacc
med|high|2|low|unacc
vhigh|high|2|low|unacc
high|high|2|low|unacc
low|vhigh|2|low|unacc
high|vhigh|2|low|unacc
med|vhigh|2|low|unacc
vhigh|vhigh|2|low|unacc

## JRip

Decision list:

rules | predicted class
---|---
(Safety = high) and (Buying = low) and (Lug_boot = big) and (Persons = 4)|vgood (15.0/3.0)
(Safety = high) and (Persons = more) and (Buying = low) and (Lug_boot = big)|vgood (15.0/4.0)
(Safety = high) and (Buying = med) and (Lug_boot = big) and (Maint = low)|vgood (10.0/3.0)
(Safety = high) and (Lug_boot = med) and (Buying = low) and (Persons = more)|vgood (15.0/7.0)
(Safety = high) and (Buying = med) and (Maint = med) and (Persons = 4) and (Lug_boot = big)|vgood (4.0/0.0)
(Safety = high) and (Buying = med) and (Persons = more) and (Maint = med)|vgood (10.0/5.0)
(Safety = high) and (Lug_boot = med) and (Buying = med) and (Maint = low) and (Persons = more)|vgood (4.0/1.0)
(Safety = high) and (Lug_boot = med) and (Persons = 4) and (Buying = low) and (Doors = 4)|vgood (4.0/1.0)
(Maint = low) and (Buying = low) and (Persons = 4) and (Safety = high)|good (6.0/0.0)
(Maint = low) and (Buying = med) and (Safety = med) and (Persons = more)|good (11.0/4.0)
(Buying = low) and (Maint = med) and (Persons = 4) and (Safety = high)|good (7.0/1.0)
(Maint = low) and (Buying = med) and (Persons = 4) and (Safety = high)|good (8.0/2.0)
(Maint = low) and (Safety = med) and (Buying = low) and (Lug_boot = big)|good (8.0/3.0)
(Buying = low) and (Safety = med) and (Maint = med) and (Lug_boot = big) and (Persons = 4)|good (4.0/0.0)
(Buying = low) and (Persons = more) and (Safety = med) and (Maint = med)|good (8.0/4.0)
(Maint = low) and (Safety = med) and (Buying = low) and (Lug_boot = med) and (Persons = more)|good (3.0/0.0)
(Maint = low) and (Buying = med) and (Safety = med) and (Persons = 4)|good (9.0/4.0)
(Buying = low) and (Maint = med) and (Safety = high) and (Persons = more)|good (3.0/1.0)
(Maint = low) and (Buying = low) and (Persons = more) and (Safety = high)|good (3.0/1.0)
(Maint = low) and (Buying = med) and (Safety = high) and (Persons = more)|good (4.0/1.0)
(Safety = high) and (Persons = 4)|acc (127.0/34.0)
(Persons = more) and (Safety = high) and (Maint = med)|acc (22.0/2.0)
(Safety = med) and (Persons = more) and (Lug_boot = big)|acc (45.0/10.0)
(Safety = med) and (Persons = 4) and (Lug_boot = big)|acc (47.0/12.0)
(Persons = more) and (Safety = high) and (Maint = low)|acc (19.0/2.0)
(Persons = more) and (Safety = high) and (Buying = med)|acc (21.0/2.0)
(Safety = med) and (Lug_boot = med) and (Persons = more)|acc (51.0/19.0)
(Safety = med) and (Persons = 4) and (Buying = low)|acc (30.0/10.0)
(Safety = med) and (Persons = 4) and (Lug_boot = med) and (Doors = 5more)|acc (11.0/3.0)
(Persons = more) and (Safety = high) and (Maint = high) and (Buying = high)|acc (12.0/1.0)
(Safety = med) and (Persons = 4) and (Buying = med) and (Maint = med)|acc (6.0/0.0)
(Safety = med) and (Doors = 4) and (Persons = 4) and (Lug_boot = med)|acc (10.0/3.0)
(Persons = more) and (Buying = low) and (Safety = med)|acc (10.0/4.0)
(Persons = more) and (Safety = high) and (Buying = low)|acc (7.0/2.0)
|unacc (984.0/2.0)


## PART

Decision list:

rules | predicted class
---|---
Safety = low|unacc (518.0)
Persons = 2|unacc (345.0)
Buying = vhigh AND Maint = high|unacc (44.0)
Buying = high AND Maint = vhigh|unacc (44.0)
Safety = med AND Lug_boot = small AND Buying = vhigh|unacc (23.0)
Safety = med AND Lug_boot = small AND Buying = high|unacc (22.0)
Maint = high AND Safety = med AND Lug_boot = big|acc (22.0)
Maint = vhigh AND Buying = vhigh|unacc (36.0)
Safety = med AND Lug_boot = big AND Buying = high|acc (15.0)
Safety = med AND Lug_boot = big AND Maint = vhigh|acc (15.0)
Safety = med AND Lug_boot = small AND Maint = vhigh|unacc (15.0)
Safety = med AND Lug_boot = small AND Maint = low|acc (14.0/1.0)
Safety = med AND Lug_boot = small AND Buying = low|acc (14.0)
Safety = med AND Lug_boot = small AND Maint = high|unacc (7.0)
Buying = vhigh|acc (71.0/7.0)
Buying = high AND Safety = high|acc (64.0/3.0)
Maint = vhigh AND Safety = high|acc (43.0/2.0)
Safety = med AND Lug_boot = big AND Maint = low|good (12.0)
Safety = med AND Buying = high AND Doors = 2|unacc (6.0)
Safety = med AND Maint = high|acc (19.0/2.0)
Safety = med AND Maint = vhigh AND Persons = more|acc (8.0/2.0)
Safety = med AND Buying = med AND Maint = med|acc (19.0)
Safety = med AND Buying = low AND Maint = med|good (13.0/3.0)
Lug_boot = big AND Maint = med|vgood (15.0)
Lug_boot = big AND Buying = low|vgood (15.0)
Maint = high AND Buying = med|acc (20.0/1.0)
Lug_boot = small AND Maint = low|good (15.0/2.0)
Safety = med AND Maint = vhigh|unacc (7.0/3.0)
Lug_boot = small|acc (23.0/9.0)
Safety = high AND Doors = 5more|vgood (11.0)
Safety = med AND Buying = high|acc (12.0/2.0)
Lug_boot = med AND Safety = med|good (14.0/4.0)
Doors = 4|vgood (10.0)
Maint = low AND Doors = 2|good (6.0/2.0)
Doors = 2|acc (6.0/2.0)
Persons = 4|good (5.0/2.0)
|vgood (5.0)


## J48 Decision Tree

* Safety = low: unacc (518.0)
* Safety = med
	* Persons = 2: unacc (176.0)
	* Persons = 4
		* Buying = vhigh: unacc (42.0/8.0)
		* Buying = high
			* Lug_boot = small: unacc (14.0)
			* Lug_boot = med: unacc (16.0/6.0)
			* Lug_boot = big: acc (16.0/4.0)
		* Buying = med: acc (42.0/15.0)
		* Buying = low: acc (44.0/17.0)
	* Persons = more
		* Lug_boot = small
			* Buying = vhigh: unacc (16.0)
			* Buying = high: unacc (15.0)
			* Buying = med: unacc (13.0/5.0)
			* Buying = low: acc (13.0/4.0)
		* Lug_boot = med: acc (61.0/27.0)
		* Lug_boot = big: acc (53.0/18.0)
* Safety = high
	* Persons = 2: unacc (169.0)
	* Persons = 4
		* Buying = vhigh
			* Maint = vhigh: unacc (10.0)
			* Maint = high: unacc (11.0)
			* Maint = med: acc (12.0)
			* Maint = low: acc (10.0)
		* Buying = high
			* Maint = vhigh: unacc (10.0)
			* Maint = high: acc (9.0)
			* Maint = med: acc (12.0)
			* Maint = low: acc (12.0)
		* Buying = med
			* Maint = vhigh: acc (11.0)
			* Maint = high: acc (10.0)
			* Maint = med: vgood (11.0/5.0)
			* Maint = low: good (11.0/5.0)
		* Buying = low
			* Maint = vhigh: acc (10.0)
			* Maint = high: acc (12.0/6.0)
			* Maint = med: vgood (12.0/6.0)
			* Maint = low: good (11.0/5.0)
	* Persons = more
		* Buying = vhigh
			* Maint = vhigh: unacc (11.0)
			* Maint = high: unacc (10.0)
			* Maint = med: acc (12.0/1.0)
			* Maint = low: acc (10.0/1.0)
		* Buying = high
			* Maint = vhigh: unacc (11.0)
			* Maint = high: acc (12.0/1.0)
			* Maint = med: acc (10.0/1.0)
			* Maint = low: acc (9.0/1.0)
		* Buying = med
			* Maint = vhigh: acc (11.0/1.0)
			* Maint = high: acc (10.0/1.0)
			* Maint = med: vgood (10.0/5.0)
			* Maint = low: vgood (12.0/5.0)
		* Buying = low
			* Maint = vhigh: acc (11.0/1.0)
			* Maint = high: vgood (11.0/5.0)
			* Maint = med: vgood (10.0/4.0)
			* Maint = low: vgood (11.0/4.0)


## SimpleCart Decision Tree

	* Persons=(more)|(4)
		* Safety=(high)|(med)
			* Buying=(low)|(med)
				* Maint=(low)|(med)
					* Safety=(high)|(low)
						* Lug_boot=(big)|(med)
							* Lug_boot=(big)|(small): vgood(30.0/0.0)
							* Lug_boot!=(big)|(small)
								* Doors=(5more)|(4): vgood(14.0/0.0)
								* Doors!=(5more)|(4): good(9.0/5.0)
						* Lug_boot!=(big)|(med): good(19.0/11.0)
					* Safety!=(high)|(low)
						* Lug_boot=(big)|(med)
						* Maint=(low): good(22.0/4.0)
						* Maint!=(low)
							* Buying=(low): good(10.0/3.0)
							* Buying!=(low): acc(14.0/0.0)
						* Lug_boot!=(big)|(med): acc(25.0/1.0)
				* Maint!=(low)|(med)
					* Lug_boot=(big)|(med)
							* Buying=(low)|(vhigh)|(high)
							* Safety=(high)|(low)
									* Maint=(high)|(med)|(low): vgood(12.0/3.0)
									* Maint!=(high)|(med)|(low): acc(14.0/0.0)
							* Safety!=(high)|(low): acc(26.0/3.0)
							* Buying!=(low)|(vhigh)|(high): acc(51.0/4.0)
					* Lug_boot!=(big)|(med)
						* Safety=(high)|(low): acc(26.0/4.0)
						* Safety!=(high)|(low): unacc(22.0/7.0)
			* Buying!=(low)|(med)
				* Maint=(low)|(med)
					* Lug_boot=(big)|(med)
						* Doors=(5more)|(4): acc(58.0/0.0)
						* Doors!=(5more)|(4)
							* Safety=(high)|(low): acc(28.0/0.0)
							* Safety!=(high)|(low)
							* Lug_boot=(big): acc(13.0/0.0)
							* Lug_boot!=(big): unacc(11.0/4.0)
					* Lug_boot!=(big)|(med)
						* Safety=(high)|(low): acc(27.0/4.0)
						* Safety!=(high)|(low): unacc(31.0/0.0)
				* Maint!=(low)|(med)
						* Buying=(high)|(med)|(low)
							* Maint=(high)|(med)|(low): acc(33.0/11.0)
							* Maint!=(high)|(med)|(low): unacc(44.0/0.0)
						* Buying!=(high)|(med)|(low): unacc(87.0/0.0)
		* Safety!=(high)|(med): unacc(344.0/0.0)
	* Persons!=(more)|(4): unacc(519.0/0.0)


