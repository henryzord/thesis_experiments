# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Persons != 4 | unacc | 0.604616 |
| Persons != more | unacc | 0.601609 |
| Persons != 2 and Safety != low and Buying != low and Buying != med and Maint != vhigh and Lug_boot != small and Maint != high and Safety != med | acc | 0.045095 |
| Persons != 2 and Safety != low and Buying != low and Buying = med and Maint != low and Lug_boot != small and Maint != med | acc | 0.037967 |
| Persons != 2 and Safety != low and Buying != low and Buying != med and Maint != vhigh and Lug_boot != small and Maint = high and Buying != vhigh | acc | 0.019740 |
| Persons != 2 and Safety != low and Buying != low and Buying != med and Maint != vhigh and Lug_boot != small and Maint != high and Safety = med and Lug_boot != med | acc | 0.021880 |
| Persons != 2 and Safety != low and Buying != low and Buying != med and Maint != vhigh and Lug_boot = small and Safety != med and Doors != 2 | acc | 0.018536 |
| Persons != 2 and Safety != low and Buying = low and Maint = vhigh and Safety != med | acc | 0.017901 |
| Persons != 2 and Safety != low and Buying = low and Maint != vhigh and Safety = med and Lug_boot = small | acc | 0.014209 |
| Persons != 2 and Safety != low and Buying = low and Maint != vhigh and Safety != med and Lug_boot != small | vgood | 0.020160 |
| Persons != 2 and Safety != low and Buying != low and Buying != med and Maint != vhigh and Lug_boot != small and Maint != high and Safety = med and Lug_boot = med and Doors != 2 | acc | 0.012062 |
| Persons != 2 and Safety != low and Buying != low and Buying = med and Maint != low and Lug_boot = small and Safety != med | acc | 0.012626 |
| Persons != 2 and Safety != low and Buying != low and Buying = med and Maint != low and Lug_boot != small and Maint = med and Safety = med | acc | 0.012275 |
| Persons != 2 and Safety != low and Buying = low and Maint != vhigh and Safety = med and Lug_boot != small and Maint != high | good | 0.011455 |
| Persons != 2 and Safety != low and Buying = low and Maint != vhigh and Safety = med and Lug_boot != small and Maint = high | acc | 0.011466 |
| Persons != 2 and Safety != low and Buying = low and Maint != vhigh and Safety != med and Lug_boot = small and Maint != high | good | 0.006843 |
| Persons != 2 and Safety != low and Buying = low and Maint = vhigh and Safety = med and Lug_boot != small | acc | 0.006336 |
| Persons != 2 and Safety != low and Buying != low and Buying = med and Maint = low and Safety = med and Lug_boot != small | good | 0.006391 |
| Persons != 2 and Safety != low and Buying != low and Buying = med and Maint = low and Safety = med and Lug_boot = small | acc | 0.005049 |
| Persons != 2 and Safety != low and Buying = low and Maint != vhigh and Safety != med and Lug_boot = small and Maint = high | acc | 0.004243 |
| Persons != 2 and Safety != low and Buying != low and Buying = med and Maint = low and Safety != med and Lug_boot = big | vgood | 0.004660 |
| Persons != 2 and Safety != low and Buying != low and Buying = med and Maint != low and Lug_boot = small and Safety = med and Maint = med | acc | 0.004243 |
| Persons != 2 and Safety != low and Buying != low and Buying = med and Maint != low and Lug_boot != small and Maint = med and Safety != med | vgood | 0.004497 |
| Persons != 2 and Safety != low and Buying != low and Buying = med and Maint = low and Safety != med and Lug_boot != big | good | 0.003291 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Safety = low | unacc | 0.522634 |
| Persons = 2 | unacc | 0.429975 |
| Buying = vhigh and Maint = vhigh | unacc | 0.084813 |
| Buying = high and Maint = vhigh | unacc | 0.084813 |
| Safety = med and Lug_boot = small and Buying = vhigh | unacc | 0.047228 |
| Safety = med and Lug_boot = small and Buying = high | unacc | 0.047228 |
| Buying = high and Doors = 4 | acc | 0.117886 |
| Safety = med and Maint = high and Buying = vhigh | unacc | 0.031180 |
| Safety = med and Lug_boot = big and Maint = high | acc | 0.097778 |
| Safety = med and Lug_boot = big and Buying = vhigh | acc | 0.064516 |
| Safety = med and Lug_boot = big and Maint = vhigh | acc | 0.064516 |
| Safety = med and Lug_boot = big and Buying = low | good | 0.030733 |
| Safety = med and Maint = vhigh and Lug_boot = small | unacc | 0.038760 |
| Buying = high and Safety = high and Lug_boot = med | acc | 0.093264 |
| Buying = high and Lug_boot = big | acc | 0.125000 |
| Maint = vhigh and Safety = high and Doors = 3 | acc | 0.064171 |
| Buying = high and Doors = 5more | acc | 0.048913 |
| Buying = vhigh and Maint = high | unacc | 0.063830 |
| Safety = med and Lug_boot = small and Maint = low and Doors = 3 | acc | 0.025316 |
| Safety = med and Lug_boot = small and Buying = low and Doors = 4 | acc | 0.037500 |
| Safety = med and Lug_boot = small and Maint = med and Doors = 3 | acc | 0.025316 |
| Safety = med and Lug_boot = small and Maint = low and Persons = 4 | acc | 0.031447 |
| Safety = med and Lug_boot = small and Buying = low and Doors = 5more | acc | 0.031447 |
| Safety = med and Lug_boot = small and Maint = high and Buying = med | unacc | 0.027397 |
| Safety = med and Doors = 4 and Maint = vhigh | acc | 0.026667 |
| Safety = med and Doors = 4 and Maint = high | acc | 0.020134 |
| Safety = med and Doors = 5more and Maint = med and Buying = med | acc | 0.033113 |
| Safety = med and Doors = 4 and Buying = med and Maint = med | acc | 0.033113 |
| Safety = med and Doors = 4 and Buying = med | good | 0.008555 |
| Safety = med and Doors = 5more and Lug_boot = med and Maint = high | acc | 0.020548 |
| Safety = med and Doors = 5more and Buying = vhigh | acc | 0.027211 |
| Safety = med and Doors = 5more and Maint = low and Lug_boot = med | good | 0.015504 |
| Safety = med and Lug_boot = big and Maint = low | good | 0.023077 |
| Safety = med and Doors = 2 and Buying = high | unacc | 0.023715 |
| Lug_boot = big and Buying = vhigh | acc | 0.099291 |
| Lug_boot = big and Maint = med and Safety = high | vgood | 0.066667 |
| Lug_boot = big and Maint = low | vgood | 0.066667 |
| Buying = vhigh and Safety = high and Doors = 5more | acc | 0.076190 |
| Lug_boot = big and Buying = med | acc | 0.149123 |
| Lug_boot = big and Maint = high | vgood | 0.036458 |
| Doors = 4 and Lug_boot = small and Maint = vhigh | acc | 0.042553 |
| Doors = 5more and Maint = vhigh | acc | 0.117647 |
| Doors = 4 and Lug_boot = small and Maint = high | acc | 0.042553 |
| Doors = 2 and Persons = 4 and Safety = high and Maint = high | acc | 0.042553 |
| Doors = 2 and Persons = more and Lug_boot = small | unacc | 0.103659 |
| Safety = med and Doors = 2 and Buying = vhigh | unacc | 0.026490 |
| Safety = med and Doors = 2 and Maint = med | acc | 0.067568 |
| Safety = med and Doors = 2 and Maint = vhigh | unacc | 0.027397 |
| Safety = med and Doors = 2 and Buying = low | acc | 0.071429 |
| Safety = high and Lug_boot = small and Buying = vhigh | acc | 0.109589 |
| Safety = med and Persons = more and Buying = vhigh | acc | 0.057971 |
| Safety = high and Lug_boot = small and Maint = high | acc | 0.109589 |
| Safety = med and Doors = 4 and Persons = 4 | acc | 0.007692 |
| Safety = med and Persons = more and Doors = 3 and Maint = high | acc | 0.044118 |
| Safety = high and Lug_boot = small and Buying = low and Maint = low | good | 0.072917 |
| Safety = high and Lug_boot = small and Buying = high | acc | 0.093750 |
| Safety = high and Lug_boot = small and Maint = med and Buying = med | acc | 0.079365 |
| Safety = med and Persons = 4 and Buying = high | unacc | 0.030612 |
| Safety = med and Buying = med and Maint = high | unacc | 0.030612 |
| Maint = vhigh and Safety = high | acc | 0.187500 |
| Safety = med and Persons = more and Buying = low and Maint = med | good | 0.047619 |
| Safety = med and Doors = 3 and Persons = more and Maint = low | good | 0.021858 |
| Safety = med and Doors = 2 | acc | 0.040816 |
| Safety = med and Doors = 3 and Buying = vhigh | unacc | 0.025641 |
| Lug_boot = small and Safety = high | good | 0.151515 |
| Safety = med and Doors = 3 and Maint = med | acc | 0.102564 |
| Buying = vhigh | acc | 0.204545 |
| Safety = med and Doors = 3 and Maint = vhigh and Persons = 4 | unacc | 0.036364 |
| Safety = med and Doors = 3 | acc | 0.175000 |
| Buying = low and Doors = 4 and Maint = low | vgood | 0.040000 |
| Doors = 4 and Buying = med | acc | 0.056250 |
| Doors = 2 and Maint = low | good | 0.121212 |
| Buying = low and Doors = 4 | vgood | 0.133333 |
| Buying = med and Maint = high | acc | 0.148148 |
| Doors = 5more and Safety = high | vgood | 0.363636 |
| Persons = 4 and Maint = med and Buying = low | good | 0.187500 |
| Persons = 4 and Maint = med | acc | 0.102564 |
| Doors = 3 and Persons = more | vgood | 0.357143 |
| Maint = low | good | 0.333333 |
| Maint = high | acc | 0.400000 |
|  | acc | 0.400000 |


# Text representation of classifiers as-is

## PART

Decision list:

rules | predicted class
---|---
Safety = low|unacc (508.0)
Persons = 2|unacc (350.0)
Buying = vhigh AND Maint = vhigh|unacc (43.0)
Buying = high AND Maint = vhigh|unacc (43.0)
Safety = med AND Lug_boot = small AND Buying = vhigh|unacc (23.0)
Safety = med AND Lug_boot = small AND Buying = high|unacc (23.0)
Buying = high AND Doors = 4|acc (29.0)
Safety = med AND Maint = high AND Buying = vhigh|unacc (14.0)
Safety = med AND Lug_boot = big AND Maint = high|acc (22.0)
Safety = med AND Lug_boot = big AND Buying = vhigh|acc (14.0)
Safety = med AND Lug_boot = big AND Maint = vhigh|acc (14.0)
Safety = med AND Lug_boot = big AND Buying = low|good (13.0)
Safety = med AND Maint = vhigh AND Lug_boot = small|unacc (15.0)
Buying = high AND Safety = high AND Lug_boot = med|acc (18.0)
Buying = high AND Lug_boot = big|acc (25.0)
Maint = vhigh AND Safety = high AND Doors = 3|acc (12.0)
Buying = high AND Doors = 5more|acc (9.0)
Buying = vhigh AND Maint = high|unacc (21.0)
Safety = med AND Lug_boot = small AND Maint = low AND Doors = 3|acc (4.0)
Safety = med AND Lug_boot = small AND Buying = low AND Doors = 4|acc (6.0)
Safety = med AND Lug_boot = small AND Maint = med AND Doors = 3|acc (4.0)
Safety = med AND Lug_boot = small AND Maint = low AND Persons = 4|acc (5.0)
Safety = med AND Lug_boot = small AND Buying = low AND Doors = 5more|acc (5.0)
Safety = med AND Lug_boot = small AND Maint = high AND Buying = med|unacc (8.0)
Safety = med AND Doors = 4 AND Maint = vhigh|acc (4.0)
Safety = med AND Doors = 4 AND Maint = high|acc (3.0)
Safety = med AND Doors = 5more AND Maint = med AND Buying = med|acc (5.0)
Safety = med AND Doors = 4 AND Buying = med AND Maint = med|acc (5.0)
Safety = med AND Doors = 4 AND Buying = med|good (4.0/1.0)
Safety = med AND Doors = 5more AND Lug_boot = med AND Maint = high|acc (3.0)
Safety = med AND Doors = 5more AND Buying = vhigh|acc (4.0)
Safety = med AND Doors = 5more AND Maint = low AND Lug_boot = med|good (4.0)
Safety = med AND Lug_boot = big AND Maint = low|good (6.0)
Safety = med AND Doors = 2 AND Buying = high|unacc (6.0)
Lug_boot = big AND Buying = vhigh|acc (14.0)
Lug_boot = big AND Maint = med AND Safety = high|vgood (15.0)
Lug_boot = big AND Maint = low|vgood (15.0)
Buying = vhigh AND Safety = high AND Doors = 5more|acc (8.0)
Lug_boot = big AND Buying = med|acc (17.0)
Lug_boot = big AND Maint = high|vgood (7.0)
Doors = 4 AND Lug_boot = small AND Maint = vhigh|acc (4.0)
Doors = 5more AND Maint = vhigh|acc (12.0)
Doors = 4 AND Lug_boot = small AND Maint = high|acc (4.0)
Doors = 2 AND Persons = 4 AND Safety = high AND Maint = high|acc (4.0)
Doors = 2 AND Persons = more AND Lug_boot = small|unacc (17.0)
Safety = med AND Doors = 2 AND Buying = vhigh|unacc (4.0)
Safety = med AND Doors = 2 AND Maint = med|acc (5.0)
Safety = med AND Doors = 2 AND Maint = vhigh|unacc (4.0)
Safety = med AND Doors = 2 AND Buying = low|acc (5.0)
Safety = high AND Lug_boot = small AND Buying = vhigh|acc (8.0)
Safety = med AND Persons = more AND Buying = vhigh|acc (4.0)
Safety = high AND Lug_boot = small AND Maint = high|acc (8.0)
Safety = med AND Doors = 4 AND Persons = 4|acc (2.0/1.0)
Safety = med AND Persons = more AND Doors = 3 AND Maint = high|acc (3.0)
Safety = high AND Lug_boot = small AND Buying = low AND Maint = low|good (7.0)
Safety = high AND Lug_boot = small AND Buying = high|acc (6.0)
Safety = high AND Lug_boot = small AND Maint = med AND Buying = med|acc (5.0)
Safety = med AND Persons = 4 AND Buying = high|unacc (3.0)
Safety = med AND Buying = med AND Maint = high|unacc (3.0)
Maint = vhigh AND Safety = high|acc (12.0)
Safety = med AND Persons = more AND Buying = low AND Maint = med|good (3.0)
Safety = med AND Doors = 3 AND Persons = more AND Maint = low|good (3.0/1.0)
Safety = med AND Doors = 2|acc (2.0)
Safety = med AND Doors = 3 AND Buying = vhigh|unacc (2.0)
Lug_boot = small AND Safety = high|good (10.0)
Safety = med AND Doors = 3 AND Maint = med|acc (4.0)
Buying = vhigh|acc (9.0)
Safety = med AND Doors = 3 AND Maint = vhigh AND Persons = 4|unacc (2.0)
Safety = med AND Doors = 3|acc (6.0)
Buying = low AND Doors = 4 AND Maint = low|vgood (3.0/1.0)
Doors = 4 AND Buying = med|acc (4.0/2.0)
Doors = 2 AND Maint = low|good (4.0)
Buying = low AND Doors = 4|vgood (4.0)
Buying = med AND Maint = high|acc (4.0)
Doors = 5more AND Safety = high|vgood (8.0)
Persons = 4 AND Maint = med AND Buying = low|good (3.0)
Persons = 4 AND Maint = med|acc (2.0)
Doors = 3 AND Persons = more|vgood (5.0)
Maint = low|good (3.0/1.0)
Maint = high|acc (2.0)
|acc (2.0/1.0)


## J48 Decision Tree

* Persons = 2: unacc (524.0)
* Persons != 2
	* Safety = low: unacc (334.0)
	* Safety != low
		* Buying = low
			* Maint = vhigh
				* Safety = med
					* Lug_boot = small: unacc (7.0)
					* Lug_boot != small: acc (13.0/3.0)
				* Safety != med: acc (22.0)
			* Maint != vhigh
				* Safety = med
					* Lug_boot = small: acc (23.0/3.0)
					* Lug_boot != small
						* Maint = high: acc (14.0)
						* Maint != high: good (28.0/6.0)
				* Safety != med
					* Lug_boot = small
						* Maint = high: acc (7.0/1.0)
						* Maint != high: good (14.0/2.0)
					* Lug_boot != small: vgood (47.0/9.0)
		* Buying != low
			* Buying = med
				* Maint = low
					* Safety = med
						* Lug_boot = small: acc (8.0/1.0)
						* Lug_boot != small: good (15.0/3.0)
					* Safety != med
						* Lug_boot = big: vgood (7.0)
						* Lug_boot != big: good (13.0/5.0)
				* Maint != low
					* Lug_boot = small
						* Safety = med
							* Maint = med: acc (7.0/1.0)
							* Maint != med: unacc (16.0)
						* Safety != med: acc (21.0/3.0)
					* Lug_boot != small
						* Maint = med
							* Safety = med: acc (15.0)
							* Safety != med: vgood (12.0/3.0)
						* Maint != med: acc (59.0/6.0)
			* Buying != med
				* Maint = vhigh: unacc (86.0)
				* Maint != vhigh
					* Lug_boot = small
						* Safety = med: unacc (46.0)
						* Safety != med
							* Doors = 2: unacc (11.0/4.0)
							* Doors != 2: acc (32.0/5.0)
					* Lug_boot != small
						* Maint = high
							* Buying = vhigh: unacc (28.0)
							* Buying != vhigh: acc (30.0/3.0)
						* Maint != high
							* Safety = med
								* Lug_boot = med
									* Doors = 2: unacc (8.0)
									* Doors != 2: acc (22.0/4.0)
								* Lug_boot != med: acc (27.0)
							* Safety != med: acc (57.0)


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
										* Doors=(3)|(4)|(5more)
										* Persons=(more)|(2): vgood(4.0/0.0)
										* Persons!=(more)|(2)
												* Buying=(low)|(vhigh)|(high): good(2.0/0.0)
												* Buying!=(low)|(vhigh)|(high): acc(1.0/1.0)
										* Doors!=(3)|(4)|(5more)
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
									* Maint=(low)|(vhigh)|(high)
										* Doors=(4)|(3)|(5more): good(4.0/0.0)
										* Doors!=(4)|(3)|(5more): unacc(1.0/1.0)
									* Maint!=(low)|(vhigh)|(high)
										* Doors=(5more)|(4)|(3): acc(4.0/0.0)
										* Doors!=(5more)|(4)|(3): unacc(1.0/1.0)
				* Safety!=(high)
						* Lug_boot=(big)|(med)
								* Maint=(low)|(vhigh)|(high)
								* Doors=(5more)|(4): good(15.0/0.0)
								* Doors!=(5more)|(4)
								* Lug_boot=(big): good(6.0/0.0)
								* Lug_boot!=(big)
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


