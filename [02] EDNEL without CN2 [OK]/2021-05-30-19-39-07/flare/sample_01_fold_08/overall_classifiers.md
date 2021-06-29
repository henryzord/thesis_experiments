# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = X | H | 0.311390 |
| SpotDistribution != X and LargestSpotSize = X | B | 0.134937 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution = O and LargestSpotSize != H and LargestSpotSize != A | C | 0.110895 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution != O and SpotDistribution = I | D | 0.072889 |
| SpotDistribution = O and LargestSpotSize!=(X) and SpotDistribution != I and LargestSpotSize != X and Activity!=(2) and C-class = 0 | D | 0.045842 |
| SpotDistribution = O and LargestSpotSize!=(X) and SpotDistribution != I and LargestSpotSize != X and Activity!=(2) and C-class != 8 | E | 0.004631 |
| SpotDistribution = O and LargestSpotSize!=(X) and SpotDistribution != I and LargestSpotSize != X and Activity!=(2) and C-class = 1 | D | 0.009636 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution = O and LargestSpotSize != H and LargestSpotSize = A and C-class = 0 and Evolution = 2 | C | 0.005565 |
| SpotDistribution != X and LargestSpotSize != X and Area != 1 and Prev24Hour != 1 | E | 0.007964 |
| SpotDistribution != X and LargestSpotSize != X and Area != 1 and Prev24Hour = 1 | F | 0.006387 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution != O and SpotDistribution != I | E | 0.005792 |
| LargestSpotSize = K and SpotDistribution = C and HistComplex = 2 and Area = 2 | E | 0.007602 |
| LargestSpotSize = K and SpotDistribution = I and HistComplex = 2 and Area = 2 | E | 0.000918 |
| LargestSpotSize = H and SpotDistribution = O and HistComplex = 1 and Area = 1 | C | 0.001304 |
| LargestSpotSize = A and SpotDistribution = C and HistComplex = 1 and Area = 1 | D | 0.000674 |
| LargestSpotSize = A and SpotDistribution = O and HistComplex = 2 and Area = 1 | D | 0.007046 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = X | H | 0.311390 |
| LargestSpotSize = X | B | 0.196049 |
| SpotDistribution = O and C-class = 0 and HistComplex = 1 | C | 0.186047 |
| Area = 2 and SpotDistribution = C | E | 0.018546 |
| SpotDistribution = O and C-class = 0 and Evolution = 2 | C | 0.030904 |
| SpotDistribution = O | D | 0.320900 |
| HistComplex = 2 and Area = 1 and C-class = 0 and SpotDistribution = I | D | 0.126263 |
| HistComplex = 2 and Area = 1 | D | 0.066060 |
| HistComplex = 1 | D | 0.104345 |
|  | F | 0.230769 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Area = 2 and Prev24Hour = 1 | F | 0.006387 |
| SpotDistribution = I and Evolution = 2 and Activity = 2 and LargestSpotSize = A | F | 0.002978 |
| Activity = 2 and SpotDistribution = C | E | 0.012401 |
| LargestSpotSize = A and HistComplex = 2 and Activity = 2 | E | 0.007197 |
| LargestSpotSize = X | B | 0.141758 |
| SpotDistribution = O and LargestSpotSize = R | C | 0.080423 |
| SpotDistribution = O and C-class = 0 and LargestSpotSize = S | C | 0.058336 |
| SpotDistribution = I | D | 0.129550 |
| SpotDistribution = O and Evolution = 3 | D | 0.103122 |
|  | H | 0.622129 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

largestspotsize|spotdistribution|histcomplex|area|class
---|---|---|---|---
a|c|2|2|h
k|c|2|2|e
k|i|2|2|e
a|i|2|2|f
r|o|2|2|h
h|c|2|1|h
k|c|2|1|e
a|c|2|1|e
r|c|2|1|h
x|i|2|1|b
r|i|2|1|d
k|i|2|1|d
s|i|2|1|d
h|i|2|1|d
a|i|2|1|d
r|c|1|1|e
a|c|1|1|d
x|o|2|1|b
h|o|2|1|d
r|o|2|1|c
s|o|2|1|d
a|o|2|1|d
h|x|2|1|h
x|i|1|1|b
a|i|1|1|d
r|i|1|1|d
r|x|2|1|h
a|x|2|1|h
s|x|2|1|h
s|i|1|1|d
x|o|1|1|b
h|o|1|1|c
a|o|1|1|d
s|o|1|1|c
r|o|1|1|c
k|o|1|1|h
k|x|1|1|h
a|x|1|1|h
h|x|1|1|h
r|x|1|1|h
s|x|1|1|h

## JRip

Decision list:

rules | predicted class
---|---
(Area = 2) and (Prev24Hour = 1)|F (17.0/7.0)
(SpotDistribution = I) and (Evolution = 2) and (Activity = 2) and (LargestSpotSize = A)|F (18.0/11.0)
(Activity = 2) and (SpotDistribution = C)|E (18.0/5.0)
(LargestSpotSize = A) and (HistComplex = 2) and (Activity = 2)|E (20.0/9.0)
(LargestSpotSize = X)|B (129.0/0.0)
(SpotDistribution = O) and (LargestSpotSize = R)|C (113.0/37.0)
(SpotDistribution = O) and (C-class = 0) and (LargestSpotSize = S)|C (101.0/41.0)
(SpotDistribution = I)|D (146.0/58.0)
(SpotDistribution = O) and (Evolution = 3)|D (49.0/22.0)
|H (346.0/48.0)


## PART

Decision list:

rules | predicted class
---|---
SpotDistribution = X|H (298.0)
LargestSpotSize = X|B (129.0)
SpotDistribution = O AND C-class = 0 AND HistComplex = 1|C (172.0/60.0)
Area = 2 AND SpotDistribution = C|E (16.0/6.0)
SpotDistribution = O AND C-class = 0 AND Evolution = 2|C (48.0/23.0)
SpotDistribution = O|D (95.0/53.0)
HistComplex = 2 AND Area = 1 AND C-class = 0 AND SpotDistribution = I|D (72.0/32.0)
HistComplex = 2 AND Area = 1|D (64.0/36.0)
HistComplex = 1|D (56.0/19.0)
|F (7.0/2.0)


## J48 Decision Tree

* SpotDistribution = X: H (298.0)
* SpotDistribution != X
	* LargestSpotSize = X: B (129.0)
	* LargestSpotSize != X
		* Area = 1
			* SpotDistribution = O
				* LargestSpotSize = H: D (14.0/8.0)
				* LargestSpotSize != H
					* LargestSpotSize = A
						* C-class = 0
							* Evolution = 2: C (19.0/10.0)
							* Evolution != 2: D (28.0/13.0)
						* C-class != 0: E (13.0/6.0)
					* LargestSpotSize != A: C (240.0/92.0)
			* SpotDistribution != O
				* SpotDistribution = I: D (176.0/77.0)
				* SpotDistribution != I: E (16.0/7.0)
		* Area != 1
			* Prev24Hour = 1: F (17.0/7.0)
			* Prev24Hour != 1: E (7.0)


## SimpleCart Decision Tree

		* SpotDistribution=(C)|(I)|(O)
	* LargestSpotSize=(X): B(129.0/0.0)
	* LargestSpotSize!=(X)
			* SpotDistribution=(C)|(I)
			* Area=(2)
					* Prev24Hour=(3)|(2): E(7.0/0.0)
					* Prev24Hour!=(3)|(2): F(10.0/6.0)
			* Area!=(2): D(105.0/87.0)
			* SpotDistribution!=(C)|(I)
					* LargestSpotSize=(S)|(R)|(X): C(147.0/93.0)
					* LargestSpotSize!=(S)|(R)|(X)
				* Activity=(2)
					* HistComplex=(2): E(8.0/3.0)
					* HistComplex!=(2): D(3.0/0.0)
				* Activity!=(2)
										* C-class=(0)|(1)|(5)|(6)|(7)|(8): D(27.0/30.0)
										* C-class!=(0)|(1)|(5)|(6)|(7)|(8): E(3.0/1.0)
		* SpotDistribution!=(C)|(I)|(O): H(298.0/0.0)


