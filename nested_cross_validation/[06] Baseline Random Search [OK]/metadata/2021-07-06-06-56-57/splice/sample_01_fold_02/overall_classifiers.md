# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| POS30 != G and POS35 != G | N | 0.378117 |
| POS30 = G and POS32 = T and POS31 = G and POS35 = G | EI | 0.167404 |
| POS30 = G and POS32 != T and POS29 = A and POS28 != G and POS28 != A and POS25 != G | IE | 0.154727 |
| POS30 = G and POS32 != T and POS29 != A | N | 0.132692 |
| POS30 != G and POS35 = G and POS32 != T | N | 0.115955 |
| POS30 = G and POS32 = T and POS31 != G and POS29 = A | IE | 0.049739 |
| POS30 != G and POS35 = G and POS32 = T and POS31 = G and POS34 = A | EI | 0.049284 |
| POS30 != G and POS35 = G and POS32 = T and POS31 != G | N | 0.038997 |
| POS30 = G and POS32 = T and POS31 = G and POS35 != G and POS29 = A and POS33 != A and POS28 != A | IE | 0.025222 |
| POS30 = G and POS32 = T and POS31 != G and POS29 != A | N | 0.030218 |
| POS30 = G and POS32 = T and POS31 = G and POS35 != G and POS29 = A and POS33 = A | EI | 0.022095 |
| POS30 = G and POS32 != T and POS29 = A and POS28 = G | N | 0.018692 |
| POS30 = G and POS32 != T and POS29 = A and POS28 != G and POS28 = A and POS21 != T | N | 0.017308 |
| POS30 != A and POS32 != A and POS31 != A and POS35 != A | EI | 0.130819 |
| POS30 = G and POS32 = T and POS31 = G and POS35 != G and POS29 != A and POS33 != A | N | 0.006911 |
| POS30 = G and POS32 != T and POS29 = A and POS28 != G and POS28 != A and POS25 = G and POS41 = C | IE | 0.005474 |
| POS30 != G and POS35 = G and POS32 = T and POS31 = G and POS34 != A and POS4 = A | N | 0.005309 |
| POS30 = G and POS32 != T and POS29 = A and POS28 != G and POS28 != A and POS25 = G and POS41 != C and POS22 != C | N | 0.005154 |
| POS30 = G and POS32 != T and POS29 = A and POS28 != G and POS28 != A and POS25 = G and POS41 != C and POS22 = C | IE | 0.002663 |
| POS30 = G and POS32 != T and POS29 = A and POS28 != G and POS28 = A and POS21 = T | IE | 0.002041 |
| POS30 = A and POS35 != R and POS32 != A and POS31 != T | EI | 0.005805 |
| POS30 != A and POS32 != A and POS31 != A and POS35 != T | EI | 0.131043 |
| POS30 != A and POS32 = A and POS29 != C and POS28 = A | N | 0.043154 |
| POS30 != A and POS32 != A and POS31 = A and POS29 != C | IE | 0.033617 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| POS30 != G and POS35 != G and POS13 != C and POS51 != A | N | 0.275591 |
| POS32 != T and POS29 != A and POS59 != G and POS56 != G and POS9 != G | N | 0.147095 |
| POS32 != T and POS29 != A and POS59 = G and POS50 != C | N | 0.075687 |
| POS31 != G and POS30 != G and POS32 != G and POS2 != A | N | 0.114249 |
| POS32 != T and POS29 != A and POS59 != G and POS5 != C and POS17 != A | N | 0.053498 |
| POS32 != T and POS30 != G and POS12 != A and POS6 != A | N | 0.035639 |
| POS32 != T and POS29 != A and POS22 != T and POS12 != C and POS7 != T | N | 0.022663 |
| POS32 != T and POS28 = G and POS54 != C | N | 0.023355 |
| POS32 != T and POS29 = A and POS28 != A and POS30 = G and POS28 != G and POS25 != G and POS26 != A and POS25 != A and POS19 != A and POS24 != G and POS20 != A and POS13 != A and POS16 != A | IE | 0.223980 |
| POS31 != G and POS29 != A and POS32 = T | N | 0.056075 |
| POS31 != G and POS30 = G and POS28 = A and POS19 != C | N | 0.022867 |
| POS31 != G and POS30 = G and POS29 = A and POS28 != G and POS24 != A and POS24 != G and POS60 != T and POS26 != G and POS19 != G and POS25 != A | IE | 0.123173 |
| POS32 = T and POS31 != G and POS21 != G and POS18 != A and POS53 != A and POS8 != C | IE | 0.030023 |
| POS32 = T and POS31 = G and POS35 = G and POS33 != C and POS34 != T and POS33 != T and POS34 = A and POS6 != A | EI | 0.449032 |
| POS32 != T and POS29 = A and POS30 = G and POS28 != G and POS21 != A and POS28 != A and POS23 != G and POS21 != G and POS13 != G and POS12 != A and POS16 != G | IE | 0.136842 |
| POS32 != T and POS29 = A and POS30 != G | N | 0.016529 |
| POS32 != T and POS29 = A and POS22 = A and POS4 = C | N | 0.014754 |
| POS31 != G and POS30 = G and POS25 = G and POS26 = G | N | 0.018149 |
| POS32 != T and POS29 = A and POS22 = G and POS8 != C | N | 0.011700 |
| POS31 != G and POS30 = G and POS10 = T and POS6 = T | IE | 0.011836 |
| POS31 != G and POS30 = G and POS10 != T and POS25 = T and POS3 != T | IE | 0.011790 |
| POS32 = T and POS31 != G and POS34 != C | N | 0.015922 |
| POS32 = T and POS31 = G and POS30 = T and POS35 = G | EI | 0.023068 |
| POS30 != T and POS32 = T and POS31 = G and POS30 != C and POS29 != A and POS54 != A and POS35 != T and POS36 != C and POS27 != T | EI | 0.197740 |
| POS30 = T | N | 0.030637 |
| POS32 = T and POS29 != A and POS33 = A and POS58 = T | EI | 0.039286 |
| POS29 != A and POS35 != C and POS51 != A and POS53 != G and POS1 != A | EI | 0.017647 |
| POS32 != T and POS35 != G and POS23 != A and POS10 != A and POS8 != A and POS42 != A and POS12 = A | IE | 0.057602 |
| POS29 != A and POS6 != A and POS35 != T and POS9 = G | N | 0.026506 |
| POS32 = T and POS29 != G and POS31 = G and POS29 = A and POS28 = A and POS35 != C and POS1 != A | EI | 0.196610 |
| POS29 != G and POS32 = T and POS29 = A and POS31 = G and POS28 = G and POS20 != C | EI | 0.125461 |
| POS29 != G and POS32 != T and POS41 = A | N | 0.032803 |
| POS29 = G | N | 0.030969 |
| POS32 != T and POS25 != A and POS35 != G and POS36 = C | IE | 0.066021 |
| POS32 = T and POS30 = G and POS28 != G and POS28 = A and POS35 = G | EI | 0.066667 |
| POS32 = T and POS30 = G and POS28 != G and POS28 != A and POS31 = G and POS33 = A and POS34 != T and POS51 != A and POS19 != G | EI | 0.132743 |
| POS28 = G | EI | 0.026717 |
| POS32 = T and POS30 = G and POS28 != A and POS31 = G and POS35 = G and POS36 = T and POS20 != C | EI | 0.075472 |
| POS30 = G and POS31 != G and POS32 != T | N | 0.051220 |
| POS30 = G and POS28 != A and POS32 != G and POS23 = T and POS9 != G and POS14 != G | IE | 0.276187 |
| POS30 = G and POS32 = G | IE | 0.084556 |
| POS30 = G and POS18 = A and POS49 = G | EI | 0.097512 |
| POS30 = G and POS28 != A and POS32 = T and POS26 != A and POS18 != G and POS35 != G and POS19 != G and POS8 != T | IE | 0.250000 |
| POS30 = G and POS28 != A and POS32 = T and POS28 = C and POS21 != A and POS22 != A and POS7 != T and POS42 != A and POS59 != G and POS26 != C | EI | 0.093750 |
| POS30 != G | EI | 0.041344 |
| POS22 = A and POS5 = T | EI | 0.086806 |
| POS24 = A | EI | 0.093629 |
| POS19 != A and POS28 != A and POS15 != G and POS58 != G and POS37 != G | IE | 0.238237 |
| POS8 = C | EI | 0.088235 |
| POS14 = C | IE | 0.086538 |
| POS34 != C and POS8 = T | IE | 0.180556 |
| POS17 != T | N | 0.377220 |
|  | IE | 0.342105 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| POS29 = A and POS28 = C and POS30 = G and POS19 = T and POS20 = C | IE | 0.042703 |
| POS29 = A and POS28 = C and POS20 = T and POS30 = G and POS24 = T | IE | 0.048164 |
| POS29 = A and POS30 = G and POS21 = T and POS26 = T and POS18 = T | IE | 0.026413 |
| POS29 = A and POS28 = C and POS24 = C and POS30 = G and POS23 = T | IE | 0.031548 |
| POS29 = A and POS30 = G and POS28 = T | IE | 0.038409 |
| POS28 = C and POS29 = A and POS30 = G and POS32 = G | IE | 0.018769 |
| POS28 = C and POS29 = A and POS30 = G and POS17 = C and POS60 = G | IE | 0.010907 |
| POS29 = A and POS28 = C and POS23 = C and POS32 = A and POS30 = G | IE | 0.014961 |
| POS29 = A and POS28 = C and POS30 = G and POS22 = C and POS26 = C and POS19 = T | IE | 0.005056 |
| POS29 = A and POS28 = C and POS14 = T and POS16 = T | IE | 0.006334 |
| POS29 = A and POS28 = C and POS23 = C and POS1 = T and POS60 = C | IE | 0.003088 |
| POS29 = A and POS28 = C and POS30 = G and POS33 = C and POS11 = C | IE | 0.003268 |
| POS29 = A and POS28 = C and POS35 = C and POS21 = T and POS30 = G | IE | 0.004697 |
| POS29 = A and POS28 = C and POS26 = T and POS39 = G and POS44 = A | IE | 0.001908 |
| POS29 = A and POS22 = T and POS17 = T and POS60 = G and POS6 = T | IE | 0.001466 |
| POS29 = A and POS28 = C and POS33 = T and POS57 = G | IE | 0.001728 |
| POS29 = A and POS32 = C and POS16 = C and POS30 = G and POS48 = G | IE | 0.003656 |
| POS29 = A and POS25 = C and POS14 = C and POS5 = C | IE | 0.002060 |
| POS29 = A and POS53 = T and POS20 = C and POS28 = C and POS36 = A | IE | 0.001832 |
| POS29 = A and POS52 = A and POS19 = C and POS25 = T | IE | 0.001432 |
| POS31 = G and POS32 = T and POS35 = G and POS34 = A | EI | 0.225245 |
| POS31 = G and POS32 = T and POS30 = G and POS35 = G and POS29 = A | EI | 0.059782 |
| POS31 = G and POS32 = T and POS30 = G and POS33 = A | EI | 0.054278 |
| POS31 = G and POS32 = T and POS30 = G and POS36 = T and POS33 = G | EI | 0.013717 |
| POS31 = G and POS32 = T and POS29 = A and POS28 = C and POS1 = C | EI | 0.002644 |
| POS31 = G and POS32 = T and POS29 = A and POS43 = G | EI | 0.004113 |
| POS31 = G and POS32 = T and POS35 = G and POS12 = A | EI | 0.003594 |
| POS31 = G and POS30 = G and POS38 = C and POS56 = G | EI | 0.002067 |
| POS31 = G and POS55 = G and POS40 = T and POS51 = C and POS46 = G | EI | 0.001983 |
|  | N | 0.981555 |


# Text representation of classifiers as-is

## JRip

Decision list:

rules | predicted class
---|---
(POS29 = A) and (POS28 = C) and (POS30 = G) and (POS19 = T) and (POS20 = C)|IE (107.0/5.0)
(POS29 = A) and (POS28 = C) and (POS20 = T) and (POS30 = G) and (POS24 = T)|IE (122.0/6.0)
(POS29 = A) and (POS30 = G) and (POS21 = T) and (POS26 = T) and (POS18 = T)|IE (65.0/3.0)
(POS29 = A) and (POS28 = C) and (POS24 = C) and (POS30 = G) and (POS23 = T)|IE (73.0/1.0)
(POS29 = A) and (POS30 = G) and (POS28 = T)|IE (122.0/19.0)
(POS28 = C) and (POS29 = A) and (POS30 = G) and (POS32 = G)|IE (57.0/7.0)
(POS28 = C) and (POS29 = A) and (POS30 = G) and (POS17 = C) and (POS60 = G)|IE (31.0/2.0)
(POS29 = A) and (POS28 = C) and (POS23 = C) and (POS32 = A) and (POS30 = G)|IE (36.0/1.0)
(POS29 = A) and (POS28 = C) and (POS30 = G) and (POS22 = C) and (POS26 = C) and (POS19 = T)|IE (13.0/1.0)
(POS29 = A) and (POS28 = C) and (POS14 = T) and (POS16 = T)|IE (24.0/5.0)
(POS29 = A) and (POS28 = C) and (POS23 = C) and (POS1 = T) and (POS60 = C)|IE (10.0/1.0)
(POS29 = A) and (POS28 = C) and (POS30 = G) and (POS33 = C) and (POS11 = C)|IE (13.0/3.0)
(POS29 = A) and (POS28 = C) and (POS35 = C) and (POS21 = T) and (POS30 = G)|IE (12.0/0.0)
(POS29 = A) and (POS28 = C) and (POS26 = T) and (POS39 = G) and (POS44 = A)|IE (5.0/0.0)
(POS29 = A) and (POS22 = T) and (POS17 = T) and (POS60 = G) and (POS6 = T)|IE (4.0/0.0)
(POS29 = A) and (POS28 = C) and (POS33 = T) and (POS57 = G)|IE (9.0/2.0)
(POS29 = A) and (POS32 = C) and (POS16 = C) and (POS30 = G) and (POS48 = G)|IE (8.0/0.0)
(POS29 = A) and (POS25 = C) and (POS14 = C) and (POS5 = C)|IE (7.0/1.0)
(POS29 = A) and (POS53 = T) and (POS20 = C) and (POS28 = C) and (POS36 = A)|IE (4.0/0.0)
(POS29 = A) and (POS52 = A) and (POS19 = C) and (POS25 = T)|IE (6.0/1.0)
(POS31 = G) and (POS32 = T) and (POS35 = G) and (POS34 = A)|EI (425.0/1.0)
(POS31 = G) and (POS32 = T) and (POS30 = G) and (POS35 = G) and (POS29 = A)|EI (90.0/1.0)
(POS31 = G) and (POS32 = T) and (POS30 = G) and (POS33 = A)|EI (95.0/7.0)
(POS31 = G) and (POS32 = T) and (POS30 = G) and (POS36 = T) and (POS33 = G)|EI (21.0/0.0)
(POS31 = G) and (POS32 = T) and (POS29 = A) and (POS28 = C) and (POS1 = C)|EI (7.0/1.0)
(POS31 = G) and (POS32 = T) and (POS29 = A) and (POS43 = G)|EI (11.0/2.0)
(POS31 = G) and (POS32 = T) and (POS35 = G) and (POS12 = A)|EI (8.0/1.0)
(POS31 = G) and (POS30 = G) and (POS38 = C) and (POS56 = G)|EI (7.0/2.0)
(POS31 = G) and (POS55 = G) and (POS40 = T) and (POS51 = C) and (POS46 = G)|EI (3.0/0.0)
|N (1475.0/24.0)


## PART

Decision list:

rules | predicted class
---|---
POS30 != G AND POS35 != G AND POS13 != C AND POS51 != A|N (525.0)
POS32 != T AND POS29 != A AND POS59 != G AND POS56 != G AND POS9 != G|N (238.0)
POS32 != T AND POS29 != A AND POS59 = G AND POS50 != C|N (113.0)
POS31 != G AND POS30 != G AND POS32 != G AND POS2 != A|N (178.0)
POS32 != T AND POS29 != A AND POS59 != G AND POS5 != C AND POS17 != A|N (78.0)
POS32 != T AND POS30 != G AND POS12 != A AND POS6 != A|N (51.0)
POS32 != T AND POS29 != A AND POS22 != T AND POS12 != C AND POS7 != T|N (32.0)
POS32 != T AND POS28 = G AND POS54 != C|N (33.0)
POS32 != T AND POS29 = A AND POS28 != A AND POS30 = G AND POS28 != G AND POS25 != G AND POS26 != A AND POS25 != A AND POS19 != A AND POS24 != G AND POS20 != A AND POS13 != A AND POS16 != A|IE (269.0)
POS31 != G AND POS29 != A AND POS32 = T|N (66.0)
POS31 != G AND POS30 = G AND POS28 = A AND POS19 != C|N (26.0)
POS31 != G AND POS30 = G AND POS29 = A AND POS28 != G AND POS24 != A AND POS24 != G AND POS60 != T AND POS26 != G AND POS19 != G AND POS25 != A|IE (118.0)
POS32 = T AND POS31 != G AND POS21 != G AND POS18 != A AND POS53 != A AND POS8 != C|IE (26.0)
POS32 = T AND POS31 = G AND POS35 = G AND POS33 != C AND POS34 != T AND POS33 != T AND POS34 = A AND POS6 != A|EI (348.0)
POS32 != T AND POS29 = A AND POS30 = G AND POS28 != G AND POS21 != A AND POS28 != A AND POS23 != G AND POS21 != G AND POS13 != G AND POS12 != A AND POS16 != G|IE (78.0)
POS32 != T AND POS29 = A AND POS30 != G|N (11.0/1.0)
POS32 != T AND POS29 = A AND POS22 = A AND POS4 = C|N (10.0/1.0)
POS31 != G AND POS30 = G AND POS25 = G AND POS26 = G|N (10.0)
POS32 != T AND POS29 = A AND POS22 = G AND POS8 != C|N (10.0/2.0)
POS31 != G AND POS30 = G AND POS10 = T AND POS6 = T|IE (9.0/2.0)
POS31 != G AND POS30 = G AND POS10 != T AND POS25 = T AND POS3 != T|IE (15.0/6.0)
POS32 = T AND POS31 != G AND POS34 != C|N (15.0/5.0)
POS32 = T AND POS31 = G AND POS30 = T AND POS35 = G|EI (15.0/5.0)
POS30 != T AND POS32 = T AND POS31 = G AND POS30 != C AND POS29 != A AND POS54 != A AND POS35 != T AND POS36 != C AND POS27 != T|EI (70.0)
POS30 = T|N (11.0/1.0)
POS32 = T AND POS29 != A AND POS33 = A AND POS58 = T|EI (11.0)
POS29 != A AND POS35 != C AND POS51 != A AND POS53 != G AND POS1 != A|EI (17.0/8.0)
POS32 != T AND POS35 != G AND POS23 != A AND POS10 != A AND POS8 != A AND POS42 != A AND POS12 = A|IE (20.0)
POS29 != A AND POS6 != A AND POS35 != T AND POS9 = G|N (10.0)
POS32 = T AND POS29 != G AND POS31 = G AND POS29 = A AND POS28 = A AND POS35 != C AND POS1 != A|EI (58.0)
POS29 != G AND POS32 = T AND POS29 = A AND POS31 = G AND POS28 = G AND POS20 != C|EI (34.0)
POS29 != G AND POS32 != T AND POS41 = A|N (16.0/3.0)
POS29 = G|N (15.0/4.0)
POS32 != T AND POS25 != A AND POS35 != G AND POS36 = C|IE (14.0)
POS32 = T AND POS30 = G AND POS28 != G AND POS28 = A AND POS35 = G|EI (14.0)
POS32 = T AND POS30 = G AND POS28 != G AND POS28 != A AND POS31 = G AND POS33 = A AND POS34 != T AND POS51 != A AND POS19 != G|EI (28.0)
POS28 = G|EI (16.0/7.0)
POS32 = T AND POS30 = G AND POS28 != A AND POS31 = G AND POS35 = G AND POS36 = T AND POS20 != C|EI (16.0)
POS30 = G AND POS31 != G AND POS32 != T|N (14.0/3.0)
POS30 = G AND POS28 != A AND POS32 != G AND POS23 = T AND POS9 != G AND POS14 != G|IE (40.0)
POS30 = G AND POS32 = G|IE (16.0/5.0)
POS30 = G AND POS18 = A AND POS49 = G|EI (14.0)
POS30 = G AND POS28 != A AND POS32 = T AND POS26 != A AND POS18 != G AND POS35 != G AND POS19 != G AND POS8 != T|IE (33.0)
POS30 = G AND POS28 != A AND POS32 = T AND POS28 = C AND POS21 != A AND POS22 != A AND POS7 != T AND POS42 != A AND POS59 != G AND POS26 != C|EI (15.0/3.0)
POS30 != G|EI (11.0/4.0)
POS22 = A AND POS5 = T|EI (10.0)
POS24 = A|EI (17.0/4.0)
POS19 != A AND POS28 != A AND POS15 != G AND POS58 != G AND POS37 != G|IE (16.0)
POS8 = C|EI (16.0/4.0)
POS14 = C|IE (13.0/6.0)
POS34 != C AND POS8 = T|IE (11.0/1.0)
POS17 != T|N (11.0/6.0)
|IE (9.0/3.0)


## J48 Decision Tree

* POS30 = G
	* POS32 = T
		* POS31 = G
			* POS35 = G: EI (483.0/23.0)
			* POS35 != G
				* POS29 = A
					* POS33 = A: EI (66.0/9.0)
					* POS33 != A
						* POS28 = A: EI (11.0/5.0)
						* POS28 != A: IE (87.0/17.0)
				* POS29 != A
					* POS33 = A: EI (16.0/3.0)
					* POS33 != A: N (15.0/3.0)
		* POS31 != G
			* POS29 = A: IE (137.0/12.0)
			* POS29 != A: N (43.0)
	* POS32 != T
		* POS29 = A
			* POS28 = G: N (32.0/3.0)
			* POS28 != G
				* POS28 = A
					* POS21 = T: IE (11.0/4.0)
					* POS21 != T: N (30.0/3.0)
				* POS28 != A
					* POS25 = G
						* POS41 = C: IE (12.0)
						* POS41 != C
							* POS22 = C: IE (11.0/3.0)
							* POS22 != C: N (14.0/4.0)
					* POS25 != G: IE (453.0/28.0)
		* POS29 != A: N (221.0/5.0)
* POS30 != G
	* POS35 = G
		* POS32 = T
			* POS31 = G
				* POS34 = A: EI (115.0/1.0)
				* POS34 != A
					* POS4 = A: N (11.0/2.0)
					* POS4 != A: EI (12.0/3.0)
			* POS31 != G: N (56.0)
		* POS32 != T: N (183.0/1.0)
	* POS35 != G: N (851.0/6.0)


## SimpleCart Decision Tree

		* POS30=(C)|(T)|(A)
					* POS35=(A)|(T)|(C)|(N)|(R): N(845.0/5.0)
					* POS35!=(A)|(T)|(C)|(N)|(R)
				* POS32=(G)|(C)|(A): N(182.0/1.0)
				* POS32!=(G)|(C)|(A)
					* POS31=(T)|(C)|(A): N(56.0/0.0)
					* POS31!=(T)|(C)|(A): EI(125.0/13.0)
		* POS30!=(C)|(T)|(A)
			* POS32=(G)|(C)|(A)
				* POS29=(T)|(G)|(C): N(216.0/5.0)
				* POS29!=(T)|(G)|(C)
				* POS28=(G)|(A): N(60.0/13.0)
				* POS28!=(G)|(A): IE(449.0/41.0)
			* POS32!=(G)|(C)|(A)
				* POS31=(T)|(C)|(A)
					* POS29=(T)|(G)|(C): N(43.0/0.0)
					* POS29!=(T)|(G)|(C): IE(125.0/12.0)
				* POS31!=(T)|(C)|(A)
					* POS35=(A)|(T)|(C)
							* POS33=(T)|(C)|(G)|(N)
						* POS28=(G)|(A): N(14.0/9.0)
						* POS28!=(G)|(A): IE(70.0/20.0)
							* POS33!=(T)|(C)|(G)|(N): EI(70.0/12.0)
					* POS35!=(A)|(T)|(C): EI(461.0/23.0)


