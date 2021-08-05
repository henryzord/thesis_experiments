# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = X | H | 0.311715 |
| SpotDistribution = O and LargestSpotSize = X | B | 0.122210 |
| SpotDistribution = O and LargestSpotSize!=(X) and SpotDistribution != I | C | 0.098973 |
| SpotDistribution = I and LargestSpotSize = A | D | 0.043153 |
| SpotDistribution = O and LargestSpotSize = A | D | 0.014032 |
| SpotDistribution = I and LargestSpotSize = R | D | 0.015449 |
| SpotDistribution = C | E | 0.011931 |
| SpotDistribution = I and LargestSpotSize = K and Area = 1 | D | 0.011324 |
| SpotDistribution = I and LargestSpotSize = S | D | 0.010068 |
| SpotDistribution = I and LargestSpotSize = X | B | 0.015495 |
| SpotDistribution = O and LargestSpotSize = H | D | 0.003480 |
| SpotDistribution = I and LargestSpotSize = K and Area = 2 | E | 0.001722 |
| SpotDistribution = I and LargestSpotSize = H | E | 0.001529 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = X | H | 0.311715 |
| LargestSpotSize != X and Area = 1 and SpotDistribution = O and LargestSpotSize != H and LargestSpotSize != A | C | 0.174569 |
| LargestSpotSize = X | B | 0.251969 |
| Area = 1 and HistComplex = 1 | D | 0.312871 |
| Area = 1 and LargestSpotSize != R and SpotDistribution != O and SpotDistribution = I and LargestSpotSize != K and C-class != 2 and M-class = 0 and C-class != 1 and Activity = 1 | D | 0.051666 |
| Area = 1 and LargestSpotSize != R and SpotDistribution != O and SpotDistribution = I and M-class = 0 and Evolution != 2 | D | 0.040533 |
| Area != 1 | E | 0.047805 |
| LargestSpotSize = R | D | 0.053419 |
| SpotDistribution != O and Evolution != 2 | E | 0.078884 |
| SpotDistribution != O and LargestSpotSize != S and C-class != 0 and C-class = 1 | D | 0.024777 |
| C-class != 0 and SpotDistribution = O | E | 0.050298 |
|  | D | 0.327485 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = I and Area = 2 | F | 0.003397 |
| HistComplex = 2 and SpotDistribution = C | E | 0.010886 |
| LargestSpotSize = X | B | 0.137192 |
| SpotDistribution = O and HistComplex = 1 | C | 0.118655 |
| SpotDistribution = O and Evolution = 2 and C-class = 0 and Activity = 1 | C | 0.017458 |
| SpotDistribution = I | D | 0.126143 |
|  | H | 0.538879 |


# Text representation of classifiers as-is

## JRip

Decision list:

rules | predicted class
---|---
(SpotDistribution = I) and (Area = 2)|F (8.0/3.0)
(HistComplex = 2) and (SpotDistribution = C)|E (27.0/11.0)
(LargestSpotSize = X)|B (128.0/0.0)
(SpotDistribution = O) and (HistComplex = 1)|C (200.0/74.0)
(SpotDistribution = O) and (Evolution = 2) and (C-class = 0) and (Activity = 1)|C (39.0/15.0)
(SpotDistribution = I)|D (181.0/77.0)
|H (373.0/75.0)


## PART

Decision list:

rules | predicted class
---|---
SpotDistribution = X|H (298.0)
LargestSpotSize != X AND Area = 1 AND SpotDistribution = O AND LargestSpotSize != H AND LargestSpotSize != A|C (239.0/91.0)
LargestSpotSize = X|B (128.0)
Area = 1 AND HistComplex = 1|D (77.0/30.0)
Area = 1 AND LargestSpotSize != R AND SpotDistribution != O AND SpotDistribution = I AND LargestSpotSize != K AND C-class != 2 AND M-class = 0 AND C-class != 1 AND Activity = 1|D (41.0/21.0)
Area = 1 AND LargestSpotSize != R AND SpotDistribution != O AND SpotDistribution = I AND M-class = 0 AND Evolution != 2|D (28.0/11.0)
Area != 1|E (25.0/11.0)
LargestSpotSize = R|D (15.0/4.0)
SpotDistribution != O AND Evolution != 2|E (13.0/6.0)
SpotDistribution != O AND LargestSpotSize != S AND C-class != 0 AND C-class = 1|D (12.0/6.0)
C-class != 0 AND SpotDistribution = O|E (14.0/5.0)
|D (66.0/38.0)


## J48 Decision Tree

* SpotDistribution = X: H (298.0)
* SpotDistribution = O
	* LargestSpotSize = A: D (56.0/32.0)
	* LargestSpotSize = R: C (110.0/38.0)
	* LargestSpotSize = S: C (129.0/54.0)
	* LargestSpotSize = X: B (115.0)
	* LargestSpotSize = K: C (1.0)
	* LargestSpotSize = H: D (14.0/8.0)
* SpotDistribution = I
	* LargestSpotSize = A: D (96.0/40.0)
	* LargestSpotSize = R: D (28.0/10.0)
	* LargestSpotSize = S: D (39.0/22.0)
	* LargestSpotSize = X: B (13.0)
	* LargestSpotSize = K
		* Area = 1: D (17.0/5.0)
		* Area = 2: E (6.0/3.0)
	* LargestSpotSize = H: E (3.0/1.0)
* SpotDistribution = C: E (31.0/13.0)


## SimpleCart Decision Tree

		* SpotDistribution=(C)|(I)|(O)
	* LargestSpotSize=(X): B(128.0/0.0)
	* LargestSpotSize!=(X)
			* SpotDistribution=(C)|(I)
			* Area=(2): E(13.0/11.0)
			* Area!=(2): D(109.0/87.0)
			* SpotDistribution!=(C)|(I): C(169.0/141.0)
		* SpotDistribution!=(C)|(I)|(O): H(298.0/0.0)


