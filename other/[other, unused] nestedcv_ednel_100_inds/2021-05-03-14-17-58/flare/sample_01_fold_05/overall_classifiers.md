# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = X | H | 0.311715 |
| SpotDistribution != X and LargestSpotSize = X | B | 0.134172 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and HistComplex != 1 and SpotDistribution != C and SpotDistribution != O | D | 0.049209 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and HistComplex = 1 and SpotDistribution != C and SpotDistribution = O and LargestSpotSize != H and C-class != 2 and LargestSpotSize = R | C | 0.051374 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and HistComplex = 1 and SpotDistribution != C and SpotDistribution = O and LargestSpotSize != H and C-class != 2 and LargestSpotSize != R and C-class != 1 | C | 0.045470 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and HistComplex = 1 and SpotDistribution != C and SpotDistribution != O | D | 0.031605 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and HistComplex != 1 and SpotDistribution != C and SpotDistribution = O and LargestSpotSize != H and C-class != 4 and Activity = 1 and Evolution != 1 and C-class != 1 and C-class = 0 and Evolution = 2 | C | 0.020035 |
| SpotDistribution != X and LargestSpotSize != X and Area != 1 | E | 0.008970 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and HistComplex != 1 and SpotDistribution != C and SpotDistribution = O and LargestSpotSize != H and C-class != 4 and Activity = 1 and Evolution != 1 and C-class != 1 and C-class = 0 and Evolution != 2 | D | 0.007765 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and HistComplex = 1 and SpotDistribution != C and SpotDistribution = O and LargestSpotSize != H and C-class != 2 and LargestSpotSize != R and C-class = 1 and Evolution != 2 | D | 0.006040 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and HistComplex != 1 and SpotDistribution != C and SpotDistribution = O and LargestSpotSize != H and C-class != 4 and Activity != 1 and Prev24Hour = 1 | E | 0.005143 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and HistComplex != 1 and SpotDistribution != C and SpotDistribution = O and LargestSpotSize != H and C-class != 4 and Activity = 1 and Evolution = 1 | D | 0.003742 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and HistComplex != 1 and SpotDistribution = C | E | 0.003753 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and HistComplex != 1 and SpotDistribution != C and SpotDistribution = O and LargestSpotSize != H and C-class != 4 and Activity != 1 and Prev24Hour != 1 | D | 0.003589 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and HistComplex = 1 and SpotDistribution != C and SpotDistribution = O and LargestSpotSize != H and C-class != 2 and LargestSpotSize != R and C-class = 1 and Evolution = 2 | C | 0.004161 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and HistComplex != 1 and SpotDistribution != C and SpotDistribution = O and LargestSpotSize = H | D | 0.003374 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and HistComplex != 1 and SpotDistribution != C and SpotDistribution = O and LargestSpotSize != H and C-class = 4 | E | 0.002291 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and HistComplex != 1 and SpotDistribution != C and SpotDistribution = O and LargestSpotSize != H and C-class != 4 and Activity = 1 and Evolution != 1 and C-class = 1 | D | 0.002165 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and HistComplex != 1 and SpotDistribution != C and SpotDistribution = O and LargestSpotSize != H and C-class != 4 and Activity = 1 and Evolution != 1 and C-class != 1 and C-class != 0 | D | 0.001797 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and HistComplex = 1 and SpotDistribution = C | E | 0.001148 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and HistComplex = 1 and SpotDistribution != C and SpotDistribution = O and LargestSpotSize != H and C-class = 2 | D | 0.001081 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and HistComplex = 1 and SpotDistribution != C and SpotDistribution = O and LargestSpotSize = H | D | 0.000338 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = X | H | 0.311715 |
| LargestSpotSize = X | B | 0.195122 |
| SpotDistribution = C and LargestSpotSize = K and Prev24Hour = 1 | F | 0.005081 |
| SpotDistribution = C and Area = 1 | E | 0.010343 |
| SpotDistribution = O and C-class = 0 and LargestSpotSize = R and HistComplex = 1 and Evolution = 3 | C | 0.066138 |
| SpotDistribution = O and C-class = 0 and LargestSpotSize = R and Evolution = 2 and HistComplex = 1 | C | 0.040958 |
| SpotDistribution = O and LargestSpotSize = R and C-class = 0 and Evolution = 2 | C | 0.008896 |
| SpotDistribution = O and LargestSpotSize = R and C-class = 0 | C | 0.003077 |
| SpotDistribution = O and LargestSpotSize = R | D | 0.114165 |
| SpotDistribution = O and LargestSpotSize = S and C-class = 1 and Evolution = 2 | C | 0.009513 |
| SpotDistribution = O and C-class = 0 and LargestSpotSize = S and HistComplex = 1 and Activity = 1 and Evolution = 3 | C | 0.048565 |
| Area = 2 and SpotDistribution = I | F | 0.008778 |
| SpotDistribution = I and HistComplex = 1 and LargestSpotSize = A | D | 0.078139 |
| HistComplex = 1 and Evolution = 3 and C-class = 1 and SpotDistribution = O | D | 0.016043 |
| HistComplex = 1 and Evolution = 3 and C-class = 0 and LargestSpotSize = S | D | 0.043269 |
| HistComplex = 1 and Evolution = 3 and C-class = 0 and LargestSpotSize = A | D | 0.011251 |
| HistComplex = 1 and Evolution = 3 and C-class = 0 | D | 0.005511 |
| HistComplex = 1 and C-class = 0 and Activity = 1 | C | 0.082902 |
| SpotDistribution = I and HistComplex = 1 | D | 0.015126 |
| SpotDistribution = C | E | 0.025253 |
| SpotDistribution = I and LargestSpotSize = R and Evolution = 3 | D | 0.024242 |
| SpotDistribution = I and LargestSpotSize = K and Evolution = 2 | D | 0.011042 |
| SpotDistribution = I and LargestSpotSize = A and Evolution = 3 and Activity = 1 | D | 0.043373 |
| SpotDistribution = O and C-class = 0 and HistComplex = 2 and LargestSpotSize = A and Evolution = 2 | C | 0.018941 |
| SpotDistribution = I and LargestSpotSize = S and Evolution = 2 | E | 0.015873 |
| SpotDistribution = I and LargestSpotSize = A and C-class = 0 and Evolution = 2 and Activity = 1 | D | 0.026846 |
| SpotDistribution = I and LargestSpotSize = S | D | 0.027551 |
| SpotDistribution = I and LargestSpotSize = A and Evolution = 2 and C-class = 0 | D | 0.006395 |
| LargestSpotSize = K | D | 0.028805 |
| C-class = 0 and HistComplex = 2 and LargestSpotSize = S and Evolution = 2 | C | 0.041558 |
| C-class = 0 and HistComplex = 2 and Evolution = 3 and LargestSpotSize = A and Activity = 1 | D | 0.016917 |
| HistComplex = 1 and Activity = 2 | C | 0.046682 |
| LargestSpotSize = R | D | 0.015254 |
| LargestSpotSize = H and Evolution = 3 | D | 0.015873 |
| LargestSpotSize = A and SpotDistribution = O | E | 0.054039 |
| LargestSpotSize = A and Evolution = 2 and Activity = 2 | D | 0.019791 |
| LargestSpotSize = A and Evolution = 3 | D | 0.027654 |
| Evolution = 3 | C | 0.088615 |
| C-class = 0 | D | 0.145075 |
|  | D | 0.128713 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = I and Evolution = 2 | F | 0.004433 |
| HistComplex = 2 and Activity = 2 and SpotDistribution = C | E | 0.009380 |
| HistComplex = 2 and Activity = 2 and SpotDistribution = O | E | 0.005589 |
| HistComplex = 2 and SpotDistribution = I | E | 0.012364 |
| LargestSpotSize = X | B | 0.145786 |
| SpotDistribution = O and HistComplex = 1 and C-class = 0 and Evolution = 2 and LargestSpotSize = S | C | 0.028925 |
| SpotDistribution = O and LargestSpotSize = R and Evolution = 2 | C | 0.034719 |
| SpotDistribution = O and HistComplex = 1 and C-class = 0 and LargestSpotSize = R | C | 0.040149 |
| SpotDistribution = O and LargestSpotSize = S and HistComplex = 1 and C-class = 0 and Prev24Hour = 1 | C | 0.026401 |
| SpotDistribution = O and Evolution = 2 and C-class = 0 | C | 0.013517 |
| SpotDistribution = O and HistComplex = 1 | C | 0.006289 |
| SpotDistribution = O and Evolution = 3 | C | 0.003449 |
| SpotDistribution = I and LargestSpotSize = A | D | 0.114872 |
| SpotDistribution = I | D | 0.074781 |
| SpotDistribution = O | D | 0.180436 |
|  | H | 0.786280 |


# Text representation of classifiers as-is

## JRip

Decision list:

rules | predicted class
---|---
(SpotDistribution = I) and (Evolution = 2)|F (84.0/66.0)
(HistComplex = 2) and (Activity = 2) and (SpotDistribution = C)|E (21.0/8.0)
(HistComplex = 2) and (Activity = 2) and (SpotDistribution = O)|E (21.0/11.0)
(HistComplex = 2) and (SpotDistribution = I)|E (69.0/50.0)
(LargestSpotSize = X)|B (116.0/0.0)
(SpotDistribution = O) and (HistComplex = 1) and (C-class = 0) and (Evolution = 2) and (LargestSpotSize = S)|C (29.0/7.0)
(SpotDistribution = O) and (LargestSpotSize = R) and (Evolution = 2)|C (39.0/11.0)
(SpotDistribution = O) and (HistComplex = 1) and (C-class = 0) and (LargestSpotSize = R)|C (59.0/20.0)
(SpotDistribution = O) and (LargestSpotSize = S) and (HistComplex = 1) and (C-class = 0) and (Prev24Hour = 1)|C (38.0/12.0)
(SpotDistribution = O) and (Evolution = 2) and (C-class = 0)|C (35.0/16.0)
(SpotDistribution = O) and (HistComplex = 1)|C (40.0/23.0)
(SpotDistribution = O) and (Evolution = 3)|C (29.0/18.0)
(SpotDistribution = I) and (LargestSpotSize = A)|D (18.0/2.0)
(SpotDistribution = I)|D (26.0/11.0)
(SpotDistribution = O)|D (24.0/13.0)
|H (308.0/10.0)


## PART

Decision list:

rules | predicted class
---|---
SpotDistribution = X|H (298.0)
LargestSpotSize = X|B (128.0)
SpotDistribution = C AND LargestSpotSize = K AND Prev24Hour = 1|F (10.0/5.0)
SpotDistribution = C AND Area = 1|E (13.0/6.0)
SpotDistribution = O AND C-class = 0 AND LargestSpotSize = R AND HistComplex = 1 AND Evolution = 3|C (54.0/19.0)
SpotDistribution = O AND C-class = 0 AND LargestSpotSize = R AND Evolution = 2 AND HistComplex = 1|C (26.0/7.0)
SpotDistribution = O AND LargestSpotSize = R AND C-class = 0 AND Evolution = 2|C (10.0/3.0)
SpotDistribution = O AND LargestSpotSize = R AND C-class = 0|C (10.0/4.0)
SpotDistribution = O AND LargestSpotSize = R|D (10.0/5.0)
SpotDistribution = O AND LargestSpotSize = S AND C-class = 1 AND Evolution = 2|C (9.0/4.0)
SpotDistribution = O AND C-class = 0 AND LargestSpotSize = S AND HistComplex = 1 AND Activity = 1 AND Evolution = 3|C (33.0/11.0)
Area = 2 AND SpotDistribution = I|F (8.0/3.0)
SpotDistribution = I AND HistComplex = 1 AND LargestSpotSize = A|D (21.0/2.0)
HistComplex = 1 AND Evolution = 3 AND C-class = 1 AND SpotDistribution = O|D (9.0/3.0)
HistComplex = 1 AND Evolution = 3 AND C-class = 0 AND LargestSpotSize = S|D (14.0/8.0)
HistComplex = 1 AND Evolution = 3 AND C-class = 0 AND LargestSpotSize = A|D (9.0/4.0)
HistComplex = 1 AND Evolution = 3 AND C-class = 0|D (8.0/3.0)
HistComplex = 1 AND C-class = 0 AND Activity = 1|C (30.0/9.0)
SpotDistribution = I AND HistComplex = 1|D (11.0/5.0)
SpotDistribution = C|E (8.0/1.0)
SpotDistribution = I AND LargestSpotSize = R AND Evolution = 3|D (7.0/1.0)
SpotDistribution = I AND LargestSpotSize = K AND Evolution = 2|D (9.0/5.0)
SpotDistribution = I AND LargestSpotSize = A AND Evolution = 3 AND Activity = 1|D (18.0/6.0)
SpotDistribution = O AND C-class = 0 AND HistComplex = 2 AND LargestSpotSize = A AND Evolution = 2|C (13.0/6.0)
SpotDistribution = I AND LargestSpotSize = S AND Evolution = 2|E (12.0/6.0)
SpotDistribution = I AND LargestSpotSize = A AND C-class = 0 AND Evolution = 2 AND Activity = 1|D (16.0/8.0)
SpotDistribution = I AND LargestSpotSize = S|D (11.0/6.0)
SpotDistribution = I AND LargestSpotSize = A AND Evolution = 2 AND C-class = 0|D (10.0/6.0)
LargestSpotSize = K|D (9.0/1.0)
C-class = 0 AND HistComplex = 2 AND LargestSpotSize = S AND Evolution = 2|C (20.0/9.0)
C-class = 0 AND HistComplex = 2 AND Evolution = 3 AND LargestSpotSize = A AND Activity = 1|D (12.0/6.0)
HistComplex = 1 AND Activity = 2|C (10.0/2.0)
LargestSpotSize = R|D (7.0/3.0)
LargestSpotSize = H AND Evolution = 3|D (7.0/3.0)
LargestSpotSize = A AND SpotDistribution = O|E (16.0/7.0)
LargestSpotSize = A AND Evolution = 2 AND Activity = 2|D (8.0/4.0)
LargestSpotSize = A AND Evolution = 3|D (12.0/7.0)
Evolution = 3|C (17.0/9.0)
C-class = 0|D (11.0/6.0)
|D (12.0/7.0)


## J48 Decision Tree

* SpotDistribution = X: H (256.0)
* SpotDistribution != X
	* LargestSpotSize = X: B (109.0)
	* LargestSpotSize != X
		* Area = 1
			* HistComplex = 1
				* SpotDistribution = C: E (3.0/1.0)
				* SpotDistribution != C
					* SpotDistribution = O
						* LargestSpotSize = H: D (3.0/2.0)
						* LargestSpotSize != H
							* C-class = 2: D (5.0/3.0)
							* C-class != 2
								* LargestSpotSize = R: C (80.0/27.0)
								* LargestSpotSize != R
									* C-class = 1
										* Evolution = 2: C (4.0/1.0)
										* Evolution != 2: D (6.0/2.0)
									* C-class != 1: C (68.0/23.0)
					* SpotDistribution != O: D (48.0/14.0)
			* HistComplex != 1
				* SpotDistribution = C: E (8.0/3.0)
				* SpotDistribution != C
					* SpotDistribution = O
						* LargestSpotSize = H: D (10.0/5.0)
						* LargestSpotSize != H
							* C-class = 4: E (2.0)
							* C-class != 4
								* Activity = 1
									* Evolution = 1: D (11.0/6.0)
									* Evolution != 1
										* C-class = 1: D (9.0/5.0)
										* C-class != 1
											* C-class = 0
												* Evolution = 2: C (33.0/12.0)
												* Evolution != 2: D (19.0/10.0)
											* C-class != 0: D (3.0/1.0)
								* Activity != 1
									* Prev24Hour = 1: E (7.0/2.0)
									* Prev24Hour != 1: D (5.0/2.0)
					* SpotDistribution != O: D (109.0/53.0)
		* Area != 1: E (22.0/10.0)


