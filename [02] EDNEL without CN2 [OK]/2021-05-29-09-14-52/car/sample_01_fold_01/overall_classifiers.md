# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Persons != 4 | unacc | 0.603276 |
| Persons != more | unacc | 0.602608 |
| Persons != 2 and Safety != low and Maint != vhigh and Buying != low and Buying != med and Lug_boot != small and Maint != high | acc | 0.072870 |
| Persons != 2 and Safety != low and Maint = vhigh and Buying != vhigh and Buying != high and Lug_boot != small | acc | 0.038560 |
| Persons = 4 and Safety = med | acc | 0.031267 |
| Persons = more and Safety = med | acc | 0.033414 |
| Persons = 4 and Safety = high | acc | 0.039727 |
| Persons != 2 and Safety != low and Maint != vhigh and Buying = low and Safety != med and Lug_boot != small | vgood | 0.018108 |
| Persons = more and Safety = high | acc | 0.039169 |
| Persons != 2 and Safety != low and Maint != vhigh and Buying = low and Safety = med and Maint != high and Lug_boot != small and Lug_boot != med | good | 0.009947 |
| Persons != 2 and Safety != low and Maint != vhigh and Buying = low and Safety != med and Lug_boot = small and Maint != high | good | 0.008140 |
| Persons != 2 and Safety != low and Maint != vhigh and Buying != low and Buying = med and Maint != low and Safety != med and Maint != high and Lug_boot != small | vgood | 0.007486 |
| Persons != 2 and Safety != low and Maint != vhigh and Buying != low and Buying = med and Maint = low and Safety = med | good | 0.003523 |
| Persons != 2 and Safety != low and Maint != vhigh and Buying = low and Safety = med and Maint != high and Lug_boot != small and Lug_boot = med and Doors != 2 | good | 0.003634 |
| Persons != 2 and Safety != low and Maint != vhigh and Buying != low and Buying = med and Maint = low and Safety != med | vgood | 0.004375 |

## Ordered rules

### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Safety = high and Buying = low and Lug_boot = big | vgood | 0.006535 |
| Safety = high and Buying = med and Lug_boot = big and Maint = med | vgood | 0.003881 |
| Safety = high and Buying = med and Maint = low and Lug_boot = big | vgood | 0.002976 |
| Safety = high and Lug_boot = med and Buying = low and Persons = more | vgood | 0.003289 |
| Safety = high and Lug_boot = med and Buying = med and Maint = med | vgood | 0.001673 |
| Safety = high and Buying = low and Lug_boot = med and Persons = 4 and Doors = 4 | vgood | 0.001504 |
| Buying = low and Safety = high and Doors = 5more and Persons = 4 and Lug_boot = med | vgood | 0.001504 |
| Maint = low and Buying = med and Safety = high and Lug_boot = med and Persons = more | vgood | 0.001504 |
| Buying = low and Maint = med and Persons = 4 and Safety = high | good | 0.004161 |
| Maint = low and Buying = med and Persons = 4 and Safety = high | good | 0.003125 |
| Buying = low and Maint = low and Persons = 4 and Safety = high | good | 0.004161 |
| Buying = low and Safety = med and Maint = med and Persons = more | good | 0.002840 |
| Buying = low and Safety = med and Maint = low and Lug_boot = big | good | 0.003096 |
| Maint = low and Buying = med and Safety = med and Persons = 4 | good | 0.001933 |
| Buying = low and Maint = med and Safety = med and Persons = 4 and Lug_boot = big | good | 0.002778 |
| Maint = low and Persons = more and Buying = med and Safety = med | good | 0.001741 |
| Buying = low and Persons = more and Safety = high and Maint = med | good | 0.002224 |
| Maint = low and Buying = low and Persons = more and Safety = high | good | 0.001565 |
| Safety = high and Persons = 4 and Maint = med | acc | 0.023132 |
| Persons = more and Safety = high | acc | 0.052940 |
| Safety = med and Persons = more and Lug_boot = big | acc | 0.021626 |
| Persons = 4 and Safety = high and Maint = low | acc | 0.017166 |
| Persons = 4 and Safety = med and Lug_boot = big | acc | 0.026717 |
| Persons = 4 and Safety = high and Buying = med | acc | 0.015417 |
| Safety = med and Persons = more and Lug_boot = med | acc | 0.020329 |
| Safety = med and Persons = 4 and Buying = low | acc | 0.012509 |
| Persons = 4 and Safety = high and Buying = low | acc | 0.014363 |
| Safety = med and Persons = 4 and Buying = med and Maint = med | acc | 0.005435 |
| Safety = med and Persons = more and Buying = low and Maint = low | acc | 0.002045 |
| Persons = 4 and Safety = med and Lug_boot = med and Doors = 5more | acc | 0.004046 |
| Persons = 4 and Safety = high and Maint = high and Buying = high | acc | 0.008130 |
| Safety = med and Doors = 4 and Persons = 4 and Lug_boot = med | acc | 0.002978 |
| Persons = more and Safety = med and Buying = med and Maint = med | acc | 0.002045 |
|  | unacc | 0.980198 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

persons|safety|acceptability
---|---|---
4|high|acc
more|high|acc
2|high|unacc
more|med|acc
4|med|acc
2|med|unacc
2|low|unacc
4|low|unacc
more|low|unacc

## JRip

Decision list:

rules | predicted class
---|---
(Safety = high) and (Buying = low) and (Lug_boot = big)|vgood (41.0/21.0)
(Safety = high) and (Buying = med) and (Lug_boot = big) and (Maint = med)|vgood (11.0/3.0)
(Safety = high) and (Buying = med) and (Maint = low) and (Lug_boot = big)|vgood (11.0/4.0)
(Safety = high) and (Lug_boot = med) and (Buying = low) and (Persons = more)|vgood (13.0/5.0)
(Safety = high) and (Lug_boot = med) and (Buying = med) and (Maint = med)|vgood (10.0/5.0)
(Safety = high) and (Buying = low) and (Lug_boot = med) and (Persons = 4) and (Doors = 4)|vgood (4.0/1.0)
(Buying = low) and (Safety = high) and (Doors = 5more) and (Persons = 4) and (Lug_boot = med)|vgood (4.0/1.0)
(Maint = low) and (Buying = med) and (Safety = high) and (Lug_boot = med) and (Persons = more)|vgood (4.0/1.0)
(Buying = low) and (Maint = med) and (Persons = 4) and (Safety = high)|good (6.0/0.0)
(Maint = low) and (Buying = med) and (Persons = 4) and (Safety = high)|good (8.0/2.0)
(Buying = low) and (Maint = low) and (Persons = 4) and (Safety = high)|good (6.0/0.0)
(Buying = low) and (Safety = med) and (Maint = med) and (Persons = more)|good (12.0/5.0)
(Buying = low) and (Safety = med) and (Maint = low) and (Lug_boot = big)|good (11.0/4.0)
(Maint = low) and (Buying = med) and (Safety = med) and (Persons = 4)|good (9.0/4.0)
(Buying = low) and (Maint = med) and (Safety = med) and (Persons = 4) and (Lug_boot = big)|good (4.0/0.0)
(Maint = low) and (Persons = more) and (Buying = med) and (Safety = med)|good (10.0/5.0)
(Buying = low) and (Persons = more) and (Safety = high) and (Maint = med)|good (4.0/1.0)
(Maint = low) and (Buying = low) and (Persons = more) and (Safety = high)|good (4.0/1.0)
(Safety = high) and (Persons = 4) and (Maint = med)|acc (25.0/0.0)
(Persons = more) and (Safety = high)|acc (128.0/45.0)
(Safety = med) and (Persons = more) and (Lug_boot = big)|acc (45.0/12.0)
(Persons = 4) and (Safety = high) and (Maint = low)|acc (21.0/0.0)
(Persons = 4) and (Safety = med) and (Lug_boot = big)|acc (48.0/10.0)
(Persons = 4) and (Safety = high) and (Buying = med)|acc (19.0/0.0)
(Safety = med) and (Persons = more) and (Lug_boot = med)|acc (49.0/17.0)
(Safety = med) and (Persons = 4) and (Buying = low)|acc (26.0/7.0)
(Persons = 4) and (Safety = high) and (Buying = low)|acc (11.0/0.0)
(Safety = med) and (Persons = 4) and (Buying = med) and (Maint = med)|acc (6.0/0.0)
(Safety = med) and (Persons = more) and (Buying = low) and (Maint = low)|acc (3.0/0.0)
(Persons = 4) and (Safety = med) and (Lug_boot = med) and (Doors = 5more)|acc (10.0/3.0)
(Persons = 4) and (Safety = high) and (Maint = high) and (Buying = high)|acc (9.0/0.0)
(Safety = med) and (Doors = 4) and (Persons = 4) and (Lug_boot = med)|acc (9.0/3.0)
(Persons = more) and (Safety = med) and (Buying = med) and (Maint = med)|acc (4.0/1.0)
|unacc (968.0/3.0)


## J48 Decision Tree

* Persons = 2: unacc (438.0)
* Persons != 2
	* Safety = low: unacc (291.0)
	* Safety != low
		* Maint = vhigh
			* Buying = vhigh: unacc (42.0)
			* Buying != vhigh
				* Buying = high: unacc (33.0)
				* Buying != high
					* Lug_boot = small
						* Safety = med: unacc (9.0)
						* Safety != med: acc (11.0/2.0)
					* Lug_boot != small: acc (48.0/5.0)
		* Maint != vhigh
			* Buying = low
				* Safety = med
					* Maint = high: acc (18.0)
					* Maint != high
						* Lug_boot = small: acc (10.0)
						* Lug_boot != small
							* Lug_boot = med
								* Doors = 2: acc (2.0)
								* Doors != 2: good (9.0/2.0)
							* Lug_boot != med: good (9.0)
				* Safety != med
					* Lug_boot = small
						* Maint = high: acc (5.0/1.0)
						* Maint != high: good (12.0/1.0)
					* Lug_boot != small: vgood (39.0/7.0)
			* Buying != low
				* Buying = med
					* Maint = low
						* Safety = med: good (18.0/8.0)
						* Safety != med: vgood (16.0/8.0)
					* Maint != low
						* Safety = med: acc (39.0/8.0)
						* Safety != med
							* Maint = high: acc (19.0/1.0)
							* Maint != high
								* Lug_boot = small: acc (3.0/1.0)
								* Lug_boot != small: vgood (12.0/2.0)
				* Buying != med
					* Lug_boot = small
						* Safety = med: unacc (34.0)
						* Safety != med
							* Maint = high
								* Buying = vhigh: unacc (6.0)
								* Buying != vhigh: acc (6.0/1.0)
							* Maint != high
								* Doors = 2
									* Persons = 4: acc (4.0)
									* Persons != 4: unacc (2.0)
								* Doors != 2: acc (18.0)
					* Lug_boot != small
						* Maint = high
							* Buying = vhigh: unacc (21.0)
							* Buying != vhigh: acc (24.0/2.0)
						* Maint != high: acc (97.0/10.0)


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
								* Lug_boot!=(big)|(small): good(8.0/6.0)
						* Lug_boot!=(big)|(med): good(20.0/10.0)
					* Safety!=(high)|(low)
						* Lug_boot=(big)|(med)
								* Buying=(low)|(vhigh)|(high): good(22.0/5.0)
								* Buying!=(low)|(vhigh)|(high)
							* Maint=(low): good(10.0/2.0)
							* Maint!=(low): acc(14.0/0.0)
						* Lug_boot!=(big)|(med): acc(24.0/3.0)
				* Maint!=(low)|(med)
					* Lug_boot=(big)|(med)
					* Safety=(high)
						* Buying=(low)
									* Maint=(high)|(med)|(low): vgood(11.0/3.0)
									* Maint!=(high)|(med)|(low): acc(14.0/0.0)
						* Buying!=(low): acc(30.0/0.0)
					* Safety!=(high): acc(53.0/8.0)
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
								* Doors!=(5more)|(4): unacc(10.0/4.0)
					* Lug_boot!=(big)|(med)
						* Safety=(high)|(low): acc(26.0/4.0)
						* Safety!=(high)|(low): unacc(29.0/0.0)
				* Maint!=(low)|(med)
				* Buying=(high)
							* Maint=(high)|(med)|(low)
							* Lug_boot=(big)|(med): acc(26.0/3.0)
							* Lug_boot!=(big)|(med): unacc(9.0/6.0)
							* Maint!=(high)|(med)|(low): unacc(41.0/0.0)
				* Buying!=(high): unacc(91.0/0.0)
		* Safety!=(high)|(med): unacc(343.0/0.0)
	* Persons!=(more)|(4): unacc(523.0/0.0)


