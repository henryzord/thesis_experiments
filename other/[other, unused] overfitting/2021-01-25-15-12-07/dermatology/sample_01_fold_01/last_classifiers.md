# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 1 | 0.306748 |
| Thinning < 0.5 and Vacuolisation >= 0.5 | 3 | 0.196923 |
| Thinning < 0.5 and Vacuolisation < 0.5 and Fibrosis < 0.5 and Koebner_phenomenon < 0.5 and Follicular_papules < 0.5 | 2 | 0.135417 |
| Melanin_incontinence <= 0.0 and Fibrosis > 0.0 | 5 | 0.141603 |
| Thinning < 0.5 and Vacuolisation < 0.5 and Fibrosis < 0.5 and Koebner_phenomenon >= 0.5 | 4 | 0.104191 |
| Melanin_incontinence <= 0.0 and Fibrosis <= 0.0 and Follicular_horn_plug > 0.0 | 6 | 0.052470 |
| Melanin_incontinence <= 0.0 and Fibrosis <= 0.0 and Follicular_horn_plug <= 0.0 and Clubbing <= 0.0 and Thinning <= 1.0 and Koebner_phenomenon <= 0.0 and Granular_layer > 0.0 | 4 | 0.017301 |
| Melanin_incontinence <= 0.0 and Fibrosis <= 0.0 and Follicular_horn_plug <= 0.0 and Clubbing <= 0.0 and Thinning <= 1.0 and Koebner_phenomenon <= 0.0 and Granular_layer <= 0.0 and Hyperkeratosis > 0.0 and Inflammatory_monoluclear > 1.0 | 4 | 0.006993 |
| Koebner_phenomenon > 0.5 and PNL_infiltrate > 0.5 and Fibrosis <= 0.5 and Elongation <= 0.5 and Granular_layer <= 0.5 and Saw-tooth_appearance <= 0.5 and Perifollicular_parakeratosis <= 0.5 and Band-like_infiltrate <= 1.5 | 2 | 0.001230 |
| Melanin_incontinence <= 0.0 and Fibrosis <= 0.0 and Follicular_horn_plug <= 0.0 and Clubbing <= 0.0 and Thinning <= 1.0 and Koebner_phenomenon <= 0.0 and Granular_layer <= 0.0 and Hyperkeratosis > 0.0 and Inflammatory_monoluclear <= 1.0 | 2 | 0.021583 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Melanin_incontinence > 0 | 3 | 0.194444 |
| Fibrosis > 0 and Spongiosis <= 0 | 5 | 0.149606 |
| Perifollicular_parakeratosis <= 0 and Clubbing > 0 and Definite_borders > 1 | 1 | 0.413146 |
| Fibrosis <= 0 and Thinning <= 0 and Follicular_papules <= 0 and Koebner_phenomenon > 0 and Itching <= 0 | 4 | 0.201681 |
| Fibrosis <= 0 and Thinning <= 0 and Follicular_papules <= 0 and Koebner_phenomenon <= 0 and Itching > 1 | 2 | 0.372340 |
| Perifollicular_parakeratosis > 0 | 6 | 0.230769 |
| Fibrosis <= 0 and Thinning <= 0 and Koebner_phenomenon <= 0 and Inflammatory_monoluclear > 1 | 4 | 0.099225 |
| Fibrosis <= 0 and Spongiosis <= 1 | 1 | 0.205714 |
| Fibrosis <= 0 and Koebner_phenomenon <= 0 | 2 | 0.461538 |
| Fibrosis <= 0 | 4 | 0.416667 |
|  | 5 | 0.750000 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

koebner_phenomenon|pnl_infiltrate|fibrosis|elongation|granular_layer|saw-tooth_appearance|perifollicular_parakeratosis|band-like_infiltrate|class
---|---|---|---|---|---|---|---|---
(0.5-inf)|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|(1.5-inf)|(0.5-inf)|(-inf-0.5]|(1.5-inf)|1
(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(1.5-inf)|(0.5-inf)|(-inf-0.5]|(1.5-inf)|3
(0.5-inf)|(0.5-inf)|(-inf-0.5]|(1.5-inf)|(1.5-inf)|(-inf-0.5]|(-inf-0.5]|(-inf-1.5]|1
(-inf-0.5]|(0.5-inf)|(-inf-0.5]|(1.5-inf)|(1.5-inf)|(-inf-0.5]|(-inf-0.5]|(-inf-1.5]|1
(0.5-inf)|(0.5-inf)|(-inf-0.5]|(1.5-inf)|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(1.5-inf)|1
(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(1.5-inf)|(1.5-inf)|(-inf-0.5]|(-inf-0.5]|(-inf-1.5]|1
(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(1.5-inf)|(1.5-inf)|(-inf-0.5]|(-inf-0.5]|(-inf-1.5]|1
(0.5-inf)|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|(1.5-inf)|1
(0.5-inf)|(0.5-inf)|(-inf-0.5]|(0.5-1.5]|(1.5-inf)|(-inf-0.5]|(-inf-0.5]|(-inf-1.5]|1
(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|(1.5-inf)|3
(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|(1.5-inf)|3
(-inf-0.5]|(0.5-inf)|(-inf-0.5]|(1.5-inf)|(0.5-1.5]|(-inf-0.5]|(-inf-0.5]|(-inf-1.5]|1
(0.5-inf)|(0.5-inf)|(-inf-0.5]|(1.5-inf)|(0.5-1.5]|(-inf-0.5]|(-inf-0.5]|(-inf-1.5]|1
(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(0.5-1.5]|(1.5-inf)|(-inf-0.5]|(-inf-0.5]|(-inf-1.5]|1
(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(1.5-inf)|(0.5-1.5]|(-inf-0.5]|(-inf-0.5]|(-inf-1.5]|1
(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(1.5-inf)|(0.5-1.5]|(-inf-0.5]|(-inf-0.5]|(-inf-1.5]|1
(-inf-0.5]|(0.5-inf)|(-inf-0.5]|(0.5-1.5]|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|(-inf-1.5]|1
(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(0.5-1.5]|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|(-inf-1.5]|1
(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(1.5-inf)|(-inf-0.5]|(-inf-0.5]|(-inf-1.5]|1
(-inf-0.5]|(0.5-inf)|(-inf-0.5]|(0.5-1.5]|(0.5-1.5]|(-inf-0.5]|(-inf-0.5]|(-inf-1.5]|1
(-inf-0.5]|(-inf-0.5]|(0.5-inf)|(1.5-inf)|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-1.5]|5
(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(1.5-inf)|1
(-inf-0.5]|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|(-inf-1.5]|6
(-inf-0.5]|(0.5-inf)|(-inf-0.5]|(1.5-inf)|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-1.5]|1
(0.5-inf)|(0.5-inf)|(-inf-0.5]|(1.5-inf)|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-1.5]|1
(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(1.5-inf)|1
(0.5-inf)|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|(-inf-1.5]|1
(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(1.5-inf)|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-1.5]|2
(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(1.5-inf)|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-1.5]|1
(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|(-inf-1.5]|6
(0.5-inf)|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(0.5-1.5]|(-inf-0.5]|(-inf-0.5]|(-inf-1.5]|1
(-inf-0.5]|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(0.5-1.5]|(-inf-0.5]|(-inf-0.5]|(-inf-1.5]|1
(-inf-0.5]|(-inf-0.5]|(0.5-inf)|(0.5-1.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-1.5]|5
(-inf-0.5]|(0.5-inf)|(-inf-0.5]|(0.5-1.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-1.5]|1
(0.5-inf)|(0.5-inf)|(-inf-0.5]|(0.5-1.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-1.5]|1
(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(0.5-1.5]|(-inf-0.5]|(-inf-0.5]|(-inf-1.5]|4
(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(0.5-1.5]|(-inf-0.5]|(-inf-0.5]|(-inf-1.5]|4
(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(0.5-1.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-1.5]|2
(-inf-0.5]|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-1.5]|5
(-inf-0.5]|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-1.5]|2
(0.5-inf)|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-1.5]|2
(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-1.5]|2
(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-1.5]|4

## PART

Decision list:

rules | predicted class
---|---
Melanin_incontinence > 0|3 (63.0)
Fibrosis > 0 AND Spongiosis <= 0|5 (38.0)
Perifollicular_parakeratosis <= 0 AND Clubbing > 0 AND Definite_borders > 1|1 (88.0)
Fibrosis <= 0 AND Thinning <= 0 AND Follicular_papules <= 0 AND Koebner_phenomenon > 0 AND Itching <= 0|4 (24.0)
Fibrosis <= 0 AND Thinning <= 0 AND Follicular_papules <= 0 AND Koebner_phenomenon <= 0 AND Itching > 1|2 (35.0)
Perifollicular_parakeratosis > 0|6 (18.0)
Fibrosis <= 0 AND Thinning <= 0 AND Koebner_phenomenon <= 0 AND Inflammatory_monoluclear > 1|4 (15.0/7.0)
Fibrosis <= 0 AND Spongiosis <= 1|1 (13.0/1.0)
Fibrosis <= 0 AND Koebner_phenomenon <= 0|2 (11.0)
Fibrosis <= 0|4 (11.0/1.0)
|5 (10.0/1.0)


## J48 Decision Tree

* Melanin_incontinence <= 0.0
	* Fibrosis <= 0.0
		* Follicular_horn_plug <= 0.0
			* Clubbing <= 0.0
				* Thinning <= 1.0
					* Koebner_phenomenon <= 0.0
						* Granular_layer <= 0.0
							* Hyperkeratosis <= 0.0: 2 (47.0/1.0)
							* Hyperkeratosis > 0.0
								* Inflammatory_monoluclear <= 1.0: 2 (6.0)
								* Inflammatory_monoluclear > 1.0: 4 (2.0)
						* Granular_layer > 0.0: 4 (5.0)
					* Koebner_phenomenon > 0.0: 4 (36.0/2.0)
				* Thinning > 1.0: 1 (3.0)
			* Clubbing > 0.0: 1 (97.0)
		* Follicular_horn_plug > 0.0: 6 (19.0/1.0)
	* Fibrosis > 0.0: 5 (48.0/1.0)
* Melanin_incontinence > 0.0: 3 (63.0)


## SimpleCart Decision Tree

* Thinning < 0.5
	* Vacuolisation < 0.5
		* Fibrosis < 0.5
			* Koebner_phenomenon < 0.5
				* Follicular_papules < 0.5: 2(52.0/12.0)
				* Follicular_papules >= 0.5: 6(18.0/1.0)
			* Koebner_phenomenon >= 0.5: 4(34.0/1.0)
		* Fibrosis >= 0.5: 5(46.0/1.0)
	* Vacuolisation >= 0.5: 3(64.0/0.0)
* Thinning >= 0.5: 1(96.0/1.0)


