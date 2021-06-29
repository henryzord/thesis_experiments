# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | H | 0.312042 |
| SpotDistribution != X and LargestSpotSize = X | B | 0.136411 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution = O and LargestSpotSize != H and LargestSpotSize != A and Evolution != 1 and C-class != 1 | C | 0.103066 |
| SpotDistribution = O and LargestSpotSize!=(X) and SpotDistribution != I and LargestSpotSize != X and Activity!=(2) | D | 0.056840 |
| LargestSpotSize = A and SpotDistribution = I and BecomeHist = 2 and Area = 1 | D | 0.044115 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution != O and LargestSpotSize = R | D | 0.017190 |
| LargestSpotSize = K and SpotDistribution = C and BecomeHist = 2 and Area = 2 | E | 0.008125 |
| LargestSpotSize = R and SpotDistribution = O and BecomeHist = 2 and Area = 1 | C | 0.061945 |
| LargestSpotSize = S and SpotDistribution = I and BecomeHist = 2 and Area = 1 | D | 0.010082 |
| LargestSpotSize = S and SpotDistribution = O and BecomeHist = 2 and Area = 1 | C | 0.055477 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution != O and LargestSpotSize != R and HistComplex != 1 and Evolution = 3 and LargestSpotSize != K and LargestSpotSize = A and Activity != 1 and C-class != 0 | E | 0.004086 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution != O and LargestSpotSize != R and HistComplex != 1 and Evolution = 3 and LargestSpotSize = K | D | 0.009520 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution != O and LargestSpotSize != R and HistComplex != 1 and Evolution = 3 and LargestSpotSize != K and LargestSpotSize != A | E | 0.003753 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution = O and LargestSpotSize != H and LargestSpotSize = A and Activity != 1 | E | 0.002870 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution = O and LargestSpotSize != H and LargestSpotSize = A and Activity = 1 and C-class = 0 and HistComplex != 1 and Evolution = 2 | C | 0.004074 |
| SpotDistribution != X and LargestSpotSize != X and Area != 1 and Prev24Hour = 1 and C-class = 0 | F | 0.003393 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution != O and LargestSpotSize != R and HistComplex != 1 and Evolution != 3 and C-class != 1 and C-class != 0 | F | 0.003017 |
| LargestSpotSize = K and SpotDistribution = I and BecomeHist = 2 and Area = 2 | E | 0.002064 |
| LargestSpotSize = K and SpotDistribution = C and BecomeHist = 2 and Area = 1 | E | 0.001529 |
| LargestSpotSize = A and SpotDistribution = C and BecomeHist = 2 and Area = 1 | E | 0.002043 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution = O and LargestSpotSize = H and Evolution = 2 | E | 0.001478 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution != O and LargestSpotSize != R and HistComplex != 1 and Evolution != 3 and C-class != 1 and C-class = 0 and Activity != 1 and LargestSpotSize != A | E | 0.001478 |
| LargestSpotSize = K and SpotDistribution = I and BecomeHist = 2 and Area = 1 | D | 0.008949 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution != O and LargestSpotSize != R and HistComplex != 1 and Evolution = 3 and LargestSpotSize != K and LargestSpotSize = A and Activity != 1 and C-class = 0 | D | 0.003085 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution != O and LargestSpotSize != R and HistComplex != 1 and Evolution != 3 and C-class != 1 and C-class = 0 and Activity != 1 and LargestSpotSize = A | D | 0.002168 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution != O and LargestSpotSize != R and HistComplex = 1 | D | 0.029981 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution != O and LargestSpotSize != R and HistComplex != 1 and Evolution != 3 and C-class != 1 and C-class = 0 and Activity = 1 | D | 0.006567 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = X | H | 0.312042 |
| LargestSpotSize = X | B | 0.198473 |
| Area != 1 and Prev24Hour != 1 | E | 0.015802 |
| SpotDistribution = O and LargestSpotSize != H and LargestSpotSize != A | C | 0.239798 |
| Area != 1 and C-class = 0 | F | 0.009301 |
| LargestSpotSize != R and HistComplex = 1 | D | 0.231997 |
| LargestSpotSize = R | D | 0.231022 |
| SpotDistribution != O and M-class != 0 and LargestSpotSize != A | E | 0.017857 |
| SpotDistribution != O | D | 0.203042 |
| Activity = 1 | D | 0.105841 |
|  | E | 0.467105 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| HistComplex = 2 and SpotDistribution = I and Evolution = 2 and LargestSpotSize = K | F | 0.003019 |
| HistComplex = 2 and Activity = 2 and SpotDistribution = C and Prev24Hour = 3 and LargestSpotSize = K and Evolution = 2 | E | 0.003452 |
| HistComplex = 2 and Activity = 2 and SpotDistribution = C | E | 0.006970 |
| HistComplex = 2 and SpotDistribution = I and LargestSpotSize = S and Evolution = 2 and Activity = 1 and M-class = 0 | E | 0.002592 |
| HistComplex = 2 and SpotDistribution = I and Evolution = 3 and C-class = 1 | E | 0.004147 |
| LargestSpotSize = A and HistComplex = 2 and C-class = 4 | E | 0.002592 |
| HistComplex = 2 and SpotDistribution = I and C-class = 3 and Evolution = 2 | E | 0.002076 |
| LargestSpotSize = X | B | 0.141458 |
| SpotDistribution = O and HistComplex = 1 and Evolution = 2 and LargestSpotSize = S and Activity = 2 | C | 0.010091 |
| SpotDistribution = O and HistComplex = 1 and Evolution = 2 and LargestSpotSize = S | C | 0.022023 |
| SpotDistribution = O and LargestSpotSize = R and Evolution = 2 and C-class = 0 and HistComplex = 2 | C | 0.006887 |
| SpotDistribution = O and LargestSpotSize = R and Evolution = 2 and C-class = 0 | C | 0.028016 |
| SpotDistribution = O and HistComplex = 1 and LargestSpotSize = R and C-class = 0 and Evolution = 1 | C | 0.005298 |
| SpotDistribution = O and HistComplex = 1 and LargestSpotSize = R and C-class = 0 and M-class = 0 | C | 0.035237 |
| SpotDistribution = O and LargestSpotSize = S and HistComplex = 1 and C-class = 0 and Activity = 2 and Prev24Hour = 1 | C | 0.003731 |
| SpotDistribution = O and LargestSpotSize = S and HistComplex = 1 and C-class = 0 | C | 0.016639 |
| SpotDistribution = O and LargestSpotSize = S and Evolution = 2 and C-class = 0 | C | 0.009246 |
| SpotDistribution = O and Activity = 1 and Evolution = 3 and LargestSpotSize = S and HistComplex = 2 | C | 0.007375 |
| SpotDistribution = I and Evolution = 3 and LargestSpotSize = A and HistComplex = 1 and C-class = 1 | D | 0.006742 |
| SpotDistribution = I and Evolution = 3 and LargestSpotSize = A and HistComplex = 1 and C-class = 0 | D | 0.024871 |
| SpotDistribution = I and Evolution = 3 and LargestSpotSize = K and Area = 1 | D | 0.017778 |
| SpotDistribution = I and Evolution = 3 and LargestSpotSize = R and HistComplex = 2 | D | 0.009342 |
| SpotDistribution = I and Evolution = 3 and LargestSpotSize = A and C-class = 3 | D | 0.008969 |
| SpotDistribution = I and HistComplex = 1 and C-class = 0 and LargestSpotSize = A | D | 0.006006 |
| SpotDistribution = I and Evolution = 3 and C-class = 0 and M-class = 1 | D | 0.006742 |
| SpotDistribution = I and LargestSpotSize = R and C-class = 0 and Evolution = 2 and HistComplex = 2 | D | 0.008969 |
| SpotDistribution = O and Evolution = 3 and C-class = 1 and LargestSpotSize = A | D | 0.006742 |
| SpotDistribution = O and Evolution = 3 and Activity = 2 and LargestSpotSize = A | D | 0.005068 |
| SpotDistribution = I and Evolution = 3 and HistComplex = 1 and C-class = 0 | D | 0.015409 |
| SpotDistribution = O and Evolution = 3 and C-class = 1 and LargestSpotSize = R | D | 0.005068 |
| SpotDistribution = O and LargestSpotSize = S and C-class = 1 | D | 0.011063 |
| SpotDistribution = I and C-class = 1 and Activity = 2 and X-class = 0 | D | 0.009342 |
| SpotDistribution = O and C-class = 0 and Evolution = 3 and LargestSpotSize = H | D | 0.006006 |
| LargestSpotSize = A and SpotDistribution = I and Evolution = 3 and Activity = 1 | D | 0.013219 |
| SpotDistribution = O and C-class = 0 and Evolution = 3 and LargestSpotSize = R and Area = 1 | D | 0.043388 |
|  | H | 0.547794 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

largestspotsize|spotdistribution|becomehist|area|class
---|---|---|---|---
a|c|2|2|h
k|c|2|2|e
k|i|2|2|e
r|o|2|2|h
r|c|2|1|d
k|c|2|1|e
h|c|2|1|h
a|c|2|1|e
h|i|2|1|e
x|i|2|1|b
s|i|2|1|d
r|i|2|1|d
k|i|2|1|d
a|i|2|1|d
h|o|2|1|d
x|o|2|1|b
k|o|2|1|h
r|o|2|1|c
a|o|2|1|d
s|o|2|1|c
h|x|2|1|h
a|x|2|1|h
r|x|2|1|h
s|x|2|1|h
k|x|1|1|h
h|x|1|1|h
a|x|1|1|h
r|x|1|1|h
s|x|1|1|h

## JRip

Decision list:

rules | predicted class
---|---
(HistComplex = 2) and (SpotDistribution = I) and (Evolution = 2) and (LargestSpotSize = K)|F (9.0/4.0)
(HistComplex = 2) and (Activity = 2) and (SpotDistribution = C) and (Prev24Hour = 3) and (LargestSpotSize = K) and (Evolution = 2)|E (3.0/0.0)
(HistComplex = 2) and (Activity = 2) and (SpotDistribution = C)|E (20.0/9.0)
(HistComplex = 2) and (SpotDistribution = I) and (LargestSpotSize = S) and (Evolution = 2) and (Activity = 1) and (M-class = 0)|E (4.0/1.0)
(HistComplex = 2) and (SpotDistribution = I) and (Evolution = 3) and (C-class = 1)|E (10.0/4.0)
(LargestSpotSize = A) and (HistComplex = 2) and (C-class = 4)|E (4.0/1.0)
(HistComplex = 2) and (SpotDistribution = I) and (C-class = 3) and (Evolution = 2)|E (4.0/1.0)
(LargestSpotSize = X)|B (130.0/0.0)
(SpotDistribution = O) and (HistComplex = 1) and (Evolution = 2) and (LargestSpotSize = S) and (Activity = 2)|C (8.0/1.0)
(SpotDistribution = O) and (HistComplex = 1) and (Evolution = 2) and (LargestSpotSize = S)|C (23.0/5.0)
(SpotDistribution = O) and (LargestSpotSize = R) and (Evolution = 2) and (C-class = 0) and (HistComplex = 2)|C (6.0/1.0)
(SpotDistribution = O) and (LargestSpotSize = R) and (Evolution = 2) and (C-class = 0)|C (27.0/5.0)
(SpotDistribution = O) and (HistComplex = 1) and (LargestSpotSize = R) and (C-class = 0) and (Evolution = 1)|C (5.0/1.0)
(SpotDistribution = O) and (HistComplex = 1) and (LargestSpotSize = R) and (C-class = 0) and (M-class = 0)|C (54.0/18.0)
(SpotDistribution = O) and (LargestSpotSize = S) and (HistComplex = 1) and (C-class = 0) and (Activity = 2) and (Prev24Hour = 1)|C (3.0/0.0)
(SpotDistribution = O) and (LargestSpotSize = S) and (HistComplex = 1) and (C-class = 0)|C (35.0/15.0)
(SpotDistribution = O) and (LargestSpotSize = S) and (Evolution = 2) and (C-class = 0)|C (21.0/9.0)
(SpotDistribution = O) and (Activity = 1) and (Evolution = 3) and (LargestSpotSize = S) and (HistComplex = 2)|C (11.0/4.0)
(SpotDistribution = I) and (Evolution = 3) and (LargestSpotSize = A) and (HistComplex = 1) and (C-class = 1)|D (3.0/0.0)
(SpotDistribution = I) and (Evolution = 3) and (LargestSpotSize = A) and (HistComplex = 1) and (C-class = 0)|D (15.0/2.0)
(SpotDistribution = I) and (Evolution = 3) and (LargestSpotSize = K) and (Area = 1)|D (7.0/0.0)
(SpotDistribution = I) and (Evolution = 3) and (LargestSpotSize = R) and (HistComplex = 2)|D (5.0/1.0)
(SpotDistribution = I) and (Evolution = 3) and (LargestSpotSize = A) and (C-class = 3)|D (4.0/0.0)
(SpotDistribution = I) and (HistComplex = 1) and (C-class = 0) and (LargestSpotSize = A)|D (4.0/0.0)
(SpotDistribution = I) and (Evolution = 3) and (C-class = 0) and (M-class = 1)|D (3.0/0.0)
(SpotDistribution = I) and (LargestSpotSize = R) and (C-class = 0) and (Evolution = 2) and (HistComplex = 2)|D (4.0/0.0)
(SpotDistribution = O) and (Evolution = 3) and (C-class = 1) and (LargestSpotSize = A)|D (3.0/0.0)
(SpotDistribution = O) and (Evolution = 3) and (Activity = 2) and (LargestSpotSize = A)|D (4.0/1.0)
(SpotDistribution = I) and (Evolution = 3) and (HistComplex = 1) and (C-class = 0)|D (19.0/7.0)
(SpotDistribution = O) and (Evolution = 3) and (C-class = 1) and (LargestSpotSize = R)|D (4.0/1.0)
(SpotDistribution = O) and (LargestSpotSize = S) and (C-class = 1)|D (13.0/5.0)
(SpotDistribution = I) and (C-class = 1) and (Activity = 2) and (X-class = 0)|D (5.0/1.0)
(SpotDistribution = O) and (C-class = 0) and (Evolution = 3) and (LargestSpotSize = H)|D (6.0/2.0)
(LargestSpotSize = A) and (SpotDistribution = I) and (Evolution = 3) and (Activity = 1)|D (13.0/5.0)
(SpotDistribution = O) and (C-class = 0) and (Evolution = 3) and (LargestSpotSize = R) and (Area = 1)|D (4.0/1.0)
|H (462.0/164.0)


## PART

Decision list:

rules | predicted class
---|---
SpotDistribution = X|H (298.0)
LargestSpotSize = X|B (130.0)
Area != 1 AND Prev24Hour != 1|E (9.0/1.0)
SpotDistribution = O AND LargestSpotSize != H AND LargestSpotSize != A|C (238.0/89.0)
Area != 1 AND C-class = 0|F (7.0/2.0)
LargestSpotSize != R AND HistComplex = 1|D (67.0/23.0)
LargestSpotSize = R|D (28.0/9.0)
SpotDistribution != O AND M-class != 0 AND LargestSpotSize != A|E (8.0/3.0)
SpotDistribution != O|D (124.0/69.0)
Activity = 1|D (35.0/18.0)
|E (11.0/3.0)


## J48 Decision Tree

* SpotDistribution = X: H (298.0)
* SpotDistribution != X
	* LargestSpotSize = X: B (130.0)
	* LargestSpotSize != X
		* Area = 1
			* SpotDistribution = O
				* LargestSpotSize = H
					* Evolution = 2: E (7.0/4.0)
					* Evolution != 2: D (7.0/3.0)
				* LargestSpotSize != H
					* LargestSpotSize = A
						* Activity = 1
							* C-class = 0
								* HistComplex = 1: D (14.0/7.0)
								* HistComplex != 1
									* Evolution = 2: C (8.0/3.0)
									* Evolution != 2: D (13.0/6.0)
							* C-class != 0: D (9.0/4.0)
						* Activity != 1: E (10.0/5.0)
					* LargestSpotSize != A
						* Evolution = 1
							* LargestSpotSize = R: C (8.0/2.0)
							* LargestSpotSize != R: D (10.0/6.0)
						* Evolution != 1
							* C-class = 1
								* LargestSpotSize = R: D (7.0/2.0)
								* LargestSpotSize != R
									* Evolution = 2: C (8.0/3.0)
									* Evolution != 2: D (9.0/4.0)
							* C-class != 1: C (195.0/66.0)
			* SpotDistribution != O
				* LargestSpotSize = R: D (28.0/9.0)
				* LargestSpotSize != R
					* HistComplex = 1: D (45.0/13.0)
					* HistComplex != 1
						* Evolution = 3
							* LargestSpotSize = K: D (9.0/1.0)
							* LargestSpotSize != K
								* LargestSpotSize = A
									* Activity = 1: D (21.0/7.0)
									* Activity != 1
										* C-class = 0: D (7.0/3.0)
										* C-class != 0: E (7.0/2.0)
								* LargestSpotSize != A: E (11.0/5.0)
						* Evolution != 3
							* C-class = 1: D (15.0/7.0)
							* C-class != 1
								* C-class = 0
									* Activity = 1: D (25.0/14.0)
									* Activity != 1
										* LargestSpotSize = A: D (10.0/6.0)
										* LargestSpotSize != A: E (7.0/4.0)
								* C-class != 0: F (13.0/7.0)
		* Area != 1
			* Prev24Hour = 1
				* C-class = 0: F (8.0/3.0)
				* C-class != 0: E (7.0/3.0)
			* Prev24Hour != 1: E (9.0/1.0)


## SimpleCart Decision Tree

		* SpotDistribution=(C)|(I)|(O)
	* LargestSpotSize=(X): B(130.0/0.0)
	* LargestSpotSize!=(X)
			* SpotDistribution=(C)|(I)
			* Area=(2)
					* Prev24Hour=(3)|(2): E(8.0/1.0)
					* Prev24Hour!=(3)|(2): F(7.0/7.0)
			* Area!=(2)
				* HistComplex=(2)
					* Evolution=(3)
						* LargestSpotSize=(S): D(3.0/5.0)
						* LargestSpotSize!=(S)
								* LargestSpotSize=(K)|(R): D(14.0/2.0)
								* LargestSpotSize!=(K)|(R): D(20.0/18.0)
					* Evolution!=(3)
										* C-class=(0)|(1)|(6)|(7)|(8): D(28.0/35.0)
										* C-class!=(0)|(1)|(6)|(7)|(8): F(6.0/7.0)
				* HistComplex!=(2)
									* LargestSpotSize=(S)|(R)|(X)|(K)|(H): D(18.0/14.0)
									* LargestSpotSize!=(S)|(R)|(X)|(K)|(H): D(23.0/5.0)
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


