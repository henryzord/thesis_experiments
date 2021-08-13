# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Educational_level != 1 | 0 | 0.545559 |
| Educational_level = 9 and Sex = 1 and DVRT <= 106.5 | 1 | 0.094340 |
| Educational_level = 0 and DVRT > 116.5 | 1 | 0.090047 |
| Educational_level = 9 and Sex = 1 and DVRT > 106.5 and DVRT <= 116.5 and DVRT <= 114.5 and Prestige_score > 41.5 and Prestige_score <= 50 | 1 | 0.005208 |
| Educational_level = 0 and DVRT <= 116.5 and DVRT > 106.5 and Sex = 1 and Prestige_score > 50 and Prestige_score > 63 | 1 | 0.010309 |
| Educational_level = 0 and DVRT <= 116.5 and DVRT > 106.5 and Sex = 1 and Prestige_score <= 50 | 1 | 0.015385 |
| Educational_level = 9 | 1 | 0.358325 |
| Educational_level = 1 | 1 | 0.025381 |
| Educational_level = 0 and DVRT <= 116.5 and DVRT > 106.5 and Sex = 0 | 1 | 0.015385 |
| Educational_level = 0 and DVRT <= 116.5 and DVRT > 106.5 and Sex = 1 and Prestige_score > 50 and Prestige_score <= 63 | 1 | 0.010309 |
| Educational_level = 0 and DVRT <= 116.5 and DVRT <= 106.5 | 1 | 0.054187 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Educational_level != 9 and Educational_level != 0 | 0 | 0.540205 |
|  | 1 | 0.975000 |


# Text representation of classifiers as-is

## PART

Decision list:

rules | predicted class
---|---
Educational_level != 9 AND Educational_level != 0|0 (195.24/5.0)
|1 (152.76/1.76)


## J48 Decision Tree

* Educational_level = 0
	* DVRT <= 116.5
		* DVRT <= 106.5: 1 (11.0)
		* DVRT > 106.5
			* Sex = 0: 1 (3.0)
			* Sex = 1
				* Prestige_score <= 50: 1 (3.35/0.35)
				* Prestige_score > 50
					* Prestige_score <= 63: 1 (2.0)
					* Prestige_score > 63: 1 (2.12/0.12)
	* DVRT > 116.5: 1 (19.0)
* Educational_level = 1
	* DVRT <= 118.5: 1 (2.06/0.06)
	* DVRT > 118.5: 1 (3.0)
* Educational_level = 2: 0 (22.26)
* Educational_level = 3: 0 (32.37)
* Educational_level = 4: 0 (41.48)
* Educational_level = 5: 0 (53.62)
* Educational_level = 6: 0 (28.33)
* Educational_level = 7: 0 (4.05)
* Educational_level = 8: 0 (8.09)
* Educational_level = 9
	* Sex = 0: 1 (65.0)
	* Sex = 1
		* DVRT <= 106.5: 1 (20.0)
		* DVRT > 106.5
			* DVRT <= 116.5
				* DVRT <= 114.5
					* Prestige_score <= 41.5: 1 (7.48)
					* Prestige_score > 41.5
						* Prestige_score <= 50: 1 (2.83/0.65)
						* Prestige_score > 50: 1 (5.34)
				* DVRT > 114.5: 1 (2.65/0.65)
			* DVRT > 116.5: 1 (9.0)


## SimpleCart Decision Tree

		* Educational_level=(0)|(1)|(9): 1(156.0/1.81)
		* Educational_level!=(0)|(1)|(9): 0(190.18/0.0)


