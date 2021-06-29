# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | H | 0.311390 |
| SpotDistribution = O and LargestSpotSize!=(X) and SpotDistribution != I | C | 0.101028 |
| LargestSpotSize = X and SpotDistribution = O and Area = 1 and X-class = 0 | B | 0.122081 |
| LargestSpotSize = A and SpotDistribution = I and Area = 1 and X-class = 0 | D | 0.041305 |
| LargestSpotSize = A and SpotDistribution = O and Area = 1 and X-class = 0 | D | 0.015419 |
| LargestSpotSize = S and SpotDistribution = I and Area = 1 and X-class = 0 | D | 0.012459 |
| LargestSpotSize = K and SpotDistribution = I and Area = 1 and X-class = 0 | D | 0.012519 |
| LargestSpotSize = R and SpotDistribution = I and Area = 1 and X-class = 0 | D | 0.012048 |
| LargestSpotSize = X and SpotDistribution = I and Area = 1 and X-class = 0 | B | 0.015476 |
| SpotDistribution = O and LargestSpotSize = A and Evolution = 2 | E | 0.003897 |
| SpotDistribution = C and LargestSpotSize = K | E | 0.009112 |
| SpotDistribution = O and LargestSpotSize = S and C-class = 0 and HistComplex = 2 and Evolution = 3 | D | 0.004043 |
| SpotDistribution = O and LargestSpotSize = H | D | 0.004139 |
| SpotDistribution = I and LargestSpotSize = A and HistComplex = 2 and Evolution = 3 and Activity = 2 | E | 0.003440 |
| LargestSpotSize = A and SpotDistribution = C and Area = 1 and X-class = 0 | E | 0.003182 |
| SpotDistribution = O and LargestSpotSize = S and C-class = 3 | D | 0.001348 |
| LargestSpotSize = K and SpotDistribution = I and Area = 2 and X-class = 0 | E | 0.002062 |
| SpotDistribution = O and LargestSpotSize = S and C-class = 0 and HistComplex = 2 and Evolution = 1 | D | 0.001735 |
| LargestSpotSize = A and SpotDistribution = I and Area = 2 and X-class = 0 | F | 0.002174 |
| SpotDistribution = C and LargestSpotSize = R | D | 0.001795 |
| SpotDistribution = O and LargestSpotSize = S and C-class = 2 | D | 0.001348 |
| SpotDistribution = O and LargestSpotSize = S and C-class = 0 and HistComplex = 1 and Activity = 1 and Evolution = 1 | D | 0.000674 |
| SpotDistribution = O and LargestSpotSize = S and C-class = 6 | E | 0.001145 |
| SpotDistribution = I and LargestSpotSize = H | D | 0.000674 |
| LargestSpotSize = H and SpotDistribution = I and Area = 1 and X-class = 0 | E | 0.000573 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = X | H | 0.311390 |
| LargestSpotSize = X | B | 0.194825 |
| SpotDistribution = O and C-class = 0 and LargestSpotSize = S | C | 0.103721 |
| SpotDistribution = O and LargestSpotSize = R and HistComplex = 1 and C-class = 0 | C | 0.114768 |
| Area = 2 | E | 0.025051 |
| SpotDistribution = C | E | 0.009614 |
| SpotDistribution = O and LargestSpotSize = R and C-class = 0 | C | 0.008361 |
| SpotDistribution = O and C-class = 1 and LargestSpotSize = S and Evolution = 3 | D | 0.017253 |
|  | D | 0.567568 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| HistComplex = 2 and Activity = 2 and SpotDistribution = C and Prev24Hour = 3 and LargestSpotSize = K | E | 0.005864 |
| LargestSpotSize = X | B | 0.134879 |
| SpotDistribution = O and HistComplex = 1 and C-class = 0 and LargestSpotSize = R and Evolution = 2 | C | 0.025206 |
| SpotDistribution = O and HistComplex = 1 and C-class = 0 and LargestSpotSize = S and Evolution = 2 | C | 0.024343 |
| SpotDistribution = O and LargestSpotSize = R and C-class = 0 and Evolution = 2 and Activity = 1 | C | 0.006730 |
| SpotDistribution = O and HistComplex = 1 and LargestSpotSize = R and C-class = 0 | C | 0.037987 |
| SpotDistribution = O and LargestSpotSize = S and HistComplex = 1 and C-class = 0 | C | 0.021769 |
| SpotDistribution = O and LargestSpotSize = S and C-class = 1 and Evolution = 2 | C | 0.005615 |
| SpotDistribution = O and LargestSpotSize = S and Evolution = 3 and HistComplex = 2 and Activity = 1 | C | 0.007004 |
| SpotDistribution = I and Evolution = 3 and HistComplex = 1 and LargestSpotSize = A | D | 0.029192 |
| SpotDistribution = I and Evolution = 3 and C-class = 0 and LargestSpotSize = R | D | 0.011972 |
| SpotDistribution = I and Evolution = 3 and Area = 1 and LargestSpotSize = K | D | 0.018367 |
| SpotDistribution = I and C-class = 0 and Evolution = 3 | D | 0.028014 |
| SpotDistribution = O and Evolution = 3 and Activity = 2 | D | 0.011972 |
| SpotDistribution = O and Evolution = 3 and C-class = 1 | D | 0.011157 |
| SpotDistribution = O and C-class = 0 and LargestSpotSize = H and HistComplex = 2 and Activity = 1 | D | 0.009278 |
|  | H | 0.485342 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

largestspotsize|spotdistribution|area|x-class|class
---|---|---|---|---
k|c|2|2|h
k|c|2|1|e
a|i|1|1|h
a|c|2|0|h
k|c|2|0|e
a|i|2|0|f
k|i|2|0|e
k|c|1|0|e
r|o|2|0|h
a|c|1|0|e
r|c|1|0|d
h|i|1|0|e
k|i|1|0|d
x|i|1|0|b
s|i|1|0|d
a|i|1|0|d
r|i|1|0|d
k|o|1|0|h
x|o|1|0|b
h|o|1|0|d
s|o|1|0|c
a|o|1|0|d
r|o|1|0|c
k|x|1|0|h
h|x|1|0|h
r|x|1|0|h
a|x|1|0|h
s|x|1|0|h

## JRip

Decision list:

rules | predicted class
---|---
(HistComplex = 2) and (Activity = 2) and (SpotDistribution = C) and (Prev24Hour = 3) and (LargestSpotSize = K)|E (7.0/1.0)
(LargestSpotSize = X)|B (128.0/0.0)
(SpotDistribution = O) and (HistComplex = 1) and (C-class = 0) and (LargestSpotSize = R) and (Evolution = 2)|C (27.0/6.0)
(SpotDistribution = O) and (HistComplex = 1) and (C-class = 0) and (LargestSpotSize = S) and (Evolution = 2)|C (28.0/7.0)
(SpotDistribution = O) and (LargestSpotSize = R) and (C-class = 0) and (Evolution = 2) and (Activity = 1)|C (9.0/1.0)
(SpotDistribution = O) and (HistComplex = 1) and (LargestSpotSize = R) and (C-class = 0)|C (59.0/19.0)
(SpotDistribution = O) and (LargestSpotSize = S) and (HistComplex = 1) and (C-class = 0)|C (38.0/13.0)
(SpotDistribution = O) and (LargestSpotSize = S) and (C-class = 1) and (Evolution = 2)|C (7.0/2.0)
(SpotDistribution = O) and (LargestSpotSize = S) and (Evolution = 3) and (HistComplex = 2) and (Activity = 1)|C (11.0/4.0)
(SpotDistribution = I) and (Evolution = 3) and (HistComplex = 1) and (LargestSpotSize = A)|D (20.0/3.0)
(SpotDistribution = I) and (Evolution = 3) and (C-class = 0) and (LargestSpotSize = R)|D (11.0/3.0)
(SpotDistribution = I) and (Evolution = 3) and (Area = 1) and (LargestSpotSize = K)|D (9.0/0.0)
(SpotDistribution = I) and (C-class = 0) and (Evolution = 3)|D (41.0/16.0)
(SpotDistribution = O) and (Evolution = 3) and (Activity = 2)|D (10.0/2.0)
(SpotDistribution = O) and (Evolution = 3) and (C-class = 1)|D (14.0/5.0)
(SpotDistribution = O) and (C-class = 0) and (LargestSpotSize = H) and (HistComplex = 2) and (Activity = 1)|D (8.0/2.0)
|H (530.0/232.0)


## PART

Decision list:

rules | predicted class
---|---
SpotDistribution = X|H (224.0)
LargestSpotSize = X|B (96.0)
SpotDistribution = O AND C-class = 0 AND LargestSpotSize = S|C (80.0/33.0)
SpotDistribution = O AND LargestSpotSize = R AND HistComplex = 1 AND C-class = 0|C (61.0/16.0)
Area = 2|E (19.0/7.0)
SpotDistribution = C|E (13.0/6.0)
SpotDistribution = O AND LargestSpotSize = R AND C-class = 0|C (10.0/4.0)
SpotDistribution = O AND C-class = 1 AND LargestSpotSize = S AND Evolution = 3|D (8.0/4.0)
|D (207.0/97.0)


## J48 Decision Tree

* SpotDistribution = X: H (298.0)
* SpotDistribution = O
	* LargestSpotSize = A
		* Evolution = 1: D (4.0/2.0)
		* Evolution = 2: E (24.0/15.0)
		* Evolution = 3
			* HistComplex = 1: D (15.0/6.0)
			* HistComplex = 2: D (12.0/6.0)
	* LargestSpotSize = R
		* HistComplex = 1
			* Evolution = 1: C (5.0/1.0)
			* Evolution = 2: C (30.0/8.0)
			* Evolution = 3: C (60.0/21.0)
		* HistComplex = 2: C (17.0/6.0)
	* LargestSpotSize = S
		* C-class = 0
			* HistComplex = 1
				* Activity = 1
					* Evolution = 1: D (2.0/1.0)
					* Evolution = 2: C (20.0/5.0)
					* Evolution = 3: C (32.0/11.0)
				* Activity = 2: C (12.0/3.0)
			* HistComplex = 2
				* Evolution = 1: D (7.0/4.0)
				* Evolution = 2: C (21.0/11.0)
				* Evolution = 3: D (12.0/6.0)
		* C-class = 1: C (16.0/7.0)
		* C-class = 2: D (4.0/2.0)
		* C-class = 3: D (4.0/2.0)
		* C-class = 4: C (0.0)
		* C-class = 5: C (0.0)
		* C-class = 6: E (1.0)
		* C-class = 7: C (0.0)
		* C-class = 8: C (0.0)
	* LargestSpotSize = X: B (115.0)
	* LargestSpotSize = K: C (1.0)
	* LargestSpotSize = H: D (16.0/9.0)
* SpotDistribution = I
	* LargestSpotSize = A
		* HistComplex = 1: D (24.0/4.0)
		* HistComplex = 2
			* Evolution = 1: D (2.0/1.0)
			* Evolution = 2
				* Activity = 1: D (25.0/15.0)
				* Activity = 2: D (16.0/9.0)
			* Evolution = 3
				* Activity = 1: D (21.0/7.0)
				* Activity = 2: E (12.0/6.0)
	* LargestSpotSize = R
		* HistComplex = 1: D (13.0/6.0)
		* HistComplex = 2: D (12.0/4.0)
	* LargestSpotSize = S
		* HistComplex = 1: D (14.0/5.0)
		* HistComplex = 2: D (21.0/12.0)
	* LargestSpotSize = X: B (13.0)
	* LargestSpotSize = K
		* Evolution = 1: D (0.0)
		* Evolution = 2: D (10.0/6.0)
		* Evolution = 3: D (13.0/4.0)
	* LargestSpotSize = H: D (2.0/1.0)
* SpotDistribution = C
	* LargestSpotSize = A: E (10.0/5.0)
	* LargestSpotSize = R: D (3.0/1.0)
	* LargestSpotSize = S: E (0.0)
	* LargestSpotSize = X: E (0.0)
	* LargestSpotSize = K: E (18.0/6.0)
	* LargestSpotSize = H: E (0.0)


## SimpleCart Decision Tree

		* SpotDistribution=(C)|(I)|(O)
	* LargestSpotSize=(X): B(128.0/0.0)
	* LargestSpotSize!=(X)
			* SpotDistribution=(C)|(I): D(108.0/108.0)
			* SpotDistribution!=(C)|(I): C(172.0/143.0)
		* SpotDistribution!=(C)|(I)|(O): H(298.0/0.0)


