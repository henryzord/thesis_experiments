# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | H | 0.309549 |
| SpotDistribution != X and LargestSpotSize = X | B | 0.134595 |
| SpotDistribution = O and LargestSpotSize!=(X) and SpotDistribution != I and C-class != 1 and LargestSpotSize != X | D | 0.044660 |
| LargestSpotSize = R and SpotDistribution = O and BecomeHist = 2 | C | 0.062146 |
| LargestSpotSize = S and SpotDistribution = O and BecomeHist = 2 | C | 0.053239 |
| LargestSpotSize = A and SpotDistribution = I and BecomeHist = 2 | D | 0.044615 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution != O and LargestSpotSize = R | D | 0.015511 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution = O and LargestSpotSize != H and C-class != 0 and LargestSpotSize != A | D | 0.012204 |
| LargestSpotSize = K and SpotDistribution = C and BecomeHist = 2 | E | 0.008681 |
| LargestSpotSize = S and SpotDistribution = I and BecomeHist = 2 | D | 0.010361 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution = O and LargestSpotSize != H and C-class != 0 and LargestSpotSize = A and Evolution = 2 | E | 0.005161 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution != O and LargestSpotSize != R and HistComplex != 1 and M-class = 0 and Evolution = 3 and LargestSpotSize = K | D | 0.009396 |
| SpotDistribution != X and LargestSpotSize != X and Area != 1 and Prev24Hour = 1 | F | 0.005207 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution != O and LargestSpotSize != R and HistComplex != 1 and M-class = 0 and Evolution = 3 and LargestSpotSize != K and LargestSpotSize != S and Activity != 1 and C-class != 0 | E | 0.003065 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution != O and LargestSpotSize != R and HistComplex != 1 and M-class = 0 and Evolution != 3 and C-class = 0 and LargestSpotSize = S | E | 0.003197 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution = O and LargestSpotSize != H and C-class = 0 and HistComplex != 1 and Evolution != 1 and Evolution = 2 | C | 0.021406 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution != O and LargestSpotSize != R and HistComplex != 1 and M-class = 0 and Evolution != 3 and C-class != 0 and C-class != 1 | F | 0.002820 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution = O and LargestSpotSize = H and Evolution = 2 | E | 0.001728 |
| LargestSpotSize = A and SpotDistribution = C and BecomeHist = 2 | D | 0.002174 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution = O and LargestSpotSize != H and C-class != 0 and LargestSpotSize = A and Evolution != 2 | D | 0.003604 |
| LargestSpotSize = K and SpotDistribution = I and BecomeHist = 2 | D | 0.007797 |
| SpotDistribution = O and LargestSpotSize!=(X) and SpotDistribution != I and C-class != 1 and LargestSpotSize = K and HistComplex!=(2) and Evolution!=(3) and LargestSpotSize!=(S) and Activity!=(2) and Evolution = 2 | C | 0.001307 |
| LargestSpotSize = H and SpotDistribution = I and BecomeHist = 2 | D | 0.000452 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = X | H | 0.309549 |
| LargestSpotSize = X | B | 0.195122 |
| SpotDistribution = O and C-class = 0 and HistComplex = 1 and LargestSpotSize = R | C | 0.117978 |
| Area = 1 and SpotDistribution = I | D | 0.214182 |
| Area = 1 and C-class = 0 and Evolution = 3 and HistComplex = 1 | C | 0.064263 |
| Area = 1 and LargestSpotSize = S | C | 0.106790 |
| Area = 1 | D | 0.359755 |
|  | E | 0.512048 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = I and HistComplex = 2 and Area = 2 | F | 0.002498 |
| HistComplex = 2 and Activity = 2 and SpotDistribution = C | E | 0.009806 |
| LargestSpotSize = A and C-class = 3 | E | 0.003211 |
| LargestSpotSize = X | B | 0.137931 |
| SpotDistribution = O and HistComplex = 1 and C-class = 0 | C | 0.117399 |
| SpotDistribution = O and Evolution = 2 and C-class = 0 | C | 0.018890 |
| SpotDistribution = I | D | 0.127142 |
| SpotDistribution = O and Evolution = 3 | D | 0.093773 |
|  | H | 0.602041 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

largestspotsize|spotdistribution|becomehist|class
---|---|---|---
r|c|2|d
h|c|2|h
a|c|2|d
k|c|2|e
k|i|2|d
h|i|2|d
x|i|2|b
s|i|2|d
r|i|2|d
a|i|2|d
k|o|2|h
x|o|2|b
a|o|2|d
r|o|2|c
h|o|2|d
s|o|2|c
h|x|2|h
a|x|2|h
s|x|2|h
r|x|2|h
h|x|1|h
k|x|1|h
a|x|1|h
r|x|1|h
s|x|1|h

## JRip

Decision list:

rules | predicted class
---|---
(SpotDistribution = I) and (HistComplex = 2) and (Area = 2)|F (7.0/3.0)
(HistComplex = 2) and (Activity = 2) and (SpotDistribution = C)|E (23.0/9.0)
(LargestSpotSize = A) and (C-class = 3)|E (9.0/4.0)
(LargestSpotSize = X)|B (128.0/0.0)
(SpotDistribution = O) and (HistComplex = 1) and (C-class = 0)|C (173.0/56.0)
(SpotDistribution = O) and (Evolution = 2) and (C-class = 0)|C (46.0/19.0)
(SpotDistribution = I)|D (174.0/73.0)
(SpotDistribution = O) and (Evolution = 3)|D (54.0/23.0)
|H (339.0/44.0)


## PART

Decision list:

rules | predicted class
---|---
SpotDistribution = X|H (148.0)
LargestSpotSize = X|B (65.0)
SpotDistribution = O AND C-class = 0 AND HistComplex = 1 AND LargestSpotSize = R|C (44.0/7.0)
Area = 1 AND SpotDistribution = I|D (83.0/33.0)
Area = 1 AND C-class = 0 AND Evolution = 3 AND HistComplex = 1|C (26.0/10.0)
Area = 1 AND LargestSpotSize = S|C (52.0/29.0)
Area = 1|D (45.0/24.0)
|E (14.0/6.0)


## J48 Decision Tree

* SpotDistribution = X: H (295.0)
* SpotDistribution != X
	* LargestSpotSize = X: B (128.0)
	* LargestSpotSize != X
		* Area = 1
			* SpotDistribution = O
				* LargestSpotSize = H
					* Evolution = 2: E (6.0/3.0)
					* Evolution != 2: D (8.0/3.0)
				* LargestSpotSize != H
					* C-class = 0
						* HistComplex = 1
							* LargestSpotSize = S: C (65.0/19.0)
							* LargestSpotSize != S
								* LargestSpotSize = A: D (16.0/7.0)
								* LargestSpotSize != A: C (89.0/26.0)
						* HistComplex != 1
							* Evolution = 1: D (11.0/5.0)
							* Evolution != 1
								* Evolution = 2: C (44.0/17.0)
								* Evolution != 2: D (24.0/11.0)
					* C-class != 0
						* LargestSpotSize = A
							* Evolution = 2: E (8.0/2.0)
							* Evolution != 2: D (6.0/2.0)
						* LargestSpotSize != A: D (32.0/15.0)
			* SpotDistribution != O
				* LargestSpotSize = R: D (28.0/10.0)
				* LargestSpotSize != R
					* HistComplex = 1: D (41.0/12.0)
					* HistComplex != 1
						* M-class = 0
							* Evolution = 3
								* LargestSpotSize = K: D (7.0)
								* LargestSpotSize != K
									* LargestSpotSize = S: D (10.0/5.0)
									* LargestSpotSize != S
										* Activity = 1: D (19.0/7.0)
										* Activity != 1
											* C-class = 0: D (8.0/4.0)
											* C-class != 0: E (6.0/2.0)
							* Evolution != 3
								* C-class = 0
									* LargestSpotSize = S: E (9.0/4.0)
									* LargestSpotSize != S: D (32.0/18.0)
								* C-class != 0
									* C-class = 1: D (14.0/7.0)
									* C-class != 1: F (14.0/8.0)
						* M-class != 0: D (8.0/2.0)
		* Area != 1
			* Prev24Hour = 1: F (17.0/8.0)
			* Prev24Hour != 1: E (8.0/1.0)


## SimpleCart Decision Tree

		* SpotDistribution=(C)|(I)|(O)
	* LargestSpotSize=(X): B(128.0/0.0)
	* LargestSpotSize!=(X)
			* SpotDistribution=(C)|(I)
			* Area=(2)
					* Prev24Hour=(3)|(2)
					* C-class=(1): E(1.0/1.0)
					* C-class!=(1): E(6.0/0.0)
					* Prev24Hour!=(3)|(2)
						* Evolution=(3)|(1): E(6.0/6.0)
						* Evolution!=(3)|(1): F(4.0/0.0)
			* Area!=(2)
				* HistComplex=(2)
					* Evolution=(3)
							* LargestSpotSize=(K)|(R): D(12.0/2.0)
							* LargestSpotSize!=(K)|(R)
									* C-class=(6)|(3)|(1)
								* LargestSpotSize=(S): D(1.0/1.0)
								* LargestSpotSize!=(S)
									* LargestSpotSize=(H): E(2.0/0.0)
									* LargestSpotSize!=(H)
										* Prev24Hour=(3): E(2.0/0.0)
										* Prev24Hour!=(3)
											* C-class=(3): D(2.0/1.0)
											* C-class!=(3): D(2.0/2.0)
									* C-class!=(6)|(3)|(1)
								* M-class=(1): D(3.0/0.0)
								* M-class!=(1)
									* Activity=(2)
											* LargestSpotSize=(H)|(S): E(3.0/2.0)
											* LargestSpotSize!=(H)|(S): D(4.0/4.0)
									* Activity!=(2)
										* LargestSpotSize=(S): D(3.0/2.0)
										* LargestSpotSize!=(S): D(9.0/4.0)
					* Evolution!=(3)
								* C-class=(4)|(2)|(1)
								* LargestSpotSize=(K)|(R): F(4.0/3.0)
								* LargestSpotSize!=(K)|(R): D(9.0/8.0)
								* C-class!=(4)|(2)|(1)
								* LargestSpotSize=(K)|(R): D(7.0/2.0)
								* LargestSpotSize!=(K)|(R)
									* C-class=(5)|(3): E(4.0/1.0)
									* C-class!=(5)|(3)
									* Prev24Hour=(3): D(2.0/0.0)
									* Prev24Hour!=(3)
											* M-class=(3)|(1): D(2.0/0.0)
											* M-class!=(3)|(1)
											* LargestSpotSize=(S): E(5.0/4.0)
											* LargestSpotSize!=(S)
												* Activity=(2)
													* SpotDistribution=(C): E(2.0/0.0)
													* SpotDistribution!=(C): F(3.0/4.0)
												* Activity!=(2): D(8.0/10.0)
				* HistComplex!=(2)
									* LargestSpotSize=(S)|(R)|(X)|(K)|(H)
							* Evolution=(3)|(1)
							* SpotDistribution=(C): D(1.0/1.0)
							* SpotDistribution!=(C): D(15.0/10.0)
							* Evolution!=(3)|(1): C(3.0/1.0)
									* LargestSpotSize!=(S)|(R)|(X)|(K)|(H)
								* C-class=(8)|(3)|(2): D(3.0/3.0)
								* C-class!=(8)|(3)|(2)
								* Evolution=(3)|(1)
								* Activity=(2): D(3.0/0.0)
								* Activity!=(2)
									* C-class=(1): D(2.0/0.0)
									* C-class!=(1)
											* M-class=(2)|(1): D(2.0/0.0)
											* M-class!=(2)|(1): D(7.0/2.0)
								* Evolution!=(3)|(1): D(4.0/0.0)
			* SpotDistribution!=(C)|(I)
								* C-class=(6)|(5)|(4)|(3)|(2)|(1)
							* LargestSpotSize=(K)|(S)|(R)|(X)
						* C-class=(6)|(5): E(2.0/0.0)
						* C-class!=(6)|(5)
						* Prev24Hour=(2): D(2.0/0.0)
						* Prev24Hour!=(2)
							* Activity=(2)
									* Evolution=(3)|(1): D(1.0/1.0)
									* Evolution!=(3)|(1): C(2.0/0.0)
							* Activity!=(2): D(14.0/10.0)
							* LargestSpotSize!=(K)|(S)|(R)|(X)
					* Evolution=(3)
						* C-class=(2): D(1.0/1.0)
						* C-class!=(2): D(3.0/0.0)
					* Evolution!=(3): E(9.0/3.0)
								* C-class!=(6)|(5)|(4)|(3)|(2)|(1)
							* LargestSpotSize=(S)|(R)|(X)|(K)
					* HistComplex=(2)
						* Evolution=(2)
							* Activity=(2): C(2.0/1.0)
							* Activity!=(2)
												* LargestSpotSize=(S)|(A)|(X)|(K)|(H): C(11.0/9.0)
												* LargestSpotSize!=(S)|(A)|(X)|(K)|(H): C(8.0/2.0)
						* Evolution!=(2): D(12.0/11.0)
					* HistComplex!=(2)
						* Evolution=(3)
							* Prev24Hour=(3): C(1.0/1.0)
							* Prev24Hour!=(3)
								* Activity=(2): C(2.0/0.0)
								* Activity!=(2)
									* LargestSpotSize=(S): C(20.0/11.0)
									* LargestSpotSize!=(S)
										* M-class=(1): D(1.0/1.0)
										* M-class!=(1): C(34.0/17.0)
						* Evolution!=(3)
							* LargestSpotSize=(S)
								* Activity=(2)
									* Prev24Hour=(2): C(2.0/0.0)
									* Prev24Hour!=(2): C(6.0/2.0)
								* Activity!=(2): C(15.0/5.0)
							* LargestSpotSize!=(S)
								* Activity=(2): C(2.0/0.0)
								* Activity!=(2)
										* Evolution=(2)|(3): C(22.0/7.0)
										* Evolution!=(2)|(3): C(4.0/1.0)
							* LargestSpotSize!=(S)|(R)|(X)|(K): D(25.0/26.0)
		* SpotDistribution!=(C)|(I)|(O): H(295.0/0.0)


