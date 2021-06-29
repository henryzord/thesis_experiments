# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = X | H | 0.311715 |
| SpotDistribution = O and LargestSpotSize = X | B | 0.122210 |
| LargestSpotSize = R and SpotDistribution = O and HistComplex = 1 and Area = 1 | C | 0.055013 |
| LargestSpotSize = S and SpotDistribution = O and HistComplex = 1 and Area = 1 | C | 0.043842 |
| LargestSpotSize = A and SpotDistribution = I and HistComplex = 2 and Area = 1 | D | 0.024375 |
| SpotDistribution = I and LargestSpotSize = A and HistComplex = 1 | D | 0.021676 |
| LargestSpotSize = K and SpotDistribution = I and HistComplex = 2 and Area = 1 | D | 0.011324 |
| SpotDistribution = I and LargestSpotSize = X | B | 0.015495 |
| LargestSpotSize = S and SpotDistribution = O and HistComplex = 2 and Area = 1 | C | 0.013233 |
| LargestSpotSize = A and SpotDistribution = O and HistComplex = 2 and Area = 1 | D | 0.008503 |
| LargestSpotSize = R and SpotDistribution = I and HistComplex = 2 and Area = 1 | D | 0.008352 |
| LargestSpotSize = K and SpotDistribution = C and HistComplex = 2 and Area = 2 | E | 0.008623 |
| SpotDistribution = I and LargestSpotSize = S and HistComplex = 1 | D | 0.006814 |
| LargestSpotSize = A and SpotDistribution = O and HistComplex = 1 and Area = 1 | D | 0.006748 |
| LargestSpotSize = R and SpotDistribution = O and HistComplex = 2 and Area = 1 | C | 0.008647 |
| SpotDistribution = O and LargestSpotSize = S and C-class = 0 and HistComplex = 2 and Evolution = 3 | D | 0.003374 |
| SpotDistribution = O and LargestSpotSize = S and C-class = 1 and Evolution = 3 | D | 0.003744 |
| SpotDistribution = O and LargestSpotSize = A and C-class = 0 and Evolution = 2 | C | 0.005875 |
| SpotDistribution = O and LargestSpotSize = S and C-class = 1 and Evolution = 2 | D | 0.002699 |
| SpotDistribution = I and LargestSpotSize = A and HistComplex = 2 and Evolution = 3 and Activity = 2 | E | 0.002959 |
| LargestSpotSize = S and SpotDistribution = I and HistComplex = 2 and Area = 1 | D | 0.004342 |
| LargestSpotSize = R and SpotDistribution = I and HistComplex = 1 and Area = 1 | D | 0.004411 |
| SpotDistribution = O and LargestSpotSize = H | D | 0.003252 |
| SpotDistribution = C and LargestSpotSize = A | E | 0.002612 |
| SpotDistribution = I and LargestSpotSize = S and HistComplex = 2 and Evolution = 2 | E | 0.001841 |
| SpotDistribution = O and LargestSpotSize = S and C-class = 3 | D | 0.001350 |
| SpotDistribution = O and LargestSpotSize = S and C-class = 0 and HistComplex = 2 and Evolution = 1 | D | 0.002024 |
| LargestSpotSize = A and SpotDistribution = I and HistComplex = 2 and Area = 2 | F | 0.002174 |
| SpotDistribution = I and LargestSpotSize = A and HistComplex = 2 and Evolution = 2 and C-class = 2 | F | 0.001451 |
| SpotDistribution = C and LargestSpotSize = R | D | 0.001797 |
| SpotDistribution = O and LargestSpotSize = S and C-class = 2 | D | 0.001350 |
| SpotDistribution = I and LargestSpotSize = A and HistComplex = 2 and Evolution = 2 and C-class = 3 | E | 0.001529 |
| SpotDistribution = I and LargestSpotSize = H | E | 0.001529 |
| LargestSpotSize = K and SpotDistribution = C and HistComplex = 2 and Area = 1 | E | 0.001529 |
| SpotDistribution = O and LargestSpotSize = S and C-class = 0 and HistComplex = 1 and Activity = 1 and Evolution = 1 | D | 0.000675 |
| LargestSpotSize = A and SpotDistribution = C and HistComplex = 1 and Area = 1 | D | 0.000675 |
| LargestSpotSize = H and SpotDistribution = I and HistComplex = 2 and Area = 1 | D | 0.000450 |
| LargestSpotSize = K and SpotDistribution = I and HistComplex = 2 and Area = 2 | E | 0.001148 |
| SpotDistribution = O and LargestSpotSize = A and C-class = 3 | E | 0.001147 |
| SpotDistribution = O and LargestSpotSize = S and C-class = 6 | E | 0.001147 |
| SpotDistribution = O and LargestSpotSize = S and C-class = 5 | E | 0.001147 |
| SpotDistribution = O and LargestSpotSize = K | C | 0.001304 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = X | H | 0.311715 |
| LargestSpotSize = X | B | 0.195122 |
| Area != 1 and Prev24Hour = 1 | F | 0.008654 |
| SpotDistribution != C and SpotDistribution = O and LargestSpotSize != H and LargestSpotSize != A and C-class != 1 and C-class = 0 and HistComplex = 1 | C | 0.193780 |
| Area = 1 and SpotDistribution = O and LargestSpotSize != H and Evolution != 1 and LargestSpotSize != A and M-class = 0 and C-class = 1 and Activity = 1 and HistComplex = 1 | D | 0.026273 |
| Area = 1 and SpotDistribution = O and LargestSpotSize != H and Prev24Hour = 1 and Activity = 1 and LargestSpotSize != R and Evolution != 1 and C-class = 0 and LargestSpotSize != A | C | 0.015371 |
| Area = 1 and LargestSpotSize = R and Activity = 1 and Evolution != 3 | C | 0.022336 |
| Area = 1 and HistComplex = 1 and Evolution = 3 | D | 0.240565 |
| Area = 1 and SpotDistribution != O and LargestSpotSize = R | D | 0.033807 |
| Area != 1 | E | 0.055180 |
| SpotDistribution != O and M-class != 0 and LargestSpotSize = A | D | 0.022321 |
| SpotDistribution != O and C-class != 4 and HistComplex != 1 and Evolution = 3 and LargestSpotSize != K and LargestSpotSize != S and Activity = 1 | D | 0.036468 |
| SpotDistribution != O and C-class != 4 and HistComplex != 1 and SpotDistribution = I and LargestSpotSize = K | D | 0.049187 |
| SpotDistribution = O and LargestSpotSize != H and Prev24Hour = 1 and HistComplex = 1 | C | 0.039764 |
| C-class != 4 and SpotDistribution = O and LargestSpotSize != H and Evolution != 1 and Prev24Hour != 1 | D | 0.016327 |
| C-class != 4 and SpotDistribution != O and C-class != 2 and HistComplex != 1 and C-class = 1 | D | 0.017677 |
| C-class != 4 and SpotDistribution != C and C-class = 2 | F | 0.006047 |
| C-class != 4 and SpotDistribution != C and Activity = 1 and LargestSpotSize = H | D | 0.014569 |
| C-class != 4 and SpotDistribution = C | E | 0.033264 |
| C-class != 4 and Activity = 1 and C-class != 0 and LargestSpotSize = A | E | 0.041538 |
| C-class != 4 and Activity = 1 and SpotDistribution = O and Evolution != 1 and LargestSpotSize = A and Evolution = 2 | C | 0.015972 |
| C-class != 4 and Activity = 1 | D | 0.281549 |
| C-class != 4 and SpotDistribution = O and LargestSpotSize != S | E | 0.083916 |
| Evolution != 2 | D | 0.032527 |
| LargestSpotSize != S | F | 0.124871 |
|  | C | 0.352941 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| HistComplex = 2 and SpotDistribution = C | E | 0.011376 |
| LargestSpotSize = X | B | 0.136606 |
| SpotDistribution = O and LargestSpotSize = R | C | 0.076211 |
| SpotDistribution = O and LargestSpotSize = S | C | 0.067920 |
| SpotDistribution = I and Evolution = 3 | D | 0.092323 |
| LargestSpotSize = A and SpotDistribution = O and Evolution = 3 | D | 0.021023 |
|  | H | 0.516464 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

largestspotsize|spotdistribution|histcomplex|area|class
---|---|---|---|---
a|c|2|2|h
k|c|2|2|e
k|i|2|2|e
a|i|2|2|f
r|o|2|2|h
r|c|2|1|h
k|c|2|1|e
a|c|2|1|e
h|i|2|1|d
x|i|2|1|b
k|i|2|1|d
a|i|2|1|d
s|i|2|1|d
r|i|2|1|d
r|c|1|1|d
a|c|1|1|d
a|o|2|1|d
x|o|2|1|b
r|o|2|1|c
h|o|2|1|d
s|o|2|1|c
h|x|2|1|h
x|i|1|1|b
a|x|2|1|h
r|x|2|1|h
s|x|2|1|h
s|i|1|1|d
a|i|1|1|d
r|i|1|1|d
k|o|1|1|h
x|o|1|1|b
h|o|1|1|d
s|o|1|1|c
a|o|1|1|d
r|o|1|1|c
k|x|1|1|h
r|x|1|1|h
h|x|1|1|h
s|x|1|1|h
a|x|1|1|h

## JRip

Decision list:

rules | predicted class
---|---
(HistComplex = 2) and (SpotDistribution = C)|E (29.0/12.0)
(LargestSpotSize = X)|B (128.0/0.0)
(SpotDistribution = O) and (LargestSpotSize = R)|C (112.0/37.0)
(SpotDistribution = O) and (LargestSpotSize = S)|C (129.0/54.0)
(SpotDistribution = I) and (Evolution = 3)|D (105.0/37.0)
(LargestSpotSize = A) and (SpotDistribution = O) and (Evolution = 3)|D (27.0/11.0)
|H (426.0/128.0)


## PART

Decision list:

rules | predicted class
---|---
SpotDistribution = X|H (298.0)
LargestSpotSize = X|B (128.0)
Area != 1 AND Prev24Hour = 1|F (15.0/7.0)
SpotDistribution != C AND SpotDistribution = O AND LargestSpotSize != H AND LargestSpotSize != A AND C-class != 1 AND C-class = 0 AND HistComplex = 1|C (152.0/44.0)
Area = 1 AND SpotDistribution = O AND LargestSpotSize != H AND Evolution != 1 AND LargestSpotSize != A AND M-class = 0 AND C-class = 1 AND Activity = 1 AND HistComplex = 1|D (12.0/4.0)
Area = 1 AND SpotDistribution = O AND LargestSpotSize != H AND Prev24Hour = 1 AND Activity = 1 AND LargestSpotSize != R AND Evolution != 1 AND C-class = 0 AND LargestSpotSize != A|C (26.0/12.0)
Area = 1 AND LargestSpotSize = R AND Activity = 1 AND Evolution != 3|C (20.0/6.0)
Area = 1 AND HistComplex = 1 AND Evolution = 3|D (71.0/25.0)
Area = 1 AND SpotDistribution != O AND LargestSpotSize = R|D (10.0/2.0)
Area != 1|E (9.0/1.0)
SpotDistribution != O AND M-class != 0 AND LargestSpotSize = A|D (6.0/1.0)
SpotDistribution != O AND C-class != 4 AND HistComplex != 1 AND Evolution = 3 AND LargestSpotSize != K AND LargestSpotSize != S AND Activity = 1|D (20.0/9.0)
SpotDistribution != O AND C-class != 4 AND HistComplex != 1 AND SpotDistribution = I AND LargestSpotSize = K|D (15.0/4.0)
SpotDistribution = O AND LargestSpotSize != H AND Prev24Hour = 1 AND HistComplex = 1|C (11.0/4.0)
C-class != 4 AND SpotDistribution = O AND LargestSpotSize != H AND Evolution != 1 AND Prev24Hour != 1|D (7.0/3.0)
C-class != 4 AND SpotDistribution != O AND C-class != 2 AND HistComplex != 1 AND C-class = 1|D (14.0/8.0)
C-class != 4 AND SpotDistribution != C AND C-class = 2|F (9.0/5.0)
C-class != 4 AND SpotDistribution != C AND Activity = 1 AND LargestSpotSize = H|D (9.0/4.0)
C-class != 4 AND SpotDistribution = C|E (8.0/3.0)
C-class != 4 AND Activity = 1 AND C-class != 0 AND LargestSpotSize = A|E (7.0/2.0)
C-class != 4 AND Activity = 1 AND SpotDistribution = O AND Evolution != 1 AND LargestSpotSize = A AND Evolution = 2|C (10.0/4.0)
C-class != 4 AND Activity = 1|D (54.0/23.0)
C-class != 4 AND SpotDistribution = O AND LargestSpotSize != S|E (8.0)
Evolution != 2|D (17.0/8.0)
LargestSpotSize != S|F (15.0/8.0)
|C (5.0/3.0)


## J48 Decision Tree

* SpotDistribution = X: H (298.0)
* SpotDistribution = O
	* LargestSpotSize = A
		* C-class = 0
			* Evolution = 1: D (3.0/1.0)
			* Evolution = 2: C (18.0/9.0)
			* Evolution = 3
				* HistComplex = 1: D (11.0/5.0)
				* HistComplex = 2: D (11.0/5.0)
		* C-class = 1: D (9.0/5.0)
		* C-class = 2: D (3.0/1.0)
		* C-class = 3: E (1.0)
		* C-class = 4: D (0.0)
		* C-class = 5: D (0.0)
		* C-class = 6: D (0.0)
		* C-class = 7: D (0.0)
		* C-class = 8: D (0.0)
	* LargestSpotSize = R
		* HistComplex = 1
			* Evolution = 1: C (4.0/1.0)
			* Evolution = 2: C (30.0/8.0)
			* Evolution = 3: C (62.0/22.0)
		* HistComplex = 2: C (16.0/6.0)
	* LargestSpotSize = S
		* C-class = 0
			* HistComplex = 1
				* Activity = 1
					* Evolution = 1: D (2.0/1.0)
					* Evolution = 2: C (19.0/4.0)
					* Evolution = 3: C (32.0/11.0)
				* Activity = 2: C (11.0/2.0)
			* HistComplex = 2
				* Evolution = 1: D (6.0/3.0)
				* Evolution = 2: C (22.0/10.0)
				* Evolution = 3: D (10.0/5.0)
		* C-class = 1
			* Evolution = 1: D (0.0)
			* Evolution = 2: D (8.0/4.0)
			* Evolution = 3: D (9.0/4.0)
		* C-class = 2: D (4.0/2.0)
		* C-class = 3: D (4.0/2.0)
		* C-class = 4: C (0.0)
		* C-class = 5: E (1.0)
		* C-class = 6: E (1.0)
		* C-class = 7: C (0.0)
		* C-class = 8: C (0.0)
	* LargestSpotSize = X: B (115.0)
	* LargestSpotSize = K: C (1.0)
	* LargestSpotSize = H: D (15.0/9.0)
* SpotDistribution = I
	* LargestSpotSize = A
		* HistComplex = 1: D (22.0/3.0)
		* HistComplex = 2
			* Evolution = 1: D (2.0/1.0)
			* Evolution = 2
				* C-class = 0
					* Activity = 1: D (17.0/9.0)
					* Activity = 2: D (9.0/5.0)
				* C-class = 1: D (9.0/5.0)
				* C-class = 2: F (3.0/1.0)
				* C-class = 3: E (3.0/1.0)
				* C-class = 4: D (2.0/1.0)
				* C-class = 5: D (0.0)
				* C-class = 6: D (0.0)
				* C-class = 7: D (0.0)
				* C-class = 8: D (0.0)
			* Evolution = 3
				* Activity = 1: D (19.0/6.0)
				* Activity = 2: E (14.0/8.0)
	* LargestSpotSize = R
		* HistComplex = 1: D (11.0/5.0)
		* HistComplex = 2: D (13.0/4.0)
	* LargestSpotSize = S
		* HistComplex = 1: D (16.0/7.0)
		* HistComplex = 2
			* Evolution = 1: D (1.0)
			* Evolution = 2: E (10.0/6.0)
			* Evolution = 3: D (9.0/5.0)
	* LargestSpotSize = X: B (13.0)
	* LargestSpotSize = K
		* Evolution = 1: D (0.0)
		* Evolution = 2: D (10.0/6.0)
		* Evolution = 3: D (11.0/3.0)
	* LargestSpotSize = H: E (3.0/1.0)
* SpotDistribution = C
	* LargestSpotSize = A: E (11.0/6.0)
	* LargestSpotSize = R: D (3.0/1.0)
	* LargestSpotSize = S: E (0.0)
	* LargestSpotSize = X: E (0.0)
	* LargestSpotSize = K
		* Evolution = 1: E (0.0)
		* Evolution = 2: E (8.0/2.0)
		* Evolution = 3: E (11.0/4.0)
	* LargestSpotSize = H: E (0.0)


