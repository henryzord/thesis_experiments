# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = X | H | 0.311390 |
| LargestSpotSize = X and SpotDistribution = O | B | 0.121148 |
| SpotDistribution = O and LargestSpotSize = R | C | 0.066017 |
| LargestSpotSize = A and SpotDistribution = I | D | 0.041956 |
| LargestSpotSize = S and SpotDistribution = O | C | 0.052763 |
| LargestSpotSize = A and SpotDistribution = O | D | 0.013567 |
| SpotDistribution = I and LargestSpotSize = S | D | 0.013804 |
| LargestSpotSize = R and SpotDistribution = I | D | 0.013061 |
| SpotDistribution = C | E | 0.012710 |
| LargestSpotSize = X and SpotDistribution = I | B | 0.016647 |
| SpotDistribution = O and LargestSpotSize!=(X) and SpotDistribution != I and LargestSpotSize != K and C-class != 8 | E | 0.003913 |
| SpotDistribution = I and LargestSpotSize = K | D | 0.008426 |
| SpotDistribution = O and LargestSpotSize = A and C-class = 0 and Evolution = 2 | C | 0.005867 |
| SpotDistribution = O and LargestSpotSize = H | D | 0.004408 |
| LargestSpotSize = R and SpotDistribution = C | D | 0.000674 |
| SpotDistribution = I and LargestSpotSize = H | E | 0.001527 |
| LargestSpotSize = H and SpotDistribution = I | D | 0.000450 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = X | H | 0.311390 |
| LargestSpotSize = X | B | 0.194825 |
| Area != 1 and LargestSpotSize != A and M-class = 0 and Prev24Hour != 1 | E | 0.007127 |
| Area != 1 and LargestSpotSize != A and M-class = 0 and SpotDistribution = C | F | 0.006517 |
| SpotDistribution = O and LargestSpotSize != H and LargestSpotSize != A and HistComplex = 1 and C-class != 2 and Activity = 1 and C-class = 1 and LargestSpotSize = R | D | 0.008602 |
| SpotDistribution = O and LargestSpotSize != H and LargestSpotSize != A and HistComplex = 1 and C-class != 2 and Activity = 1 and LargestSpotSize = R and Evolution != 1 and Evolution != 2 | C | 0.076409 |
| SpotDistribution = O and LargestSpotSize != H and LargestSpotSize != A and HistComplex = 1 and C-class != 2 and Activity != 1 and Prev24Hour = 1 and Evolution = 2 | C | 0.019104 |
| SpotDistribution = O and LargestSpotSize != H and LargestSpotSize != A and HistComplex = 1 and C-class != 2 and LargestSpotSize = R and Evolution != 1 | C | 0.034645 |
| Area != 1 and LargestSpotSize != A and SpotDistribution != I | E | 0.016129 |
| SpotDistribution = O and LargestSpotSize != H and LargestSpotSize != A and HistComplex = 1 and C-class != 2 and LargestSpotSize != R and C-class != 0 and C-class = 1 and Evolution != 2 | D | 0.006522 |
| SpotDistribution = O and LargestSpotSize != H and C-class = 0 and LargestSpotSize != A and HistComplex = 1 and Prev24Hour = 1 and LargestSpotSize != R and Activity = 1 and Evolution != 2 | C | 0.039544 |
| Area != 1 and LargestSpotSize = A | F | 0.007792 |
| SpotDistribution = O and LargestSpotSize != H and C-class = 0 and Evolution != 2 and LargestSpotSize = R and HistComplex != 1 | D | 0.008696 |
| SpotDistribution = O and LargestSpotSize != H and LargestSpotSize = R and Evolution != 1 | C | 0.004551 |
| SpotDistribution = O and LargestSpotSize != R and LargestSpotSize != H and C-class = 0 and Evolution != 1 and LargestSpotSize != A and HistComplex = 1 and Prev24Hour = 1 | C | 0.021923 |
| SpotDistribution = C and C-class = 0 and LargestSpotSize = A | E | 0.005714 |
| Area != 1 and Activity = 1 | E | 0.004233 |
| LargestSpotSize = K and SpotDistribution = I and Area = 1 and Evolution != 2 | D | 0.042781 |
| LargestSpotSize = K and SpotDistribution = I and Activity = 1 | F | 0.006503 |
| Activity = 1 and M-class = 1 and SpotDistribution = I and C-class = 0 | D | 0.022222 |
| Activity = 1 and M-class = 1 and LargestSpotSize != S and Evolution = 3 | E | 0.007475 |
| Activity = 1 and SpotDistribution != O and HistComplex = 1 and LargestSpotSize = A and Evolution != 2 | D | 0.046041 |
| Activity = 1 and SpotDistribution = O and LargestSpotSize = H and Evolution != 2 and HistComplex != 1 | D | 0.015238 |
| Activity = 1 and SpotDistribution = O and LargestSpotSize != H and LargestSpotSize != R and Evolution != 1 and M-class != 1 and C-class != 2 and C-class != 1 and C-class = 0 and HistComplex = 1 and Evolution != 2 | D | 0.045211 |
| Activity = 1 and SpotDistribution = O and LargestSpotSize != H and LargestSpotSize != R and Evolution = 1 | D | 0.017857 |
| SpotDistribution = O and Evolution != 1 and LargestSpotSize != H and LargestSpotSize != A and C-class != 2 and C-class = 1 and HistComplex != 1 | D | 0.015238 |
| SpotDistribution = O and Evolution != 1 and LargestSpotSize != H and C-class = 0 and Activity = 1 and HistComplex != 1 and Evolution != 2 and LargestSpotSize = A | D | 0.017341 |
| SpotDistribution = O and Evolution = 1 | C | 0.019368 |
| SpotDistribution = O and LargestSpotSize != H and LargestSpotSize != A and C-class != 2 and C-class = 3 | D | 0.006024 |
| SpotDistribution = O and LargestSpotSize != H and C-class = 0 and HistComplex = 1 and LargestSpotSize = A and Activity = 1 | D | 0.005556 |
| SpotDistribution = O and LargestSpotSize != H and C-class = 0 and LargestSpotSize != A and HistComplex != 1 and Evolution != 2 and Activity = 1 | C | 0.010246 |
| SpotDistribution = O and LargestSpotSize != H and Evolution != 2 and M-class != 1 and C-class != 1 and C-class = 0 and LargestSpotSize = A | D | 0.003947 |
| SpotDistribution = O and LargestSpotSize != H and C-class = 0 and HistComplex != 1 and Evolution = 2 and LargestSpotSize != A and Activity = 1 | C | 0.017763 |
| HistComplex = 1 and LargestSpotSize != H and Activity = 1 and C-class != 2 and LargestSpotSize = A and SpotDistribution != O | D | 0.017316 |
| HistComplex = 1 and LargestSpotSize != H and Evolution != 2 and LargestSpotSize = A and C-class != 2 | D | 0.013889 |
| HistComplex = 1 and LargestSpotSize != H and LargestSpotSize != A and Prev24Hour = 1 and Activity = 1 and Evolution != 2 and C-class = 2 | D | 0.014610 |
| SpotDistribution = O and LargestSpotSize != H and C-class = 0 and HistComplex != 1 and Evolution = 2 and LargestSpotSize = A and Activity = 1 | C | 0.015584 |
| HistComplex = 1 and LargestSpotSize != H and LargestSpotSize != A and SpotDistribution = I and Activity = 1 and C-class = 0 and LargestSpotSize != R | D | 0.024324 |
| HistComplex = 1 and LargestSpotSize = H | C | 0.004484 |
| HistComplex = 1 and C-class = 1 and SpotDistribution = O | C | 0.022556 |
| LargestSpotSize = R and Activity = 1 and C-class = 0 and Evolution != 2 and HistComplex != 1 | D | 0.022695 |
| LargestSpotSize = R and Activity = 1 and C-class = 0 and Evolution != 2 | D | 0.133082 |
| HistComplex = 1 and SpotDistribution = O | E | 0.009899 |
| C-class != 5 and Area = 1 and LargestSpotSize = R and C-class = 0 and Activity != 1 | D | 0.006154 |
| C-class != 5 and LargestSpotSize = R and C-class != 0 and Evolution != 2 | D | 0.013636 |
| C-class = 5 | E | 0.017964 |
| LargestSpotSize = R and C-class = 0 | D | 0.062745 |
| LargestSpotSize != R and Area = 1 and SpotDistribution != O and HistComplex = 1 and LargestSpotSize != A | D | 0.012698 |
| LargestSpotSize != R and Area = 1 and SpotDistribution != O and M-class != 1 and Evolution != 2 and LargestSpotSize != S and Activity = 1 and C-class != 3 and C-class = 0 | D | 0.035165 |
| LargestSpotSize != R and Area = 1 and SpotDistribution != O and M-class != 1 and C-class = 1 and Evolution = 2 | D | 0.025370 |
| LargestSpotSize != R and Area = 1 and SpotDistribution = O and LargestSpotSize = S and Evolution != 2 | D | 0.015385 |
| LargestSpotSize != R and Area = 1 and Prev24Hour = 1 and SpotDistribution = O and Activity != 1 and LargestSpotSize = A | E | 0.037313 |
| LargestSpotSize != R and Area = 1 and C-class != 0 and LargestSpotSize = H | E | 0.017176 |
| LargestSpotSize != R and Area = 1 and SpotDistribution = O and Activity = 1 and C-class = 1 | E | 0.007937 |
| LargestSpotSize != R and Area = 1 and SpotDistribution = O and Activity = 1 | D | 0.058455 |
| SpotDistribution = O | C | 0.104898 |
| LargestSpotSize != R and M-class != 1 and Area = 1 and Evolution != 2 and Activity = 1 and LargestSpotSize = A and C-class != 1 | D | 0.008523 |
| LargestSpotSize != R and M-class != 1 and Area = 1 and Evolution != 2 and Activity = 1 and LargestSpotSize != A | D | 0.016903 |
| LargestSpotSize != R and M-class != 1 and Area = 1 and Evolution != 2 and C-class != 0 and Activity != 1 and C-class != 2 | E | 0.027108 |
| LargestSpotSize != R and M-class = 0 and Prev24Hour = 1 and C-class != 4 and Area = 1 and LargestSpotSize != K and C-class != 3 and C-class = 2 | F | 0.015789 |
| LargestSpotSize != R and M-class = 0 and Prev24Hour = 1 and C-class != 4 and Area = 1 and LargestSpotSize != A and LargestSpotSize != S | D | 0.017112 |
| LargestSpotSize != R and M-class = 0 and LargestSpotSize = K | F | 0.021978 |
| LargestSpotSize != R and M-class = 0 and C-class = 3 | E | 0.048924 |
| LargestSpotSize != R and M-class = 0 and LargestSpotSize != A and Activity = 1 | E | 0.045455 |
| LargestSpotSize != R and M-class = 0 and LargestSpotSize != A and Evolution = 2 | E | 0.018935 |
| LargestSpotSize != R and M-class = 0 and LargestSpotSize = A and C-class != 1 and Activity != 1 and Evolution = 2 | F | 0.031133 |
| LargestSpotSize != R and M-class = 0 and LargestSpotSize = A and C-class != 1 and C-class = 0 and Activity = 1 | D | 0.047337 |
| LargestSpotSize != R and M-class = 0 and LargestSpotSize = A and C-class != 1 and C-class = 0 | D | 0.020292 |
| LargestSpotSize != R and Evolution = 3 and LargestSpotSize = A | D | 0.035714 |
| LargestSpotSize != R and Evolution != 3 | D | 0.051429 |
| LargestSpotSize = R | C | 0.098000 |
|  | E | 0.464286 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| SpotDistribution = I and Evolution = 2 and C-class = 1 | F | 0.003343 |
| Area = 2 | F | 0.003338 |
| LargestSpotSize = A and Activity = 2 | E | 0.007142 |
| LargestSpotSize = X | B | 0.138678 |
| SpotDistribution = O and HistComplex = 1 | C | 0.125650 |
| SpotDistribution = O and C-class = 0 and Evolution = 2 | C | 0.016380 |
| SpotDistribution = I | D | 0.137861 |
| SpotDistribution = O and C-class = 0 | D | 0.129482 |
|  | H | 0.659292 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

largestspotsize|spotdistribution|class
---|---|---
h|c|h
r|c|d
a|c|e
k|c|e
h|i|d
s|i|d
r|i|d
k|i|d
a|i|d
x|i|b
a|o|d
s|o|c
r|o|c
h|o|d
x|o|b
k|x|h
h|x|h
a|x|h
r|x|h
s|x|h

## JRip

Decision list:

rules | predicted class
---|---
(SpotDistribution = I) and (Evolution = 2) and (C-class = 1)|F (16.0/9.0)
(Area = 2)|F (21.0/13.0)
(LargestSpotSize = A) and (Activity = 2)|E (45.0/28.0)
(LargestSpotSize = X)|B (127.0/0.0)
(SpotDistribution = O) and (HistComplex = 1)|C (203.0/72.0)
(SpotDistribution = O) and (C-class = 0) and (Evolution = 2)|C (41.0/18.0)
(SpotDistribution = I)|D (137.0/51.0)
(SpotDistribution = O) and (C-class = 0)|D (40.0/18.0)
|H (327.0/30.0)


## PART

Decision list:

rules | predicted class
---|---
SpotDistribution = X|H (298.0)
LargestSpotSize = X|B (128.0)
Area != 1 AND LargestSpotSize != A AND M-class = 0 AND Prev24Hour != 1|E (5.0/1.0)
Area != 1 AND LargestSpotSize != A AND M-class = 0 AND SpotDistribution = C|F (4.0/1.0)
SpotDistribution = O AND LargestSpotSize != H AND LargestSpotSize != A AND HistComplex = 1 AND C-class != 2 AND Activity = 1 AND C-class = 1 AND LargestSpotSize = R|D (6.0/2.0)
SpotDistribution = O AND LargestSpotSize != H AND LargestSpotSize != A AND HistComplex = 1 AND C-class != 2 AND Activity = 1 AND LargestSpotSize = R AND Evolution != 1 AND Evolution != 2|C (58.0/20.0)
SpotDistribution = O AND LargestSpotSize != H AND LargestSpotSize != A AND HistComplex = 1 AND C-class != 2 AND Activity != 1 AND Prev24Hour = 1 AND Evolution = 2|C (10.0/2.0)
SpotDistribution = O AND LargestSpotSize != H AND LargestSpotSize != A AND HistComplex = 1 AND C-class != 2 AND LargestSpotSize = R AND Evolution != 1|C (31.0/7.0)
Area != 1 AND LargestSpotSize != A AND SpotDistribution != I|E (5.0)
SpotDistribution = O AND LargestSpotSize != H AND LargestSpotSize != A AND HistComplex = 1 AND C-class != 2 AND LargestSpotSize != R AND C-class != 0 AND C-class = 1 AND Evolution != 2|D (6.0/3.0)
SpotDistribution = O AND LargestSpotSize != H AND C-class = 0 AND LargestSpotSize != A AND HistComplex = 1 AND Prev24Hour = 1 AND LargestSpotSize != R AND Activity = 1 AND Evolution != 2|C (34.0/13.0)
Area != 1 AND LargestSpotSize = A|F (3.0)
SpotDistribution = O AND LargestSpotSize != H AND C-class = 0 AND Evolution != 2 AND LargestSpotSize = R AND HistComplex != 1|D (5.0/2.0)
SpotDistribution = O AND LargestSpotSize != H AND LargestSpotSize = R AND Evolution != 1|C (10.0/3.0)
SpotDistribution = O AND LargestSpotSize != R AND LargestSpotSize != H AND C-class = 0 AND Evolution != 1 AND LargestSpotSize != A AND HistComplex = 1 AND Prev24Hour = 1|C (19.0/4.0)
SpotDistribution = C AND C-class = 0 AND LargestSpotSize = A|E (5.0/2.0)
Area != 1 AND Activity = 1|E (3.0/1.0)
LargestSpotSize = K AND SpotDistribution = I AND Area = 1 AND Evolution != 2|D (8.0)
LargestSpotSize = K AND SpotDistribution = I AND Activity = 1|F (3.0/1.0)
Activity = 1 AND M-class = 1 AND SpotDistribution = I AND C-class = 0|D (4.0)
Activity = 1 AND M-class = 1 AND LargestSpotSize != S AND Evolution = 3|E (3.0)
Activity = 1 AND SpotDistribution != O AND HistComplex = 1 AND LargestSpotSize = A AND Evolution != 2|D (12.0/2.0)
Activity = 1 AND SpotDistribution = O AND LargestSpotSize = H AND Evolution != 2 AND HistComplex != 1|D (6.0/2.0)
Activity = 1 AND SpotDistribution = O AND LargestSpotSize != H AND LargestSpotSize != R AND Evolution != 1 AND M-class != 1 AND C-class != 2 AND C-class != 1 AND C-class = 0 AND HistComplex = 1 AND Evolution != 2|D (9.0/5.0)
Activity = 1 AND SpotDistribution = O AND LargestSpotSize != H AND LargestSpotSize != R AND Evolution = 1|D (7.0/3.0)
SpotDistribution = O AND Evolution != 1 AND LargestSpotSize != H AND LargestSpotSize != A AND C-class != 2 AND C-class = 1 AND HistComplex != 1|D (6.0/2.0)
SpotDistribution = O AND Evolution != 1 AND LargestSpotSize != H AND C-class = 0 AND Activity = 1 AND HistComplex != 1 AND Evolution != 2 AND LargestSpotSize = A|D (12.0/6.0)
SpotDistribution = O AND Evolution = 1|C (5.0)
SpotDistribution = O AND LargestSpotSize != H AND LargestSpotSize != A AND C-class != 2 AND C-class = 3|D (4.0/2.0)
SpotDistribution = O AND LargestSpotSize != H AND C-class = 0 AND HistComplex = 1 AND LargestSpotSize = A AND Activity = 1|D (5.0/2.0)
SpotDistribution = O AND LargestSpotSize != H AND C-class = 0 AND LargestSpotSize != A AND HistComplex != 1 AND Evolution != 2 AND Activity = 1|C (8.0/3.0)
SpotDistribution = O AND LargestSpotSize != H AND Evolution != 2 AND M-class != 1 AND C-class != 1 AND C-class = 0 AND LargestSpotSize = A|D (4.0/1.0)
SpotDistribution = O AND LargestSpotSize != H AND C-class = 0 AND HistComplex != 1 AND Evolution = 2 AND LargestSpotSize != A AND Activity = 1|C (17.0/8.0)
HistComplex = 1 AND LargestSpotSize != H AND Activity = 1 AND C-class != 2 AND LargestSpotSize = A AND SpotDistribution != O|D (4.0)
HistComplex = 1 AND LargestSpotSize != H AND Evolution != 2 AND LargestSpotSize = A AND C-class != 2|D (5.0)
HistComplex = 1 AND LargestSpotSize != H AND LargestSpotSize != A AND Prev24Hour = 1 AND Activity = 1 AND Evolution != 2 AND C-class = 2|D (4.0/1.0)
SpotDistribution = O AND LargestSpotSize != H AND C-class = 0 AND HistComplex != 1 AND Evolution = 2 AND LargestSpotSize = A AND Activity = 1|C (10.0/4.0)
HistComplex = 1 AND LargestSpotSize != H AND LargestSpotSize != A AND SpotDistribution = I AND Activity = 1 AND C-class = 0 AND LargestSpotSize != R|D (10.0/4.0)
HistComplex = 1 AND LargestSpotSize = H|C (4.0/2.0)
HistComplex = 1 AND C-class = 1 AND SpotDistribution = O|C (4.0/1.0)
LargestSpotSize = R AND Activity = 1 AND C-class = 0 AND Evolution != 2 AND HistComplex != 1|D (5.0/1.0)
LargestSpotSize = R AND Activity = 1 AND C-class = 0 AND Evolution != 2|D (4.0/1.0)
HistComplex = 1 AND SpotDistribution = O|E (5.0/2.0)
C-class != 5 AND Area = 1 AND LargestSpotSize = R AND C-class = 0 AND Activity != 1|D (4.0/2.0)
C-class != 5 AND LargestSpotSize = R AND C-class != 0 AND Evolution != 2|D (4.0/1.0)
C-class = 5|E (3.0)
LargestSpotSize = R AND C-class = 0|D (3.0)
LargestSpotSize != R AND Area = 1 AND SpotDistribution != O AND HistComplex = 1 AND LargestSpotSize != A|D (6.0/2.0)
LargestSpotSize != R AND Area = 1 AND SpotDistribution != O AND M-class != 1 AND Evolution != 2 AND LargestSpotSize != S AND Activity = 1 AND C-class != 3 AND C-class = 0|D (12.0/4.0)
LargestSpotSize != R AND Area = 1 AND SpotDistribution != O AND M-class != 1 AND C-class = 1 AND Evolution = 2|D (10.0/4.0)
LargestSpotSize != R AND Area = 1 AND SpotDistribution = O AND LargestSpotSize = S AND Evolution != 2|D (4.0/2.0)
LargestSpotSize != R AND Area = 1 AND Prev24Hour = 1 AND SpotDistribution = O AND Activity != 1 AND LargestSpotSize = A|E (4.0)
LargestSpotSize != R AND Area = 1 AND C-class != 0 AND LargestSpotSize = H|E (4.0/1.0)
LargestSpotSize != R AND Area = 1 AND SpotDistribution = O AND Activity = 1 AND C-class = 1|E (5.0/2.0)
LargestSpotSize != R AND Area = 1 AND SpotDistribution = O AND Activity = 1|D (4.0/1.0)
SpotDistribution = O|C (4.0/1.0)
LargestSpotSize != R AND M-class != 1 AND Area = 1 AND Evolution != 2 AND Activity = 1 AND LargestSpotSize = A AND C-class != 1|D (4.0/1.0)
LargestSpotSize != R AND M-class != 1 AND Area = 1 AND Evolution != 2 AND Activity = 1 AND LargestSpotSize != A|D (7.0/2.0)
LargestSpotSize != R AND M-class != 1 AND Area = 1 AND Evolution != 2 AND C-class != 0 AND Activity != 1 AND C-class != 2|E (4.0/1.0)
LargestSpotSize != R AND M-class = 0 AND Prev24Hour = 1 AND C-class != 4 AND Area = 1 AND LargestSpotSize != K AND C-class != 3 AND C-class = 2|F (6.0/3.0)
LargestSpotSize != R AND M-class = 0 AND Prev24Hour = 1 AND C-class != 4 AND Area = 1 AND LargestSpotSize != A AND LargestSpotSize != S|D (7.0/3.0)
LargestSpotSize != R AND M-class = 0 AND LargestSpotSize = K|F (5.0/1.0)
LargestSpotSize != R AND M-class = 0 AND C-class = 3|E (4.0/1.0)
LargestSpotSize != R AND M-class = 0 AND LargestSpotSize != A AND Activity = 1|E (4.0/1.0)
LargestSpotSize != R AND M-class = 0 AND LargestSpotSize != A AND Evolution = 2|E (4.0/2.0)
LargestSpotSize != R AND M-class = 0 AND LargestSpotSize = A AND C-class != 1 AND Activity != 1 AND Evolution = 2|F (9.0/5.0)
LargestSpotSize != R AND M-class = 0 AND LargestSpotSize = A AND C-class != 1 AND C-class = 0 AND Activity = 1|D (17.0/10.0)
LargestSpotSize != R AND M-class = 0 AND LargestSpotSize = A AND C-class != 1 AND C-class = 0|D (5.0/3.0)
LargestSpotSize != R AND Evolution = 3 AND LargestSpotSize = A|D (5.0/1.0)
LargestSpotSize != R AND Evolution != 3|D (5.0/1.0)
LargestSpotSize = R|C (3.0/1.0)
|E (3.0/1.0)


## J48 Decision Tree

* SpotDistribution = X: H (298.0)
* SpotDistribution = O
	* LargestSpotSize = A
		* C-class = 0
			* Evolution = 1: D (1.0)
			* Evolution = 2: C (18.0/9.0)
			* Evolution = 3: D (25.0/12.0)
		* C-class = 1: D (9.0/5.0)
		* C-class = 2: D (2.0/1.0)
		* C-class = 3: E (1.0)
		* C-class = 4: E (2.0)
		* C-class = 5: D (0.0)
		* C-class = 6: D (0.0)
		* C-class = 7: D (0.0)
		* C-class = 8: D (0.0)
	* LargestSpotSize = R: C (117.0/38.0)
	* LargestSpotSize = S: C (125.0/53.0)
	* LargestSpotSize = X: B (114.0)
	* LargestSpotSize = K: C (0.0)
	* LargestSpotSize = H: D (15.0/8.0)
* SpotDistribution = I
	* LargestSpotSize = A: D (99.0/43.0)
	* LargestSpotSize = R: D (23.0/8.0)
	* LargestSpotSize = S: D (39.0/19.0)
	* LargestSpotSize = X: B (14.0)
	* LargestSpotSize = K: D (23.0/11.0)
	* LargestSpotSize = H: E (3.0/1.0)
* SpotDistribution = C: E (29.0/11.0)


## SimpleCart Decision Tree

		* SpotDistribution=(C)|(I)|(O)
	* LargestSpotSize=(X): B(128.0/0.0)
	* LargestSpotSize!=(X)
			* SpotDistribution=(C)|(I)
			* Area=(2): E(12.0/10.0)
			* Area!=(2)
				* Evolution=(2)
								* C-class=(0)|(5)|(6)|(7): D(25.0/26.0)
								* C-class!=(0)|(5)|(6)|(7): F(13.0/17.0)
				* Evolution!=(2)
					* SpotDistribution=(C): E(6.0/3.0)
					* SpotDistribution!=(C)
							* LargestSpotSize=(S)|(R): D(26.0/16.0)
							* LargestSpotSize!=(S)|(R)
							* LargestSpotSize=(K): D(8.0/0.0)
							* LargestSpotSize!=(K): D(37.0/17.0)
			* SpotDistribution!=(C)|(I)
						* LargestSpotSize=(S)|(R)|(X)|(K)
				* HistComplex=(2): C(29.0/32.0)
				* HistComplex!=(2)
									* C-class=(0)|(4)|(6)|(7)|(8)
						* Evolution=(3): C(61.0/33.0)
						* Evolution!=(3)
							* Activity=(2): C(9.0/2.0)
							* Activity!=(2)
								* LargestSpotSize=(S): C(13.0/5.0)
								* LargestSpotSize!=(S): C(27.0/7.0)
									* C-class!=(0)|(4)|(6)|(7)|(8): C(12.0/12.0)
						* LargestSpotSize!=(S)|(R)|(X)|(K)
								* C-class=(0)|(5)|(6)|(7)|(8)
					* LargestSpotSize=(H): D(7.0/4.0)
					* LargestSpotSize!=(H): D(19.0/25.0)
								* C-class!=(0)|(5)|(6)|(7)|(8): E(10.0/8.0)
		* SpotDistribution!=(C)|(I)|(O): H(298.0/0.0)


