# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = X | H | 0.311390 |
| SpotDistribution != X and LargestSpotSize = X | B | 0.134031 |
| SpotDistribution = O and LargestSpotSize!=(X) and SpotDistribution != I and LargestSpotSize != X | D | 0.056702 |
| LargestSpotSize = R and SpotDistribution = O and X-class = 0 | C | 0.066017 |
| SpotDistribution = O and LargestSpotSize!=(X) and SpotDistribution != I and LargestSpotSize = S | C | 0.052763 |
| LargestSpotSize = A and SpotDistribution = I and X-class = 0 | D | 0.042328 |
| LargestSpotSize = S and SpotDistribution = I and X-class = 0 | D | 0.013804 |
| LargestSpotSize = K and SpotDistribution = C and X-class = 0 | E | 0.007602 |
| LargestSpotSize = R and SpotDistribution = I and X-class = 0 | D | 0.013061 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution = O and LargestSpotSize != H and LargestSpotSize = A and C-class != 0 and Evolution = 2 | E | 0.004571 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution != O and LargestSpotSize != R and HistComplex != 1 and Evolution != 2 and SpotDistribution = I and LargestSpotSize = K | D | 0.010667 |
| SpotDistribution != X and LargestSpotSize != X and Area != 1 and Prev24Hour = 1 and Activity != 1 | F | 0.004343 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution = O and LargestSpotSize != H and LargestSpotSize = A and C-class = 0 and Activity = 1 and Evolution = 2 and HistComplex != 1 | C | 0.004681 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution != O and LargestSpotSize != R and HistComplex != 1 and Evolution != 2 and SpotDistribution = I and LargestSpotSize != K and LargestSpotSize != S and Activity != 1 and C-class != 0 | E | 0.002062 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution != O and LargestSpotSize != R and HistComplex != 1 and Evolution = 2 and C-class = 0 and Activity = 1 and LargestSpotSize != A | E | 0.002062 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution != O and LargestSpotSize != R and HistComplex != 1 and Evolution = 2 and C-class != 0 and C-class != 3 and LargestSpotSize != K and C-class != 1 | F | 0.002899 |
| LargestSpotSize = A and SpotDistribution = C and X-class = 0 | E | 0.002867 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution != O and LargestSpotSize != R and HistComplex != 1 and Evolution = 2 and C-class != 0 and C-class = 3 | E | 0.002062 |
| SpotDistribution != X and LargestSpotSize != X and Area != 1 and Prev24Hour = 1 and Activity = 1 | E | 0.002618 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution != O and LargestSpotSize != R and HistComplex != 1 and Evolution = 2 and C-class != 0 and C-class != 3 and LargestSpotSize = K | F | 0.001634 |
| LargestSpotSize = K and SpotDistribution = I and X-class = 0 | D | 0.008426 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution != O and LargestSpotSize != R and HistComplex != 1 and Evolution = 2 and C-class = 0 and Activity != 1 and LargestSpotSize = A | E | 0.001674 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution != O and LargestSpotSize != R and HistComplex != 1 and Evolution != 2 and SpotDistribution != I | E | 0.003657 |
| SpotDistribution != X and LargestSpotSize != X and Area != 1 and Prev24Hour != 1 | E | 0.005864 |
| LargestSpotSize = R and SpotDistribution = C and X-class = 0 | D | 0.000674 |
| LargestSpotSize = H and SpotDistribution = I and X-class = 0 | D | 0.000450 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution != O and LargestSpotSize != R and HistComplex = 1 and LargestSpotSize = A and C-class != 0 | D | 0.003076 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution != O and LargestSpotSize != R and HistComplex != 1 and Evolution = 2 and C-class = 0 and Activity = 1 and LargestSpotSize = A | D | 0.004805 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = X | H | 0.311390 |
| LargestSpotSize = X | B | 0.194825 |
| Area != 1 and Prev24Hour != 1 | E | 0.011403 |
| Area != 1 and LargestSpotSize = K and C-class = 0 | F | 0.005464 |
| SpotDistribution = O and LargestSpotSize != H and LargestSpotSize != A and HistComplex = 1 | C | 0.208711 |
| Area != 1 and LargestSpotSize = K | E | 0.012384 |
| SpotDistribution != C and SpotDistribution = O and LargestSpotSize != H and C-class = 0 and Activity = 1 and Evolution != 1 | C | 0.041917 |
| SpotDistribution != C and LargestSpotSize = R and SpotDistribution != O | D | 0.066099 |
| SpotDistribution != C and HistComplex = 1 and LargestSpotSize != H and LargestSpotSize = A and C-class = 0 | D | 0.142136 |
| SpotDistribution != C and HistComplex != 1 and LargestSpotSize != R and SpotDistribution != O | D | 0.212515 |
| SpotDistribution = C | E | 0.026037 |
| LargestSpotSize = A and Evolution != 2 and C-class != 1 | E | 0.042397 |
| Evolution = 3 and LargestSpotSize != A and Activity = 1 and C-class = 0 | D | 0.231906 |
| LargestSpotSize != H and LargestSpotSize = A and Evolution = 2 | E | 0.067340 |
|  | D | 0.415663 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

largestspotsize|spotdistribution|x-class|class
---|---|---|---
k|c|1|h
a|i|1|h
h|c|0|h
a|c|0|e
r|c|0|d
k|c|0|e
h|i|0|d
x|i|0|b
k|i|0|d
a|i|0|d
s|i|0|d
r|i|0|d
h|o|0|d
x|o|0|b
a|o|0|d
r|o|0|c
s|o|0|c
k|x|0|h
h|x|0|h
r|x|0|h
a|x|0|h
s|x|0|h

## PART

Decision list:

rules | predicted class
---|---
SpotDistribution = X|H (298.0)
LargestSpotSize = X|B (128.0)
Area != 1 AND Prev24Hour != 1|E (7.0/1.0)
Area != 1 AND LargestSpotSize = K AND C-class = 0|F (6.0/2.0)
SpotDistribution = O AND LargestSpotSize != H AND LargestSpotSize != A AND HistComplex = 1|C (181.0/59.0)
Area != 1 AND LargestSpotSize = K|E (6.0/2.0)
SpotDistribution != C AND SpotDistribution = O AND LargestSpotSize != H AND C-class = 0 AND Activity = 1 AND Evolution != 1|C (72.0/35.0)
SpotDistribution != C AND LargestSpotSize = R AND SpotDistribution != O|D (23.0/8.0)
SpotDistribution != C AND HistComplex = 1 AND LargestSpotSize != H AND LargestSpotSize = A AND C-class = 0|D (21.0/2.0)
SpotDistribution != C AND HistComplex != 1 AND LargestSpotSize != R AND SpotDistribution != O|D (119.0/59.0)
SpotDistribution = C|E (16.0/7.0)
LargestSpotSize = A AND Evolution != 2 AND C-class != 1|E (6.0/2.0)
Evolution = 3 AND LargestSpotSize != A AND Activity = 1 AND C-class = 0|D (18.0/7.0)
LargestSpotSize != H AND LargestSpotSize = A AND Evolution = 2|E (13.0/4.0)
|D (43.0/20.0)


## J48 Decision Tree

* SpotDistribution = X: H (298.0)
* SpotDistribution != X
	* LargestSpotSize = X: B (128.0)
	* LargestSpotSize != X
		* Area = 1
			* SpotDistribution = O
				* LargestSpotSize = H
					* Evolution = 2: D (6.0/4.0)
					* Evolution != 2: D (9.0/4.0)
				* LargestSpotSize != H
					* LargestSpotSize = A
						* C-class = 0
							* Activity = 1
								* Evolution = 2
									* HistComplex = 1: D (5.0/2.0)
									* HistComplex != 1: C (10.0/4.0)
								* Evolution != 2
									* HistComplex = 1: D (9.0/5.0)
									* HistComplex != 1: D (13.0/6.0)
							* Activity != 1: D (7.0/4.0)
						* C-class != 0
							* Evolution = 2: E (9.0/3.0)
							* Evolution != 2: D (5.0/2.0)
					* LargestSpotSize != A
						* C-class = 1
							* Activity = 1
								* HistComplex = 1
									* LargestSpotSize = R: D (6.0/2.0)
									* LargestSpotSize != R: C (7.0/3.0)
								* HistComplex != 1: C (5.0/2.0)
							* Activity != 1: D (5.0/2.0)
						* C-class != 1
							* Activity = 1
								* LargestSpotSize = R
									* Evolution = 1: C (7.0/1.0)
									* Evolution != 1
										* Evolution = 2
											* HistComplex = 1: C (31.0/7.0)
											* HistComplex != 1: C (8.0/2.0)
										* Evolution != 2: C (60.0/22.0)
								* LargestSpotSize != R
									* Evolution = 1: D (6.0/2.0)
									* Evolution != 1
										* C-class = 0
											* HistComplex = 1
												* Evolution = 2: C (17.0/4.0)
												* Evolution != 2: C (33.0/12.0)
											* HistComplex != 1
												* Evolution = 2: C (17.0/8.0)
												* Evolution != 2: C (8.0/3.0)
										* C-class != 0: D (8.0/4.0)
							* Activity != 1
								* HistComplex = 1
									* Evolution = 2: C (10.0/2.0)
									* Evolution != 2: C (5.0/1.0)
								* HistComplex != 1: D (8.0/5.0)
			* SpotDistribution != O
				* LargestSpotSize = R
					* C-class = 0
						* Evolution = 2: D (5.0)
						* Evolution != 2
							* HistComplex = 1: D (5.0/2.0)
							* HistComplex != 1: D (6.0/2.0)
					* C-class != 0: D (9.0/5.0)
				* LargestSpotSize != R
					* HistComplex = 1
						* LargestSpotSize = A
							* C-class = 0: D (18.0/2.0)
							* C-class != 0: D (7.0/3.0)
						* LargestSpotSize != A: D (16.0/6.0)
					* HistComplex != 1
						* Evolution = 2
							* C-class = 0
								* Activity = 1
									* LargestSpotSize = A: D (18.0/10.0)
									* LargestSpotSize != A: E (5.0/2.0)
								* Activity != 1
									* LargestSpotSize = A: E (11.0/7.0)
									* LargestSpotSize != A: D (8.0/5.0)
							* C-class != 0
								* C-class = 3: E (5.0/2.0)
								* C-class != 3
									* LargestSpotSize = K: F (6.0/3.0)
									* LargestSpotSize != K
										* C-class = 1: D (9.0/4.0)
										* C-class != 1: F (6.0/2.0)
						* Evolution != 2
							* SpotDistribution = I
								* LargestSpotSize = K: D (8.0)
								* LargestSpotSize != K
									* LargestSpotSize = S: D (11.0/5.0)
									* LargestSpotSize != S
										* Activity = 1
											* C-class = 0: D (14.0/4.0)
											* C-class != 0: D (10.0/4.0)
										* Activity != 1
											* C-class = 0: D (7.0/3.0)
											* C-class != 0: E (5.0/2.0)
							* SpotDistribution != I: E (5.0/1.0)
		* Area != 1
			* Prev24Hour = 1
				* Activity = 1: E (7.0/3.0)
				* Activity != 1: F (9.0/3.0)
			* Prev24Hour != 1: E (7.0/1.0)


## SimpleCart Decision Tree

		* SpotDistribution=(C)|(I)|(O)
	* LargestSpotSize=(X): B(128.0/0.0)
	* LargestSpotSize!=(X)
			* SpotDistribution=(C)|(I)
			* Area=(2): E(12.0/10.0)
			* Area!=(2): D(108.0/86.0)
			* SpotDistribution!=(C)|(I)
						* LargestSpotSize=(S)|(R)|(X)|(K): C(151.0/91.0)
						* LargestSpotSize!=(S)|(R)|(X)|(K): D(31.0/42.0)
		* SpotDistribution!=(C)|(I)|(O): H(298.0/0.0)


