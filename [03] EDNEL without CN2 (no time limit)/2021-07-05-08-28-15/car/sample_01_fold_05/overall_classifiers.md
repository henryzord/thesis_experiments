# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Persons != 4 | unacc | 0.602865 |
| Persons != more | unacc | 0.602530 |
| Persons = 4 and Safety = high | acc | 0.042202 |
| Persons = more and Safety = med | acc | 0.033685 |
| Persons = 4 and Safety = med | acc | 0.030681 |
| Persons = more and Safety = high | acc | 0.036399 |
| Safety = high and Persons = more and Buying = low and Maint = high | vgood | 0.002976 |
| Safety = high and Persons = more and Buying = med and Maint = med | vgood | 0.002730 |
| Safety = high and Persons = 4 and Buying = low and Maint = med | good | 0.002192 |
| Safety = high and Persons = more and Buying = low and Maint = low | vgood | 0.002976 |
| Safety = high and Persons = more and Buying = med and Maint = low | vgood | 0.002089 |
| Safety = high and Persons = 4 and Buying = low and Maint = low | vgood | 0.002008 |
| Safety = high and Persons = more and Buying = low and Maint = med | vgood | 0.001673 |
| Safety = high and Persons = 4 and Buying = med and Maint = low | vgood | 0.001673 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Safety = low | unacc | 0.523663 |
| Persons = 2 | unacc | 0.431204 |
| Buying = vhigh and Maint = vhigh | unacc | 0.088583 |
| Buying = high and Maint = vhigh | unacc | 0.088583 |
| Safety = med and Lug_boot = small and Buying = vhigh | unacc | 0.045361 |
| Safety = med and Lug_boot = small and Buying = high | unacc | 0.043388 |
| Buying = high and Doors = 5more | acc | 0.115702 |
| Safety = med and Maint = high and Buying = vhigh | unacc | 0.031180 |
| Safety = med and Lug_boot = big and Maint = high | acc | 0.090909 |
| Buying = high and Doors = 4 | acc | 0.111111 |
| Safety = med and Lug_boot = big and Buying = vhigh | acc | 0.069767 |
| Safety = med and Lug_boot = big and Maint = vhigh | acc | 0.065421 |
| Safety = med and Lug_boot = big and Buying = low | good | 0.035264 |
| Safety = med and Maint = vhigh and Lug_boot = small | unacc | 0.041436 |
| Buying = high and Lug_boot = big | acc | 0.095238 |
| Buying = high and Safety = high and Persons = more | acc | 0.028000 |
| Maint = vhigh and Safety = high and Doors = 2 | acc | 0.041369 |
| Buying = high and Safety = med | unacc | 0.012658 |
| Buying = vhigh and Maint = high | unacc | 0.065672 |
| Safety = med and Lug_boot = small and Maint = low and Persons = 4 | acc | 0.052980 |
| Safety = med and Maint = med and Buying = med and Lug_boot = med | acc | 0.052980 |
| Safety = med and Lug_boot = small and Buying = low and Persons = more | acc | 0.039312 |
| Safety = med and Maint = high and Buying = low | acc | 0.065904 |
| Safety = med and Maint = high and Lug_boot = med | acc | 0.027397 |
| Safety = med and Maint = vhigh and Persons = 4 | unacc | 0.007353 |
| Safety = med and Maint = med and Buying = med | acc | 0.079943 |
| Safety = high and Lug_boot = big and Buying = vhigh | acc | 0.085526 |
| Safety = med and Lug_boot = small and Persons = 4 | unacc | 0.008130 |
| Lug_boot = big and Safety = high and Maint = med | vgood | 0.064103 |
| Buying = vhigh and Doors = 2 | unacc | 0.012987 |
| Maint = vhigh and Safety = high | acc | 0.209150 |
| Buying = vhigh and Safety = high | acc | 0.185714 |
| Lug_boot = big and Safety = high and Buying = low | vgood | 0.093567 |
| Maint = high and Lug_boot = small and Persons = more | acc | 0.028549 |
| Maint = high and Buying = med | acc | 0.126224 |
| Safety = med and Lug_boot = med and Buying = vhigh | acc | 0.070130 |
| Lug_boot = big and Safety = med | good | 0.064220 |
| Lug_boot = small and Buying = low and Maint = med | good | 0.036594 |
| Lug_boot = small and Maint = low and Buying = med | good | 0.024510 |
| Lug_boot = small and Maint = med | acc | 0.098495 |
| Safety = med and Maint = low | good | 0.035854 |
| Lug_boot = small | acc | 0.051020 |
| Safety = high and Doors = 2 | good | 0.029167 |
| Safety = high and Buying = med and Persons = 4 | vgood | 0.077778 |
| Safety = high and Persons = more | vgood | 0.127363 |
| Maint = med | good | 0.026596 |
|  | acc | 0.437500 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Safety = high and Lug_boot = big and Buying = low and Persons = 4 | vgood | 0.006839 |
| Safety = high and Persons = more and Buying = low and Lug_boot = big | vgood | 0.005374 |
| Safety = high and Buying = med and Maint = med and Lug_boot = big | vgood | 0.003560 |
| Safety = high and Maint = low and Buying = med and Lug_boot = big | vgood | 0.002976 |
| Safety = high and Lug_boot = med and Buying = low and Persons = more | vgood | 0.003289 |
| Safety = high and Persons = 4 and Buying = high and Maint = low | acc | 0.009386 |
| Safety = high and Persons = 4 and Buying = med and Maint = vhigh | acc | 0.010230 |
| Persons = more and Safety = high | acc | 0.043602 |
| Safety = high and Persons = 4 and Maint = med | acc | 0.016396 |
| Safety = med and Persons = more and Lug_boot = big | acc | 0.022580 |
| Persons = 4 and Safety = med and Lug_boot = big | acc | 0.017598 |
| Safety = high and Persons = 4 and Maint = high | acc | 0.014764 |
| Safety = med and Lug_boot = med and Persons = more and Maint = med | acc | 0.006906 |
| Safety = med and Persons = 4 and Buying = low | acc | 0.009288 |
| Safety = med and Persons = more and Buying = low | acc | 0.006316 |
| Persons = 4 and Safety = high and Buying = vhigh and Maint = low | acc | 0.009386 |
| Safety = med and Persons = 4 and Buying = med and Maint = med | acc | 0.006843 |
|  | unacc | 0.904485 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

persons|safety|acceptability
---|---|---
4|high|acc
2|high|unacc
more|high|acc
2|med|unacc
more|med|acc
4|med|acc
2|low|unacc
4|low|unacc
more|low|unacc

## JRip

Decision list:

rules | predicted class
---|---
(Safety = high) and (Lug_boot = big) and (Buying = low) and (Persons = 4)|vgood (14.0/2.0)
(Safety = high) and (Persons = more) and (Buying = low) and (Lug_boot = big)|vgood (15.0/4.0)
(Safety = high) and (Buying = med) and (Maint = med) and (Lug_boot = big)|vgood (12.0/4.0)
(Safety = high) and (Maint = low) and (Buying = med) and (Lug_boot = big)|vgood (11.0/4.0)
(Safety = high) and (Lug_boot = med) and (Buying = low) and (Persons = more)|vgood (13.0/5.0)
(Safety = high) and (Persons = 4) and (Buying = high) and (Maint = low)|acc (11.0/0.0)
(Safety = high) and (Persons = 4) and (Buying = med) and (Maint = vhigh)|acc (12.0/0.0)
(Persons = more) and (Safety = high)|acc (137.0/57.0)
(Safety = high) and (Persons = 4) and (Maint = med)|acc (35.0/9.0)
(Safety = med) and (Persons = more) and (Lug_boot = big)|acc (60.0/20.0)
(Persons = 4) and (Safety = med) and (Lug_boot = big)|acc (56.0/22.0)
(Safety = high) and (Persons = 4) and (Maint = high)|acc (39.0/13.0)
(Safety = med) and (Lug_boot = med) and (Persons = more) and (Maint = med)|acc (15.0/4.0)
(Safety = med) and (Persons = 4) and (Buying = low)|acc (30.0/10.0)
(Safety = med) and (Persons = more) and (Buying = low)|acc (26.0/10.0)
(Persons = 4) and (Safety = high) and (Buying = vhigh) and (Maint = low)|acc (11.0/0.0)
(Safety = med) and (Persons = 4) and (Buying = med) and (Maint = med)|acc (8.0/0.0)
|unacc (1047.0/59.0)


## PART

Decision list:

rules | predicted class
---|---
Safety = low|unacc (509.0)
Persons = 2|unacc (351.0)
Buying = vhigh AND Maint = vhigh|unacc (45.0)
Buying = high AND Maint = vhigh|unacc (45.0)
Safety = med AND Lug_boot = small AND Buying = vhigh|unacc (22.0)
Safety = med AND Lug_boot = small AND Buying = high|unacc (21.0)
Buying = high AND Doors = 5more|acc (28.0)
Safety = med AND Maint = high AND Buying = vhigh|unacc (14.0)
Safety = med AND Lug_boot = big AND Maint = high|acc (20.0)
Buying = high AND Doors = 4|acc (25.0)
Safety = med AND Lug_boot = big AND Buying = vhigh|acc (15.0)
Safety = med AND Lug_boot = big AND Maint = vhigh|acc (14.0)
Safety = med AND Lug_boot = big AND Buying = low|good (14.0)
Safety = med AND Maint = vhigh AND Lug_boot = small|unacc (15.0)
Buying = high AND Lug_boot = big|acc (18.0)
Buying = high AND Safety = high AND Persons = more|acc (10.0/3.0)
Maint = vhigh AND Safety = high AND Doors = 2|acc (11.0/2.0)
Buying = high AND Safety = med|unacc (9.0/3.0)
Buying = vhigh AND Maint = high|unacc (22.0)
Safety = med AND Lug_boot = small AND Maint = low AND Persons = 4|acc (8.0)
Safety = med AND Maint = med AND Buying = med AND Lug_boot = med|acc (8.0)
Safety = med AND Lug_boot = small AND Buying = low AND Persons = more|acc (11.0/3.0)
Safety = med AND Maint = high AND Buying = low|acc (11.0)
Safety = med AND Maint = high AND Lug_boot = med|acc (8.0/3.0)
Safety = med AND Maint = vhigh AND Persons = 4|unacc (8.0/4.0)
Safety = med AND Maint = med AND Buying = med|acc (14.0/1.0)
Safety = high AND Lug_boot = big AND Buying = vhigh|acc (13.0)
Safety = med AND Lug_boot = small AND Persons = 4|unacc (8.0/4.0)
Lug_boot = big AND Safety = high AND Maint = med|vgood (15.0)
Buying = vhigh AND Doors = 2|unacc (12.0/6.0)
Maint = vhigh AND Safety = high|acc (32.0)
Buying = vhigh AND Safety = high|acc (20.0)
Lug_boot = big AND Safety = high AND Buying = low|vgood (16.0)
Maint = high AND Lug_boot = small AND Persons = more|acc (11.0/5.0)
Maint = high AND Buying = med|acc (19.0)
Safety = med AND Lug_boot = med AND Buying = vhigh|acc (11.0/2.0)
Lug_boot = big AND Safety = med|good (7.0)
Lug_boot = small AND Buying = low AND Maint = med|good (8.0/1.0)
Lug_boot = small AND Maint = low AND Buying = med|good (10.0/5.0)
Lug_boot = small AND Maint = med|acc (9.0/1.0)
Safety = med AND Maint = low|good (14.0/6.0)
Lug_boot = small|acc (14.0/7.0)
Safety = high AND Doors = 2|good (13.0/7.0)
Safety = high AND Buying = med AND Persons = 4|vgood (7.0/1.0)
Safety = high AND Persons = more|vgood (15.0)
Maint = med|good (9.0/4.0)
|acc (13.0/6.0)


## J48 Decision Tree

* Safety = low: unacc (509.0)
* Safety = med
	* Persons = 2: unacc (173.0)
	* Persons = 4
		* Buying = vhigh: unacc (43.0/10.0)
		* Buying = high
			* Lug_boot = small: unacc (15.0)
			* Lug_boot = med: unacc (13.0/5.0)
			* Lug_boot = big: acc (14.0/4.0)
		* Buying = med: acc (47.0/18.0)
		* Buying = low: acc (43.0/17.0)
	* Persons = more
		* Lug_boot = small: unacc (54.0/12.0)
		* Lug_boot = med
			* Buying = vhigh: unacc (16.0/6.0)
			* Buying = high: unacc (12.0/6.0)
			* Buying = med: acc (14.0/4.0)
			* Buying = low: acc (14.0/5.0)
		* Lug_boot = big: acc (60.0/20.0)
* Safety = high
	* Persons = 2: unacc (178.0)
	* Persons = 4
		* Buying = vhigh
			* Maint = vhigh: unacc (12.0)
			* Maint = high: unacc (12.0)
			* Maint = med: acc (9.0)
			* Maint = low: acc (11.0)
		* Buying = high
			* Maint = vhigh: unacc (12.0)
			* Maint = high: acc (10.0)
			* Maint = med: acc (11.0)
			* Maint = low: acc (11.0)
		* Buying = med
			* Maint = vhigh: acc (12.0)
			* Maint = high: acc (11.0)
			* Maint = med: acc (12.0/6.0)
			* Maint = low: vgood (10.0/5.0)
		* Buying = low
			* Maint = vhigh: acc (9.0)
			* Maint = high: acc (10.0/5.0)
			* Maint = med: good (11.0/5.0)
			* Maint = low: vgood (12.0/6.0)
	* Persons = more
		* Buying = vhigh
			* Maint = vhigh: unacc (12.0)
			* Maint = high: unacc (10.0)
			* Maint = med: acc (10.0/1.0)
			* Maint = low: acc (11.0/1.0)
		* Buying = high
			* Maint = vhigh: unacc (10.0)
			* Maint = high: acc (10.0/1.0)
			* Maint = med: acc (12.0/1.0)
			* Maint = low: acc (11.0/1.0)
		* Buying = med
			* Maint = vhigh: acc (11.0/1.0)
			* Maint = high: acc (12.0/1.0)
			* Maint = med: vgood (12.0/5.0)
			* Maint = low: vgood (8.0/3.0)
		* Buying = low
			* Maint = vhigh: acc (11.0/1.0)
			* Maint = high: vgood (11.0/4.0)
			* Maint = med: vgood (10.0/5.0)
			* Maint = low: vgood (11.0/4.0)


## SimpleCart Decision Tree

	* Persons=(more)|(4)
		* Safety=(high)|(med)
			* Buying=(low)|(med)
				* Maint=(low)|(med)
					* Safety=(high)|(low)
						* Lug_boot=(big)|(med)
								* Doors=(5more)|(4)|(3)
									* Doors=(5more)|(4)|(2): vgood(28.0/0.0)
									* Doors!=(5more)|(4)|(2)
									* Lug_boot=(big)|(small): vgood(8.0/0.0)
									* Lug_boot!=(big)|(small)
										* Persons=(more)|(2): vgood(3.0/0.0)
										* Persons!=(more)|(2): good(2.0/1.0)
								* Doors!=(5more)|(4)|(3)
							* Lug_boot=(big): vgood(7.0/0.0)
							* Lug_boot!=(big)
										* Buying=(low)|(vhigh)|(high): good(4.0/0.0)
										* Buying!=(low)|(vhigh)|(high)
											* Maint=(low)|(vhigh)|(high): good(2.0/0.0)
											* Maint!=(low)|(vhigh)|(high): acc(2.0/0.0)
						* Lug_boot!=(big)|(med)
								* Buying=(low)|(vhigh)|(high)
									* Doors=(5more)|(4)|(3): good(12.0/0.0)
									* Doors!=(5more)|(4)|(3): good(2.0/1.0)
								* Buying!=(low)|(vhigh)|(high)
							* Maint=(low)
										* Doors=(5more)|(4)|(3): good(4.0/0.0)
										* Doors!=(5more)|(4)|(3): unacc(1.0/1.0)
							* Maint!=(low)
										* Doors=(5more)|(4)|(3): acc(6.0/0.0)
										* Doors!=(5more)|(4)|(3): unacc(1.0/1.0)
					* Safety!=(high)|(low)
						* Lug_boot=(big)|(med)
						* Buying=(low)
									* Doors=(5more)|(4)|(3)
										* Doors=(5more)|(4)|(2): good(14.0/0.0)
										* Doors!=(5more)|(4)|(2)
										* Persons=(more)|(2): good(3.0/0.0)
										* Persons!=(more)|(2): good(2.0/1.0)
									* Doors!=(5more)|(4)|(3)
								* Lug_boot=(big): good(3.0/0.0)
								* Lug_boot!=(big): acc(4.0/0.0)
						* Buying!=(low)
							* Maint=(low)
										* Doors=(5more)|(4)|(3)
											* Doors=(5more)|(4)|(2): good(7.0/0.0)
											* Doors!=(5more)|(4)|(2)
											* Persons=(more)|(2): good(2.0/0.0)
											* Persons!=(more)|(2): acc(1.0/1.0)
										* Doors!=(5more)|(4)|(3): acc(2.0/1.0)
							* Maint!=(low): acc(16.0/0.0)
						* Lug_boot!=(big)|(med)
								* Doors=(5more)|(4)|(3): acc(21.0/0.0)
								* Doors!=(5more)|(4)|(3)
								* Persons=(more)|(2): unacc(4.0/0.0)
								* Persons!=(more)|(2): acc(4.0/0.0)
				* Maint!=(low)|(med)
					* Lug_boot=(big)|(med)
					* Buying=(low)
						* Safety=(high)
									* Maint=(high)|(med)|(low)
									* Lug_boot=(big)|(small): vgood(8.0/0.0)
									* Lug_boot!=(big)|(small)
										* Doors=(5more)|(4): vgood(3.0/0.0)
										* Doors!=(5more)|(4): acc(2.0/1.0)
									* Maint!=(high)|(med)|(low): acc(13.0/0.0)
						* Safety!=(high)
									* Maint=(high)|(med)|(low): acc(15.0/0.0)
									* Maint!=(high)|(med)|(low)
									* Doors=(5more)|(4): acc(7.0/0.0)
									* Doors!=(5more)|(4)
										* Lug_boot=(big)|(small): acc(4.0/0.0)
										* Lug_boot!=(big)|(small)
												* Doors=(3)|(4)|(5more): unacc(1.0/1.0)
												* Doors!=(3)|(4)|(5more): unacc(2.0/0.0)
					* Buying!=(low)
							* Lug_boot=(big)|(small): acc(31.0/0.0)
							* Lug_boot!=(big)|(small)
									* Doors=(5more)|(4)|(3)
										* Doors=(5more)|(4)|(2): acc(14.0/0.0)
										* Doors!=(5more)|(4)|(2)
										* Persons=(more)|(2): acc(4.0/0.0)
										* Persons!=(more)|(2)
											* Safety=(high)|(low): acc(2.0/0.0)
											* Safety!=(high)|(low): unacc(2.0/0.0)
									* Doors!=(5more)|(4)|(3)
								* Safety=(high): acc(3.0/0.0)
								* Safety!=(high): unacc(4.0/0.0)
					* Lug_boot!=(big)|(med)
						* Safety=(high)|(low)
								* Doors=(5more)|(4)|(3): acc(23.0/0.0)
								* Doors!=(5more)|(4)|(3)
								* Persons=(more)|(2): unacc(4.0/0.0)
								* Persons!=(more)|(2): acc(3.0/0.0)
						* Safety!=(high)|(low)
						* Maint=(high)
									* Buying=(low)|(vhigh)|(high)
										* Doors=(5more)|(4)|(3): acc(5.0/0.0)
										* Doors!=(5more)|(4)|(3): unacc(1.0/1.0)
									* Buying!=(low)|(vhigh)|(high): unacc(7.0/0.0)
						* Maint!=(high): unacc(15.0/0.0)
			* Buying!=(low)|(med)
				* Maint=(low)|(med)
					* Lug_boot=(big)|(med)
							* Doors=(5more)|(4)|(3)
								* Doors=(5more)|(4)|(2): acc(57.0/0.0)
								* Doors!=(5more)|(4)|(2)
								* Persons=(more)|(2): acc(15.0/0.0)
								* Persons!=(more)|(2)
									* Safety=(high)|(low): acc(8.0/0.0)
									* Safety!=(high)|(low)
										* Lug_boot=(big)|(small): acc(3.0/0.0)
										* Lug_boot!=(big)|(small): unacc(3.0/0.0)
							* Doors!=(5more)|(4)|(3)
							* Lug_boot=(big)|(small): acc(15.0/0.0)
							* Lug_boot!=(big)|(small)
							* Safety=(high): acc(7.0/0.0)
							* Safety!=(high): unacc(8.0/0.0)
					* Lug_boot!=(big)|(med)
					* Safety=(high)
								* Doors=(5more)|(4)|(3): acc(20.0/0.0)
								* Doors!=(5more)|(4)|(3)
								* Persons=(more)|(2): unacc(4.0/0.0)
								* Persons!=(more)|(2): acc(4.0/0.0)
					* Safety!=(high): unacc(29.0/0.0)
				* Maint!=(low)|(med)
				* Maint=(high)
					* Buying=(high)
							* Lug_boot=(big)|(med)
									* Doors=(5more)|(4)|(3): acc(16.0/0.0)
									* Doors!=(5more)|(4)|(3)
									* Lug_boot=(big)|(small): acc(4.0/0.0)
									* Lug_boot!=(big)|(small): acc(2.0/1.0)
							* Lug_boot!=(big)|(med)
								* Safety=(high)|(low)
										* Doors=(5more)|(4)|(3): acc(6.0/0.0)
										* Doors!=(5more)|(4)|(3): unacc(1.0/1.0)
								* Safety!=(high)|(low): unacc(6.0/0.0)
					* Buying!=(high): unacc(44.0/0.0)
				* Maint!=(high): unacc(90.0/0.0)
		* Safety!=(high)|(med): unacc(342.0/0.0)
	* Persons!=(more)|(4): unacc(518.0/0.0)


