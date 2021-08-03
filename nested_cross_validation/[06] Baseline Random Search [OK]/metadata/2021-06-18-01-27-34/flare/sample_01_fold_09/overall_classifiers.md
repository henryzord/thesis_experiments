# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | H | 0.311390 |
| SpotDistribution != X and LargestSpotSize = X | B | 0.134937 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution = O and LargestSpotSize != H and LargestSpotSize != A | C | 0.114263 |
| SpotDistribution = O and LargestSpotSize!=(X) and SpotDistribution != I and LargestSpotSize != X | D | 0.056003 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution != O | D | 0.078395 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution = O and LargestSpotSize != H and LargestSpotSize = A and C-class != 0 | E | 0.005230 |
| SpotDistribution != X and LargestSpotSize != X and Area != 1 and Prev24Hour != 1 | E | 0.006976 |
| SpotDistribution != X and LargestSpotSize != X and Area != 1 and Prev24Hour = 1 | F | 0.005863 |
| LargestSpotSize = A and SpotDistribution = C and X-class = 0 | E | 0.002609 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution = O and LargestSpotSize != H and LargestSpotSize = A and C-class = 0 and HistComplex != 1 and Evolution = 2 | C | 0.003911 |
| LargestSpotSize = K and SpotDistribution = C and X-class = 0 | E | 0.006088 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = X | H | 0.311390 |
| LargestSpotSize != X and SpotDistribution = O and LargestSpotSize != H and LargestSpotSize != A | C | 0.178108 |
| LargestSpotSize != X and Area = 1 | D | 0.352440 |
| LargestSpotSize = X | B | 0.440273 |
|  | E | 0.515152 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = I and Evolution = 2 and C-class = 1 and Area = 2 | F | 0.002174 |
| HistComplex = 2 and Activity = 2 and SpotDistribution = C and Evolution = 2 and LargestSpotSize = K | E | 0.006849 |
| HistComplex = 2 and Activity = 2 and SpotDistribution = C and X-class = 1 | E | 0.002294 |
| HistComplex = 2 and LargestSpotSize = A and Activity = 2 and SpotDistribution = O and Prev24Hour = 1 | E | 0.005714 |
| HistComplex = 2 and SpotDistribution = I and LargestSpotSize = S and Evolution = 2 and Activity = 1 and M-class = 0 | E | 0.002580 |
| LargestSpotSize = X | B | 0.137527 |
| SpotDistribution = O and HistComplex = 1 and Evolution = 2 and Activity = 2 and LargestSpotSize = R | C | 0.003215 |
| SpotDistribution = O and HistComplex = 1 and Evolution = 2 and Activity = 2 and Prev24Hour = 2 | C | 0.003215 |
| SpotDistribution = O and HistComplex = 1 and Evolution = 2 and LargestSpotSize = R and C-class = 0 | C | 0.026283 |
| SpotDistribution = O and HistComplex = 1 and LargestSpotSize = S and C-class = 0 and Evolution = 2 and Activity = 2 | C | 0.006677 |
| SpotDistribution = O and HistComplex = 1 and LargestSpotSize = R and C-class = 0 and M-class = 0 and Evolution = 1 | C | 0.002147 |
| SpotDistribution = O and HistComplex = 1 and LargestSpotSize = R and C-class = 0 and M-class = 0 | C | 0.029898 |
| SpotDistribution = O and LargestSpotSize = S and HistComplex = 1 and C-class = 0 and Evolution = 2 | C | 0.015605 |
| SpotDistribution = O and LargestSpotSize = S and HistComplex = 1 and C-class = 0 and Activity = 2 and Prev24Hour = 1 | C | 0.003617 |
| SpotDistribution = O and LargestSpotSize = S and HistComplex = 1 and C-class = 0 and M-class = 1 | C | 0.003215 |
| SpotDistribution = O and LargestSpotSize = S and HistComplex = 1 and C-class = 0 and Activity = 1 and Evolution = 3 | C | 0.018426 |
| SpotDistribution = O and Evolution = 2 and LargestSpotSize = R and Activity = 1 and HistComplex = 2 | C | 0.011744 |
| SpotDistribution = O and LargestSpotSize = S and Evolution = 2 and C-class = 0 and Activity = 2 | C | 0.001613 |
| SpotDistribution = O and LargestSpotSize = S and Evolution = 2 and C-class = 0 | C | 0.007287 |
| SpotDistribution = O and HistComplex = 1 and C-class = 1 | C | 0.007673 |
| SpotDistribution = O and Activity = 1 and HistComplex = 1 and LargestSpotSize = R and M-class = 0 | C | 0.000224 |
| SpotDistribution = O and Activity = 1 and C-class = 0 and LargestSpotSize = A and Evolution = 2 and HistComplex = 2 and M-class = 0 | C | 0.005733 |
| SpotDistribution = O and Activity = 1 and Evolution = 3 and LargestSpotSize = S and HistComplex = 2 | C | 0.007150 |
| SpotDistribution = O and HistComplex = 1 and Evolution = 1 | C | 0.001613 |
| SpotDistribution = O and HistComplex = 1 and C-class = 3 | C | 0.002147 |
| SpotDistribution = I and Evolution = 3 and C-class = 0 and LargestSpotSize = A and HistComplex = 1 and M-class = 1 | D | 0.004494 |
| SpotDistribution = I and Evolution = 3 and C-class = 0 and LargestSpotSize = A and HistComplex = 1 | D | 0.017960 |
| SpotDistribution = I and Evolution = 3 and LargestSpotSize = K and Area = 1 | D | 0.019912 |
| SpotDistribution = I and Evolution = 3 and C-class = 0 and LargestSpotSize = R and HistComplex = 2 | D | 0.009321 |
| SpotDistribution = I and Evolution = 3 and LargestSpotSize = A and Activity = 1 and C-class = 1 | D | 0.006726 |
| SpotDistribution = I and C-class = 0 and Evolution = 3 and M-class = 1 | D | 0.006726 |
| SpotDistribution = I and C-class = 0 and HistComplex = 1 and LargestSpotSize = A | D | 0.007175 |
| SpotDistribution = I and Evolution = 3 and C-class = 0 and HistComplex = 1 and Activity = 2 | D | 0.004494 |
| SpotDistribution = I and Evolution = 3 and C-class = 0 and Area = 1 and Activity = 1 and HistComplex = 2 and LargestSpotSize = S | D | 0.005056 |
| SpotDistribution = I and Evolution = 3 and HistComplex = 1 and LargestSpotSize = A | D | 0.004054 |
| SpotDistribution = I and C-class = 0 and LargestSpotSize = R and Evolution = 2 and HistComplex = 2 | D | 0.008949 |
| SpotDistribution = O and Evolution = 3 and Activity = 2 and LargestSpotSize = A | D | 0.008949 |
| SpotDistribution = I and Evolution = 3 and C-class = 0 and LargestSpotSize = A and Activity = 1 | D | 0.010273 |
| SpotDistribution = O and Evolution = 3 and C-class = 1 | D | 0.017738 |
|  | H | 0.504230 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

largestspotsize|spotdistribution|x-class|class
---|---|---|---
k|c|2|h
k|c|1|e
a|i|1|h
h|c|0|h
a|c|0|e
k|c|0|e
r|c|0|d
h|i|0|d
k|i|0|d
s|i|0|d
a|i|0|d
r|i|0|d
x|i|0|b
k|o|0|h
a|o|0|d
h|o|0|d
r|o|0|c
s|o|0|c
x|o|0|b
k|x|0|h
h|x|0|h
a|x|0|h
r|x|0|h
s|x|0|h

## JRip

Decision list:

rules | predicted class
---|---
(SpotDistribution = I) and (Evolution = 2) and (C-class = 1) and (Area = 2)|F (2.0/0.0)
(HistComplex = 2) and (Activity = 2) and (SpotDistribution = C) and (Evolution = 2) and (LargestSpotSize = K)|E (6.0/0.0)
(HistComplex = 2) and (Activity = 2) and (SpotDistribution = C) and (X-class = 1)|E (2.0/0.0)
(HistComplex = 2) and (LargestSpotSize = A) and (Activity = 2) and (SpotDistribution = O) and (Prev24Hour = 1)|E (5.0/0.0)
(HistComplex = 2) and (SpotDistribution = I) and (LargestSpotSize = S) and (Evolution = 2) and (Activity = 1) and (M-class = 0)|E (4.0/1.0)
(LargestSpotSize = X)|B (129.0/0.0)
(SpotDistribution = O) and (HistComplex = 1) and (Evolution = 2) and (Activity = 2) and (LargestSpotSize = R)|C (2.0/0.0)
(SpotDistribution = O) and (HistComplex = 1) and (Evolution = 2) and (Activity = 2) and (Prev24Hour = 2)|C (2.0/0.0)
(SpotDistribution = O) and (HistComplex = 1) and (Evolution = 2) and (LargestSpotSize = R) and (C-class = 0)|C (29.0/7.0)
(SpotDistribution = O) and (HistComplex = 1) and (LargestSpotSize = S) and (C-class = 0) and (Evolution = 2) and (Activity = 2)|C (6.0/1.0)
(SpotDistribution = O) and (HistComplex = 1) and (LargestSpotSize = R) and (C-class = 0) and (M-class = 0) and (Evolution = 1)|C (3.0/1.0)
(SpotDistribution = O) and (HistComplex = 1) and (LargestSpotSize = R) and (C-class = 0) and (M-class = 0)|C (50.0/17.0)
(SpotDistribution = O) and (LargestSpotSize = S) and (HistComplex = 1) and (C-class = 0) and (Evolution = 2)|C (19.0/5.0)
(SpotDistribution = O) and (LargestSpotSize = S) and (HistComplex = 1) and (C-class = 0) and (Activity = 2) and (Prev24Hour = 1)|C (3.0/0.0)
(SpotDistribution = O) and (LargestSpotSize = S) and (HistComplex = 1) and (C-class = 0) and (M-class = 1)|C (2.0/0.0)
(SpotDistribution = O) and (LargestSpotSize = S) and (HistComplex = 1) and (C-class = 0) and (Activity = 1) and (Evolution = 3)|C (28.0/10.0)
(SpotDistribution = O) and (Evolution = 2) and (LargestSpotSize = R) and (Activity = 1) and (HistComplex = 2)|C (11.0/2.0)
(SpotDistribution = O) and (LargestSpotSize = S) and (Evolution = 2) and (C-class = 0) and (Activity = 2)|C (3.0/1.0)
(SpotDistribution = O) and (LargestSpotSize = S) and (Evolution = 2) and (C-class = 0)|C (20.0/9.0)
(SpotDistribution = O) and (HistComplex = 1) and (C-class = 1)|C (17.0/8.0)
(SpotDistribution = O) and (Activity = 1) and (HistComplex = 1) and (LargestSpotSize = R) and (M-class = 0)|C (2.0/0.0)
(SpotDistribution = O) and (Activity = 1) and (C-class = 0) and (LargestSpotSize = A) and (Evolution = 2) and (HistComplex = 2) and (M-class = 0)|C (7.0/2.0)
(SpotDistribution = O) and (Activity = 1) and (Evolution = 3) and (LargestSpotSize = S) and (HistComplex = 2)|C (11.0/4.0)
(SpotDistribution = O) and (HistComplex = 1) and (Evolution = 1)|C (3.0/1.0)
(SpotDistribution = O) and (HistComplex = 1) and (C-class = 3)|C (3.0/1.0)
(SpotDistribution = I) and (Evolution = 3) and (C-class = 0) and (LargestSpotSize = A) and (HistComplex = 1) and (M-class = 1)|D (2.0/0.0)
(SpotDistribution = I) and (Evolution = 3) and (C-class = 0) and (LargestSpotSize = A) and (HistComplex = 1)|D (10.0/1.0)
(SpotDistribution = I) and (Evolution = 3) and (LargestSpotSize = K) and (Area = 1)|D (9.0/0.0)
(SpotDistribution = I) and (Evolution = 3) and (C-class = 0) and (LargestSpotSize = R) and (HistComplex = 2)|D (6.0/1.0)
(SpotDistribution = I) and (Evolution = 3) and (LargestSpotSize = A) and (Activity = 1) and (C-class = 1)|D (3.0/0.0)
(SpotDistribution = I) and (C-class = 0) and (Evolution = 3) and (M-class = 1)|D (3.0/0.0)
(SpotDistribution = I) and (C-class = 0) and (HistComplex = 1) and (LargestSpotSize = A)|D (4.0/0.0)
(SpotDistribution = I) and (Evolution = 3) and (C-class = 0) and (HistComplex = 1) and (Activity = 2)|D (2.0/0.0)
(SpotDistribution = I) and (Evolution = 3) and (C-class = 0) and (Area = 1) and (Activity = 1) and (HistComplex = 2) and (LargestSpotSize = S)|D (4.0/1.0)
(SpotDistribution = I) and (Evolution = 3) and (HistComplex = 1) and (LargestSpotSize = A)|D (4.0/1.0)
(SpotDistribution = I) and (C-class = 0) and (LargestSpotSize = R) and (Evolution = 2) and (HistComplex = 2)|D (4.0/0.0)
(SpotDistribution = O) and (Evolution = 3) and (Activity = 2) and (LargestSpotSize = A)|D (4.0/0.0)
(SpotDistribution = I) and (Evolution = 3) and (C-class = 0) and (LargestSpotSize = A) and (Activity = 1)|D (13.0/5.0)
(SpotDistribution = O) and (Evolution = 3) and (C-class = 1)|D (2.0/0.0)
|H (518.0/220.0)


## PART

Decision list:

rules | predicted class
---|---
SpotDistribution = X|H (199.0)
LargestSpotSize != X AND SpotDistribution = O AND LargestSpotSize != H AND LargestSpotSize != A|C (164.0/63.0)
LargestSpotSize != X AND Area = 1|D (177.0/86.0)
LargestSpotSize = X|B (85.0)
|E (13.0/7.0)


## J48 Decision Tree

* SpotDistribution = X: H (199.0)
* SpotDistribution != X
	* LargestSpotSize = X: B (86.0)
	* LargestSpotSize != X
		* Area = 1
			* SpotDistribution = O
				* LargestSpotSize = H: D (10.0/5.0)
				* LargestSpotSize != H
					* LargestSpotSize = A
						* C-class = 0
							* HistComplex = 1: D (8.0/2.0)
							* HistComplex != 1
								* Evolution = 2: C (8.0/3.0)
								* Evolution != 2: D (10.0/5.0)
						* C-class != 0: E (6.0/3.0)
					* LargestSpotSize != A: C (159.0/60.0)
			* SpotDistribution != O: D (138.0/63.0)
		* Area != 1
			* Prev24Hour = 1: F (10.0/4.0)
			* Prev24Hour != 1: E (4.0)


## SimpleCart Decision Tree

		* SpotDistribution=(C)|(I)|(O)
	* LargestSpotSize=(X): B(129.0/0.0)
	* LargestSpotSize!=(X)
			* SpotDistribution=(C)|(I)
			* Area=(2): E(11.0/11.0)
			* Area!=(2)
				* Evolution=(3)
						* LargestSpotSize=(S)|(R)
						* HistComplex=(2): D(12.0/7.0)
						* HistComplex!=(2): D(15.0/11.0)
						* LargestSpotSize!=(S)|(R): D(46.0/18.0)
				* Evolution!=(3)
								* C-class=(0)|(1)|(6)|(7): D(33.0/38.0)
								* C-class!=(0)|(1)|(6)|(7): E(6.0/9.0)
			* SpotDistribution!=(C)|(I)
					* LargestSpotSize=(S)|(R)|(X)
				* HistComplex=(2): C(34.0/35.0)
				* HistComplex!=(2)
					* Activity=(2): C(14.0/2.0)
					* Activity!=(2)
									* C-class=(0)|(4)|(7)|(8)
							* Evolution=(2)
								* LargestSpotSize=(S): C(14.0/5.0)
								* LargestSpotSize!=(S): C(22.0/7.0)
							* Evolution!=(2): C(56.0/30.0)
									* C-class!=(0)|(4)|(7)|(8): D(10.0/12.0)
					* LargestSpotSize!=(S)|(R)|(X): D(31.0/41.0)
		* SpotDistribution!=(C)|(I)|(O): H(298.0/0.0)


