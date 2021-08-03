# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = X | H | 0.311715 |
| SpotDistribution = O and LargestSpotSize = X | B | 0.122210 |
| SpotDistribution = O and LargestSpotSize!=(X) and SpotDistribution != I and LargestSpotSize != X | D | 0.055483 |
| SpotDistribution = O and LargestSpotSize = R | C | 0.058909 |
| SpotDistribution = O and LargestSpotSize!=(X) and SpotDistribution != I and LargestSpotSize = S | C | 0.055768 |
| SpotDistribution = I and LargestSpotSize = A | D | 0.043153 |
| SpotDistribution = I and LargestSpotSize = R | D | 0.015449 |
| SpotDistribution = I and LargestSpotSize = X | B | 0.015495 |
| SpotDistribution = C and LargestSpotSize = K | E | 0.007683 |
| LargestSpotSize = K and SpotDistribution = I and HistComplex = 2 and X-class = 0 | D | 0.008438 |
| SpotDistribution = I and LargestSpotSize = S and C-class = 0 | D | 0.008167 |
| LargestSpotSize = S and SpotDistribution = I and HistComplex = 2 and X-class = 0 | E | 0.004067 |
| SpotDistribution = C and LargestSpotSize = A | E | 0.003186 |
| SpotDistribution = I and LargestSpotSize = S and C-class = 2 | F | 0.002174 |
| SpotDistribution = I and LargestSpotSize = S and C-class = 1 | D | 0.003080 |
| SpotDistribution = I and LargestSpotSize = H | E | 0.001529 |
| SpotDistribution = C and LargestSpotSize = H | E | 0.001147 |
| SpotDistribution = O and LargestSpotSize = K | C | 0.001304 |
| SpotDistribution = C and LargestSpotSize = R | D | 0.001797 |
| LargestSpotSize = A and SpotDistribution = C and HistComplex = 1 and X-class = 0 | D | 0.000675 |
| LargestSpotSize = H and SpotDistribution = I and HistComplex = 2 and X-class = 0 | D | 0.000450 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = X | H | 0.311715 |
| LargestSpotSize != X and Area = 1 and SpotDistribution = O and LargestSpotSize != H and LargestSpotSize != A | C | 0.174969 |
| LargestSpotSize = X | B | 0.251969 |
| Area = 1 and HistComplex != 1 and LargestSpotSize != R and SpotDistribution != O | D | 0.181176 |
| Area != 1 | E | 0.032803 |
| Activity != 1 and SpotDistribution != I | E | 0.031392 |
|  | D | 0.529210 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = I and Evolution = 2 and Area = 2 | F | 0.003257 |
| HistComplex = 2 and Activity = 2 and SpotDistribution = C and Prev24Hour = 3 | E | 0.005161 |
| HistComplex = 2 and Activity = 2 and SpotDistribution = O and Prev24Hour = 1 and LargestSpotSize = A | E | 0.005727 |
| HistComplex = 2 and SpotDistribution = I and LargestSpotSize = S and Evolution = 2 and Activity = 1 and M-class = 0 | E | 0.002586 |
| HistComplex = 2 and Activity = 2 and SpotDistribution = C | E | 0.003768 |
| LargestSpotSize = X | B | 0.137634 |
| SpotDistribution = O and HistComplex = 1 and C-class = 0 and Evolution = 2 and LargestSpotSize = S | C | 0.026534 |
| SpotDistribution = O and LargestSpotSize = R and Evolution = 2 and C-class = 0 and HistComplex = 1 | C | 0.022180 |
| SpotDistribution = O and HistComplex = 1 and C-class = 0 and LargestSpotSize = R and Evolution = 1 | C | 0.005186 |
| SpotDistribution = O and HistComplex = 1 and C-class = 0 and LargestSpotSize = S and Prev24Hour = 1 and Activity = 2 | C | 0.002927 |
| SpotDistribution = O and HistComplex = 1 and C-class = 0 and LargestSpotSize = R and M-class = 0 | C | 0.030975 |
| SpotDistribution = O and LargestSpotSize = S and HistComplex = 1 and C-class = 0 and Activity = 1 | C | 0.021331 |
| SpotDistribution = O and Evolution = 2 and C-class = 0 and LargestSpotSize = R and Activity = 1 | C | 0.005004 |
| SpotDistribution = O and Evolution = 2 and LargestSpotSize = S and C-class = 0 and Activity = 1 | C | 0.008238 |
| SpotDistribution = O and HistComplex = 1 and Evolution = 2 | C | 0.003672 |
| SpotDistribution = I and HistComplex = 1 and LargestSpotSize = A and Activity = 2 | D | 0.010799 |
| SpotDistribution = I and Evolution = 3 and Area = 1 and LargestSpotSize = K | D | 0.017167 |
| SpotDistribution = I and C-class = 0 and HistComplex = 1 and LargestSpotSize = A and Evolution = 2 | D | 0.006508 |
| SpotDistribution = I and C-class = 0 and Evolution = 3 and M-class = 1 | D | 0.008658 |
| SpotDistribution = I and HistComplex = 1 and LargestSpotSize = A | D | 0.017883 |
| SpotDistribution = I and LargestSpotSize = R and C-class = 0 and HistComplex = 2 and Evolution = 2 | D | 0.008658 |
| SpotDistribution = I and C-class = 0 and LargestSpotSize = R and Evolution = 3 and HistComplex = 2 | D | 0.009019 |
| SpotDistribution = I and HistComplex = 1 and Activity = 2 | D | 0.006508 |
| SpotDistribution = I and LargestSpotSize = A and Activity = 1 and C-class = 1 | D | 0.007747 |
| SpotDistribution = O and Evolution = 3 and C-class = 1 and LargestSpotSize = A | D | 0.006508 |
| SpotDistribution = I and C-class = 0 and Activity = 1 and LargestSpotSize = R and Evolution = 3 | D | 0.004980 |
| SpotDistribution = O and Evolution = 3 and C-class = 0 and LargestSpotSize = H and HistComplex = 2 | D | 0.004891 |
| SpotDistribution = I and C-class = 0 and Activity = 1 and HistComplex = 2 and LargestSpotSize = S | D | 0.009019 |
| SpotDistribution = O and Evolution = 3 and HistComplex = 1 and M-class = 1 | D | 0.004891 |
| SpotDistribution = O and LargestSpotSize = S and Evolution = 2 | D | 0.020205 |
| SpotDistribution = I and LargestSpotSize = A and Activity = 1 and Evolution = 3 | D | 0.008238 |
| SpotDistribution = O and Evolution = 3 and LargestSpotSize = A and Activity = 2 | D | 0.006508 |
|  | H | 0.512027 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

largestspotsize|spotdistribution|histcomplex|x-class|class
---|---|---|---|---
k|c|2|2|h
k|c|2|1|e
a|i|2|1|h
h|c|2|0|h
r|c|2|0|h
a|c|2|0|e
k|c|2|0|e
h|i|2|0|d
x|i|2|0|b
r|i|2|0|d
a|i|2|0|d
k|i|2|0|d
s|i|2|0|e
r|c|1|0|d
x|o|2|0|b
a|c|1|0|d
r|o|2|0|c
a|o|2|0|d
s|o|2|0|c
h|o|2|0|d
h|x|2|0|h
s|i|1|0|d
x|i|1|0|b
r|i|1|0|d
a|i|1|0|d
r|x|2|0|h
a|x|2|0|h
s|x|2|0|h
k|o|1|0|h
h|o|1|0|d
x|o|1|0|b
s|o|1|0|c
a|o|1|0|d
r|o|1|0|c
a|x|1|0|h
h|x|1|0|h
r|x|1|0|h
s|x|1|0|h

## JRip

Decision list:

rules | predicted class
---|---
(SpotDistribution = I) and (Evolution = 2) and (Area = 2)|F (3.0/0.0)
(HistComplex = 2) and (Activity = 2) and (SpotDistribution = C) and (Prev24Hour = 3)|E (8.0/2.0)
(HistComplex = 2) and (Activity = 2) and (SpotDistribution = O) and (Prev24Hour = 1) and (LargestSpotSize = A)|E (5.0/0.0)
(HistComplex = 2) and (SpotDistribution = I) and (LargestSpotSize = S) and (Evolution = 2) and (Activity = 1) and (M-class = 0)|E (4.0/1.0)
(HistComplex = 2) and (Activity = 2) and (SpotDistribution = C)|E (13.0/6.0)
(LargestSpotSize = X)|B (128.0/0.0)
(SpotDistribution = O) and (HistComplex = 1) and (C-class = 0) and (Evolution = 2) and (LargestSpotSize = S)|C (29.0/7.0)
(SpotDistribution = O) and (LargestSpotSize = R) and (Evolution = 2) and (C-class = 0) and (HistComplex = 1)|C (26.0/7.0)
(SpotDistribution = O) and (HistComplex = 1) and (C-class = 0) and (LargestSpotSize = R) and (Evolution = 1)|C (5.0/1.0)
(SpotDistribution = O) and (HistComplex = 1) and (C-class = 0) and (LargestSpotSize = S) and (Prev24Hour = 1) and (Activity = 2)|C (3.0/0.0)
(SpotDistribution = O) and (HistComplex = 1) and (C-class = 0) and (LargestSpotSize = R) and (M-class = 0)|C (52.0/18.0)
(SpotDistribution = O) and (LargestSpotSize = S) and (HistComplex = 1) and (C-class = 0) and (Activity = 1)|C (35.0/12.0)
(SpotDistribution = O) and (Evolution = 2) and (C-class = 0) and (LargestSpotSize = R) and (Activity = 1)|C (9.0/2.0)
(SpotDistribution = O) and (Evolution = 2) and (LargestSpotSize = S) and (C-class = 0) and (Activity = 1)|C (19.0/8.0)
(SpotDistribution = O) and (HistComplex = 1) and (Evolution = 2)|C (15.0/7.0)
(SpotDistribution = I) and (HistComplex = 1) and (LargestSpotSize = A) and (Activity = 2)|D (5.0/0.0)
(SpotDistribution = I) and (Evolution = 3) and (Area = 1) and (LargestSpotSize = K)|D (8.0/0.0)
(SpotDistribution = I) and (C-class = 0) and (HistComplex = 1) and (LargestSpotSize = A) and (Evolution = 2)|D (3.0/0.0)
(SpotDistribution = I) and (C-class = 0) and (Evolution = 3) and (M-class = 1)|D (4.0/0.0)
(SpotDistribution = I) and (HistComplex = 1) and (LargestSpotSize = A)|D (12.0/2.0)
(SpotDistribution = I) and (LargestSpotSize = R) and (C-class = 0) and (HistComplex = 2) and (Evolution = 2)|D (4.0/0.0)
(SpotDistribution = I) and (C-class = 0) and (LargestSpotSize = R) and (Evolution = 3) and (HistComplex = 2)|D (6.0/1.0)
(SpotDistribution = I) and (HistComplex = 1) and (Activity = 2)|D (3.0/0.0)
(SpotDistribution = I) and (LargestSpotSize = A) and (Activity = 1) and (C-class = 1)|D (7.0/2.0)
(SpotDistribution = O) and (Evolution = 3) and (C-class = 1) and (LargestSpotSize = A)|D (3.0/0.0)
(SpotDistribution = I) and (C-class = 0) and (Activity = 1) and (LargestSpotSize = R) and (Evolution = 3)|D (6.0/2.0)
(SpotDistribution = O) and (Evolution = 3) and (C-class = 0) and (LargestSpotSize = H) and (HistComplex = 2)|D (4.0/1.0)
(SpotDistribution = I) and (C-class = 0) and (Activity = 1) and (HistComplex = 2) and (LargestSpotSize = S)|D (5.0/1.0)
(SpotDistribution = O) and (Evolution = 3) and (HistComplex = 1) and (M-class = 1)|D (4.0/1.0)
(SpotDistribution = O) and (LargestSpotSize = S) and (Evolution = 2)|D (7.0/2.0)
(SpotDistribution = I) and (LargestSpotSize = A) and (Activity = 1) and (Evolution = 3)|D (14.0/6.0)
(SpotDistribution = O) and (Evolution = 3) and (LargestSpotSize = A) and (Activity = 2)|D (3.0/0.0)
|H (504.0/206.0)


## PART

Decision list:

rules | predicted class
---|---
SpotDistribution = X|H (248.0)
LargestSpotSize != X AND Area = 1 AND SpotDistribution = O AND LargestSpotSize != H AND LargestSpotSize != A|C (205.0/78.0)
LargestSpotSize = X|B (107.0)
Area = 1 AND HistComplex != 1 AND LargestSpotSize != R AND SpotDistribution != O|D (104.0/53.0)
Area != 1|E (21.0/8.0)
Activity != 1 AND SpotDistribution != I|E (12.0/5.0)
|D (100.0/41.0)


## J48 Decision Tree

* SpotDistribution = X: H (256.0)
* SpotDistribution = O
	* LargestSpotSize = A: D (49.0/31.0)
	* LargestSpotSize = R: C (93.0/35.0)
	* LargestSpotSize = S: C (112.0/45.0)
	* LargestSpotSize = X: B (97.0)
	* LargestSpotSize = K: C (1.0)
	* LargestSpotSize = H: D (11.0/6.0)
* SpotDistribution = I
	* LargestSpotSize = A: D (84.0/34.0)
	* LargestSpotSize = R: D (24.0/9.0)
	* LargestSpotSize = S
		* C-class = 0: D (25.0/13.0)
		* C-class = 1: D (4.0/1.0)
		* C-class = 2: F (1.0)
		* C-class = 3: E (1.0)
		* C-class = 4: D (0.0)
		* C-class = 5: E (1.0)
		* C-class = 6: D (0.0)
		* C-class = 7: D (0.0)
		* C-class = 8: D (0.0)
	* LargestSpotSize = X: B (12.0)
	* LargestSpotSize = K: D (19.0/9.0)
	* LargestSpotSize = H: E (3.0/1.0)
* SpotDistribution = C
	* LargestSpotSize = A: E (9.0/4.0)
	* LargestSpotSize = R: D (2.0/1.0)
	* LargestSpotSize = S: E (0.0)
	* LargestSpotSize = X: E (0.0)
	* LargestSpotSize = K: E (15.0/7.0)
	* LargestSpotSize = H: E (1.0)


## SimpleCart Decision Tree

		* SpotDistribution=(C)|(I)|(O)
	* LargestSpotSize=(X): B(128.0/0.0)
	* LargestSpotSize!=(X)
			* SpotDistribution=(C)|(I)
			* Area=(2): E(13.0/11.0)
			* Area!=(2): D(109.0/87.0)
			* SpotDistribution!=(C)|(I)
					* LargestSpotSize=(S)|(R)|(X): C(147.0/91.0)
					* LargestSpotSize!=(S)|(R)|(X): D(30.0/42.0)
		* SpotDistribution!=(C)|(I)|(O): H(298.0/0.0)


