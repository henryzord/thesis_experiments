# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | N | 0.519164 |
| POS30 = G and POS31 = G and POS32 = T | EI | 0.173440 |
| POS30 = G and POS32 != T and POS29 != C and POS28 != A and POS25 != G and POS26!=(A) and POS19!=(A) and POS23!=(G) and POS12!=(A) and POS24!=(G) | IE | 0.132078 |
| POS30 = G and POS32 = T and POS31 != G and POS29 != C and POS28 != A and POS25 != G and POS21!=(G) | IE | 0.041941 |
| POS30 != G and POS35 != R and POS32 != A and POS31 != A and POS34 != G | EI | 0.014923 |
| POS30 = G and POS32 != T and POS29 != C and POS28 != A and POS25 = G and POS18 != A | IE | 0.003081 |
| POS30 = G and POS29 = A and POS32 = T and POS31 = G and POS35 = C and POS33 = C | IE | 0.005474 |
| POS30 = G and POS29 = A and POS32 = T and POS31 = G and POS35 = T and POS21 = C | IE | 0.004153 |
| POS30 = G and POS32 = T and POS31 != G and POS29 != C and POS28 != A and POS25 = G | IE | 0.001692 |
| POS30 = G and POS32 != T and POS29 != C and POS28 = A and POS22 != N and POS59 != N | IE | 0.000500 |
| POS30 = G and POS29 = A and POS32 = T and POS31 = G and POS35 = C and POS33 = T | IE | 0.002928 |
| POS30 = G and POS29 = A and POS32 = T and POS31 = G and POS35 = T and POS21 = T | IE | 0.001956 |
| POS30 = G and POS29 = A and POS32 = T and POS31 = G and POS35 = C and POS33 = G and POS50 = T | IE | 0.003201 |
| POS30 = G and POS29 = A and POS32 = T and POS31 = G and POS35 = G and POS28 = T and POS24 = C | IE | 0.002745 |
| POS30 = G and POS29 = A and POS32 = T and POS31 = G and POS35 = G and POS28 = C and POS6 = A and POS45 = G | IE | 0.001832 |
| POS30 = G and POS29 = A and POS32 = T and POS31 = G and POS35 = C and POS33 = G and POS50 = C | IE | 0.000825 |
| POS30 = G and POS32 = T and POS31 != G and POS29 != C and POS28 = A and POS26 != A | IE | 0.000296 |
| POS30 = G and POS29 = A and POS32 = T and POS31 = G and POS35 = C and POS33 = G and POS50 = A | IE | 0.000459 |
| POS30 = G and POS29 = A and POS32 = G and POS28 = C | IE | 0.051664 |
| POS30 != G and POS35 != R and POS32 != A and POS31 != A and POS34 = G and POS33 != G | EI | 0.000004 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| POS30 != G and POS35 != G and POS13 != C and POS51 != A | N | 0.275591 |
| POS32 != T and POS29 != A and POS41 != G and POS6 != A | N | 0.181009 |
| POS32 != T and POS29 != A and POS59 = G and POS50 != C | N | 0.039666 |
| POS31 != G and POS30 != G and POS32 != G and POS2 != A | N | 0.106218 |
| POS32 != T and POS29 != A and POS59 != G and POS56 != G and POS9 != G | N | 0.056088 |
| POS32 != T and POS30 != G and POS59 != G and POS12 != C | N | 0.037657 |
| POS32 != T and POS28 = G and POS4 != T and POS8 != T | N | 0.028169 |
| POS32 != T and POS29 = A and POS30 != G and POS1 != A | N | 0.010043 |
| POS32 != T and POS29 = A and POS28 != A and POS28 != G and POS25 != G and POS25 != A and POS26 != A and POS19 != A and POS24 != G and POS20 != A and POS13 != A and POS16 != A | IE | 0.222682 |
| POS31 != G and POS29 != A and POS32 != G and POS32 = T | N | 0.056075 |
| POS31 != G and POS29 != A and POS24 != A and POS3 != C | N | 0.014197 |
| POS31 != G and POS30 = G and POS28 != A and POS29 = A and POS28 != G and POS23 != G and POS21 != G and POS41 != T and POS27 != T | IE | 0.124617 |
| POS32 = T and POS31 != G and POS30 = G and POS25 != G and POS25 != A and POS12 != G | IE | 0.038159 |
| POS32 = T and POS31 = G and POS35 = G and POS33 != C and POS34 != T and POS33 != T and POS34 = A and POS6 != A | EI | 0.446154 |
| POS32 != T and POS29 != G and POS29 = A and POS28 = A and POS59 != C and POS15 != T | N | 0.038035 |
| POS32 != T and POS29 = A and POS28 != G and POS21 != A and POS22 != G and POS31 != C and POS17 != A and POS8 != G and POS15 != G and POS56 != T and POS55 != T | IE | 0.111722 |
| POS32 != T and POS29 = G | N | 0.006505 |
| POS32 != T and POS30 != G and POS31 = G | N | 0.010870 |
| POS32 != T and POS30 = G and POS23 = A and POS21 != C | N | 0.019749 |
| POS32 != T and POS29 = A and POS23 != G and POS18 != G and POS25 != G and POS10 != T and POS7 != G and POS11 != T | IE | 0.057026 |
| POS31 != G and POS30 = G and POS10 = T and POS60 != T and POS34 != G | IE | 0.035417 |
| POS31 != G and POS29 = A and POS28 != A and POS30 = G and POS6 != T and POS27 != C and POS51 != G and POS26 != T | N | 0.030948 |
| POS31 != G and POS30 = G and POS28 = A | N | 0.015717 |
| POS32 = T and POS31 != G and POS2 = A | N | 0.013780 |
| POS32 = T and POS31 != G and POS6 = G | IE | 0.007356 |
| POS32 = T and POS30 = T and POS24 != A and POS33 != A and POS37 != C | N | 0.021654 |
| POS32 = T and POS29 != A and POS33 != C and POS30 != C and POS54 != A and POS35 = G and POS21 != C | EI | 0.204082 |
| POS32 = T and POS29 != A and POS33 = A and POS44 != G and POS6 != C | EI | 0.082353 |
| POS29 = G and POS13 != G | N | 0.019104 |
| POS32 = T and POS29 != A and POS21 != A and POS30 != C and POS3 = A | EI | 0.046610 |
| POS29 != A and POS39 != G and POS36 != T and POS2 != A | N | 0.040409 |
| POS32 = T and POS29 != A and POS40 != T and POS6 != C | N | 0.016990 |
| POS32 = T and POS28 = A and POS33 != T and POS19 != C and POS30 != A | EI | 0.256506 |
| POS32 = T and POS28 = G and POS4 != T | EI | 0.159769 |
| POS32 = T and POS28 = A and POS34 = A and POS1 = T | EI | 0.024390 |
| POS32 = T and POS28 != A and POS28 != G and POS29 != T and POS30 != A and POS33 = A and POS34 != T and POS51 != A and POS8 != T | EI | 0.148936 |
| POS31 = C and POS40 != G | N | 0.022814 |
| POS32 != T and POS29 = A and POS28 != G and POS25 != A and POS48 = G | IE | 0.113208 |
| POS32 = T and POS28 != A and POS28 != G and POS29 = A and POS30 != A and POS35 != G and POS23 != A and POS21 != G and POS24 != G and POS25 != A and POS17 != A | IE | 0.273196 |
| POS32 = T and POS28 != A and POS28 != G and POS29 = A and POS30 != A and POS28 != C and POS4 != A | IE | 0.066225 |
| POS32 = T and POS28 != A and POS28 != G and POS39 = A and POS57 != C and POS13 != A | IE | 0.060000 |
| POS32 = T and POS28 = C and POS55 = T and POS11 != T | EI | 0.103448 |
| POS32 = T and POS55 = T and POS4 = C | EI | 0.033378 |
| POS32 = T and POS55 != T and POS28 = C and POS19 = A | EI | 0.126050 |
| POS32 = T and POS55 != T and POS25 = T and POS24 != A and POS6 != G | IE | 0.106557 |
| POS32 = T and POS55 != T and POS28 = C and POS26 = A | EI | 0.133333 |
| POS32 = T and POS55 != T and POS28 = C and POS18 = A | EI | 0.116505 |
| POS32 != T and POS29 = A and POS20 != A and POS22 != A and POS4 != C and POS59 != A and POS3 = T | IE | 0.097826 |
| POS32 = G and POS52 != G and POS56 != G | IE | 0.097826 |
| POS29 = A and POS32 != T and POS38 = T | N | 0.103448 |
| POS29 = A and POS32 = A and POS53 = T | IE | 0.035088 |
| POS32 != A and POS32 = G | N | 0.047368 |
| POS32 != A and POS33 = C | IE | 0.068056 |
| POS32 = A | N | 0.075617 |
| POS16 = A and POS39 != T | EI | 0.133152 |
| POS16 != A and POS22 != A and POS26 != A and POS50 != T and POS43 != T and POS25 != T and POS24 != T and POS50 != A | EI | 0.205714 |
| POS16 != A and POS26 = A and POS22 != A | EI | 0.139130 |
| POS26 != A and POS20 != A and POS30 = G and POS22 != A and POS50 != T and POS27 = C | IE | 0.192857 |
| POS37 != A and POS3 != A and POS22 != T and POS28 = C | EI | 0.152381 |
| POS28 = A and POS17 != T | EI | 0.117647 |
| POS34 != A and POS5 != T and POS40 != G | IE | 0.179487 |
| POS34 = A | IE | 0.205714 |
| POS5 = T | N | 0.520833 |
|  | N | 0.750000 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| POS32 = T and POS31 = G and POS35 = G and POS34 = A | EI | 0.165752 |
| POS32 = T and POS31 = G and POS33 = A | EI | 0.054511 |
| POS32 = T and POS31 = G and POS35 = G and POS30 = G | EI | 0.021198 |
| POS31 = G and POS32 = T and POS50 = G and POS8 = T | EI | 0.003517 |
| POS29 = A and POS30 = G and POS28 = C | IE | 0.247741 |
| POS29 = A and POS30 = G and POS28 = T and POS21 = T | IE | 0.046608 |
| POS29 = A and POS30 = G and POS28 = T | IE | 0.028926 |
|  | N | 0.971317 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

pos30|pos31|pos32|class
---|---|---|---
n|n|n|ei
a|t|g|n
g|t|g|n
c|t|g|n
t|t|g|n
t|c|g|n
a|c|g|n
c|c|g|n
g|c|g|n
g|t|c|ie
t|t|c|n
c|t|c|n
a|t|c|n
t|a|g|n
a|a|g|n
c|a|g|n
g|a|g|ie
t|c|c|n
t|g|g|n
g|c|c|n
g|g|g|ie
c|g|g|n
a|c|c|n
c|c|c|n
a|g|g|n
a|a|c|n
a|t|a|n
g|t|a|n
t|a|c|n
c|a|c|n
t|t|a|n
c|t|a|n
g|a|c|ie
c|g|c|n
t|c|a|n
a|g|c|n
a|c|a|n
g|g|c|ie
g|c|a|n
c|c|a|n
t|g|c|n
g|a|a|ie
a|t|t|n
a|a|a|n
g|t|t|ie
c|t|t|n
t|a|a|n
c|a|a|n
t|t|t|n
c|g|a|n
t|c|t|n
a|g|a|n
g|c|t|ie
a|c|t|n
c|c|t|n
t|g|a|n
g|g|a|ie
t|a|t|n
g|a|t|ie
a|a|t|n
c|a|t|n
c|g|t|ei
t|g|t|ei
a|g|t|ei
g|g|t|ei

## JRip

Decision list:

rules | predicted class
---|---
(POS32 = T) and (POS31 = G) and (POS35 = G) and (POS34 = A)|EI (447.0/7.0)
(POS32 = T) and (POS31 = G) and (POS33 = A)|EI (177.0/28.0)
(POS32 = T) and (POS31 = G) and (POS35 = G) and (POS30 = G)|EI (74.0/10.0)
(POS31 = G) and (POS32 = T) and (POS50 = G) and (POS8 = T)|EI (18.0/5.0)
(POS29 = A) and (POS30 = G) and (POS28 = C)|IE (570.0/49.0)
(POS29 = A) and (POS30 = G) and (POS28 = T) and (POS21 = T)|IE (74.0/1.0)
(POS29 = A) and (POS30 = G) and (POS28 = T)|IE (53.0/7.0)
|N (1457.0/30.0)


## PART

Decision list:

rules | predicted class
---|---
POS30 != G AND POS35 != G AND POS13 != C AND POS51 != A|N (525.0)
POS32 != T AND POS29 != A AND POS41 != G AND POS6 != A|N (305.0)
POS32 != T AND POS29 != A AND POS59 = G AND POS50 != C|N (57.0)
POS31 != G AND POS30 != G AND POS32 != G AND POS2 != A|N (164.0)
POS32 != T AND POS29 != A AND POS59 != G AND POS56 != G AND POS9 != G|N (82.0)
POS32 != T AND POS30 != G AND POS59 != G AND POS12 != C|N (54.0)
POS32 != T AND POS28 = G AND POS4 != T AND POS8 != T|N (40.0)
POS32 != T AND POS29 = A AND POS30 != G AND POS1 != A|N (14.0)
POS32 != T AND POS29 = A AND POS28 != A AND POS28 != G AND POS25 != G AND POS25 != A AND POS26 != A AND POS19 != A AND POS24 != G AND POS20 != A AND POS13 != A AND POS16 != A|IE (269.0)
POS31 != G AND POS29 != A AND POS32 != G AND POS32 = T|N (66.0)
POS31 != G AND POS29 != A AND POS24 != A AND POS3 != C|N (16.0)
POS31 != G AND POS30 = G AND POS28 != A AND POS29 = A AND POS28 != G AND POS23 != G AND POS21 != G AND POS41 != T AND POS27 != T|IE (122.0)
POS32 = T AND POS31 != G AND POS30 = G AND POS25 != G AND POS25 != A AND POS12 != G|IE (34.0)
POS32 = T AND POS31 = G AND POS35 = G AND POS33 != C AND POS34 != T AND POS33 != T AND POS34 = A AND POS6 != A|EI (348.0)
POS32 != T AND POS29 != G AND POS29 = A AND POS28 = A AND POS59 != C AND POS15 != T|N (24.0)
POS32 != T AND POS29 = A AND POS28 != G AND POS21 != A AND POS22 != G AND POS31 != C AND POS17 != A AND POS8 != G AND POS15 != G AND POS56 != T AND POS55 != T|IE (61.0)
POS32 != T AND POS29 = G|N (7.0/2.0)
POS32 != T AND POS30 != G AND POS31 = G|N (6.0)
POS32 != T AND POS30 = G AND POS23 = A AND POS21 != C|N (11.0)
POS32 != T AND POS29 = A AND POS23 != G AND POS18 != G AND POS25 != G AND POS10 != T AND POS7 != G AND POS11 != T|IE (28.0)
POS31 != G AND POS30 = G AND POS10 = T AND POS60 != T AND POS34 != G|IE (17.0)
POS31 != G AND POS29 = A AND POS28 != A AND POS30 = G AND POS6 != T AND POS27 != C AND POS51 != G AND POS26 != T|N (16.0)
POS31 != G AND POS30 = G AND POS28 = A|N (8.0)
POS32 = T AND POS31 != G AND POS2 = A|N (7.0)
POS32 = T AND POS31 != G AND POS6 = G|IE (5.0/1.0)
POS32 = T AND POS30 = T AND POS24 != A AND POS33 != A AND POS37 != C|N (11.0)
POS32 = T AND POS29 != A AND POS33 != C AND POS30 != C AND POS54 != A AND POS35 = G AND POS21 != C|EI (60.0)
POS32 = T AND POS29 != A AND POS33 = A AND POS44 != G AND POS6 != C|EI (21.0)
POS29 = G AND POS13 != G|N (9.0)
POS32 = T AND POS29 != A AND POS21 != A AND POS30 != C AND POS3 = A|EI (11.0)
POS29 != A AND POS39 != G AND POS36 != T AND POS2 != A|N (18.0)
POS32 = T AND POS29 != A AND POS40 != T AND POS6 != C|N (7.0)
POS32 = T AND POS28 = A AND POS33 != T AND POS19 != C AND POS30 != A|EI (69.0)
POS32 = T AND POS28 = G AND POS4 != T|EI (39.0)
POS32 = T AND POS28 = A AND POS34 = A AND POS1 = T|EI (5.0)
POS32 = T AND POS28 != A AND POS28 != G AND POS29 != T AND POS30 != A AND POS33 = A AND POS34 != T AND POS51 != A AND POS8 != T|EI (35.0)
POS31 = C AND POS40 != G|N (6.0)
POS32 != T AND POS29 = A AND POS28 != G AND POS25 != A AND POS48 = G|IE (18.0)
POS32 = T AND POS28 != A AND POS28 != G AND POS29 = A AND POS30 != A AND POS35 != G AND POS23 != A AND POS21 != G AND POS24 != G AND POS25 != A AND POS17 != A|IE (53.0)
POS32 = T AND POS28 != A AND POS28 != G AND POS29 = A AND POS30 != A AND POS28 != C AND POS4 != A|IE (10.0)
POS32 = T AND POS28 != A AND POS28 != G AND POS39 = A AND POS57 != C AND POS13 != A|IE (9.0)
POS32 = T AND POS28 = C AND POS55 = T AND POS11 != T|EI (12.0)
POS32 = T AND POS55 = T AND POS4 = C|EI (6.0/1.0)
POS32 = T AND POS55 != T AND POS28 = C AND POS19 = A|EI (15.0)
POS32 = T AND POS55 != T AND POS25 = T AND POS24 != A AND POS6 != G|IE (13.0)
POS32 = T AND POS55 != T AND POS28 = C AND POS26 = A|EI (14.0)
POS32 = T AND POS55 != T AND POS28 = C AND POS18 = A|EI (12.0)
POS32 != T AND POS29 = A AND POS20 != A AND POS22 != A AND POS4 != C AND POS59 != A AND POS3 = T|IE (9.0)
POS32 = G AND POS52 != G AND POS56 != G|IE (9.0)
POS29 = A AND POS32 != T AND POS38 = T|N (9.0)
POS29 = A AND POS32 = A AND POS53 = T|IE (6.0/2.0)
POS32 != A AND POS32 = G|N (9.0/3.0)
POS32 != A AND POS33 = C|IE (8.0/1.0)
POS32 = A|N (6.0/1.0)
POS16 = A AND POS39 != T|EI (6.0/1.0)
POS16 != A AND POS22 != A AND POS26 != A AND POS50 != T AND POS43 != T AND POS25 != T AND POS24 != T AND POS50 != A|EI (12.0)
POS16 != A AND POS26 = A AND POS22 != A|EI (8.0)
POS26 != A AND POS20 != A AND POS30 = G AND POS22 != A AND POS50 != T AND POS27 = C|IE (9.0)
POS37 != A AND POS3 != A AND POS22 != T AND POS28 = C|EI (9.0/1.0)
POS28 = A AND POS17 != T|EI (8.0/3.0)
POS34 != A AND POS5 != T AND POS40 != G|IE (8.0/3.0)
POS34 = A|IE (5.0)
POS5 = T|N (5.0/2.0)
|N (5.0)


## J48 Decision Tree

* POS30 = G
	* POS29 = A
		* POS32 = T
			* POS31 = G
				* POS35 = G
					* POS28 = C
						* POS6 = C: EI (21.0/1.0)
						* POS6 = G: EI (22.0)
						* POS6 = T: EI (8.0)
						* POS6 = A
							* POS45 = C: EI (2.0)
							* POS45 = G: IE (3.0)
							* POS45 = A: EI (2.0/1.0)
							* POS45 = T: EI (3.0)
							* POS45 = N: EI (0.0)
					* POS28 = A: EI (46.0)
					* POS28 = T
						* POS24 = C: IE (4.0)
						* POS24 = T: IE (0.0)
						* POS24 = G: EI (3.0)
						* POS24 = A: IE (0.0)
						* POS24 = N: IE (0.0)
					* POS28 = G: EI (27.0)
					* POS28 = N: EI (0.0)
				* POS35 = C
					* POS33 = A: EI (11.0/1.0)
					* POS33 = G
						* POS50 = G: EI (4.0/1.0)
						* POS50 = C: IE (0.0)
						* POS50 = A: IE (1.0)
						* POS50 = T: IE (5.0)
						* POS50 = N: IE (0.0)
					* POS33 = C: IE (4.0)
					* POS33 = T: IE (9.0/2.0)
					* POS33 = N: IE (0.0)
				* POS35 = T
					* POS21 = C: IE (6.0)
					* POS21 = T: IE (3.0)
					* POS21 = G: EI (7.0/1.0)
					* POS21 = A: EI (8.0/1.0)
					* POS21 = N: EI (0.0)
				* POS35 = A: EI (22.0/11.0)
				* POS35 = N: EI (0.0)
				* POS35 = R: EI (0.0)
			* POS31 = A: IE (25.0/1.0)
			* POS31 = C: IE (21.0/3.0)
			* POS31 = T
				* POS28 = C: IE (12.0)
				* POS28 = A: IE (0.0)
				* POS28 = T: IE (3.0)
				* POS28 = G: N (1.0)
				* POS28 = N: IE (0.0)
			* POS31 = N: EI (0.0)
		* POS32 = A
			* POS28 = C: IE (72.0/7.0)
			* POS28 = A: N (7.0/1.0)
			* POS28 = T: IE (22.0/1.0)
			* POS28 = G: N (7.0)
			* POS28 = N: IE (0.0)
		* POS32 = C
			* POS28 = C: IE (74.0/8.0)
			* POS28 = A
				* POS21 = C: N (3.0/1.0)
				* POS21 = T: IE (1.0)
				* POS21 = G: N (0.0)
				* POS21 = A: N (4.0)
				* POS21 = N: N (0.0)
			* POS28 = T: IE (9.0/1.0)
			* POS28 = G: N (5.0/1.0)
			* POS28 = N: IE (0.0)
		* POS32 = G
			* POS28 = C: IE (67.0/5.0)
			* POS28 = A: N (5.0/1.0)
			* POS28 = T: IE (11.0)
			* POS28 = G: IE (0.0)
			* POS28 = N: IE (0.0)
		* POS32 = N: IE (0.0)
	* POS29 = C
		* POS32 = T
			* POS31 = G: EI (31.0/2.0)
			* POS31 = A: EI (0.0)
			* POS31 = C: N (4.0)
			* POS31 = T: N (2.0)
			* POS31 = N: EI (0.0)
		* POS32 = A: N (4.0)
		* POS32 = C: N (6.0)
		* POS32 = G: N (7.0)
		* POS32 = N: EI (0.0)
	* POS29 = G
		* POS32 = T
			* POS31 = G: EI (42.0/6.0)
			* POS31 = A: EI (0.0)
			* POS31 = C: N (3.0)
			* POS31 = T: EI (0.0)
			* POS31 = N: EI (0.0)
		* POS32 = A: N (18.0)
		* POS32 = C: N (14.0)
		* POS32 = G: N (18.0/1.0)
		* POS32 = N: N (0.0)
	* POS29 = T
		* POS32 = T
			* POS31 = G: EI (38.0/3.0)
			* POS31 = A: EI (0.0)
			* POS31 = C: N (3.0)
			* POS31 = T: N (5.0)
			* POS31 = N: EI (0.0)
		* POS32 = A: N (20.0)
		* POS32 = C: N (12.0/1.0)
		* POS32 = G: N (19.0)
		* POS32 = N: N (0.0)
	* POS29 = N: IE (0.0)
* POS30 = A
	* POS32 = T
		* POS31 = G
			* POS35 = G: EI (34.0/3.0)
			* POS35 = C: N (4.0)
			* POS35 = T: N (2.0)
			* POS35 = A: N (4.0/1.0)
			* POS35 = N: EI (0.0)
			* POS35 = R: EI (0.0)
		* POS31 = A: N (10.0)
		* POS31 = C: N (13.0)
		* POS31 = T: N (13.0)
		* POS31 = N: N (0.0)
	* POS32 = A: N (55.0)
	* POS32 = C: N (46.0)
	* POS32 = G: N (45.0/1.0)
	* POS32 = N: N (0.0)
* POS30 = T
	* POS35 = G
		* POS32 = T
			* POS31 = G: EI (30.0/2.0)
			* POS31 = A: N (3.0)
			* POS31 = C: N (2.0)
			* POS31 = T: N (3.0)
			* POS31 = N: EI (0.0)
		* POS32 = A: N (13.0)
		* POS32 = C: N (7.0)
		* POS32 = G: N (4.0)
		* POS32 = N: N (0.0)
	* POS35 = C: N (33.0)
	* POS35 = T: N (50.0)
	* POS35 = A: N (43.0)
	* POS35 = N: N (0.0)
	* POS35 = R: N (0.0)
* POS30 = C
	* POS31 = G
		* POS35 = G: EI (19.0/7.0)
		* POS35 = C: N (11.0)
		* POS35 = T: N (5.0)
		* POS35 = A: N (4.0)
		* POS35 = N: N (0.0)
		* POS35 = R: N (0.0)
	* POS31 = A: N (60.0)
	* POS31 = C: N (55.0)
	* POS31 = T: N (51.0)
	* POS31 = N: N (0.0)
* POS30 = N: N (0.0)


## SimpleCart Decision Tree

	* POS30=(N)|(G)
		* POS32=(N)|(T)
			* POS31=(N)|(G)
					* POS35=(N)|(G)|(R)
						* POS33=(N)|(A)|(G)
								* POS34=(N)|(A)|(G)|(C)
									* POS39=(N)|(C)|(G)|(T)
										* POS49=(N)|(G)|(C)|(T): EI(303.0/0.0)
										* POS49!=(N)|(G)|(C)|(T)
								* POS57=(C): EI(5.0/2.0)
								* POS57!=(C): EI(39.0/0.0)
									* POS39!=(N)|(C)|(G)|(T)
							* POS19=(T)
									* POS58=(A)|(T): IE(5.0/0.0)
									* POS58!=(A)|(T): EI(7.0/0.0)
							* POS19!=(T)
								* POS16=(G): EI(4.0/1.0)
								* POS16!=(G): EI(50.0/0.0)
								* POS34!=(N)|(A)|(G)|(C)
						* POS38=(A): IE(4.0/2.0)
						* POS38!=(A): EI(27.0/3.0)
						* POS33!=(N)|(A)|(G)
						* POS36=(G)|(C): IE(6.0/3.0)
						* POS36!=(G)|(C): EI(21.0/2.0)
					* POS35!=(N)|(G)|(R)
							* POS33=(T)|(C)|(G)|(N)
						* POS28=(G)|(A)
						* POS18=(A): EI(6.0/1.0)
						* POS18!=(A): N(13.0/3.0)
						* POS28!=(G)|(A)
							* POS19=(A)|(G)
							* POS26=(A): EI(9.0/1.0)
							* POS26!=(A): IE(11.0/5.0)
							* POS19!=(A)|(G): IE(59.0/5.0)
							* POS33!=(T)|(C)|(G)|(N)
								* POS52=(T)|(C)|(A)|(N)
									* POS25=(A)|(G)|(T)|(N): EI(50.0/1.0)
									* POS25!=(A)|(G)|(T)|(N): EI(7.0/3.0)
								* POS52!=(T)|(C)|(A)|(N): EI(13.0/8.0)
			* POS31!=(N)|(G)
					* POS29=(T)|(G)|(C): N(43.0/0.0)
					* POS29!=(T)|(G)|(C)
					* POS28=(G)|(A)
							* POS26=(G)|(A)|(N): N(7.0/0.0)
							* POS26!=(G)|(A)|(N): IE(4.0/1.0)
					* POS28!=(G)|(A)
						* POS25=(A)|(G): IE(14.0/3.0)
						* POS25!=(A)|(G)
						* POS21=(G): IE(4.0/1.0)
						* POS21!=(G): IE(103.0/0.0)
		* POS32!=(N)|(T)
				* POS29=(T)|(G)|(C)
						* POS41=(A)|(T)|(C)|(N): N(158.0/0.0)
						* POS41!=(A)|(T)|(C)|(N)
				* POS54=(T): N(10.0/3.0)
				* POS54!=(T)
					* POS1=(T): N(8.0/1.0)
					* POS1!=(T): N(40.0/0.0)
				* POS29!=(T)|(G)|(C)
				* POS28=(G)|(A)
						* POS22=(A)|(G)|(N): N(42.0/0.0)
						* POS22!=(A)|(G)|(N)
								* POS59=(T)|(A)|(G)|(N)
								* POS16=(G)|(A)|(T): N(17.0/3.0)
								* POS16!=(G)|(A)|(T): IE(4.0/1.0)
								* POS59!=(T)|(A)|(G)|(N): IE(6.0/0.0)
				* POS28!=(G)|(A)
					* POS25=(A)|(G)
						* POS18=(A)|(G)
									* POS38=(T)|(A)|(G)|(N): N(12.0/1.0)
									* POS38!=(T)|(A)|(G)|(N): IE(7.0/3.0)
						* POS18!=(A)|(G): IE(38.0/6.0)
					* POS25!=(A)|(G)
					* POS26=(A)
							* POS18=(A)|(G): N(7.0/3.0)
							* POS18!=(A)|(G): IE(11.0/0.0)
					* POS26!=(A)
						* POS19=(A)
								* POS58=(T)|(G): IE(6.0/5.0)
								* POS58!=(T)|(G): IE(20.0/0.0)
						* POS19!=(A)
							* POS23=(G)
								* POS19=(G): IE(3.0/3.0)
								* POS19!=(G): IE(30.0/1.0)
							* POS23!=(G)
								* POS12=(A): IE(48.0/3.0)
								* POS12!=(A)
									* POS24=(G): IE(15.0/1.0)
									* POS24!=(G): IE(268.0/0.0)
	* POS30!=(N)|(G)
					* POS35=(A)|(T)|(C)|(N)|(R)
		* POS45=(G)
			* POS28=(A)
				* POS36=(G): N(7.0/3.0)
				* POS36!=(G)
					* POS12=(T): N(6.0/1.0)
					* POS12!=(T): N(36.0/0.0)
			* POS28!=(A)
				* POS22=(T): N(29.0/1.0)
				* POS22!=(T): N(136.0/0.0)
		* POS45!=(G): N(631.0/0.0)
					* POS35!=(A)|(T)|(C)|(N)|(R)
				* POS32=(G)|(C)|(A)
			* POS34=(C): N(22.0/1.0)
			* POS34!=(C): N(160.0/0.0)
				* POS32!=(G)|(C)|(A)
					* POS31=(T)|(C)|(A): N(56.0/0.0)
					* POS31!=(T)|(C)|(A)
						* POS34=(T)|(C)|(G)
								* POS33=(T)|(C)|(G)|(N): N(12.0/3.0)
								* POS33!=(T)|(C)|(G)|(N): EI(8.0/0.0)
						* POS34!=(T)|(C)|(G): EI(114.0/1.0)


