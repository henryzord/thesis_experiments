# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = X | H | 0.312042 |
| SpotDistribution != X and LargestSpotSize = X | B | 0.136411 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution = O and LargestSpotSize != H and LargestSpotSize != A | C | 0.113408 |
| SpotDistribution = O and LargestSpotSize!=(X) and SpotDistribution != I and LargestSpotSize != X and Activity!=(2) | D | 0.056840 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution != O | D | 0.077716 |
| SpotDistribution != X and LargestSpotSize != X and Area != 1 | E | 0.010690 |
| LargestSpotSize = H and SpotDistribution = I | E | 0.002291 |
| LargestSpotSize = K and SpotDistribution = C | E | 0.009635 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = X | H | 0.312042 |
| LargestSpotSize = X | B | 0.198473 |
| SpotDistribution = O and C-class = 0 and LargestSpotSize = S | C | 0.106305 |
| HistComplex = 1 and LargestSpotSize = R and C-class = 0 and SpotDistribution = O | C | 0.120273 |
| Area = 2 and Prev24Hour = 1 and C-class = 0 | F | 0.008515 |
| SpotDistribution = C | E | 0.035023 |
| HistComplex = 1 and C-class = 1 and LargestSpotSize = S | C | 0.015530 |
| SpotDistribution = O and Activity = 2 and Prev24Hour = 1 and Evolution = 2 | E | 0.016644 |
| SpotDistribution = O and LargestSpotSize = R and C-class = 0 | C | 0.004647 |
| HistComplex = 1 | D | 0.359938 |
| SpotDistribution = O and LargestSpotSize = S and Evolution = 2 | D | 0.051557 |
| SpotDistribution = O | D | 0.103125 |
| LargestSpotSize = R | D | 0.031279 |
| M-class = 0 and Evolution = 3 | D | 0.076552 |
| M-class = 0 and C-class = 0 and LargestSpotSize = A and Activity = 1 | D | 0.012759 |
| M-class = 0 and C-class = 1 | D | 0.012072 |
| M-class = 0 and C-class = 0 and LargestSpotSize = S | E | 0.085333 |
| M-class = 0 | F | 0.166840 |
|  | D | 0.144144 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| HistComplex = 2 and SpotDistribution = I and Evolution = 2 and LargestSpotSize = A and Activity = 2 | F | 0.003340 |
| LargestSpotSize = K and Evolution = 2 and Activity = 1 | F | 0.002895 |
| HistComplex = 2 and SpotDistribution = C and Prev24Hour = 1 and M-class = 0 and Area = 2 | F | 0.003471 |
| HistComplex = 2 and Activity = 2 | E | 0.017667 |
| LargestSpotSize = X | B | 0.144444 |
| SpotDistribution = O and HistComplex = 1 and Evolution = 2 | C | 0.060672 |
| SpotDistribution = O and LargestSpotSize = R | C | 0.050576 |
| SpotDistribution = O and LargestSpotSize = S | C | 0.041920 |
| SpotDistribution = I | D | 0.142792 |
| SpotDistribution = O | D | 0.163049 |
|  | H | 0.721550 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

largestspotsize|spotdistribution|class
---|---|---
h|c|h
a|c|d
k|c|e
r|c|d
k|i|d
h|i|e
x|i|b
s|i|d
r|i|d
a|i|d
h|o|d
x|o|b
k|o|h
a|o|d
s|o|c
r|o|c
k|x|h
h|x|h
r|x|h
a|x|h
s|x|h

## JRip

Decision list:

rules | predicted class
---|---
(HistComplex = 2) and (SpotDistribution = I) and (Evolution = 2) and (LargestSpotSize = A) and (Activity = 2)|F (16.0/9.0)
(LargestSpotSize = K) and (Evolution = 2) and (Activity = 1)|F (6.0/2.0)
(HistComplex = 2) and (SpotDistribution = C) and (Prev24Hour = 1) and (M-class = 0) and (Area = 2)|F (5.0/1.0)
(HistComplex = 2) and (Activity = 2)|E (88.0/53.0)
(LargestSpotSize = X)|B (127.0/0.0)
(SpotDistribution = O) and (HistComplex = 1) and (Evolution = 2)|C (66.0/17.0)
(SpotDistribution = O) and (LargestSpotSize = R)|C (79.0/28.0)
(SpotDistribution = O) and (LargestSpotSize = S)|C (88.0/42.0)
(SpotDistribution = I)|D (129.0/52.0)
(SpotDistribution = O)|D (51.0/25.0)
|H (300.0/8.0)


## PART

Decision list:

rules | predicted class
---|---
SpotDistribution = X|H (298.0)
LargestSpotSize = X|B (130.0)
SpotDistribution = O AND C-class = 0 AND LargestSpotSize = S|C (104.0/41.0)
HistComplex = 1 AND LargestSpotSize = R AND C-class = 0 AND SpotDistribution = O|C (88.0/25.0)
Area = 2 AND Prev24Hour = 1 AND C-class = 0|F (8.0/3.0)
SpotDistribution = C|E (28.0/11.0)
HistComplex = 1 AND C-class = 1 AND LargestSpotSize = S|C (13.0/5.0)
SpotDistribution = O AND Activity = 2 AND Prev24Hour = 1 AND Evolution = 2|E (6.0)
SpotDistribution = O AND LargestSpotSize = R AND C-class = 0|C (11.0/4.0)
HistComplex = 1|D (89.0/32.0)
SpotDistribution = O AND LargestSpotSize = S AND Evolution = 2|D (6.0/2.0)
SpotDistribution = O|D (45.0/25.0)
LargestSpotSize = R|D (12.0/3.0)
M-class = 0 AND Evolution = 3|D (46.0/20.0)
M-class = 0 AND C-class = 0 AND LargestSpotSize = A AND Activity = 1|D (18.0/11.0)
M-class = 0 AND C-class = 1|D (14.0/7.0)
M-class = 0 AND C-class = 0 AND LargestSpotSize = S|E (10.0/5.0)
M-class = 0|F (19.0/9.0)
|D (10.0/3.0)


## J48 Decision Tree

* SpotDistribution = X: H (298.0)
* SpotDistribution != X
	* LargestSpotSize = X: B (130.0)
	* LargestSpotSize != X
		* Area = 1
			* SpotDistribution = O
				* LargestSpotSize = H: D (14.0/8.0)
				* LargestSpotSize != H
					* LargestSpotSize = A: D (54.0/29.0)
					* LargestSpotSize != A: C (237.0/88.0)
			* SpotDistribution != O: D (198.0/90.0)
		* Area != 1: E (24.0/9.0)


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
					* Evolution!=(3): C(53.0/15.0)
					* LargestSpotSize!=(S)|(R)|(X)
				* Activity=(2): E(8.0/5.0)
				* Activity!=(2): D(27.0/29.0)
		* SpotDistribution!=(C)|(I)|(O): H(298.0/0.0)


