# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = X | H | 0.311715 |
| LargestSpotSize = X and SpotDistribution = O and Area = 1 | B | 0.122210 |
| SpotDistribution = O and LargestSpotSize!=(X) and SpotDistribution != I and LargestSpotSize != X | D | 0.056753 |
| LargestSpotSize = R and SpotDistribution = O and Area = 1 | C | 0.061868 |
| LargestSpotSize = S and SpotDistribution = O and Area = 1 | C | 0.055406 |
| LargestSpotSize = A and SpotDistribution = I and Area = 1 | D | 0.043683 |
| LargestSpotSize = R and SpotDistribution = I and Area = 1 | D | 0.014840 |
| SpotDistribution = C and LargestSpotSize = K | E | 0.009635 |
| LargestSpotSize = X and SpotDistribution = I and Area = 1 | B | 0.015495 |
| LargestSpotSize = S and SpotDistribution = I and Area = 1 | D | 0.010068 |
| LargestSpotSize = K and SpotDistribution = I and Area = 1 | D | 0.008937 |
| SpotDistribution = O and LargestSpotSize = A and Activity = 2 | E | 0.002870 |
| SpotDistribution = I and LargestSpotSize = A and HistComplex = 2 and Evolution = 3 and Activity = 2 | E | 0.002959 |
| SpotDistribution = I and LargestSpotSize = S and HistComplex = 2 and Activity = 2 | E | 0.002612 |
| LargestSpotSize = H and SpotDistribution = I and Area = 1 | E | 0.002291 |
| SpotDistribution = C and LargestSpotSize = R | D | 0.002692 |
| LargestSpotSize = K and SpotDistribution = I and Area = 2 | F | 0.001634 |
| LargestSpotSize = A and SpotDistribution = C and Area = 1 | D | 0.002402 |
| SpotDistribution = O and LargestSpotSize = S and C-class = 5 | E | 0.001147 |
| SpotDistribution = O and LargestSpotSize = S and C-class = 6 | E | 0.001147 |
| SpotDistribution = C and LargestSpotSize = H | E | 0.001147 |
| SpotDistribution = O and LargestSpotSize = K | C | 0.001304 |

## Ordered rules

### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| HistComplex = 2 and Activity = 2 and SpotDistribution = C | E | 0.009728 |
| LargestSpotSize = X | B | 0.136170 |
| SpotDistribution = O and HistComplex = 1 and Evolution = 2 and LargestSpotSize = S | C | 0.031355 |
| SpotDistribution = O and LargestSpotSize = R and Evolution = 2 and C-class = 0 | C | 0.034249 |
| SpotDistribution = O and HistComplex = 1 and LargestSpotSize = R and C-class = 0 | C | 0.039796 |
| SpotDistribution = O and LargestSpotSize = S and HistComplex = 1 and C-class = 0 | C | 0.019621 |
| SpotDistribution = O and LargestSpotSize = S and Evolution = 2 and C-class = 0 | C | 0.008904 |
| SpotDistribution = O and Activity = 1 and Evolution = 3 and LargestSpotSize = S | C | 0.005106 |
| SpotDistribution = I and Evolution = 3 and HistComplex = 1 and LargestSpotSize = A | D | 0.032413 |
| SpotDistribution = I and Evolution = 3 and C-class = 0 | D | 0.041949 |
| SpotDistribution = O and Evolution = 3 | D | 0.092857 |
|  | H | 0.532143 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

largestspotsize|spotdistribution|area|class
---|---|---|---
a|c|2|h
k|c|2|e
a|i|2|h
k|i|2|f
r|o|2|h
r|c|1|d
k|c|1|e
a|c|1|d
h|c|1|h
h|i|1|e
k|i|1|d
x|i|1|b
s|i|1|d
a|i|1|d
r|i|1|d
k|o|1|h
h|o|1|d
x|o|1|b
a|o|1|d
s|o|1|c
r|o|1|c
k|x|1|h
h|x|1|h
a|x|1|h
r|x|1|h
s|x|1|h

## JRip

Decision list:

rules | predicted class
---|---
(HistComplex = 2) and (Activity = 2) and (SpotDistribution = C)|E (23.0/9.0)
(LargestSpotSize = X)|B (128.0/0.0)
(SpotDistribution = O) and (HistComplex = 1) and (Evolution = 2) and (LargestSpotSize = S)|C (31.0/6.0)
(SpotDistribution = O) and (LargestSpotSize = R) and (Evolution = 2) and (C-class = 0)|C (33.0/6.0)
(SpotDistribution = O) and (HistComplex = 1) and (LargestSpotSize = R) and (C-class = 0)|C (61.0/20.0)
(SpotDistribution = O) and (LargestSpotSize = S) and (HistComplex = 1) and (C-class = 0)|C (38.0/15.0)
(SpotDistribution = O) and (LargestSpotSize = S) and (Evolution = 2) and (C-class = 0)|C (21.0/9.0)
(SpotDistribution = O) and (Activity = 1) and (Evolution = 3) and (LargestSpotSize = S)|C (19.0/9.0)
(SpotDistribution = I) and (Evolution = 3) and (HistComplex = 1) and (LargestSpotSize = A)|D (21.0/3.0)
(SpotDistribution = I) and (Evolution = 3) and (C-class = 0)|D (53.0/20.0)
(SpotDistribution = O) and (Evolution = 3)|D (49.0/21.0)
|H (479.0/181.0)


## J48 Decision Tree

* SpotDistribution = X: H (298.0)
* SpotDistribution = O
	* LargestSpotSize = A
		* Activity = 1
			* Evolution = 1: D (3.0/1.0)
			* Evolution = 2: D (18.0/11.0)
			* Evolution = 3
				* HistComplex = 1: D (11.0/5.0)
				* HistComplex = 2: D (12.0/6.0)
		* Activity = 2: E (10.0/5.0)
	* LargestSpotSize = R
		* HistComplex = 1
			* Evolution = 1: C (5.0/1.0)
			* Evolution = 2: C (29.0/7.0)
			* Evolution = 3: C (61.0/22.0)
		* HistComplex = 2: C (13.0/5.0)
	* LargestSpotSize = S
		* C-class = 0
			* HistComplex = 1
				* Evolution = 1: C (3.0/1.0)
				* Evolution = 2: C (26.0/5.0)
				* Evolution = 3: C (35.0/14.0)
			* HistComplex = 2
				* Evolution = 1: D (7.0/4.0)
				* Evolution = 2: C (21.0/9.0)
				* Evolution = 3: D (12.0/6.0)
		* C-class = 1: C (17.0/8.0)
		* C-class = 2: D (2.0/1.0)
		* C-class = 3: D (4.0/2.0)
		* C-class = 4: C (0.0)
		* C-class = 5: E (1.0)
		* C-class = 6: E (1.0)
		* C-class = 7: C (0.0)
		* C-class = 8: C (0.0)
	* LargestSpotSize = X: B (115.0)
	* LargestSpotSize = K: C (1.0)
	* LargestSpotSize = H: D (14.0/8.0)
* SpotDistribution = I
	* LargestSpotSize = A
		* HistComplex = 1: D (26.0/4.0)
		* HistComplex = 2
			* Evolution = 1: D (2.0/1.0)
			* Evolution = 2
				* Activity = 1: D (23.0/14.0)
				* Activity = 2: D (17.0/10.0)
			* Evolution = 3
				* Activity = 1: D (21.0/7.0)
				* Activity = 2: E (14.0/8.0)
	* LargestSpotSize = R
		* HistComplex = 1: D (14.0/6.0)
		* HistComplex = 2: D (12.0/3.0)
	* LargestSpotSize = S
		* HistComplex = 1: D (17.0/8.0)
		* HistComplex = 2
			* Activity = 1: D (11.0/6.0)
			* Activity = 2: E (11.0/6.0)
	* LargestSpotSize = X: B (13.0)
	* LargestSpotSize = K: D (21.0/11.0)
	* LargestSpotSize = H: E (2.0)
* SpotDistribution = C
	* LargestSpotSize = A: D (10.0/6.0)
	* LargestSpotSize = R: D (2.0)
	* LargestSpotSize = S: E (0.0)
	* LargestSpotSize = X: E (0.0)
	* LargestSpotSize = K: E (20.0/7.0)
	* LargestSpotSize = H: E (1.0)


## SimpleCart Decision Tree

		* SpotDistribution=(C)|(I)|(O)
	* LargestSpotSize=(X): B(128.0/0.0)
	* LargestSpotSize!=(X)
			* SpotDistribution=(C)|(I): D(109.0/115.0)
			* SpotDistribution!=(C)|(I)
					* LargestSpotSize=(S)|(R)|(X): C(148.0/89.0)
					* LargestSpotSize!=(S)|(R)|(X): D(31.0/38.0)
		* SpotDistribution!=(C)|(I)|(O): H(298.0/0.0)


