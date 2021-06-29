# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = X | H | 0.311390 |
| SpotDistribution = O and LargestSpotSize = X | B | 0.122081 |
| SpotDistribution = O and LargestSpotSize!=(X) and SpotDistribution != I and LargestSpotSize != X | D | 0.056665 |
| LargestSpotSize = R and SpotDistribution = O and Area = 1 | C | 0.061791 |
| SpotDistribution = O and LargestSpotSize = S | C | 0.055336 |
| LargestSpotSize = A and SpotDistribution = I and Area = 1 | D | 0.043259 |
| SpotDistribution = C | E | 0.011234 |
| SpotDistribution = I and LargestSpotSize = R | D | 0.014821 |
| SpotDistribution = I and LargestSpotSize = X | B | 0.015476 |
| LargestSpotSize = S and SpotDistribution = I and Area = 1 | D | 0.010055 |
| SpotDistribution = I and LargestSpotSize = K and Area = 1 and Evolution = 3 | D | 0.010667 |
| LargestSpotSize = H and SpotDistribution = I and Area = 1 | E | 0.002291 |
| LargestSpotSize = A and SpotDistribution = C and Area = 1 | D | 0.002399 |
| SpotDistribution = O and LargestSpotSize = H and Evolution = 2 | E | 0.001478 |
| SpotDistribution = I and LargestSpotSize = K and Area = 2 | E | 0.001722 |
| LargestSpotSize = K and SpotDistribution = I and Area = 2 | F | 0.001632 |
| LargestSpotSize = R and SpotDistribution = C and Area = 1 | D | 0.002688 |
| SpotDistribution = I and LargestSpotSize = K and Area = 1 and Evolution = 2 | F | 0.001401 |
| SpotDistribution = O and LargestSpotSize = K | C | 0.001302 |
| LargestSpotSize = K and SpotDistribution = I and Area = 1 | D | 0.008925 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = X | H | 0.311390 |
| LargestSpotSize = X | B | 0.194825 |
| Area != 1 and Prev24Hour != 1 | E | 0.015733 |
| SpotDistribution = O and LargestSpotSize != H and LargestSpotSize != A and Evolution != 1 and C-class = 1 and LargestSpotSize != R and Evolution != 2 | D | 0.008990 |
| SpotDistribution = O and LargestSpotSize != H and LargestSpotSize != A and Evolution != 1 and C-class = 1 and LargestSpotSize != R | C | 0.020210 |
| SpotDistribution = O and LargestSpotSize != H and C-class != 1 and LargestSpotSize != A and Evolution != 1 and C-class = 0 and LargestSpotSize = R and HistComplex = 1 and Evolution != 2 | C | 0.070654 |
| Area != 1 and C-class != 1 and Activity = 1 | E | 0.003807 |
| SpotDistribution = O and LargestSpotSize != H and C-class = 1 and HistComplex = 1 | D | 0.020623 |
| SpotDistribution = O and LargestSpotSize != H and LargestSpotSize != A and LargestSpotSize != S and Evolution = 2 and HistComplex = 1 | C | 0.056229 |
| SpotDistribution = O and LargestSpotSize != H and LargestSpotSize != A and HistComplex = 1 and Activity != 1 and Evolution = 2 | C | 0.015922 |
| SpotDistribution = O and LargestSpotSize != H and LargestSpotSize != A and HistComplex = 1 and Activity = 1 and Evolution != 2 and LargestSpotSize != R | C | 0.034507 |
| SpotDistribution = O and LargestSpotSize != H and LargestSpotSize != A and HistComplex = 1 and Activity = 1 and LargestSpotSize != R | C | 0.022105 |
| LargestSpotSize = R and SpotDistribution = O and Evolution = 2 | C | 0.009434 |
| Area != 1 and C-class != 1 | F | 0.015208 |
| LargestSpotSize = R and Evolution != 1 and Activity = 1 and HistComplex != 1 | D | 0.044092 |
| LargestSpotSize = R and Activity = 1 and Evolution != 3 | C | 0.016708 |
| SpotDistribution = O and C-class != 1 and LargestSpotSize != H and Evolution != 1 and C-class = 0 and Activity = 1 and HistComplex != 1 and LargestSpotSize != A and Evolution = 2 | C | 0.018335 |
| LargestSpotSize = R and Activity = 1 and C-class = 0 | D | 0.144300 |
| SpotDistribution != O and LargestSpotSize = R and Activity != 1 | D | 0.025100 |
| SpotDistribution != O and HistComplex = 1 and LargestSpotSize = A and C-class = 0 | D | 0.085935 |
| HistComplex = 1 and Evolution != 2 and SpotDistribution != O and LargestSpotSize != A and C-class = 0 | D | 0.026176 |
| SpotDistribution = O and C-class != 1 and LargestSpotSize != H and Evolution != 1 and C-class = 0 and Activity = 1 and LargestSpotSize = A and HistComplex = 1 | D | 0.023124 |
| SpotDistribution != O and LargestSpotSize != R and HistComplex = 1 and Activity = 1 | D | 0.004174 |
| SpotDistribution != O and LargestSpotSize != R and C-class != 4 and Evolution = 3 and LargestSpotSize != S and Activity = 1 and LargestSpotSize = A and C-class = 0 | D | 0.029231 |
| SpotDistribution != O and LargestSpotSize != R and C-class != 4 and HistComplex != 1 and Evolution = 3 and LargestSpotSize = K | D | 0.027875 |
| SpotDistribution = O and C-class != 1 and LargestSpotSize != H and Evolution != 1 and C-class = 0 and Activity = 1 and LargestSpotSize = A and Evolution != 2 | D | 0.010016 |
| SpotDistribution != O and LargestSpotSize != R and C-class != 4 and HistComplex != 1 and C-class != 0 and Evolution != 2 and C-class != 3 and Activity = 1 | D | 0.011042 |
| SpotDistribution = O and C-class != 1 and LargestSpotSize != H and Evolution != 1 and LargestSpotSize != A and HistComplex != 1 and Activity = 1 | C | 0.009569 |
| LargestSpotSize != R and SpotDistribution != O and HistComplex != 1 and C-class != 4 and C-class = 1 and Activity != 1 | D | 0.011748 |
| LargestSpotSize != R and LargestSpotSize != K and C-class != 0 and LargestSpotSize != H and Evolution = 3 and HistComplex != 1 | D | 0.014024 |
| LargestSpotSize != R and LargestSpotSize = K | F | 0.010870 |
| LargestSpotSize != R and C-class != 3 and SpotDistribution = C | D | 0.008488 |
| LargestSpotSize = R | D | 0.005643 |
| C-class = 3 | E | 0.021114 |
| SpotDistribution != O and C-class != 0 and Activity = 1 | F | 0.004980 |
| C-class != 0 and LargestSpotSize = A and SpotDistribution = O | E | 0.020559 |
| SpotDistribution = O and Activity != 1 and LargestSpotSize = S and HistComplex != 1 | D | 0.014815 |
| SpotDistribution != O and C-class = 0 and LargestSpotSize != A and Activity = 1 | D | 0.010443 |
| SpotDistribution = O and Activity != 1 and LargestSpotSize != S | E | 0.025175 |
| LargestSpotSize = H | D | 0.021635 |
| SpotDistribution = O and HistComplex != 1 and Evolution = 1 | D | 0.021368 |
| SpotDistribution = O and Evolution = 2 | C | 0.022857 |
| SpotDistribution != O and C-class = 0 and LargestSpotSize = A and Activity != 1 and Evolution = 2 | F | 0.010323 |
| SpotDistribution != O and C-class = 0 and LargestSpotSize = A and Evolution = 2 | D | 0.038820 |
| SpotDistribution != O and Evolution = 3 | D | 0.015802 |
| SpotDistribution != O | E | 0.233645 |
|  | C | 0.342342 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| HistComplex = 2 and Activity = 2 and SpotDistribution = C | E | 0.009728 |
| LargestSpotSize = X | B | 0.136026 |
| SpotDistribution = O and HistComplex = 1 and Evolution = 2 and LargestSpotSize = S | C | 0.031306 |
| SpotDistribution = O and LargestSpotSize = R and Evolution = 2 and C-class = 0 | C | 0.034196 |
| SpotDistribution = O and HistComplex = 1 and LargestSpotSize = R and C-class = 0 | C | 0.039734 |
| SpotDistribution = O and LargestSpotSize = S and HistComplex = 1 and C-class = 0 | C | 0.019590 |
| SpotDistribution = O and LargestSpotSize = S and Evolution = 2 and C-class = 0 | C | 0.008890 |
| SpotDistribution = O and Activity = 1 and Evolution = 3 and LargestSpotSize = S | C | 0.005098 |
| SpotDistribution = I and Evolution = 3 and HistComplex = 1 and LargestSpotSize = A | D | 0.032345 |
| SpotDistribution = I and Evolution = 3 and C-class = 0 | D | 0.041860 |
| SpotDistribution = O and Evolution = 3 | D | 0.092672 |
|  | H | 0.531194 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

largestspotsize|spotdistribution|area|class
---|---|---|---
a|c|2|h
k|c|2|e
a|i|2|h
k|i|2|f
k|c|1|e
r|c|1|d
a|c|1|d
h|c|1|h
r|o|2|h
h|i|1|e
x|i|1|b
s|i|1|d
r|i|1|d
a|i|1|d
k|i|1|d
k|o|1|h
x|o|1|b
a|o|1|d
h|o|1|d
r|o|1|c
s|o|1|c
k|x|1|h
h|x|1|h
a|x|1|h
r|x|1|h
s|x|1|h

## JRip

Decision list:

rules | predicted class
---|---
(HistComplex = 2) and (Activity = 2) and (SpotDistribution = C)|E (23.0/9.0)
(LargestSpotSize = X)|B (128.0/0.0)
(SpotDistribution = O) and (HistComplex = 1) and (Evolution = 2) and (LargestSpotSize = S)|C (31.0/6.0)
(SpotDistribution = O) and (LargestSpotSize = R) and (Evolution = 2) and (C-class = 0)|C (33.0/6.0)
(SpotDistribution = O) and (HistComplex = 1) and (LargestSpotSize = R) and (C-class = 0)|C (61.0/20.0)
(SpotDistribution = O) and (LargestSpotSize = S) and (HistComplex = 1) and (C-class = 0)|C (38.0/15.0)
(SpotDistribution = O) and (LargestSpotSize = S) and (Evolution = 2) and (C-class = 0)|C (21.0/9.0)
(SpotDistribution = O) and (Activity = 1) and (Evolution = 3) and (LargestSpotSize = S)|C (19.0/9.0)
(SpotDistribution = I) and (Evolution = 3) and (HistComplex = 1) and (LargestSpotSize = A)|D (21.0/3.0)
(SpotDistribution = I) and (Evolution = 3) and (C-class = 0)|D (53.0/20.0)
(SpotDistribution = O) and (Evolution = 3)|D (49.0/21.0)
|H (480.0/182.0)


## PART

Decision list:

rules | predicted class
---|---
SpotDistribution = X|H (298.0)
LargestSpotSize = X|B (128.0)
Area != 1 AND Prev24Hour != 1|E (9.0/1.0)
SpotDistribution = O AND LargestSpotSize != H AND LargestSpotSize != A AND Evolution != 1 AND C-class = 1 AND LargestSpotSize != R AND Evolution != 2|D (9.0/4.0)
SpotDistribution = O AND LargestSpotSize != H AND LargestSpotSize != A AND Evolution != 1 AND C-class = 1 AND LargestSpotSize != R|C (8.0/3.0)
SpotDistribution = O AND LargestSpotSize != H AND C-class != 1 AND LargestSpotSize != A AND Evolution != 1 AND C-class = 0 AND LargestSpotSize = R AND HistComplex = 1 AND Evolution != 2|C (56.0/19.0)
Area != 1 AND C-class != 1 AND Activity = 1|E (6.0/3.0)
SpotDistribution = O AND LargestSpotSize != H AND C-class = 1 AND HistComplex = 1|D (9.0/2.0)
SpotDistribution = O AND LargestSpotSize != H AND LargestSpotSize != A AND LargestSpotSize != S AND Evolution = 2 AND HistComplex = 1|C (28.0/5.0)
SpotDistribution = O AND LargestSpotSize != H AND LargestSpotSize != A AND HistComplex = 1 AND Activity != 1 AND Evolution = 2|C (7.0/1.0)
SpotDistribution = O AND LargestSpotSize != H AND LargestSpotSize != A AND HistComplex = 1 AND Activity = 1 AND Evolution != 2 AND LargestSpotSize != R|C (36.0/16.0)
SpotDistribution = O AND LargestSpotSize != H AND LargestSpotSize != A AND HistComplex = 1 AND Activity = 1 AND LargestSpotSize != R|C (21.0/5.0)
LargestSpotSize = R AND SpotDistribution = O AND Evolution = 2|C (7.0/1.0)
Area != 1 AND C-class != 1|F (6.0/2.0)
LargestSpotSize = R AND Evolution != 1 AND Activity = 1 AND HistComplex != 1|D (11.0/2.0)
LargestSpotSize = R AND Activity = 1 AND Evolution != 3|C (10.0/2.0)
SpotDistribution = O AND C-class != 1 AND LargestSpotSize != H AND Evolution != 1 AND C-class = 0 AND Activity = 1 AND HistComplex != 1 AND LargestSpotSize != A AND Evolution = 2|C (18.0/8.0)
LargestSpotSize = R AND Activity = 1 AND C-class = 0|D (6.0/2.0)
SpotDistribution != O AND LargestSpotSize = R AND Activity != 1|D (6.0/1.0)
SpotDistribution != O AND HistComplex = 1 AND LargestSpotSize = A AND C-class = 0|D (19.0/2.0)
HistComplex = 1 AND Evolution != 2 AND SpotDistribution != O AND LargestSpotSize != A AND C-class = 0|D (13.0/5.0)
SpotDistribution = O AND C-class != 1 AND LargestSpotSize != H AND Evolution != 1 AND C-class = 0 AND Activity = 1 AND LargestSpotSize = A AND HistComplex = 1|D (13.0/6.0)
SpotDistribution != O AND LargestSpotSize != R AND HistComplex = 1 AND Activity = 1|D (7.0/4.0)
SpotDistribution != O AND LargestSpotSize != R AND C-class != 4 AND Evolution = 3 AND LargestSpotSize != S AND Activity = 1 AND LargestSpotSize = A AND C-class = 0|D (15.0/6.0)
SpotDistribution != O AND LargestSpotSize != R AND C-class != 4 AND HistComplex != 1 AND Evolution = 3 AND LargestSpotSize = K|D (11.0/3.0)
SpotDistribution = O AND C-class != 1 AND LargestSpotSize != H AND Evolution != 1 AND C-class = 0 AND Activity = 1 AND LargestSpotSize = A AND Evolution != 2|D (11.0/6.0)
SpotDistribution != O AND LargestSpotSize != R AND C-class != 4 AND HistComplex != 1 AND C-class != 0 AND Evolution != 2 AND C-class != 3 AND Activity = 1|D (8.0/4.0)
SpotDistribution = O AND C-class != 1 AND LargestSpotSize != H AND Evolution != 1 AND LargestSpotSize != A AND HistComplex != 1 AND Activity = 1|C (11.0/5.0)
LargestSpotSize != R AND SpotDistribution != O AND HistComplex != 1 AND C-class != 4 AND C-class = 1 AND Activity != 1|D (12.0/7.0)
LargestSpotSize != R AND LargestSpotSize != K AND C-class != 0 AND LargestSpotSize != H AND Evolution = 3 AND HistComplex != 1|D (11.0/5.0)
LargestSpotSize != R AND LargestSpotSize = K|F (9.0/5.0)
LargestSpotSize != R AND C-class != 3 AND SpotDistribution = C|D (7.0/3.0)
LargestSpotSize = R|D (6.0/3.0)
C-class = 3|E (6.0/2.0)
SpotDistribution != O AND C-class != 0 AND Activity = 1|F (6.0/3.0)
C-class != 0 AND LargestSpotSize = A AND SpotDistribution = O|E (7.0/2.0)
SpotDistribution = O AND Activity != 1 AND LargestSpotSize = S AND HistComplex != 1|D (6.0/3.0)
SpotDistribution != O AND C-class = 0 AND LargestSpotSize != A AND Activity = 1|D (9.0/4.0)
SpotDistribution = O AND Activity != 1 AND LargestSpotSize != S|E (10.0/4.0)
LargestSpotSize = H|D (11.0/5.0)
SpotDistribution = O AND HistComplex != 1 AND Evolution = 1|D (9.0/4.0)
SpotDistribution = O AND Evolution = 2|C (8.0/3.0)
SpotDistribution != O AND C-class = 0 AND LargestSpotSize = A AND Activity != 1 AND Evolution = 2|F (9.0/5.0)
SpotDistribution != O AND C-class = 0 AND LargestSpotSize = A AND Evolution = 2|D (17.0/10.0)
SpotDistribution != O AND Evolution = 3|D (12.0/6.0)
SpotDistribution != O|E (9.0/6.0)
|C (6.0/1.0)


## J48 Decision Tree

* SpotDistribution = X: H (298.0)
* SpotDistribution = O
	* LargestSpotSize = A: D (54.0/29.0)
	* LargestSpotSize = R
		* C-class = 0: C (100.0/30.0)
		* C-class = 1: D (7.0/2.0)
		* C-class = 2: C (0.0)
		* C-class = 3: C (0.0)
		* C-class = 4: C (0.0)
		* C-class = 5: C (1.0)
		* C-class = 6: C (0.0)
		* C-class = 7: C (0.0)
		* C-class = 8: C (0.0)
	* LargestSpotSize = S: C (129.0/54.0)
	* LargestSpotSize = X: B (115.0)
	* LargestSpotSize = K: C (1.0)
	* LargestSpotSize = H
		* Evolution = 1: D (0.0)
		* Evolution = 2: E (7.0/4.0)
		* Evolution = 3: D (7.0/3.0)
* SpotDistribution = I
	* LargestSpotSize = A: D (104.0/46.0)
	* LargestSpotSize = R: D (26.0/9.0)
	* LargestSpotSize = S: D (39.0/22.0)
	* LargestSpotSize = X: B (13.0)
	* LargestSpotSize = K
		* Area = 1
			* Evolution = 1: D (0.0)
			* Evolution = 2: F (7.0/4.0)
			* Evolution = 3: D (8.0)
		* Area = 2: E (6.0/3.0)
	* LargestSpotSize = H: E (2.0)
* SpotDistribution = C: E (33.0/15.0)


## SimpleCart Decision Tree

		* SpotDistribution=(C)|(I)|(O)
	* LargestSpotSize=(X): B(128.0/0.0)
	* LargestSpotSize!=(X)
			* SpotDistribution=(C)|(I)
			* Area=(2): E(14.0/11.0)
			* Area!=(2): D(108.0/92.0)
			* SpotDistribution!=(C)|(I)
					* LargestSpotSize=(S)|(R)|(X): C(148.0/89.0)
					* LargestSpotSize!=(S)|(R)|(X): D(31.0/38.0)
		* SpotDistribution!=(C)|(I)|(O): H(298.0/0.0)


