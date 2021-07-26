# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Persons != 4 | unacc | 0.604612 |
| Persons != more | unacc | 0.601605 |
| Persons != 2 and Safety != low and Buying != low and Buying != med and Maint != vhigh and Lug_boot != small and Maint != high and Lug_boot != med | acc | 0.043582 |
| Persons != 2 and Safety != low and Buying = low and Maint = vhigh | acc | 0.019838 |
| Persons != 2 and Safety != low and Buying != low and Buying = med and Maint != low and Lug_boot != small and Maint != med and Lug_boot != med | acc | 0.025040 |
| Persons != 2 and Safety != low and Buying != low and Buying != med and Maint != vhigh and Lug_boot != small and Maint != high and Lug_boot = med and Safety != med | acc | 0.023463 |
| Persons != 2 and Safety != low and Buying != low and Buying != med and Maint != vhigh and Lug_boot != small and Maint = high and Buying != vhigh | acc | 0.019740 |
| Persons != 2 and Safety != low and Buying != low and Buying != med and Maint != vhigh and Lug_boot = small and Safety != med and Doors != 2 and Maint != high | acc | 0.017101 |
| Persons != 2 and Safety != low and Buying = low and Maint != vhigh and Safety = med and Lug_boot = small | acc | 0.014209 |
| Persons != 2 and Safety != low and Buying = low and Maint != vhigh and Safety != med and Lug_boot != small | vgood | 0.020160 |
| Persons != 2 and Safety != low and Buying = low and Maint != vhigh and Safety = med and Lug_boot != small and Maint = high | acc | 0.011466 |
| Persons != 2 and Safety != low and Buying != low and Buying != med and Maint != vhigh and Lug_boot != small and Maint != high and Lug_boot = med and Safety = med and Doors != 2 and Doors != 3 | acc | 0.011466 |
| Persons != 2 and Safety != low and Buying != low and Buying = med and Maint != low and Lug_boot != small and Maint != med and Lug_boot = med and Safety != med | acc | 0.011466 |
| Persons != 2 and Safety != low and Buying != low and Buying = med and Maint != low and Lug_boot = small and Maint != med and Safety != med | acc | 0.009250 |
| Persons != 2 and Safety != low and Buying = low and Maint != vhigh and Safety = med and Lug_boot != small and Maint != high | good | 0.011455 |
| Persons != 2 and Safety != low and Buying != low and Buying = med and Maint != low and Lug_boot != small and Maint = med | acc | 0.009868 |
| Persons != 2 and Safety != low and Buying != low and Buying = med and Maint != low and Lug_boot = small and Maint = med | acc | 0.007654 |
| Persons != 2 and Safety != low and Buying = low and Maint != vhigh and Safety != med and Lug_boot = small and Maint != high | good | 0.006843 |
| Persons != 2 and Safety != low and Buying != low and Buying = med and Maint = low and Safety = med and Lug_boot = small | acc | 0.005049 |
| Persons != 2 and Safety != low and Buying != low and Buying = med and Maint = low and Safety = med and Lug_boot != small | good | 0.006391 |
| Persons != 2 and Safety != low and Buying != low and Buying != med and Maint != vhigh and Lug_boot = small and Safety != med and Doors != 2 and Maint = high and Buying != vhigh | acc | 0.004946 |
| Persons != 2 and Safety != low and Buying != low and Buying = med and Maint = low and Safety != med and Lug_boot != small | vgood | 0.006189 |
| Persons != 2 and Safety != low and Buying = low and Maint != vhigh and Safety != med and Lug_boot = small and Maint = high | acc | 0.004243 |
| Persons != 2 and Safety != low and Buying != low and Buying != med and Maint != vhigh and Lug_boot = small and Safety != med and Doors = 2 and Persons = 4 | acc | 0.002645 |
| Persons != 2 and Safety != low and Buying != low and Buying = med and Maint = low and Safety != med and Lug_boot = small | good | 0.003433 |
| Persons != 2 and Safety != low and Buying != low and Buying = med and Maint != low and Lug_boot != small and Maint != med and Lug_boot = med and Safety = med and Doors = 4 | acc | 0.003303 |
| Persons != 2 and Safety != low and Buying != low and Buying != med and Maint != vhigh and Lug_boot != small and Maint != high and Lug_boot = med and Safety = med and Doors != 2 and Doors = 3 and Persons != 4 | acc | 0.003303 |
| Buying = med and Maint = med and Persons = more and Safety = high | vgood | 0.001528 |
| Buying = med and Maint = low and Persons = 4 and Safety = med | acc | 0.002709 |
| Buying = med and Maint = high and Persons = more and Safety = med | acc | 0.003377 |
| Buying = med and Maint = vhigh and Persons = more and Safety = med | acc | 0.003377 |
| Buying = low and Maint = low and Persons = 4 and Safety = med | acc | 0.002709 |
| Buying = low and Maint = low and Persons = 4 and Safety = high | good | 0.002009 |
| Buying = med and Maint = low and Persons = 4 and Safety = high | good | 0.001340 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Safety = low | unacc | 0.522634 |
| Persons = 2 | unacc | 0.429975 |
| Buying = vhigh and Maint = med | acc | 0.060731 |
| Buying = vhigh and Maint = vhigh | unacc | 0.090336 |
| Buying = vhigh and Maint = low | acc | 0.070187 |
| Buying = high and Maint = high | acc | 0.074006 |
| Buying = high and Maint = low | acc | 0.071389 |
| Buying = high and Maint = med | acc | 0.075457 |
| Buying = med and Maint = high | acc | 0.074006 |
| Buying = med and Maint = low | good | 0.023491 |
| Buying = med | acc | 0.139355 |
| Buying = high | unacc | 0.303502 |
| Buying = vhigh | unacc | 0.269388 |
| Maint = vhigh | acc | 0.124756 |
| Safety = med | acc | 0.131395 |
| Lug_boot = small | good | 0.033134 |
|  | vgood | 0.417266 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Safety = high and Buying = low and Lug_boot = big and Persons = 4 | vgood | 0.005988 |
| Safety = high and Persons = more and Buying = low | vgood | 0.006097 |
| Safety = high and Buying = med and Maint = low | vgood | 0.002712 |
| Maint = low and Buying = med and Safety = med | good | 0.003121 |
| Buying = low and Persons = 4 and Safety = high | good | 0.002475 |
| Safety = high and Persons = 4 and Maint = low | acc | 0.014129 |
| Persons = more and Safety = high | acc | 0.042734 |
| Safety = med and Persons = more and Lug_boot = big | acc | 0.021080 |
| Safety = med and Persons = 4 and Lug_boot = big | acc | 0.021458 |
| Safety = med and Persons = more and Lug_boot = med | acc | 0.015914 |
| Persons = 4 and Safety = high and Buying = med | acc | 0.018267 |
| Safety = med and Persons = more and Buying = low | acc | 0.002558 |
| Safety = med and Persons = 4 and Buying = low | acc | 0.009704 |
| Maint = med and Persons = 4 and Safety = high | acc | 0.014437 |
| Persons = 4 and Safety = high and Maint = high and Buying = high | acc | 0.009549 |
|  | unacc | 0.918212 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

buying|maint|persons|safety|acceptability
---|---|---|---|---
med|low|more|high|vgood
low|low|more|high|vgood
vhigh|low|more|high|acc
high|low|more|high|acc
vhigh|med|more|high|acc
high|med|more|high|acc
low|med|more|high|vgood
med|med|more|high|vgood
med|low|4|high|good
high|low|4|high|acc
med|high|more|high|acc
low|low|4|high|good
vhigh|high|more|high|unacc
high|high|more|high|acc
low|high|more|high|vgood
vhigh|low|4|high|acc
med|vhigh|more|high|acc
low|vhigh|more|high|acc
low|med|4|high|vgood
low|low|more|med|good
high|vhigh|more|high|unacc
vhigh|vhigh|more|high|unacc
med|med|4|high|acc
high|med|4|high|acc
high|low|more|med|unacc
vhigh|low|more|med|acc
med|low|more|med|good
vhigh|med|4|high|acc
low|low|2|high|unacc
med|low|2|high|unacc
high|med|more|med|unacc
vhigh|med|more|med|acc
vhigh|low|2|high|unacc
vhigh|high|4|high|unacc
high|low|2|high|unacc
low|high|4|high|vgood
med|med|more|med|acc
low|med|more|med|good
high|high|4|high|acc
med|high|4|high|acc
med|high|more|med|acc
high|med|2|high|unacc
low|high|more|med|acc
vhigh|vhigh|4|high|unacc
med|vhigh|4|high|acc
med|low|4|med|acc
high|vhigh|4|high|unacc
low|med|2|high|unacc
vhigh|med|2|high|unacc
vhigh|high|more|med|unacc
med|med|2|high|unacc
high|low|4|med|unacc
low|low|4|med|acc
low|vhigh|4|high|acc
high|high|more|med|acc
vhigh|low|4|med|unacc
med|low|more|low|unacc
vhigh|high|2|high|unacc
med|med|4|med|acc
high|low|more|low|unacc
med|vhigh|more|med|acc
vhigh|vhigh|more|med|unacc
med|high|2|high|unacc
high|vhigh|more|med|unacc
high|high|2|high|unacc
high|med|4|med|acc
low|high|2|high|unacc
vhigh|low|more|low|unacc
low|low|more|low|unacc
vhigh|med|4|med|unacc
low|vhigh|more|med|acc
low|med|4|med|good
med|med|more|low|unacc
vhigh|vhigh|2|high|unacc
high|vhigh|2|high|unacc
high|high|4|med|unacc
low|med|more|low|unacc
med|low|2|med|unacc
high|low|2|med|unacc
vhigh|low|2|med|unacc
vhigh|med|more|low|unacc
med|vhigh|2|high|unacc
low|low|2|med|unacc
vhigh|high|4|med|unacc
low|vhigh|2|high|unacc
med|high|4|med|unacc
high|med|more|low|unacc
low|high|4|med|acc
high|high|more|low|unacc
med|high|more|low|unacc
med|vhigh|4|med|unacc
vhigh|high|more|low|unacc
low|med|2|med|unacc
high|med|2|med|unacc
low|low|4|low|unacc
med|med|2|med|unacc
high|low|4|low|unacc
vhigh|vhigh|4|med|unacc
med|low|4|low|unacc
vhigh|low|4|low|unacc
vhigh|med|2|med|unacc
high|vhigh|4|med|unacc
low|high|more|low|unacc
low|vhigh|4|med|unacc
vhigh|vhigh|more|low|unacc
high|med|4|low|unacc
med|vhigh|more|low|unacc
high|high|2|med|unacc
low|vhigh|more|low|unacc
vhigh|high|2|med|unacc
med|high|2|med|unacc
high|vhigh|more|low|unacc
med|med|4|low|unacc
vhigh|med|4|low|unacc
low|med|4|low|unacc
low|high|2|med|unacc
vhigh|high|4|low|unacc
med|low|2|low|unacc
med|high|4|low|unacc
vhigh|low|2|low|unacc
high|high|4|low|unacc
low|low|2|low|unacc
med|vhigh|2|med|unacc
high|vhigh|2|med|unacc
high|low|2|low|unacc
low|vhigh|2|med|unacc
low|high|4|low|unacc
vhigh|vhigh|2|med|unacc
med|med|2|low|unacc
low|med|2|low|unacc
vhigh|med|2|low|unacc
med|vhigh|4|low|unacc
low|vhigh|4|low|unacc
high|vhigh|4|low|unacc
high|med|2|low|unacc
vhigh|vhigh|4|low|unacc
high|high|2|low|unacc
med|high|2|low|unacc
low|high|2|low|unacc
vhigh|high|2|low|unacc
vhigh|vhigh|2|low|unacc
med|vhigh|2|low|unacc
low|vhigh|2|low|unacc
high|vhigh|2|low|unacc

## JRip

Decision list:

rules | predicted class
---|---
(Safety = high) and (Buying = low) and (Lug_boot = big) and (Persons = 4)|vgood (16.0/4.0)
(Safety = high) and (Persons = more) and (Buying = low)|vgood (44.0/24.0)
(Safety = high) and (Buying = med) and (Maint = low)|vgood (30.0/19.0)
(Maint = low) and (Buying = med) and (Safety = med)|good (32.0/20.0)
(Buying = low) and (Persons = 4) and (Safety = high)|good (30.0/19.0)
(Safety = high) and (Persons = 4) and (Maint = low)|acc (21.0/0.0)
(Persons = more) and (Safety = high)|acc (116.0/45.0)
(Safety = med) and (Persons = more) and (Lug_boot = big)|acc (53.0/17.0)
(Safety = med) and (Persons = 4) and (Lug_boot = big)|acc (55.0/18.0)
(Safety = med) and (Persons = more) and (Lug_boot = med)|acc (55.0/24.0)
(Persons = 4) and (Safety = high) and (Buying = med)|acc (33.0/5.0)
(Safety = med) and (Persons = more) and (Buying = low)|acc (15.0/6.0)
(Safety = med) and (Persons = 4) and (Buying = low)|acc (29.0/9.0)
(Maint = med) and (Persons = 4) and (Safety = high)|acc (22.0/0.0)
(Persons = 4) and (Safety = high) and (Maint = high) and (Buying = high)|acc (11.0/0.0)
|unacc (991.0/19.0)


## PART

Decision list:

rules | predicted class
---|---
Safety = low|unacc (406.0)
Persons = 2|unacc (276.0)
Buying = vhigh AND Maint = med|acc (37.0/11.0)
Buying = vhigh AND Maint = vhigh|unacc (34.0)
Buying = vhigh AND Maint = low|acc (34.0/11.0)
Buying = high AND Maint = high|acc (37.0/11.0)
Buying = high AND Maint = low|acc (37.0/11.0)
Buying = high AND Maint = med|acc (36.0/9.0)
Buying = med AND Maint = high|acc (38.0/11.0)
Buying = med AND Maint = low|good (37.0/20.0)
Buying = med|acc (70.0/20.0)
Buying = high|unacc (34.0)
Buying = vhigh|unacc (32.0)
Maint = vhigh|acc (32.0/8.0)
Safety = med|acc (48.0/19.0)
Lug_boot = small|good (19.0/9.0)
|vgood (36.0/7.0)


## J48 Decision Tree

* Persons = 2: unacc (442.0)
* Persons != 2
	* Safety = low: unacc (280.0)
	* Safety != low
		* Buying = low
			* Maint = vhigh: acc (39.0/10.0)
			* Maint != vhigh
				* Safety = med
					* Lug_boot = small: acc (20.0/3.0)
					* Lug_boot != small
						* Maint = high: acc (7.0)
						* Maint != high: good (25.0/6.0)
				* Safety != med
					* Lug_boot = small
						* Maint = high: acc (4.0/1.0)
						* Maint != high: good (10.0/1.0)
					* Lug_boot != small: vgood (39.0/9.0)
		* Buying != low
			* Buying = med
				* Maint = low
					* Safety = med
						* Lug_boot = small: acc (8.0/1.0)
						* Lug_boot != small: good (11.0/2.0)
					* Safety != med
						* Lug_boot = small: good (6.0/1.0)
						* Lug_boot != small: vgood (12.0/2.0)
				* Maint != low
					* Lug_boot = small
						* Maint = med: acc (11.0/1.0)
						* Maint != med
							* Safety = med: unacc (13.0)
							* Safety != med: acc (10.0/2.0)
					* Lug_boot != small
						* Maint = med: acc (24.0/9.0)
						* Maint != med
							* Lug_boot = med
								* Safety = med
									* Doors = 4: acc (4.0)
									* Doors != 4: unacc (7.0/3.0)
								* Safety != med: acc (12.0)
							* Lug_boot != med: acc (28.0)
			* Buying != med
				* Maint = vhigh: unacc (68.0)
				* Maint != vhigh
					* Lug_boot = small
						* Safety = med: unacc (39.0)
						* Safety != med
							* Doors = 2
								* Persons = 4: acc (4.0/1.0)
								* Persons != 4: unacc (6.0)
							* Doors != 2
								* Maint = high
									* Buying = vhigh: unacc (4.0)
									* Buying != vhigh: acc (5.0)
								* Maint != high: acc (17.0)
					* Lug_boot != small
						* Maint = high
							* Buying = vhigh: unacc (20.0)
							* Buying != vhigh: acc (25.0/2.0)
						* Maint != high
							* Lug_boot = med
								* Safety = med
									* Doors = 2: unacc (6.0)
									* Doors != 2
										* Doors = 3
											* Persons = 4: unacc (3.0)
											* Persons != 4: acc (3.0)
										* Doors != 3: acc (12.0)
								* Safety != med: acc (24.0)
							* Lug_boot != med: acc (47.0)


## SimpleCart Decision Tree

	* Persons=(more)|(4)
		* Safety=(high)|(med)
			* Buying=(low)|(med)
				* Maint=(low)|(med)
				* Safety=(high)
						* Lug_boot=(big)|(med)
							* Lug_boot=(big)|(small): vgood(30.0/0.0)
							* Lug_boot!=(big)|(small)
								* Doors=(5more)|(4): vgood(12.0/0.0)
								* Doors!=(5more)|(4)
										* Buying=(low)|(vhigh)|(high)
											* Doors=(3)|(4)|(5more)
											* Persons=(more)|(2): vgood(2.0/0.0)
											* Persons!=(more)|(2): good(2.0/0.0)
											* Doors!=(3)|(4)|(5more): good(4.0/0.0)
										* Buying!=(low)|(vhigh)|(high)
									* Maint=(low): good(2.0/1.0)
									* Maint!=(low)
												* Doors=(3)|(4)|(5more): acc(1.0/1.0)
												* Doors!=(3)|(4)|(5more): acc(2.0/0.0)
						* Lug_boot!=(big)|(med)
								* Maint=(low)|(vhigh)|(high)
									* Doors=(5more)|(4)|(3): good(11.0/0.0)
									* Doors!=(5more)|(4)|(3)
									* Persons=(more)|(2): unacc(2.0/0.0)
									* Persons!=(more)|(2): good(2.0/0.0)
								* Maint!=(low)|(vhigh)|(high)
									* Buying=(low)|(vhigh)|(high)
										* Doors=(5more)|(4)|(3): good(4.0/0.0)
										* Doors!=(5more)|(4)|(3): unacc(1.0/1.0)
									* Buying!=(low)|(vhigh)|(high)
										* Doors=(5more)|(4)|(3): acc(4.0/0.0)
										* Doors!=(5more)|(4)|(3): unacc(1.0/1.0)
				* Safety!=(high)
						* Lug_boot=(big)|(med)
								* Maint=(low)|(vhigh)|(high)
								* Lug_boot=(big)|(small): good(15.0/0.0)
								* Lug_boot!=(big)|(small)
									* Doors=(5more)|(4): good(6.0/0.0)
									* Doors!=(5more)|(4)
											* Doors=(3)|(4)|(5more)
											* Persons=(more)|(2): good(2.0/0.0)
											* Persons!=(more)|(2): acc(2.0/0.0)
											* Doors!=(3)|(4)|(5more): acc(4.0/0.0)
								* Maint!=(low)|(vhigh)|(high)
							* Buying=(low)
									* Lug_boot=(big)|(small): good(7.0/0.0)
									* Lug_boot!=(big)|(small)
										* Doors=(5more)|(4): good(3.0/0.0)
										* Doors!=(5more)|(4)
												* Doors=(3)|(4)|(5more): acc(1.0/1.0)
												* Doors!=(3)|(4)|(5more): acc(2.0/0.0)
							* Buying!=(low): acc(15.0/0.0)
						* Lug_boot!=(big)|(med)
								* Doors=(5more)|(4)|(3): acc(23.0/0.0)
								* Doors!=(5more)|(4)|(3)
								* Persons=(more)|(2): unacc(4.0/0.0)
								* Persons!=(more)|(2): acc(3.0/0.0)
				* Maint!=(low)|(med)
					* Lug_boot=(big)|(med)
					* Buying=(low)
								* Maint=(high)|(med)|(low)
								* Safety=(high)|(low)
									* Doors=(5more)|(4): vgood(8.0/0.0)
									* Doors!=(5more)|(4)
									* Lug_boot=(big): vgood(3.0/0.0)
									* Lug_boot!=(big)
												* Doors=(3)|(4)|(5more): acc(1.0/1.0)
												* Doors!=(3)|(4)|(5more): acc(2.0/0.0)
								* Safety!=(high)|(low): acc(14.0/0.0)
								* Maint!=(high)|(med)|(low)
									* Doors=(5more)|(4)|(3)
										* Doors=(5more)|(4)|(2): acc(15.0/0.0)
										* Doors!=(5more)|(4)|(2)
										* Persons=(more)|(2): acc(4.0/0.0)
										* Persons!=(more)|(2): acc(2.0/1.0)
									* Doors!=(5more)|(4)|(3)
									* Lug_boot=(big)|(small): acc(3.0/0.0)
									* Lug_boot!=(big)|(small): unacc(2.0/1.0)
					* Buying!=(low)
							* Lug_boot=(big)|(small): acc(31.0/0.0)
							* Lug_boot!=(big)|(small)
								* Doors=(5more)|(4): acc(14.0/0.0)
								* Doors!=(5more)|(4)
								* Safety=(high): acc(6.0/0.0)
								* Safety!=(high)
											* Doors=(3)|(4)|(5more)
											* Persons=(more)|(2): acc(2.0/0.0)
											* Persons!=(more)|(2): unacc(2.0/0.0)
											* Doors!=(3)|(4)|(5more): unacc(4.0/0.0)
					* Lug_boot!=(big)|(med)
					* Safety=(high)
								* Doors=(5more)|(4)|(3): acc(22.0/0.0)
								* Doors!=(5more)|(4)|(3)
							* Persons=(more): unacc(3.0/0.0)
							* Persons!=(more): acc(4.0/0.0)
					* Safety!=(high)
						* Buying=(low)
									* Maint=(high)|(med)|(low)
										* Doors=(5more)|(4)|(3): acc(6.0/0.0)
										* Doors!=(5more)|(4)|(3): unacc(1.0/1.0)
									* Maint!=(high)|(med)|(low): unacc(7.0/0.0)
						* Buying!=(low): unacc(16.0/0.0)
			* Buying!=(low)|(med)
				* Maint=(low)|(med)
					* Lug_boot=(big)|(med)
						* Doors=(5more)|(4): acc(58.0/0.0)
						* Doors!=(5more)|(4)
							* Safety=(high)|(low): acc(28.0/0.0)
							* Safety!=(high)|(low)
							* Lug_boot=(big): acc(12.0/0.0)
							* Lug_boot!=(big)
										* Doors=(3)|(4)|(5more)
										* Persons=(more)|(2): acc(4.0/0.0)
										* Persons!=(more)|(2): unacc(4.0/0.0)
										* Doors!=(3)|(4)|(5more): unacc(8.0/0.0)
					* Lug_boot!=(big)|(med)
					* Safety=(high)
								* Doors=(5more)|(4)|(3): acc(21.0/0.0)
								* Doors!=(5more)|(4)|(3)
								* Persons=(more)|(2): unacc(4.0/0.0)
								* Persons!=(more)|(2): acc(4.0/0.0)
					* Safety!=(high): unacc(30.0/0.0)
				* Maint!=(low)|(med)
						* Buying=(high)|(med)|(low)
							* Maint=(high)|(med)|(low)
							* Lug_boot=(big)|(med)
								* Lug_boot=(big)|(small): acc(15.0/0.0)
								* Lug_boot!=(big)|(small)
									* Safety=(high)|(low): acc(8.0/0.0)
									* Safety!=(high)|(low)
										* Doors=(5more)|(4): acc(3.0/0.0)
										* Doors!=(5more)|(4)
												* Doors=(3)|(4)|(5more): unacc(1.0/1.0)
												* Doors!=(3)|(4)|(5more): unacc(2.0/0.0)
							* Lug_boot!=(big)|(med)
							* Safety=(high): acc(6.0/1.0)
							* Safety!=(high): unacc(8.0/0.0)
							* Maint!=(high)|(med)|(low): unacc(43.0/0.0)
						* Buying!=(high)|(med)|(low): unacc(86.0/0.0)
		* Safety!=(high)|(med): unacc(334.0/0.0)
	* Persons!=(more)|(4): unacc(524.0/0.0)


