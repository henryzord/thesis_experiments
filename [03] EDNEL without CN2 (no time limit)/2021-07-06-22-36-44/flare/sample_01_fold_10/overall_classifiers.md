# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = X | H | 0.311390 |
| SpotDistribution != X and LargestSpotSize = X | B | 0.134031 |
| LargestSpotSize = R and SpotDistribution = O | C | 0.062940 |
| LargestSpotSize = A and SpotDistribution = I | D | 0.041234 |
| LargestSpotSize = S and SpotDistribution = O | C | 0.054007 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution = O and LargestSpotSize != A and LargestSpotSize != H and C-class = 1 | D | 0.010523 |
| LargestSpotSize = R and SpotDistribution = I | D | 0.015979 |
| LargestSpotSize = A and SpotDistribution = O | D | 0.012458 |
| SpotDistribution = O and LargestSpotSize!=(X) and SpotDistribution != I and LargestSpotSize != X and C-class != 8 | E | 0.004668 |
| LargestSpotSize = S and SpotDistribution = I | D | 0.012492 |
| LargestSpotSize = K and SpotDistribution = C | E | 0.008642 |
| LargestSpotSize = K and SpotDistribution = I | D | 0.007084 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution = O and LargestSpotSize = A and C-class = 0 and Activity = 1 and Evolution = 2 | C | 0.004908 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution = O and LargestSpotSize != A and LargestSpotSize = H | D | 0.005073 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution = O and LargestSpotSize = A and C-class = 0 and Activity = 1 and Evolution != 2 and HistComplex = 1 | C | 0.003617 |
| SpotDistribution != X and LargestSpotSize != X and Area != 1 and Prev24Hour = 1 and Evolution != 2 and C-class != 1 | F | 0.003023 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution != O and HistComplex != 1 and LargestSpotSize != R and LargestSpotSize != H and M-class != 1 and C-class != 2 and Evolution = 3 and LargestSpotSize = A and Activity != 1 and C-class != 0 | E | 0.003657 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution = O and LargestSpotSize != A and LargestSpotSize != H and C-class != 1 and LargestSpotSize != S and Evolution != 2 and HistComplex != 1 | D | 0.002423 |
| SpotDistribution != X and LargestSpotSize != X and Area != 1 and Prev24Hour = 1 and Evolution = 2 | F | 0.004338 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution != O and HistComplex != 1 and LargestSpotSize != R and LargestSpotSize != H and M-class != 1 and C-class = 2 and Evolution = 2 | F | 0.002446 |
| LargestSpotSize = A and SpotDistribution = C | D | 0.002399 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution = O and LargestSpotSize != A and LargestSpotSize != H and C-class != 1 and LargestSpotSize = S and C-class != 0 and C-class = 3 | D | 0.001348 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution != O and HistComplex != 1 and LargestSpotSize != R and LargestSpotSize = H | E | 0.002574 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution != O and HistComplex != 1 and LargestSpotSize != R and LargestSpotSize != H and M-class != 1 and C-class != 2 and Evolution != 3 and C-class = 3 | E | 0.002062 |
| LargestSpotSize = R and SpotDistribution = C | D | 0.001795 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution != O and HistComplex != 1 and LargestSpotSize != R and LargestSpotSize != H and M-class != 1 and C-class != 2 and Evolution != 3 and C-class != 3 and C-class = 0 and Prev24Hour = 1 and LargestSpotSize = A and Activity != 1 | F | 0.001402 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution != O and HistComplex != 1 and LargestSpotSize != R and LargestSpotSize != H and M-class != 1 and C-class != 2 and Evolution != 3 and C-class != 3 and C-class != 0 and LargestSpotSize != A | F | 0.001089 |
| SpotDistribution != X and LargestSpotSize != X and Area != 1 and Prev24Hour = 1 and Evolution != 2 and C-class = 1 | E | 0.001147 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution = O and LargestSpotSize != A and LargestSpotSize != H and C-class != 1 and LargestSpotSize != S and Evolution = 2 | C | 0.032364 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = X | H | 0.311390 |
| LargestSpotSize = X | B | 0.194825 |
| Area != 1 and C-class != 0 | E | 0.007848 |
| SpotDistribution = O and LargestSpotSize != A and LargestSpotSize != H and C-class = 1 and Evolution != 2 | D | 0.015779 |
| SpotDistribution = O and LargestSpotSize != A and LargestSpotSize != H and LargestSpotSize != S and HistComplex = 1 and Evolution = 3 | C | 0.072374 |
| SpotDistribution = O and LargestSpotSize != A and LargestSpotSize != H and C-class != 1 and C-class = 0 and HistComplex = 1 and Activity = 1 and LargestSpotSize != R and Evolution != 2 | C | 0.035436 |
| SpotDistribution = O and LargestSpotSize != A and LargestSpotSize != H and C-class != 1 and LargestSpotSize != S and HistComplex = 1 | C | 0.044264 |
| Area = 1 and SpotDistribution = O and C-class = 0 and LargestSpotSize != H and LargestSpotSize != A and HistComplex = 1 and Activity = 1 | C | 0.009911 |
| Area = 1 and SpotDistribution = O and C-class = 0 and LargestSpotSize != H and LargestSpotSize != A and HistComplex != 1 and Evolution != 3 and LargestSpotSize != R | C | 0.021472 |
| Area = 1 and SpotDistribution = O and C-class = 0 and LargestSpotSize != H and LargestSpotSize = S | C | 0.015362 |
| Area = 1 and SpotDistribution = O and Activity = 1 and LargestSpotSize != H and LargestSpotSize != R and C-class = 0 and Evolution != 2 | D | 0.075127 |
| Area = 1 and LargestSpotSize = R and Evolution = 3 | D | 0.153751 |
| Area = 1 and LargestSpotSize = R and SpotDistribution = O | C | 0.019928 |
| Area = 1 and HistComplex = 1 and LargestSpotSize = A and SpotDistribution = I | D | 0.090090 |
| Area = 1 and HistComplex = 1 and C-class != 1 and C-class = 0 and LargestSpotSize = S | D | 0.030190 |
| Area != 1 | E | 0.012831 |
| HistComplex = 1 and C-class != 1 and C-class = 0 | D | 0.028040 |
| HistComplex = 1 and C-class = 1 | C | 0.024885 |
| SpotDistribution = O and LargestSpotSize != H and LargestSpotSize = A and C-class = 0 | C | 0.048433 |
| HistComplex != 1 and SpotDistribution != C and LargestSpotSize != K and C-class != 3 and M-class = 0 and C-class != 2 and Activity = 1 and LargestSpotSize != A and Evolution = 2 | D | 0.079724 |
| HistComplex != 1 and SpotDistribution != C and LargestSpotSize != K and C-class != 2 and M-class = 0 and C-class != 3 and SpotDistribution != O and Evolution = 3 | D | 0.055147 |
| HistComplex != 1 and M-class = 0 and C-class != 2 and C-class != 3 and SpotDistribution != I and C-class = 0 | D | 0.038833 |
| SpotDistribution = O and LargestSpotSize = S | D | 0.010714 |
| SpotDistribution != O and Evolution = 3 and Activity = 1 | D | 0.019853 |
| SpotDistribution != O and Evolution != 3 and C-class != 1 and C-class = 0 and Activity = 1 | D | 0.024339 |
| SpotDistribution != O and Evolution != 3 and LargestSpotSize = A | D | 0.025636 |
| SpotDistribution != O and Evolution != 3 | D | 0.006940 |
| SpotDistribution = O | E | 0.192537 |
|  | D | 0.130081 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = I and Evolution = 2 | F | 0.005508 |
| Area = 2 | F | 0.003054 |
| LargestSpotSize = A and Activity = 2 and HistComplex = 2 and Prev24Hour = 1 | E | 0.006833 |
| LargestSpotSize = A and HistComplex = 2 and SpotDistribution = I | E | 0.004832 |
| LargestSpotSize = X | B | 0.142222 |
| SpotDistribution = O and LargestSpotSize = R and Evolution = 2 and C-class = 0 and HistComplex = 1 | C | 0.029827 |
| SpotDistribution = O and HistComplex = 1 and C-class = 0 and Evolution = 2 and LargestSpotSize = S | C | 0.023296 |
| SpotDistribution = O and LargestSpotSize = R and C-class = 0 and Evolution = 2 and Activity = 1 | C | 0.007293 |
| SpotDistribution = O and HistComplex = 1 and C-class = 0 and LargestSpotSize = R | C | 0.039196 |
| SpotDistribution = O and LargestSpotSize = S and C-class = 0 and Evolution = 3 | C | 0.029281 |
| SpotDistribution = O and LargestSpotSize = S and Evolution = 2 | C | 0.014500 |
| SpotDistribution = O and HistComplex = 1 | C | 0.007274 |
| SpotDistribution = O and Activity = 1 | C | 0.003985 |
| SpotDistribution = I and LargestSpotSize = A | D | 0.109230 |
| SpotDistribution = I | D | 0.064810 |
|  | H | 0.596000 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

largestspotsize|spotdistribution|class
---|---|---
h|c|h
r|c|d
a|c|d
k|c|e
h|i|e
x|i|b
r|i|d
s|i|d
a|i|d
k|i|d
k|o|h
x|o|b
r|o|c
h|o|d
s|o|c
a|o|d
k|x|h
a|x|h
r|x|h
s|x|h
h|x|h

## JRip

Decision list:

rules | predicted class
---|---
(SpotDistribution = I) and (Evolution = 2)|F (83.0/63.0)
(Area = 2)|F (23.0/15.0)
(LargestSpotSize = A) and (Activity = 2) and (HistComplex = 2) and (Prev24Hour = 1)|E (17.0/7.0)
(LargestSpotSize = A) and (HistComplex = 2) and (SpotDistribution = I)|E (26.0/17.0)
(LargestSpotSize = X)|B (121.0/0.0)
(SpotDistribution = O) and (LargestSpotSize = R) and (Evolution = 2) and (C-class = 0) and (HistComplex = 1)|C (27.0/5.0)
(SpotDistribution = O) and (HistComplex = 1) and (C-class = 0) and (Evolution = 2) and (LargestSpotSize = S)|C (26.0/7.0)
(SpotDistribution = O) and (LargestSpotSize = R) and (C-class = 0) and (Evolution = 2) and (Activity = 1)|C (10.0/2.0)
(SpotDistribution = O) and (HistComplex = 1) and (C-class = 0) and (LargestSpotSize = R)|C (60.0/21.0)
(SpotDistribution = O) and (LargestSpotSize = S) and (C-class = 0) and (Evolution = 3)|C (45.0/17.0)
(SpotDistribution = O) and (LargestSpotSize = S) and (Evolution = 2)|C (36.0/17.0)
(SpotDistribution = O) and (HistComplex = 1)|C (44.0/25.0)
(SpotDistribution = O) and (Activity = 1)|C (48.0/32.0)
(SpotDistribution = I) and (LargestSpotSize = A)|D (19.0/3.0)
(SpotDistribution = I)|D (54.0/18.0)
|H (318.0/20.0)


## PART

Decision list:

rules | predicted class
---|---
SpotDistribution = X|H (298.0)
LargestSpotSize = X|B (128.0)
Area != 1 AND C-class != 0|E (14.0/7.0)
SpotDistribution = O AND LargestSpotSize != A AND LargestSpotSize != H AND C-class = 1 AND Evolution != 2|D (13.0/5.0)
SpotDistribution = O AND LargestSpotSize != A AND LargestSpotSize != H AND LargestSpotSize != S AND HistComplex = 1 AND Evolution = 3|C (56.0/20.0)
SpotDistribution = O AND LargestSpotSize != A AND LargestSpotSize != H AND C-class != 1 AND C-class = 0 AND HistComplex = 1 AND Activity = 1 AND LargestSpotSize != R AND Evolution != 2|C (34.0/14.0)
SpotDistribution = O AND LargestSpotSize != A AND LargestSpotSize != H AND C-class != 1 AND LargestSpotSize != S AND HistComplex = 1|C (34.0/6.0)
Area = 1 AND SpotDistribution = O AND C-class = 0 AND LargestSpotSize != H AND LargestSpotSize != A AND HistComplex = 1 AND Activity = 1|C (18.0/5.0)
Area = 1 AND SpotDistribution = O AND C-class = 0 AND LargestSpotSize != H AND LargestSpotSize != A AND HistComplex != 1 AND Evolution != 3 AND LargestSpotSize != R|C (28.0/14.0)
Area = 1 AND SpotDistribution = O AND C-class = 0 AND LargestSpotSize != H AND LargestSpotSize = S|C (22.0/6.0)
Area = 1 AND SpotDistribution = O AND Activity = 1 AND LargestSpotSize != H AND LargestSpotSize != R AND C-class = 0 AND Evolution != 2|D (21.0/11.0)
Area = 1 AND LargestSpotSize = R AND Evolution = 3|D (22.0/5.0)
Area = 1 AND LargestSpotSize = R AND SpotDistribution = O|C (17.0/6.0)
Area = 1 AND HistComplex = 1 AND LargestSpotSize = A AND SpotDistribution = I|D (24.0/4.0)
Area = 1 AND HistComplex = 1 AND C-class != 1 AND C-class = 0 AND LargestSpotSize = S|D (13.0/5.0)
Area != 1|E (12.0/5.0)
HistComplex = 1 AND C-class != 1 AND C-class = 0|D (11.0/4.0)
HistComplex = 1 AND C-class = 1|C (10.0/4.0)
SpotDistribution = O AND LargestSpotSize != H AND LargestSpotSize = A AND C-class = 0|C (14.0/8.0)
HistComplex != 1 AND SpotDistribution != C AND LargestSpotSize != K AND C-class != 3 AND M-class = 0 AND C-class != 2 AND Activity = 1 AND LargestSpotSize != A AND Evolution = 2|D (14.0/6.0)
HistComplex != 1 AND SpotDistribution != C AND LargestSpotSize != K AND C-class != 2 AND M-class = 0 AND C-class != 3 AND SpotDistribution != O AND Evolution = 3|D (30.0/15.0)
HistComplex != 1 AND M-class = 0 AND C-class != 2 AND C-class != 3 AND SpotDistribution != I AND C-class = 0|D (14.0/7.0)
SpotDistribution = O AND LargestSpotSize = S|D (12.0/7.0)
SpotDistribution != O AND Evolution = 3 AND Activity = 1|D (13.0/6.0)
SpotDistribution != O AND Evolution != 3 AND C-class != 1 AND C-class = 0 AND Activity = 1|D (19.0/10.0)
SpotDistribution != O AND Evolution != 3 AND LargestSpotSize = A|D (27.0/16.0)
SpotDistribution != O AND Evolution != 3|D (17.0/11.0)
SpotDistribution = O|E (11.0/3.0)
|D (11.0/2.0)


## J48 Decision Tree

* SpotDistribution = X: H (298.0)
* SpotDistribution != X
	* LargestSpotSize = X: B (128.0)
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
						* C-class != 1
							* LargestSpotSize = S
								* C-class = 0: C (102.0/39.0)
								* C-class != 0
									* C-class = 3: D (4.0/2.0)
									* C-class != 3: E (6.0/3.0)
							* LargestSpotSize != S
								* Evolution = 2: C (40.0/8.0)
								* Evolution != 2
									* HistComplex = 1: C (61.0/21.0)
									* HistComplex != 1: D (5.0/2.0)
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
										* LargestSpotSize = A
											* Activity = 1: D (19.0/8.0)
											* Activity != 1
												* C-class = 0: D (5.0/3.0)
												* C-class != 0: E (5.0/1.0)
										* LargestSpotSize != A: D (10.0/3.0)
									* Evolution != 3
										* C-class = 3: E (5.0/2.0)
										* C-class != 3
											* C-class = 0
												* Prev24Hour = 1
													* LargestSpotSize = A
														* Activity = 1: D (18.0/10.0)
														* Activity != 1: F (7.0/4.0)
													* LargestSpotSize != A: D (13.0/7.0)
												* Prev24Hour != 1: D (4.0/2.0)
											* C-class != 0
												* LargestSpotSize = A: D (11.0/6.0)
												* LargestSpotSize != A: F (4.0/2.0)
		* Area != 1
			* Prev24Hour = 1
				* Evolution = 2: F (4.0)
				* Evolution != 2
					* C-class = 1: E (4.0/2.0)
					* C-class != 1: F (9.0/4.0)
			* Prev24Hour != 1: E (9.0/1.0)


## SimpleCart Decision Tree

		* SpotDistribution=(C)|(I)|(O)
	* LargestSpotSize=(X): B(128.0/0.0)
	* LargestSpotSize!=(X)
			* SpotDistribution=(C)|(I)
			* Area=(2)
					* Prev24Hour=(3)|(2): E(8.0/1.0)
					* Prev24Hour!=(3)|(2): F(10.0/6.0)
			* Area!=(2): D(110.0/86.0)
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


