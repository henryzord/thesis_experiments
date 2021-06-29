# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | unacc | 0.701675 |
| Safety != low and Persons != 2 and Maint != vhigh and Buying != vhigh and Buying = high and Lug_boot != small | acc | 0.054538 |
| Safety != low and Persons != 2 and Maint = vhigh and Buying != vhigh and Buying != high and Lug_boot != small | acc | 0.037967 |
| Safety != low and Persons != 2 and Maint != vhigh and Buying = vhigh and Maint != high and Safety != med | acc | 0.033697 |
| Safety != low and Persons != 2 and Maint != vhigh and Buying != vhigh and Buying != high and Safety = med and Lug_boot = small and Maint != high | acc | 0.019903 |
| Safety != low and Persons != 2 and Maint != vhigh and Buying != vhigh and Buying != high and Safety = med and Lug_boot != small and Maint = high | acc | 0.019740 |
| Safety != low and Persons != 2 and Maint != vhigh and Buying != vhigh and Buying != high and Safety != med and Lug_boot != small and Maint != high | vgood | 0.024697 |
| Safety != low and Persons != 2 and Maint != vhigh and Buying = vhigh and Maint != high and Safety = med and Lug_boot != small | acc | 0.013366 |
| Safety != low and Persons != 2 and Maint != vhigh and Buying != vhigh and Buying = high and Lug_boot = small and Safety != med | acc | 0.012447 |
| Safety != low and Persons != 2 and Maint != vhigh and Buying != vhigh and Buying != high and Safety != med and Lug_boot = small and Maint != low | acc | 0.011680 |
| Safety != low and Persons != 2 and Maint != vhigh and Buying != vhigh and Buying != high and Safety = med and Lug_boot != small and Maint != high and Buying != med | good | 0.011463 |
| Safety != low and Persons != 2 and Maint != vhigh and Buying != vhigh and Buying != high and Safety = med and Lug_boot != small and Maint != high and Buying = med and Maint = med | acc | 0.012275 |
| Safety != low and Persons != 2 and Maint != vhigh and Buying != vhigh and Buying != high and Safety != med and Lug_boot != small and Maint = high and Buying = med | acc | 0.011466 |
| Safety != low and Persons != 2 and Maint != vhigh and Buying != vhigh and Buying != high and Safety != med and Lug_boot = small and Maint = low | good | 0.006848 |
| Safety != low and Persons != 2 and Maint = vhigh and Buying != vhigh and Buying != high and Lug_boot = small and Safety != med | acc | 0.006859 |
| Safety != low and Persons != 2 and Maint != vhigh and Buying != vhigh and Buying != high and Safety = med and Lug_boot != small and Maint != high and Buying = med and Maint != med | good | 0.005762 |
| Safety != low and Persons != 2 and Maint != vhigh and Buying != vhigh and Buying != high and Safety != med and Lug_boot != small and Maint = high and Buying != med | vgood | 0.006839 |
| Buying = low and Maint = med and Persons = 4 and Safety = high | good | 0.002410 |
| Buying = low and Maint = high and Persons = 4 and Safety = med | acc | 0.008217 |
| Buying = low and Maint = med and Persons = 4 and Safety = med | acc | 0.002978 |
| Buying = med and Maint = med and Persons = 4 and Safety = high | acc | 0.002709 |
| Buying = low and Maint = high and Persons = more and Safety = med | acc | 0.007476 |
| Buying = low and Maint = low and Persons = 4 and Safety = high | good | 0.001676 |
| Buying = med and Maint = low and Persons = 4 and Safety = high | good | 0.002011 |
| Buying = low and Maint = high and Persons = 4 and Safety = high | acc | 0.001885 |
| Buying = med and Maint = low and Persons = more and Safety = med | acc | 0.001328 |
| Buying = low and Maint = low and Persons = more and Safety = med | acc | 0.001328 |

## Ordered rules

### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Safety = high and Buying = low and Lug_boot = big and Persons = more | vgood | 0.004762 |
| Safety = high and Buying = low and Persons = 4 and Lug_boot = big | vgood | 0.004762 |
| Safety = high and Buying = med and Lug_boot = big and Maint = low | vgood | 0.003881 |
| Safety = high and Persons = 4 | acc | 0.049071 |
| Persons = 4 and Safety = med and Buying = low | acc | 0.015647 |
| Persons = more and Safety = high and Buying = high | acc | 0.015277 |
| Persons = more and Safety = med and Buying = med | acc | 0.014641 |
| Safety = med and Persons = 4 and Buying = med and Maint = med | acc | 0.009244 |
| Safety = med and Persons = 4 and Lug_boot = big | acc | 0.013491 |
| Persons = more and Safety = med and Buying = low | acc | 0.011730 |
| Persons = more and Safety = high and Buying = med and Maint = high | acc | 0.007652 |
| Persons = more and Safety = high and Buying = vhigh and Maint = low | acc | 0.008481 |
| Persons = more and Safety = high and Maint = vhigh | acc | 0.007151 |
| Persons = more and Safety = med and Lug_boot = big | acc | 0.004528 |
| Persons = more and Safety = high and Maint = med and Buying = vhigh | acc | 0.008481 |
| Safety = med and Lug_boot = med and Persons = more and Buying = high | acc | 0.004287 |
|  | unacc | 0.901490 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

buying|maint|persons|safety|acceptability
---|---|---|---|---
low|low|more|high|vgood
med|low|more|high|vgood
high|low|more|high|acc
vhigh|low|more|high|acc
med|med|more|high|vgood
low|med|more|high|vgood
vhigh|med|more|high|acc
high|med|more|high|acc
high|low|4|high|acc
vhigh|low|4|high|acc
med|low|4|high|good
low|low|4|high|good
vhigh|high|more|high|unacc
high|high|more|high|acc
med|high|more|high|acc
low|high|more|high|vgood
high|vhigh|more|high|unacc
low|vhigh|more|high|acc
med|low|more|med|acc
low|med|4|high|good
low|low|more|med|acc
med|vhigh|more|high|acc
vhigh|vhigh|more|high|unacc
high|low|more|med|unacc
vhigh|med|4|high|acc
med|med|4|high|acc
vhigh|low|more|med|acc
high|med|4|high|acc
vhigh|low|2|high|unacc
med|high|4|high|acc
low|high|4|high|acc
low|low|2|high|unacc
vhigh|high|4|high|unacc
high|med|more|med|acc
high|low|2|high|unacc
med|low|2|high|unacc
vhigh|med|more|med|unacc
med|med|more|med|acc
high|high|4|high|acc
low|med|more|med|good
high|vhigh|4|high|unacc
high|high|more|med|unacc
med|low|4|med|good
high|low|4|med|acc
vhigh|high|more|med|unacc
high|med|2|high|unacc
vhigh|vhigh|4|high|unacc
med|med|2|high|unacc
low|med|2|high|unacc
vhigh|med|2|high|unacc
low|high|more|med|acc
low|low|4|med|good
med|vhigh|4|high|acc
med|high|more|med|acc
vhigh|low|4|med|unacc
low|vhigh|4|high|acc
high|vhigh|more|med|unacc
med|vhigh|more|med|acc
high|low|more|low|unacc
low|vhigh|more|med|acc
high|high|2|high|unacc
vhigh|vhigh|more|med|unacc
vhigh|med|4|med|acc
vhigh|low|more|low|unacc
med|high|2|high|unacc
low|high|2|high|unacc
med|low|more|low|unacc
low|low|more|low|unacc
vhigh|high|2|high|unacc
low|med|4|med|acc
med|med|4|med|acc
high|med|4|med|unacc
low|vhigh|2|high|unacc
med|med|more|low|unacc
vhigh|high|4|med|unacc
med|low|2|med|unacc
high|low|2|med|unacc
low|med|more|low|unacc
high|med|more|low|unacc
high|vhigh|2|high|unacc
vhigh|med|more|low|unacc
med|vhigh|2|high|unacc
low|low|2|med|unacc
vhigh|low|2|med|unacc
vhigh|vhigh|2|high|unacc
low|high|4|med|acc
high|high|4|med|unacc
med|high|4|med|unacc
med|high|more|low|unacc
vhigh|low|4|low|unacc
vhigh|vhigh|4|med|unacc
high|high|more|low|unacc
low|high|more|low|unacc
high|low|4|low|unacc
med|med|2|med|unacc
high|vhigh|4|med|unacc
low|med|2|med|unacc
vhigh|med|2|med|unacc
high|med|2|med|unacc
low|low|4|low|unacc
vhigh|high|more|low|unacc
med|low|4|low|unacc
low|vhigh|4|med|acc
med|vhigh|4|med|unacc
med|vhigh|more|low|unacc
high|high|2|med|unacc
vhigh|high|2|med|unacc
high|vhigh|more|low|unacc
low|high|2|med|unacc
vhigh|vhigh|more|low|unacc
low|med|4|low|unacc
high|med|4|low|unacc
med|high|2|med|unacc
low|vhigh|more|low|unacc
med|med|4|low|unacc
vhigh|med|4|low|unacc
low|high|4|low|unacc
med|low|2|low|unacc
high|low|2|low|unacc
vhigh|low|2|low|unacc
vhigh|vhigh|2|med|unacc
high|high|4|low|unacc
med|high|4|low|unacc
high|vhigh|2|med|unacc
low|vhigh|2|med|unacc
vhigh|high|4|low|unacc
med|vhigh|2|med|unacc
low|low|2|low|unacc
med|vhigh|4|low|unacc
med|med|2|low|unacc
low|vhigh|4|low|unacc
high|vhigh|4|low|unacc
vhigh|vhigh|4|low|unacc
vhigh|med|2|low|unacc
low|med|2|low|unacc
high|med|2|low|unacc
vhigh|high|2|low|unacc
high|high|2|low|unacc
med|high|2|low|unacc
low|high|2|low|unacc
med|vhigh|2|low|unacc
vhigh|vhigh|2|low|unacc
high|vhigh|2|low|unacc
low|vhigh|2|low|unacc

## JRip

Decision list:

rules | predicted class
---|---
(Safety = high) and (Buying = low) and (Lug_boot = big) and (Persons = more)|vgood (14.0/4.0)
(Safety = high) and (Buying = low) and (Persons = 4) and (Lug_boot = big)|vgood (14.0/4.0)
(Safety = high) and (Buying = med) and (Lug_boot = big) and (Maint = low)|vgood (11.0/3.0)
(Safety = high) and (Persons = 4)|acc (147.0/56.0)
(Persons = 4) and (Safety = med) and (Buying = low)|acc (42.0/14.0)
(Persons = more) and (Safety = high) and (Buying = high)|acc (40.0/13.0)
(Persons = more) and (Safety = med) and (Buying = med)|acc (45.0/17.0)
(Safety = med) and (Persons = 4) and (Buying = med) and (Maint = med)|acc (11.0/0.0)
(Safety = med) and (Persons = 4) and (Lug_boot = big)|acc (43.0/15.0)
(Persons = more) and (Safety = med) and (Buying = low)|acc (45.0/20.0)
(Persons = more) and (Safety = high) and (Buying = med) and (Maint = high)|acc (11.0/1.0)
(Persons = more) and (Safety = high) and (Buying = vhigh) and (Maint = low)|acc (12.0/1.0)
(Persons = more) and (Safety = high) and (Maint = vhigh)|acc (28.0/13.0)
(Persons = more) and (Safety = med) and (Lug_boot = big)|acc (26.0/12.0)
(Persons = more) and (Safety = high) and (Maint = med) and (Buying = vhigh)|acc (12.0/1.0)
(Safety = med) and (Lug_boot = med) and (Persons = more) and (Buying = high)|acc (16.0/7.0)
|unacc (1035.0/59.0)


## J48 Decision Tree

* Safety = low: unacc (519.0)
* Safety != low
	* Persons = 2: unacc (349.0)
	* Persons != 2
		* Maint = vhigh
			* Buying = vhigh: unacc (43.0)
			* Buying != vhigh
				* Buying = high: unacc (43.0)
				* Buying != high
					* Lug_boot = small
						* Safety = med: unacc (13.0)
						* Safety != med: acc (12.0/2.0)
					* Lug_boot != small: acc (59.0/6.0)
		* Maint != vhigh
			* Buying = vhigh
				* Maint = high: unacc (41.0)
				* Maint != high
					* Safety = med
						* Lug_boot = small: unacc (14.0)
						* Lug_boot != small: acc (27.0/6.0)
					* Safety != med: acc (46.0/2.0)
			* Buying != vhigh
				* Buying = high
					* Lug_boot = small
						* Safety = med: unacc (21.0)
						* Safety != med: acc (19.0/2.0)
					* Lug_boot != small: acc (83.0/7.0)
				* Buying != high
					* Safety = med
						* Lug_boot = small
							* Maint = high: unacc (15.0/6.0)
							* Maint != high: acc (32.0/4.0)
						* Lug_boot != small
							* Maint = high: acc (30.0/3.0)
							* Maint != high
								* Buying = med
									* Maint = med: acc (15.0)
									* Maint != med: good (14.0/3.0)
								* Buying != med: good (28.0/6.0)
					* Safety != med
						* Lug_boot = small
							* Maint = low: good (14.0/2.0)
							* Maint != low: acc (31.0/10.0)
						* Lug_boot != small
							* Maint = high
								* Buying = med: acc (14.0)
								* Buying != med: vgood (14.0/2.0)
							* Maint != high: vgood (56.0/10.0)


