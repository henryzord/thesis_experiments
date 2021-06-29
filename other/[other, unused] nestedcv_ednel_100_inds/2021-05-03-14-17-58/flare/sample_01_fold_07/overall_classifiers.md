# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution != C | H | 0.292642 |
| SpotDistribution = O and LargestSpotSize!=(X) and SpotDistribution != I and LargestSpotSize != K | D | 0.049888 |
| SpotDistribution = O and LargestSpotSize!=(X) and SpotDistribution != I and LargestSpotSize = R | C | 0.067504 |
| SpotDistribution = O and LargestSpotSize!=(X) and SpotDistribution != I and LargestSpotSize = S | C | 0.052020 |
| SpotDistribution = O and LargestSpotSize!=(X) and SpotDistribution != I and LargestSpotSize = K | C | 0.001302 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = X | H | 0.311390 |
| LargestSpotSize = X | B | 0.194825 |
| SpotDistribution = C and LargestSpotSize = K | E | 0.015782 |
| SpotDistribution = O and LargestSpotSize = R and HistComplex = 1 and Evolution = 3 | C | 0.078511 |
| SpotDistribution = O and LargestSpotSize = R and HistComplex = 1 | C | 0.041807 |
| SpotDistribution = O and LargestSpotSize = S and C-class = 0 and HistComplex = 1 and Evolution = 2 and Activity = 1 | C | 0.035749 |
| SpotDistribution = O and LargestSpotSize = S and C-class = 0 and HistComplex = 1 and Evolution = 3 | C | 0.037389 |
| SpotDistribution = O and LargestSpotSize = S and C-class = 0 and HistComplex = 2 and Evolution = 2 | C | 0.016667 |
| SpotDistribution = O and LargestSpotSize = R | C | 0.007286 |
| Area = 1 and HistComplex = 1 and SpotDistribution = I and LargestSpotSize = A | D | 0.085911 |
| Area = 1 and HistComplex = 1 and Evolution = 2 and Activity = 1 | C | 0.011111 |
| Area = 1 and HistComplex = 1 and Evolution = 3 and C-class = 0 and SpotDistribution = I | D | 0.031143 |
| Area = 1 and HistComplex = 1 and C-class = 1 | D | 0.058110 |
| Area = 1 and SpotDistribution = I and Evolution = 3 and LargestSpotSize = A and Activity = 1 | D | 0.049259 |
| Area = 1 and SpotDistribution = I and LargestSpotSize = R | D | 0.045977 |
| Area = 1 and SpotDistribution = I and LargestSpotSize = K | D | 0.054237 |
| Area = 1 and SpotDistribution = O and C-class = 0 and LargestSpotSize = S and Evolution = 3 | D | 0.060606 |
| Area = 1 and HistComplex = 1 and Evolution = 3 | D | 0.069716 |
| HistComplex = 2 and Area = 1 and SpotDistribution = O and C-class = 0 and Evolution = 2 | C | 0.006568 |
| HistComplex = 2 and Area = 1 and SpotDistribution = O and C-class = 0 and Evolution = 3 | D | 0.029577 |
| HistComplex = 1 | C | 0.065844 |
| Area = 1 and LargestSpotSize = A and SpotDistribution = O | E | 0.054638 |
| Area = 1 and SpotDistribution = I and C-class = 1 | D | 0.024848 |
| Area = 1 and C-class = 0 and Evolution = 3 | D | 0.021193 |
| Area = 1 and LargestSpotSize = A and Activity = 2 | D | 0.025862 |
| Area = 1 and C-class = 0 and Evolution = 2 and LargestSpotSize = A | D | 0.041724 |
| LargestSpotSize = S and SpotDistribution = O | D | 0.089929 |
| LargestSpotSize = S | E | 0.125071 |
| Area = 1 | E | 0.248883 |
|  | F | 0.453488 |


# Text representation of classifiers as-is

## PART

Decision list:

rules | predicted class
---|---
SpotDistribution = X|H (298.0)
LargestSpotSize = X|B (128.0)
SpotDistribution = C AND LargestSpotSize = K|E (17.0/6.0)
SpotDistribution = O AND LargestSpotSize = R AND HistComplex = 1 AND Evolution = 3|C (61.0/20.0)
SpotDistribution = O AND LargestSpotSize = R AND HistComplex = 1|C (37.0/9.0)
SpotDistribution = O AND LargestSpotSize = S AND C-class = 0 AND HistComplex = 1 AND Evolution = 2 AND Activity = 1|C (21.0/5.0)
SpotDistribution = O AND LargestSpotSize = S AND C-class = 0 AND HistComplex = 1 AND Evolution = 3|C (35.0/14.0)
SpotDistribution = O AND LargestSpotSize = S AND C-class = 0 AND HistComplex = 2 AND Evolution = 2|C (22.0/11.0)
SpotDistribution = O AND LargestSpotSize = R|C (16.0/6.0)
Area = 1 AND HistComplex = 1 AND SpotDistribution = I AND LargestSpotSize = A|D (24.0/4.0)
Area = 1 AND HistComplex = 1 AND Evolution = 2 AND Activity = 1|C (17.0/7.0)
Area = 1 AND HistComplex = 1 AND Evolution = 3 AND C-class = 0 AND SpotDistribution = I|D (17.0/7.0)
Area = 1 AND HistComplex = 1 AND C-class = 1|D (17.0/7.0)
Area = 1 AND SpotDistribution = I AND Evolution = 3 AND LargestSpotSize = A AND Activity = 1|D (21.0/7.0)
Area = 1 AND SpotDistribution = I AND LargestSpotSize = R|D (15.0/3.0)
Area = 1 AND SpotDistribution = I AND LargestSpotSize = K|D (15.0/3.0)
Area = 1 AND SpotDistribution = O AND C-class = 0 AND LargestSpotSize = S AND Evolution = 3|D (10.0/4.0)
Area = 1 AND HistComplex = 1 AND Evolution = 3|D (17.0/10.0)
HistComplex = 2 AND Area = 1 AND SpotDistribution = O AND C-class = 0 AND Evolution = 2|C (15.0/9.0)
HistComplex = 2 AND Area = 1 AND SpotDistribution = O AND C-class = 0 AND Evolution = 3|D (15.0/7.0)
HistComplex = 1|C (13.0/3.0)
Area = 1 AND LargestSpotSize = A AND SpotDistribution = O|E (13.0/6.0)
Area = 1 AND SpotDistribution = I AND C-class = 1|D (14.0/7.0)
Area = 1 AND C-class = 0 AND Evolution = 3|D (16.0/7.0)
Area = 1 AND LargestSpotSize = A AND Activity = 2|D (20.0/13.0)
Area = 1 AND C-class = 0 AND Evolution = 2 AND LargestSpotSize = A|D (14.0/7.0)
LargestSpotSize = S AND SpotDistribution = O|D (16.0/8.0)
LargestSpotSize = S|E (14.0/7.0)
Area = 1|E (10.0/6.0)
|F (9.0/3.0)


## SimpleCart Decision Tree

		* SpotDistribution=(C)|(I)|(O)
	* LargestSpotSize=(X): B(128.0/0.0)
	* LargestSpotSize!=(X)
			* SpotDistribution=(C)|(I)
			* Area=(2): E(12.0/11.0)
			* Area!=(2): D(108.0/85.0)
			* SpotDistribution!=(C)|(I)
						* LargestSpotSize=(K)|(S)|(R)|(X): C(153.0/93.0)
						* LargestSpotSize!=(K)|(S)|(R)|(X): D(29.0/40.0)
		* SpotDistribution!=(C)|(I)|(O): H(298.0/0.0)


