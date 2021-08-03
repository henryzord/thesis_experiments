# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Safety != high | unacc | 0.614062 |
| Safety != med | unacc | 0.592358 |
| Safety = med and Persons = 4 and Buying = med and Maint = med and Safety!=(high) and Lug_boot = med and Maint != high and Buying != low | acc | 0.003300 |
| Safety = med and Persons = 4 and Buying = med and Maint = med and Safety!=(high) and Lug_boot != med and Doors = 5more | acc | 0.001653 |
| Safety = med and Persons = 4 and Buying = med and Maint = med and Safety!=(high) and Lug_boot != med and Doors = 3 | acc | 0.001653 |
| Safety = med and Persons = 4 and Buying != med and Maint = med and Safety!=(high) and Lug_boot = med and Lug_boot != small and Doors = 5more | acc | 0.001103 |
| Safety = med and Persons = 4 and Buying = med and Maint != med and Safety!=(high) and Lug_boot = med and Doors = 5more | acc | 0.001103 |
| Safety = med and Persons = 4 and Buying = med and Maint = med and Safety!=(high) and Lug_boot != med and Doors = 4 | acc | 0.000827 |
| Safety = med and Persons = 4 and Buying = med and Maint != med and Safety!=(high) and Lug_boot = med and Doors = 4 | acc | 0.000414 |
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
| Safety = med and Maint = high and Buying = vhigh | unacc | 0.031315 |
| Safety = med and Lug_boot = big and Maint = high | acc | 0.102679 |
| Safety = med and Lug_boot = big and Buying = vhigh | acc | 0.065116 |
| Safety = med and Lug_boot = big and Maint = vhigh | acc | 0.065116 |
| Safety = med and Lug_boot = small and Maint = vhigh | unacc | 0.037296 |
| Buying = high and Safety = high and Doors = 4 | acc | 0.084158 |
| Buying = high and Safety = high and Doors = 3 | acc | 0.079602 |
| Buying = high and Doors = 5more | acc | 0.123223 |
| Safety = med and Lug_boot = small and Maint = med | acc | 0.062183 |
| Safety = med and Lug_boot = small and Buying = low | acc | 0.049485 |
| Buying = high and Lug_boot = big | acc | 0.075000 |
| Buying = vhigh and Maint = high | unacc | 0.068452 |
| Safety = high and Lug_boot = big and Buying = low and Persons = 4 | vgood | 0.026535 |
| Safety = high and Lug_boot = big and Buying = med | acc | 0.049669 |
| Safety = high and Lug_boot = big and Buying = vhigh | acc | 0.084848 |
| Safety = med and Lug_boot = big and Maint = low | good | 0.051852 |
| Safety = med and Buying = vhigh | acc | 0.038571 |
| Safety = med and Buying = high | unacc | 0.021344 |
| Maint = vhigh and Safety = high and Lug_boot = small | acc | 0.086224 |
| Safety = med and Maint = vhigh | acc | 0.047348 |
| Buying = vhigh and Lug_boot = small | acc | 0.081055 |
| Buying = vhigh | acc | 0.072464 |
| Maint = high and Safety = high and Lug_boot = med | acc | 0.072563 |
| Maint = high and Safety = high | acc | 0.069136 |
| Maint = vhigh | acc | 0.105070 |
| Safety = med and Buying = low and Persons = 4 | acc | 0.028219 |
| Safety = med and Maint = med | acc | 0.062500 |
| Safety = med and Maint = high | unacc | 0.042969 |
| Lug_boot = small and Buying = low | good | 0.087203 |
| Lug_boot = small and Persons = 4 | acc | 0.045370 |
| Lug_boot = med and Safety = high and Buying = med | vgood | 0.071839 |
| Buying = low and Maint = low | vgood | 0.042105 |
| Buying = med | acc | 0.061869 |
|  | vgood | 0.303030 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Safety = high and Persons = 4 and Buying = high and Maint = high | acc | 0.009836 |
| Safety = high and Persons = 4 and Buying = med | acc | 0.013908 |
| Persons = more and Safety = high and Buying = med | acc | 0.011963 |
| Safety = med and Persons = 4 and Lug_boot = big | acc | 0.017214 |
| Persons = more and Safety = high and Buying = high | acc | 0.015635 |
| Safety = med and Persons = more and Lug_boot = big | acc | 0.018973 |
| Safety = high and Persons = 4 and Maint = med | acc | 0.009168 |
| Safety = high and Persons = 4 and Maint = low | acc | 0.009106 |
| Safety = med and Persons = more and Lug_boot = med | acc | 0.014081 |
| Buying = low and Persons = 4 and Safety = med | acc | 0.009575 |
|  | unacc | 0.840927 |


# Text representation of classifiers as-is

## JRip

Decision list:

rules | predicted class
---|---
(Safety = high) and (Persons = 4) and (Buying = high) and (Maint = high)|acc (12.0/0.0)
(Safety = high) and (Persons = 4) and (Buying = med)|acc (43.0/16.0)
(Persons = more) and (Safety = high) and (Buying = med)|acc (43.0/18.0)
(Safety = med) and (Persons = 4) and (Lug_boot = big)|acc (55.0/21.0)
(Persons = more) and (Safety = high) and (Buying = high)|acc (41.0/13.0)
(Safety = med) and (Persons = more) and (Lug_boot = big)|acc (59.0/22.0)
(Safety = high) and (Persons = 4) and (Maint = med)|acc (31.0/11.0)
(Safety = high) and (Persons = 4) and (Maint = low)|acc (33.0/11.0)
(Safety = med) and (Persons = more) and (Lug_boot = med)|acc (60.0/28.0)
(Buying = low) and (Persons = 4) and (Safety = med)|acc (31.0/10.0)
|unacc (1145.0/119.0)


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
Safety = med AND Maint = high AND Buying = vhigh|unacc (15.0)
Safety = med AND Lug_boot = big AND Maint = high|acc (23.0)
Safety = med AND Lug_boot = big AND Buying = vhigh|acc (14.0)
Safety = med AND Lug_boot = big AND Maint = vhigh|acc (14.0)
Safety = med AND Lug_boot = small AND Maint = vhigh|unacc (16.0)
Buying = high AND Safety = high AND Doors = 4|acc (17.0)
Buying = high AND Safety = high AND Doors = 3|acc (16.0)
Buying = high AND Doors = 5more|acc (26.0)
Safety = med AND Lug_boot = small AND Maint = med|acc (16.0/2.0)
Safety = med AND Lug_boot = small AND Buying = low|acc (14.0/2.0)
Buying = high AND Lug_boot = big|acc (15.0)
Buying = vhigh AND Maint = high|unacc (23.0)
Safety = high AND Lug_boot = big AND Buying = low AND Persons = 4|vgood (15.0/4.0)
Safety = high AND Lug_boot = big AND Buying = med|acc (30.0/15.0)
Safety = high AND Lug_boot = big AND Buying = vhigh|acc (14.0)
Safety = med AND Lug_boot = big AND Maint = low|good (14.0)
Safety = med AND Buying = vhigh|acc (15.0/6.0)
Safety = med AND Buying = high|unacc (15.0/6.0)
Maint = vhigh AND Safety = high AND Lug_boot = small|acc (14.0/1.0)
Safety = med AND Maint = vhigh|acc (16.0/6.0)
Buying = vhigh AND Lug_boot = small|acc (15.0/2.0)
Buying = vhigh|acc (15.0)
Maint = high AND Safety = high AND Lug_boot = med|acc (17.0/4.0)
Maint = high AND Safety = high|acc (17.0/3.0)
Maint = vhigh|acc (16.0)
Safety = med AND Buying = low AND Persons = 4|acc (16.0/8.0)
Safety = med AND Maint = med|acc (20.0/5.0)
Safety = med AND Maint = high|unacc (18.0/8.0)
Lug_boot = small AND Buying = low|good (14.0/1.0)
Lug_boot = small AND Persons = 4|acc (10.0/3.0)
Lug_boot = med AND Safety = high AND Buying = med|vgood (16.0/6.0)
Buying = low AND Maint = low|vgood (15.0/7.0)
Buying = med|acc (16.0/9.0)
|vgood (14.0/6.0)


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
										* Maint=(low)|(vhigh)|(high): good(6.0/2.0)
										* Maint!=(low)|(vhigh)|(high): acc(3.0/4.0)
						* Lug_boot!=(big)|(med)
								* Buying=(low)|(vhigh)|(high): good(13.0/1.0)
								* Buying!=(low)|(vhigh)|(high)
							* Maint=(low): good(4.0/1.0)
							* Maint!=(low): acc(6.0/1.0)
				* Safety!=(high)
						* Lug_boot=(big)|(med)
								* Maint=(low)|(vhigh)|(high)
								* Doors=(5more)|(4): good(15.0/0.0)
								* Doors!=(5more)|(4)
									* Lug_boot=(big)|(small): good(7.0/0.0)
									* Lug_boot!=(big)|(small): acc(5.0/2.0)
								* Maint!=(low)|(vhigh)|(high)
									* Buying=(low)|(vhigh)|(high)
									* Doors=(5more)|(4): good(7.0/0.0)
									* Doors!=(5more)|(4): good(4.0/3.0)
									* Buying!=(low)|(vhigh)|(high): acc(14.0/0.0)
						* Lug_boot!=(big)|(med)
								* Doors=(5more)|(4)|(3): acc(21.0/0.0)
								* Doors!=(5more)|(4)|(3): unacc(4.0/4.0)
				* Maint!=(low)|(med)
				* Safety=(high)
					* Buying=(low)
								* Maint=(high)|(med)|(low)
								* Lug_boot=(big)|(med)
									* Lug_boot=(big)|(small): vgood(7.0/0.0)
									* Lug_boot!=(big)|(small): vgood(4.0/3.0)
								* Lug_boot!=(big)|(med): acc(7.0/0.0)
								* Maint!=(high)|(med)|(low)
									* Doors=(5more)|(4)|(3): acc(15.0/0.0)
									* Doors!=(5more)|(4)|(3): acc(4.0/1.0)
					* Buying!=(low): acc(43.0/0.0)
				* Safety!=(high)
						* Lug_boot=(big)|(med)
							* Doors=(5more)|(4): acc(29.0/0.0)
							* Doors!=(5more)|(4)
							* Lug_boot=(big): acc(15.0/0.0)
							* Lug_boot!=(big)
										* Buying=(low)|(vhigh)|(high): acc(5.0/3.0)
										* Buying!=(low)|(vhigh)|(high): unacc(6.0/2.0)
						* Lug_boot!=(big)|(med)
						* Maint=(high)
									* Buying=(low)|(vhigh)|(high): acc(6.0/1.0)
									* Buying!=(low)|(vhigh)|(high): unacc(7.0/0.0)
						* Maint!=(high): unacc(16.0/0.0)
			* Buying!=(low)|(med)
				* Maint=(low)|(med)
				* Safety=(high)
							* Doors=(5more)|(4)|(3): acc(65.0/0.0)
							* Doors!=(5more)|(4)|(3)
							* Lug_boot=(big)|(med): acc(14.0/0.0)
							* Lug_boot!=(big)|(med): unacc(3.0/3.0)
				* Safety!=(high)
						* Lug_boot=(big)|(med)
							* Lug_boot=(big)|(small): acc(28.0/0.0)
							* Lug_boot!=(big)|(small)
								* Doors=(5more)|(4): acc(13.0/0.0)
								* Doors!=(5more)|(4)
								* Doors=(3): unacc(4.0/3.0)
								* Doors!=(3): unacc(8.0/0.0)
						* Lug_boot!=(big)|(med): unacc(30.0/0.0)
				* Maint!=(low)|(med)
				* Maint=(high)
							* Buying=(high)|(med)|(low)
						* Safety=(high): acc(21.0/0.0)
						* Safety!=(high)
								* Lug_boot=(big)|(med)
									* Doors=(5more)|(4): acc(8.0/0.0)
									* Doors!=(5more)|(4): acc(5.0/3.0)
								* Lug_boot!=(big)|(med): unacc(8.0/0.0)
							* Buying!=(high)|(med)|(low): unacc(45.0/0.0)
				* Maint!=(high): unacc(92.0/0.0)
		* Persons!=(more)|(4): unacc(333.0/0.0)
	* Safety!=(high)|(med): unacc(522.0/0.0)


