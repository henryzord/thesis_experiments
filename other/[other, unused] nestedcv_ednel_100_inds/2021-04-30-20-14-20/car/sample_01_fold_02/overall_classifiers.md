# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Safety != high | unacc | 0.614024 |
| Safety != med | unacc | 0.592317 |
| Buying = high and Maint = high and Persons = 4 and Safety = high | acc | 0.009836 |
| Buying = vhigh and Maint = low and Persons = 4 and Safety = high | acc | 0.009024 |
| Buying = med and Maint = vhigh and Persons = more and Safety = high | acc | 0.009024 |
| Buying = med and Maint = vhigh and Persons = 4 and Safety = high | acc | 0.009024 |
| Buying = med and Maint = med and Persons = 4 and Safety = med | acc | 0.009024 |
| Buying = med and Maint = high and Persons = 4 and Safety = high | acc | 0.009024 |
| Buying = vhigh and Maint = med and Persons = more and Safety = high | acc | 0.008279 |
| Buying = high and Maint = low and Persons = 4 and Safety = high | acc | 0.009024 |
| Buying = low and Maint = high and Persons = 4 and Safety = med | acc | 0.009024 |
| Buying = high and Maint = med and Persons = more and Safety = high | acc | 0.007470 |
| Buying = vhigh and Maint = med and Persons = 4 and Safety = high | acc | 0.008210 |
| Buying = med and Maint = high and Persons = more and Safety = high | acc | 0.008210 |
| Buying = med and Maint = med and Persons = more and Safety = med | acc | 0.007470 |
| Buying = low and Maint = vhigh and Persons = 4 and Safety = high | acc | 0.008210 |
| Buying = vhigh and Maint = low and Persons = more and Safety = high | acc | 0.007470 |
| Buying = high and Maint = med and Persons = 4 and Safety = high | acc | 0.008210 |
| Buying = low and Maint = high and Persons = more and Safety = med | acc | 0.007470 |
| Buying = low and Maint = vhigh and Persons = more and Safety = high | acc | 0.006661 |
| Buying = high and Maint = low and Persons = more and Safety = high | acc | 0.007395 |
| Buying = high and Maint = high and Persons = more and Safety = high | acc | 0.007395 |
| Buying = med and Maint = vhigh and Persons = more and Safety = med | acc | 0.003375 |
| Buying = med and Maint = high and Persons = more and Safety = med | acc | 0.003678 |
| Buying = vhigh and Maint = med and Persons = more and Safety = med | acc | 0.003375 |
| Buying = high and Maint = high and Persons = more and Safety = med | acc | 0.003375 |
| Buying = vhigh and Maint = low and Persons = more and Safety = med | acc | 0.003375 |
| Buying = high and Maint = high and Persons = 4 and Safety = med | acc | 0.002483 |
| Buying = low and Maint = vhigh and Persons = more and Safety = med | acc | 0.002707 |
| Buying = high and Maint = low and Persons = more and Safety = med | acc | 0.002707 |
| Buying = med and Maint = low and Persons = more and Safety = med | good | 0.003273 |
| Buying = med and Maint = low and Persons = more and Safety = high | vgood | 0.003271 |
| Buying = low and Maint = med and Persons = more and Safety = med | good | 0.002731 |
| Buying = med and Maint = med and Persons = more and Safety = high | vgood | 0.002730 |
| Buying = low and Maint = low and Persons = 4 and Safety = med | acc | 0.002707 |
| Buying = low and Maint = high and Persons = 4 and Safety = high | acc | 0.002483 |
| Buying = low and Maint = low and Persons = more and Safety = med | good | 0.002408 |
| Buying = low and Maint = med and Persons = 4 and Safety = med | acc | 0.002483 |
| Buying = low and Maint = med and Persons = more and Safety = high | vgood | 0.002672 |
| Buying = med and Maint = low and Persons = 4 and Safety = high | vgood | 0.002406 |
| Buying = med and Maint = med and Persons = 4 and Safety = high | acc | 0.002070 |
| Buying = low and Maint = low and Persons = more and Safety = high | vgood | 0.002189 |
| Buying = low and Maint = low and Persons = 4 and Safety = high | good | 0.002191 |
| Buying = low and Maint = med and Persons = 4 and Safety = high | vgood | 0.002189 |
| Buying = med and Maint = low and Persons = 4 and Safety = med | good | 0.001674 |
| Safety = med and Persons = 4 and Buying = med and Maint != med and Safety!=(high) and Lug_boot = med and Doors = 5more | acc | 0.001103 |
| Buying = low and Maint = high and Persons = more and Safety = high | vgood | 0.001858 |
| Safety = med and Persons = 4 and Buying != med and Maint = med and Safety!=(high) and Lug_boot = med and Lug_boot != small and Doors = 5more | acc | 0.001103 |
| Safety = med and Persons = 4 and Buying = med and Maint != med and Safety!=(high) and Lug_boot = med and Doors = 4 | acc | 0.000414 |
| Safety = med and Persons = 4 and Buying != med and Maint = med and Safety!=(high) and Lug_boot = med and Lug_boot != small and Doors = 4 | acc | 0.000414 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Safety = low | unacc | 0.529412 |
| Persons = 2 | unacc | 0.417817 |
| Maint = vhigh and Buying = vhigh | unacc | 0.090196 |
| Buying != low and Buying != med and Maint != vhigh and Lug_boot != small and Maint != high and Lug_boot != med | acc | 0.158904 |
| Buying = vhigh and Maint = high | unacc | 0.099778 |
| Buying = high and Maint = vhigh | unacc | 0.101770 |
| Safety != med and Lug_boot = small and Doors != 2 and Buying != low | acc | 0.159879 |
| Safety = med and Lug_boot = small and Buying = high | unacc | 0.059585 |
| Safety = med and Lug_boot = big and Maint != low and Maint != med | acc | 0.160870 |
| Safety = med and Lug_boot = big and Buying != med | good | 0.042254 |
| Safety = med and Lug_boot = big and Maint != med | good | 0.020173 |
| Safety = med and Doors = 2 and Buying != vhigh and Maint != vhigh and Buying != high and Persons = 4 | acc | 0.051709 |
| Safety = med and Doors = 2 and Lug_boot = small | unacc | 0.048701 |
| Lug_boot = big and Maint != vhigh and Buying != high and Safety != med and Maint != high | vgood | 0.087227 |
| Safety = med and Doors = 2 and Buying != low | unacc | 0.047002 |
| Lug_boot != small and Safety != med and Buying != low and Buying != med | acc | 0.269231 |
| Safety = med and Lug_boot = small and Maint != vhigh and Buying != vhigh and Maint != high | acc | 0.155556 |
| Lug_boot != small and Safety = med and Maint != low and Buying != low and Doors != 3 | acc | 0.179856 |
| Lug_boot = small and Safety = med and Maint != high | unacc | 0.115000 |
| Maint = vhigh and Safety != med | acc | 0.272222 |
| Maint = high and Safety != med and Buying != low | acc | 0.157407 |
| Safety = med and Maint = high and Buying = low | acc | 0.116505 |
| Safety = med and Lug_boot = small | unacc | 0.042373 |
| Safety = med and Maint = vhigh and Persons = 4 | unacc | 0.015789 |
| Buying = vhigh | acc | 0.051797 |
| Buying = high and Doors != 3 | acc | 0.047893 |
| Buying != high and Safety = med and Maint != vhigh and Doors = 4 | good | 0.072289 |
| Safety = med and Doors != 5more and Buying != high | acc | 0.111111 |
| Lug_boot = small and Maint != high and Buying != med | good | 0.132238 |
| Buying != high and Lug_boot = small and Buying != med | acc | 0.066486 |
| Buying != high and Lug_boot != small and Safety != med and Doors != 2 and Doors != 3 | vgood | 0.333333 |
| Lug_boot != big and Buying != high and Lug_boot != small and Maint != high and Doors != 3 and Maint = low | good | 0.170732 |
| Lug_boot != big and Buying = high | unacc | 0.078431 |
| Lug_boot != small and Lug_boot = med and Doors != 3 and Maint = med | good | 0.058065 |
| Lug_boot != small and Lug_boot = med and Persons != 4 | vgood | 0.068681 |
| Lug_boot != big and Maint != low | acc | 0.244939 |
| Maint = high | vgood | 0.145455 |
|  | good | 0.473684 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

buying|maint|persons|safety|acceptability
---|---|---|---|---
low|low|more|high|vgood
vhigh|low|more|high|acc
high|low|more|high|acc
med|low|more|high|vgood
vhigh|med|more|high|acc
high|med|more|high|acc
low|med|more|high|vgood
med|med|more|high|vgood
high|high|more|high|acc
med|high|more|high|acc
high|low|4|high|acc
low|high|more|high|vgood
vhigh|low|4|high|acc
low|low|4|high|good
med|low|4|high|vgood
vhigh|high|more|high|unacc
med|med|4|high|acc
vhigh|low|more|med|acc
low|vhigh|more|high|acc
low|low|more|med|good
vhigh|med|4|high|acc
med|vhigh|more|high|acc
high|med|4|high|acc
med|low|more|med|good
low|med|4|high|vgood
vhigh|vhigh|more|high|unacc
high|low|more|med|acc
high|vhigh|more|high|unacc
med|med|more|med|acc
vhigh|high|4|high|unacc
low|med|more|med|good
low|low|2|high|unacc
vhigh|med|more|med|acc
high|med|more|med|unacc
med|high|4|high|acc
high|high|4|high|acc
low|high|4|high|acc
high|low|2|high|unacc
vhigh|low|2|high|unacc
med|low|2|high|unacc
low|vhigh|4|high|acc
med|vhigh|4|high|acc
med|high|more|med|acc
med|med|2|high|unacc
vhigh|med|2|high|unacc
med|low|4|med|good
low|high|more|med|acc
high|high|more|med|acc
high|low|4|med|unacc
low|low|4|med|acc
vhigh|low|4|med|unacc
high|med|2|high|unacc
high|vhigh|4|high|unacc
low|med|2|high|unacc
vhigh|high|more|med|unacc
vhigh|vhigh|4|high|unacc
vhigh|low|more|low|unacc
vhigh|high|2|high|unacc
low|med|4|med|acc
med|med|4|med|acc
low|vhigh|more|med|acc
high|high|2|high|unacc
med|vhigh|more|med|acc
med|low|more|low|unacc
high|low|more|low|unacc
med|high|2|high|unacc
vhigh|vhigh|more|med|unacc
high|vhigh|more|med|unacc
low|high|2|high|unacc
low|low|more|low|unacc
vhigh|med|4|med|unacc
high|med|4|med|unacc
high|med|more|low|unacc
low|high|4|med|acc
med|vhigh|2|high|unacc
med|high|4|med|unacc
high|vhigh|2|high|unacc
high|low|2|med|unacc
med|low|2|med|unacc
low|low|2|med|unacc
vhigh|low|2|med|unacc
high|high|4|med|acc
vhigh|med|more|low|unacc
vhigh|high|4|med|unacc
med|med|more|low|unacc
low|med|more|low|unacc
low|vhigh|2|high|unacc
vhigh|vhigh|2|high|unacc
vhigh|med|2|med|unacc
med|med|2|med|unacc
med|vhigh|4|med|unacc
high|high|more|low|unacc
low|vhigh|4|med|unacc
low|low|4|low|unacc
vhigh|high|more|low|unacc
high|vhigh|4|med|unacc
low|high|more|low|unacc
low|med|2|med|unacc
vhigh|low|4|low|unacc
high|low|4|low|unacc
med|low|4|low|unacc
vhigh|vhigh|4|med|unacc
med|high|more|low|unacc
high|med|2|med|unacc
high|vhigh|more|low|unacc
low|vhigh|more|low|unacc
med|vhigh|more|low|unacc
vhigh|vhigh|more|low|unacc
med|med|4|low|unacc
high|high|2|med|unacc
low|med|4|low|unacc
vhigh|high|2|med|unacc
vhigh|med|4|low|unacc
med|high|2|med|unacc
low|high|2|med|unacc
high|med|4|low|unacc
low|high|4|low|unacc
med|high|4|low|unacc
med|low|2|low|unacc
vhigh|low|2|low|unacc
low|vhigh|2|med|unacc
vhigh|vhigh|2|med|unacc
med|vhigh|2|med|unacc
low|low|2|low|unacc
high|high|4|low|unacc
high|vhigh|2|med|unacc
high|low|2|low|unacc
vhigh|high|4|low|unacc
vhigh|med|2|low|unacc
high|vhigh|4|low|unacc
med|vhigh|4|low|unacc
med|med|2|low|unacc
vhigh|vhigh|4|low|unacc
low|vhigh|4|low|unacc
high|med|2|low|unacc
low|med|2|low|unacc
med|high|2|low|unacc
high|high|2|low|unacc
low|high|2|low|unacc
vhigh|high|2|low|unacc
med|vhigh|2|low|unacc
high|vhigh|2|low|unacc
low|vhigh|2|low|unacc
vhigh|vhigh|2|low|unacc

## PART

Decision list:

rules | predicted class
---|---
Safety = low|unacc (522.0)
Persons = 2|unacc (333.0)
Maint = vhigh AND Buying = vhigh|unacc (46.0)
Buying != low AND Buying != med AND Maint != vhigh AND Lug_boot != small AND Maint != high AND Lug_boot != med|acc (58.0)
Buying = vhigh AND Maint = high|unacc (45.0)
Buying = high AND Maint = vhigh|unacc (46.0)
Safety != med AND Lug_boot = small AND Doors != 2 AND Buying != low|acc (45.0/2.0)
Safety = med AND Lug_boot = small AND Buying = high|unacc (23.0)
Safety = med AND Lug_boot = big AND Maint != low AND Maint != med|acc (37.0)
Safety = med AND Lug_boot = big AND Buying != med|good (15.0)
Safety = med AND Lug_boot = big AND Maint != med|good (7.0)
Safety = med AND Doors = 2 AND Buying != vhigh AND Maint != vhigh AND Buying != high AND Persons = 4|acc (13.0/2.0)
Safety = med AND Doors = 2 AND Lug_boot = small|unacc (14.0)
Lug_boot = big AND Maint != vhigh AND Buying != high AND Safety != med AND Maint != high|vgood (28.0)
Safety = med AND Doors = 2 AND Buying != low|unacc (14.0/1.0)
Lug_boot != small AND Safety != med AND Buying != low AND Buying != med|acc (42.0)
Safety = med AND Lug_boot = small AND Maint != vhigh AND Buying != vhigh AND Maint != high|acc (21.0)
Lug_boot != small AND Safety = med AND Maint != low AND Buying != low AND Doors != 3|acc (24.0)
Lug_boot = small AND Safety = med AND Maint != high|unacc (23.0)
Maint = vhigh AND Safety != med|acc (36.0/1.0)
Maint = high AND Safety != med AND Buying != low|acc (17.0)
Safety = med AND Maint = high AND Buying = low|acc (12.0)
Safety = med AND Lug_boot = small|unacc (5.0)
Safety = med AND Maint = vhigh AND Persons = 4|unacc (5.0/2.0)
Buying = vhigh|acc (11.0/4.0)
Buying = high AND Doors != 3|acc (6.0/1.0)
Buying != high AND Safety = med AND Maint != vhigh AND Doors = 4|good (6.0)
Safety = med AND Doors != 5more AND Buying != high|acc (18.0/5.0)
Lug_boot = small AND Maint != high AND Buying != med|good (14.0/1.0)
Buying != high AND Lug_boot = small AND Buying != med|acc (7.0)
Buying != high AND Lug_boot != small AND Safety != med AND Doors != 2 AND Doors != 3|vgood (22.0)
Lug_boot != big AND Buying != high AND Lug_boot != small AND Maint != high AND Doors != 3 AND Maint = low|good (7.0)
Lug_boot != big AND Buying = high|unacc (5.0/2.0)
Lug_boot != small AND Lug_boot = med AND Doors != 3 AND Maint = med|good (5.0/2.0)
Lug_boot != small AND Lug_boot = med AND Persons != 4|vgood (7.0/2.0)
Lug_boot != big AND Maint != low|acc (6.0/2.0)
Maint = high|vgood (4.0)
|good (4.0/1.0)


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
								* Lug_boot!=(big)|(small)
										* Maint=(low)|(vhigh)|(high)
											* Doors=(3)|(4)|(5more)
											* Persons=(more)|(2): vgood(2.0/0.0)
											* Persons!=(more)|(2): good(2.0/0.0)
											* Doors!=(3)|(4)|(5more): good(4.0/0.0)
										* Maint!=(low)|(vhigh)|(high)
									* Buying=(low): good(2.0/1.0)
									* Buying!=(low)
												* Doors=(3)|(4)|(5more): acc(1.0/1.0)
												* Doors!=(3)|(4)|(5more): acc(2.0/0.0)
						* Lug_boot!=(big)|(med)
								* Buying=(low)|(vhigh)|(high)
									* Doors=(5more)|(4)|(3): good(11.0/0.0)
									* Doors!=(5more)|(4)|(3): good(2.0/1.0)
								* Buying!=(low)|(vhigh)|(high)
							* Maint=(low)
										* Doors=(4)|(3)|(5more): good(2.0/0.0)
										* Doors!=(4)|(3)|(5more): unacc(1.0/1.0)
							* Maint!=(low)
										* Doors=(5more)|(4)|(3): acc(5.0/0.0)
										* Doors!=(5more)|(4)|(3): unacc(1.0/1.0)
				* Safety!=(high)
						* Lug_boot=(big)|(med)
						* Maint=(low)
								* Doors=(5more)|(4): good(14.0/0.0)
								* Doors!=(5more)|(4)
									* Lug_boot=(big)|(small): good(7.0/0.0)
									* Lug_boot!=(big)|(small)
									* Persons=(more): good(2.0/1.0)
									* Persons!=(more): acc(4.0/0.0)
						* Maint!=(low)
									* Buying=(low)|(vhigh)|(high)
									* Doors=(5more)|(4): good(8.0/0.0)
									* Doors!=(5more)|(4)
										* Lug_boot=(big)|(small): good(4.0/0.0)
										* Lug_boot!=(big)|(small)
												* Doors=(3)|(4)|(5more): acc(1.0/1.0)
												* Doors!=(3)|(4)|(5more): acc(2.0/0.0)
									* Buying!=(low)|(vhigh)|(high): acc(14.0/0.0)
						* Lug_boot!=(big)|(med)
								* Doors=(5more)|(4)|(3): acc(21.0/0.0)
								* Doors!=(5more)|(4)|(3)
								* Persons=(more)|(2): unacc(4.0/0.0)
								* Persons!=(more)|(2): acc(4.0/0.0)
				* Maint!=(low)|(med)
				* Safety=(high)
					* Buying=(low)
								* Maint=(high)|(med)|(low)
								* Lug_boot=(big)|(med)
									* Lug_boot=(big)|(small): vgood(7.0/0.0)
									* Lug_boot!=(big)|(small)
										* Doors=(5more)|(4): vgood(3.0/0.0)
										* Doors!=(5more)|(4)
												* Doors=(3)|(4)|(5more): acc(1.0/1.0)
												* Doors!=(3)|(4)|(5more): acc(2.0/0.0)
								* Lug_boot!=(big)|(med): acc(7.0/0.0)
								* Maint!=(high)|(med)|(low)
									* Doors=(5more)|(4)|(3): acc(15.0/0.0)
									* Doors!=(5more)|(4)|(3)
								* Persons=(more): unacc(1.0/1.0)
								* Persons!=(more): acc(3.0/0.0)
					* Buying!=(low): acc(43.0/0.0)
				* Safety!=(high)
						* Lug_boot=(big)|(med)
							* Doors=(5more)|(4): acc(29.0/0.0)
							* Doors!=(5more)|(4)
							* Lug_boot=(big): acc(15.0/0.0)
							* Lug_boot!=(big)
										* Buying=(low)|(vhigh)|(high)
											* Maint=(high)|(med)|(low): acc(4.0/0.0)
											* Maint!=(high)|(med)|(low)
												* Doors=(3)|(4)|(5more): unacc(1.0/1.0)
												* Doors!=(3)|(4)|(5more): unacc(2.0/0.0)
										* Buying!=(low)|(vhigh)|(high)
											* Doors=(3)|(4)|(5more)
											* Persons=(more)|(2): acc(2.0/0.0)
											* Persons!=(more)|(2): unacc(2.0/0.0)
											* Doors!=(3)|(4)|(5more): unacc(4.0/0.0)
						* Lug_boot!=(big)|(med)
						* Maint=(high)
									* Buying=(low)|(vhigh)|(high)
										* Doors=(5more)|(4)|(3): acc(5.0/0.0)
										* Doors!=(5more)|(4)|(3): unacc(1.0/1.0)
									* Buying!=(low)|(vhigh)|(high): unacc(7.0/0.0)
						* Maint!=(high): unacc(16.0/0.0)
			* Buying!=(low)|(med)
				* Maint=(low)|(med)
				* Safety=(high)
							* Doors=(5more)|(4)|(3): acc(65.0/0.0)
							* Doors!=(5more)|(4)|(3)
							* Lug_boot=(big)|(med): acc(14.0/0.0)
							* Lug_boot!=(big)|(med)
								* Persons=(more)|(2): unacc(3.0/0.0)
								* Persons!=(more)|(2): acc(3.0/0.0)
				* Safety!=(high)
						* Lug_boot=(big)|(med)
							* Lug_boot=(big)|(small): acc(28.0/0.0)
							* Lug_boot!=(big)|(small)
								* Doors=(5more)|(4): acc(13.0/0.0)
								* Doors!=(5more)|(4)
								* Doors=(3)
									* Persons=(more): acc(3.0/0.0)
									* Persons!=(more): unacc(4.0/0.0)
								* Doors!=(3): unacc(8.0/0.0)
						* Lug_boot!=(big)|(med): unacc(30.0/0.0)
				* Maint!=(low)|(med)
				* Maint=(high)
							* Buying=(high)|(med)|(low)
						* Safety=(high): acc(21.0/0.0)
						* Safety!=(high)
								* Lug_boot=(big)|(med)
									* Doors=(5more)|(4): acc(8.0/0.0)
									* Doors!=(5more)|(4)
										* Lug_boot=(big)|(small): acc(4.0/0.0)
										* Lug_boot!=(big)|(small)
												* Doors=(3)|(4)|(5more): unacc(1.0/1.0)
												* Doors!=(3)|(4)|(5more): unacc(2.0/0.0)
								* Lug_boot!=(big)|(med): unacc(8.0/0.0)
							* Buying!=(high)|(med)|(low): unacc(45.0/0.0)
				* Maint!=(high): unacc(92.0/0.0)
		* Persons!=(more)|(4): unacc(333.0/0.0)
	* Safety!=(high)|(med): unacc(522.0/0.0)


