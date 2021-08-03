# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | H | 0.309549 |
| LargestSpotSize = X and SpotDistribution = O and BecomeHist = 2 and Area = 1 and X-class = 0 | B | 0.122601 |
| LargestSpotSize = R and SpotDistribution = O and BecomeHist = 2 and Area = 1 and X-class = 0 | C | 0.062622 |
| LargestSpotSize = A and SpotDistribution = I and BecomeHist = 2 and Area = 1 and X-class = 0 | D | 0.045405 |
| LargestSpotSize = S and SpotDistribution = O and BecomeHist = 2 and Area = 1 and X-class = 0 | C | 0.053590 |
| LargestSpotSize = R and SpotDistribution = I and BecomeHist = 2 and Area = 1 and X-class = 0 | D | 0.014900 |
| LargestSpotSize = A and SpotDistribution = O and BecomeHist = 2 and Area = 1 and X-class = 0 | D | 0.013654 |
| LargestSpotSize = X and SpotDistribution = I and BecomeHist = 2 and Area = 1 and X-class = 0 | B | 0.016726 |
| LargestSpotSize = S and SpotDistribution = I and BecomeHist = 2 and Area = 1 and X-class = 0 | D | 0.011303 |
| LargestSpotSize = K and SpotDistribution = I and BecomeHist = 2 and Area = 1 and X-class = 0 | D | 0.010828 |
| LargestSpotSize = K and SpotDistribution = C and BecomeHist = 2 and Area = 2 and X-class = 0 | E | 0.006116 |
| LargestSpotSize = H and SpotDistribution = O and BecomeHist = 2 and Area = 1 and X-class = 0 | D | 0.003494 |
| LargestSpotSize = A and SpotDistribution = C and BecomeHist = 2 and Area = 1 and X-class = 0 | E | 0.002050 |
| LargestSpotSize = K and SpotDistribution = I and BecomeHist = 2 and Area = 2 and X-class = 0 | E | 0.001728 |
| LargestSpotSize = K and SpotDistribution = C and BecomeHist = 2 and Area = 1 and X-class = 0 | E | 0.001534 |
| LargestSpotSize = K and SpotDistribution = C and BecomeHist = 2 and Area = 2 and X-class = 1 | E | 0.001534 |
| LargestSpotSize = R and SpotDistribution = C and BecomeHist = 2 and Area = 1 and X-class = 0 | E | 0.000576 |
| LargestSpotSize = H and SpotDistribution = I and BecomeHist = 2 and Area = 1 and X-class = 0 | D | 0.000452 |

## Ordered rules

### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| HistComplex = 2 and Area = 2 and Prev24Hour = 1 | F | 0.005207 |
| Activity = 2 and SpotDistribution = C | E | 0.011296 |
| HistComplex = 2 and LargestSpotSize = A and C-class = 1 and SpotDistribution = O | E | 0.003712 |
| HistComplex = 2 and SpotDistribution = I and C-class = 3 | E | 0.003230 |
| LargestSpotSize = X | B | 0.140370 |
| SpotDistribution = O and HistComplex = 1 and C-class = 0 | C | 0.119860 |
| SpotDistribution = O and Evolution = 2 and C-class = 0 | C | 0.019241 |
| SpotDistribution = I | D | 0.132576 |
| SpotDistribution = O | D | 0.140833 |
|  | H | 0.673516 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

largestspotsize|spotdistribution|becomehist|area|x-class|class
---|---|---|---|---|---
k|c|2|2|2|h
k|c|2|2|1|e
a|c|2|2|0|h
k|c|2|2|0|e
a|i|2|1|1|h
a|i|2|2|0|h
k|i|2|2|0|e
r|o|2|2|0|h
h|c|2|1|0|h
k|c|2|1|0|e
r|c|2|1|0|e
a|c|2|1|0|e
h|i|2|1|0|d
s|i|2|1|0|d
k|i|2|1|0|d
r|i|2|1|0|d
a|i|2|1|0|d
x|i|2|1|0|b
k|o|2|1|0|h
h|o|2|1|0|d
a|o|2|1|0|d
r|o|2|1|0|c
s|o|2|1|0|c
x|o|2|1|0|b
h|x|2|1|0|h
s|x|2|1|0|h
r|x|2|1|0|h
a|x|2|1|0|h
k|x|1|1|0|h
r|x|1|1|0|h
a|x|1|1|0|h
h|x|1|1|0|h
s|x|1|1|0|h

## JRip

Decision list:

rules | predicted class
---|---
(HistComplex = 2) and (Area = 2) and (Prev24Hour = 1)|F (17.0/8.0)
(Activity = 2) and (SpotDistribution = C)|E (20.0/7.0)
(HistComplex = 2) and (LargestSpotSize = A) and (C-class = 1) and (SpotDistribution = O)|E (5.0/1.0)
(HistComplex = 2) and (SpotDistribution = I) and (C-class = 3)|E (9.0/4.0)
(LargestSpotSize = X)|B (129.0/0.0)
(SpotDistribution = O) and (HistComplex = 1) and (C-class = 0)|C (172.0/55.0)
(SpotDistribution = O) and (Evolution = 2) and (C-class = 0)|C (46.0/19.0)
(SpotDistribution = I)|D (173.0/71.0)
(SpotDistribution = O)|D (84.0/41.0)
|H (298.0/3.0)


