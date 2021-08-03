# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = X | H | 0.311390 |
| LargestSpotSize = X and SpotDistribution = O | B | 0.122081 |
| SpotDistribution = O and LargestSpotSize!=(X) and SpotDistribution != I | C | 0.100323 |
| SpotDistribution = I and LargestSpotSize = A | D | 0.042708 |
| SpotDistribution = O and LargestSpotSize = A | D | 0.014013 |
| SpotDistribution = I and LargestSpotSize = R | D | 0.012533 |
| SpotDistribution = I and LargestSpotSize = S | D | 0.010722 |
| LargestSpotSize = X and SpotDistribution = I | B | 0.016647 |
| SpotDistribution = C | E | 0.010654 |
| LargestSpotSize = K and SpotDistribution = I | D | 0.009204 |
| LargestSpotSize = H and SpotDistribution = O | D | 0.004408 |
| LargestSpotSize = R and SpotDistribution = C | D | 0.001795 |
| LargestSpotSize = H and SpotDistribution = I | D | 0.000450 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = X | H | 0.311390 |
| LargestSpotSize = X | B | 0.196049 |
| SpotDistribution = C and Area = 2 | E | 0.011326 |
| SpotDistribution = O and LargestSpotSize = R and HistComplex = 1 and Evolution = 3 | C | 0.069016 |
| SpotDistribution = O and LargestSpotSize = R and HistComplex = 1 | C | 0.039568 |
| SpotDistribution = O and LargestSpotSize = S and C-class = 0 and HistComplex = 1 and Activity = 1 and Evolution = 3 | C | 0.036613 |
| SpotDistribution = O and LargestSpotSize = S and C-class = 0 and HistComplex = 1 and Activity = 1 | C | 0.021994 |
| SpotDistribution = O and LargestSpotSize = S and C-class = 0 and HistComplex = 2 and Evolution = 2 | C | 0.021999 |
| SpotDistribution = O and LargestSpotSize = R | C | 0.008413 |
| HistComplex = 1 and SpotDistribution = I and LargestSpotSize = A | D | 0.086524 |
| HistComplex = 1 and Evolution = 2 | C | 0.023689 |
| HistComplex = 1 and C-class = 0 and SpotDistribution = O | D | 0.184692 |
| HistComplex = 1 and C-class = 0 | D | 0.022449 |
| SpotDistribution = O and LargestSpotSize = S and C-class = 0 | D | 0.046658 |
| SpotDistribution = O and LargestSpotSize = A and Evolution = 2 | E | 0.023923 |
| HistComplex = 1 | D | 0.038228 |
| SpotDistribution = O and C-class = 0 | D | 0.046620 |
| LargestSpotSize = R | D | 0.036468 |
| SpotDistribution = I and Evolution = 3 and LargestSpotSize = A and Activity = 1 | D | 0.059394 |
| SpotDistribution = I and Evolution = 3 and LargestSpotSize = A | E | 0.044518 |
| SpotDistribution = I and C-class = 0 and Evolution = 2 and LargestSpotSize = A | D | 0.029343 |
| SpotDistribution = I and C-class = 1 | D | 0.026645 |
| C-class = 0 and Evolution = 2 | E | 0.075000 |
| SpotDistribution = I and Evolution = 3 | D | 0.054701 |
| SpotDistribution = O | D | 0.016021 |
|  | F | 0.286765 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = I and Evolution = 2 and C-class = 1 and Area = 2 | F | 0.002174 |
| HistComplex = 2 and Activity = 2 and SpotDistribution = C and Evolution = 2 and LargestSpotSize = K | E | 0.006849 |
| HistComplex = 2 and Activity = 2 and SpotDistribution = C and X-class = 1 | E | 0.002294 |
| HistComplex = 2 and LargestSpotSize = A and Activity = 2 and SpotDistribution = O and Prev24Hour = 1 | E | 0.005714 |
| HistComplex = 2 and SpotDistribution = I and LargestSpotSize = S and Evolution = 2 and Activity = 1 and M-class = 0 | E | 0.002580 |
| LargestSpotSize = X | B | 0.137527 |
| SpotDistribution = O and HistComplex = 1 and Evolution = 2 and Activity = 2 and LargestSpotSize = R | C | 0.003215 |
| SpotDistribution = O and HistComplex = 1 and Evolution = 2 and Activity = 2 and Prev24Hour = 2 | C | 0.003215 |
| SpotDistribution = O and HistComplex = 1 and Evolution = 2 and LargestSpotSize = R and C-class = 0 | C | 0.026283 |
| SpotDistribution = O and HistComplex = 1 and LargestSpotSize = S and C-class = 0 and Evolution = 2 and Activity = 2 | C | 0.006677 |
| SpotDistribution = O and HistComplex = 1 and LargestSpotSize = R and C-class = 0 and M-class = 0 and Evolution = 1 | C | 0.002147 |
| SpotDistribution = O and HistComplex = 1 and LargestSpotSize = R and C-class = 0 and M-class = 0 | C | 0.029898 |
| SpotDistribution = O and LargestSpotSize = S and HistComplex = 1 and C-class = 0 and Evolution = 2 | C | 0.015605 |
| SpotDistribution = O and LargestSpotSize = S and HistComplex = 1 and C-class = 0 and Activity = 2 and Prev24Hour = 1 | C | 0.003617 |
| SpotDistribution = O and LargestSpotSize = S and HistComplex = 1 and C-class = 0 and M-class = 1 | C | 0.003215 |
| SpotDistribution = O and LargestSpotSize = S and HistComplex = 1 and C-class = 0 and Activity = 1 and Evolution = 3 | C | 0.018426 |
| SpotDistribution = O and Evolution = 2 and LargestSpotSize = R and Activity = 1 and HistComplex = 2 | C | 0.011744 |
| SpotDistribution = O and LargestSpotSize = S and Evolution = 2 and C-class = 0 and Activity = 2 | C | 0.001613 |
| SpotDistribution = O and LargestSpotSize = S and Evolution = 2 and C-class = 0 | C | 0.007287 |
| SpotDistribution = O and HistComplex = 1 and C-class = 1 | C | 0.007673 |
| SpotDistribution = O and Activity = 1 and HistComplex = 1 and LargestSpotSize = R and M-class = 0 | C | 0.000224 |
| SpotDistribution = O and Activity = 1 and C-class = 0 and LargestSpotSize = A and Evolution = 2 and HistComplex = 2 and M-class = 0 | C | 0.005733 |
| SpotDistribution = O and Activity = 1 and Evolution = 3 and LargestSpotSize = S and HistComplex = 2 | C | 0.007150 |
| SpotDistribution = O and HistComplex = 1 and Evolution = 1 | C | 0.001613 |
| SpotDistribution = O and HistComplex = 1 and C-class = 3 | C | 0.002147 |
| SpotDistribution = I and Evolution = 3 and C-class = 0 and LargestSpotSize = A and HistComplex = 1 and M-class = 1 | D | 0.004494 |
| SpotDistribution = I and Evolution = 3 and C-class = 0 and LargestSpotSize = A and HistComplex = 1 | D | 0.017960 |
| SpotDistribution = I and Evolution = 3 and LargestSpotSize = K and Area = 1 | D | 0.019912 |
| SpotDistribution = I and Evolution = 3 and C-class = 0 and LargestSpotSize = R and HistComplex = 2 | D | 0.009321 |
| SpotDistribution = I and Evolution = 3 and LargestSpotSize = A and Activity = 1 and C-class = 1 | D | 0.006726 |
| SpotDistribution = I and C-class = 0 and Evolution = 3 and M-class = 1 | D | 0.006726 |
| SpotDistribution = I and C-class = 0 and HistComplex = 1 and LargestSpotSize = A | D | 0.007175 |
| SpotDistribution = I and Evolution = 3 and C-class = 0 and HistComplex = 1 and Activity = 2 | D | 0.004494 |
| SpotDistribution = I and Evolution = 3 and C-class = 0 and Area = 1 and Activity = 1 and HistComplex = 2 and LargestSpotSize = S | D | 0.005056 |
| SpotDistribution = I and Evolution = 3 and HistComplex = 1 and LargestSpotSize = A | D | 0.004054 |
| SpotDistribution = I and C-class = 0 and LargestSpotSize = R and Evolution = 2 and HistComplex = 2 | D | 0.008949 |
| SpotDistribution = O and Evolution = 3 and Activity = 2 and LargestSpotSize = A | D | 0.008949 |
| SpotDistribution = I and Evolution = 3 and C-class = 0 and LargestSpotSize = A and Activity = 1 | D | 0.010273 |
| SpotDistribution = O and Evolution = 3 and C-class = 1 | D | 0.017738 |
|  | H | 0.504230 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

largestspotsize|spotdistribution|class
---|---|---
h|c|h
r|c|d
a|c|e
k|c|e
h|i|d
x|i|b
k|i|d
a|i|d
s|i|d
r|i|d
k|o|h
x|o|b
a|o|d
s|o|c
r|o|c
h|o|d
k|x|h
h|x|h
a|x|h
s|x|h
r|x|h

## JRip

Decision list:

rules | predicted class
---|---
(SpotDistribution = I) and (Evolution = 2) and (C-class = 1) and (Area = 2)|F (2.0/0.0)
(HistComplex = 2) and (Activity = 2) and (SpotDistribution = C) and (Evolution = 2) and (LargestSpotSize = K)|E (6.0/0.0)
(HistComplex = 2) and (Activity = 2) and (SpotDistribution = C) and (X-class = 1)|E (2.0/0.0)
(HistComplex = 2) and (LargestSpotSize = A) and (Activity = 2) and (SpotDistribution = O) and (Prev24Hour = 1)|E (5.0/0.0)
(HistComplex = 2) and (SpotDistribution = I) and (LargestSpotSize = S) and (Evolution = 2) and (Activity = 1) and (M-class = 0)|E (4.0/1.0)
(LargestSpotSize = X)|B (129.0/0.0)
(SpotDistribution = O) and (HistComplex = 1) and (Evolution = 2) and (Activity = 2) and (LargestSpotSize = R)|C (2.0/0.0)
(SpotDistribution = O) and (HistComplex = 1) and (Evolution = 2) and (Activity = 2) and (Prev24Hour = 2)|C (2.0/0.0)
(SpotDistribution = O) and (HistComplex = 1) and (Evolution = 2) and (LargestSpotSize = R) and (C-class = 0)|C (29.0/7.0)
(SpotDistribution = O) and (HistComplex = 1) and (LargestSpotSize = S) and (C-class = 0) and (Evolution = 2) and (Activity = 2)|C (6.0/1.0)
(SpotDistribution = O) and (HistComplex = 1) and (LargestSpotSize = R) and (C-class = 0) and (M-class = 0) and (Evolution = 1)|C (3.0/1.0)
(SpotDistribution = O) and (HistComplex = 1) and (LargestSpotSize = R) and (C-class = 0) and (M-class = 0)|C (50.0/17.0)
(SpotDistribution = O) and (LargestSpotSize = S) and (HistComplex = 1) and (C-class = 0) and (Evolution = 2)|C (19.0/5.0)
(SpotDistribution = O) and (LargestSpotSize = S) and (HistComplex = 1) and (C-class = 0) and (Activity = 2) and (Prev24Hour = 1)|C (3.0/0.0)
(SpotDistribution = O) and (LargestSpotSize = S) and (HistComplex = 1) and (C-class = 0) and (M-class = 1)|C (2.0/0.0)
(SpotDistribution = O) and (LargestSpotSize = S) and (HistComplex = 1) and (C-class = 0) and (Activity = 1) and (Evolution = 3)|C (28.0/10.0)
(SpotDistribution = O) and (Evolution = 2) and (LargestSpotSize = R) and (Activity = 1) and (HistComplex = 2)|C (11.0/2.0)
(SpotDistribution = O) and (LargestSpotSize = S) and (Evolution = 2) and (C-class = 0) and (Activity = 2)|C (3.0/1.0)
(SpotDistribution = O) and (LargestSpotSize = S) and (Evolution = 2) and (C-class = 0)|C (20.0/9.0)
(SpotDistribution = O) and (HistComplex = 1) and (C-class = 1)|C (17.0/8.0)
(SpotDistribution = O) and (Activity = 1) and (HistComplex = 1) and (LargestSpotSize = R) and (M-class = 0)|C (2.0/0.0)
(SpotDistribution = O) and (Activity = 1) and (C-class = 0) and (LargestSpotSize = A) and (Evolution = 2) and (HistComplex = 2) and (M-class = 0)|C (7.0/2.0)
(SpotDistribution = O) and (Activity = 1) and (Evolution = 3) and (LargestSpotSize = S) and (HistComplex = 2)|C (11.0/4.0)
(SpotDistribution = O) and (HistComplex = 1) and (Evolution = 1)|C (3.0/1.0)
(SpotDistribution = O) and (HistComplex = 1) and (C-class = 3)|C (3.0/1.0)
(SpotDistribution = I) and (Evolution = 3) and (C-class = 0) and (LargestSpotSize = A) and (HistComplex = 1) and (M-class = 1)|D (2.0/0.0)
(SpotDistribution = I) and (Evolution = 3) and (C-class = 0) and (LargestSpotSize = A) and (HistComplex = 1)|D (10.0/1.0)
(SpotDistribution = I) and (Evolution = 3) and (LargestSpotSize = K) and (Area = 1)|D (9.0/0.0)
(SpotDistribution = I) and (Evolution = 3) and (C-class = 0) and (LargestSpotSize = R) and (HistComplex = 2)|D (6.0/1.0)
(SpotDistribution = I) and (Evolution = 3) and (LargestSpotSize = A) and (Activity = 1) and (C-class = 1)|D (3.0/0.0)
(SpotDistribution = I) and (C-class = 0) and (Evolution = 3) and (M-class = 1)|D (3.0/0.0)
(SpotDistribution = I) and (C-class = 0) and (HistComplex = 1) and (LargestSpotSize = A)|D (4.0/0.0)
(SpotDistribution = I) and (Evolution = 3) and (C-class = 0) and (HistComplex = 1) and (Activity = 2)|D (2.0/0.0)
(SpotDistribution = I) and (Evolution = 3) and (C-class = 0) and (Area = 1) and (Activity = 1) and (HistComplex = 2) and (LargestSpotSize = S)|D (4.0/1.0)
(SpotDistribution = I) and (Evolution = 3) and (HistComplex = 1) and (LargestSpotSize = A)|D (4.0/1.0)
(SpotDistribution = I) and (C-class = 0) and (LargestSpotSize = R) and (Evolution = 2) and (HistComplex = 2)|D (4.0/0.0)
(SpotDistribution = O) and (Evolution = 3) and (Activity = 2) and (LargestSpotSize = A)|D (4.0/0.0)
(SpotDistribution = I) and (Evolution = 3) and (C-class = 0) and (LargestSpotSize = A) and (Activity = 1)|D (13.0/5.0)
(SpotDistribution = O) and (Evolution = 3) and (C-class = 1)|D (2.0/0.0)
|H (518.0/220.0)


## PART

Decision list:

rules | predicted class
---|---
SpotDistribution = X|H (298.0)
LargestSpotSize = X|B (129.0)
SpotDistribution = C AND Area = 2|E (16.0/7.0)
SpotDistribution = O AND LargestSpotSize = R AND HistComplex = 1 AND Evolution = 3|C (57.0/20.0)
SpotDistribution = O AND LargestSpotSize = R AND HistComplex = 1|C (36.0/9.0)
SpotDistribution = O AND LargestSpotSize = S AND C-class = 0 AND HistComplex = 1 AND Activity = 1 AND Evolution = 3|C (29.0/10.0)
SpotDistribution = O AND LargestSpotSize = S AND C-class = 0 AND HistComplex = 1 AND Activity = 1|C (21.0/6.0)
SpotDistribution = O AND LargestSpotSize = S AND C-class = 0 AND HistComplex = 2 AND Evolution = 2|C (23.0/10.0)
SpotDistribution = O AND LargestSpotSize = R|C (18.0/7.0)
HistComplex = 1 AND SpotDistribution = I AND LargestSpotSize = A|D (23.0/3.0)
HistComplex = 1 AND Evolution = 2|C (26.0/9.0)
HistComplex = 1 AND C-class = 0 AND SpotDistribution = O|D (18.0/10.0)
HistComplex = 1 AND C-class = 0|D (17.0/7.0)
SpotDistribution = O AND LargestSpotSize = S AND C-class = 0|D (18.0/9.0)
SpotDistribution = O AND LargestSpotSize = A AND Evolution = 2|E (20.0/10.0)
HistComplex = 1|D (24.0/12.0)
SpotDistribution = O AND C-class = 0|D (23.0/10.0)
LargestSpotSize = R|D (15.0/4.0)
SpotDistribution = I AND Evolution = 3 AND LargestSpotSize = A AND Activity = 1|D (19.0/5.0)
SpotDistribution = I AND Evolution = 3 AND LargestSpotSize = A|E (11.0/6.0)
SpotDistribution = I AND C-class = 0 AND Evolution = 2 AND LargestSpotSize = A|D (24.0/14.0)
SpotDistribution = I AND C-class = 1|D (21.0/11.0)
C-class = 0 AND Evolution = 2|E (19.0/11.0)
SpotDistribution = I AND Evolution = 3|D (19.0/7.0)
SpotDistribution = O|D (15.0/8.0)
|F (18.0/10.0)


## J48 Decision Tree

* SpotDistribution = X: H (199.0)
* SpotDistribution = O
	* LargestSpotSize = A: D (40.0/25.0)
	* LargestSpotSize = R: C (68.0/22.0)
	* LargestSpotSize = S: C (85.0/34.0)
	* LargestSpotSize = X: B (75.0)
	* LargestSpotSize = K: C (1.0)
	* LargestSpotSize = H: D (10.0/5.0)
* SpotDistribution = I
	* LargestSpotSize = A: D (67.0/30.0)
	* LargestSpotSize = R: D (18.0/6.0)
	* LargestSpotSize = S: D (26.0/13.0)
	* LargestSpotSize = X: B (11.0)
	* LargestSpotSize = K: D (14.0/6.0)
	* LargestSpotSize = H: D (2.0/1.0)
* SpotDistribution = C: E (22.0/11.0)


## SimpleCart Decision Tree

		* SpotDistribution=(C)|(I)|(O)
	* LargestSpotSize=(X): B(129.0/0.0)
	* LargestSpotSize!=(X)
			* SpotDistribution=(C)|(I): D(109.0/108.0)
			* SpotDistribution!=(C)|(I): C(171.0/142.0)
		* SpotDistribution!=(C)|(I)|(O): H(298.0/0.0)


