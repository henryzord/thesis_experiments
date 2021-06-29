# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = X | H | 0.311390 |
| SpotDistribution = O and LargestSpotSize!=(X) and SpotDistribution != I | C | 0.101203 |
| SpotDistribution = O and LargestSpotSize = X | B | 0.122081 |
| SpotDistribution = I and LargestSpotSize = A | D | 0.041592 |
| LargestSpotSize = A and SpotDistribution = O | D | 0.015164 |
| SpotDistribution = I and LargestSpotSize = R | D | 0.012533 |
| SpotDistribution = C | E | 0.013415 |
| SpotDistribution = I and LargestSpotSize = S | D | 0.010848 |
| SpotDistribution = I and LargestSpotSize = X | B | 0.015476 |
| LargestSpotSize = K and SpotDistribution = I | D | 0.009204 |
| SpotDistribution = O and LargestSpotSize = R and Activity = 1 and C-class = 1 | D | 0.004794 |
| SpotDistribution = O and LargestSpotSize = A and Evolution = 2 and C-class = 1 | E | 0.003055 |
| LargestSpotSize = H and SpotDistribution = O | D | 0.003248 |
| LargestSpotSize = R and SpotDistribution = C | D | 0.001795 |
| LargestSpotSize = H and SpotDistribution = I | E | 0.001529 |

## Ordered rules

### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| HistComplex = 2 and Activity = 2 and SpotDistribution = C and LargestSpotSize = K | E | 0.009188 |
| LargestSpotSize = X | B | 0.135593 |
| SpotDistribution = O and HistComplex = 1 and C-class = 0 and Evolution = 2 and LargestSpotSize = R | C | 0.025402 |
| SpotDistribution = O and HistComplex = 1 and C-class = 0 and LargestSpotSize = S and Evolution = 2 and Activity = 1 | C | 0.018532 |
| SpotDistribution = O and HistComplex = 1 and C-class = 0 and LargestSpotSize = S and Activity = 2 | C | 0.011596 |
| SpotDistribution = O and LargestSpotSize = R and C-class = 0 and HistComplex = 1 | C | 0.039020 |
| SpotDistribution = O and LargestSpotSize = S and C-class = 0 and HistComplex = 1 | C | 0.019146 |
| SpotDistribution = O and Evolution = 2 and C-class = 0 | C | 0.019221 |
| SpotDistribution = I and Evolution = 3 and C-class = 0 | D | 0.067716 |
| SpotDistribution = O and Evolution = 3 and C-class = 1 | D | 0.015080 |
| SpotDistribution = I and Evolution = 3 and Area = 1 | D | 0.019298 |
| SpotDistribution = O and C-class = 0 | D | 0.109820 |
| SpotDistribution = I and C-class = 0 and Activity = 1 | D | 0.013338 |
|  | H | 0.591270 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

largestspotsize|spotdistribution|class
---|---|---
r|c|d
h|c|h
a|c|e
k|c|e
h|i|e
x|i|b
k|i|d
r|i|d
a|i|d
s|i|d
k|o|h
x|o|b
h|o|d
a|o|d
r|o|c
s|o|c
k|x|h
h|x|h
a|x|h
s|x|h
r|x|h

## JRip

Decision list:

rules | predicted class
---|---
(HistComplex = 2) and (Activity = 2) and (SpotDistribution = C) and (LargestSpotSize = K)|E (15.0/4.0)
(LargestSpotSize = X)|B (128.0/0.0)
(SpotDistribution = O) and (HistComplex = 1) and (C-class = 0) and (Evolution = 2) and (LargestSpotSize = R)|C (27.0/6.0)
(SpotDistribution = O) and (HistComplex = 1) and (C-class = 0) and (LargestSpotSize = S) and (Evolution = 2) and (Activity = 1)|C (19.0/4.0)
(SpotDistribution = O) and (HistComplex = 1) and (C-class = 0) and (LargestSpotSize = S) and (Activity = 2)|C (11.0/2.0)
(SpotDistribution = O) and (LargestSpotSize = R) and (C-class = 0) and (HistComplex = 1)|C (61.0/20.0)
(SpotDistribution = O) and (LargestSpotSize = S) and (C-class = 0) and (HistComplex = 1)|C (34.0/12.0)
(SpotDistribution = O) and (Evolution = 2) and (C-class = 0)|C (54.0/26.0)
(SpotDistribution = I) and (Evolution = 3) and (C-class = 0)|D (63.0/17.0)
(SpotDistribution = O) and (Evolution = 3) and (C-class = 1)|D (17.0/6.0)
(SpotDistribution = I) and (Evolution = 3) and (Area = 1)|D (38.0/16.0)
(SpotDistribution = O) and (C-class = 0)|D (53.0/25.0)
(SpotDistribution = I) and (C-class = 0) and (Activity = 1)|D (30.0/14.0)
|H (407.0/109.0)


## J48 Decision Tree

* SpotDistribution = X: H (239.0)
* SpotDistribution = O
	* LargestSpotSize = A
		* Evolution = 1: D (4.0/2.0)
		* Evolution = 2
			* C-class = 0: C (12.0/6.0)
			* C-class = 1: E (3.0/1.0)
			* C-class = 2: D (1.0)
			* C-class = 3: C (0.0)
			* C-class = 4: C (0.0)
			* C-class = 5: C (0.0)
			* C-class = 6: C (0.0)
			* C-class = 7: C (0.0)
			* C-class = 8: C (0.0)
		* Evolution = 3: D (22.0/6.0)
	* LargestSpotSize = R
		* Activity = 1
			* C-class = 0: C (80.0/25.0)
			* C-class = 1: D (5.0/2.0)
			* C-class = 2: C (0.0)
			* C-class = 3: C (1.0)
			* C-class = 4: C (0.0)
			* C-class = 5: C (0.0)
			* C-class = 6: C (0.0)
			* C-class = 7: C (0.0)
			* C-class = 8: C (0.0)
		* Activity = 2: C (3.0/1.0)
	* LargestSpotSize = S: C (102.0/40.0)
	* LargestSpotSize = X: B (93.0)
	* LargestSpotSize = K: C (1.0)
	* LargestSpotSize = H: D (12.0/7.0)
* SpotDistribution = I
	* LargestSpotSize = A: D (78.0/35.0)
	* LargestSpotSize = R: D (18.0/8.0)
	* LargestSpotSize = S: D (32.0/18.0)
	* LargestSpotSize = X: B (10.0)
	* LargestSpotSize = K: D (18.0/7.0)
	* LargestSpotSize = H: E (3.0/1.0)
* SpotDistribution = C: E (29.0/12.0)


## SimpleCart Decision Tree

		* SpotDistribution=(C)|(I)|(O)
	* LargestSpotSize=(X): B(128.0/0.0)
	* LargestSpotSize!=(X)
			* SpotDistribution=(C)|(I): D(108.0/110.0)
			* SpotDistribution!=(C)|(I): C(172.0/141.0)
		* SpotDistribution!=(C)|(I)|(O): H(298.0/0.0)


