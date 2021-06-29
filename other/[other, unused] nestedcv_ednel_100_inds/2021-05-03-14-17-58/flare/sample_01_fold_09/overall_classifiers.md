# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = X | H | 0.311390 |
| SpotDistribution != X and LargestSpotSize = X | B | 0.134937 |
| SpotDistribution = O and LargestSpotSize!=(X) and SpotDistribution != I and LargestSpotSize != X and C-class != 1 and Activity!=(2) and LargestSpotSize!=(H) | D | 0.046793 |
| LargestSpotSize = R and SpotDistribution = O and Area = 1 and X-class = 0 | C | 0.063366 |
| LargestSpotSize = S and SpotDistribution = O and Area = 1 and X-class = 0 | C | 0.054980 |
| LargestSpotSize = A and SpotDistribution = I and Area = 1 and X-class = 0 | D | 0.043897 |
| LargestSpotSize = R and SpotDistribution = I and Area = 1 and X-class = 0 | D | 0.012533 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution != O and HistComplex != 1 and LargestSpotSize != R and Evolution = 3 and LargestSpotSize = K | D | 0.011984 |
| LargestSpotSize = S and SpotDistribution = I and Area = 1 and X-class = 0 | D | 0.010722 |
| SpotDistribution != X and LargestSpotSize != X and Area != 1 and Prev24Hour != 1 | E | 0.006976 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution = O and LargestSpotSize != H and LargestSpotSize = A and C-class != 0 and Evolution != 3 | E | 0.005594 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution != O and HistComplex != 1 and LargestSpotSize != R and Evolution = 3 and LargestSpotSize != K and LargestSpotSize != H and LargestSpotSize = A and Activity != 1 and C-class != 0 | E | 0.004082 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution != O and HistComplex = 1 and LargestSpotSize != A and Activity = 1 and LargestSpotSize = R | C | 0.003617 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution != O and HistComplex != 1 and LargestSpotSize != R and Evolution != 3 and C-class != 3 and C-class = 0 and Prev24Hour = 1 and SpotDistribution = I and LargestSpotSize = S | E | 0.002867 |
| SpotDistribution != X and LargestSpotSize != X and Area != 1 and Prev24Hour = 1 and Evolution = 2 | F | 0.004338 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution = O and LargestSpotSize != H and LargestSpotSize = A and C-class = 0 and Activity = 1 and Evolution = 2 and HistComplex != 1 | C | 0.004064 |
| LargestSpotSize = A and SpotDistribution = C and Area = 1 and X-class = 0 | E | 0.002867 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution != O and HistComplex != 1 and LargestSpotSize != R and Evolution != 3 and C-class != 3 and C-class != 0 and LargestSpotSize != K and C-class = 2 | F | 0.002446 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution != O and HistComplex != 1 and LargestSpotSize != R and Evolution != 3 and C-class = 3 | E | 0.002574 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution != O and HistComplex != 1 and LargestSpotSize != R and Evolution = 3 and LargestSpotSize != K and LargestSpotSize = H | E | 0.002574 |
| SpotDistribution != X and LargestSpotSize != X and Area != 1 and Prev24Hour = 1 and Evolution != 2 and SpotDistribution != C | E | 0.002574 |
| SpotDistribution != X and LargestSpotSize != X and Area != 1 and Prev24Hour = 1 and Evolution != 2 and SpotDistribution = C | F | 0.002487 |
| LargestSpotSize = K and SpotDistribution = C and Area = 2 and X-class = 0 | E | 0.005091 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution = O and LargestSpotSize != H and LargestSpotSize = A and C-class = 0 and Activity != 1 and Evolution = 2 | E | 0.001147 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution != O and HistComplex != 1 and LargestSpotSize != R and Evolution = 3 and LargestSpotSize != K and LargestSpotSize != H and LargestSpotSize != A and C-class != 0 | F | 0.001089 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution = O and LargestSpotSize != H and LargestSpotSize = A and C-class != 0 and Evolution = 3 | D | 0.003024 |
| LargestSpotSize = R and SpotDistribution = C and Area = 1 and X-class = 0 | D | 0.001795 |
| LargestSpotSize = K and SpotDistribution = I and Area = 1 and X-class = 0 | D | 0.011309 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution != O and HistComplex != 1 and LargestSpotSize != R and Evolution != 3 and C-class != 3 and C-class != 0 and LargestSpotSize = K | E | 0.000918 |
| LargestSpotSize = A and SpotDistribution = I and Area = 2 and X-class = 0 | F | 0.002174 |
| LargestSpotSize = H and SpotDistribution = I and Area = 1 and X-class = 0 | D | 0.000450 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution != O and HistComplex != 1 and LargestSpotSize != R and Evolution != 3 and C-class != 3 and C-class = 0 and Prev24Hour = 1 and SpotDistribution != I | E | 0.002574 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution != O and HistComplex != 1 and LargestSpotSize != R and Evolution = 3 and LargestSpotSize != K and LargestSpotSize != H and LargestSpotSize = A and Activity != 1 and C-class = 0 | D | 0.003024 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution = O and LargestSpotSize != H and LargestSpotSize != A and Evolution != 1 and Activity != 1 and HistComplex != 1 and Evolution != 2 | D | 0.003024 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution != O and HistComplex != 1 and LargestSpotSize != R and Evolution != 3 and C-class != 3 and C-class = 0 and Prev24Hour != 1 | D | 0.001348 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution = O and LargestSpotSize != H and LargestSpotSize != A and Evolution != 1 and Activity = 1 and LargestSpotSize != S | C | 0.059676 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution != O and HistComplex = 1 and LargestSpotSize = A | D | 0.023241 |
| SpotDistribution = O and LargestSpotSize!=(X) and SpotDistribution != I and LargestSpotSize != X and C-class = 1 | E | 0.000892 |
| LargestSpotSize = A and SpotDistribution = O and Area = 1 and X-class = 0 | D | 0.014013 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = X | H | 0.311390 |
| LargestSpotSize = R | C | 0.100443 |
| LargestSpotSize = X | B | 0.224348 |
| SpotDistribution = O and LargestSpotSize = S and C-class = 0 and Evolution = 2 | C | 0.064581 |
| Area = 2 and Activity = 2 and Prev24Hour = 1 | F | 0.008311 |
| SpotDistribution = I | D | 0.267483 |
| Area = 1 and SpotDistribution = O and LargestSpotSize = S and C-class = 0 and Evolution = 3 | C | 0.068182 |
| Area = 1 and SpotDistribution = O and Activity = 1 and LargestSpotSize = A and C-class = 0 and Evolution = 3 | D | 0.027108 |
| Area = 1 and SpotDistribution = O and LargestSpotSize = A and C-class = 0 | D | 0.019806 |
| Area = 2 | E | 0.044199 |
| LargestSpotSize = A and C-class = 1 | E | 0.017702 |
| SpotDistribution = O | D | 0.294468 |
|  | E | 0.428571 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| HistComplex = 2 and Activity = 2 | E | 0.015375 |
| LargestSpotSize = X | B | 0.140370 |
| SpotDistribution = O and HistComplex = 1 | C | 0.121709 |
| SpotDistribution = O and LargestSpotSize = R | C | 0.004559 |
| SpotDistribution = I | D | 0.128630 |
|  | H | 0.538879 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

largestspotsize|spotdistribution|area|x-class|class
---|---|---|---|---
k|c|2|2|h
k|c|2|1|e
a|i|1|1|h
a|c|2|0|h
k|c|2|0|e
k|i|2|0|f
a|i|2|0|f
r|o|2|0|h
k|c|1|0|h
r|c|1|0|d
h|c|1|0|h
a|c|1|0|e
h|i|1|0|d
k|i|1|0|d
x|i|1|0|b
s|i|1|0|d
a|i|1|0|d
r|i|1|0|d
k|o|1|0|h
a|o|1|0|d
r|o|1|0|c
s|o|1|0|c
x|o|1|0|b
h|o|1|0|d
h|x|1|0|h
k|x|1|0|h
a|x|1|0|h
r|x|1|0|h
s|x|1|0|h

## JRip

Decision list:

rules | predicted class
---|---
(HistComplex = 2) and (Activity = 2)|E (106.0/69.0)
(LargestSpotSize = X)|B (125.0/0.0)
(SpotDistribution = O) and (HistComplex = 1)|C (196.0/71.0)
(SpotDistribution = O) and (LargestSpotSize = R)|C (17.0/6.0)
(SpotDistribution = I)|D (131.0/54.0)
|H (382.0/90.0)


## PART

Decision list:

rules | predicted class
---|---
SpotDistribution = X|H (256.0)
LargestSpotSize = R|C (119.0/48.0)
LargestSpotSize = X|B (110.0)
SpotDistribution = O AND LargestSpotSize = S AND C-class = 0 AND Evolution = 2|C (47.0/15.0)
Area = 2 AND Activity = 2 AND Prev24Hour = 1|F (7.0/3.0)
SpotDistribution = I|D (134.0/60.0)
Area = 1 AND SpotDistribution = O AND LargestSpotSize = S AND C-class = 0 AND Evolution = 3|C (41.0/17.0)
Area = 1 AND SpotDistribution = O AND Activity = 1 AND LargestSpotSize = A AND C-class = 0 AND Evolution = 3|D (15.0/8.0)
Area = 1 AND SpotDistribution = O AND LargestSpotSize = A AND C-class = 0|D (19.0/12.0)
Area = 2|E (10.0/3.0)
LargestSpotSize = A AND C-class = 1|E (7.0/4.0)
SpotDistribution = O|D (48.0/27.0)
|E (8.0/3.0)


## J48 Decision Tree

* SpotDistribution = X: H (298.0)
* SpotDistribution != X
	* LargestSpotSize = X: B (129.0)
	* LargestSpotSize != X
		* Area = 1
			* SpotDistribution = O
				* LargestSpotSize = H: D (15.0/8.0)
				* LargestSpotSize != H
					* LargestSpotSize = A
						* C-class = 0
							* Activity = 1
								* Evolution = 2
									* HistComplex = 1: D (5.0/2.0)
									* HistComplex != 1: C (8.0/3.0)
								* Evolution != 2: D (21.0/10.0)
							* Activity != 1
								* Evolution = 2: E (4.0/2.0)
								* Evolution != 2: D (4.0/1.0)
						* C-class != 0
							* Evolution = 3: D (4.0/1.0)
							* Evolution != 3: E (10.0/3.0)
					* LargestSpotSize != A
						* Evolution = 1
							* LargestSpotSize = R: C (6.0/2.0)
							* LargestSpotSize != R: D (10.0/6.0)
						* Evolution != 1
							* Activity = 1
								* LargestSpotSize = S
									* C-class = 2: D (4.0/2.0)
									* C-class != 2: C (94.0/37.0)
								* LargestSpotSize != S: C (102.0/32.0)
							* Activity != 1
								* HistComplex = 1: C (15.0/2.0)
								* HistComplex != 1
									* Evolution = 2: C (6.0/3.0)
									* Evolution != 2: D (4.0/1.0)
			* SpotDistribution != O
				* HistComplex = 1
					* LargestSpotSize = A: D (25.0/4.0)
					* LargestSpotSize != A
						* Activity = 1
							* LargestSpotSize = R: C (9.0/4.0)
							* LargestSpotSize != R: D (16.0/8.0)
						* Activity != 1: D (5.0/1.0)
				* HistComplex != 1
					* LargestSpotSize = R: D (15.0/4.0)
					* LargestSpotSize != R
						* Evolution = 3
							* LargestSpotSize = K: D (9.0)
							* LargestSpotSize != K
								* LargestSpotSize = H: E (4.0/1.0)
								* LargestSpotSize != H
									* LargestSpotSize = A
										* Activity = 1: D (20.0/6.0)
										* Activity != 1
											* C-class = 0: D (4.0/1.0)
											* C-class != 0: E (7.0/2.0)
									* LargestSpotSize != A
										* C-class = 0: D (7.0/3.0)
										* C-class != 0: F (4.0/2.0)
						* Evolution != 3
							* C-class = 3: E (4.0/1.0)
							* C-class != 3
								* C-class = 0
									* Prev24Hour = 1
										* SpotDistribution = I
											* LargestSpotSize = S: E (10.0/5.0)
											* LargestSpotSize != S: D (25.0/14.0)
										* SpotDistribution != I: E (4.0/1.0)
									* Prev24Hour != 1: D (4.0/2.0)
								* C-class != 0
									* LargestSpotSize = K: E (5.0/3.0)
									* LargestSpotSize != K
										* C-class = 2: F (4.0/1.0)
										* C-class != 2: D (14.0/7.0)
		* Area != 1
			* Prev24Hour = 1
				* Evolution = 2: F (4.0)
				* Evolution != 2
					* SpotDistribution = C: F (7.0/3.0)
					* SpotDistribution != C: E (4.0/1.0)
			* Prev24Hour != 1: E (8.0/1.0)


## SimpleCart Decision Tree

		* SpotDistribution=(C)|(I)|(O)
	* LargestSpotSize=(X): B(129.0/0.0)
	* LargestSpotSize!=(X)
			* SpotDistribution=(C)|(I)
			* Area=(2)
					* Prev24Hour=(3)|(2): E(7.0/1.0)
					* Prev24Hour!=(3)|(2): F(9.0/5.0)
			* Area!=(2)
				* Evolution=(3): D(73.0/36.0)
				* Evolution!=(3)
							* C-class=(8)|(5)|(3): E(5.0/1.0)
							* C-class!=(8)|(5)|(3)
								* C-class=(4)|(2)|(1): F(11.0/14.0)
								* C-class!=(4)|(2)|(1)
							* HistComplex=(2)
								* LargestSpotSize=(R): D(4.0/1.0)
								* LargestSpotSize!=(R): D(17.0/26.0)
							* HistComplex!=(2): D(5.0/2.0)
			* SpotDistribution!=(C)|(I)
						* LargestSpotSize=(K)|(S)|(R)|(X)
				* HistComplex=(2): C(34.0/35.0)
				* HistComplex!=(2)
							* C-class=(6)|(2)|(1): D(9.0/10.0)
							* C-class!=(6)|(2)|(1)
						* Activity=(2): C(13.0/2.0)
						* Activity!=(2)
							* Evolution=(2)
								* LargestSpotSize=(S): C(15.0/6.0)
								* LargestSpotSize!=(S): C(23.0/7.0)
							* Evolution!=(2): C(58.0/30.0)
						* LargestSpotSize!=(K)|(S)|(R)|(X)
						* C-class=(4)|(3)|(1): E(8.0/6.0)
						* C-class!=(4)|(3)|(1)
					* Activity=(2): D(5.0/5.0)
					* Activity!=(2)
						* LargestSpotSize=(H): D(7.0/4.0)
						* LargestSpotSize!=(H): D(16.0/20.0)
		* SpotDistribution!=(C)|(I)|(O): H(298.0/0.0)


