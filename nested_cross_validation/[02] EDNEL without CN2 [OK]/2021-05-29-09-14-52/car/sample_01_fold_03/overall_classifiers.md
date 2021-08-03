# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | unacc | 0.701223 |
| Persons != 2 and Safety != low and Buying != low and Buying != med and Maint != vhigh and Lug_boot != small and Maint != high | acc | 0.073702 |
| Persons != 2 and Safety != low and Buying != low and Buying = med and Maint != low and Lug_boot != small and Maint != med | acc | 0.036919 |
| Persons != 2 and Safety != low and Buying != low and Buying != med and Maint != vhigh and Lug_boot = small and Safety != med | acc | 0.020868 |
| Persons != 2 and Safety != low and Buying = low and Maint = vhigh | acc | 0.019822 |
| Persons != 2 and Safety != low and Buying != low and Buying != med and Maint != vhigh and Lug_boot != small and Maint = high and Buying != vhigh | acc | 0.018936 |
| Persons != 2 and Safety != low and Buying = low and Maint != vhigh and Safety != med and Lug_boot != small | vgood | 0.019554 |
| Persons != 2 and Safety != low and Buying != low and Buying = med and Maint != low and Lug_boot = small and Safety != med | acc | 0.013406 |
| Persons != 2 and Safety != low and Buying = low and Maint != vhigh and Safety = med and Lug_boot = small | acc | 0.013406 |
| Persons != 2 and Safety != low and Buying = low and Maint != vhigh and Safety = med and Lug_boot != small and Maint != high | good | 0.012804 |
| Persons != 2 and Safety != low and Buying != low and Buying = med and Maint != low and Lug_boot != small and Maint = med and Safety = med | acc | 0.012265 |
| Persons != 2 and Safety != low and Buying = low and Maint != vhigh and Safety = med and Lug_boot != small and Maint = high | acc | 0.011457 |
| Persons != 2 and Safety != low and Buying = low and Maint != vhigh and Safety != med and Lug_boot = small | good | 0.004584 |
| Persons != 2 and Safety != low and Buying != low and Buying = med and Maint = low and Safety = med | good | 0.004378 |
| Persons != 2 and Safety != low and Buying != low and Buying = med and Maint != low and Lug_boot != small and Maint = med and Safety != med | vgood | 0.005125 |
| Persons != 2 and Safety != low and Buying != low and Buying = med and Maint = low and Safety != med | vgood | 0.004581 |
| Buying = med and Maint = med and Persons = more and Safety = med | acc | 0.008279 |
| Buying = med and Maint = med and Persons = 4 and Safety = med | acc | 0.008210 |
| Persons = 4 and Safety = med and Buying = med and Maint != med and Lug_boot = med and Maint = low and Buying != vhigh | acc | 0.000828 |
| Buying = low and Maint = med and Persons = 4 and Safety = med | acc | 0.002707 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Persons = 2 | unacc | 0.529412 |
| Safety = low | unacc | 0.428571 |
| Buying = vhigh and Maint = vhigh | unacc | 0.086614 |
| Buying != low and Buying != med and Maint != vhigh and Maint != high and Lug_boot != small and Doors != 2 | acc | 0.216276 |
| Buying = vhigh and Maint = high | unacc | 0.095238 |
| Buying = high and Maint != vhigh and Safety != med | acc | 0.130837 |
| Buying = high and Maint != high and Lug_boot != big | unacc | 0.126289 |
| Safety = med and Buying = vhigh and Lug_boot != big | unacc | 0.053073 |
| Maint = vhigh and Buying != high and Lug_boot != small | acc | 0.202446 |
| Maint = vhigh and Safety = med | unacc | 0.079618 |
| Lug_boot = small and Doors != 2 and Buying != high and Maint != high and Safety = med | acc | 0.115385 |
| Lug_boot = small and Safety != med and Doors != 2 and Maint != low | acc | 0.156005 |
| Lug_boot = small and Maint != low | unacc | 0.059186 |
| Safety = med and Maint = high and Lug_boot != med | acc | 0.170732 |
| Buying = high and Maint != vhigh | acc | 0.047535 |
| Safety = med and Lug_boot != small and Maint != high and Buying = low | good | 0.111908 |
| Safety = med and Maint != low | acc | 0.186856 |
| Buying != high and Lug_boot != small and Safety = med and Doors != 2 | good | 0.063613 |
| Buying != high and Lug_boot != small and Buying != vhigh and Maint != high | vgood | 0.277581 |
| Buying != high and Lug_boot != small | acc | 0.283963 |
| Buying != vhigh and Safety != med and Buying != high | good | 0.294553 |
| Buying != high and Doors != 2 | acc | 0.076923 |
| Persons != 4 | unacc | 0.198529 |
| Buying = high | unacc | 0.206897 |
|  | acc | 0.320000 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Safety = high and Buying = low and Lug_boot = big and Persons = 4 | vgood | 0.005374 |
| Safety = high and Buying = low and Persons = more and Lug_boot = big | vgood | 0.006387 |
| Safety = high and Buying = med and Maint = low and Lug_boot = big and Persons = 4 | vgood | 0.002670 |
| Safety = high and Maint = med and Buying = med and Lug_boot = big | vgood | 0.002089 |
| Buying = low and Safety = high and Lug_boot = med and Persons = more | vgood | 0.003607 |
| Safety = high and Buying = med and Maint = low and Persons = more | vgood | 0.002406 |
| Safety = high and Lug_boot = med and Buying = med and Maint = med | vgood | 0.001522 |
| Buying = low and Maint = low and Persons = 4 and Safety = high | good | 0.002884 |
| Buying = low and Safety = med and Maint = low and Persons = more | good | 0.002830 |
| Buying = low and Maint = med and Safety = high and Persons = 4 | good | 0.002473 |
| Maint = low and Buying = med and Persons = 4 and Safety = high | good | 0.002473 |
| Buying = low and Safety = med and Maint = med and Lug_boot = big | good | 0.004024 |
| Maint = low and Safety = med and Buying = med and Lug_boot = big | good | 0.003391 |
| Buying = low and Maint = low and Safety = med and Persons = 4 | good | 0.002166 |
| Buying = low and Persons = more and Safety = high | good | 0.001861 |
| Lug_boot = med and Safety = med and Maint = low and Buying = med | good | 0.001448 |
| Safety = high and Persons = 4 | acc | 0.062261 |
| Safety = high and Persons = more | acc | 0.047980 |
| Safety = med and Persons = more and Lug_boot = big | acc | 0.026646 |
| Persons = 4 and Safety = med and Lug_boot = big and Maint = med | acc | 0.010782 |
| Safety = med and Persons = 4 and Buying = low | acc | 0.018001 |
| Safety = med and Persons = 4 and Buying = med and Lug_boot = big | acc | 0.005420 |
| Safety = med and Persons = more and Lug_boot = med | acc | 0.016517 |
| Safety = med and Persons = 4 and Lug_boot = big and Maint = low | acc | 0.007214 |
| Safety = med and Persons = 4 and Lug_boot = med and Doors = 4 | acc | 0.005781 |
| Safety = med and Persons = 4 and Buying = med and Maint = med | acc | 0.004521 |
| Safety = med and Persons = 4 and Buying = med and Maint = low | acc | 0.005420 |
| Safety = med and Persons = 4 and Doors = 5more and Lug_boot = med | acc | 0.003623 |
|  | unacc | 0.974933 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

buying|maint|persons|safety|acceptability
---|---|---|---|---
med|low|more|high|vgood
low|low|more|high|vgood
high|low|more|high|acc
vhigh|low|more|high|acc
low|med|more|high|vgood
high|med|more|high|acc
med|med|more|high|vgood
vhigh|med|more|high|acc
med|low|4|high|vgood
low|low|4|high|vgood
vhigh|high|more|high|unacc
med|high|more|high|acc
low|high|more|high|vgood
high|low|4|high|acc
high|high|more|high|acc
vhigh|low|4|high|acc
low|med|4|high|vgood
high|vhigh|more|high|unacc
vhigh|vhigh|more|high|unacc
low|low|more|med|good
vhigh|med|4|high|acc
high|low|more|med|acc
med|low|more|med|good
med|vhigh|more|high|acc
high|med|4|high|acc
med|med|4|high|vgood
low|vhigh|more|high|acc
vhigh|low|more|med|acc
high|low|2|high|unacc
low|low|2|high|unacc
vhigh|high|4|high|unacc
vhigh|low|2|high|unacc
med|low|2|high|unacc
vhigh|med|more|med|acc
med|high|4|high|acc
high|med|more|med|acc
high|high|4|high|acc
low|med|more|med|good
med|med|more|med|acc
low|high|4|high|vgood
low|med|2|high|unacc
vhigh|high|more|med|unacc
high|med|2|high|unacc
med|med|2|high|unacc
high|vhigh|4|high|unacc
vhigh|med|2|high|unacc
vhigh|vhigh|4|high|unacc
med|vhigh|4|high|acc
high|low|4|med|unacc
low|high|more|med|acc
vhigh|low|4|med|unacc
med|high|more|med|unacc
med|low|4|med|good
low|low|4|med|good
low|vhigh|4|high|acc
high|high|more|med|acc
med|low|more|low|unacc
low|low|more|low|unacc
vhigh|vhigh|more|med|unacc
vhigh|high|2|high|unacc
high|high|2|high|unacc
med|high|2|high|unacc
low|high|2|high|unacc
vhigh|low|more|low|unacc
high|vhigh|more|med|unacc
high|low|more|low|unacc
low|vhigh|more|med|acc
med|vhigh|more|med|acc
vhigh|med|4|med|unacc
med|med|4|med|acc
high|med|4|med|unacc
low|med|4|med|acc
low|vhigh|2|high|unacc
low|low|2|med|unacc
low|med|more|low|unacc
high|low|2|med|unacc
med|low|2|med|unacc
vhigh|vhigh|2|high|unacc
high|med|more|low|unacc
vhigh|high|4|med|unacc
vhigh|med|more|low|unacc
high|vhigh|2|high|unacc
med|med|more|low|unacc
vhigh|low|2|med|unacc
med|vhigh|2|high|unacc
low|high|4|med|acc
med|high|4|med|unacc
high|high|4|med|unacc
vhigh|vhigh|4|med|unacc
med|low|4|low|unacc
vhigh|low|4|low|unacc
vhigh|high|more|low|unacc
high|vhigh|4|med|unacc
high|high|more|low|unacc
high|med|2|med|unacc
high|low|4|low|unacc
low|low|4|low|unacc
med|med|2|med|unacc
vhigh|med|2|med|unacc
med|high|more|low|unacc
low|med|2|med|unacc
low|high|more|low|unacc
med|vhigh|4|med|unacc
low|vhigh|4|med|unacc
high|vhigh|more|low|unacc
vhigh|vhigh|more|low|unacc
low|high|2|med|unacc
high|med|4|low|unacc
med|high|2|med|unacc
vhigh|med|4|low|unacc
vhigh|high|2|med|unacc
low|vhigh|more|low|unacc
high|high|2|med|unacc
med|med|4|low|unacc
med|vhigh|more|low|unacc
low|med|4|low|unacc
med|high|4|low|unacc
med|vhigh|2|med|unacc
high|vhigh|2|med|unacc
high|low|2|low|unacc
vhigh|high|4|low|unacc
med|low|2|low|unacc
low|low|2|low|unacc
vhigh|low|2|low|unacc
low|vhigh|2|med|unacc
vhigh|vhigh|2|med|unacc
low|high|4|low|unacc
high|high|4|low|unacc
low|vhigh|4|low|unacc
med|vhigh|4|low|unacc
vhigh|vhigh|4|low|unacc
high|vhigh|4|low|unacc
med|med|2|low|unacc
low|med|2|low|unacc
high|med|2|low|unacc
vhigh|med|2|low|unacc
med|high|2|low|unacc
low|high|2|low|unacc
vhigh|high|2|low|unacc
high|high|2|low|unacc
low|vhigh|2|low|unacc
med|vhigh|2|low|unacc
high|vhigh|2|low|unacc
vhigh|vhigh|2|low|unacc

## JRip

Decision list:

rules | predicted class
---|---
(Safety = high) and (Buying = low) and (Lug_boot = big) and (Persons = 4)|vgood (15.0/4.0)
(Safety = high) and (Buying = low) and (Persons = more) and (Lug_boot = big)|vgood (15.0/3.0)
(Safety = high) and (Buying = med) and (Maint = low) and (Lug_boot = big) and (Persons = 4)|vgood (4.0/0.0)
(Safety = high) and (Maint = med) and (Buying = med) and (Lug_boot = big)|vgood (8.0/3.0)
(Buying = low) and (Safety = high) and (Lug_boot = med) and (Persons = more)|vgood (15.0/6.0)
(Safety = high) and (Buying = med) and (Maint = low) and (Persons = more)|vgood (10.0/4.0)
(Safety = high) and (Lug_boot = med) and (Buying = med) and (Maint = med)|vgood (11.0/6.0)
(Buying = low) and (Maint = low) and (Persons = 4) and (Safety = high)|good (6.0/1.0)
(Buying = low) and (Safety = med) and (Maint = low) and (Persons = more)|good (12.0/5.0)
(Buying = low) and (Maint = med) and (Safety = high) and (Persons = 4)|good (7.0/2.0)
(Maint = low) and (Buying = med) and (Persons = 4) and (Safety = high)|good (7.0/2.0)
(Buying = low) and (Safety = med) and (Maint = med) and (Lug_boot = big)|good (11.0/3.0)
(Maint = low) and (Safety = med) and (Buying = med) and (Lug_boot = big)|good (10.0/3.0)
(Buying = low) and (Maint = low) and (Safety = med) and (Persons = 4)|good (8.0/3.0)
(Buying = low) and (Persons = more) and (Safety = high)|good (15.0/9.0)
(Lug_boot = med) and (Safety = med) and (Maint = low) and (Buying = med)|good (12.0/7.0)
(Safety = high) and (Persons = 4)|acc (130.0/35.0)
(Safety = high) and (Persons = more)|acc (108.0/37.0)
(Safety = med) and (Persons = more) and (Lug_boot = big)|acc (48.0/10.0)
(Persons = 4) and (Safety = med) and (Lug_boot = big) and (Maint = med)|acc (12.0/0.0)
(Safety = med) and (Persons = 4) and (Buying = low)|acc (28.0/6.0)
(Safety = med) and (Persons = 4) and (Buying = med) and (Lug_boot = big)|acc (6.0/0.0)
(Safety = med) and (Persons = more) and (Lug_boot = med)|acc (47.0/19.0)
(Safety = med) and (Persons = 4) and (Lug_boot = big) and (Maint = low)|acc (8.0/0.0)
(Safety = med) and (Persons = 4) and (Lug_boot = med) and (Doors = 4)|acc (10.0/2.0)
(Safety = med) and (Persons = 4) and (Buying = med) and (Maint = med)|acc (5.0/0.0)
(Safety = med) and (Persons = 4) and (Buying = med) and (Maint = low)|acc (4.0/0.0)
(Safety = med) and (Persons = 4) and (Doors = 5more) and (Lug_boot = med)|acc (8.0/2.0)
|unacc (973.0/13.0)


## PART

Decision list:

rules | predicted class
---|---
Persons = 2|unacc (453.0)
Safety = low|unacc (300.0)
Buying = vhigh AND Maint = vhigh|unacc (36.0)
Buying != low AND Buying != med AND Maint != vhigh AND Maint != high AND Lug_boot != small AND Doors != 2|acc (72.0/2.0)
Buying = vhigh AND Maint = high|unacc (36.0)
Buying = high AND Maint != vhigh AND Safety != med|acc (39.0/3.0)
Buying = high AND Maint != high AND Lug_boot != big|unacc (35.0)
Safety = med AND Buying = vhigh AND Lug_boot != big|unacc (16.0)
Maint = vhigh AND Buying != high AND Lug_boot != small|acc (44.0/1.0)
Maint = vhigh AND Safety = med|unacc (16.0)
Lug_boot = small AND Doors != 2 AND Buying != high AND Maint != high AND Safety = med|acc (19.0)
Lug_boot = small AND Safety != med AND Doors != 2 AND Maint != low|acc (34.0/5.0)
Lug_boot = small AND Maint != low|unacc (36.0/14.0)
Safety = med AND Maint = high AND Lug_boot != med|acc (18.0)
Buying = high AND Maint != vhigh|acc (10.0/3.0)
Safety = med AND Lug_boot != small AND Maint != high AND Buying = low|good (23.0/3.0)
Safety = med AND Maint != low|acc (24.0/2.0)
Buying != high AND Lug_boot != small AND Safety = med AND Doors != 2|good (7.0/1.0)
Buying != high AND Lug_boot != small AND Buying != vhigh AND Maint != high|vgood (52.0/14.0)
Buying != high AND Lug_boot != small|acc (36.0/13.0)
Buying != vhigh AND Safety != med AND Buying != high|good (12.0/2.0)
Buying != high AND Doors != 2|acc (5.0)
Persons != 4|unacc (5.0)
Buying = high|unacc (2.0)
|acc (2.0)


## J48 Decision Tree

* Persons = 2: unacc (522.0)
* Persons != 2
	* Safety = low: unacc (348.0)
	* Safety != low
		* Buying = low
			* Maint = vhigh: acc (42.0/10.0)
			* Maint != vhigh
				* Safety = med
					* Lug_boot = small: acc (22.0/3.0)
					* Lug_boot != small
						* Maint = high: acc (14.0)
						* Maint != high: good (25.0/3.0)
				* Safety != med
					* Lug_boot = small: good (21.0/9.0)
					* Lug_boot != small: vgood (46.0/9.0)
		* Buying != low
			* Buying = med
				* Maint = low
					* Safety = med: good (22.0/10.0)
					* Safety != med: vgood (21.0/9.0)
				* Maint != low
					* Lug_boot = small
						* Safety = med: unacc (22.0/6.0)
						* Safety != med: acc (22.0/3.0)
					* Lug_boot != small
						* Maint = med
							* Safety = med: acc (15.0)
							* Safety != med: vgood (13.0/3.0)
						* Maint != med: acc (54.0/4.0)
			* Buying != med
				* Maint = vhigh: unacc (85.0)
				* Maint != vhigh
					* Lug_boot = small
						* Safety = med: unacc (41.0)
						* Safety != med: acc (45.0/11.0)
					* Lug_boot != small
						* Maint = high
							* Buying = vhigh: unacc (27.0)
							* Buying != vhigh: acc (29.0/3.0)
						* Maint != high: acc (117.0/11.0)


## SimpleCart Decision Tree

	* Persons=(more)|(4)
		* Safety=(high)|(med)
			* Buying=(low)|(med)
				* Maint=(low)|(med)
					* Safety=(high)|(low)
						* Lug_boot=(big)|(med)
							* Doors=(5more)|(4): vgood(30.0/0.0)
							* Doors!=(5more)|(4)
							* Lug_boot=(big): vgood(12.0/0.0)
							* Lug_boot!=(big)
								* Persons=(more)
											* Doors=(3)|(4)|(5more): vgood(4.0/0.0)
											* Doors!=(3)|(4)|(5more): good(2.0/1.0)
								* Persons!=(more)
											* Buying=(low)|(vhigh)|(high): good(4.0/0.0)
											* Buying!=(low)|(vhigh)|(high)
												* Maint=(low)|(vhigh)|(high): good(2.0/0.0)
												* Maint!=(low)|(vhigh)|(high): acc(2.0/0.0)
						* Lug_boot!=(big)|(med)
								* Buying=(low)|(vhigh)|(high)
									* Doors=(5more)|(4)|(3): good(10.0/0.0)
									* Doors!=(5more)|(4)|(3)
									* Persons=(more)|(2): unacc(2.0/0.0)
									* Persons!=(more)|(2): good(2.0/0.0)
								* Buying!=(low)|(vhigh)|(high)
									* Maint=(low)|(vhigh)|(high): good(6.0/1.0)
									* Maint!=(low)|(vhigh)|(high): acc(6.0/1.0)
					* Safety!=(high)|(low)
						* Lug_boot=(big)|(med)
								* Maint=(low)|(vhigh)|(high)
									* Doors=(5more)|(4)|(3): good(20.0/1.0)
									* Doors!=(5more)|(4)|(3)
									* Lug_boot=(big)|(small): good(4.0/0.0)
									* Lug_boot!=(big)|(small): acc(3.0/0.0)
								* Maint!=(low)|(vhigh)|(high)
							* Buying=(low)
									* Lug_boot=(big)|(small): good(8.0/0.0)
									* Lug_boot!=(big)|(small)
										* Doors=(5more)|(4): good(2.0/0.0)
										* Doors!=(5more)|(4): acc(2.0/0.0)
							* Buying!=(low): acc(15.0/0.0)
						* Lug_boot!=(big)|(med)
								* Doors=(5more)|(4)|(3): acc(21.0/0.0)
								* Doors!=(5more)|(4)|(3)
								* Persons=(more)|(2): unacc(4.0/0.0)
								* Persons!=(more)|(2): acc(3.0/0.0)
				* Maint!=(low)|(med)
					* Lug_boot=(big)|(med)
							* Maint=(high)|(med)|(low)
								* Buying=(low)|(vhigh)|(high)
								* Safety=(high)|(low)
									* Doors=(5more)|(4): vgood(8.0/0.0)
									* Doors!=(5more)|(4)
										* Lug_boot=(big)|(small): vgood(4.0/0.0)
										* Lug_boot!=(big)|(small): acc(3.0/1.0)
								* Safety!=(high)|(low): acc(14.0/0.0)
								* Buying!=(low)|(vhigh)|(high): acc(25.0/3.0)
							* Maint!=(high)|(med)|(low)
								* Doors=(5more)|(4)|(3): acc(38.0/0.0)
								* Doors!=(5more)|(4)|(3)
								* Lug_boot=(big)|(small): acc(8.0/0.0)
								* Lug_boot!=(big)|(small)
									* Safety=(high)|(low): acc(4.0/0.0)
									* Safety!=(high)|(low): unacc(3.0/0.0)
					* Lug_boot!=(big)|(med)
						* Safety=(high)|(low)
								* Doors=(5more)|(4)|(3): acc(22.0/0.0)
								* Doors!=(5more)|(4)|(3)
								* Persons=(more)|(2): unacc(4.0/0.0)
								* Persons!=(more)|(2): acc(4.0/0.0)
						* Safety!=(high)|(low)
								* Buying=(low)|(vhigh)|(high)
									* Maint=(high)|(med)|(low): acc(7.0/1.0)
									* Maint!=(high)|(med)|(low): unacc(7.0/0.0)
								* Buying!=(low)|(vhigh)|(high): unacc(15.0/0.0)
			* Buying!=(low)|(med)
				* Maint=(low)|(med)
					* Lug_boot=(big)|(med)
							* Doors=(5more)|(4)|(3)
								* Doors=(5more)|(4)|(2): acc(59.0/0.0)
								* Doors!=(5more)|(4)|(2)
								* Lug_boot=(big)|(small): acc(15.0/0.0)
								* Lug_boot!=(big)|(small)
									* Safety=(high)|(low): acc(7.0/0.0)
									* Safety!=(high)|(low)
										* Persons=(more)|(2): acc(3.0/0.0)
										* Persons!=(more)|(2): unacc(3.0/0.0)
							* Doors!=(5more)|(4)|(3)
						* Lug_boot=(big): acc(14.0/0.0)
						* Lug_boot!=(big)
								* Safety=(high)|(low): acc(8.0/0.0)
								* Safety!=(high)|(low): unacc(8.0/0.0)
					* Lug_boot!=(big)|(med)
						* Safety=(high)|(low)
								* Doors=(5more)|(4)|(3): acc(24.0/0.0)
								* Doors!=(5more)|(4)|(3)
								* Persons=(more)|(2): unacc(4.0/0.0)
								* Persons!=(more)|(2): acc(4.0/0.0)
						* Safety!=(high)|(low): unacc(28.0/0.0)
				* Maint!=(low)|(med)
				* Maint=(high)
							* Buying=(high)|(med)|(low)
							* Lug_boot=(big)|(med): acc(26.0/3.0)
							* Lug_boot!=(big)|(med)
								* Safety=(high)|(low): acc(6.0/1.0)
								* Safety!=(high)|(low): unacc(6.0/0.0)
							* Buying!=(high)|(med)|(low): unacc(40.0/0.0)
				* Maint!=(high): unacc(85.0/0.0)
		* Safety!=(high)|(med): unacc(348.0/0.0)
	* Persons!=(more)|(4): unacc(522.0/0.0)


