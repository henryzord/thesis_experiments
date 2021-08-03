# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| POS30 != G and POS35 != G | N | 0.376713 |
| POS30 = G and POS31 = G and POS32 = T | EI | 0.174975 |
| POS30 = G and POS32 != T and POS29 = A and POS28 != G and POS28 != A | IE | 0.160263 |
| POS30 = G and POS32 != T and POS29 != A | N | 0.133780 |
| POS30 != G and POS35 = G and POS32 != T | N | 0.119901 |
| POS30 = G and POS32 = T and POS31 != G and POS29 = A | IE | 0.049400 |
| POS30 != G and POS35 = G and POS32 = T and POS31 = G and POS34 = A | EI | 0.050113 |
| POS30 != G and POS35 = G and POS32 = T and POS31 != G | N | 0.038997 |
| POS30 = G and POS32 = T and POS31 != G and POS29 != A | N | 0.032258 |
| POS30 = G and POS32 = T and POS31 = G and POS35 != G and POS33 != A and POS29 = A and POS26 != A and POS28 != A | IE | 0.024926 |
| POS30 = G and POS32 != T and POS29 = A and POS28 = G | N | 0.018139 |
| POS30 = G and POS32 != T and POS29 = A and POS28 != G and POS28 = A | N | 0.013451 |
| POS30 != G and POS35 = G and POS32 = T and POS31 = G and POS34 != A and POS33 != A | N | 0.007400 |
| POS30 = G and POS32 = T and POS31 = G and POS35 != G and POS33 != A and POS29 != A | N | 0.005309 |
| POS30 = G and POS31 = C and POS32 = C | N | 0.012525 |
| POS30 != G and POS35 = G and POS32 = T and POS31 = G and POS34 != A and POS33 = A | EI | 0.003201 |
| POS30 = G and POS32 = T and POS31 = G and POS35 != G and POS33 != A and POS29 = A and POS26 = A and POS23 = T | IE | 0.002244 |
| POS30 = G and POS31 = C and POS32 = A | N | 0.010385 |
| POS30 = G and POS31 = C and POS32 = G | N | 0.005901 |
| POS30 = T and POS31 = G and POS32 = T | EI | 0.014683 |
| POS30 != A and POS32 != A and POS31 != A and POS35 = C and POS33 != N and POS18 != C and POS10 != A | IE | 0.018234 |
| POS30 != A and POS32 != A and POS31 = A and POS29 != C and POS28 = A | N | 0.024807 |
| POS30 != A and POS32 != A and POS31 = A and POS29 != C and POS28 = G | N | 0.028169 |
| POS30 != A and POS32 = A and POS29 != C and POS28 != A and POS25 = G and POS18 = G and POS38 = T | N | 0.004329 |
| POS30 != A and POS32 != A and POS31 = A and POS29 != C and POS28 != A and POS25 = A | IE | 0.000598 |
| POS30 = A and POS31 = G and POS32 = T | EI | 0.017752 |
| POS30 != A and POS32 != A and POS31 != A and POS35 != C and POS33 != C and POS34!=(T) and POS39!=(A) and POS49!=(A) | EI | 0.137701 |
| POS30 = G and POS31 = G and POS32 = C | IE | 0.025465 |
| POS30 = G and POS31 = T and POS32 = G | N | 0.012952 |
| POS30 = G and POS31 = T and POS32 = A | N | 0.004516 |
| POS30 != A and POS32 = A and POS29 != C and POS28 != A and POS25 = G and POS18 != A | IE | 0.000093 |
| POS30 = G and POS31 = G and POS32 = A | IE | 0.025420 |
| POS30 = G and POS31 = A and POS32 = A | IE | 0.013780 |
| POS30 = G and POS31 = A and POS32 = G | IE | 0.014920 |
| POS30 = G and POS31 = A and POS32 = C | IE | 0.012301 |
| POS30 != A and POS32 != A and POS31 != A and POS35 = C and POS33 != N and POS18 != C and POS10 != G | IE | 0.015896 |
| POS30 != A and POS32 != A and POS31 = A and POS29 != C and POS28 != A and POS25 != G | IE | 0.042039 |
| POS30 = G and POS31 = G and POS32 = G | IE | 0.021341 |
| POS30 != A and POS32 != A and POS31 != A and POS35 != C and POS33 = C | EI | 0.000573 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| POS30 != G and POS35 != G and POS33 != N and POS45 != G | N | 0.314796 |
| POS32 != T and POS29 != A | N | 0.258930 |
| POS31 != G and POS30 = G and POS29 = A and POS28 != G and POS28 != A and POS25 != G and POS24 != G and POS25 != A and POS21 != A and POS22 != G | IE | 0.177570 |
| POS31 != G and POS30 != G | N | 0.111877 |
| POS32 != T and POS30 = G and POS28 = G and POS31 != T | N | 0.021272 |
| POS32 != T and POS30 = G and POS28 != A and POS31 != C and POS28 != G and POS20 != A and POS17 != A and POS26 != G and POS43 != T and POS7 != G | IE | 0.160958 |
| POS32 != T and POS30 = G and POS28 = A and POS59 != C and POS18 != T | N | 0.022925 |
| POS32 != T and POS30 = G and POS18 != G and POS23 != G and POS19 != A and POS21 != G and POS28 != G and POS16 != A and POS1 != G | IE | 0.083422 |
| POS31 != G and POS29 != A | N | 0.044736 |
| POS32 = T and POS31 != G and POS19 != A and POS28 != G and POS28 != A and POS59 != A | IE | 0.053676 |
| POS32 = T and POS31 = G and POS35 = G and POS33 != C and POS33 != T and POS34 = A and POS36 != A | EI | 0.557427 |
| POS32 != T and POS30 != G | N | 0.040022 |
| POS31 != G and POS18 = A | N | 0.018504 |
| POS32 != T and POS21 = A and POS13 != C | N | 0.020007 |
| POS32 != T and POS25 = A and POS23 != T | N | 0.014194 |
| POS32 != T and POS50 != G and POS26 != A and POS31 != A and POS33 != G and POS45 != T and POS48 != A | IE | 0.062371 |
| POS31 != G and POS28 != T and POS50 != G and POS17 != T | N | 0.021609 |
| POS32 != T and POS17 = C and POS38 != C | IE | 0.013323 |
| POS32 != T and POS17 != C and POS20 != A and POS19 != T and POS38 != T and POS31 != C | IE | 0.033426 |
| POS31 != G and POS25 != G and POS6 != G | IE | 0.024615 |
| POS32 = A and POS9 = C | N | 0.009195 |
| POS30 = T and POS60 != G and POS5 != C | N | 0.022676 |
| POS29 != A and POS33 != C and POS30 != C and POS30 != A and POS35 = G and POS14 != T | EI | 0.301435 |
| POS29 != A and POS9 != T and POS6 != A and POS51 != A and POS54 != A and POS58 != G | EI | 0.151370 |
| POS29 != A and POS36 != A | N | 0.037388 |
| POS31 = G and POS28 = A and POS29 != T and POS27 != T and POS33 != T and POS30 = G and POS43 != A | EI | 0.341709 |
| POS28 = G and POS29 = A and POS22 != A | EI | 0.201220 |
| POS28 = G and POS44 != C | EI | 0.030864 |
| POS28 != G and POS31 = G and POS29 != T and POS28 != A and POS33 = A and POS32 = T and POS18 != T and POS34 != T | EI | 0.272331 |
| POS28 != G and POS29 != T and POS31 = G and POS28 != A and POS35 != G and POS23 != A and POS18 != G and POS19 != A and POS35 != A | IE | 0.307323 |
| POS28 != G and POS31 = G and POS29 != T and POS28 != A and POS17 = A and POS26 != C | EI | 0.117840 |
| POS28 != G and POS31 = G and POS29 != T and POS28 != A and POS17 != A and POS25 = A and POS50 != A | EI | 0.135417 |
| POS28 != G and POS29 != T and POS31 = G and POS28 != A and POS17 != A and POS35 = A and POS49 != T | IE | 0.206309 |
| POS28 != G and POS31 = G and POS29 != T and POS34 != C and POS25 = G and POS46 != C | EI | 0.120773 |
| POS29 = A and POS31 = G and POS28 != G and POS28 != T and POS34 != C and POS25 != G and POS24 != G and POS21 != A and POS1 != T and POS15 != A and POS53 != A and POS12 != T and POS5 != G and POS39 != A | EI | 0.186667 |
| POS29 = A and POS31 = G and POS28 != G and POS28 != A and POS35 != A and POS18 != A and POS44 != G and POS10 != G and POS7 != C | IE | 0.259740 |
| POS29 = A and POS31 = G and POS28 != G and POS28 != T and POS4 != A and POS25 != G and POS33 != C and POS7 != T and POS60 != A and POS59 != G | EI | 0.305932 |
| POS44 = G and POS49 != T | EI | 0.108889 |
| POS17 != G and POS44 != G and POS41 != G and POS15 != T and POS37 != A | N | 0.430252 |
| POS49 = A and POS2 != C | N | 0.130435 |
| POS49 != A and POS5 != G | IE | 0.490000 |
| POS3 = A | N | 0.400000 |
|  | EI | 0.555556 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| POS32 = T and POS31 = G and POS35 = G and POS34 = A and POS36 = T | EI | 0.088248 |
| POS32 = T and POS31 = G and POS35 = G and POS34 = A and POS33 = A | EI | 0.049280 |
| POS32 = T and POS31 = G and POS35 = G and POS30 = G and POS28 = A and POS29 = A | EI | 0.027654 |
| POS32 = T and POS31 = G and POS35 = G and POS30 = G and POS6 = G and POS33 = G | EI | 0.022422 |
| POS32 = T and POS31 = G and POS35 = G and POS30 = G and POS25 = G | EI | 0.019343 |
| POS32 = T and POS31 = G and POS33 = A and POS10 = A | EI | 0.016245 |
| POS32 = T and POS31 = G and POS35 = G and POS50 = G and POS2 = C | EI | 0.009541 |
| POS32 = T and POS31 = G and POS33 = A and POS41 = T and POS30 = G | EI | 0.012681 |
| POS32 = T and POS31 = G and POS35 = G and POS24 = G and POS54 = G | EI | 0.005928 |
| POS32 = T and POS31 = G and POS35 = G and POS30 = G and POS46 = C and POS33 = G | EI | 0.005474 |
| POS32 = T and POS31 = G and POS33 = A and POS16 = T and POS39 = C | EI | 0.004566 |
| POS32 = T and POS31 = G and POS34 = A and POS21 = G and POS29 = A and POS33 = G | EI | 0.005021 |
| POS32 = T and POS31 = G and POS33 = A and POS60 = T and POS12 = C | EI | 0.003656 |
| POS32 = T and POS31 = G and POS35 = G and POS19 = A and POS54 = T | EI | 0.004111 |
| POS32 = T and POS31 = G and POS34 = A and POS10 = G and POS7 = G | EI | 0.002745 |
| POS32 = T and POS31 = G and POS35 = G and POS25 = A and POS30 = G | EI | 0.003201 |
| POS31 = G and POS32 = T and POS33 = A and POS7 = C | EI | 0.002442 |
| POS31 = G and POS32 = T and POS23 = A and POS30 = G and POS9 = C | EI | 0.004111 |
| POS31 = G and POS32 = T and POS34 = A and POS14 = G | EI | 0.002041 |
| POS29 = A and POS30 = G and POS28 = C and POS19 = T and POS18 = C | IE | 0.065351 |
| POS29 = A and POS30 = G and POS28 = C and POS18 = T and POS16 = T | IE | 0.069368 |
| POS29 = A and POS30 = G and POS28 = C and POS25 = C and POS24 = C | IE | 0.058970 |
| POS29 = A and POS30 = G and POS21 = T and POS25 = T and POS23 = T | IE | 0.041113 |
| POS29 = A and POS30 = G and POS28 = C and POS24 = T and POS20 = T and POS26 = C | IE | 0.026958 |
| POS29 = A and POS30 = G and POS28 = T and POS26 = T and POS31 = G | IE | 0.021304 |
| POS29 = A and POS30 = G and POS28 = C and POS25 = T and POS26 = T and POS11 = T | IE | 0.013663 |
| POS29 = A and POS30 = G and POS28 = C and POS18 = T and POS16 = C | IE | 0.021304 |
| POS29 = A and POS30 = G and POS28 = T and POS43 = A and POS24 = C | IE | 0.010444 |
| POS29 = A and POS30 = G and POS28 = C and POS25 = T and POS2 = G | IE | 0.011734 |
| POS29 = A and POS30 = G and POS25 = C and POS21 = T and POS10 = C | IE | 0.011734 |
| POS29 = A and POS30 = G and POS28 = C and POS50 = G and POS36 = C | IE | 0.011734 |
| POS29 = A and POS30 = G and POS28 = T and POS32 = T | IE | 0.008502 |
| POS29 = A and POS30 = G and POS28 = C and POS18 = C and POS33 = C | IE | 0.007853 |
| POS29 = A and POS30 = G and POS28 = T and POS1 = A and POS10 = T | IE | 0.005249 |
| POS29 = A and POS30 = G and POS28 = C and POS27 = A and POS26 = C | IE | 0.007204 |
| POS29 = A and POS30 = G and POS25 = C and POS23 = C and POS21 = C | IE | 0.005902 |
| POS29 = A and POS30 = G and POS28 = T and POS23 = C and POS18 = T | IE | 0.003942 |
| POS29 = A and POS30 = G and POS13 = T and POS17 = T and POS50 = A | IE | 0.005249 |
| POS29 = A and POS30 = G and POS22 = C and POS12 = C and POS3 = C | IE | 0.003942 |
| POS29 = A and POS30 = G and POS13 = T and POS45 = C and POS35 = A | IE | 0.004596 |
|  | N | 0.962532 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

pos30|pos31|pos32|class
---|---|---|---
n|n|n|ei
c|t|g|n
t|t|g|n
g|t|g|n
a|t|g|n
t|c|g|n
c|c|g|n
a|c|g|n
g|c|g|n
t|a|g|n
a|t|c|n
t|t|c|n
a|a|g|n
c|a|g|n
g|t|c|ie
c|t|c|n
g|a|g|ie
a|c|c|n
c|g|g|n
g|g|g|ie
g|c|c|n
a|g|g|n
t|g|g|n
c|c|c|n
t|c|c|n
g|a|c|ie
c|t|a|n
c|a|c|n
t|t|a|n
t|a|c|n
a|a|c|n
a|t|a|n
g|t|a|n
a|g|c|n
t|c|a|n
a|c|a|n
g|c|a|n
c|c|a|n
t|g|c|n
g|g|c|ie
c|g|c|n
g|t|t|ie
c|t|t|n
a|a|a|n
g|a|a|ie
c|a|a|n
t|a|a|n
a|t|t|n
t|t|t|n
g|g|a|ie
g|c|t|ie
a|g|a|n
c|g|a|n
a|c|t|n
c|c|t|n
t|g|a|n
t|c|t|n
g|a|t|ie
c|a|t|n
t|a|t|n
a|a|t|n
g|g|t|ei
c|g|t|ei
t|g|t|ei
a|g|t|ei

## JRip

Decision list:

rules | predicted class
---|---
(POS32 = T) and (POS31 = G) and (POS35 = G) and (POS34 = A) and (POS36 = T)|EI (211.0/0.0)
(POS32 = T) and (POS31 = G) and (POS35 = G) and (POS34 = A) and (POS33 = A)|EI (113.0/0.0)
(POS32 = T) and (POS31 = G) and (POS35 = G) and (POS30 = G) and (POS28 = A) and (POS29 = A)|EI (62.0/0.0)
(POS32 = T) and (POS31 = G) and (POS35 = G) and (POS30 = G) and (POS6 = G) and (POS33 = G)|EI (50.0/0.0)
(POS32 = T) and (POS31 = G) and (POS35 = G) and (POS30 = G) and (POS25 = G)|EI (43.0/0.0)
(POS32 = T) and (POS31 = G) and (POS33 = A) and (POS10 = A)|EI (36.0/0.0)
(POS32 = T) and (POS31 = G) and (POS35 = G) and (POS50 = G) and (POS2 = C)|EI (21.0/0.0)
(POS32 = T) and (POS31 = G) and (POS33 = A) and (POS41 = T) and (POS30 = G)|EI (28.0/0.0)
(POS32 = T) and (POS31 = G) and (POS35 = G) and (POS24 = G) and (POS54 = G)|EI (13.0/0.0)
(POS32 = T) and (POS31 = G) and (POS35 = G) and (POS30 = G) and (POS46 = C) and (POS33 = G)|EI (12.0/0.0)
(POS32 = T) and (POS31 = G) and (POS33 = A) and (POS16 = T) and (POS39 = C)|EI (10.0/0.0)
(POS32 = T) and (POS31 = G) and (POS34 = A) and (POS21 = G) and (POS29 = A) and (POS33 = G)|EI (11.0/0.0)
(POS32 = T) and (POS31 = G) and (POS33 = A) and (POS60 = T) and (POS12 = C)|EI (8.0/0.0)
(POS32 = T) and (POS31 = G) and (POS35 = G) and (POS19 = A) and (POS54 = T)|EI (9.0/0.0)
(POS32 = T) and (POS31 = G) and (POS34 = A) and (POS10 = G) and (POS7 = G)|EI (6.0/0.0)
(POS32 = T) and (POS31 = G) and (POS35 = G) and (POS25 = A) and (POS30 = G)|EI (7.0/0.0)
(POS31 = G) and (POS32 = T) and (POS33 = A) and (POS7 = C)|EI (12.0/4.0)
(POS31 = G) and (POS32 = T) and (POS23 = A) and (POS30 = G) and (POS9 = C)|EI (9.0/0.0)
(POS31 = G) and (POS32 = T) and (POS34 = A) and (POS14 = G)|EI (11.0/4.0)
(POS29 = A) and (POS30 = G) and (POS28 = C) and (POS19 = T) and (POS18 = C)|IE (106.0/0.0)
(POS29 = A) and (POS30 = G) and (POS28 = C) and (POS18 = T) and (POS16 = T)|IE (112.0/0.0)
(POS29 = A) and (POS30 = G) and (POS28 = C) and (POS25 = C) and (POS24 = C)|IE (95.0/0.0)
(POS29 = A) and (POS30 = G) and (POS21 = T) and (POS25 = T) and (POS23 = T)|IE (64.0/0.0)
(POS29 = A) and (POS30 = G) and (POS28 = C) and (POS24 = T) and (POS20 = T) and (POS26 = C)|IE (42.0/0.0)
(POS29 = A) and (POS30 = G) and (POS28 = T) and (POS26 = T) and (POS31 = G)|IE (32.0/0.0)
(POS29 = A) and (POS30 = G) and (POS28 = C) and (POS25 = T) and (POS26 = T) and (POS11 = T)|IE (21.0/0.0)
(POS29 = A) and (POS30 = G) and (POS28 = C) and (POS18 = T) and (POS16 = C)|IE (33.0/0.0)
(POS29 = A) and (POS30 = G) and (POS28 = T) and (POS43 = A) and (POS24 = C)|IE (16.0/0.0)
(POS29 = A) and (POS30 = G) and (POS28 = C) and (POS25 = T) and (POS2 = G)|IE (18.0/0.0)
(POS29 = A) and (POS30 = G) and (POS25 = C) and (POS21 = T) and (POS10 = C)|IE (18.0/0.0)
(POS29 = A) and (POS30 = G) and (POS28 = C) and (POS50 = G) and (POS36 = C)|IE (18.0/0.0)
(POS29 = A) and (POS30 = G) and (POS28 = T) and (POS32 = T)|IE (13.0/0.0)
(POS29 = A) and (POS30 = G) and (POS28 = C) and (POS18 = C) and (POS33 = C)|IE (12.0/0.0)
(POS29 = A) and (POS30 = G) and (POS28 = T) and (POS1 = A) and (POS10 = T)|IE (8.0/0.0)
(POS29 = A) and (POS30 = G) and (POS28 = C) and (POS27 = A) and (POS26 = C)|IE (11.0/0.0)
(POS29 = A) and (POS30 = G) and (POS25 = C) and (POS23 = C) and (POS21 = C)|IE (9.0/0.0)
(POS29 = A) and (POS30 = G) and (POS28 = T) and (POS23 = C) and (POS18 = T)|IE (6.0/0.0)
(POS29 = A) and (POS30 = G) and (POS13 = T) and (POS17 = T) and (POS50 = A)|IE (8.0/0.0)
(POS29 = A) and (POS30 = G) and (POS22 = C) and (POS12 = C) and (POS3 = C)|IE (6.0/0.0)
(POS29 = A) and (POS30 = G) and (POS13 = T) and (POS45 = C) and (POS35 = A)|IE (7.0/0.0)
|N (1543.0/56.0)


## PART

Decision list:

rules | predicted class
---|---
POS30 != G AND POS35 != G AND POS33 != N AND POS45 != G|N (634.0)
POS32 != T AND POS29 != A|N (498.0/8.0)
POS31 != G AND POS30 = G AND POS29 = A AND POS28 != G AND POS28 != A AND POS25 != G AND POS24 != G AND POS25 != A AND POS21 != A AND POS22 != G|IE (228.0)
POS31 != G AND POS30 != G|N (150.0/1.0)
POS32 != T AND POS30 = G AND POS28 = G AND POS31 != T|N (27.0/1.0)
POS32 != T AND POS30 = G AND POS28 != A AND POS31 != C AND POS28 != G AND POS20 != A AND POS17 != A AND POS26 != G AND POS43 != T AND POS7 != G|IE (170.0)
POS32 != T AND POS30 = G AND POS28 = A AND POS59 != C AND POS18 != T|N (25.0/1.0)
POS32 != T AND POS30 = G AND POS18 != G AND POS23 != G AND POS19 != A AND POS21 != G AND POS28 != G AND POS16 != A AND POS1 != G|IE (77.0)
POS31 != G AND POS29 != A|N (46.0)
POS32 = T AND POS31 != G AND POS19 != A AND POS28 != G AND POS28 != A AND POS59 != A|IE (46.0)
POS32 = T AND POS31 = G AND POS35 = G AND POS33 != C AND POS33 != T AND POS34 = A AND POS36 != A|EI (364.0)
POS32 != T AND POS30 != G|N (24.0)
POS31 != G AND POS18 = A|N (11.0)
POS32 != T AND POS21 = A AND POS13 != C|N (11.0)
POS32 != T AND POS25 = A AND POS23 != T|N (8.0)
POS32 != T AND POS50 != G AND POS26 != A AND POS31 != A AND POS33 != G AND POS45 != T AND POS48 != A|IE (27.0)
POS31 != G AND POS28 != T AND POS50 != G AND POS17 != T|N (12.0)
POS32 != T AND POS17 = C AND POS38 != C|IE (6.0)
POS32 != T AND POS17 != C AND POS20 != A AND POS19 != T AND POS38 != T AND POS31 != C|IE (18.0/2.0)
POS31 != G AND POS25 != G AND POS6 != G|IE (10.0)
POS32 = A AND POS9 = C|N (4.0)
POS30 = T AND POS60 != G AND POS5 != C|N (10.0)
POS29 != A AND POS33 != C AND POS30 != C AND POS30 != A AND POS35 = G AND POS14 != T|EI (62.0)
POS29 != A AND POS9 != T AND POS6 != A AND POS51 != A AND POS54 != A AND POS58 != G|EI (26.0/1.0)
POS29 != A AND POS36 != A|N (15.0)
POS31 = G AND POS28 = A AND POS29 != T AND POS27 != T AND POS33 != T AND POS30 = G AND POS43 != A|EI (68.0)
POS28 = G AND POS29 = A AND POS22 != A|EI (32.0)
POS28 = G AND POS44 != C|EI (6.0/1.0)
POS28 != G AND POS31 = G AND POS29 != T AND POS28 != A AND POS33 = A AND POS32 = T AND POS18 != T AND POS34 != T|EI (51.0/1.0)
POS28 != G AND POS29 != T AND POS31 = G AND POS28 != A AND POS35 != G AND POS23 != A AND POS18 != G AND POS19 != A AND POS35 != A|IE (48.0)
POS28 != G AND POS31 = G AND POS29 != T AND POS28 != A AND POS17 = A AND POS26 != C|EI (13.0/1.0)
POS28 != G AND POS31 = G AND POS29 != T AND POS28 != A AND POS17 != A AND POS25 = A AND POS50 != A|EI (13.0)
POS28 != G AND POS29 != T AND POS31 = G AND POS28 != A AND POS17 != A AND POS35 = A AND POS49 != T|IE (23.0/1.0)
POS28 != G AND POS31 = G AND POS29 != T AND POS34 != C AND POS25 = G AND POS46 != C|EI (11.0/1.0)
POS29 = A AND POS31 = G AND POS28 != G AND POS28 != T AND POS34 != C AND POS25 != G AND POS24 != G AND POS21 != A AND POS1 != T AND POS15 != A AND POS53 != A AND POS12 != T AND POS5 != G AND POS39 != A|EI (14.0)
POS29 = A AND POS31 = G AND POS28 != G AND POS28 != A AND POS35 != A AND POS18 != A AND POS44 != G AND POS10 != G AND POS7 != C|IE (19.0)
POS29 = A AND POS31 = G AND POS28 != G AND POS28 != T AND POS4 != A AND POS25 != G AND POS33 != C AND POS7 != T AND POS60 != A AND POS59 != G|EI (19.0)
POS44 = G AND POS49 != T|EI (9.0/2.0)
POS17 != G AND POS44 != G AND POS41 != G AND POS15 != T AND POS37 != A|N (14.0)
POS49 = A AND POS2 != C|N (3.0)
POS49 != A AND POS5 != G|IE (14.0/2.0)
POS3 = A|N (2.0)
|EI (2.0)


## J48 Decision Tree

* POS30 = G
	* POS32 = T
		* POS31 = G
			* POS35 = G: EI (369.0/12.0)
			* POS35 != G
				* POS33 = A: EI (54.0/5.0)
				* POS33 != A
					* POS29 = A
						* POS26 = A
							* POS23 = T: IE (6.0/2.0)
							* POS23 != T: EI (10.0/1.0)
						* POS26 != A
							* POS28 = A: EI (7.0/2.0)
							* POS28 != A: IE (58.0/6.0)
					* POS29 != A: N (7.0/1.0)
		* POS31 != G
			* POS29 = A: IE (94.0/8.0)
			* POS29 != A: N (26.0)
	* POS32 != T
		* POS29 = A
			* POS28 = G: N (26.0/3.0)
			* POS28 != G
				* POS28 = A: N (29.0/9.0)
				* POS28 != A: IE (378.0/34.0)
		* POS29 != A: N (171.0/3.0)
* POS30 != G
	* POS35 = G
		* POS32 = T
			* POS31 = G
				* POS34 = A: EI (78.0/1.0)
				* POS34 != A
					* POS33 = A: EI (6.0)
					* POS33 != A: N (12.0/2.0)
			* POS31 != G: N (38.0)
		* POS32 != T: N (149.0/1.0)
	* POS35 != G: N (635.0/3.0)


## SimpleCart Decision Tree

		* POS30=(C)|(T)|(A)
					* POS35=(A)|(T)|(C)|(N)|(R)
		* POS45=(G)
					* POS13=(A)|(G)|(T)
				* POS21=(T): N(27.0/1.0)
				* POS21!=(T): N(129.0/0.0)
					* POS13!=(A)|(G)|(T)
							* POS29=(T)|(G)|(C)|(N): N(43.0/1.0)
							* POS29!=(T)|(G)|(C)|(N): N(6.0/3.0)
		* POS45!=(G): N(635.0/0.0)
					* POS35!=(A)|(T)|(C)|(N)|(R)
				* POS32=(G)|(C)|(A)
			* POS34=(C): N(19.0/1.0)
			* POS34!=(C): N(170.0/0.0)
				* POS32!=(G)|(C)|(A)
					* POS31=(T)|(C)|(A): N(56.0/0.0)
					* POS31!=(T)|(C)|(A)
						* POS34=(T)|(C)|(G): N(12.0/9.0)
						* POS34!=(T)|(C)|(G): EI(116.0/1.0)
		* POS30!=(C)|(T)|(A)
			* POS32=(G)|(C)|(A)
				* POS29=(T)|(G)|(C)
					* POS10=(G)|(A)|(C)
				* POS1=(T): N(29.0/1.0)
				* POS1!=(T): N(149.0/0.0)
					* POS10!=(G)|(A)|(C)
				* POS47=(T): N(7.0/3.0)
				* POS47!=(T): N(33.0/1.0)
				* POS29!=(T)|(G)|(C)
				* POS28=(G)|(A)
						* POS22=(A)|(G)|(N): N(38.0/1.0)
						* POS22!=(A)|(G)|(N): N(17.0/13.0)
				* POS28!=(G)|(A)
					* POS25=(A)|(G)
						* POS18=(A)|(G)
									* POS38=(T)|(A)|(G)|(N): N(13.0/1.0)
									* POS38!=(T)|(A)|(G)|(N): IE(7.0/3.0)
						* POS18!=(A)|(G): IE(37.0/6.0)
					* POS25!=(A)|(G)
					* POS26=(A)
							* POS18=(A)|(G): N(6.0/3.0)
							* POS18!=(A)|(G): IE(11.0/0.0)
					* POS26!=(A)
						* POS21=(A): IE(27.0/5.0)
						* POS21!=(A)
							* POS23=(G): IE(39.0/4.0)
							* POS23!=(G)
									* POS24=(A)|(G)
												* POS37=(T)|(C)|(A)|(N): IE(39.0/0.0)
												* POS37!=(T)|(C)|(A)|(N): IE(6.0/3.0)
									* POS24!=(A)|(G)
									* POS19=(A): IE(14.0/1.0)
									* POS19!=(A): IE(269.0/0.0)
			* POS32!=(G)|(C)|(A)
				* POS31=(T)|(C)|(A)
					* POS29=(T)|(G)|(C): N(46.0/0.0)
					* POS29!=(T)|(G)|(C)
					* POS28=(G)|(A): N(8.0/3.0)
					* POS28!=(G)|(A)
						* POS25=(A)|(G): IE(12.0/4.0)
						* POS25!=(A)|(G): IE(110.0/1.0)
				* POS31!=(T)|(C)|(A)
					* POS35=(A)|(T)|(C)
							* POS33=(T)|(C)|(G)|(N)
						* POS28=(G)|(A)
									* POS27=(T)|(A)|(G)|(N): N(11.0/2.0)
									* POS27!=(T)|(A)|(G)|(N): EI(7.0/4.0)
						* POS28!=(G)|(A)
							* POS19=(A)|(G)
							* POS26=(A): EI(8.0/1.0)
							* POS26!=(A): IE(10.0/3.0)
							* POS19!=(A)|(G): IE(59.0/6.0)
							* POS33!=(T)|(C)|(G)|(N)
							* POS18=(A)|(G)|(C): EI(55.0/2.0)
							* POS18!=(A)|(G)|(C)
							* POS10=(G)|(A): EI(10.0/0.0)
							* POS10!=(G)|(A): IE(4.0/6.0)
					* POS35!=(A)|(T)|(C)
					* POS33=(T)|(C): EI(24.0/8.0)
					* POS33!=(T)|(C)
					* POS34=(T): EI(27.0/5.0)
					* POS34!=(T)
						* POS39=(A)
							* POS46=(A): EI(5.0/4.0)
							* POS46!=(A): EI(52.0/2.0)
						* POS39!=(A)
							* POS49=(A): EI(44.0/2.0)
							* POS49!=(A): EI(310.0/0.0)


