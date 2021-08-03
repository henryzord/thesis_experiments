# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | H | 0.311390 |
| SpotDistribution = O and LargestSpotSize = X | B | 0.122081 |
| LargestSpotSize = R and SpotDistribution = O | C | 0.062940 |
| LargestSpotSize = A and SpotDistribution = I | D | 0.041234 |
| LargestSpotSize = S and SpotDistribution = O | C | 0.054007 |
| LargestSpotSize = R and SpotDistribution = I | D | 0.015979 |
| LargestSpotSize = A and SpotDistribution = O | D | 0.012458 |
| LargestSpotSize = S and SpotDistribution = I | D | 0.012492 |
| SpotDistribution = O and LargestSpotSize!=(X) and SpotDistribution != I and LargestSpotSize != X and C-class != 7 | E | 0.004668 |
| LargestSpotSize = X and SpotDistribution = I | B | 0.015476 |
| LargestSpotSize = K and SpotDistribution = C | E | 0.008642 |
| LargestSpotSize = K and SpotDistribution = I | D | 0.007084 |
| SpotDistribution = O and LargestSpotSize = R and HistComplex = 1 and C-class = 1 | D | 0.004794 |
| SpotDistribution = O and LargestSpotSize = A and Activity = 1 and Evolution = 2 | C | 0.003568 |
| SpotDistribution = O and LargestSpotSize = S and C-class = 1 and Evolution = 3 | D | 0.004200 |
| LargestSpotSize = H and SpotDistribution = O | D | 0.005073 |
| SpotDistribution = C and LargestSpotSize = K and Prev24Hour = 1 | F | 0.002723 |
| SpotDistribution = I and LargestSpotSize = A and HistComplex = 2 and Evolution = 3 and Activity = 2 | E | 0.003179 |
| SpotDistribution = I and LargestSpotSize = S and HistComplex = 2 and Evolution = 2 | E | 0.002395 |
| SpotDistribution = I and LargestSpotSize = K and Evolution = 2 | F | 0.002179 |
| SpotDistribution = O and LargestSpotSize = S and C-class = 2 | D | 0.001348 |
| SpotDistribution = O and LargestSpotSize = S and C-class = 3 | D | 0.001348 |
| SpotDistribution = C and LargestSpotSize = A | D | 0.002399 |
| SpotDistribution = I and LargestSpotSize = A and HistComplex = 2 and Evolution = 2 and C-class = 2 | F | 0.001451 |
| SpotDistribution = C and LargestSpotSize = R | D | 0.001795 |
| SpotDistribution = I and LargestSpotSize = A and HistComplex = 2 and Evolution = 2 and C-class = 3 | E | 0.001527 |
| SpotDistribution = I and LargestSpotSize = H | E | 0.001527 |
| SpotDistribution = I and LargestSpotSize = R and Evolution = 1 | C | 0.001302 |
| SpotDistribution = O and LargestSpotSize = K | C | 0.001302 |
| SpotDistribution = C and LargestSpotSize = H | E | 0.001145 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = X | H | 0.311390 |
| LargestSpotSize = X | B | 0.194825 |
| SpotDistribution = O and C-class = 0 and LargestSpotSize = R and Activity = 1 and HistComplex = 1 | C | 0.111628 |
| Area = 2 and X-class = 0 and LargestSpotSize = K and C-class = 0 and Prev24Hour = 1 | F | 0.006144 |
| SpotDistribution = C and LargestSpotSize = K | E | 0.023077 |
| SpotDistribution = C and C-class = 0 and Evolution = 3 | E | 0.005859 |
| SpotDistribution = C | D | 0.014768 |
| SpotDistribution = O and C-class = 1 and LargestSpotSize = R | D | 0.013075 |
| SpotDistribution = O and C-class = 3 and HistComplex = 1 | C | 0.007212 |
| SpotDistribution = O and C-class = 1 and LargestSpotSize = A | E | 0.004891 |
| SpotDistribution = O and C-class = 1 and LargestSpotSize = S and Prev24Hour = 1 and HistComplex = 1 and Evolution = 3 | D | 0.007759 |
| SpotDistribution = O and C-class = 1 and LargestSpotSize = S and Prev24Hour = 1 and HistComplex = 2 | D | 0.007759 |
| SpotDistribution = O and C-class = 1 and LargestSpotSize = S and Prev24Hour = 1 | C | 0.019951 |
| SpotDistribution = O and C-class = 2 | D | 0.008929 |
| SpotDistribution = O and C-class = 1 and Prev24Hour = 1 | C | 0.006734 |
| SpotDistribution = O and C-class = 0 and LargestSpotSize = R and Evolution = 2 | C | 0.015989 |
| SpotDistribution = O and C-class = 0 and LargestSpotSize = R and Evolution = 1 | C | 0.003367 |
| SpotDistribution = O and C-class = 0 and LargestSpotSize = S and Evolution = 2 | C | 0.066981 |
| SpotDistribution = O and C-class = 0 and LargestSpotSize = A and Activity = 1 and Evolution = 3 and HistComplex = 2 | D | 0.018386 |
| HistComplex = 1 and C-class = 0 and SpotDistribution = I | D | 0.105803 |
| HistComplex = 1 and C-class = 0 and Prev24Hour = 1 and LargestSpotSize = A and Activity = 1 | C | 0.012468 |
| HistComplex = 1 and C-class = 0 and Prev24Hour = 1 and LargestSpotSize = S | C | 0.055513 |
| Area = 2 and Evolution = 3 and Activity = 2 | F | 0.011852 |
| SpotDistribution = I and HistComplex = 1 and Activity = 2 | D | 0.012857 |
| HistComplex = 1 and C-class = 1 | D | 0.046552 |
| SpotDistribution = I and Evolution = 3 and LargestSpotSize = A and M-class = 0 and Activity = 1 | D | 0.048290 |
| SpotDistribution = O and C-class = 0 and LargestSpotSize = H | D | 0.031370 |
| SpotDistribution = O and C-class = 0 and LargestSpotSize = A and HistComplex = 1 | D | 0.048706 |
| SpotDistribution = O and C-class = 0 and LargestSpotSize = A and Activity = 2 and Prev24Hour = 1 | E | 0.015385 |
| SpotDistribution = O and C-class = 0 and LargestSpotSize = A | C | 0.025368 |
| SpotDistribution = O and LargestSpotSize = S and C-class = 0 and Evolution = 3 | C | 0.009863 |
| M-class = 1 | D | 0.037780 |
| LargestSpotSize = K and C-class = 0 | D | 0.012605 |
| LargestSpotSize = R and C-class = 0 | D | 0.222368 |
| HistComplex = 2 and C-class = 3 | E | 0.028346 |
| HistComplex = 2 and SpotDistribution = I and Evolution = 3 and LargestSpotSize = A | E | 0.064171 |
| HistComplex = 2 and SpotDistribution = I and Evolution = 2 and LargestSpotSize = A | D | 0.070914 |
| SpotDistribution = I and HistComplex = 2 and Evolution = 3 | D | 0.075385 |
| LargestSpotSize = S | E | 0.081637 |
| HistComplex = 2 | F | 0.155223 |
|  | C | 0.236559 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

largestspotsize|spotdistribution|class
---|---|---
r|c|d
k|c|e
h|c|h
a|c|d
x|i|b
h|i|e
k|i|d
r|i|d
a|i|d
s|i|d
k|o|h
x|o|b
s|o|c
h|o|d
a|o|d
r|o|c
k|x|h
h|x|h
r|x|h
a|x|h
s|x|h

## PART

Decision list:

rules | predicted class
---|---
SpotDistribution = X|H (298.0)
LargestSpotSize = X|B (128.0)
SpotDistribution = O AND C-class = 0 AND LargestSpotSize = R AND Activity = 1 AND HistComplex = 1|C (86.0/26.0)
Area = 2 AND X-class = 0 AND LargestSpotSize = K AND C-class = 0 AND Prev24Hour = 1|F (6.0/2.0)
SpotDistribution = C AND LargestSpotSize = K|E (15.0/4.0)
SpotDistribution = C AND C-class = 0 AND Evolution = 3|E (4.0/1.0)
SpotDistribution = C|D (9.0/4.0)
SpotDistribution = O AND C-class = 1 AND LargestSpotSize = R|D (8.0/3.0)
SpotDistribution = O AND C-class = 3 AND HistComplex = 1|C (4.0/1.0)
SpotDistribution = O AND C-class = 1 AND LargestSpotSize = A|E (5.0/2.0)
SpotDistribution = O AND C-class = 1 AND LargestSpotSize = S AND Prev24Hour = 1 AND HistComplex = 1 AND Evolution = 3|D (5.0/2.0)
SpotDistribution = O AND C-class = 1 AND LargestSpotSize = S AND Prev24Hour = 1 AND HistComplex = 2|D (5.0/2.0)
SpotDistribution = O AND C-class = 1 AND LargestSpotSize = S AND Prev24Hour = 1|C (4.0/1.0)
SpotDistribution = O AND C-class = 2|D (8.0/4.0)
SpotDistribution = O AND C-class = 1 AND Prev24Hour = 1|C (2.0/1.0)
SpotDistribution = O AND C-class = 0 AND LargestSpotSize = R AND Evolution = 2|C (12.0/3.0)
SpotDistribution = O AND C-class = 0 AND LargestSpotSize = R AND Evolution = 1|C (3.0/1.0)
SpotDistribution = O AND C-class = 0 AND LargestSpotSize = S AND Evolution = 2|C (49.0/17.0)
SpotDistribution = O AND C-class = 0 AND LargestSpotSize = A AND Activity = 1 AND Evolution = 3 AND HistComplex = 2|D (11.0/5.0)
HistComplex = 1 AND C-class = 0 AND SpotDistribution = I|D (38.0/10.0)
HistComplex = 1 AND C-class = 0 AND Prev24Hour = 1 AND LargestSpotSize = A AND Activity = 1|C (13.0/6.0)
HistComplex = 1 AND C-class = 0 AND Prev24Hour = 1 AND LargestSpotSize = S|C (37.0/14.0)
Area = 2 AND Evolution = 3 AND Activity = 2|F (3.0/1.0)
SpotDistribution = I AND HistComplex = 1 AND Activity = 2|D (5.0/2.0)
HistComplex = 1 AND C-class = 1|D (10.0/3.0)
SpotDistribution = I AND Evolution = 3 AND LargestSpotSize = A AND M-class = 0 AND Activity = 1|D (19.0/7.0)
SpotDistribution = O AND C-class = 0 AND LargestSpotSize = H|D (11.0/4.0)
SpotDistribution = O AND C-class = 0 AND LargestSpotSize = A AND HistComplex = 1|D (3.0)
SpotDistribution = O AND C-class = 0 AND LargestSpotSize = A AND Activity = 2 AND Prev24Hour = 1|E (3.0)
SpotDistribution = O AND C-class = 0 AND LargestSpotSize = A|C (12.0/6.0)
SpotDistribution = O AND LargestSpotSize = S AND C-class = 0 AND Evolution = 3|C (11.0/4.0)
M-class = 1|D (10.0/3.0)
LargestSpotSize = K AND C-class = 0|D (4.0/1.0)
LargestSpotSize = R AND C-class = 0|D (13.0/2.0)
HistComplex = 2 AND C-class = 3|E (9.0/4.0)
HistComplex = 2 AND SpotDistribution = I AND Evolution = 3 AND LargestSpotSize = A|E (10.0/4.0)
HistComplex = 2 AND SpotDistribution = I AND Evolution = 2 AND LargestSpotSize = A|D (37.0/21.0)
SpotDistribution = I AND HistComplex = 2 AND Evolution = 3|D (16.0/5.0)
LargestSpotSize = S|E (20.0/12.0)
HistComplex = 2|F (7.0/3.0)
|C (4.0/1.0)


## J48 Decision Tree

* SpotDistribution = X: H (298.0)
* SpotDistribution = O
	* LargestSpotSize = A
		* Activity = 1
			* Evolution = 1: D (3.0/2.0)
			* Evolution = 2: C (18.0/11.0)
			* Evolution = 3
				* HistComplex = 1: D (10.0/6.0)
				* HistComplex = 2: D (11.0/5.0)
		* Activity = 2: D (11.0/6.0)
	* LargestSpotSize = R
		* HistComplex = 1
			* C-class = 0
				* Evolution = 1: C (5.0/1.0)
				* Evolution = 2: C (27.0/5.0)
				* Evolution = 3: C (55.0/20.0)
			* C-class = 1: D (7.0/2.0)
			* C-class = 2: C (0.0)
			* C-class = 3: C (1.0)
			* C-class = 4: C (0.0)
			* C-class = 5: C (1.0)
			* C-class = 6: C (0.0)
			* C-class = 7: C (0.0)
			* C-class = 8: C (0.0)
		* HistComplex = 2: C (18.0/7.0)
	* LargestSpotSize = S
		* C-class = 0
			* Evolution = 1: C (8.0/5.0)
			* Evolution = 2
				* HistComplex = 1
					* Activity = 1: C (18.0/5.0)
					* Activity = 2: C (8.0/2.0)
				* HistComplex = 2: C (23.0/10.0)
			* Evolution = 3
				* HistComplex = 1: C (36.0/14.0)
				* HistComplex = 2: C (9.0/3.0)
		* C-class = 1
			* Evolution = 1: D (0.0)
			* Evolution = 2: C (9.0/4.0)
			* Evolution = 3: D (8.0/3.0)
		* C-class = 2: D (4.0/2.0)
		* C-class = 3: D (4.0/2.0)
		* C-class = 4: C (0.0)
		* C-class = 5: E (1.0)
		* C-class = 6: E (1.0)
		* C-class = 7: C (0.0)
		* C-class = 8: C (0.0)
	* LargestSpotSize = X: B (115.0)
	* LargestSpotSize = K: C (1.0)
	* LargestSpotSize = H: D (13.0/6.0)
* SpotDistribution = I
	* LargestSpotSize = A
		* HistComplex = 1
			* Activity = 1: D (17.0/2.0)
			* Activity = 2: D (7.0/2.0)
		* HistComplex = 2
			* Evolution = 1: D (2.0/1.0)
			* Evolution = 2
				* C-class = 0
					* Activity = 1: D (16.0/9.0)
					* Activity = 2: D (9.0/5.0)
				* C-class = 1: D (8.0/4.0)
				* C-class = 2: F (3.0/1.0)
				* C-class = 3: E (3.0/1.0)
				* C-class = 4: D (2.0/1.0)
				* C-class = 5: D (0.0)
				* C-class = 6: D (0.0)
				* C-class = 7: D (0.0)
				* C-class = 8: D (0.0)
			* Evolution = 3
				* Activity = 1: D (21.0/7.0)
				* Activity = 2: E (13.0/7.0)
	* LargestSpotSize = R
		* Evolution = 1: C (1.0)
		* Evolution = 2: D (9.0/4.0)
		* Evolution = 3: D (17.0/4.0)
	* LargestSpotSize = S
		* HistComplex = 1: D (17.0/7.0)
		* HistComplex = 2
			* Evolution = 1: D (1.0)
			* Evolution = 2: E (12.0/7.0)
			* Evolution = 3: D (9.0/5.0)
	* LargestSpotSize = X: B (13.0)
	* LargestSpotSize = K
		* Evolution = 1: D (0.0)
		* Evolution = 2: F (8.0/4.0)
		* Evolution = 3: D (11.0/4.0)
	* LargestSpotSize = H: E (3.0/1.0)
* SpotDistribution = C
	* LargestSpotSize = A: D (9.0/5.0)
	* LargestSpotSize = R: D (3.0/1.0)
	* LargestSpotSize = S: E (0.0)
	* LargestSpotSize = X: E (0.0)
	* LargestSpotSize = K
		* Prev24Hour = 1: F (10.0/5.0)
		* Prev24Hour = 2: E (2.0)
		* Prev24Hour = 3: E (7.0/1.0)
	* LargestSpotSize = H: E (1.0)


## SimpleCart Decision Tree

		* SpotDistribution=(C)|(I)|(O)
	* LargestSpotSize=(X): B(128.0/0.0)
	* LargestSpotSize!=(X)
			* SpotDistribution=(C)|(I)
			* Area=(2)
					* Prev24Hour=(3)|(2)
					* Evolution=(3): E(3.0/1.0)
					* Evolution!=(3): E(5.0/0.0)
					* Prev24Hour!=(3)|(2): F(10.0/6.0)
			* Area!=(2)
				* HistComplex=(2)
					* Evolution=(3): D(38.0/25.0)
					* Evolution!=(3): D(32.0/43.0)
				* HistComplex!=(2)
									* LargestSpotSize=(S)|(R)|(X)|(K)|(H)
						* Activity=(2): D(4.0/1.0)
						* Activity!=(2): D(15.0/13.0)
									* LargestSpotSize!=(S)|(R)|(X)|(K)|(H)
											* C-class=(0)|(1)|(4)|(5)|(6)|(7)
								* Evolution=(3)|(1): D(14.0/2.0)
								* Evolution!=(3)|(1): D(4.0/0.0)
											* C-class!=(0)|(1)|(4)|(5)|(6)|(7): D(3.0/2.0)
			* SpotDistribution!=(C)|(I)
					* LargestSpotSize=(S)|(R)|(X)
							* C-class=(0)|(4)|(7)|(8): C(134.0/72.0)
							* C-class!=(0)|(4)|(7)|(8): D(18.0/19.0)
					* LargestSpotSize!=(S)|(R)|(X)
								* C-class=(0)|(5)|(6)|(7)|(8)
					* Activity=(2): D(4.0/5.0)
					* Activity!=(2)
						* LargestSpotSize=(H): D(7.0/3.0)
						* LargestSpotSize!=(H): C(16.0/18.0)
								* C-class!=(0)|(5)|(6)|(7)|(8): E(8.0/6.0)
		* SpotDistribution!=(C)|(I)|(O): H(298.0/0.0)


