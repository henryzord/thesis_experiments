# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | unacc | 0.701223 |
| Persons = 4 and Safety = med and Buying = med and Maint != low | acc | 0.012454 |
| Safety = med and Persons = 4 and Buying = low and Maint = high | acc | 0.009836 |
| Safety = high and Persons = more and Buying = vhigh and Maint = med | acc | 0.008279 |
| Buying = low and Maint = vhigh and Persons = 4 and Safety = high | acc | 0.009024 |
| Buying = med and Maint = high and Persons = more and Safety = high | acc | 0.008279 |
| Safety = high and Persons = 4 and Buying = high and Maint = low | acc | 0.009024 |
| Safety = med and Persons = 4 and Buying = high and Lug_boot = big | acc | 0.007108 |
| Buying = vhigh and Maint = med and Persons = 4 and Safety = high | acc | 0.009024 |
| Safety = high and Persons = more and Buying = high and Maint = low | acc | 0.008279 |
| Buying = high and Maint = high and Persons = more and Safety = high | acc | 0.008279 |
| Safety = med and Persons = more and Buying = low and Maint = high | acc | 0.008279 |
| Buying = high and Maint = med and Persons = more and Safety = high | acc | 0.008279 |
| Buying = med and Maint = vhigh and Persons = more and Safety = high | acc | 0.007470 |
| Safety = high and Persons = more and Buying = vhigh and Maint = low | acc | 0.007470 |
| Safety = med and Persons = more and Buying = med and Maint = med | acc | 0.007470 |
| Buying = high and Maint = med and Persons = 4 and Safety = high | acc | 0.008210 |
| Safety = high and Persons = 4 and Buying = vhigh and Maint = low | acc | 0.008210 |
| Buying = low and Maint = vhigh and Persons = more and Safety = high | acc | 0.007470 |
| Safety = high and Persons = 4 and Buying = med and Maint = high | acc | 0.008210 |
| Safety = med and Persons = more and Buying = high and Lug_boot = big | acc | 0.005884 |
| Safety = med and Persons = more and Buying = high and Lug_boot = med | acc | 0.004774 |
| Buying = med and Maint = vhigh and Persons = 4 and Safety = high | acc | 0.007395 |
| Safety = high and Persons = 4 and Buying = high and Maint = high | acc | 0.007395 |
| Safety = high and Persons = more and Buying = low and Lug_boot = big | vgood | 0.004762 |
| Safety = med and Persons = more and Buying = vhigh and Maint = med | acc | 0.003375 |
| Buying = med and Maint = high and Persons = more and Safety = med | acc | 0.004043 |
| Safety = med and Persons = more and Buying = low and Maint = vhigh | acc | 0.003375 |
| Safety = med and Persons = 4 and Buying = low and Maint = vhigh | acc | 0.002975 |
| Buying = vhigh and Maint = med and Persons = 4 and Safety = med | acc | 0.002483 |
| Buying = vhigh and Maint = low and Persons = 4 and Safety = med | acc | 0.002483 |
| Safety = high and Persons = more and Buying = low and Lug_boot = med | vgood | 0.003289 |
| Safety = med and Persons = more and Buying = med and Maint = vhigh | acc | 0.002975 |
| Buying = med and Maint = low and Persons = more and Safety = med | good | 0.002731 |
| Safety = high and Persons = more and Buying = med and Maint = med | vgood | 0.002976 |
| Buying = low and Maint = med and Persons = more and Safety = med | good | 0.002191 |
| Safety = high and Persons = more and Buying = med and Maint = low | vgood | 0.002406 |
| Buying = low and Maint = low and Persons = 4 and Safety = med | acc | 0.002707 |
| Buying = low and Maint = low and Persons = 4 and Safety = high | good | 0.002191 |
| Buying = low and Maint = med and Persons = 4 and Safety = med | good | 0.002090 |
| Persons = 4 and Safety = med and Buying != med and Maint = med and Lug_boot = med | acc | 0.002070 |
| Buying = vhigh and Maint = low and Persons = more and Safety = med | acc | 0.001242 |
| Buying = med and Maint = low and Persons = 4 and Safety = high | good | 0.002009 |
| Safety = high and Persons = 4 and Buying = med and Maint = low | vgood | 0.002008 |
| Buying = low and Maint = med and Persons = 4 and Safety = high | good | 0.002009 |
| Safety = high and Persons = 4 and Buying = low and Maint = med | vgood | 0.002008 |
| Buying = low and Maint = high and Persons = 4 and Safety = high | acc | 0.002070 |
| Safety = high and Persons = 4 and Buying = med and Maint = med | vgood | 0.002189 |
| Safety = med and Persons = 4 and Buying = med and Maint = low | good | 0.001859 |
| Persons = 4 and Safety = med and Buying = med and Maint != med | acc | 0.006641 |
| Safety = med and Persons = more and Buying = low and Maint = low | acc | 0.001656 |
| Safety = high and Persons = more and Buying = low and Lug_boot = small | acc | 0.001869 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Safety = low | unacc | 0.526531 |
| Persons = 2 | unacc | 0.429975 |
| Buying = vhigh and Maint = vhigh | unacc | 0.093750 |
| Buying = high and Maint = vhigh | unacc | 0.081188 |
| Safety = med and Lug_boot = small and Buying = vhigh | unacc | 0.045267 |
| Safety = med and Lug_boot = small and Buying = high | unacc | 0.045267 |
| Buying = high | acc | 0.297669 |
| Maint = vhigh and Lug_boot = med | acc | 0.090975 |
| Safety = med and Maint = high and Buying = low | acc | 0.095418 |
| Buying = vhigh and Maint = med | acc | 0.130876 |
| Maint = vhigh and Lug_boot = big | acc | 0.118143 |
| Buying = vhigh and Maint = high | unacc | 0.123711 |
| Safety = med and Maint = vhigh | unacc | 0.062500 |
| Safety = med and Lug_boot = small and Maint = low | acc | 0.071854 |
| Safety = med and Maint = high and Lug_boot = med | acc | 0.014663 |
| Safety = med and Lug_boot = small | acc | 0.040053 |
| Safety = med and Buying = low | good | 0.068587 |
| Buying = vhigh | acc | 0.147855 |
| Maint = high and Buying = med | acc | 0.144775 |
| Lug_boot = big and Safety = high | vgood | 0.217391 |
| Lug_boot = big and Maint = med | acc | 0.064815 |
| Lug_boot = small and Maint = low | good | 0.084585 |
| Lug_boot = small and Maint = vhigh | acc | 0.095956 |
| Lug_boot = small and Buying = low and Maint = med | good | 0.056128 |
| Lug_boot = small | acc | 0.060606 |
| Safety = med and Maint = low | good | 0.079823 |
| Safety = high and Doors = 3 | vgood | 0.039063 |
| Safety = high and Doors = 4 | vgood | 0.135135 |
| Safety = high and Doors = 5more | vgood | 0.123288 |
| Safety = high | good | 0.053512 |
|  | acc | 0.339286 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Safety = high and Buying = low and Lug_boot = big | vgood | 0.006535 |
| Safety = high and Buying = med and Maint = med | vgood | 0.003661 |
| Safety = high and Maint = low and Buying = med | vgood | 0.002938 |
| Buying = low and Maint = med and Persons = 4 | good | 0.003223 |
| Maint = low and Buying = low and Persons = 4 | good | 0.002895 |
| Safety = med and Maint = low and Buying = med | good | 0.003125 |
| Safety = high and Persons = more and Buying = med | acc | 0.016213 |
| Persons = 4 and Safety = high | acc | 0.051487 |
| Safety = med and Persons = more and Lug_boot = big | acc | 0.018665 |
| Safety = med and Persons = 4 and Lug_boot = big | acc | 0.026001 |
| Persons = more and Safety = high and Maint = med | acc | 0.012865 |
| Persons = more and Safety = med and Lug_boot = med | acc | 0.018729 |
| Persons = more and Safety = high and Maint = high and Buying = high | acc | 0.008853 |
| Safety = med and Persons = 4 and Buying = low and Maint = high | acc | 0.007036 |
| Persons = more and Safety = high and Maint = low | acc | 0.011743 |
| Safety = med and Persons = 4 and Buying = med | acc | 0.007849 |
| Buying = low and Persons = more and Safety = med | acc | 0.002779 |
| Safety = high and Buying = low and Persons = more | acc | 0.005284 |
|  | unacc | 0.942857 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

buying|maint|persons|safety|acceptability
---|---|---|---|---
vhigh|low|more|high|acc
med|low|more|high|vgood
low|low|more|high|vgood
high|low|more|high|acc
med|med|more|high|vgood
low|med|more|high|vgood
vhigh|med|more|high|acc
high|med|more|high|acc
high|low|4|high|acc
vhigh|low|4|high|acc
vhigh|high|more|high|unacc
med|low|4|high|good
low|low|4|high|good
high|high|more|high|acc
med|high|more|high|acc
low|high|more|high|vgood
med|med|4|high|vgood
med|low|more|med|good
high|med|4|high|acc
low|low|more|med|acc
low|med|4|high|good
med|vhigh|more|high|acc
high|low|more|med|acc
low|vhigh|more|high|acc
vhigh|med|4|high|acc
vhigh|low|more|med|acc
vhigh|vhigh|more|high|unacc
high|vhigh|more|high|unacc
vhigh|high|4|high|unacc
low|low|2|high|unacc
med|med|more|med|acc
low|high|4|high|acc
low|med|more|med|good
med|high|4|high|acc
high|high|4|high|acc
high|med|more|med|acc
vhigh|low|2|high|unacc
high|low|2|high|unacc
med|low|2|high|unacc
vhigh|med|more|med|acc
vhigh|med|2|high|unacc
low|high|more|med|acc
low|vhigh|4|high|acc
med|vhigh|4|high|acc
med|low|4|med|good
low|low|4|med|acc
high|low|4|med|unacc
med|high|more|med|acc
high|high|more|med|unacc
vhigh|high|more|med|unacc
vhigh|vhigh|4|high|unacc
vhigh|low|4|med|acc
med|med|2|high|unacc
high|med|2|high|unacc
low|med|2|high|unacc
high|vhigh|4|high|unacc
high|low|more|low|unacc
med|low|more|low|unacc
med|high|2|high|unacc
high|med|4|med|unacc
low|med|4|med|good
med|med|4|med|acc
med|vhigh|more|med|acc
high|vhigh|more|med|unacc
low|vhigh|more|med|acc
vhigh|low|more|low|unacc
high|high|2|high|unacc
low|high|2|high|unacc
vhigh|vhigh|more|med|unacc
low|low|more|low|unacc
vhigh|high|2|high|unacc
vhigh|med|4|med|acc
med|high|4|med|acc
high|vhigh|2|high|unacc
high|med|more|low|unacc
high|high|4|med|unacc
low|high|4|med|acc
low|low|2|med|unacc
high|low|2|med|unacc
vhigh|med|more|low|unacc
med|low|2|med|unacc
med|med|more|low|unacc
low|med|more|low|unacc
med|vhigh|2|high|unacc
low|vhigh|2|high|unacc
vhigh|vhigh|2|high|unacc
vhigh|low|2|med|unacc
vhigh|high|4|med|unacc
low|med|2|med|unacc
med|vhigh|4|med|acc
vhigh|med|2|med|unacc
med|med|2|med|unacc
vhigh|low|4|low|unacc
high|med|2|med|unacc
low|vhigh|4|med|acc
med|high|more|low|unacc
vhigh|vhigh|4|med|unacc
med|low|4|low|unacc
low|low|4|low|unacc
vhigh|high|more|low|unacc
low|high|more|low|unacc
high|vhigh|4|med|unacc
high|high|more|low|unacc
high|low|4|low|unacc
vhigh|vhigh|more|low|unacc
low|med|4|low|unacc
med|high|2|med|unacc
med|med|4|low|unacc
high|high|2|med|unacc
high|med|4|low|unacc
med|vhigh|more|low|unacc
low|high|2|med|unacc
low|vhigh|more|low|unacc
vhigh|med|4|low|unacc
vhigh|high|2|med|unacc
high|vhigh|more|low|unacc
low|low|2|low|unacc
vhigh|high|4|low|unacc
med|vhigh|2|med|unacc
med|low|2|low|unacc
vhigh|low|2|low|unacc
vhigh|vhigh|2|med|unacc
high|vhigh|2|med|unacc
high|low|2|low|unacc
high|high|4|low|unacc
med|high|4|low|unacc
low|high|4|low|unacc
low|vhigh|2|med|unacc
vhigh|med|2|low|unacc
low|med|2|low|unacc
low|vhigh|4|low|unacc
vhigh|vhigh|4|low|unacc
med|vhigh|4|low|unacc
high|med|2|low|unacc
med|med|2|low|unacc
high|vhigh|4|low|unacc
vhigh|high|2|low|unacc
low|high|2|low|unacc
high|high|2|low|unacc
med|high|2|low|unacc
vhigh|vhigh|2|low|unacc
med|vhigh|2|low|unacc
high|vhigh|2|low|unacc
low|vhigh|2|low|unacc

## JRip

Decision list:

rules | predicted class
---|---
(Safety = high) and (Buying = low) and (Lug_boot = big)|vgood (41.0/21.0)
(Safety = high) and (Buying = med) and (Maint = med)|vgood (31.0/18.0)
(Safety = high) and (Maint = low) and (Buying = med)|vgood (33.0/21.0)
(Buying = low) and (Maint = med) and (Persons = 4)|good (26.0/15.0)
(Maint = low) and (Buying = low) and (Persons = 4)|good (29.0/18.0)
(Safety = med) and (Maint = low) and (Buying = med)|good (32.0/20.0)
(Safety = high) and (Persons = more) and (Buying = med)|acc (23.0/2.0)
(Persons = 4) and (Safety = high)|acc (119.0/36.0)
(Safety = med) and (Persons = more) and (Lug_boot = big)|acc (51.0/18.0)
(Safety = med) and (Persons = 4) and (Lug_boot = big)|acc (48.0/10.0)
(Persons = more) and (Safety = high) and (Maint = med)|acc (32.0/10.0)
(Persons = more) and (Safety = med) and (Lug_boot = med)|acc (53.0/20.0)
(Persons = more) and (Safety = high) and (Maint = high) and (Buying = high)|acc (12.0/1.0)
(Safety = med) and (Persons = 4) and (Buying = low) and (Maint = high)|acc (8.0/0.0)
(Persons = more) and (Safety = high) and (Maint = low)|acc (29.0/8.0)
(Safety = med) and (Persons = 4) and (Buying = med)|acc (18.0/8.0)
(Buying = low) and (Persons = more) and (Safety = med)|acc (15.0/6.0)
(Safety = high) and (Buying = low) and (Persons = more)|acc (15.0/5.0)
|unacc (938.0/14.0)


## PART

Decision list:

rules | predicted class
---|---
Safety = low|unacc (516.0)
Persons = 2|unacc (350.0)
Buying = vhigh AND Maint = vhigh|unacc (48.0)
Buying = high AND Maint = vhigh|unacc (41.0)
Safety = med AND Lug_boot = small AND Buying = vhigh|unacc (22.0)
Safety = med AND Lug_boot = small AND Buying = high|unacc (22.0)
Buying = high|acc (109.0/11.0)
Maint = vhigh AND Lug_boot = med|acc (30.0/5.0)
Safety = med AND Maint = high AND Buying = low|acc (24.0/1.0)
Buying = vhigh AND Maint = med|acc (39.0/4.0)
Maint = vhigh AND Lug_boot = big|acc (28.0)
Buying = vhigh AND Maint = high|unacc (36.0)
Safety = med AND Maint = vhigh|unacc (12.0)
Safety = med AND Lug_boot = small AND Maint = low|acc (14.0/1.0)
Safety = med AND Maint = high AND Lug_boot = med|acc (8.0/3.0)
Safety = med AND Lug_boot = small|acc (17.0/6.0)
Safety = med AND Buying = low|good (25.0/5.0)
Buying = vhigh|acc (32.0/3.0)
Maint = high AND Buying = med|acc (30.0/1.0)
Lug_boot = big AND Safety = high|vgood (35.0)
Lug_boot = big AND Maint = med|acc (7.0)
Lug_boot = small AND Maint = low|good (15.0/2.0)
Lug_boot = small AND Maint = vhigh|acc (13.0/2.0)
Lug_boot = small AND Buying = low AND Maint = med|good (8.0/1.0)
Lug_boot = small|acc (14.0/2.0)
Safety = med AND Maint = low|good (14.0/2.0)
Safety = high AND Doors = 3|vgood (10.0/5.0)
Safety = high AND Doors = 4|vgood (10.0)
Safety = high AND Doors = 5more|vgood (9.0)
Safety = high|good (8.0/3.0)
|acc (7.0)


## J48 Decision Tree

* Safety = low: unacc (516.0)
* Safety = med
	* Persons = 2: unacc (176.0)
	* Persons = 4
		* Buying = vhigh: unacc (47.0/12.0)
		* Buying = high
			* Lug_boot = small: unacc (15.0)
			* Lug_boot = med: unacc (15.0/5.0)
			* Lug_boot = big: acc (14.0/3.0)
		* Buying = med
			* Maint = vhigh: acc (9.0/4.0)
			* Maint = high: acc (10.0/4.0)
			* Maint = med: acc (10.0)
			* Maint = low: good (9.0/4.0)
		* Buying = low
			* Maint = vhigh: acc (10.0/4.0)
			* Maint = high: acc (12.0)
			* Maint = med: good (8.0/3.0)
			* Maint = low: acc (11.0/5.0)
	* Persons = more
		* Buying = vhigh
			* Maint = vhigh: unacc (12.0)
			* Maint = high: unacc (10.0)
			* Maint = med: acc (12.0/5.0)
			* Maint = low: unacc (6.0/3.0)
		* Buying = high
			* Lug_boot = small: unacc (14.0)
			* Lug_boot = med: acc (14.0/5.0)
			* Lug_boot = big: acc (14.0/4.0)
		* Buying = med
			* Maint = vhigh: acc (10.0/4.0)
			* Maint = high: acc (10.0/3.0)
			* Maint = med: acc (11.0/1.0)
			* Maint = low: good (12.0/5.0)
		* Buying = low
			* Maint = vhigh: acc (12.0/5.0)
			* Maint = high: acc (12.0/1.0)
			* Maint = med: good (11.0/5.0)
			* Maint = low: acc (8.0/4.0)
* Safety = high
	* Persons = 2: unacc (174.0)
	* Persons = 4
		* Buying = vhigh
			* Maint = vhigh: unacc (12.0)
			* Maint = high: unacc (11.0)
			* Maint = med: acc (11.0)
			* Maint = low: acc (10.0)
		* Buying = high
			* Maint = vhigh: unacc (11.0)
			* Maint = high: acc (9.0)
			* Maint = med: acc (10.0)
			* Maint = low: acc (11.0)
		* Buying = med
			* Maint = vhigh: acc (9.0)
			* Maint = high: acc (10.0)
			* Maint = med: vgood (11.0/5.0)
			* Maint = low: vgood (12.0/6.0)
		* Buying = low
			* Maint = vhigh: acc (11.0)
			* Maint = high: acc (10.0/5.0)
			* Maint = med: vgood (12.0/6.0)
			* Maint = low: good (11.0/5.0)
	* Persons = more
		* Buying = vhigh
			* Maint = vhigh: unacc (12.0)
			* Maint = high: unacc (11.0)
			* Maint = med: acc (12.0/1.0)
			* Maint = low: acc (11.0/1.0)
		* Buying = high
			* Maint = vhigh: unacc (9.0)
			* Maint = high: acc (12.0/1.0)
			* Maint = med: acc (12.0/1.0)
			* Maint = low: acc (12.0/1.0)
		* Buying = med
			* Maint = vhigh: acc (11.0/1.0)
			* Maint = high: acc (12.0/1.0)
			* Maint = med: vgood (11.0/4.0)
			* Maint = low: vgood (10.0/4.0)
		* Buying = low
			* Lug_boot = small: acc (16.0/10.0)
			* Lug_boot = med: vgood (13.0/5.0)
			* Lug_boot = big: vgood (14.0/4.0)


## SimpleCart Decision Tree

	* Persons=(more)|(4)
		* Safety=(high)|(med)
			* Buying=(low)|(med)
				* Maint=(low)|(med)
					* Safety=(high)|(low)
						* Lug_boot=(big)|(med): vgood(48.0/10.0)
						* Lug_boot!=(big)|(med): good(20.0/10.0)
					* Safety!=(high)|(low)
						* Lug_boot=(big)|(med)
						* Maint=(low): good(21.0/5.0)
						* Maint!=(low)
							* Buying=(low): good(11.0/2.0)
							* Buying!=(low): acc(14.0/0.0)
						* Lug_boot!=(big)|(med): acc(24.0/3.0)
				* Maint!=(low)|(med): acc(130.0/40.0)
			* Buying!=(low)|(med)
				* Maint=(low)|(med)
					* Lug_boot=(big)|(med): acc(104.0/10.0)
					* Lug_boot!=(big)|(med)
						* Safety=(high)|(low): acc(26.0/4.0)
						* Safety!=(high)|(low): unacc(29.0/0.0)
				* Maint!=(low)|(med)
				* Buying=(high)
							* Maint=(high)|(med)|(low): acc(32.0/12.0)
							* Maint!=(high)|(med)|(low): unacc(41.0/0.0)
				* Buying!=(high): unacc(91.0/0.0)
		* Safety!=(high)|(med): unacc(343.0/0.0)
	* Persons!=(more)|(4): unacc(523.0/0.0)


