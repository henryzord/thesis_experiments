# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | unacc | 0.701223 |
| Persons = 4 and Safety = med | acc | 0.035449 |
| Persons = 4 and Safety = high | acc | 0.044869 |
| Persons = more and Safety = high | acc | 0.035626 |
| Safety = med and Persons = more and Lug_boot = big and Maint = high | acc | 0.006645 |
| Safety = med and Persons = more and Lug_boot = med and Buying = med | acc | 0.007113 |
| Safety = med and Persons = more and Lug_boot = med and Buying = high | acc | 0.004187 |
| Safety = med and Persons = more and Lug_boot = small and Buying = low | acc | 0.003532 |
| Safety = high and Persons = more and Buying = med and Maint = med | vgood | 0.003269 |
| Safety = high and Persons = more and Buying = low and Maint = high | vgood | 0.002188 |
| Safety = med and Persons = more and Lug_boot = big and Maint = med | acc | 0.005141 |
| Safety = high and Persons = 4 and Buying = low and Maint = high | vgood | 0.002188 |
| Safety = med and Persons = more and Lug_boot = big and Maint = low | good | 0.003058 |
| Safety = med and Persons = more and Lug_boot = med and Buying = low | acc | 0.004187 |
| Safety = high and Persons = more and Buying = low and Maint = med | vgood | 0.002974 |
| Safety = high and Persons = 4 and Buying = low and Maint = med | good | 0.002408 |
| Safety = high and Persons = more and Buying = med and Maint = low | vgood | 0.002728 |
| Safety = high and Persons = 4 and Buying = med and Maint = low | vgood | 0.002188 |
| Safety = high and Persons = more and Buying = low and Maint = low | vgood | 0.001672 |
| Safety = high and Persons = 4 and Buying = low and Maint = low | vgood | 0.001857 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Safety = low | unacc | 0.527976 |
| Persons = 2 | unacc | 0.429274 |
| Buying = vhigh and Maint = vhigh | unacc | 0.084813 |
| Safety = med and Lug_boot = small and Buying = high | unacc | 0.058824 |
| Buying = high and Maint = vhigh | unacc | 0.070140 |
| Safety = med and Lug_boot = small and Buying = vhigh | unacc | 0.043299 |
| Safety = med and Maint = high and Buying = vhigh | unacc | 0.031315 |
| Buying = high and Doors = 4 | acc | 0.113122 |
| Safety = med and Lug_boot = big and Maint = high | acc | 0.092593 |
| Safety = med and Lug_boot = big and Buying = vhigh | acc | 0.071090 |
| Safety = med and Lug_boot = big and Maint = vhigh | acc | 0.071090 |
| Safety = med and Lug_boot = small and Maint = med | acc | 0.058894 |
| Safety = med and Lug_boot = big and Buying = med | acc | 0.017857 |
| Buying = high and Safety = high and Lug_boot = med | acc | 0.079812 |
| Safety = med and Lug_boot = big and Buying = low | good | 0.036554 |
| Lug_boot = big and Buying = high | acc | 0.116505 |
| Safety = med and Maint = vhigh and Lug_boot = med | acc | 0.033602 |
| Lug_boot = big and Buying = vhigh and Persons = more | acc | 0.031113 |
| Lug_boot = big and Maint = med | vgood | 0.033504 |
| Lug_boot = big and Maint = high | vgood | 0.010289 |
| Lug_boot = big and Maint = low | vgood | 0.022213 |
| Lug_boot = small and Safety = med and Maint = low | acc | 0.077044 |
| Maint = vhigh and Safety = high and Lug_boot = med | acc | 0.092593 |
| Maint = vhigh and Safety = med | unacc | 0.076000 |
| Maint = vhigh and Lug_boot = small | acc | 0.067939 |
| Buying = high and Doors = 5more | acc | 0.079137 |
| Maint = high and Buying = low and Lug_boot = small | acc | 0.081055 |
| Buying = vhigh and Maint = high | unacc | 0.088372 |
| Buying = vhigh and Safety = high and Lug_boot = small | acc | 0.093889 |
| Safety = med and Buying = low and Persons = 4 | acc | 0.047198 |
| Safety = med and Buying = med and Persons = 4 | acc | 0.031778 |
| Buying = vhigh and Safety = high | acc | 0.162769 |
| Lug_boot = small and Buying = med and Persons = more | unacc | 0.031250 |
| Buying = high and Doors = 3 | acc | 0.060377 |
| Buying = med and Maint = high | acc | 0.158809 |
| Lug_boot = small and Persons = 4 | good | 0.044408 |
| Lug_boot = big | acc | 0.087113 |
| Safety = med and Buying = vhigh | unacc | 0.033333 |
| Safety = med | acc | 0.082336 |
| Lug_boot = small | good | 0.053360 |
| Doors = 4 | vgood | 0.073260 |
| Maint = low | vgood | 0.024064 |
|  | vgood | 0.095890 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Safety = high and Buying = low and Lug_boot = big and Persons = 4 | vgood | 0.004759 |
| Safety = high and Persons = more and Buying = low and Lug_boot = big | vgood | 0.004759 |
| Safety = high and Buying = med and Lug_boot = big and Maint = low | vgood | 0.003879 |
| Safety = high and Lug_boot = med and Buying = low and Persons = more | vgood | 0.003054 |
| Safety = high and Persons = 4 | acc | 0.049976 |
| Persons = more and Safety = high | acc | 0.041330 |
| Safety = med and Persons = 4 and Lug_boot = big | acc | 0.020217 |
| Safety = med and Persons = more and Lug_boot = big | acc | 0.016191 |
| Safety = med and Persons = more and Lug_boot = med | acc | 0.014758 |
| Safety = med and Persons = 4 and Buying = low | acc | 0.011403 |
| Safety = med and Persons = 4 and Buying = med and Maint = med | acc | 0.006785 |
|  | unacc | 0.904485 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

persons|safety|acceptability
---|---|---
2|high|unacc
more|high|acc
4|high|acc
2|med|unacc
4|med|acc
more|med|unacc
4|low|unacc
more|low|unacc
2|low|unacc

## JRip

Decision list:

rules | predicted class
---|---
(Safety = high) and (Buying = low) and (Lug_boot = big) and (Persons = 4)|vgood (14.0/4.0)
(Safety = high) and (Persons = more) and (Buying = low) and (Lug_boot = big)|vgood (14.0/4.0)
(Safety = high) and (Buying = med) and (Lug_boot = big) and (Maint = low)|vgood (11.0/3.0)
(Safety = high) and (Lug_boot = med) and (Buying = low) and (Persons = more)|vgood (14.0/6.0)
(Safety = high) and (Persons = 4)|acc (145.0/54.0)
(Persons = more) and (Safety = high)|acc (140.0/63.0)
(Safety = med) and (Persons = 4) and (Lug_boot = big)|acc (57.0/20.0)
(Safety = med) and (Persons = more) and (Lug_boot = big)|acc (57.0/24.0)
(Safety = med) and (Persons = more) and (Lug_boot = med)|acc (59.0/27.0)
(Safety = med) and (Persons = 4) and (Buying = low)|acc (30.0/8.0)
(Safety = med) and (Persons = 4) and (Buying = med) and (Maint = med)|acc (8.0/0.0)
|unacc (1004.0/35.0)


## PART

Decision list:

rules | predicted class
---|---
Safety = low|unacc (519.0)
Persons = 2|unacc (349.0)
Buying = vhigh AND Maint = vhigh|unacc (43.0)
Safety = med AND Lug_boot = small AND Buying = high|unacc (29.0)
Buying = high AND Maint = vhigh|unacc (35.0)
Safety = med AND Lug_boot = small AND Buying = vhigh|unacc (21.0)
Safety = med AND Maint = high AND Buying = vhigh|unacc (15.0)
Buying = high AND Doors = 4|acc (25.0)
Safety = med AND Lug_boot = big AND Maint = high|acc (20.0)
Safety = med AND Lug_boot = big AND Buying = vhigh|acc (15.0)
Safety = med AND Lug_boot = big AND Maint = vhigh|acc (15.0)
Safety = med AND Lug_boot = small AND Maint = med|acc (16.0/2.0)
Safety = med AND Lug_boot = big AND Buying = med|acc (14.0/7.0)
Buying = high AND Safety = high AND Lug_boot = med|acc (17.0)
Safety = med AND Lug_boot = big AND Buying = low|good (14.0)
Lug_boot = big AND Buying = high|acc (24.0)
Safety = med AND Maint = vhigh AND Lug_boot = med|acc (16.0/6.0)
Lug_boot = big AND Buying = vhigh AND Persons = more|acc (11.0/3.0)
Lug_boot = big AND Maint = med|vgood (18.0/4.0)
Lug_boot = big AND Maint = high|vgood (17.0/9.0)
Lug_boot = big AND Maint = low|vgood (17.0/4.0)
Lug_boot = small AND Safety = med AND Maint = low|acc (16.0/2.0)
Maint = vhigh AND Safety = high AND Lug_boot = med|acc (15.0)
Maint = vhigh AND Safety = med|unacc (13.0)
Maint = vhigh AND Lug_boot = small|acc (13.0/2.0)
Buying = high AND Doors = 5more|acc (11.0)
Maint = high AND Buying = low AND Lug_boot = small|acc (15.0/2.0)
Buying = vhigh AND Maint = high|unacc (14.0)
Buying = vhigh AND Safety = high AND Lug_boot = small|acc (15.0/2.0)
Safety = med AND Buying = low AND Persons = 4|acc (12.0/4.0)
Safety = med AND Buying = med AND Persons = 4|acc (16.0/8.0)
Buying = vhigh AND Safety = high|acc (15.0)
Lug_boot = small AND Buying = med AND Persons = more|unacc (15.0/9.0)
Buying = high AND Doors = 3|acc (10.0/2.0)
Buying = med AND Maint = high|acc (15.0/1.0)
Lug_boot = small AND Persons = 4|good (15.0/6.0)
Lug_boot = big|acc (13.0)
Safety = med AND Buying = vhigh|unacc (12.0/6.0)
Safety = med|acc (23.0/12.0)
Lug_boot = small|good (10.0/4.0)
Doors = 4|vgood (10.0)
Maint = low|vgood (12.0/6.0)
|vgood (13.0/6.0)


## J48 Decision Tree

* Safety = low: unacc (519.0)
* Safety = med
	* Persons = 2: unacc (174.0)
	* Persons = 4
		* Buying = vhigh
			* Maint = vhigh: unacc (11.0)
			* Maint = high: unacc (10.0)
			* Maint = med: acc (11.0/5.0)
			* Maint = low: unacc (11.0/5.0)
		* Buying = high
			* Lug_boot = small: unacc (14.0)
			* Lug_boot = med: unacc (13.0/6.0)
			* Lug_boot = big: acc (16.0/4.0)
		* Buying = med: acc (45.0/16.0)
		* Buying = low: acc (42.0/14.0)
	* Persons = more
		* Lug_boot = small
			* Buying = vhigh: unacc (15.0)
			* Buying = high: unacc (15.0)
			* Buying = med: unacc (16.0/6.0)
			* Buying = low: acc (15.0/7.0)
		* Lug_boot = med
			* Buying = vhigh: unacc (13.0/3.0)
			* Buying = high: acc (16.0/7.0)
			* Buying = med: acc (14.0/3.0)
			* Buying = low: acc (16.0/7.0)
		* Lug_boot = big
			* Maint = vhigh: unacc (15.0/7.0)
			* Maint = high: acc (15.0/4.0)
			* Maint = med: acc (13.0/4.0)
			* Maint = low: good (14.0/6.0)
* Safety = high
	* Persons = 2: unacc (175.0)
	* Persons = 4
		* Buying = vhigh
			* Maint = vhigh: unacc (9.0)
			* Maint = high: unacc (9.0)
			* Maint = med: acc (11.0)
			* Maint = low: acc (11.0)
		* Buying = high
			* Maint = vhigh: unacc (9.0)
			* Maint = high: acc (12.0)
			* Maint = med: acc (9.0)
			* Maint = low: acc (11.0)
		* Buying = med
			* Maint = vhigh: acc (10.0)
			* Maint = high: acc (11.0)
			* Maint = med: acc (11.0/5.0)
			* Maint = low: vgood (11.0/5.0)
		* Buying = low
			* Maint = vhigh: acc (9.0)
			* Maint = high: vgood (11.0/5.0)
			* Maint = med: good (10.0/4.0)
			* Maint = low: vgood (9.0/4.0)
	* Persons = more
		* Buying = vhigh
			* Maint = vhigh: unacc (11.0)
			* Maint = high: unacc (10.0)
			* Maint = med: acc (12.0/1.0)
			* Maint = low: acc (12.0/1.0)
		* Buying = high
			* Maint = vhigh: unacc (11.0)
			* Maint = high: acc (11.0/1.0)
			* Maint = med: acc (9.0)
			* Maint = low: acc (9.0/1.0)
		* Buying = med
			* Maint = vhigh: acc (10.0/1.0)
			* Maint = high: acc (11.0/1.0)
			* Maint = med: vgood (10.0/3.0)
			* Maint = low: vgood (12.0/5.0)
		* Buying = low
			* Maint = vhigh: acc (12.0/1.0)
			* Maint = high: vgood (11.0/5.0)
			* Maint = med: vgood (11.0/4.0)
			* Maint = low: vgood (10.0/5.0)


## SimpleCart Decision Tree

	* Safety=(high)|(med)
		* Persons=(more)|(4)
			* Buying=(low)|(med)
				* Maint=(low)|(med)
				* Safety=(high)
						* Lug_boot=(big)|(med)
							* Doors=(5more)|(4): vgood(28.0/0.0)
							* Doors!=(5more)|(4)
								* Lug_boot=(big)|(small): vgood(14.0/0.0)
								* Lug_boot!=(big)|(small)
								* Persons=(more): vgood(4.0/2.0)
								* Persons!=(more): good(6.0/2.0)
						* Lug_boot!=(big)|(med)
								* Buying=(low)|(vhigh)|(high): good(12.0/2.0)
								* Buying!=(low)|(vhigh)|(high)
									* Maint=(low)|(vhigh)|(high): good(6.0/1.0)
									* Maint!=(low)|(vhigh)|(high): acc(7.0/0.0)
				* Safety!=(high)
						* Lug_boot=(big)|(med)
								* Buying=(low)|(vhigh)|(high)
								* Doors=(5more)|(4): good(16.0/0.0)
								* Doors!=(5more)|(4)
								* Lug_boot=(big): good(6.0/0.0)
								* Lug_boot!=(big): acc(6.0/2.0)
								* Buying!=(low)|(vhigh)|(high)
							* Maint=(low): good(10.0/3.0)
							* Maint!=(low): acc(15.0/0.0)
						* Lug_boot!=(big)|(med): acc(28.0/4.0)
				* Maint!=(low)|(med)
					* Lug_boot=(big)|(med)
					* Safety=(high)
								* Maint=(high)|(med)|(low)
									* Buying=(low)|(vhigh)|(high): vgood(12.0/2.0)
									* Buying!=(low)|(vhigh)|(high): acc(14.0/0.0)
								* Maint!=(high)|(med)|(low): acc(28.0/0.0)
					* Safety!=(high): acc(52.0/9.0)
					* Lug_boot!=(big)|(med)
						* Safety=(high)|(low)
								* Doors=(5more)|(4)|(3): acc(23.0/0.0)
								* Doors!=(5more)|(4)|(3): unacc(4.0/2.0)
						* Safety!=(high)|(low)
						* Buying=(low)
									* Maint=(high)|(med)|(low): acc(6.0/1.0)
									* Maint!=(high)|(med)|(low): unacc(6.0/0.0)
						* Buying!=(low): unacc(15.0/0.0)
			* Buying!=(low)|(med)
				* Maint=(low)|(med)
					* Lug_boot=(big)|(med)
						* Safety=(high)|(low): acc(57.0/0.0)
						* Safety!=(high)|(low)
							* Lug_boot=(big)|(small): acc(27.0/0.0)
							* Lug_boot!=(big)|(small)
								* Doors=(5more)|(4): acc(13.0/0.0)
								* Doors!=(5more)|(4): unacc(10.0/3.0)
					* Lug_boot!=(big)|(med)
					* Safety=(high): acc(24.0/3.0)
					* Safety!=(high): unacc(28.0/0.0)
				* Maint!=(low)|(med)
						* Maint=(high)|(med)|(low)
							* Buying=(high)|(med)|(low)
							* Lug_boot=(big)|(med): acc(28.0/3.0)
							* Lug_boot!=(big)|(med)
								* Safety=(high)|(low): acc(6.0/1.0)
								* Safety!=(high)|(low): unacc(7.0/0.0)
							* Buying!=(high)|(med)|(low): unacc(41.0/0.0)
						* Maint!=(high)|(med)|(low): unacc(86.0/0.0)
		* Persons!=(more)|(4): unacc(349.0/0.0)
	* Safety!=(high)|(med): unacc(519.0/0.0)


