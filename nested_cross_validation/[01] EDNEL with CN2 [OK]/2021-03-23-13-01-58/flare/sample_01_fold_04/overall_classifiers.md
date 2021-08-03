# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = X | H | 0.311715 |
| SpotDistribution = O and LargestSpotSize = X | B | 0.122210 |
| SpotDistribution = O and LargestSpotSize!=(X) and SpotDistribution != I and LargestSpotSize != X and Activity!=(2) | D | 0.056753 |
| SpotDistribution = O and LargestSpotSize = R | C | 0.061371 |
| SpotDistribution = O and LargestSpotSize = S | C | 0.055406 |
| SpotDistribution = I and LargestSpotSize = A | D | 0.042956 |
| SpotDistribution = C | E | 0.010345 |
| SpotDistribution = I and LargestSpotSize = R | D | 0.014840 |
| SpotDistribution = I and LargestSpotSize = X | B | 0.015495 |
| SpotDistribution = I and LargestSpotSize = S | D | 0.010068 |
| SpotDistribution = I and LargestSpotSize = K | D | 0.006435 |
| SpotDistribution = I and LargestSpotSize = H | E | 0.002291 |
| SpotDistribution = O and LargestSpotSize = K | C | 0.001304 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = X | H | 0.311715 |
| LargestSpotSize = X | B | 0.195122 |
| SpotDistribution = O and C-class = 0 and LargestSpotSize = R and HistComplex = 1 | C | 0.119318 |
| Area = 2 and X-class = 0 and Prev24Hour = 1 and Activity = 2 | F | 0.009259 |
| SpotDistribution = C and LargestSpotSize = K | E | 0.022116 |
| SpotDistribution = C and C-class = 0 and Evolution = 2 | D | 0.004274 |
| SpotDistribution = C and C-class = 0 | E | 0.004011 |
| SpotDistribution = O and LargestSpotSize = R and C-class = 1 | D | 0.015263 |
| SpotDistribution = O and LargestSpotSize = R | C | 0.008562 |
| SpotDistribution = C | D | 0.009513 |
| SpotDistribution = O and LargestSpotSize = S and C-class = 1 and Evolution = 2 and HistComplex = 2 | D | 0.008108 |
| SpotDistribution = O and LargestSpotSize = S and C-class = 1 and Evolution = 3 | D | 0.012513 |
| SpotDistribution = O and C-class = 0 and LargestSpotSize = S and HistComplex = 1 | C | 0.093653 |
| SpotDistribution = O and C-class = 0 and Prev24Hour = 1 and LargestSpotSize = H | D | 0.022222 |
| SpotDistribution = O and C-class = 0 and Prev24Hour = 1 and Activity = 1 and Evolution = 2 and HistComplex = 2 | C | 0.028153 |
| HistComplex = 1 and C-class = 1 and Evolution = 3 and LargestSpotSize = A | D | 0.029940 |
| HistComplex = 1 and C-class = 1 and SpotDistribution = O | C | 0.027027 |
| HistComplex = 1 and Activity = 2 | D | 0.047778 |
| HistComplex = 1 and C-class = 2 | C | 0.005396 |
| HistComplex = 1 and C-class = 1 and LargestSpotSize = R | D | 0.008772 |
| HistComplex = 1 and C-class = 0 | D | 0.258329 |
| SpotDistribution = O and C-class = 0 and Evolution = 3 and LargestSpotSize = S and Activity = 1 | C | 0.010163 |
| LargestSpotSize = R | D | 0.058612 |
| SpotDistribution = I and HistComplex = 2 and M-class = 0 and Evolution = 3 and LargestSpotSize = A and Activity = 1 | D | 0.050192 |
| SpotDistribution = O and C-class = 0 and Prev24Hour = 1 and Evolution = 3 | D | 0.029227 |
| HistComplex = 2 and M-class = 1 | D | 0.020548 |
| HistComplex = 1 | C | 0.057927 |
| C-class = 2 and LargestSpotSize = A | D | 0.017857 |
| C-class = 1 and Evolution = 2 and SpotDistribution = I | D | 0.027559 |
| C-class = 1 and Activity = 2 | E | 0.030586 |
| C-class = 3 | E | 0.030586 |
| C-class = 1 and Evolution = 2 | E | 0.011429 |
| C-class = 2 | D | 0.013468 |
| C-class = 0 and Prev24Hour = 3 and SpotDistribution = O | D | 0.013514 |
| C-class = 0 and Prev24Hour = 1 and Activity = 1 and Evolution = 2 and LargestSpotSize = A | D | 0.037156 |
| C-class = 4 | E | 0.014446 |
| C-class = 0 and Prev24Hour = 1 and Evolution = 3 and LargestSpotSize = S and Activity = 1 | D | 0.005442 |
| C-class = 0 and Prev24Hour = 1 and LargestSpotSize = S | E | 0.074013 |
| C-class = 0 and SpotDistribution = I and Evolution = 2 | F | 0.038118 |
| Evolution = 3 and C-class = 0 | D | 0.012419 |
| Activity = 1 | D | 0.114605 |
|  | E | 0.404494 |


# Text representation of classifiers as-is

## PART

Decision list:

rules | predicted class
---|---
SpotDistribution = X|H (298.0)
LargestSpotSize = X|B (128.0)
SpotDistribution = O AND C-class = 0 AND LargestSpotSize = R AND HistComplex = 1|C (88.0/25.0)
Area = 2 AND X-class = 0 AND Prev24Hour = 1 AND Activity = 2|F (9.0/3.0)
SpotDistribution = C AND LargestSpotSize = K|E (15.0/5.0)
SpotDistribution = C AND C-class = 0 AND Evolution = 2|D (3.0/1.0)
SpotDistribution = C AND C-class = 0|E (3.0/1.0)
SpotDistribution = O AND LargestSpotSize = R AND C-class = 1|D (7.0/2.0)
SpotDistribution = O AND LargestSpotSize = R|C (13.0/5.0)
SpotDistribution = C|D (6.0/3.0)
SpotDistribution = O AND LargestSpotSize = S AND C-class = 1 AND Evolution = 2 AND HistComplex = 2|D (5.0/2.0)
SpotDistribution = O AND LargestSpotSize = S AND C-class = 1 AND Evolution = 3|D (9.0/4.0)
SpotDistribution = O AND C-class = 0 AND LargestSpotSize = S AND HistComplex = 1|C (64.0/20.0)
SpotDistribution = O AND C-class = 0 AND Prev24Hour = 1 AND LargestSpotSize = H|D (9.0/3.0)
SpotDistribution = O AND C-class = 0 AND Prev24Hour = 1 AND Activity = 1 AND Evolution = 2 AND HistComplex = 2|C (26.0/11.0)
HistComplex = 1 AND C-class = 1 AND Evolution = 3 AND LargestSpotSize = A|D (5.0)
HistComplex = 1 AND C-class = 1 AND SpotDistribution = O|C (5.0)
HistComplex = 1 AND Activity = 2|D (11.0/2.0)
HistComplex = 1 AND C-class = 2|C (5.0/2.0)
HistComplex = 1 AND C-class = 1 AND LargestSpotSize = R|D (3.0/1.0)
HistComplex = 1 AND C-class = 0|D (50.0/18.0)
SpotDistribution = O AND C-class = 0 AND Evolution = 3 AND LargestSpotSize = S AND Activity = 1|C (9.0/4.0)
LargestSpotSize = R|D (12.0/3.0)
SpotDistribution = I AND HistComplex = 2 AND M-class = 0 AND Evolution = 3 AND LargestSpotSize = A AND Activity = 1|D (19.0/7.0)
SpotDistribution = O AND C-class = 0 AND Prev24Hour = 1 AND Evolution = 3|D (15.0/8.0)
HistComplex = 2 AND M-class = 1|D (10.0/4.0)
HistComplex = 1|C (7.0/3.0)
C-class = 2 AND LargestSpotSize = A|D (6.0/2.0)
C-class = 1 AND Evolution = 2 AND SpotDistribution = I|D (13.0/6.0)
C-class = 1 AND Activity = 2|E (5.0)
C-class = 3|E (8.0/4.0)
C-class = 1 AND Evolution = 2|E (4.0/2.0)
C-class = 2|D (6.0/3.0)
C-class = 0 AND Prev24Hour = 3 AND SpotDistribution = O|D (5.0/2.0)
C-class = 0 AND Prev24Hour = 1 AND Activity = 1 AND Evolution = 2 AND LargestSpotSize = A|D (17.0/10.0)
C-class = 4|E (5.0/3.0)
C-class = 0 AND Prev24Hour = 1 AND Evolution = 3 AND LargestSpotSize = S AND Activity = 1|D (3.0/1.0)
C-class = 0 AND Prev24Hour = 1 AND LargestSpotSize = S|E (21.0/12.0)
C-class = 0 AND SpotDistribution = I AND Evolution = 2|F (10.0/4.0)
Evolution = 3 AND C-class = 0|D (8.0/4.0)
Activity = 1|D (6.0/2.0)
|E (5.0)


## J48 Decision Tree

* SpotDistribution = X: H (149.0)
* SpotDistribution = O
	* LargestSpotSize = A: D (28.0/13.0)
	* LargestSpotSize = R: C (53.0/17.0)
	* LargestSpotSize = S: C (57.0/16.0)
	* LargestSpotSize = X: B (58.0)
	* LargestSpotSize = K: C (1.0)
	* LargestSpotSize = H: D (10.0/6.0)
* SpotDistribution = I
	* LargestSpotSize = A: D (56.0/26.0)
	* LargestSpotSize = R: D (15.0/4.0)
	* LargestSpotSize = S: D (18.0/7.0)
	* LargestSpotSize = X: B (6.0)
	* LargestSpotSize = K: D (6.0/3.0)
	* LargestSpotSize = H: E (2.0)
* SpotDistribution = C: E (19.0/10.0)


## SimpleCart Decision Tree

		* SpotDistribution=(C)|(I)|(O)
	* LargestSpotSize=(X): B(128.0/0.0)
	* LargestSpotSize!=(X)
			* SpotDistribution=(C)|(I)
			* Area=(2)
					* Prev24Hour=(3)|(2)
						* Evolution=(3)|(1): E(3.0/1.0)
						* Evolution!=(3)|(1): E(4.0/0.0)
					* Prev24Hour!=(3)|(2): F(9.0/7.0)
			* Area!=(2)
				* HistComplex=(2)
					* Evolution=(3)
						* LargestSpotSize=(S): D(3.0/5.0)
						* LargestSpotSize!=(S)
								* LargestSpotSize=(K)|(R): D(14.0/2.0)
								* LargestSpotSize!=(K)|(R): D(20.0/19.0)
					* Evolution!=(3): D(30.0/47.0)
				* HistComplex!=(2)
									* LargestSpotSize=(S)|(R)|(X)|(K)|(H)
						* Activity=(2): D(4.0/0.0)
						* Activity!=(2): D(14.0/14.0)
									* LargestSpotSize!=(S)|(R)|(X)|(K)|(H)
											* C-class=(0)|(1)|(4)|(5)|(6)|(7)
								* Evolution=(3)|(1): D(16.0/2.0)
								* Evolution!=(3)|(1): D(4.0/0.0)
											* C-class!=(0)|(1)|(4)|(5)|(6)|(7): D(3.0/3.0)
			* SpotDistribution!=(C)|(I)
					* LargestSpotSize=(S)|(R)|(X)
				* HistComplex=(2): C(31.0/32.0)
				* HistComplex!=(2)
					* Evolution=(3): C(64.0/42.0)
					* Evolution!=(3)
							* C-class=(3)|(1): C(4.0/3.0)
							* C-class!=(3)|(1)
							* LargestSpotSize=(S): C(23.0/6.0)
							* LargestSpotSize!=(S): C(26.0/6.0)
					* LargestSpotSize!=(S)|(R)|(X)
				* Activity=(2): E(8.0/5.0)
				* Activity!=(2): D(27.0/29.0)
		* SpotDistribution!=(C)|(I)|(O): H(298.0/0.0)


