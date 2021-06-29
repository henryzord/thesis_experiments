# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | H | 0.310417 |
| LargestSpotSize = X and SpotDistribution = O and HistComplex = 1 and Area = 1 and X-class = 0 | B | 0.108836 |
| SpotDistribution = O and LargestSpotSize!=(X) and SpotDistribution != I and LargestSpotSize != X and C-class != 1 and Activity!=(2) and LargestSpotSize!=(H) | D | 0.046577 |
| LargestSpotSize = R and SpotDistribution = O and HistComplex = 1 and Area = 1 and X-class = 0 | C | 0.054712 |
| LargestSpotSize = S and SpotDistribution = O and HistComplex = 1 and Area = 1 and X-class = 0 | C | 0.043054 |
| LargestSpotSize = A and SpotDistribution = I and HistComplex = 2 and Area = 1 and X-class = 0 | D | 0.024469 |
| LargestSpotSize = A and SpotDistribution = I and HistComplex = 1 and Area = 1 and X-class = 0 | D | 0.022823 |
| LargestSpotSize = X and SpotDistribution = O and HistComplex = 2 and Area = 1 and X-class = 0 | B | 0.018980 |
| LargestSpotSize = R and SpotDistribution = O and HistComplex = 2 and Area = 1 and X-class = 0 | C | 0.009184 |
| LargestSpotSize = K and SpotDistribution = I and HistComplex = 2 and Area = 1 and X-class = 0 | D | 0.011264 |
| LargestSpotSize = X and SpotDistribution = I and HistComplex = 1 and Area = 1 and X-class = 0 | B | 0.011947 |
| LargestSpotSize = R and SpotDistribution = I and HistComplex = 2 and Area = 1 and X-class = 0 | D | 0.009511 |
| LargestSpotSize = K and SpotDistribution = C and HistComplex = 2 and Area = 2 and X-class = 0 | E | 0.005074 |
| LargestSpotSize = S and SpotDistribution = I and HistComplex = 1 and Area = 1 and X-class = 0 | D | 0.007437 |
| LargestSpotSize = S and SpotDistribution = I and HistComplex = 2 and Area = 1 and X-class = 0 | E | 0.004048 |
| LargestSpotSize = X and SpotDistribution = I and HistComplex = 2 and Area = 1 and X-class = 0 | B | 0.006010 |
| LargestSpotSize = R and SpotDistribution = I and HistComplex = 1 and Area = 1 and X-class = 0 | C | 0.003247 |
| LargestSpotSize = A and SpotDistribution = C and HistComplex = 2 and Area = 1 and X-class = 0 | E | 0.002286 |
| SpotDistribution = O and LargestSpotSize!=(X) and SpotDistribution != I and LargestSpotSize != X and C-class = 4 | E | 0.002281 |
| LargestSpotSize = A and SpotDistribution = I and HistComplex = 2 and Area = 2 and X-class = 0 | F | 0.002167 |
| LargestSpotSize = K and SpotDistribution = C and HistComplex = 2 and Area = 2 and X-class = 1 | E | 0.001522 |
| LargestSpotSize = H and SpotDistribution = O and HistComplex = 1 and Area = 1 and X-class = 0 | C | 0.001299 |
| SpotDistribution = O and LargestSpotSize!=(X) and SpotDistribution != I and LargestSpotSize != X and C-class = 1 | E | 0.000889 |
| SpotDistribution = O and LargestSpotSize!=(X) and SpotDistribution != I and LargestSpotSize != X and C-class = 3 | E | 0.000191 |
| LargestSpotSize = K and SpotDistribution = I and HistComplex = 2 and Area = 2 and X-class = 0 | F | 0.001086 |
| LargestSpotSize = S and SpotDistribution = O and HistComplex = 2 and Area = 1 and X-class = 0 | D | 0.012859 |
| LargestSpotSize = R and SpotDistribution = C and HistComplex = 1 and Area = 1 and X-class = 0 | E | 0.000571 |
| LargestSpotSize = A and SpotDistribution = C and HistComplex = 1 and Area = 1 and X-class = 0 | D | 0.000671 |
| LargestSpotSize = H and SpotDistribution = I and HistComplex = 2 and Area = 1 and X-class = 0 | D | 0.000448 |
| LargestSpotSize = A and SpotDistribution = O and HistComplex = 2 and Area = 1 and X-class = 0 | D | 0.006223 |
| LargestSpotSize = A and SpotDistribution = O and HistComplex = 1 and Area = 1 and X-class = 0 | D | 0.008514 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = X | H | 0.310417 |
| LargestSpotSize = X | B | 0.199697 |
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
| Area = 2 and Prev24Hour = 1 | F | 0.005844 |
| Activity = 2 and SpotDistribution = C | E | 0.010691 |
| HistComplex = 2 and LargestSpotSize = A and Activity = 2 and Prev24Hour = 1 and SpotDistribution = O | E | 0.005741 |
| LargestSpotSize = X | B | 0.141783 |
| SpotDistribution = O and HistComplex = 1 | C | 0.120059 |
| SpotDistribution = O and C-class = 0 and Evolution = 2 | C | 0.018984 |
| SpotDistribution = I and Evolution = 3 | D | 0.098768 |
| SpotDistribution = O and Evolution = 3 | D | 0.098511 |
| SpotDistribution = I and C-class = 0 | D | 0.020510 |
|  | H | 0.605691 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

largestspotsize|spotdistribution|histcomplex|area|x-class|class
---|---|---|---|---|---
k|c|2|2|2|h
k|c|2|2|1|e
a|c|2|2|0|h
a|i|2|1|1|h
k|c|2|2|0|e
k|i|2|2|0|f
a|i|2|2|0|f
r|o|2|2|0|h
r|c|2|1|0|h
h|c|2|1|0|h
k|c|2|1|0|h
a|c|2|1|0|e
k|i|2|1|0|d
h|i|2|1|0|d
r|i|2|1|0|d
a|i|2|1|0|d
s|i|2|1|0|e
x|i|2|1|0|b
r|c|1|1|0|e
a|c|1|1|0|d
s|o|2|1|0|d
a|o|2|1|0|d
r|o|2|1|0|c
h|o|2|1|0|d
x|o|2|1|0|b
h|x|2|1|0|h
r|x|2|1|0|h
s|i|1|1|0|d
a|i|1|1|0|d
r|i|1|1|0|c
a|x|2|1|0|h
s|x|2|1|0|h
x|i|1|1|0|b
k|o|1|1|0|h
h|o|1|1|0|c
a|o|1|1|0|d
s|o|1|1|0|c
r|o|1|1|0|c
x|o|1|1|0|b
k|x|1|1|0|h
r|x|1|1|0|h
a|x|1|1|0|h
h|x|1|1|0|h
s|x|1|1|0|h

## JRip

Decision list:

rules | predicted class
---|---
(Area = 2) and (Prev24Hour = 1)|F (15.0/6.0)
(Activity = 2) and (SpotDistribution = C)|E (19.0/6.0)
(HistComplex = 2) and (LargestSpotSize = A) and (Activity = 2) and (Prev24Hour = 1) and (SpotDistribution = O)|E (5.0/0.0)
(LargestSpotSize = X)|B (132.0/0.0)
(SpotDistribution = O) and (HistComplex = 1)|C (196.0/71.0)
(SpotDistribution = O) and (C-class = 0) and (Evolution = 2)|C (47.0/20.0)
(SpotDistribution = I) and (Evolution = 3)|D (101.0/32.0)
(SpotDistribution = O) and (Evolution = 3)|D (36.0/16.0)
(SpotDistribution = I) and (C-class = 0)|D (50.0/26.0)
|H (359.0/61.0)


## PART

Decision list:

rules | predicted class
---|---
SpotDistribution = X|H (298.0)
LargestSpotSize = X|B (132.0)
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


## SimpleCart Decision Tree

		* SpotDistribution=(C)|(I)|(O)
	* LargestSpotSize=(X): B(132.0/0.0)
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


