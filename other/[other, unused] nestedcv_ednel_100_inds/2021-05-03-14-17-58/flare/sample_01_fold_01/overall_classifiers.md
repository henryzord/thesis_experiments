# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = X | H | 0.309549 |
| SpotDistribution != X and LargestSpotSize = X | B | 0.134595 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution = O and LargestSpotSize != H and C-class = 0 and LargestSpotSize != A and HistComplex = 1 | C | 0.093176 |
| LargestSpotSize = A and SpotDistribution = I | D | 0.043583 |
| SpotDistribution = O and LargestSpotSize!=(X) and SpotDistribution != I and C-class != 8 and LargestSpotSize = R | D | 0.016455 |
| SpotDistribution = O and LargestSpotSize!=(X) and SpotDistribution != I and C-class != 8 and LargestSpotSize = S | D | 0.017272 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution = O and LargestSpotSize != H and C-class = 0 and LargestSpotSize != A and HistComplex != 1 and Evolution = 2 | C | 0.017288 |
| LargestSpotSize = A and SpotDistribution = O | D | 0.014572 |
| SpotDistribution = O and LargestSpotSize!=(X) and SpotDistribution != I and C-class != 8 and LargestSpotSize != X | E | 0.004119 |
| LargestSpotSize = R and SpotDistribution = I | D | 0.014900 |
| LargestSpotSize = S and SpotDistribution = O | C | 0.053239 |
| LargestSpotSize = S and SpotDistribution = I | D | 0.011303 |
| LargestSpotSize = K and SpotDistribution = C | E | 0.008681 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution = O and LargestSpotSize != H and C-class = 0 and LargestSpotSize = A and HistComplex != 1 and Evolution = 2 | C | 0.004278 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution != O and HistComplex != 1 and C-class != 4 and LargestSpotSize != R and Prev24Hour = 1 and LargestSpotSize = K | D | 0.007797 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution != O and HistComplex != 1 and C-class != 4 and LargestSpotSize != R and Prev24Hour = 1 and LargestSpotSize != K and C-class != 2 and C-class != 1 and SpotDistribution = I and C-class != 0 | E | 0.003592 |
| LargestSpotSize = R and SpotDistribution = O | C | 0.062146 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution = O and LargestSpotSize = H | D | 0.003494 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution != O and HistComplex != 1 and C-class = 4 | F | 0.001967 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution != O and HistComplex != 1 and C-class != 4 and LargestSpotSize != R and Prev24Hour = 1 and LargestSpotSize != K and C-class = 2 | F | 0.001641 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution != O and HistComplex != 1 and C-class != 4 and LargestSpotSize != R and Prev24Hour = 1 and LargestSpotSize != K and C-class != 2 and C-class != 1 and SpotDistribution != I | E | 0.002071 |
| LargestSpotSize = A and SpotDistribution = C | D | 0.002174 |
| SpotDistribution != X and LargestSpotSize != X and Area != 1 | E | 0.009001 |
| LargestSpotSize = R and SpotDistribution = C | E | 0.000576 |
| LargestSpotSize = K and SpotDistribution = I | D | 0.007797 |
| LargestSpotSize = H and SpotDistribution = I | D | 0.000452 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution != O and HistComplex = 1 | D | 0.033465 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = X | H | 0.309549 |
| LargestSpotSize = A | D | 0.098500 |
| LargestSpotSize = R | C | 0.119458 |
| LargestSpotSize = X | B | 0.262295 |
| Area = 1 and SpotDistribution = O and LargestSpotSize = S and C-class = 0 and HistComplex = 1 | C | 0.115031 |
| Area = 2 | E | 0.033504 |
| SpotDistribution = O and LargestSpotSize = S and C-class = 0 and Evolution = 2 | C | 0.024383 |
|  | D | 0.449827 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| HistComplex = 2 and Activity = 2 and SpotDistribution = C and Prev24Hour = 3 | E | 0.005161 |
| HistComplex = 2 and Activity = 2 and SpotDistribution = C and Evolution = 2 and C-class = 0 | E | 0.003674 |
| HistComplex = 2 and Activity = 2 and LargestSpotSize = H | E | 0.003674 |
| LargestSpotSize = X | B | 0.136606 |
| SpotDistribution = O and HistComplex = 1 and C-class = 0 and Evolution = 2 and LargestSpotSize = R | C | 0.029078 |
| SpotDistribution = O and HistComplex = 1 and C-class = 0 and LargestSpotSize = S and Evolution = 2 | C | 0.024764 |
| SpotDistribution = O and HistComplex = 1 and C-class = 0 and LargestSpotSize = R and Evolution = 1 | C | 0.005120 |
| SpotDistribution = O and HistComplex = 1 and C-class = 0 and LargestSpotSize = S and Activity = 2 | C | 0.003669 |
| SpotDistribution = O and C-class = 0 and HistComplex = 1 and LargestSpotSize = R and M-class = 0 | C | 0.031051 |
| SpotDistribution = O and C-class = 0 and LargestSpotSize = S and HistComplex = 1 | C | 0.017668 |
| SpotDistribution = O and Evolution = 2 and C-class = 0 and LargestSpotSize = R and Activity = 1 | C | 0.006062 |
| SpotDistribution = O and C-class = 0 and Evolution = 2 and LargestSpotSize = S | C | 0.009415 |
| SpotDistribution = I and Evolution = 3 and HistComplex = 1 and LargestSpotSize = A | D | 0.028070 |
| SpotDistribution = I and Evolution = 3 and C-class = 0 | D | 0.042807 |
| SpotDistribution = O and Evolution = 3 and C-class = 1 | D | 0.015988 |
| SpotDistribution = I and Area = 1 and LargestSpotSize = K and Evolution = 3 | D | 0.012685 |
| SpotDistribution = O and Evolution = 3 and Activity = 2 | D | 0.006993 |
| SpotDistribution = I and C-class = 0 and LargestSpotSize = R and Evolution = 2 and HistComplex = 2 | D | 0.008493 |
| SpotDistribution = O and Evolution = 3 and LargestSpotSize = H and HistComplex = 2 | D | 0.005686 |
| SpotDistribution = I and LargestSpotSize = A and Activity = 1 and HistComplex = 1 | D | 0.005686 |
|  | H | 0.493311 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

largestspotsize|spotdistribution|class
---|---|---
h|c|h
r|c|e
k|c|e
a|c|d
h|i|d
r|i|d
k|i|d
s|i|d
a|i|d
x|i|b
k|o|h
a|o|d
h|o|d
r|o|c
s|o|c
x|o|b
k|x|h
a|x|h
h|x|h
r|x|h
s|x|h

## JRip

Decision list:

rules | predicted class
---|---
(HistComplex = 2) and (Activity = 2) and (SpotDistribution = C) and (Prev24Hour = 3)|E (8.0/2.0)
(HistComplex = 2) and (Activity = 2) and (SpotDistribution = C) and (Evolution = 2) and (C-class = 0)|E (4.0/0.0)
(HistComplex = 2) and (Activity = 2) and (LargestSpotSize = H)|E (5.0/1.0)
(LargestSpotSize = X)|B (128.0/0.0)
(SpotDistribution = O) and (HistComplex = 1) and (C-class = 0) and (Evolution = 2) and (LargestSpotSize = R)|C (31.0/7.0)
(SpotDistribution = O) and (HistComplex = 1) and (C-class = 0) and (LargestSpotSize = S) and (Evolution = 2)|C (28.0/7.0)
(SpotDistribution = O) and (HistComplex = 1) and (C-class = 0) and (LargestSpotSize = R) and (Evolution = 1)|C (5.0/1.0)
(SpotDistribution = O) and (HistComplex = 1) and (C-class = 0) and (LargestSpotSize = S) and (Activity = 2)|C (5.0/1.0)
(SpotDistribution = O) and (C-class = 0) and (HistComplex = 1) and (LargestSpotSize = R) and (M-class = 0)|C (51.0/17.0)
(SpotDistribution = O) and (C-class = 0) and (LargestSpotSize = S) and (HistComplex = 1)|C (32.0/11.0)
(SpotDistribution = O) and (Evolution = 2) and (C-class = 0) and (LargestSpotSize = R) and (Activity = 1)|C (10.0/2.0)
(SpotDistribution = O) and (C-class = 0) and (Evolution = 2) and (LargestSpotSize = S)|C (22.0/9.0)
(SpotDistribution = I) and (Evolution = 3) and (HistComplex = 1) and (LargestSpotSize = A)|D (19.0/3.0)
(SpotDistribution = I) and (Evolution = 3) and (C-class = 0)|D (50.0/18.0)
(SpotDistribution = O) and (Evolution = 3) and (C-class = 1)|D (16.0/5.0)
(SpotDistribution = I) and (Area = 1) and (LargestSpotSize = K) and (Evolution = 3)|D (6.0/0.0)
(SpotDistribution = O) and (Evolution = 3) and (Activity = 2)|D (9.0/3.0)
(SpotDistribution = I) and (C-class = 0) and (LargestSpotSize = R) and (Evolution = 2) and (HistComplex = 2)|D (4.0/0.0)
(SpotDistribution = O) and (Evolution = 3) and (LargestSpotSize = H) and (HistComplex = 2)|D (6.0/2.0)
(SpotDistribution = I) and (LargestSpotSize = A) and (Activity = 1) and (HistComplex = 1)|D (4.0/0.0)
|H (510.0/215.0)


## PART

Decision list:

rules | predicted class
---|---
SpotDistribution = X|H (246.0)
LargestSpotSize = A|D (128.0/59.0)
LargestSpotSize = R|C (119.0/51.0)
LargestSpotSize = X|B (106.0)
Area = 1 AND SpotDistribution = O AND LargestSpotSize = S AND C-class = 0 AND HistComplex = 1|C (58.0/17.0)
Area = 2|E (20.0/9.0)
SpotDistribution = O AND LargestSpotSize = S AND C-class = 0 AND Evolution = 2|C (19.0/7.0)
|D (99.0/53.0)


## J48 Decision Tree

* SpotDistribution = X: H (197.0)
* SpotDistribution != X
	* LargestSpotSize = X: B (85.0)
	* LargestSpotSize != X
		* Area = 1
			* SpotDistribution = O
				* LargestSpotSize = H: D (11.0/7.0)
				* LargestSpotSize != H
					* C-class = 0
						* LargestSpotSize = A
							* HistComplex = 1: D (13.0/5.0)
							* HistComplex != 1
								* Evolution = 2: C (8.0/4.0)
								* Evolution != 2: D (6.0/2.0)
						* LargestSpotSize != A
							* HistComplex = 1: C (94.0/24.0)
							* HistComplex != 1
								* Evolution = 2: C (22.0/9.0)
								* Evolution != 2: D (14.0/6.0)
					* C-class != 0: D (32.0/15.0)
			* SpotDistribution != O
				* HistComplex = 1: D (43.0/12.0)
				* HistComplex != 1
					* C-class = 4: F (5.0/2.0)
					* C-class != 4
						* LargestSpotSize = R: D (7.0/3.0)
						* LargestSpotSize != R
							* Prev24Hour = 1
								* LargestSpotSize = K: D (9.0/4.0)
								* LargestSpotSize != K
									* C-class = 2: F (6.0/3.0)
									* C-class != 2
										* C-class = 1: D (15.0/7.0)
										* C-class != 1
											* SpotDistribution = I
												* C-class = 0: D (40.0/24.0)
												* C-class != 0: E (5.0/2.0)
											* SpotDistribution != I: E (5.0/2.0)
							* Prev24Hour != 1: D (5.0/1.0)
		* Area != 1: E (14.0/5.0)


## SimpleCart Decision Tree

		* SpotDistribution=(C)|(I)|(O)
	* LargestSpotSize=(X): B(128.0/0.0)
	* LargestSpotSize!=(X)
			* SpotDistribution=(C)|(I)
			* Area=(2)
					* Prev24Hour=(3)|(2): E(7.0/1.0)
					* Prev24Hour!=(3)|(2): F(9.0/7.0)
			* Area!=(2)
				* HistComplex=(2)
					* Evolution=(3): D(38.0/23.0)
					* Evolution!=(3)
									* C-class=(0)|(6)|(7)|(8): D(23.0/26.0)
									* C-class!=(0)|(6)|(7)|(8): F(12.0/17.0)
				* HistComplex!=(2): D(38.0/19.0)
			* SpotDistribution!=(C)|(I)
					* C-class=(0)|(7)|(8)
							* LargestSpotSize=(S)|(R)|(X)|(K)
					* HistComplex=(2)
						* Evolution=(2): C(21.0/12.0)
						* Evolution!=(2): D(12.0/11.0)
					* HistComplex!=(2): C(109.0/45.0)
							* LargestSpotSize!=(S)|(R)|(X)|(K): D(25.0/26.0)
					* C-class!=(0)|(7)|(8)
						* LargestSpotSize=(S)|(R)|(X): D(17.0/14.0)
						* LargestSpotSize!=(S)|(R)|(X): E(10.0/8.0)
		* SpotDistribution!=(C)|(I)|(O): H(295.0/0.0)


