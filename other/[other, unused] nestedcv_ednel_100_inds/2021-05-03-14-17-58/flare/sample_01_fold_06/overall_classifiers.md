# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = X | H | 0.311715 |
| SpotDistribution = O and LargestSpotSize = X | B | 0.122210 |
| SpotDistribution = O and LargestSpotSize!=(X) and SpotDistribution != I and LargestSpotSize != X and Activity!=(2) and C-class != 3 | D | 0.055764 |
| SpotDistribution = O and LargestSpotSize = R | C | 0.062467 |
| SpotDistribution = O and LargestSpotSize = S | C | 0.055406 |
| SpotDistribution = I and LargestSpotSize = A | D | 0.041647 |
| SpotDistribution = C | E | 0.013415 |
| SpotDistribution = I and LargestSpotSize = X | B | 0.015495 |
| SpotDistribution = I and LargestSpotSize = R | D | 0.012550 |
| SpotDistribution = I and LargestSpotSize = S | D | 0.010863 |
| SpotDistribution = I and LargestSpotSize = K | D | 0.009664 |
| SpotDistribution = I and LargestSpotSize = H | E | 0.001529 |
| SpotDistribution = O and LargestSpotSize!=(X) and SpotDistribution != I and LargestSpotSize != X and Activity!=(2) and C-class = 3 | D | 0.000902 |
| SpotDistribution = O and LargestSpotSize = K | C | 0.001304 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = X | H | 0.311715 |
| LargestSpotSize = X | B | 0.195122 |
| SpotDistribution = O and LargestSpotSize = S | C | 0.120789 |
| HistComplex = 1 and SpotDistribution = O | C | 0.113018 |
| Area = 2 and X-class = 0 and LargestSpotSize = K | E | 0.022297 |
| HistComplex = 1 and Activity = 1 and LargestSpotSize = A | D | 0.113252 |
| SpotDistribution = C | E | 0.018060 |
| SpotDistribution = O and Activity = 2 and Prev24Hour = 1 | E | 0.015686 |
| SpotDistribution = O and C-class = 0 and Evolution = 2 | C | 0.015503 |
| HistComplex = 1 and Activity = 1 and Evolution = 3 | D | 0.239860 |
| Evolution = 3 | D | 0.285124 |
| HistComplex = 1 | C | 0.019545 |
| LargestSpotSize = R and C-class = 0 and Evolution = 1 | C | 0.010526 |
| LargestSpotSize = R and C-class = 0 | D | 0.095480 |
|  | D | 0.363095 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = I and Evolution = 2 | F | 0.005631 |
| Activity = 2 and SpotDistribution = C and C-class = 0 | E | 0.008965 |
| HistComplex = 2 and Activity = 2 | E | 0.011945 |
| LargestSpotSize = X | B | 0.143177 |
| SpotDistribution = O and HistComplex = 1 and C-class = 0 and Evolution = 2 and LargestSpotSize = R | C | 0.027544 |
| SpotDistribution = O and HistComplex = 1 and C-class = 0 and LargestSpotSize = S and Evolution = 2 and Activity = 1 | C | 0.020105 |
| SpotDistribution = O and HistComplex = 1 and C-class = 0 and LargestSpotSize = S | C | 0.033185 |
| SpotDistribution = O and LargestSpotSize = R and C-class = 0 | C | 0.051699 |
| SpotDistribution = O and LargestSpotSize = S and Evolution = 3 | C | 0.006119 |
| SpotDistribution = O and Evolution = 2 and C-class = 0 | C | 0.014191 |
| SpotDistribution = O and HistComplex = 1 | C | 0.004917 |
| SpotDistribution = I and C-class = 0 | D | 0.114145 |
| SpotDistribution = O and C-class = 0 | D | 0.145799 |
| SpotDistribution = I | D | 0.034658 |
|  | H | 0.709524 |


# Text representation of classifiers as-is

## JRip

Decision list:

rules | predicted class
---|---
(SpotDistribution = I) and (Evolution = 2)|F (81.0/61.0)
(Activity = 2) and (SpotDistribution = C) and (C-class = 0)|E (13.0/3.0)
(HistComplex = 2) and (Activity = 2)|E (68.0/44.0)
(LargestSpotSize = X)|B (119.0/0.0)
(SpotDistribution = O) and (HistComplex = 1) and (C-class = 0) and (Evolution = 2) and (LargestSpotSize = R)|C (27.0/6.0)
(SpotDistribution = O) and (HistComplex = 1) and (C-class = 0) and (LargestSpotSize = S) and (Evolution = 2) and (Activity = 1)|C (19.0/4.0)
(SpotDistribution = O) and (HistComplex = 1) and (C-class = 0) and (LargestSpotSize = S)|C (45.0/14.0)
(SpotDistribution = O) and (LargestSpotSize = R) and (C-class = 0)|C (75.0/25.0)
(SpotDistribution = O) and (LargestSpotSize = S) and (Evolution = 3)|C (20.0/10.0)
(SpotDistribution = O) and (Evolution = 2) and (C-class = 0)|C (36.0/18.0)
(SpotDistribution = O) and (HistComplex = 1)|C (34.0/19.0)
(SpotDistribution = I) and (C-class = 0)|D (53.0/13.0)
(SpotDistribution = O) and (C-class = 0)|D (23.0/9.0)
(SpotDistribution = I)|D (28.0/11.0)
|H (315.0/23.0)


## PART

Decision list:

rules | predicted class
---|---
SpotDistribution = X|H (298.0)
LargestSpotSize = X|B (128.0)
SpotDistribution = O AND LargestSpotSize = S|C (129.0/54.0)
HistComplex = 1 AND SpotDistribution = O|C (121.0/45.0)
Area = 2 AND X-class = 0 AND LargestSpotSize = K|E (15.0/5.0)
HistComplex = 1 AND Activity = 1 AND LargestSpotSize = A|D (17.0/2.0)
SpotDistribution = C|E (21.0/11.0)
SpotDistribution = O AND Activity = 2 AND Prev24Hour = 1|E (7.0)
SpotDistribution = O AND C-class = 0 AND Evolution = 2|C (24.0/10.0)
HistComplex = 1 AND Activity = 1 AND Evolution = 3|D (22.0/9.0)
Evolution = 3|D (86.0/31.0)
HistComplex = 1|C (4.0/1.0)
LargestSpotSize = R AND C-class = 0 AND Evolution = 1|C (4.0/1.0)
LargestSpotSize = R AND C-class = 0|D (3.0)
|D (77.0/46.0)


## J48 Decision Tree

* SpotDistribution = X: H (298.0)
* SpotDistribution = O
	* LargestSpotSize = A: D (56.0/31.0)
	* LargestSpotSize = R: C (112.0/37.0)
	* LargestSpotSize = S: C (129.0/54.0)
	* LargestSpotSize = X: B (115.0)
	* LargestSpotSize = K: C (1.0)
	* LargestSpotSize = H: D (15.0/9.0)
* SpotDistribution = I
	* LargestSpotSize = A: D (100.0/44.0)
	* LargestSpotSize = R: D (24.0/9.0)
	* LargestSpotSize = S: D (36.0/19.0)
	* LargestSpotSize = X: B (13.0)
	* LargestSpotSize = K: D (20.0/8.0)
	* LargestSpotSize = H: E (3.0/1.0)
* SpotDistribution = C: E (34.0/14.0)


## SimpleCart Decision Tree

		* SpotDistribution=(C)|(I)|(O)
	* LargestSpotSize=(X): B(128.0/0.0)
	* LargestSpotSize!=(X)
			* SpotDistribution=(C)|(I)
			* Area=(2): E(12.0/10.0)
			* Area!=(2)
				* Evolution=(3)
									* C-class=(0)|(1)|(2)|(7)|(8)
							* LargestSpotSize=(S)|(R): D(27.0/15.0)
							* LargestSpotSize!=(S)|(R)
							* HistComplex=(2): D(24.0/15.0)
							* HistComplex!=(2): D(17.0/2.0)
									* C-class!=(0)|(1)|(2)|(7)|(8): E(6.0/4.0)
				* Evolution!=(3): D(35.0/50.0)
			* SpotDistribution!=(C)|(I)
					* LargestSpotSize=(S)|(R)|(X)
							* C-class=(0)|(4)|(7)|(8)
					* HistComplex=(2): C(27.0/26.0)
					* HistComplex!=(2)
						* Evolution=(2)
							* LargestSpotSize=(S): C(20.0/6.0)
							* LargestSpotSize!=(S): C(21.0/6.0)
						* Evolution!=(2): C(67.0/32.0)
							* C-class!=(0)|(4)|(7)|(8): D(18.0/18.0)
					* LargestSpotSize!=(S)|(R)|(X)
				* Activity=(2): E(7.0/5.0)
				* Activity!=(2)
							* C-class=(3)|(2)|(1): D(5.0/9.0)
							* C-class!=(3)|(2)|(1): D(22.0/24.0)
		* SpotDistribution!=(C)|(I)|(O): H(298.0/0.0)


