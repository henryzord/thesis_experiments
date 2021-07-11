# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | N | 0.519164 |
| POS30 = G and POS32 = T and POS31 = G and POS35 != R and POS33 != C | EI | 0.176326 |
| POS30 = G and POS32 != T and POS29 != C and POS28 != G | IE | 0.131730 |
| POS30 = G and POS32 = T and POS31 != G and POS29 = A | IE | 0.049400 |
| POS30 != G and POS35 != R and POS32 != A and POS31 != T | EI | 0.013713 |
| POS30 = G and POS32 = T and POS31 = G and POS35 != G and POS33 != A and POS29 = A and POS23 != A | IE | 0.023964 |
| POS30 = G and POS32 = T and POS31 = G and POS35 != R and POS33 != N | EI | 0.174866 |
| POS28 = T and POS29 = A and POS30 = G and POS31 = G and POS32 = T | IE | 0.005690 |
| POS30 = G and POS32 != T and POS29 != C and POS28 != A | IE | 0.129790 |
| POS28 = A and POS29 = C and POS30 = A and POS31 = T and POS32 = G | IE | 0.000229 |
| POS28 = C and POS29 = T and POS30 = G and POS31 = G and POS32 = C | EI | 0.000153 |
| POS28 = A and POS29 = G and POS30 = G and POS31 = G and POS32 = A | EI | 0.000459 |
| POS28 = C and POS29 = T and POS30 = A and POS31 = C and POS32 = A | EI | 0.000229 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| POS30 != G and POS35 != G | N | 0.376713 |
| POS32 != T and POS29 = A and POS30 = G and POS28 != G and POS28 != A and POS25 != G and POS25 != A | IE | 0.225921 |
| POS32 != T and POS29 != A | N | 0.267853 |
| POS31 != G and POS29 = A and POS30 = G and POS32 = T and POS28 != A and POS25 != G | IE | 0.102969 |
| POS31 != G and POS29 != A | N | 0.086832 |
| POS32 = T and POS31 != A and POS31 = G and POS35 = G and POS33 != C and POS33 != T and POS34 = A and POS36 != A | EI | 0.498630 |
| POS32 != T and POS30 != G | N | 0.075957 |
| POS31 != G and POS17 != A and POS20 != A and POS17 != G and POS21 != A and POS21 != G | IE | 0.051686 |
| POS31 != G and POS5 != C | N | 0.134344 |
| POS32 != T and POS21 != A and POS28 != G and POS1 != A and POS19 != A and POS42 != G | IE | 0.037045 |
| POS32 != T and POS15 = G | N | 0.030008 |
| POS32 != T and POS5 = G | N | 0.017364 |
| POS32 != T and POS10 = T | IE | 0.010634 |
| POS32 != T and POS22 = G | N | 0.011850 |
| POS32 != T and POS1 = A | IE | 0.011842 |
| POS32 = T and POS30 != G and POS33 != A | N | 0.025982 |
| POS32 = T and POS35 = G and POS29 != T and POS28 != A and POS24 != G and POS26 != T | EI | 0.322911 |
| POS32 = T and POS33 != C and POS33 != T and POS29 = A and POS28 = A | EI | 0.357061 |
| POS32 = T and POS29 != A and POS35 != T | EI | 0.319447 |
| POS32 = T and POS29 = A and POS33 = A and POS34 != T and POS51 != A | EI | 0.237129 |
| POS29 = A and POS32 = T and POS28 != G and POS28 != A and POS23 != A and POS44 != T and POS25 != A and POS17 != A and POS24 != G | IE | 0.301176 |
| POS32 = T and POS29 = A and POS44 = T and POS3 != G | IE | 0.147820 |
| POS32 = T and POS29 = A and POS51 != T and POS28 != G and POS35 = G | EI | 0.233253 |
| POS28 = A | N | 0.120321 |
| POS28 = G and POS9 != G | N | 0.041958 |
| POS9 != T and POS53 != A and POS1 != G | EI | 0.416109 |
| POS43 != A | IE | 0.423878 |
|  | EI | 0.354839 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| POS29 = A and POS28 = C and POS20 = T and POS30 = G and POS24 = T | IE | 0.051846 |
| POS29 = A and POS28 = C and POS24 = C and POS23 = T and POS30 = G | IE | 0.040498 |
| POS29 = A and POS30 = G and POS28 = C and POS19 = T | IE | 0.053772 |
| POS29 = A and POS30 = G and POS28 = T | IE | 0.045417 |
| POS28 = C and POS29 = A and POS19 = C and POS32 = A | IE | 0.015814 |
| POS29 = A and POS28 = C and POS30 = G and POS32 = G | IE | 0.018966 |
| POS29 = A and POS28 = C and POS19 = C and POS15 = C and POS31 = A | IE | 0.002745 |
| POS29 = A and POS30 = G and POS33 = T and POS40 = C | IE | 0.008197 |
| POS29 = A and POS28 = C and POS14 = T and POS9 = T and POS30 = G | IE | 0.004972 |
| POS29 = A and POS22 = T and POS35 = T and POS30 = G and POS21 = T | IE | 0.004252 |
| POS29 = A and POS28 = C and POS35 = C and POS4 = C and POS42 = G | IE | 0.005056 |
| POS29 = A and POS28 = C and POS30 = G and POS18 = T and POS24 = T | IE | 0.003950 |
| POS29 = A and POS22 = T and POS33 = C and POS30 = G | IE | 0.003258 |
| POS32 = T and POS31 = G and POS35 = G and POS34 = A | EI | 0.223642 |
| POS31 = G and POS32 = T and POS30 = G | EI | 0.117129 |
|  | N | 0.965026 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

pos28|pos29|pos30|pos31|pos32|class
---|---|---|---|---|---
n|n|n|n|n|ei
g|t|c|t|g|ei
a|t|c|t|g|n
t|t|c|t|g|n
c|t|c|t|g|n
c|g|c|t|g|ei
t|g|c|t|g|n
g|g|c|t|g|ei
a|g|c|t|g|n
t|t|t|t|g|ei
c|c|c|t|g|ei
a|c|c|t|g|ei
c|t|t|t|g|n
a|t|t|t|g|n
g|c|c|t|g|n
t|c|c|t|g|n
g|t|t|t|g|ei
a|g|t|t|g|n
g|a|c|t|g|ei
t|g|t|t|g|ei
g|t|c|c|g|n
g|g|t|t|g|ei
a|c|t|t|g|ei
g|g|c|c|g|ei
c|t|a|t|g|n
g|t|c|t|c|n
t|t|a|t|g|n
c|t|c|t|c|n
t|c|t|t|g|n
a|t|c|t|c|n
c|c|t|t|g|ei
c|g|c|c|g|ei
t|t|c|t|c|n
c|g|a|t|g|ei
t|a|t|t|g|n
g|a|t|t|g|ei
c|c|c|c|g|n
a|a|t|t|g|n
g|t|t|c|g|ei
a|g|c|t|c|n
t|g|c|t|c|n
c|t|t|c|g|ei
g|g|c|t|c|n
g|c|c|c|g|n
g|g|a|t|g|n
t|g|a|t|g|n
a|t|g|t|g|ei
a|c|c|t|c|ei
c|c|a|t|g|ei
t|c|a|t|g|n
g|t|c|a|g|ei
c|t|g|t|g|n
a|t|t|t|c|n
c|t|t|t|c|n
c|a|c|c|g|ei
t|t|g|t|g|n
t|t|t|t|c|n
c|t|c|a|g|n
t|t|c|a|g|n
g|t|g|t|g|n
a|c|a|t|g|ie
g|c|c|t|c|n
c|c|c|t|c|n
a|t|c|a|g|n
t|c|c|t|c|n
c|a|c|t|c|ei
g|t|c|c|c|ei
t|g|t|t|c|ei
a|g|t|t|c|ei
g|t|a|c|g|ei
c|g|g|t|g|ei
a|t|a|c|g|ei
t|c|t|c|g|ei
g|a|a|t|g|ei
a|c|t|c|g|ei
a|t|c|c|c|n
c|t|a|c|g|ei
t|a|c|t|c|n
a|g|c|a|g|ei
c|t|c|c|c|ei
t|t|c|c|c|n
a|a|c|t|c|n
g|g|g|t|g|n
a|a|a|t|g|ei
t|g|c|a|g|n
c|g|c|a|g|ei
a|g|g|t|g|n
g|g|c|a|g|n
t|a|a|t|g|ei
t|g|g|t|g|n
g|a|c|t|c|n
c|a|a|t|g|n
g|t|t|a|g|ei
c|t|t|a|g|ei
a|t|c|t|a|ei
a|c|g|t|g|ei
t|c|t|t|c|n
c|t|a|t|c|ei
g|t|a|t|c|ei
a|t|t|a|g|ei
c|g|a|c|g|ei
c|a|t|c|g|ei
g|c|t|t|c|ei
a|g|c|c|c|n
t|c|c|a|g|n
t|c|g|t|g|n
t|t|a|t|c|ei
a|c|t|t|c|n
g|g|c|c|c|n
g|c|c|a|g|n
a|c|c|a|g|ei
c|c|c|a|g|n
c|g|c|c|c|n
g|c|g|t|g|ei
t|g|c|c|c|n
t|t|c|t|a|n
a|t|t|c|c|ei
g|a|t|t|c|ei
c|c|a|c|g|ei
g|g|c|t|a|n
g|c|c|c|c|ei
g|a|g|t|g|n
t|a|t|t|c|ei
t|t|t|c|c|ei
t|a|c|a|g|n
t|g|c|t|a|n
t|c|c|c|c|n
c|a|t|t|c|n
a|a|g|t|g|n
c|g|a|t|c|n
c|c|c|c|c|n
a|g|a|t|c|n
c|t|t|c|c|n
g|c|a|c|g|n
a|t|c|g|g|ei
a|c|a|c|g|n
c|t|g|c|g|n
a|c|c|c|c|n
c|a|c|a|g|n
g|g|a|t|c|n
t|t|c|g|g|ei
t|a|g|t|g|ie
c|a|g|t|g|ie
a|g|g|c|g|n
t|t|t|t|a|ei
c|t|g|t|c|ei
a|g|c|g|g|ei
g|a|c|c|c|n
t|t|c|a|c|n
t|a|c|c|c|ei
c|a|c|c|c|ei
c|c|c|t|a|ei
a|a|a|c|g|ei
c|t|t|t|a|n
a|c|c|t|a|ei
a|g|t|c|c|n
a|c|a|t|c|n
a|a|c|c|c|ei
c|a|a|c|g|n
g|t|t|t|a|ei
c|t|c|a|c|n
t|g|g|c|g|n
c|c|a|t|c|n
a|t|g|t|c|n
c|g|g|c|g|ei
c|t|a|a|g|n
a|t|t|t|a|n
g|a|a|c|g|ei
t|g|t|c|c|n
t|t|g|t|c|n
g|c|a|t|c|n
g|t|c|a|c|n
g|t|a|a|g|n
g|g|t|t|a|ei
c|a|c|t|a|ei
a|c|t|c|c|ei
a|a|a|t|c|ei
c|g|c|a|c|ei
t|g|a|a|g|ei
c|t|t|g|g|ei
t|g|c|a|c|ei
a|g|c|a|c|ei
t|t|t|g|g|n
a|g|t|t|a|n
t|g|g|t|c|ei
g|t|a|c|c|ei
c|c|g|c|g|ei
t|c|t|c|c|n
g|c|t|c|c|n
t|t|c|c|a|ei
a|t|a|c|c|ei
c|t|a|c|c|n
c|c|t|c|c|n
a|g|g|t|c|ei
a|g|a|a|g|n
g|a|a|t|c|ei
a|a|t|a|g|ei
g|t|t|g|g|n
t|a|a|t|c|n
g|a|t|a|g|n
a|c|c|g|g|ei
g|g|a|a|g|n
a|t|t|g|g|ei
g|c|c|g|g|n
c|t|c|c|a|n
g|t|c|c|a|n
a|t|c|c|a|n
c|c|c|g|g|n
a|a|t|c|c|ei
t|c|a|a|g|ei
g|a|t|c|c|ei
c|g|a|c|c|ei
t|c|c|a|c|ei
g|t|g|a|g|ei
a|t|g|a|g|n
t|t|a|t|a|ei
c|c|g|t|c|ei
g|g|t|g|g|n
a|c|a|a|g|n
g|a|c|g|g|n
c|g|c|c|a|n
t|g|t|g|g|n
a|a|g|c|g|n
c|c|t|t|a|ei
c|c|a|a|g|n
t|t|t|a|c|ei
a|c|t|t|a|ei
a|g|t|g|g|ei
g|g|a|c|c|ei
t|c|t|t|a|n
a|g|a|c|c|n
c|t|t|a|c|ei
t|t|c|t|t|n
t|g|a|c|c|n
c|c|c|a|c|n
g|g|c|c|a|n
a|g|c|c|a|n
a|c|c|a|c|n
c|t|c|t|t|n
t|g|c|c|a|n
g|t|c|t|t|n
c|t|g|a|g|n
c|a|g|c|g|ie
g|a|a|a|g|ei
c|g|a|t|a|ei
c|g|g|a|g|ei
g|t|g|c|c|n
c|a|a|a|g|n
a|t|a|g|g|ei
a|a|c|a|c|n
g|t|c|g|c|ei
a|g|t|a|c|ei
t|g|c|t|t|ei
t|g|t|a|c|ei
g|c|a|c|c|ei
c|g|c|t|t|ei
g|g|g|a|g|ei
c|t|t|c|a|ei
t|c|t|g|g|ei
g|a|g|t|c|ei
c|c|a|c|c|n
g|c|t|g|g|n
a|c|t|g|g|n
t|g|g|a|g|n
a|t|g|c|c|ei
t|g|a|t|a|n
t|c|a|c|c|n
a|c|a|c|c|n
c|a|c|a|c|n
t|t|t|c|a|n
a|g|g|a|g|n
g|a|c|a|c|n
g|t|a|g|g|ei
a|g|a|t|a|ei
a|c|c|c|a|ei
a|a|g|t|c|ei
a|t|t|c|a|n
c|t|g|c|c|n
g|g|t|a|c|ei
a|g|c|t|t|n
a|a|a|a|g|ei
g|c|c|c|a|n
c|c|c|c|a|n
c|c|t|g|g|n
c|a|g|t|c|ie
t|a|g|t|c|ie
c|g|c|g|c|ei
g|t|c|a|a|ei
t|g|c|g|c|ei
g|c|c|t|t|n
a|g|a|g|g|n
c|c|t|a|c|ei
c|c|a|t|a|ei
a|a|c|c|a|n
t|a|t|g|g|ei
a|a|a|c|c|n
a|a|t|g|g|n
c|c|c|t|t|ei
a|c|c|t|t|n
g|c|t|a|c|ei
t|t|g|t|a|ei
g|t|g|t|a|ei
g|g|t|c|a|ei
g|a|c|c|a|n
a|t|t|t|t|n
t|g|t|c|a|n
c|g|g|c|c|ei
g|t|t|t|t|n
g|c|g|a|g|ei
a|c|a|t|a|n
t|c|t|a|c|ei
a|t|a|a|c|ei
g|g|g|c|c|n
g|g|c|g|c|n
t|g|g|c|c|n
c|t|c|a|a|n
g|a|a|c|c|n
a|t|g|t|a|n
c|a|a|c|c|ei
g|g|a|g|g|n
c|a|t|g|g|n
t|t|t|t|t|n
t|c|c|t|t|n
c|a|c|c|a|ei
a|t|c|a|a|n
a|g|g|c|c|n
t|g|a|a|c|ei
t|t|t|g|c|ei
t|c|g|c|c|ei
a|g|c|a|a|ei
a|a|c|t|t|ei
g|g|g|t|a|ei
a|c|t|c|a|ei
g|c|t|c|a|ei
a|t|c|c|t|ei
g|a|a|t|a|n
t|g|c|a|a|n
g|c|c|g|c|ei
c|a|c|t|t|ei
g|g|a|a|c|ei
a|a|a|t|a|n
a|g|t|t|t|ei
g|a|g|a|g|n
t|g|t|t|t|ei
t|t|c|c|t|n
g|c|a|g|g|n
g|t|t|g|c|ei
a|c|a|g|g|n
a|t|a|c|a|ei
t|t|g|g|g|n
c|t|a|c|a|ei
a|t|g|g|g|n
t|t|a|c|a|ei
c|t|g|g|g|n
t|c|a|g|g|n
g|g|c|a|a|n
c|t|t|g|c|n
t|a|a|t|a|n
a|g|a|a|c|n
c|c|a|g|g|n
c|t|c|c|t|n
t|c|c|g|c|ei
g|g|t|t|t|n
c|a|a|t|a|n
c|c|g|c|c|ei
t|g|g|t|a|ei
a|a|g|a|g|ie
a|c|c|g|c|n
g|t|g|g|g|n
g|t|c|c|t|n
c|c|t|c|a|n
t|a|g|a|g|ie
c|a|g|a|g|ie
c|a|c|g|c|ei
a|c|c|a|a|ei
g|c|t|t|t|ei
t|c|g|t|a|ei
a|t|a|t|t|n
c|a|a|g|g|ei
c|c|g|t|a|ei
a|c|a|a|c|ei
c|t|a|t|t|ei
t|a|t|c|a|n
c|c|c|a|a|n
a|a|g|c|c|n
c|a|t|c|a|ei
g|g|t|g|c|ei
g|g|c|c|t|n
a|g|c|c|t|ei
a|c|t|t|t|n
t|t|g|a|c|ei
g|g|a|c|a|n
a|a|t|c|a|n
g|a|c|g|c|ei
c|g|t|g|c|ei
c|c|a|a|c|n
g|g|g|g|g|n
c|g|a|c|a|n
c|g|g|g|g|n
a|t|g|a|c|n
t|c|t|t|t|n
g|a|a|g|g|n
a|a|a|g|g|n
a|t|t|a|a|n
t|g|c|c|t|n
g|c|c|a|a|n
t|g|t|g|c|n
c|t|g|a|c|n
g|t|g|a|c|n
t|g|g|g|g|n
a|g|g|g|g|n
t|t|t|a|a|n
c|a|g|c|c|ie
t|a|g|c|c|ie
a|a|a|a|c|ei
g|g|g|a|c|n
c|c|c|c|t|ei
g|a|c|a|a|ei
c|t|c|g|a|ei
g|a|g|t|a|ei
t|c|t|g|c|ei
t|g|t|a|a|ei
t|c|a|c|a|ei
t|c|g|g|g|n
c|a|a|a|c|n
a|c|c|c|t|ei
g|c|g|g|g|ei
g|a|a|a|c|ei
t|t|t|c|t|n
g|g|t|a|a|ei
g|c|c|c|t|n
t|g|a|t|t|ei
t|a|c|a|a|n
a|g|g|a|c|ei
c|t|t|c|t|n
g|t|t|c|t|n
g|c|t|g|c|n
t|g|g|a|c|n
a|c|a|c|a|ei
c|g|t|a|a|ei
t|a|g|t|a|ie
c|a|g|t|a|ie
c|c|g|g|g|ei
c|t|a|g|c|n
a|t|g|c|a|n
a|g|t|a|a|n
a|a|g|t|a|ei
c|a|t|t|t|n
a|g|a|t|t|n
c|c|a|c|a|n
c|t|g|c|a|n
t|a|t|t|t|n
t|t|a|g|c|n
a|a|t|t|t|n
c|c|t|g|c|n
c|g|g|a|c|n
a|c|t|g|c|n
g|c|a|c|a|n
c|c|a|t|t|ei
g|t|a|a|a|n
c|a|c|c|t|ei
a|a|t|g|c|ei
t|g|g|c|a|ei
c|g|g|c|a|ei
a|t|a|a|a|ei
a|g|g|c|a|n
t|t|c|a|t|ei
c|t|g|t|t|n
g|g|a|g|c|n
g|a|g|g|g|ei
a|g|c|g|a|ei
a|g|t|c|t|n
c|c|g|a|c|ei
t|g|a|g|c|ei
c|a|a|c|a|ei
g|c|a|t|t|n
c|a|t|g|c|ei
t|t|g|t|t|n
t|a|t|g|c|n
a|a|a|c|a|ei
g|t|c|a|t|ei
g|g|g|c|a|n
g|a|a|c|a|n
a|t|g|t|t|n
g|c|t|a|a|ei
a|a|g|g|g|n
t|a|a|c|a|ei
a|c|a|t|t|ei
g|a|c|c|t|n
a|g|a|g|c|n
t|t|a|a|a|n
t|c|a|t|t|n
g|g|c|g|a|ei
g|g|t|c|t|n
c|g|c|g|a|ei
g|a|t|g|c|n
c|t|c|a|t|n
c|t|a|a|a|n
t|a|g|g|g|ie
c|a|g|g|g|ie
a|t|t|g|a|ei
t|c|c|g|a|ei
c|a|a|t|t|ei
a|c|c|g|a|ei
g|t|g|g|c|ei
a|g|c|a|t|n
t|g|g|t|t|ei
t|t|g|g|c|ei
t|g|a|a|a|n
c|g|c|a|t|ei
g|g|c|a|t|ei
g|a|g|a|c|n
c|c|t|c|t|n
a|t|a|c|t|n
g|g|g|t|t|ei
g|c|t|c|t|n
g|a|a|t|t|n
t|c|a|g|c|n
t|a|g|a|c|ie
a|a|a|t|t|n
a|a|g|a|c|n
g|c|a|g|c|ei
a|c|a|g|c|ei
t|t|t|g|a|n
t|t|a|c|t|n
t|a|a|t|t|n
c|t|g|g|c|ei
c|c|a|g|c|n
c|t|a|c|t|ei
t|c|g|c|a|ei
g|t|t|g|a|n
c|t|t|g|a|n
t|a|t|a|a|n
a|g|a|a|a|n
g|g|a|a|a|n
a|c|g|c|a|n
a|c|t|c|t|n
a|g|g|t|t|ei
t|c|t|c|t|n
c|a|g|a|c|ie
g|c|a|a|a|ei
a|c|a|a|a|ei
g|t|t|a|t|ei
g|c|c|a|t|ei
g|t|g|a|a|ei
g|g|t|g|a|n
g|a|g|c|a|n
a|a|a|g|c|ei
g|g|g|g|c|ei
a|a|g|c|a|n
t|t|g|a|a|ei
t|c|c|a|t|n
a|c|c|a|t|n
c|a|t|c|t|n
t|c|g|t|t|ei
a|t|t|a|t|n
t|a|g|c|a|ie
t|a|t|c|t|n
c|a|a|g|c|n
g|a|a|g|c|ei
c|g|t|g|a|n
t|g|t|g|a|n
c|t|g|a|a|n
a|g|t|g|a|n
a|t|g|a|a|n
a|g|g|g|c|n
c|c|g|t|t|n
a|g|a|c|t|n
g|a|c|g|a|ei
g|g|a|c|t|n
c|g|g|g|c|n
t|g|g|g|c|ei
c|c|c|a|t|n
c|a|g|c|a|ie
c|t|a|g|a|ei
a|c|a|c|t|ei
t|t|a|g|a|ei
g|t|c|g|t|ei
a|c|g|g|c|ei
g|a|g|t|t|n
a|a|g|t|t|n
t|c|g|g|c|ei
a|t|a|g|a|n
t|t|g|c|t|n
a|t|g|c|t|n
g|a|c|a|t|n
t|c|a|c|t|n
c|a|a|a|a|n
g|c|t|g|a|n
a|a|a|a|a|n
c|c|g|g|c|n
t|g|g|a|a|n
t|a|a|a|a|n
g|c|g|g|c|n
c|t|g|c|t|n
g|t|a|g|a|n
g|c|a|c|t|n
t|t|c|g|t|n
g|t|g|c|t|ei
a|g|g|a|a|n
g|a|a|a|a|n
a|a|c|a|t|n
a|c|t|g|a|n
t|c|t|g|a|n
g|g|g|a|a|n
g|g|t|a|t|ei
c|c|t|g|a|n
t|a|c|a|t|n
c|a|c|a|t|n
t|a|g|t|t|ie
c|a|g|t|t|ie
g|g|a|g|a|ei
a|t|a|a|t|ei
g|t|a|a|t|ei
t|a|t|g|a|ei
g|g|c|g|t|ei
c|g|c|g|t|ei
a|g|a|g|a|ei
t|a|a|c|t|n
t|g|c|g|t|ei
g|a|a|c|t|n
a|c|t|a|t|ei
a|a|t|g|a|n
t|g|g|c|t|n
c|g|g|c|t|n
a|a|g|g|c|ie
a|g|g|c|t|ei
g|a|g|g|c|n
g|g|g|c|t|n
c|t|a|a|t|n
c|c|t|a|t|ei
g|a|t|g|a|n
a|a|a|c|t|n
c|g|a|g|a|ei
t|c|t|a|t|n
t|a|g|g|c|ie
c|a|g|g|c|ie
g|t|t|g|t|ei
c|c|g|c|t|ei
t|t|g|g|a|ei
g|c|c|g|t|ei
a|c|g|c|t|ei
a|c|a|g|a|ei
c|c|a|g|a|n
a|t|g|g|a|n
t|g|a|a|t|ei
c|t|g|g|a|n
c|a|t|a|t|ei
g|a|t|a|t|n
a|a|t|a|t|ei
t|c|g|c|t|n
g|c|a|g|a|n
a|c|c|g|t|ei
g|g|a|a|t|n
t|t|t|g|t|ei
c|t|t|g|t|n
t|c|c|g|t|ei
g|t|g|g|a|ei
t|c|a|g|a|ei
a|t|t|g|t|n
g|a|g|a|a|n
a|a|g|a|a|n
c|a|g|a|a|ie
t|a|g|a|a|ie
c|g|g|g|a|ei
c|a|c|g|t|ei
c|c|a|a|t|n
a|c|a|a|t|ei
a|a|c|g|t|ei
a|a|g|c|t|ie
g|a|c|g|t|ei
c|g|t|g|t|n
t|g|t|g|t|n
a|g|g|g|a|ei
a|g|t|g|t|ei
g|g|g|g|a|n
g|a|g|c|t|ie
t|g|g|g|a|n
a|t|g|a|t|n
t|t|g|a|t|ei
g|c|a|a|t|n
g|g|t|g|t|ei
g|a|a|g|a|n
a|a|a|g|a|n
t|a|g|c|t|ie
c|a|g|c|t|ie
c|g|g|a|t|ei
a|c|g|g|a|ei
g|a|a|a|t|n
t|c|g|g|a|n
a|t|a|g|t|ei
c|a|a|a|t|n
a|c|t|g|t|ei
c|c|t|g|t|ei
t|g|g|a|t|ei
g|g|g|a|t|ei
g|c|t|g|t|n
c|c|g|g|a|n
t|c|t|g|t|ei
a|a|a|a|t|n
t|a|t|g|t|ei
c|g|a|g|t|ei
g|g|a|g|t|ei
a|g|a|g|t|ei
c|a|t|g|t|ei
t|g|a|g|t|n
g|a|g|g|a|n
a|a|t|g|t|ei
a|a|g|g|a|ie
g|a|t|g|t|ei
c|a|g|g|a|ie
t|a|g|g|a|ie
g|a|g|a|t|ei
a|a|g|a|t|n
t|t|g|g|t|ei
a|c|a|g|t|ei
g|t|g|g|t|ei
c|c|a|g|t|ei
t|c|a|g|t|ei
c|t|g|g|t|ei
g|c|a|g|t|n
a|t|g|g|t|ei
t|a|g|a|t|ie
c|a|g|a|t|ie
t|a|a|g|t|ei
c|a|a|g|t|ei
a|g|g|g|t|ei
a|a|a|g|t|ei
c|g|g|g|t|ei
t|g|g|g|t|ei
g|g|g|g|t|ei
g|a|a|g|t|ei
c|c|g|g|t|ei
a|c|g|g|t|ei
g|c|g|g|t|ei
t|c|g|g|t|ei
a|a|g|g|t|ei
g|a|g|g|t|ei
t|a|g|g|t|ie
c|a|g|g|t|ei

## JRip

Decision list:

rules | predicted class
---|---
(POS29 = A) and (POS28 = C) and (POS20 = T) and (POS30 = G) and (POS24 = T)|IE (129.0/5.0)
(POS29 = A) and (POS28 = C) and (POS24 = C) and (POS23 = T) and (POS30 = G)|IE (94.0/1.0)
(POS29 = A) and (POS30 = G) and (POS28 = C) and (POS19 = T)|IE (169.0/24.0)
(POS29 = A) and (POS30 = G) and (POS28 = T)|IE (139.0/19.0)
(POS28 = C) and (POS29 = A) and (POS19 = C) and (POS32 = A)|IE (37.0/1.0)
(POS29 = A) and (POS28 = C) and (POS30 = G) and (POS32 = G)|IE (54.0/5.0)
(POS29 = A) and (POS28 = C) and (POS19 = C) and (POS15 = C) and (POS31 = A)|IE (6.0/0.0)
(POS29 = A) and (POS30 = G) and (POS33 = T) and (POS40 = C)|IE (27.0/3.0)
(POS29 = A) and (POS28 = C) and (POS14 = T) and (POS9 = T) and (POS30 = G)|IE (14.0/0.0)
(POS29 = A) and (POS22 = T) and (POS35 = T) and (POS30 = G) and (POS21 = T)|IE (13.0/2.0)
(POS29 = A) and (POS28 = C) and (POS35 = C) and (POS4 = C) and (POS42 = G)|IE (12.0/0.0)
(POS29 = A) and (POS28 = C) and (POS30 = G) and (POS18 = T) and (POS24 = T)|IE (14.0/3.0)
(POS29 = A) and (POS22 = T) and (POS33 = C) and (POS30 = G)|IE (15.0/4.0)
(POS32 = T) and (POS31 = G) and (POS35 = G) and (POS34 = A)|EI (425.0/2.0)
(POS31 = G) and (POS32 = T) and (POS30 = G)|EI (240.0/29.0)
|N (1482.0/44.0)


## PART

Decision list:

rules | predicted class
---|---
POS30 != G AND POS35 != G|N (846.0/6.0)
POS32 != T AND POS29 = A AND POS30 = G AND POS28 != G AND POS28 != A AND POS25 != G AND POS25 != A|IE (428.0/19.0)
POS32 != T AND POS29 != A|N (369.0/6.0)
POS31 != G AND POS29 = A AND POS30 = G AND POS32 = T AND POS28 != A AND POS25 != G|IE (120.0/4.0)
POS31 != G AND POS29 != A|N (86.0)
POS32 = T AND POS31 != A AND POS31 = G AND POS35 = G AND POS33 != C AND POS33 != T AND POS34 = A AND POS36 != A|EI (364.0)
POS32 != T AND POS30 != G|N (44.0)
POS31 != G AND POS17 != A AND POS20 != A AND POS17 != G AND POS21 != A AND POS21 != G|IE (32.0/3.0)
POS31 != G AND POS5 != C|N (64.0/2.0)
POS32 != T AND POS21 != A AND POS28 != G AND POS1 != A AND POS19 != A AND POS42 != G|IE (28.0/5.0)
POS32 != T AND POS15 = G|N (13.0/1.0)
POS32 != T AND POS5 = G|N (7.0)
POS32 != T AND POS10 = T|IE (6.0)
POS32 != T AND POS22 = G|N (6.0)
POS32 != T AND POS1 = A|IE (6.0/1.0)
POS32 = T AND POS30 != G AND POS33 != A|N (18.0/3.0)
POS32 = T AND POS35 = G AND POS29 != T AND POS28 != A AND POS24 != G AND POS26 != T|EI (76.0/7.0)
POS32 = T AND POS33 != C AND POS33 != T AND POS29 = A AND POS28 = A|EI (79.0/4.0)
POS32 = T AND POS29 != A AND POS35 != T|EI (74.0/7.0)
POS32 = T AND POS29 = A AND POS33 = A AND POS34 != T AND POS51 != A|EI (42.0)
POS29 = A AND POS32 = T AND POS28 != G AND POS28 != A AND POS23 != A AND POS44 != T AND POS25 != A AND POS17 != A AND POS24 != G|IE (47.0/3.0)
POS32 = T AND POS29 = A AND POS44 = T AND POS3 != G|IE (18.0)
POS32 = T AND POS29 = A AND POS51 != T AND POS28 != G AND POS35 = G|EI (22.0/1.0)
POS28 = A|N (8.0/2.0)
POS28 = G AND POS9 != G|N (8.0/2.0)
POS9 != T AND POS53 != A AND POS1 != G|EI (31.0/4.0)
POS43 != A|IE (22.0/1.0)
|EI (6.0/2.0)


## J48 Decision Tree

* POS30 = G
	* POS32 = T
		* POS31 = G
			* POS35 = G: EI (441.0/21.0)
			* POS35 != G
				* POS33 = A: EI (63.0/7.0)
				* POS33 != A
					* POS29 = A
						* POS23 = A: EI (14.0/4.0)
						* POS23 != A: IE (75.0/14.0)
					* POS29 != A: N (11.0/2.0)
		* POS31 != G
			* POS29 = A: IE (117.0/11.0)
			* POS29 != A: N (40.0)
	* POS32 != T
		* POS29 = A
			* POS28 = G: N (27.0/3.0)
			* POS28 != G
				* POS28 = A: N (33.0/10.0)
				* POS28 != A: IE (453.0/40.0)
		* POS29 != A: N (197.0/4.0)
* POS30 != G
	* POS35 = G
		* POS32 = T
			* POS31 = G
				* POS34 = A: EI (104.0)
				* POS34 != A: N (18.0/8.0)
			* POS31 != G: N (53.0)
		* POS32 != T: N (172.0/1.0)
	* POS35 != G: N (765.0/6.0)


## SimpleCart Decision Tree

	* POS30=(N)|(G)
		* POS32=(N)|(T)
			* POS31=(N)|(G)
					* POS35=(N)|(G)|(R): EI(462.0/21.0)
					* POS35!=(N)|(G)|(R)
							* POS33=(T)|(C)|(G)|(N)
						* POS28=(G)|(A): N(13.0/11.0)
						* POS28!=(G)|(A): IE(68.0/18.0)
							* POS33!=(T)|(C)|(G)|(N): EI(68.0/9.0)
			* POS31!=(N)|(G)
					* POS29=(T)|(G)|(C): N(46.0/0.0)
					* POS29!=(T)|(G)|(C): IE(125.0/13.0)
		* POS32!=(N)|(T)
				* POS29=(T)|(G)|(C): N(218.0/5.0)
				* POS29!=(T)|(G)|(C)
				* POS28=(G)|(A): N(55.0/14.0)
				* POS28!=(G)|(A): IE(454.0/41.0)
	* POS30!=(N)|(G)
					* POS35=(A)|(T)|(C)|(N)|(R): N(840.0/5.0)
					* POS35!=(A)|(T)|(C)|(N)|(R)
				* POS32=(G)|(C)|(A): N(189.0/1.0)
				* POS32!=(G)|(C)|(A)
					* POS31=(T)|(C)|(A): N(56.0/0.0)
					* POS31!=(T)|(C)|(A): EI(125.0/13.0)


