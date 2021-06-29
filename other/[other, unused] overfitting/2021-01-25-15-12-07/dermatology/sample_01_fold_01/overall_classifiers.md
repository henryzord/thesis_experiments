# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Melanin_incontinence <= 0 and Fibrosis <= 0 and Follicular_horn_plug <= 0 and Clubbing > 0 | 1 | 0.300310 |
| Thinning < 0.5 and Vacuolisation >= 0.5 | 3 | 0.196923 |
| Melanin_incontinence <= 0 and Fibrosis <= 0 and Follicular_horn_plug <= 0 and Clubbing <= 0 and Thinning <= 1 and Koebner_phenomenon <= 0 and Granular_layer <= 0 | 2 | 0.153158 |
| Melanin_incontinence <= 0 and Fibrosis > 0 | 5 | 0.141603 |
| Thinning < 0.5 and Vacuolisation < 0.5 and Fibrosis < 0.5 and Koebner_phenomenon >= 0.5 | 4 | 0.104191 |
| Thinning < 0.5 and Vacuolisation < 0.5 and Fibrosis < 0.5 and Koebner_phenomenon < 0.5 and Follicular_papules >= 0.5 | 6 | 0.052470 |
| Melanin_incontinence <= 0 and Fibrosis <= 0 and Follicular_horn_plug <= 0 and Clubbing <= 0 and Thinning <= 1 and Koebner_phenomenon <= 0 and Granular_layer > 0 | 4 | 0.017301 |
| Koebner_phenomenon <= 0.5 and PNL_infiltrate > 0.5 and Fibrosis <= 0.5 and Elongation > 1.5 and Munro_microabcess <= 0.5 and Spongiosis <= 0.5 and Saw-tooth_appearance <= 0.5 and Follicular_horn_plug <= 0.5 | 1 | 0.066116 |
| Koebner_phenomenon <= 0.5 and PNL_infiltrate > 0.5 and Fibrosis <= 0.5 and Elongation <= 0.5 and Munro_microabcess <= 0.5 and Spongiosis > 0.5 and Saw-tooth_appearance <= 0.5 and Follicular_horn_plug > 0.5 | 2 | 0.001838 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Melanin_incontinence <= 0 and Fibrosis <= 0 and Follicular_horn_plug <= 0 and Clubbing > 0 | 1 | 0.300310 |
| Band-like_infiltrate > 1 | 3 | 0.280768 |
| Fibrosis <= 0 and Follicular_horn_plug <= 0 and Koebner_phenomenon <= 0 and Granular_layer <= 0 | 2 | 0.298851 |
| Fibrosis > 0 | 5 | 0.419643 |
| Follicular_papules <= 0 | 4 | 0.625532 |
|  | 6 | 0.782609 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Follicular_horn_plug >= 1 and Follicular_papules >= 1 | 6 | 0.055215 |
| Spongiosis >= 1 and Itching <= 1 and Koebner_phenomenon >= 1 | 4 | 0.095351 |
| Fibrosis >= 1 and Koebner_phenomenon <= 0 | 5 | 0.168459 |
| Spongiosis >= 2 and Melanin_incontinence <= 0 and Granular_layer <= 0 | 2 | 0.196705 |
| Band-like_infiltrate >= 2 | 3 | 0.349810 |
|  | 1 | 0.840336 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

koebner_phenomenon|pnl_infiltrate|fibrosis|elongation|munro_microabcess|spongiosis|saw-tooth_appearance|follicular_horn_plug|class
---|---|---|---|---|---|---|---|---
(-inf-0.5]|(-inf-0.5]|(0.5-inf)|(1.5-inf)|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|(0.5-inf)|1
(0.5-inf)|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|(0.5-inf)|(0.5-inf)|(0.5-inf)|(-inf-0.5]|1
(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(0.5-1.5]|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|(0.5-inf)|1
(0.5-inf)|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|(0.5-inf)|(-inf-0.5]|1
(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|(0.5-inf)|1
(-inf-0.5]|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|(0.5-inf)|2
(-inf-0.5]|(-inf-0.5]|(0.5-inf)|(1.5-inf)|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|5
(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|(0.5-inf)|6
(-inf-0.5]|(0.5-inf)|(-inf-0.5]|(0.5-1.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|1
(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(1.5-inf)|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|2
(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|(0.5-inf)|(-inf-0.5]|3
(0.5-inf)|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|1
(0.5-inf)|(0.5-inf)|(-inf-0.5]|(1.5-inf)|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|1
(-inf-0.5]|(0.5-inf)|(-inf-0.5]|(1.5-inf)|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|1
(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|(0.5-inf)|(-inf-0.5]|3
(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(1.5-inf)|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|1
(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(1.5-inf)|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|1
(-inf-0.5]|(0.5-inf)|(-inf-0.5]|(0.5-1.5]|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|2
(-inf-0.5]|(0.5-inf)|(-inf-0.5]|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|1
(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(0.5-1.5]|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|2
(-inf-0.5]|(-inf-0.5]|(0.5-inf)|(1.5-inf)|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|5
(0.5-inf)|(0.5-inf)|(-inf-0.5]|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|1
(0.5-inf)|(0.5-inf)|(-inf-0.5]|(1.5-inf)|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|1
(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|6
(-inf-0.5]|(0.5-inf)|(-inf-0.5]|(1.5-inf)|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|1
(0.5-inf)|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|4
(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(1.5-inf)|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|1
(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(1.5-inf)|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|1
(-inf-0.5]|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|2
(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|3
(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|3
(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|4
(-inf-0.5]|(-inf-0.5]|(0.5-inf)|(0.5-1.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|5
(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|2
(0.5-inf)|(0.5-inf)|(-inf-0.5]|(0.5-1.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|1
(-inf-0.5]|(0.5-inf)|(-inf-0.5]|(0.5-1.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|1
(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(0.5-1.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|1
(-inf-0.5]|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|5
(-inf-0.5]|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|2
(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|1

## JRip

Decision list:

rules | predicted class
---|---
(Follicular_horn_plug >= 1) and (Follicular_papules >= 1)|6 (18.0/0.0)
(Spongiosis >= 1) and (Itching <= 1) and (Koebner_phenomenon >= 1)|4 (30.0/1.0)
(Fibrosis >= 1) and (Koebner_phenomenon <= 0)|5 (47.0/0.0)
(Spongiosis >= 2) and (Melanin_incontinence <= 0) and (Granular_layer <= 0)|2 (53.0/5.0)
(Band-like_infiltrate >= 2)|3 (65.0/1.0)
|1 (113.0/14.0)


## PART

Decision list:

rules | predicted class
---|---
Melanin_incontinence <= 0 AND Fibrosis <= 0 AND Follicular_horn_plug <= 0 AND Clubbing > 0|1 (97.0)
Band-like_infiltrate > 1|3 (66.0/1.0)
Fibrosis <= 0 AND Follicular_horn_plug <= 0 AND Koebner_phenomenon <= 0 AND Granular_layer <= 0|2 (57.0/6.0)
Fibrosis > 0|5 (47.0)
Follicular_papules <= 0|4 (41.0/2.0)
|6 (18.0)


## J48 Decision Tree

* Melanin_incontinence <= 0
	* Fibrosis <= 0
		* Follicular_horn_plug <= 0
			* Clubbing <= 0
				* Thinning <= 1
					* Koebner_phenomenon <= 0
						* Granular_layer <= 0: 2 (55.0/3.0)
						* Granular_layer > 0: 4 (5.0)
					* Koebner_phenomenon > 0: 4 (36.0/2.0)
				* Thinning > 1: 1 (3.0)
			* Clubbing > 0: 1 (97.0)
		* Follicular_horn_plug > 0: 6 (19.0/1.0)
	* Fibrosis > 0: 5 (48.0/1.0)
* Melanin_incontinence > 0: 3 (63.0)


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


