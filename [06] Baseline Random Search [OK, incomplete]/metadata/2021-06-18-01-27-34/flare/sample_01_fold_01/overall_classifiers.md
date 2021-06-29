# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = X | H | 0.310669 |
| SpotDistribution = O and LargestSpotSize = X | B | 0.121277 |
| SpotDistribution = O and LargestSpotSize = R and C-class = 0 | C | 0.061255 |
| SpotDistribution = I and LargestSpotSize = A | D | 0.044497 |
| SpotDistribution = O and LargestSpotSize = S | C | 0.053035 |
| SpotDistribution = O and LargestSpotSize = A | D | 0.014532 |
| SpotDistribution = I and LargestSpotSize = R | D | 0.014860 |
| SpotDistribution = I and LargestSpotSize = X | B | 0.016667 |
| SpotDistribution = I and LargestSpotSize = S | D | 0.011272 |
| SpotDistribution = C | E | 0.011571 |
| SpotDistribution = I and LargestSpotSize = K | D | 0.007776 |
| SpotDistribution = O and LargestSpotSize = R and C-class = 1 | D | 0.004807 |
| SpotDistribution = O and LargestSpotSize = H | D | 0.003484 |
| SpotDistribution = I and LargestSpotSize = H | E | 0.001529 |
| LargestSpotSize = A and SpotDistribution = C and HistComplex = 1 and X-class = 0 | D | 0.000676 |
| LargestSpotSize = H and SpotDistribution = I and HistComplex = 2 and X-class = 0 | D | 0.000451 |
| SpotDistribution = O and LargestSpotSize = K | C | 0.001302 |
| SpotDistribution = O and LargestSpotSize = R and C-class = 3 | C | 0.001302 |
| LargestSpotSize = R and SpotDistribution = O and HistComplex = 1 and X-class = 0 | C | 0.055994 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = X | H | 0.310669 |
| LargestSpotSize = X | B | 0.194825 |
| Area != 1 and Prev24Hour = 1 | F | 0.009665 |
| SpotDistribution = C | E | 0.026906 |
| SpotDistribution = O and LargestSpotSize != H and HistComplex = 1 and C-class != 2 and C-class = 1 and LargestSpotSize != R and Evolution != 2 | D | 0.013746 |
| SpotDistribution = O and LargestSpotSize != H and HistComplex = 1 and C-class != 2 and LargestSpotSize != S and C-class != 1 | C | 0.137845 |
| SpotDistribution = O and LargestSpotSize != H and Evolution != 1 and C-class != 2 and LargestSpotSize != A and C-class != 1 and HistComplex = 1 | C | 0.072249 |
| SpotDistribution != O and LargestSpotSize = R | D | 0.066298 |
| SpotDistribution != O and M-class = 0 and Evolution = 3 and LargestSpotSize != K and C-class != 2 and LargestSpotSize != S and HistComplex = 1 | D | 0.052160 |
| SpotDistribution != O and M-class = 0 and C-class != 3 and HistComplex = 1 | D | 0.037412 |
| SpotDistribution != O and M-class = 0 and C-class != 3 and Evolution = 3 and LargestSpotSize != S and LargestSpotSize = A and C-class = 0 | D | 0.034770 |
| SpotDistribution != O and M-class = 0 and C-class != 3 and Evolution = 3 and LargestSpotSize != A | D | 0.031038 |
| M-class = 0 and SpotDistribution = O and LargestSpotSize != H and C-class != 2 and Evolution != 1 and Evolution = 2 and LargestSpotSize != A and Activity = 1 and C-class = 0 | C | 0.036421 |
| M-class = 0 and SpotDistribution = O and LargestSpotSize != H and Evolution != 1 and C-class != 2 and Prev24Hour = 1 and Evolution != 2 | D | 0.183879 |
| M-class = 0 and C-class != 3 and HistComplex != 1 and Prev24Hour != 3 and C-class != 2 and C-class != 0 and SpotDistribution != O | D | 0.026164 |
| M-class = 0 and C-class != 3 and HistComplex != 1 and C-class != 1 | D | 0.137195 |
| M-class != 0 | D | 0.066803 |
| C-class != 0 and LargestSpotSize != H and C-class = 3 | E | 0.020851 |
| HistComplex = 1 | C | 0.090566 |
|  | E | 0.418919 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = I and Evolution = 2 and C-class = 1 and Area = 2 | F | 0.002176 |
| HistComplex = 2 and SpotDistribution = I and Evolution = 2 and C-class = 4 | F | 0.001452 |
| HistComplex = 2 and SpotDistribution = I and Evolution = 2 and C-class = 1 | F | 0.001827 |
| HistComplex = 2 and Area = 2 and Prev24Hour = 1 and C-class = 0 and SpotDistribution = C and Activity = 1 | F | 0.002176 |
| Activity = 2 and Area = 2 and Prev24Hour = 1 and M-class = 0 and SpotDistribution = C | F | 0.002448 |
| SpotDistribution = I and HistComplex = 2 and Evolution = 2 and Activity = 2 and LargestSpotSize = A | F | 0.001715 |
| SpotDistribution = I and HistComplex = 2 and LargestSpotSize = S and C-class = 2 | F | 0.002176 |
| HistComplex = 2 and SpotDistribution = I and Area = 2 | F | 0.000873 |
| HistComplex = 2 and C-class = 1 and SpotDistribution = C and X-class = 0 | F | 0.002176 |
| HistComplex = 2 and Activity = 2 and SpotDistribution = C and Area = 2 and X-class = 0 | E | 0.008206 |
| HistComplex = 2 and Activity = 2 and SpotDistribution = C and X-class = 1 | E | 0.002358 |
| HistComplex = 2 and Activity = 2 and LargestSpotSize = A and C-class = 1 | E | 0.001773 |
| HistComplex = 2 and Activity = 2 and LargestSpotSize = H and SpotDistribution = O | E | 0.003534 |
| HistComplex = 2 and LargestSpotSize = A and Activity = 2 and SpotDistribution = C | E | 0.002125 |
| HistComplex = 2 and SpotDistribution = I and LargestSpotSize = S and Evolution = 2 | E | 0.003546 |
| LargestSpotSize = A and HistComplex = 2 and C-class = 1 and Evolution = 2 | E | 0.002104 |
| HistComplex = 2 and SpotDistribution = I and LargestSpotSize = A and C-class = 3 | E | 0.002125 |
| HistComplex = 2 and SpotDistribution = I and LargestSpotSize = A | E | 0.004013 |
| Activity = 2 and SpotDistribution = C and C-class = 0 | E | 0.002125 |
| HistComplex = 2 and M-class = 1 and LargestSpotSize = K | E | 0.002358 |
| Activity = 2 and LargestSpotSize = A and Prev24Hour = 1 and Evolution = 2 | E | 0.000528 |
| HistComplex = 2 and M-class = 1 and LargestSpotSize = A and SpotDistribution = O | E | 0.002358 |
| LargestSpotSize = X | B | 0.146286 |
| SpotDistribution = O and HistComplex = 1 and C-class = 0 and Evolution = 2 and LargestSpotSize = R and Activity = 2 | C | 0.003559 |
| SpotDistribution = O and HistComplex = 1 and C-class = 0 and Evolution = 2 and LargestSpotSize = R | C | 0.029025 |
| SpotDistribution = O and HistComplex = 1 and C-class = 0 and LargestSpotSize = S and Evolution = 2 and Prev24Hour = 2 | C | 0.003559 |
| SpotDistribution = O and HistComplex = 1 and C-class = 0 and LargestSpotSize = S and Evolution = 2 and Activity = 1 | C | 0.018130 |
| SpotDistribution = O and HistComplex = 1 and C-class = 0 and Evolution = 1 and LargestSpotSize = S | C | 0.003559 |
| SpotDistribution = O and HistComplex = 1 and C-class = 0 and LargestSpotSize = R and Evolution = 1 | C | 0.005684 |
| SpotDistribution = O and HistComplex = 1 and C-class = 0 and LargestSpotSize = R and M-class = 0 | C | 0.034434 |
| SpotDistribution = O and C-class = 0 and Evolution = 2 and LargestSpotSize = R and Activity = 1 | C | 0.006735 |
| SpotDistribution = O and LargestSpotSize = S and C-class = 0 and HistComplex = 1 and Activity = 2 and Prev24Hour = 1 and Evolution = 3 | C | 0.003559 |
| SpotDistribution = O and LargestSpotSize = S and C-class = 0 and HistComplex = 1 and M-class = 1 | C | 0.003559 |
| SpotDistribution = O and LargestSpotSize = S and C-class = 0 and HistComplex = 1 and Evolution = 2 | C | 0.003734 |
| SpotDistribution = O and LargestSpotSize = S and C-class = 0 and HistComplex = 1 and Activity = 1 | C | 0.018320 |
| SpotDistribution = O and Evolution = 2 and C-class = 0 and LargestSpotSize = S and Activity = 2 | C | 0.001786 |
| SpotDistribution = O and Evolution = 2 and LargestSpotSize = A | C | 0.008493 |
| SpotDistribution = O and Evolution = 2 and LargestSpotSize = S and C-class = 0 | C | 0.008075 |
| SpotDistribution = O and HistComplex = 1 and C-class = 3 | C | 0.002377 |
| SpotDistribution = O and HistComplex = 1 and C-class = 0 and Activity = 1 and LargestSpotSize = A | C | 0.004066 |
| SpotDistribution = O and LargestSpotSize = S and C-class = 1 and HistComplex = 1 and Activity = 2 and Prev24Hour = 1 | C | 0.003559 |
| SpotDistribution = O and Evolution = 3 and Activity = 1 and LargestSpotSize = S and HistComplex = 2 | C | 0.004951 |
| SpotDistribution = I and LargestSpotSize = A and Evolution = 2 | D | 0.045040 |
| SpotDistribution = I and LargestSpotSize = A and C-class = 1 | D | 0.015504 |
| SpotDistribution = I and LargestSpotSize = K and Evolution = 3 | D | 0.012727 |
| SpotDistribution = I and C-class = 0 and LargestSpotSize = A and Activity = 2 | D | 0.009301 |
| SpotDistribution = I and C-class = 0 and LargestSpotSize = A | D | 0.031919 |
| SpotDistribution = O and C-class = 1 and LargestSpotSize = A | D | 0.007813 |
| SpotDistribution = O and C-class = 1 and Prev24Hour = 2 | D | 0.005222 |
| SpotDistribution = I and C-class = 0 and HistComplex = 2 and Evolution = 2 | D | 0.013218 |
| SpotDistribution = O and Evolution = 3 and C-class = 2 and LargestSpotSize = S | D | 0.005222 |
| SpotDistribution = O and C-class = 1 and LargestSpotSize = R and Evolution = 2 | D | 0.005222 |
| SpotDistribution = O and Evolution = 3 and Activity = 2 and LargestSpotSize = A and HistComplex = 1 | D | 0.007813 |
| SpotDistribution = I and Evolution = 3 and LargestSpotSize = R and HistComplex = 2 and Activity = 2 | D | 0.005222 |
| SpotDistribution = O and HistComplex = 2 and Activity = 1 and Evolution = 2 and LargestSpotSize = S | D | 0.018978 |
| SpotDistribution = I and C-class = 0 and Evolution = 3 and LargestSpotSize = R and HistComplex = 2 | D | 0.005875 |
| SpotDistribution = O and Evolution = 3 and C-class = 1 | D | 0.011600 |
| SpotDistribution = I and C-class = 0 and Evolution = 3 | D | 0.019685 |
| SpotDistribution = O and C-class = 0 and Activity = 1 and HistComplex = 2 and LargestSpotSize = H | D | 0.009301 |
| SpotDistribution = O and C-class = 0 and Activity = 1 and LargestSpotSize = A and Evolution = 1 | D | 0.005222 |
| SpotDistribution = O and C-class = 0 and Evolution = 3 and LargestSpotSize = R and Area = 1 and HistComplex = 2 | D | 0.005222 |
| SpotDistribution = O and C-class = 0 and Evolution = 3 and LargestSpotSize = S and Prev24Hour = 1 | D | 0.027849 |
| SpotDistribution = I and Activity = 2 and C-class = 3 | D | 0.007813 |
| SpotDistribution = O and C-class = 0 and Activity = 1 and LargestSpotSize = A | D | 0.022925 |
|  | H | 0.671946 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

largestspotsize|spotdistribution|histcomplex|x-class|class
---|---|---|---|---
k|c|2|2|h
k|c|2|1|e
a|i|2|1|h
k|c|2|0|e
h|c|2|0|h
a|c|2|0|e
h|i|2|0|d
k|i|2|0|d
x|i|2|0|b
a|i|2|0|d
s|i|2|0|d
r|i|2|0|d
r|c|1|0|e
a|c|1|0|d
x|o|2|0|b
a|o|2|0|d
r|o|2|0|c
h|o|2|0|d
s|o|2|0|c
h|x|2|0|h
s|i|1|0|d
x|i|1|0|b
a|x|2|0|h
s|x|2|0|h
r|x|2|0|h
r|i|1|0|d
a|i|1|0|d
k|o|1|0|h
h|o|1|0|d
x|o|1|0|b
a|o|1|0|d
r|o|1|0|c
s|o|1|0|c
k|x|1|0|h
a|x|1|0|h
r|x|1|0|h
h|x|1|0|h
s|x|1|0|h

## JRip

Decision list:

rules | predicted class
---|---
(SpotDistribution = I) and (Evolution = 2) and (C-class = 1) and (Area = 2)|F (2.0/0.0)
(HistComplex = 2) and (SpotDistribution = I) and (Evolution = 2) and (C-class = 4)|F (3.0/1.0)
(HistComplex = 2) and (SpotDistribution = I) and (Evolution = 2) and (C-class = 1)|F (15.0/10.0)
(HistComplex = 2) and (Area = 2) and (Prev24Hour = 1) and (C-class = 0) and (SpotDistribution = C) and (Activity = 1)|F (2.0/0.0)
(Activity = 2) and (Area = 2) and (Prev24Hour = 1) and (M-class = 0) and (SpotDistribution = C)|F (4.0/1.0)
(SpotDistribution = I) and (HistComplex = 2) and (Evolution = 2) and (Activity = 2) and (LargestSpotSize = A)|F (13.0/8.0)
(SpotDistribution = I) and (HistComplex = 2) and (LargestSpotSize = S) and (C-class = 2)|F (2.0/0.0)
(HistComplex = 2) and (SpotDistribution = I) and (Area = 2)|F (5.0/3.0)
(HistComplex = 2) and (C-class = 1) and (SpotDistribution = C) and (X-class = 0)|F (2.0/0.0)
(HistComplex = 2) and (Activity = 2) and (SpotDistribution = C) and (Area = 2) and (X-class = 0)|E (6.0/0.0)
(HistComplex = 2) and (Activity = 2) and (SpotDistribution = C) and (X-class = 1)|E (2.0/0.0)
(HistComplex = 2) and (Activity = 2) and (LargestSpotSize = A) and (C-class = 1)|E (3.0/0.0)
(HistComplex = 2) and (Activity = 2) and (LargestSpotSize = H) and (SpotDistribution = O)|E (3.0/0.0)
(HistComplex = 2) and (LargestSpotSize = A) and (Activity = 2) and (SpotDistribution = C)|E (5.0/2.0)
(HistComplex = 2) and (SpotDistribution = I) and (LargestSpotSize = S) and (Evolution = 2)|E (11.0/5.0)
(LargestSpotSize = A) and (HistComplex = 2) and (C-class = 1) and (Evolution = 2)|E (3.0/0.0)
(HistComplex = 2) and (SpotDistribution = I) and (LargestSpotSize = A) and (C-class = 3)|E (4.0/2.0)
(HistComplex = 2) and (SpotDistribution = I) and (LargestSpotSize = A)|E (45.0/33.0)
(Activity = 2) and (SpotDistribution = C) and (C-class = 0)|E (3.0/0.0)
(HistComplex = 2) and (M-class = 1) and (LargestSpotSize = K)|E (2.0/0.0)
(Activity = 2) and (LargestSpotSize = A) and (Prev24Hour = 1) and (Evolution = 2)|E (2.0/0.0)
(HistComplex = 2) and (M-class = 1) and (LargestSpotSize = A) and (SpotDistribution = O)|E (2.0/0.0)
(LargestSpotSize = X)|B (127.0/0.0)
(SpotDistribution = O) and (HistComplex = 1) and (C-class = 0) and (Evolution = 2) and (LargestSpotSize = R) and (Activity = 2)|C (2.0/0.0)
(SpotDistribution = O) and (HistComplex = 1) and (C-class = 0) and (Evolution = 2) and (LargestSpotSize = R)|C (29.0/7.0)
(SpotDistribution = O) and (HistComplex = 1) and (C-class = 0) and (LargestSpotSize = S) and (Evolution = 2) and (Prev24Hour = 2)|C (2.0/0.0)
(SpotDistribution = O) and (HistComplex = 1) and (C-class = 0) and (LargestSpotSize = S) and (Evolution = 2) and (Activity = 1)|C (19.0/5.0)
(SpotDistribution = O) and (HistComplex = 1) and (C-class = 0) and (Evolution = 1) and (LargestSpotSize = S)|C (2.0/0.0)
(SpotDistribution = O) and (HistComplex = 1) and (C-class = 0) and (LargestSpotSize = R) and (Evolution = 1)|C (5.0/1.0)
(SpotDistribution = O) and (HistComplex = 1) and (C-class = 0) and (LargestSpotSize = R) and (M-class = 0)|C (51.0/17.0)
(SpotDistribution = O) and (C-class = 0) and (Evolution = 2) and (LargestSpotSize = R) and (Activity = 1)|C (10.0/2.0)
(SpotDistribution = O) and (LargestSpotSize = S) and (C-class = 0) and (HistComplex = 1) and (Activity = 2) and (Prev24Hour = 1) and (Evolution = 3)|C (2.0/0.0)
(SpotDistribution = O) and (LargestSpotSize = S) and (C-class = 0) and (HistComplex = 1) and (M-class = 1)|C (2.0/0.0)
(SpotDistribution = O) and (LargestSpotSize = S) and (C-class = 0) and (HistComplex = 1) and (Evolution = 2)|C (7.0/2.0)
(SpotDistribution = O) and (LargestSpotSize = S) and (C-class = 0) and (HistComplex = 1) and (Activity = 1)|C (30.0/11.0)
(SpotDistribution = O) and (Evolution = 2) and (C-class = 0) and (LargestSpotSize = S) and (Activity = 2)|C (2.0/0.0)
(SpotDistribution = O) and (Evolution = 2) and (LargestSpotSize = A)|C (17.0/8.0)
(SpotDistribution = O) and (Evolution = 2) and (LargestSpotSize = S) and (C-class = 0)|C (20.0/9.0)
(SpotDistribution = O) and (HistComplex = 1) and (C-class = 3)|C (3.0/1.0)
(SpotDistribution = O) and (HistComplex = 1) and (C-class = 0) and (Activity = 1) and (LargestSpotSize = A)|C (8.0/3.0)
(SpotDistribution = O) and (LargestSpotSize = S) and (C-class = 1) and (HistComplex = 1) and (Activity = 2) and (Prev24Hour = 1)|C (2.0/0.0)
(SpotDistribution = O) and (Evolution = 3) and (Activity = 1) and (LargestSpotSize = S) and (HistComplex = 2)|C (9.0/4.0)
(SpotDistribution = I) and (LargestSpotSize = A) and (Evolution = 2)|D (4.0/0.0)
(SpotDistribution = I) and (LargestSpotSize = A) and (C-class = 1)|D (3.0/0.0)
(SpotDistribution = I) and (LargestSpotSize = K) and (Evolution = 3)|D (7.0/0.0)
(SpotDistribution = I) and (C-class = 0) and (LargestSpotSize = A) and (Activity = 2)|D (2.0/0.0)
(SpotDistribution = I) and (C-class = 0) and (LargestSpotSize = A)|D (11.0/2.0)
(SpotDistribution = O) and (C-class = 1) and (LargestSpotSize = A)|D (3.0/0.0)
(SpotDistribution = O) and (C-class = 1) and (Prev24Hour = 2)|D (2.0/0.0)
(SpotDistribution = I) and (C-class = 0) and (HistComplex = 2) and (Evolution = 2)|D (6.0/0.0)
(SpotDistribution = O) and (Evolution = 3) and (C-class = 2) and (LargestSpotSize = S)|D (2.0/0.0)
(SpotDistribution = O) and (C-class = 1) and (LargestSpotSize = R) and (Evolution = 2)|D (2.0/0.0)
(SpotDistribution = O) and (Evolution = 3) and (Activity = 2) and (LargestSpotSize = A) and (HistComplex = 1)|D (3.0/0.0)
(SpotDistribution = I) and (Evolution = 3) and (LargestSpotSize = R) and (HistComplex = 2) and (Activity = 2)|D (2.0/0.0)
(SpotDistribution = O) and (HistComplex = 2) and (Activity = 1) and (Evolution = 2) and (LargestSpotSize = S)|D (2.0/0.0)
(SpotDistribution = I) and (C-class = 0) and (Evolution = 3) and (LargestSpotSize = R) and (HistComplex = 2)|D (4.0/1.0)
(SpotDistribution = O) and (Evolution = 3) and (C-class = 1)|D (11.0/4.0)
(SpotDistribution = I) and (C-class = 0) and (Evolution = 3)|D (24.0/9.0)
(SpotDistribution = O) and (C-class = 0) and (Activity = 1) and (HistComplex = 2) and (LargestSpotSize = H)|D (7.0/2.0)
(SpotDistribution = O) and (C-class = 0) and (Activity = 1) and (LargestSpotSize = A) and (Evolution = 1)|D (2.0/0.0)
(SpotDistribution = O) and (C-class = 0) and (Evolution = 3) and (LargestSpotSize = R) and (Area = 1) and (HistComplex = 2)|D (2.0/0.0)
(SpotDistribution = O) and (C-class = 0) and (Evolution = 3) and (LargestSpotSize = S) and (Prev24Hour = 1)|D (3.0/1.0)
(SpotDistribution = I) and (Activity = 2) and (C-class = 3)|D (2.0/0.0)
(SpotDistribution = O) and (C-class = 0) and (Activity = 1) and (LargestSpotSize = A)|D (10.0/5.0)
|H (354.0/57.0)


## PART

Decision list:

rules | predicted class
---|---
SpotDistribution = X|H (222.0)
LargestSpotSize = X|B (97.0)
Area != 1 AND Prev24Hour = 1|F (12.0/6.0)
SpotDistribution = C|E (20.0/7.0)
SpotDistribution = O AND LargestSpotSize != H AND HistComplex = 1 AND C-class != 2 AND C-class = 1 AND LargestSpotSize != R AND Evolution != 2|D (7.0/3.0)
SpotDistribution = O AND LargestSpotSize != H AND HistComplex = 1 AND C-class != 2 AND LargestSpotSize != S AND C-class != 1|C (73.0/22.0)
SpotDistribution = O AND LargestSpotSize != H AND Evolution != 1 AND C-class != 2 AND LargestSpotSize != A AND C-class != 1 AND HistComplex = 1|C (48.0/14.0)
SpotDistribution != O AND LargestSpotSize = R|D (18.0/7.0)
SpotDistribution != O AND M-class = 0 AND Evolution = 3 AND LargestSpotSize != K AND C-class != 2 AND LargestSpotSize != S AND HistComplex = 1|D (12.0/2.0)
SpotDistribution != O AND M-class = 0 AND C-class != 3 AND HistComplex = 1|D (18.0/7.0)
SpotDistribution != O AND M-class = 0 AND C-class != 3 AND Evolution = 3 AND LargestSpotSize != S AND LargestSpotSize = A AND C-class = 0|D (10.0/2.0)
SpotDistribution != O AND M-class = 0 AND C-class != 3 AND Evolution = 3 AND LargestSpotSize != A|D (14.0/2.0)
M-class = 0 AND SpotDistribution = O AND LargestSpotSize != H AND C-class != 2 AND Evolution != 1 AND Evolution = 2 AND LargestSpotSize != A AND Activity = 1 AND C-class = 0|C (24.0/9.0)
M-class = 0 AND SpotDistribution = O AND LargestSpotSize != H AND Evolution != 1 AND C-class != 2 AND Prev24Hour = 1 AND Evolution != 2|D (23.0/10.0)
M-class = 0 AND C-class != 3 AND HistComplex != 1 AND Prev24Hour != 3 AND C-class != 2 AND C-class != 0 AND SpotDistribution != O|D (19.0/10.0)
M-class = 0 AND C-class != 3 AND HistComplex != 1 AND C-class != 1|D (60.0/37.0)
M-class != 0|D (12.0/2.0)
C-class != 0 AND LargestSpotSize != H AND C-class = 3|E (7.0/3.0)
HistComplex = 1|C (13.0/6.0)
|E (8.0/2.0)


## J48 Decision Tree

* SpotDistribution = X: H (297.0)
* SpotDistribution = O
	* LargestSpotSize = A: D (54.0/30.0)
	* LargestSpotSize = R
		* C-class = 0: C (105.0/33.0)
		* C-class = 1: D (7.0/2.0)
		* C-class = 2: C (0.0)
		* C-class = 3: C (1.0)
		* C-class = 4: C (0.0)
		* C-class = 5: C (0.0)
		* C-class = 6: C (0.0)
		* C-class = 7: C (0.0)
		* C-class = 8: C (0.0)
	* LargestSpotSize = S: C (128.0/55.0)
	* LargestSpotSize = X: B (114.0)
	* LargestSpotSize = K: C (1.0)
	* LargestSpotSize = H: D (14.0/8.0)
* SpotDistribution = I
	* LargestSpotSize = A: D (100.0/42.0)
	* LargestSpotSize = R: D (26.0/9.0)
	* LargestSpotSize = S: D (39.0/21.0)
	* LargestSpotSize = X: B (14.0)
	* LargestSpotSize = K: D (21.0/10.0)
	* LargestSpotSize = H: E (3.0/1.0)
* SpotDistribution = C: E (32.0/14.0)


