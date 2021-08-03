# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | H | 0.310417 |
| SpotDistribution != X and LargestSpotSize = X | B | 0.136743 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution = O and LargestSpotSize != A and LargestSpotSize != H and C-class != 1 | C | 0.108063 |
| SpotDistribution = O and LargestSpotSize!=(X) and SpotDistribution != I and LargestSpotSize != X and C-class = 0 | D | 0.039941 |
| LargestSpotSize = A and SpotDistribution = I and X-class = 0 | D | 0.041071 |
| SpotDistribution = O and LargestSpotSize!=(X) and SpotDistribution != I and LargestSpotSize != X and C-class != 7 | E | 0.004645 |
| LargestSpotSize = R and SpotDistribution = I and X-class = 0 | D | 0.015915 |
| LargestSpotSize = S and SpotDistribution = I and X-class = 0 | D | 0.012441 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution = O and LargestSpotSize != A and LargestSpotSize != H and C-class = 1 | D | 0.010481 |
| SpotDistribution != X and LargestSpotSize != X and Area != 1 and Prev24Hour != 1 | E | 0.008062 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution = O and LargestSpotSize = A and C-class = 0 and Activity = 1 and Evolution = 2 | C | 0.004889 |
| SpotDistribution != X and LargestSpotSize != X and Area != 1 and Prev24Hour = 1 | F | 0.006366 |
| LargestSpotSize = K and SpotDistribution = I and X-class = 0 | D | 0.007055 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution = O and LargestSpotSize = A and C-class = 0 and Activity = 1 and Evolution != 2 and HistComplex = 1 | C | 0.003603 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution != O and HistComplex != 1 and LargestSpotSize != R and LargestSpotSize != H and M-class != 1 and C-class != 2 and Evolution = 3 and Activity != 1 and C-class != 0 | E | 0.003645 |
| LargestSpotSize = S and SpotDistribution = O and X-class = 0 | C | 0.053802 |
| LargestSpotSize = K and SpotDistribution = C and X-class = 0 | E | 0.007576 |
| LargestSpotSize = R and SpotDistribution = O and X-class = 0 | C | 0.062706 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution != O and HistComplex != 1 and LargestSpotSize != R and LargestSpotSize != H and M-class != 1 and C-class = 2 and Evolution = 2 | F | 0.002438 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution != O and HistComplex != 1 and LargestSpotSize != R and LargestSpotSize != H and M-class != 1 and C-class != 2 and Evolution != 3 and C-class = 3 | E | 0.002055 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution != O and HistComplex != 1 and LargestSpotSize != R and LargestSpotSize = H | E | 0.002566 |
| LargestSpotSize = A and SpotDistribution = C and X-class = 0 | D | 0.002389 |
| LargestSpotSize = A and SpotDistribution = O and X-class = 0 | D | 0.012408 |
| LargestSpotSize = R and SpotDistribution = C and X-class = 0 | D | 0.001787 |
| LargestSpotSize = H and SpotDistribution = I and X-class = 0 | D | 0.000448 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = X | H | 0.310417 |
| LargestSpotSize = X | B | 0.198485 |
| Area != 1 and Prev24Hour = 1 and C-class != 1 | F | 0.008999 |
| SpotDistribution = O and LargestSpotSize != A and LargestSpotSize != H and C-class = 1 and Evolution != 2 | D | 0.015779 |
| SpotDistribution = O and LargestSpotSize != A and LargestSpotSize != H and LargestSpotSize != S and HistComplex = 1 and Evolution = 3 | C | 0.072374 |
| SpotDistribution = O and LargestSpotSize != A and LargestSpotSize != H and C-class != 1 and C-class = 0 and LargestSpotSize = R and HistComplex = 1 | C | 0.039877 |
| SpotDistribution = O and LargestSpotSize != A and LargestSpotSize != H and C-class != 1 and Evolution != 1 and Activity = 1 and LargestSpotSize = S and C-class = 0 and HistComplex != 1 and Evolution = 2 | C | 0.018445 |
| SpotDistribution = O and LargestSpotSize != A and LargestSpotSize != H and C-class = 1 | D | 0.010390 |
| SpotDistribution = O and C-class != 1 and LargestSpotSize = H | D | 0.018796 |
| SpotDistribution = O and C-class != 1 and C-class = 0 and LargestSpotSize != A and Evolution != 1 and Activity = 1 and HistComplex != 1 and Evolution = 2 | C | 0.010866 |
| SpotDistribution = O and LargestSpotSize != A and C-class = 0 and LargestSpotSize != R and Evolution != 1 and Activity != 1 and Evolution = 2 | C | 0.016824 |
| SpotDistribution = O and Activity != 1 and LargestSpotSize != S | E | 0.013895 |
| SpotDistribution = O and C-class = 0 and Evolution != 1 and LargestSpotSize = S and HistComplex = 1 and Evolution != 2 | C | 0.042953 |
| Area != 1 and C-class = 1 | F | 0.005714 |
| SpotDistribution = O and C-class = 0 and LargestSpotSize != S and Evolution != 2 and HistComplex != 1 | D | 0.027174 |
| SpotDistribution = O and C-class = 0 and Evolution != 1 and LargestSpotSize != A and Evolution = 2 | C | 0.016313 |
| Area = 1 and SpotDistribution = O and C-class = 0 and Evolution != 1 and LargestSpotSize = A and HistComplex = 1 | C | 0.008333 |
| Area = 1 and SpotDistribution != O and HistComplex = 1 and LargestSpotSize = A and Activity = 1 | D | 0.074356 |
| Area = 1 and SpotDistribution = O and C-class = 0 and Evolution != 3 and LargestSpotSize = A | C | 0.012681 |
| Area = 1 and HistComplex = 1 and LargestSpotSize = A | D | 0.064157 |
| Area != 1 | E | 0.052688 |
| HistComplex = 1 and Evolution != 3 and C-class = 0 | C | 0.003568 |
| HistComplex = 1 and Evolution != 2 and SpotDistribution = I and C-class = 0 and LargestSpotSize != R | D | 0.032193 |
| HistComplex = 1 and SpotDistribution = I and C-class != 0 | D | 0.015097 |
| SpotDistribution != O and LargestSpotSize = R and Evolution = 3 and HistComplex = 1 | D | 0.017857 |
| SpotDistribution != O and LargestSpotSize = R and Evolution = 3 | D | 0.028756 |
| SpotDistribution != O and LargestSpotSize != R and M-class = 0 and C-class != 2 and Evolution = 3 and LargestSpotSize != S and Activity = 1 and C-class = 0 | D | 0.023501 |
| SpotDistribution = O and LargestSpotSize != A and Evolution = 3 and C-class = 0 | C | 0.007521 |
| HistComplex = 1 | C | 0.028197 |
| LargestSpotSize = R | D | 0.197283 |
| M-class != 0 and C-class != 0 | E | 0.011765 |
| M-class = 0 and C-class = 2 | D | 0.037037 |
| M-class = 0 and C-class != 0 and SpotDistribution != O and Evolution != 2 and C-class = 1 | D | 0.025484 |
| M-class = 0 and C-class = 3 and Evolution = 2 | E | 0.010369 |
| M-class = 0 and C-class != 3 and SpotDistribution != O and C-class != 0 | D | 0.014107 |
| C-class = 0 and SpotDistribution != C and LargestSpotSize != S and Activity != 1 and Evolution = 2 | D | 0.035559 |
| C-class != 0 | E | 0.072200 |
| SpotDistribution != C and Evolution = 3 and Activity != 1 | D | 0.046402 |
| SpotDistribution != C and Evolution != 3 and Evolution != 1 and LargestSpotSize = A | D | 0.042230 |
| SpotDistribution != C and Evolution != 3 and Evolution != 1 | E | 0.057781 |
| SpotDistribution != I | E | 0.046429 |
|  | D | 0.442308 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

largestspotsize|spotdistribution|x-class|class
---|---|---|---
k|c|2|h
k|c|1|e
h|c|0|h
k|c|0|e
a|c|0|d
r|c|0|d
h|i|0|d
k|i|0|d
r|i|0|d
a|i|0|d
s|i|0|d
x|i|0|b
k|o|0|h
h|o|0|d
a|o|0|d
r|o|0|c
s|o|0|c
x|o|0|b
k|x|0|h
h|x|0|h
s|x|0|h
a|x|0|h
r|x|0|h

## PART

Decision list:

rules | predicted class
---|---
SpotDistribution = X|H (298.0)
LargestSpotSize = X|B (131.0)
Area != 1 AND Prev24Hour = 1 AND C-class != 1|F (11.0/4.0)
SpotDistribution = O AND LargestSpotSize != A AND LargestSpotSize != H AND C-class = 1 AND Evolution != 2|D (13.0/5.0)
SpotDistribution = O AND LargestSpotSize != A AND LargestSpotSize != H AND LargestSpotSize != S AND HistComplex = 1 AND Evolution = 3|C (56.0/20.0)
SpotDistribution = O AND LargestSpotSize != A AND LargestSpotSize != H AND C-class != 1 AND C-class = 0 AND LargestSpotSize = R AND HistComplex = 1|C (32.0/6.0)
SpotDistribution = O AND LargestSpotSize != A AND LargestSpotSize != H AND C-class != 1 AND Evolution != 1 AND Activity = 1 AND LargestSpotSize = S AND C-class = 0 AND HistComplex != 1 AND Evolution = 2|C (20.0/9.0)
SpotDistribution = O AND LargestSpotSize != A AND LargestSpotSize != H AND C-class = 1|D (12.0/6.0)
SpotDistribution = O AND C-class != 1 AND LargestSpotSize = H|D (11.0/4.0)
SpotDistribution = O AND C-class != 1 AND C-class = 0 AND LargestSpotSize != A AND Evolution != 1 AND Activity = 1 AND HistComplex != 1 AND Evolution = 2|C (10.0/2.0)
SpotDistribution = O AND LargestSpotSize != A AND C-class = 0 AND LargestSpotSize != R AND Evolution != 1 AND Activity != 1 AND Evolution = 2|C (11.0/3.0)
SpotDistribution = O AND Activity != 1 AND LargestSpotSize != S|E (13.0/6.0)
SpotDistribution = O AND C-class = 0 AND Evolution != 1 AND LargestSpotSize = S AND HistComplex = 1 AND Evolution != 2|C (36.0/14.0)
Area != 1 AND C-class = 1|F (8.0/4.0)
SpotDistribution = O AND C-class = 0 AND LargestSpotSize != S AND Evolution != 2 AND HistComplex != 1|D (17.0/7.0)
SpotDistribution = O AND C-class = 0 AND Evolution != 1 AND LargestSpotSize != A AND Evolution = 2|C (18.0/5.0)
Area = 1 AND SpotDistribution = O AND C-class = 0 AND Evolution != 1 AND LargestSpotSize = A AND HistComplex = 1|C (12.0/6.0)
Area = 1 AND SpotDistribution != O AND HistComplex = 1 AND LargestSpotSize = A AND Activity = 1|D (17.0/2.0)
Area = 1 AND SpotDistribution = O AND C-class = 0 AND Evolution != 3 AND LargestSpotSize = A|C (10.0/4.0)
Area = 1 AND HistComplex = 1 AND LargestSpotSize = A|D (10.0/3.0)
Area != 1|E (7.0)
HistComplex = 1 AND Evolution != 3 AND C-class = 0|C (6.0/2.0)
HistComplex = 1 AND Evolution != 2 AND SpotDistribution = I AND C-class = 0 AND LargestSpotSize != R|D (12.0/4.0)
HistComplex = 1 AND SpotDistribution = I AND C-class != 0|D (10.0/5.0)
SpotDistribution != O AND LargestSpotSize = R AND Evolution = 3 AND HistComplex = 1|D (8.0/3.0)
SpotDistribution != O AND LargestSpotSize = R AND Evolution = 3|D (7.0)
SpotDistribution != O AND LargestSpotSize != R AND M-class = 0 AND C-class != 2 AND Evolution = 3 AND LargestSpotSize != S AND Activity = 1 AND C-class = 0|D (13.0/6.0)
SpotDistribution = O AND LargestSpotSize != A AND Evolution = 3 AND C-class = 0|C (9.0/3.0)
HistComplex = 1|C (10.0/5.0)
LargestSpotSize = R|D (7.0/3.0)
M-class != 0 AND C-class != 0|E (7.0/3.0)
M-class = 0 AND C-class = 2|D (12.0/5.0)
M-class = 0 AND C-class != 0 AND SpotDistribution != O AND Evolution != 2 AND C-class = 1|D (9.0/4.0)
M-class = 0 AND C-class = 3 AND Evolution = 2|E (6.0/3.0)
M-class = 0 AND C-class != 3 AND SpotDistribution != O AND C-class != 0|D (16.0/10.0)
C-class = 0 AND SpotDistribution != C AND LargestSpotSize != S AND Activity != 1 AND Evolution = 2|D (12.0/6.0)
C-class != 0|E (10.0/4.0)
SpotDistribution != C AND Evolution = 3 AND Activity != 1|D (8.0/4.0)
SpotDistribution != C AND Evolution != 3 AND Evolution != 1 AND LargestSpotSize = A|D (16.0/9.0)
SpotDistribution != C AND Evolution != 3 AND Evolution != 1|E (9.0/5.0)
SpotDistribution != I|E (12.0/6.0)
|D (8.0/2.0)


## J48 Decision Tree

* SpotDistribution = X: H (298.0)
* SpotDistribution != X
	* LargestSpotSize = X: B (131.0)
	* LargestSpotSize != X
		* Area = 1
			* SpotDistribution = O
				* LargestSpotSize = A
					* C-class = 0
						* Activity = 1
							* Evolution = 2: C (13.0/6.0)
							* Evolution != 2
								* HistComplex = 1: C (9.0/4.0)
								* HistComplex != 1: D (12.0/5.0)
						* Activity != 1
							* Evolution = 2: E (4.0/2.0)
							* Evolution != 2: D (4.0/1.0)
					* C-class != 0: E (11.0/4.0)
				* LargestSpotSize != A
					* LargestSpotSize = H: D (13.0/6.0)
					* LargestSpotSize != H
						* C-class = 1: D (25.0/11.0)
						* C-class != 1: C (218.0/78.0)
			* SpotDistribution != O
				* HistComplex = 1: D (58.0/18.0)
				* HistComplex != 1
					* LargestSpotSize = R: D (14.0/3.0)
					* LargestSpotSize != R
						* LargestSpotSize = H: E (4.0/1.0)
						* LargestSpotSize != H
							* M-class = 1: D (8.0/2.0)
							* M-class != 1
								* C-class = 2
									* Evolution = 2: F (4.0/1.0)
									* Evolution != 2: D (7.0/2.0)
								* C-class != 2
									* Evolution = 3
										* Activity = 1: D (27.0/10.0)
										* Activity != 1
											* C-class = 0: D (7.0/4.0)
											* C-class != 0: E (5.0/1.0)
									* Evolution != 3
										* C-class = 3: E (5.0/2.0)
										* C-class != 3: D (57.0/33.0)
		* Area != 1
			* Prev24Hour = 1: F (17.0/7.0)
			* Prev24Hour != 1: E (9.0/1.0)


## SimpleCart Decision Tree

		* SpotDistribution=(C)|(I)|(O)
	* LargestSpotSize=(X): B(131.0/0.0)
	* LargestSpotSize!=(X)
			* SpotDistribution=(C)|(I)
			* Area=(2): E(13.0/12.0)
			* Area!=(2)
				* HistComplex=(2)
					* Evolution=(3): D(38.0/25.0)
					* Evolution!=(3): D(32.0/43.0)
				* HistComplex!=(2)
									* LargestSpotSize=(S)|(R)|(X)|(K)|(H): D(19.0/14.0)
									* LargestSpotSize!=(S)|(R)|(X)|(K)|(H): D(21.0/4.0)
			* SpotDistribution!=(C)|(I)
					* LargestSpotSize=(S)|(R)|(X)
							* C-class=(0)|(4)|(7)|(8): C(134.0/72.0)
							* C-class!=(0)|(4)|(7)|(8): D(18.0/19.0)
					* LargestSpotSize!=(S)|(R)|(X)
								* C-class=(0)|(5)|(6)|(7)|(8): D(25.0/28.0)
								* C-class!=(0)|(5)|(6)|(7)|(8): E(8.0/6.0)
		* SpotDistribution!=(C)|(I)|(O): H(298.0/0.0)


