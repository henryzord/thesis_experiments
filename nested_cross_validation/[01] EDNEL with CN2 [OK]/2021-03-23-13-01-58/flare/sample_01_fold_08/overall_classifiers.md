# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = X | H | 0.311390 |
| SpotDistribution != X and LargestSpotSize = X | B | 0.134937 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution = O | C | 0.117137 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution != O | D | 0.075555 |
| SpotDistribution = O and LargestSpotSize!=(X) and SpotDistribution != I and LargestSpotSize != X and C-class != 1 and Activity!=(2) | D | 0.047766 |
| SpotDistribution != X and LargestSpotSize != X and Area != 1 | E | 0.008057 |
| LargestSpotSize = K and SpotDistribution = I and Area = 2 | F | 0.001959 |
| SpotDistribution = O and LargestSpotSize!=(X) and SpotDistribution != I and LargestSpotSize != X and C-class = 2 | E | 0.000766 |
| SpotDistribution = O and LargestSpotSize!=(X) and SpotDistribution != I and LargestSpotSize != X and C-class = 4 | E | 0.002288 |
| LargestSpotSize = A and SpotDistribution = I and Area = 2 | F | 0.002174 |
| SpotDistribution = O and LargestSpotSize!=(X) and SpotDistribution != I and LargestSpotSize != X and C-class = 1 | E | 0.000821 |
| LargestSpotSize = K and SpotDistribution = C and Area = 1 | E | 0.001527 |
| SpotDistribution = O and LargestSpotSize!=(X) and SpotDistribution != I and LargestSpotSize != X and C-class = 3 | E | 0.000230 |
| LargestSpotSize = H and SpotDistribution = I and Area = 1 | E | 0.000573 |
| LargestSpotSize = A and SpotDistribution = O and Area = 1 | D | 0.015350 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = X | H | 0.311390 |
| LargestSpotSize = X | B | 0.196049 |
| Area != 1 and Prev24Hour = 1 and Activity != 1 | F | 0.008097 |
| Area != 1 and Activity = 1 | E | 0.004556 |
| SpotDistribution = C and LargestSpotSize != K | D | 0.009836 |
| HistComplex = 1 and LargestSpotSize != A and LargestSpotSize = R and C-class != 1 and SpotDistribution = O and Evolution = 3 | C | 0.068067 |
| SpotDistribution = C | E | 0.033566 |
| SpotDistribution = O and LargestSpotSize != H and LargestSpotSize != A and C-class = 1 and LargestSpotSize != R and HistComplex = 1 | C | 0.011650 |
| SpotDistribution = O and LargestSpotSize != H and LargestSpotSize != A and C-class = 1 and HistComplex != 1 | D | 0.008130 |
| SpotDistribution = O and C-class = 0 and HistComplex = 1 and LargestSpotSize != A and Evolution != 3 and LargestSpotSize = R | C | 0.064685 |
| SpotDistribution = O and C-class = 0 and LargestSpotSize != H and LargestSpotSize != A and Evolution != 1 and HistComplex != 1 and Evolution = 2 and LargestSpotSize != R | C | 0.018152 |
| SpotDistribution = O and C-class = 0 and Evolution = 3 and LargestSpotSize != S and LargestSpotSize = A and HistComplex != 1 | D | 0.013378 |
| SpotDistribution = O and C-class = 0 and LargestSpotSize != H and LargestSpotSize != A and Evolution != 1 and Evolution = 2 and Activity = 1 and LargestSpotSize != R | C | 0.024360 |
| SpotDistribution = O and C-class = 0 and LargestSpotSize != H and Evolution = 3 and LargestSpotSize = S and HistComplex = 1 | C | 0.042527 |
| LargestSpotSize = R and Evolution = 3 and HistComplex = 1 and C-class = 1 | D | 0.017857 |
| SpotDistribution != O and LargestSpotSize = R and Evolution = 3 and HistComplex = 1 | D | 0.011561 |
| SpotDistribution != O and LargestSpotSize = R and Evolution != 3 | D | 0.007475 |
| SpotDistribution != O and HistComplex = 1 and LargestSpotSize = A and Activity = 1 | D | 0.071157 |
| SpotDistribution = O and C-class = 0 and Evolution = 3 and Activity = 1 and LargestSpotSize != A and LargestSpotSize = S | C | 0.004596 |
| SpotDistribution != O and HistComplex = 1 and Activity = 1 | D | 0.013920 |
| SpotDistribution != O and LargestSpotSize != R and C-class != 3 and M-class = 0 and HistComplex != 1 and Evolution = 3 and LargestSpotSize != K and LargestSpotSize != S and Activity = 1 | D | 0.036016 |
| SpotDistribution != O and LargestSpotSize != R and C-class = 3 | D | 0.021176 |
| SpotDistribution != O and LargestSpotSize != R and M-class = 0 and HistComplex != 1 and LargestSpotSize = K and Evolution = 2 | D | 0.005488 |
| SpotDistribution != O and LargestSpotSize != K and LargestSpotSize != R and C-class != 2 and M-class = 0 and C-class = 1 and Activity != 1 | D | 0.016437 |
| SpotDistribution != O and LargestSpotSize != K and LargestSpotSize != R and C-class != 2 and M-class = 0 and Evolution != 2 and Activity != 1 | D | 0.020833 |
| SpotDistribution != O and LargestSpotSize != K and LargestSpotSize != R and M-class = 0 and C-class != 2 and Evolution = 2 and LargestSpotSize = A and Activity = 1 and C-class = 0 | D | 0.018449 |
| SpotDistribution != O and LargestSpotSize != K and LargestSpotSize != R and M-class = 0 and Activity = 1 and Evolution = 2 | D | 0.004723 |
| SpotDistribution != O and LargestSpotSize != K and LargestSpotSize != R and M-class = 0 and Activity != 1 and LargestSpotSize = A | E | 0.019324 |
| M-class != 0 | D | 0.028571 |
| SpotDistribution != O and Evolution != 2 and LargestSpotSize != R and LargestSpotSize != K | D | 0.008571 |
| Evolution = 3 and LargestSpotSize != K and LargestSpotSize != S and Activity = 1 and HistComplex = 1 | D | 0.095805 |
| Evolution = 3 and LargestSpotSize != S and Activity = 1 and LargestSpotSize != R | D | 0.017165 |
| LargestSpotSize != H and Evolution = 3 and LargestSpotSize != S and Activity != 1 | D | 0.043554 |
| LargestSpotSize != H and C-class = 0 and Evolution = 3 | D | 0.050858 |
| LargestSpotSize != H and SpotDistribution = O and C-class != 0 and HistComplex = 1 | C | 0.023378 |
| C-class = 0 and HistComplex = 1 and LargestSpotSize != A | C | 0.055125 |
| C-class = 0 and Activity = 1 and LargestSpotSize != S and LargestSpotSize != R and HistComplex != 1 | C | 0.043556 |
| C-class = 0 and Activity = 1 and LargestSpotSize != S and LargestSpotSize != A | C | 0.031250 |
| HistComplex != 1 and C-class = 0 and LargestSpotSize = S | E | 0.032258 |
| HistComplex != 1 and LargestSpotSize = A | E | 0.121336 |
| LargestSpotSize != A | E | 0.065266 |
|  | D | 0.428571 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = I and Evolution = 2 and C-class = 1 | F | 0.003150 |
| Area = 2 | F | 0.003190 |
| LargestSpotSize = A and Activity = 2 | E | 0.007834 |
| HistComplex = 2 and M-class = 1 | E | 0.004084 |
| LargestSpotSize = X | B | 0.140830 |
| SpotDistribution = O and HistComplex = 1 | C | 0.122424 |
| SpotDistribution = O and LargestSpotSize = R | C | 0.003655 |
| SpotDistribution = I | D | 0.128701 |
| SpotDistribution = O and Evolution = 3 | D | 0.105641 |
|  | H | 0.615702 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

largestspotsize|spotdistribution|area|class
---|---|---|---
a|c|2|h
k|c|2|e
a|i|2|f
k|i|2|f
r|o|2|h
k|c|1|e
h|c|1|h
a|c|1|d
r|c|1|d
h|i|1|e
x|i|1|b
k|i|1|d
a|i|1|d
s|i|1|d
r|i|1|d
x|o|1|b
a|o|1|d
h|o|1|d
r|o|1|c
k|o|1|h
s|o|1|c
k|x|1|h
h|x|1|h
a|x|1|h
r|x|1|h
s|x|1|h

## JRip

Decision list:

rules | predicted class
---|---
(SpotDistribution = I) and (Evolution = 2) and (C-class = 1)|F (17.0/10.0)
(Area = 2)|F (22.0/14.0)
(LargestSpotSize = A) and (Activity = 2)|E (46.0/28.0)
(HistComplex = 2) and (M-class = 1)|E (10.0/5.0)
(LargestSpotSize = X)|B (128.0/0.0)
(SpotDistribution = O) and (HistComplex = 1)|C (200.0/73.0)
(SpotDistribution = O) and (LargestSpotSize = R)|C (15.0/5.0)
(SpotDistribution = I)|D (128.0/50.0)
(SpotDistribution = O) and (Evolution = 3)|D (33.0/15.0)
|H (358.0/61.0)


## PART

Decision list:

rules | predicted class
---|---
SpotDistribution = X|H (298.0)
LargestSpotSize = X|B (129.0)
Area != 1 AND Prev24Hour = 1 AND Activity != 1|F (9.0/3.0)
Area != 1 AND Activity = 1|E (8.0/4.0)
SpotDistribution = C AND LargestSpotSize != K|D (12.0/6.0)
HistComplex = 1 AND LargestSpotSize != A AND LargestSpotSize = R AND C-class != 1 AND SpotDistribution = O AND Evolution = 3|C (56.0/20.0)
SpotDistribution = C|E (10.0/1.0)
SpotDistribution = O AND LargestSpotSize != H AND LargestSpotSize != A AND C-class = 1 AND LargestSpotSize != R AND HistComplex = 1|C (10.0/4.0)
SpotDistribution = O AND LargestSpotSize != H AND LargestSpotSize != A AND C-class = 1 AND HistComplex != 1|D (8.0/4.0)
SpotDistribution = O AND C-class = 0 AND HistComplex = 1 AND LargestSpotSize != A AND Evolution != 3 AND LargestSpotSize = R|C (35.0/8.0)
SpotDistribution = O AND C-class = 0 AND LargestSpotSize != H AND LargestSpotSize != A AND Evolution != 1 AND HistComplex != 1 AND Evolution = 2 AND LargestSpotSize != R|C (22.0/11.0)
SpotDistribution = O AND C-class = 0 AND Evolution = 3 AND LargestSpotSize != S AND LargestSpotSize = A AND HistComplex != 1|D (13.0/7.0)
SpotDistribution = O AND C-class = 0 AND LargestSpotSize != H AND LargestSpotSize != A AND Evolution != 1 AND Evolution = 2 AND Activity = 1 AND LargestSpotSize != R|C (17.0/3.0)
SpotDistribution = O AND C-class = 0 AND LargestSpotSize != H AND Evolution = 3 AND LargestSpotSize = S AND HistComplex = 1|C (34.0/13.0)
LargestSpotSize = R AND Evolution = 3 AND HistComplex = 1 AND C-class = 1|D (8.0/3.0)
SpotDistribution != O AND LargestSpotSize = R AND Evolution = 3 AND HistComplex = 1|D (7.0/3.0)
SpotDistribution != O AND LargestSpotSize = R AND Evolution != 3|D (7.0/4.0)
SpotDistribution != O AND HistComplex = 1 AND LargestSpotSize = A AND Activity = 1|D (17.0/2.0)
SpotDistribution = O AND C-class = 0 AND Evolution = 3 AND Activity = 1 AND LargestSpotSize != A AND LargestSpotSize = S|C (9.0/4.0)
SpotDistribution != O AND HistComplex = 1 AND Activity = 1|D (15.0/8.0)
SpotDistribution != O AND LargestSpotSize != R AND C-class != 3 AND M-class = 0 AND HistComplex != 1 AND Evolution = 3 AND LargestSpotSize != K AND LargestSpotSize != S AND Activity = 1|D (13.0/4.0)
SpotDistribution != O AND LargestSpotSize != R AND C-class = 3|D (10.0/4.0)
SpotDistribution != O AND LargestSpotSize != R AND M-class = 0 AND HistComplex != 1 AND LargestSpotSize = K AND Evolution = 2|D (8.0/5.0)
SpotDistribution != O AND LargestSpotSize != K AND LargestSpotSize != R AND C-class != 2 AND M-class = 0 AND C-class = 1 AND Activity != 1|D (9.0/4.0)
SpotDistribution != O AND LargestSpotSize != K AND LargestSpotSize != R AND C-class != 2 AND M-class = 0 AND Evolution != 2 AND Activity != 1|D (12.0/5.0)
SpotDistribution != O AND LargestSpotSize != K AND LargestSpotSize != R AND M-class = 0 AND C-class != 2 AND Evolution = 2 AND LargestSpotSize = A AND Activity = 1 AND C-class = 0|D (16.0/9.0)
SpotDistribution != O AND LargestSpotSize != K AND LargestSpotSize != R AND M-class = 0 AND Activity = 1 AND Evolution = 2|D (10.0/6.0)
SpotDistribution != O AND LargestSpotSize != K AND LargestSpotSize != R AND M-class = 0 AND Activity != 1 AND LargestSpotSize = A|E (14.0/9.0)
M-class != 0|D (11.0/5.0)
SpotDistribution != O AND Evolution != 2 AND LargestSpotSize != R AND LargestSpotSize != K|D (9.0/4.0)
Evolution = 3 AND LargestSpotSize != K AND LargestSpotSize != S AND Activity = 1 AND HistComplex = 1|D (15.0/8.0)
Evolution = 3 AND LargestSpotSize != S AND Activity = 1 AND LargestSpotSize != R|D (10.0/1.0)
LargestSpotSize != H AND Evolution = 3 AND LargestSpotSize != S AND Activity != 1|D (10.0)
LargestSpotSize != H AND C-class = 0 AND Evolution = 3|D (9.0/2.0)
LargestSpotSize != H AND SpotDistribution = O AND C-class != 0 AND HistComplex = 1|C (9.0/4.0)
C-class = 0 AND HistComplex = 1 AND LargestSpotSize != A|C (11.0/4.0)
C-class = 0 AND Activity = 1 AND LargestSpotSize != S AND LargestSpotSize != R AND HistComplex != 1|C (12.0/6.0)
C-class = 0 AND Activity = 1 AND LargestSpotSize != S AND LargestSpotSize != A|C (11.0/2.0)
HistComplex != 1 AND C-class = 0 AND LargestSpotSize = S|E (11.0/7.0)
HistComplex != 1 AND LargestSpotSize = A|E (10.0/3.0)
LargestSpotSize != A|E (7.0/2.0)
|D (6.0/3.0)


## J48 Decision Tree

* SpotDistribution = X: H (239.0)
* SpotDistribution != X
	* LargestSpotSize = X: B (103.0)
	* LargestSpotSize != X
		* Area = 1
			* SpotDistribution = O: C (248.0/111.0)
			* SpotDistribution != O: D (156.0/71.0)
		* Area != 1: E (20.0/9.0)


## SimpleCart Decision Tree

		* SpotDistribution=(C)|(I)|(O)
	* LargestSpotSize=(X): B(129.0/0.0)
	* LargestSpotSize!=(X)
			* SpotDistribution=(C)|(I)
			* Area=(2)
					* Prev24Hour=(3)|(2): E(7.0/0.0)
					* Prev24Hour!=(3)|(2): F(10.0/6.0)
			* Area!=(2)
				* Evolution=(3)
						* LargestSpotSize=(S)|(R)
						* HistComplex=(2): D(11.0/6.0)
						* HistComplex!=(2): D(16.0/12.0)
						* LargestSpotSize!=(S)|(R): D(43.0/21.0)
				* Evolution!=(3)
						* C-class=(4)|(2): F(6.0/2.0)
						* C-class!=(4)|(2): D(34.0/41.0)
			* SpotDistribution!=(C)|(I)
						* LargestSpotSize=(K)|(S)|(R)|(X)
				* HistComplex=(2): C(31.0/33.0)
				* HistComplex!=(2)
							* C-class=(6)|(2)|(1): D(10.0/11.0)
							* C-class!=(6)|(2)|(1)
						* Evolution=(2)
							* Activity=(2): C(8.0/2.0)
							* Activity!=(2)
								* LargestSpotSize=(S): C(15.0/4.0)
								* LargestSpotSize!=(S): C(23.0/7.0)
						* Evolution!=(2): C(62.0/35.0)
						* LargestSpotSize!=(K)|(S)|(R)|(X)
							* C-class=(4)|(3)|(2)|(1): E(9.0/8.0)
							* C-class!=(4)|(3)|(2)|(1)
					* Activity=(2): D(4.0/5.0)
					* Activity!=(2): D(23.0/25.0)
		* SpotDistribution!=(C)|(I)|(O): H(298.0/0.0)


