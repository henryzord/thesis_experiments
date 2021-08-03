# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | N | 0.518996 |
| POS30 != A and POS32 != A and POS31 != A and POS35 != C | EI | 0.134036 |
| POS30 = G and POS32 != T and POS29 = A and POS28 != G and POS28 != A and POS25 != G | IE | 0.154460 |
| POS30 = G and POS32 = T and POS31 != G and POS29 = A | IE | 0.053736 |
| POS30 = G and POS32 = T and POS31 = G and POS35 != G and POS33 != A and POS29 = A and POS28 != A and POS23 != A | IE | 0.023930 |
| POS30 = A and POS35 != R and POS32 != A and POS31 != C | EI | 0.004894 |
| POS30 = G and POS32 != T and POS29 = A and POS28 != G and POS28 != A and POS25 = G and POS21 != A and POS57 != T | IE | 0.008808 |
| POS30 != A and POS32 != A and POS31 != A and POS35 = C and POS33 != T | EI | 0.001918 |
| POS30 = G and POS32 != T and POS29 = A and POS28 != G and POS28 = A and POS59 = C | IE | 0.002061 |
| POS30 != A and POS32 != A and POS31 != A and POS35 = C and POS33 = T | IE | 0.011244 |
| POS30 != A and POS32 != A and POS31 = A and POS29 != G | IE | 0.035233 |
| POS30 != A and POS32 = A and POS29 != C and POS28 != A | IE | 0.036627 |
| POS29 = A and POS30 = G and POS31 = G and POS32 = G | IE | 0.028309 |
| POS29 = A and POS30 = G and POS31 = A and POS32 = A | IE | 0.018655 |
| POS29 = A and POS30 = G and POS31 = T and POS32 = G | IE | 0.010332 |
| POS29 = A and POS30 = G and POS31 = G and POS32 = C | IE | 0.027988 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| POS30 != G and POS35 != G | N | 0.380623 |
| POS32 != T and POS29 = A and POS30 = G and POS28 != G and POS28 != A and POS25 != G and POS25 != A | IE | 0.224609 |
| POS32 != T and POS29 != A | N | 0.263074 |
| POS31 = G and POS32 = T and POS35 = G and POS34 != T and POS33 != C and POS33 != T and POS34 = A and POS39 != A | EI | 0.376780 |
| POS31 != G and POS30 = G and POS29 = A and POS32 = T | IE | 0.164932 |
| POS31 != G and POS32 = T | N | 0.180033 |
| POS32 != T and POS30 = G and POS21 != A and POS20 != A and POS22 != G and POS22 != A and POS24 != A and POS24 != G | IE | 0.064793 |
| POS32 != T and POS28 != C | N | 0.161978 |
| POS32 != T and POS30 = G and POS17 != A and POS19 != C | IE | 0.014286 |
| POS31 = G and POS32 = T and POS29 != A and POS33 != C and POS36 = T | EI | 0.260570 |
| POS31 = G and POS32 = T and POS29 != A and POS33 = A | EI | 0.134348 |
| POS31 != G | N | 0.055556 |
| POS29 != G and POS32 != T | N | 0.022509 |
| POS29 != G and POS29 != A and POS39 != A and POS44 != C | N | 0.023399 |
| POS29 != G and POS28 = T and POS25 != A | IE | 0.074214 |
| POS29 != G and POS28 != C and POS43 != A and POS17 != T | EI | 0.490340 |
| POS29 != G and POS30 = G and POS35 = G and POS36 = T | EI | 0.278571 |
| POS29 != G and POS33 = A and POS47 != A | EI | 0.341811 |
| POS29 != G and POS28 = C and POS26 != A and POS35 != G and POS33 != A and POS14 != G | IE | 0.348211 |
| POS29 != G and POS21 != T and POS23 != T | EI | 0.352734 |
| POS29 != G and POS25 != G and POS4 != A and POS43 != T and POS10 != T | IE | 0.328182 |
| POS28 != C | N | 0.296703 |
| POS44 != T and POS22 != T | IE | 0.241071 |
| POS44 = T | N | 0.086957 |
|  | EI | 0.652174 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| POS32 = T and POS31 = G and POS35 = G and POS34 = A | EI | 0.165804 |
| POS32 = T and POS31 = G and POS33 = A | EI | 0.057111 |
| POS32 = T and POS31 = G and POS35 = G and POS36 = T | EI | 0.014523 |
| POS32 = T and POS31 = G and POS53 = G and POS40 = G | EI | 0.005738 |
| POS32 = T and POS31 = G and POS35 = G and POS39 = C | EI | 0.003079 |
| POS32 = T and POS31 = G and POS50 = G and POS28 = A and POS33 = G | EI | 0.004155 |
| POS29 = A and POS30 = G and POS28 = C | IE | 0.248485 |
| POS30 = G and POS28 = T and POS29 = A | IE | 0.071704 |
| POS29 = A and POS30 = G and POS22 = T | IE | 0.002526 |
|  | N | 0.977034 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

pos29|pos30|pos31|pos32|class
---|---|---|---|---
n|n|n|n|ei
c|c|t|g|n
a|c|t|g|n
t|c|t|g|n
g|c|t|g|n
c|t|t|g|n
a|t|t|g|n
t|t|t|g|n
g|t|t|g|n
a|c|c|g|n
g|a|t|g|n
t|a|t|g|n
g|c|c|g|n
c|c|c|g|n
a|a|t|g|n
c|a|t|g|n
t|c|c|g|n
t|t|c|g|ei
g|g|t|g|n
a|t|c|g|ei
c|t|c|g|n
t|c|t|c|n
a|c|t|c|n
a|g|t|g|ie
c|g|t|g|n
c|c|t|c|n
g|c|t|c|n
t|g|t|g|n
a|a|c|g|n
g|t|t|c|n
g|a|c|g|ei
a|t|t|c|n
c|t|t|c|n
c|c|a|g|n
c|a|c|g|n
g|c|a|g|n
a|c|a|g|n
t|c|a|g|n
t|t|t|c|n
t|a|c|g|n
t|t|a|g|n
a|c|c|c|n
a|t|a|g|n
t|g|c|g|n
a|g|c|g|ie
c|c|c|c|n
c|g|c|g|ei
t|c|c|c|n
g|c|c|c|n
a|a|t|c|n
g|g|c|g|n
c|a|t|c|n
g|a|t|c|n
t|a|t|c|n
c|g|t|c|ei
g|c|g|g|n
a|c|t|a|ei
a|c|g|g|n
t|t|c|c|n
a|g|t|c|ie
g|g|t|c|n
t|c|t|a|n
c|a|a|g|n
t|g|t|c|n
a|t|c|c|n
t|c|g|g|ei
t|a|a|g|n
c|t|c|c|n
g|c|t|a|n
g|t|c|c|n
c|c|t|a|n
c|c|g|g|n
a|a|a|g|n
g|a|a|g|n
t|c|a|c|n
a|a|c|c|n
c|g|a|g|n
c|c|a|c|n
g|c|a|c|n
c|a|c|c|n
a|t|g|g|n
t|g|a|g|n
c|t|g|g|n
a|g|a|g|ie
c|t|t|a|n
a|c|a|c|n
g|g|a|g|n
g|t|g|g|n
t|t|g|g|n
g|a|c|c|n
t|t|t|a|n
g|t|t|a|n
t|a|c|c|n
g|a|t|a|n
t|t|a|c|n
a|t|a|c|ei
t|a|g|g|n
g|t|a|c|n
a|c|c|a|n
a|a|t|a|n
t|a|t|a|ei
c|g|c|c|n
t|c|c|a|n
a|a|g|g|n
t|g|c|c|n
g|g|c|c|n
c|a|t|a|n
c|t|a|c|n
a|g|c|c|ie
g|a|g|g|n
c|c|c|a|n
g|c|c|a|n
c|a|g|g|n
t|c|g|c|ei
g|g|t|a|n
a|c|t|t|n
c|g|g|g|n
a|g|t|a|ie
c|a|a|c|n
t|g|t|a|n
g|t|c|a|n
a|a|a|c|n
a|t|c|a|n
a|g|g|g|ie
a|c|g|c|n
c|g|t|a|ei
c|t|c|a|n
c|c|g|c|n
g|c|t|t|n
t|a|a|c|ei
t|t|c|a|n
g|g|g|g|n
g|c|g|c|n
c|c|t|t|n
g|a|a|c|n
t|g|g|g|n
t|c|t|t|n
g|a|c|a|n
t|c|a|a|n
c|t|g|c|n
c|g|a|c|ei
g|t|t|t|n
t|g|a|c|n
t|t|t|t|n
c|a|c|a|n
a|g|a|c|ie
a|c|a|a|n
t|a|c|a|n
a|t|t|t|n
a|t|g|c|n
c|t|t|t|n
g|c|a|a|n
g|g|a|c|n
g|t|g|c|n
a|a|c|a|n
c|c|a|a|n
t|t|g|c|n
a|a|g|c|n
t|a|g|c|n
a|c|c|t|n
c|t|a|a|n
g|a|g|c|n
c|a|t|t|n
g|a|t|t|n
a|t|a|a|n
t|c|c|t|n
g|t|a|a|n
t|a|t|t|n
a|g|c|a|ie
g|g|c|a|n
t|g|c|a|n
c|a|g|c|n
c|g|c|a|n
a|a|t|t|n
g|c|c|t|n
t|t|a|a|n
c|c|c|t|n
a|c|g|a|ei
g|c|g|a|ei
c|a|a|a|ei
t|c|g|a|ei
c|g|t|t|n
t|g|t|t|n
t|g|g|c|n
a|g|g|c|ie
c|c|g|a|n
c|g|g|c|n
g|t|c|t|n
g|a|a|a|n
g|g|t|t|n
a|g|t|t|ie
g|g|g|c|n
a|t|c|t|n
t|a|a|a|n
a|a|a|a|n
t|t|c|t|n
c|t|c|t|n
c|g|a|a|ei
t|c|a|t|n
t|g|a|a|n
a|a|c|t|n
g|t|g|a|n
c|a|c|t|n
g|a|c|t|n
g|c|a|t|n
a|t|g|a|n
c|c|a|t|n
t|a|c|t|n
c|t|g|a|n
a|c|a|t|n
t|t|g|a|n
a|g|a|a|ie
g|g|a|a|n
t|t|a|t|n
a|g|c|t|ie
c|t|a|t|n
a|a|g|a|n
t|a|g|a|n
g|t|a|t|n
g|a|g|a|n
c|g|c|t|n
a|t|a|t|n
c|a|g|a|n
t|g|c|t|n
g|g|c|t|n
c|g|g|a|n
t|c|g|t|n
a|c|g|t|ei
c|a|a|t|n
g|c|g|t|ei
c|c|g|t|ei
g|a|a|t|n
t|g|g|a|n
g|g|g|a|n
a|g|g|a|ie
a|a|a|t|n
t|a|a|t|n
t|g|a|t|n
c|t|g|t|ei
a|g|a|t|ie
a|t|g|t|ei
g|g|a|t|n
g|t|g|t|n
t|t|g|t|ei
t|a|g|t|ei
c|a|g|t|ei
a|a|g|t|ei
g|a|g|t|ei
g|g|g|t|ei
c|g|g|t|ei
a|g|g|t|ei
t|g|g|t|ei

## JRip

Decision list:

rules | predicted class
---|---
(POS32 = T) and (POS31 = G) and (POS35 = G) and (POS34 = A)|EI (445.0/6.0)
(POS32 = T) and (POS31 = G) and (POS33 = A)|EI (180.0/26.0)
(POS32 = T) and (POS31 = G) and (POS35 = G) and (POS36 = T)|EI (36.0/2.0)
(POS32 = T) and (POS31 = G) and (POS53 = G) and (POS40 = G)|EI (21.0/4.0)
(POS32 = T) and (POS31 = G) and (POS35 = G) and (POS39 = C)|EI (13.0/2.0)
(POS32 = T) and (POS31 = G) and (POS50 = G) and (POS28 = A) and (POS33 = G)|EI (10.0/0.0)
(POS29 = A) and (POS30 = G) and (POS28 = C)|IE (569.0/44.0)
(POS30 = G) and (POS28 = T) and (POS29 = A)|IE (132.0/11.0)
(POS29 = A) and (POS30 = G) and (POS22 = T)|IE (22.0/10.0)
|N (1441.0/23.0)


## PART

Decision list:

rules | predicted class
---|---
POS30 != G AND POS35 != G|N (858.0/5.0)
POS32 != T AND POS29 = A AND POS30 = G AND POS28 != G AND POS28 != A AND POS25 != G AND POS25 != A|IE (421.0/19.0)
POS32 != T AND POS29 != A|N (360.0/5.0)
POS31 = G AND POS32 = T AND POS35 = G AND POS34 != T AND POS33 != C AND POS33 != T AND POS34 = A AND POS39 != A|EI (344.0)
POS31 != G AND POS30 = G AND POS29 = A AND POS32 = T|IE (143.0/10.0)
POS31 != G AND POS32 = T|N (100.0)
POS32 != T AND POS30 = G AND POS21 != A AND POS20 != A AND POS22 != G AND POS22 != A AND POS24 != A AND POS24 != G|IE (43.0/3.0)
POS32 != T AND POS28 != C|N (96.0/6.0)
POS32 != T AND POS30 = G AND POS17 != A AND POS19 != C|IE (13.0/3.0)
POS31 = G AND POS32 = T AND POS29 != A AND POS33 != C AND POS36 = T|EI (64.0/1.0)
POS31 = G AND POS32 = T AND POS29 != A AND POS33 = A|EI (33.0/3.0)
POS31 != G|N (14.0)
POS29 != G AND POS32 != T|N (12.0/3.0)
POS29 != G AND POS29 != A AND POS39 != A AND POS44 != C|N (11.0/1.0)
POS29 != G AND POS28 = T AND POS25 != A|IE (22.0/1.0)
POS29 != G AND POS28 != C AND POS43 != A AND POS17 != T|EI (96.0/1.0)
POS29 != G AND POS30 = G AND POS35 = G AND POS36 = T|EI (37.0)
POS29 != G AND POS33 = A AND POS47 != A|EI (63.0/5.0)
POS29 != G AND POS28 = C AND POS26 != A AND POS35 != G AND POS33 != A AND POS14 != G|IE (42.0/2.0)
POS29 != G AND POS21 != T AND POS23 != T|EI (45.0/7.0)
POS29 != G AND POS25 != G AND POS4 != A AND POS43 != T AND POS10 != T|IE (13.0)
POS28 != C|N (19.0/4.0)
POS44 != T AND POS22 != T|IE (8.0/2.0)
POS44 = T|N (6.0/2.0)
|EI (6.0)


## J48 Decision Tree

* POS30 = G
	* POS32 = T
		* POS31 = G
			* POS35 = G: EI (487.0/21.0)
			* POS35 != G
				* POS33 = A: EI (81.0/12.0)
				* POS33 != A
					* POS29 = A
						* POS28 = A
							* POS41 = T: N (5.0/2.0)
							* POS41 != T: EI (6.0)
						* POS28 != A
							* POS23 = A: EI (10.0/3.0)
							* POS23 != A: IE (72.0/10.0)
					* POS29 != A: N (13.0/3.0)
		* POS31 != G
			* POS29 = A: IE (143.0/10.0)
			* POS29 != A: N (41.0)
	* POS32 != T
		* POS29 = A
			* POS28 = G: N (30.0/4.0)
			* POS28 != G
				* POS28 = A
					* POS59 = C: IE (8.0/2.0)
					* POS59 != C: N (32.0/4.0)
				* POS28 != A
					* POS25 = G
						* POS21 = A: N (5.0)
						* POS21 != A
							* POS57 = T: N (5.0/1.0)
							* POS57 != T: IE (25.0/3.0)
					* POS25 != G: IE (452.0/28.0)
		* POS29 != A: N (212.0/4.0)
* POS30 != G
	* POS35 = G
		* POS32 = T
			* POS31 = G
				* POS34 = G: N (5.0/1.0)
				* POS34 != G
					* POS34 = A: EI (112.0/1.0)
					* POS34 != A
						* POS3 = C: N (5.0)
						* POS3 != C: EI (13.0/3.0)
			* POS31 != G: N (59.0)
		* POS32 != T: N (190.0/1.0)
	* POS35 != G: N (858.0/5.0)


## SimpleCart Decision Tree

		* POS30=(C)|(T)|(A)
					* POS35=(A)|(T)|(C)|(N)|(R): N(853.0/4.0)
					* POS35!=(A)|(T)|(C)|(N)|(R)
				* POS32=(G)|(C)|(A): N(189.0/1.0)
				* POS32!=(G)|(C)|(A)
					* POS31=(T)|(C)|(A): N(59.0/0.0)
					* POS31!=(T)|(C)|(A): EI(122.0/13.0)
		* POS30!=(C)|(T)|(A)
			* POS32=(G)|(C)|(A)
				* POS29=(T)|(G)|(C): N(208.0/4.0)
				* POS29!=(T)|(G)|(C)
				* POS28=(G)|(A): N(56.0/14.0)
				* POS28!=(G)|(A): IE(447.0/40.0)
			* POS32!=(G)|(C)|(A)
				* POS31=(T)|(C)|(A)
					* POS29=(T)|(G)|(C): N(41.0/0.0)
					* POS29!=(T)|(G)|(C): IE(133.0/10.0)
				* POS31!=(T)|(C)|(A)
					* POS35=(A)|(T)|(C)
							* POS33=(T)|(C)|(G)|(N): IE(67.0/39.0)
							* POS33!=(T)|(C)|(G)|(N): EI(69.0/12.0)
					* POS35!=(A)|(T)|(C): EI(467.0/21.0)


