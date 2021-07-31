# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Persons != 4 | unacc | 0.604958 |
| Persons != more | unacc | 0.600608 |
| Buying = high and Maint = med and Persons = 4 and Safety = high | acc | 0.009836 |
| Buying = low and Maint = vhigh and Persons = 4 and Safety = high | acc | 0.009836 |
| Buying = vhigh and Maint = med and Persons = 4 and Safety = high | acc | 0.009836 |
| Buying = high and Maint = high and Persons = 4 and Safety = high | acc | 0.009024 |
| Buying = low and Maint = high and Persons = 4 and Safety = med | acc | 0.009024 |
| Buying = med and Maint = med and Persons = more and Safety = med | acc | 0.008279 |
| Buying = high and Maint = low and Persons = more and Safety = high | acc | 0.008279 |
| Buying = med and Maint = high and Persons = 4 and Safety = high | acc | 0.009024 |
| Buying = med and Maint = vhigh and Persons = 4 and Safety = high | acc | 0.009024 |
| Buying = high and Maint = low and Persons = 4 and Safety = high | acc | 0.009024 |
| Buying = med and Maint = high and Persons = more and Safety = high | acc | 0.007470 |
| Buying = vhigh and Maint = low and Persons = 4 and Safety = high | acc | 0.008210 |
| Buying = high and Maint = med and Persons = more and Safety = high | acc | 0.007470 |
| Buying = med and Maint = med and Persons = 4 and Safety = med | acc | 0.008210 |
| Buying = low and Maint = high and Persons = more and Safety = med | acc | 0.007470 |
| Buying = vhigh and Maint = low and Persons = more and Safety = high | acc | 0.007470 |
| Buying = vhigh and Maint = med and Persons = more and Safety = high | acc | 0.006661 |
| Buying = high and Maint = high and Persons = more and Safety = high | acc | 0.006661 |
| Buying = low and Maint = vhigh and Persons = more and Safety = high | acc | 0.006661 |
| Buying = med and Maint = vhigh and Persons = more and Safety = high | acc | 0.006661 |
| Buying = high and Maint = low and Persons = more and Safety = med | acc | 0.003678 |
| Buying = vhigh and Maint = low and Persons = more and Safety = med | acc | 0.003375 |
| Buying = high and Maint = high and Persons = more and Safety = med | acc | 0.003375 |
| Buying = med and Maint = vhigh and Persons = more and Safety = med | acc | 0.002975 |
| Buying = low and Maint = vhigh and Persons = more and Safety = med | acc | 0.002975 |
| Buying = high and Maint = med and Persons = more and Safety = med | acc | 0.002975 |
| Buying = vhigh and Maint = med and Persons = 4 and Safety = med | acc | 0.002707 |
| Buying = vhigh and Maint = med and Persons = more and Safety = med | acc | 0.003303 |
| Buying = med and Maint = high and Persons = more and Safety = med | acc | 0.002707 |
| Buying = vhigh and Maint = low and Persons = 4 and Safety = med | acc | 0.002483 |
| Buying = med and Maint = vhigh and Persons = 4 and Safety = med | acc | 0.002298 |
| Buying = low and Maint = high and Persons = more and Safety = high | vgood | 0.002976 |
| Buying = low and Maint = med and Persons = more and Safety = med | good | 0.002674 |
| Buying = low and Maint = low and Persons = more and Safety = med | good | 0.002731 |
| Buying = med and Maint = low and Persons = more and Safety = high | vgood | 0.002672 |
| Buying = low and Maint = low and Persons = more and Safety = high | vgood | 0.002730 |
| Buying = low and Maint = med and Persons = more and Safety = high | vgood | 0.002730 |
| Buying = med and Maint = low and Persons = 4 and Safety = med | acc | 0.002707 |
| Buying = med and Maint = low and Persons = more and Safety = med | good | 0.002408 |
| Buying = low and Maint = high and Persons = 4 and Safety = high | acc | 0.002483 |
| Buying = low and Maint = low and Persons = 4 and Safety = med | good | 0.002090 |
| Buying = med and Maint = low and Persons = 4 and Safety = high | vgood | 0.002189 |
| Buying = low and Maint = med and Persons = 4 and Safety = med | good | 0.002009 |
| Persons = 4 and Safety = med and Buying = med and Maint != med and Lug_boot = med and Maint != low and Doors != 3 and Lug_boot != big | acc | 0.002642 |
| Buying = med and Maint = med and Persons = more and Safety = high | acc | 0.001327 |
| Buying = low and Maint = med and Persons = 4 and Safety = high | good | 0.001674 |
| Buying = med and Maint = med and Persons = 4 and Safety = high | vgood | 0.001673 |
| Buying = low and Maint = low and Persons = 4 and Safety = high | good | 0.001674 |
| Persons = 4 and Safety = med and Buying != med and Maint = med and Lug_boot = med and Doors = 3 and Doors != 2 and Lug_boot != big | acc | 0.000414 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Safety = low | unacc | 0.528455 |
| Persons = 2 | unacc | 0.429975 |
| Buying = vhigh and Maint = low | acc | 0.067409 |
| Buying = vhigh and Maint = vhigh | unacc | 0.092632 |
| Buying = vhigh and Maint = med | acc | 0.081536 |
| Buying = high and Maint = med | acc | 0.081038 |
| Buying = high and Maint = low | acc | 0.081038 |
| Maint = vhigh and Buying = low | acc | 0.077155 |
| Buying = high and Maint = high | acc | 0.077155 |
| Buying = med and Maint = high | acc | 0.074117 |
| Buying = med and Maint = med | acc | 0.068681 |
| Buying = high | unacc | 0.263538 |
| Buying = vhigh | unacc | 0.230189 |
| Safety = med and Lug_boot = small and Buying = low | acc | 0.073658 |
| Maint = vhigh | acc | 0.111744 |
| Safety = med and Maint = high | acc | 0.046534 |
| Safety = med and Lug_boot = big | good | 0.147887 |
| Lug_boot = small | good | 0.049622 |
| Safety = high | vgood | 0.351190 |
|  | good | 0.261905 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Safety = high and Buying = low and Lug_boot = big | vgood | 0.007863 |
| Safety = high and Buying = med and Maint = low | vgood | 0.003028 |
| Buying = low and Maint = med and Safety = med | good | 0.003103 |
| Safety = high and Persons = 4 | acc | 0.053287 |
| Safety = high and Persons = more and Buying = high | acc | 0.018175 |
| Safety = med and Persons = 4 and Buying = med | acc | 0.014068 |
| Persons = more and Safety = med and Maint = med | acc | 0.015618 |
| Safety = med and Persons = 4 and Lug_boot = big | acc | 0.014149 |
| Persons = more and Safety = high and Buying = med | acc | 0.013264 |
| Persons = more and Safety = med and Lug_boot = big | acc | 0.014149 |
| Safety = med and Persons = more and Buying = low | acc | 0.005396 |
|  | unacc | 0.882496 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

buying|maint|persons|safety|acceptability
---|---|---|---|---
low|low|more|high|vgood
med|low|more|high|vgood
vhigh|low|more|high|acc
high|low|more|high|acc
low|med|more|high|vgood
med|med|more|high|acc
high|med|more|high|acc
vhigh|med|more|high|acc
med|low|4|high|vgood
low|low|4|high|good
med|high|more|high|acc
high|high|more|high|acc
high|low|4|high|acc
vhigh|low|4|high|acc
low|high|more|high|vgood
vhigh|high|more|high|unacc
low|med|4|high|good
high|med|4|high|acc
low|low|more|med|good
low|vhigh|more|high|acc
vhigh|med|4|high|acc
med|med|4|high|vgood
med|vhigh|more|high|acc
vhigh|vhigh|more|high|unacc
med|low|more|med|good
high|low|more|med|acc
vhigh|low|more|med|acc
high|vhigh|more|high|unacc
low|high|4|high|acc
vhigh|med|more|med|acc
vhigh|high|4|high|unacc
high|med|more|med|acc
high|low|2|high|unacc
low|med|more|med|good
med|high|4|high|acc
high|high|4|high|acc
vhigh|low|2|high|unacc
med|med|more|med|acc
low|low|2|high|unacc
med|low|2|high|unacc
low|high|more|med|acc
vhigh|med|2|high|unacc
vhigh|vhigh|4|high|unacc
low|low|4|med|good
med|vhigh|4|high|acc
low|vhigh|4|high|acc
med|low|4|med|acc
med|med|2|high|unacc
vhigh|high|more|med|unacc
high|high|more|med|acc
high|low|4|med|unacc
vhigh|low|4|med|acc
low|med|2|high|unacc
med|high|more|med|acc
high|vhigh|4|high|unacc
high|med|2|high|unacc
med|vhigh|more|med|acc
low|med|4|med|good
med|high|2|high|unacc
low|low|more|low|unacc
med|med|4|med|acc
high|med|4|med|unacc
high|high|2|high|unacc
low|vhigh|more|med|acc
vhigh|vhigh|more|med|unacc
vhigh|med|4|med|acc
high|low|more|low|unacc
high|vhigh|more|med|unacc
med|low|more|low|unacc
vhigh|low|more|low|unacc
low|high|2|high|unacc
vhigh|high|2|high|unacc
high|med|more|low|unacc
high|vhigh|2|high|unacc
med|med|more|low|unacc
vhigh|high|4|med|unacc
high|low|2|med|unacc
med|high|4|med|unacc
high|high|4|med|unacc
low|high|4|med|acc
low|vhigh|2|high|unacc
vhigh|vhigh|2|high|unacc
low|med|more|low|unacc
med|vhigh|2|high|unacc
med|low|2|med|unacc
vhigh|med|more|low|unacc
low|low|2|med|unacc
vhigh|low|2|med|unacc
med|high|more|low|unacc
low|high|more|low|unacc
low|vhigh|4|med|unacc
med|med|2|med|unacc
med|vhigh|4|med|acc
vhigh|vhigh|4|med|unacc
med|low|4|low|unacc
high|high|more|low|unacc
low|med|2|med|unacc
vhigh|low|4|low|unacc
low|low|4|low|unacc
high|vhigh|4|med|unacc
vhigh|med|2|med|unacc
vhigh|high|more|low|unacc
high|low|4|low|unacc
high|med|2|med|unacc
vhigh|vhigh|more|low|unacc
high|high|2|med|unacc
med|vhigh|more|low|unacc
low|med|4|low|unacc
low|high|2|med|unacc
med|high|2|med|unacc
vhigh|high|2|med|unacc
vhigh|med|4|low|unacc
low|vhigh|more|low|unacc
high|vhigh|more|low|unacc
med|med|4|low|unacc
high|med|4|low|unacc
high|high|4|low|unacc
vhigh|vhigh|2|med|unacc
high|low|2|low|unacc
low|high|4|low|unacc
high|vhigh|2|med|unacc
med|vhigh|2|med|unacc
low|low|2|low|unacc
med|low|2|low|unacc
vhigh|low|2|low|unacc
low|vhigh|2|med|unacc
vhigh|high|4|low|unacc
med|high|4|low|unacc
vhigh|vhigh|4|low|unacc
med|vhigh|4|low|unacc
low|med|2|low|unacc
high|vhigh|4|low|unacc
vhigh|med|2|low|unacc
low|vhigh|4|low|unacc
high|med|2|low|unacc
med|med|2|low|unacc
low|high|2|low|unacc
vhigh|high|2|low|unacc
high|high|2|low|unacc
med|high|2|low|unacc
med|vhigh|2|low|unacc
vhigh|vhigh|2|low|unacc
high|vhigh|2|low|unacc
low|vhigh|2|low|unacc

## JRip

Decision list:

rules | predicted class
---|---
(Safety = high) and (Buying = low) and (Lug_boot = big)|vgood (45.0/22.0)
(Safety = high) and (Buying = med) and (Maint = low)|vgood (32.0/20.0)
(Buying = low) and (Maint = med) and (Safety = med)|good (32.0/20.0)
(Safety = high) and (Persons = 4)|acc (150.0/53.0)
(Safety = high) and (Persons = more) and (Buying = high)|acc (42.0/12.0)
(Safety = med) and (Persons = 4) and (Buying = med)|acc (41.0/15.0)
(Persons = more) and (Safety = med) and (Maint = med)|acc (31.0/8.0)
(Safety = med) and (Persons = 4) and (Lug_boot = big)|acc (41.0/14.0)
(Persons = more) and (Safety = high) and (Buying = med)|acc (31.0/8.0)
(Persons = more) and (Safety = med) and (Lug_boot = big)|acc (44.0/17.0)
(Safety = med) and (Persons = more) and (Buying = low)|acc (22.0/9.0)
|unacc (1042.0/86.0)


## PART

Decision list:

rules | predicted class
---|---
Safety = low|unacc (520.0)
Persons = 2|unacc (350.0)
Buying = vhigh AND Maint = low|acc (45.0/12.0)
Buying = vhigh AND Maint = vhigh|unacc (44.0)
Buying = vhigh AND Maint = med|acc (42.0/9.0)
Buying = high AND Maint = med|acc (45.0/11.0)
Buying = high AND Maint = low|acc (45.0/11.0)
Maint = vhigh AND Buying = low|acc (42.0/10.0)
Buying = high AND Maint = high|acc (42.0/10.0)
Buying = med AND Maint = high|acc (44.0/12.0)
Buying = med AND Maint = med|acc (42.0/12.0)
Buying = high|unacc (41.0)
Buying = vhigh|unacc (40.0)
Safety = med AND Lug_boot = small AND Buying = low|acc (22.0/3.0)
Maint = vhigh|acc (40.0/9.0)
Safety = med AND Maint = high|acc (14.0)
Safety = med AND Lug_boot = big|good (21.0)
Lug_boot = small|good (34.0/17.0)
Safety = high|vgood (60.0/11.0)
|good (20.0/6.0)


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
								* Persons=(more): vgood(4.0/3.0)
								* Persons!=(more): good(6.0/2.0)
						* Lug_boot!=(big)|(med)
								* Buying=(low)|(vhigh)|(high): good(12.0/2.0)
								* Buying!=(low)|(vhigh)|(high): acc(6.0/7.0)
					* Safety!=(high)|(low)
						* Lug_boot=(big)|(med)
						* Buying=(low)
								* Lug_boot=(big)|(small): good(15.0/0.0)
								* Lug_boot!=(big)|(small): good(9.0/3.0)
						* Buying!=(low)
							* Maint=(low): good(11.0/3.0)
							* Maint!=(low): acc(15.0/0.0)
						* Lug_boot!=(big)|(med)
								* Doors=(5more)|(4)|(3): acc(21.0/0.0)
								* Doors!=(5more)|(4)|(3): unacc(4.0/3.0)
				* Maint!=(low)|(med)
					* Lug_boot=(big)|(med)
							* Maint=(high)|(med)|(low)
								* Buying=(low)|(vhigh)|(high)
								* Safety=(high)|(low)
									* Doors=(5more)|(4): vgood(8.0/0.0)
									* Doors!=(5more)|(4): vgood(5.0/3.0)
								* Safety!=(high)|(low): acc(14.0/0.0)
								* Buying!=(low)|(vhigh)|(high)
								* Doors=(5more)|(4): acc(14.0/0.0)
								* Doors!=(5more)|(4)
									* Safety=(high)|(low): acc(7.0/0.0)
									* Safety!=(high)|(low): acc(4.0/3.0)
							* Maint!=(high)|(med)|(low)
								* Doors=(5more)|(4)|(3): acc(38.0/0.0)
								* Doors!=(5more)|(4)|(3)
								* Lug_boot=(big)|(small): acc(8.0/0.0)
								* Lug_boot!=(big)|(small): acc(4.0/3.0)
					* Lug_boot!=(big)|(med)
						* Safety=(high)|(low)
								* Doors=(5more)|(4)|(3): acc(22.0/0.0)
								* Doors!=(5more)|(4)|(3): unacc(4.0/4.0)
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
								* Lug_boot!=(big)|(small): acc(10.0/3.0)
							* Doors!=(5more)|(4)|(3)
						* Lug_boot=(big): acc(14.0/0.0)
						* Lug_boot!=(big)
								* Safety=(high)|(low): acc(8.0/0.0)
								* Safety!=(high)|(low): unacc(8.0/0.0)
					* Lug_boot!=(big)|(med)
						* Safety=(high)|(low)
								* Doors=(5more)|(4)|(3): acc(24.0/0.0)
								* Doors!=(5more)|(4)|(3): unacc(4.0/4.0)
						* Safety!=(high)|(low): unacc(28.0/0.0)
				* Maint!=(low)|(med)
				* Maint=(high)
							* Buying=(high)|(med)|(low)
							* Lug_boot=(big)|(med)
									* Doors=(5more)|(4)|(3)
										* Doors=(5more)|(4)|(2): acc(14.0/0.0)
										* Doors!=(5more)|(4)|(2): acc(7.0/1.0)
									* Doors!=(5more)|(4)|(3): acc(5.0/2.0)
							* Lug_boot!=(big)|(med): unacc(7.0/6.0)
							* Buying!=(high)|(med)|(low): unacc(40.0/0.0)
				* Maint!=(high): unacc(85.0/0.0)
		* Safety!=(high)|(med): unacc(348.0/0.0)
	* Persons!=(more)|(4): unacc(522.0/0.0)


