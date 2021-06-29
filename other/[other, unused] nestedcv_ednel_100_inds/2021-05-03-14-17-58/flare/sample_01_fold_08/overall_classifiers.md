# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| LargestSpotSize = S and SpotDistribution = X and Area = 1 and X-class = 0 | H | 0.238150 |
| LargestSpotSize = X and SpotDistribution = O and Area = 1 and X-class = 0 | B | 0.123012 |
| LargestSpotSize = R and SpotDistribution = O and Area = 1 and X-class = 0 | C | 0.063418 |
| LargestSpotSize = R and SpotDistribution = X and Area = 1 and X-class = 0 | H | 0.078322 |
| LargestSpotSize = S and SpotDistribution = O and Area = 1 and X-class = 0 | C | 0.051096 |
| LargestSpotSize = A and SpotDistribution = I and Area = 1 and X-class = 0 | D | 0.038613 |
| LargestSpotSize = A and SpotDistribution = X and Area = 1 and X-class = 0 | H | 0.040757 |
| LargestSpotSize = A and SpotDistribution = O and Area = 1 and X-class = 0 | D | 0.015589 |
| LargestSpotSize = S and SpotDistribution = I and Area = 1 and X-class = 0 | D | 0.012196 |
| LargestSpotSize = K and SpotDistribution = I and Area = 1 and X-class = 0 | D | 0.012519 |
| LargestSpotSize = X and SpotDistribution = I and Area = 1 and X-class = 0 | B | 0.015476 |
| LargestSpotSize = R and SpotDistribution = I and Area = 1 and X-class = 0 | D | 0.011408 |
| LargestSpotSize = K and SpotDistribution = C and Area = 2 and X-class = 0 | E | 0.007688 |
| LargestSpotSize = H and SpotDistribution = X and Area = 1 and X-class = 0 | H | 0.010511 |
| LargestSpotSize = H and SpotDistribution = O and Area = 1 and X-class = 0 | D | 0.003475 |
| LargestSpotSize = A and SpotDistribution = C and Area = 1 and X-class = 0 | D | 0.002399 |
| LargestSpotSize = A and SpotDistribution = I and Area = 2 and X-class = 0 | F | 0.002174 |
| LargestSpotSize = R and SpotDistribution = C and Area = 1 and X-class = 0 | D | 0.001795 |
| LargestSpotSize = K and SpotDistribution = C and Area = 1 and X-class = 0 | E | 0.001527 |
| LargestSpotSize = K and SpotDistribution = I and Area = 2 and X-class = 0 | E | 0.000918 |
| LargestSpotSize = K and SpotDistribution = X and Area = 1 and X-class = 0 | H | 0.001515 |
| LargestSpotSize = H and SpotDistribution = I and Area = 1 and X-class = 0 | E | 0.000573 |
| LargestSpotSize = K and SpotDistribution = C and Area = 2 and X-class = 1 | F | 0.000545 |

## Ordered rules

### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = I and Evolution = 2 | F | 0.006194 |
| Activity = 2 and SpotDistribution = C | E | 0.010939 |
| LargestSpotSize = A and Activity = 2 and HistComplex = 2 | E | 0.006068 |
| LargestSpotSize = X | B | 0.142227 |
| SpotDistribution = O and HistComplex = 1 and Evolution = 2 | C | 0.061864 |
| SpotDistribution = O and LargestSpotSize = R | C | 0.048546 |
| SpotDistribution = O and LargestSpotSize = S and HistComplex = 1 and C-class = 0 | C | 0.019941 |
| SpotDistribution = O and C-class = 0 and Evolution = 2 | C | 0.010335 |
| SpotDistribution = O and Evolution = 3 and LargestSpotSize = S | C | 0.005557 |
| SpotDistribution = O and Evolution = 3 and Activity = 1 and C-class = 0 | C | 0.003320 |
| SpotDistribution = I and LargestSpotSize = A and HistComplex = 1 | D | 0.038004 |
| SpotDistribution = I and Activity = 2 and Evolution = 3 and Area = 1 | D | 0.028954 |
| SpotDistribution = I and LargestSpotSize = A | D | 0.040717 |
| SpotDistribution = I and Area = 1 | D | 0.038894 |
| SpotDistribution = O | D | 0.174803 |
|  | H | 0.735802 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

largestspotsize|spotdistribution|area|x-class|class
---|---|---|---|---
k|c|2|2|h
k|c|2|1|f
a|i|1|1|h
k|c|2|0|e
a|c|2|0|h
a|i|2|0|f
k|i|2|0|e
r|o|2|0|h
a|c|1|0|d
h|c|1|0|h
k|c|1|0|e
r|c|1|0|d
h|i|1|0|e
s|i|1|0|d
k|i|1|0|d
r|i|1|0|d
a|i|1|0|d
x|i|1|0|b
k|o|1|0|h
h|o|1|0|d
a|o|1|0|d
r|o|1|0|c
s|o|1|0|c
x|o|1|0|b
h|x|1|0|h
a|x|1|0|h
r|x|1|0|h
k|x|1|0|h
s|x|1|0|h

## JRip

Decision list:

rules | predicted class
---|---
(SpotDistribution = I) and (Evolution = 2)|F (81.0/60.0)
(Activity = 2) and (SpotDistribution = C)|E (24.0/9.0)
(LargestSpotSize = A) and (Activity = 2) and (HistComplex = 2)|E (20.0/10.0)
(LargestSpotSize = X)|B (124.0/0.0)
(SpotDistribution = O) and (HistComplex = 1) and (Evolution = 2)|C (73.0/20.0)
(SpotDistribution = O) and (LargestSpotSize = R)|C (81.0/30.0)
(SpotDistribution = O) and (LargestSpotSize = S) and (HistComplex = 1) and (C-class = 0)|C (36.0/14.0)
(SpotDistribution = O) and (C-class = 0) and (Evolution = 2)|C (34.0/17.0)
(SpotDistribution = O) and (Evolution = 3) and (LargestSpotSize = S)|C (25.0/14.0)
(SpotDistribution = O) and (Evolution = 3) and (Activity = 1) and (C-class = 0)|C (28.0/17.0)
(SpotDistribution = I) and (LargestSpotSize = A) and (HistComplex = 1)|D (19.0/3.0)
(SpotDistribution = I) and (Activity = 2) and (Evolution = 3) and (Area = 1)|D (12.0/1.0)
(SpotDistribution = I) and (LargestSpotSize = A)|D (18.0/6.0)
(SpotDistribution = I) and (Area = 1)|D (43.0/18.0)
(SpotDistribution = O)|D (30.0/16.0)
|H (309.0/11.0)


