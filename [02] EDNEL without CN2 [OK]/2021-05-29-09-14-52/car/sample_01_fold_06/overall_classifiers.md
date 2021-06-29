# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Persons != 4 | unacc | 0.605194 |
| Persons != more | unacc | 0.602189 |
| Persons = 4 and Safety = med and Buying != med and Maint != med and Buying = low and Maint = high | acc | 0.009031 |
| Persons = 4 and Safety = med and Buying = med and Maint = med and Safety!=(high) and Lug_boot != med | acc | 0.005766 |
| Persons = 4 and Safety = med and Buying = med and Maint != med and Lug_boot = med and Buying!=(low) | acc | 0.001657 |
| Persons = 4 and Safety = med and Buying != med and Maint != med and Buying = low and Maint = low | acc | 0.002709 |
| Persons = 4 and Safety = med and Buying = med and Maint = med and Safety!=(high) and Lug_boot != big | acc | 0.004946 |
| Persons = 4 and Safety = med and Buying != med and Maint = med and Lug_boot = med and Doors = 5more | acc | 0.001104 |
| Persons = 4 and Safety = med and Buying != med and Maint = med and Lug_boot = med and Doors = 4 | acc | 0.000828 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Safety = low | unacc | 0.523172 |
| Persons = 2 | unacc | 0.430504 |
| Buying = vhigh and Maint = vhigh | unacc | 0.084980 |
| Buying = high and Maint = vhigh | unacc | 0.084980 |
| Safety = med and Lug_boot = small and Buying = vhigh | unacc | 0.047325 |
| Safety = med and Lug_boot = small and Buying = high | unacc | 0.047325 |
| Buying = high and Doors = 4 | acc | 0.117886 |
| Safety = med and Maint = high and Buying = vhigh | unacc | 0.031250 |
| Safety = med and Lug_boot = big and Maint = high | acc | 0.097778 |
| Safety = med and Lug_boot = big and Buying = vhigh | acc | 0.060185 |
| Safety = med and Lug_boot = big and Maint = vhigh | acc | 0.064516 |
| Safety = med and Lug_boot = big and Buying = low | good | 0.033019 |
| Safety = med and Maint = vhigh and Lug_boot = small | unacc | 0.038860 |
| Buying = high and Safety = high and Lug_boot = med | acc | 0.093750 |
| Buying = high and Lug_boot = big | acc | 0.125628 |
| Maint = vhigh and Safety = high and Doors = 3 | acc | 0.064516 |
| Buying = high and Doors = 5more | acc | 0.049180 |
| Buying = vhigh and Maint = high | unacc | 0.064024 |
| Safety = med and Lug_boot = small and Maint = low and Doors = 2 | unacc | 0.003257 |
| Safety = med and Lug_boot = small and Maint = low | acc | 0.084848 |
| Safety = med and Maint = vhigh and Doors = 2 | unacc | 0.013468 |
| Safety = med and Maint = vhigh and Persons = 4 | acc | 0.012162 |
| Safety = med and Maint = vhigh | acc | 0.023810 |
| Safety = med and Maint = high and Buying = low and Doors = 2 | acc | 0.015101 |
| Safety = med and Maint = high and Buying = low | acc | 0.058275 |
| Safety = med and Maint = high and Lug_boot = small | unacc | 0.032028 |
| Buying = vhigh and Safety = high and Doors = 5more | acc | 0.073826 |
| Buying = vhigh and Safety = high and Lug_boot = big | acc | 0.073826 |
| Buying = vhigh and Doors = 4 | acc | 0.061224 |
| Buying = vhigh and Doors = 3 and Persons = more | acc | 0.041667 |
| Maint = vhigh and Doors = 4 | acc | 0.080000 |
| Buying = vhigh and Doors = 2 and Safety = high | acc | 0.025329 |
| Safety = med and Buying = high and Doors = 2 | unacc | 0.026786 |
| Safety = med and Maint = high and Persons = more | acc | 0.023704 |
| Lug_boot = small and Maint = high and Persons = 4 | acc | 0.063830 |
| Safety = med and Maint = med and Buying = med and Lug_boot = big | acc | 0.057143 |
| Safety = med and Lug_boot = big | good | 0.042781 |
| Lug_boot = big and Maint = med | vgood | 0.086207 |
| Lug_boot = big and Maint = low | vgood | 0.086207 |
| Buying = high and Doors = 3 and Persons = 4 | unacc | 0.011250 |
| Maint = vhigh and Doors = 5more | acc | 0.107843 |
| Buying = high and Doors = 2 | unacc | 0.012081 |
| Buying = high | acc | 0.092784 |
| Buying = vhigh and Doors = 2 | unacc | 0.041379 |
| Maint = vhigh and Buying = med | acc | 0.031746 |
| Maint = high and Buying = med and Doors = 2 | acc | 0.027539 |
| Safety = med and Lug_boot = small and Doors = 3 | acc | 0.046512 |
| Lug_boot = big and Buying = med | acc | 0.068182 |
| Safety = med and Doors = 2 and Persons = more | acc | 0.027539 |
| Lug_boot = big and Persons = 4 | vgood | 0.029630 |
| Safety = med and Buying = med and Maint = med | acc | 0.104493 |
| Lug_boot = small and Maint = low and Persons = 4 | good | 0.079545 |
| Lug_boot = small and Maint = low | good | 0.042517 |
| Safety = med and Persons = more and Doors = 5more | acc | 0.022727 |
| Lug_boot = small and Buying = med and Persons = 4 | acc | 0.057143 |
| Safety = med and Persons = more | good | 0.078870 |
| Lug_boot = small and Maint = med and Persons = 4 | acc | 0.026316 |
| Maint = high and Buying = med and Persons = 4 | acc | 0.045198 |
| Lug_boot = small and Maint = high | acc | 0.045198 |
| Safety = med and Doors = 3 | acc | 0.020455 |
| Lug_boot = med and Doors = 4 and Persons = 4 | vgood | 0.057143 |
| Lug_boot = med and Doors = 2 and Maint = low | good | 0.045977 |
| Lug_boot = med and Doors = 2 | acc | 0.100629 |
| Lug_boot = med and Persons = more and Buying = low | vgood | 0.165306 |
| Lug_boot = med and Buying = med | vgood | 0.050607 |
| Doors = 5more and Safety = high | vgood | 0.054422 |
| Lug_boot = med | acc | 0.096838 |
|  | unacc | 0.444444 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Safety = high and Buying = low and Lug_boot = big and Persons = 4 | vgood | 0.005992 |
| Safety = high and Buying = low and Persons = more and Lug_boot = big | vgood | 0.005374 |
| Safety = high and Buying = low and Lug_boot = med and Persons = more | vgood | 0.003384 |
| Safety = high and Buying = med and Lug_boot = big and Maint = med | vgood | 0.002976 |
| Buying = low and Maint = low and Safety = med and Lug_boot = big | good | 0.003363 |
| Maint = low and Buying = med and Safety = med and Lug_boot = big | good | 0.003991 |
| Persons = 4 and Safety = high | acc | 0.052284 |
| Safety = med and Persons = more and Lug_boot = big | acc | 0.021720 |
| Safety = med and Persons = 4 and Lug_boot = big and Buying = med | acc | 0.010300 |
| Safety = med and Persons = 4 and Buying = low and Maint = high | acc | 0.009450 |
| Persons = more and Safety = high | acc | 0.041547 |
| Safety = med and Persons = 4 and Maint = low | acc | 0.012304 |
| Safety = med and Persons = more and Lug_boot = med and Maint = med | acc | 0.006525 |
| Safety = med and Persons = more and Buying = low | acc | 0.006300 |
| Safety = med and Persons = 4 and Maint = med | acc | 0.010990 |
|  | unacc | 0.918987 |


# Text representation of classifiers as-is

## JRip

Decision list:

rules | predicted class
---|---
(Safety = high) and (Buying = low) and (Lug_boot = big) and (Persons = 4)|vgood (16.0/4.0)
(Safety = high) and (Buying = low) and (Persons = more) and (Lug_boot = big)|vgood (15.0/4.0)
(Safety = high) and (Buying = low) and (Lug_boot = med) and (Persons = more)|vgood (16.0/7.0)
(Safety = high) and (Buying = med) and (Lug_boot = big) and (Maint = med)|vgood (11.0/4.0)
(Buying = low) and (Maint = low) and (Safety = med) and (Lug_boot = big)|good (10.0/3.0)
(Maint = low) and (Buying = med) and (Safety = med) and (Lug_boot = big)|good (11.0/3.0)
(Persons = 4) and (Safety = high)|acc (153.0/58.0)
(Safety = med) and (Persons = more) and (Lug_boot = big)|acc (48.0/13.0)
(Safety = med) and (Persons = 4) and (Lug_boot = big) and (Buying = med)|acc (12.0/0.0)
(Safety = med) and (Persons = 4) and (Buying = low) and (Maint = high)|acc (11.0/0.0)
(Persons = more) and (Safety = high)|acc (137.0/61.0)
(Safety = med) and (Persons = 4) and (Maint = low)|acc (37.0/14.0)
(Safety = med) and (Persons = more) and (Lug_boot = med) and (Maint = med)|acc (16.0/5.0)
(Safety = med) and (Persons = more) and (Buying = low)|acc (25.0/10.0)
(Safety = med) and (Persons = 4) and (Maint = med)|acc (38.0/16.0)
|unacc (996.0/35.0)


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
Safety = med AND Lug_boot = big AND Buying = vhigh|acc (13.0)
Safety = med AND Lug_boot = big AND Maint = vhigh|acc (14.0)
Safety = med AND Lug_boot = big AND Buying = low|good (14.0)
Safety = med AND Maint = vhigh AND Lug_boot = small|unacc (15.0)
Buying = high AND Safety = high AND Lug_boot = med|acc (18.0)
Buying = high AND Lug_boot = big|acc (25.0)
Maint = vhigh AND Safety = high AND Doors = 3|acc (12.0)
Buying = high AND Doors = 5more|acc (9.0)
Buying = vhigh AND Maint = high|unacc (21.0)
Safety = med AND Lug_boot = small AND Maint = low AND Doors = 2|unacc (4.0/2.0)
Safety = med AND Lug_boot = small AND Maint = low|acc (12.0)
Safety = med AND Maint = vhigh AND Doors = 2|unacc (4.0)
Safety = med AND Maint = vhigh AND Persons = 4|acc (5.0/2.0)
Safety = med AND Maint = vhigh|acc (5.0)
Safety = med AND Maint = high AND Buying = low AND Doors = 2|acc (4.0/1.0)
Safety = med AND Maint = high AND Buying = low|acc (10.0)
Safety = med AND Maint = high AND Lug_boot = small|unacc (8.0)
Buying = vhigh AND Safety = high AND Doors = 5more|acc (11.0)
Buying = vhigh AND Safety = high AND Lug_boot = big|acc (11.0)
Buying = vhigh AND Doors = 4|acc (9.0)
Buying = vhigh AND Doors = 3 AND Persons = more|acc (6.0)
Maint = vhigh AND Doors = 4|acc (12.0)
Buying = vhigh AND Doors = 2 AND Safety = high|acc (7.0/2.0)
Safety = med AND Buying = high AND Doors = 2|unacc (6.0)
Safety = med AND Maint = high AND Persons = more|acc (5.0/1.0)
Lug_boot = small AND Maint = high AND Persons = 4|acc (9.0)
Safety = med AND Maint = med AND Buying = med AND Lug_boot = big|acc (8.0)
Safety = med AND Lug_boot = big|good (8.0)
Lug_boot = big AND Maint = med|vgood (15.0)
Lug_boot = big AND Maint = low|vgood (15.0)
Buying = high AND Doors = 3 AND Persons = 4|unacc (5.0/2.0)
Maint = vhigh AND Doors = 5more|acc (11.0)
Buying = high AND Doors = 2|unacc (5.0/2.0)
Buying = high|acc (5.0)
Buying = vhigh AND Doors = 2|unacc (4.0)
Maint = vhigh AND Buying = med|acc (5.0/1.0)
Maint = high AND Buying = med AND Doors = 2|acc (6.0/2.0)
Safety = med AND Lug_boot = small AND Doors = 3|acc (4.0)
Lug_boot = big AND Buying = med|acc (6.0)
Safety = med AND Doors = 2 AND Persons = more|acc (6.0/2.0)
Lug_boot = big AND Persons = 4|vgood (5.0/1.0)
Safety = med AND Buying = med AND Maint = med|acc (10.0)
Lug_boot = small AND Maint = low AND Persons = 4|good (7.0)
Lug_boot = small AND Maint = low|good (7.0/2.0)
Safety = med AND Persons = more AND Doors = 5more|acc (6.0/3.0)
Lug_boot = small AND Buying = med AND Persons = 4|acc (4.0)
Safety = med AND Persons = more|good (7.0/1.0)
Lug_boot = small AND Maint = med AND Persons = 4|acc (6.0/3.0)
Maint = high AND Buying = med AND Persons = 4|acc (5.0/1.0)
Lug_boot = small AND Maint = high|acc (5.0/1.0)
Safety = med AND Doors = 3|acc (5.0/2.0)
Lug_boot = med AND Doors = 4 AND Persons = 4|vgood (5.0/1.0)
Lug_boot = med AND Doors = 2 AND Maint = low|good (6.0/2.0)
Lug_boot = med AND Doors = 2|acc (8.0/2.0)
Lug_boot = med AND Persons = more AND Buying = low|vgood (9.0)
Lug_boot = med AND Buying = med|vgood (9.0/4.0)
Doors = 5more AND Safety = high|vgood (6.0/2.0)
Lug_boot = med|acc (8.0/4.0)
|unacc (7.0/5.0)


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
								* Doors!=(5more)|(4): good(9.0/7.0)
						* Lug_boot!=(big)|(med): good(17.0/9.0)
				* Safety!=(high)
						* Lug_boot=(big)|(med)
								* Buying=(low)|(vhigh)|(high): good(23.0/6.0)
								* Buying!=(low)|(vhigh)|(high)
							* Maint=(low): good(11.0/3.0)
							* Maint!=(low): acc(15.0/0.0)
						* Lug_boot!=(big)|(med): acc(26.0/4.0)
				* Maint!=(low)|(med)
					* Lug_boot=(big)|(med)
					* Buying=(low)
								* Maint=(high)|(med)|(low)
								* Safety=(high)|(low): vgood(12.0/3.0)
								* Safety!=(high)|(low): acc(14.0/0.0)
								* Maint!=(high)|(med)|(low): acc(25.0/3.0)
					* Buying!=(low): acc(53.0/6.0)
					* Lug_boot!=(big)|(med)
					* Safety=(high): acc(26.0/3.0)
					* Safety!=(high): unacc(24.0/7.0)
			* Buying!=(low)|(med)
				* Maint=(low)|(med)
					* Lug_boot=(big)|(med)
						* Doors=(5more)|(4): acc(57.0/0.0)
						* Doors!=(5more)|(4)
							* Safety=(high)|(low): acc(28.0/0.0)
							* Safety!=(high)|(low)
							* Lug_boot=(big): acc(12.0/0.0)
							* Lug_boot!=(big): unacc(12.0/4.0)
					* Lug_boot!=(big)|(med)
					* Safety=(high): acc(25.0/4.0)
					* Safety!=(high): unacc(30.0/0.0)
				* Maint!=(low)|(med)
						* Buying=(high)|(med)|(low)
							* Maint=(high)|(med)|(low): acc(33.0/12.0)
							* Maint!=(high)|(med)|(low): unacc(43.0/0.0)
						* Buying!=(high)|(med)|(low): unacc(86.0/0.0)
		* Safety!=(high)|(med): unacc(334.0/0.0)
	* Persons!=(more)|(4): unacc(524.0/0.0)


