# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | N | 0.518996 |
| POS30 = G and POS32 = T and POS31 = G and POS35 != R and POS33 != T | EI | 0.176411 |
| POS30 = G and POS32 != T and POS29 != C and POS28 != G | IE | 0.128499 |
| POS30 = G and POS32 = T and POS31 != G and POS29 != T | IE | 0.047828 |
| POS30 != G and POS35 != R and POS32 != A and POS31 != T | EI | 0.012623 |
| POS29 = A and POS30 = G and POS31 = G and POS32 = T and POS35 = C | IE | 0.007113 |
| POS30 = G and POS29 = A and POS32 = T and POS31 = G and POS28 = T and POS24 = C | IE | 0.006384 |
| POS30 = G and POS29 = A and POS32 = T and POS31 = G and POS28 = C and POS35 = T and POS36 = C | IE | 0.005023 |
| POS30 = G and POS29 = A and POS32 = T and POS31 = G and POS28 = C and POS35 = A and POS49 = G | IE | 0.002803 |
| POS30 = G and POS29 = A and POS32 = T and POS31 = G and POS28 = C and POS35 = A and POS49 = C | IE | 0.002803 |
| POS30 = G and POS32 = T and POS31 = G and POS35 != R and POS33 != N | EI | 0.175101 |
| POS30 = G and POS29 = A and POS32 = T and POS31 = G and POS28 = C and POS35 = A and POS49 = A | IE | 0.001832 |
| POS30 = G and POS29 = A and POS32 = T and POS31 = G and POS28 = T and POS24 = T | IE | 0.002746 |
| POS30 = G and POS32 != T and POS29 != C and POS28 != A | IE | 0.124879 |
| POS30 = G and POS29 = A and POS32 = T and POS31 = G and POS28 = T and POS24 = A | IE | 0.000459 |
| POS29 = A and POS30 = C and POS31 = A and POS32 = G and POS35 = C | IE | 0.000153 |
| POS29 = T and POS30 = A and POS31 = C and POS32 = A and POS35 = G | EI | 0.000459 |
| POS29 = T and POS30 = G and POS31 = G and POS32 = C and POS35 = G | EI | 0.000153 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| POS30 != G and POS35 != G and POS33 != N and POS39 != G | N | 0.323198 |
| POS32 != T and POS29 != A and POS20 != N and POS56 != G and POS50 != C | N | 0.156995 |
| POS31 != G and POS29 != A and POS20 != N and POS59 != G | N | 0.128241 |
| POS32 != T and POS30 != G and POS56 != N and POS27 != T | N | 0.073203 |
| POS32 != T and POS29 != A and POS36 != T and POS20 != N and POS1 != T | N | 0.028186 |
| POS32 != T and POS28 = G and POS31 != T | N | 0.022684 |
| POS32 != T and POS30 != T and POS20 != N and POS29 != G and POS30 != A and POS28 != A and POS29 = A and POS25 != G and POS28 != G and POS26 != A and POS25 != A and POS30 = G and POS21 != A and POS15 != A and POS23 != G | IE | 0.242873 |
| POS31 != G and POS20 != N and POS30 != G and POS32 != G | N | 0.036017 |
| POS31 != G and POS20 != N and POS28 != A and POS29 = A and POS28 != G and POS25 != G and POS30 = G and POS18 != A and POS32 = T | IE | 0.118403 |
| POS32 = T and POS31 = G and POS35 = G and POS33 != C and POS34 != T and POS33 != T and POS34 = A and POS15 != T | EI | 0.442186 |
| POS32 != T and POS29 = A and POS28 != A and POS20 != A and POS17 != A and POS33 != G and POS37 != T and POS28 != G and POS30 = G and POS16 != G | IE | 0.163529 |
| POS31 != G and POS20 != N and POS22 = G and POS18 != A | N | 0.030466 |
| POS32 != T and POS29 = A and POS25 = T and POS13 != G and POS16 != A | IE | 0.062061 |
| POS31 != G and POS20 != N and POS28 = A and POS21 != T | N | 0.034250 |
| POS31 != G and POS20 != N and POS23 = G and POS6 != T | N | 0.023170 |
| POS31 != G and POS20 != N and POS41 != T and POS15 != A and POS49 != T and POS29 != T | IE | 0.070274 |
| POS32 = T and POS30 != G and POS33 = A and POS35 != T | EI | 0.098814 |
| POS30 != G and POS36 != T and POS51 != G | N | 0.052710 |
| POS31 != G and POS41 != A and POS52 != T and POS35 != C | N | 0.025010 |
| POS32 = T and POS29 != A and POS33 != C and POS30 != T and POS35 != A and POS35 = G and POS14 != T | EI | 0.268482 |
| POS32 = T and POS29 != A and POS9 != T and POS10 != T and POS50 != T and POS1 != T and POS11 != T | EI | 0.100478 |
| POS29 != A and POS3 != A and POS32 != G and POS46 != T and POS35 != G | N | 0.042701 |
| POS32 = T and POS28 = T and POS22 != A and POS24 != G | IE | 0.079861 |
| POS32 = T and POS28 != C and POS33 != T and POS28 != T and POS29 = A and POS43 != A | EI | 0.388473 |
| POS32 = T and POS29 != C and POS29 != A and POS3 != C | EI | 0.027412 |
| POS32 = T and POS29 = A and POS33 = A and POS34 != T and POS51 != A | EI | 0.229601 |
| POS32 = T and POS29 = A and POS28 != A and POS28 != G and POS31 = G and POS35 != G and POS23 = A and POS9 != T | EI | 0.069182 |
| POS35 = G and POS29 != A and POS21 = C | N | 0.021739 |
| POS35 = G and POS32 != G and POS36 = T | EI | 0.177316 |
| POS28 != A and POS32 = T and POS28 != G and POS31 = G and POS23 = T | IE | 0.294424 |
| POS28 = C and POS32 = T and POS25 != A and POS26 != A and POS14 != G and POS23 != A and POS13 = C | IE | 0.234043 |
| POS32 != T and POS29 != G and POS22 != G and POS23 != A and POS15 != G and POS6 != A and POS28 = C | IE | 0.208791 |
| POS32 != T and POS25 != T and POS26 != T and POS9 != T | N | 0.181159 |
| POS32 = G and POS16 != A | N | 0.040506 |
| POS28 != T and POS19 = A | EI | 0.168421 |
| POS45 = A and POS26 != A and POS40 != A | IE | 0.171247 |
| POS45 != A and POS35 = C and POS22 != G | IE | 0.250000 |
| POS45 != A and POS28 != A and POS42 = A and POS3 != C | IE | 0.142857 |
| POS45 != A and POS35 != C and POS29 = A and POS59 != T and POS48 != A | EI | 0.428571 |
| POS44 != G and POS15 != T and POS35 != C and POS7 != G | IE | 0.357143 |
| POS44 != G and POS9 != G | N | 0.476471 |
|  | EI | 0.800000 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| POS29 = A and POS28 = C and POS30 = G and POS31 = A | IE | 0.066134 |
| POS29 = A and POS28 = C and POS30 = G and POS20 = T and POS22 = T | IE | 0.041881 |
| POS29 = A and POS30 = G and POS21 = T and POS26 = T | IE | 0.039759 |
| POS29 = A and POS30 = G and POS19 = T and POS17 = T and POS28 = C | IE | 0.017813 |
| POS29 = A and POS30 = G and POS28 = C and POS22 = C | IE | 0.030090 |
| POS29 = A and POS30 = G and POS28 = T | IE | 0.028314 |
| POS29 = A and POS28 = C and POS24 = C and POS30 = G and POS23 = T | IE | 0.008216 |
| POS29 = A and POS28 = C and POS22 = T and POS44 = T | IE | 0.006147 |
| POS29 = A and POS28 = C and POS30 = G and POS33 = T | IE | 0.003559 |
| POS29 = A and POS28 = C and POS30 = G and POS33 = C | IE | 0.003791 |
| POS32 = T and POS31 = G and POS35 = G and POS34 = A | EI | 0.222733 |
| POS32 = T and POS31 = G and POS30 = G and POS35 = G | EI | 0.080839 |
| POS31 = G and POS32 = T and POS30 = G and POS33 = A | EI | 0.040302 |
| POS31 = G and POS32 = T and POS29 = A and POS7 = C and POS37 = C | EI | 0.007161 |
|  | N | 0.956941 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

pos29|pos30|pos31|pos32|pos35|class
---|---|---|---|---|---
n|n|n|n|n|ei
g|c|t|g|a|n
t|c|t|g|a|n
c|c|t|g|a|n
t|t|t|g|a|n
a|t|t|g|a|n
c|t|t|g|a|ei
a|a|t|g|a|n
c|a|t|g|a|ei
t|a|t|g|a|ei
g|g|t|g|a|n
a|g|t|g|a|ie
a|c|t|c|a|n
c|g|t|g|a|ei
g|c|t|c|a|ei
t|g|t|g|a|ei
c|c|t|c|a|n
t|c|t|c|a|n
t|c|a|g|a|ei
c|a|c|g|a|ei
g|t|t|c|a|ei
g|c|t|g|t|ei
a|c|a|g|a|ei
c|t|t|c|a|n
a|t|t|c|a|ei
c|c|a|g|a|n
g|c|a|g|a|n
t|c|t|g|t|n
c|c|t|g|t|n
t|a|c|g|a|ei
a|a|c|g|a|n
t|t|t|c|a|n
t|c|c|c|a|n
a|c|c|c|a|ei
a|a|t|c|a|n
g|a|t|c|a|n
t|t|t|g|t|n
g|t|t|g|t|n
t|t|a|g|a|n
a|t|a|g|a|ei
a|t|t|g|t|n
a|g|c|g|a|ie
c|c|c|c|a|n
t|a|t|c|a|n
c|t|t|g|t|n
g|c|c|c|a|ei
c|a|t|c|a|n
c|a|t|g|t|ei
g|c|t|a|a|ei
t|c|g|g|a|ei
a|c|c|g|t|ei
t|a|t|g|t|n
t|a|a|g|a|ei
a|c|g|g|a|ei
g|a|t|g|t|n
g|a|a|g|a|n
c|t|c|c|a|n
c|c|g|g|a|ei
g|t|c|c|a|n
g|c|c|g|t|ei
a|a|t|g|t|n
a|a|a|g|a|n
c|a|a|g|a|ei
t|a|c|c|a|ei
c|t|t|a|a|n
t|g|a|g|a|n
a|g|t|g|t|ie
c|a|c|c|a|n
t|t|g|g|a|n
c|t|c|g|t|n
a|g|a|g|a|ie
t|t|t|a|a|ei
g|c|a|c|a|ei
c|t|g|g|a|n
t|g|t|g|t|n
a|t|g|g|a|n
g|c|t|c|t|n
c|c|t|c|t|n
g|a|c|c|a|n
g|t|t|a|a|ei
a|c|a|c|a|n
a|c|t|c|t|n
t|c|t|c|t|n
g|g|a|g|a|n
t|t|c|g|t|ei
g|t|g|g|a|n
c|a|c|g|t|ei
a|t|a|c|a|ei
c|t|a|c|a|ei
c|c|a|g|t|n
t|c|c|a|a|ei
a|c|c|a|a|n
a|a|g|g|a|n
t|t|t|c|t|n
g|t|a|c|a|ei
c|c|t|g|c|n
t|c|a|g|t|ei
a|a|t|a|a|n
c|a|g|g|a|n
c|t|t|c|t|ei
g|c|c|a|a|n
t|g|c|c|a|n
g|g|c|c|a|n
c|c|c|a|a|n
a|c|a|g|t|n
g|c|a|g|t|n
a|c|t|g|c|n
a|t|t|c|t|n
g|a|t|a|a|ei
g|c|t|g|c|n
a|g|c|c|a|ie
t|c|t|g|c|n
c|a|t|a|a|n
c|g|c|c|a|ei
a|t|c|a|a|n
c|a|a|c|a|ei
c|a|t|c|t|ei
a|t|t|g|c|ei
g|c|c|c|t|n
c|t|c|a|a|n
c|c|g|c|a|n
c|c|t|t|a|n
c|t|t|g|c|ei
g|a|a|c|a|n
t|t|t|g|c|ei
t|g|g|g|a|n
g|t|c|a|a|ei
c|g|c|g|t|ei
g|t|t|g|c|n
t|c|t|t|a|n
a|g|c|g|t|ie
t|c|c|c|t|ei
c|g|t|a|a|n
a|g|t|a|a|n
a|g|g|g|a|ie
t|t|c|a|a|ei
g|g|g|g|a|n
g|c|t|t|a|n
g|a|t|c|t|ei
g|g|t|a|a|ei
c|c|c|c|t|n
g|g|c|g|t|n
g|g|a|c|a|ei
c|c|a|a|a|ei
c|a|c|a|a|ei
t|c|c|g|c|ei
c|t|c|c|t|ei
g|a|t|g|c|ei
g|a|c|a|a|ei
t|t|t|t|a|ei
g|c|t|a|t|ei
g|t|t|t|a|ei
t|c|t|a|t|ei
g|t|c|c|t|ei
t|c|a|a|a|ei
t|a|a|g|t|ei
c|t|t|t|a|ei
t|a|c|a|a|n
g|t|g|c|a|n
a|g|a|c|a|ie
c|a|t|g|c|ei
a|t|g|c|a|ei
t|t|c|c|t|ei
a|a|c|a|a|n
t|g|t|c|t|n
g|a|a|g|t|n
c|c|g|g|t|n
a|t|c|c|t|ei
t|g|a|c|a|n
c|t|g|c|a|ei
g|c|a|a|a|n
c|c|c|g|c|n
g|t|t|a|t|ei
t|a|c|c|t|ei
g|g|c|a|a|ei
a|t|g|g|t|ei
g|a|g|c|a|ei
a|t|a|a|a|ei
t|t|c|g|c|ei
t|t|t|a|t|n
g|g|t|g|c|n
g|c|c|t|a|n
t|g|t|g|c|n
t|g|a|g|t|ei
a|c|c|t|a|n
a|a|c|c|t|ei
t|t|g|g|t|n
a|g|t|g|c|ie
c|c|c|t|a|n
a|t|c|g|c|ei
t|g|c|a|a|ei
c|t|t|a|t|ei
g|c|a|c|t|ei
t|c|a|c|t|n
t|a|t|t|a|n
c|g|a|g|t|ei
t|t|a|a|a|n
a|c|t|c|c|n
c|t|g|g|t|n
a|g|c|a|a|ie
g|g|a|g|t|ei
a|g|a|g|t|ie
c|c|t|c|c|n
c|g|t|g|c|ei
g|t|a|a|a|n
g|a|t|t|a|ei
c|c|a|c|t|ei
g|c|t|c|c|n
a|a|t|t|a|n
a|c|a|c|t|n
g|t|g|g|t|n
c|a|t|t|a|n
c|a|g|c|a|ei
t|c|c|t|a|n
t|a|g|c|a|ei
c|a|c|c|t|n
t|c|t|c|c|n
a|a|c|g|c|ei
t|t|t|c|c|n
g|c|a|g|c|n
t|a|a|a|a|ei
c|g|g|c|a|ei
g|a|g|g|t|ei
g|c|t|g|g|ei
g|g|t|t|a|ei
c|a|a|a|a|n
t|g|c|c|t|ei
t|g|g|c|a|ei
g|g|g|c|a|ei
a|g|c|c|t|ie
t|a|c|g|c|ei
t|t|a|c|t|n
a|a|t|a|t|ei
c|a|c|g|c|ei
a|g|g|c|a|ie
c|c|c|a|t|n
a|c|c|a|t|ei
c|t|t|c|c|n
g|c|c|a|t|n
c|t|c|t|a|n
c|c|t|g|g|n
c|g|t|t|a|n
t|g|t|t|a|n
c|c|a|g|c|n
a|a|g|g|t|n
a|a|a|a|a|n
t|c|c|a|t|n
g|a|a|a|a|n
t|a|t|a|t|ei
g|a|t|a|t|n
g|g|c|c|t|n
a|g|t|t|a|ie
a|c|a|g|c|ie
t|c|t|g|g|n
c|a|g|g|t|n
g|t|a|c|t|ei
t|c|a|g|c|n
t|g|c|g|c|ei
g|c|g|c|t|ei
a|t|g|a|a|n
g|g|g|g|t|n
t|g|t|a|t|n
a|c|g|c|t|ei
t|a|c|t|a|n
c|c|t|t|t|n
a|g|t|a|t|ie
a|t|c|a|t|ei
a|c|c|c|c|ei
g|c|c|c|c|n
a|g|g|g|t|ie
a|g|a|a|a|ie
t|c|t|t|t|n
g|g|a|a|a|ei
a|a|a|c|t|ei
t|t|g|a|a|n
c|t|g|a|a|n
c|t|t|g|g|ei
t|t|c|a|t|ei
a|c|a|t|a|n
c|g|g|g|t|ei
a|a|c|t|a|n
g|a|c|t|a|n
g|c|a|t|a|ei
t|g|g|g|t|n
a|t|a|g|c|ei
g|t|g|a|a|ei
t|c|c|c|c|n
g|a|t|c|c|n
t|g|a|a|a|n
g|t|c|a|t|n
c|a|t|c|c|n
g|t|t|t|t|ei
g|c|c|g|g|ei
a|a|t|g|g|n
t|t|a|t|a|ei
a|c|a|a|t|ei
a|a|a|g|c|ei
g|g|c|t|a|ei
g|c|g|g|c|n
g|a|a|g|c|n
t|g|t|c|c|n
g|c|a|a|t|ei
c|a|t|g|g|n
t|a|a|g|c|n
c|t|t|t|t|n
t|a|c|a|t|ei
g|t|g|c|t|n
c|t|g|c|t|ei
a|g|a|c|t|ie
a|g|c|t|a|ie
c|c|c|g|g|ei
c|a|g|a|a|ei
t|c|t|a|c|n
t|t|t|t|t|n
t|g|c|t|a|ei
g|t|c|c|c|ei
a|a|c|a|t|ei
a|t|a|t|a|ei
g|g|t|c|c|ei
a|g|t|c|c|ie
g|c|t|a|c|n
a|c|t|a|c|ei
t|t|c|c|c|n
g|a|g|a|a|ei
t|t|g|c|t|n
a|c|c|g|g|ei
t|c|c|g|g|ei
c|t|a|t|a|n
t|a|g|a|a|ei
c|t|c|c|c|n
c|a|c|a|t|n
a|t|t|t|t|n
c|a|a|g|c|n
t|g|a|c|t|n
a|a|g|a|a|n
g|g|a|c|t|n
a|t|g|c|t|n
c|c|a|a|t|n
c|c|g|g|c|n
t|t|g|g|c|ei
g|g|a|g|c|ei
c|t|g|g|c|ei
c|t|a|a|t|ei
t|a|t|t|t|ei
a|c|c|t|t|ei
a|c|a|c|c|n
c|t|t|a|c|ei
c|a|c|c|c|n
c|c|t|c|g|n
t|g|c|a|t|ei
a|a|a|t|a|ei
t|c|t|c|g|n
a|a|c|c|c|n
c|g|g|a|a|n
a|c|t|c|g|ei
t|t|a|a|t|ei
g|c|c|t|t|ei
c|a|t|t|t|n
a|a|g|c|t|ei
c|g|t|g|g|n
c|c|g|t|a|ei
a|a|t|t|t|n
c|g|a|g|c|n
c|a|g|c|t|n
c|g|c|a|t|ei
a|g|g|a|a|ie
g|c|t|c|g|n
g|g|t|g|g|n
a|g|a|g|c|ie
g|g|c|a|t|ei
a|g|t|g|g|ie
c|c|a|c|c|n
t|c|a|c|c|n
g|g|g|a|a|n
g|t|a|a|t|n
t|g|g|a|a|n
t|c|c|t|t|n
a|g|c|a|t|ie
t|t|t|a|c|n
g|t|t|a|c|n
g|a|c|c|c|n
t|g|a|g|c|ie
c|c|c|t|t|n
t|g|t|g|g|n
g|a|a|t|a|n
t|t|t|c|g|ei
g|a|g|g|c|ei
t|a|c|g|g|ei
g|c|g|a|t|ei
g|t|c|t|t|ei
a|c|a|g|g|ei
g|a|c|g|g|ei
a|t|g|t|a|ei
g|t|g|t|a|ei
a|g|c|c|c|ie
a|g|t|t|t|ie
a|g|a|t|a|ie
c|a|g|g|c|n
a|a|g|g|c|n
c|a|c|g|g|n
c|c|c|a|c|ei
g|g|t|t|t|ei
t|c|c|a|c|n
c|t|c|t|t|n
c|t|g|t|a|n
a|g|g|c|t|ie
g|a|a|a|t|ei
c|g|g|c|t|n
a|a|a|a|t|n
t|g|t|t|t|n
g|t|t|c|g|ei
t|a|a|a|t|n
t|c|a|g|g|n
g|c|c|a|c|ei
t|g|c|c|c|n
c|t|a|c|c|ei
g|g|c|c|c|n
t|t|g|t|a|n
a|a|t|a|c|n
t|t|c|t|t|n
g|c|a|g|g|n
a|t|c|t|t|n
a|c|c|a|c|n
c|c|a|g|g|n
a|g|t|a|c|ei
t|c|c|c|g|ei
t|t|a|g|g|ei
t|g|t|a|c|n
g|g|c|g|g|n
c|g|g|g|c|ei
c|t|c|a|c|ei
t|a|a|c|c|ei
g|g|a|a|t|n
a|c|t|t|c|ei
a|a|g|t|a|ei
g|c|g|c|c|n
a|c|c|c|g|n
g|a|a|c|c|ei
t|t|g|a|t|n
t|a|c|t|t|n
a|t|a|g|g|n
g|a|g|t|a|n
a|c|a|t|t|n
g|c|c|c|g|n
c|c|g|c|c|ei
c|c|c|c|g|n
c|a|c|t|t|n
c|a|a|c|c|n
t|g|g|g|c|ei
a|g|a|a|t|ie
g|c|t|t|c|ei
t|c|a|t|t|ei
c|a|t|c|g|n
c|c|t|t|c|n
t|t|c|a|c|n
a|g|c|g|g|ie
t|g|c|g|g|n
g|c|a|t|t|ei
g|g|g|g|c|n
g|t|c|a|c|n
a|g|g|g|c|ie
a|a|c|t|t|n
t|g|a|a|t|n
a|a|t|c|g|n
g|t|g|a|t|n
c|a|g|t|a|ei
c|t|g|a|t|n
c|c|a|t|t|n
a|a|a|c|c|n
a|t|g|a|t|n
t|c|t|t|c|n
g|t|a|t|t|ei
g|a|g|a|t|ei
g|t|t|t|c|ei
a|t|a|t|t|ei
t|t|c|c|g|ei
c|c|g|g|g|ei
c|g|g|t|a|ei
c|g|t|c|g|ei
a|a|c|a|c|n
t|g|c|t|t|n
t|c|g|g|g|ei
t|a|a|g|g|ei
g|c|a|a|c|ei
a|t|g|c|c|n
a|g|g|t|a|ei
a|g|t|c|g|ie
g|t|g|c|c|ei
t|g|t|c|g|n
a|c|g|g|g|ei
a|g|a|c|c|ie
c|a|c|a|c|n
t|g|a|c|c|n
g|g|g|t|a|ei
a|g|c|t|t|ie
a|a|g|a|t|n
g|g|t|c|g|n
a|c|a|a|c|ei
t|g|g|t|a|ei
t|c|a|a|c|n
c|c|t|a|g|n
a|t|c|c|g|ei
c|t|t|t|c|n
g|g|c|t|t|n
c|t|c|c|g|n
g|a|a|g|g|n
c|t|g|c|c|n
a|t|t|t|c|n
c|t|a|t|t|ei
c|a|g|a|t|n
g|a|c|a|c|ei
t|t|t|t|c|ei
a|a|g|c|c|ei
g|a|a|t|t|ei
g|c|c|t|c|ei
c|t|a|a|c|ei
g|a|c|c|g|n
c|c|a|c|g|ei
t|c|g|t|t|n
t|c|c|t|c|ei
t|t|t|a|g|n
g|g|c|a|c|ei
c|t|g|g|g|n
g|t|a|a|c|ei
g|g|g|a|t|ei
g|c|g|t|t|ei
a|t|g|g|g|ei
t|t|g|g|g|ei
c|t|t|a|g|ei
a|g|a|g|g|ie
a|g|g|a|t|ie
t|a|a|t|t|ei
t|g|a|g|g|ei
t|c|a|c|g|n
c|a|t|t|c|ei
t|t|a|a|c|n
c|c|c|t|c|n
a|c|c|t|c|ei
t|a|c|c|g|n
t|g|c|a|c|ei
t|g|g|a|t|n
t|a|g|c|c|n
g|g|a|g|g|n
a|g|c|a|c|ie
g|c|a|c|g|ei
a|c|a|c|g|ei
c|a|c|c|g|ei
a|a|a|t|t|n
g|a|g|c|c|n
c|a|g|c|c|n
c|a|a|t|t|n
t|g|a|t|t|ei
t|a|a|a|c|ei
c|g|g|c|c|ei
a|a|t|a|g|n
g|c|g|a|c|ei
c|g|t|t|c|ei
c|t|a|c|g|n
g|g|a|t|t|ei
t|g|c|c|g|ei
a|c|g|a|c|ei
c|a|t|a|g|ei
a|g|t|t|c|ie
a|g|a|t|t|ie
t|c|c|a|g|ei
g|t|a|c|g|ei
a|t|g|t|t|n
t|g|t|t|c|n
g|t|g|t|t|n
a|a|g|g|g|n
g|g|c|c|g|n
c|t|c|t|c|n
a|g|c|c|g|n
c|t|g|t|t|n
a|c|c|a|g|ei
t|t|c|t|c|n
a|g|g|c|c|ie
c|c|g|a|c|ei
c|a|g|g|g|n
g|a|g|g|g|n
g|a|a|a|c|ei
t|a|g|g|g|n
t|c|g|a|c|ei
t|g|g|c|c|ei
a|a|a|a|c|n
g|g|g|c|c|n
t|t|g|t|t|ei
c|c|c|a|g|ei
g|c|c|a|g|n
t|a|g|t|t|ei
g|a|g|t|t|ei
g|g|t|a|g|ei
c|c|t|t|g|ei
c|g|g|g|g|ei
g|g|g|g|g|ei
c|c|g|c|g|n
c|t|c|a|g|n
t|g|a|a|c|n
c|a|c|t|c|ei
g|a|c|t|c|ei
a|a|c|t|c|ei
a|g|t|a|g|ie
a|g|g|g|g|ie
c|t|g|a|c|n
t|c|a|t|c|n
t|g|g|g|g|n
t|a|c|t|c|n
g|c|t|t|g|ei
c|a|a|c|g|ei
g|a|a|c|g|ei
a|a|g|t|t|n
a|g|a|a|c|ie
a|t|c|a|g|n
a|c|t|t|g|n
c|c|a|t|c|n
a|t|g|a|c|n
g|g|a|a|c|n
t|c|g|c|g|ei
g|t|g|a|c|n
a|c|g|c|g|ei
a|a|a|c|g|n
t|a|c|a|g|ei
t|t|t|t|g|n
c|t|a|t|c|ei
a|t|t|t|g|n
g|a|g|a|c|ei
a|a|c|a|g|n
g|c|a|a|g|ei
c|t|t|t|g|n
t|a|g|a|c|n
t|g|g|t|t|ei
a|g|g|t|t|ei
a|g|c|t|c|ie
t|g|a|c|g|ei
g|a|c|a|g|ei
g|g|c|t|c|n
g|g|a|c|g|n
a|t|a|t|c|ei
g|g|g|t|t|n
a|t|g|c|g|n
a|c|a|a|g|ei
c|a|g|a|c|n
g|t|t|t|g|n
a|a|g|a|c|ei
t|g|c|t|c|n
c|c|a|a|g|n
t|c|a|a|g|ei
a|g|a|c|g|ie
c|g|a|c|g|ei
c|t|g|c|g|n
c|g|c|a|g|ei
t|c|c|t|g|n
c|a|a|t|c|n
c|c|g|t|c|n
g|t|a|a|g|ei
g|c|c|t|g|n
t|g|g|a|c|n
a|a|t|t|g|ei
a|a|g|c|g|n
a|t|a|a|g|ei
c|a|g|c|g|n
g|g|g|a|c|n
t|a|t|t|g|ei
g|g|c|a|g|n
g|a|g|c|g|n
a|a|a|t|c|n
t|a|a|t|c|ei
c|c|c|t|g|ei
t|g|c|a|g|n
a|g|c|a|g|ie
g|a|a|t|c|n
a|g|g|a|c|ie
t|t|g|t|c|ei
c|g|g|c|g|n
a|g|t|t|g|ie
a|g|g|c|g|ie
a|g|a|t|c|ie
g|g|t|t|g|ei
a|t|c|t|g|n
t|g|g|c|g|ei
t|a|a|a|g|n
c|t|c|t|g|ei
a|t|g|t|c|n
c|c|g|a|g|ei
g|a|a|a|g|n
t|g|t|t|g|ei
t|t|c|t|g|ei
a|a|a|a|g|n
g|g|g|c|g|n
g|t|c|t|g|n
g|t|g|t|c|n
g|a|g|t|c|n
c|a|g|t|c|ei
c|c|a|t|g|ei
g|a|c|t|g|ei
c|g|a|a|g|ei
c|t|g|a|g|n
a|g|a|a|g|ie
g|c|a|t|g|ei
c|a|c|t|g|n
t|t|g|a|g|n
a|a|g|t|c|n
t|g|a|a|g|ei
g|g|a|a|g|n
a|c|a|t|g|n
g|t|g|a|g|n
t|c|a|t|g|ei
t|t|a|t|g|ei
c|g|c|t|g|n
t|g|g|t|c|n
g|g|g|t|c|ei
a|g|c|t|g|ie
c|g|g|t|c|ei
a|t|a|t|g|ei
t|g|c|t|g|n
a|g|g|t|c|ie
c|a|g|a|g|n
g|a|g|a|g|ei
t|a|g|a|g|n
a|a|g|a|g|n
g|g|c|t|g|n
t|c|g|t|g|ei
t|a|a|t|g|n
g|c|g|t|g|ei
a|c|g|t|g|ei
a|g|g|a|g|ie
g|g|g|a|g|ei
a|a|a|t|g|n
c|g|g|a|g|n
c|c|g|t|g|ei
t|g|g|a|g|n
c|a|a|t|g|ei
g|g|a|t|g|ei
t|t|g|t|g|ei
a|t|g|t|g|ei
g|t|g|t|g|ei
a|g|a|t|g|ie
t|g|a|t|g|n
c|t|g|t|g|ei
a|a|g|t|g|ei
c|a|g|t|g|ei
g|a|g|t|g|ei
g|g|g|t|g|ei
c|g|g|t|g|ei
a|g|g|t|g|ei
t|g|g|t|g|ei

## JRip

Decision list:

rules | predicted class
---|---
(POS29 = A) and (POS28 = C) and (POS30 = G) and (POS31 = A)|IE (168.0/7.0)
(POS29 = A) and (POS28 = C) and (POS30 = G) and (POS20 = T) and (POS22 = T)|IE (104.0/4.0)
(POS29 = A) and (POS30 = G) and (POS21 = T) and (POS26 = T)|IE (118.0/14.0)
(POS29 = A) and (POS30 = G) and (POS19 = T) and (POS17 = T) and (POS28 = C)|IE (48.0/4.0)
(POS29 = A) and (POS30 = G) and (POS28 = C) and (POS22 = C)|IE (142.0/44.0)
(POS29 = A) and (POS30 = G) and (POS28 = T)|IE (101.0/21.0)
(POS29 = A) and (POS28 = C) and (POS24 = C) and (POS30 = G) and (POS23 = T)|IE (20.0/1.0)
(POS29 = A) and (POS28 = C) and (POS22 = T) and (POS44 = T)|IE (19.0/3.0)
(POS29 = A) and (POS28 = C) and (POS30 = G) and (POS33 = T)|IE (22.0/7.0)
(POS29 = A) and (POS28 = C) and (POS30 = G) and (POS33 = C)|IE (25.0/8.0)
(POS32 = T) and (POS31 = G) and (POS35 = G) and (POS34 = A)|EI (399.0/1.0)
(POS32 = T) and (POS31 = G) and (POS30 = G) and (POS35 = G)|EI (118.0/4.0)
(POS31 = G) and (POS32 = T) and (POS30 = G) and (POS33 = A)|EI (69.0/6.0)
(POS31 = G) and (POS32 = T) and (POS29 = A) and (POS7 = C) and (POS37 = C)|EI (11.0/0.0)
|N (1505.0/59.0)


## PART

Decision list:

rules | predicted class
---|---
POS30 != G AND POS35 != G AND POS33 != N AND POS39 != G|N (659.0)
POS32 != T AND POS29 != A AND POS20 != N AND POS56 != G AND POS50 != C|N (257.0)
POS31 != G AND POS29 != A AND POS20 != N AND POS59 != G|N (205.0/1.0)
POS32 != T AND POS30 != G AND POS56 != N AND POS27 != T|N (109.0)
POS32 != T AND POS29 != A AND POS36 != T AND POS20 != N AND POS1 != T|N (41.0)
POS32 != T AND POS28 = G AND POS31 != T|N (34.0/1.0)
POS32 != T AND POS30 != T AND POS20 != N AND POS29 != G AND POS30 != A AND POS28 != A AND POS29 = A AND POS25 != G AND POS28 != G AND POS26 != A AND POS25 != A AND POS30 = G AND POS21 != A AND POS15 != A AND POS23 != G|IE (283.0/1.0)
POS31 != G AND POS20 != N AND POS30 != G AND POS32 != G|N (42.0)
POS31 != G AND POS20 != N AND POS28 != A AND POS29 = A AND POS28 != G AND POS25 != G AND POS30 = G AND POS18 != A AND POS32 = T|IE (114.0/1.0)
POS32 = T AND POS31 = G AND POS35 = G AND POS33 != C AND POS34 != T AND POS33 != T AND POS34 = A AND POS15 != T|EI (348.0)
POS32 != T AND POS29 = A AND POS28 != A AND POS20 != A AND POS17 != A AND POS33 != G AND POS37 != T AND POS28 != G AND POS30 = G AND POS16 != G|IE (97.0/1.0)
POS31 != G AND POS20 != N AND POS22 = G AND POS18 != A|N (17.0)
POS32 != T AND POS29 = A AND POS25 = T AND POS13 != G AND POS16 != A|IE (32.0)
POS31 != G AND POS20 != N AND POS28 = A AND POS21 != T|N (20.0/1.0)
POS31 != G AND POS20 != N AND POS23 = G AND POS6 != T|N (14.0/1.0)
POS31 != G AND POS20 != N AND POS41 != T AND POS15 != A AND POS49 != T AND POS29 != T|IE (34.0)
POS32 = T AND POS30 != G AND POS33 = A AND POS35 != T|EI (25.0)
POS30 != G AND POS36 != T AND POS51 != G|N (27.0/1.0)
POS31 != G AND POS41 != A AND POS52 != T AND POS35 != C|N (13.0)
POS32 = T AND POS29 != A AND POS33 != C AND POS30 != T AND POS35 != A AND POS35 = G AND POS14 != T|EI (69.0)
POS32 = T AND POS29 != A AND POS9 != T AND POS10 != T AND POS50 != T AND POS1 != T AND POS11 != T|EI (21.0)
POS29 != A AND POS3 != A AND POS32 != G AND POS46 != T AND POS35 != G|N (17.0)
POS32 = T AND POS28 = T AND POS22 != A AND POS24 != G|IE (23.0)
POS32 = T AND POS28 != C AND POS33 != T AND POS28 != T AND POS29 = A AND POS43 != A|EI (96.0/1.0)
POS32 = T AND POS29 != C AND POS29 != A AND POS3 != C|EI (6.0/1.0)
POS32 = T AND POS29 = A AND POS33 = A AND POS34 != T AND POS51 != A|EI (47.0/1.0)
POS32 = T AND POS29 = A AND POS28 != A AND POS28 != G AND POS31 = G AND POS35 != G AND POS23 = A AND POS9 != T|EI (11.0)
POS35 = G AND POS29 != A AND POS21 = C|N (3.0)
POS35 = G AND POS32 != G AND POS36 = T|EI (32.0)
POS28 != A AND POS32 = T AND POS28 != G AND POS31 = G AND POS23 = T|IE (32.0/1.0)
POS28 = C AND POS32 = T AND POS25 != A AND POS26 != A AND POS14 != G AND POS23 != A AND POS13 = C|IE (22.0)
POS32 != T AND POS29 != G AND POS22 != G AND POS23 != A AND POS15 != G AND POS6 != A AND POS28 = C|IE (19.0)
POS32 != T AND POS25 != T AND POS26 != T AND POS9 != T|N (21.0/1.0)
POS32 = G AND POS16 != A|N (4.0)
POS28 != T AND POS19 = A|EI (10.0)
POS45 = A AND POS26 != A AND POS40 != A|IE (8.0)
POS45 != A AND POS35 = C AND POS22 != G|IE (11.0)
POS45 != A AND POS28 != A AND POS42 = A AND POS3 != C|IE (6.0)
POS45 != A AND POS35 != C AND POS29 = A AND POS59 != T AND POS48 != A|EI (19.0/1.0)
POS44 != G AND POS15 != T AND POS35 != C AND POS7 != G|IE (8.0)
POS44 != G AND POS9 != G|N (7.0)
|EI (6.0)


## J48 Decision Tree

* POS30 = G
	* POS29 = A
		* POS32 = T
			* POS31 = G
				* POS28 = C
					* POS35 = G: EI (130.0/16.0)
					* POS35 = C
						* POS33 = A: EI (16.0/2.0)
						* POS33 = G: IE (15.0/6.0)
						* POS33 = C: IE (8.0)
						* POS33 = T: IE (6.0)
						* POS33 = N: IE (0.0)
					* POS35 = T
						* POS36 = T: EI (3.0/1.0)
						* POS36 = C: IE (11.0)
						* POS36 = G: EI (14.0/4.0)
						* POS36 = A: EI (3.0/1.0)
						* POS36 = N: IE (0.0)
						* POS36 = S: IE (0.0)
					* POS35 = A
						* POS49 = G: IE (8.0/1.0)
						* POS49 = C: IE (8.0/1.0)
						* POS49 = A: IE (4.0)
						* POS49 = T: EI (6.0)
						* POS49 = N: IE (0.0)
					* POS35 = N: EI (0.0)
					* POS35 = R: EI (0.0)
				* POS28 = A: EI (126.0/7.0)
				* POS28 = T
					* POS24 = C: IE (14.0)
					* POS24 = T: IE (6.0)
					* POS24 = G: EI (12.0/1.0)
					* POS24 = A: IE (1.0)
					* POS24 = N: IE (0.0)
				* POS28 = G: EI (63.0/1.0)
				* POS28 = N: EI (0.0)
			* POS31 = A: IE (62.0/4.0)
			* POS31 = C: IE (52.0/4.0)
			* POS31 = T: IE (30.0/3.0)
			* POS31 = N: EI (0.0)
		* POS32 = A
			* POS28 = C: IE (122.0/10.0)
			* POS28 = A: N (16.0/3.0)
			* POS28 = T: IE (47.0/4.0)
			* POS28 = G: N (16.0/1.0)
			* POS28 = N: IE (0.0)
		* POS32 = C
			* POS28 = C: IE (119.0/11.0)
			* POS28 = A: IE (12.0/6.0)
			* POS28 = T: IE (24.0/2.0)
			* POS28 = G: N (9.0/2.0)
			* POS28 = N: IE (0.0)
		* POS32 = G
			* POS28 = C: IE (143.0/8.0)
			* POS28 = A: N (12.0/3.0)
			* POS28 = T: IE (23.0/4.0)
			* POS28 = G: N (5.0)
			* POS28 = N: IE (0.0)
		* POS32 = N: IE (0.0)
	* POS29 = C
		* POS32 = T
			* POS33 = A: EI (12.0/2.0)
			* POS33 = G: EI (40.0/1.0)
			* POS33 = C: N (3.0/1.0)
			* POS33 = T: N (2.0)
			* POS33 = N: EI (0.0)
		* POS32 = A: N (11.0)
		* POS32 = C: N (9.0)
		* POS32 = G: N (11.0)
		* POS32 = N: EI (0.0)
	* POS29 = G
		* POS32 = T
			* POS31 = G: EI (89.0/8.0)
			* POS31 = A: N (2.0)
			* POS31 = C: N (8.0)
			* POS31 = T: N (3.0)
			* POS31 = N: EI (0.0)
		* POS32 = A: N (31.0/1.0)
		* POS32 = C: N (33.0/1.0)
		* POS32 = G: N (35.0/1.0)
		* POS32 = N: N (0.0)
	* POS29 = T
		* POS32 = T
			* POS31 = G: EI (86.0/6.0)
			* POS31 = A: N (3.0)
			* POS31 = C: N (10.0)
			* POS31 = T: N (10.0)
			* POS31 = N: EI (0.0)
		* POS32 = A: N (32.0)
		* POS32 = C: N (27.0/1.0)
		* POS32 = G: N (32.0/1.0)
		* POS32 = N: N (0.0)
	* POS29 = N: IE (0.0)
* POS30 = A
	* POS35 = G
		* POS32 = T
			* POS34 = A
				* POS33 = A: EI (26.0)
				* POS33 = G: EI (26.0/4.0)
				* POS33 = C: N (2.0)
				* POS33 = T: N (1.0)
				* POS33 = N: EI (0.0)
			* POS34 = G: N (3.0)
			* POS34 = C: N (2.0)
			* POS34 = T: N (10.0/4.0)
			* POS34 = N: EI (0.0)
		* POS32 = A: N (26.0/1.0)
		* POS32 = C: N (21.0)
		* POS32 = G: N (23.0)
		* POS32 = N: N (0.0)
	* POS35 = C: N (106.0)
	* POS35 = T: N (79.0/1.0)
	* POS35 = A: N (99.0/1.0)
	* POS35 = N: N (0.0)
	* POS35 = R: N (0.0)
* POS30 = T
	* POS35 = G
		* POS31 = G
			* POS32 = T: EI (55.0/5.0)
			* POS32 = A: N (7.0)
			* POS32 = C: N (6.0)
			* POS32 = G: N (5.0)
			* POS32 = N: EI (0.0)
		* POS31 = A: N (10.0)
		* POS31 = C: N (22.0)
		* POS31 = T: N (16.0)
		* POS31 = N: N (0.0)
	* POS35 = C: N (86.0)
	* POS35 = T: N (106.0)
	* POS35 = A: N (99.0)
	* POS35 = N: N (0.0)
	* POS35 = R: N (0.0)
* POS30 = C
	* POS31 = G
		* POS32 = T
			* POS26 = T: N (8.0/1.0)
			* POS26 = C: EI (4.0/1.0)
			* POS26 = A: EI (11.0)
			* POS26 = G: EI (6.0/1.0)
			* POS26 = N: EI (0.0)
		* POS32 = A: N (6.0)
		* POS32 = C: N (12.0)
		* POS32 = G: N (12.0)
		* POS32 = N: N (0.0)
	* POS31 = A: N (112.0/1.0)
	* POS31 = C: N (109.0)
	* POS31 = T: N (117.0)
	* POS31 = N: N (0.0)
* POS30 = N: EI (1.0)


## SimpleCart Decision Tree

	* POS30=(N)|(G)
		* POS32=(N)|(T)
			* POS31=(N)|(G)
					* POS35=(N)|(G)|(R): EI(465.0/24.0)
					* POS35!=(N)|(G)|(R)
							* POS33=(T)|(C)|(G)|(N)
						* POS28=(G)|(A): N(12.0/10.0)
						* POS28!=(G)|(A): IE(68.0/19.0)
							* POS33!=(T)|(C)|(G)|(N): EI(72.0/12.0)
			* POS31!=(N)|(G)
					* POS29=(T)|(G)|(C): N(41.0/0.0)
					* POS29!=(T)|(G)|(C): IE(133.0/11.0)
		* POS32!=(N)|(T)
				* POS29=(T)|(G)|(C): N(216.0/5.0)
				* POS29!=(T)|(G)|(C)
				* POS28=(G)|(A): N(55.0/15.0)
				* POS28!=(G)|(A): IE(439.0/39.0)
	* POS30!=(N)|(G)
					* POS35=(A)|(T)|(C)|(N)|(R): N(859.0/3.0)
					* POS35!=(A)|(T)|(C)|(N)|(R)
				* POS32=(G)|(C)|(A): N(184.0/1.0)
				* POS32!=(G)|(C)|(A)
					* POS31=(T)|(C)|(A): N(51.0/0.0)
					* POS31!=(T)|(C)|(A): EI(122.0/13.0)


