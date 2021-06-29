# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = X | H | 0.311715 |
| SpotDistribution != X and LargestSpotSize = X | B | 0.134172 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution = O and LargestSpotSize != H and LargestSpotSize != A and C-class != 1 and LargestSpotSize != S and HistComplex = 1 and Evolution = 3 | C | 0.033364 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution = O and LargestSpotSize != H and LargestSpotSize != A and C-class != 1 and LargestSpotSize != S and HistComplex = 1 and Evolution != 3 | C | 0.026095 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution != O and HistComplex = 1 and LargestSpotSize = A and C-class = 0 | D | 0.018626 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution = O and LargestSpotSize != H and LargestSpotSize != A and C-class != 1 and LargestSpotSize = S and C-class = 0 and HistComplex = 1 and Activity = 1 and Evolution != 2 | C | 0.018344 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution = O and LargestSpotSize != H and LargestSpotSize != A and C-class != 1 and LargestSpotSize = S and C-class = 0 and HistComplex = 1 and Activity = 1 and Evolution = 2 | C | 0.015241 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution != O and HistComplex != 1 and LargestSpotSize != R and Evolution = 3 and LargestSpotSize != K and C-class = 0 and Activity = 1 | D | 0.010784 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution != O and HistComplex != 1 and LargestSpotSize = R | D | 0.009562 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution != O and HistComplex != 1 and LargestSpotSize != R and Evolution = 3 and LargestSpotSize = K | D | 0.009507 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution = O and LargestSpotSize != H and LargestSpotSize != A and C-class = 1 and HistComplex = 1 | D | 0.008389 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution != O and HistComplex != 1 and LargestSpotSize != R and Evolution != 3 and C-class = 0 and Activity = 1 | D | 0.008097 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution = O and LargestSpotSize != H and LargestSpotSize != A and C-class != 1 and LargestSpotSize = S and C-class = 0 and HistComplex = 1 and Activity != 1 | C | 0.009526 |
| SpotDistribution != X and LargestSpotSize != X and Area != 1 and Prev24Hour != 1 | E | 0.008099 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution = O and LargestSpotSize != H and LargestSpotSize = A and C-class = 0 and Evolution != 2 and HistComplex != 1 | D | 0.006617 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution = O and LargestSpotSize != H and LargestSpotSize != A and C-class != 1 and LargestSpotSize = S and C-class = 0 and HistComplex != 1 and Evolution = 2 | C | 0.008523 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution = O and LargestSpotSize != H and LargestSpotSize != A and C-class != 1 and LargestSpotSize != S and HistComplex != 1 | C | 0.007514 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution != O and HistComplex = 1 and LargestSpotSize != A and C-class = 0 and LargestSpotSize != R | D | 0.005496 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution = O and LargestSpotSize != H and LargestSpotSize != A and C-class != 1 and LargestSpotSize = S and C-class = 0 and HistComplex != 1 and Evolution != 2 | D | 0.005398 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution != O and HistComplex != 1 and LargestSpotSize != R and Evolution != 3 and C-class != 0 and C-class = 1 | D | 0.004723 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution = O and LargestSpotSize != H and LargestSpotSize = A and C-class = 0 and Evolution = 2 | C | 0.005875 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution != O and HistComplex = 1 and LargestSpotSize = A and C-class != 0 | D | 0.004206 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution = O and LargestSpotSize != H and LargestSpotSize = A and C-class = 0 and Evolution != 2 and HistComplex = 1 | D | 0.004049 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution != O and HistComplex != 1 and LargestSpotSize != R and Evolution = 3 and LargestSpotSize != K and C-class = 0 and Activity != 1 | D | 0.004049 |
| SpotDistribution != X and LargestSpotSize != X and Area != 1 and Prev24Hour = 1 | F | 0.004643 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution != O and HistComplex != 1 and LargestSpotSize != R and Evolution = 3 and LargestSpotSize != K and C-class != 0 and C-class != 1 | E | 0.003753 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution = O and LargestSpotSize != H and LargestSpotSize = A and C-class != 0 | D | 0.003742 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution != O and HistComplex = 1 and LargestSpotSize != A and C-class != 0 | D | 0.003744 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution != O and HistComplex != 1 and LargestSpotSize != R and Evolution != 3 and C-class = 0 and Activity != 1 | D | 0.003504 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution = O and LargestSpotSize = H | D | 0.003252 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution != O and HistComplex != 1 and LargestSpotSize != R and Evolution != 3 and C-class != 0 and C-class != 1 | F | 0.003562 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution = O and LargestSpotSize != H and LargestSpotSize != A and C-class = 1 and HistComplex != 1 | D | 0.002699 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution != O and HistComplex = 1 and LargestSpotSize != A and C-class = 0 and LargestSpotSize = R | D | 0.002699 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution != O and HistComplex != 1 and LargestSpotSize != R and Evolution = 3 and LargestSpotSize != K and C-class != 0 and C-class = 1 | E | 0.002296 |
| SpotDistribution != X and LargestSpotSize != X and Area = 1 and SpotDistribution = O and LargestSpotSize != H and LargestSpotSize != A and C-class != 1 and LargestSpotSize = S and C-class != 0 | D | 0.002165 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = X | H | 0.311715 |
| LargestSpotSize = X | B | 0.195122 |
| SpotDistribution = O and LargestSpotSize = S | C | 0.120789 |
| HistComplex = 1 and SpotDistribution = O and C-class = 0 | C | 0.110423 |
| Area = 1 and HistComplex = 1 | D | 0.307243 |
| Area = 1 and SpotDistribution = I and Evolution = 3 | D | 0.113375 |
| Area = 1 and SpotDistribution = O and Activity = 1 and LargestSpotSize = A | D | 0.032203 |
| Area = 1 and SpotDistribution = I and C-class = 0 | D | 0.044444 |
| SpotDistribution = I | F | 0.052484 |
| Activity = 2 | E | 0.210904 |
| LargestSpotSize = R | C | 0.136111 |
|  | D | 0.372093 |


# Text representation of classifiers as-is

## PART

Decision list:

rules | predicted class
---|---
SpotDistribution = X|H (298.0)
LargestSpotSize = X|B (128.0)
SpotDistribution = O AND LargestSpotSize = S|C (129.0/54.0)
HistComplex = 1 AND SpotDistribution = O AND C-class = 0|C (107.0/37.0)
Area = 1 AND HistComplex = 1|D (67.0/24.0)
Area = 1 AND SpotDistribution = I AND Evolution = 3|D (58.0/21.0)
Area = 1 AND SpotDistribution = O AND Activity = 1 AND LargestSpotSize = A|D (29.0/16.0)
Area = 1 AND SpotDistribution = I AND C-class = 0|D (42.0/22.0)
SpotDistribution = I|F (34.0/19.0)
Activity = 2|E (34.0/11.0)
LargestSpotSize = R|C (16.0/6.0)
|D (14.0/8.0)


## J48 Decision Tree

* SpotDistribution = X: H (298.0)
* SpotDistribution != X
	* LargestSpotSize = X: B (128.0)
	* LargestSpotSize != X
		* Area = 1
			* SpotDistribution = O
				* LargestSpotSize = H: D (15.0/9.0)
				* LargestSpotSize != H
					* LargestSpotSize = A
						* C-class = 0
							* Evolution = 2: C (18.0/9.0)
							* Evolution != 2
								* HistComplex = 1: D (12.0/6.0)
								* HistComplex != 1: D (13.0/5.0)
						* C-class != 0: D (13.0/7.0)
					* LargestSpotSize != A
						* C-class = 1
							* HistComplex = 1: D (16.0/6.0)
							* HistComplex != 1: D (8.0/4.0)
						* C-class != 1
							* LargestSpotSize = S
								* C-class = 0
									* HistComplex = 1
										* Activity = 1
											* Evolution = 2: C (19.0/4.0)
											* Evolution != 2: C (34.0/12.0)
										* Activity != 1: C (11.0/2.0)
									* HistComplex != 1
										* Evolution = 2: C (22.0/10.0)
										* Evolution != 2: D (16.0/8.0)
								* C-class != 0: D (10.0/6.0)
							* LargestSpotSize != S
								* HistComplex = 1
									* Evolution = 3: C (58.0/19.0)
									* Evolution != 3: C (33.0/7.0)
								* HistComplex != 1: C (14.0/5.0)
			* SpotDistribution != O
				* HistComplex = 1
					* LargestSpotSize = A
						* C-class = 0: D (16.0/1.0)
						* C-class != 0: D (8.0/3.0)
					* LargestSpotSize != A
						* C-class = 0
							* LargestSpotSize = R: D (8.0/4.0)
							* LargestSpotSize != R: D (12.0/5.0)
						* C-class != 0: D (9.0/4.0)
				* HistComplex != 1
					* LargestSpotSize = R: D (14.0/4.0)
					* LargestSpotSize != R
						* Evolution = 3
							* LargestSpotSize = K: D (9.0/1.0)
							* LargestSpotSize != K
								* C-class = 0
									* Activity = 1: D (15.0/4.0)
									* Activity != 1: D (12.0/6.0)
								* C-class != 0
									* C-class = 1: E (8.0/4.0)
									* C-class != 1: E (11.0/5.0)
						* Evolution != 3
							* C-class = 0
								* Activity = 1: D (24.0/12.0)
								* Activity != 1: D (19.0/12.0)
							* C-class != 0
								* C-class = 1: D (14.0/7.0)
								* C-class != 1: F (15.0/8.0)
		* Area != 1
			* Prev24Hour = 1: F (15.0/7.0)
			* Prev24Hour != 1: E (9.0/1.0)


