# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | H | 0.311715 |
| LargestSpotSize = X and SpotDistribution = O and Area = 1 | B | 0.122210 |
| SpotDistribution = O and LargestSpotSize!=(X) and SpotDistribution != I and LargestSpotSize != X and Activity!=(2) | D | 0.056753 |
| LargestSpotSize = R and SpotDistribution = O and Area = 1 | C | 0.061868 |
| LargestSpotSize = S and SpotDistribution = O and Area = 1 | C | 0.055406 |
| LargestSpotSize = A and SpotDistribution = I and Area = 1 | D | 0.043683 |
| LargestSpotSize = R and SpotDistribution = I and Area = 1 | D | 0.014840 |
| SpotDistribution = C and LargestSpotSize = K | E | 0.009635 |
| LargestSpotSize = X and SpotDistribution = I and Area = 1 | B | 0.015495 |
| LargestSpotSize = S and SpotDistribution = I and Area = 1 | D | 0.010068 |
| SpotDistribution = I and LargestSpotSize = K and Area = 1 and Evolution = 3 | D | 0.010681 |
| SpotDistribution = I and LargestSpotSize = S and HistComplex = 2 and Evolution = 2 | E | 0.003183 |
| SpotDistribution = O and LargestSpotSize = A and C-class = 0 and Activity = 1 and Evolution = 2 | C | 0.003916 |
| SpotDistribution = I and LargestSpotSize = A and HistComplex = 2 and Evolution = 3 and C-class = 1 | E | 0.001722 |
| SpotDistribution = I and LargestSpotSize = A and HistComplex = 2 and Evolution = 2 and C-class = 0 and Activity = 2 | F | 0.001939 |
| LargestSpotSize = H and SpotDistribution = I and Area = 1 | E | 0.002291 |
| SpotDistribution = O and LargestSpotSize = A and C-class = 4 | E | 0.002291 |
| LargestSpotSize = A and SpotDistribution = C and Area = 1 | E | 0.002043 |
| SpotDistribution = O and LargestSpotSize = H and Evolution = 2 | E | 0.001478 |
| SpotDistribution = C and LargestSpotSize = A | D | 0.002165 |
| SpotDistribution = I and LargestSpotSize = K and Area = 2 | E | 0.001722 |
| LargestSpotSize = K and SpotDistribution = I and Area = 2 | F | 0.001634 |
| SpotDistribution = I and LargestSpotSize = A and HistComplex = 2 and Evolution = 2 and C-class = 3 | E | 0.001529 |
| LargestSpotSize = R and SpotDistribution = C and Area = 1 | D | 0.002692 |
| SpotDistribution = I and LargestSpotSize = K and Area = 1 and Evolution = 2 | F | 0.001402 |
| SpotDistribution = C and LargestSpotSize = H | E | 0.001147 |
| SpotDistribution = O and LargestSpotSize = S and C-class = 5 | E | 0.001147 |
| SpotDistribution = O and LargestSpotSize = S and C-class = 6 | E | 0.001147 |
| SpotDistribution = I and LargestSpotSize = A and HistComplex = 2 and Evolution = 3 and C-class = 6 | E | 0.001147 |
| SpotDistribution = I and LargestSpotSize = A and HistComplex = 2 and Evolution = 3 and C-class = 4 | E | 0.001147 |
| SpotDistribution = O and LargestSpotSize = K | C | 0.001304 |
| SpotDistribution = I and LargestSpotSize = R and Evolution = 1 | C | 0.001304 |
| SpotDistribution = I and LargestSpotSize = A and HistComplex = 2 and Evolution = 2 and C-class = 4 | F | 0.001088 |
| LargestSpotSize = K and SpotDistribution = I and Area = 1 | D | 0.008937 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = X | H | 0.311715 |
| LargestSpotSize = X | B | 0.195122 |
| Area != 1 and Prev24Hour != 1 and Evolution = 2 | E | 0.011111 |
| Area != 1 and Evolution != 2 and X-class = 0 and Activity = 1 | E | 0.007143 |
| SpotDistribution = O and LargestSpotSize != H and LargestSpotSize != A and Evolution != 1 and C-class = 1 and LargestSpotSize = R and Evolution != 2 | D | 0.007305 |
| SpotDistribution = O and LargestSpotSize != H and LargestSpotSize != A and Evolution != 1 and LargestSpotSize != S and C-class != 1 and Evolution = 2 and HistComplex = 1 | C | 0.054604 |
| Area != 1 and Evolution != 2 and X-class = 0 and SpotDistribution != I and C-class != 0 | E | 0.002387 |
| SpotDistribution = O and LargestSpotSize != H and LargestSpotSize != A and Evolution != 1 and LargestSpotSize = R and C-class != 1 and Evolution != 2 | C | 0.071354 |
| SpotDistribution = O and LargestSpotSize != H and LargestSpotSize != A and C-class = 1 and LargestSpotSize != R and Prev24Hour = 1 and HistComplex = 1 and Evolution != 2 | D | 0.006173 |
| SpotDistribution = O and LargestSpotSize != H and LargestSpotSize != A and C-class = 1 and LargestSpotSize != R and HistComplex = 1 | C | 0.015679 |
| SpotDistribution = O and LargestSpotSize != H and LargestSpotSize != A and C-class = 1 and LargestSpotSize != R and Activity = 1 | D | 0.004219 |
| SpotDistribution = O and LargestSpotSize != H and C-class = 0 and LargestSpotSize = R and Evolution != 1 | C | 0.002613 |
| SpotDistribution = O and LargestSpotSize != H and C-class = 0 and LargestSpotSize != A and HistComplex = 1 and Prev24Hour = 1 and Evolution = 2 and Activity = 1 | C | 0.028670 |
| Area != 1 and Evolution != 2 and X-class = 0 | F | 0.013924 |
| SpotDistribution = O and LargestSpotSize != H and C-class = 0 and Evolution != 1 and LargestSpotSize != A and HistComplex != 1 and Evolution != 2 and Activity = 1 | C | 0.007261 |
| SpotDistribution = O and LargestSpotSize != H and C-class = 0 and Evolution != 1 and LargestSpotSize != A and HistComplex != 1 and Evolution = 2 and Activity = 1 | C | 0.016708 |
| HistComplex = 1 and LargestSpotSize != H and LargestSpotSize = A and SpotDistribution != O and C-class = 0 and Evolution != 2 and M-class = 0 | D | 0.044563 |
| HistComplex = 1 and LargestSpotSize != H and LargestSpotSize = A and SpotDistribution != O and C-class = 0 | D | 0.030473 |
| HistComplex = 1 and LargestSpotSize != H and SpotDistribution != C and C-class = 1 and LargestSpotSize != S and Evolution != 2 and LargestSpotSize = A | D | 0.025000 |
| HistComplex = 1 and LargestSpotSize != H and SpotDistribution != C and Prev24Hour = 1 and Evolution = 1 and LargestSpotSize != S | C | 0.014077 |
| HistComplex = 1 and LargestSpotSize != H and SpotDistribution != C and Prev24Hour = 1 and LargestSpotSize = R and C-class != 2 and C-class = 0 | D | 0.125681 |
| HistComplex = 1 and LargestSpotSize != H and SpotDistribution != C and Prev24Hour = 1 and LargestSpotSize != A and LargestSpotSize = R and C-class = 1 | D | 0.013889 |
| HistComplex = 1 and LargestSpotSize != H and SpotDistribution != C and Prev24Hour = 1 and LargestSpotSize != A and Evolution = 2 and C-class = 0 | C | 0.012636 |
| HistComplex = 1 and LargestSpotSize != H and SpotDistribution != C and Prev24Hour = 1 and LargestSpotSize != A and SpotDistribution != O and C-class = 0 | D | 0.023063 |
| HistComplex = 1 and LargestSpotSize != H and SpotDistribution != C and Prev24Hour = 1 and LargestSpotSize != A and Activity = 1 and C-class != 2 and Evolution = 3 and C-class = 0 | C | 0.058300 |
| LargestSpotSize = R and SpotDistribution != O and C-class != 2 and Evolution = 3 and Activity = 1 | D | 0.016461 |
| LargestSpotSize = R and SpotDistribution != O and C-class != 2 and Evolution != 3 | D | 0.016461 |
| SpotDistribution = O and LargestSpotSize != H and LargestSpotSize != R and Evolution != 1 and C-class != 2 and C-class = 0 and LargestSpotSize != A and HistComplex = 1 | C | 0.004569 |
| SpotDistribution = O and LargestSpotSize != H and LargestSpotSize != R and Prev24Hour != 1 and LargestSpotSize != A | D | 0.014652 |
| SpotDistribution = O and M-class != 1 and C-class != 2 and Activity != 1 and LargestSpotSize != H and C-class = 0 and LargestSpotSize != A | C | 0.008403 |
| LargestSpotSize = R and Activity = 1 and SpotDistribution = O | C | 0.008403 |
| HistComplex = 1 and LargestSpotSize != H and Activity != 1 and SpotDistribution = I | D | 0.006803 |
| HistComplex = 1 and LargestSpotSize != H and Activity = 1 and C-class != 1 and Evolution != 3 and LargestSpotSize != A | C | 0.004292 |
| HistComplex = 1 and LargestSpotSize != H and Activity = 1 and C-class != 1 and Evolution != 2 and C-class != 2 and C-class = 0 | D | 0.060403 |
| HistComplex = 1 and Activity = 1 and C-class = 0 | D | 0.009328 |
| HistComplex = 1 and Activity = 1 and C-class != 2 and C-class = 1 | C | 0.018939 |
| SpotDistribution != O and LargestSpotSize != H and LargestSpotSize != R and X-class != 1 and Evolution = 3 and LargestSpotSize != S and LargestSpotSize != A and C-class != 0 | D | 0.042241 |
| Area = 1 and SpotDistribution != O and LargestSpotSize != H and C-class != 4 and LargestSpotSize != R and M-class != 0 and Evolution = 3 | D | 0.010791 |
| Area != 1 | F | 0.006241 |
| C-class = 4 and SpotDistribution = I | F | 0.006410 |
| SpotDistribution != O and LargestSpotSize != H and HistComplex = 1 | D | 0.012121 |
| SpotDistribution != O and LargestSpotSize != H and M-class = 0 and Evolution = 3 and LargestSpotSize != S and LargestSpotSize = A and Activity = 1 and C-class != 0 and C-class != 1 | D | 0.016544 |
| SpotDistribution != O and LargestSpotSize != H and M-class = 0 and Evolution = 3 and LargestSpotSize != S and LargestSpotSize = A and Activity = 1 and C-class = 0 | D | 0.026119 |
| SpotDistribution = O and Activity != 1 and Prev24Hour != 3 and Evolution = 2 | E | 0.040563 |
| SpotDistribution = O and M-class != 1 and C-class != 2 and LargestSpotSize = H and Evolution != 2 | D | 0.014062 |
| SpotDistribution = O and LargestSpotSize != H and M-class != 1 and C-class != 2 and C-class != 1 and LargestSpotSize = A and Evolution != 2 and Activity = 1 | D | 0.022132 |
| SpotDistribution != O and LargestSpotSize = H | E | 0.021739 |
| SpotDistribution = O and LargestSpotSize != H and M-class != 1 and C-class != 2 and C-class != 1 and Evolution = 2 | C | 0.012564 |
| HistComplex = 1 | D | 0.009520 |
| LargestSpotSize != H and M-class = 1 | D | 0.004425 |
| C-class != 0 and SpotDistribution != C and Prev24Hour = 1 and C-class = 1 and Evolution != 2 and Activity = 1 | D | 0.015254 |
| LargestSpotSize != H and C-class != 0 and SpotDistribution != C and SpotDistribution = O and Activity = 1 | D | 0.007305 |
| LargestSpotSize != H and C-class != 0 and SpotDistribution != C and Prev24Hour = 1 and C-class = 1 and Evolution = 2 and Activity != 1 | D | 0.029762 |
| C-class != 0 and SpotDistribution != C and Activity != 1 and Evolution != 2 and LargestSpotSize = A and C-class != 2 | E | 0.028319 |
| Prev24Hour != 1 and Evolution = 2 | D | 0.013274 |
| Prev24Hour = 1 and C-class != 0 and C-class != 1 and Activity != 1 and LargestSpotSize != S and C-class != 2 | F | 0.004796 |
| LargestSpotSize != H and Prev24Hour != 1 | D | 0.008411 |
| LargestSpotSize = H | D | 0.006116 |
| C-class = 2 and LargestSpotSize = A | D | 0.002294 |
| C-class != 2 and C-class = 1 and Activity = 1 | D | 0.003017 |
| C-class != 2 and C-class != 1 and C-class = 0 and LargestSpotSize != K and SpotDistribution != C and Activity = 1 and Evolution != 3 and Evolution != 1 and LargestSpotSize = A | D | 0.037156 |
| C-class != 2 and C-class != 1 and C-class = 0 and SpotDistribution = C | D | 0.004673 |
| C-class != 2 and C-class != 1 and C-class = 0 and LargestSpotSize != A and Evolution = 3 and Activity = 1 | D | 0.040541 |
| C-class != 2 and C-class != 1 and C-class = 0 and LargestSpotSize != A and Evolution != 3 and Activity = 1 and SpotDistribution = O | D | 0.053540 |
| C-class != 1 and C-class != 2 and C-class = 0 and LargestSpotSize != A and Evolution = 2 and Activity = 1 | E | 0.052941 |
| C-class = 1 | D | 0.002339 |
| C-class != 0 and C-class = 2 | F | 0.012228 |
| C-class = 0 and LargestSpotSize != A and Evolution = 2 | E | 0.014610 |
| C-class = 0 and LargestSpotSize = A and Evolution != 3 | F | 0.028824 |
| C-class = 0 and LargestSpotSize = A | D | 0.003988 |
| C-class = 0 | D | 0.023088 |
|  | E | 0.542553 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| HistComplex = 2 and Area = 2 | E | 0.009890 |
| LargestSpotSize = A and Activity = 2 | E | 0.006799 |
| LargestSpotSize = X | B | 0.138979 |
| SpotDistribution = O and C-class = 0 and LargestSpotSize = R | C | 0.076618 |
| SpotDistribution = O and LargestSpotSize = S | C | 0.069656 |
| SpotDistribution = I | D | 0.127229 |
| SpotDistribution = O and Evolution = 3 | D | 0.101597 |
|  | H | 0.616977 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

largestspotsize|spotdistribution|area|class
---|---|---|---
a|c|2|h
k|c|2|e
a|i|2|h
k|i|2|f
r|o|2|h
r|c|1|d
h|c|1|h
k|c|1|e
a|c|1|e
x|i|1|b
k|i|1|d
h|i|1|e
r|i|1|d
s|i|1|d
a|i|1|d
h|o|1|d
x|o|1|b
k|o|1|h
a|o|1|d
r|o|1|c
s|o|1|c
k|x|1|h
h|x|1|h
a|x|1|h
s|x|1|h
r|x|1|h

## JRip

Decision list:

rules | predicted class
---|---
(HistComplex = 2) and (Area = 2)|E (26.0/11.0)
(LargestSpotSize = A) and (Activity = 2)|E (54.0/36.0)
(LargestSpotSize = X)|B (128.0/0.0)
(SpotDistribution = O) and (C-class = 0) and (LargestSpotSize = R)|C (99.0/29.0)
(SpotDistribution = O) and (LargestSpotSize = S)|C (129.0/54.0)
(SpotDistribution = I)|D (147.0/62.0)
(SpotDistribution = O) and (Evolution = 3)|D (35.0/16.0)
|H (338.0/41.0)


## PART

Decision list:

rules | predicted class
---|---
SpotDistribution = X|H (298.0)
LargestSpotSize = X|B (128.0)
Area != 1 AND Prev24Hour != 1 AND Evolution = 2|E (5.0)
Area != 1 AND Evolution != 2 AND X-class = 0 AND Activity = 1|E (5.0/1.0)
SpotDistribution = O AND LargestSpotSize != H AND LargestSpotSize != A AND Evolution != 1 AND C-class = 1 AND LargestSpotSize = R AND Evolution != 2|D (4.0/1.0)
SpotDistribution = O AND LargestSpotSize != H AND LargestSpotSize != A AND Evolution != 1 AND LargestSpotSize != S AND C-class != 1 AND Evolution = 2 AND HistComplex = 1|C (28.0/5.0)
Area != 1 AND Evolution != 2 AND X-class = 0 AND SpotDistribution != I AND C-class != 0|E (4.0/2.0)
SpotDistribution = O AND LargestSpotSize != H AND LargestSpotSize != A AND Evolution != 1 AND LargestSpotSize = R AND C-class != 1 AND Evolution != 2|C (59.0/21.0)
SpotDistribution = O AND LargestSpotSize != H AND LargestSpotSize != A AND C-class = 1 AND LargestSpotSize != R AND Prev24Hour = 1 AND HistComplex = 1 AND Evolution != 2|D (6.0/3.0)
SpotDistribution = O AND LargestSpotSize != H AND LargestSpotSize != A AND C-class = 1 AND LargestSpotSize != R AND HistComplex = 1|C (4.0/1.0)
SpotDistribution = O AND LargestSpotSize != H AND LargestSpotSize != A AND C-class = 1 AND LargestSpotSize != R AND Activity = 1|D (4.0/2.0)
SpotDistribution = O AND LargestSpotSize != H AND C-class = 0 AND LargestSpotSize = R AND Evolution != 1|C (6.0/1.0)
SpotDistribution = O AND LargestSpotSize != H AND C-class = 0 AND LargestSpotSize != A AND HistComplex = 1 AND Prev24Hour = 1 AND Evolution = 2 AND Activity = 1|C (19.0/4.0)
Area != 1 AND Evolution != 2 AND X-class = 0|F (6.0/2.0)
SpotDistribution = O AND LargestSpotSize != H AND C-class = 0 AND Evolution != 1 AND LargestSpotSize != A AND HistComplex != 1 AND Evolution != 2 AND Activity = 1|C (9.0/4.0)
SpotDistribution = O AND LargestSpotSize != H AND C-class = 0 AND Evolution != 1 AND LargestSpotSize != A AND HistComplex != 1 AND Evolution = 2 AND Activity = 1|C (18.0/8.0)
HistComplex = 1 AND LargestSpotSize != H AND LargestSpotSize = A AND SpotDistribution != O AND C-class = 0 AND Evolution != 2 AND M-class = 0|D (11.0/1.0)
HistComplex = 1 AND LargestSpotSize != H AND LargestSpotSize = A AND SpotDistribution != O AND C-class = 0|D (7.0)
HistComplex = 1 AND LargestSpotSize != H AND SpotDistribution != C AND C-class = 1 AND LargestSpotSize != S AND Evolution != 2 AND LargestSpotSize = A|D (5.0)
HistComplex = 1 AND LargestSpotSize != H AND SpotDistribution != C AND Prev24Hour = 1 AND Evolution = 1 AND LargestSpotSize != S|C (6.0/1.0)
HistComplex = 1 AND LargestSpotSize != H AND SpotDistribution != C AND Prev24Hour = 1 AND LargestSpotSize = R AND C-class != 2 AND C-class = 0|D (8.0/3.0)
HistComplex = 1 AND LargestSpotSize != H AND SpotDistribution != C AND Prev24Hour = 1 AND LargestSpotSize != A AND LargestSpotSize = R AND C-class = 1|D (5.0/1.0)
HistComplex = 1 AND LargestSpotSize != H AND SpotDistribution != C AND Prev24Hour = 1 AND LargestSpotSize != A AND Evolution = 2 AND C-class = 0|C (6.0/1.0)
HistComplex = 1 AND LargestSpotSize != H AND SpotDistribution != C AND Prev24Hour = 1 AND LargestSpotSize != A AND SpotDistribution != O AND C-class = 0|D (13.0/5.0)
HistComplex = 1 AND LargestSpotSize != H AND SpotDistribution != C AND Prev24Hour = 1 AND LargestSpotSize != A AND Activity = 1 AND C-class != 2 AND Evolution = 3 AND C-class = 0|C (31.0/13.0)
LargestSpotSize = R AND SpotDistribution != O AND C-class != 2 AND Evolution = 3 AND Activity = 1|D (5.0/1.0)
LargestSpotSize = R AND SpotDistribution != O AND C-class != 2 AND Evolution != 3|D (6.0/2.0)
SpotDistribution = O AND LargestSpotSize != H AND LargestSpotSize != R AND Evolution != 1 AND C-class != 2 AND C-class = 0 AND LargestSpotSize != A AND HistComplex = 1|C (6.0/1.0)
SpotDistribution = O AND LargestSpotSize != H AND LargestSpotSize != R AND Prev24Hour != 1 AND LargestSpotSize != A|D (5.0/2.0)
SpotDistribution = O AND M-class != 1 AND C-class != 2 AND Activity != 1 AND LargestSpotSize != H AND C-class = 0 AND LargestSpotSize != A|C (5.0/2.0)
LargestSpotSize = R AND Activity = 1 AND SpotDistribution = O|C (4.0/1.0)
HistComplex = 1 AND LargestSpotSize != H AND Activity != 1 AND SpotDistribution = I|D (4.0/2.0)
HistComplex = 1 AND LargestSpotSize != H AND Activity = 1 AND C-class != 1 AND Evolution != 3 AND LargestSpotSize != A|C (5.0/2.0)
HistComplex = 1 AND LargestSpotSize != H AND Activity = 1 AND C-class != 1 AND Evolution != 2 AND C-class != 2 AND C-class = 0|D (9.0/5.0)
HistComplex = 1 AND Activity = 1 AND C-class = 0|D (6.0/2.0)
HistComplex = 1 AND Activity = 1 AND C-class != 2 AND C-class = 1|C (5.0/1.0)
SpotDistribution != O AND LargestSpotSize != H AND LargestSpotSize != R AND X-class != 1 AND Evolution = 3 AND LargestSpotSize != S AND LargestSpotSize != A AND C-class != 0|D (7.0)
Area = 1 AND SpotDistribution != O AND LargestSpotSize != H AND C-class != 4 AND LargestSpotSize != R AND M-class != 0 AND Evolution = 3|D (6.0/3.0)
Area != 1|F (5.0/2.0)
C-class = 4 AND SpotDistribution = I|F (3.0/1.0)
SpotDistribution != O AND LargestSpotSize != H AND HistComplex = 1|D (4.0/1.0)
SpotDistribution != O AND LargestSpotSize != H AND M-class = 0 AND Evolution = 3 AND LargestSpotSize != S AND LargestSpotSize = A AND Activity = 1 AND C-class != 0 AND C-class != 1|D (4.0/1.0)
SpotDistribution != O AND LargestSpotSize != H AND M-class = 0 AND Evolution = 3 AND LargestSpotSize != S AND LargestSpotSize = A AND Activity = 1 AND C-class = 0|D (13.0/6.0)
SpotDistribution = O AND Activity != 1 AND Prev24Hour != 3 AND Evolution = 2|E (7.0)
SpotDistribution = O AND M-class != 1 AND C-class != 2 AND LargestSpotSize = H AND Evolution != 2|D (5.0/2.0)
SpotDistribution = O AND LargestSpotSize != H AND M-class != 1 AND C-class != 2 AND C-class != 1 AND LargestSpotSize = A AND Evolution != 2 AND Activity = 1|D (13.0/6.0)
SpotDistribution != O AND LargestSpotSize = H|E (3.0)
SpotDistribution = O AND LargestSpotSize != H AND M-class != 1 AND C-class != 2 AND C-class != 1 AND Evolution = 2|C (10.0/4.0)
HistComplex = 1|D (5.0/2.0)
LargestSpotSize != H AND M-class = 1|D (5.0/3.0)
C-class != 0 AND SpotDistribution != C AND Prev24Hour = 1 AND C-class = 1 AND Evolution != 2 AND Activity = 1|D (4.0/1.0)
LargestSpotSize != H AND C-class != 0 AND SpotDistribution != C AND SpotDistribution = O AND Activity = 1|D (4.0/2.0)
LargestSpotSize != H AND C-class != 0 AND SpotDistribution != C AND Prev24Hour = 1 AND C-class = 1 AND Evolution = 2 AND Activity != 1|D (7.0/2.0)
C-class != 0 AND SpotDistribution != C AND Activity != 1 AND Evolution != 2 AND LargestSpotSize = A AND C-class != 2|E (4.0/1.0)
Prev24Hour != 1 AND Evolution = 2|D (4.0/2.0)
Prev24Hour = 1 AND C-class != 0 AND C-class != 1 AND Activity != 1 AND LargestSpotSize != S AND C-class != 2|F (4.0/2.0)
LargestSpotSize != H AND Prev24Hour != 1|D (4.0/1.0)
LargestSpotSize = H|D (3.0/1.0)
C-class = 2 AND LargestSpotSize = A|D (3.0/2.0)
C-class != 2 AND C-class = 1 AND Activity = 1|D (6.0/4.0)
C-class != 2 AND C-class != 1 AND C-class = 0 AND LargestSpotSize != K AND SpotDistribution != C AND Activity = 1 AND Evolution != 3 AND Evolution != 1 AND LargestSpotSize = A|D (17.0/10.0)
C-class != 2 AND C-class != 1 AND C-class = 0 AND SpotDistribution = C|D (4.0/2.0)
C-class != 2 AND C-class != 1 AND C-class = 0 AND LargestSpotSize != A AND Evolution = 3 AND Activity = 1|D (4.0/1.0)
C-class != 2 AND C-class != 1 AND C-class = 0 AND LargestSpotSize != A AND Evolution != 3 AND Activity = 1 AND SpotDistribution = O|D (6.0/4.0)
C-class != 1 AND C-class != 2 AND C-class = 0 AND LargestSpotSize != A AND Evolution = 2 AND Activity = 1|E (5.0/2.0)
C-class = 1|D (3.0/1.0)
C-class != 0 AND C-class = 2|F (3.0/1.0)
C-class = 0 AND LargestSpotSize != A AND Evolution = 2|E (5.0/3.0)
C-class = 0 AND LargestSpotSize = A AND Evolution != 3|F (7.0/3.0)
C-class = 0 AND LargestSpotSize = A|D (6.0/4.0)
C-class = 0|D (5.0/2.0)
|E (3.0)


## J48 Decision Tree

* SpotDistribution = X: H (298.0)
* SpotDistribution = O
	* LargestSpotSize = A
		* C-class = 0
			* Activity = 1
				* Evolution = 1: D (3.0/1.0)
				* Evolution = 2: C (12.0/6.0)
				* Evolution = 3: D (20.0/11.0)
			* Activity = 2: D (7.0/4.0)
		* C-class = 1: D (8.0/4.0)
		* C-class = 2: D (2.0)
		* C-class = 3: D (0.0)
		* C-class = 4: E (2.0)
		* C-class = 5: D (0.0)
		* C-class = 6: D (0.0)
		* C-class = 7: D (0.0)
		* C-class = 8: D (0.0)
	* LargestSpotSize = R
		* C-class = 0: C (100.0/30.0)
		* C-class = 1: D (7.0/2.0)
		* C-class = 2: C (0.0)
		* C-class = 3: C (0.0)
		* C-class = 4: C (0.0)
		* C-class = 5: C (1.0)
		* C-class = 6: C (0.0)
		* C-class = 7: C (0.0)
		* C-class = 8: C (0.0)
	* LargestSpotSize = S
		* C-class = 0
			* HistComplex = 1: C (64.0/20.0)
			* HistComplex = 2
				* Evolution = 1: D (7.0/4.0)
				* Evolution = 2: C (21.0/9.0)
				* Evolution = 3: D (12.0/6.0)
		* C-class = 1
			* Evolution = 1: C (0.0)
			* Evolution = 2: C (8.0/3.0)
			* Evolution = 3: D (9.0/4.0)
		* C-class = 2: D (2.0/1.0)
		* C-class = 3: D (4.0/2.0)
		* C-class = 4: C (0.0)
		* C-class = 5: E (1.0)
		* C-class = 6: E (1.0)
		* C-class = 7: C (0.0)
		* C-class = 8: C (0.0)
	* LargestSpotSize = X: B (115.0)
	* LargestSpotSize = K: C (1.0)
	* LargestSpotSize = H
		* Evolution = 1: D (0.0)
		* Evolution = 2: E (7.0/4.0)
		* Evolution = 3: D (7.0/3.0)
* SpotDistribution = I
	* LargestSpotSize = A
		* HistComplex = 1: D (25.0/3.0)
		* HistComplex = 2
			* Evolution = 1: D (2.0/1.0)
			* Evolution = 2
				* C-class = 0
					* Activity = 1: D (17.0/10.0)
					* Activity = 2: F (9.0/5.0)
				* C-class = 1: D (9.0/4.0)
				* C-class = 2: D (2.0/1.0)
				* C-class = 3: E (3.0/1.0)
				* C-class = 4: F (1.0)
				* C-class = 5: D (0.0)
				* C-class = 6: D (0.0)
				* C-class = 7: D (0.0)
				* C-class = 8: D (0.0)
			* Evolution = 3
				* C-class = 0: D (20.0/8.0)
				* C-class = 1: E (6.0/3.0)
				* C-class = 2: D (3.0/1.0)
				* C-class = 3: D (4.0/1.0)
				* C-class = 4: E (1.0)
				* C-class = 5: D (0.0)
				* C-class = 6: E (1.0)
				* C-class = 7: D (0.0)
				* C-class = 8: D (0.0)
	* LargestSpotSize = R
		* Evolution = 1: C (1.0)
		* Evolution = 2: D (8.0/3.0)
		* Evolution = 3: D (17.0/5.0)
	* LargestSpotSize = S
		* HistComplex = 1: D (17.0/8.0)
		* HistComplex = 2
			* Evolution = 1: D (1.0)
			* Evolution = 2: E (13.0/7.0)
			* Evolution = 3: D (8.0/5.0)
	* LargestSpotSize = X: B (13.0)
	* LargestSpotSize = K
		* Area = 1
			* Evolution = 1: D (0.0)
			* Evolution = 2: F (7.0/4.0)
			* Evolution = 3: D (8.0)
		* Area = 2: E (6.0/3.0)
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
			* SpotDistribution=(C)|(I)
			* Area=(2): E(14.0/11.0)
			* Area!=(2)
				* HistComplex=(2)
					* Evolution=(3): D(37.0/26.0)
					* Evolution!=(3): D(30.0/47.0)
				* HistComplex!=(2)
									* LargestSpotSize=(S)|(R)|(X)|(K)|(H): D(18.0/14.0)
									* LargestSpotSize!=(S)|(R)|(X)|(K)|(H): D(23.0/4.0)
			* SpotDistribution!=(C)|(I)
					* LargestSpotSize=(S)|(R)|(X)
				* HistComplex=(2): C(31.0/32.0)
				* HistComplex!=(2)
					* Evolution=(3): C(64.0/42.0)
					* Evolution!=(3): C(53.0/15.0)
					* LargestSpotSize!=(S)|(R)|(X)
				* Activity=(2): E(8.0/5.0)
				* Activity!=(2): D(27.0/29.0)
		* SpotDistribution!=(C)|(I)|(O): H(298.0/0.0)


