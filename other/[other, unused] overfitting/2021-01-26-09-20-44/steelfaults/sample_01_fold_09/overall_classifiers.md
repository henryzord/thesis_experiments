# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 0 | 0.653295 |
| Bumps = 0 and K_Scatch = 0 and Z_Scratch = 0 and Pastry = 0 and Stains = 0 and Dirtiness = 0 | 1 | 0.346705 |

## Ordered rules

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

## J48 Decision Tree

* Bumps = 0
	* K_Scatch = 0
		* Z_Scratch = 0
			* Pastry = 0
				* Stains = 0
					* Dirtiness = 0: 1 (404.0)
					* Dirtiness = 1: 0 (33.0)
				* Stains = 1: 0 (37.0)
			* Pastry = 1: 0 (100.0)
		* Z_Scratch = 1: 0 (116.0)
	* K_Scatch = 1: 0 (231.0)
* Bumps = 1: 0 (243.0)


## SimpleCart Decision Tree

* Bumps=(0)
	* K_Scatch=(0)
		* Z_Scratch=(0)
			* Pastry=(0)
				* Stains=(0)
					* Dirtiness=(0): 1(605.0/0.0)
					* Dirtiness!=(0): 0(50.0/0.0)
				* Stains!=(0): 0(65.0/0.0)
			* Pastry!=(0): 0(143.0/0.0)
		* Z_Scratch!=(0): 0(170.0/0.0)
	* K_Scatch!=(0): 0(350.0/0.0)
* Bumps!=(0): 0(362.0/0.0)


