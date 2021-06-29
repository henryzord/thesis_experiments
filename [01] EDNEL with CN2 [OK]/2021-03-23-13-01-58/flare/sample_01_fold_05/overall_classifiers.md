# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = X | H | 0.311715 |
| SpotDistribution != X and LargestSpotSize = X | B | 0.134172 |
| SpotDistribution = O and LargestSpotSize!=(X) and SpotDistribution != I and LargestSpotSize != X and Activity!=(2) | D | 0.055391 |
| LargestSpotSize = R and SpotDistribution = O and Area = 1 and X-class = 0 | C | 0.059375 |
| LargestSpotSize = S and SpotDistribution = O and Area = 1 and X-class = 0 | C | 0.055406 |
| LargestSpotSize = A and SpotDistribution = I and Area = 1 and X-class = 0 | D | 0.044792 |
| LargestSpotSize = R and SpotDistribution = I and Area = 1 and X-class = 0 | D | 0.015449 |
| SpotDistribution != X and LargestSpotSize != X and Area != 1 and Prev24Hour != 1 | E | 0.006984 |
| LargestSpotSize = K and SpotDistribution = I and Area = 1 and X-class = 0 | D | 0.011324 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution = O and LargestSpotSize != H and LargestSpotSize = A and C-class = 0 and Activity = 1 and Evolution = 2 | C | 0.006402 |
| LargestSpotSize = S and SpotDistribution = I and Area = 1 and X-class = 0 | D | 0.010068 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution = O and LargestSpotSize != H and LargestSpotSize = A and C-class != 0 and Evolution = 2 | E | 0.004577 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution != O and HistComplex != 1 and LargestSpotSize != R and SpotDistribution = I and M-class = 0 and LargestSpotSize != K and C-class != 2 and C-class != 1 and Activity != 1 and LargestSpotSize = S | E | 0.003580 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution != O and HistComplex != 1 and LargestSpotSize != R and SpotDistribution != I | E | 0.004124 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution != O and HistComplex != 1 and LargestSpotSize != R and SpotDistribution = I and M-class = 0 and LargestSpotSize != K and C-class != 2 and C-class != 1 and Activity != 1 and LargestSpotSize != S and Evolution = 2 | F | 0.002723 |
| SpotDistribution != X and LargestSpotSize != X and Area != 1 and Prev24Hour = 1 and C-class != 1 | F | 0.003561 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution = O and LargestSpotSize != H and LargestSpotSize = A and C-class = 0 and Activity = 1 and Evolution != 2 and HistComplex = 1 | C | 0.002611 |
| LargestSpotSize = K and SpotDistribution = C and Area = 2 and X-class = 0 | E | 0.006095 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution != O and HistComplex != 1 and LargestSpotSize != R and SpotDistribution = I and M-class = 0 and LargestSpotSize != K and C-class = 2 | F | 0.002179 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution = O and LargestSpotSize = H and Evolution = 2 | E | 0.001478 |
| LargestSpotSize = H and SpotDistribution = I and Area = 1 and X-class = 0 | E | 0.001529 |
| LargestSpotSize = A and SpotDistribution = I and Area = 2 and X-class = 0 | F | 0.002174 |
| LargestSpotSize = R and SpotDistribution = C and Area = 1 and X-class = 0 | D | 0.001797 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution = O and LargestSpotSize != H and LargestSpotSize != A and C-class != 1 and LargestSpotSize != S and HistComplex = 1 and Evolution != 3 | C | 0.024188 |
| LargestSpotSize = K and SpotDistribution = C and Area = 1 and X-class = 0 | F | 0.000545 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution != O and HistComplex = 1 and LargestSpotSize = A and Activity != 1 | D | 0.008032 |
| LargestSpotSize = A and SpotDistribution = C and Area = 1 and X-class = 0 | E | 0.003186 |
| SpotDistribution != X and LargestSpotSize != X and Area != 1 and Prev24Hour = 1 and C-class = 1 | F | 0.001634 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution != O and HistComplex != 1 and LargestSpotSize != R and SpotDistribution = I and M-class = 0 and LargestSpotSize != K and C-class != 2 and C-class != 1 and Activity != 1 and LargestSpotSize != S and Evolution != 2 | D | 0.002699 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = X | H | 0.311715 |
| LargestSpotSize = X | B | 0.195122 |
| SpotDistribution = C and M-class = 0 and LargestSpotSize = K and Prev24Hour = 1 | F | 0.006465 |
| SpotDistribution = O and C-class = 0 and LargestSpotSize = S | C | 0.111463 |
| HistComplex = 1 and SpotDistribution = I | D | 0.090640 |
| SpotDistribution = O and Activity = 1 and LargestSpotSize = R | C | 0.137109 |
| Area = 2 and X-class = 0 and LargestSpotSize = K | E | 0.029017 |
| SpotDistribution = C and Evolution = 3 and C-class = 0 | E | 0.015152 |
| SpotDistribution = C and Evolution = 3 | D | 0.019290 |
| SpotDistribution = I and LargestSpotSize = A and Area = 1 | D | 0.115625 |
| SpotDistribution = I and LargestSpotSize = K | D | 0.043902 |
| Area = 1 and SpotDistribution = O and LargestSpotSize = S and C-class = 1 and Prev24Hour = 1 | C | 0.016247 |
| Area = 1 and C-class = 3 | E | 0.018779 |
| Area = 1 and C-class = 5 | E | 0.014085 |
| Area = 2 | F | 0.022591 |
| C-class = 0 and Activity = 2 and HistComplex = 1 and LargestSpotSize = A | D | 0.014388 |
| C-class = 0 and Activity = 2 and HistComplex = 2 and Prev24Hour = 1 | E | 0.033465 |
| SpotDistribution = O and C-class = 0 and Prev24Hour = 1 and LargestSpotSize = A | C | 0.041493 |
| Evolution = 3 and HistComplex = 2 and M-class = 0 | D | 0.143800 |
| Prev24Hour = 3 | D | 0.013986 |
| HistComplex = 2 and C-class = 1 | E | 0.036923 |
| C-class = 0 and HistComplex = 2 | D | 0.120563 |
| C-class = 0 | C | 0.054797 |
| C-class = 1 | D | 0.118007 |
| Activity = 1 and LargestSpotSize = A | E | 0.091093 |
| M-class = 0 | E | 0.155763 |
|  | D | 0.549451 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

largestspotsize|spotdistribution|area|x-class|class
---|---|---|---|---
k|c|2|2|h
k|c|2|1|e
a|i|1|1|h
k|c|2|0|e
a|i|2|0|f
k|i|2|0|f
r|o|2|0|h
k|c|1|0|f
h|c|1|0|h
a|c|1|0|e
r|c|1|0|d
x|i|1|0|b
h|i|1|0|e
k|i|1|0|d
r|i|1|0|d
s|i|1|0|d
a|i|1|0|d
x|o|1|0|b
k|o|1|0|h
h|o|1|0|d
a|o|1|0|d
r|o|1|0|c
s|o|1|0|c
h|x|1|0|h
r|x|1|0|h
a|x|1|0|h
s|x|1|0|h

## PART

Decision list:

rules | predicted class
---|---
SpotDistribution = X|H (298.0)
LargestSpotSize = X|B (128.0)
SpotDistribution = C AND M-class = 0 AND LargestSpotSize = K AND Prev24Hour = 1|F (5.0/1.0)
SpotDistribution = O AND C-class = 0 AND LargestSpotSize = S|C (105.0/40.0)
HistComplex = 1 AND SpotDistribution = I|D (51.0/16.0)
SpotDistribution = O AND Activity = 1 AND LargestSpotSize = R|C (107.0/37.0)
Area = 2 AND X-class = 0 AND LargestSpotSize = K|E (14.0/4.0)
SpotDistribution = C AND Evolution = 3 AND C-class = 0|E (6.0/1.0)
SpotDistribution = C AND Evolution = 3|D (6.0/2.0)
SpotDistribution = I AND LargestSpotSize = A AND Area = 1|D (72.0/35.0)
SpotDistribution = I AND LargestSpotSize = K|D (17.0/5.0)
Area = 1 AND SpotDistribution = O AND LargestSpotSize = S AND C-class = 1 AND Prev24Hour = 1|C (13.0/6.0)
Area = 1 AND C-class = 3|E (5.0/2.0)
Area = 1 AND C-class = 5|E (3.0)
Area = 2|F (3.0)
C-class = 0 AND Activity = 2 AND HistComplex = 1 AND LargestSpotSize = A|D (2.0)
C-class = 0 AND Activity = 2 AND HistComplex = 2 AND Prev24Hour = 1|E (16.0/6.0)
SpotDistribution = O AND C-class = 0 AND Prev24Hour = 1 AND LargestSpotSize = A|C (35.0/18.0)
Evolution = 3 AND HistComplex = 2 AND M-class = 0|D (19.0/5.0)
Prev24Hour = 3|D (4.0/2.0)
HistComplex = 2 AND C-class = 1|E (14.0/7.0)
C-class = 0 AND HistComplex = 2|D (12.0/4.0)
C-class = 0|C (5.0/2.0)
C-class = 1|D (5.0/2.0)
Activity = 1 AND LargestSpotSize = A|E (3.0/1.0)
M-class = 0|E (5.0/2.0)
|D (3.0/1.0)


## J48 Decision Tree

* SpotDistribution = X: H (298.0)
* SpotDistribution != X
	* LargestSpotSize = X: B (128.0)
	* LargestSpotSize != X
		* Area = 1
			* SpotDistribution = O
				* LargestSpotSize = H
					* Evolution = 2: E (7.0/4.0)
					* Evolution != 2: D (7.0/3.0)
				* LargestSpotSize != H
					* LargestSpotSize = A
						* C-class = 0
							* Activity = 1
								* Evolution = 2: C (13.0/5.0)
								* Evolution != 2
									* HistComplex = 1: C (8.0/4.0)
									* HistComplex != 1: D (14.0/6.0)
							* Activity != 1: D (7.0/4.0)
						* C-class != 0
							* Evolution = 2: E (9.0/3.0)
							* Evolution != 2: D (6.0/2.0)
					* LargestSpotSize != A
						* C-class = 1
							* HistComplex = 1
								* LargestSpotSize = R: D (7.0/2.0)
								* LargestSpotSize != R: D (10.0/5.0)
							* HistComplex != 1: C (7.0/3.0)
						* C-class != 1
							* LargestSpotSize = S
								* C-class = 0
									* Evolution = 1: D (10.0/6.0)
									* Evolution != 1
										* HistComplex = 1
											* Activity = 1
												* Evolution = 2: C (20.0/5.0)
												* Evolution != 2: C (33.0/11.0)
											* Activity != 1: C (12.0/3.0)
										* HistComplex != 1
											* Evolution = 2: C (20.0/9.0)
											* Evolution != 2: D (10.0/5.0)
								* C-class != 0: D (8.0/5.0)
							* LargestSpotSize != S
								* HistComplex = 1
									* Evolution = 3: C (55.0/19.0)
									* Evolution != 3: C (33.0/8.0)
								* HistComplex != 1: C (14.0/5.0)
			* SpotDistribution != O
				* HistComplex = 1
					* LargestSpotSize = A
						* Activity = 1: D (17.0/3.0)
						* Activity != 1: D (6.0)
					* LargestSpotSize != A
						* C-class = 0
							* LargestSpotSize = R: D (9.0/4.0)
							* LargestSpotSize != R: D (12.0/6.0)
						* C-class != 0: D (11.0/5.0)
				* HistComplex != 1
					* LargestSpotSize = R
						* Evolution = 3: D (8.0/1.0)
						* Evolution != 3: D (7.0/3.0)
					* LargestSpotSize != R
						* SpotDistribution = I
							* M-class = 0
								* LargestSpotSize = K
									* Evolution = 2: D (9.0/5.0)
									* Evolution != 2: D (7.0)
								* LargestSpotSize != K
									* C-class = 2: F (8.0/4.0)
									* C-class != 2
										* C-class = 1
											* Evolution = 2: D (9.0/3.0)
											* Evolution != 2: D (6.0/3.0)
										* C-class != 1
											* Activity = 1
												* Evolution = 2: D (22.0/12.0)
												* Evolution != 2: D (19.0/9.0)
											* Activity != 1
												* LargestSpotSize = S: E (8.0/3.0)
												* LargestSpotSize != S
													* Evolution = 2: F (10.0/5.0)
													* Evolution != 2: D (8.0/4.0)
							* M-class != 0: D (9.0/2.0)
						* SpotDistribution != I: E (10.0/4.0)
		* Area != 1
			* Prev24Hour = 1
				* C-class = 1: F (6.0/3.0)
				* C-class != 1: F (11.0/5.0)
			* Prev24Hour != 1: E (8.0/1.0)


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
					* Evolution=(3)
						* LargestSpotSize=(S): D(4.0/6.0)
						* LargestSpotSize!=(S)
								* LargestSpotSize=(K)|(R): D(15.0/2.0)
								* LargestSpotSize!=(K)|(R): D(19.0/17.0)
					* Evolution!=(3)
										* C-class=(0)|(1)|(6)|(7)|(8): D(31.0/33.0)
										* C-class!=(0)|(1)|(6)|(7)|(8): F(6.0/7.0)
				* HistComplex!=(2)
									* LargestSpotSize=(S)|(R)|(X)|(K)|(H): D(17.0/15.0)
									* LargestSpotSize!=(S)|(R)|(X)|(K)|(H): D(20.0/3.0)
			* SpotDistribution!=(C)|(I)
					* LargestSpotSize=(S)|(R)|(X)
							* C-class=(0)|(4)|(7)|(8)
					* HistComplex=(2): C(26.0/26.0)
					* HistComplex!=(2): C(106.0/47.0)
							* C-class!=(0)|(4)|(7)|(8): D(16.0/18.0)
					* LargestSpotSize!=(S)|(R)|(X)
				* Activity=(2): E(8.0/5.0)
				* Activity!=(2): D(26.0/33.0)
		* SpotDistribution!=(C)|(I)|(O): H(298.0/0.0)


