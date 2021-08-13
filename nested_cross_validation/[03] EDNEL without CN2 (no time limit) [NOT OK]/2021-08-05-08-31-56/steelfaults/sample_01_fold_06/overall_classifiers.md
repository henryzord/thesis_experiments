# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 0 | 0.653295 |
| Pastry = 0 and Z_Scratch = 0 and K_Scatch = 0 and Stains = 0 and Dirtiness = 0 and Bumps = 0 | 1 | 0.346705 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Bumps = 0 and K_Scatch = 0 and Z_Scratch = 0 and Pastry = 0 and Stains = 0 and Dirtiness = 0 | 1 | 0.346705 |
|  | 0 | 1.000000 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Bumps = 0 and K_Scatch = 0 and Z_Scratch = 0 and Pastry = 0 and Stains = 0 and Dirtiness = 0 | 1 | 0.346705 |
|  | 0 | 1.000000 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

pastry|z_scratch|k_scatch|stains|dirtiness|bumps|other_faults
---|---|---|---|---|---|---
0|0|0|0|0|1|0
0|0|0|0|1|0|0
0|0|0|1|0|0|0
0|0|1|0|0|0|0
0|1|0|0|0|0|0
0|0|0|0|0|0|1
1|0|0|0|0|0|0

## JRip

Decision list:

rules | predicted class
---|---
(Bumps = 0) and (K_Scatch = 0) and (Z_Scratch = 0) and (Pastry = 0) and (Stains = 0) and (Dirtiness = 0)|1 (605.0/0.0)
|0 (1140.0/0.0)


## PART

Decision list:

rules | predicted class
---|---
Bumps = 0 AND K_Scatch = 0 AND Z_Scratch = 0 AND Pastry = 0 AND Stains = 0 AND Dirtiness = 0|1 (605.0)
|0 (1140.0)


## SimpleCart Decision Tree

* Bumps=(0)
	* K_Scatch=(0)
		* Z_Scratch=(0)
			* Pastry=(0)
				* Stains=(0)
					* Dirtiness=(0): 1(605.0/0.0)
					* Dirtiness!=(0): 0(49.0/0.0)
				* Stains!=(0): 0(65.0/0.0)
			* Pastry!=(0): 0(141.0/0.0)
		* Z_Scratch!=(0): 0(171.0/0.0)
	* K_Scatch!=(0): 0(352.0/0.0)
* Bumps!=(0): 0(362.0/0.0)


