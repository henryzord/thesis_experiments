# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Safety != high | unacc | 0.617833 |
| Safety != med | unacc | 0.591601 |
| Safety = med and Persons = 4 and Buying = med and Maint = med and Safety!=(high) and Lug_boot != med and Doors != 3 and Persons != 2 | acc | 0.004946 |
| Safety = med and Persons = 4 and Buying = med and Maint = med and Safety!=(high) and Lug_boot = med and Buying != high and Maint != vhigh | acc | 0.003303 |
| Safety = med and Persons = 4 and Buying = med and Maint = med and Safety!=(high) and Lug_boot != med and Doors = 3 | acc | 0.001654 |
| Safety = med and Persons = 4 and Buying != med and Maint = med and Lug_boot = med and Lug_boot!=(big) and Safety != low and Doors = 5more | acc | 0.001104 |
| Safety = med and Persons = 4 and Buying != med and Maint = med and Lug_boot = med and Lug_boot!=(big) and Safety != low and Doors = 4 | acc | 0.001104 |
| Safety = med and Persons = 4 and Buying = med and Maint != med and Lug_boot = med and Buying!=(low) and Doors = 3 and Doors != 2 and Lug_boot != small and Maint = low | acc | 0.000828 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Safety = low | unacc | 0.532795 |
| Persons = 2 | unacc | 0.422693 |
| Maint = vhigh and Buying = high | unacc | 0.086785 |
| Buying = vhigh and Maint = vhigh | unacc | 0.083168 |
| Buying = vhigh and Maint = high | unacc | 0.083168 |
| Safety = med and Lug_boot = small and Buying = high | unacc | 0.045361 |
| Safety = med and Lug_boot = small and Maint != vhigh and Buying != vhigh and Maint != high and Doors != 2 | acc | 0.103774 |
| Safety = med and Lug_boot = small and Maint = vhigh | unacc | 0.035011 |
| Safety = med and Lug_boot = small and Buying != low and Doors != 2 | unacc | 0.032895 |
| Buying = high and Doors != 2 and Doors != 3 | acc | 0.246445 |
| Safety = med and Lug_boot = big and Maint != low and Buying != low | acc | 0.171875 |
| Safety = med and Lug_boot = big and Buying != med and Maint != med and Maint != low | acc | 0.075581 |
| Safety != med and Lug_boot != small and Buying != vhigh and Maint != vhigh and Buying != high and Maint != high and Doors != 2 and Doors != 3 | vgood | 0.086835 |
| Buying = vhigh and Doors != 2 and Doors != 3 | acc | 0.209877 |
| Maint = vhigh and Doors != 2 and Safety != med | acc | 0.200000 |
| Buying = high and Safety != med and Lug_boot != small | acc | 0.152318 |
| Lug_boot = big and Safety = med and Buying != vhigh and Buying != high | good | 0.093333 |
| Lug_boot = big and Buying = low and Doors != 2 | vgood | 0.031390 |
| Lug_boot = big and Buying = vhigh | acc | 0.099099 |
| Lug_boot = big and Maint != med and Maint != low and Buying = med | acc | 0.082569 |
| Lug_boot = big and Buying != high and Buying = med | vgood | 0.029703 |
| Doors != 2 and Maint = high and Buying != high and Buying = med | acc | 0.145455 |
| Doors != 2 and Maint = high and Lug_boot = small | acc | 0.113208 |
| Lug_boot = big and Buying = high | acc | 0.040816 |
| Lug_boot = big and Persons != 4 | vgood | 0.013554 |
| Doors = 2 and Lug_boot != big and Safety = med and Buying != vhigh and Buying != high and Maint != vhigh and Persons = 4 and Maint != high | acc | 0.080808 |
| Doors = 2 and Lug_boot != big and Safety = med and Buying != low and Maint != low | unacc | 0.093525 |
| Buying = high and Lug_boot != small and Persons = 4 | unacc | 0.030769 |
| Buying = vhigh and Safety != med and Doors != 2 | acc | 0.097561 |
| Maint = vhigh and Doors != 4 and Doors != 5more and Safety != med and Persons = 4 | acc | 0.063291 |
| Maint = high and Lug_boot != small and Safety = med | acc | 0.097561 |
| Maint = vhigh and Doors != 4 and Doors != 5more and Persons != 4 | acc | 0.046382 |
| Buying = vhigh and Safety != med and Persons = 4 | acc | 0.051282 |
| Maint = high and Doors != 2 and Persons = 4 | vgood | 0.012121 |
| Buying = vhigh and Persons != 4 and Safety = med | unacc | 0.010638 |
| Maint = vhigh and Doors = 4 | acc | 0.054054 |
| Maint = high and Doors = 2 and Persons = 4 | acc | 0.078947 |
| Maint = high and Lug_boot = small | unacc | 0.045455 |
| Maint = high | vgood | 0.019149 |
| Buying = vhigh and Persons = 4 | unacc | 0.035714 |
| Buying = high and Doors != 2 | acc | 0.090909 |
| Maint = vhigh and Doors = 5more | acc | 0.062500 |
| Maint != vhigh and Doors != 2 and Maint != med and Doors != 3 | good | 0.229508 |
| Maint != vhigh and Lug_boot = small and Doors != 2 and Buying != med | good | 0.113208 |
| Maint != vhigh and Lug_boot = small and Persons = 4 and Maint != med | good | 0.045918 |
| Maint != vhigh and Lug_boot = small and Doors = 2 and Maint = med | unacc | 0.053333 |
| Maint != vhigh and Lug_boot = small and Maint != med | unacc | 0.070028 |
| Maint != vhigh and Lug_boot = small | acc | 0.180147 |
| Maint != vhigh and Safety = med and Doors = 2 | acc | 0.075000 |
| Maint != vhigh and Buying = low and Safety = med and Doors = 3 | acc | 0.035714 |
| Maint != vhigh and Buying = low and Safety != med and Doors = 2 | good | 0.084656 |
| Maint != vhigh and Buying = low and Doors != 3 | good | 0.084656 |
| Maint != vhigh and Buying != low and Maint = med and Doors != 3 | acc | 0.230769 |
| Maint = vhigh | unacc | 0.185185 |
| Persons = 4 and Maint = med | acc | 0.066667 |
| Buying = med and Persons != 4 | vgood | 0.057143 |
| Buying = med | good | 0.277778 |
|  | vgood | 0.285714 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Safety = high and Buying = low and Persons = more and Lug_boot = big | vgood | 0.006387 |
| Safety = high and Buying = low and Maint = med and Persons = 4 and Lug_boot = big | vgood | 0.002004 |
| Safety = high and Buying = med and Maint = med and Persons = 4 and Lug_boot = big | vgood | 0.002004 |
| Safety = high and Buying = low and Lug_boot = med and Doors = 5more and Persons = more | vgood | 0.001504 |
| Safety = high and Maint = low and Buying = med and Persons = more | vgood | 0.002406 |
| Safety = high and Buying = low and Persons = 4 and Maint = low and Lug_boot = big | vgood | 0.002670 |
| Safety = high and Doors = 4 and Lug_boot = med and Buying = low | vgood | 0.002008 |
| Safety = high and Buying = med and Persons = more and Maint = med and Lug_boot = big | vgood | 0.002670 |
| Safety = high and Buying = med and Maint = low and Persons = 4 and Lug_boot = big | vgood | 0.002004 |
| Safety = high and Lug_boot = med and Buying = low and Doors = 5more and Persons = 4 | vgood | 0.001504 |
| Safety = high and Lug_boot = med and Buying = med and Maint = med | vgood | 0.001396 |
| Safety = high and Buying = low and Doors = 3 and Persons = more and Lug_boot = med | vgood | 0.001504 |
| Buying = low and Maint = med and Persons = more and Safety = med | good | 0.003093 |
| Maint = low and Buying = low and Safety = high and Persons = 4 | good | 0.003467 |
| Maint = low and Buying = med and Persons = 4 and Safety = high | good | 0.003123 |
| Safety = med and Maint = low and Buying = med and Lug_boot = big and Persons = 4 | good | 0.002776 |
| Buying = low and Maint = med and Persons = 4 and Safety = high | good | 0.002776 |
| Buying = low and Maint = low and Safety = med and Lug_boot = big and Persons = 4 | good | 0.002776 |
| Maint = low and Buying = med and Safety = med and Persons = more | good | 0.002276 |
| Buying = low and Maint = low and Persons = more and Safety = high | good | 0.002222 |
| Buying = low and Safety = med and Maint = med and Persons = 4 and Lug_boot = big | good | 0.002083 |
| Safety = med and Buying = low and Maint = low and Persons = more | good | 0.002276 |
| Buying = low and Maint = med and Safety = high and Persons = more | good | 0.001564 |
| Safety = high and Persons = 4 and Maint = low | acc | 0.018876 |
| Safety = high and Persons = 4 and Buying = med | acc | 0.023209 |
| Safety = med and Persons = 4 and Buying = low | acc | 0.018936 |
| Safety = high and Persons = 4 and Maint = med | acc | 0.021352 |
| Persons = more and Safety = high and Maint = med | acc | 0.017301 |
| Safety = med and Persons = more and Lug_boot = big and Maint = med | acc | 0.009901 |
| Safety = med and Persons = 4 and Buying = med and Maint = med | acc | 0.010791 |
| Persons = more and Safety = high and Buying = med | acc | 0.010848 |
| Safety = med and Persons = more and Lug_boot = big and Maint = low | acc | 0.007220 |
| Safety = med and Persons = 4 and Lug_boot = big | acc | 0.015584 |
| Safety = high and Persons = more and Maint = low | acc | 0.014138 |
| Safety = med and Persons = more and Buying = med and Lug_boot = big | acc | 0.004525 |
| Safety = med and Persons = more and Lug_boot = med | acc | 0.017205 |
| Persons = 4 and Safety = med and Maint = low and Buying = med | acc | 0.004654 |
| Safety = high and Persons = 4 and Buying = low | acc | 0.015266 |
| Persons = more and Safety = high and Buying = low | acc | 0.008123 |
| Persons = 4 and Safety = med and Lug_boot = med and Doors = 4 | acc | 0.003423 |
| Maint = high and Buying = high and Safety = high | acc | 0.011635 |
| Safety = med and Buying = low and Persons = more and Lug_boot = big | acc | 0.005425 |
| Safety = med and Persons = 4 and Doors = 5more and Lug_boot = med | acc | 0.004039 |
| Persons = more and Safety = med and Maint = med and Buying = med | acc | 0.002042 |
|  | unacc | 0.979317 |


# Text representation of classifiers as-is

## JRip

Decision list:

rules | predicted class
---|---
(Safety = high) and (Buying = low) and (Persons = more) and (Lug_boot = big)|vgood (15.0/3.0)
(Safety = high) and (Buying = low) and (Maint = med) and (Persons = 4) and (Lug_boot = big)|vgood (3.0/0.0)
(Safety = high) and (Buying = med) and (Maint = med) and (Persons = 4) and (Lug_boot = big)|vgood (3.0/0.0)
(Safety = high) and (Buying = low) and (Lug_boot = med) and (Doors = 5more) and (Persons = more)|vgood (4.0/1.0)
(Safety = high) and (Maint = low) and (Buying = med) and (Persons = more)|vgood (10.0/4.0)
(Safety = high) and (Buying = low) and (Persons = 4) and (Maint = low) and (Lug_boot = big)|vgood (4.0/0.0)
(Safety = high) and (Doors = 4) and (Lug_boot = med) and (Buying = low)|vgood (12.0/6.0)
(Safety = high) and (Buying = med) and (Persons = more) and (Maint = med) and (Lug_boot = big)|vgood (4.0/0.0)
(Safety = high) and (Buying = med) and (Maint = low) and (Persons = 4) and (Lug_boot = big)|vgood (3.0/0.0)
(Safety = high) and (Lug_boot = med) and (Buying = low) and (Doors = 5more) and (Persons = 4)|vgood (4.0/1.0)
(Safety = high) and (Lug_boot = med) and (Buying = med) and (Maint = med)|vgood (12.0/7.0)
(Safety = high) and (Buying = low) and (Doors = 3) and (Persons = more) and (Lug_boot = med)|vgood (4.0/1.0)
(Buying = low) and (Maint = med) and (Persons = more) and (Safety = med)|good (11.0/4.0)
(Maint = low) and (Buying = low) and (Safety = high) and (Persons = 4)|good (5.0/0.0)
(Maint = low) and (Buying = med) and (Persons = 4) and (Safety = high)|good (8.0/2.0)
(Safety = med) and (Maint = low) and (Buying = med) and (Lug_boot = big) and (Persons = 4)|good (4.0/0.0)
(Buying = low) and (Maint = med) and (Persons = 4) and (Safety = high)|good (4.0/0.0)
(Buying = low) and (Maint = low) and (Safety = med) and (Lug_boot = big) and (Persons = 4)|good (4.0/0.0)
(Maint = low) and (Buying = med) and (Safety = med) and (Persons = more)|good (11.0/5.0)
(Buying = low) and (Maint = low) and (Persons = more) and (Safety = high)|good (5.0/1.0)
(Buying = low) and (Safety = med) and (Maint = med) and (Persons = 4) and (Lug_boot = big)|good (3.0/0.0)
(Safety = med) and (Buying = low) and (Maint = low) and (Persons = more)|good (11.0/5.0)
(Buying = low) and (Maint = med) and (Safety = high) and (Persons = more)|good (4.0/1.0)
(Safety = high) and (Persons = 4) and (Maint = low)|acc (23.0/0.0)
(Safety = high) and (Persons = 4) and (Buying = med)|acc (26.0/0.0)
(Safety = med) and (Persons = 4) and (Buying = low)|acc (37.0/9.0)
(Safety = high) and (Persons = 4) and (Maint = med)|acc (24.0/0.0)
(Persons = more) and (Safety = high) and (Maint = med)|acc (23.0/2.0)
(Safety = med) and (Persons = more) and (Lug_boot = big) and (Maint = med)|acc (11.0/0.0)
(Safety = med) and (Persons = 4) and (Buying = med) and (Maint = med)|acc (12.0/0.0)
(Persons = more) and (Safety = high) and (Buying = med)|acc (19.0/2.0)
(Safety = med) and (Persons = more) and (Lug_boot = big) and (Maint = low)|acc (8.0/0.0)
(Safety = med) and (Persons = 4) and (Lug_boot = big)|acc (36.0/11.0)
(Safety = high) and (Persons = more) and (Maint = low)|acc (23.0/2.0)
(Safety = med) and (Persons = more) and (Buying = med) and (Lug_boot = big)|acc (5.0/0.0)
(Safety = med) and (Persons = more) and (Lug_boot = med)|acc (44.0/17.0)
(Persons = 4) and (Safety = med) and (Maint = low) and (Buying = med)|acc (7.0/1.0)
(Safety = high) and (Persons = 4) and (Buying = low)|acc (17.0/1.0)
(Persons = more) and (Safety = high) and (Buying = low)|acc (8.0/2.0)
(Persons = 4) and (Safety = med) and (Lug_boot = med) and (Doors = 4)|acc (10.0/3.0)
(Maint = high) and (Buying = high) and (Safety = high)|acc (31.0/11.0)
(Safety = med) and (Buying = low) and (Persons = more) and (Lug_boot = big)|acc (6.0/0.0)
(Safety = med) and (Persons = 4) and (Doors = 5more) and (Lug_boot = med)|acc (10.0/3.0)
(Persons = more) and (Safety = med) and (Maint = med) and (Buying = med)|acc (4.0/1.0)
|unacc (1020.0/4.0)


## PART

Decision list:

rules | predicted class
---|---
Safety = low|unacc (528.0)
Persons = 2|unacc (339.0)
Maint = vhigh AND Buying = high|unacc (44.0)
Buying = vhigh AND Maint = vhigh|unacc (42.0)
Buying = vhigh AND Maint = high|unacc (42.0)
Safety = med AND Lug_boot = small AND Buying = high|unacc (22.0)
Safety = med AND Lug_boot = small AND Maint != vhigh AND Buying != vhigh AND Maint != high AND Doors != 2|acc (22.0)
Safety = med AND Lug_boot = small AND Maint = vhigh|unacc (16.0)
Safety = med AND Lug_boot = small AND Buying != low AND Doors != 2|unacc (15.0)
Buying = high AND Doors != 2 AND Doors != 3|acc (52.0)
Safety = med AND Lug_boot = big AND Maint != low AND Buying != low|acc (33.0)
Safety = med AND Lug_boot = big AND Buying != med AND Maint != med AND Maint != low|acc (13.0)
Safety != med AND Lug_boot != small AND Buying != vhigh AND Maint != vhigh AND Buying != high AND Maint != high AND Doors != 2 AND Doors != 3|vgood (31.0)
Buying = vhigh AND Doors != 2 AND Doors != 3|acc (34.0)
Maint = vhigh AND Doors != 2 AND Safety != med|acc (32.0)
Buying = high AND Safety != med AND Lug_boot != small|acc (23.0)
Lug_boot = big AND Safety = med AND Buying != vhigh AND Buying != high|good (21.0)
Lug_boot = big AND Buying = low AND Doors != 2|vgood (7.0)
Lug_boot = big AND Buying = vhigh|acc (11.0)
Lug_boot = big AND Maint != med AND Maint != low AND Buying = med|acc (9.0)
Lug_boot = big AND Buying != high AND Buying = med|vgood (6.0)
Doors != 2 AND Maint = high AND Buying != high AND Buying = med|acc (16.0)
Doors != 2 AND Maint = high AND Lug_boot = small|acc (12.0)
Lug_boot = big AND Buying = high|acc (4.0)
Lug_boot = big AND Persons != 4|vgood (4.0/1.0)
Doors = 2 AND Lug_boot != big AND Safety = med AND Buying != vhigh AND Buying != high AND Maint != vhigh AND Persons = 4 AND Maint != high|acc (8.0)
Doors = 2 AND Lug_boot != big AND Safety = med AND Buying != low AND Maint != low|unacc (13.0)
Buying = high AND Lug_boot != small AND Persons = 4|unacc (4.0)
Buying = vhigh AND Safety != med AND Doors != 2|acc (8.0)
Maint = vhigh AND Doors != 4 AND Doors != 5more AND Safety != med AND Persons = 4|acc (5.0)
Maint = high AND Lug_boot != small AND Safety = med|acc (8.0)
Maint = vhigh AND Doors != 4 AND Doors != 5more AND Persons != 4|acc (6.0/2.0)
Buying = vhigh AND Safety != med AND Persons = 4|acc (4.0)
Maint = high AND Doors != 2 AND Persons = 4|vgood (3.0/1.0)
Buying = vhigh AND Persons != 4 AND Safety = med|unacc (4.0/2.0)
Maint = vhigh AND Doors = 4|acc (4.0)
Maint = high AND Doors = 2 AND Persons = 4|acc (6.0)
Maint = high AND Lug_boot = small|unacc (4.0)
Maint = high|vgood (4.0/1.0)
Buying = vhigh AND Persons = 4|unacc (3.0)
Buying = high AND Doors != 2|acc (6.0)
Maint = vhigh AND Doors = 5more|acc (4.0)
Maint != vhigh AND Doors != 2 AND Maint != med AND Doors != 3|good (14.0)
Maint != vhigh AND Lug_boot = small AND Doors != 2 AND Buying != med|good (6.0)
Maint != vhigh AND Lug_boot = small AND Persons = 4 AND Maint != med|good (4.0/1.0)
Maint != vhigh AND Lug_boot = small AND Doors = 2 AND Maint = med|unacc (6.0/2.0)
Maint != vhigh AND Lug_boot = small AND Maint != med|unacc (6.0/1.0)
Maint != vhigh AND Lug_boot = small|acc (4.0)
Maint != vhigh AND Safety = med AND Doors = 2|acc (4.0/1.0)
Maint != vhigh AND Buying = low AND Safety = med AND Doors = 3|acc (4.0/2.0)
Maint != vhigh AND Buying = low AND Safety != med AND Doors = 2|good (6.0/2.0)
Maint != vhigh AND Buying = low AND Doors != 3|good (4.0)
Maint != vhigh AND Buying != low AND Maint = med AND Doors != 3|acc (6.0)
Maint = vhigh|unacc (3.0)
Persons = 4 AND Maint = med|acc (3.0/1.0)
Buying = med AND Persons != 4|vgood (4.0/2.0)
Buying = med|good (3.0/1.0)
|vgood (3.0/1.0)


## SimpleCart Decision Tree

	* Safety=(high)|(med)
		* Persons=(more)|(4)
			* Buying=(low)|(med)
				* Maint=(low)|(med)
				* Safety=(high)
						* Lug_boot=(big)|(med)
								* Doors=(5more)|(4)|(3)
									* Doors=(5more)|(4)|(2): vgood(31.0/0.0)
									* Doors!=(5more)|(4)|(2)
									* Persons=(more)|(2): vgood(7.0/0.0)
									* Persons!=(more)|(2)
										* Lug_boot=(big)|(small): vgood(3.0/0.0)
										* Lug_boot!=(big)|(small): good(2.0/1.0)
								* Doors!=(5more)|(4)|(3)
							* Lug_boot=(big): vgood(7.0/0.0)
							* Lug_boot!=(big)
										* Buying=(low)|(vhigh)|(high): good(4.0/0.0)
										* Buying!=(low)|(vhigh)|(high)
											* Maint=(low)|(vhigh)|(high): good(2.0/0.0)
											* Maint!=(low)|(vhigh)|(high): acc(2.0/0.0)
						* Lug_boot!=(big)|(med)
								* Maint=(low)|(vhigh)|(high)
									* Doors=(5more)|(4)|(3): good(12.0/0.0)
									* Doors!=(5more)|(4)|(3): good(2.0/1.0)
								* Maint!=(low)|(vhigh)|(high)
							* Buying=(low): good(4.0/1.0)
							* Buying!=(low)
										* Doors=(5more)|(4)|(3): acc(4.0/0.0)
										* Doors!=(5more)|(4)|(3): unacc(1.0/1.0)
				* Safety!=(high)
						* Lug_boot=(big)|(med)
								* Buying=(low)|(vhigh)|(high)
									* Doors=(5more)|(4)|(3)
										* Doors=(5more)|(4)|(2): good(14.0/0.0)
										* Doors!=(5more)|(4)|(2)
										* Persons=(more)|(2): good(4.0/0.0)
										* Persons!=(more)|(2)
											* Lug_boot=(big)|(small): good(2.0/0.0)
											* Lug_boot!=(big)|(small): acc(2.0/0.0)
									* Doors!=(5more)|(4)|(3)
								* Lug_boot=(big): good(3.0/0.0)
								* Lug_boot!=(big): acc(4.0/0.0)
								* Buying!=(low)|(vhigh)|(high)
									* Maint=(low)|(vhigh)|(high)
									* Lug_boot=(big)|(small): good(7.0/0.0)
									* Lug_boot!=(big)|(small)
										* Doors=(5more)|(4): good(3.0/0.0)
										* Doors!=(5more)|(4)
												* Doors=(3)|(4)|(5more): acc(1.0/1.0)
												* Doors!=(3)|(4)|(5more): acc(2.0/0.0)
									* Maint!=(low)|(vhigh)|(high): acc(13.0/0.0)
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
										* Doors=(5more)|(4)|(3)
											* Doors=(5more)|(4)|(2): vgood(6.0/0.0)
											* Doors!=(5more)|(4)|(2)
											* Persons=(more)|(2): vgood(2.0/0.0)
											* Persons!=(more)|(2): acc(1.0/1.0)
										* Doors!=(5more)|(4)|(3): acc(2.0/1.0)
							* Safety!=(high): acc(14.0/0.0)
						* Maint!=(high)
								* Safety=(high)|(low): acc(15.0/0.0)
								* Safety!=(high)|(low)
									* Doors=(5more)|(4): acc(7.0/0.0)
									* Doors!=(5more)|(4)
										* Lug_boot=(big)|(small): acc(4.0/0.0)
										* Lug_boot!=(big)|(small): unacc(2.0/1.0)
					* Buying!=(low)
								* Doors=(5more)|(4)|(3)
									* Doors=(5more)|(4)|(2): acc(30.0/0.0)
									* Doors!=(5more)|(4)|(2)
									* Lug_boot=(big)|(small): acc(8.0/0.0)
									* Lug_boot!=(big)|(small)
											* Maint=(high)|(med)|(low): acc(3.0/0.0)
											* Maint!=(high)|(med)|(low): acc(2.0/1.0)
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
									* Buying=(low)|(vhigh)|(high)
										* Doors=(5more)|(4)|(3): acc(5.0/0.0)
										* Doors!=(5more)|(4)|(3): unacc(1.0/1.0)
									* Buying!=(low)|(vhigh)|(high): unacc(7.0/0.0)
						* Maint!=(high): unacc(16.0/0.0)
			* Buying!=(low)|(med)
				* Maint=(low)|(med)
					* Lug_boot=(big)|(med)
					* Lug_boot=(big): acc(59.0/0.0)
					* Lug_boot!=(big)
							* Safety=(high)|(low): acc(30.0/0.0)
							* Safety!=(high)|(low)
								* Doors=(5more)|(4): acc(15.0/0.0)
								* Doors!=(5more)|(4)
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
							* Safety=(high)|(low)
									* Doors=(5more)|(4)|(3): acc(15.0/0.0)
									* Doors!=(5more)|(4)|(3)
									* Lug_boot=(big)|(med): acc(4.0/0.0)
									* Lug_boot!=(big)|(med): unacc(1.0/1.0)
							* Safety!=(high)|(low)
								* Lug_boot=(big)|(med)
									* Doors=(5more)|(4): acc(7.0/0.0)
									* Doors!=(5more)|(4): unacc(3.0/1.0)
								* Lug_boot!=(big)|(med): unacc(7.0/0.0)
					* Buying!=(high): unacc(42.0/0.0)
				* Maint!=(high): unacc(86.0/0.0)
		* Persons!=(more)|(4): unacc(339.0/0.0)
	* Safety!=(high)|(med): unacc(528.0/0.0)


