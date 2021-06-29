# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 1 | 0.306748 |
| Band-like_infiltrate > 1 | 3 | 0.194629 |
| Clubbing < 0.5 and Vacuolisation < 0.5 and Fibrosis < 0.5 and Koebner_phenomenon < 0.5 and Follicular_papules < 1.5 and Granular_layer < 0.5 and Thinning < 1.5 | 2 | 0.153522 |
| Band-like_infiltrate <= 1 and Fibrosis > 0 | 5 | 0.144172 |
| Band-like_infiltrate <= 1 and Fibrosis <= 0 and Perifollicular_parakeratosis <= 0 and Clubbing <= 0 and Thinning <= 0 and Koebner_phenomenon > 0 | 4 | 0.104191 |
| Band-like_infiltrate <= 1 and Fibrosis <= 0 and Perifollicular_parakeratosis > 0 | 6 | 0.052470 |
| Clubbing < 0.5 and Vacuolisation < 0.5 and Fibrosis < 0.5 and Koebner_phenomenon < 0.5 and Follicular_papules < 1.5 and Granular_layer >= 0.5 | 4 | 0.017301 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Melanin_incontinence <= 0 and Fibrosis <= 0 and Follicular_horn_plug <= 0 and Clubbing > 0 | 1 | 0.300310 |
| Band-like_infiltrate > 1 | 3 | 0.280768 |
| Fibrosis <= 0 and Follicular_papules <= 0 and Thinning <= 1 and Koebner_phenomenon <= 0 and Granular_layer <= 0 | 2 | 0.309205 |
| Fibrosis > 0 | 5 | 0.419643 |
| Follicular_horn_plug <= 0 and Elongation <= 1 | 4 | 0.636364 |
| Thinning <= 1 | 6 | 0.771429 |
|  | 1 | 0.600000 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Perifollicular_parakeratosis >= 1 | 6 | 0.052470 |
| Spongiosis >= 1 and Itching <= 1 and Koebner_phenomenon >= 1 | 4 | 0.092268 |
| Fibrosis >= 1 and Koebner_phenomenon <= 0 | 5 | 0.167857 |
| Spongiosis >= 2 and Melanin_incontinence <= 0 and Granular_layer <= 0 | 2 | 0.195818 |
| Band-like_infiltrate >= 2 | 3 | 0.347908 |
|  | 1 | 0.833333 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

itching|koebner_phenomenon|knee_and_elbow|melanin_incontinence|fibrosis|elongation|focal_hypergranulosis|class
---|---|---|---|---|---|---|---
(1.5-inf)|(0.5-inf)|(1.5-inf)|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|1
(1.5-inf)|(0.5-inf)|(-inf-0.5]|(0.5-inf)|(0.5-inf)|(-inf-0.5]|(0.5-inf)|1
(1.5-inf)|(-inf-0.5]|(0.5-1.5]|(-inf-0.5]|(0.5-inf)|(0.5-inf)|(-inf-0.5]|5
(-inf-1.5]|(0.5-inf)|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|3
(1.5-inf)|(0.5-inf)|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|3
(1.5-inf)|(0.5-inf)|(1.5-inf)|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|1
(-inf-1.5]|(0.5-inf)|(1.5-inf)|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|1
(-inf-1.5]|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|3
(1.5-inf)|(-inf-0.5]|(1.5-inf)|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|1
(-inf-1.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|(0.5-inf)|(-inf-0.5]|5
(1.5-inf)|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|(0.5-inf)|(-inf-0.5]|5
(1.5-inf)|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|3
(-inf-1.5]|(-inf-0.5]|(1.5-inf)|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|1
(1.5-inf)|(0.5-inf)|(0.5-1.5]|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|1
(-inf-1.5]|(-inf-0.5]|(0.5-1.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|1
(-inf-1.5]|(0.5-inf)|(0.5-1.5]|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|1
(1.5-inf)|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|1
(1.5-inf)|(-inf-0.5]|(0.5-1.5]|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|1
(-inf-1.5]|(-inf-0.5]|(0.5-1.5]|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|1
(1.5-inf)|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|1
(-inf-1.5]|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|1
(1.5-inf)|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|1
(1.5-inf)|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|2
(-inf-1.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|1
(1.5-inf)|(0.5-inf)|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|1
(1.5-inf)|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|5
(-inf-1.5]|(-inf-0.5]|(1.5-inf)|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|6
(1.5-inf)|(-inf-0.5]|(0.5-1.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|1
(-inf-1.5]|(-inf-0.5]|(0.5-1.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|6
(-inf-1.5]|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|4
(1.5-inf)|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|4
(1.5-inf)|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|2
(-inf-1.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|2

## JRip

Decision list:

rules | predicted class
---|---
(Perifollicular_parakeratosis >= 1)|6 (19.0/1.0)
(Spongiosis >= 1) and (Itching <= 1) and (Koebner_phenomenon >= 1)|4 (29.0/1.0)
(Fibrosis >= 1) and (Koebner_phenomenon <= 0)|5 (47.0/0.0)
(Spongiosis >= 2) and (Melanin_incontinence <= 0) and (Granular_layer <= 0)|2 (52.0/5.0)
(Band-like_infiltrate >= 2)|3 (65.0/1.0)
|1 (114.0/15.0)


## PART

Decision list:

rules | predicted class
---|---
Melanin_incontinence <= 0 AND Fibrosis <= 0 AND Follicular_horn_plug <= 0 AND Clubbing > 0|1 (97.0)
Band-like_infiltrate > 1|3 (66.0/1.0)
Fibrosis <= 0 AND Follicular_papules <= 0 AND Thinning <= 1 AND Koebner_phenomenon <= 0 AND Granular_layer <= 0|2 (54.0/3.0)
Fibrosis > 0|5 (47.0)
Follicular_horn_plug <= 0 AND Elongation <= 1|4 (41.0/2.0)
Thinning <= 1|6 (18.0)
|1 (3.0)


## J48 Decision Tree

* Band-like_infiltrate <= 1
	* Fibrosis <= 0
		* Perifollicular_parakeratosis <= 0
			* Clubbing <= 0
				* Thinning <= 0
					* Koebner_phenomenon <= 0: 2 (50.0/8.0)
					* Koebner_phenomenon > 0: 4 (28.0/1.0)
				* Thinning > 0: 1 (4.0/1.0)
			* Clubbing > 0: 1 (80.0)
		* Perifollicular_parakeratosis > 0: 6 (16.0/1.0)
	* Fibrosis > 0: 5 (40.0)
* Band-like_infiltrate > 1: 3 (54.0)


## SimpleCart Decision Tree

* Clubbing < 0.5
	* Vacuolisation < 0.5
		* Fibrosis < 0.5
			* Koebner_phenomenon < 0.5
				* Follicular_papules < 1.5
					* Granular_layer < 0.5
						* Thinning < 1.5: 2(53.0/4.0)
						* Thinning >= 1.5: 1(3.0/0.0)
					* Granular_layer >= 0.5: 4(5.0/0.0)
				* Follicular_papules >= 1.5: 6(15.0/0.0)
			* Koebner_phenomenon >= 0.5
				* PNL_infiltrate < 0.5: 4(31.0/0.0)
				* PNL_infiltrate >= 0.5: 4(3.0/1.0)
		* Fibrosis >= 0.5: 5(46.0/1.0)
	* Vacuolisation >= 0.5: 3(64.0/0.0)
* Clubbing >= 0.5: 1(97.0/3.0)


