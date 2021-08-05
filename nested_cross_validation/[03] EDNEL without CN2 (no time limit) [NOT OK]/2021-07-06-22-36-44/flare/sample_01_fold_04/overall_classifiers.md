# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | H | 0.311715 |
| LargestSpotSize = X and SpotDistribution = O and Area = 1 | B | 0.122210 |
| SpotDistribution = O and LargestSpotSize!=(X) and SpotDistribution != I and LargestSpotSize != X and Activity!=(2) and M-class!=(1) and LargestSpotSize!=(H) and C-class!=(1) | D | 0.056753 |
| LargestSpotSize = R and SpotDistribution = O and Area = 1 | C | 0.061868 |
| SpotDistribution = O and LargestSpotSize = S | C | 0.055406 |
| LargestSpotSize = A and SpotDistribution = I and Area = 1 | D | 0.043316 |
| SpotDistribution = I and LargestSpotSize = R | D | 0.014840 |
| SpotDistribution = C and LargestSpotSize = K | E | 0.009635 |
| LargestSpotSize = X and SpotDistribution = I and Area = 1 | B | 0.015495 |
| LargestSpotSize = S and SpotDistribution = I and Area = 1 | D | 0.010068 |
| SpotDistribution = I and LargestSpotSize = K and Area = 1 and Evolution = 3 | D | 0.010681 |
| SpotDistribution = O and LargestSpotSize = A and M-class = 0 and Activity = 2 and Prev24Hour = 1 and HistComplex = 2 | E | 0.005708 |
| SpotDistribution = O and LargestSpotSize = H and Activity = 2 | E | 0.003432 |
| SpotDistribution = I and LargestSpotSize = K and Area = 2 and Evolution = 3 | E | 0.002577 |
| LargestSpotSize = K and SpotDistribution = I and Area = 2 | F | 0.001634 |
| LargestSpotSize = H and SpotDistribution = I and Area = 1 | E | 0.002291 |
| SpotDistribution = O and LargestSpotSize = A and M-class = 1 | E | 0.002291 |
| SpotDistribution = I and LargestSpotSize = S and C-class = 2 | F | 0.002174 |
| LargestSpotSize = A and SpotDistribution = C and Area = 1 | D | 0.002699 |
| SpotDistribution = C and LargestSpotSize = R | D | 0.002692 |
| SpotDistribution = I and LargestSpotSize = K and Area = 1 and Evolution = 2 and Activity = 1 | F | 0.001451 |
| SpotDistribution = I and LargestSpotSize = S and C-class = 3 | E | 0.001147 |
| SpotDistribution = C and LargestSpotSize = H | E | 0.001147 |
| SpotDistribution = I and LargestSpotSize = S and C-class = 5 | E | 0.001147 |
| SpotDistribution = O and LargestSpotSize = K | C | 0.001304 |
| SpotDistribution = I and LargestSpotSize = K and Area = 1 and Evolution = 2 and Activity = 2 | D | 0.001350 |
| SpotDistribution = O and LargestSpotSize = H and Activity = 1 and C-class = 1 | C | 0.000653 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = X | H | 0.311715 |
| LargestSpotSize != X and Area = 1 and SpotDistribution = O and LargestSpotSize != H and LargestSpotSize != A | C | 0.177080 |
| LargestSpotSize = X | B | 0.252465 |
| Area = 1 and LargestSpotSize != R and HistComplex = 1 | D | 0.213250 |
| Area = 1 and LargestSpotSize != R and SpotDistribution != O and Evolution = 3 | D | 0.089089 |
| Area = 1 and LargestSpotSize != R and SpotDistribution = O and Activity = 1 | D | 0.098358 |
| LargestSpotSize = R | D | 0.213336 |
| SpotDistribution != O and Area != 1 | E | 0.066441 |
| SpotDistribution != O and C-class != 0 and C-class = 1 | D | 0.020979 |
| SpotDistribution != O and C-class = 0 | D | 0.031315 |
| SpotDistribution != O | F | 0.127538 |
|  | E | 0.559055 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| HistComplex = 2 and Activity = 2 and SpotDistribution = C and LargestSpotSize = K | E | 0.008623 |
| LargestSpotSize = X | B | 0.135737 |
| SpotDistribution = O and HistComplex = 1 and Evolution = 2 and LargestSpotSize = S | C | 0.031209 |
| SpotDistribution = O and LargestSpotSize = R and Evolution = 2 and C-class = 0 | C | 0.034091 |
| SpotDistribution = O and HistComplex = 1 and LargestSpotSize = R and C-class = 0 | C | 0.039611 |
| SpotDistribution = O and LargestSpotSize = S and HistComplex = 1 and C-class = 0 | C | 0.019528 |
| SpotDistribution = O and LargestSpotSize = S and Evolution = 2 and C-class = 0 | C | 0.008862 |
| SpotDistribution = O and Activity = 1 and Evolution = 3 and LargestSpotSize = S | C | 0.005081 |
| SpotDistribution = I and Evolution = 3 and HistComplex = 1 and LargestSpotSize = A | D | 0.032210 |
| SpotDistribution = I and Evolution = 3 and C-class = 0 | D | 0.041684 |
| SpotDistribution = O and Evolution = 3 | D | 0.092303 |
|  | H | 0.529307 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

largestspotsize|spotdistribution|area|class
---|---|---|---
a|c|2|h
k|c|2|e
a|i|2|h
k|i|2|f
r|o|2|h
k|c|1|e
h|c|1|h
a|c|1|d
r|c|1|d
x|i|1|b
h|i|1|e
r|i|1|d
k|i|1|d
s|i|1|d
a|i|1|d
k|o|1|h
h|o|1|d
x|o|1|b
s|o|1|c
r|o|1|c
a|o|1|d
k|x|1|h
h|x|1|h
a|x|1|h
r|x|1|h
s|x|1|h

## JRip

Decision list:

rules | predicted class
---|---
(HistComplex = 2) and (Activity = 2) and (SpotDistribution = C) and (LargestSpotSize = K)|E (16.0/5.0)
(LargestSpotSize = X)|B (128.0/0.0)
(SpotDistribution = O) and (HistComplex = 1) and (Evolution = 2) and (LargestSpotSize = S)|C (31.0/6.0)
(SpotDistribution = O) and (LargestSpotSize = R) and (Evolution = 2) and (C-class = 0)|C (33.0/6.0)
(SpotDistribution = O) and (HistComplex = 1) and (LargestSpotSize = R) and (C-class = 0)|C (61.0/20.0)
(SpotDistribution = O) and (LargestSpotSize = S) and (HistComplex = 1) and (C-class = 0)|C (38.0/15.0)
(SpotDistribution = O) and (LargestSpotSize = S) and (Evolution = 2) and (C-class = 0)|C (21.0/9.0)
(SpotDistribution = O) and (Activity = 1) and (Evolution = 3) and (LargestSpotSize = S)|C (19.0/9.0)
(SpotDistribution = I) and (Evolution = 3) and (HistComplex = 1) and (LargestSpotSize = A)|D (21.0/3.0)
(SpotDistribution = I) and (Evolution = 3) and (C-class = 0)|D (53.0/20.0)
(SpotDistribution = O) and (Evolution = 3)|D (49.0/21.0)
|H (486.0/188.0)


## PART

Decision list:

rules | predicted class
---|---
SpotDistribution = X|H (298.0)
LargestSpotSize != X AND Area = 1 AND SpotDistribution = O AND LargestSpotSize != H AND LargestSpotSize != A|C (237.0/88.0)
LargestSpotSize = X|B (128.0)
Area = 1 AND LargestSpotSize != R AND HistComplex = 1|D (67.0/23.0)
Area = 1 AND LargestSpotSize != R AND SpotDistribution != O AND Evolution = 3|D (56.0/25.0)
Area = 1 AND LargestSpotSize != R AND SpotDistribution = O AND Activity = 1|D (35.0/18.0)
LargestSpotSize = R|D (29.0/10.0)
SpotDistribution != O AND Area != 1|E (25.0/11.0)
SpotDistribution != O AND C-class != 0 AND C-class = 1|D (15.0/7.0)
SpotDistribution != O AND C-class = 0|D (43.0/27.0)
SpotDistribution != O|F (12.0/6.0)
|E (11.0/3.0)


## J48 Decision Tree

* SpotDistribution = X: H (298.0)
* SpotDistribution = O
	* LargestSpotSize = A
		* M-class = 0
			* Activity = 1: D (42.0/21.0)
			* Activity = 2
				* Prev24Hour = 1
					* HistComplex = 1: D (2.0)
					* HistComplex = 2: E (5.0)
				* Prev24Hour = 2: E (0.0)
				* Prev24Hour = 3: D (3.0/1.0)
		* M-class = 1: E (2.0)
		* M-class = 2: D (0.0)
		* M-class = 3: D (0.0)
		* M-class = 4: D (0.0)
		* M-class = 5: D (0.0)
	* LargestSpotSize = R
		* C-class = 0: C (100.0/30.0)
		* C-class = 1: D (7.0/2.0)
		* C-class = 2: C (0.0)
		* C-class = 3: C (0.0)
		* C-class = 4: C (0.0)
		* C-class = 5: C (1.0)
		* C-class = 6: C (0.0)
		* C-class = 7: C (0.0)
		* C-class = 8: C (0.0)
	* LargestSpotSize = S: C (129.0/54.0)
	* LargestSpotSize = X: B (115.0)
	* LargestSpotSize = K: C (1.0)
	* LargestSpotSize = H
		* Activity = 1
			* C-class = 0: D (9.0/3.0)
			* C-class = 1: C (2.0/1.0)
			* C-class = 2: D (0.0)
			* C-class = 3: D (0.0)
			* C-class = 4: D (0.0)
			* C-class = 5: D (0.0)
			* C-class = 6: D (0.0)
			* C-class = 7: D (0.0)
			* C-class = 8: D (0.0)
		* Activity = 2: E (3.0)
* SpotDistribution = I
	* LargestSpotSize = A: D (104.0/46.0)
	* LargestSpotSize = R: D (26.0/9.0)
	* LargestSpotSize = S
		* C-class = 0: D (31.0/16.0)
		* C-class = 1: D (4.0/2.0)
		* C-class = 2: F (2.0)
		* C-class = 3: E (1.0)
		* C-class = 4: D (0.0)
		* C-class = 5: E (1.0)
		* C-class = 6: D (0.0)
		* C-class = 7: D (0.0)
		* C-class = 8: D (0.0)
	* LargestSpotSize = X: B (13.0)
	* LargestSpotSize = K
		* Area = 1
			* Evolution = 1: D (0.0)
			* Evolution = 2
				* Activity = 1: F (3.0/1.0)
				* Activity = 2: D (4.0/2.0)
			* Evolution = 3: D (8.0)
		* Area = 2
			* Evolution = 1: E (0.0)
			* Evolution = 2: F (2.0)
			* Evolution = 3: E (4.0/1.0)
	* LargestSpotSize = H: E (2.0)
* SpotDistribution = C
	* LargestSpotSize = A: D (9.0/5.0)
	* LargestSpotSize = R: D (2.0)
	* LargestSpotSize = S: E (0.0)
	* LargestSpotSize = X: E (0.0)
	* LargestSpotSize = K: E (20.0/7.0)
	* LargestSpotSize = H: E (1.0)


## SimpleCart Decision Tree

		* SpotDistribution=(C)|(I)|(O)
	* LargestSpotSize=(X): B(128.0/0.0)
	* LargestSpotSize!=(X)
			* SpotDistribution=(C)|(I)
			* Area=(2)
					* Prev24Hour=(3)|(2)
					* Evolution=(3)
												* C-class=(1)|(2)|(3)|(4)|(5)|(7)|(8): E(1.0/1.0)
												* C-class!=(1)|(2)|(3)|(4)|(5)|(7)|(8): E(2.0/0.0)
					* Evolution!=(3): E(5.0/0.0)
					* Prev24Hour!=(3)|(2): F(9.0/7.0)
			* Area!=(2)
				* HistComplex=(2)
					* Evolution=(3)
						* LargestSpotSize=(S): D(3.0/5.0)
						* LargestSpotSize!=(S)
								* LargestSpotSize=(K)|(R)
								* SpotDistribution=(C): D(1.0/1.0)
								* SpotDistribution!=(C)
													* LargestSpotSize=(K)|(A)|(S)|(X)|(H): D(8.0/0.0)
													* LargestSpotSize!=(K)|(A)|(S)|(X)|(H)
										* Activity=(2): D(2.0/0.0)
										* Activity!=(2): D(3.0/1.0)
								* LargestSpotSize!=(K)|(R)
								* LargestSpotSize=(H): E(3.0/0.0)
								* LargestSpotSize!=(H)
															* C-class=(0)|(1)|(2)|(3)|(5)|(7)|(8)
										* M-class=(1): D(3.0/0.0)
										* M-class!=(1)
											* C-class=(1)
												* Activity=(2): E(2.0/0.0)
												* Activity!=(2): D(2.0/1.0)
											* C-class!=(1)
												* Activity=(2): D(5.0/4.0)
												* Activity!=(2): D(10.0/7.0)
															* C-class!=(0)|(1)|(2)|(3)|(5)|(7)|(8): E(2.0/0.0)
					* Evolution!=(3)
						* LargestSpotSize=(R): D(4.0/2.0)
						* LargestSpotSize!=(R)
								* M-class=(3)|(1): D(3.0/0.0)
								* M-class!=(3)|(1)
													* C-class=(0)|(1)|(5)|(6)|(7)|(8)
									* C-class=(1): D(7.0/7.0)
									* C-class!=(1)
										* Prev24Hour=(3): D(2.0/2.0)
										* Prev24Hour!=(3)
											* Activity=(2)
												* SpotDistribution=(C): E(2.0/0.0)
												* SpotDistribution!=(C)
													* LargestSpotSize=(S): E(2.0/3.0)
													* LargestSpotSize!=(S): F(3.0/3.0)
											* Activity!=(2)
												* LargestSpotSize=(S): E(3.0/2.0)
												* LargestSpotSize!=(S): D(8.0/11.0)
													* C-class!=(0)|(1)|(5)|(6)|(7)|(8)
									* C-class=(4): F(3.0/0.0)
									* C-class!=(4)
										* LargestSpotSize=(K): D(1.0/1.0)
										* LargestSpotSize!=(K)
																		* C-class=(3)|(0)|(1)|(4)|(5)|(6)|(7)|(8): E(3.0/1.0)
																		* C-class!=(3)|(0)|(1)|(4)|(5)|(6)|(7)|(8): F(2.0/1.0)
				* HistComplex!=(2)
									* LargestSpotSize=(S)|(R)|(X)|(K)|(H)
						* Activity=(2): D(4.0/0.0)
						* Activity!=(2)
								* Evolution=(3)|(1)
									* C-class=(2)|(1)
									* LargestSpotSize=(S): C(2.0/1.0)
									* LargestSpotSize!=(S)
										* C-class=(2): D(1.0/1.0)
										* C-class!=(2): D(2.0/1.0)
									* C-class!=(2)|(1)
													* LargestSpotSize=(S)|(A)|(X)|(K)|(H): D(6.0/5.0)
													* LargestSpotSize!=(S)|(A)|(X)|(K)|(H): D(4.0/2.0)
								* Evolution!=(3)|(1): C(3.0/0.0)
									* LargestSpotSize!=(S)|(R)|(X)|(K)|(H)
											* C-class=(0)|(1)|(4)|(5)|(6)|(7)
								* Evolution=(3)|(1)
								* Activity=(2): D(3.0/0.0)
								* Activity!=(2)
										* M-class=(2)|(1): D(3.0/0.0)
										* M-class!=(2)|(1)
										* C-class=(1): D(2.0/0.0)
										* C-class!=(1): D(8.0/2.0)
								* Evolution!=(3)|(1): D(4.0/0.0)
											* C-class!=(0)|(1)|(4)|(5)|(6)|(7): D(3.0/3.0)
			* SpotDistribution!=(C)|(I)
					* LargestSpotSize=(S)|(R)|(X)
				* HistComplex=(2): C(31.0/32.0)
				* HistComplex!=(2)
					* Evolution=(3): C(64.0/42.0)
					* Evolution!=(3)
							* C-class=(3)|(1)
											* LargestSpotSize=(S)|(A)|(X)|(K)|(H)
								* C-class=(3): D(1.0/1.0)
								* C-class!=(3): C(3.0/0.0)
											* LargestSpotSize!=(S)|(A)|(X)|(K)|(H): D(2.0/0.0)
							* C-class!=(3)|(1)
							* LargestSpotSize=(S)
									* Evolution=(2)|(3)
									* Activity=(2)
										* Prev24Hour=(2): C(2.0/0.0)
										* Prev24Hour!=(2): C(4.0/1.0)
									* Activity!=(2): C(15.0/4.0)
									* Evolution!=(2)|(3): C(2.0/1.0)
							* LargestSpotSize!=(S): C(26.0/6.0)
					* LargestSpotSize!=(S)|(R)|(X)
				* Activity=(2)
					* Prev24Hour=(3): D(2.0/1.0)
					* Prev24Hour!=(3)
						* HistComplex=(2): E(8.0/0.0)
						* HistComplex!=(2): D(2.0/0.0)
				* Activity!=(2)
					* M-class=(1): E(2.0/0.0)
					* M-class!=(1)
						* LargestSpotSize=(H)
							* C-class=(1): C(1.0/1.0)
							* C-class!=(1)
								* HistComplex=(2)
										* Evolution=(3)|(1): D(3.0/2.0)
										* Evolution!=(3)|(1): D(2.0/0.0)
								* HistComplex!=(2): D(1.0/1.0)
						* LargestSpotSize!=(H)
							* C-class=(1)
								* Evolution=(3): D(3.0/0.0)
								* Evolution!=(3): E(2.0/2.0)
							* C-class!=(1): D(17.0/19.0)
		* SpotDistribution!=(C)|(I)|(O): H(298.0/0.0)


