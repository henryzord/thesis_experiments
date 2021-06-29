# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | N | 0.519164 |
| POS30 != A and POS32 != A and POS31 != A and POS35 != C and POS33 != C and POS34!=(T) and POS39!=(A) and POS34!=(C) | EI | 0.137890 |
| POS30 != A and POS32 = A and POS29 != C and POS28 != A and POS25 != G and POS26!=(A) and POS19!=(A) and POS13!=(A) and POS24!=(G) and POS47!=(T) | IE | 0.041516 |
| POS30 = G and POS29 = A and POS32 = C | IE | 0.053672 |
| POS30 = G and POS29 = A and POS32 = G and POS28 = C | IE | 0.053712 |
| POS30 != A and POS32 != A and POS31 = A and POS29 != C and POS25 != G | IE | 0.035281 |
| POS30 = G and POS29 = A and POS32 = T and POS31 = C | IE | 0.018243 |
| POS30 = A and POS35 != R and POS31 != N and POS32 != A and POS34 != G | EI | 0.005857 |
| POS29 = A and POS30 = G and POS31 = T and POS32 = T | IE | 0.010233 |
| POS30 = G and POS29 = A and POS32 = T and POS31 = G and POS35 = A and POS28 = C | IE | 0.005482 |
| POS30 = G and POS29 = A and POS32 = G and POS28 = T | IE | 0.008804 |
| POS29 = A and POS30 = G and POS31 = G and POS32 = T | EI | 0.112202 |
| POS30 = G and POS29 = A and POS32 = T and POS31 = G and POS35 = C and POS33 = C | IE | 0.005474 |
| POS30 = G and POS29 = A and POS32 = T and POS31 = G and POS35 = C and POS33 = T | IE | 0.003367 |
| POS30 = G and POS29 = A and POS32 = T and POS31 = G and POS35 = T and POS33 = G and POS22 = T | IE | 0.003656 |
| POS30 = G and POS29 = A and POS32 = T and POS31 = G and POS35 = T and POS33 = T | IE | 0.002354 |
| POS30 = G and POS29 = A and POS32 = T and POS31 = G and POS35 = C and POS33 = G and POS50 = T | IE | 0.002745 |
| POS30 = G and POS29 = A and POS32 = T and POS31 = G and POS35 = A and POS28 = T | IE | 0.001466 |
| POS30 = G and POS29 = A and POS32 = T and POS31 = G and POS35 = T and POS33 = C | IE | 0.001466 |
| POS30 = G and POS29 = A and POS32 = T and POS31 = G and POS35 = C and POS33 = G and POS50 = C | IE | 0.000825 |
| POS30 = G and POS29 = A and POS32 = T and POS31 = G and POS35 = T and POS33 = G and POS22 = C | IE | 0.001374 |
| POS30 != A and POS32 = A and POS29 != C and POS28 = A and POS22 != N and POS59 != G | IE | 0.000078 |
| POS30 != A and POS32 = A and POS29 != C and POS28 != A and POS25 = G and POS21!=(A) and POS24 != G and POS22!=(G) and POS36 = C | IE | 0.000230 |
| POS30 != A and POS32 != A and POS31 != A and POS35 = C and POS33 != N and POS22!=(T) and POS41!=(A) | EI | 0.001855 |
| POS29 = A and POS30 = G and POS31 = C and POS32 = A | IE | 0.007703 |
| POS29 = A and POS30 = G and POS31 = T and POS32 = G | IE | 0.009316 |
| POS29 = A and POS30 = G and POS31 = G and POS32 = G | IE | 0.028722 |
| POS30 != A and POS32 != A and POS31 != A and POS35 != C and POS33 = C and POS18 != C and POS8!=(T) | EI | 0.000391 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| POS30 = C and POS31 = T | N | 0.080000 |
| POS30 = C and POS31 = A | N | 0.075073 |
| POS30 = T and POS35 = T | N | 0.074447 |
| POS30 = C and POS31 = C | N | 0.066306 |
| POS30 = A and POS32 = A | N | 0.068197 |
| POS30 = T and POS35 = A | N | 0.061863 |
| POS32 = G and POS29 = A and POS30 = G and POS28 = C | IE | 0.074116 |
| POS32 = G and POS29 = G | N | 0.044457 |
| POS32 = G and POS29 = T | N | 0.042991 |
| POS32 = G and POS30 = A | N | 0.040045 |
| POS32 = G and POS29 = A and POS28 = T | IE | 0.014564 |
| POS32 = A and POS29 = A and POS28 = C | IE | 0.069001 |
| POS32 = G | N | 0.049206 |
| POS32 = A and POS29 = A and POS28 = T | IE | 0.026686 |
| POS32 = A | N | 0.127366 |
| POS32 = C and POS29 = A and POS30 = G and POS28 = C | IE | 0.085929 |
| POS32 = C and POS29 = C | N | 0.074976 |
| POS31 = T and POS30 = A | N | 0.035560 |
| POS31 = C and POS29 = G | N | 0.035560 |
| POS31 = T and POS29 = A and POS28 = C | IE | 0.019576 |
| POS31 = T | N | 0.040746 |
| POS31 = C and POS29 = T | N | 0.034304 |
| POS32 = C and POS29 = G | N | 0.034333 |
| POS31 = C and POS30 = G and POS25 = C | IE | 0.030857 |
| POS31 = C and POS30 = G | IE | 0.011903 |
| POS31 = A and POS30 = G and POS29 = A and POS28 = C | IE | 0.042622 |
| POS31 = C | N | 0.051136 |
| POS31 = A and POS28 = A | N | 0.018465 |
| POS31 = A and POS28 = G | N | 0.022248 |
| POS32 = T and POS31 = G and POS35 = G and POS30 = G | EI | 0.630176 |
| POS32 = C and POS28 = T | IE | 0.037557 |
| POS32 = C and POS28 = C | N | 0.046625 |
| POS31 = G and POS32 = T and POS33 = A | EI | 0.357226 |
| POS30 = C | EI | 0.039823 |
| POS30 = A and POS43 = G | N | 0.030788 |
| POS30 = A and POS43 = T | N | 0.027640 |
| POS29 = A and POS30 = G and POS28 = C and POS23 = T | IE | 0.182478 |
| POS29 = A and POS30 = G and POS28 = T | IE | 0.160595 |
| POS29 = A and POS30 = G and POS28 = C and POS26 = C | IE | 0.101626 |
| POS33 = G and POS34 = A | EI | 0.272824 |
| POS29 = A and POS23 = C | IE | 0.155727 |
| POS29 = A and POS23 = A | EI | 0.047872 |
|  | N | 0.714286 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

pos29|pos30|pos31|pos32|class
---|---|---|---|---
n|n|n|n|ei
a|c|t|g|n
t|c|t|g|n
c|c|t|g|n
g|c|t|g|n
c|t|t|g|n
a|t|t|g|n
g|t|t|g|n
t|t|t|g|n
t|c|c|g|n
a|c|c|g|ei
g|a|t|g|n
c|a|t|g|n
a|a|t|g|n
t|a|t|g|n
c|c|c|g|n
g|c|c|g|n
t|t|c|g|n
c|c|t|c|n
a|t|c|g|ei
t|c|t|c|n
g|c|t|c|n
c|t|c|g|n
t|g|t|g|n
c|g|t|g|n
g|g|t|g|n
a|c|t|c|n
a|g|t|g|ie
t|a|c|g|ei
c|t|t|c|n
a|a|c|g|n
g|t|t|c|ei
c|a|c|g|n
g|a|c|g|ei
t|c|a|g|n
c|c|a|g|n
t|t|t|c|n
a|c|a|g|n
g|c|a|g|n
a|t|t|c|n
g|a|t|c|n
t|g|c|g|n
a|a|t|c|n
t|c|c|c|n
t|t|a|g|n
a|t|a|g|n
c|g|c|g|ei
c|a|t|c|n
g|c|c|c|n
t|a|t|c|n
c|c|c|c|n
a|c|c|c|n
g|g|c|g|n
a|g|c|g|ie
c|c|t|a|n
a|t|c|c|n
g|c|g|g|n
a|a|a|g|n
a|c|g|g|n
g|t|c|c|n
t|c|t|a|n
t|t|c|c|n
c|g|t|c|ei
a|g|t|c|ie
c|c|g|g|n
t|c|g|g|n
a|c|t|a|ei
g|a|a|g|n
t|g|t|c|n
c|t|c|c|n
c|a|a|g|n
g|g|t|c|n
g|c|t|a|n
t|a|a|g|n
t|a|c|c|n
t|c|a|c|n
t|t|g|g|n
t|t|t|a|n
g|g|a|g|n
a|c|a|c|n
a|t|g|g|n
g|a|c|c|n
c|c|a|c|n
g|c|a|c|n
a|a|c|c|n
g|t|g|g|n
g|t|t|a|n
c|g|a|g|n
t|g|a|g|n
c|t|t|a|n
c|t|g|g|n
c|a|c|c|n
a|g|a|g|ie
a|c|c|a|n
t|a|g|g|n
g|t|a|c|n
t|t|a|c|n
c|g|c|c|n
c|c|c|a|n
t|a|t|a|ei
c|t|a|c|n
a|t|a|c|ei
c|a|t|a|n
c|a|g|g|n
t|g|c|c|n
g|c|c|a|n
t|c|c|a|n
a|a|t|a|n
a|a|g|g|n
g|a|t|a|n
g|a|g|g|n
g|g|c|c|n
a|g|c|c|ie
t|c|g|c|ei
g|c|g|c|n
c|g|t|a|n
c|g|g|g|n
g|a|a|c|n
g|c|t|t|n
a|c|g|c|n
t|g|g|g|n
g|g|t|a|ei
a|c|t|t|n
a|a|a|c|n
c|c|g|c|n
c|c|t|t|n
a|g|t|a|ie
t|g|t|a|n
t|t|c|a|n
g|t|c|a|n
g|g|g|g|n
c|a|a|c|n
t|c|t|t|n
c|t|c|a|n
a|t|c|a|n
a|g|g|g|ie
c|g|a|c|ei
a|c|a|a|n
t|c|a|a|n
g|c|a|a|n
t|a|c|a|n
c|c|a|a|n
g|a|c|a|n
a|t|g|c|n
g|t|t|t|n
g|t|g|c|n
a|a|c|a|n
a|t|t|t|n
c|t|t|t|n
t|t|t|t|n
t|t|g|c|n
c|a|c|a|n
c|t|g|c|n
t|g|a|c|n
g|g|a|c|n
a|g|a|c|ie
a|a|g|c|n
a|t|a|a|n
c|t|a|a|ei
t|g|c|a|n
c|a|g|c|n
g|a|g|c|n
a|c|c|t|n
a|a|t|t|n
t|a|t|t|n
c|a|t|t|n
t|a|g|c|n
g|a|t|t|n
g|g|c|a|n
c|g|c|a|n
c|c|c|t|n
t|t|a|a|n
g|c|c|t|n
g|t|a|a|n
t|c|c|t|n
a|g|c|a|ie
c|c|g|a|n
t|c|g|a|ei
t|t|c|t|n
t|g|g|c|n
c|a|a|a|n
g|g|t|t|n
a|t|c|t|n
c|t|c|t|n
g|g|g|c|n
c|g|g|c|n
c|g|t|t|n
a|c|g|a|ei
g|c|g|a|n
g|a|a|a|n
g|t|c|t|n
t|a|a|a|n
t|g|t|t|n
a|a|a|a|n
a|g|t|t|ie
a|g|g|c|ie
c|g|a|a|ei
g|c|a|t|n
g|a|c|t|n
g|g|a|a|n
t|g|a|a|n
t|a|c|t|n
c|a|c|t|n
a|c|a|t|n
c|c|a|t|n
g|t|g|a|n
t|c|a|t|n
a|t|g|a|n
a|a|c|t|n
t|t|g|a|n
c|t|g|a|n
a|g|a|a|ie
a|t|a|t|n
t|t|a|t|n
g|a|g|a|n
a|a|g|a|n
g|t|a|t|n
c|g|c|t|n
g|g|c|t|n
t|a|g|a|n
t|g|c|t|n
c|a|g|a|n
c|t|a|t|n
a|g|c|t|ie
g|g|g|a|n
t|c|g|t|ei
g|a|a|t|n
g|c|g|t|ei
c|g|g|a|n
t|g|g|a|n
c|a|a|t|n
t|a|a|t|n
c|c|g|t|ei
a|a|a|t|n
a|g|g|a|ie
a|c|g|t|ei
t|t|g|t|n
g|t|g|t|n
t|g|a|t|n
g|g|a|t|n
a|g|a|t|ie
a|t|g|t|ei
c|t|g|t|ei
t|a|g|t|ei
g|a|g|t|ei
a|a|g|t|ei
c|a|g|t|ei
t|g|g|t|ei
c|g|g|t|ei
a|g|g|t|ei
g|g|g|t|ei

## PART

Decision list:

rules | predicted class
---|---
POS30 = C AND POS31 = T|N (120.0)
POS30 = C AND POS31 = A|N (114.0/1.0)
POS30 = T AND POS35 = T|N (111.0)
POS30 = C AND POS31 = C|N (98.0)
POS30 = A AND POS32 = A|N (101.0)
POS30 = T AND POS35 = A|N (91.0)
POS32 = G AND POS29 = A AND POS30 = G AND POS28 = C|IE (143.0/10.0)
POS32 = G AND POS29 = G|N (60.0/1.0)
POS32 = G AND POS29 = T|N (58.0/1.0)
POS32 = G AND POS30 = A|N (54.0/1.0)
POS32 = G AND POS29 = A AND POS28 = T|IE (25.0/3.0)
POS32 = A AND POS29 = A AND POS28 = C|IE (123.0/11.0)
POS32 = G|N (53.0/3.0)
POS32 = A AND POS29 = A AND POS28 = T|IE (49.0/7.0)
POS32 = A|N (148.0/5.0)
POS32 = C AND POS29 = A AND POS30 = G AND POS28 = C|IE (133.0/13.0)
POS32 = C AND POS29 = C|N (77.0)
POS31 = T AND POS30 = A|N (36.0)
POS31 = C AND POS29 = G|N (37.0/1.0)
POS31 = T AND POS29 = A AND POS28 = C|IE (22.0/1.0)
POS31 = T|N (57.0/9.0)
POS31 = C AND POS29 = T|N (33.0)
POS32 = C AND POS29 = G|N (34.0)
POS31 = C AND POS30 = G AND POS25 = C|IE (32.0/2.0)
POS31 = C AND POS30 = G|IE (26.0/7.0)
POS31 = A AND POS30 = G AND POS29 = A AND POS28 = C|IE (45.0/1.0)
POS31 = C|N (30.0)
POS31 = A AND POS28 = A|N (21.0/2.0)
POS31 = A AND POS28 = G|N (19.0)
POS32 = T AND POS31 = G AND POS35 = G AND POS30 = G|EI (479.0/19.0)
POS32 = C AND POS28 = T|IE (24.0/8.0)
POS32 = C AND POS28 = C|N (16.0/1.0)
POS31 = G AND POS32 = T AND POS33 = A|EI (161.0/19.0)
POS30 = C|EI (25.0/10.0)
POS30 = A AND POS43 = G|N (15.0/6.0)
POS30 = A AND POS43 = T|N (15.0/7.0)
POS29 = A AND POS30 = G AND POS28 = C AND POS23 = T|IE (28.0)
POS29 = A AND POS30 = G AND POS28 = T|IE (20.0)
POS29 = A AND POS30 = G AND POS28 = C AND POS26 = C|IE (17.0/2.0)
POS33 = G AND POS34 = A|EI (46.0/7.0)
POS29 = A AND POS23 = C|IE (14.0/5.0)
POS29 = A AND POS23 = A|EI (13.0/4.0)
|N (47.0/13.0)


## J48 Decision Tree

* POS30 = G
	* POS29 = A
		* POS32 = T
			* POS31 = G
				* POS35 = G: EI (289.0/18.0)
				* POS35 = C
					* POS33 = A: EI (19.0/2.0)
					* POS33 = G
						* POS50 = G: EI (9.0)
						* POS50 = C: IE (5.0/2.0)
						* POS50 = A: EI (2.0/1.0)
						* POS50 = T: IE (6.0)
						* POS50 = N: EI (0.0)
					* POS33 = C: IE (12.0)
					* POS33 = T: IE (11.0/2.0)
					* POS33 = N: IE (0.0)
				* POS35 = T
					* POS33 = A: EI (30.0/5.0)
					* POS33 = G
						* POS22 = C: IE (3.0)
						* POS22 = T: IE (8.0)
						* POS22 = G: IE (0.0)
						* POS22 = A: EI (4.0)
						* POS22 = N: IE (0.0)
					* POS33 = C: IE (5.0/1.0)
					* POS33 = T: IE (7.0/1.0)
					* POS33 = N: EI (0.0)
				* POS35 = A
					* POS28 = C: IE (27.0/9.0)
					* POS28 = A: EI (11.0/1.0)
					* POS28 = T: IE (5.0/1.0)
					* POS28 = G: EI (7.0/1.0)
					* POS28 = N: EI (0.0)
				* POS35 = N: EI (0.0)
				* POS35 = R: EI (0.0)
			* POS31 = A: IE (55.0/3.0)
			* POS31 = C: IE (50.0/5.0)
			* POS31 = T
				* POS28 = C: IE (21.0)
				* POS28 = A: N (2.0)
				* POS28 = T: IE (5.0)
				* POS28 = G: N (2.0)
				* POS28 = N: IE (0.0)
			* POS31 = N: EI (0.0)
		* POS32 = A
			* POS28 = C: IE (122.0/10.0)
			* POS28 = A: N (15.0/3.0)
			* POS28 = T: IE (46.0/4.0)
			* POS28 = G: N (16.0/1.0)
			* POS28 = N: IE (0.0)
		* POS32 = C: IE (180.0/31.0)
		* POS32 = G
			* POS28 = C: IE (143.0/10.0)
			* POS28 = A: N (12.0/2.0)
			* POS28 = T: IE (25.0/3.0)
			* POS28 = G: N (7.0/1.0)
			* POS28 = N: IE (0.0)
		* POS32 = N: IE (0.0)
	* POS29 = C
		* POS32 = T
			* POS31 = G
				* POS35 = G: EI (52.0)
				* POS35 = C: EI (2.0/1.0)
				* POS35 = T: EI (0.0)
				* POS35 = A: N (1.0)
				* POS35 = N: EI (0.0)
				* POS35 = R: EI (0.0)
			* POS31 = A: EI (0.0)
			* POS31 = C: N (3.0)
			* POS31 = T: N (3.0)
			* POS31 = N: EI (0.0)
		* POS32 = A: N (11.0)
		* POS32 = C: N (9.0)
		* POS32 = G: N (12.0)
		* POS32 = N: EI (0.0)
	* POS29 = G
		* POS32 = T
			* POS31 = G: EI (83.0/7.0)
			* POS31 = A: N (3.0)
			* POS31 = C: N (8.0)
			* POS31 = T: N (3.0)
			* POS31 = N: EI (0.0)
		* POS32 = A: N (29.0/1.0)
		* POS32 = C: N (34.0/1.0)
		* POS32 = G: N (34.0/1.0)
		* POS32 = N: N (0.0)
	* POS29 = T
		* POS31 = G
			* POS32 = T: EI (79.0/6.0)
			* POS32 = A: N (11.0)
			* POS32 = C: N (5.0/1.0)
			* POS32 = G: N (11.0)
			* POS32 = N: EI (0.0)
		* POS31 = A: N (29.0/1.0)
		* POS31 = C: N (29.0)
		* POS31 = T: N (30.0)
		* POS31 = N: N (0.0)
	* POS29 = N: IE (0.0)
* POS30 = A
	* POS32 = T
		* POS31 = G
			* POS35 = G: EI (58.0/4.0)
			* POS35 = C: N (8.0)
			* POS35 = T: N (5.0/1.0)
			* POS35 = A: N (6.0/1.0)
			* POS35 = N: EI (0.0)
			* POS35 = R: EI (0.0)
		* POS31 = A: N (21.0)
		* POS31 = C: N (25.0)
		* POS31 = T: N (21.0)
		* POS31 = N: N (0.0)
	* POS32 = A: N (101.0)
	* POS32 = C: N (94.0)
	* POS32 = G: N (89.0/1.0)
	* POS32 = N: N (0.0)
* POS30 = T
	* POS35 = G
		* POS31 = G
			* POS32 = T: EI (53.0/4.0)
			* POS32 = A: N (7.0)
			* POS32 = C: N (5.0)
			* POS32 = G: N (6.0)
			* POS32 = N: EI (0.0)
		* POS31 = A: N (13.0)
		* POS31 = C: N (22.0)
		* POS31 = T: N (17.0)
		* POS31 = N: N (0.0)
	* POS35 = C: N (83.0/1.0)
	* POS35 = T: N (111.0)
	* POS35 = A: N (91.0)
	* POS35 = N: N (0.0)
	* POS35 = R: N (0.0)
* POS30 = C
	* POS31 = G
		* POS32 = T
			* POS35 = G: EI (24.0/3.0)
			* POS35 = C: N (3.0)
			* POS35 = T: N (2.0)
			* POS35 = A: EI (0.0)
			* POS35 = N: EI (0.0)
			* POS35 = R: EI (0.0)
		* POS32 = A: N (7.0)
		* POS32 = C: N (11.0)
		* POS32 = G: N (12.0)
		* POS32 = N: N (0.0)
	* POS31 = A: N (114.0/1.0)
	* POS31 = C: N (98.0)
	* POS31 = T: N (120.0)
	* POS31 = N: N (0.0)
* POS30 = N: EI (1.0)


## SimpleCart Decision Tree

		* POS30=(C)|(T)|(A)
					* POS35=(A)|(T)|(C)|(N)|(R)
		* POS45=(G)
			* POS23=(T)
							* POS44=(A)|(T)|(C)|(N): N(37.0/0.0)
							* POS44!=(A)|(T)|(C)|(N): N(8.0/4.0)
			* POS23!=(T)
				* POS26=(G)
							* POS15=(A)|(G)|(T): N(28.0/0.0)
							* POS15!=(A)|(G)|(T): N(3.0/1.0)
				* POS26!=(G): N(135.0/0.0)
		* POS45!=(G): N(625.0/0.0)
					* POS35!=(A)|(T)|(C)|(N)|(R)
					* POS31=(T)|(C)|(A)|(N): N(193.0/0.0)
					* POS31!=(T)|(C)|(A)|(N)
					* POS32=(G)|(C)|(A): N(58.0/0.0)
					* POS32!=(G)|(C)|(A)
						* POS34=(T)|(C)|(G)
						* POS8=(A)|(T): EI(6.0/0.0)
						* POS8!=(A)|(T)
									* POS33=(C)|(G)|(T)|(N): N(10.0/0.0)
									* POS33!=(C)|(G)|(T)|(N): EI(3.0/0.0)
						* POS34!=(T)|(C)|(G): EI(115.0/1.0)
		* POS30!=(C)|(T)|(A)
			* POS32=(G)|(C)|(A)
				* POS29=(T)|(G)|(C)
							* POS36=(A)|(G)|(C)|(N)|(S)
				* POS1=(T)
							* POS18=(A)|(G)|(C): N(27.0/0.0)
							* POS18!=(A)|(G)|(C): N(4.0/1.0)
				* POS1!=(T): N(143.0/0.0)
							* POS36!=(A)|(G)|(C)|(N)|(S)
				* POS50=(C): N(3.0/2.0)
				* POS50!=(C)
					* POS15=(A): N(7.0/2.0)
					* POS15!=(A): N(32.0/0.0)
				* POS29!=(T)|(G)|(C)
				* POS28=(G)|(A)
						* POS22=(A)|(G)|(N)
					* POS13=(T): N(5.0/1.0)
					* POS13!=(T): N(34.0/0.0)
						* POS22!=(A)|(G)|(N)
								* POS59=(T)|(A)|(G)|(N)
						* POS3=(A): IE(3.0/0.0)
						* POS3!=(A): N(18.0/5.0)
								* POS59!=(T)|(A)|(G)|(N): IE(6.0/0.0)
				* POS28!=(G)|(A)
					* POS25=(A)|(G)
					* POS21=(A): N(8.0/0.0)
					* POS21!=(A)
							* POS24=(A)|(G)
									* POS22=(A)|(G)|(T): N(8.0/1.0)
									* POS22!=(A)|(G)|(T)
									* POS7=(T)|(G): IE(8.0/0.0)
									* POS7!=(T)|(G): N(3.0/0.0)
							* POS24!=(A)|(G)
							* POS22=(G): N(2.0/1.0)
							* POS22!=(G)
												* POS36=(A)|(G)|(C)|(N)|(S): IE(34.0/0.0)
												* POS36!=(A)|(G)|(C)|(N)|(S): IE(3.0/2.0)
					* POS25!=(A)|(G)
					* POS26=(A)
							* POS18=(A)|(G): N(7.0/2.0)
							* POS18!=(A)|(G): IE(11.0/0.0)
					* POS26!=(A)
						* POS19=(A)
								* POS58=(T)|(G)
								* POS54=(A): N(4.0/1.0)
								* POS54!=(A): IE(6.0/1.0)
								* POS58!=(T)|(G): IE(19.0/0.0)
						* POS19!=(A)
							* POS13=(A)
								* POS47=(C)
										* POS43=(A)|(C): N(3.0/1.0)
										* POS43!=(A)|(C): IE(5.0/0.0)
								* POS47!=(C): IE(31.0/0.0)
							* POS13!=(A)
								* POS24=(G)
									* POS41=(A): N(2.0/1.0)
									* POS41!=(A): IE(20.0/0.0)
								* POS24!=(G)
									* POS47=(T)
											* POS21=(A)|(G): IE(6.0/2.0)
											* POS21!=(A)|(G): IE(43.0/0.0)
									* POS47!=(T): IE(259.0/0.0)
			* POS32!=(G)|(C)|(A)
				* POS31=(T)|(C)|(A)
					* POS29=(T)|(G)|(C): N(43.0/0.0)
					* POS29!=(T)|(G)|(C)
					* POS25=(A)|(G)
							* POS18=(A)|(G)|(C)
									* POS48=(T)|(A)|(C)|(N): N(9.0/0.0)
									* POS48!=(T)|(A)|(C)|(N): IE(4.0/1.0)
							* POS18!=(A)|(G)|(C): IE(7.0/0.0)
					* POS25!=(A)|(G): IE(112.0/2.0)
				* POS31!=(T)|(C)|(A)
					* POS35=(A)|(T)|(C)
							* POS33=(T)|(C)|(G)|(N)
						* POS28=(G)|(A)
							* POS18=(A)|(C)
								* POS11=(G)|(C): EI(7.0/0.0)
								* POS11!=(G)|(C): N(2.0/1.0)
							* POS18!=(A)|(C)
										* POS34=(C)|(G)|(T)|(N): N(11.0/0.0)
										* POS34!=(C)|(G)|(T)|(N): IE(2.0/1.0)
						* POS28!=(G)|(A)
							* POS21=(A)|(G)
							* POS26=(A): EI(9.0/1.0)
							* POS26!=(A)
											* POS34=(T)|(C)|(G)|(N): IE(12.0/0.0)
											* POS34!=(T)|(C)|(G)|(N)
											* POS16=(G)|(A)|(T): IE(2.0/2.0)
											* POS16!=(G)|(A)|(T): EI(4.0/0.0)
							* POS21!=(A)|(G): IE(56.0/5.0)
							* POS33!=(T)|(C)|(G)|(N)
					* POS22=(T)
						* POS10=(C): N(3.0/2.0)
						* POS10!=(C)
							* POS38=(T): IE(3.0/1.0)
							* POS38!=(T): EI(17.0/2.0)
					* POS22!=(T)
						* POS41=(A)
								* POS3=(T)|(G): IE(2.0/1.0)
								* POS3!=(T)|(G): EI(5.0/0.0)
						* POS41!=(A): EI(47.0/0.0)
					* POS35!=(A)|(T)|(C)
					* POS33=(T)|(C)
							* POS18=(A)|(G)|(C): EI(20.0/1.0)
							* POS18!=(A)|(G)|(C)
						* POS8=(T): IE(5.0/0.0)
						* POS8!=(T): EI(3.0/0.0)
					* POS33!=(T)|(C)
					* POS34=(T)
						* POS38=(A): IE(3.0/1.0)
						* POS38!=(A)
							* POS12=(T): EI(3.0/2.0)
							* POS12!=(T): EI(22.0/0.0)
					* POS34!=(T)
						* POS39=(A)
							* POS19=(T)
											* POS47=(A)|(C)|(T)|(N): EI(7.0/0.0)
											* POS47!=(A)|(C)|(T)|(N): IE(5.0/1.0)
							* POS19!=(T)
								* POS46=(A): EI(5.0/2.0)
								* POS46!=(A): EI(51.0/0.0)
						* POS39!=(A)
							* POS34=(C): EI(21.0/1.0)
							* POS34!=(C): EI(327.0/0.0)


