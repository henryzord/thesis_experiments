# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = X | H | 0.311390 |
| SpotDistribution = O and LargestSpotSize!=(X) and SpotDistribution != C | C | 0.101028 |
| SpotDistribution = O and LargestSpotSize = X | B | 0.122081 |
| SpotDistribution = I and LargestSpotSize = A and HistComplex = 1 | D | 0.021988 |
| SpotDistribution = I and LargestSpotSize = A and HistComplex = 2 and Evolution = 3 and Activity = 1 | D | 0.012461 |
| SpotDistribution = I and LargestSpotSize = R and Evolution = 3 | D | 0.010110 |
| SpotDistribution = I and LargestSpotSize = X | B | 0.015476 |
| SpotDistribution = I and LargestSpotSize = K and Evolution = 3 | D | 0.008341 |
| SpotDistribution = O and LargestSpotSize = A and C-class = 0 and Evolution = 3 and HistComplex = 1 | D | 0.005488 |
| SpotDistribution = O and LargestSpotSize = S and C-class = 0 and HistComplex = 2 and Evolution = 3 | D | 0.004043 |
| SpotDistribution = I and LargestSpotSize = S and HistComplex = 1 | D | 0.007756 |
| SpotDistribution = O and LargestSpotSize = H | D | 0.004139 |
| SpotDistribution = I and LargestSpotSize = A and HistComplex = 2 and Evolution = 2 and C-class = 0 and Activity = 1 | D | 0.004805 |
| SpotDistribution = O and LargestSpotSize = A and C-class = 0 and Evolution = 2 | D | 0.003049 |
| SpotDistribution = C and LargestSpotSize = K and Evolution = 2 | E | 0.005137 |
| SpotDistribution = C and LargestSpotSize = K and Evolution = 3 | E | 0.004119 |
| SpotDistribution = I and LargestSpotSize = S and HistComplex = 2 and Evolution = 3 | D | 0.003067 |
| SpotDistribution = I and LargestSpotSize = A and HistComplex = 2 and Evolution = 3 and Activity = 2 | E | 0.003440 |
| SpotDistribution = O and LargestSpotSize = A and C-class = 1 | D | 0.002695 |
| SpotDistribution = I and LargestSpotSize = A and HistComplex = 2 and Evolution = 2 and C-class = 0 and Activity = 2 | D | 0.002695 |
| SpotDistribution = I and LargestSpotSize = R and Evolution = 2 | D | 0.002695 |
| SpotDistribution = C and LargestSpotSize = A | E | 0.002867 |
| SpotDistribution = O and LargestSpotSize = A and C-class = 0 and Evolution = 1 | D | 0.001795 |
| SpotDistribution = O and LargestSpotSize = S and C-class = 3 | D | 0.001348 |
| SpotDistribution = I and LargestSpotSize = K and Evolution = 2 | D | 0.002162 |
| SpotDistribution = O and LargestSpotSize = A and C-class = 4 | E | 0.002288 |
| SpotDistribution = O and LargestSpotSize = S and C-class = 0 and HistComplex = 2 and Evolution = 1 | D | 0.001735 |
| SpotDistribution = I and LargestSpotSize = S and HistComplex = 2 and Evolution = 2 | E | 0.002041 |
| SpotDistribution = I and LargestSpotSize = A and HistComplex = 2 and Evolution = 2 and C-class = 1 | F | 0.002179 |
| SpotDistribution = C and LargestSpotSize = R | D | 0.001795 |
| SpotDistribution = O and LargestSpotSize = A and C-class = 2 | D | 0.001795 |
| SpotDistribution = O and LargestSpotSize = S and C-class = 2 | D | 0.001348 |
| SpotDistribution = I and LargestSpotSize = S and HistComplex = 2 and Evolution = 1 | D | 0.001346 |
| SpotDistribution = O and LargestSpotSize = S and C-class = 0 and HistComplex = 1 and Activity = 1 and Evolution = 1 | D | 0.000674 |
| SpotDistribution = I and LargestSpotSize = A and HistComplex = 2 and Evolution = 2 and C-class = 2 | F | 0.001451 |
| SpotDistribution = O and LargestSpotSize = S and C-class = 6 | E | 0.001145 |
| SpotDistribution = O and LargestSpotSize = A and C-class = 3 | E | 0.001145 |
| SpotDistribution = I and LargestSpotSize = R and Evolution = 1 | C | 0.001302 |
| SpotDistribution = I and LargestSpotSize = H | D | 0.000674 |
| SpotDistribution = I and LargestSpotSize = A and HistComplex = 2 and Evolution = 1 | D | 0.000674 |
| SpotDistribution = I and LargestSpotSize = A and HistComplex = 2 and Evolution = 2 and C-class = 4 | D | 0.000674 |
| SpotDistribution = I and LargestSpotSize = A and HistComplex = 2 and Evolution = 2 and C-class = 3 | E | 0.000573 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = X | H | 0.311390 |
| LargestSpotSize = X | B | 0.194825 |
| SpotDistribution = O and LargestSpotSize = R and HistComplex = 1 and C-class = 0 | C | 0.114768 |
| SpotDistribution = C | E | 0.026799 |
| SpotDistribution = O and LargestSpotSize = R and Evolution = 2 | C | 0.015480 |
| SpotDistribution = O and LargestSpotSize = S and C-class = 0 | C | 0.109164 |
| HistComplex = 1 | D | 0.314846 |
| SpotDistribution = O | D | 0.122439 |
| LargestSpotSize = K | D | 0.040329 |
| LargestSpotSize = S | E | 0.049357 |
| LargestSpotSize = A and Evolution = 3 and Activity = 1 | D | 0.040580 |
|  | D | 0.224599 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = I and Evolution = 2 | F | 0.005151 |
| Area = 2 | F | 0.002448 |
| LargestSpotSize = A and HistComplex = 2 and Activity = 2 and Prev24Hour = 1 | E | 0.006501 |
| LargestSpotSize = A and HistComplex = 2 | E | 0.007229 |
| LargestSpotSize = X | B | 0.143337 |
| SpotDistribution = O and LargestSpotSize = R and Evolution = 2 and C-class = 0 and Activity = 1 and HistComplex = 2 | C | 0.012177 |
| SpotDistribution = O and HistComplex = 1 and C-class = 0 and LargestSpotSize = R and Evolution = 2 | C | 0.027590 |
| SpotDistribution = O and HistComplex = 1 and C-class = 0 and LargestSpotSize = S and Evolution = 2 | C | 0.026650 |
| SpotDistribution = O and HistComplex = 1 and LargestSpotSize = R and C-class = 0 | C | 0.041580 |
| SpotDistribution = O and LargestSpotSize = S and HistComplex = 1 and C-class = 0 | C | 0.023864 |
| SpotDistribution = O and LargestSpotSize = S and C-class = 1 | C | 0.008744 |
| SpotDistribution = O and LargestSpotSize = S and Evolution = 3 and HistComplex = 2 | C | 0.006066 |
| SpotDistribution = O and LargestSpotSize = R | C | 0.002079 |
| SpotDistribution = O and Evolution = 2 and LargestSpotSize = S | C | 0.006299 |
| SpotDistribution = O and HistComplex = 1 and Activity = 1 | C | 0.002914 |
| SpotDistribution = I and LargestSpotSize = K | D | 0.023472 |
| SpotDistribution = I and LargestSpotSize = A | D | 0.106495 |
| SpotDistribution = I and C-class = 0 and Activity = 1 and HistComplex = 2 | D | 0.013392 |
| SpotDistribution = I and HistComplex = 1 | D | 0.021013 |
| SpotDistribution = O and Evolution = 3 | D | 0.117569 |
|  | H | 0.663697 |


# Text representation of classifiers as-is

## JRip

Decision list:

rules | predicted class
---|---
(SpotDistribution = I) and (Evolution = 2)|F (80.0/61.0)
(Area = 2)|F (22.0/15.0)
(LargestSpotSize = A) and (HistComplex = 2) and (Activity = 2) and (Prev24Hour = 1)|E (14.0/5.0)
(LargestSpotSize = A) and (HistComplex = 2)|E (79.0/60.0)
(LargestSpotSize = X)|B (121.0/0.0)
(SpotDistribution = O) and (LargestSpotSize = R) and (Evolution = 2) and (C-class = 0) and (Activity = 1) and (HistComplex = 2)|C (9.0/1.0)
(SpotDistribution = O) and (HistComplex = 1) and (C-class = 0) and (LargestSpotSize = R) and (Evolution = 2)|C (27.0/6.0)
(SpotDistribution = O) and (HistComplex = 1) and (C-class = 0) and (LargestSpotSize = S) and (Evolution = 2)|C (28.0/7.0)
(SpotDistribution = O) and (HistComplex = 1) and (LargestSpotSize = R) and (C-class = 0)|C (59.0/19.0)
(SpotDistribution = O) and (LargestSpotSize = S) and (HistComplex = 1) and (C-class = 0)|C (38.0/13.0)
(SpotDistribution = O) and (LargestSpotSize = S) and (C-class = 1)|C (16.0/7.0)
(SpotDistribution = O) and (LargestSpotSize = S) and (Evolution = 3) and (HistComplex = 2)|C (13.0/6.0)
(SpotDistribution = O) and (LargestSpotSize = R)|C (16.0/9.0)
(SpotDistribution = O) and (Evolution = 2) and (LargestSpotSize = S)|C (25.0/14.0)
(SpotDistribution = O) and (HistComplex = 1) and (Activity = 1)|C (27.0/16.0)
(SpotDistribution = I) and (LargestSpotSize = K)|D (9.0/0.0)
(SpotDistribution = I) and (LargestSpotSize = A)|D (20.0/3.0)
(SpotDistribution = I) and (C-class = 0) and (Activity = 1) and (HistComplex = 2)|D (9.0/2.0)
(SpotDistribution = I) and (HistComplex = 1)|D (23.0/8.0)
(SpotDistribution = O) and (Evolution = 3)|D (9.0/2.0)
|H (313.0/33.0)


## PART

Decision list:

rules | predicted class
---|---
SpotDistribution = X|H (199.0)
LargestSpotSize = X|B (86.0)
SpotDistribution = O AND LargestSpotSize = R AND HistComplex = 1 AND C-class = 0|C (66.0/18.0)
SpotDistribution = C|E (21.0/12.0)
SpotDistribution = O AND LargestSpotSize = R AND Evolution = 2|C (11.0/4.0)
SpotDistribution = O AND LargestSpotSize = S AND C-class = 0|C (59.0/22.0)
HistComplex = 1|D (70.0/28.0)
SpotDistribution = O|D (34.0/19.0)
LargestSpotSize = K|D (18.0/7.0)
LargestSpotSize = S|E (14.0/8.0)
LargestSpotSize = A AND Evolution = 3 AND Activity = 1|D (13.0/5.0)
|D (47.0/26.0)


## J48 Decision Tree

* SpotDistribution = X: H (298.0)
* SpotDistribution = O
	* LargestSpotSize = A
		* C-class = 0
			* Evolution = 1: D (3.0/1.0)
			* Evolution = 2: D (16.0/10.0)
			* Evolution = 3
				* HistComplex = 1: D (12.0/5.0)
				* HistComplex = 2: C (10.0/5.0)
		* C-class = 1: D (8.0/4.0)
		* C-class = 2: D (3.0/1.0)
		* C-class = 3: E (1.0)
		* C-class = 4: E (2.0)
		* C-class = 5: D (0.0)
		* C-class = 6: D (0.0)
		* C-class = 7: D (0.0)
		* C-class = 8: D (0.0)
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
				* C-class = 0
					* Activity = 1: D (18.0/10.0)
					* Activity = 2: D (8.0/4.0)
				* C-class = 1: F (8.0/4.0)
				* C-class = 2: F (3.0/1.0)
				* C-class = 3: E (2.0/1.0)
				* C-class = 4: D (2.0/1.0)
				* C-class = 5: D (0.0)
				* C-class = 6: D (0.0)
				* C-class = 7: D (0.0)
				* C-class = 8: D (0.0)
			* Evolution = 3
				* Activity = 1: D (21.0/7.0)
				* Activity = 2: E (12.0/6.0)
	* LargestSpotSize = R
		* Evolution = 1: C (1.0)
		* Evolution = 2: D (8.0/4.0)
		* Evolution = 3: D (16.0/5.0)
	* LargestSpotSize = S
		* HistComplex = 1: D (14.0/5.0)
		* HistComplex = 2
			* Evolution = 1: D (1.0)
			* Evolution = 2: E (9.0/5.0)
			* Evolution = 3: D (11.0/6.0)
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
	* LargestSpotSize = K
		* Evolution = 1: E (0.0)
		* Evolution = 2: E (8.0/2.0)
		* Evolution = 3: E (10.0/4.0)
	* LargestSpotSize = H: E (0.0)


## SimpleCart Decision Tree

		* SpotDistribution=(C)|(I)|(O)
	* LargestSpotSize=(X): B(128.0/0.0)
	* LargestSpotSize!=(X)
			* SpotDistribution=(C)|(I)
			* Area=(2): E(13.0/10.0)
			* Area!=(2): D(107.0/86.0)
			* SpotDistribution!=(C)|(I): C(172.0/143.0)
		* SpotDistribution!=(C)|(I)|(O): H(298.0/0.0)


