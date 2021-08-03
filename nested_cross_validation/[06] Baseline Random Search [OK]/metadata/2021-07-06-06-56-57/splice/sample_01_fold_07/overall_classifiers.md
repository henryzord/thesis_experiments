# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | N | 0.518996 |
| POS30 = G and POS32 = T and POS31 = G and POS35 != R and POS33 != N | EI | 0.174958 |
| POS30 = G and POS32 != T and POS29 != C and POS28 != A and POS25 != A | IE | 0.127649 |
| POS30 = G and POS32 = T and POS31 != G and POS29 != C and POS28 != G | IE | 0.042462 |
| POS30 != G and POS35 != R and POS32 != N and POS31 != T | EI | 0.011568 |
| POS21 = T and POS29 = A and POS30 = G | IE | 0.103085 |
| POS21 = C and POS29 = A and POS30 = G | IE | 0.071541 |
| POS30 = G and POS29 = A and POS32 = T and POS31 = G and POS35 = T and POS33 = T | IE | 0.002746 |
| POS30 = G and POS29 = A and POS32 = T and POS31 = G and POS35 = C and POS33 = G | IE | 0.003143 |
| POS30 = G and POS29 = A and POS32 = T and POS31 = G and POS35 = C and POS33 = C | IE | 0.005023 |
| POS30 = G and POS29 = A and POS32 = T and POS31 = G and POS35 = C and POS33 = T | IE | 0.003704 |
| POS30 = G and POS29 = A and POS32 = T and POS31 = G and POS35 = G and POS28 = C and POS25 = T and POS55 = C | IE | 0.001501 |
| POS30 = G and POS29 = A and POS32 = T and POS31 = G and POS35 = T and POS33 = C | IE | 0.001467 |
| POS21 = N and POS29 = N and POS30 = N | EI | 0.000459 |
| POS30 = G and POS32 != T and POS29 != C and POS28 != A and POS25 != G | IE | 0.131770 |
| POS30 = G and POS32 = T and POS31 = G and POS35 != R and POS33 != T | EI | 0.175397 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| POS30 != G and POS35 != G | N | 0.379784 |
| POS32 != T and POS29 = A and POS30 = G and POS28 != G and POS28 != A and POS25 != G and POS25 != A | IE | 0.226786 |
| POS32 != T and POS29 != A | N | 0.268202 |
| POS31 = G and POS32 = T and POS35 = G and POS34 != T and POS33 != C and POS39 != A | EI | 0.439795 |
| POS31 != G and POS29 = A and POS30 = G and POS32 = T and POS25 != G | IE | 0.179131 |
| POS31 != G and POS29 != A | N | 0.163832 |
| POS32 != T and POS30 = G and POS20 != A and POS21 != A and POS22 != G and POS17 != A and POS10 != G | IE | 0.076433 |
| POS32 != T | N | 0.250216 |
| POS31 = A | N | 0.027106 |
| POS31 != G and POS48 = G | IE | 0.022651 |
| POS31 = G and POS29 != A and POS28 != G and POS35 = G | EI | 0.281364 |
| POS31 = G and POS29 != A and POS3 != A and POS37 != A | N | 0.044554 |
| POS31 = G and POS33 = A and POS25 != C | EI | 0.397928 |
| POS31 = G and POS28 != G and POS28 != A and POS23 = T | IE | 0.245030 |
| POS31 = G and POS22 = T and POS13 != C and POS15 != C | IE | 0.065964 |
| POS31 = G and POS23 != T and POS33 != T and POS28 != A and POS18 != G and POS28 != G and POS26 != A and POS35 != G | IE | 0.167972 |
| POS31 = G and POS33 != T | EI | 0.612505 |
| POS31 = G | IE | 0.317965 |
|  | N | 0.787879 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

pos21|pos29|pos30|class
---|---|---|---
n|n|n|ei
c|t|c|n
g|t|c|n
t|t|c|n
a|t|c|n
a|g|c|n
c|g|c|n
t|g|c|n
g|g|c|n
g|c|c|n
c|t|t|n
t|c|c|n
g|t|t|n
t|t|t|n
c|c|c|n
a|t|t|n
a|c|c|n
a|g|t|n
t|a|c|n
c|g|t|n
a|a|c|n
g|g|t|n
g|a|c|n
c|a|c|n
t|g|t|n
g|t|a|n
a|t|a|n
t|t|a|n
c|c|t|n
c|t|a|n
t|c|t|n
g|c|t|n
a|c|t|n
a|a|t|n
t|g|a|n
g|a|t|n
t|a|t|n
g|g|a|n
c|g|a|n
c|a|t|n
a|g|a|n
t|c|a|n
c|t|g|n
g|c|a|n
t|t|g|n
c|c|a|n
a|c|a|n
g|t|g|n
a|t|g|n
t|g|g|n
g|g|g|n
c|a|a|n
t|a|a|n
c|g|g|ei
a|g|g|n
a|a|a|n
g|a|a|n
n|c|g|ei
a|c|g|ei
t|c|g|ei
g|c|g|n
c|c|g|ei
t|a|g|ie
c|a|g|ie
g|a|g|ei
a|a|g|ei

## PART

Decision list:

rules | predicted class
---|---
POS30 != G AND POS35 != G|N (853.0/4.0)
POS32 != T AND POS29 = A AND POS30 = G AND POS28 != G AND POS28 != A AND POS25 != G AND POS25 != A|IE (427.0/19.0)
POS32 != T AND POS29 != A|N (370.0/6.0)
POS31 = G AND POS32 = T AND POS35 = G AND POS34 != T AND POS33 != C AND POS39 != A|EI (446.0/4.0)
POS31 != G AND POS29 = A AND POS30 = G AND POS32 = T AND POS25 != G|IE (126.0/6.0)
POS31 != G AND POS29 != A|N (85.0)
POS32 != T AND POS30 = G AND POS20 != A AND POS21 != A AND POS22 != G AND POS17 != A AND POS10 != G|IE (57.0/10.0)
POS32 != T|N (118.0/9.0)
POS31 = A|N (10.0)
POS31 != G AND POS48 = G|IE (9.0/2.0)
POS31 = G AND POS29 != A AND POS28 != G AND POS35 = G|EI (64.0/3.0)
POS31 = G AND POS29 != A AND POS3 != A AND POS37 != A|N (19.0/4.0)
POS31 = G AND POS33 = A AND POS25 != C|EI (100.0/7.0)
POS31 = G AND POS28 != G AND POS28 != A AND POS23 = T|IE (45.0/4.0)
POS31 = G AND POS22 = T AND POS13 != C AND POS15 != C|IE (13.0/2.0)
POS31 = G AND POS23 != T AND POS33 != T AND POS28 != A AND POS18 != G AND POS28 != G AND POS26 != A AND POS35 != G|IE (28.0/4.0)
POS31 = G AND POS33 != T|EI (79.0/11.0)
POS31 = G|IE (12.0/3.0)
|N (8.0)


## J48 Decision Tree

* POS30 = G
	* POS29 = A
		* POS32 = T
			* POS31 = G
				* POS35 = G
					* POS28 = C
						* POS25 = C: EI (49.0/6.0)
						* POS25 = T
							* POS55 = G: EI (5.0/1.0)
							* POS55 = C: IE (11.0/5.0)
							* POS55 = A: EI (4.0)
							* POS55 = T: EI (10.0/2.0)
							* POS55 = N: EI (0.0)
						* POS25 = G: EI (25.0)
						* POS25 = A: EI (24.0)
						* POS25 = N: EI (0.0)
					* POS28 = A: EI (98.0)
					* POS28 = T: EI (13.0/5.0)
					* POS28 = G: EI (47.0)
					* POS28 = N: EI (0.0)
				* POS35 = C
					* POS33 = A: EI (20.0/2.0)
					* POS33 = G: IE (21.0/9.0)
					* POS33 = C: IE (11.0)
					* POS33 = T: IE (10.0/1.0)
					* POS33 = N: IE (0.0)
				* POS35 = T
					* POS33 = A: EI (27.0/4.0)
					* POS33 = G: IE (14.0/3.0)
					* POS33 = C: IE (5.0/1.0)
					* POS33 = T: IE (6.0)
					* POS33 = N: EI (0.0)
				* POS35 = A
					* POS33 = A: EI (20.0/3.0)
					* POS33 = G: IE (22.0/8.0)
					* POS33 = C: IE (3.0)
					* POS33 = T: EI (0.0)
					* POS33 = N: EI (0.0)
				* POS35 = N: EI (0.0)
				* POS35 = R: EI (0.0)
			* POS31 = A
				* POS25 = C: IE (25.0)
				* POS25 = T: IE (33.0/1.0)
				* POS25 = G: N (3.0)
				* POS25 = A: IE (2.0)
				* POS25 = N: IE (0.0)
			* POS31 = C
				* POS19 = C: IE (20.0/1.0)
				* POS19 = T: IE (22.0)
				* POS19 = G: IE (5.0/2.0)
				* POS19 = A: N (3.0/1.0)
				* POS19 = N: IE (0.0)
			* POS31 = T
				* POS18 = T: IE (10.0)
				* POS18 = C: IE (10.0/1.0)
				* POS18 = G: IE (5.0/1.0)
				* POS18 = A: N (2.0)
			* POS31 = N: EI (0.0)
		* POS32 = A
			* POS28 = C: IE (121.0/9.0)
			* POS28 = A: N (14.0/3.0)
			* POS28 = T
				* POS25 = C: IE (16.0/2.0)
				* POS25 = T: IE (26.0)
				* POS25 = G: N (2.0)
				* POS25 = A: IE (4.0)
				* POS25 = N: IE (0.0)
			* POS28 = G: N (15.0/1.0)
			* POS28 = N: IE (0.0)
		* POS32 = C
			* POS28 = C: IE (132.0/12.0)
			* POS28 = A: N (13.0/6.0)
			* POS28 = T: IE (24.0/3.0)
			* POS28 = G: N (7.0/2.0)
			* POS28 = N: IE (0.0)
		* POS32 = G
			* POS28 = C
				* POS21 = C
					* POS24 = C: IE (25.0)
					* POS24 = T: IE (29.0)
					* POS24 = G: N (1.0)
					* POS24 = A: IE (2.0)
					* POS24 = N: IE (0.0)
				* POS21 = T: IE (50.0/1.0)
				* POS21 = G
					* POS22 = C: IE (12.0/1.0)
					* POS22 = T: IE (10.0)
					* POS22 = G: N (1.0)
					* POS22 = A: N (1.0)
					* POS22 = N: IE (0.0)
				* POS21 = A: IE (10.0/5.0)
				* POS21 = N: IE (0.0)
			* POS28 = A: N (13.0/3.0)
			* POS28 = T
				* POS26 = T: IE (12.0/2.0)
				* POS26 = C: IE (10.0)
				* POS26 = A: IE (0.0)
				* POS26 = G: N (2.0)
				* POS26 = N: IE (0.0)
			* POS28 = G: N (8.0/1.0)
			* POS28 = N: IE (0.0)
		* POS32 = N: IE (0.0)
	* POS29 = C
		* POS32 = T
			* POS33 = A: EI (11.0/2.0)
			* POS33 = G: EI (45.0/2.0)
			* POS33 = C: EI (2.0/1.0)
			* POS33 = T: N (4.0/1.0)
			* POS33 = N: EI (0.0)
		* POS32 = A: N (12.0)
		* POS32 = C: N (8.0)
		* POS32 = G: N (13.0)
		* POS32 = N: EI (0.0)
	* POS29 = G
		* POS32 = T
			* POS31 = G
				* POS35 = G: EI (69.0)
				* POS35 = C: EI (6.0/1.0)
				* POS35 = T: N (10.0/4.0)
				* POS35 = A: EI (3.0/1.0)
				* POS35 = N: EI (0.0)
				* POS35 = R: EI (0.0)
			* POS31 = A: N (3.0)
			* POS31 = C: N (10.0)
			* POS31 = T: N (3.0)
			* POS31 = N: EI (0.0)
		* POS32 = A: N (27.0/1.0)
		* POS32 = C: N (34.0/1.0)
		* POS32 = G: N (33.0/1.0)
		* POS32 = N: N (0.0)
	* POS29 = T
		* POS32 = T
			* POS31 = G
				* POS34 = A
					* POS33 = A: EI (32.0)
					* POS33 = G: EI (23.0)
					* POS33 = C: EI (0.0)
					* POS33 = T: N (1.0)
					* POS33 = N: EI (0.0)
				* POS34 = G: EI (10.0/2.0)
				* POS34 = C: EI (7.0/3.0)
				* POS34 = T: EI (13.0/1.0)
				* POS34 = N: EI (0.0)
			* POS31 = A: N (2.0)
			* POS31 = C: N (9.0)
			* POS31 = T: N (11.0)
			* POS31 = N: EI (0.0)
		* POS32 = A: N (32.0)
		* POS32 = C: N (24.0/1.0)
		* POS32 = G: N (40.0/1.0)
		* POS32 = N: N (0.0)
	* POS29 = N: IE (0.0)
* POS30 = A
	* POS35 = G
		* POS32 = T
			* POS34 = A
				* POS33 = A: EI (26.0)
				* POS33 = G: EI (27.0/4.0)
				* POS33 = C: N (3.0)
				* POS33 = T: N (1.0)
				* POS33 = N: EI (0.0)
			* POS34 = G: N (3.0)
			* POS34 = C: N (1.0)
			* POS34 = T: N (10.0/3.0)
			* POS34 = N: EI (0.0)
		* POS32 = A: N (26.0/1.0)
		* POS32 = C: N (22.0)
		* POS32 = G: N (24.0)
		* POS32 = N: N (0.0)
	* POS35 = C: N (106.0)
	* POS35 = T: N (82.0/2.0)
	* POS35 = A: N (99.0)
	* POS35 = N: N (0.0)
	* POS35 = R: N (0.0)
* POS30 = T
	* POS35 = G
		* POS32 = T
			* POS34 = A
				* POS33 = A: EI (34.0)
				* POS33 = G: EI (15.0/1.0)
				* POS33 = C: N (2.0)
				* POS33 = T: EI (0.0)
				* POS33 = N: EI (0.0)
			* POS34 = G: N (8.0/1.0)
			* POS34 = C: EI (2.0)
			* POS34 = T: N (10.0)
			* POS34 = N: EI (0.0)
		* POS32 = A: N (21.0)
		* POS32 = C: N (17.0)
		* POS32 = G: N (10.0)
		* POS32 = N: N (0.0)
	* POS35 = C: N (87.0/1.0)
	* POS35 = T: N (107.0)
	* POS35 = A: N (90.0)
	* POS35 = N: N (0.0)
	* POS35 = R: N (0.0)
* POS30 = C
	* POS31 = G
		* POS32 = T
			* POS2 = C: EI (12.0)
			* POS2 = G: EI (10.0/5.0)
			* POS2 = A: EI (3.0/1.0)
			* POS2 = T: N (5.0/2.0)
			* POS2 = D: EI (0.0)
		* POS32 = A: N (6.0)
		* POS32 = C: N (13.0)
		* POS32 = G: N (12.0)
		* POS32 = N: N (0.0)
	* POS31 = A: N (107.0)
	* POS31 = C: N (106.0)
	* POS31 = T: N (119.0)
	* POS31 = N: N (0.0)
* POS30 = N: EI (1.0)


## SimpleCart Decision Tree

	* POS30=(N)|(G)
		* POS32=(N)|(T)
			* POS31=(N)|(G)
					* POS35=(N)|(G)|(R): EI(462.0/22.0)
					* POS35!=(N)|(G)|(R)
							* POS33=(T)|(C)|(G)|(N)
						* POS29=(T)|(G): N(11.0/3.0)
						* POS29!=(T)|(G)
							* POS22=(A)|(G)
							* POS26=(A): EI(11.0/2.0)
							* POS26!=(A): IE(14.0/5.0)
							* POS22!=(A)|(G): IE(56.0/4.0)
							* POS33!=(T)|(C)|(G)|(N): EI(73.0/12.0)
			* POS31!=(N)|(G)
					* POS29=(T)|(G)|(C): N(45.0/0.0)
					* POS29!=(T)|(G)|(C)
					* POS28=(G)|(A): N(8.0/4.0)
					* POS28!=(G)|(A): IE(123.0/5.0)
		* POS32!=(N)|(T)
				* POS29=(T)|(G)|(C): N(218.0/5.0)
				* POS29!=(T)|(G)|(C)
				* POS28=(G)|(A)
						* POS22=(A)|(G)|(N): N(40.0/1.0)
						* POS22!=(A)|(G)|(N)
								* POS48=(T)|(A)|(C)|(N): N(13.0/4.0)
								* POS48!=(T)|(A)|(C)|(N): IE(10.0/2.0)
				* POS28!=(G)|(A)
					* POS25=(A)|(G)
						* POS24=(A)|(G)
						* POS51=(A): IE(7.0/1.0)
						* POS51!=(A): N(16.0/1.0)
						* POS24!=(A)|(G): IE(32.0/6.0)
					* POS25!=(A)|(G): IE(408.0/19.0)
	* POS30!=(N)|(G)
					* POS35=(A)|(T)|(C)|(N)|(R): N(849.0/3.0)
					* POS35!=(A)|(T)|(C)|(N)|(R)
					* POS32=(G)|(C)|(A)|(N): N(188.0/1.0)
					* POS32!=(G)|(C)|(A)|(N)
					* POS31=(T)|(C)|(A): N(53.0/0.0)
					* POS31!=(T)|(C)|(A): EI(124.0/8.0)


