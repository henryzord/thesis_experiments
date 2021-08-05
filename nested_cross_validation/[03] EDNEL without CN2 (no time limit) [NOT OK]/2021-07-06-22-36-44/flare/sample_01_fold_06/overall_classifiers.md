# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | H | 0.311715 |
| SpotDistribution = O and LargestSpotSize = X | B | 0.122210 |
| SpotDistribution = O and LargestSpotSize!=(X) and SpotDistribution != I and LargestSpotSize != X | D | 0.057069 |
| LargestSpotSize = R and SpotDistribution = O and Area = 1 | C | 0.062951 |
| SpotDistribution = O and LargestSpotSize = S | C | 0.055406 |
| LargestSpotSize = A and SpotDistribution = I and Area = 1 | D | 0.042384 |
| SpotDistribution = C | E | 0.013415 |
| LargestSpotSize = X and SpotDistribution = I and Area = 1 | B | 0.015495 |
| SpotDistribution = I and LargestSpotSize = R | D | 0.012550 |
| LargestSpotSize = S and SpotDistribution = I and Area = 1 | D | 0.010863 |
| LargestSpotSize = K and SpotDistribution = I and Area = 1 | D | 0.011324 |
| LargestSpotSize = A and SpotDistribution = C and Area = 1 | D | 0.002165 |
| LargestSpotSize = A and SpotDistribution = I and Area = 2 | F | 0.002174 |
| LargestSpotSize = H and SpotDistribution = I and Area = 1 | E | 0.001529 |
| LargestSpotSize = R and SpotDistribution = C and Area = 1 | D | 0.001797 |
| LargestSpotSize = K and SpotDistribution = I and Area = 2 | E | 0.001148 |
| SpotDistribution = O and LargestSpotSize!=(X) and SpotDistribution != I and LargestSpotSize = K | C | 0.001304 |
| SpotDistribution = I and LargestSpotSize = H | D | 0.000450 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = X | H | 0.311715 |
| LargestSpotSize = X | B | 0.195122 |
| SpotDistribution = O and LargestSpotSize = S | C | 0.120789 |
| HistComplex = 1 and SpotDistribution = O | C | 0.113018 |
| Area = 1 and SpotDistribution = I | D | 0.304835 |
| Area = 1 and C-class = 0 and Activity = 1 and LargestSpotSize = A | D | 0.041333 |
| Area = 2 | E | 0.045370 |
| LargestSpotSize = R | C | 0.030033 |
| C-class = 0 and Activity = 2 | E | 0.046176 |
| C-class = 1 | E | 0.019630 |
|  | D | 0.480198 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Area = 2 and LargestSpotSize = A | F | 0.003257 |
| HistComplex = 2 and Activity = 2 and SpotDistribution = C | E | 0.011675 |
| LargestSpotSize = X | B | 0.136752 |
| SpotDistribution = O and C-class = 0 and HistComplex = 1 | C | 0.115551 |
| SpotDistribution = O and C-class = 0 and Evolution = 2 | C | 0.017373 |
| SpotDistribution = I and Evolution = 3 | D | 0.091673 |
|  | H | 0.496667 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

largestspotsize|spotdistribution|area|class
---|---|---|---
a|c|2|h
k|c|2|e
k|i|2|e
a|i|2|f
r|c|1|d
k|c|1|e
r|o|2|h
a|c|1|d
h|c|1|h
x|i|1|b
k|i|1|d
r|i|1|d
h|i|1|e
s|i|1|d
a|i|1|d
k|o|1|h
x|o|1|b
h|o|1|d
a|o|1|d
s|o|1|c
r|o|1|c
k|x|1|h
h|x|1|h
a|x|1|h
s|x|1|h
r|x|1|h

## JRip

Decision list:

rules | predicted class
---|---
(Area = 2) and (LargestSpotSize = A)|F (3.0/0.0)
(HistComplex = 2) and (Activity = 2) and (SpotDistribution = C)|E (22.0/7.0)
(LargestSpotSize = X)|B (128.0/0.0)
(SpotDistribution = O) and (C-class = 0) and (HistComplex = 1)|C (171.0/55.0)
(SpotDistribution = O) and (C-class = 0) and (Evolution = 2)|C (49.0/23.0)
(SpotDistribution = I) and (Evolution = 3)|D (104.0/36.0)
|H (479.0/181.0)


## PART

Decision list:

rules | predicted class
---|---
SpotDistribution = X|H (298.0)
LargestSpotSize = X|B (128.0)
SpotDistribution = O AND LargestSpotSize = S|C (129.0/54.0)
HistComplex = 1 AND SpotDistribution = O|C (121.0/45.0)
Area = 1 AND SpotDistribution = I|D (178.0/77.0)
Area = 1 AND C-class = 0 AND Activity = 1 AND LargestSpotSize = A|D (24.0/13.0)
Area = 2|E (24.0/10.0)
LargestSpotSize = R|C (18.0/8.0)
C-class = 0 AND Activity = 2|E (12.0/4.0)
C-class = 1|E (9.0/4.0)
|D (15.0/7.0)


## J48 Decision Tree

* SpotDistribution = X: H (248.0)
* SpotDistribution = O
	* LargestSpotSize = A: D (49.0/27.0)
	* LargestSpotSize = R: C (90.0/33.0)
	* LargestSpotSize = S: C (106.0/42.0)
	* LargestSpotSize = X: B (96.0)
	* LargestSpotSize = K: C (1.0)
	* LargestSpotSize = H: D (13.0/7.0)
* SpotDistribution = I
	* LargestSpotSize = A: D (80.0/36.0)
	* LargestSpotSize = R: D (22.0/8.0)
	* LargestSpotSize = S: D (33.0/19.0)
	* LargestSpotSize = X: B (10.0)
	* LargestSpotSize = K: D (19.0/8.0)
	* LargestSpotSize = H: D (2.0/1.0)
* SpotDistribution = C: E (28.0/13.0)


## SimpleCart Decision Tree

		* SpotDistribution=(C)|(I)|(O)
	* LargestSpotSize=(X): B(128.0/0.0)
	* LargestSpotSize!=(X)
			* SpotDistribution=(C)|(I)
			* Area=(2): E(13.0/10.0)
			* Area!=(2): D(107.0/88.0)
			* SpotDistribution!=(C)|(I)
						* LargestSpotSize=(K)|(S)|(R)|(X): C(151.0/91.0)
						* LargestSpotSize!=(K)|(S)|(R)|(X): D(31.0/39.0)
		* SpotDistribution!=(C)|(I)|(O): H(298.0/0.0)


