# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | H | 0.311390 |
| LargestSpotSize = X and SpotDistribution = O and Area = 1 | B | 0.122081 |
| SpotDistribution = O and LargestSpotSize!=(X) and SpotDistribution != I and LargestSpotSize != X | D | 0.056702 |
| LargestSpotSize = R and SpotDistribution = O and Area = 1 | C | 0.064401 |
| SpotDistribution = O and LargestSpotSize!=(X) and SpotDistribution != I and LargestSpotSize = S | C | 0.054630 |
| LargestSpotSize = A and SpotDistribution = I and Area = 1 | D | 0.040938 |
| LargestSpotSize = X and SpotDistribution = I and Area = 1 | B | 0.015476 |
| LargestSpotSize = S and SpotDistribution = I and Area = 1 | D | 0.012459 |
| LargestSpotSize = K and SpotDistribution = C and Area = 2 | E | 0.007602 |
| LargestSpotSize = K and SpotDistribution = I and Area = 1 | D | 0.012519 |
| LargestSpotSize = R and SpotDistribution = I and Area = 1 | D | 0.012048 |
| LargestSpotSize = A and SpotDistribution = C and Area = 1 | E | 0.003182 |
| LargestSpotSize = K and SpotDistribution = I and Area = 2 | E | 0.002062 |
| LargestSpotSize = A and SpotDistribution = I and Area = 2 | F | 0.002174 |
| LargestSpotSize = K and SpotDistribution = C and Area = 1 | E | 0.001527 |
| LargestSpotSize = R and SpotDistribution = C and Area = 1 | D | 0.001795 |
| SpotDistribution = O and LargestSpotSize!=(X) and SpotDistribution != I and LargestSpotSize = K | C | 0.001302 |
| LargestSpotSize = H and SpotDistribution = I and Area = 1 | E | 0.000573 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = X | H | 0.311390 |
| LargestSpotSize = X | B | 0.194825 |
| SpotDistribution = O and LargestSpotSize = S | C | 0.119275 |
| HistComplex = 1 and SpotDistribution = O and LargestSpotSize = R | C | 0.118281 |
| Area = 1 and LargestSpotSize = R and Evolution = 3 | D | 0.149792 |
| SpotDistribution = I | D | 0.258652 |
| SpotDistribution = O and LargestSpotSize = A | D | 0.066454 |
| SpotDistribution = C | E | 0.069394 |
| LargestSpotSize = H | D | 0.018596 |
|  | C | 0.233645 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = I and Evolution = 2 | F | 0.005151 |
| HistComplex = 2 and Activity = 2 and SpotDistribution = C | E | 0.009837 |
| LargestSpotSize = A and HistComplex = 2 | E | 0.011358 |
| LargestSpotSize = X | B | 0.143820 |
| SpotDistribution = O and LargestSpotSize = R and Evolution = 2 and C-class = 0 and Activity = 1 | C | 0.036096 |
| SpotDistribution = O and HistComplex = 1 and C-class = 0 and LargestSpotSize = S and Evolution = 2 | C | 0.026786 |
| SpotDistribution = O and HistComplex = 1 and LargestSpotSize = R and C-class = 0 | C | 0.044549 |
| SpotDistribution = O and LargestSpotSize = S and HistComplex = 1 and C-class = 0 | C | 0.023988 |
| SpotDistribution = O and LargestSpotSize = S | C | 0.018088 |
| SpotDistribution = O and HistComplex = 1 and Activity = 1 | C | 0.004550 |
| SpotDistribution = I and LargestSpotSize = A | D | 0.105364 |
| SpotDistribution = I and Area = 1 | D | 0.064971 |
| SpotDistribution = O | D | 0.170845 |
|  | H | 0.750630 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

largestspotsize|spotdistribution|area|class
---|---|---|---
a|c|2|h
k|c|2|e
a|i|2|f
k|i|2|e
r|c|1|d
r|o|2|h
a|c|1|e
k|c|1|e
h|i|1|e
k|i|1|d
s|i|1|d
x|i|1|b
a|i|1|d
r|i|1|d
k|o|1|h
h|o|1|d
x|o|1|b
s|o|1|c
a|o|1|d
r|o|1|c
k|x|1|h
a|x|1|h
r|x|1|h
h|x|1|h
s|x|1|h

## JRip

Decision list:

rules | predicted class
---|---
(SpotDistribution = I) and (Evolution = 2)|F (80.0/61.0)
(HistComplex = 2) and (Activity = 2) and (SpotDistribution = C)|E (20.0/7.0)
(LargestSpotSize = A) and (HistComplex = 2)|E (89.0/64.0)
(LargestSpotSize = X)|B (121.0/0.0)
(SpotDistribution = O) and (LargestSpotSize = R) and (Evolution = 2) and (C-class = 0) and (Activity = 1)|C (34.0/7.0)
(SpotDistribution = O) and (HistComplex = 1) and (C-class = 0) and (LargestSpotSize = S) and (Evolution = 2)|C (28.0/7.0)
(SpotDistribution = O) and (HistComplex = 1) and (LargestSpotSize = R) and (C-class = 0)|C (61.0/19.0)
(SpotDistribution = O) and (LargestSpotSize = S) and (HistComplex = 1) and (C-class = 0)|C (38.0/13.0)
(SpotDistribution = O) and (LargestSpotSize = S)|C (65.0/36.0)
(SpotDistribution = O) and (HistComplex = 1) and (Activity = 1)|C (32.0/18.0)
(SpotDistribution = I) and (LargestSpotSize = A)|D (20.0/3.0)
(SpotDistribution = I) and (Area = 1)|D (53.0/17.0)
(SpotDistribution = O)|D (23.0/11.0)
|H (293.0/13.0)


## PART

Decision list:

rules | predicted class
---|---
SpotDistribution = X|H (149.0)
LargestSpotSize = X|B (63.0)
SpotDistribution = O AND LargestSpotSize = S|C (70.0/30.0)
HistComplex = 1 AND SpotDistribution = O AND LargestSpotSize = R|C (48.0/14.0)
Area = 1 AND LargestSpotSize = R AND Evolution = 3|D (11.0/2.0)
SpotDistribution = I|D (77.0/34.0)
SpotDistribution = O AND LargestSpotSize = A|D (27.0/12.0)
SpotDistribution = C|E (16.0/6.0)
LargestSpotSize = H|D (9.0/6.0)
|C (9.0/1.0)


## SimpleCart Decision Tree

		* SpotDistribution=(C)|(I)|(O)
	* LargestSpotSize=(X): B(128.0/0.0)
	* LargestSpotSize!=(X)
			* SpotDistribution=(C)|(I)
			* Area=(2): E(13.0/10.0)
			* Area!=(2): D(107.0/86.0)
			* SpotDistribution!=(C)|(I)
						* LargestSpotSize=(K)|(S)|(R)|(X): C(152.0/92.0)
						* LargestSpotSize!=(K)|(S)|(R)|(X): D(32.0/39.0)
		* SpotDistribution!=(C)|(I)|(O): H(298.0/0.0)


