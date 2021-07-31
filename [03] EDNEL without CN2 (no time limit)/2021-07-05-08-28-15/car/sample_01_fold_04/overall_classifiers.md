# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Persons != 4 | unacc | 0.604302 |
| Persons != more | unacc | 0.600277 |
| Safety = med and Persons = more and Lug_boot = big | acc | 0.018534 |
| Safety = med and Persons = more and Lug_boot = med | acc | 0.015597 |
| Safety = med and Persons = 4 and Buying = med | acc | 0.014227 |
| Safety = med and Persons = 4 and Buying = low | acc | 0.013311 |
| Safety = high and Persons = 4 and Buying = vhigh and Maint = med | acc | 0.009836 |
| Safety = high and Persons = 4 and Buying = high and Maint = med | acc | 0.009836 |
| Safety = high and Persons = 4 and Buying = high and Maint = low | acc | 0.009836 |
| Safety = med and Persons = 4 and Buying = high and Lug_boot = big | acc | 0.007401 |
| Safety = high and Persons = more and Buying = vhigh and Maint = med | acc | 0.008279 |
| Safety = high and Persons = more and Buying = high and Maint = high | acc | 0.008279 |
| Safety = high and Persons = 4 and Buying = med and Maint = vhigh | acc | 0.009024 |
| Safety = high and Persons = 4 and Buying = vhigh and Maint = low | acc | 0.008210 |
| Safety = high and Persons = 4 and Buying = med and Maint = high | acc | 0.008210 |
| Safety = high and Persons = 4 and Buying = low and Maint = vhigh | acc | 0.008210 |
| Safety = high and Persons = more and Buying = low and Maint = vhigh | acc | 0.007470 |
| Safety = high and Persons = more and Buying = med and Maint = vhigh | acc | 0.007470 |
| Safety = high and Persons = 4 and Buying = high and Maint = high | acc | 0.007395 |
| Safety = med and Persons = more and Lug_boot = small and Buying = low | acc | 0.005137 |
| Safety = high and Persons = more and Buying = vhigh and Maint = low | acc | 0.006661 |
| Safety = high and Persons = more and Buying = med and Maint = high | acc | 0.006661 |
| Safety = high and Persons = more and Buying = high and Maint = med | acc | 0.006661 |
| Safety = high and Persons = more and Buying = high and Maint = low | acc | 0.005853 |
| Safety = high and Persons = more and Buying = med and Maint = low | vgood | 0.002976 |
| Safety = high and Persons = more and Buying = low and Maint = low | vgood | 0.002976 |
| Safety = high and Persons = more and Buying = low and Maint = med | vgood | 0.002406 |
| Safety = high and Persons = 4 and Buying = med and Maint = low | good | 0.002191 |
| Safety = high and Persons = more and Buying = low and Maint = high | vgood | 0.002189 |
| Safety = high and Persons = 4 and Buying = med and Maint = med | vgood | 0.002189 |
| Safety = high and Persons = 4 and Buying = low and Maint = high | acc | 0.002483 |
| Safety = high and Persons = 4 and Buying = low and Maint = med | vgood | 0.002008 |
| Safety = high and Persons = more and Buying = med and Maint = med | vgood | 0.001673 |
| Safety = high and Persons = 4 and Buying = low and Maint = low | vgood | 0.001673 |
| Persons = 4 and Safety = med and Buying != med and Maint = med and Lug_boot = med and Doors = 4 | acc | 0.001103 |
| Persons = 4 and Safety = med and Buying != med and Maint = med and Lug_boot = med and Doors = 5more | acc | 0.001103 |

## Ordered rules

### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Safety = high and Buying = low and Lug_boot = big and Persons = more | vgood | 0.005374 |
| Safety = high and Lug_boot = big and Buying = low and Persons = 4 | vgood | 0.006387 |
| Safety = high and Buying = med and Maint = low and Lug_boot = big | vgood | 0.003271 |
| Safety = high and Buying = med and Maint = med and Lug_boot = big | vgood | 0.002976 |
| Safety = high and Lug_boot = med and Buying = low and Persons = more | vgood | 0.002854 |
| Buying = low and Maint = med and Persons = 4 | good | 0.003329 |
| Maint = low and Safety = med and Lug_boot = big and Buying = low | good | 0.003375 |
| Maint = low and Buying = med and Safety = med and Lug_boot = big | good | 0.003070 |
| Maint = low and Safety = high and Buying = med | good | 0.002163 |
| Safety = high and Persons = 4 and Buying = med | acc | 0.019594 |
| Persons = more and Safety = high and Maint = med and Buying = vhigh | acc | 0.008861 |
| Persons = more and Safety = high and Buying = med | acc | 0.014476 |
| Safety = med and Persons = more and Buying = low | acc | 0.014804 |
| Safety = med and Persons = more and Lug_boot = big | acc | 0.016354 |
| Persons = 4 and Safety = high and Maint = med | acc | 0.017919 |
| Persons = 4 and Safety = med and Lug_boot = big | acc | 0.022645 |
| Persons = 4 and Safety = med and Buying = low and Maint = high | acc | 0.006167 |
| Persons = more and Safety = high and Maint = low and Buying = vhigh | acc | 0.007130 |
| Safety = high and Persons = 4 and Maint = low | acc | 0.014127 |
| Persons = more and Safety = high and Buying = high | acc | 0.016346 |
| Persons = 4 and Safety = high and Buying = high and Maint = high | acc | 0.007916 |
| Safety = med and Lug_boot = med and Persons = more | acc | 0.011317 |
| Persons = 4 and Safety = med and Buying = med and Maint = med | acc | 0.006167 |
| Persons = 4 and Safety = med and Maint = low | acc | 0.006206 |
| Buying = low and Safety = high and Persons = 4 | acc | 0.008683 |
| Safety = med and Persons = 4 and Lug_boot = med and Doors = 4 | acc | 0.002899 |
| Safety = med and Doors = 5more and Persons = 4 and Lug_boot = med | acc | 0.002216 |
|  | unacc | 0.944493 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

acceptability
---
unacc

## JRip

Decision list:

rules | predicted class
---|---
(Safety = high) and (Buying = low) and (Lug_boot = big) and (Persons = more)|vgood (15.0/4.0)
(Safety = high) and (Lug_boot = big) and (Buying = low) and (Persons = 4)|vgood (15.0/3.0)
(Safety = high) and (Buying = med) and (Maint = low) and (Lug_boot = big)|vgood (10.0/3.0)
(Safety = high) and (Buying = med) and (Maint = med) and (Lug_boot = big)|vgood (11.0/4.0)
(Safety = high) and (Lug_boot = med) and (Buying = low) and (Persons = more)|vgood (15.0/7.0)
(Buying = low) and (Maint = med) and (Persons = 4)|good (30.0/18.0)
(Maint = low) and (Safety = med) and (Lug_boot = big) and (Buying = low)|good (10.0/3.0)
(Maint = low) and (Buying = med) and (Safety = med) and (Lug_boot = big)|good (11.0/4.0)
(Maint = low) and (Safety = high) and (Buying = med)|good (23.0/14.0)
(Safety = high) and (Persons = 4) and (Buying = med)|acc (28.0/2.0)
(Persons = more) and (Safety = high) and (Maint = med) and (Buying = vhigh)|acc (12.0/1.0)
(Persons = more) and (Safety = high) and (Buying = med)|acc (28.0/5.0)
(Safety = med) and (Persons = more) and (Buying = low)|acc (37.0/12.0)
(Safety = med) and (Persons = more) and (Lug_boot = big)|acc (37.0/10.0)
(Persons = 4) and (Safety = high) and (Maint = med)|acc (24.0/0.0)
(Persons = 4) and (Safety = med) and (Lug_boot = big)|acc (47.0/12.0)
(Persons = 4) and (Safety = med) and (Buying = low) and (Maint = high)|acc (7.0/0.0)
(Persons = more) and (Safety = high) and (Maint = low) and (Buying = vhigh)|acc (10.0/1.0)
(Safety = high) and (Persons = 4) and (Maint = low)|acc (28.0/6.0)
(Persons = more) and (Safety = high) and (Buying = high)|acc (42.0/14.0)
(Persons = 4) and (Safety = high) and (Buying = high) and (Maint = high)|acc (9.0/0.0)
(Safety = med) and (Lug_boot = med) and (Persons = more)|acc (47.0/21.0)
(Persons = 4) and (Safety = med) and (Buying = med) and (Maint = med)|acc (7.0/0.0)
(Persons = 4) and (Safety = med) and (Maint = low)|acc (28.0/14.0)
(Buying = low) and (Safety = high) and (Persons = 4)|acc (15.0/2.0)
(Safety = med) and (Persons = 4) and (Lug_boot = med) and (Doors = 4)|acc (9.0/3.0)
(Safety = med) and (Doors = 5more) and (Persons = 4) and (Lug_boot = med)|acc (8.0/3.0)
|unacc (990.0/14.0)


## J48 Decision Tree

* Safety = low: unacc (518.0)
* Safety = med
	* Persons = 2: unacc (176.0)
	* Persons = 4
		* Buying = vhigh: unacc (42.0/8.0)
		* Buying = high
			* Lug_boot = small: unacc (14.0)
			* Lug_boot = med: unacc (16.0/6.0)
			* Lug_boot = big: acc (16.0/4.0)
		* Buying = med: acc (42.0/15.0)
		* Buying = low: acc (45.0/18.0)
	* Persons = more
		* Lug_boot = small
			* Buying = vhigh: unacc (16.0)
			* Buying = high: unacc (15.0)
			* Buying = med: unacc (13.0/5.0)
			* Buying = low: acc (13.0/4.0)
		* Lug_boot = med: acc (61.0/27.0)
		* Lug_boot = big: acc (54.0/19.0)
* Safety = high
	* Persons = 2: unacc (169.0)
	* Persons = 4
		* Buying = vhigh
			* Maint = vhigh: unacc (10.0)
			* Maint = high: unacc (11.0)
			* Maint = med: acc (12.0)
			* Maint = low: acc (10.0)
		* Buying = high
			* Maint = vhigh: unacc (10.0)
			* Maint = high: acc (9.0)
			* Maint = med: acc (12.0)
			* Maint = low: acc (12.0)
		* Buying = med
			* Maint = vhigh: acc (11.0)
			* Maint = high: acc (10.0)
			* Maint = med: vgood (11.0/5.0)
			* Maint = low: good (11.0/5.0)
		* Buying = low
			* Maint = vhigh: acc (10.0)
			* Maint = high: acc (12.0/6.0)
			* Maint = med: vgood (12.0/6.0)
			* Maint = low: vgood (10.0/5.0)
	* Persons = more
		* Buying = vhigh
			* Maint = vhigh: unacc (11.0)
			* Maint = high: unacc (10.0)
			* Maint = med: acc (12.0/1.0)
			* Maint = low: acc (10.0/1.0)
		* Buying = high
			* Maint = vhigh: unacc (11.0)
			* Maint = high: acc (12.0/1.0)
			* Maint = med: acc (10.0/1.0)
			* Maint = low: acc (9.0/1.0)
		* Buying = med
			* Maint = vhigh: acc (11.0/1.0)
			* Maint = high: acc (10.0/1.0)
			* Maint = med: vgood (10.0/5.0)
			* Maint = low: vgood (11.0/4.0)
		* Buying = low
			* Maint = vhigh: acc (11.0/1.0)
			* Maint = high: vgood (11.0/5.0)
			* Maint = med: vgood (10.0/4.0)
			* Maint = low: vgood (11.0/4.0)


## SimpleCart Decision Tree

	* Persons=(more)|(4)
		* Safety=(high)|(med)
			* Buying=(low)|(med)
				* Maint=(low)|(med)
					* Safety=(high)|(low)
						* Lug_boot=(big)|(med)
							* Lug_boot=(big)|(small): vgood(30.0/0.0)
							* Lug_boot!=(big)|(small)
								* Doors=(5more)|(4): vgood(14.0/0.0)
								* Doors!=(5more)|(4): good(9.0/5.0)
						* Lug_boot!=(big)|(med)
						* Buying=(low): good(11.0/2.0)
						* Buying!=(low)
							* Maint=(low): good(6.0/1.0)
							* Maint!=(low): acc(7.0/1.0)
					* Safety!=(high)|(low)
						* Lug_boot=(big)|(med)
								* Maint=(low)|(vhigh)|(high)
								* Doors=(5more)|(4): good(15.0/0.0)
								* Doors!=(5more)|(4)
									* Lug_boot=(big)|(small): good(7.0/0.0)
									* Lug_boot!=(big)|(small): acc(4.0/2.0)
								* Maint!=(low)|(vhigh)|(high)
							* Buying=(low): good(10.0/3.0)
							* Buying!=(low): acc(14.0/0.0)
						* Lug_boot!=(big)|(med): acc(25.0/1.0)
				* Maint!=(low)|(med)
					* Lug_boot=(big)|(med)
							* Buying=(low)|(vhigh)|(high)
							* Safety=(high)|(low)
									* Maint=(high)|(med)|(low): vgood(12.0/3.0)
									* Maint!=(high)|(med)|(low): acc(14.0/0.0)
							* Safety!=(high)|(low): acc(26.0/3.0)
							* Buying!=(low)|(vhigh)|(high)
							* Doors=(5more)|(4): acc(29.0/0.0)
							* Doors!=(5more)|(4)
								* Safety=(high)|(low): acc(13.0/0.0)
								* Safety!=(high)|(low)
									* Lug_boot=(big)|(small): acc(7.0/0.0)
									* Lug_boot!=(big)|(small): unacc(4.0/2.0)
					* Lug_boot!=(big)|(med)
						* Safety=(high)|(low)
								* Doors=(5more)|(4)|(3): acc(23.0/0.0)
								* Doors!=(5more)|(4)|(3): unacc(4.0/3.0)
						* Safety!=(high)|(low)
						* Buying=(low)
									* Maint=(high)|(med)|(low): acc(7.0/0.0)
									* Maint!=(high)|(med)|(low): unacc(7.0/0.0)
						* Buying!=(low): unacc(15.0/0.0)
			* Buying!=(low)|(med)
				* Maint=(low)|(med)
					* Lug_boot=(big)|(med)
						* Doors=(5more)|(4): acc(58.0/0.0)
						* Doors!=(5more)|(4)
							* Safety=(high)|(low): acc(28.0/0.0)
							* Safety!=(high)|(low)
							* Lug_boot=(big): acc(13.0/0.0)
							* Lug_boot!=(big): unacc(11.0/4.0)
					* Lug_boot!=(big)|(med)
						* Safety=(high)|(low): acc(27.0/4.0)
						* Safety!=(high)|(low): unacc(31.0/0.0)
				* Maint!=(low)|(med)
						* Buying=(high)|(med)|(low)
							* Maint=(high)|(med)|(low)
							* Lug_boot=(big)|(med): acc(27.0/3.0)
							* Lug_boot!=(big)|(med)
								* Safety=(high)|(low): acc(6.0/1.0)
								* Safety!=(high)|(low): unacc(7.0/0.0)
							* Maint!=(high)|(med)|(low): unacc(44.0/0.0)
						* Buying!=(high)|(med)|(low): unacc(87.0/0.0)
		* Safety!=(high)|(med): unacc(344.0/0.0)
	* Persons!=(more)|(4): unacc(519.0/0.0)


