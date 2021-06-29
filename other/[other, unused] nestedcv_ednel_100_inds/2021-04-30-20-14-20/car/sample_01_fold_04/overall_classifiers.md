# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Persons != 4 | unacc | 0.604295 |
| Persons != more | unacc | 0.600269 |
| Persons != 2 and Safety != low and Buying != vhigh and Buying = high and Maint != vhigh and Lug_boot = big | acc | 0.035914 |
| Persons != 2 and Safety != low and Buying = vhigh and Maint != high and Maint != vhigh and Safety != med | acc | 0.032124 |
| Persons != 2 and Safety != low and Buying != vhigh and Buying = high and Maint != vhigh and Lug_boot != big and Safety != med | acc | 0.029111 |
| Persons != 2 and Safety != low and Buying != vhigh and Buying != high and Maint = vhigh and Lug_boot = big | acc | 0.023444 |
| Persons != 2 and Safety != low and Buying != vhigh and Buying != high and Maint = vhigh and Lug_boot != big and Safety != med | acc | 0.020388 |
| Persons != 2 and Safety != low and Buying != vhigh and Buying != high and Maint != vhigh and Safety = med and Maint != high and Lug_boot = small | acc | 0.019512 |
| Persons != 2 and Safety != low and Buying != vhigh and Buying != high and Maint != vhigh and Safety = med and Maint = high and Buying != med | acc | 0.017886 |
| Persons != 2 and Safety != low and Buying = vhigh and Maint != high and Maint != vhigh and Safety = med and Lug_boot != small | acc | 0.014633 |
| Persons != 2 and Safety != low and Buying != vhigh and Buying != high and Maint != vhigh and Safety != med and Lug_boot != small and Maint != high and Lug_boot != med | vgood | 0.019685 |
| Persons != 2 and Safety != low and Buying != vhigh and Buying = high and Maint != vhigh and Lug_boot != big and Safety = med and Lug_boot != small | acc | 0.007722 |
| Persons != 2 and Safety != low and Buying != vhigh and Buying != high and Maint != vhigh and Safety = med and Maint != high and Lug_boot != small and Maint != med | good | 0.013596 |
| Buying = med and Persons = 4 and Safety = med | acc | 0.014227 |
| Buying = med and Persons = more and Safety = med | acc | 0.011842 |
| Persons != 2 and Safety != low and Buying != vhigh and Buying != high and Maint != vhigh and Safety != med and Lug_boot = small and Maint != low and Doors != 2 | acc | 0.011537 |
| Persons != 2 and Safety != low and Buying != vhigh and Buying != high and Maint != vhigh and Safety != med and Lug_boot != small and Maint != high and Lug_boot = med and Doors != 2 | vgood | 0.009582 |
| Persons != 2 and Safety != low and Buying != vhigh and Buying != high and Maint != vhigh and Safety != med and Lug_boot = small and Maint = low | good | 0.006843 |
| Persons != 2 and Safety != low and Buying != vhigh and Buying != high and Maint != vhigh and Safety != med and Lug_boot != small and Maint = high and Buying = med | acc | 0.010647 |
| Persons != 2 and Safety != low and Buying != vhigh and Buying != high and Maint != vhigh and Safety = med and Maint != high and Lug_boot != small and Maint = med and Buying != med | good | 0.004503 |
| Persons != 2 and Safety != low and Buying != vhigh and Buying != high and Maint != vhigh and Safety != med and Lug_boot != small and Maint = high and Buying != med | vgood | 0.006387 |
| Buying = low and Persons = 4 and Safety = med | acc | 0.013603 |
| Persons != 2 and Safety != low and Buying != vhigh and Buying != high and Maint != vhigh and Safety != med and Lug_boot != small and Maint != high and Lug_boot = med and Doors = 2 | good | 0.003006 |
| Buying = low and Persons = more and Safety = med | acc | 0.012828 |
| Buying = med and Persons = 4 and Safety = high | acc | 0.013214 |
| Buying = med and Persons = more and Safety = high | acc | 0.010159 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Persons = 2 | unacc | 0.527976 |
| Safety = low | unacc | 0.425743 |
| Buying = vhigh and Maint = high | unacc | 0.086614 |
| Maint = vhigh and Buying = high | unacc | 0.086614 |
| Buying = vhigh and Maint = vhigh | unacc | 0.084813 |
| Lug_boot = small and Safety = med and Buying != low and Buying != med | unacc | 0.075697 |
| Safety = med and Lug_boot = big and Maint != low and Buying != low | acc | 0.188940 |
| Safety = med and Lug_boot = big and Maint != low and Persons = 4 | acc | 0.027222 |
| Safety = med and Maint = vhigh and Lug_boot != small | acc | 0.048605 |
| Safety = med and Maint != vhigh and Lug_boot = big and Buying != low | acc | 0.051002 |
| Safety = med and Maint = vhigh | unacc | 0.051220 |
| Buying = high and Doors != 2 and Safety != med | acc | 0.240196 |
| Lug_boot = big and Safety != med and Maint != vhigh and Buying != vhigh and Buying = low | vgood | 0.067647 |
| Buying = high and Doors != 2 | acc | 0.086806 |
| Maint = vhigh and Doors != 2 | acc | 0.190184 |
| Maint = high and Buying = low and Safety = med | acc | 0.120000 |
| Buying = vhigh and Doors != 2 and Safety != med | acc | 0.195122 |
| Lug_boot = small and Safety = med and Maint = med | acc | 0.083333 |
| Maint = high and Safety != med and Lug_boot != med and Persons != 4 | acc | 0.055340 |
| Safety = med and Maint != high and Doors != 2 and Buying != vhigh and Lug_boot != small and Buying != med | good | 0.077922 |
| Safety = med and Maint = high | unacc | 0.040441 |
| Buying = vhigh and Doors = 2 | acc | 0.061728 |
| Lug_boot = small and Doors != 2 and Safety != med and Maint != low | acc | 0.077005 |
| Safety = med and Buying = med and Persons != 4 | acc | 0.062825 |
| Lug_boot = small and Persons = 4 and Doors = 2 | acc | 0.061927 |
| Lug_boot = small and Persons != 4 | unacc | 0.057110 |
| Safety = med and Doors != 2 and Buying = vhigh | acc | 0.085911 |
| Buying != high and Safety = med | acc | 0.112360 |
| Buying != high and Maint = low and Persons = 4 | good | 0.136837 |
| Buying != high and Doors != 2 and Maint != high | vgood | 0.211304 |
| Buying != high and Maint = high | acc | 0.177149 |
| Buying != high | acc | 0.127551 |
|  | acc | 0.150943 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Safety = high and Buying = low and Lug_boot = big and Persons = 4 | vgood | 0.006387 |
| Safety = high and Persons = more and Buying = low and Lug_boot = big | vgood | 0.005374 |
| Safety = high and Buying = med and Maint = low | vgood | 0.002938 |
| Safety = high and Maint = med and Buying = med | vgood | 0.002548 |
| Buying = low and Maint = low and Persons = 4 | good | 0.003331 |
| Buying = low and Maint = med and Persons = 4 | good | 0.002898 |
| Maint = low and Safety = med and Buying = med | good | 0.003331 |
| Safety = high and Persons = 4 | acc | 0.057634 |
| Persons = more and Safety = high | acc | 0.042487 |
| Safety = med and Persons = more and Lug_boot = big | acc | 0.021360 |
| Safety = med and Persons = 4 and Lug_boot = big | acc | 0.022664 |
| Safety = med and Lug_boot = med and Persons = more | acc | 0.017529 |
|  | unacc | 0.918212 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

buying|persons|safety|acceptability
---|---|---|---
med|more|high|acc
high|more|high|acc
low|more|high|vgood
vhigh|more|high|unacc
high|4|high|acc
low|4|high|vgood
med|4|high|acc
vhigh|4|high|acc
low|more|med|acc
vhigh|2|high|unacc
high|more|med|unacc
vhigh|more|med|unacc
med|2|high|unacc
med|more|med|acc
low|2|high|unacc
high|2|high|unacc
med|4|med|acc
low|4|med|acc
high|4|med|unacc
vhigh|4|med|unacc
high|2|med|unacc
vhigh|2|med|unacc
med|2|med|unacc
low|2|med|unacc
high|more|low|unacc
low|more|low|unacc
vhigh|more|low|unacc
med|more|low|unacc
vhigh|4|low|unacc
low|4|low|unacc
med|4|low|unacc
high|4|low|unacc
vhigh|2|low|unacc
med|2|low|unacc
high|2|low|unacc
low|2|low|unacc

## JRip

Decision list:

rules | predicted class
---|---
(Safety = high) and (Buying = low) and (Lug_boot = big) and (Persons = 4)|vgood (15.0/3.0)
(Safety = high) and (Persons = more) and (Buying = low) and (Lug_boot = big)|vgood (15.0/4.0)
(Safety = high) and (Buying = med) and (Maint = low)|vgood (33.0/21.0)
(Safety = high) and (Maint = med) and (Buying = med)|vgood (32.0/21.0)
(Buying = low) and (Maint = low) and (Persons = 4)|good (30.0/18.0)
(Buying = low) and (Maint = med) and (Persons = 4)|good (29.0/18.0)
(Maint = low) and (Safety = med) and (Buying = med)|good (30.0/18.0)
(Safety = high) and (Persons = 4)|acc (122.0/33.0)
(Persons = more) and (Safety = high)|acc (134.0/57.0)
(Safety = med) and (Persons = more) and (Lug_boot = big)|acc (50.0/15.0)
(Safety = med) and (Persons = 4) and (Lug_boot = big)|acc (47.0/12.0)
(Safety = med) and (Lug_boot = med) and (Persons = more)|acc (57.0/24.0)
|unacc (959.0/40.0)


## PART

Decision list:

rules | predicted class
---|---
Persons = 2|unacc (519.0)
Safety = low|unacc (344.0)
Buying = vhigh AND Maint = high|unacc (44.0)
Maint = vhigh AND Buying = high|unacc (44.0)
Buying = vhigh AND Maint = vhigh|unacc (43.0)
Lug_boot = small AND Safety = med AND Buying != low AND Buying != med|unacc (38.0)
Safety = med AND Lug_boot = big AND Maint != low AND Buying != low|acc (41.0)
Safety = med AND Lug_boot = big AND Maint != low AND Persons = 4|acc (10.0/3.0)
Safety = med AND Maint = vhigh AND Lug_boot != small|acc (19.0/6.0)
Safety = med AND Maint != vhigh AND Lug_boot = big AND Buying != low|acc (21.0/7.0)
Safety = med AND Maint = vhigh|unacc (15.0)
Buying = high AND Doors != 2 AND Safety != med|acc (49.0)
Lug_boot = big AND Safety != med AND Maint != vhigh AND Buying != vhigh AND Buying = low|vgood (23.0)
Buying = high AND Doors != 2|acc (18.0/3.0)
Maint = vhigh AND Doors != 2|acc (31.0)
Maint = high AND Buying = low AND Safety = med|acc (18.0)
Buying = vhigh AND Doors != 2 AND Safety != med|acc (32.0)
Lug_boot = small AND Safety = med AND Maint = med|acc (12.0)
Maint = high AND Safety != med AND Lug_boot != med AND Persons != 4|acc (13.0/3.0)
Safety = med AND Maint != high AND Doors != 2 AND Buying != vhigh AND Lug_boot != small AND Buying != med|good (18.0/2.0)
Safety = med AND Maint = high|unacc (15.0/5.0)
Buying = vhigh AND Doors = 2|acc (15.0/5.0)
Lug_boot = small AND Doors != 2 AND Safety != med AND Maint != low|acc (17.0/5.0)
Safety = med AND Buying = med AND Persons != 4|acc (11.0/3.0)
Lug_boot = small AND Persons = 4 AND Doors = 2|acc (12.0/3.0)
Lug_boot = small AND Persons != 4|unacc (17.0/8.0)
Safety = med AND Doors != 2 AND Buying = vhigh|acc (12.0/2.0)
Buying != high AND Safety = med|acc (17.0/4.0)
Buying != high AND Maint = low AND Persons = 4|good (15.0/6.0)
Buying != high AND Doors != 2 AND Maint != high|vgood (23.0/1.0)
Buying != high AND Maint = high|acc (18.0/5.0)
Buying != high|acc (17.0/7.0)
|acc (12.0/4.0)


## J48 Decision Tree

* Persons = 2: unacc (519.0)
* Persons != 2
	* Safety = low: unacc (344.0)
	* Safety != low
		* Buying = vhigh
			* Maint = high: unacc (44.0)
			* Maint != high
				* Maint = vhigh: unacc (43.0)
				* Maint != vhigh
					* Safety = med
						* Lug_boot = small: unacc (16.0)
						* Lug_boot != small: acc (27.0/5.0)
					* Safety != med: acc (44.0/2.0)
		* Buying != vhigh
			* Buying = high
				* Maint = vhigh: unacc (44.0)
				* Maint != vhigh
					* Lug_boot = big: acc (45.0)
					* Lug_boot != big
						* Safety = med
							* Lug_boot = small: unacc (22.0)
							* Lug_boot != small: acc (24.0/9.0)
						* Safety != med: acc (42.0/3.0)
			* Buying != high
				* Maint = vhigh
					* Lug_boot = big: acc (29.0)
					* Lug_boot != big
						* Safety = med
							* Lug_boot = small: unacc (15.0)
							* Lug_boot != small: acc (15.0/6.0)
						* Safety != med: acc (29.0/2.0)
				* Maint != vhigh
					* Safety = med
						* Maint = high
							* Buying = med
								* Lug_boot = small: unacc (7.0)
								* Lug_boot != small: acc (12.0/1.0)
							* Buying != med: acc (22.0)
						* Maint != high
							* Lug_boot = small: acc (26.0/1.0)
							* Lug_boot != small
								* Maint = med
									* Buying = med: acc (14.0)
									* Buying != med: good (12.0/3.0)
								* Maint != med: good (28.0/4.0)
					* Safety != med
						* Lug_boot = small
							* Maint = low: good (14.0/2.0)
							* Maint != low
								* Doors = 2: unacc (7.0/3.0)
								* Doors != 2: acc (23.0/5.0)
						* Lug_boot != small
							* Maint = high
								* Buying = med: acc (13.0)
								* Buying != med: vgood (15.0/3.0)
							* Maint != high
								* Lug_boot = med
									* Doors = 2: good (8.0/2.0)
									* Doors != 2: vgood (20.0/3.0)
								* Lug_boot != med: vgood (30.0)


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
								* Doors!=(5more)|(4)
								* Doors=(3)
										* Persons=(more)|(2): vgood(3.0/0.0)
										* Persons!=(more)|(2): good(3.0/0.0)
								* Doors!=(3)
											* Buying=(low)|(vhigh)|(high): good(4.0/0.0)
											* Buying!=(low)|(vhigh)|(high)
												* Maint=(low)|(vhigh)|(high): good(2.0/0.0)
												* Maint!=(low)|(vhigh)|(high): acc(2.0/0.0)
						* Lug_boot!=(big)|(med)
						* Buying=(low)
									* Doors=(5more)|(4)|(3): good(10.0/0.0)
									* Doors!=(5more)|(4)|(3)
									* Persons=(more)|(2): unacc(2.0/0.0)
									* Persons!=(more)|(2): good(2.0/0.0)
						* Buying!=(low)
							* Maint=(low)
										* Doors=(5more)|(4)|(3): good(5.0/0.0)
										* Doors!=(5more)|(4)|(3): unacc(1.0/1.0)
							* Maint!=(low)
										* Doors=(5more)|(4)|(3): acc(6.0/0.0)
										* Doors!=(5more)|(4)|(3): unacc(1.0/1.0)
					* Safety!=(high)|(low)
						* Lug_boot=(big)|(med)
								* Maint=(low)|(vhigh)|(high)
								* Doors=(5more)|(4): good(15.0/0.0)
								* Doors!=(5more)|(4)
									* Lug_boot=(big)|(small): good(7.0/0.0)
									* Lug_boot!=(big)|(small)
										* Persons=(more)|(2): good(2.0/1.0)
										* Persons!=(more)|(2): acc(3.0/0.0)
								* Maint!=(low)|(vhigh)|(high)
							* Buying=(low)
									* Doors=(5more)|(4): good(6.0/0.0)
									* Doors!=(5more)|(4)
										* Lug_boot=(big)|(small): good(3.0/0.0)
										* Lug_boot!=(big)|(small): acc(3.0/0.0)
							* Buying!=(low): acc(14.0/0.0)
						* Lug_boot!=(big)|(med)
								* Doors=(5more)|(4)|(3): acc(21.0/0.0)
								* Doors!=(5more)|(4)|(3): acc(4.0/1.0)
				* Maint!=(low)|(med)
					* Lug_boot=(big)|(med)
							* Buying=(low)|(vhigh)|(high)
							* Safety=(high)|(low)
									* Maint=(high)|(med)|(low)
									* Doors=(5more)|(4): vgood(7.0/0.0)
									* Doors!=(5more)|(4)
										* Lug_boot=(big)|(small): vgood(4.0/0.0)
										* Lug_boot!=(big)|(small)
												* Doors=(3)|(4)|(5more): acc(1.0/1.0)
												* Doors!=(3)|(4)|(5more): acc(2.0/0.0)
									* Maint!=(high)|(med)|(low): acc(14.0/0.0)
							* Safety!=(high)|(low)
									* Maint=(high)|(med)|(low): acc(15.0/0.0)
									* Maint!=(high)|(med)|(low)
									* Lug_boot=(big)|(small): acc(7.0/0.0)
									* Lug_boot!=(big)|(small)
										* Doors=(5more)|(4): acc(3.0/0.0)
										* Doors!=(5more)|(4)
												* Doors=(3)|(4)|(5more): unacc(1.0/1.0)
												* Doors!=(3)|(4)|(5more): unacc(2.0/0.0)
							* Buying!=(low)|(vhigh)|(high)
							* Doors=(5more)|(4): acc(29.0/0.0)
							* Doors!=(5more)|(4)
								* Safety=(high)|(low): acc(13.0/0.0)
								* Safety!=(high)|(low)
									* Lug_boot=(big)|(small): acc(7.0/0.0)
									* Lug_boot!=(big)|(small)
										* Persons=(more)|(2): acc(2.0/1.0)
										* Persons!=(more)|(2): unacc(3.0/0.0)
					* Lug_boot!=(big)|(med)
						* Safety=(high)|(low)
								* Doors=(5more)|(4)|(3): acc(23.0/0.0)
								* Doors!=(5more)|(4)|(3)
								* Persons=(more)|(2): unacc(4.0/0.0)
								* Persons!=(more)|(2): acc(3.0/0.0)
						* Safety!=(high)|(low)
						* Buying=(low)
									* Maint=(high)|(med)|(low): acc(7.0/0.0)
									* Maint!=(high)|(med)|(low): unacc(7.0/0.0)
						* Buying!=(low): unacc(15.0/0.0)
			* Buying!=(low)|(med)
				* Maint=(low)|(med)
					* Lug_boot=(big)|(med)
						* Doors=(5more)|(4): acc(58.0/0.0)
						* Doors!=(5more)|(4)
							* Safety=(high)|(low): acc(28.0/0.0)
							* Safety!=(high)|(low)
							* Lug_boot=(big): acc(13.0/0.0)
							* Lug_boot!=(big)
										* Doors=(3)|(4)|(5more)
										* Persons=(more)|(2): acc(4.0/0.0)
										* Persons!=(more)|(2): unacc(4.0/0.0)
										* Doors!=(3)|(4)|(5more): unacc(7.0/0.0)
					* Lug_boot!=(big)|(med)
						* Safety=(high)|(low)
								* Doors=(5more)|(4)|(3): acc(23.0/0.0)
								* Doors!=(5more)|(4)|(3)
								* Persons=(more)|(2): unacc(4.0/0.0)
								* Persons!=(more)|(2): acc(4.0/0.0)
						* Safety!=(high)|(low): unacc(31.0/0.0)
				* Maint!=(low)|(med)
						* Buying=(high)|(med)|(low)
							* Maint=(high)|(med)|(low)
							* Lug_boot=(big)|(med)
									* Doors=(5more)|(4)|(3)
										* Doors=(5more)|(4)|(2): acc(16.0/0.0)
										* Doors!=(5more)|(4)|(2)
										* Persons=(more)|(2): acc(4.0/0.0)
										* Persons!=(more)|(2)
											* Lug_boot=(big)|(small): acc(2.0/0.0)
											* Lug_boot!=(big)|(small): unacc(1.0/1.0)
									* Doors!=(5more)|(4)|(3)
									* Lug_boot=(big)|(small): acc(3.0/0.0)
									* Lug_boot!=(big)|(small): unacc(2.0/1.0)
							* Lug_boot!=(big)|(med)
								* Safety=(high)|(low)
										* Doors=(5more)|(4)|(3): acc(5.0/0.0)
										* Doors!=(5more)|(4)|(3): unacc(1.0/1.0)
								* Safety!=(high)|(low): unacc(7.0/0.0)
							* Maint!=(high)|(med)|(low): unacc(44.0/0.0)
						* Buying!=(high)|(med)|(low): unacc(87.0/0.0)
		* Safety!=(high)|(med): unacc(344.0/0.0)
	* Persons!=(more)|(4): unacc(519.0/0.0)


