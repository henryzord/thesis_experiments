# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = X | H | 0.311390 |
| SpotDistribution = O and LargestSpotSize = X | B | 0.121148 |
| LargestSpotSize = R and SpotDistribution = O and Area = 1 | C | 0.066504 |
| LargestSpotSize = A and SpotDistribution = I and Area = 1 | D | 0.042708 |
| LargestSpotSize = S and SpotDistribution = O and Area = 1 | C | 0.052763 |
| SpotDistribution = O and LargestSpotSize = A | D | 0.013567 |
| LargestSpotSize = S and SpotDistribution = I and Area = 1 | D | 0.013804 |
| LargestSpotSize = R and SpotDistribution = I and Area = 1 | D | 0.013061 |
| SpotDistribution = C | E | 0.012710 |
| LargestSpotSize = X and SpotDistribution = I and Area = 1 | B | 0.016647 |
| SpotDistribution = O and LargestSpotSize!=(X) and SpotDistribution != I and LargestSpotSize != K and C-class != 8 | E | 0.003913 |
| LargestSpotSize = K and SpotDistribution = I and Area = 1 | D | 0.011309 |
| SpotDistribution = O and LargestSpotSize = H and C-class = 0 | D | 0.005979 |
| LargestSpotSize = A and SpotDistribution = I and Area = 2 | F | 0.002174 |
| LargestSpotSize = K and SpotDistribution = I and Area = 2 | E | 0.001720 |
| LargestSpotSize = R and SpotDistribution = C and Area = 1 | D | 0.000674 |
| SpotDistribution = I and LargestSpotSize = H | E | 0.001527 |
| LargestSpotSize = H and SpotDistribution = I and Area = 1 | D | 0.000450 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = X | H | 0.311390 |
| LargestSpotSize = X | B | 0.194825 |
| Area != 1 and Prev24Hour = 1 | F | 0.010248 |
| SpotDistribution = C | E | 0.028929 |
| SpotDistribution = O and LargestSpotSize != H and LargestSpotSize != A and C-class = 1 and LargestSpotSize != R and HistComplex = 1 | C | 0.011392 |
| SpotDistribution = O and LargestSpotSize != H and LargestSpotSize != A and Activity = 1 and LargestSpotSize = R | C | 0.146917 |
| SpotDistribution != O and LargestSpotSize != R and HistComplex != 1 and Evolution != 2 | D | 0.103712 |
| SpotDistribution = O and LargestSpotSize != H and C-class = 0 and Evolution != 1 and LargestSpotSize != A | C | 0.110005 |
| Evolution = 3 | D | 0.344777 |
| SpotDistribution = O and LargestSpotSize != H and HistComplex != 1 and LargestSpotSize = A and C-class = 0 | C | 0.038523 |
| LargestSpotSize != R and HistComplex = 1 | D | 0.032803 |
| LargestSpotSize != R and SpotDistribution = O and LargestSpotSize != S | E | 0.062486 |
| LargestSpotSize != R and SpotDistribution != O and Activity != 1 | D | 0.039120 |
| LargestSpotSize != R and LargestSpotSize != S and C-class = 0 | D | 0.037143 |
|  | D | 0.243421 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = I and Evolution = 2 and C-class = 1 | F | 0.003343 |
| Area = 2 | F | 0.003338 |
| LargestSpotSize = A and Activity = 2 | E | 0.007142 |
| SpotDistribution = C | E | 0.012372 |
| LargestSpotSize = X | B | 0.140969 |
| SpotDistribution = O and HistComplex = 1 | C | 0.128558 |
| SpotDistribution = O and C-class = 0 and Evolution = 2 | C | 0.016803 |
| SpotDistribution = I | D | 0.142436 |
| SpotDistribution = O and C-class = 0 | D | 0.133659 |
|  | H | 0.681922 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

largestspotsize|spotdistribution|area|class
---|---|---|---
a|c|2|h
k|c|2|e
k|i|2|e
a|i|2|f
h|c|1|h
r|o|2|h
a|c|1|e
k|c|1|e
r|c|1|d
h|i|1|d
x|i|1|b
k|i|1|d
r|i|1|d
s|i|1|d
a|i|1|d
x|o|1|b
h|o|1|d
a|o|1|d
s|o|1|c
r|o|1|c
h|x|1|h
k|x|1|h
r|x|1|h
a|x|1|h
s|x|1|h

## JRip

Decision list:

rules | predicted class
---|---
(SpotDistribution = I) and (Evolution = 2) and (C-class = 1)|F (16.0/9.0)
(Area = 2)|F (21.0/13.0)
(LargestSpotSize = A) and (Activity = 2)|E (45.0/28.0)
(SpotDistribution = C)|E (9.0/3.0)
(LargestSpotSize = X)|B (127.0/0.0)
(SpotDistribution = O) and (HistComplex = 1)|C (203.0/72.0)
(SpotDistribution = O) and (C-class = 0) and (Evolution = 2)|C (41.0/18.0)
(SpotDistribution = I)|D (137.0/51.0)
(SpotDistribution = O) and (C-class = 0)|D (40.0/18.0)
|H (318.0/21.0)


## PART

Decision list:

rules | predicted class
---|---
SpotDistribution = X|H (298.0)
LargestSpotSize = X|B (128.0)
Area != 1 AND Prev24Hour = 1|F (16.0/7.0)
SpotDistribution = C|E (22.0/7.0)
SpotDistribution = O AND LargestSpotSize != H AND LargestSpotSize != A AND C-class = 1 AND LargestSpotSize != R AND HistComplex = 1|C (10.0/4.0)
SpotDistribution = O AND LargestSpotSize != H AND LargestSpotSize != A AND Activity = 1 AND LargestSpotSize = R|C (113.0/36.0)
SpotDistribution != O AND LargestSpotSize != R AND HistComplex != 1 AND Evolution != 2|D (55.0/19.0)
SpotDistribution = O AND LargestSpotSize != H AND C-class = 0 AND Evolution != 1 AND LargestSpotSize != A|C (96.0/34.0)
Evolution = 3|D (93.0/34.0)
SpotDistribution = O AND LargestSpotSize != H AND HistComplex != 1 AND LargestSpotSize = A AND C-class = 0|C (14.0/7.0)
LargestSpotSize != R AND HistComplex = 1|D (17.0/8.0)
LargestSpotSize != R AND SpotDistribution = O AND LargestSpotSize != S|E (14.0/5.0)
LargestSpotSize != R AND SpotDistribution != O AND Activity != 1|D (31.0/18.0)
LargestSpotSize != R AND LargestSpotSize != S AND C-class = 0|D (17.0/10.0)
|D (33.0/17.0)


## J48 Decision Tree

* SpotDistribution = X: H (298.0)
* SpotDistribution = O
	* LargestSpotSize = A: D (58.0/34.0)
	* LargestSpotSize = R: C (117.0/38.0)
	* LargestSpotSize = S: C (125.0/53.0)
	* LargestSpotSize = X: B (114.0)
	* LargestSpotSize = K: C (0.0)
	* LargestSpotSize = H
		* C-class = 0: D (11.0/4.0)
		* C-class = 1: E (4.0/2.0)
		* C-class = 2: D (0.0)
		* C-class = 3: D (0.0)
		* C-class = 4: D (0.0)
		* C-class = 5: D (0.0)
		* C-class = 6: D (0.0)
		* C-class = 7: D (0.0)
		* C-class = 8: D (0.0)
* SpotDistribution = I
	* LargestSpotSize = A: D (99.0/43.0)
	* LargestSpotSize = R: D (23.0/8.0)
	* LargestSpotSize = S: D (39.0/19.0)
	* LargestSpotSize = X: B (14.0)
	* LargestSpotSize = K
		* Area = 1: D (17.0/5.0)
		* Area = 2: E (6.0/3.0)
	* LargestSpotSize = H: E (3.0/1.0)
* SpotDistribution = C: E (29.0/11.0)


## SimpleCart Decision Tree

		* SpotDistribution=(C)|(I)|(O)
	* LargestSpotSize=(X): B(128.0/0.0)
	* LargestSpotSize!=(X)
			* SpotDistribution=(C)|(I)
			* Area=(2): E(12.0/10.0)
			* Area!=(2)
				* Evolution=(2)
								* C-class=(0)|(5)|(6)|(7): D(25.0/26.0)
								* C-class!=(0)|(5)|(6)|(7): F(13.0/17.0)
				* Evolution!=(2)
					* SpotDistribution=(C): E(6.0/3.0)
					* SpotDistribution!=(C)
							* LargestSpotSize=(S)|(R): D(26.0/16.0)
							* LargestSpotSize!=(S)|(R)
							* LargestSpotSize=(K): D(8.0/0.0)
							* LargestSpotSize!=(K): D(37.0/17.0)
			* SpotDistribution!=(C)|(I)
						* LargestSpotSize=(S)|(R)|(X)|(K)
				* HistComplex=(2): C(29.0/32.0)
				* HistComplex!=(2)
									* C-class=(0)|(4)|(6)|(7)|(8)
						* Evolution=(3): C(61.0/33.0)
						* Evolution!=(3)
							* Activity=(2): C(9.0/2.0)
							* Activity!=(2)
								* LargestSpotSize=(S): C(13.0/5.0)
								* LargestSpotSize!=(S): C(27.0/7.0)
									* C-class!=(0)|(4)|(6)|(7)|(8): C(12.0/12.0)
						* LargestSpotSize!=(S)|(R)|(X)|(K)
								* C-class=(0)|(5)|(6)|(7)|(8)
					* LargestSpotSize=(H): D(7.0/4.0)
					* LargestSpotSize!=(H): D(19.0/25.0)
								* C-class!=(0)|(5)|(6)|(7)|(8): E(10.0/8.0)
		* SpotDistribution!=(C)|(I)|(O): H(298.0/0.0)


