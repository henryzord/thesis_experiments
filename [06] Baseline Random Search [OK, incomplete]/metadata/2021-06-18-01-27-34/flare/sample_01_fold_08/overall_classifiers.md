# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = X | H | 0.311065 |
| SpotDistribution != X and LargestSpotSize = X | B | 0.134796 |
| SpotDistribution = O and LargestSpotSize!=(X) and SpotDistribution != C | C | 0.099918 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution != O | D | 0.075164 |
| LargestSpotSize = A and SpotDistribution = O and Area = 1 | D | 0.015329 |
| SpotDistribution != X and LargestSpotSize != X and Area != 1 | E | 0.008057 |
| LargestSpotSize = A and SpotDistribution = C and Area = 1 | E | 0.003182 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution = O and LargestSpotSize = H | D | 0.003470 |
| LargestSpotSize = K and SpotDistribution = I and Area = 2 | F | 0.001957 |
| LargestSpotSize = A and SpotDistribution = I and Area = 2 | F | 0.002172 |
| LargestSpotSize = K and SpotDistribution = C and Area = 1 | E | 0.001527 |
| LargestSpotSize = H and SpotDistribution = I and Area = 1 | E | 0.000573 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = X | H | 0.311065 |
| LargestSpotSize = X | B | 0.195751 |
| SpotDistribution = C and LargestSpotSize = K and M-class = 0 and Prev24Hour = 1 | F | 0.005398 |
| SpotDistribution = C and Area = 1 and Evolution = 3 and Activity = 2 | D | 0.005751 |
| SpotDistribution = O and C-class = 0 and HistComplex = 1 and LargestSpotSize = R | C | 0.116063 |
| SpotDistribution = O and C-class = 0 and LargestSpotSize = S | C | 0.100973 |
| Area = 2 and Prev24Hour = 1 and Evolution = 3 and Activity = 2 | F | 0.004087 |
| SpotDistribution = C | E | 0.045999 |
| SpotDistribution = O and Activity = 2 and HistComplex = 2 and Prev24Hour = 1 | E | 0.021160 |
| SpotDistribution = O and M-class = 0 and LargestSpotSize = R | C | 0.014184 |
| SpotDistribution = O and M-class = 0 and LargestSpotSize = S | C | 0.007421 |
| HistComplex = 1 | D | 0.368936 |
| SpotDistribution = O and C-class = 0 and Evolution = 3 | D | 0.067164 |
| SpotDistribution = I and Evolution = 3 and LargestSpotSize = A and C-class = 0 | D | 0.040850 |
| SpotDistribution = I and Evolution = 3 | D | 0.083300 |
| SpotDistribution = O and C-class = 0 | C | 0.056742 |
| LargestSpotSize = A and C-class = 0 | D | 0.068383 |
| LargestSpotSize = A and SpotDistribution = I | D | 0.012727 |
| LargestSpotSize = S | D | 0.074822 |
| LargestSpotSize = K | F | 0.024725 |
| LargestSpotSize = A | E | 0.266389 |
|  | D | 0.159091 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| HistComplex = 2 and Activity = 2 and SpotDistribution = C | E | 0.010618 |
| HistComplex = 2 and LargestSpotSize = A and SpotDistribution = O and Activity = 2 and Prev24Hour = 1 | E | 0.005701 |
| LargestSpotSize = X | B | 0.137527 |
| SpotDistribution = O and HistComplex = 1 | C | 0.118410 |
| SpotDistribution = O and C-class = 0 and Evolution = 2 | C | 0.016580 |
| SpotDistribution = I and Evolution = 3 | D | 0.088927 |
| SpotDistribution = O and Evolution = 3 | D | 0.104125 |
|  | H | 0.568702 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

largestspotsize|spotdistribution|area|class
---|---|---|---
a|c|2|h
k|c|2|e
a|i|2|f
k|i|2|f
r|o|2|h
h|c|1|h
r|c|1|d
k|c|1|e
a|c|1|e
h|i|1|e
x|i|1|b
k|i|1|d
s|i|1|d
r|i|1|d
a|i|1|d
h|o|1|d
k|o|1|h
x|o|1|b
a|o|1|d
s|o|1|c
r|o|1|c
k|x|1|h
h|x|1|h
r|x|1|h
s|x|1|h
a|x|1|h

## JRip

Decision list:

rules | predicted class
---|---
(HistComplex = 2) and (Activity = 2) and (SpotDistribution = C)|E (21.0/7.0)
(HistComplex = 2) and (LargestSpotSize = A) and (SpotDistribution = O) and (Activity = 2) and (Prev24Hour = 1)|E (5.0/0.0)
(LargestSpotSize = X)|B (129.0/0.0)
(SpotDistribution = O) and (HistComplex = 1)|C (203.0/76.0)
(SpotDistribution = O) and (C-class = 0) and (Evolution = 2)|C (46.0/21.0)
(SpotDistribution = I) and (Evolution = 3)|D (104.0/38.0)
(SpotDistribution = O) and (Evolution = 3)|D (37.0/16.0)
|H (413.0/115.0)


## PART

Decision list:

rules | predicted class
---|---
SpotDistribution = X|H (298.0)
LargestSpotSize = X|B (129.0)
SpotDistribution = C AND LargestSpotSize = K AND M-class = 0 AND Prev24Hour = 1|F (6.0/2.0)
SpotDistribution = C AND Area = 1 AND Evolution = 3 AND Activity = 2|D (5.0/2.0)
SpotDistribution = O AND C-class = 0 AND HistComplex = 1 AND LargestSpotSize = R|C (90.0/28.0)
SpotDistribution = O AND C-class = 0 AND LargestSpotSize = S|C (101.0/41.0)
Area = 2 AND Prev24Hour = 1 AND Evolution = 3 AND Activity = 2|F (5.0/2.0)
SpotDistribution = C|E (18.0/4.0)
SpotDistribution = O AND Activity = 2 AND HistComplex = 2 AND Prev24Hour = 1|E (10.0/1.0)
SpotDistribution = O AND M-class = 0 AND LargestSpotSize = R|C (22.0/8.0)
SpotDistribution = O AND M-class = 0 AND LargestSpotSize = S|C (20.0/9.0)
HistComplex = 1|D (82.0/31.0)
SpotDistribution = O AND C-class = 0 AND Evolution = 3|D (17.0/7.0)
SpotDistribution = I AND Evolution = 3 AND LargestSpotSize = A AND C-class = 0|D (16.0/6.0)
SpotDistribution = I AND Evolution = 3|D (41.0/16.0)
SpotDistribution = O AND C-class = 0|C (16.0/9.0)
LargestSpotSize = A AND C-class = 0|D (27.0/16.0)
LargestSpotSize = A AND SpotDistribution = I|D (17.0/10.0)
LargestSpotSize = S|D (14.0/8.0)
LargestSpotSize = K|F (11.0/6.0)
LargestSpotSize = A|E (7.0/3.0)
|D (6.0/4.0)


## J48 Decision Tree

* SpotDistribution = X: H (298.0)
* SpotDistribution != X
	* LargestSpotSize = X: B (129.0)
	* LargestSpotSize != X
		* Area = 1
			* SpotDistribution = O
				* LargestSpotSize = H: D (14.0/8.0)
				* LargestSpotSize != H
					* LargestSpotSize = A
						* Evolution = 2: C (26.0/16.0)
						* Evolution != 2: D (34.0/15.0)
					* LargestSpotSize != A: C (240.0/92.0)
			* SpotDistribution != O: D (193.0/88.0)
		* Area != 1: E (24.0/11.0)


## SimpleCart Decision Tree

		* SpotDistribution=(C)|(I)|(O)
	* LargestSpotSize=(X): B(129.0/0.0)
	* LargestSpotSize!=(X)
			* SpotDistribution=(C)|(I): D(106.0/110.0)
			* SpotDistribution!=(C)|(I): C(171.0/144.0)
		* SpotDistribution!=(C)|(I)|(O): H(298.0/0.0)


