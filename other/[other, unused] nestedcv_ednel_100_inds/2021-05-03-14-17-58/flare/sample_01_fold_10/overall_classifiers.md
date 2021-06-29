# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | H | 0.311390 |
| SpotDistribution = O and LargestSpotSize!=(X) and SpotDistribution != I and LargestSpotSize != X and C-class != 1 and Activity!=(2) and LargestSpotSize!=(H) | C | 0.112688 |
| LargestSpotSize = X and SpotDistribution = O and Area = 1 and X-class = 0 | B | 0.121148 |
| LargestSpotSize = A and SpotDistribution = I and Area = 1 and X-class = 0 | D | 0.041956 |
| LargestSpotSize = A and SpotDistribution = O and Area = 1 and X-class = 0 | D | 0.012458 |
| LargestSpotSize = R and SpotDistribution = I and Area = 1 and X-class = 0 | D | 0.015979 |
| LargestSpotSize = S and SpotDistribution = I and Area = 1 and X-class = 0 | D | 0.012492 |
| LargestSpotSize = X and SpotDistribution = I and Area = 1 and X-class = 0 | B | 0.016647 |
| LargestSpotSize = K and SpotDistribution = I and Area = 1 and X-class = 0 | D | 0.010270 |
| LargestSpotSize = K and SpotDistribution = C and Area = 2 and X-class = 0 | E | 0.006088 |
| LargestSpotSize = H and SpotDistribution = O and Area = 1 and X-class = 0 | D | 0.005073 |
| LargestSpotSize = A and SpotDistribution = C and Area = 1 and X-class = 0 | D | 0.002695 |
| LargestSpotSize = A and SpotDistribution = I and Area = 2 and X-class = 0 | F | 0.002174 |
| LargestSpotSize = R and SpotDistribution = C and Area = 1 and X-class = 0 | D | 0.001795 |
| LargestSpotSize = K and SpotDistribution = C and Area = 2 and X-class = 1 | E | 0.001527 |
| LargestSpotSize = H and SpotDistribution = I and Area = 1 and X-class = 0 | E | 0.001527 |
| LargestSpotSize = K and SpotDistribution = C and Area = 1 and X-class = 0 | E | 0.001527 |
| LargestSpotSize = K and SpotDistribution = I and Area = 2 and X-class = 0 | F | 0.001634 |
| LargestSpotSize = S and SpotDistribution = O and Area = 1 and X-class = 0 | C | 0.054007 |
| SpotDistribution = O and LargestSpotSize!=(X) and SpotDistribution != I and LargestSpotSize != X and C-class = 1 and Evolution!=(3) and Activity!=(2) and C-class != 4 | E | 0.000590 |
| LargestSpotSize = R and SpotDistribution = O and Area = 1 and X-class = 0 | C | 0.063418 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = X | H | 0.311390 |
| LargestSpotSize = X | B | 0.194825 |
| Area != 1 and Prev24Hour = 1 | F | 0.011884 |
| SpotDistribution = C and LargestSpotSize = K | E | 0.021573 |
| SpotDistribution = O and LargestSpotSize != A and LargestSpotSize != H and C-class != 1 | C | 0.235520 |
| HistComplex = 1 and Activity = 1 and LargestSpotSize != A | D | 0.243544 |
| SpotDistribution != O and HistComplex != 1 and LargestSpotSize != R and M-class = 0 and LargestSpotSize != K and Evolution = 3 | D | 0.068182 |
| SpotDistribution != O and Evolution != 3 and C-class = 0 | D | 0.093067 |
| SpotDistribution != O and Evolution != 2 | D | 0.122346 |
| SpotDistribution = O and LargestSpotSize != H and LargestSpotSize = A and C-class = 0 and Evolution != 2 | D | 0.043613 |
| SpotDistribution = O and Evolution != 3 and Activity = 1 and C-class = 0 | C | 0.013853 |
| SpotDistribution = O and LargestSpotSize != S and Evolution != 3 | E | 0.052599 |
| SpotDistribution != O | F | 0.065810 |
|  | D | 0.305195 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| HistComplex = 2 and SpotDistribution = C | E | 0.010089 |
| LargestSpotSize = X | B | 0.136315 |
| SpotDistribution = O and HistComplex = 1 | C | 0.116085 |
| SpotDistribution = O and LargestSpotSize = S and C-class = 0 | C | 0.011225 |
| SpotDistribution = O and LargestSpotSize = R and Evolution = 2 | C | 0.006854 |
| SpotDistribution = I | D | 0.123602 |
|  | H | 0.536937 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

largestspotsize|spotdistribution|area|x-class|class
---|---|---|---|---
k|c|2|2|h
k|c|2|1|e
a|c|2|0|h
k|c|2|0|e
a|i|2|0|f
k|i|2|0|f
h|c|1|0|h
k|c|1|0|e
r|o|2|0|h
a|c|1|0|d
r|c|1|0|d
h|i|1|0|e
x|i|1|0|b
k|i|1|0|d
a|i|1|0|d
s|i|1|0|d
r|i|1|0|d
k|o|1|0|h
x|o|1|0|b
h|o|1|0|d
a|o|1|0|d
s|o|1|0|c
r|o|1|0|c
k|x|1|0|h
h|x|1|0|h
r|x|1|0|h
s|x|1|0|h
a|x|1|0|h

## JRip

Decision list:

rules | predicted class
---|---
(HistComplex = 2) and (SpotDistribution = C)|E (29.0/13.0)
(LargestSpotSize = X)|B (128.0/0.0)
(SpotDistribution = O) and (HistComplex = 1)|C (200.0/75.0)
(SpotDistribution = O) and (LargestSpotSize = S) and (C-class = 0)|C (37.0/17.0)
(SpotDistribution = O) and (LargestSpotSize = R) and (Evolution = 2)|C (12.0/3.0)
(SpotDistribution = I)|D (189.0/85.0)
|H (362.0/64.0)


## PART

Decision list:

rules | predicted class
---|---
SpotDistribution = X|H (298.0)
LargestSpotSize = X|B (128.0)
Area != 1 AND Prev24Hour = 1|F (17.0/7.0)
SpotDistribution = C AND LargestSpotSize = K|E (12.0/2.0)
SpotDistribution = O AND LargestSpotSize != A AND LargestSpotSize != H AND C-class != 1|C (218.0/78.0)
HistComplex = 1 AND Activity = 1 AND LargestSpotSize != A|D (46.0/21.0)
SpotDistribution != O AND HistComplex != 1 AND LargestSpotSize != R AND M-class = 0 AND LargestSpotSize != K AND Evolution = 3|D (42.0/21.0)
SpotDistribution != O AND Evolution != 3 AND C-class = 0|D (52.0/24.0)
SpotDistribution != O AND Evolution != 2|D (46.0/8.0)
SpotDistribution = O AND LargestSpotSize != H AND LargestSpotSize = A AND C-class = 0 AND Evolution != 2|D (25.0/12.0)
SpotDistribution = O AND Evolution != 3 AND Activity = 1 AND C-class = 0|C (15.0/8.0)
SpotDistribution = O AND LargestSpotSize != S AND Evolution != 3|E (15.0/5.0)
SpotDistribution != O|F (25.0/15.0)
|D (18.0/7.0)


## SimpleCart Decision Tree

		* SpotDistribution=(C)|(I)|(O)
	* LargestSpotSize=(X): B(128.0/0.0)
	* LargestSpotSize!=(X)
			* SpotDistribution=(C)|(I)
			* Area=(2)
					* Prev24Hour=(3)|(2)
					* C-class=(1): E(1.0/1.0)
					* C-class!=(1): E(7.0/0.0)
					* Prev24Hour!=(3)|(2): F(10.0/6.0)
			* Area!=(2)
				* HistComplex=(2)
					* Evolution=(3)
							* LargestSpotSize=(K)|(R)
							* SpotDistribution=(C): D(1.0/1.0)
							* SpotDistribution!=(C): D(13.0/0.0)
							* LargestSpotSize!=(K)|(R)
									* C-class=(6)|(5)|(4): E(3.0/0.0)
									* C-class!=(6)|(5)|(4)
								* LargestSpotSize=(S): D(4.0/4.0)
								* LargestSpotSize!=(S)
									* LargestSpotSize=(H)
										* Activity=(2): D(1.0/1.0)
										* Activity!=(2): E(2.0/0.0)
									* LargestSpotSize!=(H)
										* M-class=(1): D(3.0/0.0)
										* M-class!=(1)
												* C-class=(3)|(2): D(5.0/2.0)
												* C-class!=(3)|(2): D(11.0/12.0)
					* Evolution!=(3)
							* C-class=(4)|(2)
								* LargestSpotSize=(K)|(S): F(2.0/0.0)
								* LargestSpotSize!=(K)|(S)
								* Activity=(2): D(1.0/1.0)
								* Activity!=(2): F(2.0/1.0)
							* C-class!=(4)|(2)
								* C-class=(5)|(3): E(4.0/2.0)
								* C-class!=(5)|(3)
									* M-class=(3)|(1): D(3.0/0.0)
									* M-class!=(3)|(1)
									* LargestSpotSize=(R)
										* C-class=(1): C(1.0/1.0)
										* C-class!=(1): D(4.0/1.0)
									* LargestSpotSize!=(R)
										* Activity=(2)
											* SpotDistribution=(C): E(2.0/2.0)
											* SpotDistribution!=(C)
												* C-class=(1): D(3.0/1.0)
												* C-class!=(1)
													* LargestSpotSize=(S): D(1.0/3.0)
													* LargestSpotSize!=(S)
														* LargestSpotSize=(K): D(2.0/1.0)
														* LargestSpotSize!=(K)
															* Prev24Hour=(3): D(1.0/1.0)
															* Prev24Hour!=(3): F(3.0/3.0)
										* Activity!=(2)
												* LargestSpotSize=(K)|(S): E(4.0/3.0)
												* LargestSpotSize!=(K)|(S): D(10.0/12.0)
				* HistComplex!=(2)
									* LargestSpotSize=(S)|(R)|(X)|(K)|(H)
						* Activity=(2)
							* SpotDistribution=(C): D(1.0/1.0)
							* SpotDistribution!=(C): D(3.0/0.0)
						* Activity!=(2)
								* Evolution=(3)|(1)
									* C-class=(2)|(1)
									* LargestSpotSize=(S): D(2.0/2.0)
									* LargestSpotSize!=(S)
										* C-class=(2): D(1.0/1.0)
										* C-class!=(2): D(2.0/1.0)
									* C-class!=(2)|(1)
													* LargestSpotSize=(S)|(A)|(X)|(K)|(H): D(6.0/4.0)
													* LargestSpotSize!=(S)|(A)|(X)|(K)|(H): D(4.0/2.0)
								* Evolution!=(3)|(1): C(3.0/0.0)
									* LargestSpotSize!=(S)|(R)|(X)|(K)|(H): D(21.0/4.0)
			* SpotDistribution!=(C)|(I)
						* LargestSpotSize=(K)|(S)|(R)|(X)
						* C-class=(6)|(2)|(1): D(16.0/15.0)
						* C-class!=(6)|(2)|(1)
					* HistComplex=(2): C(30.0/26.0)
					* HistComplex!=(2)
						* Evolution=(3)
							* Prev24Hour=(3): C(1.0/1.0)
							* Prev24Hour!=(3)
								* Activity=(2): C(2.0/0.0)
								* Activity!=(2)
										* C-class=(5)|(3): C(2.0/0.0)
										* C-class!=(5)|(3)
										* LargestSpotSize=(S): C(19.0/13.0)
										* LargestSpotSize!=(S)
											* M-class=(1): D(1.0/1.0)
											* M-class!=(1): C(34.0/19.0)
						* Evolution!=(3)
							* LargestSpotSize=(S)
								* C-class=(3): D(1.0/1.0)
								* C-class!=(3)
									* Prev24Hour=(2): C(2.0/0.0)
									* Prev24Hour!=(2)
										* Activity=(2): C(5.0/2.0)
										* Activity!=(2)
												* Evolution=(2)|(3): C(13.0/5.0)
												* Evolution!=(2)|(3): D(1.0/1.0)
							* LargestSpotSize!=(S): C(27.0/6.0)
						* LargestSpotSize!=(K)|(S)|(R)|(X)
						* C-class=(4)|(3)|(1)
					* Evolution=(3): D(1.0/1.0)
					* Evolution!=(3)
						* Activity=(2): E(3.0/0.0)
						* Activity!=(2)
								* C-class=(4)|(3): E(2.0/0.0)
								* C-class!=(4)|(3): E(2.0/1.0)
						* C-class!=(4)|(3)|(1)
					* Activity=(2)
						* HistComplex=(2)
							* Prev24Hour=(3): D(2.0/1.0)
							* Prev24Hour!=(3): E(4.0/0.0)
						* HistComplex!=(2): D(3.0/0.0)
					* Activity!=(2)
						* LargestSpotSize=(H)
							* HistComplex=(2)
									* Evolution=(3)|(1): D(4.0/2.0)
									* Evolution!=(3)|(1): D(2.0/0.0)
							* HistComplex!=(2): D(1.0/1.0)
						* LargestSpotSize!=(H): C(16.0/20.0)
		* SpotDistribution!=(C)|(I)|(O): H(298.0/0.0)


