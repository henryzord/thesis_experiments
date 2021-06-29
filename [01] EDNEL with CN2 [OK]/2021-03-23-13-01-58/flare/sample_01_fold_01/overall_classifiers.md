# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = X | H | 0.308577 |
| LargestSpotSize = X and SpotDistribution = O and Area = 1 | B | 0.124468 |
| LargestSpotSize = R and SpotDistribution = O and Area = 1 | C | 0.062389 |
| LargestSpotSize = A and SpotDistribution = I and Area = 1 | D | 0.043795 |
| LargestSpotSize = S and SpotDistribution = O and Area = 1 | C | 0.053035 |
| SpotDistribution = O and LargestSpotSize!=(X) and SpotDistribution != I and C-class != 8 and LargestSpotSize = R | D | 0.016384 |
| SpotDistribution = O and LargestSpotSize!=(X) and SpotDistribution != I and C-class != 8 and LargestSpotSize = S | D | 0.017197 |
| LargestSpotSize = A and SpotDistribution = O and Area = 1 | D | 0.014512 |
| SpotDistribution = O and LargestSpotSize!=(X) and SpotDistribution != I and C-class != 8 and LargestSpotSize != X | E | 0.004099 |
| SpotDistribution = O and LargestSpotSize = A and C-class = 0 and Activity = 1 | C | 0.011082 |
| SpotDistribution = I and LargestSpotSize = R | D | 0.014840 |
| LargestSpotSize = X and SpotDistribution = I and Area = 1 | B | 0.016726 |
| LargestSpotSize = S and SpotDistribution = I and Area = 1 | D | 0.011257 |
| LargestSpotSize = K and SpotDistribution = C and Area = 2 | E | 0.007143 |
| SpotDistribution = I and LargestSpotSize = K and Area = 1 | D | 0.010784 |
| SpotDistribution = C and LargestSpotSize = K and Prev24Hour = 1 and M-class = 0 | F | 0.002902 |
| SpotDistribution = O and LargestSpotSize = H | D | 0.003480 |
| LargestSpotSize = K and SpotDistribution = C and Area = 1 | E | 0.001529 |
| LargestSpotSize = A and SpotDistribution = C and Area = 1 | E | 0.002043 |
| SpotDistribution = I and LargestSpotSize = K and Area = 2 | E | 0.001722 |
| SpotDistribution = I and LargestSpotSize = H | E | 0.001529 |
| SpotDistribution = I and LargestSpotSize = A and Evolution = 2 and C-class = 3 | E | 0.001529 |
| SpotDistribution = C and LargestSpotSize = H | E | 0.001147 |
| SpotDistribution = I and LargestSpotSize = A and Evolution = 2 and C-class = 8 | E | 0.001147 |
| SpotDistribution = O and LargestSpotSize = K | C | 0.001302 |
| LargestSpotSize = H and SpotDistribution = I and Area = 1 | D | 0.000450 |
| SpotDistribution = C and LargestSpotSize = R | E | 0.000574 |
| LargestSpotSize = R and SpotDistribution = C and Area = 1 | D | 0.000675 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = X | H | 0.308577 |
| LargestSpotSize = X | B | 0.198786 |
| SpotDistribution = C and LargestSpotSize = K | E | 0.016842 |
| SpotDistribution = O and C-class = 0 and LargestSpotSize = R and HistComplex = 1 and Evolution = 3 | C | 0.066801 |
| SpotDistribution = O and C-class = 0 and LargestSpotSize = R and HistComplex = 1 | C | 0.043863 |
| SpotDistribution = O and C-class = 0 and LargestSpotSize = A and HistComplex = 1 | D | 0.020919 |
| SpotDistribution = O and C-class = 0 and HistComplex = 1 and Evolution = 3 | C | 0.041918 |
| SpotDistribution = O and C-class = 0 and HistComplex = 1 and Activity = 1 | C | 0.017775 |
| SpotDistribution = O and C-class = 0 and HistComplex = 2 and Evolution = 2 and LargestSpotSize = S | C | 0.023709 |
| SpotDistribution = C | E | 0.005882 |
| SpotDistribution = O and C-class = 0 and HistComplex = 2 and Evolution = 2 and LargestSpotSize = A | C | 0.010390 |
| SpotDistribution = O and C-class = 0 and HistComplex = 2 and Evolution = 2 | C | 0.007823 |
| HistComplex = 1 and LargestSpotSize = A | D | 0.097659 |
| HistComplex = 1 and Activity = 2 | C | 0.017963 |
| HistComplex = 1 and C-class = 1 and LargestSpotSize = S | D | 0.026688 |
| HistComplex = 1 and LargestSpotSize = R | D | 0.179412 |
| C-class = 1 and SpotDistribution = I and Evolution = 2 | D | 0.020554 |
| C-class = 1 and Activity = 1 | D | 0.015180 |
| C-class = 0 and SpotDistribution = O and LargestSpotSize = S | D | 0.099672 |
| C-class = 0 and Evolution = 3 and LargestSpotSize = A and SpotDistribution = I | D | 0.049560 |
| C-class = 2 | D | 0.029377 |
| C-class = 0 and Evolution = 3 and LargestSpotSize = S | D | 0.026525 |
| C-class = 0 and LargestSpotSize = A and Evolution = 2 | D | 0.052980 |
| C-class = 0 and LargestSpotSize = R | D | 0.051587 |
| C-class = 0 and LargestSpotSize = A | D | 0.012598 |
| LargestSpotSize = A | E | 0.159845 |
| LargestSpotSize = S and Activity = 1 | D | 0.007090 |
| LargestSpotSize = S | E | 0.090221 |
| LargestSpotSize = K | D | 0.018414 |
|  | D | 0.127273 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| HistComplex = 2 and SpotDistribution = C | E | 0.010449 |
| LargestSpotSize = X | B | 0.139659 |
| SpotDistribution = O and C-class = 0 and HistComplex = 1 | C | 0.116193 |
| SpotDistribution = O and C-class = 0 and Evolution = 2 | C | 0.018673 |
| SpotDistribution = I and Evolution = 3 | D | 0.090881 |
| SpotDistribution = O and Evolution = 3 | D | 0.092425 |
| SpotDistribution = I and C-class = 0 | D | 0.020519 |
|  | H | 0.580709 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

largestspotsize|spotdistribution|area|class
---|---|---|---
a|c|2|h
k|c|2|e
k|i|2|e
a|i|2|h
h|c|1|h
r|o|2|h
r|c|1|d
k|c|1|e
a|c|1|e
h|i|1|d
s|i|1|d
k|i|1|d
r|i|1|d
x|i|1|b
a|i|1|d
h|o|1|d
x|o|1|b
k|o|1|h
a|o|1|d
r|o|1|c
s|o|1|c
k|x|1|h
h|x|1|h
r|x|1|h
s|x|1|h
a|x|1|h

## JRip

Decision list:

rules | predicted class
---|---
(HistComplex = 2) and (SpotDistribution = C)|E (28.0/12.0)
(LargestSpotSize = X)|B (131.0/0.0)
(SpotDistribution = O) and (C-class = 0) and (HistComplex = 1)|C (173.0/56.0)
(SpotDistribution = O) and (C-class = 0) and (Evolution = 2)|C (46.0/19.0)
(SpotDistribution = I) and (Evolution = 3)|D (106.0/38.0)
(SpotDistribution = O) and (Evolution = 3)|D (54.0/23.0)
(SpotDistribution = I) and (C-class = 0)|D (51.0/26.0)
|H (367.0/72.0)


## PART

Decision list:

rules | predicted class
---|---
SpotDistribution = X|H (295.0)
LargestSpotSize = X|B (131.0)
SpotDistribution = C AND LargestSpotSize = K|E (19.0/7.0)
SpotDistribution = O AND C-class = 0 AND LargestSpotSize = R AND HistComplex = 1 AND Evolution = 3|C (53.0/18.0)
SpotDistribution = O AND C-class = 0 AND LargestSpotSize = R AND HistComplex = 1|C (36.0/8.0)
SpotDistribution = O AND C-class = 0 AND LargestSpotSize = A AND HistComplex = 1|D (16.0/7.0)
SpotDistribution = O AND C-class = 0 AND HistComplex = 1 AND Evolution = 3|C (37.0/13.0)
SpotDistribution = O AND C-class = 0 AND HistComplex = 1 AND Activity = 1|C (21.0/6.0)
SpotDistribution = O AND C-class = 0 AND HistComplex = 2 AND Evolution = 2 AND LargestSpotSize = S|C (22.0/9.0)
SpotDistribution = C|E (13.0/7.0)
SpotDistribution = O AND C-class = 0 AND HistComplex = 2 AND Evolution = 2 AND LargestSpotSize = A|C (11.0/5.0)
SpotDistribution = O AND C-class = 0 AND HistComplex = 2 AND Evolution = 2|C (13.0/5.0)
HistComplex = 1 AND LargestSpotSize = A|D (27.0/6.0)
HistComplex = 1 AND Activity = 2|C (15.0/5.0)
HistComplex = 1 AND C-class = 1 AND LargestSpotSize = S|D (11.0/5.0)
HistComplex = 1 AND LargestSpotSize = R|D (21.0/9.0)
C-class = 1 AND SpotDistribution = I AND Evolution = 2|D (16.0/9.0)
C-class = 1 AND Activity = 1|D (16.0/8.0)
C-class = 0 AND SpotDistribution = O AND LargestSpotSize = S|D (18.0/9.0)
C-class = 0 AND Evolution = 3 AND LargestSpotSize = A AND SpotDistribution = I|D (20.0/7.0)
C-class = 2|D (18.0/8.0)
C-class = 0 AND Evolution = 3 AND LargestSpotSize = S|D (16.0/7.0)
C-class = 0 AND LargestSpotSize = A AND Evolution = 2|D (25.0/14.0)
C-class = 0 AND LargestSpotSize = R|D (15.0/4.0)
C-class = 0 AND LargestSpotSize = A|D (14.0/7.0)
LargestSpotSize = A|E (15.0/5.0)
LargestSpotSize = S AND Activity = 1|D (11.0/6.0)
LargestSpotSize = S|E (10.0/6.0)
LargestSpotSize = K|D (10.0/5.0)
|D (11.0/5.0)


## J48 Decision Tree

* SpotDistribution = X: H (197.0)
* SpotDistribution = O
	* LargestSpotSize = A
		* C-class = 0
			* Activity = 1: C (20.0/10.0)
			* Activity = 2: D (5.0/2.0)
		* C-class = 1: E (3.0/1.0)
		* C-class = 2: D (3.0/1.0)
		* C-class = 3: E (1.0)
		* C-class = 4: E (1.0)
		* C-class = 5: D (0.0)
		* C-class = 6: D (0.0)
		* C-class = 7: D (0.0)
		* C-class = 8: D (0.0)
	* LargestSpotSize = R
		* C-class = 0: C (64.0/19.0)
		* C-class = 1: D (6.0/2.0)
		* C-class = 2: C (0.0)
		* C-class = 3: C (0.0)
		* C-class = 4: C (0.0)
		* C-class = 5: C (0.0)
		* C-class = 6: C (0.0)
		* C-class = 7: C (0.0)
		* C-class = 8: C (0.0)
	* LargestSpotSize = S
		* C-class = 0: C (73.0/27.0)
		* C-class = 1: D (7.0/3.0)
		* C-class = 2: D (3.0/1.0)
		* C-class = 3: D (2.0/1.0)
		* C-class = 4: C (0.0)
		* C-class = 5: C (0.0)
		* C-class = 6: C (0.0)
		* C-class = 7: C (0.0)
		* C-class = 8: C (0.0)
	* LargestSpotSize = X: B (76.0)
	* LargestSpotSize = K: C (0.0)
	* LargestSpotSize = H: D (11.0/8.0)
* SpotDistribution = I
	* LargestSpotSize = A
		* Evolution = 1: D (1.0)
		* Evolution = 2
			* C-class = 0: D (22.0/10.0)
			* C-class = 1: D (7.0/4.0)
			* C-class = 2: D (2.0/1.0)
			* C-class = 3: E (2.0/1.0)
			* C-class = 4: D (1.0)
			* C-class = 5: D (0.0)
			* C-class = 6: D (0.0)
			* C-class = 7: D (0.0)
			* C-class = 8: E (1.0)
		* Evolution = 3: D (38.0/12.0)
	* LargestSpotSize = R: D (20.0/8.0)
	* LargestSpotSize = S: D (23.0/14.0)
	* LargestSpotSize = X: B (11.0)
	* LargestSpotSize = K
		* Area = 1: D (12.0/1.0)
		* Area = 2: E (4.0/2.0)
	* LargestSpotSize = H: E (3.0/1.0)
* SpotDistribution = C
	* LargestSpotSize = A: E (6.0/3.0)
	* LargestSpotSize = R: E (1.0)
	* LargestSpotSize = S: E (0.0)
	* LargestSpotSize = X: E (0.0)
	* LargestSpotSize = K
		* Prev24Hour = 1
			* M-class = 0: F (3.0/1.0)
			* M-class = 1: E (3.0/1.0)
			* M-class = 2: E (0.0)
			* M-class = 3: E (0.0)
			* M-class = 4: E (0.0)
			* M-class = 5: E (0.0)
		* Prev24Hour = 2: E (0.0)
		* Prev24Hour = 3: E (5.0/1.0)
	* LargestSpotSize = H: E (1.0)


## SimpleCart Decision Tree

		* SpotDistribution=(C)|(I)|(O)
	* LargestSpotSize=(X): B(131.0/0.0)
	* LargestSpotSize!=(X)
			* SpotDistribution=(C)|(I)
			* Area=(2): E(13.0/11.0)
			* Area!=(2)
				* HistComplex=(2)
					* Evolution=(3): D(38.0/23.0)
					* Evolution!=(3)
									* C-class=(0)|(6)|(7)|(8): D(23.0/26.0)
									* C-class!=(0)|(6)|(7)|(8)
											* C-class=(1)|(0)|(6)|(7)|(8): D(8.0/8.0)
											* C-class!=(1)|(0)|(6)|(7)|(8): F(6.0/8.0)
				* HistComplex!=(2): D(37.0/19.0)
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


