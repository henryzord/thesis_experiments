# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| LargestSpotSize != X and SpotDistribution = X | H | 0.311390 |
| LargestSpotSize = X | B | 0.134937 |
| SpotDistribution = O and LargestSpotSize!=(X) and SpotDistribution != I and LargestSpotSize != X and C-class != 1 and Activity!=(2) | D | 0.047766 |
| LargestSpotSize = R and SpotDistribution = O and HistComplex = 1 and Area = 1 | C | 0.055492 |
| LargestSpotSize = S and SpotDistribution = O and HistComplex = 1 and Area = 1 | C | 0.040623 |
| LargestSpotSize != X and SpotDistribution != X and Area = 1 and HistComplex != 1 and SpotDistribution != O | D | 0.045549 |
| LargestSpotSize != X and SpotDistribution != X and Area = 1 and HistComplex != 1 and SpotDistribution = O and Activity = 1 and C-class = 0 and Evolution != 1 and Evolution = 2 | C | 0.016075 |
| LargestSpotSize = A and SpotDistribution = I and HistComplex = 1 and Area = 1 | D | 0.020734 |
| LargestSpotSize != X and SpotDistribution != X and Area != 1 | E | 0.008057 |
| LargestSpotSize != X and SpotDistribution != X and Area = 1 and HistComplex != 1 and SpotDistribution = O and Activity != 1 | E | 0.005225 |
| LargestSpotSize = S and SpotDistribution = I and HistComplex = 1 and Area = 1 | D | 0.006804 |
| LargestSpotSize = A and SpotDistribution = C and HistComplex = 2 and Area = 1 | E | 0.002618 |
| LargestSpotSize = R and SpotDistribution = I and HistComplex = 1 and Area = 1 | D | 0.005488 |
| LargestSpotSize = R and SpotDistribution = O and HistComplex = 2 and Area = 1 | C | 0.008636 |
| LargestSpotSize != X and SpotDistribution != X and Area = 1 and HistComplex = 1 and LargestSpotSize != A and Activity = 1 and C-class != 0 | C | 0.010127 |
| LargestSpotSize = A and SpotDistribution = I and HistComplex = 2 and Area = 2 | F | 0.002174 |
| LargestSpotSize = K and SpotDistribution = C and HistComplex = 2 and Area = 1 | E | 0.001527 |
| LargestSpotSize != X and SpotDistribution != X and Area = 1 and HistComplex != 1 and SpotDistribution = O and Activity = 1 and C-class != 0 | D | 0.001807 |
| LargestSpotSize != X and SpotDistribution != X and Area = 1 and HistComplex = 1 and LargestSpotSize != A and Activity = 1 and C-class = 0 and Evolution != 3 | C | 0.040292 |
| LargestSpotSize != X and SpotDistribution != X and Area = 1 and HistComplex = 1 and LargestSpotSize = A | D | 0.028705 |
| LargestSpotSize = R and SpotDistribution = C and HistComplex = 1 and Area = 1 | D | 0.000674 |
| SpotDistribution = O and LargestSpotSize!=(X) and SpotDistribution != I and LargestSpotSize != X and C-class = 1 and Evolution!=(3) | E | 0.000821 |
| LargestSpotSize != X and SpotDistribution != X and Area = 1 and HistComplex = 1 and LargestSpotSize != A and Activity = 1 and C-class = 0 and Evolution = 3 and SpotDistribution = O | C | 0.042535 |
| LargestSpotSize = S and SpotDistribution = O and HistComplex = 2 and Area = 1 | D | 0.012483 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = X | H | 0.311390 |
| LargestSpotSize = S | C | 0.081871 |
| LargestSpotSize = R | C | 0.101408 |
| LargestSpotSize = X | B | 0.260606 |
| Area = 1 and SpotDistribution = I | D | 0.322401 |
| Area = 1 and SpotDistribution = O and C-class = 0 and LargestSpotSize = A and Evolution = 3 | D | 0.044183 |
| Area = 1 and C-class = 0 and Activity = 1 | D | 0.242017 |
| Area = 1 and Evolution = 2 | E | 0.191005 |
| Area = 2 | E | 0.070417 |
|  | D | 0.234848 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = I and Evolution = 2 and Area = 2 | F | 0.003257 |
| Activity = 2 and SpotDistribution = C | E | 0.010714 |
| LargestSpotSize = X | B | 0.137527 |
| SpotDistribution = O and LargestSpotSize = R | C | 0.077001 |
| SpotDistribution = O and HistComplex = 1 | C | 0.044894 |
| SpotDistribution = I | D | 0.114391 |
| SpotDistribution = O and Evolution = 3 | D | 0.100121 |
|  | H | 0.588933 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

largestspotsize|spotdistribution|histcomplex|area|class
---|---|---|---|---
a|c|2|2|h
k|c|2|2|e
a|i|2|2|f
k|i|2|2|e
r|o|2|2|h
k|c|2|1|e
h|c|2|1|h
a|c|2|1|e
r|c|2|1|h
x|i|2|1|b
h|i|2|1|d
s|i|2|1|d
k|i|2|1|d
r|i|2|1|d
a|i|2|1|d
a|c|1|1|d
r|o|2|1|c
x|o|2|1|b
r|c|1|1|d
a|o|2|1|d
h|o|2|1|d
s|o|2|1|d
h|x|2|1|h
r|x|2|1|h
x|i|1|1|b
s|i|1|1|d
a|i|1|1|d
r|i|1|1|d
a|x|2|1|h
s|x|2|1|h
k|o|1|1|h
h|o|1|1|d
x|o|1|1|b
a|o|1|1|d
r|o|1|1|c
s|o|1|1|c
k|x|1|1|h
a|x|1|1|h
h|x|1|1|h
r|x|1|1|h
s|x|1|1|h

## JRip

Decision list:

rules | predicted class
---|---
(SpotDistribution = I) and (Evolution = 2) and (Area = 2)|F (3.0/0.0)
(Activity = 2) and (SpotDistribution = C)|E (24.0/9.0)
(LargestSpotSize = X)|B (129.0/0.0)
(SpotDistribution = O) and (LargestSpotSize = R)|C (114.0/38.0)
(SpotDistribution = O) and (HistComplex = 1)|C (105.0/44.0)
(SpotDistribution = I)|D (180.0/81.0)
(SpotDistribution = O) and (Evolution = 3)|D (35.0/16.0)
|H (367.0/69.0)


## PART

Decision list:

rules | predicted class
---|---
SpotDistribution = X|H (239.0)
LargestSpotSize = S|C (132.0/72.0)
LargestSpotSize = R|C (113.0/45.0)
LargestSpotSize = X|B (103.0)
Area = 1 AND SpotDistribution = I|D (96.0/44.0)
Area = 1 AND SpotDistribution = O AND C-class = 0 AND LargestSpotSize = A AND Evolution = 3|D (16.0/8.0)
Area = 1 AND C-class = 0 AND Activity = 1|D (25.0/13.0)
Area = 1 AND Evolution = 2|E (16.0/6.0)
Area = 2|E (15.0/7.0)
|D (11.0/6.0)


## J48 Decision Tree

* LargestSpotSize = X: B (113.0)
* LargestSpotSize != X
	* SpotDistribution = X: H (261.0)
	* SpotDistribution != X
		* Area = 1
			* HistComplex = 1
				* LargestSpotSize = A: D (39.0/13.0)
				* LargestSpotSize != A
					* Activity = 1
						* C-class = 0
							* Evolution = 3
								* SpotDistribution = O: C (73.0/25.0)
								* SpotDistribution != O: D (13.0/6.0)
							* Evolution != 3: C (49.0/11.0)
						* C-class != 0: C (31.0/16.0)
					* Activity != 1: C (18.0/8.0)
			* HistComplex != 1
				* SpotDistribution = O
					* Activity = 1
						* C-class = 0
							* Evolution = 1: D (10.0/6.0)
							* Evolution != 1
								* Evolution = 2: C (35.0/16.0)
								* Evolution != 2: D (23.0/8.0)
						* C-class != 0: D (11.0/7.0)
					* Activity != 1: E (19.0/9.0)
				* SpotDistribution != O: D (122.0/62.0)
		* Area != 1: E (21.0/11.0)


## SimpleCart Decision Tree

		* SpotDistribution=(C)|(I)|(O)
	* LargestSpotSize=(X): B(129.0/0.0)
	* LargestSpotSize!=(X)
			* SpotDistribution=(C)|(I)
			* Area=(2)
					* Prev24Hour=(3)|(2): E(7.0/0.0)
					* Prev24Hour!=(3)|(2): F(10.0/6.0)
			* Area!=(2)
				* HistComplex=(2)
					* Evolution=(3)
							* LargestSpotSize=(K)|(R)
							* SpotDistribution=(C): D(1.0/1.0)
							* SpotDistribution!=(C)
												* LargestSpotSize=(K)|(A)|(S)|(X)|(H): D(9.0/0.0)
												* LargestSpotSize!=(K)|(A)|(S)|(X)|(H)
									* Activity=(2): D(2.0/0.0)
									* Activity!=(2): D(3.0/1.0)
							* LargestSpotSize!=(K)|(R)
										* C-class=(6)|(5)|(4)|(1)
								* Activity=(2): E(4.0/0.0)
								* Activity!=(2)
									* M-class=(1): E(2.0/0.0)
									* M-class!=(1)
														* LargestSpotSize=(S)|(R)|(X)|(K)|(H): D(1.0/1.0)
														* LargestSpotSize!=(S)|(R)|(X)|(K)|(H): D(1.0/1.0)
										* C-class!=(6)|(5)|(4)|(1)
								* SpotDistribution=(C): E(2.0/1.0)
								* SpotDistribution!=(C)
									* C-class=(2): D(1.0/2.0)
									* C-class!=(2): D(18.0/9.0)
					* Evolution!=(3)
							* C-class=(4)|(2)
							* LargestSpotSize=(K): F(2.0/1.0)
							* LargestSpotSize!=(K)
								* C-class=(4): D(1.0/1.0)
								* C-class!=(4): F(3.0/0.0)
							* C-class!=(4)|(2)
								* C-class=(5)|(3): E(4.0/1.0)
								* C-class!=(5)|(3)
									* M-class=(3)|(1): D(3.0/0.0)
									* M-class!=(3)|(1)
									* SpotDistribution=(C): E(3.0/2.0)
									* SpotDistribution!=(C)
										* LargestSpotSize=(R)
											* C-class=(1): C(1.0/1.0)
											* C-class!=(1): D(2.0/1.0)
										* LargestSpotSize!=(R): D(22.0/29.0)
				* HistComplex!=(2)
									* LargestSpotSize=(S)|(R)|(X)|(K)|(H)
						* Activity=(2)
							* SpotDistribution=(C): D(1.0/1.0)
							* SpotDistribution!=(C): D(3.0/0.0)
						* Activity!=(2)
								* Evolution=(3)|(1)
												* LargestSpotSize=(S)|(A)|(X)|(K)|(H)
									* C-class=(1): D(2.0/2.0)
									* C-class!=(1): D(5.0/4.0)
												* LargestSpotSize!=(S)|(A)|(X)|(K)|(H)
									* C-class=(2): D(1.0/1.0)
									* C-class!=(2)
										* C-class=(1): D(2.0/1.0)
										* C-class!=(1): D(3.0/2.0)
								* Evolution!=(3)|(1): C(2.0/0.0)
									* LargestSpotSize!=(S)|(R)|(X)|(K)|(H)
								* C-class=(8)|(3)|(2): D(3.0/3.0)
								* C-class!=(8)|(3)|(2)
								* Evolution=(3)|(1)
									* M-class=(2)|(1): D(3.0/0.0)
									* M-class!=(2)|(1)
									* Activity=(2): D(2.0/0.0)
									* Activity!=(2): D(9.0/2.0)
								* Evolution!=(3)|(1): D(3.0/0.0)
			* SpotDistribution!=(C)|(I)
						* LargestSpotSize=(K)|(S)|(R)|(X)
				* HistComplex=(2): C(31.0/33.0)
				* HistComplex!=(2)
							* C-class=(6)|(2)|(1)
							* M-class=(2)|(1): D(3.0/0.0)
							* M-class!=(2)|(1)
								* C-class=(6)|(2): E(2.0/1.0)
								* C-class!=(6)|(2): C(8.0/7.0)
							* C-class!=(6)|(2)|(1)
						* Evolution=(2)
							* Activity=(2)
												* LargestSpotSize=(S)|(A)|(X)|(K)|(H)
									* Prev24Hour=(2): C(2.0/0.0)
									* Prev24Hour!=(2): C(4.0/2.0)
												* LargestSpotSize!=(S)|(A)|(X)|(K)|(H): C(2.0/0.0)
							* Activity!=(2)
								* LargestSpotSize=(S)
									* C-class=(3): D(1.0/1.0)
									* C-class!=(3): C(14.0/3.0)
								* LargestSpotSize!=(S): C(23.0/7.0)
						* Evolution!=(2)
							* Prev24Hour=(3): C(1.0/1.0)
							* Prev24Hour!=(3)
								* Activity=(2): C(2.0/0.0)
								* Activity!=(2)
										* C-class=(5)|(3): C(2.0/0.0)
										* C-class!=(5)|(3)
										* LargestSpotSize=(S): C(19.0/13.0)
										* LargestSpotSize!=(S)
												* Evolution=(3)|(2)
												* M-class=(1): D(1.0/1.0)
												* M-class!=(1): C(34.0/19.0)
												* Evolution!=(3)|(2): C(3.0/1.0)
						* LargestSpotSize!=(K)|(S)|(R)|(X)
							* C-class=(4)|(3)|(2)|(1)
					* Evolution=(3): D(4.0/2.0)
					* Evolution!=(3): E(8.0/3.0)
							* C-class!=(4)|(3)|(2)|(1)
					* Activity=(2)
						* HistComplex=(2)
							* Prev24Hour=(3): D(1.0/1.0)
							* Prev24Hour!=(3): E(4.0/0.0)
						* HistComplex!=(2): D(3.0/0.0)
					* Activity!=(2): D(23.0/25.0)
		* SpotDistribution!=(C)|(I)|(O): H(298.0/0.0)


