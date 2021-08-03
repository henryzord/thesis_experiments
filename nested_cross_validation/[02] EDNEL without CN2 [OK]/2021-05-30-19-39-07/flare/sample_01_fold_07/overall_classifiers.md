# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = X | H | 0.311390 |
| SpotDistribution = O and LargestSpotSize = X | B | 0.123012 |
| SpotDistribution = O and LargestSpotSize!=(X) and SpotDistribution != I and LargestSpotSize != X and C-class != 1 and Activity!=(2) | D | 0.045151 |
| LargestSpotSize = R and SpotDistribution = O and HistComplex = 1 and Area = 1 | C | 0.060200 |
| SpotDistribution = O and LargestSpotSize = S and C-class = 0 | C | 0.046196 |
| SpotDistribution = I and LargestSpotSize = A | D | 0.041680 |
| SpotDistribution = I and LargestSpotSize = R | D | 0.016571 |
| SpotDistribution = C | E | 0.010997 |
| SpotDistribution = I and LargestSpotSize = X | B | 0.014303 |
| LargestSpotSize = K and SpotDistribution = I and HistComplex = 2 and Area = 1 | D | 0.012783 |
| LargestSpotSize = R and SpotDistribution = O and HistComplex = 2 and Area = 1 | C | 0.008106 |
| LargestSpotSize = A and SpotDistribution = O and HistComplex = 2 and Area = 1 | E | 0.005595 |
| SpotDistribution = I and LargestSpotSize = S | D | 0.009817 |
| SpotDistribution = O and LargestSpotSize = A and C-class = 0 and Activity = 1 and Evolution = 2 | C | 0.004908 |
| LargestSpotSize = S and SpotDistribution = I and HistComplex = 2 and Area = 1 | E | 0.003897 |
| SpotDistribution = O and LargestSpotSize = R and HistComplex = 1 and C-class = 1 | D | 0.003584 |
| SpotDistribution = O and LargestSpotSize = A and C-class = 1 | D | 0.002399 |
| LargestSpotSize = S and SpotDistribution = O and HistComplex = 1 and Area = 1 | C | 0.042840 |
| SpotDistribution = O and LargestSpotSize = S and C-class = 1 and HistComplex = 1 and Evolution = 3 | D | 0.002423 |
| LargestSpotSize = A and SpotDistribution = I and HistComplex = 2 and Area = 2 | F | 0.002174 |
| SpotDistribution = O and LargestSpotSize = S and C-class = 1 and HistComplex = 2 | D | 0.003076 |
| LargestSpotSize = A and SpotDistribution = C and HistComplex = 2 and Area = 1 | D | 0.001735 |
| LargestSpotSize = K and SpotDistribution = I and HistComplex = 2 and Area = 2 | F | 0.001634 |
| LargestSpotSize = H and SpotDistribution = I and HistComplex = 2 and Area = 1 | E | 0.001527 |
| LargestSpotSize = H and SpotDistribution = O and HistComplex = 1 and Area = 1 | C | 0.001736 |
| SpotDistribution = O and LargestSpotSize = S and C-class = 6 | E | 0.001145 |
| SpotDistribution = O and LargestSpotSize = S and C-class = 5 | E | 0.001145 |
| SpotDistribution = O and LargestSpotSize = K | C | 0.001302 |
| LargestSpotSize = R and SpotDistribution = C and HistComplex = 1 and Area = 1 | D | 0.000674 |
| SpotDistribution = O and LargestSpotSize!=(X) and SpotDistribution != I and LargestSpotSize != X and C-class = 1 and Evolution!=(3) | E | 0.001179 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = X | H | 0.311390 |
| LargestSpotSize = X | B | 0.194825 |
| SpotDistribution = O and LargestSpotSize = S | C | 0.114268 |
| HistComplex = 1 and SpotDistribution = O and LargestSpotSize = R | C | 0.127511 |
| Area = 1 and SpotDistribution = I and HistComplex = 1 | D | 0.126699 |
| Area = 1 and SpotDistribution = I and LargestSpotSize = A and Evolution = 3 | D | 0.058273 |
| M-class = 0 and Area = 1 and SpotDistribution = O and Activity = 1 and LargestSpotSize = A | D | 0.050560 |
| M-class = 0 and Area = 1 and Activity = 2 | D | 0.088644 |
| M-class = 0 and Area = 1 and SpotDistribution = O and LargestSpotSize = R | C | 0.011074 |
| M-class = 0 and Area = 1 | D | 0.327224 |
|  | E | 0.494186 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| HistComplex = 2 and Area = 2 and Prev24Hour = 1 | F | 0.005503 |
| Activity = 2 and SpotDistribution = C | E | 0.009724 |
| LargestSpotSize = X | B | 0.137192 |
| SpotDistribution = O and HistComplex = 1 | C | 0.125732 |
| SpotDistribution = O and LargestSpotSize = R and Evolution = 2 | C | 0.006585 |
| SpotDistribution = I | D | 0.123137 |
| SpotDistribution = O and Evolution = 3 | D | 0.092420 |
|  | H | 0.593625 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

largestspotsize|spotdistribution|histcomplex|area|class
---|---|---|---|---
a|c|2|2|h
k|c|2|2|e
a|i|2|2|f
k|i|2|2|f
h|c|2|1|h
r|c|2|1|h
k|c|2|1|e
a|c|2|1|d
x|i|2|1|b
h|i|2|1|e
s|i|2|1|e
r|i|2|1|d
a|i|2|1|d
k|i|2|1|d
a|c|1|1|h
r|c|1|1|d
r|o|2|1|c
h|o|2|1|d
x|o|2|1|b
a|o|2|1|e
s|o|2|1|d
h|x|2|1|h
r|x|2|1|h
a|x|2|1|h
s|x|2|1|h
x|i|1|1|b
s|i|1|1|d
r|i|1|1|d
a|i|1|1|d
k|o|1|1|h
h|o|1|1|c
x|o|1|1|b
s|o|1|1|c
a|o|1|1|d
r|o|1|1|c
k|x|1|1|h
h|x|1|1|h
r|x|1|1|h
s|x|1|1|h
a|x|1|1|h

## JRip

Decision list:

rules | predicted class
---|---
(HistComplex = 2) and (Area = 2) and (Prev24Hour = 1)|F (16.0/7.0)
(Activity = 2) and (SpotDistribution = C)|E (17.0/6.0)
(LargestSpotSize = X)|B (128.0/0.0)
(SpotDistribution = O) and (HistComplex = 1)|C (205.0/73.0)
(SpotDistribution = O) and (LargestSpotSize = R) and (Evolution = 2)|C (12.0/3.0)
(SpotDistribution = I)|D (178.0/75.0)
(SpotDistribution = O) and (Evolution = 3)|D (33.0/14.0)
|H (368.0/70.0)


## PART

Decision list:

rules | predicted class
---|---
SpotDistribution = X|H (249.0)
LargestSpotSize = X|B (107.0)
SpotDistribution = O AND LargestSpotSize = S|C (106.0/46.0)
HistComplex = 1 AND SpotDistribution = O AND LargestSpotSize = R|C (83.0/27.0)
Area = 1 AND SpotDistribution = I AND HistComplex = 1|D (46.0/13.0)
Area = 1 AND SpotDistribution = I AND LargestSpotSize = A AND Evolution = 3|D (27.0/12.0)
M-class = 0 AND Area = 1 AND SpotDistribution = O AND Activity = 1 AND LargestSpotSize = A|D (37.0/20.0)
M-class = 0 AND Area = 1 AND Activity = 2|D (50.0/28.0)
M-class = 0 AND Area = 1 AND SpotDistribution = O AND LargestSpotSize = R|C (14.0/5.0)
M-class = 0 AND Area = 1|D (53.0/30.0)
|E (26.0/10.0)


## J48 Decision Tree

* SpotDistribution = X: H (256.0)
* SpotDistribution = O
	* LargestSpotSize = A
		* C-class = 0
			* Activity = 1
				* Evolution = 1: D (3.0/1.0)
				* Evolution = 2: C (10.0/5.0)
				* Evolution = 3: D (14.0/7.0)
			* Activity = 2: D (7.0/4.0)
		* C-class = 1: D (9.0/5.0)
		* C-class = 2: D (3.0/1.0)
		* C-class = 3: E (1.0)
		* C-class = 4: E (2.0)
		* C-class = 5: D (0.0)
		* C-class = 6: D (0.0)
		* C-class = 7: D (0.0)
		* C-class = 8: D (0.0)
	* LargestSpotSize = R
		* HistComplex = 1
			* C-class = 0: C (73.0/21.0)
			* C-class = 1: D (5.0/2.0)
			* C-class = 2: C (0.0)
			* C-class = 3: C (1.0)
			* C-class = 4: C (0.0)
			* C-class = 5: C (0.0)
			* C-class = 6: C (0.0)
			* C-class = 7: C (0.0)
			* C-class = 8: C (0.0)
		* HistComplex = 2: C (14.0/6.0)
	* LargestSpotSize = S
		* C-class = 0: C (94.0/38.0)
		* C-class = 1
			* HistComplex = 1
				* Evolution = 1: C (0.0)
				* Evolution = 2: C (4.0/1.0)
				* Evolution = 3: D (4.0/2.0)
			* HistComplex = 2: D (7.0/3.0)
		* C-class = 2: D (3.0/2.0)
		* C-class = 3: D (4.0/2.0)
		* C-class = 4: C (0.0)
		* C-class = 5: E (1.0)
		* C-class = 6: E (1.0)
		* C-class = 7: C (0.0)
		* C-class = 8: C (0.0)
	* LargestSpotSize = X: B (101.0)
	* LargestSpotSize = K: C (1.0)
	* LargestSpotSize = H: D (11.0/7.0)
* SpotDistribution = I
	* LargestSpotSize = A: D (81.0/35.0)
	* LargestSpotSize = R: D (22.0/6.0)
	* LargestSpotSize = S: D (34.0/20.0)
	* LargestSpotSize = X: B (10.0)
	* LargestSpotSize = K: D (17.0/7.0)
	* LargestSpotSize = H: E (3.0/1.0)
* SpotDistribution = C: E (25.0/10.0)


## SimpleCart Decision Tree

		* SpotDistribution=(C)|(I)|(O)
	* LargestSpotSize=(X): B(128.0/0.0)
	* LargestSpotSize!=(X)
			* SpotDistribution=(C)|(I)
			* Area=(2): E(12.0/11.0)
			* Area!=(2)
				* Evolution=(3)
						* LargestSpotSize=(S)|(R)
						* HistComplex=(2)
											* LargestSpotSize=(S)|(A)|(X)|(K)|(H): D(5.0/6.0)
											* LargestSpotSize!=(S)|(A)|(X)|(K)|(H): D(7.0/1.0)
						* HistComplex!=(2): D(16.0/11.0)
						* LargestSpotSize!=(S)|(R)
						* SpotDistribution=(C): E(4.0/1.0)
						* SpotDistribution!=(C)
							* LargestSpotSize=(K): D(8.0/0.0)
							* LargestSpotSize!=(K)
								* HistComplex=(2)
										* C-class=(4)|(1): E(5.0/2.0)
										* C-class!=(4)|(1): D(18.0/10.0)
								* HistComplex!=(2): D(16.0/3.0)
				* Evolution!=(3)
						* C-class=(4)|(2): F(6.0/4.0)
						* C-class!=(4)|(2)
							* C-class=(8)|(3): E(4.0/2.0)
							* C-class!=(8)|(3)
							* LargestSpotSize=(S): E(5.0/7.0)
							* LargestSpotSize!=(S)
								* HistComplex=(2)
									* SpotDistribution=(C): E(3.0/3.0)
									* SpotDistribution!=(C): D(21.0/19.0)
								* HistComplex!=(2): D(5.0/1.0)
			* SpotDistribution!=(C)|(I)
						* LargestSpotSize=(K)|(S)|(R)|(X)
				* HistComplex=(2): C(30.0/34.0)
				* HistComplex!=(2)
							* C-class=(6)|(2)|(1): D(9.0/10.0)
							* C-class!=(6)|(2)|(1)
						* Evolution=(3): C(61.0/32.0)
						* Evolution!=(3)
							* Activity=(2): C(10.0/2.0)
							* Activity!=(2)
								* LargestSpotSize=(S): C(18.0/7.0)
								* LargestSpotSize!=(S): C(26.0/7.0)
						* LargestSpotSize!=(K)|(S)|(R)|(X)
						* C-class=(4)|(3)|(1)
					* Evolution=(3): D(3.0/1.0)
					* Evolution!=(3): E(9.0/3.0)
						* C-class!=(4)|(3)|(1)
					* Activity=(2): D(5.0/5.0)
					* Activity!=(2): D(20.0/23.0)
		* SpotDistribution!=(C)|(I)|(O): H(298.0/0.0)


