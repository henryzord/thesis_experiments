# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Safety != high | unacc | 0.615952 |
| Safety != med | unacc | 0.590944 |
| Buying = low and Maint = vhigh and Persons = 4 and Safety = high | acc | 0.009836 |
| Buying = high and Maint = high and Persons = 4 and Safety = high | acc | 0.009836 |
| Buying = med and Maint = vhigh and Persons = 4 and Safety = high | acc | 0.009836 |
| Buying = med and Maint = med and Persons = more and Safety = med | acc | 0.008279 |
| Buying = vhigh and Maint = low and Persons = 4 and Safety = high | acc | 0.009024 |
| Buying = high and Maint = med and Persons = more and Safety = high | acc | 0.008279 |
| Buying = low and Maint = high and Persons = 4 and Safety = med | acc | 0.009024 |
| Buying = high and Maint = high and Persons = more and Safety = high | acc | 0.007470 |
| Buying = high and Maint = low and Persons = 4 and Safety = high | acc | 0.008210 |
| Buying = high and Maint = med and Persons = 4 and Safety = high | acc | 0.008210 |
| Buying = low and Maint = high and Persons = more and Safety = med | acc | 0.007470 |
| Buying = med and Maint = vhigh and Persons = more and Safety = high | acc | 0.007470 |
| Buying = high and Maint = low and Persons = more and Safety = high | acc | 0.007470 |
| Buying = low and Maint = vhigh and Persons = more and Safety = high | acc | 0.007470 |
| Buying = med and Maint = med and Persons = 4 and Safety = med | acc | 0.008210 |
| Buying = med and Maint = high and Persons = 4 and Safety = high | acc | 0.008210 |
| Buying = vhigh and Maint = low and Persons = more and Safety = high | acc | 0.006661 |
| Buying = med and Maint = high and Persons = more and Safety = high | acc | 0.006661 |
| Buying = vhigh and Maint = med and Persons = 4 and Safety = high | acc | 0.007395 |
| Buying = vhigh and Maint = med and Persons = more and Safety = high | acc | 0.006661 |
| Buying = vhigh and Maint = med and Persons = more and Safety = med | acc | 0.003678 |
| Buying = high and Maint = high and Persons = more and Safety = med | acc | 0.003375 |
| Buying = high and Maint = low and Persons = more and Safety = med | acc | 0.003678 |
| Buying = low and Maint = vhigh and Persons = 4 and Safety = med | acc | 0.002483 |
| Buying = vhigh and Maint = low and Persons = 4 and Safety = med | acc | 0.002707 |
| Buying = high and Maint = high and Persons = 4 and Safety = med | acc | 0.002483 |
| Buying = med and Maint = vhigh and Persons = more and Safety = med | acc | 0.002975 |
| Buying = med and Maint = high and Persons = more and Safety = med | acc | 0.002070 |
| Buying = low and Maint = vhigh and Persons = more and Safety = med | acc | 0.001656 |
| Buying = low and Maint = med and Persons = more and Safety = med | good | 0.002978 |
| Buying = med and Maint = med and Persons = more and Safety = high | vgood | 0.002730 |
| Buying = low and Maint = low and Persons = more and Safety = med | good | 0.002731 |
| Buying = low and Maint = low and Persons = more and Safety = high | vgood | 0.002730 |
| Buying = low and Maint = med and Persons = 4 and Safety = med | acc | 0.002707 |
| Buying = med and Maint = med and Persons = 4 and Safety = high | acc | 0.002707 |
| Buying = low and Maint = low and Persons = 4 and Safety = med | acc | 0.002583 |
| Buying = med and Maint = low and Persons = more and Safety = med | good | 0.002408 |
| Buying = med and Maint = low and Persons = 4 and Safety = med | acc | 0.002483 |
| Buying = low and Maint = med and Persons = more and Safety = high | vgood | 0.002189 |
| Buying = low and Maint = high and Persons = more and Safety = high | vgood | 0.002189 |
| Buying = med and Maint = low and Persons = more and Safety = high | vgood | 0.002189 |
| Buying = low and Maint = high and Persons = 4 and Safety = high | vgood | 0.002189 |
| Buying = low and Maint = med and Persons = 4 and Safety = high | vgood | 0.002189 |
| Buying = med and Maint = low and Persons = 4 and Safety = high | good | 0.001674 |
| Buying = low and Maint = low and Persons = 4 and Safety = high | vgood | 0.001858 |
| Safety = med and Persons = 4 and Buying = med and Maint != med and Lug_boot = med and Maint!=(high) and Safety != low and Lug_boot != small and Doors = 5more | acc | 0.001103 |
| Safety = med and Persons = 4 and Buying = med and Maint != med and Lug_boot = med and Maint!=(high) and Safety != low and Lug_boot != small and Doors = 4 | acc | 0.000414 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Safety = low | unacc | 0.530364 |
| Persons = 2 | unacc | 0.422167 |
| Buying = vhigh and Maint = high | unacc | 0.086614 |
| Maint = vhigh and Buying = high | unacc | 0.086614 |
| Maint = vhigh and Buying = vhigh | unacc | 0.077535 |
| Lug_boot = small and Safety = med and Buying = high | unacc | 0.045267 |
| Safety = med and Lug_boot = small and Buying != vhigh and Maint != vhigh and Maint != high and Doors != 2 | acc | 0.096774 |
| Lug_boot != small and Safety != med and Buying = high | acc | 0.179916 |
| Safety = med and Lug_boot = small and Buying != low and Doors != 2 | unacc | 0.052133 |
| Safety = med and Lug_boot = small and Maint = vhigh | unacc | 0.022005 |
| Safety = med and Lug_boot = big and Buying != low and Maint != low | acc | 0.214286 |
| Safety = med and Doors != 2 and Maint = high and Doors != 3 | acc | 0.103261 |
| Safety = med and Lug_boot = big and Buying != med and Maint != med and Buying != low | acc | 0.088398 |
| Safety = med and Lug_boot = big and Maint != vhigh and Maint = low | good | 0.043750 |
| Safety = med and Doors = 2 and Lug_boot != big and Buying != vhigh and Buying != high and Maint != high and Persons = 4 | acc | 0.040764 |
| Safety = med and Doors = 2 and Lug_boot != big and Lug_boot = small | unacc | 0.035599 |
| Maint = vhigh and Doors != 2 and Safety != med | acc | 0.200000 |
| Buying = vhigh and Doors != 2 and Safety != med | acc | 0.171598 |
| Buying = high and Doors != 2 and Doors != 3 | acc | 0.119497 |
| Lug_boot = big and Safety != med and Buying = low and Doors != 2 | vgood | 0.077295 |
| Buying = high and Doors = 2 and Persons = 4 | unacc | 0.007538 |
| Maint = vhigh and Lug_boot = big | acc | 0.076336 |
| Buying = high and Doors = 2 | unacc | 0.020833 |
| Buying = vhigh and Doors != 2 and Persons = 4 | acc | 0.027119 |
| Maint = vhigh and Persons = 4 | acc | 0.037750 |
| Maint = high and Buying != low and Safety != med and Doors != 2 | acc | 0.122137 |
| Buying = vhigh and Doors = 2 and Lug_boot != med | acc | 0.037815 |
| Safety = med and Maint = high and Buying = low | acc | 0.072581 |
| Lug_boot = big and Safety != med and Doors != 2 | vgood | 0.078014 |
| Lug_boot = big and Safety = med | good | 0.056911 |
| Lug_boot = big and Buying != med | vgood | 0.046512 |
| Doors != 2 and Buying = high and Persons = 4 | unacc | 0.014516 |
| Doors != 2 and Safety = med and Buying != vhigh and Doors != 3 and Buying = med | acc | 0.031211 |
| Doors != 2 and Lug_boot = small and Maint != high and Buying = low | good | 0.097345 |
| Doors != 2 and Safety = med and Buying != low and Buying != med | acc | 0.084656 |
| Doors != 2 and Lug_boot = small and Maint != low | acc | 0.144444 |
| Doors != 2 and Safety != med and Lug_boot != small and Doors != 3 | vgood | 0.170000 |
| Lug_boot != big and Doors != 4 and Doors != 5more and Doors = 2 and Safety = med and Buying != med | unacc | 0.049603 |
| Lug_boot != big and Doors != 4 and Doors != 5more and Doors = 2 and Lug_boot != small and Safety != med and Buying != low | acc | 0.114695 |
| Lug_boot != big and Doors = 2 and Persons != 4 and Lug_boot = small | unacc | 0.140845 |
| Lug_boot != big and Maint = high | acc | 0.076596 |
| Lug_boot != big and Doors != 4 and Doors != 5more and Safety = med and Buying = med | acc | 0.048450 |
| Lug_boot != big and Doors != 3 and Doors != 2 | good | 0.318182 |
| Lug_boot != big and Persons = 4 and Maint = med | acc | 0.064516 |
| Lug_boot != big and Buying = med | good | 0.107143 |
| Buying != med and Maint = low | good | 0.043478 |
| Maint = med | vgood | 0.076555 |
|  | acc | 0.333333 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Safety = high and Buying = low and Lug_boot = big | vgood | 0.007529 |
| Safety = high and Buying = med and Lug_boot = big | vgood | 0.003700 |
| Buying = low and Maint = med and Safety = med | good | 0.003016 |
| Safety = high and Persons = more and Buying = high | acc | 0.017780 |
| Safety = med and Lug_boot = big and Persons = 4 | acc | 0.021130 |
| Safety = med and Persons = more and Lug_boot = big | acc | 0.023396 |
| Persons = 4 and Safety = high | acc | 0.051541 |
| Safety = med and Persons = 4 and Buying = low | acc | 0.011789 |
| Safety = med and Persons = more and Lug_boot = med | acc | 0.012537 |
| Persons = more and Safety = high and Buying = med | acc | 0.012570 |
| Safety = med and Persons = 4 and Buying = med | acc | 0.006508 |
|  | unacc | 0.897035 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

buying|maint|persons|safety|acceptability
---|---|---|---|---
low|low|more|high|vgood
high|low|more|high|acc
vhigh|low|more|high|acc
med|low|more|high|vgood
low|med|more|high|vgood
med|med|more|high|vgood
high|med|more|high|acc
vhigh|med|more|high|acc
low|low|4|high|vgood
med|low|4|high|good
low|high|more|high|vgood
high|high|more|high|acc
high|low|4|high|acc
vhigh|low|4|high|acc
med|high|more|high|acc
vhigh|high|more|high|unacc
med|low|more|med|good
low|med|4|high|vgood
low|vhigh|more|high|acc
high|med|4|high|acc
med|med|4|high|acc
vhigh|low|more|med|unacc
vhigh|med|4|high|acc
med|vhigh|more|high|acc
high|low|more|med|acc
vhigh|vhigh|more|high|unacc
high|vhigh|more|high|unacc
low|low|more|med|good
low|med|more|med|good
med|high|4|high|acc
high|med|more|med|unacc
high|high|4|high|acc
med|med|more|med|acc
low|high|4|high|vgood
vhigh|med|more|med|acc
high|low|2|high|unacc
low|low|2|high|unacc
vhigh|high|4|high|unacc
med|low|2|high|unacc
vhigh|low|2|high|unacc
med|low|4|med|acc
low|low|4|med|acc
high|high|more|med|acc
high|low|4|med|unacc
low|vhigh|4|high|acc
med|vhigh|4|high|acc
low|high|more|med|acc
med|med|2|high|unacc
vhigh|med|2|high|unacc
low|med|2|high|unacc
high|vhigh|4|high|unacc
med|high|more|med|acc
vhigh|vhigh|4|high|unacc
vhigh|high|more|med|unacc
vhigh|low|4|med|acc
high|med|2|high|unacc
low|med|4|med|acc
med|vhigh|more|med|acc
vhigh|med|4|med|unacc
med|med|4|med|acc
high|med|4|med|unacc
high|low|more|low|unacc
high|vhigh|more|med|unacc
vhigh|vhigh|more|med|unacc
low|vhigh|more|med|acc
low|low|more|low|unacc
vhigh|high|2|high|unacc
med|high|2|high|unacc
low|high|2|high|unacc
med|low|more|low|unacc
vhigh|low|more|low|unacc
high|high|2|high|unacc
low|high|4|med|acc
high|low|2|med|unacc
low|vhigh|2|high|unacc
med|med|more|low|unacc
vhigh|vhigh|2|high|unacc
med|low|2|med|unacc
vhigh|high|4|med|unacc
vhigh|med|more|low|unacc
high|med|more|low|unacc
vhigh|low|2|med|unacc
low|low|2|med|unacc
med|vhigh|2|high|unacc
high|vhigh|2|high|unacc
low|med|more|low|unacc
med|high|4|med|unacc
high|high|4|med|acc
low|vhigh|4|med|acc
vhigh|high|more|low|unacc
med|med|2|med|unacc
med|vhigh|4|med|unacc
med|low|4|low|unacc
high|high|more|low|unacc
high|med|2|med|unacc
low|med|2|med|unacc
vhigh|med|2|med|unacc
vhigh|low|4|low|unacc
med|high|more|low|unacc
high|vhigh|4|med|unacc
low|high|more|low|unacc
vhigh|vhigh|4|med|unacc
high|low|4|low|unacc
low|low|4|low|unacc
med|vhigh|more|low|unacc
vhigh|high|2|med|unacc
vhigh|med|4|low|unacc
low|med|4|low|unacc
high|high|2|med|unacc
vhigh|vhigh|more|low|unacc
low|high|2|med|unacc
low|vhigh|more|low|unacc
med|high|2|med|unacc
high|med|4|low|unacc
med|med|4|low|unacc
high|vhigh|more|low|unacc
low|vhigh|2|med|unacc
high|high|4|low|unacc
high|low|2|low|unacc
high|vhigh|2|med|unacc
vhigh|high|4|low|unacc
med|vhigh|2|med|unacc
low|high|4|low|unacc
low|low|2|low|unacc
med|high|4|low|unacc
vhigh|vhigh|2|med|unacc
vhigh|low|2|low|unacc
med|low|2|low|unacc
med|vhigh|4|low|unacc
low|vhigh|4|low|unacc
vhigh|vhigh|4|low|unacc
high|vhigh|4|low|unacc
high|med|2|low|unacc
med|med|2|low|unacc
low|med|2|low|unacc
vhigh|med|2|low|unacc
med|high|2|low|unacc
high|high|2|low|unacc
low|high|2|low|unacc
vhigh|high|2|low|unacc
low|vhigh|2|low|unacc
high|vhigh|2|low|unacc
vhigh|vhigh|2|low|unacc
med|vhigh|2|low|unacc

## JRip

Decision list:

rules | predicted class
---|---
(Safety = high) and (Buying = low) and (Lug_boot = big)|vgood (43.0/21.0)
(Safety = high) and (Buying = med) and (Lug_boot = big)|vgood (41.0/26.0)
(Buying = low) and (Maint = med) and (Safety = med)|good (33.0/21.0)
(Safety = high) and (Persons = more) and (Buying = high)|acc (46.0/15.0)
(Safety = med) and (Lug_boot = big) and (Persons = 4)|acc (55.0/18.0)
(Safety = med) and (Persons = more) and (Lug_boot = big)|acc (55.0/16.0)
(Persons = 4) and (Safety = high)|acc (141.0/55.0)
(Safety = med) and (Persons = 4) and (Buying = low)|acc (20.0/6.0)
(Safety = med) and (Persons = more) and (Lug_boot = med)|acc (49.0/23.0)
(Persons = more) and (Safety = high) and (Buying = med)|acc (29.0/13.0)
(Safety = med) and (Persons = 4) and (Buying = med)|acc (30.0/14.0)
|unacc (1011.0/66.0)


## PART

Decision list:

rules | predicted class
---|---
Safety = low|unacc (524.0)
Persons = 2|unacc (339.0)
Buying = vhigh AND Maint = high|unacc (44.0)
Maint = vhigh AND Buying = high|unacc (44.0)
Maint = vhigh AND Buying = vhigh|unacc (39.0)
Lug_boot = small AND Safety = med AND Buying = high|unacc (22.0)
Safety = med AND Lug_boot = small AND Buying != vhigh AND Maint != vhigh AND Maint != high AND Doors != 2|acc (21.0)
Lug_boot != small AND Safety != med AND Buying = high|acc (43.0)
Safety = med AND Lug_boot = small AND Buying != low AND Doors != 2|unacc (22.0)
Safety = med AND Lug_boot = small AND Maint = vhigh|unacc (9.0)
Safety = med AND Lug_boot = big AND Buying != low AND Maint != low|acc (45.0)
Safety = med AND Doors != 2 AND Maint = high AND Doors != 3|acc (19.0)
Safety = med AND Lug_boot = big AND Buying != med AND Maint != med AND Buying != low|acc (16.0)
Safety = med AND Lug_boot = big AND Maint != vhigh AND Maint = low|good (14.0)
Safety = med AND Doors = 2 AND Lug_boot != big AND Buying != vhigh AND Buying != high AND Maint != high AND Persons = 4|acc (10.0/2.0)
Safety = med AND Doors = 2 AND Lug_boot != big AND Lug_boot = small|unacc (11.0)
Maint = vhigh AND Doors != 2 AND Safety != med|acc (35.0)
Buying = vhigh AND Doors != 2 AND Safety != med|acc (29.0)
Buying = high AND Doors != 2 AND Doors != 3|acc (19.0)
Lug_boot = big AND Safety != med AND Buying = low AND Doors != 2|vgood (16.0)
Buying = high AND Doors = 2 AND Persons = 4|unacc (6.0/3.0)
Maint = vhigh AND Lug_boot = big|acc (10.0)
Buying = high AND Doors = 2|unacc (6.0)
Buying = vhigh AND Doors != 2 AND Persons = 4|acc (5.0/1.0)
Maint = vhigh AND Persons = 4|acc (9.0/2.0)
Maint = high AND Buying != low AND Safety != med AND Doors != 2|acc (16.0)
Buying = vhigh AND Doors = 2 AND Lug_boot != med|acc (8.0/2.0)
Safety = med AND Maint = high AND Buying = low|acc (9.0)
Lug_boot = big AND Safety != med AND Doors != 2|vgood (11.0)
Lug_boot = big AND Safety = med|good (7.0)
Lug_boot = big AND Buying != med|vgood (6.0)
Doors != 2 AND Buying = high AND Persons = 4|unacc (5.0/2.0)
Doors != 2 AND Safety = med AND Buying != vhigh AND Doors != 3 AND Buying = med|acc (9.0/4.0)
Doors != 2 AND Lug_boot = small AND Maint != high AND Buying = low|good (11.0)
Doors != 2 AND Safety = med AND Buying != low AND Buying != med|acc (8.0)
Doors != 2 AND Lug_boot = small AND Maint != low|acc (12.0)
Doors != 2 AND Safety != med AND Lug_boot != small AND Doors != 3|vgood (17.0)
Lug_boot != big AND Doors != 4 AND Doors != 5more AND Doors = 2 AND Safety = med AND Buying != med|unacc (6.0/2.0)
Lug_boot != big AND Doors != 4 AND Doors != 5more AND Doors = 2 AND Lug_boot != small AND Safety != med AND Buying != low|acc (9.0/1.0)
Lug_boot != big AND Doors = 2 AND Persons != 4 AND Lug_boot = small|unacc (8.0)
Lug_boot != big AND Maint = high|acc (9.0/4.0)
Lug_boot != big AND Doors != 4 AND Doors != 5more AND Safety = med AND Buying = med|acc (7.0/2.0)
Lug_boot != big AND Doors != 3 AND Doors != 2|good (10.0)
Lug_boot != big AND Persons = 4 AND Maint = med|acc (6.0/3.0)
Lug_boot != big AND Buying = med|good (6.0/2.0)
Buying != med AND Maint = low|good (6.0/3.0)
Maint = med|vgood (5.0/2.0)
|acc (5.0/2.0)


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
										* Persons!=(more)|(2)
												* Buying=(low)|(vhigh)|(high): good(2.0/0.0)
												* Buying!=(low)|(vhigh)|(high): acc(1.0/1.0)
										* Doors!=(3)|(4)|(5more)
											* Buying=(low)|(vhigh)|(high): good(3.0/0.0)
											* Buying!=(low)|(vhigh)|(high): acc(2.0/1.0)
						* Lug_boot!=(big)|(med)
								* Maint=(low)|(vhigh)|(high)
									* Doors=(5more)|(4)|(3): good(12.0/0.0)
									* Doors!=(5more)|(4)|(3): unacc(2.0/1.0)
								* Maint!=(low)|(vhigh)|(high)
							* Buying=(low)
										* Doors=(5more)|(4)|(3): good(5.0/0.0)
										* Doors!=(5more)|(4)|(3): unacc(1.0/1.0)
							* Buying!=(low)
										* Doors=(5more)|(4)|(3): acc(6.0/0.0)
										* Doors!=(5more)|(4)|(3): unacc(1.0/1.0)
					* Safety!=(high)|(low)
						* Lug_boot=(big)|(med)
						* Buying=(low)
								* Lug_boot=(big)|(small): good(14.0/0.0)
								* Lug_boot!=(big)|(small)
									* Doors=(5more)|(4): good(6.0/0.0)
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
										* Lug_boot!=(big)|(small)
												* Doors=(3)|(4)|(5more): acc(1.0/1.0)
												* Doors!=(3)|(4)|(5more): acc(2.0/0.0)
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
										* Doors!=(5more)|(4)
												* Doors=(3)|(4)|(5more): acc(1.0/1.0)
												* Doors!=(3)|(4)|(5more): acc(2.0/0.0)
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
									* Doors=(5more)|(4): acc(4.0/0.0)
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
							* Lug_boot=(big)|(med)
								* Doors=(5more)|(4): acc(16.0/0.0)
								* Doors!=(5more)|(4)
									* Lug_boot=(big)|(small): acc(8.0/0.0)
									* Lug_boot!=(big)|(small)
										* Safety=(high)|(low): acc(4.0/0.0)
										* Safety!=(high)|(low)
												* Doors=(3)|(4)|(5more): unacc(1.0/1.0)
												* Doors!=(3)|(4)|(5more): unacc(2.0/0.0)
							* Lug_boot!=(big)|(med)
							* Safety=(high)
										* Doors=(5more)|(4)|(3): acc(5.0/0.0)
										* Doors!=(5more)|(4)|(3): unacc(1.0/1.0)
							* Safety!=(high): unacc(8.0/0.0)
							* Maint!=(high)|(med)|(low): unacc(44.0/0.0)
						* Buying!=(high)|(med)|(low): unacc(83.0/0.0)
		* Persons!=(more)|(4): unacc(339.0/0.0)
	* Safety!=(high)|(med): unacc(524.0/0.0)


