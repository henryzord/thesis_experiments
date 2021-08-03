# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 0 | 0.935345 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| gpuls <= 1328 and nbumps <= 2.5 and gpuls > 32.5 and nbumps <= 1.5 and gdenergy <= 104.5 and gdenergy <= 69.5 and gdpuls > -74.5 and gdenergy > -72.5 and gdenergy > -59.5 and genergy <= 55925 and genergy <= 39985 and gdenergy > -54.5 and genergy <= 17635 | 0 | 0.757758 |
| gpuls <= 1328 and nbumps <= 2.5 | 0 | 0.900309 |
| gdenergy <= 131.5 and genergy <= 1062020 and nbumps > 0.5 and maxenergy <= 25000 and gpuls <= 378.5 and genergy > 20960 | 0 | 0.231022 |
| genergy <= 1062020 and gdenergy <= 131.5 and nbumps > 0.5 and maxenergy > 9500 and gdenergy <= 67.5 and gdpuls <= 57.5 and gdenergy <= 46 | 0 | 0.222368 |
| genergy <= 1062020 and gdenergy <= 131.5 and nbumps > 0.5 and gdpuls > 22 and gpuls <= 2902.5 and nbumps3 <= 3.5 | 0 | 0.240484 |
| gdenergy <= 131.5 and genergy > 1062020 | 0 | 0.158790 |
| gdenergy <= 131.5 and nbumps > 0.5 and ghazard = a and gpuls > 153.5 and gdenergy > -44.5 and gpuls <= 2164 and gpuls > 1540 | 0 | 0.084048 |
| gdenergy > 131.5 | 0 | 0.110806 |
| nbumps > 0.5 and maxenergy > 850 and genergy <= 784250 and gpuls > 153.5 and gdenergy > -43.5 and maxenergy > 1500 and genergy <= 666375 and gpuls <= 1404 and gdenergy > -41.5 and energy > 3550 and nbumps2 > 0.5 and genergy > 19040 and energy > 4050 and energy > 6100 and genergy > 32550 | 1 | 0.176835 |
| nbumps > 0.5 and maxenergy > 850 and genergy <= 784250 and maxenergy <= 6500 and gpuls <= 1326.5 | 0 | 0.116445 |
| nbumps > 0.5 | 1 | 0.700916 |
|  | 0 | 0.513889 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| nbumps >= 3 and gpuls >= 382 and gdpuls <= 21 and gdpuls >= 2 and energy <= 35900 | 1 | 0.004704 |
| nbumps >= 2 and gdenergy <= -30 and gpuls >= 768 and energy <= 12700 | 1 | 0.003272 |
|  | 0 | 0.946358 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

class
---
0

## JRip

Decision list:

rules | predicted class
---|---
(nbumps >= 3) and (gpuls >= 382) and (gdpuls <= 21) and (gdpuls >= 2) and (energy <= 35900)|1 (25.0/9.0)
(nbumps >= 2) and (gdenergy <= -30) and (gpuls >= 768) and (energy <= 12700)|1 (17.0/6.0)
|0 (2278.0/123.0)


## PART

Decision list:

rules | predicted class
---|---
gpuls <= 1328 AND nbumps <= 2.5 AND gpuls > 32.5 AND nbumps <= 1.5 AND gdenergy <= 104.5 AND gdenergy <= 69.5 AND gdpuls > -74.5 AND gdenergy > -72.5 AND gdenergy > -59.5 AND genergy <= 55925 AND genergy <= 39985 AND gdenergy > -54.5 AND genergy <= 17635|0 (391.0/3.0)
gpuls <= 1328 AND nbumps <= 2.5|0 (1156.0/48.0)
gdenergy <= 131.5 AND genergy <= 1062020 AND nbumps > 0.5 AND maxenergy <= 25000 AND gpuls <= 378.5 AND genergy > 20960|0 (41.0/3.0)
genergy <= 1062020 AND gdenergy <= 131.5 AND nbumps > 0.5 AND maxenergy > 9500 AND gdenergy <= 67.5 AND gdpuls <= 57.5 AND gdenergy <= 46|0 (47.0/6.0)
genergy <= 1062020 AND gdenergy <= 131.5 AND nbumps > 0.5 AND gdpuls > 22 AND gpuls <= 2902.5 AND nbumps3 <= 3.5|0 (53.0/6.0)
gdenergy <= 131.5 AND genergy > 1062020|0 (29.0/1.0)
gdenergy <= 131.5 AND nbumps > 0.5 AND ghazard = a AND gpuls > 153.5 AND gdenergy > -44.5 AND gpuls <= 2164 AND gpuls > 1540|0 (21.0/5.0)
gdenergy > 131.5|0 (19.0)
nbumps > 0.5 AND maxenergy > 850 AND genergy <= 784250 AND gpuls > 153.5 AND gdenergy > -43.5 AND maxenergy > 1500 AND genergy <= 666375 AND gpuls <= 1404 AND gdenergy > -41.5 AND energy > 3550 AND nbumps2 > 0.5 AND genergy > 19040 AND energy > 4050 AND energy > 6100 AND genergy > 32550|1 (17.0/6.0)
nbumps > 0.5 AND maxenergy > 850 AND genergy <= 784250 AND maxenergy <= 6500 AND gpuls <= 1326.5|0 (32.0/8.0)
nbumps > 0.5|1 (34.0/6.0)
|0 (16.0/1.0)


## SimpleCart Decision Tree

* : 0(2170.0/150.0)


