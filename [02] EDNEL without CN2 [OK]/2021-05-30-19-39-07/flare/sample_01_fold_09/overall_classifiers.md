# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | H | 0.311390 |
| LargestSpotSize = X and SpotDistribution = O and X-class = 0 | B | 0.121148 |
| SpotDistribution = O and LargestSpotSize!=(X) and SpotDistribution != I and LargestSpotSize != X and C-class != 1 and Activity!=(2) and LargestSpotSize!=(H) | D | 0.046793 |
| LargestSpotSize = R and SpotDistribution = O and X-class = 0 | C | 0.062873 |
| LargestSpotSize = S and SpotDistribution = O and X-class = 0 | C | 0.054980 |
| LargestSpotSize = A and SpotDistribution = I and X-class = 0 | D | 0.043096 |
| LargestSpotSize = X and SpotDistribution = I and X-class = 0 | B | 0.017815 |
| LargestSpotSize = R and SpotDistribution = I and X-class = 0 | D | 0.012533 |
| LargestSpotSize = S and SpotDistribution = I and X-class = 0 | D | 0.010722 |
| LargestSpotSize = K and SpotDistribution = C and X-class = 0 | E | 0.006088 |
| LargestSpotSize = K and SpotDistribution = I and X-class = 0 | D | 0.009204 |
| SpotDistribution = O and LargestSpotSize!=(X) and SpotDistribution != I and LargestSpotSize != X and C-class = 4 | E | 0.002288 |
| LargestSpotSize = H and SpotDistribution = I and X-class = 0 | E | 0.001527 |
| LargestSpotSize = K and SpotDistribution = C and X-class = 1 | E | 0.001527 |
| SpotDistribution = O and LargestSpotSize!=(X) and SpotDistribution != I and LargestSpotSize != X and C-class = 1 | E | 0.000892 |
| LargestSpotSize = A and SpotDistribution = C and X-class = 0 | D | 0.001968 |
| SpotDistribution = O and LargestSpotSize!=(X) and SpotDistribution != I and LargestSpotSize != X and C-class = 3 | E | 0.000192 |
| LargestSpotSize = R and SpotDistribution = C and X-class = 0 | D | 0.001795 |
| LargestSpotSize = A and SpotDistribution = O and X-class = 0 | D | 0.014013 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = X | H | 0.311390 |
| LargestSpotSize = X | B | 0.196049 |
| SpotDistribution = C and Area = 2 and Prev24Hour = 1 | F | 0.006339 |
| SpotDistribution = C and Area = 1 and Evolution = 3 | D | 0.006452 |
| SpotDistribution = C and LargestSpotSize = K | E | 0.018769 |
| SpotDistribution = O and LargestSpotSize = R and HistComplex = 1 and C-class = 0 and Evolution = 3 | C | 0.065967 |
| SpotDistribution = O and LargestSpotSize = R and HistComplex = 1 and C-class = 0 | C | 0.040498 |
| SpotDistribution = O and LargestSpotSize = R and C-class = 0 | C | 0.007804 |
| SpotDistribution = O and LargestSpotSize = S and C-class = 1 and HistComplex = 1 | C | 0.008627 |
| SpotDistribution = O and LargestSpotSize = R | C | 0.002103 |
| SpotDistribution = O and LargestSpotSize = S and C-class = 0 and HistComplex = 1 and Activity = 2 and Evolution = 2 | C | 0.018731 |
| SpotDistribution = O and LargestSpotSize = S and C-class = 0 and Evolution = 3 and HistComplex = 1 and Activity = 1 | C | 0.037722 |
| SpotDistribution = O and LargestSpotSize = S and C-class = 0 and HistComplex = 1 and Evolution = 2 | C | 0.029787 |
| SpotDistribution = O and C-class = 0 and LargestSpotSize = A and Activity = 1 and Evolution = 3 and HistComplex = 2 | D | 0.012697 |
| SpotDistribution = O and LargestSpotSize = S and C-class = 0 and HistComplex = 2 and Evolution = 2 | C | 0.023034 |
| HistComplex = 1 and C-class = 1 and LargestSpotSize = A | D | 0.018824 |
| HistComplex = 1 and C-class = 0 and LargestSpotSize = A and SpotDistribution = I and Evolution = 3 | D | 0.056968 |
| HistComplex = 1 and C-class = 0 and Evolution = 2 and SpotDistribution = I | D | 0.021008 |
| HistComplex = 1 and C-class = 0 and Evolution = 3 and LargestSpotSize = S and SpotDistribution = I | D | 0.028959 |
| HistComplex = 1 and C-class = 0 and LargestSpotSize = A and Evolution = 3 | D | 0.026203 |
| HistComplex = 1 and C-class = 1 | C | 0.006039 |
| HistComplex = 1 and C-class = 0 and Activity = 1 and Evolution = 2 | D | 0.043373 |
| HistComplex = 1 and C-class = 0 and Activity = 1 | D | 0.110250 |
| SpotDistribution = I and Evolution = 3 and LargestSpotSize = K and Activity = 2 | D | 0.025100 |
| SpotDistribution = I and LargestSpotSize = R and Evolution = 3 | D | 0.034839 |
| SpotDistribution = I and Area = 1 and Evolution = 3 and LargestSpotSize = A and C-class = 0 | D | 0.045383 |
| SpotDistribution = O and LargestSpotSize = A and C-class = 0 and Activity = 1 | C | 0.046488 |
| HistComplex = 1 and LargestSpotSize = S and Activity = 1 | D | 0.023936 |
| HistComplex = 1 and LargestSpotSize = A | E | 0.018713 |
| HistComplex = 1 | C | 0.046518 |
| SpotDistribution = O and LargestSpotSize = A and C-class = 1 | E | 0.017897 |
| SpotDistribution = O and LargestSpotSize = S and C-class = 0 and Evolution = 3 | D | 0.023271 |
| Area = 1 and C-class = 3 and Evolution = 2 | E | 0.012676 |
| Area = 1 and C-class = 0 and Prev24Hour = 1 and LargestSpotSize = H | D | 0.037121 |
| Area = 1 and LargestSpotSize = K and Evolution = 2 | D | 0.009783 |
| Area = 1 and LargestSpotSize = R | D | 0.065041 |
| Area = 1 and LargestSpotSize = A and Evolution = 3 and Activity = 2 and Prev24Hour = 1 | E | 0.016807 |
| Area = 1 and C-class = 2 and Evolution = 2 | F | 0.008991 |
| Area = 1 and LargestSpotSize = A and C-class = 1 and Activity = 2 | D | 0.011796 |
| Area = 1 and C-class = 1 and LargestSpotSize = A | D | 0.027273 |
| Area = 1 and C-class = 1 and SpotDistribution = O and Activity = 1 | D | 0.007339 |
| Area = 1 and LargestSpotSize = A and Evolution = 2 and Prev24Hour = 1 and SpotDistribution = I and Activity = 1 | D | 0.030189 |
| Area = 1 and LargestSpotSize = A and Evolution = 2 and SpotDistribution = I | D | 0.007092 |
| Area = 1 and LargestSpotSize = A and Evolution = 2 and SpotDistribution = O | E | 0.037895 |
| Area = 1 and LargestSpotSize = A and Evolution = 3 | D | 0.033351 |
| Area = 1 and LargestSpotSize = A | E | 0.119512 |
| Area = 1 and LargestSpotSize = S and C-class = 0 and Evolution = 3 | D | 0.014035 |
| Area = 1 and LargestSpotSize = S and C-class = 0 and Activity = 1 and SpotDistribution = O | D | 0.051282 |
| Area = 1 and LargestSpotSize = S and C-class = 0 and Activity = 1 | E | 0.077465 |
| Area = 1 and LargestSpotSize = S and C-class = 0 | E | 0.019841 |
| Area = 1 and LargestSpotSize = S and SpotDistribution = O | D | 0.014545 |
| LargestSpotSize = K | D | 0.026882 |
| LargestSpotSize = S | F | 0.041958 |
|  | E | 0.222222 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Area = 2 and Prev24Hour = 1 | F | 0.005863 |
| Activity = 2 and SpotDistribution = C | E | 0.010728 |
| HistComplex = 2 and LargestSpotSize = A and Activity = 2 and SpotDistribution = O and Prev24Hour = 1 | E | 0.005760 |
| LargestSpotSize = X | B | 0.139009 |
| SpotDistribution = O and HistComplex = 1 | C | 0.120059 |
| SpotDistribution = O and C-class = 0 and Evolution = 2 | C | 0.018984 |
| SpotDistribution = I and Evolution = 3 | D | 0.098768 |
|  | H | 0.514680 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

largestspotsize|spotdistribution|x-class|class
---|---|---|---
k|c|2|h
k|c|1|e
a|i|1|h
h|c|0|h
r|c|0|d
k|c|0|e
a|c|0|d
h|i|0|e
x|i|0|b
a|i|0|d
k|i|0|d
s|i|0|d
r|i|0|d
k|o|0|h
x|o|0|b
h|o|0|d
a|o|0|d
s|o|0|c
r|o|0|c
k|x|0|h
r|x|0|h
h|x|0|h
a|x|0|h
s|x|0|h

## JRip

Decision list:

rules | predicted class
---|---
(Area = 2) and (Prev24Hour = 1)|F (15.0/6.0)
(Activity = 2) and (SpotDistribution = C)|E (19.0/6.0)
(HistComplex = 2) and (LargestSpotSize = A) and (Activity = 2) and (SpotDistribution = O) and (Prev24Hour = 1)|E (5.0/0.0)
(LargestSpotSize = X)|B (129.0/0.0)
(SpotDistribution = O) and (HistComplex = 1)|C (196.0/71.0)
(SpotDistribution = O) and (C-class = 0) and (Evolution = 2)|C (47.0/20.0)
(SpotDistribution = I) and (Evolution = 3)|D (101.0/32.0)
|H (445.0/147.0)


## PART

Decision list:

rules | predicted class
---|---
SpotDistribution = X|H (298.0)
LargestSpotSize = X|B (129.0)
SpotDistribution = C AND Area = 2 AND Prev24Hour = 1|F (8.0/3.0)
SpotDistribution = C AND Area = 1 AND Evolution = 3|D (8.0/4.0)
SpotDistribution = C AND LargestSpotSize = K|E (9.0/1.0)
SpotDistribution = O AND LargestSpotSize = R AND HistComplex = 1 AND C-class = 0 AND Evolution = 3|C (52.0/18.0)
SpotDistribution = O AND LargestSpotSize = R AND HistComplex = 1 AND C-class = 0|C (34.0/8.0)
SpotDistribution = O AND LargestSpotSize = R AND C-class = 0|C (17.0/7.0)
SpotDistribution = O AND LargestSpotSize = S AND C-class = 1 AND HistComplex = 1|C (9.0/4.0)
SpotDistribution = O AND LargestSpotSize = R|C (8.0/3.0)
SpotDistribution = O AND LargestSpotSize = S AND C-class = 0 AND HistComplex = 1 AND Activity = 2 AND Evolution = 2|C (8.0/1.0)
SpotDistribution = O AND LargestSpotSize = S AND C-class = 0 AND Evolution = 3 AND HistComplex = 1 AND Activity = 1|C (29.0/10.0)
SpotDistribution = O AND LargestSpotSize = S AND C-class = 0 AND HistComplex = 1 AND Evolution = 2|C (19.0/5.0)
SpotDistribution = O AND C-class = 0 AND LargestSpotSize = A AND Activity = 1 AND Evolution = 3 AND HistComplex = 2|D (11.0/6.0)
SpotDistribution = O AND LargestSpotSize = S AND C-class = 0 AND HistComplex = 2 AND Evolution = 2|C (23.0/10.0)
HistComplex = 1 AND C-class = 1 AND LargestSpotSize = A|D (5.0/1.0)
HistComplex = 1 AND C-class = 0 AND LargestSpotSize = A AND SpotDistribution = I AND Evolution = 3|D (12.0/1.0)
HistComplex = 1 AND C-class = 0 AND Evolution = 2 AND SpotDistribution = I|D (7.0/2.0)
HistComplex = 1 AND C-class = 0 AND Evolution = 3 AND LargestSpotSize = S AND SpotDistribution = I|D (13.0/5.0)
HistComplex = 1 AND C-class = 0 AND LargestSpotSize = A AND Evolution = 3|D (10.0/3.0)
HistComplex = 1 AND C-class = 1|C (7.0/3.0)
HistComplex = 1 AND C-class = 0 AND Activity = 1 AND Evolution = 2|D (6.0/3.0)
HistComplex = 1 AND C-class = 0 AND Activity = 1|D (8.0/4.0)
SpotDistribution = I AND Evolution = 3 AND LargestSpotSize = K AND Activity = 2|D (6.0/1.0)
SpotDistribution = I AND LargestSpotSize = R AND Evolution = 3|D (9.0/2.0)
SpotDistribution = I AND Area = 1 AND Evolution = 3 AND LargestSpotSize = A AND C-class = 0|D (18.0/6.0)
SpotDistribution = O AND LargestSpotSize = A AND C-class = 0 AND Activity = 1|C (10.0/5.0)
HistComplex = 1 AND LargestSpotSize = S AND Activity = 1|D (7.0/4.0)
HistComplex = 1 AND LargestSpotSize = A|E (5.0/2.0)
HistComplex = 1|C (7.0/1.0)
SpotDistribution = O AND LargestSpotSize = A AND C-class = 1|E (6.0/2.0)
SpotDistribution = O AND LargestSpotSize = S AND C-class = 0 AND Evolution = 3|D (11.0/5.0)
Area = 1 AND C-class = 3 AND Evolution = 2|E (5.0/2.0)
Area = 1 AND C-class = 0 AND Prev24Hour = 1 AND LargestSpotSize = H|D (9.0/2.0)
Area = 1 AND LargestSpotSize = K AND Evolution = 2|D (8.0/5.0)
Area = 1 AND LargestSpotSize = R|D (7.0/3.0)
Area = 1 AND LargestSpotSize = A AND Evolution = 3 AND Activity = 2 AND Prev24Hour = 1|E (5.0/1.0)
Area = 1 AND C-class = 2 AND Evolution = 2|F (5.0/2.0)
Area = 1 AND LargestSpotSize = A AND C-class = 1 AND Activity = 2|D (7.0/4.0)
Area = 1 AND C-class = 1 AND LargestSpotSize = A|D (6.0/2.0)
Area = 1 AND C-class = 1 AND SpotDistribution = O AND Activity = 1|D (5.0/3.0)
Area = 1 AND LargestSpotSize = A AND Evolution = 2 AND Prev24Hour = 1 AND SpotDistribution = I AND Activity = 1|D (18.0/10.0)
Area = 1 AND LargestSpotSize = A AND Evolution = 2 AND SpotDistribution = I|D (8.0/5.0)
Area = 1 AND LargestSpotSize = A AND Evolution = 2 AND SpotDistribution = O|E (6.0/2.0)
Area = 1 AND LargestSpotSize = A AND Evolution = 3|D (6.0/1.0)
Area = 1 AND LargestSpotSize = A|E (7.0/3.0)
Area = 1 AND LargestSpotSize = S AND C-class = 0 AND Evolution = 3|D (7.0/3.0)
Area = 1 AND LargestSpotSize = S AND C-class = 0 AND Activity = 1 AND SpotDistribution = O|D (7.0/4.0)
Area = 1 AND LargestSpotSize = S AND C-class = 0 AND Activity = 1|E (5.0/2.0)
Area = 1 AND LargestSpotSize = S AND C-class = 0|E (5.0/3.0)
Area = 1 AND LargestSpotSize = S AND SpotDistribution = O|D (5.0/3.0)
LargestSpotSize = K|D (7.0/3.0)
LargestSpotSize = S|F (4.0/2.0)
|E (6.0/2.0)


## SimpleCart Decision Tree

		* SpotDistribution=(C)|(I)|(O)
	* LargestSpotSize=(X): B(129.0/0.0)
	* LargestSpotSize!=(X)
			* SpotDistribution=(C)|(I)
			* Area=(2)
					* Prev24Hour=(3)|(2): E(7.0/1.0)
					* Prev24Hour!=(3)|(2): F(9.0/5.0)
			* Area!=(2)
				* Evolution=(3): D(73.0/36.0)
				* Evolution!=(3): D(35.0/51.0)
			* SpotDistribution!=(C)|(I)
						* LargestSpotSize=(K)|(S)|(R)|(X)
				* HistComplex=(2): C(34.0/35.0)
				* HistComplex!=(2)
							* C-class=(6)|(2)|(1): D(9.0/10.0)
							* C-class!=(6)|(2)|(1)
						* Activity=(2): C(13.0/2.0)
						* Activity!=(2)
							* Evolution=(2)
								* LargestSpotSize=(S): C(15.0/6.0)
								* LargestSpotSize!=(S): C(23.0/7.0)
							* Evolution!=(2): C(58.0/30.0)
						* LargestSpotSize!=(K)|(S)|(R)|(X)
						* C-class=(4)|(3)|(1): E(8.0/6.0)
						* C-class!=(4)|(3)|(1)
					* Activity=(2): D(5.0/5.0)
					* Activity!=(2)
						* LargestSpotSize=(H): D(7.0/4.0)
						* LargestSpotSize!=(H): D(16.0/20.0)
		* SpotDistribution!=(C)|(I)|(O): H(298.0/0.0)


