# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = X | H | 0.312042 |
| SpotDistribution = O and LargestSpotSize = X | B | 0.124468 |
| SpotDistribution = O and LargestSpotSize!=(X) and SpotDistribution != I and LargestSpotSize != X and C-class != 1 and LargestSpotSize!=(H) and Activity!=(2) and Evolution!=(2) and HistComplex!=(2) | C | 0.110874 |
| LargestSpotSize = A and SpotDistribution = I and Area = 1 | D | 0.044013 |
| LargestSpotSize = A and SpotDistribution = O and Area = 1 | D | 0.013824 |
| LargestSpotSize = R and SpotDistribution = I and Area = 1 | D | 0.015470 |
| LargestSpotSize = K and SpotDistribution = I and Area = 1 | D | 0.012032 |
| SpotDistribution = I and LargestSpotSize = X | B | 0.015550 |
| LargestSpotSize = S and SpotDistribution = I and Area = 1 | D | 0.010333 |
| LargestSpotSize = K and SpotDistribution = C and Area = 2 | E | 0.007143 |
| SpotDistribution = O and LargestSpotSize = S and C-class = 0 and HistComplex = 2 and Evolution = 3 | D | 0.003378 |
| SpotDistribution = O and LargestSpotSize = R and HistComplex = 1 and C-class = 1 | D | 0.004807 |
| SpotDistribution = I and LargestSpotSize = S and HistComplex = 2 and Evolution = 2 | E | 0.002612 |
| LargestSpotSize = H and SpotDistribution = O and Area = 1 | D | 0.003747 |
| SpotDistribution = C and LargestSpotSize = K and Prev24Hour = 1 | F | 0.002720 |
| SpotDistribution = C and LargestSpotSize = A | E | 0.003186 |
| SpotDistribution = O and LargestSpotSize = S and C-class = 1 and Evolution = 3 | D | 0.003085 |
| SpotDistribution = O and LargestSpotSize = S and C-class = 1 and Evolution = 2 | C | 0.003626 |
| SpotDistribution = I and LargestSpotSize = K and C-class = 1 | E | 0.001722 |
| SpotDistribution = O and LargestSpotSize!=(X) and SpotDistribution != I and LargestSpotSize != X and C-class = 1 and Evolution!=(3) | E | 0.001150 |
| SpotDistribution = O and LargestSpotSize = A and C-class = 4 | E | 0.002291 |
| SpotDistribution = O and LargestSpotSize = S and C-class = 0 and HistComplex = 2 and Evolution = 1 | D | 0.001740 |
| LargestSpotSize = A and SpotDistribution = I and Area = 2 | F | 0.002172 |
| SpotDistribution = I and LargestSpotSize = A and HistComplex = 2 and Evolution = 2 and C-class = 2 | F | 0.001449 |
| LargestSpotSize = R and SpotDistribution = C and Area = 1 | D | 0.001799 |
| SpotDistribution = O and LargestSpotSize = S and C-class = 2 | D | 0.001351 |
| SpotDistribution = I and LargestSpotSize = H | E | 0.001529 |
| LargestSpotSize = H and SpotDistribution = I and Area = 1 | D | 0.000451 |
| SpotDistribution = O and LargestSpotSize = S and C-class = 3 | D | 0.000676 |
| SpotDistribution = O and LargestSpotSize = S and C-class = 0 and HistComplex = 1 and Activity = 1 and Evolution = 1 | D | 0.000676 |
| SpotDistribution = O and LargestSpotSize = S and C-class = 5 | E | 0.001147 |
| SpotDistribution = O and LargestSpotSize = S and C-class = 6 | E | 0.001147 |
| SpotDistribution = O and LargestSpotSize = A and C-class = 3 | E | 0.001147 |
| SpotDistribution = C and LargestSpotSize = H | E | 0.001147 |
| SpotDistribution = I and LargestSpotSize = R and Evolution = 1 | C | 0.001305 |
| SpotDistribution = I and LargestSpotSize = A and HistComplex = 2 and Evolution = 2 and C-class = 3 | E | 0.000574 |
| LargestSpotSize = K and SpotDistribution = I and Area = 2 | E | 0.002064 |
| LargestSpotSize = R and SpotDistribution = O and Area = 1 | C | 0.059450 |
| LargestSpotSize = S and SpotDistribution = O and Area = 1 | C | 0.055477 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = X | H | 0.312042 |
| LargestSpotSize = X | B | 0.198473 |
| SpotDistribution = C and Area = 2 | E | 0.013982 |
| SpotDistribution = O and C-class = 0 and LargestSpotSize = R and HistComplex = 1 and Evolution = 3 | C | 0.066138 |
| SpotDistribution = O and C-class = 0 and LargestSpotSize = R and HistComplex = 1 | C | 0.032755 |
| SpotDistribution = O and LargestSpotSize = S and C-class = 0 and HistComplex = 1 and Activity = 1 and Evolution = 3 | C | 0.043393 |
| SpotDistribution = O and LargestSpotSize = R | C | 0.012440 |
| SpotDistribution = O and LargestSpotSize = S and C-class = 0 and HistComplex = 1 and Activity = 1 | C | 0.023796 |
| SpotDistribution = O and LargestSpotSize = S and C-class = 0 and HistComplex = 2 and Evolution = 2 | C | 0.018389 |
| HistComplex = 1 and Evolution = 3 and SpotDistribution = I and LargestSpotSize = A | D | 0.072934 |
| HistComplex = 1 and Evolution = 3 and C-class = 0 and SpotDistribution = I | D | 0.028918 |
| HistComplex = 1 and SpotDistribution = I | D | 0.018621 |
| SpotDistribution = I and LargestSpotSize = K | D | 0.037267 |
| SpotDistribution = C | E | 0.011287 |
| SpotDistribution = O and LargestSpotSize = A and Activity = 1 and Evolution = 3 and HistComplex = 2 | D | 0.021662 |
| HistComplex = 1 and Evolution = 2 and Activity = 1 | C | 0.011345 |
| HistComplex = 1 and Evolution = 3 and LargestSpotSize = S | D | 0.044528 |
| HistComplex = 1 and Evolution = 3 | D | 0.100520 |
| HistComplex = 2 and SpotDistribution = I and LargestSpotSize = A and Evolution = 3 and Activity = 1 | D | 0.044846 |
| HistComplex = 2 and C-class = 0 and LargestSpotSize = S and SpotDistribution = O | D | 0.051511 |
| HistComplex = 2 and C-class = 0 and LargestSpotSize = A and SpotDistribution = I and Activity = 1 | D | 0.018412 |
| HistComplex = 2 and SpotDistribution = I and LargestSpotSize = A and Evolution = 2 | D | 0.023965 |
| HistComplex = 2 and C-class = 0 and LargestSpotSize = S | D | 0.012019 |
| HistComplex = 1 | C | 0.089056 |
| C-class = 0 and LargestSpotSize = A and Activity = 1 | C | 0.034678 |
| LargestSpotSize = A and SpotDistribution = O | E | 0.066441 |
| C-class = 0 and Activity = 1 | D | 0.150165 |
| C-class = 1 | D | 0.048900 |
|  | D | 0.123967 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = I and Evolution = 2 and Activity = 2 and LargestSpotSize = A | F | 0.003877 |
| Area = 2 and Prev24Hour = 1 | F | 0.004353 |
| HistComplex = 2 and Activity = 2 and SpotDistribution = C and Area = 2 | E | 0.008543 |
| HistComplex = 2 and LargestSpotSize = A and Activity = 2 and Prev24Hour = 1 and SpotDistribution = O | E | 0.005814 |
| HistComplex = 2 and SpotDistribution = I and LargestSpotSize = A and Evolution = 3 | E | 0.005478 |
| HistComplex = 2 and SpotDistribution = I and LargestSpotSize = S and C-class = 0 and Evolution = 2 and M-class = 0 | E | 0.003646 |
| LargestSpotSize = X | B | 0.143488 |
| SpotDistribution = O and HistComplex = 1 and C-class = 0 and Evolution = 2 and LargestSpotSize = S | C | 0.027678 |
| SpotDistribution = O and LargestSpotSize = R and Evolution = 2 and C-class = 0 and HistComplex = 1 | C | 0.023141 |
| SpotDistribution = O and LargestSpotSize = R and C-class = 0 and Evolution = 1 | C | 0.007601 |
| SpotDistribution = O and HistComplex = 1 and C-class = 0 and LargestSpotSize = S and Prev24Hour = 1 | C | 0.025247 |
| SpotDistribution = O and LargestSpotSize = R and C-class = 0 and Evolution = 2 and Activity = 1 | C | 0.005226 |
| SpotDistribution = O and LargestSpotSize = R and C-class = 0 and HistComplex = 1 and M-class = 0 | C | 0.032327 |
| SpotDistribution = O and Evolution = 2 and C-class = 0 and LargestSpotSize = A and HistComplex = 2 and Activity = 1 | C | 0.006768 |
| SpotDistribution = O and LargestSpotSize = S and Evolution = 2 and C-class = 0 and Activity = 1 | C | 0.008604 |
| SpotDistribution = O and HistComplex = 1 and Evolution = 2 | C | 0.003838 |
| SpotDistribution = O and Evolution = 3 and LargestSpotSize = S and HistComplex = 2 and Activity = 1 | C | 0.006102 |
| SpotDistribution = O and HistComplex = 1 | C | 0.003686 |
| SpotDistribution = I and LargestSpotSize = R and HistComplex = 1 | C | 0.004388 |
| SpotDistribution = I and Activity = 2 and Evolution = 3 and HistComplex = 1 | D | 0.017241 |
| SpotDistribution = I and Evolution = 3 and LargestSpotSize = K | D | 0.014401 |
| SpotDistribution = I and C-class = 0 and LargestSpotSize = R | D | 0.029805 |
| SpotDistribution = I and LargestSpotSize = A and HistComplex = 1 | D | 0.029805 |
| SpotDistribution = I and Activity = 2 | D | 0.034805 |
| SpotDistribution = O and C-class = 0 and LargestSpotSize = H | D | 0.011166 |
| SpotDistribution = O and C-class = 0 | D | 0.126970 |
| SpotDistribution = I and C-class = 0 and HistComplex = 2 | D | 0.024513 |
| C-class = 1 and LargestSpotSize = A | D | 0.013433 |
| SpotDistribution = I and HistComplex = 1 | D | 0.010711 |
| SpotDistribution = O | D | 0.014400 |
| SpotDistribution = C | D | 0.005089 |
|  | H | 0.737624 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

largestspotsize|spotdistribution|area|class
---|---|---|---
k|c|2|e
k|i|2|e
a|i|2|f
r|o|2|h
k|c|1|f
h|c|1|h
a|c|1|e
r|c|1|d
x|i|1|b
h|i|1|d
k|i|1|d
r|i|1|d
s|i|1|d
a|i|1|d
k|o|1|h
x|o|1|b
a|o|1|d
r|o|1|c
s|o|1|c
h|o|1|d
h|x|1|h
r|x|1|h
a|x|1|h
s|x|1|h

## JRip

Decision list:

rules | predicted class
---|---
(SpotDistribution = I) and (Evolution = 2) and (Activity = 2) and (LargestSpotSize = A)|F (18.0/10.0)
(Area = 2) and (Prev24Hour = 1)|F (16.0/8.0)
(HistComplex = 2) and (Activity = 2) and (SpotDistribution = C) and (Area = 2)|E (8.0/1.0)
(HistComplex = 2) and (LargestSpotSize = A) and (Activity = 2) and (Prev24Hour = 1) and (SpotDistribution = O)|E (5.0/0.0)
(HistComplex = 2) and (SpotDistribution = I) and (LargestSpotSize = A) and (Evolution = 3)|E (31.0/19.0)
(HistComplex = 2) and (SpotDistribution = I) and (LargestSpotSize = S) and (C-class = 0) and (Evolution = 2) and (M-class = 0)|E (8.0/3.0)
(LargestSpotSize = X)|B (130.0/0.0)
(SpotDistribution = O) and (HistComplex = 1) and (C-class = 0) and (Evolution = 2) and (LargestSpotSize = S)|C (29.0/7.0)
(SpotDistribution = O) and (LargestSpotSize = R) and (Evolution = 2) and (C-class = 0) and (HistComplex = 1)|C (26.0/7.0)
(SpotDistribution = O) and (LargestSpotSize = R) and (C-class = 0) and (Evolution = 1)|C (8.0/2.0)
(SpotDistribution = O) and (HistComplex = 1) and (C-class = 0) and (LargestSpotSize = S) and (Prev24Hour = 1)|C (38.0/12.0)
(SpotDistribution = O) and (LargestSpotSize = R) and (C-class = 0) and (Evolution = 2) and (Activity = 1)|C (9.0/2.0)
(SpotDistribution = O) and (LargestSpotSize = R) and (C-class = 0) and (HistComplex = 1) and (M-class = 0)|C (52.0/18.0)
(SpotDistribution = O) and (Evolution = 2) and (C-class = 0) and (LargestSpotSize = A) and (HistComplex = 2) and (Activity = 1)|C (9.0/3.0)
(SpotDistribution = O) and (LargestSpotSize = S) and (Evolution = 2) and (C-class = 0) and (Activity = 1)|C (19.0/8.0)
(SpotDistribution = O) and (HistComplex = 1) and (Evolution = 2)|C (15.0/7.0)
(SpotDistribution = O) and (Evolution = 3) and (LargestSpotSize = S) and (HistComplex = 2) and (Activity = 1)|C (10.0/4.0)
(SpotDistribution = O) and (HistComplex = 1)|C (35.0/22.0)
(SpotDistribution = I) and (LargestSpotSize = R) and (HistComplex = 1)|C (14.0/8.0)
(SpotDistribution = I) and (Activity = 2) and (Evolution = 3) and (HistComplex = 1)|D (7.0/0.0)
(SpotDistribution = I) and (Evolution = 3) and (LargestSpotSize = K)|D (8.0/0.0)
(SpotDistribution = I) and (C-class = 0) and (LargestSpotSize = R)|D (11.0/2.0)
(SpotDistribution = I) and (LargestSpotSize = A) and (HistComplex = 1)|D (16.0/2.0)
(SpotDistribution = I) and (Activity = 2)|D (13.0/5.0)
(SpotDistribution = O) and (C-class = 0) and (LargestSpotSize = H)|D (6.0/1.0)
(SpotDistribution = O) and (C-class = 0)|D (28.0/13.0)
(SpotDistribution = I) and (C-class = 0) and (HistComplex = 2)|D (22.0/10.0)
(C-class = 1) and (LargestSpotSize = A)|D (11.0/6.0)
(SpotDistribution = I) and (HistComplex = 1)|D (14.0/8.0)
(SpotDistribution = O)|D (15.0/9.0)
(SpotDistribution = C)|D (14.0/9.0)
|H (310.0/13.0)


## PART

Decision list:

rules | predicted class
---|---
SpotDistribution = X|H (298.0)
LargestSpotSize = X|B (130.0)
SpotDistribution = C AND Area = 2|E (16.0/6.0)
SpotDistribution = O AND C-class = 0 AND LargestSpotSize = R AND HistComplex = 1 AND Evolution = 3|C (54.0/19.0)
SpotDistribution = O AND C-class = 0 AND LargestSpotSize = R AND HistComplex = 1|C (31.0/8.0)
SpotDistribution = O AND LargestSpotSize = S AND C-class = 0 AND HistComplex = 1 AND Activity = 1 AND Evolution = 3|C (33.0/11.0)
SpotDistribution = O AND LargestSpotSize = R|C (25.0/11.0)
SpotDistribution = O AND LargestSpotSize = S AND C-class = 0 AND HistComplex = 1 AND Activity = 1|C (22.0/6.0)
SpotDistribution = O AND LargestSpotSize = S AND C-class = 0 AND HistComplex = 2 AND Evolution = 2|C (20.0/9.0)
HistComplex = 1 AND Evolution = 3 AND SpotDistribution = I AND LargestSpotSize = A|D (18.0/2.0)
HistComplex = 1 AND Evolution = 3 AND C-class = 0 AND SpotDistribution = I|D (17.0/7.0)
HistComplex = 1 AND SpotDistribution = I|D (16.0/7.0)
SpotDistribution = I AND LargestSpotSize = K|D (21.0/9.0)
SpotDistribution = C|E (15.0/7.0)
SpotDistribution = O AND LargestSpotSize = A AND Activity = 1 AND Evolution = 3 AND HistComplex = 2|D (13.0/6.0)
HistComplex = 1 AND Evolution = 2 AND Activity = 1|C (11.0/5.0)
HistComplex = 1 AND Evolution = 3 AND LargestSpotSize = S|D (13.0/7.0)
HistComplex = 1 AND Evolution = 3|D (15.0/7.0)
HistComplex = 2 AND SpotDistribution = I AND LargestSpotSize = A AND Evolution = 3 AND Activity = 1|D (19.0/7.0)
HistComplex = 2 AND C-class = 0 AND LargestSpotSize = S AND SpotDistribution = O|D (17.0/9.0)
HistComplex = 2 AND C-class = 0 AND LargestSpotSize = A AND SpotDistribution = I AND Activity = 1|D (17.0/9.0)
HistComplex = 2 AND SpotDistribution = I AND LargestSpotSize = A AND Evolution = 2|D (25.0/14.0)
HistComplex = 2 AND C-class = 0 AND LargestSpotSize = S|D (16.0/9.0)
HistComplex = 1|C (12.0/2.0)
C-class = 0 AND LargestSpotSize = A AND Activity = 1|C (11.0/5.0)
LargestSpotSize = A AND SpotDistribution = O|E (15.0/5.0)
C-class = 0 AND Activity = 1|D (14.0/2.0)
C-class = 1|D (19.0/12.0)
|D (22.0/13.0)


## J48 Decision Tree

* SpotDistribution = X: H (298.0)
* SpotDistribution = O
	* LargestSpotSize = A
		* C-class = 0
			* Activity = 1
				* Evolution = 1: D (3.0/1.0)
				* Evolution = 2: C (13.0/5.0)
				* Evolution = 3
					* HistComplex = 1: D (7.0/4.0)
					* HistComplex = 2: D (12.0/6.0)
			* Activity = 2: D (7.0/4.0)
		* C-class = 1: D (9.0/5.0)
		* C-class = 2: D (3.0/1.0)
		* C-class = 3: E (1.0)
		* C-class = 4: E (2.0)
		* C-class = 5: D (0.0)
		* C-class = 6: D (0.0)
		* C-class = 7: D (0.0)
		* C-class = 8: D (0.0)
	* LargestSpotSize = R
		* HistComplex = 1
			* C-class = 0
				* Evolution = 1: C (5.0/1.0)
				* Evolution = 2: C (26.0/7.0)
				* Evolution = 3: C (54.0/19.0)
			* C-class = 1: D (7.0/2.0)
			* C-class = 2: C (0.0)
			* C-class = 3: C (1.0)
			* C-class = 4: C (0.0)
			* C-class = 5: C (1.0)
			* C-class = 6: C (0.0)
			* C-class = 7: C (0.0)
			* C-class = 8: C (0.0)
		* HistComplex = 2: C (16.0/6.0)
	* LargestSpotSize = S
		* C-class = 0
			* HistComplex = 1
				* Activity = 1
					* Evolution = 1: D (2.0/1.0)
					* Evolution = 2: C (20.0/5.0)
					* Evolution = 3: C (33.0/11.0)
				* Activity = 2: C (13.0/3.0)
			* HistComplex = 2
				* Evolution = 1: D (7.0/4.0)
				* Evolution = 2: C (20.0/9.0)
				* Evolution = 3: D (10.0/5.0)
		* C-class = 1
			* Evolution = 1: D (0.0)
			* Evolution = 2: C (9.0/4.0)
			* Evolution = 3: D (7.0/3.0)
		* C-class = 2: D (4.0/2.0)
		* C-class = 3: D (2.0/1.0)
		* C-class = 4: C (0.0)
		* C-class = 5: E (1.0)
		* C-class = 6: E (1.0)
		* C-class = 7: C (0.0)
		* C-class = 8: C (0.0)
	* LargestSpotSize = X: B (117.0)
	* LargestSpotSize = K: C (1.0)
	* LargestSpotSize = H
		* Evolution = 1: D (0.0)
		* Evolution = 2: D (6.0/4.0)
		* Evolution = 3: D (7.0/3.0)
* SpotDistribution = I
	* LargestSpotSize = A
		* HistComplex = 1: D (21.0/2.0)
		* HistComplex = 2
			* Evolution = 1: D (2.0/1.0)
			* Evolution = 2
				* C-class = 0
					* Activity = 1: D (16.0/8.0)
					* Activity = 2: D (10.0/6.0)
				* C-class = 1: D (9.0/4.0)
				* C-class = 2: F (3.0/1.0)
				* C-class = 3: E (2.0/1.0)
				* C-class = 4: D (1.0)
				* C-class = 5: D (0.0)
				* C-class = 6: D (0.0)
				* C-class = 7: D (0.0)
				* C-class = 8: D (0.0)
			* Evolution = 3
				* Activity = 1: D (19.0/7.0)
				* Activity = 2: D (13.0/8.0)
	* LargestSpotSize = R
		* Evolution = 1: C (1.0)
		* Evolution = 2: D (9.0/4.0)
		* Evolution = 3
			* HistComplex = 1: D (11.0/4.0)
			* HistComplex = 2: D (7.0/1.0)
	* LargestSpotSize = S
		* HistComplex = 1: D (16.0/8.0)
		* HistComplex = 2
			* Evolution = 1: D (1.0)
			* Evolution = 2: E (11.0/6.0)
			* Evolution = 3: D (10.0/6.0)
	* LargestSpotSize = X: B (13.0)
	* LargestSpotSize = K
		* C-class = 0: D (7.0/3.0)
		* C-class = 1: E (6.0/3.0)
		* C-class = 2: D (4.0/1.0)
		* C-class = 3: D (3.0/1.0)
		* C-class = 4: D (1.0)
		* C-class = 5: D (0.0)
		* C-class = 6: D (0.0)
		* C-class = 7: D (0.0)
		* C-class = 8: D (0.0)
	* LargestSpotSize = H: E (3.0/1.0)
* SpotDistribution = C
	* LargestSpotSize = A: E (9.0/4.0)
	* LargestSpotSize = R: D (3.0/1.0)
	* LargestSpotSize = S: E (0.0)
	* LargestSpotSize = X: E (0.0)
	* LargestSpotSize = K
		* Prev24Hour = 1: F (10.0/5.0)
		* Prev24Hour = 2: E (2.0)
		* Prev24Hour = 3: E (6.0/1.0)
	* LargestSpotSize = H: E (1.0)


## SimpleCart Decision Tree

		* SpotDistribution=(C)|(I)|(O)
	* LargestSpotSize=(X): B(130.0/0.0)
	* LargestSpotSize!=(X)
			* SpotDistribution=(C)|(I)
			* Area=(2)
					* Prev24Hour=(3)|(2): E(7.0/1.0)
					* Prev24Hour!=(3)|(2): F(8.0/7.0)
			* Area!=(2)
				* HistComplex=(2)
						* LargestSpotSize=(K)|(R)
						* Evolution=(3): D(15.0/2.0)
						* Evolution!=(3)
									* C-class=(4)|(2)|(1): F(3.0/4.0)
									* C-class!=(4)|(2)|(1): D(7.0/2.0)
						* LargestSpotSize!=(K)|(R): D(49.0/57.0)
				* HistComplex!=(2): D(37.0/18.0)
			* SpotDistribution!=(C)|(I)
						* LargestSpotSize=(K)|(S)|(R)|(X)
						* C-class=(6)|(2)|(1): D(15.0/15.0)
						* C-class!=(6)|(2)|(1): C(135.0/75.0)
						* LargestSpotSize!=(K)|(S)|(R)|(X)
							* C-class=(4)|(3)|(2)|(1)
					* Evolution=(3): D(4.0/2.0)
					* Evolution!=(3): E(9.0/4.0)
							* C-class!=(4)|(3)|(2)|(1)
					* LargestSpotSize=(H): D(6.0/3.0)
					* LargestSpotSize!=(H)
						* Activity=(2): D(3.0/4.0)
						* Activity!=(2)
							* Evolution=(2): C(8.0/5.0)
							* Evolution!=(2)
								* HistComplex=(2): D(8.0/6.0)
								* HistComplex!=(2): C(4.0/4.0)
		* SpotDistribution!=(C)|(I)|(O): H(298.0/0.0)


