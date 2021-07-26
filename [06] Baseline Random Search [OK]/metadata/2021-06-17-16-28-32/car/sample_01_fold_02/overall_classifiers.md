# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Safety != high | unacc | 0.614062 |
| Safety = high and Persons = 2 | unacc | 0.273865 |
| Safety = med and Persons = more and Lug_boot = big | acc | 0.018381 |
| Safety = med and Persons = 4 and Buying = med | acc | 0.013214 |
| Safety = med and Persons = 4 and Buying = low | acc | 0.014986 |
| Safety != med | unacc | 0.592358 |
| Buying = high and Maint = high and Persons = 4 and Safety = high | acc | 0.009836 |
| Buying = med and Maint = vhigh and Persons = 4 and Safety = high | acc | 0.009024 |
| Safety = high and Persons = 4 and Buying = high and Maint = low | acc | 0.009024 |
| Safety = high and Persons = 4 and Buying = med and Maint = high | acc | 0.009024 |
| Safety = high and Persons = more and Buying = med and Maint = vhigh | acc | 0.009024 |
| Safety = high and Persons = 4 and Buying = vhigh and Maint = low | acc | 0.009024 |
| Safety = high and Persons = more and Buying = vhigh and Maint = med | acc | 0.008279 |
| Safety = high and Persons = 4 and Buying = high and Maint = med | acc | 0.008210 |
| Safety = high and Persons = more and Buying = high and Maint = med | acc | 0.007470 |
| Buying = med and Maint = high and Persons = more and Safety = high | acc | 0.008210 |
| Safety = high and Persons = 4 and Buying = low and Maint = vhigh | acc | 0.008210 |
| Safety = high and Persons = more and Buying = vhigh and Maint = low | acc | 0.007470 |
| Buying = vhigh and Maint = med and Persons = 4 and Safety = high | acc | 0.008210 |
| Safety = med and Persons = 4 and Buying = high and Lug_boot = big | acc | 0.005884 |
| Safety = med and Persons = more and Lug_boot = med and Maint = high | acc | 0.005496 |
| Buying = high and Maint = high and Persons = more and Safety = high | acc | 0.007395 |
| Buying = high and Maint = low and Persons = more and Safety = high | acc | 0.007395 |
| Safety = high and Persons = more and Buying = low and Maint = vhigh | acc | 0.006661 |
| Safety = med and Persons = more and Lug_boot = med and Maint = med | acc | 0.005884 |
| Buying = med and Maint = low and Persons = more and Safety = med | good | 0.003273 |
| Buying = med and Maint = low and Persons = more and Safety = high | vgood | 0.003271 |
| Buying = low and Maint = low and Persons = more and Safety = med | good | 0.002978 |
| Safety = med and Persons = more and Lug_boot = med and Maint = low | acc | 0.002132 |
| Safety = high and Persons = more and Buying = med and Maint = med | vgood | 0.002730 |
| Buying = low and Maint = med and Persons = more and Safety = med | good | 0.002191 |
| Buying = low and Maint = med and Persons = more and Safety = high | vgood | 0.002672 |
| Buying = low and Maint = low and Persons = more and Safety = high | vgood | 0.002189 |
| Buying = low and Maint = high and Persons = 4 and Safety = high | acc | 0.002483 |
| Safety = high and Persons = 4 and Buying = low and Maint = low | good | 0.002191 |
| Buying = low and Maint = vhigh and Persons = more and Safety = med | acc | 0.002707 |
| Buying = low and Maint = high and Persons = more and Safety = med | acc | 0.007470 |
| Buying = med and Maint = low and Persons = 4 and Safety = high | vgood | 0.002189 |
| Buying = med and Maint = vhigh and Persons = more and Safety = med | acc | 0.003375 |
| Buying = med and Maint = med and Persons = more and Safety = med | acc | 0.007470 |
| Buying = low and Maint = med and Persons = 4 and Safety = high | vgood | 0.002189 |
| Safety = high and Persons = 4 and Buying = med and Maint = med | acc | 0.002070 |
| Buying = med and Maint = med and Persons = 4 and Safety = high | vgood | 0.001673 |
| Safety = high and Persons = more and Buying = low and Maint = high | vgood | 0.001858 |
| Buying = high and Maint = high and Persons = 4 and Safety = med | acc | 0.002483 |
| Buying = high and Maint = low and Persons = 4 and Safety = med | acc | 0.002707 |
| Safety = med and Persons = 4 and Buying != med and Maint = med and Safety!=(high) and Lug_boot = med and Lug_boot != small and Doors = 5more | acc | 0.001103 |
| Safety = med and Persons = 4 and Buying != med and Maint = med and Safety!=(high) and Lug_boot = med and Lug_boot != small and Doors = 4 | acc | 0.000414 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Safety = low | unacc | 0.529412 |
| Persons = 2 | unacc | 0.417817 |
| Buying = vhigh and Maint = vhigh | unacc | 0.090196 |
| Buying = high and Maint = vhigh | unacc | 0.090196 |
| Safety = med and Lug_boot = small and Buying = high | unacc | 0.047228 |
| Safety = med and Lug_boot = small and Buying = vhigh | unacc | 0.045267 |
| Safety = med and Maint = high and Buying = low | acc | 0.084938 |
| Buying = high and Safety = high | acc | 0.217450 |
| Safety = med and Maint = high and Buying = high | acc | 0.046737 |
| Safety = med and Maint = high and Buying = vhigh | unacc | 0.039063 |
| Safety = med and Lug_boot = big and Buying = vhigh | acc | 0.065116 |
| Safety = med and Lug_boot = big and Buying = high | acc | 0.065116 |
| Safety = med and Lug_boot = big and Maint = vhigh | acc | 0.065116 |
| Safety = med and Lug_boot = big and Buying = low | good | 0.041209 |
| Safety = med and Maint = vhigh and Lug_boot = small | unacc | 0.048780 |
| Buying = vhigh and Maint = med | acc | 0.117361 |
| Safety = med and Lug_boot = big and Maint = high | acc | 0.044944 |
| Maint = vhigh | acc | 0.209555 |
| Safety = med and Maint = high and Lug_boot = small | unacc | 0.034043 |
| Buying = vhigh and Maint = low | acc | 0.117769 |
| Buying = med and Maint = high | acc | 0.121312 |
| Safety = med and Lug_boot = small | acc | 0.117769 |
| Buying = vhigh | unacc | 0.169399 |
| Safety = med and Buying = low | good | 0.030682 |
| Safety = med and Buying = med and Maint = med | acc | 0.096790 |
| Safety = med and Buying = high | acc | 0.025521 |
| Lug_boot = big and Safety = high | vgood | 0.280000 |
| Lug_boot = small and Maint = low | good | 0.094902 |
| Lug_boot = small and Buying = med | acc | 0.046154 |
| Lug_boot = small and Maint = high | acc | 0.084337 |
| Lug_boot = med and Safety = high and Doors = 3 | vgood | 0.037879 |
| Lug_boot = med and Safety = high and Doors = 5more | vgood | 0.131579 |
| Doors = 4 | vgood | 0.082653 |
|  | good | 0.378788 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

buying|maint|persons|safety|acceptability
---|---|---|---|---
vhigh|low|more|high|acc
med|low|more|high|vgood
low|low|more|high|vgood
high|low|more|high|acc
vhigh|med|more|high|acc
med|med|more|high|vgood
high|med|more|high|acc
low|med|more|high|vgood
low|low|4|high|good
high|high|more|high|acc
med|high|more|high|acc
vhigh|low|4|high|acc
high|low|4|high|acc
low|high|more|high|vgood
vhigh|high|more|high|unacc
med|low|4|high|vgood
med|low|more|med|good
med|med|4|high|vgood
high|low|more|med|acc
low|low|more|med|good
low|vhigh|more|high|acc
med|vhigh|more|high|acc
high|med|4|high|acc
vhigh|med|4|high|acc
high|vhigh|more|high|unacc
vhigh|low|more|med|acc
vhigh|vhigh|more|high|unacc
low|med|4|high|vgood
high|low|2|high|unacc
low|high|4|high|acc
med|med|more|med|acc
med|high|4|high|acc
high|high|4|high|acc
low|low|2|high|unacc
vhigh|med|more|med|acc
vhigh|low|2|high|unacc
med|low|2|high|unacc
high|med|more|med|acc
vhigh|high|4|high|unacc
low|med|more|med|good
med|vhigh|4|high|acc
low|med|2|high|unacc
high|vhigh|4|high|unacc
vhigh|low|4|med|unacc
low|vhigh|4|high|acc
high|med|2|high|unacc
high|low|4|med|acc
med|high|more|med|acc
med|low|4|med|acc
low|high|more|med|acc
high|high|more|med|acc
med|med|2|high|unacc
vhigh|vhigh|4|high|unacc
vhigh|med|2|high|unacc
vhigh|high|more|med|unacc
low|low|4|med|acc
med|vhigh|more|med|acc
high|high|2|high|unacc
vhigh|med|4|med|unacc
low|vhigh|more|med|acc
med|high|2|high|unacc
high|low|more|low|unacc
low|med|4|med|acc
med|med|4|med|acc
med|low|more|low|unacc
vhigh|low|more|low|unacc
vhigh|high|2|high|unacc
low|low|more|low|unacc
high|vhigh|more|med|unacc
high|med|4|med|unacc
vhigh|vhigh|more|med|unacc
low|high|2|high|unacc
low|high|4|med|acc
low|med|more|low|unacc
vhigh|vhigh|2|high|unacc
low|vhigh|2|high|unacc
low|low|2|med|unacc
med|vhigh|2|high|unacc
high|low|2|med|unacc
high|high|4|med|acc
med|low|2|med|unacc
vhigh|low|2|med|unacc
med|med|more|low|unacc
high|vhigh|2|high|unacc
vhigh|med|more|low|unacc
med|high|4|med|unacc
high|med|more|low|unacc
vhigh|high|4|med|unacc
vhigh|low|4|low|unacc
vhigh|high|more|low|unacc
med|low|4|low|unacc
low|high|more|low|unacc
vhigh|vhigh|4|med|unacc
high|vhigh|4|med|unacc
high|high|more|low|unacc
low|low|4|low|unacc
med|vhigh|4|med|unacc
high|med|2|med|unacc
low|med|2|med|unacc
med|med|2|med|unacc
vhigh|med|2|med|unacc
high|low|4|low|unacc
low|vhigh|4|med|acc
med|high|more|low|unacc
vhigh|med|4|low|unacc
med|vhigh|more|low|unacc
vhigh|vhigh|more|low|unacc
med|high|2|med|unacc
high|med|4|low|unacc
vhigh|high|2|med|unacc
low|vhigh|more|low|unacc
med|med|4|low|unacc
low|med|4|low|unacc
high|vhigh|more|low|unacc
high|high|2|med|unacc
low|high|2|med|unacc
med|vhigh|2|med|unacc
high|low|2|low|unacc
low|vhigh|2|med|unacc
low|high|4|low|unacc
med|low|2|low|unacc
vhigh|high|4|low|unacc
vhigh|vhigh|2|med|unacc
high|high|4|low|unacc
vhigh|low|2|low|unacc
low|low|2|low|unacc
high|vhigh|2|med|unacc
med|high|4|low|unacc
vhigh|med|2|low|unacc
high|vhigh|4|low|unacc
med|vhigh|4|low|unacc
low|med|2|low|unacc
low|vhigh|4|low|unacc
high|med|2|low|unacc
med|med|2|low|unacc
vhigh|vhigh|4|low|unacc
vhigh|high|2|low|unacc
low|high|2|low|unacc
high|high|2|low|unacc
med|high|2|low|unacc
high|vhigh|2|low|unacc
low|vhigh|2|low|unacc
vhigh|vhigh|2|low|unacc
med|vhigh|2|low|unacc

## PART

Decision list:

rules | predicted class
---|---
Safety = low|unacc (522.0)
Persons = 2|unacc (333.0)
Buying = vhigh AND Maint = vhigh|unacc (46.0)
Buying = high AND Maint = vhigh|unacc (46.0)
Safety = med AND Lug_boot = small AND Buying = high|unacc (23.0)
Safety = med AND Lug_boot = small AND Buying = vhigh|unacc (22.0)
Safety = med AND Maint = high AND Buying = low|acc (22.0/1.0)
Buying = high AND Safety = high|acc (62.0/1.0)
Safety = med AND Maint = high AND Buying = high|acc (16.0/3.0)
Safety = med AND Maint = high AND Buying = vhigh|unacc (15.0)
Safety = med AND Lug_boot = big AND Buying = vhigh|acc (14.0)
Safety = med AND Lug_boot = big AND Buying = high|acc (14.0)
Safety = med AND Lug_boot = big AND Maint = vhigh|acc (14.0)
Safety = med AND Lug_boot = big AND Buying = low|good (15.0)
Safety = med AND Maint = vhigh AND Lug_boot = small|unacc (16.0)
Buying = vhigh AND Maint = med|acc (30.0/4.0)
Safety = med AND Lug_boot = big AND Maint = high|acc (8.0)
Maint = vhigh|acc (58.0/7.0)
Safety = med AND Maint = high AND Lug_boot = small|unacc (7.0)
Buying = vhigh AND Maint = low|acc (29.0/4.0)
Buying = med AND Maint = high|acc (28.0/3.0)
Safety = med AND Lug_boot = small|acc (29.0/4.0)
Buying = vhigh|unacc (23.0)
Safety = med AND Buying = low|good (15.0/6.0)
Safety = med AND Buying = med AND Maint = med|acc (14.0)
Safety = med AND Buying = high|acc (13.0/6.0)
Lug_boot = big AND Safety = high|vgood (35.0)
Lug_boot = small AND Maint = low|good (13.0/2.0)
Lug_boot = small AND Buying = med|acc (7.0/1.0)
Lug_boot = small AND Maint = high|acc (7.0)
Lug_boot = med AND Safety = high AND Doors = 3|vgood (10.0/5.0)
Lug_boot = med AND Safety = high AND Doors = 5more|vgood (10.0)
Doors = 4|vgood (14.0/5.0)
|good (23.0/6.0)


## J48 Decision Tree

* Safety = low: unacc (522.0)
* Safety = med
	* Persons = 2: unacc (158.0)
	* Persons = 4
		* Buying = vhigh: unacc (42.0/9.0)
		* Buying = high
			* Lug_boot = small: unacc (15.0)
			* Lug_boot = med: unacc (15.0/5.0)
			* Lug_boot = big: acc (14.0/4.0)
		* Buying = med: acc (42.0/16.0)
		* Buying = low: acc (46.0/17.0)
	* Persons = more
		* Lug_boot = small: unacc (60.0/13.0)
		* Lug_boot = med
			* Maint = vhigh: unacc (16.0/6.0)
			* Maint = high: acc (15.0/5.0)
			* Maint = med: acc (14.0/4.0)
			* Maint = low: acc (14.0/8.0)
		* Lug_boot = big: acc (61.0/24.0)
* Safety = high
	* Persons = 2: unacc (175.0)
	* Persons = 4
		* Buying = vhigh
			* Maint = vhigh: unacc (11.0)
			* Maint = high: unacc (11.0)
			* Maint = med: acc (10.0)
			* Maint = low: acc (11.0)
		* Buying = high
			* Maint = vhigh: unacc (11.0)
			* Maint = high: acc (12.0)
			* Maint = med: acc (10.0)
			* Maint = low: acc (11.0)
		* Buying = med
			* Maint = vhigh: acc (11.0)
			* Maint = high: acc (11.0)
			* Maint = med: acc (10.0/5.0)
			* Maint = low: vgood (11.0/5.0)
		* Buying = low
			* Maint = vhigh: acc (10.0)
			* Maint = high: acc (12.0/6.0)
			* Maint = med: vgood (11.0/5.0)
			* Maint = low: good (11.0/5.0)
	* Persons = more
		* Buying = vhigh
			* Maint = vhigh: unacc (12.0)
			* Maint = high: unacc (12.0)
			* Maint = med: acc (12.0/1.0)
			* Maint = low: acc (11.0/1.0)
		* Buying = high
			* Maint = vhigh: unacc (12.0)
			* Maint = high: acc (9.0)
			* Maint = med: acc (11.0/1.0)
			* Maint = low: acc (9.0)
		* Buying = med
			* Maint = vhigh: acc (11.0)
			* Maint = high: acc (10.0)
			* Maint = med: vgood (12.0/5.0)
			* Maint = low: vgood (10.0/3.0)
		* Buying = low
			* Maint = vhigh: acc (10.0/1.0)
			* Maint = high: vgood (9.0/4.0)
			* Maint = med: vgood (9.0/3.0)
			* Maint = low: vgood (11.0/5.0)


## SimpleCart Decision Tree

	* Safety=(high)|(med)
		* Persons=(more)|(4)
			* Buying=(low)|(med)
				* Maint=(low)|(med)
				* Safety=(high)
						* Lug_boot=(big)|(med)
							* Doors=(5more)|(4): vgood(29.0/0.0)
							* Doors!=(5more)|(4)
								* Lug_boot=(big)|(small): vgood(15.0/0.0)
								* Lug_boot!=(big)|(small): good(8.0/7.0)
						* Lug_boot!=(big)|(med)
								* Buying=(low)|(vhigh)|(high): good(13.0/1.0)
								* Buying!=(low)|(vhigh)|(high): acc(6.0/6.0)
				* Safety!=(high)
						* Lug_boot=(big)|(med)
						* Maint=(low)
								* Doors=(5more)|(4): good(14.0/0.0)
								* Doors!=(5more)|(4)
									* Lug_boot=(big)|(small): good(7.0/0.0)
									* Lug_boot!=(big)|(small): acc(5.0/2.0)
						* Maint!=(low)
									* Buying=(low)|(vhigh)|(high): good(12.0/3.0)
									* Buying!=(low)|(vhigh)|(high): acc(14.0/0.0)
						* Lug_boot!=(big)|(med): acc(25.0/4.0)
				* Maint!=(low)|(med)
				* Safety=(high)
					* Buying=(low)
								* Maint=(high)|(med)|(low)
								* Lug_boot=(big)|(med): vgood(11.0/3.0)
								* Lug_boot!=(big)|(med): acc(7.0/0.0)
								* Maint!=(high)|(med)|(low): acc(19.0/1.0)
					* Buying!=(low): acc(43.0/0.0)
				* Safety!=(high)
						* Lug_boot=(big)|(med): acc(51.0/9.0)
						* Lug_boot!=(big)|(med)
						* Maint=(high)
									* Buying=(low)|(vhigh)|(high): acc(6.0/1.0)
									* Buying!=(low)|(vhigh)|(high): unacc(7.0/0.0)
						* Maint!=(high): unacc(16.0/0.0)
			* Buying!=(low)|(med)
				* Maint=(low)|(med)
				* Safety=(high): acc(82.0/3.0)
				* Safety!=(high)
						* Lug_boot=(big)|(med)
							* Lug_boot=(big)|(small): acc(28.0/0.0)
							* Lug_boot!=(big)|(small)
								* Doors=(5more)|(4): acc(13.0/0.0)
								* Doors!=(5more)|(4): unacc(12.0/3.0)
						* Lug_boot!=(big)|(med): unacc(30.0/0.0)
				* Maint!=(low)|(med)
				* Maint=(high)
							* Buying=(high)|(med)|(low)
						* Safety=(high): acc(21.0/0.0)
						* Safety!=(high)
								* Lug_boot=(big)|(med): acc(13.0/3.0)
								* Lug_boot!=(big)|(med): unacc(8.0/0.0)
							* Buying!=(high)|(med)|(low): unacc(45.0/0.0)
				* Maint!=(high): unacc(92.0/0.0)
		* Persons!=(more)|(4): unacc(333.0/0.0)
	* Safety!=(high)|(med): unacc(522.0/0.0)


