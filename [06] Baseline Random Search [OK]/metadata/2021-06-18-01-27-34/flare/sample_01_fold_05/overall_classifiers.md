# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = X | H | 0.311390 |
| SpotDistribution != X and LargestSpotSize = X | B | 0.134031 |
| SpotDistribution = O and LargestSpotSize!=(X) and SpotDistribution != I and LargestSpotSize != X and Activity!=(2) | D | 0.055304 |
| LargestSpotSize = R and SpotDistribution = O and Area = 1 | C | 0.059301 |
| LargestSpotSize = S and SpotDistribution = O and Area = 1 | C | 0.055336 |
| LargestSpotSize = A and SpotDistribution = I and Area = 1 | D | 0.043897 |
| LargestSpotSize = R and SpotDistribution = I and Area = 1 | D | 0.015429 |
| LargestSpotSize = K and SpotDistribution = C and Area = 2 | E | 0.007143 |
| LargestSpotSize = K and SpotDistribution = I and Area = 1 | D | 0.011309 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution = O and LargestSpotSize != H and LargestSpotSize = A and C-class != 0 and Evolution != 3 | E | 0.005600 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution = O and LargestSpotSize != H and LargestSpotSize = A and C-class = 0 and Activity = 1 and Evolution = 2 | C | 0.006394 |
| LargestSpotSize = S and SpotDistribution = I and Area = 1 | D | 0.010055 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution != O and HistComplex != 1 and LargestSpotSize != R and SpotDistribution = I and M-class != 1 and LargestSpotSize != K and C-class != 2 and C-class != 1 and C-class != 0 | E | 0.003753 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution != O and HistComplex = 1 and LargestSpotSize != A and Activity = 1 and LargestSpotSize != R | C | 0.004563 |
| SpotDistribution != X and LargestSpotSize != X and Area != 1 and Prev24Hour = 1 | F | 0.005179 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution != O and HistComplex != 1 and LargestSpotSize != R and SpotDistribution != I | E | 0.004124 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution != O and HistComplex != 1 and LargestSpotSize != R and SpotDistribution = I and M-class != 1 and LargestSpotSize != K and C-class != 2 and C-class != 1 and C-class = 0 and Activity != 1 and LargestSpotSize = S | E | 0.002621 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution != O and HistComplex != 1 and LargestSpotSize != R and SpotDistribution = I and M-class != 1 and LargestSpotSize != K and C-class != 2 and C-class != 1 and C-class = 0 and Activity = 1 and Evolution = 2 and LargestSpotSize != A | E | 0.002064 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution != O and HistComplex != 1 and LargestSpotSize != R and SpotDistribution = I and M-class != 1 and LargestSpotSize != K and C-class = 2 | F | 0.002176 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution = O and LargestSpotSize != H and LargestSpotSize = A and C-class = 0 and Activity = 1 and Evolution != 2 and HistComplex = 1 | C | 0.002608 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution != O and HistComplex != 1 and LargestSpotSize != R and SpotDistribution = I and M-class != 1 and LargestSpotSize != K and C-class != 2 and C-class != 1 and C-class = 0 and Activity != 1 and LargestSpotSize != S and Evolution = 2 | F | 0.001937 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution = O and LargestSpotSize = H and Evolution = 2 | E | 0.001478 |
| LargestSpotSize = R and SpotDistribution = C and Area = 1 | D | 0.001795 |
| LargestSpotSize = H and SpotDistribution = I and Area = 1 | E | 0.001529 |
| LargestSpotSize = A and SpotDistribution = C and Area = 1 | E | 0.003186 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution != O and HistComplex = 1 and LargestSpotSize = A | D | 0.022913 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution = O and LargestSpotSize != H and LargestSpotSize != A and C-class != 1 and C-class != 0 | C | 0.002967 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution != O and HistComplex != 1 and LargestSpotSize != R and SpotDistribution = I and M-class != 1 and LargestSpotSize != K and C-class != 2 and C-class != 1 and C-class = 0 and Activity != 1 and LargestSpotSize != S and Evolution != 2 | D | 0.002022 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution = O | C | 0.115890 |
| LargestSpotSize != X and SpotDistribution = X | H | 0.378173 |
| LargestSpotSize != X and Area = 1 | D | 0.371293 |
| LargestSpotSize = X | B | 0.467153 |
|  | E | 0.581081 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = I and Evolution = 2 | F | 0.004428 |
| Area = 2 | F | 0.002445 |
| LargestSpotSize = A and HistComplex = 2 and Activity = 2 and Prev24Hour = 1 | E | 0.007151 |
| HistComplex = 2 and LargestSpotSize = A and SpotDistribution = I and M-class = 0 | E | 0.004585 |
| HistComplex = 2 and Activity = 2 | E | 0.008430 |
| LargestSpotSize = A and SpotDistribution = O | E | 0.001918 |
| LargestSpotSize = X | B | 0.146958 |
| SpotDistribution = O and HistComplex = 1 and C-class = 0 and Evolution = 2 and Activity = 2 | C | 0.013103 |
| SpotDistribution = O and HistComplex = 1 and C-class = 0 and Evolution = 2 and LargestSpotSize = S | C | 0.018166 |
| SpotDistribution = O and LargestSpotSize = R and Evolution = 2 and HistComplex = 2 | C | 0.011408 |
| SpotDistribution = O and HistComplex = 1 and C-class = 0 and LargestSpotSize = R and Evolution = 2 | C | 0.021313 |
| SpotDistribution = O and HistComplex = 1 and C-class = 0 | C | 0.070928 |
| SpotDistribution = O and Evolution = 2 and LargestSpotSize = S and C-class = 0 | C | 0.008148 |
| SpotDistribution = O and HistComplex = 1 | C | 0.004009 |
| SpotDistribution = O and LargestSpotSize = S | C | 0.003100 |
| SpotDistribution = I and LargestSpotSize = A | D | 0.115839 |
| SpotDistribution = I and C-class = 0 and HistComplex = 2 | D | 0.032984 |
| SpotDistribution = I and LargestSpotSize = R | D | 0.012000 |
| SpotDistribution = I | D | 0.016298 |
| SpotDistribution = O | D | 0.179630 |
|  | H | 0.782152 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

largestspotsize|spotdistribution|area|class
---|---|---|---
k|c|2|e
a|i|2|f
k|i|2|f
h|c|1|h
r|o|2|h
r|c|1|d
k|c|1|e
a|c|1|e
h|i|1|e
k|i|1|d
s|i|1|d
r|i|1|d
a|i|1|d
x|i|1|b
h|o|1|d
k|o|1|h
a|o|1|d
s|o|1|c
r|o|1|c
x|o|1|b
h|x|1|h
r|x|1|h
s|x|1|h
a|x|1|h

## JRip

Decision list:

rules | predicted class
---|---
(SpotDistribution = I) and (Evolution = 2)|F (84.0/66.0)
(Area = 2)|F (22.0/15.0)
(LargestSpotSize = A) and (HistComplex = 2) and (Activity = 2) and (Prev24Hour = 1)|E (19.0/8.0)
(HistComplex = 2) and (LargestSpotSize = A) and (SpotDistribution = I) and (M-class = 0)|E (20.0/12.0)
(HistComplex = 2) and (Activity = 2)|E (36.0/27.0)
(LargestSpotSize = A) and (SpotDistribution = O)|E (49.0/40.0)
(LargestSpotSize = X)|B (119.0/0.0)
(SpotDistribution = O) and (HistComplex = 1) and (C-class = 0) and (Evolution = 2) and (Activity = 2)|C (11.0/2.0)
(SpotDistribution = O) and (HistComplex = 1) and (C-class = 0) and (Evolution = 2) and (LargestSpotSize = S)|C (20.0/5.0)
(SpotDistribution = O) and (LargestSpotSize = R) and (Evolution = 2) and (HistComplex = 2)|C (10.0/2.0)
(SpotDistribution = O) and (HistComplex = 1) and (C-class = 0) and (LargestSpotSize = R) and (Evolution = 2)|C (24.0/7.0)
(SpotDistribution = O) and (HistComplex = 1) and (C-class = 0)|C (101.0/35.0)
(SpotDistribution = O) and (Evolution = 2) and (LargestSpotSize = S) and (C-class = 0)|C (19.0/8.0)
(SpotDistribution = O) and (HistComplex = 1)|C (26.0/14.0)
(SpotDistribution = O) and (LargestSpotSize = S)|C (21.0/13.0)
(SpotDistribution = I) and (LargestSpotSize = A)|D (21.0/2.0)
(SpotDistribution = I) and (C-class = 0) and (HistComplex = 2)|D (10.0/2.0)
(SpotDistribution = I) and (LargestSpotSize = R)|D (11.0/4.0)
(SpotDistribution = I)|D (23.0/12.0)
(SpotDistribution = O)|D (11.0/4.0)
|H (300.0/7.0)


## PART

Decision list:

rules | predicted class
---|---
SpotDistribution != X AND LargestSpotSize != X AND Area = 1 AND SpotDistribution = O|C (205.0/92.0)
LargestSpotSize != X AND SpotDistribution = X|H (199.0)
LargestSpotSize != X AND Area = 1|D (128.0/58.0)
LargestSpotSize = X|B (85.0)
|E (21.0/9.0)


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
							* Evolution = 3: D (5.0/1.0)
							* Evolution != 3: E (10.0/3.0)
					* LargestSpotSize != A
						* C-class = 1
							* Activity = 1
								* HistComplex = 1: D (14.0/5.0)
								* HistComplex != 1: C (5.0/2.0)
							* Activity != 1: C (5.0/2.0)
						* C-class != 1
							* C-class = 0
								* LargestSpotSize = R: C (99.0/32.0)
								* LargestSpotSize != R
									* Evolution = 1: D (10.0/6.0)
									* Evolution != 1: C (95.0/33.0)
							* C-class != 0: C (11.0/6.0)
			* SpotDistribution != O
				* HistComplex = 1
					* LargestSpotSize = A: D (23.0/3.0)
					* LargestSpotSize != A
						* Activity = 1
							* LargestSpotSize = R: D (13.0/6.0)
							* LargestSpotSize != R: C (14.0/7.0)
						* Activity != 1: D (5.0/1.0)
				* HistComplex != 1
					* LargestSpotSize = R: D (15.0/4.0)
					* LargestSpotSize != R
						* SpotDistribution = I
							* M-class = 1: D (8.0/2.0)
							* M-class != 1
								* LargestSpotSize = K: D (16.0/5.0)
								* LargestSpotSize != K
									* C-class = 2: F (8.0/4.0)
									* C-class != 2
										* C-class = 1: D (15.0/6.0)
										* C-class != 1
											* C-class = 0
												* Activity = 1
													* Evolution = 2
														* LargestSpotSize = A: D (16.0/8.0)
														* LargestSpotSize != A: E (5.0/2.0)
													* Evolution != 2: D (15.0/7.0)
												* Activity != 1
													* LargestSpotSize = S: E (7.0/3.0)
													* LargestSpotSize != S
														* Evolution = 2: F (9.0/5.0)
														* Evolution != 2: D (6.0/3.0)
											* C-class != 0: E (11.0/5.0)
						* SpotDistribution != I: E (10.0/4.0)
		* Area != 1
			* Prev24Hour = 1: F (17.0/8.0)
			* Prev24Hour != 1: E (8.0/1.0)


## SimpleCart Decision Tree

		* SpotDistribution=(C)|(I)|(O)
	* LargestSpotSize=(X): B(128.0/0.0)
	* LargestSpotSize!=(X)
			* SpotDistribution=(C)|(I)
			* Area=(2): E(13.0/11.0)
			* Area!=(2)
				* HistComplex=(2)
					* Evolution=(3)
						* LargestSpotSize=(S): D(4.0/6.0)
						* LargestSpotSize!=(S)
								* LargestSpotSize=(K)|(R): D(15.0/2.0)
								* LargestSpotSize!=(K)|(R): D(19.0/18.0)
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


