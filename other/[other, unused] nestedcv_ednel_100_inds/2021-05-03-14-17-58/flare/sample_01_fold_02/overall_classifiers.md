# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = X | H | 0.311390 |
| SpotDistribution != X and LargestSpotSize = X | B | 0.134031 |
| SpotDistribution = O and LargestSpotSize!=(X) and SpotDistribution != I and LargestSpotSize != K and C-class != 1 and LargestSpotSize!=(H) and Activity!=(2) | C | 0.094609 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution != O | D | 0.078696 |
| LargestSpotSize = A and SpotDistribution = O and BecomeHist = 2 | D | 0.013567 |
| LargestSpotSize = K and SpotDistribution = C and BecomeHist = 2 | E | 0.008613 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution = O and LargestSpotSize != H and LargestSpotSize = A and C-class != 0 | E | 0.005230 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution = O and LargestSpotSize = H | D | 0.004408 |
| LargestSpotSize = A and SpotDistribution = C and BecomeHist = 2 | E | 0.002867 |
| LargestSpotSize = H and SpotDistribution = I and BecomeHist = 2 | E | 0.001527 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution = O and LargestSpotSize != H and LargestSpotSize != A | C | 0.114263 |
| SpotDistribution != X and LargestSpotSize != X and Area != 1 | E | 0.008398 |
| SpotDistribution = O and LargestSpotSize!=(X) and SpotDistribution != I and LargestSpotSize != K and C-class = 2 | E | 0.000658 |
| SpotDistribution = O and LargestSpotSize!=(X) and SpotDistribution != I and LargestSpotSize != K and C-class = 1 | E | 0.000974 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = X | H | 0.311390 |
| LargestSpotSize = X | B | 0.194825 |
| SpotDistribution = O and HistComplex = 1 and C-class = 0 and LargestSpotSize = R | C | 0.123260 |
| Area = 1 and SpotDistribution = O and LargestSpotSize = S | C | 0.115200 |
| Area = 1 and SpotDistribution = I and HistComplex = 2 and Evolution = 3 | D | 0.127023 |
| Area = 1 and Activity = 1 and C-class = 0 and SpotDistribution = I | D | 0.111187 |
| Area = 1 and Activity = 2 and Evolution = 2 | E | 0.029009 |
| Area = 1 and SpotDistribution = O and LargestSpotSize = A | D | 0.069264 |
| Area = 2 | E | 0.034497 |
| SpotDistribution = O and LargestSpotSize = R | C | 0.018249 |
|  | D | 0.466135 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| HistComplex = 2 and SpotDistribution = C | E | 0.011214 |
| LargestSpotSize = X | B | 0.136315 |
| SpotDistribution = O and HistComplex = 1 | C | 0.122689 |
| SpotDistribution = O and Activity = 1 and Evolution = 2 and C-class = 0 | C | 0.013835 |
| SpotDistribution = I | D | 0.123853 |
|  | H | 0.535009 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

largestspotsize|spotdistribution|becomehist|class
---|---|---|---
r|c|2|d
h|c|2|h
a|c|2|e
k|c|2|e
s|i|2|d
k|i|2|d
r|i|2|d
h|i|2|e
a|i|2|d
x|i|2|b
h|o|2|d
s|o|2|c
a|o|2|d
r|o|2|c
x|o|2|b
h|x|2|h
s|x|2|h
a|x|2|h
r|x|2|h
k|x|1|h
h|x|1|h
r|x|1|h
a|x|1|h
s|x|1|h

## JRip

Decision list:

rules | predicted class
---|---
(HistComplex = 2) and (SpotDistribution = C)|E (26.0/10.0)
(LargestSpotSize = X)|B (128.0/0.0)
(SpotDistribution = O) and (HistComplex = 1)|C (206.0/75.0)
(SpotDistribution = O) and (Activity = 1) and (Evolution = 2) and (C-class = 0)|C (37.0/16.0)
(SpotDistribution = I)|D (187.0/83.0)
|H (373.0/75.0)


## PART

Decision list:

rules | predicted class
---|---
SpotDistribution = X|H (261.0)
LargestSpotSize = X|B (113.0)
SpotDistribution = O AND HistComplex = 1 AND C-class = 0 AND LargestSpotSize = R|C (82.0/25.0)
Area = 1 AND SpotDistribution = O AND LargestSpotSize = S|C (106.0/44.0)
Area = 1 AND SpotDistribution = I AND HistComplex = 2 AND Evolution = 3|D (51.0/17.0)
Area = 1 AND Activity = 1 AND C-class = 0 AND SpotDistribution = I|D (46.0/14.0)
Area = 1 AND Activity = 2 AND Evolution = 2|E (41.0/25.0)
Area = 1 AND SpotDistribution = O AND LargestSpotSize = A|D (49.0/28.0)
Area = 2|E (22.0/9.0)
SpotDistribution = O AND LargestSpotSize = R|C (19.0/8.0)
|D (48.0/25.0)


## J48 Decision Tree

* SpotDistribution = X: H (298.0)
* SpotDistribution != X
	* LargestSpotSize = X: B (128.0)
	* LargestSpotSize != X
		* Area = 1
			* SpotDistribution = O
				* LargestSpotSize = H: D (15.0/8.0)
				* LargestSpotSize != H
					* LargestSpotSize = A
						* C-class = 0: D (44.0/25.0)
						* C-class != 0: E (14.0/6.0)
					* LargestSpotSize != A: C (241.0/90.0)
			* SpotDistribution != O: D (194.0/86.0)
		* Area != 1: E (23.0/10.0)


## SimpleCart Decision Tree

		* SpotDistribution=(C)|(I)|(O)
	* LargestSpotSize=(X): B(128.0/0.0)
	* LargestSpotSize!=(X)
			* SpotDistribution=(C)|(I)
			* Area=(2): E(12.0/10.0)
			* Area!=(2)
				* Evolution=(2)
							* C-class=(4)|(2)|(1): F(12.0/12.0)
							* C-class!=(4)|(2)|(1): D(26.0/31.0)
				* Evolution!=(2): D(74.0/39.0)
			* SpotDistribution!=(C)|(I)
						* LargestSpotSize=(S)|(R)|(X)|(K)
				* HistComplex=(2): C(29.0/32.0)
				* HistComplex!=(2)
						* C-class=(2)|(1): D(10.0/9.0)
						* C-class!=(2)|(1)
						* Evolution=(3): C(63.0/33.0)
						* Evolution!=(3)
							* Activity=(2): C(9.0/2.0)
							* Activity!=(2)
								* LargestSpotSize=(S): C(14.0/6.0)
								* LargestSpotSize!=(S): C(28.0/7.0)
						* LargestSpotSize!=(S)|(R)|(X)|(K)
							* C-class=(4)|(3)|(2)|(1): E(10.0/8.0)
							* C-class!=(4)|(3)|(2)|(1)
					* LargestSpotSize=(H): D(7.0/4.0)
					* LargestSpotSize!=(H)
						* Activity=(2): D(3.0/4.0)
						* Activity!=(2): C(17.0/20.0)
		* SpotDistribution!=(C)|(I)|(O): H(298.0/0.0)


