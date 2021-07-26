# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | H | 0.311065 |
| SpotDistribution = O and LargestSpotSize = X | B | 0.121951 |
| SpotDistribution = O and LargestSpotSize!=(X) and SpotDistribution != I and LargestSpotSize != X | D | 0.055734 |
| SpotDistribution = O and LargestSpotSize!=(X) and SpotDistribution != I and LargestSpotSize = R | C | 0.067421 |
| SpotDistribution = O and LargestSpotSize!=(X) and SpotDistribution != I and LargestSpotSize = S | C | 0.051953 |
| SpotDistribution = I and LargestSpotSize = A | D | 0.041251 |
| SpotDistribution = I and LargestSpotSize = R | D | 0.016549 |
| SpotDistribution = C | E | 0.010997 |
| SpotDistribution = I and LargestSpotSize = X | B | 0.015458 |
| SpotDistribution = I and LargestSpotSize = K and Area = 1 | D | 0.012766 |
| SpotDistribution = I and LargestSpotSize = S and Evolution = 3 | D | 0.008748 |
| LargestSpotSize = S and SpotDistribution = I and HistComplex = 2 and Area = 1 and X-class = 0 | E | 0.003897 |
| SpotDistribution = O and LargestSpotSize = H and Activity = 2 | E | 0.003429 |
| LargestSpotSize = A and SpotDistribution = I and HistComplex = 2 and Area = 2 and X-class = 0 | F | 0.002172 |
| SpotDistribution = I and LargestSpotSize = K and Area = 2 | E | 0.001720 |
| LargestSpotSize = K and SpotDistribution = I and HistComplex = 2 and Area = 2 and X-class = 0 | F | 0.001632 |
| LargestSpotSize = A and SpotDistribution = C and HistComplex = 2 and Area = 1 and X-class = 0 | D | 0.001733 |
| SpotDistribution = I and LargestSpotSize = H | E | 0.001527 |
| SpotDistribution = O and LargestSpotSize = H and Activity = 1 and HistComplex = 1 | C | 0.001734 |
| SpotDistribution = O and LargestSpotSize = K | C | 0.001300 |
| SpotDistribution = I and LargestSpotSize = S and Evolution = 1 | D | 0.001344 |
| LargestSpotSize = H and SpotDistribution = I and HistComplex = 2 and Area = 1 and X-class = 0 | D | 0.000449 |
| LargestSpotSize = R and SpotDistribution = C and HistComplex = 1 and Area = 1 and X-class = 0 | D | 0.000673 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = X | H | 0.311065 |
| LargestSpotSize = X | B | 0.194529 |
| SpotDistribution = C and M-class = 1 | E | 0.007127 |
| SpotDistribution = O and LargestSpotSize = R | C | 0.143313 |
| SpotDistribution = O and LargestSpotSize = S and C-class = 0 and HistComplex = 1 | C | 0.085960 |
| Area = 2 and Prev24Hour = 1 | F | 0.015722 |
| SpotDistribution = I and HistComplex = 2 and Evolution = 3 | D | 0.123138 |
| SpotDistribution = O and LargestSpotSize = S | D | 0.120850 |
| HistComplex = 1 | D | 0.228038 |
| SpotDistribution = C | E | 0.050934 |
| SpotDistribution = O and C-class = 0 and Activity = 1 and LargestSpotSize = A and Evolution = 3 | D | 0.011798 |
| SpotDistribution = O and C-class = 0 and Evolution = 2 and Activity = 1 | C | 0.056952 |
| Prev24Hour = 1 and SpotDistribution = O and Activity = 1 | D | 0.033662 |
| SpotDistribution = I and C-class = 0 | D | 0.041812 |
| SpotDistribution = I and C-class = 1 | D | 0.015685 |
| SpotDistribution = O | E | 0.158730 |
| C-class = 2 | F | 0.013889 |
| Activity = 1 | F | 0.051484 |
|  | E | 0.348214 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| HistComplex = 2 and Activity = 2 and SpotDistribution = C | E | 0.007837 |
| HistComplex = 2 and Activity = 2 and SpotDistribution = O | E | 0.004800 |
| LargestSpotSize = A and C-class = 3 | E | 0.002867 |
| LargestSpotSize = X | B | 0.137783 |
| SpotDistribution = O and LargestSpotSize = R | C | 0.083936 |
| SpotDistribution = O and HistComplex = 1 | C | 0.048398 |
| SpotDistribution = I | D | 0.123200 |
|  | H | 0.534050 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

largestspotsize|spotdistribution|histcomplex|area|x-class|class
---|---|---|---|---|---
k|c|2|2|2|h
k|c|2|2|1|e
a|c|2|2|0|h
a|i|2|1|1|h
k|c|2|2|0|e
a|i|2|2|0|f
k|i|2|2|0|f
h|c|2|1|0|h
r|c|2|1|0|h
k|c|2|1|0|e
a|c|2|1|0|d
h|i|2|1|0|d
x|i|2|1|0|b
r|i|2|1|0|d
s|i|2|1|0|e
k|i|2|1|0|d
a|i|2|1|0|d
a|c|1|1|0|h
r|c|1|1|0|d
x|o|2|1|0|b
r|o|2|1|0|c
a|o|2|1|0|d
h|o|2|1|0|d
s|o|2|1|0|d
h|x|2|1|0|h
x|i|1|1|0|b
r|i|1|1|0|d
a|i|1|1|0|d
s|i|1|1|0|d
r|x|2|1|0|h
a|x|2|1|0|h
s|x|2|1|0|h
k|o|1|1|0|h
x|o|1|1|0|b
h|o|1|1|0|c
s|o|1|1|0|c
r|o|1|1|0|c
a|o|1|1|0|d
k|x|1|1|0|h
a|x|1|1|0|h
r|x|1|1|0|h
h|x|1|1|0|h
s|x|1|1|0|h

## JRip

Decision list:

rules | predicted class
---|---
(HistComplex = 2) and (Activity = 2) and (SpotDistribution = C)|E (21.0/9.0)
(HistComplex = 2) and (Activity = 2) and (SpotDistribution = O)|E (24.0/14.0)
(LargestSpotSize = A) and (C-class = 3)|E (10.0/5.0)
(LargestSpotSize = X)|B (126.0/0.0)
(SpotDistribution = O) and (LargestSpotSize = R)|C (113.0/34.0)
(SpotDistribution = O) and (HistComplex = 1)|C (107.0/44.0)
(SpotDistribution = I)|D (179.0/80.0)
|H (378.0/80.0)


## PART

Decision list:

rules | predicted class
---|---
SpotDistribution = X|H (298.0)
LargestSpotSize = X|B (128.0)
SpotDistribution = C AND M-class = 1|E (5.0/1.0)
SpotDistribution = O AND LargestSpotSize = R|C (114.0/35.0)
SpotDistribution = O AND LargestSpotSize = S AND C-class = 0 AND HistComplex = 1|C (68.0/22.0)
Area = 2 AND Prev24Hour = 1|F (13.0/5.0)
SpotDistribution = I AND HistComplex = 2 AND Evolution = 3|D (61.0/22.0)
SpotDistribution = O AND LargestSpotSize = S|D (63.0/34.0)
HistComplex = 1|D (79.0/31.0)
SpotDistribution = C|E (18.0/7.0)
SpotDistribution = O AND C-class = 0 AND Activity = 1 AND LargestSpotSize = A AND Evolution = 3|D (9.0/4.0)
SpotDistribution = O AND C-class = 0 AND Evolution = 2 AND Activity = 1|C (10.0/5.0)
Prev24Hour = 1 AND SpotDistribution = O AND Activity = 1|D (16.0/8.0)
SpotDistribution = I AND C-class = 0|D (40.0/22.0)
SpotDistribution = I AND C-class = 1|D (12.0/5.0)
SpotDistribution = O|E (11.0/3.0)
C-class = 2|F (5.0/2.0)
Activity = 1|F (4.0/2.0)
|E (4.0/2.0)


## J48 Decision Tree

* SpotDistribution = X: H (298.0)
* SpotDistribution = O
	* LargestSpotSize = A: D (55.0/31.0)
	* LargestSpotSize = R: C (114.0/35.0)
	* LargestSpotSize = S: C (131.0/58.0)
	* LargestSpotSize = X: B (115.0)
	* LargestSpotSize = K: C (1.0)
	* LargestSpotSize = H
		* Activity = 1
			* HistComplex = 1: C (3.0/1.0)
			* HistComplex = 2: D (8.0/3.0)
		* Activity = 2: E (3.0)
* SpotDistribution = I
	* LargestSpotSize = A: D (97.0/42.0)
	* LargestSpotSize = R: D (26.0/8.0)
	* LargestSpotSize = S
		* Evolution = 1: D (1.0)
		* Evolution = 2: E (13.0/7.0)
		* Evolution = 3: D (26.0/13.0)
	* LargestSpotSize = X: B (13.0)
	* LargestSpotSize = K
		* Area = 1: D (15.0/3.0)
		* Area = 2: E (6.0/3.0)
	* LargestSpotSize = H: E (3.0/1.0)
* SpotDistribution = C: E (30.0/13.0)


## SimpleCart Decision Tree

		* SpotDistribution=(C)|(I)|(O)
	* LargestSpotSize=(X): B(128.0/0.0)
	* LargestSpotSize!=(X)
			* SpotDistribution=(C)|(I)
			* Area=(2): E(12.0/11.0)
			* Area!=(2): D(108.0/86.0)
			* SpotDistribution!=(C)|(I)
					* LargestSpotSize=(S)|(R)|(X): C(152.0/93.0)
					* LargestSpotSize!=(S)|(R)|(X): D(29.0/41.0)
		* SpotDistribution!=(C)|(I)|(O): H(298.0/0.0)


