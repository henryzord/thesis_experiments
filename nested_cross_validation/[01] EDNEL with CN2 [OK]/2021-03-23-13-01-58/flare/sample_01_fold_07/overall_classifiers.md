# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = X | H | 0.311390 |
| LargestSpotSize = X and SpotDistribution = O and BecomeHist = 2 and Area = 1 | B | 0.123012 |
| LargestSpotSize = R and SpotDistribution = O and BecomeHist = 2 and Area = 1 | C | 0.067504 |
| LargestSpotSize = A and SpotDistribution = I and BecomeHist = 2 and Area = 1 | D | 0.042455 |
| LargestSpotSize = S and SpotDistribution = O and BecomeHist = 2 and Area = 1 | C | 0.052020 |
| SpotDistribution = I and LargestSpotSize = R | D | 0.016571 |
| LargestSpotSize = A and SpotDistribution = O and BecomeHist = 2 and Area = 1 | D | 0.014249 |
| LargestSpotSize = K and SpotDistribution = I and BecomeHist = 2 and Area = 1 | D | 0.012783 |
| SpotDistribution = I and LargestSpotSize = X | B | 0.014303 |
| LargestSpotSize = S and SpotDistribution = I and BecomeHist = 2 and Area = 1 | D | 0.009817 |
| SpotDistribution = C and LargestSpotSize = K | E | 0.008116 |
| SpotDistribution = O and LargestSpotSize = S and C-class = 0 and HistComplex = 2 and Evolution = 3 | D | 0.004839 |
| SpotDistribution = O and LargestSpotSize = A and C-class = 0 and Activity = 1 and Evolution = 2 | C | 0.004908 |
| SpotDistribution = O and LargestSpotSize = S and C-class = 1 and Evolution = 3 | D | 0.003076 |
| SpotDistribution = O and LargestSpotSize = R and C-class = 1 | D | 0.003076 |
| SpotDistribution = I and LargestSpotSize = S and HistComplex = 2 and Evolution = 2 | E | 0.003440 |
| SpotDistribution = I and LargestSpotSize = A and Evolution = 2 and C-class = 0 and Activity = 2 | F | 0.001939 |
| SpotDistribution = O and LargestSpotSize = S and C-class = 3 | D | 0.001348 |
| LargestSpotSize = A and SpotDistribution = C and BecomeHist = 2 and Area = 1 | E | 0.002294 |
| SpotDistribution = O and LargestSpotSize = A and C-class = 4 | E | 0.002288 |
| LargestSpotSize = H and SpotDistribution = O and BecomeHist = 2 and Area = 1 | D | 0.002420 |
| SpotDistribution = O and LargestSpotSize = S and C-class = 0 and HistComplex = 2 and Evolution = 1 | D | 0.002022 |
| SpotDistribution = O and LargestSpotSize = H and Evolution = 2 | E | 0.001476 |
| SpotDistribution = I and LargestSpotSize = A and Evolution = 2 and C-class = 2 | F | 0.001451 |
| LargestSpotSize = A and SpotDistribution = I and BecomeHist = 2 and Area = 2 | F | 0.002174 |
| LargestSpotSize = K and SpotDistribution = I and BecomeHist = 2 and Area = 2 | E | 0.001720 |
| LargestSpotSize = R and SpotDistribution = C and BecomeHist = 2 and Area = 1 | D | 0.001795 |
| SpotDistribution = I and LargestSpotSize = A and Evolution = 2 and C-class = 3 | E | 0.001527 |
| SpotDistribution = I and LargestSpotSize = H | E | 0.001527 |
| SpotDistribution = O and LargestSpotSize = S and C-class = 5 | E | 0.001145 |
| SpotDistribution = I and LargestSpotSize = A and Evolution = 2 and C-class = 8 | E | 0.001145 |
| SpotDistribution = O and LargestSpotSize = A and C-class = 3 | E | 0.001145 |
| SpotDistribution = C and LargestSpotSize = H | E | 0.001145 |
| SpotDistribution = I and LargestSpotSize = A and Evolution = 3 and M-class = 4 | E | 0.001145 |
| SpotDistribution = O and LargestSpotSize = S and C-class = 6 | E | 0.001145 |
| SpotDistribution = O and LargestSpotSize = K | C | 0.001302 |
| SpotDistribution = I and LargestSpotSize = A and Evolution = 1 | F | 0.001088 |
| SpotDistribution = O and LargestSpotSize = S and C-class = 2 | D | 0.000450 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = X | H | 0.311390 |
| LargestSpotSize = X | B | 0.194825 |
| Area != 1 and Prev24Hour = 1 and X-class = 0 and LargestSpotSize != A | E | 0.007322 |
| SpotDistribution = O and LargestSpotSize != A and LargestSpotSize != H and HistComplex = 1 and LargestSpotSize != S and M-class = 0 and C-class != 1 | C | 0.130502 |
| Area = 1 and SpotDistribution = O and C-class != 4 and LargestSpotSize = A and C-class != 2 and HistComplex = 1 | D | 0.025888 |
| SpotDistribution = C | E | 0.019673 |
| SpotDistribution = O and LargestSpotSize = A and C-class != 4 and Prev24Hour = 1 and Activity = 1 and C-class = 0 and Evolution != 1 and Evolution != 2 | D | 0.008509 |
| SpotDistribution = O and LargestSpotSize = A and Prev24Hour = 1 and Activity = 1 and M-class = 0 and C-class != 0 | D | 0.004425 |
| SpotDistribution = O and LargestSpotSize = A and Evolution != 1 and Prev24Hour = 1 and Activity = 1 and M-class = 0 | C | 0.028926 |
| SpotDistribution = O and LargestSpotSize != A and Evolution != 1 and LargestSpotSize != H | C | 0.134660 |
| HistComplex = 1 | D | 0.332195 |
| Area = 1 and LargestSpotSize != R and LargestSpotSize = K | D | 0.063830 |
| Area = 1 and LargestSpotSize = R | D | 0.070836 |
| Area = 1 and Prev24Hour = 3 | D | 0.030247 |
| Area = 1 and C-class = 2 | F | 0.008081 |
| Area = 1 and M-class = 1 and C-class = 0 | D | 0.024242 |
| Area = 1 and M-class != 1 and Activity = 1 and C-class != 3 and LargestSpotSize != H and Evolution != 2 | D | 0.078650 |
| Area = 1 and M-class != 1 and LargestSpotSize != S and C-class != 0 and LargestSpotSize = A | D | 0.026123 |
| Area = 1 and M-class != 1 and C-class != 3 and Activity = 1 and LargestSpotSize != S | D | 0.030727 |
| Area = 1 and SpotDistribution != O and LargestSpotSize != A | E | 0.056333 |
| SpotDistribution = O | E | 0.167660 |
| Evolution = 2 | F | 0.142780 |
|  | D | 0.284091 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

largestspotsize|spotdistribution|becomehist|area|class
---|---|---|---|---
a|c|2|2|h
k|c|2|2|e
a|i|2|2|f
k|i|2|2|e
h|c|2|1|h
k|c|2|1|e
a|c|2|1|e
r|c|2|1|d
h|i|2|1|e
x|i|2|1|b
k|i|2|1|d
s|i|2|1|d
r|i|2|1|d
a|i|2|1|d
k|o|2|1|h
x|o|2|1|b
h|o|2|1|d
r|o|2|1|c
s|o|2|1|c
a|o|2|1|d
h|x|2|1|h
s|x|2|1|h
r|x|2|1|h
a|x|2|1|h
h|x|1|1|h
k|x|1|1|h
r|x|1|1|h
a|x|1|1|h
s|x|1|1|h

## PART

Decision list:

rules | predicted class
---|---
SpotDistribution = X|H (256.0)
LargestSpotSize = X|B (109.0)
Area != 1 AND Prev24Hour = 1 AND X-class = 0 AND LargestSpotSize != A|E (10.0/5.0)
SpotDistribution = O AND LargestSpotSize != A AND LargestSpotSize != H AND HistComplex = 1 AND LargestSpotSize != S AND M-class = 0 AND C-class != 1|C (75.0/20.0)
Area = 1 AND SpotDistribution = O AND C-class != 4 AND LargestSpotSize = A AND C-class != 2 AND HistComplex = 1|D (17.0/8.0)
SpotDistribution = C|E (23.0/10.0)
SpotDistribution = O AND LargestSpotSize = A AND C-class != 4 AND Prev24Hour = 1 AND Activity = 1 AND C-class = 0 AND Evolution != 1 AND Evolution != 2|D (9.0/4.0)
SpotDistribution = O AND LargestSpotSize = A AND Prev24Hour = 1 AND Activity = 1 AND M-class = 0 AND C-class != 0|D (6.0/3.0)
SpotDistribution = O AND LargestSpotSize = A AND Evolution != 1 AND Prev24Hour = 1 AND Activity = 1 AND M-class = 0|C (4.0/2.0)
SpotDistribution = O AND LargestSpotSize != A AND Evolution != 1 AND LargestSpotSize != H|C (123.0/50.0)
HistComplex = 1|D (53.0/19.0)
Area = 1 AND LargestSpotSize != R AND LargestSpotSize = K|D (14.0/3.0)
Area = 1 AND LargestSpotSize = R|D (12.0/4.0)
Area = 1 AND Prev24Hour = 3|D (7.0/2.0)
Area = 1 AND C-class = 2|F (4.0/1.0)
Area = 1 AND M-class = 1 AND C-class = 0|D (4.0/1.0)
Area = 1 AND M-class != 1 AND Activity = 1 AND C-class != 3 AND LargestSpotSize != H AND Evolution != 2|D (27.0/10.0)
Area = 1 AND M-class != 1 AND LargestSpotSize != S AND C-class != 0 AND LargestSpotSize = A|D (19.0/10.0)
Area = 1 AND M-class != 1 AND C-class != 3 AND Activity = 1 AND LargestSpotSize != S|D (18.0/8.0)
Area = 1 AND SpotDistribution != O AND LargestSpotSize != A|E (16.0/6.0)
SpotDistribution = O|E (6.0)
Evolution = 2|F (5.0/1.0)
|D (4.0/3.0)


## J48 Decision Tree

* SpotDistribution = X: H (298.0)
* SpotDistribution = O
	* LargestSpotSize = A
		* C-class = 0
			* Activity = 1
				* Evolution = 1: D (3.0/1.0)
				* Evolution = 2: C (13.0/6.0)
				* Evolution = 3: D (16.0/8.0)
			* Activity = 2: D (8.0/4.0)
		* C-class = 1: D (9.0/5.0)
		* C-class = 2: D (3.0/1.0)
		* C-class = 3: E (1.0)
		* C-class = 4: E (2.0)
		* C-class = 5: D (0.0)
		* C-class = 6: D (0.0)
		* C-class = 7: D (0.0)
		* C-class = 8: D (0.0)
	* LargestSpotSize = R
		* C-class = 0: C (105.0/31.0)
		* C-class = 1: D (7.0/3.0)
		* C-class = 2: C (0.0)
		* C-class = 3: C (1.0)
		* C-class = 4: C (0.0)
		* C-class = 5: C (1.0)
		* C-class = 6: C (0.0)
		* C-class = 7: C (0.0)
		* C-class = 8: C (0.0)
	* LargestSpotSize = S
		* C-class = 0
			* HistComplex = 1: C (68.0/22.0)
			* HistComplex = 2
				* Evolution = 1: D (6.0/3.0)
				* Evolution = 2: C (22.0/11.0)
				* Evolution = 3: D (10.0/4.0)
		* C-class = 1
			* Evolution = 1: D (0.0)
			* Evolution = 2: C (9.0/4.0)
			* Evolution = 3: D (7.0/3.0)
		* C-class = 2: D (3.0/2.0)
		* C-class = 3: D (4.0/2.0)
		* C-class = 4: C (0.0)
		* C-class = 5: E (1.0)
		* C-class = 6: E (1.0)
		* C-class = 7: C (0.0)
		* C-class = 8: C (0.0)
	* LargestSpotSize = X: B (116.0)
	* LargestSpotSize = K: C (1.0)
	* LargestSpotSize = H
		* Evolution = 1: D (0.0)
		* Evolution = 2: E (7.0/4.0)
		* Evolution = 3: D (7.0/4.0)
* SpotDistribution = I
	* LargestSpotSize = A
		* Evolution = 1: F (1.0)
		* Evolution = 2
			* C-class = 0
				* Activity = 1: D (17.0/7.0)
				* Activity = 2: F (9.0/5.0)
			* C-class = 1: D (9.0/4.0)
			* C-class = 2: F (3.0/1.0)
			* C-class = 3: E (3.0/1.0)
			* C-class = 4: D (2.0/1.0)
			* C-class = 5: D (0.0)
			* C-class = 6: D (0.0)
			* C-class = 7: D (0.0)
			* C-class = 8: E (1.0)
		* Evolution = 3
			* M-class = 0: D (43.0/14.0)
			* M-class = 1: D (6.0/1.0)
			* M-class = 2: D (1.0)
			* M-class = 3: D (0.0)
			* M-class = 4: E (1.0)
			* M-class = 5: D (0.0)
	* LargestSpotSize = R: D (26.0/8.0)
	* LargestSpotSize = S
		* HistComplex = 1: D (16.0/8.0)
		* HistComplex = 2
			* Evolution = 1: D (1.0)
			* Evolution = 2: E (12.0/6.0)
			* Evolution = 3: D (11.0/6.0)
	* LargestSpotSize = X: B (12.0)
	* LargestSpotSize = K
		* Area = 1: D (15.0/3.0)
		* Area = 2: E (6.0/3.0)
	* LargestSpotSize = H: E (3.0/1.0)
* SpotDistribution = C
	* LargestSpotSize = A: E (9.0/5.0)
	* LargestSpotSize = R: D (3.0/1.0)
	* LargestSpotSize = S: E (0.0)
	* LargestSpotSize = X: E (0.0)
	* LargestSpotSize = K: E (17.0/6.0)
	* LargestSpotSize = H: E (1.0)


