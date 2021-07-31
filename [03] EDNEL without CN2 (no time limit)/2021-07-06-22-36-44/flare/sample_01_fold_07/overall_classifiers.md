# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = X | H | 0.311390 |
| SpotDistribution != X and LargestSpotSize = X | B | 0.134031 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and LargestSpotSize != A and SpotDistribution != C and LargestSpotSize != H and LargestSpotSize != K and SpotDistribution = O and Activity = 1 and LargestSpotSize = R | C | 0.065944 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and LargestSpotSize = A | D | 0.057180 |
| SpotDistribution = O and LargestSpotSize!=(X) and SpotDistribution != I and LargestSpotSize != X and Activity!=(2) and C-class = 0 | D | 0.042522 |
| LargestSpotSize = S and SpotDistribution = O and HistComplex = 1 and Area = 1 and X-class = 0 | C | 0.042840 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and LargestSpotSize != A and SpotDistribution != C and LargestSpotSize != H and LargestSpotSize != K and SpotDistribution != O | D | 0.024880 |
| SpotDistribution = O and LargestSpotSize!=(X) and SpotDistribution != I and LargestSpotSize != X and Activity!=(2) and C-class != 7 | E | 0.004631 |
| LargestSpotSize = K and SpotDistribution = I and HistComplex = 2 and Area = 1 and X-class = 0 | D | 0.012783 |
| SpotDistribution != X and LargestSpotSize != X and Area != 1 | E | 0.007172 |
| SpotDistribution = O and LargestSpotSize!=(X) and SpotDistribution != I and LargestSpotSize != X and Activity!=(2) and C-class = 1 | D | 0.009636 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and LargestSpotSize != A and SpotDistribution != C and LargestSpotSize != H and LargestSpotSize != K and SpotDistribution = O and Activity != 1 | C | 0.014435 |
| LargestSpotSize = S and SpotDistribution = I and HistComplex = 2 and Area = 1 and X-class = 0 | E | 0.003897 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and LargestSpotSize != A and SpotDistribution = C and C-class = 0 | E | 0.004566 |
| LargestSpotSize = A and SpotDistribution = I and HistComplex = 2 and Area = 2 and X-class = 0 | F | 0.002174 |
| LargestSpotSize = H and SpotDistribution = O and HistComplex = 1 and Area = 1 and X-class = 0 | C | 0.001736 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and LargestSpotSize != A and SpotDistribution != C and LargestSpotSize = H and C-class != 0 | E | 0.003051 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and LargestSpotSize != A and SpotDistribution = C and C-class != 0 | D | 0.001795 |
| LargestSpotSize = H and SpotDistribution = I and HistComplex = 2 and Area = 1 and X-class = 0 | D | 0.000450 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and LargestSpotSize != A and SpotDistribution != C and LargestSpotSize != H and LargestSpotSize != K and SpotDistribution = O and Activity = 1 and LargestSpotSize != R and HistComplex = 1 and Evolution != 2 and C-class != 0 | D | 0.002022 |
| LargestSpotSize = S and SpotDistribution = O and HistComplex = 2 and Area = 1 and X-class = 0 | D | 0.014893 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = X | H | 0.311390 |
| LargestSpotSize = X | B | 0.194825 |
| SpotDistribution = O and LargestSpotSize = R | C | 0.142196 |
| SpotDistribution = O and LargestSpotSize = S and C-class = 0 and HistComplex = 1 | C | 0.085254 |
| Area = 1 and SpotDistribution = I and HistComplex = 2 and Evolution = 3 | D | 0.119877 |
| Area = 1 and SpotDistribution = O and LargestSpotSize = S | D | 0.113297 |
| Area = 1 and HistComplex = 1 | D | 0.214866 |
| Area = 1 and SpotDistribution = O and C-class = 0 | D | 0.031255 |
| Area = 1 and SpotDistribution = I and C-class = 0 | D | 0.031672 |
| Area = 2 | E | 0.049689 |
| LargestSpotSize = A and SpotDistribution = I | D | 0.007040 |
|  | E | 0.382199 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = I and Area = 2 | F | 0.003397 |
| Activity = 2 and SpotDistribution = C | E | 0.008446 |
| HistComplex = 2 and Activity = 2 and SpotDistribution = O and Prev24Hour = 1 | E | 0.005826 |
| LargestSpotSize = X | B | 0.137931 |
| SpotDistribution = O and HistComplex = 1 | C | 0.126669 |
| SpotDistribution = O and C-class = 0 and Evolution = 2 | C | 0.016801 |
| SpotDistribution = I | D | 0.128820 |
| SpotDistribution = O and C-class = 0 | D | 0.130406 |
|  | H | 0.652079 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

largestspotsize|spotdistribution|histcomplex|area|x-class|class
---|---|---|---|---|---
k|c|2|2|2|h
k|c|2|2|1|e
a|i|2|1|1|h
a|c|2|2|0|h
k|c|2|2|0|e
a|i|2|2|0|f
k|i|2|2|0|e
r|c|2|1|0|h
k|c|2|1|0|e
h|c|2|1|0|h
a|c|2|1|0|d
h|i|2|1|0|d
x|i|2|1|0|b
r|i|2|1|0|d
s|i|2|1|0|e
k|i|2|1|0|d
a|i|2|1|0|d
a|c|1|1|0|h
r|c|1|1|0|d
r|o|2|1|0|c
x|o|2|1|0|b
s|o|2|1|0|d
h|o|2|1|0|d
a|o|2|1|0|e
h|x|2|1|0|h
r|i|1|1|0|d
r|x|2|1|0|h
x|i|1|1|0|b
s|i|1|1|0|d
a|i|1|1|0|d
a|x|2|1|0|h
s|x|2|1|0|h
h|o|1|1|0|c
k|o|1|1|0|h
x|o|1|1|0|b
s|o|1|1|0|c
a|o|1|1|0|d
r|o|1|1|0|c
k|x|1|1|0|h
h|x|1|1|0|h
r|x|1|1|0|h
a|x|1|1|0|h
s|x|1|1|0|h

## JRip

Decision list:

rules | predicted class
---|---
(SpotDistribution = I) and (Area = 2)|F (8.0/3.0)
(Activity = 2) and (SpotDistribution = C)|E (23.0/10.0)
(HistComplex = 2) and (Activity = 2) and (SpotDistribution = O) and (Prev24Hour = 1)|E (16.0/7.0)
(LargestSpotSize = X)|B (126.0/0.0)
(SpotDistribution = O) and (HistComplex = 1)|C (205.0/73.0)
(SpotDistribution = O) and (C-class = 0) and (Evolution = 2)|C (44.0/20.0)
(SpotDistribution = I)|D (178.0/75.0)
(SpotDistribution = O) and (C-class = 0)|D (33.0/13.0)
|H (324.0/26.0)


## PART

Decision list:

rules | predicted class
---|---
SpotDistribution = X|H (298.0)
LargestSpotSize = X|B (128.0)
SpotDistribution = O AND LargestSpotSize = R|C (114.0/35.0)
SpotDistribution = O AND LargestSpotSize = S AND C-class = 0 AND HistComplex = 1|C (68.0/22.0)
Area = 1 AND SpotDistribution = I AND HistComplex = 2 AND Evolution = 3|D (61.0/22.0)
Area = 1 AND SpotDistribution = O AND LargestSpotSize = S|D (63.0/34.0)
Area = 1 AND HistComplex = 1|D (80.0/32.0)
Area = 1 AND SpotDistribution = O AND C-class = 0|D (32.0/18.0)
Area = 1 AND SpotDistribution = I AND C-class = 0|D (40.0/22.0)
Area = 2|E (23.0/11.0)
LargestSpotSize = A AND SpotDistribution = I|D (15.0/8.0)
|E (35.0/18.0)


## J48 Decision Tree

* SpotDistribution = X: H (199.0)
* SpotDistribution != X
	* LargestSpotSize = X: B (86.0)
	* LargestSpotSize != X
		* Area = 1
			* LargestSpotSize = A: D (104.0/50.0)
			* LargestSpotSize != A
				* SpotDistribution = C
					* C-class = 0: E (3.0)
					* C-class != 0: D (2.0/1.0)
				* SpotDistribution != C
					* LargestSpotSize = H
						* C-class = 0: D (4.0/1.0)
						* C-class != 0: E (6.0/2.0)
					* LargestSpotSize != H
						* LargestSpotSize = K: D (13.0/4.0)
						* LargestSpotSize != K
							* SpotDistribution = O
								* Activity = 1
									* LargestSpotSize = R: C (74.0/22.0)
									* LargestSpotSize != R
										* HistComplex = 1
											* Evolution = 2: C (17.0/5.0)
											* Evolution != 2
												* C-class = 0: C (23.0/9.0)
												* C-class != 0: D (5.0/3.0)
										* HistComplex != 1: D (29.0/15.0)
								* Activity != 1: C (17.0/8.0)
							* SpotDistribution != O: D (39.0/18.0)
		* Area != 1: E (17.0/9.0)


## SimpleCart Decision Tree

		* SpotDistribution=(C)|(I)|(O)
	* LargestSpotSize=(X): B(128.0/0.0)
	* LargestSpotSize!=(X)
			* SpotDistribution=(C)|(I)
			* Area=(2)
								* LargestSpotSize=(K)|(R)|(S)|(X)|(H): E(12.0/8.0)
								* LargestSpotSize!=(K)|(R)|(S)|(X)|(H): F(3.0/0.0)
			* Area!=(2)
				* Evolution=(3)
						* LargestSpotSize=(S)|(R)
						* HistComplex=(2)
											* LargestSpotSize=(S)|(A)|(X)|(K)|(H)
								* Activity=(2): E(2.0/1.0)
								* Activity!=(2): D(4.0/4.0)
											* LargestSpotSize!=(S)|(A)|(X)|(K)|(H)
								* Activity=(2): D(2.0/0.0)
								* Activity!=(2): D(5.0/1.0)
						* HistComplex!=(2)
							* SpotDistribution=(C): D(1.0/1.0)
							* SpotDistribution!=(C): D(15.0/10.0)
						* LargestSpotSize!=(S)|(R)
						* SpotDistribution=(C)
							* Activity=(2): D(1.0/1.0)
							* Activity!=(2): E(3.0/0.0)
						* SpotDistribution!=(C)
							* LargestSpotSize=(K): D(8.0/0.0)
							* LargestSpotSize!=(K)
								* HistComplex=(2)
													* C-class=(0)|(5)|(6)|(7)|(8)
										* M-class=(1): D(3.0/0.0)
										* M-class!=(1): D(10.0/7.0)
													* C-class!=(0)|(5)|(6)|(7)|(8)
										* LargestSpotSize=(H): E(2.0/0.0)
										* LargestSpotSize!=(H)
											* Activity=(2)
																		* C-class=(3)|(2)|(0)|(5)|(6)|(7)|(8): D(2.0/1.0)
																		* C-class!=(3)|(2)|(0)|(5)|(6)|(7)|(8): E(3.0/0.0)
											* Activity!=(2): D(5.0/2.0)
								* HistComplex!=(2)
									* C-class=(2): D(1.0/1.0)
									* C-class!=(2)
										* Activity=(2): D(4.0/0.0)
										* Activity!=(2)
												* M-class=(2)|(1): D(3.0/0.0)
												* M-class!=(2)|(1): D(8.0/2.0)
				* Evolution!=(3)
									* C-class=(0)|(1)|(5)|(6)|(7)
						* LargestSpotSize=(S): E(5.0/7.0)
						* LargestSpotSize!=(S)
							* HistComplex=(2)
								* SpotDistribution=(C): E(3.0/3.0)
								* SpotDistribution!=(C): D(21.0/19.0)
							* HistComplex!=(2)
								* LargestSpotSize=(R): D(1.0/1.0)
								* LargestSpotSize!=(R): D(4.0/0.0)
									* C-class!=(0)|(1)|(5)|(6)|(7)
							* C-class=(8)|(3): E(4.0/2.0)
							* C-class!=(8)|(3): F(6.0/4.0)
			* SpotDistribution!=(C)|(I)
					* LargestSpotSize=(S)|(R)|(X)
				* HistComplex=(2)
					* Evolution=(2)
										* LargestSpotSize=(S)|(A)|(X)|(K)|(H): D(13.0/15.0)
										* LargestSpotSize!=(S)|(A)|(X)|(K)|(H): C(9.0/3.0)
					* Evolution!=(2): D(13.0/11.0)
				* HistComplex!=(2)
								* C-class=(0)|(4)|(7)|(8)
						* Evolution=(3)
							* Prev24Hour=(3): C(1.0/1.0)
							* Prev24Hour!=(3): C(58.0/31.0)
						* Evolution!=(3)
							* LargestSpotSize=(S)
									* Evolution=(2)|(3)
									* Activity=(2)
										* Prev24Hour=(2): C(2.0/0.0)
										* Prev24Hour!=(2): C(5.0/2.0)
									* Activity!=(2): C(16.0/5.0)
									* Evolution!=(2)|(3): C(2.0/1.0)
							* LargestSpotSize!=(S)
								* Activity=(2): C(2.0/0.0)
								* Activity!=(2)
										* Evolution=(2)|(3): C(21.0/6.0)
										* Evolution!=(2)|(3): C(4.0/1.0)
								* C-class!=(0)|(4)|(7)|(8): C(11.0/12.0)
					* LargestSpotSize!=(S)|(R)|(X)
				* Activity=(2)
					* HistComplex=(2)
						* Prev24Hour=(3): D(2.0/1.0)
						* Prev24Hour!=(3): E(8.0/0.0)
					* HistComplex!=(2): D(3.0/0.0)
				* Activity!=(2)
											* C-class=(0)|(1)|(2)|(5)|(6)|(7)|(8): D(24.0/30.0)
											* C-class!=(0)|(1)|(2)|(5)|(6)|(7)|(8): E(2.0/0.0)
		* SpotDistribution!=(C)|(I)|(O): H(298.0/0.0)


