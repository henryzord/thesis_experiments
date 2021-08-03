# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = X | H | 0.311390 |
| SpotDistribution != X and LargestSpotSize = X | B | 0.134031 |
| SpotDistribution = O and LargestSpotSize!=(X) and SpotDistribution != I | C | 0.100678 |
| LargestSpotSize = A and SpotDistribution = I and Area = 1 and X-class = 0 | D | 0.041956 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution = O and LargestSpotSize != A and LargestSpotSize != H and C-class = 1 | D | 0.010523 |
| LargestSpotSize = A and SpotDistribution = O and Area = 1 and X-class = 0 | D | 0.012458 |
| LargestSpotSize = R and SpotDistribution = I and Area = 1 and X-class = 0 | D | 0.015979 |
| LargestSpotSize = S and SpotDistribution = I and Area = 1 and X-class = 0 | D | 0.012492 |
| LargestSpotSize = K and SpotDistribution = I and Area = 1 and X-class = 0 | D | 0.010270 |
| SpotDistribution != X and LargestSpotSize != X and Area != 1 and Prev24Hour != 1 | E | 0.008090 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution = O and LargestSpotSize = A and C-class != 0 | E | 0.005091 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution = O and LargestSpotSize != A and LargestSpotSize = H | D | 0.005073 |
| SpotDistribution != X and LargestSpotSize != X and Area != 1 and Prev24Hour = 1 | F | 0.006387 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution != O and HistComplex != 1 and LargestSpotSize != R and M-class = 0 and C-class != 2 and Evolution = 3 and Activity != 1 | E | 0.003179 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution != O and HistComplex != 1 and LargestSpotSize != R and M-class = 0 and C-class != 2 and Evolution != 3 and LargestSpotSize = S | E | 0.002609 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution = O and LargestSpotSize != A and LargestSpotSize != H and C-class != 1 and LargestSpotSize = S and C-class != 0 | D | 0.002162 |
| LargestSpotSize = A and SpotDistribution = C and Area = 1 and X-class = 0 | D | 0.002695 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution != O and HistComplex != 1 and LargestSpotSize != R and M-class = 0 and C-class != 2 and Evolution != 3 and LargestSpotSize != S and Activity != 1 and C-class != 0 | F | 0.001939 |
| LargestSpotSize = K and SpotDistribution = C and Area = 1 and X-class = 0 | E | 0.001527 |
| LargestSpotSize = R and SpotDistribution = C and Area = 1 and X-class = 0 | D | 0.001795 |
| LargestSpotSize = K and SpotDistribution = C and Area = 2 and X-class = 0 | E | 0.006088 |
| LargestSpotSize = H and SpotDistribution = I and Area = 1 and X-class = 0 | D | 0.000450 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = X | H | 0.311390 |
| LargestSpotSize = X | B | 0.194825 |
| SpotDistribution = O and C-class = 0 and LargestSpotSize = R | C | 0.127892 |
| Area = 2 and X-class = 0 and LargestSpotSize = K | E | 0.017737 |
| SpotDistribution = O and C-class = 1 | D | 0.034188 |
| SpotDistribution = C | E | 0.009561 |
| SpotDistribution = O and C-class = 3 and HistComplex = 1 | C | 0.007329 |
| SpotDistribution = O and C-class = 0 and LargestSpotSize = S | C | 0.118273 |
| HistComplex = 1 | D | 0.298491 |
| SpotDistribution = O and Activity = 2 and Prev24Hour = 1 | E | 0.028244 |
| SpotDistribution = O and M-class = 0 | D | 0.106878 |
| LargestSpotSize = R | D | 0.032703 |
| C-class = 3 and LargestSpotSize = A and Evolution = 3 | D | 0.014706 |
| C-class = 1 and Area = 1 | D | 0.022358 |
|  | D | 0.233503 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Area = 2 and Prev24Hour = 1 | F | 0.006387 |
| SpotDistribution = I and Evolution = 2 and Activity = 2 and LargestSpotSize = A | F | 0.003150 |
| Activity = 2 and SpotDistribution = C | E | 0.011349 |
| LargestSpotSize = A and HistComplex = 2 and Activity = 2 | E | 0.006039 |
| LargestSpotSize = X | B | 0.140659 |
| SpotDistribution = O and LargestSpotSize = R | C | 0.080169 |
| SpotDistribution = O and LargestSpotSize = S and C-class = 0 | C | 0.062964 |
| SpotDistribution = I | D | 0.136461 |
| SpotDistribution = O and Evolution = 3 | D | 0.096383 |
|  | H | 0.624738 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

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
r|c|1|0|d
a|c|1|0|d
r|o|2|0|h
x|i|1|0|b
r|i|1|0|d
k|i|1|0|d
s|i|1|0|d
h|i|1|0|d
a|i|1|0|d
k|o|1|0|h
x|o|1|0|b
r|o|1|0|c
h|o|1|0|d
a|o|1|0|d
s|o|1|0|c
k|x|1|0|h
h|x|1|0|h
r|x|1|0|h
a|x|1|0|h
s|x|1|0|h

## JRip

Decision list:

rules | predicted class
---|---
(Area = 2) and (Prev24Hour = 1)|F (17.0/7.0)
(SpotDistribution = I) and (Evolution = 2) and (Activity = 2) and (LargestSpotSize = A)|F (17.0/10.0)
(Activity = 2) and (SpotDistribution = C)|E (20.0/7.0)
(LargestSpotSize = A) and (HistComplex = 2) and (Activity = 2)|E (21.0/10.0)
(LargestSpotSize = X)|B (128.0/0.0)
(SpotDistribution = O) and (LargestSpotSize = R)|C (113.0/37.0)
(SpotDistribution = O) and (LargestSpotSize = S) and (C-class = 0)|C (102.0/39.0)
(SpotDistribution = I)|D (152.0/59.0)
(SpotDistribution = O) and (Evolution = 3)|D (47.0/22.0)
|H (340.0/43.0)


## PART

Decision list:

rules | predicted class
---|---
SpotDistribution = X|H (298.0)
LargestSpotSize = X|B (128.0)
SpotDistribution = O AND C-class = 0 AND LargestSpotSize = R|C (104.0/33.0)
Area = 2 AND X-class = 0 AND LargestSpotSize = K|E (18.0/7.0)
SpotDistribution = O AND C-class = 1|D (32.0/16.0)
SpotDistribution = C|E (20.0/11.0)
SpotDistribution = O AND C-class = 3 AND HistComplex = 1|C (4.0/1.0)
SpotDistribution = O AND C-class = 0 AND LargestSpotSize = S|C (102.0/39.0)
HistComplex = 1|D (80.0/31.0)
SpotDistribution = O AND Activity = 2 AND Prev24Hour = 1|E (5.0)
SpotDistribution = O AND M-class = 0|D (35.0/16.0)
LargestSpotSize = R|D (13.0/3.0)
C-class = 3 AND LargestSpotSize = A AND Evolution = 3|D (4.0/1.0)
C-class = 1 AND Area = 1|D (21.0/10.0)
|D (93.0/51.0)


## J48 Decision Tree

* SpotDistribution = X: H (298.0)
* SpotDistribution != X
	* LargestSpotSize = X: B (128.0)
	* LargestSpotSize != X
		* Area = 1
			* SpotDistribution = O
				* LargestSpotSize = A
					* C-class = 0
						* Evolution = 2: C (17.0/9.0)
						* Evolution != 2: D (25.0/12.0)
					* C-class != 0: E (11.0/4.0)
				* LargestSpotSize != A
					* LargestSpotSize = H: D (13.0/6.0)
					* LargestSpotSize != H
						* C-class = 1: D (25.0/11.0)
						* C-class != 1
							* LargestSpotSize = S
								* C-class = 0: C (102.0/39.0)
								* C-class != 0: D (10.0/6.0)
							* LargestSpotSize != S: C (106.0/32.0)
			* SpotDistribution != O
				* HistComplex = 1: D (58.0/18.0)
				* HistComplex != 1
					* LargestSpotSize = R: D (14.0/3.0)
					* LargestSpotSize != R
						* M-class = 0
							* C-class = 2: D (11.0/5.0)
							* C-class != 2
								* Evolution = 3
									* Activity = 1: D (28.0/11.0)
									* Activity != 1: E (13.0/7.0)
								* Evolution != 3
									* LargestSpotSize = S: E (11.0/6.0)
									* LargestSpotSize != S
										* Activity = 1: D (27.0/16.0)
										* Activity != 1
											* C-class = 0: D (14.0/8.0)
											* C-class != 0: F (9.0/5.0)
						* M-class != 0: D (11.0/4.0)
		* Area != 1
			* Prev24Hour = 1: F (17.0/7.0)
			* Prev24Hour != 1: E (9.0/1.0)


## SimpleCart Decision Tree

		* SpotDistribution=(C)|(I)|(O)
	* LargestSpotSize=(X): B(128.0/0.0)
	* LargestSpotSize!=(X)
			* SpotDistribution=(C)|(I)
			* Area=(2): E(13.0/12.0)
			* Area!=(2): D(110.0/86.0)
			* SpotDistribution!=(C)|(I): C(171.0/139.0)
		* SpotDistribution!=(C)|(I)|(O): H(298.0/0.0)


