# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | H | 0.311390 |
| SpotDistribution = O and LargestSpotSize = X | B | 0.122081 |
| LargestSpotSize = R and SpotDistribution = O and Area = 1 | C | 0.066504 |
| SpotDistribution = O and LargestSpotSize!=(X) and SpotDistribution != I and LargestSpotSize != K and C-class != 1 and LargestSpotSize!=(H) | D | 0.039876 |
| LargestSpotSize = S and SpotDistribution = O and Area = 1 | C | 0.052763 |
| LargestSpotSize = A and SpotDistribution = I and Area = 1 | D | 0.042708 |
| LargestSpotSize = S and SpotDistribution = I and Area = 1 | D | 0.013804 |
| LargestSpotSize = X and SpotDistribution = I and Area = 1 | B | 0.015476 |
| SpotDistribution = I and LargestSpotSize = R | D | 0.013061 |
| LargestSpotSize = K and SpotDistribution = C and Area = 2 | E | 0.007105 |
| SpotDistribution = I and LargestSpotSize = K and Area = 1 | D | 0.011309 |
| SpotDistribution = C and C-class = 0 and Area = 1 | E | 0.006208 |
| SpotDistribution = C and C-class = 0 and Area = 2 and Prev24Hour = 1 | F | 0.002446 |
| SpotDistribution = I and LargestSpotSize = K and Area = 2 and Evolution = 3 | E | 0.002574 |
| SpotDistribution = O and LargestSpotSize!=(X) and SpotDistribution != I and LargestSpotSize != K and C-class = 2 | E | 0.000658 |
| SpotDistribution = O and LargestSpotSize!=(X) and SpotDistribution != I and LargestSpotSize != K and C-class = 4 | E | 0.002288 |
| SpotDistribution = O and LargestSpotSize!=(X) and SpotDistribution != I and LargestSpotSize != K and C-class = 1 | E | 0.000974 |
| SpotDistribution = I and LargestSpotSize = K and Area = 2 and Evolution = 2 | F | 0.002174 |
| LargestSpotSize = A and SpotDistribution = I and Area = 2 | F | 0.002174 |
| SpotDistribution = C and C-class = 3 | E | 0.001145 |
| SpotDistribution = C and C-class = 5 | E | 0.001145 |
| SpotDistribution = O and LargestSpotSize!=(X) and SpotDistribution != I and LargestSpotSize != K and C-class = 3 | E | 0.000192 |
| SpotDistribution = C and C-class = 4 | F | 0.001088 |
| LargestSpotSize = R and SpotDistribution = C and Area = 1 | D | 0.000674 |
| SpotDistribution = O and LargestSpotSize = A | D | 0.013567 |
| LargestSpotSize = H and SpotDistribution = I and Area = 1 | D | 0.000450 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = X | H | 0.311390 |
| LargestSpotSize = X | B | 0.194825 |
| SpotDistribution = O and HistComplex = 1 | C | 0.209838 |
| Area = 2 and SpotDistribution = C | E | 0.018137 |
| SpotDistribution = O and C-class = 0 and LargestSpotSize = S and Evolution = 2 | C | 0.014189 |
| SpotDistribution = I and HistComplex = 2 and Area = 1 and Evolution = 3 | D | 0.136047 |
| Activity = 1 and LargestSpotSize = R and Evolution = 2 | C | 0.011719 |
| SpotDistribution = O | D | 0.338088 |
| HistComplex = 1 | D | 0.130121 |
| C-class = 0 and SpotDistribution = I | D | 0.047348 |
| C-class = 1 | D | 0.012813 |
| SpotDistribution = I | F | 0.099291 |
|  | E | 0.571429 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = I and Evolution = 2 and Activity = 2 and LargestSpotSize = A | F | 0.003681 |
| Area = 2 | F | 0.004752 |
| HistComplex = 2 and Activity = 2 and LargestSpotSize = A | E | 0.008012 |
| HistComplex = 2 and SpotDistribution = I and LargestSpotSize = S | E | 0.004148 |
| LargestSpotSize = X | B | 0.140197 |
| SpotDistribution = O and LargestSpotSize = R | C | 0.083608 |
| SpotDistribution = O and LargestSpotSize = S and HistComplex = 1 | C | 0.054428 |
| SpotDistribution = I | D | 0.139421 |
| SpotDistribution = O and Evolution = 3 | D | 0.093432 |
|  | H | 0.611910 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

largestspotsize|spotdistribution|area|class
---|---|---|---
a|c|2|h
k|c|2|e
a|i|2|f
k|i|2|e
h|c|1|h
r|o|2|h
k|c|1|e
r|c|1|d
a|c|1|e
h|i|1|d
r|i|1|d
k|i|1|d
s|i|1|d
a|i|1|d
x|i|1|b
h|o|1|d
r|o|1|c
a|o|1|d
s|o|1|c
x|o|1|b
k|x|1|h
h|x|1|h
a|x|1|h
r|x|1|h
s|x|1|h

## JRip

Decision list:

rules | predicted class
---|---
(SpotDistribution = I) and (Evolution = 2) and (Activity = 2) and (LargestSpotSize = A)|F (19.0/11.0)
(Area = 2)|F (23.0/13.0)
(HistComplex = 2) and (Activity = 2) and (LargestSpotSize = A)|E (23.0/11.0)
(HistComplex = 2) and (SpotDistribution = I) and (LargestSpotSize = S)|E (23.0/14.0)
(LargestSpotSize = X)|B (128.0/0.0)
(SpotDistribution = O) and (LargestSpotSize = R)|C (116.0/37.0)
(SpotDistribution = O) and (LargestSpotSize = S) and (HistComplex = 1)|C (80.0/28.0)
(SpotDistribution = I)|D (126.0/44.0)
(SpotDistribution = O) and (Evolution = 3)|D (52.0/25.0)
|H (367.0/70.0)


## PART

Decision list:

rules | predicted class
---|---
SpotDistribution = X|H (298.0)
LargestSpotSize = X|B (128.0)
SpotDistribution = O AND HistComplex = 1|C (206.0/75.0)
Area = 2 AND SpotDistribution = C|E (14.0/5.0)
SpotDistribution = O AND C-class = 0 AND LargestSpotSize = S AND Evolution = 2|C (20.0/9.0)
SpotDistribution = I AND HistComplex = 2 AND Area = 1 AND Evolution = 3|D (58.0/20.0)
Activity = 1 AND LargestSpotSize = R AND Evolution = 2|C (15.0/6.0)
SpotDistribution = O|D (80.0/46.0)
HistComplex = 1|D (52.0/15.0)
C-class = 0 AND SpotDistribution = I|D (43.0/26.0)
C-class = 1|D (19.0/11.0)
SpotDistribution = I|F (14.0/7.0)
|E (10.0/3.0)


## J48 Decision Tree

* SpotDistribution = X: H (269.0)
* SpotDistribution = O
	* LargestSpotSize = A: D (55.0/33.0)
	* LargestSpotSize = R: C (104.0/32.0)
	* LargestSpotSize = S: C (111.0/50.0)
	* LargestSpotSize = X: B (103.0)
	* LargestSpotSize = K: C (0.0)
	* LargestSpotSize = H: D (15.0/8.0)
* SpotDistribution = I
	* LargestSpotSize = A: D (90.0/40.0)
	* LargestSpotSize = R: D (20.0/7.0)
	* LargestSpotSize = S: D (34.0/17.0)
	* LargestSpotSize = X: B (12.0)
	* LargestSpotSize = K
		* Area = 1: D (17.0/5.0)
		* Area = 2
			* Evolution = 1: F (0.0)
			* Evolution = 2: F (2.0)
			* Evolution = 3: E (3.0/1.0)
	* LargestSpotSize = H: D (2.0/1.0)
* SpotDistribution = C
	* C-class = 0
		* Area = 1: E (9.0/2.0)
		* Area = 2
			* Prev24Hour = 1: F (3.0/1.0)
			* Prev24Hour = 2: E (1.0)
			* Prev24Hour = 3: E (3.0)
	* C-class = 1: D (2.0/1.0)
	* C-class = 2: E (4.0/1.0)
	* C-class = 3: E (1.0)
	* C-class = 4: F (1.0)
	* C-class = 5: E (1.0)
	* C-class = 6: E (0.0)
	* C-class = 7: E (0.0)
	* C-class = 8: E (0.0)


## SimpleCart Decision Tree

		* SpotDistribution=(C)|(I)|(O)
	* LargestSpotSize=(X): B(128.0/0.0)
	* LargestSpotSize!=(X)
			* SpotDistribution=(C)|(I)
			* Area=(2): E(12.0/10.0)
			* Area!=(2)
				* Evolution=(2)
							* C-class=(4)|(2)|(1): F(12.0/12.0)
							* C-class!=(4)|(2)|(1): D(26.0/31.0)
				* Evolution!=(2): D(74.0/39.0)
			* SpotDistribution!=(C)|(I)
						* LargestSpotSize=(S)|(R)|(X)|(K)
				* HistComplex=(2): C(29.0/32.0)
				* HistComplex!=(2)
						* C-class=(2)|(1): D(10.0/9.0)
						* C-class!=(2)|(1)
						* Evolution=(3): C(63.0/33.0)
						* Evolution!=(3)
							* Activity=(2): C(9.0/2.0)
							* Activity!=(2)
								* LargestSpotSize=(S): C(14.0/6.0)
								* LargestSpotSize!=(S): C(28.0/7.0)
						* LargestSpotSize!=(S)|(R)|(X)|(K)
							* C-class=(4)|(3)|(2)|(1): E(10.0/8.0)
							* C-class!=(4)|(3)|(2)|(1)
					* LargestSpotSize=(H): D(7.0/4.0)
					* LargestSpotSize!=(H): D(19.0/25.0)
		* SpotDistribution!=(C)|(I)|(O): H(298.0/0.0)


