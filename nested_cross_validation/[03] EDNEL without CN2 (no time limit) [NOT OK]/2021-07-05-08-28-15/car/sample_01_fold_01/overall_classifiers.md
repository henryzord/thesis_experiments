# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Persons != 4 | unacc | 0.603276 |
| Persons != more | unacc | 0.602607 |
| Buying = high and Persons = more and Safety = high | acc | 0.019691 |
| Buying = high and Persons = 4 and Safety = high | acc | 0.017890 |
| Buying = med and Persons = more and Safety = med | acc | 0.014227 |
| Buying = med and Persons = 4 and Safety = med | acc | 0.013481 |
| Buying = low and Persons = 4 and Safety = med | acc | 0.014562 |
| Buying = low and Persons = more and Safety = med | acc | 0.012635 |
| Buying = med and Persons = more and Safety = high | acc | 0.010801 |
| Buying = med and Persons = 4 and Safety = high | acc | 0.011297 |
| Buying = low and Persons = more and Safety = high | vgood | 0.005067 |
| Buying = low and Persons = 4 and Safety = high | vgood | 0.003926 |
| Persons = 4 and Safety = med and Buying != med and Maint = med and Lug_boot = med and Safety != low and Lug_boot!=(big) and Doors = 5more | acc | 0.001653 |
| Persons = 4 and Safety = med and Buying != med and Maint = med and Lug_boot = med and Safety != low and Lug_boot!=(big) and Doors = 4 | acc | 0.001103 |

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
| Buying = high and Doors = 4 | acc | 0.118143 |
| Safety = med and Maint = high and Buying = low | acc | 0.095418 |
| Buying = high and Lug_boot = big | acc | 0.125523 |
| Buying = high and Safety = high and Lug_boot = med | acc | 0.075221 |
| Safety = med and Maint = high and Buying = vhigh | unacc | 0.036842 |
| Maint = vhigh and Lug_boot = big | acc | 0.125561 |
| Buying = vhigh and Maint = low | acc | 0.118920 |
| Maint = vhigh and Safety = high and Lug_boot = med | acc | 0.071429 |
| Safety = med and Lug_boot = small and Maint = low | acc | 0.058316 |
| Maint = vhigh and Safety = high and Doors = 5more | acc | 0.020101 |
| Maint = vhigh and Safety = high and Persons = 4 | acc | 0.020101 |
| Maint = vhigh and Lug_boot = small and Safety = med | unacc | 0.042105 |
| Maint = vhigh and Doors = 4 | acc | 0.031746 |
| Buying = high and Doors = 5more | acc | 0.056701 |
| Maint = vhigh and Doors = 2 | unacc | 0.019157 |
| Buying = vhigh and Maint = high | unacc | 0.079137 |
| Safety = med and Maint = vhigh and Doors = 5more | acc | 0.025000 |
| Safety = med and Maint = high and Lug_boot = big | acc | 0.048780 |
| Safety = med and Maint = high and Lug_boot = small | unacc | 0.020080 |
| Safety = med and Maint = vhigh and Persons = 4 | unacc | 0.008130 |
| Safety = med and Maint = high and Doors = 2 | unacc | 0.016129 |
| Safety = med and Buying = vhigh | acc | 0.061365 |
| Buying = vhigh | acc | 0.104310 |
| Safety = med and Buying = high and Persons = 4 | unacc | 0.023364 |
| Safety = med and Maint = low and Lug_boot = big | good | 0.071038 |
| Safety = med and Buying = med | acc | 0.148148 |
| Lug_boot = big and Safety = high and Maint = med | vgood | 0.109589 |
| Lug_boot = big and Safety = high and Maint = low | vgood | 0.090909 |
| Lug_boot = small and Maint = high and Doors = 3 | acc | 0.048544 |
| Lug_boot = small and Maint = high and Persons = 4 | acc | 0.057692 |
| Lug_boot = small and Doors = 3 and Buying = low and Safety = high | good | 0.030476 |
| Lug_boot = small and Doors = 3 and Maint = med | acc | 0.060000 |
| Lug_boot = small and Persons = 4 and Buying = low | good | 0.050919 |
| Lug_boot = small and Doors = 4 | acc | 0.034722 |
| Lug_boot = small and Doors = 3 and Buying = high | acc | 0.022222 |
| Lug_boot = small and Doors = 5more and Maint = med | acc | 0.014981 |
| Lug_boot = small and Doors = 5more and Maint = low | good | 0.033333 |
| Lug_boot = small and Doors = 2 and Persons = more | unacc | 0.122807 |
| Safety = med and Buying = low and Lug_boot = big | good | 0.087500 |
| Safety = med and Doors = 3 | acc | 0.050350 |
| Maint = high and Buying = med | acc | 0.190618 |
| Safety = med and Doors = 2 | acc | 0.031250 |
| Safety = high and Doors = 4 | vgood | 0.181132 |
| Lug_boot = small and Buying = med | good | 0.084211 |
| Safety = high and Lug_boot = med and Doors = 5more | vgood | 0.183673 |
| Lug_boot = med and Maint = low | good | 0.284034 |
| Lug_boot = med and Doors = 2 | acc | 0.043478 |
| Safety = high and Lug_boot = big | vgood | 0.142857 |
| Safety = high and Persons = 4 | acc | 0.142857 |
| Safety = high | vgood | 0.120192 |
|  | good | 0.526316 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Safety = high and Maint = med and Lug_boot = big and Buying = med | vgood | 0.003881 |
| Safety = high and Buying = low and Lug_boot = big and Persons = more | vgood | 0.004762 |
| Safety = high and Buying = low and Persons = 4 and Lug_boot = big | vgood | 0.005125 |
| Safety = high and Persons = more and Buying = low and Lug_boot = med | vgood | 0.003289 |
| Buying = med and Safety = high and Maint = low and Lug_boot = big | vgood | 0.002976 |
| Maint = med and Safety = high and Buying = med and Lug_boot = med | vgood | 0.001673 |
| Buying = low and Maint = med and Persons = more and Safety = med | good | 0.002822 |
| Maint = low and Persons = 4 and Buying = low and Safety = high | good | 0.003106 |
| Maint = low and Buying = med and Safety = med and Persons = more | good | 0.002263 |
| Maint = low and Buying = med and Persons = 4 and Safety = high | good | 0.003106 |
| Buying = low and Maint = low and Safety = med and Lug_boot = big | good | 0.003076 |
| Buying = low and Safety = high and Maint = med and Persons = 4 | good | 0.003106 |
| Buying = low and Safety = high and Persons = more | good | 0.001367 |
| Safety = high and Persons = 4 and Buying = med | acc | 0.019484 |
| Persons = more and Safety = med and Buying = low | acc | 0.017548 |
| Safety = high and Persons = more and Maint = med | acc | 0.018972 |
| Persons = 4 and Safety = med and Lug_boot = big | acc | 0.023519 |
| Safety = high and Persons = 4 and Maint = med | acc | 0.016908 |
| Persons = more and Safety = high and Maint = low and Buying = high | acc | 0.008963 |
| Persons = more and Safety = med and Lug_boot = big and Buying = med | acc | 0.008889 |
| Persons = more and Safety = high and Buying = med and Maint = vhigh | acc | 0.008088 |
| Safety = med and Persons = more and Lug_boot = med | acc | 0.013251 |
| Persons = 4 and Safety = high and Maint = low | acc | 0.015583 |
| Safety = med and Persons = 4 and Buying = low | acc | 0.011075 |
| Safety = high and Persons = more and Maint = high and Buying = med | acc | 0.008963 |
| Safety = high and Persons = 4 and Buying = low | acc | 0.010343 |
| Persons = more and Safety = high and Maint = low and Buying = vhigh | acc | 0.008088 |
| Safety = med and Maint = med and Buying = med and Persons = 4 | acc | 0.005352 |
| Safety = med and Persons = more and Lug_boot = big and Maint = med | acc | 0.007124 |
| Maint = high and Buying = high and Safety = high and Persons = more | acc | 0.008963 |
| Persons = 4 and Safety = high and Maint = high and Buying = high | acc | 0.008007 |
| Safety = med and Persons = 4 and Lug_boot = med and Doors = 4 | acc | 0.002691 |
| Safety = med and Doors = 5more and Persons = 4 and Lug_boot = med | acc | 0.003656 |
| Safety = med and Persons = more and Lug_boot = big and Maint = low | acc | 0.003575 |
|  | unacc | 0.953590 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

buying|persons|safety|acceptability
---|---|---|---
med|more|high|acc
vhigh|more|high|unacc
high|more|high|acc
low|more|high|vgood
low|4|high|vgood
med|4|high|acc
high|4|high|acc
vhigh|4|high|unacc
low|more|med|acc
med|2|high|unacc
vhigh|2|high|unacc
vhigh|more|med|unacc
high|more|med|unacc
med|more|med|acc
low|2|high|unacc
high|2|high|unacc
low|4|med|acc
med|4|med|acc
high|4|med|unacc
vhigh|4|med|unacc
med|2|med|unacc
low|more|low|unacc
high|more|low|unacc
vhigh|2|med|unacc
vhigh|more|low|unacc
med|more|low|unacc
high|2|med|unacc
low|2|med|unacc
high|4|low|unacc
low|4|low|unacc
vhigh|4|low|unacc
med|4|low|unacc
vhigh|2|low|unacc
low|2|low|unacc
high|2|low|unacc
med|2|low|unacc

## JRip

Decision list:

rules | predicted class
---|---
(Safety = high) and (Maint = med) and (Lug_boot = big) and (Buying = med)|vgood (11.0/3.0)
(Safety = high) and (Buying = low) and (Lug_boot = big) and (Persons = more)|vgood (14.0/4.0)
(Safety = high) and (Buying = low) and (Persons = 4) and (Lug_boot = big)|vgood (13.0/3.0)
(Safety = high) and (Persons = more) and (Buying = low) and (Lug_boot = med)|vgood (13.0/5.0)
(Buying = med) and (Safety = high) and (Maint = low) and (Lug_boot = big)|vgood (11.0/4.0)
(Maint = med) and (Safety = high) and (Buying = med) and (Lug_boot = med)|vgood (10.0/5.0)
(Buying = low) and (Maint = med) and (Persons = more) and (Safety = med)|good (12.0/5.0)
(Maint = low) and (Persons = 4) and (Buying = low) and (Safety = high)|good (8.0/2.0)
(Maint = low) and (Buying = med) and (Safety = med) and (Persons = more)|good (11.0/5.0)
(Maint = low) and (Buying = med) and (Persons = 4) and (Safety = high)|good (8.0/2.0)
(Buying = low) and (Maint = low) and (Safety = med) and (Lug_boot = big)|good (11.0/4.0)
(Buying = low) and (Safety = high) and (Maint = med) and (Persons = 4)|good (8.0/2.0)
(Buying = low) and (Safety = high) and (Persons = more)|good (16.0/10.0)
(Safety = high) and (Persons = 4) and (Buying = med)|acc (23.0/0.0)
(Persons = more) and (Safety = med) and (Buying = low)|acc (29.0/7.0)
(Safety = high) and (Persons = more) and (Maint = med)|acc (27.0/3.0)
(Persons = 4) and (Safety = med) and (Lug_boot = big)|acc (54.0/16.0)
(Safety = high) and (Persons = 4) and (Maint = med)|acc (21.0/0.0)
(Persons = more) and (Safety = high) and (Maint = low) and (Buying = high)|acc (12.0/1.0)
(Persons = more) and (Safety = med) and (Lug_boot = big) and (Buying = med)|acc (10.0/0.0)
(Persons = more) and (Safety = high) and (Buying = med) and (Maint = vhigh)|acc (11.0/1.0)
(Safety = med) and (Persons = more) and (Lug_boot = med)|acc (39.0/15.0)
(Persons = 4) and (Safety = high) and (Maint = low)|acc (21.0/0.0)
(Safety = med) and (Persons = 4) and (Buying = low)|acc (26.0/7.0)
(Safety = high) and (Persons = more) and (Maint = high) and (Buying = med)|acc (12.0/1.0)
(Safety = high) and (Persons = 4) and (Buying = low)|acc (15.0/2.0)
(Persons = more) and (Safety = high) and (Maint = low) and (Buying = vhigh)|acc (11.0/1.0)
(Safety = med) and (Maint = med) and (Buying = med) and (Persons = 4)|acc (6.0/0.0)
(Safety = med) and (Persons = more) and (Lug_boot = big) and (Maint = med)|acc (8.0/0.0)
(Maint = high) and (Buying = high) and (Safety = high) and (Persons = more)|acc (12.0/1.0)
(Persons = 4) and (Safety = high) and (Maint = high) and (Buying = high)|acc (9.0/0.0)
(Safety = med) and (Persons = 4) and (Lug_boot = med) and (Doors = 4)|acc (10.0/4.0)
(Safety = med) and (Doors = 5more) and (Persons = 4) and (Lug_boot = med)|acc (11.0/4.0)
(Safety = med) and (Persons = more) and (Lug_boot = big) and (Maint = low)|acc (4.0/0.0)
|unacc (1036.0/16.0)


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
Buying = high AND Doors = 4|acc (28.0)
Safety = med AND Maint = high AND Buying = low|acc (24.0/1.0)
Buying = high AND Lug_boot = big|acc (30.0)
Buying = high AND Safety = high AND Lug_boot = med|acc (17.0)
Safety = med AND Maint = high AND Buying = vhigh|unacc (14.0)
Maint = vhigh AND Lug_boot = big|acc (28.0)
Buying = vhigh AND Maint = low|acc (32.0/3.0)
Maint = vhigh AND Safety = high AND Lug_boot = med|acc (15.0)
Safety = med AND Lug_boot = small AND Maint = low|acc (14.0/1.0)
Maint = vhigh AND Safety = high AND Doors = 5more|acc (4.0)
Maint = vhigh AND Safety = high AND Persons = 4|acc (4.0)
Maint = vhigh AND Lug_boot = small AND Safety = med|unacc (12.0)
Maint = vhigh AND Doors = 4|acc (6.0)
Buying = high AND Doors = 5more|acc (11.0)
Maint = vhigh AND Doors = 2|unacc (5.0)
Buying = vhigh AND Maint = high|unacc (22.0)
Safety = med AND Maint = vhigh AND Doors = 5more|acc (4.0)
Safety = med AND Maint = high AND Lug_boot = big|acc (8.0)
Safety = med AND Maint = high AND Lug_boot = small|unacc (4.0)
Safety = med AND Maint = vhigh AND Persons = 4|unacc (2.0)
Safety = med AND Maint = high AND Doors = 2|unacc (4.0)
Safety = med AND Buying = vhigh|acc (16.0/3.0)
Buying = vhigh|acc (23.0/1.0)
Safety = med AND Buying = high AND Persons = 4|unacc (5.0)
Safety = med AND Maint = low AND Lug_boot = big|good (13.0)
Safety = med AND Buying = med|acc (35.0/7.0)
Lug_boot = big AND Safety = high AND Maint = med|vgood (16.0)
Lug_boot = big AND Safety = high AND Maint = low|vgood (13.0)
Lug_boot = small AND Maint = high AND Doors = 3|acc (5.0)
Lug_boot = small AND Maint = high AND Persons = 4|acc (6.0)
Lug_boot = small AND Doors = 3 AND Buying = low AND Safety = high|good (5.0/1.0)
Lug_boot = small AND Doors = 3 AND Maint = med|acc (6.0)
Lug_boot = small AND Persons = 4 AND Buying = low|good (7.0/1.0)
Lug_boot = small AND Doors = 4|acc (8.0/3.0)
Lug_boot = small AND Doors = 3 AND Buying = high|acc (2.0)
Lug_boot = small AND Doors = 5more AND Maint = med|acc (3.0/1.0)
Lug_boot = small AND Doors = 5more AND Maint = low|good (3.0)
Lug_boot = small AND Doors = 2 AND Persons = more|unacc (10.0)
Safety = med AND Buying = low AND Lug_boot = big|good (7.0)
Safety = med AND Doors = 3|acc (7.0/1.0)
Maint = high AND Buying = med|acc (16.0)
Safety = med AND Doors = 2|acc (4.0/1.0)
Safety = high AND Doors = 4|vgood (12.0)
Lug_boot = small AND Buying = med|good (4.0/1.0)
Safety = high AND Lug_boot = med AND Doors = 5more|vgood (9.0)
Lug_boot = med AND Maint = low|good (10.0/2.0)
Lug_boot = med AND Doors = 2|acc (5.0/2.0)
Safety = high AND Lug_boot = big|vgood (4.0)
Safety = high AND Persons = 4|acc (5.0/1.0)
Safety = high|vgood (4.0/1.0)
|good (3.0)


## SimpleCart Decision Tree

	* Persons=(more)|(4)
		* Safety=(high)|(med)
			* Buying=(low)|(med)
				* Maint=(low)|(med)
					* Safety=(high)|(low)
						* Lug_boot=(big)|(med)
							* Doors=(5more)|(4): vgood(29.0/0.0)
							* Doors!=(5more)|(4)
								* Lug_boot=(big)|(small): vgood(15.0/0.0)
								* Lug_boot!=(big)|(small)
									* Persons=(more)|(2): vgood(4.0/3.0)
									* Persons!=(more)|(2): good(6.0/1.0)
						* Lug_boot!=(big)|(med)
								* Buying=(low)|(vhigh)|(high): good(14.0/2.0)
								* Buying!=(low)|(vhigh)|(high)
									* Maint=(low)|(vhigh)|(high): good(6.0/1.0)
									* Maint!=(low)|(vhigh)|(high): acc(6.0/1.0)
					* Safety!=(high)|(low)
						* Lug_boot=(big)|(med)
						* Buying=(low)
								* Doors=(5more)|(4): good(14.0/0.0)
								* Doors!=(5more)|(4)
									* Lug_boot=(big)|(small): good(6.0/0.0)
									* Lug_boot!=(big)|(small): acc(5.0/1.0)
						* Buying!=(low)
							* Maint=(low): good(11.0/2.0)
							* Maint!=(low): acc(14.0/0.0)
						* Lug_boot!=(big)|(med): acc(24.0/3.0)
				* Maint!=(low)|(med)
					* Lug_boot=(big)|(med)
					* Safety=(high)
						* Buying=(low)
									* Maint=(high)|(med)|(low): vgood(11.0/3.0)
									* Maint!=(high)|(med)|(low): acc(14.0/0.0)
						* Buying!=(low): acc(30.0/0.0)
					* Safety!=(high)
							* Doors=(5more)|(4): acc(32.0/0.0)
							* Doors!=(5more)|(4)
							* Lug_boot=(big): acc(14.0/0.0)
							* Lug_boot!=(big)
								* Buying=(low): acc(5.0/2.0)
								* Buying!=(low): unacc(6.0/2.0)
					* Lug_boot!=(big)|(med)
						* Safety=(high)|(low): acc(23.0/4.0)
						* Safety!=(high)|(low)
								* Maint=(high)|(med)|(low): acc(7.0/5.0)
								* Maint!=(high)|(med)|(low): unacc(12.0/0.0)
			* Buying!=(low)|(med)
				* Maint=(low)|(med)
					* Lug_boot=(big)|(med)
						* Safety=(high)|(low): acc(59.0/0.0)
						* Safety!=(high)|(low)
						* Lug_boot=(big): acc(27.0/0.0)
						* Lug_boot!=(big)
								* Doors=(5more)|(4): acc(14.0/0.0)
								* Doors!=(5more)|(4)
								* Persons=(more): acc(4.0/2.0)
								* Persons!=(more): unacc(8.0/0.0)
					* Lug_boot!=(big)|(med)
						* Safety=(high)|(low): acc(26.0/4.0)
						* Safety!=(high)|(low): unacc(29.0/0.0)
				* Maint!=(low)|(med)
				* Buying=(high)
							* Maint=(high)|(med)|(low)
							* Lug_boot=(big)|(med): acc(26.0/3.0)
							* Lug_boot!=(big)|(med)
							* Safety=(high): acc(6.0/1.0)
							* Safety!=(high): unacc(8.0/0.0)
							* Maint!=(high)|(med)|(low): unacc(41.0/0.0)
				* Buying!=(high): unacc(91.0/0.0)
		* Safety!=(high)|(med): unacc(343.0/0.0)
	* Persons!=(more)|(4): unacc(523.0/0.0)


