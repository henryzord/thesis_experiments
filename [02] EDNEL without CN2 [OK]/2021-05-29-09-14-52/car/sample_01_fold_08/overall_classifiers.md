# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | unacc | 0.701675 |
| Buying = low and Maint = vhigh and Persons = 4 and Safety = high | acc | 0.009844 |
| Buying = high and Maint = med and Persons = 4 and Safety = high | acc | 0.009844 |
| Buying = vhigh and Maint = low and Persons = 4 and Safety = high | acc | 0.009844 |
| Buying = med and Maint = med and Persons = 4 and Safety = med | acc | 0.009844 |
| Buying = vhigh and Maint = med and Persons = 4 and Safety = high | acc | 0.009844 |
| Buying = med and Maint = high and Persons = 4 and Safety = high | acc | 0.009844 |
| Buying = med and Maint = vhigh and Persons = 4 and Safety = high | acc | 0.009844 |
| Buying = high and Maint = low and Persons = 4 and Safety = high | acc | 0.009031 |
| Buying = low and Maint = high and Persons = 4 and Safety = med | acc | 0.009031 |
| Buying = vhigh and Maint = low and Persons = more and Safety = high | acc | 0.008285 |
| Buying = high and Maint = low and Persons = more and Safety = high | acc | 0.007476 |
| Buying = high and Maint = high and Persons = more and Safety = high | acc | 0.007476 |
| Buying = high and Maint = high and Persons = 4 and Safety = high | acc | 0.008217 |
| Buying = low and Maint = vhigh and Persons = more and Safety = high | acc | 0.006667 |
| Buying = high and Maint = med and Persons = more and Safety = high | acc | 0.006667 |
| Buying = low and Maint = high and Persons = more and Safety = med | acc | 0.006667 |
| Buying = med and Maint = med and Persons = more and Safety = med | acc | 0.006667 |
| Buying = med and Maint = high and Persons = more and Safety = high | acc | 0.006667 |
| Buying = med and Maint = vhigh and Persons = more and Safety = high | acc | 0.005858 |
| Buying = vhigh and Maint = med and Persons = more and Safety = high | acc | 0.006584 |
| Buying = high and Maint = med and Persons = more and Safety = med | acc | 0.003681 |
| Buying = high and Maint = low and Persons = more and Safety = med | acc | 0.003377 |
| Buying = low and Maint = vhigh and Persons = 4 and Safety = med | acc | 0.002486 |
| Buying = vhigh and Maint = med and Persons = more and Safety = med | acc | 0.002978 |
| Buying = low and Maint = vhigh and Persons = more and Safety = med | acc | 0.002978 |
| Buying = med and Maint = high and Persons = 4 and Safety = med | acc | 0.002978 |
| Buying = vhigh and Maint = med and Persons = 4 and Safety = med | acc | 0.002486 |
| Buying = med and Maint = vhigh and Persons = 4 and Safety = med | acc | 0.002486 |
| Buying = vhigh and Maint = low and Persons = more and Safety = med | acc | 0.002978 |
| Buying = vhigh and Maint = low and Persons = 4 and Safety = med | acc | 0.002978 |
| Buying = med and Maint = high and Persons = more and Safety = med | acc | 0.002709 |
| Buying = med and Maint = vhigh and Persons = more and Safety = med | acc | 0.002071 |
| Buying = low and Maint = med and Persons = more and Safety = med | good | 0.002980 |
| Buying = low and Maint = high and Persons = more and Safety = high | vgood | 0.002976 |
| Buying = low and Maint = high and Persons = 4 and Safety = high | acc | 0.003306 |
| Buying = low and Maint = low and Persons = more and Safety = high | vgood | 0.002730 |
| Buying = med and Maint = med and Persons = more and Safety = high | vgood | 0.002730 |
| Buying = med and Maint = low and Persons = 4 and Safety = med | acc | 0.002978 |
| Buying = low and Maint = med and Persons = more and Safety = high | vgood | 0.002730 |
| Buying = med and Maint = low and Persons = more and Safety = med | good | 0.002192 |
| Buying = low and Maint = low and Persons = 4 and Safety = med | acc | 0.002709 |
| Buying = med and Maint = low and Persons = more and Safety = high | vgood | 0.002406 |
| Buying = low and Maint = low and Persons = more and Safety = med | good | 0.001676 |
| Buying = low and Maint = med and Persons = 4 and Safety = med | acc | 0.002071 |
| Buying = low and Maint = low and Persons = 4 and Safety = high | vgood | 0.002189 |
| Buying = low and Maint = med and Persons = 4 and Safety = high | good | 0.001676 |
| Buying = med and Maint = med and Persons = 4 and Safety = high | vgood | 0.001858 |
| Buying = med and Maint = low and Persons = 4 and Safety = high | vgood | 0.001522 |
| Safety = med and Persons = 4 and Buying != med and Maint = med and Lug_boot = med and Lug_boot != small and Doors = 5more | acc | 0.001104 |
| Safety = med and Persons = 4 and Buying != med and Maint = med and Lug_boot = med and Lug_boot != small and Doors = 4 | acc | 0.001104 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Safety = low | unacc | 0.532795 |
| Persons = 2 | unacc | 0.422693 |
| Buying = vhigh and Maint = med | acc | 0.067351 |
| Buying = vhigh and Maint = high | unacc | 0.088795 |
| Buying = vhigh and Maint = vhigh | unacc | 0.088795 |
| Buying = vhigh | acc | 0.083401 |
| Buying = high and Maint = vhigh | unacc | 0.100000 |
| Safety = med and Lug_boot = big and Maint = med | acc | 0.050364 |
| Safety = med and Lug_boot = big and Maint = high | acc | 0.074236 |
| Safety = med and Lug_boot = small and Buying = med | unacc | 0.025472 |
| Safety = med and Lug_boot = small and Buying = low | acc | 0.055309 |
| Safety = med and Lug_boot = med | acc | 0.149723 |
| Buying = high and Safety = high | acc | 0.232829 |
| Maint = vhigh | acc | 0.180602 |
| Safety = med and Lug_boot = small | unacc | 0.165010 |
| Maint = high | acc | 0.115741 |
| Safety = high and Lug_boot = med | vgood | 0.128601 |
| Lug_boot = big and Safety = high | vgood | 0.214286 |
|  | good | 0.495868 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Safety = high and Buying = low and Lug_boot = big and Persons = more | vgood | 0.006387 |
| Safety = high and Buying = low and Lug_boot = med and Persons = more | vgood | 0.003384 |
| Safety = high and Buying = med and Maint = low and Persons = more | vgood | 0.002406 |
| Safety = high and Persons = 4 and Buying = low and Lug_boot = big | vgood | 0.003560 |
| Safety = high and Buying = med and Maint = med and Lug_boot = big | vgood | 0.003271 |
| Buying = low and Maint = med and Safety = med and Persons = more | good | 0.003066 |
| Buying = low and Persons = 4 and Maint = med and Safety = high | good | 0.002458 |
| Maint = low and Buying = low and Safety = high and Lug_boot = small | good | 0.002812 |
| Maint = low and Safety = med and Lug_boot = big and Buying = low | good | 0.003066 |
| Maint = low and Buying = med and Safety = med and Lug_boot = big | good | 0.003066 |
| Maint = low and Buying = med and Safety = high and Persons = 4 | good | 0.002255 |
| Safety = high and Persons = 4 | acc | 0.060187 |
| Persons = more and Safety = high | acc | 0.041608 |
| Safety = med and Persons = 4 and Lug_boot = big | acc | 0.022578 |
| Safety = med and Persons = more and Lug_boot = big and Maint = med | acc | 0.009675 |
| Safety = med and Persons = more and Buying = low | acc | 0.013708 |
| Safety = med and Persons = 4 and Buying = low | acc | 0.011774 |
| Safety = med and Persons = more and Lug_boot = big and Maint = low | acc | 0.007055 |
| Safety = med and Buying = med and Persons = 4 | acc | 0.010204 |
| Safety = med and Persons = more and Buying = med | acc | 0.010105 |
| Safety = med and Lug_boot = med and Persons = more and Maint = med | acc | 0.003982 |
| Safety = med and Lug_boot = med and Maint = low and Persons = more | acc | 0.001853 |
|  | unacc | 0.955263 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

buying|maint|persons|safety|acceptability
---|---|---|---|---
low|low|more|high|vgood
med|low|more|high|vgood
vhigh|low|more|high|acc
high|low|more|high|acc
low|med|more|high|vgood
high|med|more|high|acc
med|med|more|high|vgood
vhigh|med|more|high|acc
vhigh|high|more|high|unacc
vhigh|low|4|high|acc
low|low|4|high|vgood
low|high|more|high|vgood
med|low|4|high|vgood
high|high|more|high|acc
high|low|4|high|acc
med|high|more|high|acc
vhigh|low|more|med|acc
med|vhigh|more|high|acc
high|vhigh|more|high|unacc
low|med|4|high|good
low|low|more|med|good
med|med|4|high|vgood
low|vhigh|more|high|acc
vhigh|med|4|high|acc
high|med|4|high|acc
vhigh|vhigh|more|high|unacc
high|low|more|med|acc
med|low|more|med|good
med|med|more|med|acc
low|med|more|med|good
high|med|more|med|acc
vhigh|low|2|high|unacc
high|high|4|high|acc
low|high|4|high|acc
med|high|4|high|acc
vhigh|high|4|high|unacc
vhigh|med|more|med|acc
high|low|2|high|unacc
med|low|2|high|unacc
low|low|2|high|unacc
high|high|more|med|unacc
low|high|more|med|acc
low|vhigh|4|high|acc
vhigh|high|more|med|unacc
low|med|2|high|unacc
low|low|4|med|acc
med|vhigh|4|high|acc
med|low|4|med|acc
high|low|4|med|unacc
med|med|2|high|unacc
vhigh|med|2|high|unacc
high|med|2|high|unacc
vhigh|low|4|med|acc
vhigh|vhigh|4|high|unacc
med|high|more|med|acc
high|vhigh|4|high|unacc
high|high|2|high|unacc
low|med|4|med|acc
low|vhigh|more|med|acc
med|med|4|med|acc
high|med|4|med|unacc
vhigh|vhigh|more|med|unacc
high|low|more|low|unacc
low|high|2|high|unacc
vhigh|med|4|med|acc
low|low|more|low|unacc
vhigh|high|2|high|unacc
high|vhigh|more|med|unacc
vhigh|low|more|low|unacc
med|low|more|low|unacc
med|vhigh|more|med|acc
med|high|2|high|unacc
med|low|2|med|unacc
med|high|4|med|acc
low|vhigh|2|high|unacc
vhigh|vhigh|2|high|unacc
vhigh|low|2|med|unacc
low|high|4|med|acc
vhigh|high|4|med|unacc
high|high|4|med|unacc
vhigh|med|more|low|unacc
med|med|more|low|unacc
high|vhigh|2|high|unacc
med|vhigh|2|high|unacc
low|low|2|med|unacc
low|med|more|low|unacc
high|low|2|med|unacc
high|med|more|low|unacc
vhigh|high|more|low|unacc
med|low|4|low|unacc
low|med|2|med|unacc
high|vhigh|4|med|unacc
med|high|more|low|unacc
vhigh|vhigh|4|med|unacc
high|low|4|low|unacc
high|high|more|low|unacc
med|vhigh|4|med|acc
low|low|4|low|unacc
low|high|more|low|unacc
vhigh|low|4|low|unacc
high|med|2|med|unacc
vhigh|med|2|med|unacc
low|vhigh|4|med|acc
med|med|2|med|unacc
vhigh|vhigh|more|low|unacc
high|high|2|med|unacc
low|med|4|low|unacc
vhigh|high|2|med|unacc
med|high|2|med|unacc
med|vhigh|more|low|unacc
high|vhigh|more|low|unacc
low|high|2|med|unacc
vhigh|med|4|low|unacc
low|vhigh|more|low|unacc
high|med|4|low|unacc
med|med|4|low|unacc
vhigh|vhigh|2|med|unacc
high|low|2|low|unacc
med|vhigh|2|med|unacc
med|high|4|low|unacc
low|high|4|low|unacc
vhigh|high|4|low|unacc
low|vhigh|2|med|unacc
high|high|4|low|unacc
med|low|2|low|unacc
vhigh|low|2|low|unacc
high|vhigh|2|med|unacc
low|low|2|low|unacc
vhigh|vhigh|4|low|unacc
med|med|2|low|unacc
med|vhigh|4|low|unacc
low|med|2|low|unacc
vhigh|med|2|low|unacc
low|vhigh|4|low|unacc
high|med|2|low|unacc
high|vhigh|4|low|unacc
med|high|2|low|unacc
vhigh|high|2|low|unacc
high|high|2|low|unacc
low|high|2|low|unacc
low|vhigh|2|low|unacc
high|vhigh|2|low|unacc
med|vhigh|2|low|unacc
vhigh|vhigh|2|low|unacc

## JRip

Decision list:

rules | predicted class
---|---
(Safety = high) and (Buying = low) and (Lug_boot = big) and (Persons = more)|vgood (15.0/3.0)
(Safety = high) and (Buying = low) and (Lug_boot = med) and (Persons = more)|vgood (16.0/7.0)
(Safety = high) and (Buying = med) and (Maint = low) and (Persons = more)|vgood (10.0/4.0)
(Safety = high) and (Persons = 4) and (Buying = low) and (Lug_boot = big)|vgood (12.0/4.0)
(Safety = high) and (Buying = med) and (Maint = med) and (Lug_boot = big)|vgood (10.0/3.0)
(Buying = low) and (Maint = med) and (Safety = med) and (Persons = more)|good (11.0/4.0)
(Buying = low) and (Persons = 4) and (Maint = med) and (Safety = high)|good (7.0/2.0)
(Maint = low) and (Buying = low) and (Safety = high) and (Lug_boot = small)|good (12.0/5.0)
(Maint = low) and (Safety = med) and (Lug_boot = big) and (Buying = low)|good (11.0/4.0)
(Maint = low) and (Buying = med) and (Safety = med) and (Lug_boot = big)|good (11.0/4.0)
(Maint = low) and (Buying = med) and (Safety = high) and (Persons = 4)|good (11.0/5.0)
(Safety = high) and (Persons = 4)|acc (138.0/39.0)
(Persons = more) and (Safety = high)|acc (122.0/49.0)
(Safety = med) and (Persons = 4) and (Lug_boot = big)|acc (50.0/14.0)
(Safety = med) and (Persons = more) and (Lug_boot = big) and (Maint = med)|acc (11.0/0.0)
(Safety = med) and (Persons = more) and (Buying = low)|acc (27.0/8.0)
(Safety = med) and (Persons = 4) and (Buying = low)|acc (30.0/9.0)
(Safety = med) and (Persons = more) and (Lug_boot = big) and (Maint = low)|acc (8.0/0.0)
(Safety = med) and (Buying = med) and (Persons = 4)|acc (28.0/10.0)
(Safety = med) and (Persons = more) and (Buying = med)|acc (35.0/15.0)
(Safety = med) and (Lug_boot = med) and (Persons = more) and (Maint = med)|acc (8.0/2.0)
(Safety = med) and (Lug_boot = med) and (Maint = low) and (Persons = more)|acc (7.0/2.0)
|unacc (962.0/14.0)


## PART

Decision list:

rules | predicted class
---|---
Safety = low|unacc (350.0)
Persons = 2|unacc (230.0)
Buying = vhigh AND Maint = med|acc (32.0/9.0)
Buying = vhigh AND Maint = high|unacc (31.0)
Buying = vhigh AND Maint = vhigh|unacc (28.0)
Buying = vhigh|acc (27.0/4.0)
Buying = high AND Maint = vhigh|unacc (25.0)
Safety = med AND Lug_boot = big AND Maint = med|acc (17.0/6.0)
Safety = med AND Lug_boot = big AND Maint = high|acc (13.0)
Safety = med AND Lug_boot = small AND Buying = med|unacc (22.0/11.0)
Safety = med AND Lug_boot = small AND Buying = low|acc (18.0/6.0)
Safety = med AND Lug_boot = med|acc (53.0/18.0)
Buying = high AND Safety = high|acc (42.0/3.0)
Maint = vhigh|acc (35.0)
Safety = med AND Lug_boot = small|unacc (15.0)
Maint = high|acc (29.0/8.0)
Safety = high AND Lug_boot = med|vgood (23.0/8.0)
Lug_boot = big AND Safety = high|vgood (18.0)
|good (27.0/6.0)


## SimpleCart Decision Tree

	* Safety=(high)|(med)
		* Persons=(more)|(4)
			* Buying=(low)|(med)
				* Maint=(low)|(med)
					* Safety=(high)|(low)
						* Lug_boot=(big)|(med)
								* Doors=(5more)|(4)|(3): vgood(41.0/3.0)
								* Doors!=(5more)|(4)|(3)
							* Lug_boot=(big): vgood(7.0/0.0)
							* Lug_boot!=(big): good(6.0/2.0)
						* Lug_boot!=(big)|(med)
								* Maint=(low)|(vhigh)|(high): good(14.0/1.0)
								* Maint!=(low)|(vhigh)|(high)
									* Buying=(low)|(vhigh)|(high): good(6.0/1.0)
									* Buying!=(low)|(vhigh)|(high): acc(5.0/1.0)
					* Safety!=(high)|(low)
						* Lug_boot=(big)|(med)
								* Buying=(low)|(vhigh)|(high)
								* Lug_boot=(big)|(small): good(14.0/0.0)
								* Lug_boot!=(big)|(small)
									* Doors=(5more)|(4): good(6.0/0.0)
									* Doors!=(5more)|(4): acc(6.0/2.0)
								* Buying!=(low)|(vhigh)|(high)
							* Maint=(low): good(10.0/3.0)
							* Maint!=(low): acc(14.0/0.0)
						* Lug_boot!=(big)|(med)
								* Doors=(5more)|(4)|(3): acc(22.0/0.0)
								* Doors!=(5more)|(4)|(3)
								* Persons=(more)|(2): unacc(4.0/0.0)
								* Persons!=(more)|(2): acc(4.0/0.0)
				* Maint!=(low)|(med)
					* Lug_boot=(big)|(med)
					* Buying=(low)
						* Maint=(high)
							* Safety=(high)
										* Doors=(5more)|(4)|(3): vgood(9.0/1.0)
										* Doors!=(5more)|(4)|(3): acc(2.0/1.0)
							* Safety!=(high): acc(14.0/0.0)
						* Maint!=(high): acc(27.0/2.0)
					* Buying!=(low)
								* Doors=(5more)|(4)|(3): acc(43.0/1.0)
								* Doors!=(5more)|(4)|(3)
							* Lug_boot=(big): acc(6.0/0.0)
							* Lug_boot!=(big)
								* Safety=(high): acc(3.0/0.0)
								* Safety!=(high): unacc(4.0/0.0)
					* Lug_boot!=(big)|(med)
					* Safety=(high)
								* Doors=(5more)|(4)|(3): acc(20.0/0.0)
								* Doors!=(5more)|(4)|(3)
								* Persons=(more)|(2): unacc(4.0/0.0)
								* Persons!=(more)|(2): acc(4.0/0.0)
					* Safety!=(high)
						* Maint=(high)
									* Buying=(low)|(vhigh)|(high): acc(6.0/1.0)
									* Buying!=(low)|(vhigh)|(high): unacc(7.0/0.0)
						* Maint!=(high): unacc(16.0/0.0)
			* Buying!=(low)|(med)
				* Maint=(low)|(med)
					* Lug_boot=(big)|(med)
						* Lug_boot=(big)|(small): acc(59.0/0.0)
						* Lug_boot!=(big)|(small)
							* Doors=(5more)|(4): acc(29.0/0.0)
							* Doors!=(5more)|(4)
								* Safety=(high)|(low): acc(15.0/0.0)
								* Safety!=(high)|(low)
										* Doors=(3)|(4)|(5more)
										* Persons=(more)|(2): acc(4.0/0.0)
										* Persons!=(more)|(2): unacc(4.0/0.0)
										* Doors!=(3)|(4)|(5more): unacc(7.0/0.0)
					* Lug_boot!=(big)|(med)
						* Safety=(high)|(low)
								* Doors=(5more)|(4)|(3): acc(23.0/0.0)
								* Doors!=(5more)|(4)|(3)
							* Persons=(more): unacc(3.0/0.0)
							* Persons!=(more): acc(4.0/0.0)
						* Safety!=(high)|(low): unacc(27.0/0.0)
				* Maint!=(low)|(med)
				* Maint=(high)
					* Buying=(high)
							* Safety=(high)|(low): acc(20.0/1.0)
							* Safety!=(high)|(low)
								* Lug_boot=(big)|(med)
									* Doors=(5more)|(4): acc(7.0/0.0)
									* Doors!=(5more)|(4): unacc(3.0/1.0)
								* Lug_boot!=(big)|(med): unacc(7.0/0.0)
					* Buying!=(high): unacc(42.0/0.0)
				* Maint!=(high): unacc(86.0/0.0)
		* Persons!=(more)|(4): unacc(339.0/0.0)
	* Safety!=(high)|(med): unacc(528.0/0.0)


