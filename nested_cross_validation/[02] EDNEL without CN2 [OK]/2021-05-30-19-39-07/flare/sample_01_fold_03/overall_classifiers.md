# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution != C | H | 0.291491 |
| LargestSpotSize = X and SpotDistribution = O and BecomeHist = 2 and Area = 1 and X-class = 0 | B | 0.123941 |
| LargestSpotSize = R and SpotDistribution = O and BecomeHist = 2 and Area = 1 and X-class = 0 | C | 0.064401 |
| LargestSpotSize = A and SpotDistribution = I and BecomeHist = 2 and Area = 1 and X-class = 0 | D | 0.041305 |
| LargestSpotSize = S and SpotDistribution = O and BecomeHist = 2 and Area = 1 and X-class = 0 | C | 0.054630 |
| LargestSpotSize = A and SpotDistribution = O and BecomeHist = 2 and Area = 1 and X-class = 0 | D | 0.015419 |
| LargestSpotSize = S and SpotDistribution = I and BecomeHist = 2 and Area = 1 and X-class = 0 | D | 0.012459 |
| LargestSpotSize = K and SpotDistribution = I and BecomeHist = 2 and Area = 1 and X-class = 0 | D | 0.012519 |
| SpotDistribution = O and LargestSpotSize!=(X) and SpotDistribution != I and LargestSpotSize != X and C-class != 5 | E | 0.004348 |
| LargestSpotSize = R and SpotDistribution = I and BecomeHist = 2 and Area = 1 and X-class = 0 | D | 0.012048 |
| LargestSpotSize = X and SpotDistribution = I and BecomeHist = 2 and Area = 1 and X-class = 0 | B | 0.013126 |
| LargestSpotSize = K and SpotDistribution = C and BecomeHist = 2 and Area = 2 and X-class = 0 | E | 0.006634 |
| LargestSpotSize = H and SpotDistribution = O and BecomeHist = 2 and Area = 1 and X-class = 0 | D | 0.004139 |
| LargestSpotSize = A and SpotDistribution = C and BecomeHist = 2 and Area = 1 and X-class = 0 | E | 0.003182 |
| LargestSpotSize = A and SpotDistribution = I and BecomeHist = 2 and Area = 2 and X-class = 0 | F | 0.002174 |
| LargestSpotSize = K and SpotDistribution = I and BecomeHist = 2 and Area = 2 and X-class = 0 | E | 0.002062 |
| LargestSpotSize = R and SpotDistribution = C and BecomeHist = 2 and Area = 1 and X-class = 0 | D | 0.001795 |
| LargestSpotSize = K and SpotDistribution = C and BecomeHist = 2 and Area = 1 and X-class = 0 | E | 0.001527 |
| LargestSpotSize = K and SpotDistribution = C and BecomeHist = 2 and Area = 2 and X-class = 1 | E | 0.001527 |
| LargestSpotSize = H and SpotDistribution = I and BecomeHist = 2 and Area = 1 and X-class = 0 | D | 0.000674 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = X | H | 0.311390 |
| LargestSpotSize = X | B | 0.194825 |
| SpotDistribution = O and LargestSpotSize = S | C | 0.119275 |
| HistComplex = 1 and SpotDistribution = O | C | 0.109564 |
| Area = 1 and SpotDistribution = I and HistComplex = 1 and LargestSpotSize = A | D | 0.091575 |
| Area = 2 | E | 0.029167 |
| SpotDistribution = I and HistComplex = 1 and Activity = 1 and Evolution = 3 | D | 0.047405 |
| SpotDistribution = I and HistComplex = 2 and Evolution = 3 | D | 0.134638 |
| Activity = 1 and LargestSpotSize = A | D | 0.094613 |
| Activity = 2 | D | 0.093644 |
| LargestSpotSize = R | C | 0.038536 |
|  | D | 0.380282 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

largestspotsize|spotdistribution|becomehist|area|x-class|class
---|---|---|---|---|---
k|c|2|2|2|h
k|c|2|2|1|e
a|i|2|1|1|h
a|c|2|2|0|h
k|c|2|2|0|e
a|i|2|2|0|f
k|i|2|2|0|e
r|o|2|2|0|h
k|c|2|1|0|e
r|c|2|1|0|d
a|c|2|1|0|e
x|i|2|1|0|b
h|i|2|1|0|d
k|i|2|1|0|d
r|i|2|1|0|d
a|i|2|1|0|d
s|i|2|1|0|d
k|o|2|1|0|h
x|o|2|1|0|b
h|o|2|1|0|d
a|o|2|1|0|d
s|o|2|1|0|c
r|o|2|1|0|c
r|x|2|1|0|h
a|x|2|1|0|h
s|x|2|1|0|h
h|x|2|1|0|h
k|x|1|1|0|h
r|x|1|1|0|h
h|x|1|1|0|h
s|x|1|1|0|h
a|x|1|1|0|h

## PART

Decision list:

rules | predicted class
---|---
SpotDistribution = X|H (269.0)
LargestSpotSize = X|B (116.0)
SpotDistribution = O AND LargestSpotSize = S|C (117.0/51.0)
HistComplex = 1 AND SpotDistribution = O|C (110.0/41.0)
Area = 1 AND SpotDistribution = I AND HistComplex = 1 AND LargestSpotSize = A|D (23.0/4.0)
Area = 2|E (23.0/9.0)
SpotDistribution = I AND HistComplex = 1 AND Activity = 1 AND Evolution = 3|D (17.0/8.0)
SpotDistribution = I AND HistComplex = 2 AND Evolution = 3|D (54.0/20.0)
Activity = 1 AND LargestSpotSize = A|D (52.0/33.0)
Activity = 2|D (47.0/27.0)
LargestSpotSize = R|C (21.0/8.0)
|D (13.0/7.0)


## SimpleCart Decision Tree

		* SpotDistribution=(C)|(I)|(O)
	* LargestSpotSize=(X): B(128.0/0.0)
	* LargestSpotSize!=(X)
			* SpotDistribution=(C)|(I)
			* Area=(2)
					* Prev24Hour=(3)|(2)
					* Evolution=(3)
												* C-class=(1)|(2)|(3)|(4)|(5)|(7)|(8): E(1.0/1.0)
												* C-class!=(1)|(2)|(3)|(4)|(5)|(7)|(8): E(2.0/0.0)
					* Evolution!=(3): E(5.0/0.0)
					* Prev24Hour!=(3)|(2): F(8.0/6.0)
			* Area!=(2)
				* Evolution=(3)
									* C-class=(0)|(1)|(2)|(7)|(8)
						* HistComplex=(2)
										* LargestSpotSize=(S)|(R)|(H)|(K)
								* LargestSpotSize=(S)
									* Activity=(2): E(2.0/1.0)
									* Activity!=(2): D(4.0/3.0)
								* LargestSpotSize!=(S): D(14.0/2.0)
										* LargestSpotSize!=(S)|(R)|(H)|(K)
								* M-class=(1): D(2.0/0.0)
								* M-class!=(1): D(13.0/13.0)
						* HistComplex!=(2)
											* LargestSpotSize=(S)|(R)|(X)|(K)|(H): D(16.0/9.0)
											* LargestSpotSize!=(S)|(R)|(X)|(K)|(H)
								* C-class=(2): D(2.0/1.0)
								* C-class!=(2)
									* Activity=(2): D(3.0/0.0)
									* Activity!=(2)
										* C-class=(1): D(2.0/0.0)
										* C-class!=(1)
											* M-class=(1): D(2.0/0.0)
											* M-class!=(1): D(8.0/2.0)
									* C-class!=(0)|(1)|(2)|(7)|(8)
						* LargestSpotSize=(K): D(2.0/0.0)
						* LargestSpotSize!=(K)
									* C-class=(6)|(5)|(4): E(3.0/0.0)
									* C-class!=(6)|(5)|(4): D(3.0/3.0)
				* Evolution!=(3)
							* C-class=(0)|(6)|(7)
						* LargestSpotSize=(R): D(4.0/2.0)
						* LargestSpotSize!=(R)
							* HistComplex=(2)
								* Prev24Hour=(3): D(2.0/2.0)
								* Prev24Hour!=(3)
									* SpotDistribution=(C): E(3.0/1.0)
									* SpotDistribution!=(C)
										* LargestSpotSize=(K): D(2.0/0.0)
										* LargestSpotSize!=(K): D(14.0/20.0)
							* HistComplex!=(2): D(3.0/1.0)
							* C-class!=(0)|(6)|(7)
						* LargestSpotSize=(R): C(2.0/1.0)
						* LargestSpotSize!=(R): F(11.0/15.0)
			* SpotDistribution!=(C)|(I)
					* LargestSpotSize=(S)|(R)|(X)
				* HistComplex=(2): C(32.0/32.0)
				* HistComplex!=(2)
								* C-class=(0)|(4)|(7)|(8)
						* Evolution=(3)
							* Prev24Hour=(3): C(1.0/1.0)
							* Prev24Hour!=(3)
								* LargestSpotSize=(S): C(22.0/11.0)
								* LargestSpotSize!=(S): C(36.0/18.0)
						* Evolution!=(3)
							* LargestSpotSize=(S)
								* Prev24Hour=(2): C(2.0/0.0)
								* Prev24Hour!=(2)
									* Activity=(2): C(5.0/2.0)
									* Activity!=(2)
											* Evolution=(2)|(3): C(15.0/5.0)
											* Evolution!=(2)|(3): D(1.0/1.0)
							* LargestSpotSize!=(S)
								* Activity=(2): C(2.0/0.0)
								* Activity!=(2)
										* Evolution=(2)|(3): C(19.0/6.0)
										* Evolution!=(2)|(3): C(4.0/1.0)
								* C-class!=(0)|(4)|(7)|(8)
							* M-class=(2)|(1): D(3.0/0.0)
							* M-class!=(2)|(1): C(12.0/12.0)
					* LargestSpotSize!=(S)|(R)|(X)
										* C-class=(0)|(1)|(2)|(5)|(6)|(7)|(8)
					* Activity=(2)
						* Evolution=(3): D(4.0/0.0)
						* Evolution!=(3): E(5.0/1.0)
					* Activity!=(2)
						* LargestSpotSize=(H)
							* C-class=(1): C(1.0/1.0)
							* C-class!=(1)
								* HistComplex=(2)
										* Evolution=(3)|(1): D(4.0/2.0)
										* Evolution!=(3)|(1): D(2.0/0.0)
								* HistComplex!=(2): D(1.0/2.0)
						* LargestSpotSize!=(H)
								* C-class=(2)|(1): D(5.0/6.0)
								* C-class!=(2)|(1): C(16.0/19.0)
										* C-class!=(0)|(1)|(2)|(5)|(6)|(7)|(8): E(3.0/0.0)
		* SpotDistribution!=(C)|(I)|(O): H(298.0/0.0)


