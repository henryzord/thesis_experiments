# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = X | H | 0.311390 |
| SpotDistribution = O and LargestSpotSize!=(X) and SpotDistribution != I | C | 0.101028 |
| SpotDistribution = O and LargestSpotSize = X | B | 0.122081 |
| LargestSpotSize = A and SpotDistribution = I and HistComplex = 2 | D | 0.021900 |
| LargestSpotSize = A and SpotDistribution = I and HistComplex = 1 | D | 0.021988 |
| LargestSpotSize = A and SpotDistribution = O and HistComplex = 1 | D | 0.009204 |
| SpotDistribution = I and LargestSpotSize = K and Area = 1 | D | 0.012519 |
| SpotDistribution = I and LargestSpotSize = R and C-class = 0 | D | 0.011309 |
| SpotDistribution = I and LargestSpotSize = X | B | 0.015476 |
| LargestSpotSize = A and SpotDistribution = O and HistComplex = 2 | D | 0.006772 |
| LargestSpotSize = K and SpotDistribution = C and HistComplex = 2 | E | 0.009112 |
| LargestSpotSize = S and SpotDistribution = I and HistComplex = 1 | D | 0.007756 |
| SpotDistribution = O and LargestSpotSize = H and Activity = 1 and C-class = 0 | D | 0.005979 |
| SpotDistribution = O and LargestSpotSize = S and C-class = 1 and Evolution = 3 | D | 0.003739 |
| LargestSpotSize = S and SpotDistribution = I and HistComplex = 2 | D | 0.005219 |
| SpotDistribution = I and LargestSpotSize = A and HistComplex = 2 and M-class = 0 and Evolution = 3 and Activity = 2 | E | 0.002867 |
| SpotDistribution = O and LargestSpotSize = H and Activity = 2 | E | 0.003429 |
| SpotDistribution = O and LargestSpotSize = A and C-class = 1 and Evolution = 2 | E | 0.002062 |
| SpotDistribution = I and LargestSpotSize = A and HistComplex = 2 and M-class = 0 and Evolution = 2 and C-class = 1 | F | 0.002179 |
| SpotDistribution = I and LargestSpotSize = S and C-class = 0 and HistComplex = 2 and Evolution = 2 | E | 0.002294 |
| SpotDistribution = I and LargestSpotSize = R and C-class = 1 and Evolution = 3 | D | 0.003024 |
| SpotDistribution = C and M-class = 0 and Area = 1 and C-class = 0 | E | 0.004082 |
| SpotDistribution = C and M-class = 0 and Area = 2 and Prev24Hour = 1 | F | 0.003257 |
| SpotDistribution = O and LargestSpotSize = S and C-class = 3 | D | 0.001348 |
| SpotDistribution = O and LargestSpotSize = S and C-class = 0 and HistComplex = 2 and Evolution = 3 and Activity = 2 | D | 0.001795 |
| SpotDistribution = O and LargestSpotSize = A and C-class = 0 and Activity = 2 and Evolution = 2 | E | 0.001527 |
| SpotDistribution = O and LargestSpotSize = A and C-class = 4 | E | 0.002288 |
| SpotDistribution = I and LargestSpotSize = S and C-class = 0 and HistComplex = 2 and Evolution = 3 and Activity = 2 | E | 0.001527 |
| SpotDistribution = O and LargestSpotSize = S and C-class = 0 and HistComplex = 2 and Evolution = 1 | D | 0.001735 |
| SpotDistribution = I and LargestSpotSize = K and Area = 2 | E | 0.002062 |
| SpotDistribution = I and LargestSpotSize = A and HistComplex = 2 and M-class = 0 and Evolution = 2 and C-class = 2 | F | 0.001451 |
| SpotDistribution = C and M-class = 0 and Area = 1 and C-class = 1 | D | 0.001795 |
| SpotDistribution = O and LargestSpotSize = S and C-class = 2 | D | 0.001348 |
| SpotDistribution = I and LargestSpotSize = R and C-class = 2 | C | 0.002601 |
| SpotDistribution = C and M-class = 0 and Area = 1 and C-class = 2 | D | 0.001346 |
| SpotDistribution = C and M-class = 3 | D | 0.001346 |
| SpotDistribution = O and LargestSpotSize = A and C-class = 3 | E | 0.001145 |
| SpotDistribution = I and LargestSpotSize = A and HistComplex = 2 and M-class = 4 | E | 0.001145 |
| SpotDistribution = O and LargestSpotSize = S and C-class = 6 | E | 0.001145 |
| SpotDistribution = I and LargestSpotSize = S and C-class = 5 | E | 0.001145 |
| SpotDistribution = C and M-class = 0 and Area = 1 and C-class = 5 | E | 0.001145 |
| SpotDistribution = I and LargestSpotSize = A and HistComplex = 2 and M-class = 0 and Evolution = 1 | F | 0.001088 |
| SpotDistribution = I and LargestSpotSize = S and C-class = 2 | F | 0.001088 |
| SpotDistribution = C and M-class = 0 and Area = 1 and C-class = 4 | F | 0.001088 |
| SpotDistribution = I and LargestSpotSize = H | D | 0.000674 |
| LargestSpotSize = H and SpotDistribution = I and HistComplex = 2 | E | 0.000573 |
| SpotDistribution = C and M-class = 1 | E | 0.003657 |
| SpotDistribution = I and LargestSpotSize = A and HistComplex = 2 and M-class = 0 and Evolution = 2 and C-class = 3 | E | 0.000573 |
| SpotDistribution = I and LargestSpotSize = R and C-class = 1 and Evolution = 2 | C | 0.000652 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = X | H | 0.311390 |
| LargestSpotSize = X | B | 0.194825 |
| Area != 1 and LargestSpotSize != A | E | 0.020603 |
| SpotDistribution = O and LargestSpotSize != A and LargestSpotSize != H and Activity = 1 and Evolution != 1 and LargestSpotSize != S and HistComplex = 1 and C-class != 1 | C | 0.113641 |
| SpotDistribution = O and C-class != 4 and LargestSpotSize != H and LargestSpotSize != A and Activity != 1 | C | 0.033180 |
| SpotDistribution = O and Activity != 1 and Evolution = 2 | E | 0.011911 |
| SpotDistribution = O and Activity = 1 and LargestSpotSize = H | D | 0.017055 |
| SpotDistribution = O and Activity = 1 and LargestSpotSize != A and Evolution != 1 and C-class != 0 and M-class = 0 and Evolution != 2 | C | 0.012004 |
| SpotDistribution = O and Activity = 1 and C-class = 0 and LargestSpotSize = R and Evolution = 2 | C | 0.013588 |
| SpotDistribution = O and Activity = 1 and C-class = 0 and HistComplex = 1 | C | 0.075073 |
| LargestSpotSize = R and C-class != 2 and Evolution != 1 and Activity = 1 and Evolution != 2 | D | 0.158239 |
| SpotDistribution = C | E | 0.012121 |
| LargestSpotSize = R and C-class != 2 and Evolution != 3 and C-class = 0 | D | 0.062919 |
| SpotDistribution = O and Evolution = 1 | D | 0.018711 |
| SpotDistribution = O and Activity = 1 and LargestSpotSize != A and C-class = 1 and HistComplex = 1 | D | 0.029412 |
| SpotDistribution = O | D | 0.185848 |
| LargestSpotSize != R and HistComplex = 1 | D | 0.105042 |
| HistComplex != 1 and Evolution != 2 and LargestSpotSize != K and C-class != 2 and Prev24Hour != 3 and LargestSpotSize != R and Activity = 1 | D | 0.057554 |
| HistComplex != 1 and Prev24Hour != 2 and LargestSpotSize != R and C-class != 0 and Prev24Hour = 1 and LargestSpotSize = K | D | 0.035526 |
| HistComplex != 1 and LargestSpotSize != K and C-class != 3 and C-class != 2 and LargestSpotSize != R and Evolution != 2 and C-class = 0 | D | 0.003910 |
| HistComplex != 1 and LargestSpotSize != K and C-class != 3 and C-class != 2 and Evolution = 2 and LargestSpotSize != R and C-class != 0 and Activity = 1 | F | 0.009732 |
|  | D | 0.176136 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = I and Evolution = 2 and Activity = 2 and LargestSpotSize = A | F | 0.003150 |
| Area = 2 and Prev24Hour = 1 | F | 0.004643 |
| HistComplex = 2 and LargestSpotSize = A and Activity = 2 | E | 0.007403 |
| SpotDistribution = C | E | 0.010863 |
| Activity = 2 and LargestSpotSize = H | E | 0.002619 |
| LargestSpotSize = X | B | 0.140969 |
| SpotDistribution = O and LargestSpotSize = R and C-class = 0 | C | 0.078199 |
| SpotDistribution = O and LargestSpotSize = S | C | 0.070276 |
| SpotDistribution = I | D | 0.136546 |
| SpotDistribution = O and Evolution = 3 | D | 0.100049 |
|  | H | 0.634043 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

largestspotsize|spotdistribution|histcomplex|class
---|---|---|---
r|c|2|h
a|c|2|e
k|c|2|e
h|i|2|e
x|i|2|b
s|i|2|d
k|i|2|d
r|i|2|d
a|i|2|d
a|c|1|d
x|o|2|b
r|c|1|d
a|o|2|d
h|o|2|d
s|o|2|c
r|o|2|c
h|x|2|h
r|i|1|d
x|i|1|b
s|i|1|d
a|i|1|d
a|x|2|h
r|x|2|h
s|x|2|h
h|o|1|c
x|o|1|b
k|o|1|h
a|o|1|d
s|o|1|c
r|o|1|c
k|x|1|h
a|x|1|h
h|x|1|h
r|x|1|h
s|x|1|h

## JRip

Decision list:

rules | predicted class
---|---
(SpotDistribution = I) and (Evolution = 2) and (Activity = 2) and (LargestSpotSize = A)|F (17.0/10.0)
(Area = 2) and (Prev24Hour = 1)|F (15.0/7.0)
(HistComplex = 2) and (LargestSpotSize = A) and (Activity = 2)|E (22.0/10.0)
(SpotDistribution = C)|E (19.0/6.0)
(Activity = 2) and (LargestSpotSize = H)|E (4.0/1.0)
(LargestSpotSize = X)|B (128.0/0.0)
(SpotDistribution = O) and (LargestSpotSize = R) and (C-class = 0)|C (101.0/30.0)
(SpotDistribution = O) and (LargestSpotSize = S)|C (131.0/56.0)
(SpotDistribution = I)|D (149.0/58.0)
(SpotDistribution = O) and (Evolution = 3)|D (41.0/19.0)
|H (330.0/33.0)


## PART

Decision list:

rules | predicted class
---|---
SpotDistribution = X|H (261.0)
LargestSpotSize = X|B (112.0)
Area != 1 AND LargestSpotSize != A|E (20.0/7.0)
SpotDistribution = O AND LargestSpotSize != A AND LargestSpotSize != H AND Activity = 1 AND Evolution != 1 AND LargestSpotSize != S AND HistComplex = 1 AND C-class != 1|C (74.0/23.0)
SpotDistribution = O AND C-class != 4 AND LargestSpotSize != H AND LargestSpotSize != A AND Activity != 1|C (20.0/6.0)
SpotDistribution = O AND Activity != 1 AND Evolution = 2|E (6.0/1.0)
SpotDistribution = O AND Activity = 1 AND LargestSpotSize = H|D (11.0/5.0)
SpotDistribution = O AND Activity = 1 AND LargestSpotSize != A AND Evolution != 1 AND C-class != 0 AND M-class = 0 AND Evolution != 2|C (10.0/4.0)
SpotDistribution = O AND Activity = 1 AND C-class = 0 AND LargestSpotSize = R AND Evolution = 2|C (6.0)
SpotDistribution = O AND Activity = 1 AND C-class = 0 AND HistComplex = 1|C (65.0/24.0)
LargestSpotSize = R AND C-class != 2 AND Evolution != 1 AND Activity = 1 AND Evolution != 2|D (14.0/4.0)
SpotDistribution = C|E (14.0/7.0)
LargestSpotSize = R AND C-class != 2 AND Evolution != 3 AND C-class = 0|D (9.0/4.0)
SpotDistribution = O AND Evolution = 1|D (9.0/4.0)
SpotDistribution = O AND Activity = 1 AND LargestSpotSize != A AND C-class = 1 AND HistComplex = 1|D (4.0/2.0)
SpotDistribution = O|D (62.0/32.0)
LargestSpotSize != R AND HistComplex = 1|D (33.0/8.0)
HistComplex != 1 AND Evolution != 2 AND LargestSpotSize != K AND C-class != 2 AND Prev24Hour != 3 AND LargestSpotSize != R AND Activity = 1|D (28.0/11.0)
HistComplex != 1 AND Prev24Hour != 2 AND LargestSpotSize != R AND C-class != 0 AND Prev24Hour = 1 AND LargestSpotSize = K|D (10.0/4.0)
HistComplex != 1 AND LargestSpotSize != K AND C-class != 3 AND C-class != 2 AND LargestSpotSize != R AND Evolution != 2 AND C-class = 0|D (8.0/5.0)
HistComplex != 1 AND LargestSpotSize != K AND C-class != 3 AND C-class != 2 AND Evolution = 2 AND LargestSpotSize != R AND C-class != 0 AND Activity = 1|F (6.0/3.0)
|D (56.0/32.0)


## J48 Decision Tree

* SpotDistribution = X: H (298.0)
* SpotDistribution = O
	* LargestSpotSize = A
		* C-class = 0
			* Activity = 1
				* Evolution = 1: D (3.0/1.0)
				* Evolution = 2
					* HistComplex = 1: D (4.0/1.0)
					* HistComplex = 2: C (9.0/4.0)
				* Evolution = 3: C (19.0/10.0)
			* Activity = 2
				* Evolution = 1: D (0.0)
				* Evolution = 2: E (3.0/1.0)
				* Evolution = 3: D (3.0)
		* C-class = 1
			* Evolution = 1: D (0.0)
			* Evolution = 2: E (5.0/2.0)
			* Evolution = 3: D (3.0)
		* C-class = 2: D (3.0/1.0)
		* C-class = 3: E (1.0)
		* C-class = 4: E (2.0)
		* C-class = 5: D (0.0)
		* C-class = 6: D (0.0)
		* C-class = 7: D (0.0)
		* C-class = 8: D (0.0)
	* LargestSpotSize = R: C (112.0/36.0)
	* LargestSpotSize = S
		* C-class = 0
			* HistComplex = 1: C (66.0/20.0)
			* HistComplex = 2
				* Evolution = 1: D (7.0/4.0)
				* Evolution = 2: C (21.0/11.0)
				* Evolution = 3
					* Activity = 1: C (9.0/4.0)
					* Activity = 2: D (3.0/1.0)
		* C-class = 1
			* Evolution = 1: C (0.0)
			* Evolution = 2: C (7.0/2.0)
			* Evolution = 3: D (9.0/4.0)
		* C-class = 2: D (4.0/2.0)
		* C-class = 3: D (4.0/2.0)
		* C-class = 4: C (0.0)
		* C-class = 5: C (0.0)
		* C-class = 6: E (1.0)
		* C-class = 7: C (0.0)
		* C-class = 8: C (0.0)
	* LargestSpotSize = X: B (115.0)
	* LargestSpotSize = K: C (1.0)
	* LargestSpotSize = H
		* Activity = 1
			* C-class = 0: D (11.0/4.0)
			* C-class = 1: C (2.0/1.0)
			* C-class = 2: D (0.0)
			* C-class = 3: D (0.0)
			* C-class = 4: D (0.0)
			* C-class = 5: D (0.0)
			* C-class = 6: D (0.0)
			* C-class = 7: D (0.0)
			* C-class = 8: D (0.0)
		* Activity = 2: E (3.0)
* SpotDistribution = I
	* LargestSpotSize = A
		* HistComplex = 1: D (24.0/4.0)
		* HistComplex = 2
			* M-class = 0
				* Evolution = 1: F (1.0)
				* Evolution = 2
					* C-class = 0: D (25.0/14.0)
					* C-class = 1: F (8.0/4.0)
					* C-class = 2: F (3.0/1.0)
					* C-class = 3: E (2.0/1.0)
					* C-class = 4: D (2.0/1.0)
					* C-class = 5: D (0.0)
					* C-class = 6: D (0.0)
					* C-class = 7: D (0.0)
					* C-class = 8: D (0.0)
				* Evolution = 3
					* Activity = 1: D (19.0/7.0)
					* Activity = 2: E (10.0/5.0)
			* M-class = 1: D (5.0/1.0)
			* M-class = 2: D (0.0)
			* M-class = 3: D (0.0)
			* M-class = 4: E (1.0)
			* M-class = 5: D (0.0)
	* LargestSpotSize = R
		* C-class = 0: D (17.0/5.0)
		* C-class = 1
			* Evolution = 1: D (0.0)
			* Evolution = 2: C (2.0/1.0)
			* Evolution = 3: D (4.0/1.0)
		* C-class = 2: C (2.0)
		* C-class = 3: D (0.0)
		* C-class = 4: D (0.0)
		* C-class = 5: D (0.0)
		* C-class = 6: D (0.0)
		* C-class = 7: D (0.0)
		* C-class = 8: D (0.0)
	* LargestSpotSize = S
		* C-class = 0
			* HistComplex = 1: D (13.0/5.0)
			* HistComplex = 2
				* Evolution = 1: D (1.0)
				* Evolution = 2: E (8.0/4.0)
				* Evolution = 3
					* Activity = 1: D (4.0/1.0)
					* Activity = 2: E (3.0/1.0)
		* C-class = 1: D (4.0/1.0)
		* C-class = 2: F (1.0)
		* C-class = 3: D (0.0)
		* C-class = 4: D (0.0)
		* C-class = 5: E (1.0)
		* C-class = 6: D (0.0)
		* C-class = 7: D (0.0)
		* C-class = 8: D (0.0)
	* LargestSpotSize = X: B (13.0)
	* LargestSpotSize = K
		* Area = 1: D (18.0/5.0)
		* Area = 2: E (5.0/2.0)
	* LargestSpotSize = H: D (2.0/1.0)
* SpotDistribution = C
	* M-class = 0
		* Area = 1
			* C-class = 0: E (7.0/2.0)
			* C-class = 1: D (3.0/1.0)
			* C-class = 2: D (1.0)
			* C-class = 3: E (0.0)
			* C-class = 4: F (1.0)
			* C-class = 5: E (1.0)
			* C-class = 6: E (0.0)
			* C-class = 7: E (0.0)
			* C-class = 8: E (0.0)
		* Area = 2
			* Prev24Hour = 1: F (3.0)
			* Prev24Hour = 2: E (2.0)
			* Prev24Hour = 3: E (5.0/1.0)
	* M-class = 1: E (5.0/1.0)
	* M-class = 2: E (1.0)
	* M-class = 3: D (1.0)
	* M-class = 4: E (0.0)
	* M-class = 5: E (1.0)


## SimpleCart Decision Tree

		* SpotDistribution=(C)|(I)|(O)
	* LargestSpotSize=(X): B(128.0/0.0)
	* LargestSpotSize!=(X)
			* SpotDistribution=(C)|(I): D(108.0/108.0)
			* SpotDistribution!=(C)|(I): C(172.0/143.0)
		* SpotDistribution!=(C)|(I)|(O): H(298.0/0.0)


