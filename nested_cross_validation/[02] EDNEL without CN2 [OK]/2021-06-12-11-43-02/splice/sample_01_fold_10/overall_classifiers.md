# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| POS30 = T | N | 0.186223 |
| POS30 = G and POS32 = T and POS31 = G and POS35 != R and POS33 != C | EI | 0.174184 |
| POS30 = G and POS32 != T and POS29 != C and POS28 != G | IE | 0.133557 |
| POS30 != G and POS35 = C | N | 0.176127 |
| POS30 != G and POS35 = T | N | 0.170681 |
| POS30 != G and POS35 = A | N | 0.160075 |
| POS30 = G and POS32 != T and POS29 = G | N | 0.061288 |
| POS30 = G and POS32 != T and POS29 = T | N | 0.058051 |
| POS30 = G and POS32 = T and POS31 != G and POS29 != T | IE | 0.041937 |
| POS30 != G and POS35 != R and POS31 = A | N | 0.150772 |
| POS30 != G and POS35 != R and POS31 != A and POS32 != C | EI | 0.013521 |
| POS30 != G and POS35 != R and POS31 != A and POS32 = C | N | 0.147095 |
| POS30 = G and POS32 != T and POS29 = C | N | 0.023355 |
| POS30 != G and POS35 != R and POS31 != A and POS32 = G | N | 0.113114 |
| POS30 = G and POS32 != T and POS29 != C and POS28 = G | N | 0.049725 |
| POS30 != G and POS35 != R and POS31 != A and POS32 = A | N | 0.128241 |
| POS30 = G and POS32 != T and POS29 != C and POS28 = A | N | 0.044328 |
| POS29 = A and POS30 = G and POS31 = G and POS32 = T and POS35 = C | IE | 0.008046 |
| POS30 = G and POS32 = T and POS31 != G and POS29 = T | N | 0.014989 |
| POS30 = G and POS32 = T and POS31 != G and POS29 = G | N | 0.010043 |
| POS30 != G and POS35 != R and POS31 = C | N | 0.163639 |
| POS30 != G and POS35 != R and POS31 = T | N | 0.177104 |
| POS30 = G and POS32 = T and POS31 != G and POS29 = C | N | 0.005047 |
| POS30 = G and POS29 = A and POS32 = T and POS31 = G and POS35 = A and POS28 = C and POS49 = C | IE | 0.002803 |
| POS29 = G and POS30 = G and POS31 = G and POS32 = T and POS35 = T | N | 0.002892 |
| POS30 = G and POS29 = A and POS32 = T and POS31 = G and POS35 = A and POS28 = C and POS49 = G | IE | 0.002061 |
| POS30 = G and POS32 = T and POS31 = G and POS35 = G | EI | 0.168702 |
| POS30 = G and POS29 = A and POS32 = T and POS31 = G and POS35 = A and POS28 = C and POS49 = A | IE | 0.001909 |
| POS30 = G and POS29 = A and POS32 = T and POS31 = A and POS25 = G | N | 0.002169 |
| POS30 = G and POS29 = A and POS32 = A and POS28 = T and POS23 = G | N | 0.001628 |
| POS30 = G and POS29 = A and POS32 = T and POS31 = G and POS35 = A and POS28 = T | IE | 0.001032 |
| POS30 = G and POS29 = C and POS32 = T and POS34 = C | N | 0.001303 |
| POS29 = T and POS30 = G and POS31 = G and POS32 = T and POS35 = T | N | 0.000725 |
| POS30 = A and POS32 = T and POS31 = G and POS34 = G | N | 0.002169 |
| POS30 = A and POS32 = T and POS31 = G and POS34 = A and POS36 = A | N | 0.001655 |
| POS30 = C and POS31 = G and POS32 = T and POS36 = A | N | 0.002261 |
| POS29 = A and POS30 = G and POS31 = A and POS32 = A and POS35 = G | N | 0.001930 |
| POS30 = A and POS32 = T and POS31 = G and POS34 = C | N | 0.003011 |
| POS29 = A and POS30 = G and POS31 = T and POS32 = C and POS35 = C | IE | 0.001467 |
| POS29 = A and POS30 = G and POS31 = T and POS32 = G and POS35 = T | IE | 0.003202 |
| POS29 = T and POS30 = G and POS31 = G and POS32 = C and POS35 = G | EI | 0.000153 |
| POS30 = G and POS32 != T and POS29 != C and POS28 != A | IE | 0.131016 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| POS30 = C and POS31 = T | N | 0.080613 |
| POS30 = C and POS31 = A | N | 0.073831 |
| POS30 = C and POS31 = C | N | 0.074447 |
| POS30 = T and POS35 = T | N | 0.070081 |
| POS30 = A and POS32 = A | N | 0.068832 |
| POS29 = T and POS31 = G and POS32 = T and POS35 = G | EI | 0.044044 |
| POS29 = T | N | 0.147385 |
| POS29 = C and POS32 = T and POS31 = G and POS35 = G | EI | 0.062477 |
| POS29 = C | N | 0.162413 |
| POS29 = G and POS32 = T and POS31 = G and POS35 = G | EI | 0.068484 |
| POS29 = G and POS31 = C | N | 0.047756 |
| POS29 = G and POS31 = A | N | 0.044482 |
| POS29 = G | N | 0.094914 |
| POS30 = T and POS32 = T and POS31 = G | EI | 0.016053 |
| POS30 = T | N | 0.041048 |
| POS30 = A and POS31 = G and POS32 = T | EI | 0.027778 |
| POS30 = A | N | 0.055756 |
| POS32 = G and POS28 = C | IE | 0.190716 |
| POS32 = A and POS28 = C | IE | 0.179458 |
| POS32 = C and POS28 = C | IE | 0.183716 |
| POS32 = A and POS28 = T | IE | 0.071411 |
| POS32 = A | N | 0.050191 |
| POS31 = C | IE | 0.072564 |
| POS31 = A and POS28 = C | IE | 0.091676 |
| POS32 = G and POS28 = T | IE | 0.042947 |
| POS32 = T and POS31 = G and POS35 = G and POS28 = C | EI | 0.309691 |
| POS32 = C and POS28 = T | IE | 0.048852 |
| POS32 = G | N | 0.062959 |
| POS32 = C and POS55 = G | N | 0.016543 |
| POS31 = T | IE | 0.076087 |
| POS32 = T and POS31 = G and POS28 = A | EI | 0.432134 |
| POS32 = T and POS31 = G and POS28 = G | EI | 0.283314 |
| POS32 = T and POS31 = G and POS33 = G | IE | 0.230320 |
| POS32 = T and POS33 = A and POS28 = C | EI | 0.212526 |
| POS28 = C | IE | 0.242119 |
| POS28 = T and POS24 = C | IE | 0.064257 |
| POS28 = A | N | 0.155376 |
| POS28 = T and POS24 = G | EI | 0.178253 |
| POS28 = T | IE | 0.080503 |
|  | N | 0.365079 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| POS29 = A and POS28 = C and POS30 = G and POS20 = T | IE | 0.093664 |
| POS29 = A and POS30 = G and POS21 = T and POS28 = C and POS24 = C | IE | 0.023863 |
| POS29 = A and POS30 = G and POS28 = T | IE | 0.046469 |
| POS29 = A and POS30 = G and POS28 = C and POS20 = C and POS19 = T | IE | 0.031812 |
| POS29 = A and POS30 = G and POS28 = C and POS24 = C and POS16 = T | IE | 0.010679 |
| POS29 = A and POS28 = C and POS30 = G and POS34 = C | IE | 0.011114 |
| POS29 = A and POS30 = G and POS21 = T and POS18 = T and POS17 = T | IE | 0.006933 |
| POS29 = A and POS28 = C and POS30 = G and POS31 = A | IE | 0.008163 |
| POS29 = A and POS30 = G and POS28 = C and POS32 = A and POS8 = C | IE | 0.004155 |
| POS29 = A and POS28 = C and POS30 = G and POS32 = C | IE | 0.003367 |
| POS29 = A and POS28 = C and POS24 = T and POS58 = A | IE | 0.002524 |
| POS29 = A and POS19 = C and POS20 = C and POS32 = G | IE | 0.003369 |
| POS32 = T and POS31 = G and POS35 = G and POS34 = A and POS33 = G | EI | 0.135690 |
| POS32 = T and POS31 = G and POS35 = G and POS33 = A | EI | 0.151194 |
| POS30 = G and POS32 = T and POS31 = G | EI | 0.081981 |
|  | N | 0.973203 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

pos29|pos30|pos31|pos32|pos35|class
---|---|---|---|---|---
n|n|n|n|n|ei
c|c|t|g|a|n
g|c|t|g|a|n
t|c|t|g|a|n
a|g|g|g|r|ei
c|t|t|g|a|ei
a|t|t|g|a|n
t|t|t|g|a|n
a|a|t|g|a|n
t|a|t|g|a|n
c|a|t|g|a|ei
c|c|t|c|a|ei
g|g|t|g|a|n
t|c|t|c|a|n
a|g|t|g|a|ie
a|c|t|c|a|n
t|g|t|g|a|n
g|c|t|c|a|n
t|c|a|g|a|ei
a|c|a|g|a|ei
g|t|t|c|a|ei
c|a|c|g|a|ei
t|a|c|g|a|ei
c|t|t|c|a|n
a|a|c|g|a|n
c|c|a|g|a|n
t|t|t|c|a|n
a|t|t|c|a|ei
c|c|t|g|t|n
g|c|a|g|a|n
t|c|t|g|t|n
a|a|t|c|a|ei
a|t|a|g|a|ei
a|g|c|g|a|ie
a|c|c|c|a|ei
g|c|c|c|a|ei
g|a|t|c|a|ei
g|t|t|g|t|n
t|a|t|c|a|n
c|t|t|g|t|n
t|c|c|c|a|n
a|t|t|g|t|n
c|a|t|c|a|n
t|t|t|g|t|ei
t|t|a|g|a|n
t|g|c|g|a|ei
c|c|c|c|a|n
c|a|t|g|t|ei
c|c|g|g|a|ei
a|c|g|g|a|n
g|a|t|g|t|ei
a|a|a|g|a|n
g|c|c|g|t|ei
g|t|c|c|a|n
a|c|c|g|t|ei
t|c|c|g|t|ei
t|a|t|g|t|n
t|c|g|g|a|ei
g|c|t|a|a|ei
a|a|t|g|t|n
g|a|a|g|a|n
c|t|c|c|a|n
c|t|c|g|t|ei
g|g|t|g|t|ei
c|c|t|c|t|n
a|c|a|c|a|n
g|t|t|a|a|ei
c|a|c|c|a|n
g|c|a|c|a|ei
g|t|g|g|a|n
t|t|t|a|a|ei
c|t|g|g|a|n
t|g|a|g|a|n
g|c|t|c|t|n
a|g|t|g|t|ie
t|c|t|c|t|n
t|g|t|g|t|n
a|g|a|g|a|ie
t|t|g|g|a|n
g|g|a|g|a|n
a|c|t|c|t|n
t|a|c|c|a|ei
c|t|t|a|a|n
a|t|g|g|a|n
g|a|c|c|a|n
t|c|c|a|a|ei
c|g|c|c|a|ei
t|c|a|g|t|ei
a|c|t|g|c|n
a|a|g|g|a|n
t|t|t|c|t|n
c|t|t|c|t|ei
g|t|a|c|a|ei
c|c|a|g|t|n
c|a|c|g|t|ei
c|a|t|a|a|n
a|t|a|c|a|ei
g|c|t|g|c|n
a|g|c|c|a|ie
g|g|c|c|a|n
g|c|a|g|t|n
g|a|t|a|a|ei
c|a|g|g|a|n
c|t|a|c|a|ei
a|t|t|c|t|n
c|c|c|a|a|ei
c|c|t|g|c|n
t|c|t|g|c|n
a|c|c|a|a|n
a|c|a|g|t|n
a|a|t|a|a|n
g|c|c|a|a|n
c|a|t|c|t|ei
c|a|a|c|a|ei
c|g|c|g|t|ei
g|t|c|a|a|ei
c|g|t|a|a|n
t|t|c|a|a|ei
t|c|t|t|a|n
g|a|t|c|t|ei
a|t|c|a|a|n
g|a|a|c|a|ei
t|t|t|g|c|ei
a|g|t|a|a|n
c|c|t|t|a|n
c|c|c|c|t|n
a|g|c|g|t|ie
t|c|c|c|t|ei
c|c|g|c|a|ei
g|g|c|g|t|n
g|c|c|c|t|n
t|g|g|g|a|n
c|t|c|a|a|n
g|t|t|g|c|n
g|c|t|t|a|ei
a|g|g|g|a|ie
g|g|g|g|a|n
c|t|t|g|c|n
g|a|t|g|c|ei
c|a|a|g|t|ei
g|t|c|c|t|ei
a|t|c|c|t|ei
t|c|c|g|c|ei
a|a|a|g|t|ei
c|t|t|t|a|ei
g|g|a|c|a|ei
a|t|g|c|a|ei
c|t|c|c|t|n
c|a|c|a|a|n
g|a|c|a|a|ei
c|c|g|g|t|n
c|c|c|g|c|n
a|g|a|c|a|ie
t|a|a|g|t|ei
t|g|a|c|a|n
a|a|c|a|a|n
c|t|g|c|a|ei
g|a|a|g|t|n
c|c|a|a|a|n
g|c|t|a|t|n
t|a|c|a|a|n
t|c|a|a|a|ei
t|g|t|c|t|n
g|t|g|c|a|n
g|c|a|a|a|n
g|t|t|t|a|ei
t|c|t|a|t|ei
c|a|t|g|c|ei
t|t|t|t|a|ei
t|t|c|c|t|ei
t|a|g|c|a|ei
t|g|a|g|t|ei
t|c|c|t|a|n
g|g|t|g|c|n
c|g|t|g|c|ei
a|t|a|a|a|ei
a|c|c|t|a|n
g|t|t|a|t|ei
t|a|c|c|t|ei
a|c|t|c|c|n
a|c|a|c|t|n
g|c|c|t|a|n
a|a|t|t|a|n
g|g|c|a|a|ei
g|t|g|g|t|n
t|t|c|g|c|ei
a|g|c|a|a|ie
g|t|a|a|a|n
c|a|g|c|a|ei
c|c|a|c|t|n
a|t|g|g|t|ei
c|t|t|a|t|ei
t|a|t|t|a|n
c|t|g|g|t|n
c|c|c|t|a|ei
c|a|t|t|a|n
g|c|t|c|c|n
t|t|a|a|a|n
g|c|a|c|t|ei
c|g|a|g|t|ei
g|a|t|t|a|ei
t|g|t|g|c|n
c|c|t|c|c|n
g|g|a|g|t|ei
t|t|g|g|t|n
c|a|c|c|t|n
a|g|t|g|c|ie
t|t|t|a|t|n
a|g|a|g|t|ie
a|a|c|c|t|n
t|c|a|c|t|n
t|c|t|c|c|n
t|a|t|a|t|ei
t|g|c|c|t|ei
g|t|a|c|t|ei
a|a|t|a|t|ei
t|g|g|c|a|ei
t|g|t|t|a|n
c|g|g|c|a|ei
c|t|t|c|c|n
g|c|a|g|c|ei
t|c|c|a|t|n
c|a|a|a|a|n
c|a|c|g|c|ei
c|g|t|t|a|n
c|a|g|g|t|n
t|t|a|c|t|n
g|c|c|a|t|n
t|a|c|g|c|ei
g|g|c|c|t|n
g|a|t|a|t|n
t|a|a|a|a|n
a|g|c|c|t|ie
a|a|g|g|t|ei
a|c|c|a|t|ei
t|c|a|g|c|n
a|g|g|c|a|ie
c|c|c|a|t|n
a|c|a|g|c|n
c|t|c|t|a|n
a|a|c|g|c|n
t|c|t|g|g|n
a|a|a|a|a|n
g|c|t|g|g|ei
t|t|t|c|c|n
a|g|t|t|a|ie
c|c|a|g|c|n
g|a|a|a|a|n
c|c|t|g|g|n
g|a|g|g|t|ei
t|t|c|a|t|ei
a|t|c|a|t|ei
c|c|t|t|t|n
c|t|t|g|g|ei
c|t|c|a|t|ei
a|t|a|g|c|ei
g|g|g|g|t|n
t|g|t|a|t|n
t|c|t|t|t|n
t|c|c|c|c|n
g|c|a|t|a|ei
t|g|a|a|a|n
a|t|g|a|a|n
a|g|t|a|t|ie
a|g|g|g|t|ie
a|g|a|a|a|ie
g|c|g|c|t|ei
t|a|c|t|a|n
a|a|c|t|a|n
c|a|t|c|c|n
a|c|a|t|a|n
t|g|g|g|t|n
g|a|c|t|a|n
g|t|c|a|t|n
t|t|g|a|a|n
t|t|t|g|g|ei
c|g|g|g|t|n
a|c|g|c|t|ei
g|t|g|a|a|ei
g|c|c|c|c|n
c|t|g|a|a|n
g|g|a|a|a|ei
g|a|t|c|c|n
c|c|c|g|g|ei
t|g|t|c|c|n
c|a|g|a|a|ei
a|c|c|g|g|ei
t|a|c|a|t|ei
g|c|g|g|c|ei
g|a|c|a|t|ei
a|a|a|g|c|ei
a|t|a|t|a|ei
c|a|c|a|t|n
t|c|c|g|g|ei
a|c|t|a|c|ei
c|t|c|c|c|n
t|c|t|a|c|ei
t|t|g|c|t|n
g|t|t|t|t|ei
g|g|c|t|a|n
c|g|c|t|a|n
c|a|t|g|g|n
g|a|g|a|a|ei
c|t|a|t|a|n
a|g|c|t|a|ie
g|g|t|c|c|ei
a|g|a|c|t|ie
g|t|g|c|t|n
a|a|c|a|t|ei
c|t|t|t|t|n
a|a|t|g|g|n
g|c|t|a|c|n
g|c|a|a|t|ei
a|t|g|c|t|n
t|t|a|t|a|ei
c|c|a|a|t|n
g|a|a|g|c|n
t|t|c|c|c|n
t|g|a|c|t|n
a|g|t|c|c|ie
c|t|g|c|t|n
t|a|a|g|c|n
t|a|g|a|a|ei
t|t|t|t|t|n
g|g|a|c|t|n
c|a|a|g|c|n
c|c|g|g|c|n
a|t|t|t|t|n
a|a|g|a|a|n
a|c|c|t|t|ei
t|t|t|a|c|ei
g|a|t|t|t|ei
c|t|t|a|c|ei
g|c|c|t|t|ei
c|g|c|a|t|ei
c|g|t|g|g|n
c|c|c|t|t|n
t|t|a|a|t|ei
c|g|a|g|c|n
g|g|g|a|a|n
g|g|c|a|t|ei
c|c|a|c|c|n
t|c|a|c|c|n
t|g|c|a|t|n
a|g|c|a|t|ie
a|g|a|g|c|ie
g|a|a|t|a|ei
t|a|t|t|t|ei
g|g|a|g|c|ei
c|c|g|t|a|ei
c|a|c|c|c|n
t|c|t|c|g|n
g|t|t|a|c|ei
a|a|a|t|a|ei
c|g|g|a|a|n
t|g|g|a|a|n
a|g|g|a|a|ie
g|g|t|g|g|n
c|c|t|c|g|n
a|a|g|c|t|ei
g|t|a|a|t|n
a|a|c|c|c|n
c|a|t|t|t|n
t|g|a|g|c|ie
a|c|a|c|c|n
g|a|c|c|c|n
c|t|a|a|t|ei
g|c|t|c|g|n
a|g|t|g|g|ie
t|c|c|t|t|n
c|t|g|g|c|n
t|g|t|g|g|n
c|a|g|c|t|n
a|a|t|t|t|n
g|a|c|g|g|ei
g|g|t|t|t|ei
g|t|t|c|g|ei
g|a|a|a|t|ei
c|c|a|g|g|n
c|a|c|g|g|ei
c|t|c|t|t|n
g|t|g|t|a|ei
g|c|g|a|t|ei
c|c|c|a|c|n
g|a|g|g|c|ei
t|a|c|g|g|ei
c|g|c|c|c|ei
t|t|t|c|g|ei
t|g|t|t|t|n
g|t|c|t|t|ei
a|t|t|c|g|ei
t|c|a|g|g|n
a|c|c|a|c|n
c|t|a|c|c|ei
a|g|c|c|c|ie
a|g|t|t|t|ie
a|g|a|t|a|ie
a|g|g|c|t|ie
t|g|c|c|c|n
a|c|a|g|g|n
g|c|a|g|g|n
g|a|t|a|c|ei
c|g|g|c|t|n
c|a|g|g|c|n
t|a|a|a|t|n
a|a|a|a|t|n
a|t|c|t|t|n
t|t|c|t|t|ei
a|a|t|a|c|n
a|t|g|t|a|ei
g|c|c|a|c|ei
t|t|g|t|a|n
a|a|g|g|c|n
t|c|c|a|c|n
c|t|g|t|a|n
g|g|c|c|c|n
a|g|t|a|c|ei
t|g|t|a|c|ei
c|c|g|c|c|ei
t|c|c|c|g|ei
g|a|t|c|g|n
g|a|a|c|c|ei
a|c|a|t|t|n
t|g|c|g|g|n
a|t|g|a|t|n
a|g|c|g|g|ie
t|a|a|c|c|ei
t|c|a|t|t|ei
c|a|c|t|t|n
t|t|g|a|t|n
g|a|g|t|a|n
t|g|g|g|c|ei
c|t|c|a|c|ei
t|c|t|t|c|n
c|c|c|c|g|n
c|t|g|a|t|n
a|a|a|c|c|n
a|t|a|g|g|n
a|a|c|t|t|n
c|a|g|t|a|ei
g|c|t|t|c|ei
g|t|g|a|t|n
a|g|g|g|c|ie
a|a|g|t|a|ei
t|t|a|g|g|ei
t|g|a|a|t|n
g|g|c|g|g|n
a|a|t|c|g|ei
g|c|c|c|g|n
g|t|c|a|c|n
a|g|a|a|t|ie
t|a|c|t|t|ei
g|g|a|a|t|n
t|t|c|a|c|n
g|c|a|t|t|n
g|c|g|c|c|n
g|g|g|g|c|n
c|c|t|t|c|n
a|c|c|c|g|n
c|a|a|c|c|n
c|c|a|t|t|n
c|a|t|c|g|n
a|t|c|c|g|ei
t|t|g|c|c|ei
g|g|g|t|a|ei
c|c|t|a|g|n
a|a|g|a|t|n
a|c|a|a|c|ei
c|g|t|c|g|ei
g|a|c|a|c|ei
a|a|c|a|c|n
a|c|g|g|g|ei
c|c|g|g|g|ei
t|a|a|g|g|ei
t|c|g|g|g|ei
t|g|a|c|c|n
c|g|g|t|a|ei
g|t|a|t|t|ei
a|g|c|t|t|ie
a|g|t|c|g|ie
a|g|g|t|a|ei
t|a|g|a|t|ei
t|g|g|t|a|ei
g|c|a|a|c|ei
t|g|t|c|g|n
a|t|a|t|t|ei
t|g|c|t|t|n
c|a|c|a|c|n
a|t|g|c|c|n
c|t|g|c|c|n
c|t|c|c|g|n
g|g|c|t|t|n
g|t|t|t|c|ei
t|c|a|a|c|n
g|t|g|c|c|ei
t|t|c|c|g|ei
a|g|a|c|c|ie
c|t|t|t|c|n
a|t|t|t|c|n
t|t|a|t|t|n
c|a|g|a|t|n
t|t|t|t|c|ei
g|g|t|c|g|ei
g|a|g|a|t|ei
g|t|a|a|c|ei
t|c|c|t|c|ei
g|a|t|t|c|ei
g|a|a|t|t|ei
a|a|g|c|c|ei
g|t|g|g|g|ei
a|t|g|g|g|ei
t|t|t|a|g|n
g|c|c|t|c|ei
c|a|t|t|c|ei
c|c|a|c|g|n
t|a|a|t|t|ei
g|g|a|g|g|n
c|t|a|a|c|ei
t|t|g|g|g|ei
t|a|c|c|g|n
g|c|a|c|g|ei
g|c|g|t|t|ei
a|g|g|a|t|ie
c|a|c|c|g|n
a|g|c|a|c|ie
t|a|g|c|c|n
a|c|c|t|c|ei
t|g|a|g|g|n
g|g|g|a|t|n
t|c|a|c|g|n
g|g|c|a|c|n
c|a|g|c|c|n
a|g|a|g|g|ie
c|t|g|g|g|n
a|c|a|c|g|ei
g|a|g|c|c|n
c|c|c|t|c|n
a|a|a|t|t|n
t|g|g|a|t|n
c|a|a|t|t|n
t|g|c|a|c|ei
g|a|c|c|g|n
t|t|a|a|c|n
t|c|g|t|t|n
c|t|t|a|g|ei
t|c|g|a|c|ei
c|a|t|a|g|ei
t|c|c|a|g|ei
c|g|t|t|c|ei
t|g|t|t|c|n
g|t|a|c|g|ei
c|t|a|c|g|n
a|a|g|g|g|ei
c|c|g|a|c|ei
t|g|g|c|c|ei
t|g|c|c|g|ei
a|c|g|a|c|ei
g|c|c|a|g|n
c|a|g|g|g|n
g|g|c|c|g|n
c|t|g|t|t|n
t|g|a|t|t|ei
c|c|c|a|g|ei
a|g|t|t|c|ie
a|g|a|t|t|ie
t|a|g|g|g|n
t|t|g|t|t|ei
a|g|c|c|g|ie
a|t|g|t|t|n
c|g|g|c|c|ei
t|a|a|a|c|ei
g|g|g|c|c|n
a|g|g|c|c|ie
g|t|g|t|t|n
g|g|a|t|t|ei
a|a|a|a|c|n
c|t|c|t|c|n
a|a|t|a|g|n
g|a|g|g|g|n
a|c|c|a|g|ei
t|t|c|t|c|n
g|c|g|a|c|ei
c|g|g|g|g|ei
c|c|t|t|g|n
g|a|a|c|g|ei
t|c|t|t|g|ei
a|g|t|a|g|ie
t|c|g|c|g|ei
a|c|g|c|g|ei
c|t|c|a|g|n
t|c|a|t|c|n
c|a|a|c|g|ei
c|c|g|c|g|n
g|g|a|a|c|n
a|a|c|t|c|ei
a|c|t|t|g|n
g|a|g|t|t|ei
g|c|g|c|g|ei
t|a|g|t|t|ei
a|g|g|g|g|ie
c|a|g|t|t|ei
a|a|a|c|g|ei
a|a|g|t|t|n
c|c|a|t|c|n
g|g|g|g|g|ei
g|c|t|t|g|n
c|a|c|t|c|n
a|t|g|a|c|n
t|a|c|t|c|n
t|g|a|a|c|n
g|g|t|a|g|ei
c|t|g|a|c|n
a|t|c|a|g|n
a|g|a|a|c|ie
g|t|g|a|c|n
g|a|c|t|c|ei
c|g|a|c|g|ei
c|t|a|t|c|ei
a|t|a|t|c|ei
t|g|c|t|c|n
t|a|c|a|g|ei
c|t|t|t|g|n
g|g|a|c|g|n
c|t|g|c|g|n
g|c|a|a|g|ei
c|a|g|a|c|n
t|g|a|c|g|ei
a|g|c|t|c|ie
a|g|a|c|g|ie
t|g|g|t|t|n
a|c|a|a|g|ei
g|t|t|t|g|n
t|c|a|a|g|n
g|g|g|t|t|n
a|g|g|t|t|ei
c|c|a|a|g|n
a|t|g|c|g|n
g|g|c|t|c|n
a|t|t|t|g|n
t|a|g|a|c|n
t|t|t|t|g|n
a|a|c|a|g|n
g|a|g|a|c|n
c|c|c|t|g|ei
t|g|c|a|g|ei
a|a|t|t|g|n
g|t|a|a|g|ei
c|a|t|t|g|ei
a|g|c|a|g|ie
t|a|a|t|c|ei
t|t|a|a|g|ei
c|g|c|a|g|n
g|a|t|t|g|ei
a|a|g|c|g|n
a|c|c|t|g|n
g|a|g|c|g|n
c|a|g|c|g|n
a|a|a|t|c|ei
c|a|a|t|c|n
g|a|a|t|c|n
t|g|g|a|c|ei
t|c|c|t|g|n
g|c|c|t|g|n
c|c|g|t|c|n
a|g|g|a|c|ie
g|g|c|a|g|n
t|c|g|t|c|ei
g|g|g|a|c|n
c|t|c|t|g|ei
a|a|a|a|g|n
g|g|t|t|g|ei
a|g|t|t|g|ie
g|c|g|a|g|ei
t|t|g|t|c|ei
a|t|g|t|c|ei
c|g|g|c|g|n
a|g|a|t|c|ie
g|g|g|c|g|n
g|a|a|a|g|n
c|c|g|a|g|ei
a|t|c|t|g|n
a|g|g|c|g|ie
t|g|g|c|g|ei
g|t|g|t|c|n
g|t|c|t|g|n
t|a|a|a|g|n
g|a|c|t|g|ei
g|t|g|a|g|n
t|c|a|t|g|ei
c|a|c|t|g|n
t|t|g|a|g|n
a|g|a|a|g|n
c|a|g|t|c|ei
g|c|a|t|g|ei
a|a|g|t|c|n
c|c|a|t|g|n
t|g|a|a|g|ei
c|t|g|a|g|n
c|g|a|a|g|ei
g|g|a|a|g|n
g|a|g|t|c|n
a|c|a|t|g|n
t|g|g|t|c|ei
g|t|a|t|g|ei
c|g|g|t|c|ei
c|t|a|t|g|ei
c|g|c|t|g|n
a|t|a|t|g|ei
a|a|g|a|g|n
a|g|c|t|g|ie
g|g|g|t|c|ei
a|g|g|t|c|ie
g|g|c|t|g|n
t|t|a|t|g|ei
t|g|c|t|g|n
c|a|g|a|g|n
g|a|g|a|g|ei
t|a|g|a|g|n
t|a|a|t|g|n
a|a|a|t|g|n
a|g|g|a|g|ie
t|c|g|t|g|ei
c|c|g|t|g|ei
g|c|g|t|g|ei
t|g|g|a|g|n
a|c|g|t|g|ei
c|g|g|a|g|n
g|g|g|a|g|ei
g|g|a|t|g|ei
t|g|a|t|g|n
a|g|a|t|g|ie
t|t|g|t|g|ei
a|t|g|t|g|ei
c|t|g|t|g|ei
g|t|g|t|g|ei
c|a|g|t|g|ei
a|a|g|t|g|ei
g|a|g|t|g|ei
g|g|g|t|g|ei
a|g|g|t|g|ei
c|g|g|t|g|ei
t|g|g|t|g|ei

## JRip

Decision list:

rules | predicted class
---|---
(POS29 = A) and (POS28 = C) and (POS30 = G) and (POS20 = T)|IE (287.0/33.0)
(POS29 = A) and (POS30 = G) and (POS21 = T) and (POS28 = C) and (POS24 = C)|IE (59.0/2.0)
(POS29 = A) and (POS30 = G) and (POS28 = T)|IE (145.0/21.0)
(POS29 = A) and (POS30 = G) and (POS28 = C) and (POS20 = C) and (POS19 = T)|IE (84.0/6.0)
(POS29 = A) and (POS30 = G) and (POS28 = C) and (POS24 = C) and (POS16 = T)|IE (28.0/1.0)
(POS29 = A) and (POS28 = C) and (POS30 = G) and (POS34 = C)|IE (59.0/18.0)
(POS29 = A) and (POS30 = G) and (POS21 = T) and (POS18 = T) and (POS17 = T)|IE (19.0/2.0)
(POS29 = A) and (POS28 = C) and (POS30 = G) and (POS31 = A)|IE (24.0/2.0)
(POS29 = A) and (POS30 = G) and (POS28 = C) and (POS32 = A) and (POS8 = C)|IE (11.0/1.0)
(POS29 = A) and (POS28 = C) and (POS30 = G) and (POS32 = C)|IE (17.0/4.0)
(POS29 = A) and (POS28 = C) and (POS24 = T) and (POS58 = A)|IE (19.0/8.0)
(POS29 = A) and (POS19 = C) and (POS20 = C) and (POS32 = G)|IE (11.0/2.0)
(POS32 = T) and (POS31 = G) and (POS35 = G) and (POS34 = A) and (POS33 = G)|EI (229.0/0.0)
(POS32 = T) and (POS31 = G) and (POS35 = G) and (POS33 = A)|EI (254.0/3.0)
(POS30 = G) and (POS32 = T) and (POS31 = G)|EI (171.0/32.0)
|N (1452.0/27.0)


## PART

Decision list:

rules | predicted class
---|---
POS30 = C AND POS31 = T|N (121.0)
POS30 = C AND POS31 = A|N (112.0/1.0)
POS30 = C AND POS31 = C|N (111.0)
POS30 = T AND POS35 = T|N (104.0)
POS30 = A AND POS32 = A|N (104.0/1.0)
POS29 = T AND POS31 = G AND POS32 = T AND POS35 = G|EI (79.0/2.0)
POS29 = T|N (236.0/6.0)
POS29 = C AND POS32 = T AND POS31 = G AND POS35 = G|EI (99.0/3.0)
POS29 = C|N (237.0/3.0)
POS29 = G AND POS32 = T AND POS31 = G AND POS35 = G|EI (95.0/5.0)
POS29 = G AND POS31 = C|N (58.0/1.0)
POS29 = G AND POS31 = A|N (52.0)
POS29 = G|N (134.0/11.0)
POS30 = T AND POS32 = T AND POS31 = G|EI (24.0/5.0)
POS30 = T|N (42.0)
POS30 = A AND POS31 = G AND POS32 = T|EI (35.0/6.0)
POS30 = A|N (59.0)
POS32 = G AND POS28 = C|IE (132.0/8.0)
POS32 = A AND POS28 = C|IE (129.0/10.0)
POS32 = C AND POS28 = C|IE (134.0/11.0)
POS32 = A AND POS28 = T|IE (46.0/4.0)
POS32 = A|N (30.0/4.0)
POS31 = C|IE (54.0/8.0)
POS31 = A AND POS28 = C|IE (51.0/1.0)
POS32 = G AND POS28 = T|IE (27.0/4.0)
POS32 = T AND POS31 = G AND POS35 = G AND POS28 = C|EI (134.0/14.0)
POS32 = C AND POS28 = T|IE (23.0/3.0)
POS32 = G|N (20.0/3.0)
POS32 = C AND POS55 = G|N (9.0/2.0)
POS31 = T|IE (29.0/4.0)
POS32 = T AND POS31 = G AND POS28 = A|EI (129.0/7.0)
POS32 = T AND POS31 = G AND POS28 = G|EI (64.0/2.0)
POS32 = T AND POS31 = G AND POS33 = G|IE (56.0/16.0)
POS32 = T AND POS33 = A AND POS28 = C|EI (35.0/6.0)
POS28 = C|IE (25.0)
POS28 = T AND POS24 = C|IE (8.0)
POS28 = A|N (11.0/4.0)
POS28 = T AND POS24 = G|EI (7.0)
POS28 = T|IE (8.0)
|N (6.0/2.0)


## J48 Decision Tree

* POS30 = G
	* POS29 = A
		* POS32 = T
			* POS31 = G
				* POS35 = G: EI (235.0/15.0)
				* POS35 = C
					* POS28 = C: IE (39.0/17.0)
					* POS28 = A: EI (8.0/2.0)
					* POS28 = T: IE (5.0)
					* POS28 = G: EI (2.0/1.0)
					* POS28 = N: IE (0.0)
				* POS35 = T: EI (41.0/21.0)
				* POS35 = A
					* POS28 = C
						* POS49 = G: IE (7.0/2.0)
						* POS49 = C: IE (7.0/1.0)
						* POS49 = A: IE (6.0/1.0)
						* POS49 = T: EI (5.0)
						* POS49 = N: IE (0.0)
					* POS28 = A: EI (9.0/1.0)
					* POS28 = T: IE (3.0/1.0)
					* POS28 = G: EI (5.0/1.0)
					* POS28 = N: EI (0.0)
				* POS35 = N: EI (0.0)
				* POS35 = R: EI (0.0)
			* POS31 = A
				* POS25 = C: IE (21.0)
				* POS25 = T: IE (26.0)
				* POS25 = G: N (2.0)
				* POS25 = A: IE (3.0)
				* POS25 = N: IE (0.0)
			* POS31 = C: IE (41.0/4.0)
			* POS31 = T: IE (23.0/2.0)
			* POS31 = N: EI (0.0)
		* POS32 = A
			* POS28 = C: IE (108.0/8.0)
			* POS28 = A: N (10.0/2.0)
			* POS28 = T
				* POS23 = C: IE (8.0)
				* POS23 = T: IE (25.0)
				* POS23 = G: N (3.0/1.0)
				* POS23 = A: IE (2.0)
				* POS23 = N: IE (0.0)
			* POS28 = G: N (13.0/1.0)
			* POS28 = N: IE (0.0)
		* POS32 = C: IE (159.0/26.0)
		* POS32 = G
			* POS28 = C: IE (115.0/8.0)
			* POS28 = A: N (9.0/2.0)
			* POS28 = T: IE (21.0/3.0)
			* POS28 = G: N (8.0/1.0)
			* POS28 = N: IE (0.0)
		* POS32 = N: IE (0.0)
	* POS29 = C
		* POS32 = T
			* POS34 = A: EI (41.0/1.0)
			* POS34 = G: EI (6.0/2.0)
			* POS34 = C: N (5.0/2.0)
			* POS34 = T: N (2.0)
			* POS34 = N: EI (0.0)
		* POS32 = A: N (10.0)
		* POS32 = C: N (9.0)
		* POS32 = G: N (11.0)
		* POS32 = N: EI (0.0)
	* POS29 = G
		* POS32 = T
			* POS31 = G
				* POS35 = G: EI (61.0)
				* POS35 = C: EI (5.0/1.0)
				* POS35 = T: N (8.0/3.0)
				* POS35 = A: EI (2.0/1.0)
				* POS35 = N: EI (0.0)
				* POS35 = R: EI (0.0)
			* POS31 = A: N (1.0)
			* POS31 = C: N (9.0)
			* POS31 = T: N (2.0)
			* POS31 = N: EI (0.0)
		* POS32 = A: N (29.0/1.0)
		* POS32 = C: N (27.0/1.0)
		* POS32 = G: N (28.0)
		* POS32 = N: N (0.0)
	* POS29 = T
		* POS31 = G
			* POS32 = T: EI (70.0/6.0)
			* POS32 = A: N (10.0)
			* POS32 = C: N (5.0/1.0)
			* POS32 = G: N (10.0)
			* POS32 = N: EI (0.0)
		* POS31 = A: N (27.0/1.0)
		* POS31 = C: N (19.0)
		* POS31 = T: N (27.0)
		* POS31 = N: N (0.0)
	* POS29 = N: IE (0.0)
* POS30 = A
	* POS32 = T
		* POS31 = G
			* POS34 = A
				* POS36 = T: EI (35.0)
				* POS36 = C: N (3.0/1.0)
				* POS36 = G: EI (10.0/1.0)
				* POS36 = A: N (7.0/3.0)
				* POS36 = N: EI (0.0)
				* POS36 = S: EI (0.0)
			* POS34 = G: N (3.0)
			* POS34 = C: N (5.0/1.0)
			* POS34 = T: EI (7.0/3.0)
			* POS34 = N: EI (0.0)
		* POS31 = A: N (16.0)
		* POS31 = C: N (23.0)
		* POS31 = T: N (17.0)
		* POS31 = N: N (0.0)
	* POS32 = A: N (94.0/1.0)
	* POS32 = C: N (81.0)
	* POS32 = G: N (71.0/1.0)
	* POS32 = N: N (0.0)
* POS30 = T: N (358.0/49.0)
* POS30 = C
	* POS31 = G
		* POS32 = T
			* POS36 = T: EI (15.0)
			* POS36 = C: N (2.0)
			* POS36 = G: EI (1.0)
			* POS36 = A: N (8.0/3.0)
			* POS36 = N: EI (0.0)
			* POS36 = S: EI (0.0)
		* POS32 = A: N (5.0)
		* POS32 = C: N (11.0)
		* POS32 = G: N (12.0)
		* POS32 = N: N (0.0)
	* POS31 = A: N (93.0/1.0)
	* POS31 = C: N (92.0)
	* POS31 = T: N (97.0)
	* POS31 = N: N (0.0)
* POS30 = N: EI (1.0)


## SimpleCart Decision Tree

	* POS30=(N)|(G)
		* POS32=(N)|(T)
			* POS31=(N)|(G)
					* POS35=(N)|(G)|(R): EI(464.0/22.0)
					* POS35!=(N)|(G)|(R)
							* POS33=(T)|(C)|(G)|(N)
						* POS28=(G)|(A): N(14.0/8.0)
						* POS28!=(G)|(A): IE(68.0/20.0)
							* POS33!=(T)|(C)|(G)|(N): EI(67.0/12.0)
			* POS31!=(N)|(G)
					* POS29=(T)|(G)|(C): N(42.0/0.0)
					* POS29!=(T)|(G)|(C): IE(121.0/12.0)
		* POS32!=(N)|(T)
				* POS29=(T)|(G)|(C): N(213.0/5.0)
				* POS29!=(T)|(G)|(C)
				* POS28=(G)|(A): N(57.0/15.0)
				* POS28!=(G)|(A): IE(455.0/39.0)
	* POS30!=(N)|(G)
					* POS35=(A)|(T)|(C)|(N)|(R): N(847.0/5.0)
					* POS35!=(A)|(T)|(C)|(N)|(R)
				* POS31=(T)|(C)|(A): N(186.0/1.0)
				* POS31!=(T)|(C)|(A)
					* POS32=(G)|(C)|(A): N(59.0/0.0)
					* POS32!=(G)|(C)|(A): EI(126.0/11.0)


