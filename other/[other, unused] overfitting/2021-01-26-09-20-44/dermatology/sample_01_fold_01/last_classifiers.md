# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 1 | 0.306748 |
| Clubbing < 0.5 and Vacuolisation >= 0.5 | 3 | 0.196923 |
| Melanin_incontinence <= 0.0 and Fibrosis <= 0.0 and Follicular_horn_plug <= 0.0 and Clubbing <= 0.0 and Thinning <= 1.0 and Koebner_phenomenon <= 0.0 and Granular_layer <= 0.0 | 2 | 0.153158 |
| Melanin_incontinence <= 0.0 and Fibrosis > 0.0 | 5 | 0.141603 |
| Melanin_incontinence <= 0.0 and Fibrosis <= 0.0 and Follicular_horn_plug <= 0.0 and Clubbing <= 0.0 and Thinning <= 1.0 and Koebner_phenomenon > 0.0 | 4 | 0.101617 |
| Koebner_phenomenon <= 0.5 and Fibrosis <= 0.5 and Thinning <= 0.5 and Vacuolisation <= 0.5 and Perifollicular_parakeratosis > 0.5 | 6 | 0.052470 |
| Melanin_incontinence <= 0.0 and Fibrosis <= 0.0 and Follicular_horn_plug <= 0.0 and Clubbing <= 0.0 and Thinning <= 1.0 and Koebner_phenomenon <= 0.0 and Granular_layer > 0.0 | 4 | 0.017301 |
| Clubbing < 0.5 and Vacuolisation < 0.5 and Fibrosis < 0.5 and Koebner_phenomenon < 0.5 and Follicular_papules < 1.5 | 2 | 0.138068 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Melanin_incontinence <= 0.5 and Fibrosis <= 0.5 and Follicular_horn_plug <= 0.5 and Clubbing > 0.5 | 1 | 0.300310 |
| Band-like_infiltrate > 1.5 | 3 | 0.280768 |
| Fibrosis <= 0.5 and Follicular_horn_plug <= 0.5 and Koebner_phenomenon <= 0.5 and Granular_layer <= 0.5 | 2 | 0.298851 |
| Fibrosis > 0.5 | 5 | 0.419643 |
| Follicular_papules <= 0.5 | 4 | 0.625532 |
|  | 6 | 0.782609 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Koebner_phenomenon >= 1 and Spongiosis >= 1 and Polygonal_papules <= 0 | 4 | 0.098509 |
| Fibrosis >= 1 and Koebner_phenomenon <= 0 | 5 | 0.159864 |
| Spongiosis >= 2 and Saw-tooth_appearance <= 0 | 2 | 0.163706 |
| Band-like_infiltrate >= 2 | 3 | 0.323309 |
|  | 1 | 0.746269 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

koebner_phenomenon|fibrosis|thinning|vacuolisation|perifollicular_parakeratosis|class
---|---|---|---|---|---
(0.5-inf)|(-inf-0.5]|(0.5-inf)|(0.5-inf)|(-inf-0.5]|1
(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|6
(0.5-inf)|(0.5-inf)|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|1
(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|3
(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|3
(-inf-0.5]|(0.5-inf)|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|1
(0.5-inf)|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|1
(-inf-0.5]|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|1
(0.5-inf)|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|1
(-inf-0.5]|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|5
(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|4
(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|2

## JRip

Decision list:

rules | predicted class
---|---
(Koebner_phenomenon >= 1) and (Spongiosis >= 1) and (Polygonal_papules <= 0)|4 (33.0/1.0)
(Fibrosis >= 1) and (Koebner_phenomenon <= 0)|5 (47.0/0.0)
(Spongiosis >= 2) and (Saw-tooth_appearance <= 0)|2 (61.0/14.0)
(Band-like_infiltrate >= 2)|3 (66.0/1.0)
|1 (119.0/20.0)


## PART

Decision list:

rules | predicted class
---|---
Melanin_incontinence <= 0.5 AND Fibrosis <= 0.5 AND Follicular_horn_plug <= 0.5 AND Clubbing > 0.5|1 (97.0)
Band-like_infiltrate > 1.5|3 (66.0/1.0)
Fibrosis <= 0.5 AND Follicular_horn_plug <= 0.5 AND Koebner_phenomenon <= 0.5 AND Granular_layer <= 0.5|2 (57.0/6.0)
Fibrosis > 0.5|5 (47.0)
Follicular_papules <= 0.5|4 (41.0/2.0)
|6 (18.0)


## J48 Decision Tree

* Melanin_incontinence <= 0.0
	* Fibrosis <= 0.0
		* Follicular_horn_plug <= 0.0
			* Clubbing <= 0.0
				* Thinning <= 1.0
					* Koebner_phenomenon <= 0.0
						* Granular_layer <= 0.0: 2 (55.0/3.0)
						* Granular_layer > 0.0: 4 (5.0)
					* Koebner_phenomenon > 0.0: 4 (36.0/2.0)
				* Thinning > 1.0: 1 (3.0)
			* Clubbing > 0.0: 1 (97.0)
		* Follicular_horn_plug > 0.0: 6 (19.0/1.0)
	* Fibrosis > 0.0: 5 (48.0/1.0)
* Melanin_incontinence > 0.0: 3 (63.0)


## SimpleCart Decision Tree

* Clubbing < 0.5
	* Vacuolisation < 0.5
		* Fibrosis < 0.5
			* Koebner_phenomenon < 0.5
				* Follicular_papules < 1.5: 2(53.0/12.0)
				* Follicular_papules >= 1.5: 6(15.0/0.0)
			* Koebner_phenomenon >= 0.5: 4(34.0/1.0)
		* Fibrosis >= 0.5: 5(46.0/1.0)
	* Vacuolisation >= 0.5: 3(64.0/0.0)
* Clubbing >= 0.5: 1(97.0/3.0)


